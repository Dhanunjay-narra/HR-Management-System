"""
Leave Entitlement Balance Sheet Financial Liability Reporter (GAAP ASC 710 / IFRS IAS 19)
Computes accumulated earned leave liability, employer tax burden (FICA), and balance sheet accrual entries.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class EmployeeLeaveLiability:
    employee_id: str
    employee_name: str
    department: str
    hourly_rate: float
    accrued_unused_pto_hours: float
    raw_wage_liability: float
    employer_tax_burden: float  # Employer FICA 7.65%
    total_balance_sheet_liability: float


class LeaveLiabilityReportEngine:
    EMPLOYER_TAX_BURDEN_RATE = 0.0765  # 6.2% SS + 1.45% Medicare

    @classmethod
    def calculate_workforce_leave_liability(
        cls,
        employees: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        liabilities: List[EmployeeLeaveLiability] = []
        total_liability_sum = 0.0
        dept_breakdown: Dict[str, float] = {}

        for e in employees:
            annual_salary = float(e.get("annual_salary", 100000.0))
            hourly = annual_salary / 2080.0  # 2,080 working hours per year
            unused_days = float(e.get("unused_pto_days", 10.0))
            unused_hours = unused_days * 8.0

            wage_liab = round(hourly * unused_hours, 2)
            tax_liab = round(wage_liab * cls.EMPLOYER_TAX_BURDEN_RATE, 2)
            total_emp_liab = round(wage_liab + tax_liab, 2)

            total_liability_sum += total_emp_liab
            dept = e.get("department", "General")
            dept_breakdown[dept] = dept_breakdown.get(dept, 0.0) + total_emp_liab

            liabilities.append(EmployeeLeaveLiability(
                employee_id=e["id"],
                employee_name=e.get("full_name", "Employee"),
                department=dept,
                hourly_rate=round(hourly, 2),
                accrued_unused_pto_hours=round(unused_hours, 1),
                raw_wage_liability=wage_liab,
                employer_tax_burden=tax_liab,
                total_balance_sheet_liability=total_emp_liab
            ))

        return {
            "total_workforce_audited": len(employees),
            "total_balance_sheet_accrual_usd": round(total_liability_sum, 2),
            "department_accruals": {k: round(v, 2) for k, v in dept_breakdown.items()},
            "employee_liabilities": [l.__dict__ for l in liabilities]
        }
