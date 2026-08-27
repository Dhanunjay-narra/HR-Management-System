"""
Service Desk Service
"""
import uuid
from datetime import datetime, timezone, timedelta
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.service_desk.models import TicketCategory, HRTicket, TicketComment
from app.modules.service_desk.schemas import (
    TicketCategoryCreate, TicketCreate, TicketCommentCreate, TicketStatusUpdate
)
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class ServiceDeskService:
    @staticmethod
    async def create_category(db: AsyncSession, tenant_id: str, data: TicketCategoryCreate) -> TicketCategory:
        res = await db.execute(
            select(TicketCategory).where(
                TicketCategory.code == data.code,
                TicketCategory.tenant_id == tenant_id,
                TicketCategory.is_deleted == False
            )
        )
        if res.scalar_one_or_none():
            raise DuplicateResourceException("TicketCategory", "code", data.code)

        cat = TicketCategory(tenant_id=tenant_id, **data.model_dump())
        db.add(cat)
        await db.flush()
        return cat

    @staticmethod
    async def list_categories(db: AsyncSession, tenant_id: str) -> List[TicketCategory]:
        result = await db.execute(
            select(TicketCategory).where(TicketCategory.tenant_id == tenant_id, TicketCategory.is_deleted == False)
        )
        return list(result.scalars().all())

    @staticmethod
    async def create_ticket(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        data: TicketCreate
    ) -> HRTicket:
        tkt_num = f"TKT-{datetime.now(timezone.utc).strftime('%Y%m')}-{uuid.uuid4().hex[:4].upper()}"
        now = datetime.now(timezone.utc)
        due = now + timedelta(hours=72)

        if data.category_id:
            res_cat = await db.execute(select(TicketCategory).where(TicketCategory.id == data.category_id))
            cat = res_cat.scalar_one_or_none()
            if cat:
                due = now + timedelta(hours=cat.sla_resolution_hours)

        ticket = HRTicket(
            tenant_id=tenant_id,
            ticket_number=tkt_num,
            employee_id=employee_id,
            category_id=data.category_id,
            subject=data.subject,
            description=data.description,
            priority=data.priority,
            status="OPEN",
            due_date=due
        )
        db.add(ticket)
        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="ticket.created",
            tenant_id=tenant_id,
            actor_id=employee_id,
            payload={"ticket_id": ticket.id, "ticket_number": tkt_num, "subject": ticket.subject}
        ))
        return ticket

    @staticmethod
    async def get_ticket(db: AsyncSession, tenant_id: str, ticket_id: str) -> HRTicket:
        result = await db.execute(
            select(HRTicket)
            .options(
                selectinload(HRTicket.category),
                selectinload(HRTicket.employee),
                selectinload(HRTicket.comments)
            )
            .where(HRTicket.id == ticket_id, HRTicket.tenant_id == tenant_id, HRTicket.is_deleted == False)
        )
        ticket = result.scalar_one_or_none()
        if not ticket:
            raise ResourceNotFoundException("HRTicket", ticket_id)
        return ticket

    @staticmethod
    async def list_tickets(
        db: AsyncSession,
        tenant_id: str,
        employee_id: Optional[str] = None,
        status: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[HRTicket]:
        query = (
            select(HRTicket)
            .options(selectinload(HRTicket.category), selectinload(HRTicket.employee))
            .where(HRTicket.tenant_id == tenant_id, HRTicket.is_deleted == False)
        )
        if employee_id:
            query = query.where(HRTicket.employee_id == employee_id)
        if status:
            query = query.where(HRTicket.status == status)

        query = query.order_by(desc(HRTicket.created_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def add_comment(
        db: AsyncSession,
        tenant_id: str,
        ticket_id: str,
        user_id: str,
        user_name: str,
        data: TicketCommentCreate
    ) -> TicketComment:
        ticket = await ServiceDeskService.get_ticket(db, tenant_id, ticket_id)
        comment = TicketComment(
            tenant_id=tenant_id,
            ticket_id=ticket.id,
            author_user_id=user_id,
            author_name=user_name,
            **data.model_dump()
        )
        db.add(comment)
        await db.flush()
        return comment

    @staticmethod
    async def update_status(
        db: AsyncSession,
        tenant_id: str,
        ticket_id: str,
        actor_id: str,
        data: TicketStatusUpdate
    ) -> HRTicket:
        ticket = await ServiceDeskService.get_ticket(db, tenant_id, ticket_id)
        ticket.status = data.status
        if data.status in ("RESOLVED", "CLOSED"):
            ticket.resolved_at = datetime.now(timezone.utc)
            if data.resolution_summary:
                ticket.resolution_summary = data.resolution_summary

            # Record timeline event
            db.add(EmployeeTimelineEvent(
                tenant_id=tenant_id,
                employee_id=ticket.employee_id,
                actor_id=actor_id,
                event_type="TICKET_RESOLVED",
                title=f"HR Service Request Resolved: {ticket.ticket_number}",
                description=f"Ticket '{ticket.subject}' resolved.",
                entity_type="HRTicket",
                entity_id=ticket.id
            ))

        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type=f"ticket.{data.status.lower()}",
            tenant_id=tenant_id,
            actor_id=actor_id,
            payload={"ticket_id": ticket.id, "status": data.status}
        ))
        return ticket
