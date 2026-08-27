"""
Skills Intelligence Models
Entities: SkillCatalog, EmployeeSkill, JobSkillRequirement
"""
from datetime import datetime
from sqlalchemy import Column, String, Float, Boolean, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class SkillCatalog(TenantBaseModel):
    """Centralized Organization Skills Taxonomy."""
    __tablename__ = "skills_catalog"

    name = Column(String(100), nullable=False, index=True)
    code = Column(String(50), nullable=False, unique=True, index=True)
    category = Column(String(50), default="TECHNICAL", nullable=False)  # TECHNICAL, LEADERSHIP, DOMAIN, COMPLIANCE
    description = Column(Text, nullable=True)

    # Relationships
    employee_skills = relationship("EmployeeSkill", back_populates="skill", cascade="all, delete-orphan")


class EmployeeSkill(TenantBaseModel):
    """Skill proficiency profile of an individual employee."""
    __tablename__ = "employee_skills"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_id = Column(String(36), ForeignKey("skills_catalog.id", ondelete="CASCADE"), nullable=False, index=True)
    proficiency_level = Column(Integer, default=3, nullable=False)  # 1: Novice, 2: Beginner, 3: Intermediate, 4: Advanced, 5: Expert
    years_of_experience = Column(Float, default=1.0, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    verified_by_user_id = Column(String(36), nullable=True)

    # Relationships
    skill = relationship("SkillCatalog", back_populates="employee_skills")
    employee = relationship("Employee")


class JobSkillRequirement(TenantBaseModel):
    """Target skill matrix required for a job designation / role."""
    __tablename__ = "job_skill_requirements"

    designation_id = Column(String(36), ForeignKey("designations.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_id = Column(String(36), ForeignKey("skills_catalog.id", ondelete="CASCADE"), nullable=False, index=True)
    required_proficiency_level = Column(Integer, default=4, nullable=False)  # 1 to 5
    importance_weight = Column(Float, default=1.0, nullable=False)  # 1.0 - 2.0 multiplier

    # Relationships
    skill = relationship("SkillCatalog")
    designation = relationship("Designation")
