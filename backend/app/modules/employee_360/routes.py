"""
Employee 360 API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.employee_360.schemas import Employee360OverviewResponse, TimelineEventResponse
from app.modules.employee_360.services import Employee360Service
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/employees", tags=["Employee 360 CRM"])


@router.get("/{employee_id}/360", response_model=Employee360OverviewResponse)
async def get_employee_360_profile(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("employee_360.view")),
):
    """Retrieve full unified Employee 360 CRM relationship overview."""
    return await Employee360Service.get_employee_360(
        db,
        tenant_id=current_user.tenant_id or "default",
        employee_id=employee_id
    )


@router.get("/{employee_id}/timeline", response_model=List[TimelineEventResponse])
async def get_employee_timeline(
    employee_id: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("employee.timeline.view")),
):
    """Retrieve complete chronological life-cycle event timeline for an employee."""
    events = await Employee360Service.get_timeline(
        db,
        tenant_id=current_user.tenant_id or "default",
        employee_id=employee_id,
        skip=skip,
        limit=limit
    )
    return [
        TimelineEventResponse(
            id=e.id,
            event_type=e.event_type,
            title=e.title,
            description=e.description,
            actor_name=e.actor_name,
            entity_type=e.entity_type,
            entity_id=e.entity_id,
            metadata_json=e.metadata_json or {},
            event_timestamp=e.event_timestamp
        ) for e in events
    ]
