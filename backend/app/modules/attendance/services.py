"""
Attendance Service
"""
from datetime import datetime, date, timezone
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc

from app.modules.attendance.models import AttendanceRecord, ShiftSchedule, AttendanceCorrectionRequest
from app.modules.attendance.schemas import ClockInRequest, ClockOutRequest, RegularizationRequestCreate
from app.core.exceptions import ValidationException, ResourceNotFoundException
from app.events.event_bus import event_bus, DomainEvent


class AttendanceService:
    @staticmethod
    async def clock_in(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        data: ClockInRequest,
        ip_address: Optional[str] = None
    ) -> AttendanceRecord:
        today = date.today()
        now = datetime.now(timezone.utc)

        # Check existing record today
        result = await db.execute(
            select(AttendanceRecord).where(
                AttendanceRecord.employee_id == employee_id,
                AttendanceRecord.work_date == today,
                AttendanceRecord.tenant_id == tenant_id,
                AttendanceRecord.is_deleted == False
            )
        )
        record = result.scalar_one_or_none()

        if record and record.clock_in_time:
            raise ValidationException("Employee is already clocked in for today")

        if not record:
            record = AttendanceRecord(
                tenant_id=tenant_id,
                employee_id=employee_id,
                work_date=today,
                clock_in_time=now,
                status="PRESENT",
                clock_in_ip=ip_address,
                clock_in_lat=data.latitude,
                clock_in_lng=data.longitude,
                notes=data.notes
            )
            db.add(record)
        else:
            record.clock_in_time = now
            record.clock_in_ip = ip_address
            record.clock_in_lat = data.latitude
            record.clock_in_lng = data.longitude
            record.notes = data.notes

        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="attendance.clock_in",
            tenant_id=tenant_id,
            actor_id=employee_id,
            payload={"employee_id": employee_id, "work_date": str(today), "clock_in": str(now)}
        ))

        return record

    @staticmethod
    async def clock_out(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        data: ClockOutRequest,
        ip_address: Optional[str] = None
    ) -> AttendanceRecord:
        today = date.today()
        now = datetime.now(timezone.utc)

        result = await db.execute(
            select(AttendanceRecord).where(
                AttendanceRecord.employee_id == employee_id,
                AttendanceRecord.work_date == today,
                AttendanceRecord.tenant_id == tenant_id,
                AttendanceRecord.is_deleted == False
            )
        )
        record = result.scalar_one_or_none()
        if not record or not record.clock_in_time:
            raise ValidationException("Cannot clock out without prior clock-in today")

        record.clock_out_time = now
        record.clock_out_ip = ip_address
        if data.notes:
            record.notes = f"{record.notes or ''} | Out: {data.notes}".strip()

        # Calculate duration
        clock_in = record.clock_in_time
        if clock_in.tzinfo is None:
            clock_in = clock_in.replace(tzinfo=timezone.utc)
        diff = now - clock_in
        total_hrs = round(diff.total_seconds() / 3600.0, 2)
        record.total_hours = total_hrs

        if total_hrs >= 9.0:
            record.overtime_hours = round(total_hrs - 8.0, 2)
        elif total_hrs < 4.0:
            record.status = "HALF_DAY"

        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="attendance.clock_out",
            tenant_id=tenant_id,
            actor_id=employee_id,
            payload={"employee_id": employee_id, "work_date": str(today), "total_hours": total_hrs}
        ))

        return record

    @staticmethod
    async def get_today_status(db: AsyncSession, tenant_id: str, employee_id: str) -> Optional[AttendanceRecord]:
        today = date.today()
        result = await db.execute(
            select(AttendanceRecord).where(
                AttendanceRecord.employee_id == employee_id,
                AttendanceRecord.work_date == today,
                AttendanceRecord.tenant_id == tenant_id,
                AttendanceRecord.is_deleted == False
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def list_records(
        db: AsyncSession,
        tenant_id: str,
        employee_id: Optional[str] = None,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> List[AttendanceRecord]:
        query = select(AttendanceRecord).where(
            AttendanceRecord.tenant_id == tenant_id,
            AttendanceRecord.is_deleted == False
        )
        if employee_id:
            query = query.where(AttendanceRecord.employee_id == employee_id)
        if from_date:
            query = query.where(AttendanceRecord.work_date >= from_date)
        if to_date:
            query = query.where(AttendanceRecord.work_date <= to_date)

        query = query.order_by(desc(AttendanceRecord.work_date)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())
