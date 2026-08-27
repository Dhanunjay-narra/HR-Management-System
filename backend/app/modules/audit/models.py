"""
Audit Log Models
Provides an immutable trail of every important business mutation with diffs and actor context.
"""
from sqlalchemy import Column, String, JSON, DateTime, Index
from app.database.base import BaseModel


class AuditLog(BaseModel):
    """Immutable enterprise audit log."""
    __tablename__ = "audit_logs"

    tenant_id = Column(String(36), nullable=True, index=True)
    actor_id = Column(String(36), nullable=True, index=True)
    actor_email = Column(String(255), nullable=True)
    action = Column(String(100), nullable=False, index=True)  # e.g., employee.update, salary.change
    entity_name = Column(String(100), nullable=False, index=True)  # e.g., Employee, Payroll
    entity_id = Column(String(36), nullable=False, index=True)
    before_state = Column(JSON, nullable=True)
    after_state = Column(JSON, nullable=True)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(String(500), nullable=True)
    request_id = Column(String(50), nullable=True, index=True)
    description = Column(String(500), nullable=True)
