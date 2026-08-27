"""
Communication Service
"""
from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc, or_
from sqlalchemy.orm import selectinload

from app.modules.communication.models import Announcement
from app.modules.communication.schemas import AnnouncementCreate
from app.events.event_bus import event_bus, DomainEvent


class CommunicationService:
    @staticmethod
    async def create_announcement(
        db: AsyncSession,
        tenant_id: str,
        author_id: str,
        author_name: str,
        data: AnnouncementCreate
    ) -> Announcement:
        announcement = Announcement(
            tenant_id=tenant_id,
            author_user_id=author_id,
            author_name=author_name,
            publish_at=data.publish_at or datetime.now(timezone.utc),
            **data.model_dump(exclude={"publish_at"})
        )
        db.add(announcement)
        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="communication.announcement_published",
            tenant_id=tenant_id,
            actor_id=author_id,
            payload={"announcement_id": announcement.id, "title": announcement.title, "priority": announcement.priority}
        ))
        return announcement

    @staticmethod
    async def list_announcements(
        db: AsyncSession,
        tenant_id: str,
        department_id: Optional[str] = None,
        limit: int = 50
    ) -> List[Announcement]:
        now = datetime.now(timezone.utc)
        query = (
            select(Announcement)
            .options(selectinload(Announcement.target_department), selectinload(Announcement.target_branch))
            .where(
                Announcement.tenant_id == tenant_id,
                Announcement.publish_at <= now,
                or_(Announcement.expires_at == None, Announcement.expires_at > now),
                Announcement.is_deleted == False
            )
        )
        if department_id:
            query = query.where(
                or_(Announcement.target_department_id == None, Announcement.target_department_id == department_id)
            )

        query = query.order_by(desc(Announcement.is_pinned), desc(Announcement.publish_at)).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())
