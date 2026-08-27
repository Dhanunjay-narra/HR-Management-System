"""
Approval Engine API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.approvals.schemas import (
    ApprovalChainCreate, ApprovalChainResponse, ApprovalRequestCreate,
    ApprovalRequestResponse, ApprovalActionRequest
)
from app.modules.approvals.services import ApprovalService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/approvals", tags=["Approval Engine"])


def format_request_response(r) -> dict:
    history = r.__dict__.get("history", [])
    return {
        "id": r.id,
        "tenant_id": r.tenant_id,
        "chain_id": r.chain_id,
        "requester_employee_id": r.requester_employee_id,
        "entity_type": r.entity_type,
        "entity_id": r.entity_id,
        "current_step_index": r.current_step_index,
        "total_steps": r.total_steps,
        "status": r.status,
        "history": [
            {
                "id": h.id,
                "step_index": h.step_index,
                "approver_user_id": h.approver_user_id,
                "action": h.action,
                "comments": h.comments,
                "acted_at": h.acted_at,
            } for h in history
        ],
        "created_at": r.created_at,
    }


@router.get("/chains", response_model=List[ApprovalChainResponse])
async def list_approval_chains(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List configured approval chains."""
    return await ApprovalService.list_chains(db, current_user.tenant_id or "default")


@router.post("/chains", response_model=ApprovalChainResponse, status_code=status.HTTP_201_CREATED)
async def create_approval_chain(
    data: ApprovalChainCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("approval.chain.manage")),
):
    """Define a multi-step approval workflow chain."""
    return await ApprovalService.create_chain(db, current_user.tenant_id or "default", data)


@router.post("/requests", response_model=ApprovalRequestResponse, status_code=status.HTTP_201_CREATED)
async def submit_approval_request(
    data: ApprovalRequestCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("approval.request.create")),
):
    """Initiate an approval flow."""
    req = await ApprovalService.submit_request(db, current_user.tenant_id or "default", current_user.id, data)
    return format_request_response(req)


@router.post("/requests/{request_id}/action", response_model=ApprovalRequestResponse)
async def process_approval_action(
    request_id: str,
    data: ApprovalActionRequest,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("approval.request.approve")),
):
    """Approve or reject at the current approval stage."""
    req = await ApprovalService.process_approval_step(
        db, current_user.tenant_id or "default", request_id, current_user.id, data
    )
    return format_request_response(req)
