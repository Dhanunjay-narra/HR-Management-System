"""
Analytics Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel


class HeadcountMetric(BaseModel):
    total_employees: int
    active_employees: int
    probation_employees: int
    on_leave_employees: int
    contractors_count: int
    attrition_rate_percent: float


class DepartmentMetric(BaseModel):
    department_id: str
    department_name: str
    headcount: int
    monthly_payroll_budget: float


class WorkforceAnalyticsOverview(BaseModel):
    headcount: HeadcountMetric
    department_distribution: List[DepartmentMetric] = []
    gender_diversity: Dict[str, int] = {}
    average_attendance_rate: float
    open_requisitions_count: int
    total_open_tickets: int
    total_active_goals: int
    generated_at: datetime
