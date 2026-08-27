"""
Goals & OKR API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.goals.schemas import GoalCreate, GoalResponse, GoalCheckInCreate
from app.modules.goals.services import GoalService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/goals", tags=["Goals & OKRs"])


def format_goal_response(g) -> dict:
    krs = g.__dict__.get("key_results", [])
    return {
        "id": g.id,
        "tenant_id": g.tenant_id,
        "title": g.title,
        "description": g.description,
        "level": g.level,
        "parent_goal_id": g.parent_goal_id,
        "owner_employee_id": g.owner_employee_id,
        "department_id": g.department_id,
        "target_value": g.target_value,
        "current_value": g.current_value,
        "unit": g.unit,
        "weight": g.weight,
        "start_date": g.start_date,
        "deadline": g.deadline,
        "status": g.status,
        "progress_percentage": g.progress_percentage,
        "key_results": [
            {
                "id": kr.id,
                "goal_id": kr.goal_id,
                "title": kr.title,
                "target_value": kr.target_value,
                "current_value": kr.current_value,
                "unit": kr.unit
            } for kr in krs
        ],
        "created_at": g.created_at,
    }


@router.get("", response_model=List[GoalResponse])
async def list_goals(
    owner_id: Optional[str] = Query(None),
    level: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List goals."""
    goals = await GoalService.list_goals(
        db, current_user.tenant_id or "default", owner_id=owner_id, level=level, skip=skip, limit=limit
    )
    return [format_goal_response(g) for g in goals]


@router.post("", response_model=GoalResponse, status_code=status.HTTP_201_CREATED)
async def create_goal(
    data: GoalCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("goal.manage")),
):
    """Create a new goal or OKR."""
    goal = await GoalService.create_goal(
        db, current_user.tenant_id or "default", data, actor_id=current_user.id
    )
    loaded_goal = await GoalService.get_by_id(db, current_user.tenant_id or "default", goal.id)
    return format_goal_response(loaded_goal)


@router.post("/{goal_id}/check-in", response_model=GoalResponse)
async def check_in_goal(
    goal_id: str,
    data: GoalCheckInCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Log an OKR check-in progress update."""
    goal = await GoalService.record_check_in(
        db, current_user.tenant_id or "default", goal_id, current_user.id, data
    )
    loaded_goal = await GoalService.get_by_id(db, current_user.tenant_id or "default", goal.id)
    return format_goal_response(loaded_goal)
