"""
Centralized Multi-Level Approval Engine Models
"""
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class ApprovalChain(TenantBaseModel):
    """Approval Policy Definition."""
    __tablename__ = "approval_chains"

    name = Column(String(255), nullable=False)
    module_name = Column(String(50), nullable=False, index=True)  # LEAVE, EXPENSE, PROMOTION, SALARY_CHANGE, ASSET_REQUEST
    steps = Column(JSON, default=list, nullable=False)
    # [{"step": 1, "role": "dept_manager", "description": "Manager Review"}, {"step": 2, "role": "finance_admin", "description": "Finance Clearance"}]
    is_active = Column(Boolean, default=True, nullable=False)


class ApprovalRequest(TenantBaseModel):
    """Individual Approval Process Instance."""
    __tablename__ = "approval_requests"

    chain_id = Column(String(36), ForeignKey("approval_chains.id", ondelete="SET NULL"), nullable=True, index=True)
    requester_employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    
    entity_type = Column(String(50), nullable=False, index=True)  # ExpenseClaim, Promotion, LeaveRequest
    entity_id = Column(String(36), nullable=False, index=True)
    
    current_step_index = Column(Integer, default=1, nullable=False)
    total_steps = Column(Integer, default=1, nullable=False)
    status = Column(String(50), default="PENDING", nullable=False, index=True)  # PENDING, APPROVED, REJECTED, CANCELLED

    # Relationships
    chain = relationship("ApprovalChain")
    requester = relationship("Employee")
    history = relationship("ApprovalHistory", back_populates="request", cascade="all, delete-orphan")


class ApprovalHistory(TenantBaseModel):
    """Action log at each step of approval."""
    __tablename__ = "approval_history"

    request_id = Column(String(36), ForeignKey("approval_requests.id", ondelete="CASCADE"), nullable=False, index=True)
    step_index = Column(Integer, nullable=False)
    approver_user_id = Column(String(36), nullable=False)
    action = Column(String(50), nullable=False)  # APPROVED, REJECTED
    comments = Column(Text, nullable=True)
    acted_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    request = relationship("ApprovalRequest", back_populates="history")
