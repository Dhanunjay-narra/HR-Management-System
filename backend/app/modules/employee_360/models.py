"""
Employee 360 & Life-Cycle Timeline Models
"""
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class EmployeeTimelineEvent(TenantBaseModel):
    """
    Chronological Life-Cycle Event in the Employee 360 CRM.
    Records onboarding, promotions, transfers, compensation revisions, performance reviews, trainings, recognitions, and exits.
    """
    __tablename__ = "employee_timeline_events"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    actor_id = Column(String(36), nullable=True)  # User ID who triggered or authored the event
    actor_name = Column(String(255), nullable=True)
    
    event_type = Column(String(100), nullable=False, index=True)  # JOINED, PROMOTION, TRANSFER, GOAL_ACHIEVED, REVIEW_COMPLETED, ASSET_ASSIGNED, SALARY_REVISED, TICKET_RESOLVED, TRAINING_COMPLETED, EXIT
    title = Column(String(255), nullable=False)
    description = Column(String(2000), nullable=True)
    
    entity_type = Column(String(100), nullable=True)  # Goal, PerformanceReview, Asset, Payroll, Course
    entity_id = Column(String(36), nullable=True)
    metadata_json = Column(JSON, default=dict, nullable=False)
    
    event_timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    # Relationships
    employee = relationship("Employee", back_populates="timeline_events")
