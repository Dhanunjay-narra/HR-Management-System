"""
Leave API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.leave.schemas import (
    LeaveTypeCreate, LeaveTypeResponse, LeaveRequestCreate, LeaveRequestResponse,
    LeaveApprovalAction, LeaveBalanceResponse
)
from app.modules.leave.services import LeaveService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/leave", tags=["Leave Management"])


def format_leave_request(req) -> dict:
    emp = req.__dict__.get("employee")
    lt = req.__dict__.get("leave_type")
    return {
        "id": req.id,
        "tenant_id": req.tenant_id,
        "employee_id": req.employee_id,
        "employee_name": emp.full_name if emp else None,
        "leave_type_id": req.leave_type_id,
        "leave_type_name": lt.name if lt else None,
        "start_date": req.start_date,
        "end_date": req.end_date,
        "total_days": req.total_days,
        "is_half_day": req.is_half_day,
        "reason": req.reason,
        "status": req.status,
        "approver_id": req.approver_id,
        "approver_comments": req.approver_comments,
        "created_at": req.created_at,
    }


@router.get("/types", response_model=List[LeaveTypeResponse])
async def list_leave_types(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List available leave types."""
    return await LeaveService.list_leave_types(db, current_user.tenant_id or "default")


@router.post("/types", response_model=LeaveTypeResponse, status_code=status.HTTP_201_CREATED)
async def create_leave_type(
    data: LeaveTypeCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("leave.manage_policies")),
):
    """Create a new leave policy type."""
    return await LeaveService.create_leave_type(db, current_user.tenant_id or "default", data)


@router.post("/apply", response_model=LeaveRequestResponse, status_code=status.HTTP_201_CREATED)
async def apply_leave(
    data: LeaveRequestCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("leave.apply")),
):
    """Submit a leave application."""
    req = await LeaveService.apply_leave(db, current_user.tenant_id or "default", current_user.id, data)
    return format_leave_request(req)


@router.get("/requests", response_model=List[LeaveRequestResponse])
async def list_leave_requests(
    status: Optional[str] = Query(None),
    all_employees: bool = Query(False),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List leave requests (filtered to self unless manager/admin)."""
    emp_id = None if (all_employees and (current_user.is_superuser or "leave.approve" in current_user.permissions)) else current_user.id
    requests = await LeaveService.list_requests(
        db, current_user.tenant_id or "default", employee_id=emp_id, status=status, skip=skip, limit=limit
    )
    return [format_leave_request(r) for r in requests]


@router.post("/requests/{request_id}/review", response_model=LeaveRequestResponse)
async def review_leave_request(
    request_id: str,
    action: LeaveApprovalAction,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("leave.approve")),
):
    """Approve or reject a pending leave application."""
    req = await LeaveService.review_leave(
        db, current_user.tenant_id or "default", request_id, current_user.id, action
    )
    return format_leave_request(req)
