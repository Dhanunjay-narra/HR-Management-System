"""
Asset Schemas
"""
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class AssetBase(BaseModel):
    asset_tag: str = Field(..., min_length=2, max_length=50)
    name: str = Field(..., min_length=2, max_length=255)
    category: str = "LAPTOP"  # LAPTOP, DESKTOP, MONITOR, PHONE, ACCESS_CARD, LICENSE
    serial_number: Optional[str] = None
    model_number: Optional[str] = None
    purchase_date: Optional[date] = None
    purchase_cost: float = 0.0
    status: str = "IN_INVENTORY"


class AssetCreate(AssetBase):
    pass


class AssetAssignRequest(BaseModel):
    employee_id: str
    condition: str = "EXCELLENT"
    notes: Optional[str] = None


class AssetResponse(AssetBase):
    id: str
    tenant_id: str
    current_employee_id: Optional[str] = None
    current_employee_name: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
