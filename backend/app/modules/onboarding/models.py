"""
Onboarding & Milestone Review Models
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class OnboardingWorkflow(TenantBaseModel):
    """Employee Onboarding Journey."""
    __tablename__ = "onboarding_workflows"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    template_name = Column(String(100), default="Standard Enterprise Onboarding", nullable=False)
    status = Column(String(50), default="IN_PROGRESS", nullable=False, index=True)  # IN_PROGRESS, COMPLETED, OVERDUE
    start_date = Column(Date, default=date.today, nullable=False)
    target_completion_date = Column(Date, nullable=False)
    completed_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    employee = relationship("Employee")
    tasks = relationship("OnboardingTask", back_populates="workflow", cascade="all, delete-orphan")


class OnboardingTask(TenantBaseModel):
    """Individual Checklist Task in the onboarding flow."""
    __tablename__ = "onboarding_tasks"

    workflow_id = Column(String(36), ForeignKey("onboarding_workflows.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String(50), default="DOCUMENTATION", nullable=False)  # DOCUMENTATION, IT_HARDWARE, ACCESS_CREDENTIALS, TRAINING, MANAGER_1ON1
    assigned_to_user_id = Column(String(36), nullable=True)  # User ID of Assignee (IT Admin, HR, Employee)
    due_date = Column(Date, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False, index=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    workflow = relationship("OnboardingWorkflow", back_populates="tasks")


class MilestoneReview(TenantBaseModel):
    """30 / 60 / 90 Day Check-in reviews for new hires."""
    __tablename__ = "milestone_reviews"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    milestone = Column(String(20), nullable=False)  # DAY_30, DAY_60, DAY_90
    due_date = Column(Date, nullable=False)
    status = Column(String(50), default="PENDING", nullable=False)  # PENDING, COMPLETED
    reviewer_id = Column(String(36), nullable=True)
    rating = Column(Integer, default=5, nullable=True)  # 1 to 5
    feedback = Column(Text, nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    employee = relationship("Employee")
