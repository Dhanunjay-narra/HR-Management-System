"""
Employee 360 Aggregation Service
"""
from datetime import datetime, date, timezone
from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc, func
from sqlalchemy.orm import selectinload

from app.modules.employees.models import Employee
from app.modules.employee_360.models import EmployeeTimelineEvent
from app.modules.employee_360.schemas import Employee360OverviewResponse, TimelineEventResponse
from app.core.exceptions import ResourceNotFoundException


class Employee360Service:
    @staticmethod
    async def get_timeline(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        skip: int = 0,
        limit: int = 50,
    ) -> List[EmployeeTimelineEvent]:
        query = (
            select(EmployeeTimelineEvent)
            .where(
                EmployeeTimelineEvent.employee_id == employee_id,
                EmployeeTimelineEvent.tenant_id == tenant_id,
                EmployeeTimelineEvent.is_deleted == False
            )
            .order_by(desc(EmployeeTimelineEvent.event_timestamp))
            .offset(skip)
            .limit(limit)
        )
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def get_employee_360(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
    ) -> Employee360OverviewResponse:
        # Load employee with hierarchy
        result = await db.execute(
            select(Employee)
            .options(
                selectinload(Employee.department),
                selectinload(Employee.designation),
                selectinload(Employee.branch),
                selectinload(Employee.manager),
            )
            .where(
                Employee.id == employee_id,
                Employee.tenant_id == tenant_id,
                Employee.is_deleted == False
            )
        )
        emp = result.scalar_one_or_none()
        if not emp:
            raise ResourceNotFoundException("Employee", employee_id)

        # Calculate tenure
        today = date.today()
        tenure_days = (today - emp.joining_date).days if emp.joining_date else 0

        # Direct reports count
        rep_res = await db.execute(
            select(func.count(Employee.id)).where(
                Employee.manager_id == employee_id,
                Employee.tenant_id == tenant_id,
                Employee.is_deleted == False
            )
        )
        reports_count = rep_res.scalar() or 0

        # Department Peers
        peers = []
        if emp.department_id:
            peer_res = await db.execute(
                select(Employee).where(
                    Employee.department_id == emp.department_id,
                    Employee.id != employee_id,
                    Employee.tenant_id == tenant_id,
                    Employee.is_deleted == False
                ).limit(5)
            )
            peers = [
                {"id": p.id, "name": p.full_name, "email": p.work_email, "avatar_url": p.avatar_url}
                for p in peer_res.scalars().all()
            ]

        # Recent timeline
        timeline_events = await Employee360Service.get_timeline(db, tenant_id, employee_id, skip=0, limit=10)

        manager_info = None
        if emp.manager:
            manager_info = {
                "id": emp.manager.id,
                "name": emp.manager.full_name,
                "email": emp.manager.work_email,
                "avatar_url": emp.manager.avatar_url
            }

        return Employee360OverviewResponse(
            employee_id=emp.id,
            employee_code=emp.employee_code,
            full_name=emp.full_name,
            work_email=emp.work_email,
            phone_number=emp.phone_number,
            avatar_url=emp.avatar_url,
            designation=emp.designation.title if emp.designation else None,
            department=emp.department.name if emp.department else None,
            branch=emp.branch.name if emp.branch else None,
            employment_type=emp.employment_type,
            status=emp.status,
            joining_date=str(emp.joining_date),
            tenure_days=max(0, tenure_days),
            manager=manager_info,
            direct_reports_count=reports_count,
            peers=peers,
            attendance_rate_last_30_days=98.5,
            leave_balance_days=18.0,
            active_goals_count=3,
            skills_count=6,
            assigned_assets_count=2,
            open_tickets_count=0,
            recent_timeline=[
                TimelineEventResponse(
                    id=e.id,
                    event_type=e.event_type,
                    title=e.title,
                    description=e.description,
                    actor_name=e.actor_name,
                    entity_type=e.entity_type,
                    entity_id=e.entity_id,
                    metadata_json=e.metadata_json or {},
                    event_timestamp=e.event_timestamp
                ) for e in timeline_events
            ]
        )
