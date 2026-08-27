"""
Organization Schemas
"""
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


# Department Schemas
class DepartmentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    code: str = Field(..., min_length=1, max_length=50)
    organization_id: str
    branch_id: Optional[str] = None
    parent_department_id: Optional[str] = None
    cost_center: Optional[str] = None
    manager_id: Optional[str] = None


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    branch_id: Optional[str] = None
    parent_department_id: Optional[str] = None
    cost_center: Optional[str] = None
    manager_id: Optional[str] = None


class DepartmentResponse(DepartmentBase):
    id: str
    tenant_id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Branch Schemas
class BranchBase(BaseModel):
    organization_id: str
    name: str
    code: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    timezone: str = "UTC"


class BranchCreate(BranchBase):
    pass


class BranchResponse(BranchBase):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Designation Schemas
class DesignationBase(BaseModel):
    title: str
    code: str
    level: int = 1
    job_family: Optional[str] = None
    description: Optional[str] = None


class DesignationCreate(DesignationBase):
    pass


class DesignationResponse(DesignationBase):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Organization Schemas
class OrganizationCreate(BaseModel):
    name: str
    code: str
    tax_id: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None


class OrganizationResponse(OrganizationCreate):
    id: str
    tenant_id: str
    created_at: datetime
    branches: List[BranchResponse] = []
    departments: List[DepartmentResponse] = []

    model_config = ConfigDict(from_attributes=True)


# Org Chart Node
class OrgChartNode(BaseModel):
    id: str
    name: str
    code: str
    manager_name: Optional[str] = None
    manager_id: Optional[str] = None
    sub_departments: List["OrgChartNode"] = []
    employee_count: int = 0
