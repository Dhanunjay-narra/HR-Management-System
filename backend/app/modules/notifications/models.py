"""
Notification Models
"""
from sqlalchemy import Column, String, Boolean, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel, BaseModel


class Notification(TenantBaseModel):
    """In-app and channel notifications for users."""
    __tablename__ = "notifications"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    message = Column(String(1000), nullable=False)
    notification_type = Column(String(50), default="info", nullable=False)  # info, warning, success, action_required
    category = Column(String(50), default="general", nullable=False)  # leave, payroll, workflow, performance, ticket
    action_url = Column(String(500), nullable=True)
    is_read = Column(Boolean, default=False, nullable=False, index=True)
    read_at = Column(DateTime(timezone=True), nullable=True)
    metadata_json = Column(JSON, default=dict, nullable=False)


class NotificationTemplate(BaseModel):
    """Reusable notification message templates."""
    __tablename__ = "notification_templates"

    event_type = Column(String(100), nullable=False, unique=True, index=True)
    title_template = Column(String(255), nullable=False)
    body_template = Column(String(2000), nullable=False)
    channels = Column(JSON, default=lambda: ["in_app", "email"], nullable=False)
