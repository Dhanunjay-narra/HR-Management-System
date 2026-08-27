"""
Internal Communication & Announcements Models
"""
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class Announcement(TenantBaseModel):
    """Company-wide or targeted department announcement."""
    __tablename__ = "announcements"

    title = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    target_department_id = Column(String(36), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True, index=True)
    target_branch_id = Column(String(36), ForeignKey("branches.id", ondelete="SET NULL"), nullable=True, index=True)
    
    priority = Column(String(20), default="NORMAL", nullable=False)  # NORMAL, URGENT, CRITICAL
    author_user_id = Column(String(36), nullable=False)
    author_name = Column(String(100), nullable=True)
    
    is_pinned = Column(Boolean, default=False, nullable=False)
    publish_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    expires_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    target_department = relationship("Department")
    target_branch = relationship("Branch")
