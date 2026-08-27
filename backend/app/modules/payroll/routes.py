"""
Payroll API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.payroll.schemas import (
    SalaryStructureCreate, SalaryStructureResponse, PayrollRunCreate, PayrollRunResponse, PayslipResponse
)
from app.modules.payroll.services import PayrollService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/payroll", tags=["Payroll Management"])


def format_payroll_run_response(r) -> dict:
    slips = r.__dict__.get("payslips", [])
    return {
        "id": r.id,
        "tenant_id": r.tenant_id,
        "month": r.month,
        "year": r.year,
        "pay_period_start": r.pay_period_start,
        "pay_period_end": r.pay_period_end,
        "status": r.status,
        "total_employees_count": r.total_employees_count,
        "total_gross_payout": r.total_gross_payout,
        "total_deductions": r.total_deductions,
        "total_net_payout": r.total_net_payout,
        "created_at": r.created_at,
        "payslips": [
            {
                "id": s.id,
                "payroll_run_id": s.payroll_run_id,
                "employee_id": s.employee_id,
                "employee_name": s.employee.full_name if hasattr(s, "employee") and s.employee else None,
                "month": s.month,
                "year": s.year,
                "working_days": s.working_days,
                "paid_days": s.paid_days,
                "gross_earnings": s.gross_earnings,
                "total_deductions": s.total_deductions,
                "net_pay": s.net_pay,
                "earnings_breakdown": s.earnings_breakdown,
                "deductions_breakdown": s.deductions_breakdown,
                "status": s.status,
                "created_at": s.created_at,
            } for s in slips
        ]
    }


@router.post("/salary-structure", response_model=SalaryStructureResponse, status_code=status.HTTP_200_OK)
async def set_salary_structure(
    data: SalaryStructureCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("payroll.process")),
):
    """Configure or update employee compensation structure."""
    sal = await PayrollService.create_or_update_salary(
        db, current_user.tenant_id or "default", data, actor_id=current_user.id
    )
    return {
        "id": sal.id,
        "tenant_id": sal.tenant_id,
        "employee_id": sal.employee_id,
        "currency": sal.currency,
        "base_salary": sal.base_salary,
        "house_rent_allowance": sal.house_rent_allowance,
        "special_allowance": sal.special_allowance,
        "transport_allowance": sal.transport_allowance,
        "medical_allowance": sal.medical_allowance,
        "provident_fund_percentage": sal.provident_fund_percentage,
        "professional_tax": sal.professional_tax,
        "income_tax_tds": sal.income_tax_tds,
        "health_insurance_deduction": sal.health_insurance_deduction,
        "effective_from": sal.effective_from,
        "gross_monthly_salary": sal.gross_monthly_salary,
        "total_monthly_deductions": sal.total_monthly_deductions,
        "net_monthly_salary": sal.net_monthly_salary,
        "created_at": sal.created_at,
    }


@router.get("/salary-structure/{employee_id}", response_model=Optional[SalaryStructureResponse])
async def get_salary_structure(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("payroll.view_own")),
):
    """Retrieve employee compensation breakdown."""
    target_id = employee_id if current_user.is_superuser or "payroll.view_all" in current_user.permissions else current_user.id
    sal = await PayrollService.get_salary(db, current_user.tenant_id or "default", target_id)
    if not sal:
        return None
    return {
        "id": sal.id,
        "tenant_id": sal.tenant_id,
        "employee_id": sal.employee_id,
        "currency": sal.currency,
        "base_salary": sal.base_salary,
        "house_rent_allowance": sal.house_rent_allowance,
        "special_allowance": sal.special_allowance,
        "transport_allowance": sal.transport_allowance,
        "medical_allowance": sal.medical_allowance,
        "provident_fund_percentage": sal.provident_fund_percentage,
        "professional_tax": sal.professional_tax,
        "income_tax_tds": sal.income_tax_tds,
        "health_insurance_deduction": sal.health_insurance_deduction,
        "effective_from": sal.effective_from,
        "gross_monthly_salary": sal.gross_monthly_salary,
        "total_monthly_deductions": sal.total_monthly_deductions,
        "net_monthly_salary": sal.net_monthly_salary,
        "created_at": sal.created_at,
    }


@router.post("/process", response_model=PayrollRunResponse, status_code=status.HTTP_201_CREATED)
async def process_payroll(
    data: PayrollRunCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("payroll.process")),
):
    """Execute monthly organization payroll run and generate payslips."""
    pr = await PayrollService.execute_payroll_run(
        db, current_user.tenant_id or "default", data, actor_id=current_user.id
    )
    return format_payroll_run_response(pr)


@router.get("/runs", response_model=List[PayrollRunResponse])
async def list_payroll_runs(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("payroll.view_all")),
):
    """List payroll processing batches."""
    runs = await PayrollService.list_payroll_runs(db, current_user.tenant_id or "default")
    return [format_payroll_run_response(r) for r in runs]
