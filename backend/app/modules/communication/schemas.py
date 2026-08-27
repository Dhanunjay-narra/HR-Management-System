"""
Communication Schemas
"""
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class AnnouncementBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    content: str = Field(..., min_length=5)
    target_department_id: Optional[str] = None
    target_branch_id: Optional[str] = None
    priority: str = "NORMAL"  # NORMAL, URGENT, CRITICAL
    is_pinned: bool = False
    publish_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None


class AnnouncementCreate(AnnouncementBase):
    pass


class AnnouncementResponse(AnnouncementBase):
    id: str
    tenant_id: str
    author_user_id: str
    author_name: Optional[str] = None
    target_department_name: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
