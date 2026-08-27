"""
Recruitment CRM, Interview Panels, and Offer Models
"""
from datetime import datetime, date
from sqlalchemy import Column, String, Date, DateTime, Float, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class JobRequisition(TenantBaseModel):
    """Job Opening / Requisition."""
    __tablename__ = "job_requisitions"

    title = Column(String(255), nullable=False, index=True)
    code = Column(String(50), nullable=False, unique=True, index=True)
    department_id = Column(String(36), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True, index=True)
    positions_count = Column(Integer, default=1, nullable=False)
    min_experience_years = Column(Float, default=0.0, nullable=False)
    max_experience_years = Column(Float, default=10.0, nullable=False)
    required_skills = Column(JSON, default=list, nullable=False)  # ["Python", "FastAPI", "PostgreSQL"]
    job_description = Column(Text, nullable=False)
    salary_min = Column(Float, default=0.0, nullable=False)
    salary_max = Column(Float, default=0.0, nullable=False)
    currency = Column(String(10), default="USD", nullable=False)
    status = Column(String(50), default="OPEN", nullable=False, index=True)  # DRAFT, OPEN, ON_HOLD, CLOSED

    # Relationships
    department = relationship("Department")
    candidates = relationship("Candidate", back_populates="job_requisition", cascade="all, delete-orphan")


class Candidate(TenantBaseModel):
    """Applicant / Talent Pool Candidate profile."""
    __tablename__ = "candidates"

    job_requisition_id = Column(String(36), ForeignKey("job_requisitions.id", ondelete="CASCADE"), nullable=False, index=True)
    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    email = Column(String(255), nullable=False, index=True)
    phone_number = Column(String(50), nullable=True)
    current_company = Column(String(255), nullable=True)
    experience_years = Column(Float, default=0.0, nullable=False)
    
    resume_url = Column(String(500), nullable=True)
    raw_resume_text = Column(Text, nullable=True)
    extracted_skills = Column(JSON, default=list, nullable=False)
    match_score = Column(Float, default=0.0, nullable=False)  # 0.0 - 100.0% AI match score
    
    pipeline_stage = Column(String(50), default="APPLIED", nullable=False, index=True)
    # APPLIED, SCREENING, SHORTLISTED, ASSESSMENT, TECH_INTERVIEW, HR_INTERVIEW, OFFER, HIRED, REJECTED
    
    recruiter_id = Column(String(36), nullable=True)  # User ID
    rejection_reason = Column(String(500), nullable=True)
    notes = Column(Text, nullable=True)

    # Relationships
    job_requisition = relationship("JobRequisition", back_populates="candidates")
    interviews = relationship("Interview", back_populates="candidate", cascade="all, delete-orphan")
    offers = relationship("JobOffer", back_populates="candidate", cascade="all, delete-orphan")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()


class Interview(TenantBaseModel):
    """Scheduled Interview Panel."""
    __tablename__ = "interviews"

    candidate_id = Column(String(36), ForeignKey("candidates.id", ondelete="CASCADE"), nullable=False, index=True)
    interviewer_id = Column(String(36), nullable=False, index=True)  # User ID of Interviewer
    stage = Column(String(50), default="TECH_INTERVIEW", nullable=False)
    scheduled_at = Column(DateTime(timezone=True), nullable=False)
    duration_minutes = Column(Integer, default=45, nullable=False)
    meeting_link = Column(String(500), nullable=True)
    status = Column(String(50), default="SCHEDULED", nullable=False)  # SCHEDULED, COMPLETED, CANCELLED

    # Relationships
    candidate = relationship("Candidate", back_populates="interviews")
    evaluations = relationship("InterviewEvaluation", back_populates="interview", cascade="all, delete-orphan")


class InterviewEvaluation(TenantBaseModel):
    """Interview Scorecard & Feedback Assessment."""
    __tablename__ = "interview_evaluations"

    interview_id = Column(String(36), ForeignKey("interviews.id", ondelete="CASCADE"), nullable=False, index=True)
    evaluator_id = Column(String(36), nullable=False)
    overall_score = Column(Float, default=4.0, nullable=False)  # 1.0 - 5.0
    recommendation = Column(String(50), default="HIRE", nullable=False)  # STRONG_HIRE, HIRE, HOLD, NO_HIRE
    competency_scores = Column(JSON, default=dict, nullable=False)  # {"coding": 4.5, "system_design": 4.0, "communication": 5.0}
    feedback_notes = Column(Text, nullable=False)

    # Relationships
    interview = relationship("Interview", back_populates="evaluations")


class JobOffer(TenantBaseModel):
    """Employment Offer Letter."""
    __tablename__ = "job_offers"

    candidate_id = Column(String(36), ForeignKey("candidates.id", ondelete="CASCADE"), nullable=False, index=True)
    job_requisition_id = Column(String(36), ForeignKey("job_requisitions.id", ondelete="CASCADE"), nullable=False, index=True)
    base_salary = Column(Float, nullable=False)
    joining_bonus = Column(Float, default=0.0, nullable=False)
    proposed_joining_date = Column(Date, nullable=False)
    offer_expiry_date = Column(Date, nullable=False)
    status = Column(String(50), default="DRAFT", nullable=False)  # DRAFT, SENT, ACCEPTED, DECLINED, EXPIRED

    # Relationships
    candidate = relationship("Candidate", back_populates="offers")
