"""
Notification API Endpoints
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.notifications.services import NotificationService
from app.middleware.auth_deps import get_current_user, CurrentUser

router = APIRouter(prefix="/notifications", tags=["Notifications"])


class NotificationResponse(BaseModel):
    id: str
    tenant_id: str
    user_id: str
    title: str
    message: str
    notification_type: str
    category: str
    action_url: Optional[str] = None
    is_read: bool
    read_at: Optional[datetime] = None
    metadata_json: Dict[str, Any]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


@router.get("", response_model=List[NotificationResponse])
async def list_user_notifications(
    unread_only: bool = Query(False),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Retrieve in-app notifications for the logged-in user."""
    return await NotificationService.get_user_notifications(
        db, current_user.id, unread_only=unread_only, skip=skip, limit=limit
    )


@router.post("/{notification_id}/read", response_model=NotificationResponse)
async def mark_notification_read(
    notification_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Mark a notification as read."""
    return await NotificationService.mark_as_read(db, notification_id, current_user.id)


@router.post("/read-all")
async def mark_all_notifications_read(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Mark all notifications as read for the logged-in user."""
    count = await NotificationService.mark_all_as_read(db, current_user.id)
    return {"success": True, "count": count}
