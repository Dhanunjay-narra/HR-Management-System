"""
Skills Intelligence Service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, delete
from sqlalchemy.orm import selectinload

from app.modules.skills.models import SkillCatalog, EmployeeSkill, JobSkillRequirement
from app.modules.skills.schemas import (
    SkillCatalogCreate, EmployeeSkillUpsert, JobSkillRequirementCreate,
    SkillGapAnalysisResponse, SkillGapItem
)
from app.modules.employees.models import Employee
from app.modules.learning.models import Course
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException


class SkillsService:
    @staticmethod
    async def create_skill(db: AsyncSession, tenant_id: str, data: SkillCatalogCreate) -> SkillCatalog:
        res = await db.execute(
            select(SkillCatalog).where(
                SkillCatalog.code == data.code,
                SkillCatalog.tenant_id == tenant_id,
                SkillCatalog.is_deleted == False
            )
        )
        if res.scalar_one_or_none():
            raise DuplicateResourceException("SkillCatalog", "code", data.code)

        skill = SkillCatalog(tenant_id=tenant_id, **data.model_dump())
        db.add(skill)
        await db.flush()
        return skill

    @staticmethod
    async def list_skills(db: AsyncSession, tenant_id: str) -> List[SkillCatalog]:
        result = await db.execute(
            select(SkillCatalog).where(SkillCatalog.tenant_id == tenant_id, SkillCatalog.is_deleted == False)
        )
        return list(result.scalars().all())

    @staticmethod
    async def upsert_employee_skills(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        data: EmployeeSkillUpsert
    ) -> List[EmployeeSkill]:
        # Delete existing and re-insert or update
        await db.execute(
            delete(EmployeeSkill).where(
                EmployeeSkill.employee_id == employee_id,
                EmployeeSkill.tenant_id == tenant_id
            )
        )
        created_skills = []
        for item in data.skills:
            es = EmployeeSkill(
                tenant_id=tenant_id,
                employee_id=employee_id,
                skill_id=item.skill_id,
                proficiency_level=item.proficiency_level,
                years_of_experience=item.years_of_experience,
                is_verified=item.is_verified
            )
            db.add(es)
            created_skills.append(es)
        await db.flush()
        return created_skills

    @staticmethod
    async def set_job_requirement(db: AsyncSession, tenant_id: str, data: JobSkillRequirementCreate) -> JobSkillRequirement:
        req = JobSkillRequirement(tenant_id=tenant_id, **data.model_dump())
        db.add(req)
        await db.flush()
        return req

    @staticmethod
    async def run_skill_gap_analysis(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str
    ) -> SkillGapAnalysisResponse:
        """
        Calculates organizational skill gaps by contrasting employee proficiency with role requirements.
        """
        # 1. Load employee
        res_emp = await db.execute(
            select(Employee)
            .options(selectinload(Employee.designation))
            .where(Employee.id == employee_id, Employee.tenant_id == tenant_id, Employee.is_deleted == False)
        )
        emp = res_emp.scalar_one_or_none()
        if not emp:
            raise ResourceNotFoundException("Employee", employee_id)

        # 2. Load employee current skills
        res_skills = await db.execute(
            select(EmployeeSkill)
            .options(selectinload(EmployeeSkill.skill))
            .where(EmployeeSkill.employee_id == employee_id, EmployeeSkill.tenant_id == tenant_id)
        )
        emp_skills_map = {es.skill_id: es for es in res_skills.scalars().all()}

        # 3. Load role requirements
        reqs = []
        if emp.designation_id:
            res_reqs = await db.execute(
                select(JobSkillRequirement)
                .options(selectinload(JobSkillRequirement.skill))
                .where(
                    JobSkillRequirement.designation_id == emp.designation_id,
                    JobSkillRequirement.tenant_id == tenant_id
                )
            )
            reqs = list(res_reqs.scalars().all())

        # If no explicit requirements, evaluate against all existing skills
        gap_matrix: List[SkillGapItem] = []
        met_count = 0
        total_assessed = len(reqs) if reqs else len(emp_skills_map)

        for req in reqs:
            sk = req.skill
            current_lvl = emp_skills_map[req.skill_id].proficiency_level if req.skill_id in emp_skills_map else 0
            gap = max(0, req.required_proficiency_level - current_lvl)
            is_met = current_lvl >= req.required_proficiency_level

            if is_met:
                met_count += 1

            # Check recommended learning course if gap exists
            rec_course = None
            if not is_met:
                res_course = await db.execute(
                    select(Course).where(
                        Course.target_skill_id == req.skill_id,
                        Course.tenant_id == tenant_id,
                        Course.is_deleted == False
                    )
                )
                c = res_course.scalars().first()
                if c:
                    rec_course = {"id": c.id, "title": c.title, "duration_hours": c.duration_hours}

            gap_matrix.append(SkillGapItem(
                skill_id=req.skill_id,
                skill_name=sk.name if sk else "Unknown",
                category=sk.category if sk else "TECHNICAL",
                current_proficiency=current_lvl,
                required_proficiency=req.required_proficiency_level,
                gap_level=gap,
                is_met=is_met,
                recommended_course=rec_course
            ))

        readiness = round((met_count / total_assessed) * 100.0, 1) if total_assessed > 0 else 100.0

        return SkillGapAnalysisResponse(
            employee_id=emp.id,
            employee_name=emp.full_name,
            designation_id=emp.designation_id,
            designation_title=emp.designation.title if emp.designation else None,
            overall_readiness_score=readiness,
            skills_assessed_count=total_assessed,
            skills_met_count=met_count,
            skills_gap_count=total_assessed - met_count,
            gap_matrix=gap_matrix
        )
