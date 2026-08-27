"""
Payroll Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class SalaryStructureBase(BaseModel):
    employee_id: str
    currency: str = "USD"
    base_salary: float = Field(..., ge=0.0)
    house_rent_allowance: float = 0.0
    special_allowance: float = 0.0
    transport_allowance: float = 0.0
    medical_allowance: float = 0.0
    provident_fund_percentage: float = 12.0
    professional_tax: float = 0.0
    income_tax_tds: float = 0.0
    health_insurance_deduction: float = 0.0
    effective_from: date = Field(default_factory=date.today)


class SalaryStructureCreate(SalaryStructureBase):
    pass


class SalaryStructureResponse(SalaryStructureBase):
    id: str
    tenant_id: str
    gross_monthly_salary: float
    total_monthly_deductions: float
    net_monthly_salary: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PayrollRunCreate(BaseModel):
    month: int = Field(..., ge=1, le=12)
    year: int = Field(..., ge=2020)
    pay_period_start: date
    pay_period_end: date


class PayslipResponse(BaseModel):
    id: str
    payroll_run_id: str
    employee_id: str
    employee_name: Optional[str] = None
    month: int
    year: int
    working_days: float
    paid_days: float
    gross_earnings: float
    total_deductions: float
    net_pay: float
    earnings_breakdown: Dict[str, Any]
    deductions_breakdown: Dict[str, Any]
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PayrollRunResponse(BaseModel):
    id: str
    tenant_id: str
    month: int
    year: int
    pay_period_start: date
    pay_period_end: date
    status: str
    total_employees_count: int
    total_gross_payout: float
    total_deductions: float
    total_net_payout: float
    created_at: datetime
    payslips: List[PayslipResponse] = []

    model_config = ConfigDict(from_attributes=True)
