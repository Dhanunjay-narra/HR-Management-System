"""
Learning Management Service
"""
from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.learning.models import Course, Lesson, CourseEnrollment, Certification
from app.modules.learning.schemas import CourseCreate, EnrollmentCreate, CertificationCreate
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class LearningService:
    @staticmethod
    async def create_course(db: AsyncSession, tenant_id: str, data: CourseCreate) -> Course:
        res = await db.execute(
            select(Course).where(Course.code == data.code, Course.tenant_id == tenant_id, Course.is_deleted == False)
        )
        if res.scalar_one_or_none():
            raise DuplicateResourceException("Course", "code", data.code)

        lessons = data.lessons
        course_data = data.model_dump(exclude={"lessons"})
        course = Course(tenant_id=tenant_id, **course_data)
        db.add(course)
        await db.flush()

        for les in lessons:
            lesson_item = Lesson(tenant_id=tenant_id, course_id=course.id, **les.model_dump())
            db.add(lesson_item)
        await db.flush()
        return course

    @staticmethod
    async def list_courses(db: AsyncSession, tenant_id: str, category: Optional[str] = None) -> List[Course]:
        query = (
            select(Course)
            .options(selectinload(Course.lessons))
            .where(Course.tenant_id == tenant_id, Course.is_deleted == False)
        )
        if category:
            query = query.where(Course.category == category)
        query = query.order_by(Course.title)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def enroll(db: AsyncSession, tenant_id: str, data: EnrollmentCreate) -> CourseEnrollment:
        res = await db.execute(
            select(CourseEnrollment).where(
                CourseEnrollment.course_id == data.course_id,
                CourseEnrollment.employee_id == data.employee_id,
                CourseEnrollment.tenant_id == tenant_id,
                CourseEnrollment.is_deleted == False
            )
        )
        existing = res.scalar_one_or_none()
        if existing:
            return existing

        enrollment = CourseEnrollment(tenant_id=tenant_id, **data.model_dump(), status="ENROLLED", progress_percentage=0.0)
        db.add(enrollment)
        await db.flush()
        return enrollment

    @staticmethod
    async def update_progress(
        db: AsyncSession,
        tenant_id: str,
        enrollment_id: str,
        progress: float
    ) -> CourseEnrollment:
        res = await db.execute(
            select(CourseEnrollment)
            .options(selectinload(CourseEnrollment.course))
            .where(
                CourseEnrollment.id == enrollment_id,
                CourseEnrollment.tenant_id == tenant_id,
                CourseEnrollment.is_deleted == False
            )
        )
        en = res.scalar_one_or_none()
        if not en:
            raise ResourceNotFoundException("CourseEnrollment", enrollment_id)

        en.progress_percentage = min(100.0, max(0.0, progress))
        if en.progress_percentage >= 100.0:
            en.status = "COMPLETED"
            en.completed_at = datetime.now(timezone.utc)
            en.certificate_url = f"/certificates/{en.id}.pdf"

            # Record timeline event
            course_title = en.course.title if en.course else "Course"
            db.add(EmployeeTimelineEvent(
                tenant_id=tenant_id,
                employee_id=en.employee_id,
                event_type="TRAINING_COMPLETED",
                title=f"Training Completed: {course_title}",
                description=f"Successfully completed {course_title} with verified certificate.",
                entity_type="Course",
                entity_id=en.course_id
            ))
        else:
            en.status = "IN_PROGRESS"

        await db.flush()
        return en

    @staticmethod
    async def add_certification(db: AsyncSession, tenant_id: str, data: CertificationCreate) -> Certification:
        cert = Certification(tenant_id=tenant_id, **data.model_dump())
        db.add(cert)
        await db.flush()

        db.add(EmployeeTimelineEvent(
            tenant_id=tenant_id,
            employee_id=cert.employee_id,
            event_type="CERTIFICATION_EARNED",
            title=f"Certification Earned: {cert.name}",
            description=f"Issued by {cert.issuing_organization} on {cert.issue_date}.",
            entity_type="Certification",
            entity_id=cert.id
        ))
        await db.flush()
        return cert
