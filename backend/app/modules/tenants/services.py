"""
Tenant Service
"""
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.modules.tenants.models import Tenant
from app.modules.tenants.schemas import TenantCreate, TenantUpdate
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException


class TenantService:
    @staticmethod
    async def get_by_id(db: AsyncSession, tenant_id: str) -> Tenant:
        result = await db.execute(select(Tenant).where(Tenant.id == tenant_id, Tenant.is_deleted == False))
        tenant = result.scalar_one_or_none()
        if not tenant:
            raise ResourceNotFoundException("Tenant", tenant_id)
        return tenant

    @staticmethod
    async def get_by_slug(db: AsyncSession, slug: str) -> Optional[Tenant]:
        result = await db.execute(select(Tenant).where(Tenant.slug == slug, Tenant.is_deleted == False))
        return result.scalar_one_or_none()

    @staticmethod
    async def list_tenants(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Tenant]:
        result = await db.execute(select(Tenant).where(Tenant.is_deleted == False).offset(skip).limit(limit))
        return list(result.scalars().all())

    @staticmethod
    async def create_tenant(db: AsyncSession, data: TenantCreate) -> Tenant:
        existing = await TenantService.get_by_slug(db, data.slug)
        if existing:
            raise DuplicateResourceException("Tenant", "slug", data.slug)
        
        tenant = Tenant(**data.model_dump())
        db.add(tenant)
        await db.flush()
        return tenant

    @staticmethod
    async def update_tenant(db: AsyncSession, tenant_id: str, data: TenantUpdate) -> Tenant:
        tenant = await TenantService.get_by_id(db, tenant_id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(tenant, key, value)
        await db.flush()
        return tenant
