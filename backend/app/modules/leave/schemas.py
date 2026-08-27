"""
Leave Schemas
"""
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class LeaveTypeBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    code: str = Field(..., min_length=1, max_length=50)
    annual_allowance_days: float = 12.0
    is_paid: bool = True
    is_carry_forward: bool = True
    max_carry_forward_days: float = 5.0
    requires_attachment: bool = False
    description: Optional[str] = None


class LeaveTypeCreate(LeaveTypeBase):
    pass


class LeaveTypeResponse(LeaveTypeBase):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LeaveBalanceResponse(BaseModel):
    id: str
    leave_type_id: str
    leave_type_name: Optional[str] = None
    leave_type_code: Optional[str] = None
    year: int
    allocated_days: float
    carried_forward_days: float
    used_days: float
    pending_days: float
    remaining_days: float

    model_config = ConfigDict(from_attributes=True)


class LeaveRequestCreate(BaseModel):
    leave_type_id: str
    start_date: date
    end_date: date
    is_half_day: bool = False
    half_day_session: Optional[str] = None
    reason: str = Field(..., min_length=3, max_length=1000)
    attachment_url: Optional[str] = None


class LeaveApprovalAction(BaseModel):
    status: str  # APPROVED, REJECTED
    comments: Optional[str] = None


class LeaveRequestResponse(BaseModel):
    id: str
    tenant_id: str
    employee_id: str
    employee_name: Optional[str] = None
    leave_type_id: str
    leave_type_name: Optional[str] = None
    start_date: date
    end_date: date
    total_days: float
    is_half_day: bool
    reason: str
    status: str
    approver_id: Optional[str] = None
    approver_comments: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class HolidayCalendarCreate(BaseModel):
    name: str
    holiday_date: date
    year: Optional[int] = None
    is_optional: bool = False
    description: Optional[str] = None


class HolidayCalendarResponse(HolidayCalendarCreate):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
