"""
Employee Service
"""
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload

from app.modules.employees.models import Employee, EmergencyContact, EmploymentHistory, EmployeeBankDetail
from app.modules.employees.schemas import EmployeeCreate, EmployeeUpdate, EmergencyContactSchema
from app.modules.auth.models import User
from app.core.security import get_password_hash
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class EmployeeService:
    @staticmethod
    async def get_by_id(db: AsyncSession, tenant_id: str, employee_id: str) -> Employee:
        result = await db.execute(
            select(Employee)
            .options(
                selectinload(Employee.emergency_contacts),
                selectinload(Employee.employment_history),
                selectinload(Employee.bank_details),
                selectinload(Employee.department),
                selectinload(Employee.designation),
                selectinload(Employee.manager),
            )
            .where(Employee.id == employee_id, Employee.tenant_id == tenant_id, Employee.is_deleted == False)
        )
        emp = result.scalar_one_or_none()
        if not emp:
            raise ResourceNotFoundException("Employee", employee_id)
        return emp

    @staticmethod
    async def get_by_code(db: AsyncSession, tenant_id: str, employee_code: str) -> Optional[Employee]:
        result = await db.execute(
            select(Employee).where(
                Employee.employee_code == employee_code,
                Employee.tenant_id == tenant_id,
                Employee.is_deleted == False
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def list_employees(
        db: AsyncSession,
        tenant_id: str,
        department_id: Optional[str] = None,
        status: Optional[str] = None,
        search: Optional[str] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Employee]:
        query = (
            select(Employee)
            .options(
                selectinload(Employee.department),
                selectinload(Employee.designation),
                selectinload(Employee.manager),
            )
            .where(Employee.tenant_id == tenant_id, Employee.is_deleted == False)
        )
        if department_id:
            query = query.where(Employee.department_id == department_id)
        if status:
            query = query.where(Employee.status == status)
        if search:
            s = f"%{search.lower()}%"
            query = query.where(
                or_(
                    Employee.first_name.ilike(s),
                    Employee.last_name.ilike(s),
                    Employee.work_email.ilike(s),
                    Employee.employee_code.ilike(s),
                )
            )

        query = query.order_by(Employee.first_name).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def create_employee(
        db: AsyncSession,
        tenant_id: str,
        data: EmployeeCreate,
        actor_id: Optional[str] = None,
    ) -> Employee:
        # Check duplicate code or email
        existing_code = await EmployeeService.get_by_code(db, tenant_id, data.employee_code)
        if existing_code:
            raise DuplicateResourceException("Employee", "employee_code", data.employee_code)

        user_id = None
        if data.create_user_account:
            # Check existing user
            res_user = await db.execute(select(User).where(User.email == data.work_email.lower(), User.is_deleted == False))
            user = res_user.scalar_one_or_none()
            if not user:
                user = User(
                    email=data.work_email.lower(),
                    hashed_password=get_password_hash(data.temporary_password or "Welcome@Pulse2026!"),
                    first_name=data.first_name,
                    last_name=data.last_name,
                    tenant_id=tenant_id,
                    role=data.user_role or "employee",
                    is_active=True,
                    is_verified=True,
                )
                db.add(user)
                await db.flush()
            user_id = user.id

        emp_dict = data.model_dump(exclude={"create_user_account", "user_role", "temporary_password"})
        emp = Employee(
            tenant_id=tenant_id,
            user_id=user_id,
            **emp_dict
        )
        db.add(emp)
        await db.flush()

        # Add initial timeline event
        timeline_event = EmployeeTimelineEvent(
            tenant_id=tenant_id,
            employee_id=emp.id,
            actor_id=actor_id,
            event_type="JOINED",
            title=f"Employee Joined the Organization",
            description=f"{emp.full_name} joined as {data.employment_type} on {emp.joining_date}.",
            metadata_json={"joining_date": str(emp.joining_date), "department_id": emp.department_id}
        )
        db.add(timeline_event)
        await db.flush()

        # Publish domain event
        await event_bus.publish(DomainEvent(
            event_type="employee.joined",
            tenant_id=tenant_id,
            actor_id=actor_id,
            payload={"employee_id": emp.id, "name": emp.full_name, "email": emp.work_email}
        ))

        return emp

    @staticmethod
    async def update_employee(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        data: EmployeeUpdate,
        actor_id: Optional[str] = None
    ) -> Employee:
        emp = await EmployeeService.get_by_id(db, tenant_id, employee_id)
        
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(emp, key, value)
        await db.flush()

        # Record timeline update
        db.add(EmployeeTimelineEvent(
            tenant_id=tenant_id,
            employee_id=emp.id,
            actor_id=actor_id,
            event_type="PROFILE_UPDATED",
            title="Employee Profile Updated",
            description=f"Profile fields updated.",
            metadata_json=data.model_dump(exclude_unset=True)
        ))
        await db.flush()

        return emp

    @staticmethod
    async def add_emergency_contact(
        db: AsyncSession,
        tenant_id: str,
        employee_id: str,
        data: EmergencyContactSchema
    ) -> EmergencyContact:
        emp = await EmployeeService.get_by_id(db, tenant_id, employee_id)
        contact = EmergencyContact(tenant_id=tenant_id, employee_id=emp.id, **data.model_dump(exclude={"id"}))
        db.add(contact)
        await db.flush()
        return contact
