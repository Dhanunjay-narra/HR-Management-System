"""
Expense API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.expenses.schemas import (
    ExpenseCategoryCreate, ExpenseCategoryResponse, ExpenseClaimCreate, ExpenseClaimResponse
)
from app.modules.expenses.services import ExpenseService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/expenses", tags=["Expense Management"])


def format_claim_response(c) -> dict:
    cat = c.__dict__.get("category")
    emp = c.__dict__.get("employee")
    return {
        "id": c.id,
        "tenant_id": c.tenant_id,
        "claim_number": c.claim_number,
        "employee_id": c.employee_id,
        "employee_name": emp.full_name if emp else None,
        "category_id": c.category_id,
        "category_name": cat.name if cat else None,
        "expense_date": c.expense_date,
        "amount": c.amount,
        "currency": c.currency,
        "merchant_name": c.merchant_name,
        "description": c.description,
        "receipt_url": c.receipt_url,
        "status": c.status,
        "approver_id": c.approver_id,
        "rejection_reason": c.rejection_reason,
        "reimbursed_at": c.reimbursed_at,
        "created_at": c.created_at,
    }


@router.get("/categories", response_model=List[ExpenseCategoryResponse])
async def list_categories(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List expense categories."""
    return await ExpenseService.list_categories(db, current_user.tenant_id or "default")


@router.post("/categories", response_model=ExpenseCategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    data: ExpenseCategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("expense.manage")),
):
    """Create a new expense category."""
    return await ExpenseService.create_category(db, current_user.tenant_id or "default", data)


@router.post("/claims", response_model=ExpenseClaimResponse, status_code=status.HTTP_201_CREATED)
async def submit_claim(
    data: ExpenseClaimCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("expense.claim.create")),
):
    """Submit an expense reimbursement claim."""
    claim = await ExpenseService.submit_claim(
        db, current_user.tenant_id or "default", current_user.id, data
    )
    return format_claim_response(claim)


@router.get("/claims", response_model=List[ExpenseClaimResponse])
async def list_claims(
    status: Optional[str] = Query(None),
    all_claims: bool = Query(False),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List expense claims."""
    emp_id = None if (all_claims and (current_user.is_superuser or "expense.claim.approve" in current_user.permissions)) else current_user.id
    claims = await ExpenseService.list_claims(
        db, current_user.tenant_id or "default", employee_id=emp_id, status=status, skip=skip, limit=limit
    )
    return [format_claim_response(c) for c in claims]


@router.put("/claims/{claim_id}/review", response_model=ExpenseClaimResponse)
async def review_claim(
    claim_id: str,
    action_status: str = Query(..., pattern="^(APPROVED|REJECTED|REIMBURSED)$"),
    reason: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("expense.claim.approve")),
):
    """Approve, reject, or mark expense claim as reimbursed."""
    claim = await ExpenseService.review_claim(
        db, current_user.tenant_id or "default", claim_id, current_user.id, action_status, reason
    )
    return format_claim_response(claim)
