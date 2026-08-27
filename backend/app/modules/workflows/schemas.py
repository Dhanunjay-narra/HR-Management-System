"""
Workflow Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class WorkflowDefinitionBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    description: Optional[str] = None
    trigger_event: str = Field(..., min_length=2)  # e.g., employee.joined, leave.approved
    conditions: Dict[str, Any] = {}
    actions: List[Dict[str, Any]] = []
    is_active: bool = True


class WorkflowDefinitionCreate(WorkflowDefinitionBase):
    pass


class WorkflowDefinitionResponse(WorkflowDefinitionBase):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class WorkflowExecutionResponse(BaseModel):
    id: str
    workflow_id: str
    trigger_event: str
    status: str
    execution_logs: List[str] = []
    executed_at: datetime

    model_config = ConfigDict(from_attributes=True)
