"""
Onboarding Schemas
"""
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class OnboardingTaskResponse(BaseModel):
    id: str
    workflow_id: str
    title: str
    description: Optional[str] = None
    category: str
    assigned_to_user_id: Optional[str] = None
    due_date: date
    is_completed: bool
    completed_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class OnboardingWorkflowCreate(BaseModel):
    employee_id: str
    template_name: str = "Standard Enterprise Onboarding"
    target_completion_days: int = 30


class OnboardingWorkflowResponse(BaseModel):
    id: str
    tenant_id: str
    employee_id: str
    employee_name: Optional[str] = None
    template_name: str
    status: str
    start_date: date
    target_completion_date: date
    completed_at: Optional[datetime] = None
    tasks: List[OnboardingTaskResponse] = []
    progress_percentage: float = 0.0

    model_config = ConfigDict(from_attributes=True)


class TaskCompleteRequest(BaseModel):
    notes: Optional[str] = None


class MilestoneReviewCreate(BaseModel):
    employee_id: str
    milestone: str  # DAY_30, DAY_60, DAY_90
    rating: int = Field(5, ge=1, le=5)
    feedback: str = Field(..., min_length=5)


class MilestoneReviewResponse(BaseModel):
    id: str
    employee_id: str
    milestone: str
    due_date: date
    status: str
    rating: Optional[int] = None
    feedback: Optional[str] = None
    completed_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
