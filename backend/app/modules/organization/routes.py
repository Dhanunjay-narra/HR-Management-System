"""
Organization Structure API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.organization.schemas import (
    OrganizationCreate, OrganizationResponse, DepartmentCreate, DepartmentResponse,
    BranchCreate, BranchResponse, DesignationCreate, DesignationResponse, OrgChartNode
)
from app.modules.organization.services import OrganizationService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/organization", tags=["Organization Structure"])


@router.get("", response_model=Optional[OrganizationResponse])
async def get_organization_profile(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Retrieve tenant organization metadata."""
    return await OrganizationService.get_organization(db, current_user.tenant_id or "default")


@router.post("", response_model=OrganizationResponse, status_code=status.HTTP_201_CREATED)
async def create_or_update_organization(
    data: OrganizationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("org.structure.manage")),
):
    """Create or configure organization profile."""
    return await OrganizationService.create_organization(db, current_user.tenant_id or "default", data)


@router.get("/departments", response_model=List[DepartmentResponse])
async def list_departments(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List departments in the organization."""
    return await OrganizationService.list_departments(db, current_user.tenant_id or "default")


@router.post("/departments", response_model=DepartmentResponse, status_code=status.HTTP_201_CREATED)
async def create_department(
    data: DepartmentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("dept.manage")),
):
    """Create a new department."""
    return await OrganizationService.create_department(db, current_user.tenant_id or "default", data)


@router.get("/branches", response_model=List[BranchResponse])
async def list_branches(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List office branches."""
    return await OrganizationService.list_branches(db, current_user.tenant_id or "default")


@router.post("/branches", response_model=BranchResponse, status_code=status.HTTP_201_CREATED)
async def create_branch(
    data: BranchCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("org.structure.manage")),
):
    """Create a new office branch."""
    return await OrganizationService.create_branch(db, current_user.tenant_id or "default", data)


@router.get("/designations", response_model=List[DesignationResponse])
async def list_designations(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List job designations."""
    return await OrganizationService.list_designations(db, current_user.tenant_id or "default")


@router.post("/designations", response_model=DesignationResponse, status_code=status.HTTP_201_CREATED)
async def create_designation(
    data: DesignationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("position.manage")),
):
    """Create a job designation."""
    return await OrganizationService.create_designation(db, current_user.tenant_id or "default", data)


@router.get("/chart", response_model=List[OrgChartNode])
async def get_org_chart(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("org.chart.view")),
):
    """Retrieve organization hierarchy tree structure."""
    return await OrganizationService.get_org_chart(db, current_user.tenant_id or "default")
