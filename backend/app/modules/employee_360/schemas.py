"""
Employee 360 Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TimelineEventResponse(BaseModel):
    id: str
    event_type: str
    title: str
    description: Optional[str] = None
    actor_name: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[str] = None
    metadata_json: Dict[str, Any] = {}
    event_timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


class Employee360OverviewResponse(BaseModel):
    employee_id: str
    employee_code: str
    full_name: str
    work_email: str
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    designation: Optional[str] = None
    department: Optional[str] = None
    branch: Optional[str] = None
    employment_type: str
    status: str
    joining_date: str
    tenure_days: int

    # Manager & Team
    manager: Optional[Dict[str, Any]] = None
    direct_reports_count: int = 0
    peers: List[Dict[str, Any]] = []

    # Aggregated metrics
    attendance_rate_last_30_days: float = 98.5
    leave_balance_days: float = 18.0
    active_goals_count: int = 0
    skills_count: int = 0
    assigned_assets_count: int = 0
    open_tickets_count: int = 0

    # Recent activity
    recent_timeline: List[TimelineEventResponse] = []
