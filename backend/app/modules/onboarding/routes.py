"""
Onboarding API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.onboarding.schemas import (
    OnboardingWorkflowCreate, OnboardingWorkflowResponse, OnboardingTaskResponse,
    MilestoneReviewCreate, MilestoneReviewResponse
)
from app.modules.onboarding.services import OnboardingService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/onboarding", tags=["Onboarding Journey"])


def format_workflow_response(wf) -> dict:
    emp = wf.__dict__.get("employee")
    tasks = wf.__dict__.get("tasks", [])
    completed_count = sum(1 for t in tasks if t.is_completed)
    pct = round((completed_count / len(tasks)) * 100.0, 1) if tasks else 0.0

    return {
        "id": wf.id,
        "tenant_id": wf.tenant_id,
        "employee_id": wf.employee_id,
        "employee_name": emp.full_name if emp else None,
        "template_name": wf.template_name,
        "status": wf.status,
        "start_date": wf.start_date,
        "target_completion_date": wf.target_completion_date,
        "completed_at": wf.completed_at,
        "progress_percentage": pct,
        "tasks": [
            {
                "id": t.id,
                "workflow_id": t.workflow_id,
                "title": t.title,
                "description": t.description,
                "category": t.category,
                "assigned_to_user_id": t.assigned_to_user_id,
                "due_date": t.due_date,
                "is_completed": t.is_completed,
                "completed_at": t.completed_at,
            } for t in tasks
        ]
    }


@router.post("/workflows", response_model=OnboardingWorkflowResponse, status_code=status.HTTP_201_CREATED)
async def create_onboarding_workflow(
    data: OnboardingWorkflowCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("onboarding.template.manage")),
):
    """Start onboarding journey for an employee."""
    wf = await OnboardingService.create_workflow(
        db, current_user.tenant_id or "default", data, actor_id=current_user.id
    )
    loaded_wf = await OnboardingService.get_by_employee(db, current_user.tenant_id or "default", data.employee_id)
    return format_workflow_response(loaded_wf or wf)


@router.get("/employee/{employee_id}", response_model=Optional[OnboardingWorkflowResponse])
async def get_employee_onboarding(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("onboarding.task.view")),
):
    """Retrieve onboarding checklist and status for an employee."""
    wf = await OnboardingService.get_by_employee(db, current_user.tenant_id or "default", employee_id)
    return format_workflow_response(wf) if wf else None


@router.post("/tasks/{task_id}/complete", response_model=OnboardingTaskResponse)
async def complete_onboarding_task(
    task_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("onboarding.task.manage")),
):
    """Mark an onboarding checklist task as completed."""
    task = await OnboardingService.complete_task(
        db, current_user.tenant_id or "default", task_id, actor_id=current_user.id
    )
    return task
