"""
Analytics API Endpoints
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.analytics.schemas import WorkforceAnalyticsOverview
from app.modules.analytics.services import AnalyticsService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/analytics", tags=["Workforce Analytics"])


@router.get("/overview", response_model=WorkforceAnalyticsOverview)
async def get_workforce_overview(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("analytics.dashboard.view")),
):
    """Retrieve top-level executive workforce analytics and operational KPIs."""
    return await AnalyticsService.get_overview_analytics(db, current_user.tenant_id or "default")
