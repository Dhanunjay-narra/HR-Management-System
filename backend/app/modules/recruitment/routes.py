"""
Recruitment API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.recruitment.schemas import (
    JobRequisitionCreate, JobRequisitionResponse, CandidateCreate, CandidateResponse,
    PipelineStageUpdate, InterviewScheduleRequest, InterviewResponse, JobOfferCreate, JobOfferResponse
)
from app.modules.recruitment.services import RecruitmentService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/recruitment", tags=["Recruitment CRM"])


def format_job_response(j) -> dict:
    dept = j.__dict__.get("department")
    candidates = j.__dict__.get("candidates", [])
    return {
        "id": j.id,
        "tenant_id": j.tenant_id,
        "title": j.title,
        "code": j.code,
        "department_id": j.department_id,
        "department_name": dept.name if dept else None,
        "positions_count": j.positions_count,
        "min_experience_years": j.min_experience_years,
        "max_experience_years": j.max_experience_years,
        "required_skills": j.required_skills or [],
        "job_description": j.job_description,
        "salary_min": j.salary_min,
        "salary_max": j.salary_max,
        "currency": j.currency,
        "status": j.status,
        "candidates_count": len(candidates) if candidates else 0,
        "created_at": j.created_at,
    }


def format_candidate_response(c) -> dict:
    job = c.__dict__.get("job_requisition")
    return {
        "id": c.id,
        "tenant_id": c.tenant_id,
        "job_requisition_id": c.job_requisition_id,
        "job_title": job.title if job else None,
        "first_name": c.first_name,
        "last_name": c.last_name,
        "full_name": c.full_name,
        "email": c.email,
        "phone_number": c.phone_number,
        "current_company": c.current_company,
        "experience_years": c.experience_years,
        "resume_url": c.resume_url,
        "raw_resume_text": c.raw_resume_text,
        "extracted_skills": c.extracted_skills or [],
        "match_score": c.match_score,
        "pipeline_stage": c.pipeline_stage,
        "notes": c.notes,
        "created_at": c.created_at,
    }


@router.get("/jobs", response_model=List[JobRequisitionResponse])
async def list_jobs(
    status: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List job requisitions."""
    jobs = await RecruitmentService.list_jobs(db, current_user.tenant_id or "default", status=status)
    return [format_job_response(j) for j in jobs]


@router.post("/jobs", response_model=JobRequisitionResponse, status_code=status.HTTP_201_CREATED)
async def create_job(
    data: JobRequisitionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("recruitment.job.create")),
):
    """Create a new job opening requisition."""
    job = await RecruitmentService.create_job(db, current_user.tenant_id or "default", data)
    return format_job_response(job)


@router.get("/candidates", response_model=List[CandidateResponse])
async def list_candidates(
    job_id: Optional[str] = Query(None),
    stage: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("recruitment.candidate.read")),
):
    """List recruitment pipeline candidates."""
    candidates = await RecruitmentService.list_candidates(
        db, current_user.tenant_id or "default", job_id=job_id, stage=stage, skip=skip, limit=limit
    )
    return [format_candidate_response(c) for c in candidates]


@router.post("/candidates", response_model=CandidateResponse, status_code=status.HTTP_201_CREATED)
async def create_candidate(
    data: CandidateCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("recruitment.candidate.manage")),
):
    """Add candidate and automatically compute AI skill extraction and match scores."""
    candidate = await RecruitmentService.create_candidate(db, current_user.tenant_id or "default", data)
    return format_candidate_response(candidate)


@router.put("/candidates/{candidate_id}/stage", response_model=CandidateResponse)
async def update_candidate_stage(
    candidate_id: str,
    data: PipelineStageUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("recruitment.candidate.manage")),
):
    """Advance or update candidate stage in the recruitment funnel."""
    candidate = await RecruitmentService.update_pipeline_stage(
        db, current_user.tenant_id or "default", candidate_id, data, actor_id=current_user.id
    )
    return format_candidate_response(candidate)


@router.post("/interviews", response_model=InterviewResponse, status_code=status.HTTP_201_CREATED)
async def schedule_interview(
    data: InterviewScheduleRequest,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("recruitment.interview.conduct")),
):
    """Schedule an interview panel."""
    interview = await RecruitmentService.schedule_interview(db, current_user.tenant_id or "default", data)
    return {
        "id": interview.id,
        "candidate_id": interview.candidate_id,
        "interviewer_id": interview.interviewer_id,
        "stage": interview.stage,
        "scheduled_at": interview.scheduled_at,
        "duration_minutes": interview.duration_minutes,
        "meeting_link": interview.meeting_link,
        "status": interview.status,
        "created_at": interview.created_at,
    }


@router.post("/offers", response_model=JobOfferResponse, status_code=status.HTTP_201_CREATED)
async def create_offer(
    data: JobOfferCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("recruitment.candidate.manage")),
):
    """Generate job offer letter."""
    offer = await RecruitmentService.create_offer(db, current_user.tenant_id or "default", data)
    return offer
