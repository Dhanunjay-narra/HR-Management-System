"""
Goals & OKR Schemas
"""
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class KeyResultCreate(BaseModel):
    title: str
    target_value: float = 100.0
    current_value: float = 0.0
    unit: str = "PERCENT"


class KeyResultResponse(KeyResultCreate):
    id: str
    goal_id: str

    model_config = ConfigDict(from_attributes=True)


class GoalBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    description: Optional[str] = None
    level: str = "INDIVIDUAL"  # COMPANY, DEPARTMENT, TEAM, INDIVIDUAL
    parent_goal_id: Optional[str] = None
    owner_employee_id: Optional[str] = None
    department_id: Optional[str] = None
    target_value: float = 100.0
    current_value: float = 0.0
    unit: str = "PERCENT"
    weight: float = 1.0
    start_date: date = Field(default_factory=date.today)
    deadline: date
    status: str = "IN_PROGRESS"


class GoalCreate(GoalBase):
    key_results: List[KeyResultCreate] = []


class GoalResponse(GoalBase):
    id: str
    tenant_id: str
    progress_percentage: float
    key_results: List[KeyResultResponse] = []
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class GoalCheckInCreate(BaseModel):
    new_value: float
    confidence_score: int = Field(4, ge=1, le=5)
    notes: str = Field(..., min_length=3)
