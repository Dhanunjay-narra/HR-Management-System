"""
Employee Pydantic Schemas
"""
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, EmailStr, ConfigDict, Field


class EmergencyContactSchema(BaseModel):
    id: Optional[str] = None
    name: str
    relationship: str
    phone_number: str
    alternative_phone: Optional[str] = None
    email: Optional[EmailStr] = None
    is_primary: bool = True

    model_config = ConfigDict(from_attributes=True)


class EmploymentHistorySchema(BaseModel):
    id: Optional[str] = None
    company_name: str
    designation: str
    start_date: date
    end_date: Optional[date] = None
    reason_for_leaving: Optional[str] = None
    last_drawn_salary: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)


class EmployeeBankDetailSchema(BaseModel):
    id: Optional[str] = None
    bank_name: str
    account_number: str
    routing_number: Optional[str] = None
    swift_code: Optional[str] = None
    account_type: str = "CHECKING"
    tax_identification_number: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class EmployeeBase(BaseModel):
    employee_code: str = Field(..., min_length=2, max_length=50)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    work_email: EmailStr
    personal_email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = "PreferNotToSay"
    marital_status: Optional[str] = "Single"
    avatar_url: Optional[str] = None
    bio: Optional[str] = None

    joining_date: date = Field(default_factory=date.today)
    probation_end_date: Optional[date] = None
    employment_type: str = "FULL_TIME"
    status: str = "ACTIVE"

    department_id: Optional[str] = None
    team_id: Optional[str] = None
    designation_id: Optional[str] = None
    branch_id: Optional[str] = None
    work_location_id: Optional[str] = None
    job_grade_id: Optional[str] = None
    manager_id: Optional[str] = None


class EmployeeCreate(EmployeeBase):
    create_user_account: bool = True
    user_role: Optional[str] = "employee"
    temporary_password: Optional[str] = "Welcome@Pulse2026!"


class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    personal_email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None

    probation_end_date: Optional[date] = None
    confirmation_date: Optional[date] = None
    exit_date: Optional[date] = None
    employment_type: Optional[str] = None
    status: Optional[str] = None

    department_id: Optional[str] = None
    team_id: Optional[str] = None
    designation_id: Optional[str] = None
    branch_id: Optional[str] = None
    work_location_id: Optional[str] = None
    job_grade_id: Optional[str] = None
    manager_id: Optional[str] = None


class EmployeeResponse(EmployeeBase):
    id: str
    tenant_id: str
    user_id: Optional[str] = None
    full_name: str
    created_at: datetime
    updated_at: datetime

    department_name: Optional[str] = None
    designation_title: Optional[str] = None
    manager_name: Optional[str] = None

    emergency_contacts: List[EmergencyContactSchema] = []
    employment_history: List[EmploymentHistorySchema] = []
    bank_details: Optional[EmployeeBankDetailSchema] = None

    model_config = ConfigDict(from_attributes=True)
