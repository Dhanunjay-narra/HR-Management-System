"""
Recruitment Pydantic Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import datetime, date
from pydantic import BaseModel, EmailStr, ConfigDict, Field


class JobRequisitionBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    code: str = Field(..., min_length=1, max_length=50)
    department_id: Optional[str] = None
    positions_count: int = 1
    min_experience_years: float = 0.0
    max_experience_years: float = 10.0
    required_skills: List[str] = []
    job_description: str = Field(..., min_length=10)
    salary_min: float = 0.0
    salary_max: float = 0.0
    currency: str = "USD"
    status: str = "OPEN"


class JobRequisitionCreate(JobRequisitionBase):
    pass


class JobRequisitionResponse(JobRequisitionBase):
    id: str
    tenant_id: str
    department_name: Optional[str] = None
    candidates_count: int = 0
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CandidateBase(BaseModel):
    job_requisition_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    current_company: Optional[str] = None
    experience_years: float = 0.0
    resume_url: Optional[str] = None
    raw_resume_text: Optional[str] = None
    pipeline_stage: str = "APPLIED"
    notes: Optional[str] = None


class CandidateCreate(CandidateBase):
    pass


class PipelineStageUpdate(BaseModel):
    pipeline_stage: str  # APPLIED, SCREENING, SHORTLISTED, ASSESSMENT, TECH_INTERVIEW, HR_INTERVIEW, OFFER, HIRED, REJECTED
    rejection_reason: Optional[str] = None
    notes: Optional[str] = None


class CandidateResponse(CandidateBase):
    id: str
    tenant_id: str
    full_name: str
    extracted_skills: List[str] = []
    match_score: float = 0.0
    job_title: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class InterviewScheduleRequest(BaseModel):
    candidate_id: str
    interviewer_id: str
    stage: str = "TECH_INTERVIEW"
    scheduled_at: datetime
    duration_minutes: int = 45
    meeting_link: Optional[str] = None


class InterviewEvaluationCreate(BaseModel):
    overall_score: float = Field(..., ge=1.0, le=5.0)
    recommendation: str  # STRONG_HIRE, HIRE, HOLD, NO_HIRE
    competency_scores: Dict[str, float] = {}
    feedback_notes: str = Field(..., min_length=5)


class InterviewResponse(BaseModel):
    id: str
    candidate_id: str
    candidate_name: Optional[str] = None
    interviewer_id: str
    stage: str
    scheduled_at: datetime
    duration_minutes: int
    meeting_link: Optional[str] = None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class JobOfferCreate(BaseModel):
    candidate_id: str
    job_requisition_id: str
    base_salary: float
    joining_bonus: float = 0.0
    proposed_joining_date: date
    offer_expiry_date: date


class JobOfferResponse(JobOfferCreate):
    id: str
    tenant_id: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
