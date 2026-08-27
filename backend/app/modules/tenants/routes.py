"""
Tenant API Endpoints
"""
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.tenants.schemas import TenantCreate, TenantUpdate, TenantResponse
from app.modules.tenants.services import TenantService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/tenants", tags=["Tenants"])


@router.get("", response_model=List[TenantResponse])
async def list_tenants(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("tenant.manage")),
):
    """List all registered platform tenants."""
    return await TenantService.list_tenants(db, skip, limit)


@router.post("", response_model=TenantResponse, status_code=status.HTTP_201_CREATED)
async def create_tenant(
    data: TenantCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("tenant.manage")),
):
    """Create a new tenant organization."""
    return await TenantService.create_tenant(db, data)


@router.get("/{tenant_id}", response_model=TenantResponse)
async def get_tenant(
    tenant_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Retrieve tenant details."""
    return await TenantService.get_by_id(db, tenant_id)


@router.put("/{tenant_id}", response_model=TenantResponse)
async def update_tenant(
    tenant_id: str,
    data: TenantUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("tenant.config.update")),
):
    """Update tenant configuration."""
    return await TenantService.update_tenant(db, tenant_id, data)
