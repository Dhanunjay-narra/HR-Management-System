"""
Communication API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.communication.schemas import AnnouncementCreate, AnnouncementResponse
from app.modules.communication.services import CommunicationService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/communication", tags=["Internal Communication"])


def format_announcement_response(a) -> dict:
    dept = a.__dict__.get("target_department")
    return {
        "id": a.id,
        "tenant_id": a.tenant_id,
        "title": a.title,
        "content": a.content,
        "target_department_id": a.target_department_id,
        "target_department_name": dept.name if dept else None,
        "target_branch_id": a.target_branch_id,
        "priority": a.priority,
        "is_pinned": a.is_pinned,
        "publish_at": a.publish_at,
        "expires_at": a.expires_at,
        "author_user_id": a.author_user_id,
        "author_name": a.author_name,
        "created_at": a.created_at,
    }


@router.get("/announcements", response_model=List[AnnouncementResponse])
async def list_announcements(
    department_id: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List published announcements."""
    items = await CommunicationService.list_announcements(
        db, current_user.tenant_id or "default", department_id=department_id, limit=limit
    )
    return [format_announcement_response(a) for a in items]


@router.post("/announcements", response_model=AnnouncementResponse, status_code=status.HTTP_201_CREATED)
async def create_announcement(
    data: AnnouncementCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("communication.announcement.manage")),
):
    """Publish a new company broadcast announcement."""
    a = await CommunicationService.create_announcement(
        db, current_user.tenant_id or "default", current_user.id, current_user.email, data
    )
    return format_announcement_response(a)
