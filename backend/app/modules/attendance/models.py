"""
Attendance & Shift Scheduling Models
"""
from datetime import date, datetime, time
from sqlalchemy import Column, String, Date, DateTime, Time, Float, Boolean, ForeignKey, Integer, JSON
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class ShiftSchedule(TenantBaseModel):
    """Configurable Work Shifts."""
    __tablename__ = "shift_schedules"

    name = Column(String(100), nullable=False)  # General Shift, Morning, Night, Rotational
    code = Column(String(50), nullable=False)
    start_time = Column(Time, nullable=False, default=time(9, 0))
    end_time = Column(Time, nullable=False, default=time(18, 0))
    grace_period_minutes = Column(Integer, default=15, nullable=False)
    half_day_hours = Column(Float, default=4.0, nullable=False)
    full_day_hours = Column(Float, default=8.0, nullable=False)
    is_overnight = Column(Boolean, default=False, nullable=False)


class AttendanceRecord(TenantBaseModel):
    """Daily Employee Attendance & Clock Log."""
    __tablename__ = "attendance_records"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    work_date = Column(Date, nullable=False, index=True)
    
    clock_in_time = Column(DateTime(timezone=True), nullable=True)
    clock_out_time = Column(DateTime(timezone=True), nullable=True)
    total_hours = Column(Float, default=0.0, nullable=False)
    overtime_hours = Column(Float, default=0.0, nullable=False)
    
    status = Column(String(50), default="PRESENT", nullable=False, index=True)  # PRESENT, ABSENT, HALF_DAY, LATE, ON_LEAVE, HOLIDAY
    
    clock_in_ip = Column(String(50), nullable=True)
    clock_in_lat = Column(Float, nullable=True)
    clock_in_lng = Column(Float, nullable=True)
    clock_out_ip = Column(String(50), nullable=True)
    
    is_regularized = Column(Boolean, default=False, nullable=False)
    notes = Column(String(500), nullable=True)

    # Relationships
    employee = relationship("Employee")


class AttendanceCorrectionRequest(TenantBaseModel):
    """Regularization request submitted by employee for missed or incorrect punch."""
    __tablename__ = "attendance_corrections"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    attendance_record_id = Column(String(36), ForeignKey("attendance_records.id", ondelete="CASCADE"), nullable=True, index=True)
    work_date = Column(Date, nullable=False)
    
    requested_clock_in = Column(DateTime(timezone=True), nullable=False)
    requested_clock_out = Column(DateTime(timezone=True), nullable=False)
    reason = Column(String(500), nullable=False)
    
    status = Column(String(50), default="PENDING", nullable=False, index=True)  # PENDING, APPROVED, REJECTED
    approver_id = Column(String(36), nullable=True)
    approver_notes = Column(String(500), nullable=True)
