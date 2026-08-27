"""
Leave Management & Holiday Calendar Models
"""
from datetime import date
from sqlalchemy import Column, String, Date, Float, Boolean, ForeignKey, Integer, JSON
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class LeaveType(TenantBaseModel):
    """Configurable Leave Types (e.g., Casual, Sick, Annual, Maternity)."""
    __tablename__ = "leave_types"

    name = Column(String(100), nullable=False)
    code = Column(String(50), nullable=False, unique=True, index=True)
    annual_allowance_days = Column(Float, default=12.0, nullable=False)
    is_paid = Column(Boolean, default=True, nullable=False)
    is_carry_forward = Column(Boolean, default=True, nullable=False)
    max_carry_forward_days = Column(Float, default=5.0, nullable=False)
    requires_attachment = Column(Boolean, default=False, nullable=False)
    description = Column(String(500), nullable=True)


class LeaveBalance(TenantBaseModel):
    """Employee Leave Ledger per year and leave type."""
    __tablename__ = "leave_balances"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    leave_type_id = Column(String(36), ForeignKey("leave_types.id", ondelete="CASCADE"), nullable=False, index=True)
    year = Column(Integer, default=date.today().year, nullable=False, index=True)
    
    allocated_days = Column(Float, default=0.0, nullable=False)
    carried_forward_days = Column(Float, default=0.0, nullable=False)
    used_days = Column(Float, default=0.0, nullable=False)
    pending_days = Column(Float, default=0.0, nullable=False)

    # Relationships
    leave_type = relationship("LeaveType")
    employee = relationship("Employee")

    @property
    def remaining_days(self) -> float:
        return (self.allocated_days + self.carried_forward_days) - (self.used_days + self.pending_days)


class LeaveRequest(TenantBaseModel):
    """Leave Application submitted by employee."""
    __tablename__ = "leave_requests"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    leave_type_id = Column(String(36), ForeignKey("leave_types.id", ondelete="CASCADE"), nullable=False, index=True)
    
    start_date = Column(Date, nullable=False, index=True)
    end_date = Column(Date, nullable=False, index=True)
    total_days = Column(Float, nullable=False)
    is_half_day = Column(Boolean, default=False, nullable=False)
    half_day_session = Column(String(20), nullable=True)  # FIRST_HALF, SECOND_HALF
    
    reason = Column(String(1000), nullable=False)
    attachment_url = Column(String(500), nullable=True)
    status = Column(String(50), default="PENDING", nullable=False, index=True)  # PENDING, APPROVED, REJECTED, CANCELLED
    
    approver_id = Column(String(36), nullable=True)  # Employee ID of Approver
    approver_comments = Column(String(500), nullable=True)

    # Relationships
    leave_type = relationship("LeaveType")
    employee = relationship("Employee")


class HolidayCalendar(TenantBaseModel):
    """Statutory & Optional Holidays."""
    __tablename__ = "holiday_calendars"

    name = Column(String(255), nullable=False)
    holiday_date = Column(Date, nullable=False, index=True)
    year = Column(Integer, default=date.today().year, nullable=False, index=True)
    is_optional = Column(Boolean, default=False, nullable=False)
    description = Column(String(500), nullable=True)
