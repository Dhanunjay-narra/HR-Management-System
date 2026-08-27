"""
Leave Management Service
"""
from datetime import date, datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.leave.models import LeaveType, LeaveBalance, LeaveRequest, HolidayCalendar
from app.modules.leave.schemas import (
    LeaveTypeCreate, LeaveRequestCreate, LeaveApprovalAction, HolidayCalendarCreate
)
from app.core.exceptions import ValidationException, ResourceNotFoundException, DuplicateResourceException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class LeaveService:
    @staticmethod
    async def create_leave_type(db: AsyncSession, tenant_id: str, data: LeaveTypeCreate) -> LeaveType:
        res = await db.execute(
            select(LeaveType).where(
                LeaveType.code == data.code,
                LeaveType.tenant_id == tenant_id,
                LeaveType.is_deleted == False
            )
        )
        if res.scalar_one_or_none():
            raise DuplicateResourceException("LeaveType", "code", data.code)

        lt = LeaveType(tenant_id=tenant_id, **data.model_dump())
        db.add(lt)
        await db.flush()
        return lt

    @staticmethod
    async def list_leave_types(db: AsyncSession, tenant_id: str) -> List[LeaveType]:
        result = await db.execute(
            select(LeaveType).where(LeaveType.tenant_id == tenant_id, LeaveType.is_deleted == False)
        )
        return list(result.scalars().all())

    @staticmethod
    async def get_or_create_balance(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        leave_type_id: str,
        year: int = date.today().year
    ) -> LeaveBalance:
        result = await db.execute(
            select(LeaveBalance)
            .options(selectinload(LeaveBalance.leave_type))
            .where(
                LeaveBalance.employee_id == employee_id,
                LeaveBalance.leave_type_id == leave_type_id,
                LeaveBalance.year == year,
                LeaveBalance.tenant_id == tenant_id,
                LeaveBalance.is_deleted == False
            )
        )
        bal = result.scalar_one_or_none()
        if not bal:
            # Fetch leave type default
            res_lt = await db.execute(select(LeaveType).where(LeaveType.id == leave_type_id))
            lt = res_lt.scalar_one_or_none()
            if not lt:
                raise ResourceNotFoundException("LeaveType", leave_type_id)

            bal = LeaveBalance(
                tenant_id=tenant_id,
                employee_id=employee_id,
                leave_type_id=leave_type_id,
                year=year,
                allocated_days=lt.annual_allowance_days,
                carried_forward_days=0.0,
                used_days=0.0,
                pending_days=0.0,
            )
            db.add(bal)
            await db.flush()
        return bal

    @staticmethod
    async def apply_leave(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        data: LeaveRequestCreate
    ) -> LeaveRequest:
        if data.end_date < data.start_date:
            raise ValidationException("End date cannot be prior to start date")

        # Calculate requested days
        days = 0.5 if data.is_half_day else (data.end_date - data.start_date).days + 1

        # Check balance
        bal = await LeaveService.get_or_create_balance(
            db, tenant_id, employee_id, data.leave_type_id, data.start_date.year
        )
        if bal.remaining_days < days:
            raise ValidationException(f"Insufficient leave balance. Available: {bal.remaining_days}, Requested: {days}")

        req = LeaveRequest(
            tenant_id=tenant_id,
            employee_id=employee_id,
            leave_type_id=data.leave_type_id,
            start_date=data.start_date,
            end_date=data.end_date,
            total_days=float(days),
            is_half_day=data.is_half_day,
            half_day_session=data.half_day_session,
            reason=data.reason,
            attachment_url=data.attachment_url,
            status="PENDING"
        )
        db.add(req)
        bal.pending_days += float(days)
        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="leave.applied",
            tenant_id=tenant_id,
            actor_id=employee_id,
            payload={"request_id": req.id, "employee_id": employee_id, "days": days}
        ))
        return req

    @staticmethod
    async def review_leave(
        db: AsyncSession,
        tenant_id: str,
        request_id: str,
        approver_id: str,
        action: LeaveApprovalAction
    ) -> LeaveRequest:
        result = await db.execute(
            select(LeaveRequest)
            .options(selectinload(LeaveRequest.leave_type))
            .where(
                LeaveRequest.id == request_id,
                LeaveRequest.tenant_id == tenant_id,
                LeaveRequest.is_deleted == False
            )
        )
        req = result.scalar_one_or_none()
        if not req:
            raise ResourceNotFoundException("LeaveRequest", request_id)

        if req.status != "PENDING":
            raise ValidationException(f"Leave request is already {req.status}")

        bal = await LeaveService.get_or_create_balance(
            db, tenant_id, req.employee_id, req.leave_type_id, req.start_date.year
        )

        req.status = action.status
        req.approver_id = approver_id
        req.approver_comments = action.comments

        bal.pending_days = max(0.0, bal.pending_days - req.total_days)
        if action.status == "APPROVED":
            bal.used_days += req.total_days

            # Record timeline event
            db.add(EmployeeTimelineEvent(
                tenant_id=tenant_id,
                employee_id=req.employee_id,
                actor_id=approver_id,
                event_type="LEAVE_APPROVED",
                title=f"Leave Approved ({req.total_days} days)",
                description=f"Leave from {req.start_date} to {req.end_date} approved.",
                metadata_json={"request_id": req.id, "days": req.total_days}
            ))

        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type=f"leave.{action.status.lower()}",
            tenant_id=tenant_id,
            actor_id=approver_id,
            payload={"request_id": req.id, "status": action.status, "employee_id": req.employee_id}
        ))
        return req

    @staticmethod
    async def list_requests(
        db: AsyncSession,
        tenant_id: str,
        employee_id: Optional[str] = None,
        status: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[LeaveRequest]:
        query = (
            select(LeaveRequest)
            .options(selectinload(LeaveRequest.leave_type), selectinload(LeaveRequest.employee))
            .where(LeaveRequest.tenant_id == tenant_id, LeaveRequest.is_deleted == False)
        )
        if employee_id:
            query = query.where(LeaveRequest.employee_id == employee_id)
        if status:
            query = query.where(LeaveRequest.status == status)

        query = query.order_by(desc(LeaveRequest.created_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())
