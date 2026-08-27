"""
Skills Intelligence Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class SkillCatalogBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    code: str = Field(..., min_length=1, max_length=50)
    category: str = "TECHNICAL"
    description: Optional[str] = None


class SkillCatalogCreate(SkillCatalogBase):
    pass


class SkillCatalogResponse(SkillCatalogBase):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class EmployeeSkillItem(BaseModel):
    skill_id: str
    skill_name: Optional[str] = None
    proficiency_level: int = Field(3, ge=1, le=5)
    years_of_experience: float = 1.0
    is_verified: bool = False


class EmployeeSkillUpsert(BaseModel):
    skills: List[EmployeeSkillItem]


class JobSkillRequirementCreate(BaseModel):
    designation_id: str
    skill_id: str
    required_proficiency_level: int = Field(4, ge=1, le=5)
    importance_weight: float = 1.0


class SkillGapItem(BaseModel):
    skill_id: str
    skill_name: str
    category: str
    current_proficiency: int
    required_proficiency: int
    gap_level: int  # required - current
    is_met: bool
    recommended_course: Optional[Dict[str, Any]] = None


class SkillGapAnalysisResponse(BaseModel):
    employee_id: str
    employee_name: str
    designation_id: Optional[str] = None
    designation_title: Optional[str] = None
    overall_readiness_score: float  # 0.0 - 100.0%
    skills_assessed_count: int
    skills_met_count: int
    skills_gap_count: int
    gap_matrix: List[SkillGapItem] = []
