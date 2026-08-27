"""
Ireland Revenue PAYE, Universal Social Charge (USC) & PRSI Calculation Engine (2026 Budget Regulations)
Calculates Standard Rate Cut-Off Point (SRCOP), Universal Social Charge 4-tier progressive schedule, and Employee PRSI Class A1.
"""
from typing import Dict, Any


class IrelandPayrollCalculator:
    # 2026 Ireland Tax Bands (Single Individual)
    SRCOP_SINGLE_EUR = 42000.0
    STANDARD_RATE = 0.20  # 20%
    HIGHER_RATE = 0.40    # 40%

    PERSONAL_TAX_CREDIT_EUR = 1875.0
    EMPLOYEE_PAYE_TAX_CREDIT_EUR = 1875.0

    # 2026 USC Bands
    USC_BANDS = [
        (12012.0, 0.005),  # 0.5% on first €12,012
        (13748.0, 0.020),  # 2.0% on next €13,748 (up to €25,760)
        (44284.0, 0.040),  # 4.0% on next €44,284 (up to €70,044)
        (float("inf"), 0.080) # 8.0% on balance
    ]

    PRSI_EMPLOYEE_CLASS_A_RATE = 0.041  # 4.10%

    @classmethod
    def calculate_ireland_payroll(
        cls,
        annual_gross_salary_eur: float
    ) -> Dict[str, Any]:
        # 1. Income Tax (PAYE)
        if annual_gross_salary_eur <= cls.SRCOP_SINGLE_EUR:
            gross_paye = annual_gross_salary_eur * cls.STANDARD_RATE
        else:
            gross_paye = (cls.SRCOP_SINGLE_EUR * cls.STANDARD_RATE) + ((annual_gross_salary_eur - cls.SRCOP_SINGLE_EUR) * cls.HIGHER_RATE)

        total_tax_credits = cls.PERSONAL_TAX_CREDIT_EUR + cls.EMPLOYEE_PAYE_TAX_CREDIT_EUR
        net_paye = max(0.0, gross_paye - total_tax_credits)

        # 2. Universal Social Charge (USC)
        usc_total = 0.0
        rem_income = annual_gross_salary_eur
        for band_size, rate in cls.USC_BANDS:
            if rem_income > 0:
                chunk = min(rem_income, band_size)
                usc_total += chunk * rate
                rem_income -= chunk
            else:
                break

        # 3. PRSI Employee (Class A1 4.1%)
        prsi_employee = round(annual_gross_salary_eur * cls.PRSI_EMPLOYEE_CLASS_A_RATE, 2)
        total_deductions = round(net_paye + usc_total + prsi_employee, 2)
        annual_net = round(annual_gross_salary_eur - total_deductions, 2)

        return {
            "gross_annual_eur": annual_gross_salary_eur,
            "annual_paye_income_tax_eur": round(net_paye, 2),
            "annual_usc_charge_eur": round(usc_total, 2),
            "annual_prsi_social_insurance_eur": prsi_employee,
            "total_annual_deductions_eur": total_deductions,
            "annual_net_take_home_eur": annual_net,
            "monthly_net_pay_eur": round(annual_net / 12.0, 2),
            "effective_tax_rate_pct": round((total_deductions / annual_gross_salary_eur) * 100.0, 1)
        }
