"""
Service Desk Schemas
"""
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class TicketCategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    code: str = Field(..., min_length=1, max_length=50)
    default_priority: str = "MEDIUM"
    sla_response_hours: int = 24
    sla_resolution_hours: int = 72
    description: Optional[str] = None


class TicketCategoryCreate(TicketCategoryBase):
    pass


class TicketCategoryResponse(TicketCategoryBase):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TicketCommentCreate(BaseModel):
    comment_text: str = Field(..., min_length=1)
    is_internal_note: bool = False
    attachment_url: Optional[str] = None


class TicketCommentResponse(BaseModel):
    id: str
    ticket_id: str
    author_user_id: str
    author_name: Optional[str] = None
    comment_text: str
    is_internal_note: bool
    attachment_url: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TicketCreate(BaseModel):
    category_id: Optional[str] = None
    subject: str = Field(..., min_length=3, max_length=255)
    description: str = Field(..., min_length=5)
    priority: str = "MEDIUM"


class TicketStatusUpdate(BaseModel):
    status: str  # OPEN, IN_PROGRESS, WAITING, RESOLVED, CLOSED
    resolution_summary: Optional[str] = None


class TicketResponse(BaseModel):
    id: str
    tenant_id: str
    ticket_number: str
    category_id: Optional[str] = None
    category_name: Optional[str] = None
    employee_id: str
    employee_name: Optional[str] = None
    assigned_agent_id: Optional[str] = None
    subject: str
    description: str
    priority: str
    status: str
    due_date: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    resolution_summary: Optional[str] = None
    comments: List[TicketCommentResponse] = []
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
