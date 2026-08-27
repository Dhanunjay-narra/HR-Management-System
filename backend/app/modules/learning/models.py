"""
Learning Management System (LMS) & Certification Models
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Float, Boolean, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class Course(TenantBaseModel):
    """LMS Course."""
    __tablename__ = "courses"

    title = Column(String(255), nullable=False, index=True)
    code = Column(String(50), nullable=False, unique=True, index=True)
    category = Column(String(100), default="ENGINEERING", nullable=False)
    description = Column(Text, nullable=False)
    duration_hours = Column(Float, default=10.0, nullable=False)
    level = Column(String(50), default="INTERMEDIATE", nullable=False)  # BEGINNER, INTERMEDIATE, ADVANCED
    provider = Column(String(100), default="Internal", nullable=False)
    thumbnail_url = Column(String(500), nullable=True)
    target_skill_id = Column(String(36), ForeignKey("skills_catalog.id", ondelete="SET NULL"), nullable=True, index=True)

    # Relationships
    target_skill = relationship("SkillCatalog")
    lessons = relationship("Lesson", back_populates="course", cascade="all, delete-orphan")
    enrollments = relationship("CourseEnrollment", back_populates="course", cascade="all, delete-orphan")


class Lesson(TenantBaseModel):
    """Course Lesson."""
    __tablename__ = "lessons"

    course_id = Column(String(36), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    content_type = Column(String(50), default="VIDEO", nullable=False)  # VIDEO, ARTICLE, QUIZ, LAB
    content_url = Column(String(500), nullable=True)
    duration_minutes = Column(Integer, default=20, nullable=False)
    order_index = Column(Integer, default=1, nullable=False)

    # Relationships
    course = relationship("Course", back_populates="lessons")


class CourseEnrollment(TenantBaseModel):
    """Employee Enrollment & Progress in Course."""
    __tablename__ = "course_enrollments"

    course_id = Column(String(36), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    progress_percentage = Column(Float, default=0.0, nullable=False)
    status = Column(String(50), default="ENROLLED", nullable=False)  # ENROLLED, IN_PROGRESS, COMPLETED
    certificate_url = Column(String(500), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    course = relationship("Course", back_populates="enrollments")
    employee = relationship("Employee")


class Certification(TenantBaseModel):
    """Professional Certifications earned by employees."""
    __tablename__ = "certifications"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(255), nullable=False)  # e.g., AWS Certified Solutions Architect
    issuing_organization = Column(String(255), nullable=False)
    issue_date = Column(Date, nullable=False)
    expiry_date = Column(Date, nullable=True)
    credential_id = Column(String(100), nullable=True)
    credential_url = Column(String(500), nullable=True)

    # Relationships
    employee = relationship("Employee")
