"""
Workflow Automation Engine Models
Configurable Trigger -> Condition -> Action automation.
"""
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class WorkflowDefinition(TenantBaseModel):
    """Configurable Business Automation Rule."""
    __tablename__ = "workflow_definitions"

    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    trigger_event = Column(String(100), nullable=False, index=True)  # e.g., employee.joined, leave.applied, ticket.created
    conditions = Column(JSON, default=dict, nullable=False)  # e.g., {"department_name": "Engineering"}
    actions = Column(JSON, default=list, nullable=False)
    # [{"type": "create_task", "title": "Setup SSH Keys"}, {"type": "send_notification", "message": "New hire in your team"}]
    is_active = Column(Boolean, default=True, nullable=False, index=True)

    # Relationships
    executions = relationship("WorkflowExecution", back_populates="workflow", cascade="all, delete-orphan")


class WorkflowExecution(TenantBaseModel):
    """Audit record for triggered workflow runs."""
    __tablename__ = "workflow_executions"

    workflow_id = Column(String(36), ForeignKey("workflow_definitions.id", ondelete="CASCADE"), nullable=False, index=True)
    trigger_event = Column(String(100), nullable=False)
    payload = Column(JSON, default=dict, nullable=False)
    status = Column(String(50), default="COMPLETED", nullable=False)  # RUNNING, COMPLETED, FAILED
    execution_logs = Column(JSON, default=list, nullable=False)
    executed_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    workflow = relationship("WorkflowDefinition", back_populates="executions")
