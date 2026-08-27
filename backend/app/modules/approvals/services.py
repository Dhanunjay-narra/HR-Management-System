"""
Approval Engine Service
"""
from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.approvals.models import ApprovalChain, ApprovalRequest, ApprovalHistory
from app.modules.approvals.schemas import (
    ApprovalChainCreate, ApprovalRequestCreate, ApprovalActionRequest
)
from app.core.exceptions import ResourceNotFoundException, ValidationException
from app.events.event_bus import event_bus, DomainEvent


class ApprovalService:
    @staticmethod
    async def create_chain(db: AsyncSession, tenant_id: str, data: ApprovalChainCreate) -> ApprovalChain:
        chain = ApprovalChain(tenant_id=tenant_id, **data.model_dump())
        db.add(chain)
        await db.flush()
        return chain

    @staticmethod
    async def list_chains(db: AsyncSession, tenant_id: str) -> List[ApprovalChain]:
        result = await db.execute(
            select(ApprovalChain).where(ApprovalChain.tenant_id == tenant_id, ApprovalChain.is_deleted == False)
        )
        return list(result.scalars().all())

    @staticmethod
    async def submit_request(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        data: ApprovalRequestCreate
    ) -> ApprovalRequest:
        total_steps = 1
        if data.chain_id:
            res_c = await db.execute(select(ApprovalChain).where(ApprovalChain.id == data.chain_id))
            chain = res_c.scalar_one_or_none()
            if chain and chain.steps:
                total_steps = len(chain.steps)

        req = ApprovalRequest(
            tenant_id=tenant_id,
            chain_id=data.chain_id,
            requester_employee_id=employee_id,
            entity_type=data.entity_type,
            entity_id=data.entity_id,
            current_step_index=1,
            total_steps=total_steps,
            status="PENDING"
        )
        db.add(req)
        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="approval.requested",
            tenant_id=tenant_id,
            actor_id=employee_id,
            payload={"request_id": req.id, "entity_type": req.entity_type, "entity_id": req.entity_id}
        ))
        return req

    @staticmethod
    async def process_approval_step(
        db: AsyncSession,
        tenant_id: str,
        request_id: str,
        approver_id: str,
        data: ApprovalActionRequest
    ) -> ApprovalRequest:
        res = await db.execute(
            select(ApprovalRequest)
            .options(selectinload(ApprovalRequest.history))
            .where(
                ApprovalRequest.id == request_id,
                ApprovalRequest.tenant_id == tenant_id,
                ApprovalRequest.is_deleted == False
            )
        )
        req = res.scalar_one_or_none()
        if not req:
            raise ResourceNotFoundException("ApprovalRequest", request_id)

        if req.status != "PENDING":
            raise ValidationException(f"Approval request is already {req.status}")

        history = ApprovalHistory(
            tenant_id=tenant_id,
            request_id=req.id,
            step_index=req.current_step_index,
            approver_user_id=approver_id,
            action=data.action,
            comments=data.comments,
            acted_at=datetime.now(timezone.utc)
        )
        db.add(history)

        if data.action == "REJECTED":
            req.status = "REJECTED"
        elif data.action == "APPROVED":
            if req.current_step_index >= req.total_steps:
                req.status = "APPROVED"
            else:
                req.current_step_index += 1

        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type=f"approval.{data.action.lower()}",
            tenant_id=tenant_id,
            actor_id=approver_id,
            payload={"request_id": req.id, "status": req.status}
        ))
        return req
