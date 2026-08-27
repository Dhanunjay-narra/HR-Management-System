"""
Performance Review & 360 Feedback Models
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Float, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class PerformanceCycle(TenantBaseModel):
    """Configurable Performance Appraisal Cycles (Annual, Semi-Annual, Quarterly)."""
    __tablename__ = "performance_cycles"

    name = Column(String(255), nullable=False)
    code = Column(String(50), nullable=False, unique=True, index=True)
    cycle_type = Column(String(50), default="ANNUAL", nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    self_review_deadline = Column(Date, nullable=False)
    manager_review_deadline = Column(Date, nullable=False)
    status = Column(String(50), default="ACTIVE", nullable=False, index=True)  # DRAFT, ACTIVE, EVALUATION, CLOSED

    # Relationships
    reviews = relationship("PerformanceReview", back_populates="cycle", cascade="all, delete-orphan")


class PerformanceReview(TenantBaseModel):
    """Employee Appraisal Form."""
    __tablename__ = "performance_reviews"

    cycle_id = Column(String(36), ForeignKey("performance_cycles.id", ondelete="CASCADE"), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    manager_id = Column(String(36), ForeignKey("employees.id", ondelete="SET NULL"), nullable=True, index=True)
    
    status = Column(String(50), default="SELF_REVIEW_PENDING", nullable=False, index=True)
    # SELF_REVIEW_PENDING, MANAGER_REVIEW_PENDING, HR_CALIBRATION, COMPLETED
    
    self_rating = Column(Float, nullable=True)  # 1.0 - 5.0
    self_assessment_text = Column(Text, nullable=True)
    
    manager_rating = Column(Float, nullable=True)
    manager_feedback = Column(Text, nullable=True)
    
    final_score = Column(Float, nullable=True)
    is_pip_required = Column(Boolean, default=False, nullable=False)
    pip_plan_details = Column(Text, nullable=True)

    # Relationships
    cycle = relationship("PerformanceCycle", back_populates="reviews")
    employee = relationship("Employee", foreign_keys=[employee_id])
    manager = relationship("Employee", foreign_keys=[manager_id])
    peer_feedbacks = relationship("PeerFeedback360", back_populates="review", cascade="all, delete-orphan")


class PeerFeedback360(TenantBaseModel):
    """360-degree Peer Assessment."""
    __tablename__ = "peer_feedback_360"

    review_id = Column(String(36), ForeignKey("performance_reviews.id", ondelete="CASCADE"), nullable=False, index=True)
    peer_employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    relationship_type = Column(String(50), default="PEER", nullable=False)  # PEER, SUBORDINATE, CROSS_FUNCTIONAL
    rating = Column(Float, default=5.0, nullable=False)
    feedback_text = Column(Text, nullable=False)
    is_submitted = Column(Boolean, default=False, nullable=False)

    # Relationships
    review = relationship("PerformanceReview", back_populates="peer_feedbacks")
    peer_employee = relationship("Employee", foreign_keys=[peer_employee_id])
