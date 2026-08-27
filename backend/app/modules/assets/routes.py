"""
Asset API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.assets.schemas import AssetCreate, AssetResponse, AssetAssignRequest
from app.modules.assets.services import AssetService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/assets", tags=["Asset Inventory"])


def format_asset_response(a) -> dict:
    emp = a.__dict__.get("current_employee")
    return {
        "id": a.id,
        "tenant_id": a.tenant_id,
        "asset_tag": a.asset_tag,
        "name": a.name,
        "category": a.category,
        "serial_number": a.serial_number,
        "model_number": a.model_number,
        "purchase_date": a.purchase_date,
        "purchase_cost": a.purchase_cost,
        "status": a.status,
        "current_employee_id": a.current_employee_id,
        "current_employee_name": emp.full_name if emp else None,
        "created_at": a.created_at,
    }


@router.get("", response_model=List[AssetResponse])
async def list_assets(
    category: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List IT assets."""
    assets = await AssetService.list_assets(
        db, current_user.tenant_id or "default", category=category, status=status, skip=skip, limit=limit
    )
    return [format_asset_response(a) for a in assets]


@router.post("", response_model=AssetResponse, status_code=status.HTTP_201_CREATED)
async def create_asset(
    data: AssetCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("asset.manage")),
):
    """Register a new company asset."""
    asset = await AssetService.create_asset(db, current_user.tenant_id or "default", data)
    return format_asset_response(asset)


@router.post("/{asset_id}/assign", response_model=AssetResponse)
async def assign_asset(
    asset_id: str,
    data: AssetAssignRequest,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("asset.manage")),
):
    """Allocate custody of an asset to an employee."""
    asset = await AssetService.assign_asset(
        db, current_user.tenant_id or "default", asset_id, current_user.id, data
    )
    return format_asset_response(asset)
