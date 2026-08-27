"""
HR Service Desk CRM & Ticketing Models
"""
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class TicketCategory(TenantBaseModel):
    """Service Desk Queues (e.g. Payroll, IT, Benefits, Leave, Policy)."""
    __tablename__ = "ticket_categories"

    name = Column(String(100), nullable=False)
    code = Column(String(50), nullable=False, unique=True, index=True)
    default_priority = Column(String(20), default="MEDIUM", nullable=False)
    sla_response_hours = Column(Integer, default=24, nullable=False)
    sla_resolution_hours = Column(Integer, default=72, nullable=False)
    description = Column(String(500), nullable=True)


class HRTicket(TenantBaseModel):
    """HR Service Request Ticket."""
    __tablename__ = "hr_tickets"

    ticket_number = Column(String(50), nullable=False, unique=True, index=True)  # e.g., TKT-2026-0042
    category_id = Column(String(36), ForeignKey("ticket_categories.id", ondelete="SET NULL"), nullable=True, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    assigned_agent_id = Column(String(36), nullable=True, index=True)  # User ID of HR Agent
    
    subject = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    priority = Column(String(20), default="MEDIUM", nullable=False, index=True)  # LOW, MEDIUM, HIGH, URGENT
    status = Column(String(50), default="OPEN", nullable=False, index=True)  # OPEN, IN_PROGRESS, WAITING, RESOLVED, CLOSED
    
    due_date = Column(DateTime(timezone=True), nullable=True)
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    resolution_summary = Column(Text, nullable=True)

    # Relationships
    category = relationship("TicketCategory")
    employee = relationship("Employee")
    comments = relationship("TicketComment", back_populates="ticket", cascade="all, delete-orphan")


class TicketComment(TenantBaseModel):
    """Public message or internal note on a ticket."""
    __tablename__ = "ticket_comments"

    ticket_id = Column(String(36), ForeignKey("hr_tickets.id", ondelete="CASCADE"), nullable=False, index=True)
    author_user_id = Column(String(36), nullable=False)
    author_name = Column(String(100), nullable=True)
    comment_text = Column(Text, nullable=False)
    is_internal_note = Column(Boolean, default=False, nullable=False)
    attachment_url = Column(String(500), nullable=True)

    # Relationships
    ticket = relationship("HRTicket", back_populates="comments")
