"""
Employee Engagement, Surveys & Peer Recognition Models
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Float, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class EngagementSurvey(TenantBaseModel):
    """Pulse, eNPS, and Organizational Surveys."""
    __tablename__ = "engagement_surveys"

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    survey_type = Column(String(50), default="PULSE", nullable=False)  # PULSE, ENPS, SATISFACTION, EXIT
    start_date = Column(Date, default=date.today, nullable=False)
    end_date = Column(Date, nullable=False)
    is_anonymous = Column(Boolean, default=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    questions = Column(JSON, default=list, nullable=False)
    # [{"id": "q1", "text": "How likely are you to recommend PeoplePulse?", "type": "scale_1_10"}]

    # Relationships
    responses = relationship("SurveyResponse", back_populates="survey", cascade="all, delete-orphan")


class SurveyResponse(TenantBaseModel):
    """Submitted Survey Answers."""
    __tablename__ = "survey_responses"

    survey_id = Column(String(36), ForeignKey("engagement_surveys.id", ondelete="CASCADE"), nullable=False, index=True)
    employee_id = Column(String(36), nullable=True)  # Null if anonymous
    answers = Column(JSON, default=dict, nullable=False)
    sentiment_score = Column(Float, default=0.0, nullable=False)  # -1.0 to +1.0

    # Relationships
    survey = relationship("EngagementSurvey", back_populates="responses")


class RecognitionKudos(TenantBaseModel):
    """Peer Recognition & Kudos Badges."""
    __tablename__ = "recognition_kudos"

    sender_employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    receiver_employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    badge_type = Column(String(50), default="TEAM_PLAYER", nullable=False)  # INNOVATION, TEAM_PLAYER, LEADERSHIP, CUSTOMER_CHAMPION
    message = Column(Text, nullable=False)
    is_public = Column(Boolean, default=True, nullable=False)

    # Relationships
    sender = relationship("Employee", foreign_keys=[sender_employee_id])
    receiver = relationship("Employee", foreign_keys=[receiver_employee_id])
