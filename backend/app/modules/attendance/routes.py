"""
Attendance API Endpoints
"""
from typing import List, Optional
from datetime import date
from fastapi import APIRouter, Depends, Request, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.attendance.schemas import (
    ClockInRequest, ClockOutRequest, AttendanceRecordResponse, ShiftScheduleCreate, ShiftScheduleResponse
)
from app.modules.attendance.services import AttendanceService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/attendance", tags=["Attendance Management"])


@router.post("/clock-in", response_model=AttendanceRecordResponse)
async def clock_in(
    data: ClockInRequest,
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Clock in for the day with optional GPS coordinates."""
    ip = request.client.host if request.client else None
    return await AttendanceService.clock_in(
        db,
        tenant_id=current_user.tenant_id or "default",
        employee_id=current_user.id,
        data=data,
        ip_address=ip
    )


@router.post("/clock-out", response_model=AttendanceRecordResponse)
async def clock_out(
    data: ClockOutRequest,
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Clock out and finalize working hours."""
    ip = request.client.host if request.client else None
    return await AttendanceService.clock_out(
        db,
        tenant_id=current_user.tenant_id or "default",
        employee_id=current_user.id,
        data=data,
        ip_address=ip
    )


@router.get("/today", response_model=Optional[AttendanceRecordResponse])
async def get_today_status(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """Check current clock-in state for today."""
    return await AttendanceService.get_today_status(
        db,
        tenant_id=current_user.tenant_id or "default",
        employee_id=current_user.id
    )


@router.get("/records", response_model=List[AttendanceRecordResponse])
async def list_attendance_records(
    employee_id: Optional[str] = Query(None),
    from_date: Optional[date] = Query(None),
    to_date: Optional[date] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("attendance.view_own")),
):
    """List attendance records."""
    # Non-admins can only view their own records
    target_emp_id = employee_id if current_user.is_superuser or "attendance.manage" in current_user.permissions else current_user.id
    return await AttendanceService.list_records(
        db,
        tenant_id=current_user.tenant_id or "default",
        employee_id=target_emp_id,
        from_date=from_date,
        to_date=to_date,
        skip=skip,
        limit=limit
    )
