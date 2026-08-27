"""
Japan Shakai Hoken (Social Insurance) & Inhabitant Tax Calculation Engine (2026 Regulations)
Calculates Kenko Hoken (Health Insurance), Kosei Nenkin (Employees' Pension), Employment Insurance, and Jyuminzei (Resident Tax).
"""
from typing import Dict, Any


class JapanPayrollCalculator:
    KOSEI_NENKIN_STANDARD_MONTHLY_CAP_JPY = 650000.0

    @classmethod
    def calculate_japan_payroll(
        cls,
        monthly_gross_salary_jpy: float,
        employee_age: int = 35,
        tokyo_resident: bool = True
    ) -> Dict[str, Any]:
        """
        Kenko Hoken (Tokyo 2026: 9.98% split 50/50 = 4.99% employee).
        Kosei Nenkin (18.3% split 50/50 = 9.15% employee, capped at JPY 650k).
        Employment Insurance (Koyo Hoken: 0.6% employee).
        Inhabitant Tax (Jyuminzei: ~10% municipal + prefectural).
        """
        # 1. Health Insurance (Kenko Hoken)
        health_rate = 0.0499
        if employee_age >= 40:
            # Kaigo Hoken (Nursing Care Insurance) +0.8%
            health_rate += 0.008
        health_deduction = round(monthly_gross_salary_jpy * health_rate)

        # 2. Pension (Kosei Nenkin)
        capped_pension_base = min(monthly_gross_salary_jpy, cls.KOSEI_NENKIN_STANDARD_MONTHLY_CAP_JPY)
        pension_deduction = round(capped_pension_base * 0.0915)

        # 3. Employment Insurance (Koyo Hoken)
        employment_ins_deduction = round(monthly_gross_salary_jpy * 0.006)

        # 4. Income Tax Withholding (Gensen Choshu)
        taxable_base = max(0.0, monthly_gross_salary_jpy - health_deduction - pension_deduction - employment_ins_deduction)
        income_tax = round(taxable_base * 0.08) # Progressive average estimate

        # 5. Inhabitant Tax (Resident Tax - Jyuminzei)
        resident_tax = round(monthly_gross_salary_jpy * 0.10)

        total_deductions = health_deduction + pension_deduction + employment_ins_deduction + income_tax + resident_tax
        net_pay = monthly_gross_salary_jpy - total_deductions

        return {
            "monthly_gross_jpy": monthly_gross_salary_jpy,
            "health_insurance_kenko_hoken_jpy": health_deduction,
            "pension_kosei_nenkin_jpy": pension_deduction,
            "employment_insurance_koyo_hoken_jpy": employment_ins_deduction,
            "income_tax_gensen_choshu_jpy": income_tax,
            "resident_tax_jyuminzei_jpy": resident_tax,
            "total_deductions_jpy": total_deductions,
            "net_take_home_jpy": net_pay
        }
