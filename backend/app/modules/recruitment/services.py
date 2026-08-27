"""
Recruitment Service
"""
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.recruitment.models import JobRequisition, Candidate, Interview, InterviewEvaluation, JobOffer
from app.modules.recruitment.schemas import (
    JobRequisitionCreate, CandidateCreate, PipelineStageUpdate, InterviewScheduleRequest,
    InterviewEvaluationCreate, JobOfferCreate
)
from app.modules.recruitment.ai_matcher import CandidateIntelligenceEngine
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException, ValidationException
from app.events.event_bus import event_bus, DomainEvent


class RecruitmentService:
    @staticmethod
    async def create_job(db: AsyncSession, tenant_id: str, data: JobRequisitionCreate) -> JobRequisition:
        existing = await db.execute(
            select(JobRequisition).where(
                JobRequisition.code == data.code,
                JobRequisition.tenant_id == tenant_id,
                JobRequisition.is_deleted == False
            )
        )
        if existing.scalar_one_or_none():
            raise DuplicateResourceException("JobRequisition", "code", data.code)

        job = JobRequisition(tenant_id=tenant_id, **data.model_dump())
        db.add(job)
        await db.flush()
        return job

    @staticmethod
    async def list_jobs(db: AsyncSession, tenant_id: str, status: Optional[str] = None) -> List[JobRequisition]:
        query = (
            select(JobRequisition)
            .options(selectinload(JobRequisition.department))
            .where(JobRequisition.tenant_id == tenant_id, JobRequisition.is_deleted == False)
        )
        if status:
            query = query.where(JobRequisition.status == status)
        query = query.order_by(desc(JobRequisition.created_at))
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def create_candidate(db: AsyncSession, tenant_id: str, data: CandidateCreate) -> Candidate:
        # Load Job Requisition
        res_job = await db.execute(
            select(JobRequisition).where(
                JobRequisition.id == data.job_requisition_id,
                JobRequisition.tenant_id == tenant_id,
                JobRequisition.is_deleted == False
            )
        )
        job = res_job.scalar_one_or_none()
        if not job:
            raise ResourceNotFoundException("JobRequisition", data.job_requisition_id)

        # AI Skill Extraction & Match Scoring
        skills = CandidateIntelligenceEngine.extract_skills_from_text(data.raw_resume_text or "")
        match_score = CandidateIntelligenceEngine.calculate_match_score(
            candidate_skills=skills,
            required_skills=job.required_skills or [],
            candidate_exp_years=data.experience_years,
            min_exp_years=job.min_experience_years
        )

        candidate = Candidate(
            tenant_id=tenant_id,
            extracted_skills=skills,
            match_score=match_score,
            **data.model_dump()
        )
        db.add(candidate)
        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="candidate.created",
            tenant_id=tenant_id,
            actor_id=None,
            payload={"candidate_id": candidate.id, "name": candidate.full_name, "score": match_score}
        ))
        return candidate

    @staticmethod
    async def update_pipeline_stage(
        db: AsyncSession,
        tenant_id: str,
        candidate_id: str,
        data: PipelineStageUpdate,
        actor_id: Optional[str] = None
    ) -> Candidate:
        result = await db.execute(
            select(Candidate)
            .options(selectinload(Candidate.job_requisition))
            .where(
                Candidate.id == candidate_id,
                Candidate.tenant_id == tenant_id,
                Candidate.is_deleted == False
            )
        )
        candidate = result.scalar_one_or_none()
        if not candidate:
            raise ResourceNotFoundException("Candidate", candidate_id)

        candidate.pipeline_stage = data.pipeline_stage
        if data.rejection_reason:
            candidate.rejection_reason = data.rejection_reason
        if data.notes:
            candidate.notes = data.notes
        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type=f"candidate.stage_changed",
            tenant_id=tenant_id,
            actor_id=actor_id,
            payload={"candidate_id": candidate.id, "stage": data.pipeline_stage}
        ))
        return candidate

    @staticmethod
    async def list_candidates(
        db: AsyncSession,
        tenant_id: str,
        job_id: Optional[str] = None,
        stage: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[Candidate]:
        query = (
            select(Candidate)
            .options(selectinload(Candidate.job_requisition))
            .where(Candidate.tenant_id == tenant_id, Candidate.is_deleted == False)
        )
        if job_id:
            query = query.where(Candidate.job_requisition_id == job_id)
        if stage:
            query = query.where(Candidate.pipeline_stage == stage)

        query = query.order_by(desc(Candidate.match_score), desc(Candidate.created_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def schedule_interview(db: AsyncSession, tenant_id: str, data: InterviewScheduleRequest) -> Interview:
        interview = Interview(tenant_id=tenant_id, **data.model_dump())
        db.add(interview)
        await db.flush()
        return interview

    @staticmethod
    async def create_offer(db: AsyncSession, tenant_id: str, data: JobOfferCreate) -> JobOffer:
        offer = JobOffer(tenant_id=tenant_id, **data.model_dump())
        db.add(offer)
        await db.flush()
        return offer
