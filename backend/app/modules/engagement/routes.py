"""
Engagement API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.engagement.schemas import (
    EngagementSurveyCreate, EngagementSurveyResponse, SurveyResponseCreate,
    KudosSendRequest, KudosResponse
)
from app.modules.engagement.services import EngagementService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/engagement", tags=["Employee Engagement"])


def format_survey_response(s) -> dict:
    responses = s.__dict__.get("responses", [])
    return {
        "id": s.id,
        "tenant_id": s.tenant_id,
        "title": s.title,
        "description": s.description,
        "survey_type": s.survey_type,
        "start_date": s.start_date,
        "end_date": s.end_date,
        "is_anonymous": s.is_anonymous,
        "is_active": s.is_active,
        "questions": s.questions or [],
        "responses_count": len(responses) if responses else 0,
        "created_at": s.created_at,
    }


def format_kudos_response(k) -> dict:
    sender = k.__dict__.get("sender")
    receiver = k.__dict__.get("receiver")
    return {
        "id": k.id,
        "sender_employee_id": k.sender_employee_id,
        "sender_name": sender.full_name if sender else None,
        "receiver_employee_id": k.receiver_employee_id,
        "receiver_name": receiver.full_name if receiver else None,
        "badge_type": k.badge_type,
        "message": k.message,
        "is_public": k.is_public,
        "created_at": k.created_at,
    }


@router.get("/surveys", response_model=List[EngagementSurveyResponse])
async def list_surveys(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List engagement and pulse surveys."""
    surveys = await EngagementService.list_surveys(db, current_user.tenant_id or "default")
    return [format_survey_response(s) for s in surveys]


@router.post("/surveys", response_model=EngagementSurveyResponse, status_code=status.HTTP_201_CREATED)
async def create_survey(
    data: EngagementSurveyCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("engagement.survey.manage")),
):
    """Create a new pulse survey."""
    survey = await EngagementService.create_survey(db, current_user.tenant_id or "default", data)
    return format_survey_response(survey)


@router.post("/surveys/{survey_id}/respond", status_code=status.HTTP_201_CREATED)
async def submit_survey_response(
    survey_id: str,
    data: SurveyResponseCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("engagement.survey.participate")),
):
    """Submit responses to a survey."""
    resp = await EngagementService.submit_response(
        db, current_user.tenant_id or "default", survey_id, current_user.id, data
    )
    return {"success": True, "id": resp.id}


@router.post("/kudos", response_model=KudosResponse, status_code=status.HTTP_201_CREATED)
async def send_peer_kudos(
    data: KudosSendRequest,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("engagement.kudos.send")),
):
    """Send recognition badge and message to a colleague."""
    kudos = await EngagementService.send_kudos(
        db, current_user.tenant_id or "default", current_user.id, data
    )
    return format_kudos_response(kudos)


@router.get("/kudos/wall", response_model=List[KudosResponse])
async def get_kudos_wall(
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Retrieve public peer recognition feed."""
    kudos_items = await EngagementService.list_kudos_wall(db, current_user.tenant_id or "default", limit=limit)
    return [format_kudos_response(k) for k in kudos_items]
