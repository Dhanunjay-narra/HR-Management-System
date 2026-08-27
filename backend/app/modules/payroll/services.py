"""
Payroll Processing Service
"""
from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc, delete
from sqlalchemy.orm import selectinload

from app.modules.payroll.models import SalaryStructure, PayrollRun, Payslip
from app.modules.payroll.schemas import SalaryStructureCreate, PayrollRunCreate
from app.modules.employees.models import Employee
from app.core.exceptions import ResourceNotFoundException, ValidationException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class PayrollService:
    @staticmethod
    async def create_or_update_salary(
        db: AsyncSession,
        tenant_id: str,
        data: SalaryStructureCreate,
        actor_id: Optional[str] = None
    ) -> SalaryStructure:
        res = await db.execute(
            select(SalaryStructure).where(
                SalaryStructure.employee_id == data.employee_id,
                SalaryStructure.tenant_id == tenant_id,
                SalaryStructure.is_deleted == False
            )
        )
        sal = res.scalar_one_or_none()
        if sal:
            for k, v in data.model_dump().items():
                setattr(sal, k, v)
        else:
            sal = SalaryStructure(tenant_id=tenant_id, **data.model_dump())
            db.add(sal)

        await db.flush()

        db.add(EmployeeTimelineEvent(
            tenant_id=tenant_id,
            employee_id=data.employee_id,
            actor_id=actor_id,
            event_type="SALARY_REVISED",
            title=f"Compensation Structure Configured",
            description=f"Base: ${sal.base_salary:,.2f} | Gross: ${sal.gross_monthly_salary:,.2f} | Net: ${sal.net_monthly_salary:,.2f}",
            entity_type="SalaryStructure",
            entity_id=sal.id
        ))
        await db.flush()
        return sal

    @staticmethod
    async def get_salary(db: AsyncSession, tenant_id: str, employee_id: str) -> Optional[SalaryStructure]:
        res = await db.execute(
            select(SalaryStructure).where(
                SalaryStructure.employee_id == employee_id,
                SalaryStructure.tenant_id == tenant_id,
                SalaryStructure.is_deleted == False
            )
        )
        return res.scalar_one_or_none()

    @staticmethod
    async def execute_payroll_run(
        db: AsyncSession,
        tenant_id: str,
        data: PayrollRunCreate,
        actor_id: Optional[str] = None
    ) -> PayrollRun:
        payroll_run = PayrollRun(
            tenant_id=tenant_id,
            month=data.month,
            year=data.year,
            pay_period_start=data.pay_period_start,
            pay_period_end=data.pay_period_end,
            status="PROCESSING"
        )
        db.add(payroll_run)
        await db.flush()

        # Load all active employees with salary structure
        res_salaries = await db.execute(
            select(SalaryStructure)
            .options(selectinload(SalaryStructure.employee))
            .where(SalaryStructure.tenant_id == tenant_id, SalaryStructure.is_deleted == False)
        )
        salaries = list(res_salaries.scalars().all())

        total_gross = 0.0
        total_deductions = 0.0
        total_net = 0.0

        for sal in salaries:
            gross = sal.gross_monthly_salary
            ded = sal.total_monthly_deductions
            net = sal.net_monthly_salary

            total_gross += gross
            total_deductions += ded
            total_net += net

            earnings = {
                "base_salary": sal.base_salary,
                "house_rent_allowance": sal.house_rent_allowance,
                "special_allowance": sal.special_allowance,
                "transport_allowance": sal.transport_allowance,
                "medical_allowance": sal.medical_allowance,
            }
            deductions = {
                "provident_fund": sal.base_salary * (sal.provident_fund_percentage / 100.0),
                "professional_tax": sal.professional_tax,
                "income_tax_tds": sal.income_tax_tds,
                "health_insurance": sal.health_insurance_deduction,
            }

            payslip = Payslip(
                tenant_id=tenant_id,
                payroll_run_id=payroll_run.id,
                employee_id=sal.employee_id,
                month=data.month,
                year=data.year,
                working_days=22.0,
                paid_days=22.0,
                gross_earnings=gross,
                total_deductions=ded,
                net_pay=net,
                earnings_breakdown=earnings,
                deductions_breakdown=deductions,
                status="GENERATED"
            )
            db.add(payslip)

        payroll_run.total_employees_count = len(salaries)
        payroll_run.total_gross_payout = total_gross
        payroll_run.total_deductions = total_deductions
        payroll_run.total_net_payout = total_net
        payroll_run.status = "APPROVED"
        payroll_run.approved_by_user_id = actor_id
        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="payroll.processed",
            tenant_id=tenant_id,
            actor_id=actor_id,
            payload={"payroll_run_id": payroll_run.id, "month": data.month, "year": data.year, "total_net": total_net}
        ))
        return payroll_run

    @staticmethod
    async def list_payroll_runs(db: AsyncSession, tenant_id: str) -> List[PayrollRun]:
        result = await db.execute(
            select(PayrollRun)
            .options(selectinload(PayrollRun.payslips))
            .where(PayrollRun.tenant_id == tenant_id, PayrollRun.is_deleted == False)
            .order_by(desc(PayrollRun.created_at))
        )
        return list(result.scalars().all())
