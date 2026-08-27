"""
LMS & Learning API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.learning.schemas import (
    CourseCreate, CourseResponse, EnrollmentCreate, EnrollmentResponse,
    CertificationCreate, CertificationResponse
)
from app.modules.learning.services import LearningService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/learning", tags=["Learning & Certifications"])


def format_course_response(c) -> dict:
    lessons = c.__dict__.get("lessons", [])
    return {
        "id": c.id,
        "tenant_id": c.tenant_id,
        "title": c.title,
        "code": c.code,
        "category": c.category,
        "description": c.description,
        "duration_hours": c.duration_hours,
        "level": c.level,
        "provider": c.provider,
        "thumbnail_url": c.thumbnail_url,
        "target_skill_id": c.target_skill_id,
        "lessons": [
            {
                "id": l.id,
                "course_id": l.course_id,
                "title": l.title,
                "content_type": l.content_type,
                "content_url": l.content_url,
                "duration_minutes": l.duration_minutes,
                "order_index": l.order_index,
            } for l in lessons
        ],
        "created_at": c.created_at,
    }


@router.get("/courses", response_model=List[CourseResponse])
async def list_courses(
    category: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List training courses."""
    courses = await LearningService.list_courses(db, current_user.tenant_id or "default", category=category)
    return [format_course_response(c) for c in courses]


@router.post("/courses", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(
    data: CourseCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("learning.course.manage")),
):
    """Create a new training course with lessons."""
    course = await LearningService.create_course(db, current_user.tenant_id or "default", data)
    return format_course_response(course)


@router.post("/enroll", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
async def enroll_course(
    data: EnrollmentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("learning.course.enroll")),
):
    """Enroll employee into a course."""
    enrollment = await LearningService.enroll(db, current_user.tenant_id or "default", data)
    return {
        "id": enrollment.id,
        "course_id": enrollment.course_id,
        "employee_id": enrollment.employee_id,
        "progress_percentage": enrollment.progress_percentage,
        "status": enrollment.status,
        "certificate_url": enrollment.certificate_url,
        "created_at": enrollment.created_at,
    }


@router.put("/enrollments/{enrollment_id}/progress", response_model=EnrollmentResponse)
async def update_course_progress(
    enrollment_id: str,
    progress: float = Query(..., ge=0.0, le=100.0),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Update progress percentage and award certificate on completion."""
    enrollment = await LearningService.update_progress(
        db, current_user.tenant_id or "default", enrollment_id, progress
    )
    return {
        "id": enrollment.id,
        "course_id": enrollment.course_id,
        "employee_id": enrollment.employee_id,
        "progress_percentage": enrollment.progress_percentage,
        "status": enrollment.status,
        "certificate_url": enrollment.certificate_url,
        "created_at": enrollment.created_at,
    }


@router.post("/certifications", response_model=CertificationResponse, status_code=status.HTTP_201_CREATED)
async def add_certification(
    data: CertificationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Record an official certification earned by an employee."""
    return await LearningService.add_certification(db, current_user.tenant_id or "default", data)
