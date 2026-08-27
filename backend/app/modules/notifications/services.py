"""
Notification Service
"""
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, desc

from app.modules.notifications.models import Notification, NotificationTemplate
from app.events.event_bus import event_bus, DomainEvent
from app.core.exceptions import ResourceNotFoundException


class NotificationService:
    @staticmethod
    async def create_notification(
        db: AsyncSession,
        tenant_id: str,
        user_id: str,
        title: str,
        message: str,
        notification_type: str = "info",
        category: str = "general",
        action_url: Optional[str] = None,
        metadata_json: Optional[Dict[str, Any]] = None,
    ) -> Notification:
        notification = Notification(
            tenant_id=tenant_id,
            user_id=user_id,
            title=title,
            message=message,
            notification_type=notification_type,
            category=category,
            action_url=action_url,
            metadata_json=metadata_json or {},
        )
        db.add(notification)
        await db.flush()
        return notification

    @staticmethod
    async def get_user_notifications(
        db: AsyncSession,
        user_id: str,
        unread_only: bool = False,
        skip: int = 0,
        limit: int = 50,
    ) -> List[Notification]:
        query = select(Notification).where(
            Notification.user_id == user_id,
            Notification.is_deleted == False
        )
        if unread_only:
            query = query.where(Notification.is_read == False)
        query = query.order_by(desc(Notification.created_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def mark_as_read(db: AsyncSession, notification_id: str, user_id: str) -> Notification:
        result = await db.execute(
            select(Notification).where(
                Notification.id == notification_id,
                Notification.user_id == user_id,
                Notification.is_deleted == False
            )
        )
        notification = result.scalar_one_or_none()
        if not notification:
            raise ResourceNotFoundException("Notification", notification_id)

        notification.is_read = True
        notification.read_at = datetime.now(timezone.utc)
        await db.flush()
        return notification

    @staticmethod
    async def mark_all_as_read(db: AsyncSession, user_id: str) -> int:
        now = datetime.now(timezone.utc)
        stmt = (
            update(Notification)
            .where(Notification.user_id == user_id, Notification.is_read == False)
            .values(is_read=True, read_at=now)
        )
        result = await db.execute(stmt)
        await db.flush()
        return result.rowcount
