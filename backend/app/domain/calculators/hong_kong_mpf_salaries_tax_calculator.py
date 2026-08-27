"""
Hong Kong Mandatory Provident Fund (MPF) & Progressive Salaries Tax Engine (Inland Revenue Ordinance 2026)
Calculates MPF 5% mandatory contribution (capped at HKD 1,500/mo) and progressive vs standard rate (15%) dual-test salaries tax.
"""
from typing import Dict, Any


class HongKongPayrollCalculator:
    MPF_MINIMUM_RELEVANT_INCOME_HKD = 7100.0
    MPF_MAXIMUM_RELEVANT_INCOME_HKD = 30000.0
    MPF_MAX_MANDATORY_DEDUCTION_HKD = 1500.0

    BASIC_SALARIES_TAX_ALLOWANCE_HKD = 132000.0

    # Progressive Tax Bands (HKD 50,000 each band)
    PROGRESSIVE_BANDS = [
        (50000.0, 0.02),
        (50000.0, 0.06),
        (50000.0, 0.10),
        (50000.0, 0.14),
        (float("inf"), 0.17),
    ]
    STANDARD_RATE = 0.15

    @classmethod
    def calculate_hk_payroll(
        cls,
        monthly_gross_salary_hkd: float
    ) -> Dict[str, Any]:
        # 1. MPF Employee Deduction (5% capped at HKD 1,500)
        mpf_deduction = 0.0
        if monthly_gross_salary_hkd >= cls.MPF_MINIMUM_RELEVANT_INCOME_HKD:
            mpf_deduction = min(monthly_gross_salary_hkd * 0.05, cls.MPF_MAX_MANDATORY_DEDUCTION_HKD)

        annual_gross = monthly_gross_salary_hkd * 12.0
        annual_mpf = mpf_deduction * 12.0

        # 2. Dual Tax Test: Progressive Rate vs Standard Rate (Taxpayer pays the lower of the two)
        net_assessable_income = max(0.0, annual_gross - annual_mpf - cls.BASIC_SALARIES_TAX_ALLOWANCE_HKD)

        # Progressive Method
        progressive_tax = 0.0
        rem_income = net_assessable_income
        for band_size, rate in cls.PROGRESSIVE_BANDS:
            if rem_income > 0:
                taxable_chunk = min(rem_income, band_size)
                progressive_tax += taxable_chunk * rate
                rem_income -= taxable_chunk
            else:
                break

        # Standard Rate Method (15% on gross minus MPF, without personal allowances)
        standard_tax = (annual_gross - annual_mpf) * cls.STANDARD_RATE

        final_annual_tax = min(progressive_tax, standard_tax)
        monthly_tax_estimate = round(final_annual_tax / 12.0, 2)
        net_monthly_pay = round(monthly_gross_salary_hkd - mpf_deduction - monthly_tax_estimate, 2)

        return {
            "monthly_gross_hkd": monthly_gross_salary_hkd,
            "mpf_employee_deduction_hkd": round(mpf_deduction, 2),
            "mpf_employer_matching_hkd": round(mpf_deduction, 2),
            "annual_salaries_tax_hkd": round(final_annual_tax, 2),
            "monthly_salaries_tax_reserve_hkd": monthly_tax_estimate,
            "net_monthly_take_home_hkd": net_monthly_pay,
            "tax_calculation_method_used": "PROGRESSIVE" if progressive_tax <= standard_tax else "STANDARD_RATE"
        }
