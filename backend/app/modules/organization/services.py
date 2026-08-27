"""
Organization Service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.modules.organization.models import Organization, Branch, Department, Team, Designation, JobGrade, WorkLocation
from app.modules.organization.schemas import (
    OrganizationCreate, DepartmentCreate, BranchCreate, DesignationCreate, OrgChartNode
)
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException


class OrganizationService:
    @staticmethod
    async def create_organization(db: AsyncSession, tenant_id: str, data: OrganizationCreate) -> Organization:
        org = Organization(tenant_id=tenant_id, **data.model_dump())
        db.add(org)
        await db.flush()
        result = await db.execute(
            select(Organization)
            .options(selectinload(Organization.branches), selectinload(Organization.departments))
            .where(Organization.id == org.id)
        )
        return result.scalar_one()

    @staticmethod
    async def get_organization(db: AsyncSession, tenant_id: str) -> Optional[Organization]:
        result = await db.execute(
            select(Organization)
            .options(selectinload(Organization.branches), selectinload(Organization.departments))
            .where(Organization.tenant_id == tenant_id, Organization.is_deleted == False)
            .order_by(Organization.created_at.desc())
        )
        return result.scalars().first()

    @staticmethod
    async def create_department(db: AsyncSession, tenant_id: str, data: DepartmentCreate) -> Department:
        dept = Department(tenant_id=tenant_id, **data.model_dump())
        db.add(dept)
        await db.flush()
        return dept

    @staticmethod
    async def list_departments(db: AsyncSession, tenant_id: str) -> List[Department]:
        result = await db.execute(
            select(Department)
            .where(Department.tenant_id == tenant_id, Department.is_deleted == False)
            .order_by(Department.name)
        )
        return list(result.scalars().all())

    @staticmethod
    async def create_branch(db: AsyncSession, tenant_id: str, data: BranchCreate) -> Branch:
        branch = Branch(tenant_id=tenant_id, **data.model_dump())
        db.add(branch)
        await db.flush()
        return branch

    @staticmethod
    async def list_branches(db: AsyncSession, tenant_id: str) -> List[Branch]:
        result = await db.execute(
            select(Branch).where(Branch.tenant_id == tenant_id, Branch.is_deleted == False)
        )
        return list(result.scalars().all())

    @staticmethod
    async def create_designation(db: AsyncSession, tenant_id: str, data: DesignationCreate) -> Designation:
        designation = Designation(tenant_id=tenant_id, **data.model_dump())
        db.add(designation)
        await db.flush()
        return designation

    @staticmethod
    async def list_designations(db: AsyncSession, tenant_id: str) -> List[Designation]:
        result = await db.execute(
            select(Designation).where(Designation.tenant_id == tenant_id, Designation.is_deleted == False)
        )
        return list(result.scalars().all())

    @staticmethod
    async def get_org_chart(db: AsyncSession, tenant_id: str) -> List[OrgChartNode]:
        """Build hierarchical organization tree."""
        result = await db.execute(
            select(Department).where(Department.tenant_id == tenant_id, Department.is_deleted == False)
        )
        departments = list(result.scalars().all())
        dept_map = {
            d.id: OrgChartNode(
                id=d.id,
                name=d.name,
                code=d.code,
                manager_id=d.manager_id,
                sub_departments=[]
            ) for d in departments
        }

        root_nodes: List[OrgChartNode] = []
        for d in departments:
            node = dept_map[d.id]
            if d.parent_department_id and d.parent_department_id in dept_map:
                dept_map[d.parent_department_id].sub_departments.append(node)
            else:
                root_nodes.append(node)
        return root_nodes
