"""
Employee API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.employees.schemas import (
    EmployeeCreate, EmployeeUpdate, EmployeeResponse, EmergencyContactSchema
)
from app.modules.employees.services import EmployeeService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/employees", tags=["Employee Master"])


def format_employee_response(emp) -> dict:
    return {
        "id": emp.id,
        "tenant_id": emp.tenant_id,
        "user_id": emp.user_id,
        "employee_code": emp.employee_code,
        "first_name": emp.first_name,
        "last_name": emp.last_name,
        "full_name": emp.full_name,
        "work_email": emp.work_email,
        "personal_email": emp.personal_email,
        "phone_number": emp.phone_number,
        "date_of_birth": emp.date_of_birth,
        "gender": emp.gender,
        "marital_status": emp.marital_status,
        "avatar_url": emp.avatar_url,
        "bio": emp.bio,
        "joining_date": emp.joining_date,
        "probation_end_date": emp.probation_end_date,
        "employment_type": emp.employment_type,
        "status": emp.status,
        "department_id": emp.department_id,
        "team_id": emp.team_id,
        "designation_id": emp.designation_id,
        "branch_id": emp.branch_id,
        "work_location_id": emp.work_location_id,
        "job_grade_id": emp.job_grade_id,
        "manager_id": emp.manager_id,
        "department_name": emp.department.name if emp.department else None,
        "designation_title": emp.designation.title if emp.designation else None,
        "manager_name": emp.manager.full_name if emp.manager else None,
        "emergency_contacts": [c.to_dict() for c in emp.emergency_contacts] if hasattr(emp, "emergency_contacts") and emp.emergency_contacts else [],
        "employment_history": [h.to_dict() for h in emp.employment_history] if hasattr(emp, "employment_history") and emp.employment_history else [],
        "bank_details": emp.bank_details.to_dict() if hasattr(emp, "bank_details") and emp.bank_details else None,
        "created_at": emp.created_at,
        "updated_at": emp.updated_at,
    }


@router.get("", response_model=List[EmployeeResponse])
async def list_employees(
    department_id: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("employee.read")),
):
    """List employees with filters and search."""
    employees = await EmployeeService.list_employees(
        db,
        tenant_id=current_user.tenant_id or "default",
        department_id=department_id,
        status=status,
        search=search,
        skip=skip,
        limit=limit,
    )
    return [format_employee_response(e) for e in employees]


@router.post("", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
async def create_employee(
    data: EmployeeCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("employee.create")),
):
    """Create a new employee profile and auto-provision user access."""
    emp = await EmployeeService.create_employee(
        db,
        tenant_id=current_user.tenant_id or "default",
        data=data,
        actor_id=current_user.id
    )
    loaded_emp = await EmployeeService.get_by_id(db, current_user.tenant_id or "default", emp.id)
    return format_employee_response(loaded_emp)


@router.get("/{employee_id}", response_model=EmployeeResponse)
async def get_employee(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("employee.read")),
):
    """Retrieve full employee master record."""
    emp = await EmployeeService.get_by_id(db, current_user.tenant_id or "default", employee_id)
    return format_employee_response(emp)


@router.put("/{employee_id}", response_model=EmployeeResponse)
async def update_employee(
    employee_id: str,
    data: EmployeeUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("employee.update")),
):
    """Update employee information."""
    emp = await EmployeeService.update_employee(
        db,
        tenant_id=current_user.tenant_id or "default",
        employee_id=employee_id,
        data=data,
        actor_id=current_user.id
    )
    loaded_emp = await EmployeeService.get_by_id(db, current_user.tenant_id or "default", emp.id)
    return format_employee_response(loaded_emp)


@router.post("/{employee_id}/emergency-contacts", response_model=EmergencyContactSchema)
async def add_emergency_contact(
    employee_id: str,
    data: EmergencyContactSchema,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("employee.update")),
):
    """Add emergency contact for employee."""
    contact = await EmployeeService.add_emergency_contact(
        db,
        tenant_id=current_user.tenant_id or "default",
        employee_id=employee_id,
        data=data
    )
    return contact
