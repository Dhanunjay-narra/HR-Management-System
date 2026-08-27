"""
LMS & Learning Schemas
"""
from typing import Optional, List
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict, Field


class LessonBase(BaseModel):
    title: str
    content_type: str = "VIDEO"
    content_url: Optional[str] = None
    duration_minutes: int = 20
    order_index: int = 1


class LessonCreate(LessonBase):
    pass


class LessonResponse(LessonBase):
    id: str
    course_id: str

    model_config = ConfigDict(from_attributes=True)


class CourseBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    code: str = Field(..., min_length=1, max_length=50)
    category: str = "ENGINEERING"
    description: str = Field(..., min_length=5)
    duration_hours: float = 10.0
    level: str = "INTERMEDIATE"
    provider: str = "Internal"
    thumbnail_url: Optional[str] = None
    target_skill_id: Optional[str] = None


class CourseCreate(CourseBase):
    lessons: List[LessonCreate] = []


class CourseResponse(CourseBase):
    id: str
    tenant_id: str
    lessons: List[LessonResponse] = []
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class EnrollmentCreate(BaseModel):
    course_id: str
    employee_id: str


class EnrollmentResponse(BaseModel):
    id: str
    course_id: str
    course_title: Optional[str] = None
    employee_id: str
    progress_percentage: float
    status: str
    certificate_url: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CertificationCreate(BaseModel):
    employee_id: str
    name: str
    issuing_organization: str
    issue_date: date
    expiry_date: Optional[date] = None
    credential_id: Optional[str] = None
    credential_url: Optional[str] = None


class CertificationResponse(CertificationCreate):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
