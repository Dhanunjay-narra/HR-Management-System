"""
Asset Inventory Service
"""
from typing import List, Optional
from datetime import date, datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.assets.models import Asset, AssetAssignmentHistory
from app.modules.assets.schemas import AssetCreate, AssetAssignRequest
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class AssetService:
    @staticmethod
    async def create_asset(db: AsyncSession, tenant_id: str, data: AssetCreate) -> Asset:
        res = await db.execute(
            select(Asset).where(Asset.asset_tag == data.asset_tag, Asset.tenant_id == tenant_id, Asset.is_deleted == False)
        )
        if res.scalar_one_or_none():
            raise DuplicateResourceException("Asset", "asset_tag", data.asset_tag)

        asset = Asset(tenant_id=tenant_id, **data.model_dump())
        db.add(asset)
        await db.flush()
        return asset

    @staticmethod
    async def list_assets(
        db: AsyncSession,
        tenant_id: str,
        category: Optional[str] = None,
        status: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[Asset]:
        query = (
            select(Asset)
            .options(selectinload(Asset.current_employee))
            .where(Asset.tenant_id == tenant_id, Asset.is_deleted == False)
        )
        if category:
            query = query.where(Asset.category == category)
        if status:
            query = query.where(Asset.status == status)

        query = query.order_by(desc(Asset.created_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def assign_asset(
        db: AsyncSession,
        tenant_id: str,
        asset_id: str,
        actor_id: str,
        data: AssetAssignRequest
    ) -> Asset:
        res = await db.execute(
            select(Asset)
            .options(selectinload(Asset.current_employee))
            .where(Asset.id == asset_id, Asset.tenant_id == tenant_id, Asset.is_deleted == False)
        )
        asset = res.scalar_one_or_none()
        if not asset:
            raise ResourceNotFoundException("Asset", asset_id)

        asset.current_employee_id = data.employee_id
        asset.status = "ASSIGNED"

        history = AssetAssignmentHistory(
            tenant_id=tenant_id,
            asset_id=asset.id,
            employee_id=data.employee_id,
            assigned_date=date.today(),
            condition_at_assignment=data.condition,
            notes=data.notes
        )
        db.add(history)

        # Record timeline event
        db.add(EmployeeTimelineEvent(
            tenant_id=tenant_id,
            employee_id=data.employee_id,
            actor_id=actor_id,
            event_type="ASSET_ASSIGNED",
            title=f"Hardware Asset Assigned: {asset.name}",
            description=f"Assigned tag {asset.asset_tag} ({asset.category}).",
            entity_type="Asset",
            entity_id=asset.id
        ))

        await db.flush()
        return asset
