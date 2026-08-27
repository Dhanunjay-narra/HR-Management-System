"""
Engagement Service
"""
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.engagement.models import EngagementSurvey, SurveyResponse, RecognitionKudos
from app.modules.engagement.schemas import (
    EngagementSurveyCreate, SurveyResponseCreate, KudosSendRequest
)
from app.core.exceptions import ResourceNotFoundException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class EngagementService:
    @staticmethod
    async def create_survey(db: AsyncSession, tenant_id: str, data: EngagementSurveyCreate) -> EngagementSurvey:
        survey = EngagementSurvey(tenant_id=tenant_id, **data.model_dump())
        db.add(survey)
        await db.flush()
        return survey

    @staticmethod
    async def list_surveys(db: AsyncSession, tenant_id: str) -> List[EngagementSurvey]:
        result = await db.execute(
            select(EngagementSurvey)
            .options(selectinload(EngagementSurvey.responses))
            .where(EngagementSurvey.tenant_id == tenant_id, EngagementSurvey.is_deleted == False)
            .order_by(desc(EngagementSurvey.created_at))
        )
        return list(result.scalars().all())

    @staticmethod
    async def submit_response(
        db: AsyncSession,
        tenant_id: str,
        survey_id: str,
        employee_id: str,
        data: SurveyResponseCreate
    ) -> SurveyResponse:
        res = await db.execute(
            select(EngagementSurvey).where(
                EngagementSurvey.id == survey_id,
                EngagementSurvey.tenant_id == tenant_id,
                EngagementSurvey.is_deleted == False
            )
        )
        survey = res.scalar_one_or_none()
        if not survey:
            raise ResourceNotFoundException("EngagementSurvey", survey_id)

        resp = SurveyResponse(
            tenant_id=tenant_id,
            survey_id=survey.id,
            employee_id=None if survey.is_anonymous else employee_id,
            answers=data.answers,
            sentiment_score=0.8
        )
        db.add(resp)
        await db.flush()
        return resp

    @staticmethod
    async def send_kudos(
        db: AsyncSession,
        tenant_id: str,
        sender_id: str,
        data: KudosSendRequest
    ) -> RecognitionKudos:
        kudos = RecognitionKudos(
            tenant_id=tenant_id,
            sender_employee_id=sender_id,
            **data.model_dump()
        )
        db.add(kudos)
        await db.flush()

        # Add timeline event to receiver
        db.add(EmployeeTimelineEvent(
            tenant_id=tenant_id,
            employee_id=data.receiver_employee_id,
            actor_id=sender_id,
            event_type="RECOGNITION_RECEIVED",
            title=f"Peer Kudos: {data.badge_type.replace('_', ' ').title()}",
            description=f"Received recognition badge: '{data.message}'",
            entity_type="RecognitionKudos",
            entity_id=kudos.id
        ))
        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="engagement.kudos_sent",
            tenant_id=tenant_id,
            actor_id=sender_id,
            payload={"kudos_id": kudos.id, "receiver_id": data.receiver_employee_id, "badge": data.badge_type}
        ))
        return kudos

    @staticmethod
    async def list_kudos_wall(db: AsyncSession, tenant_id: str, limit: int = 50) -> List[RecognitionKudos]:
        result = await db.execute(
            select(RecognitionKudos)
            .options(selectinload(RecognitionKudos.sender), selectinload(RecognitionKudos.receiver))
            .where(
                RecognitionKudos.tenant_id == tenant_id,
                RecognitionKudos.is_public == True,
                RecognitionKudos.is_deleted == False
            )
            .order_by(desc(RecognitionKudos.created_at))
            .limit(limit)
        )
        return list(result.scalars().all())
