"""
Audit Log API Endpoints
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.audit.services import AuditService
from app.middleware.auth_deps import require_permission, CurrentUser

router = APIRouter(prefix="/audit", tags=["Audit & Security"])


class AuditLogResponse(BaseModel):
    id: str
    tenant_id: Optional[str] = None
    actor_id: Optional[str] = None
    actor_email: Optional[str] = None
    action: str
    entity_name: str
    entity_id: str
    before_state: Optional[Dict[str, Any]] = None
    after_state: Optional[Dict[str, Any]] = None
    ip_address: Optional[str] = None
    request_id: Optional[str] = None
    description: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


@router.get("/logs", response_model=List[AuditLogResponse])
async def get_audit_logs(
    entity_name: Optional[str] = Query(None),
    entity_id: Optional[str] = Query(None),
    actor_id: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("audit.log.view")),
):
    """Retrieve immutable audit trail records for compliance and security."""
    tenant_id = None if current_user.is_superuser else current_user.tenant_id
    return await AuditService.get_logs(
        db=db,
        tenant_id=tenant_id,
        entity_name=entity_name,
        entity_id=entity_id,
        actor_id=actor_id,
        skip=skip,
        limit=limit,
    )
