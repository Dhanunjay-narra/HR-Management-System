"""
Skills Intelligence API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.skills.schemas import (
    SkillCatalogCreate, SkillCatalogResponse, EmployeeSkillUpsert,
    JobSkillRequirementCreate, SkillGapAnalysisResponse
)
from app.modules.skills.services import SkillsService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/skills", tags=["Skills Intelligence"])


@router.get("/catalog", response_model=List[SkillCatalogResponse])
async def list_skills_catalog(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List organizational skills taxonomy."""
    return await SkillsService.list_skills(db, current_user.tenant_id or "default")


@router.post("/catalog", response_model=SkillCatalogResponse, status_code=status.HTTP_201_CREATED)
async def create_skill(
    data: SkillCatalogCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("skills.manage")),
):
    """Add a new skill to the taxonomy catalog."""
    return await SkillsService.create_skill(db, current_user.tenant_id or "default", data)


@router.post("/employee/{employee_id}", status_code=status.HTTP_200_OK)
async def upsert_employee_skills(
    employee_id: str,
    data: EmployeeSkillUpsert,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("skills.manage")),
):
    """Update employee skill proficiency profile."""
    await SkillsService.upsert_employee_skills(
        db, current_user.tenant_id or "default", employee_id, data
    )
    return {"success": True, "message": "Employee skills updated successfully."}


@router.post("/requirements", status_code=status.HTTP_201_CREATED)
async def create_job_requirement(
    data: JobSkillRequirementCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("skills.manage")),
):
    """Set required skill level for a job designation."""
    req = await SkillsService.set_job_requirement(db, current_user.tenant_id or "default", data)
    return {"success": True, "id": req.id}


@router.get("/employee/{employee_id}/gap-analysis", response_model=SkillGapAnalysisResponse)
async def get_employee_skill_gap(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("skills.gap_analysis")),
):
    """Run automated skill gap analysis contrasting employee capabilities with job requirements."""
    return await SkillsService.run_skill_gap_analysis(
        db, current_user.tenant_id or "default", employee_id
    )
