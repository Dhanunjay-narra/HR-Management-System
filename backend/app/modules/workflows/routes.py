"""
Workflow Automation API Endpoints
"""
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.workflows.schemas import WorkflowDefinitionCreate, WorkflowDefinitionResponse
from app.modules.workflows.services import WorkflowService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/workflows", tags=["Workflow Automation"])


@router.get("", response_model=List[WorkflowDefinitionResponse])
async def list_workflows(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("workflow.view")),
):
    """List defined workflow automations."""
    return await WorkflowService.list_workflows(db, current_user.tenant_id or "default")


@router.post("", response_model=WorkflowDefinitionResponse, status_code=status.HTTP_201_CREATED)
async def create_workflow(
    data: WorkflowDefinitionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("workflow.manage")),
):
    """Create a new automation workflow rule."""
    return await WorkflowService.create_workflow(db, current_user.tenant_id or "default", data)
