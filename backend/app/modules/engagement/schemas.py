"""
Engagement Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class EngagementSurveyCreate(BaseModel):
    title: str = Field(..., min_length=2)
    description: Optional[str] = None
    survey_type: str = "PULSE"
    start_date: date = Field(default_factory=date.today)
    end_date: date
    is_anonymous: bool = True
    questions: List[Dict[str, Any]] = []


class EngagementSurveyResponse(EngagementSurveyCreate):
    id: str
    tenant_id: str
    is_active: bool
    responses_count: int = 0
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SurveyResponseCreate(BaseModel):
    answers: Dict[str, Any]


class KudosSendRequest(BaseModel):
    receiver_employee_id: str
    badge_type: str = "TEAM_PLAYER"  # INNOVATION, TEAM_PLAYER, LEADERSHIP, CUSTOMER_CHAMPION
    message: str = Field(..., min_length=3, max_length=1000)
    is_public: bool = True


class KudosResponse(BaseModel):
    id: str
    sender_employee_id: str
    sender_name: Optional[str] = None
    receiver_employee_id: str
    receiver_name: Optional[str] = None
    badge_type: str
    message: str
    is_public: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
