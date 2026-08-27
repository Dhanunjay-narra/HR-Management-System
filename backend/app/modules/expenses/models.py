"""
Expense Management & Reimbursement Models
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Float, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class ExpenseCategory(TenantBaseModel):
    """Expense Claim Categories."""
    __tablename__ = "expense_categories"

    name = Column(String(100), nullable=False)
    code = Column(String(50), nullable=False, unique=True, index=True)
    max_limit = Column(Float, default=1000.0, nullable=False)
    requires_receipt = Column(Boolean, default=True, nullable=False)
    description = Column(String(500), nullable=True)


class ExpenseClaim(TenantBaseModel):
    """Employee Expense Reimbursement Request."""
    __tablename__ = "expense_claims"

    claim_number = Column(String(50), nullable=False, unique=True, index=True)  # e.g., EXP-2026-0081
    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    category_id = Column(String(36), ForeignKey("expense_categories.id", ondelete="SET NULL"), nullable=True, index=True)
    
    expense_date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String(10), default="USD", nullable=False)
    merchant_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    receipt_url = Column(String(500), nullable=True)
    
    status = Column(String(50), default="SUBMITTED", nullable=False, index=True)  # SUBMITTED, APPROVED, REJECTED, REIMBURSED
    approver_id = Column(String(36), nullable=True)
    rejection_reason = Column(String(500), nullable=True)
    reimbursed_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    category = relationship("ExpenseCategory")
    employee = relationship("Employee")
