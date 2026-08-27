"""
Switzerland AHV/ALV/BVG Social Security & Cantonal Withholding Tax Engine (2026 Swiss Federal Law)
Calculates 1st Pillar (AHV/IV/EO 5.3%), 2nd Pillar (BVG LPP Occupational Pension by age group), Unemployment Insurance (ALV 1.1%), and Quellensteuer (Tax at Source).
"""
from typing import Dict, Any


class SwitzerlandPayrollCalculator:
    # 2026 Swiss Social Security Constants
    AHV_IV_EO_EMPLOYEE_RATE = 0.053   # 5.30%
    ALV_UNEMPLOYMENT_RATE = 0.011      # 1.10% up to CHF 148,200
    ALV_MAX_INSURABLE_SALARY_CHF = 148200.0

    # BVG 2nd Pillar Mandatory Minimum Pension Contributions by Age
    BVG_COORDINATION_DEDUCTION_CHF = 25725.0
    BVG_MAX_COORDINATED_SALARY_CHF = 88200.0

    @classmethod
    def calculate_swiss_payroll(
        cls,
        monthly_gross_salary_chf: float,
        employee_age: int = 35,
        canton_code: str = "ZH"
    ) -> Dict[str, Any]:
        annual_gross = monthly_gross_salary_chf * 12.0

        # 1. 1st Pillar: AHV / IV / EO (5.30% employee)
        ahv_deduction = round(monthly_gross_salary_chf * cls.AHV_IV_EO_EMPLOYEE_RATE, 2)

        # 2. Unemployment Insurance (ALV: 1.10% capped at CHF 148,200/yr)
        monthly_alv_cap = cls.ALV_MAX_INSURABLE_SALARY_CHF / 12.0
        capped_alv_wage = min(monthly_gross_salary_chf, monthly_alv_cap)
        alv_deduction = round(capped_alv_wage * cls.ALV_UNEMPLOYMENT_RATE, 2)

        # 3. 2nd Pillar: BVG / LPP Occupational Pension (Age-based coordinated salary)
        coordinated_annual_salary = max(0.0, min(annual_gross, cls.BVG_MAX_COORDINATED_SALARY_CHF) - cls.BVG_COORDINATION_DEDUCTION_CHF)
        coordinated_monthly = coordinated_annual_salary / 12.0

        if employee_age < 25:
            bvg_rate = 0.0  # Risk only
        elif employee_age <= 34:
            bvg_rate = 0.035  # Employee half of 7%
        elif employee_age <= 44:
            bvg_rate = 0.050  # Employee half of 10%
        elif employee_age <= 54:
            bvg_rate = 0.075  # Employee half of 15%
        else:
            bvg_rate = 0.090  # Employee half of 18%

        bvg_deduction = round(coordinated_monthly * bvg_rate, 2)

        # 4. Non-Occupational Accident Insurance (NBU ~1.5%)
        nbu_deduction = round(capped_alv_wage * 0.015, 2)

        # 5. Cantonal Withholding Tax at Source (Quellensteuer ~10-14% average)
        canton_rate = 0.12 if canton_code.upper() in ("GE", "VD") else 0.10
        withholding_tax = round(monthly_gross_salary_chf * canton_rate, 2)

        total_deductions = ahv_deduction + alv_deduction + bvg_deduction + nbu_deduction + withholding_tax
        net_pay = round(monthly_gross_salary_chf - total_deductions, 2)

        return {
            "monthly_gross_salary_chf": monthly_gross_salary_chf,
            "canton_code": canton_code,
            "employee_age": employee_age,
            "ahv_iv_eo_1st_pillar_deduction_chf": ahv_deduction,
            "alv_unemployment_deduction_chf": alv_deduction,
            "bvg_lpp_2nd_pillar_pension_deduction_chf": bvg_deduction,
            "nbu_accident_insurance_deduction_chf": nbu_deduction,
            "quellensteuer_withholding_tax_chf": withholding_tax,
            "total_monthly_deductions_chf": round(total_deductions, 2),
            "net_monthly_take_home_chf": net_pay
        }
