"""
Master Scale 70k Generator
Generates comprehensive international regulatory payroll engines, ISO 27001 controls catalog, and rich React UI modules.
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. Switzerland AHV/ALV/BVG Pension & Income Tax Engine
swiss_code = '''"""
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
'''
write("backend/app/domain/calculators/switzerland_ahv_alv_bvg_calculator.py", swiss_code)

# 2. Hong Kong MPF & Salaries Tax Engine
hk_code = '''"""
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
'''
write("backend/app/domain/calculators/hong_kong_mpf_salaries_tax_calculator.py", hk_code)

# 3. Mexico IMSS, INFONAVIT & Aguinaldo Engine
mex_code = '''"""
Mexico Labor Law (Ley Federal del Trabajo) IMSS Social Security, INFONAVIT Housing & Aguinaldo Engine
Calculates Salario Diario Integrado (SDI), Cuotas Obrero-Patronales (IMSS), and mandatory 15-day Christmas Aguinaldo bonus.
"""
from typing import Dict, Any


class MexicoLaborLawCalculator:
    # 2026 UMA (Unidad de Medida y Actualización) = ~MXN 115.00 daily
    DAILY_UMA_2026 = 115.00

    @classmethod
    def calculate_mexico_compensation(
        cls,
        monthly_gross_salary_mxn: float,
        tenure_years: float = 2.0
    ) -> Dict[str, Any]:
        daily_salary = monthly_gross_salary_mxn / 30.0

        # Vacation days: 12 days year 1, +2 days each subsequent year
        vacation_days = min(32, 12 + int(tenure_years - 1) * 2) if tenure_years >= 1 else 12
        prima_vacacional = (vacation_days * daily_salary) * 0.25  # 25% statutory vacation premium

        # Aguinaldo: Minimum 15 days of salary
        aguinaldo_bonus = round(daily_salary * 15.0, 2)

        # Salario Diario Integrado (SDI) factor
        sdi_factor = 1.0 + (15.0 / 365.0) + (vacation_days * 0.25 / 365.0)
        sdi = round(daily_salary * sdi_factor, 2)

        # Employee IMSS deductions (~2.75% of SDI)
        imss_employee = round(sdi * 30.0 * 0.0275, 2)

        # ISR Income Tax Withholding (~18% progressive estimate)
        isr_tax = round(monthly_gross_salary_mxn * 0.18, 2)

        net_monthly_pay = round(monthly_gross_salary_mxn - imss_employee - isr_tax, 2)

        # Employer obligations: INFONAVIT 5% + IMSS Employer (~22% of SDI)
        infonavit_employer = round(sdi * 30.0 * 0.05, 2)
        imss_employer = round(sdi * 30.0 * 0.22, 2)

        return {
            "monthly_gross_mxn": monthly_gross_salary_mxn,
            "daily_base_salary_mxn": round(daily_salary, 2),
            "salario_diario_integrado_sdi_mxn": sdi,
            "statutory_aguinaldo_christmas_bonus_mxn": aguinaldo_bonus,
            "statutory_prima_vacacional_mxn": round(prima_vacacional, 2),
            "imss_employee_deduction_mxn": imss_employee,
            "isr_income_tax_withheld_mxn": isr_tax,
            "net_monthly_take_home_mxn": net_monthly_pay,
            "employer_infonavit_housing_mxn": infonavit_employer,
            "employer_imss_contributions_mxn": imss_employer,
            "total_company_burden_cost_mxn": round(monthly_gross_salary_mxn + infonavit_employer + imss_employer, 2)
        }
'''
write("backend/app/domain/calculators/mexico_imss_infonavit_calculator.py", mex_code)

# 4. Global Immigration & Visa Compliance Handbook
visa_code = '''"""
Global Work Authorization & Corporate Immigration Regulatory Handbook
Specifies sponsorship eligibility criteria, maximum stay durations, prevailing wage benchmarks, and renewal schedules for US, UK, EU, Canada, and Australia work visas.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class VisaCategoryRegulation:
    country_code: str
    visa_class: str
    visa_title: str
    target_role_type: str
    max_duration_years: float
    is_dual_intent_permitted: bool
    requires_labor_market_test: bool
    prevailing_wage_mandatory: bool
    filing_window_timeline: str
    renewal_extension_limits: str


GLOBAL_VISA_REGULATIONS_REGISTRY: Dict[str, VisaCategoryRegulation] = {
    "US-H1B": VisaCategoryRegulation(
        country_code="US",
        visa_class="H-1B",
        visa_title="Specialty Occupation Professional Worker",
        target_role_type="Software Engineers, Data Scientists, Product Managers",
        max_duration_years=6.0,
        is_dual_intent_permitted=True,
        requires_labor_market_test=False,  # LCA filing with DOL
        prevailing_wage_mandatory=True,
        filing_window_timeline="Annual March lottery window; petition filing April 1 - June 30.",
        renewal_extension_limits="Initial 3-year term, renewable for 3 additional years (6-year maximum without approved I-140)."
    ),
    "US-L1A": VisaCategoryRegulation(
        country_code="US",
        visa_class="L-1A",
        visa_title="Intracompany Transferee Executive or Manager",
        target_role_type="Engineering Directors, Department VPs, Regional General Managers",
        max_duration_years=7.0,
        is_dual_intent_permitted=True,
        requires_labor_market_test=False,
        prevailing_wage_mandatory=False,
        filing_window_timeline="Year-round petition filing; eligible for Blanket L program.",
        renewal_extension_limits="Initial 3-year term (1 year for new offices), renewable up to 7-year cumulative maximum."
    ),
    "US-TN": VisaCategoryRegulation(
        country_code="US",
        visa_class="TN",
        visa_title="USMCA Professional Worker (Canada & Mexico Citizens)",
        target_role_type="Software Engineers, Systems Analysts, Management Consultants",
        max_duration_years=3.0,
        is_dual_intent_permitted=False,
        requires_labor_market_test=False,
        prevailing_wage_mandatory=False,
        filing_window_timeline="Border pre-flight inspection for Canadians; consular processing for Mexicans.",
        renewal_extension_limits="Renewable indefinitely in 3-year increments provided non-immigrant intent is maintained."
    ),
    "UK-SW": VisaCategoryRegulation(
        country_code="UK",
        visa_class="Skilled Worker",
        visa_title="UK Skilled Worker Sponsor Visa",
        target_role_type="Tech professionals with Certificate of Sponsorship (CoS)",
        max_duration_years=5.0,
        is_dual_intent_permitted=True,
        requires_labor_market_test=False,
        prevailing_wage_mandatory=True,
        filing_window_timeline="Continuous online processing with defined CoS quota allocation.",
        renewal_extension_limits="Eligible for Indefinite Leave to Remain (ILR) settlement after 5 years continuous residence."
    ),
    "EU-BLUE": VisaCategoryRegulation(
        country_code="DE",
        visa_class="EU Blue Card",
        visa_title="European Union Highly Qualified Specialist Blue Card",
        target_role_type="STEM graduates, software architects, AI researchers",
        max_duration_years=4.0,
        is_dual_intent_permitted=True,
        requires_labor_market_test=False,
        prevailing_wage_mandatory=True,
        filing_window_timeline="Continuous consular processing with minimum salary threshold (~EUR 45,300 in bottleneck tech fields).",
        renewal_extension_limits="Fast-track German Permanent Settlement Permit (Niederlassungserlaubnis) after 21 months with B1 German."
    )
}
'''
write("backend/app/domain/reference/global_visas_immigration_handbook.py", visa_code)

print("Master Scale 70k Part 1 Built Successfully!")
'''
write("scripts/build_massive_enterprise_scale_70k.py", "# Scale 70k Part 1")
'''
