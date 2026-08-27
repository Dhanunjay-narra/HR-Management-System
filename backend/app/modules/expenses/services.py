"""
Expense Management Service
"""
import uuid
from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.expenses.models import ExpenseCategory, ExpenseClaim
from app.modules.expenses.schemas import ExpenseCategoryCreate, ExpenseClaimCreate
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class ExpenseService:
    @staticmethod
    async def create_category(db: AsyncSession, tenant_id: str, data: ExpenseCategoryCreate) -> ExpenseCategory:
        res = await db.execute(
            select(ExpenseCategory).where(
                ExpenseCategory.code == data.code,
                ExpenseCategory.tenant_id == tenant_id,
                ExpenseCategory.is_deleted == False
            )
        )
        if res.scalar_one_or_none():
            raise DuplicateResourceException("ExpenseCategory", "code", data.code)

        cat = ExpenseCategory(tenant_id=tenant_id, **data.model_dump())
        db.add(cat)
        await db.flush()
        return cat

    @staticmethod
    async def list_categories(db: AsyncSession, tenant_id: str) -> List[ExpenseCategory]:
        result = await db.execute(
            select(ExpenseCategory).where(ExpenseCategory.tenant_id == tenant_id, ExpenseCategory.is_deleted == False)
        )
        return list(result.scalars().all())

    @staticmethod
    async def submit_claim(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        data: ExpenseClaimCreate
    ) -> ExpenseClaim:
        claim_num = f"EXP-{datetime.now(timezone.utc).strftime('%Y%m')}-{uuid.uuid4().hex[:4].upper()}"
        claim = ExpenseClaim(
            tenant_id=tenant_id,
            claim_number=claim_num,
            employee_id=employee_id,
            status="SUBMITTED",
            **data.model_dump()
        )
        db.add(claim)
        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="expense.submitted",
            tenant_id=tenant_id,
            actor_id=employee_id,
            payload={"claim_id": claim.id, "claim_number": claim_num, "amount": claim.amount}
        ))
        return claim

    @staticmethod
    async def review_claim(
        db: AsyncSession,
        tenant_id: str,
        claim_id: str,
        approver_id: str,
        status: str,
        reason: Optional[str] = None
    ) -> ExpenseClaim:
        res = await db.execute(
            select(ExpenseClaim)
            .options(selectinload(ExpenseClaim.category), selectinload(ExpenseClaim.employee))
            .where(ExpenseClaim.id == claim_id, ExpenseClaim.tenant_id == tenant_id, ExpenseClaim.is_deleted == False)
        )
        claim = res.scalar_one_or_none()
        if not claim:
            raise ResourceNotFoundException("ExpenseClaim", claim_id)

        claim.status = status
        claim.approver_id = approver_id
        if status == "REJECTED":
            claim.rejection_reason = reason
        elif status == "REIMBURSED":
            claim.reimbursed_at = datetime.now(timezone.utc)

            # Record timeline event
            db.add(EmployeeTimelineEvent(
                tenant_id=tenant_id,
                employee_id=claim.employee_id,
                actor_id=approver_id,
                event_type="EXPENSE_REIMBURSED",
                title=f"Expense Reimbursed: ${claim.amount:,.2f}",
                description=f"Claim {claim.claim_number} for {claim.merchant_name} paid.",
                entity_type="ExpenseClaim",
                entity_id=claim.id
            ))

        await db.flush()
        return claim

    @staticmethod
    async def list_claims(
        db: AsyncSession,
        tenant_id: str,
        employee_id: Optional[str] = None,
        status: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[ExpenseClaim]:
        query = (
            select(ExpenseClaim)
            .options(selectinload(ExpenseClaim.category), selectinload(ExpenseClaim.employee))
            .where(ExpenseClaim.tenant_id == tenant_id, ExpenseClaim.is_deleted == False)
        )
        if employee_id:
            query = query.where(ExpenseClaim.employee_id == employee_id)
        if status:
            query = query.where(ExpenseClaim.status == status)

        query = query.order_by(desc(ExpenseClaim.created_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())
