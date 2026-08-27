"""
Attendance Schemas
"""
from typing import Optional, List
from datetime import date, datetime, time
from pydantic import BaseModel, ConfigDict, Field


class ShiftScheduleBase(BaseModel):
    name: str
    code: str
    start_time: time
    end_time: time
    grace_period_minutes: int = 15
    half_day_hours: float = 4.0
    full_day_hours: float = 8.0
    is_overnight: bool = False


class ShiftScheduleCreate(ShiftScheduleBase):
    pass


class ShiftScheduleResponse(ShiftScheduleBase):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ClockInRequest(BaseModel):
    notes: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class ClockOutRequest(BaseModel):
    notes: Optional[str] = None


class AttendanceRecordResponse(BaseModel):
    id: str
    tenant_id: str
    employee_id: str
    work_date: date
    clock_in_time: Optional[datetime] = None
    clock_out_time: Optional[datetime] = None
    total_hours: float = 0.0
    overtime_hours: float = 0.0
    status: str
    is_regularized: bool
    notes: Optional[str] = None
    employee_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class RegularizationRequestCreate(BaseModel):
    attendance_record_id: Optional[str] = None
    work_date: date
    requested_clock_in: datetime
    requested_clock_out: datetime
    reason: str


class RegularizationReviewRequest(BaseModel):
    status: str  # APPROVED, REJECTED
    approver_notes: Optional[str] = None
