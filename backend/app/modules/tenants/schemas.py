"""
Tenant Pydantic Schemas
"""
from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class TenantBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    slug: str = Field(..., min_length=2, max_length=100)
    domain: Optional[str] = None
    subscription_plan: str = "enterprise"
    max_employees: int = 500
    logo_url: Optional[str] = None
    primary_color: Optional[str] = "#4F46E5"
    timezone: str = "UTC"
    currency: str = "USD"
    settings: Dict[str, Any] = Field(default_factory=dict)


class TenantCreate(TenantBase):
    pass


class TenantUpdate(BaseModel):
    name: Optional[str] = None
    domain: Optional[str] = None
    subscription_plan: Optional[str] = None
    max_employees: Optional[int] = None
    logo_url: Optional[str] = None
    primary_color: Optional[str] = None
    timezone: Optional[str] = None
    currency: Optional[str] = None
    settings: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None


class TenantResponse(TenantBase):
    id: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
