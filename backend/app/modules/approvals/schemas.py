"""
Approval Engine Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ApprovalChainBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    module_name: str = Field(..., min_length=2, max_length=50)  # LEAVE, EXPENSE, PROMOTION, SALARY_CHANGE, ASSET_REQUEST
    steps: List[Dict[str, Any]] = []
    is_active: bool = True


class ApprovalChainCreate(ApprovalChainBase):
    pass


class ApprovalChainResponse(ApprovalChainBase):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ApprovalRequestCreate(BaseModel):
    chain_id: Optional[str] = None
    entity_type: str
    entity_id: str


class ApprovalActionRequest(BaseModel):
    action: str  # APPROVED, REJECTED
    comments: Optional[str] = None


class ApprovalHistoryResponse(BaseModel):
    id: str
    step_index: int
    approver_user_id: str
    action: str
    comments: Optional[str] = None
    acted_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ApprovalRequestResponse(BaseModel):
    id: str
    tenant_id: str
    chain_id: Optional[str] = None
    requester_employee_id: str
    entity_type: str
    entity_id: str
    current_step_index: int
    total_steps: int
    status: str
    history: List[ApprovalHistoryResponse] = []
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
