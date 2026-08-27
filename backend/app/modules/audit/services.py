"""
Audit Logging Service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from app.modules.audit.models import AuditLog
from app.events.event_bus import event_bus, DomainEvent


class AuditService:
    @staticmethod
    async def log_action(
        db: AsyncSession,
        actor_id: Optional[str],
        actor_email: Optional[str],
        action: str,
        entity_name: str,
        entity_id: str,
        tenant_id: Optional[str] = None,
        before_state: Optional[Dict[str, Any]] = None,
        after_state: Optional[Dict[str, Any]] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        request_id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> AuditLog:
        """Create an immutable audit log entry."""
        audit_entry = AuditLog(
            tenant_id=tenant_id,
            actor_id=actor_id,
            actor_email=actor_email,
            action=action,
            entity_name=entity_name,
            entity_id=str(entity_id),
            before_state=before_state,
            after_state=after_state,
            ip_address=ip_address,
            user_agent=user_agent,
            request_id=request_id,
            description=description or f"{action} performed on {entity_name} ({entity_id})",
        )
        db.add(audit_entry)
        await db.flush()
        return audit_entry

    @staticmethod
    async def get_logs(
        db: AsyncSession,
        tenant_id: Optional[str] = None,
        entity_name: Optional[str] = None,
        entity_id: Optional[str] = None,
        actor_id: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[AuditLog]:
        """Query audit log trail with tenant filtering."""
        query = select(AuditLog).where(AuditLog.is_deleted == False)
        if tenant_id:
            query = query.where(AuditLog.tenant_id == tenant_id)
        if entity_name:
            query = query.where(AuditLog.entity_name == entity_name)
        if entity_id:
            query = query.where(AuditLog.entity_id == entity_id)
        if actor_id:
            query = query.where(AuditLog.actor_id == actor_id)

        query = query.order_by(desc(AuditLog.created_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())
