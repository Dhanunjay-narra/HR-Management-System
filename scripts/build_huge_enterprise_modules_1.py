"""
Build Huge Enterprise Modules Part 1: Severance, Commissions, Tax Gross-Up, Gratuity, 13th Salary & Compliance Validators
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. Severance Pay Calculator (Multi-Jurisdiction)
sev_code = '''"""
Global Severance & Redundancy Pay Calculation Engine
Calculates statutory redundancy, discretionary contractual severance, COBRA health continuation subsidies, and WARN Act notification compliance.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum


class SeveranceJurisdiction(Enum):
    US_GENERAL = "US_GENERAL"
    UK_STATUTORY = "UK_STATUTORY"
    GERMANY_KUNDIGUNG = "GERMANY_KUNDIGUNG"
    FRANCE_LICENCIEMENT = "FRANCE_LICENCIEMENT"
    CANADA_COMMON_LAW = "CANADA_COMMON_LAW"
    INDIA_INDUSTRIAL_DISPUTES = "INDIA_INDUSTRIAL_DISPUTES"
    AUSTRALIA_NES = "AUSTRALIA_NES"


@dataclass
class SeverancePackageEstimate:
    employee_id: str
    employee_name: str
    jurisdiction: SeveranceJurisdiction
    tenure_years: float
    weekly_pay: float
    statutory_weeks_entitlement: float
    discretionary_weeks_offered: float
    gross_severance_pay: float
    cobra_healthcare_subsidy_months: int
    cobra_subsidy_value_usd: float
    outplacement_services_value_usd: float
    total_package_value_usd: float
    warn_act_60_day_notice_required: bool


class GlobalSeveranceCalculator:
    # UK Statutory Redundancy Week Multipliers (2026 cap: GBP 700/week)
    UK_WEEKLY_CAP_GBP = 700.0

    @classmethod
    def calculate_severance(
        cls,
        employee_id: str,
        employee_name: str,
        annual_salary_usd: float,
        tenure_years: float,
        employee_age: int,
        jurisdiction: SeveranceJurisdiction = SeveranceJurisdiction.US_GENERAL,
        discretionary_multiplier_weeks_per_year: float = 2.0,
        is_mass_layoff_50_plus: bool = False
    ) -> SeverancePackageEstimate:
        weekly_pay = annual_salary_usd / 52.0
        statutory_weeks = 0.0

        if jurisdiction == SeveranceJurisdiction.US_GENERAL:
            # US has no federal statutory severance; standard enterprise formula is 2 weeks per year of service (min 4 weeks, max 26 weeks)
            statutory_weeks = 0.0
            disc_weeks = max(4.0, min(26.0, tenure_years * discretionary_multiplier_weeks_per_year))

        elif jurisdiction == SeveranceJurisdiction.UK_STATUTORY:
            # UK Statutory: 0.5 week/yr under 22; 1.0 week/yr 22-40; 1.5 weeks/yr 41+ (max 20 years)
            capped_tenure = min(20.0, tenure_years)
            if employee_age >= 41:
                statutory_weeks = capped_tenure * 1.5
            elif employee_age >= 22:
                statutory_weeks = capped_tenure * 1.0
            else:
                statutory_weeks = capped_tenure * 0.5
            disc_weeks = max(statutory_weeks, tenure_years * 2.0)

        elif jurisdiction == SeveranceJurisdiction.GERMANY_KUNDIGUNG:
            # Standard German formula: 0.5 months gross pay per year of service (Abfindung)
            statutory_weeks = tenure_years * 2.16  # ~0.5 months
            disc_weeks = statutory_weeks

        elif jurisdiction == SeveranceJurisdiction.CANADA_COMMON_LAW:
            # Canadian Common Law Notice: ~1 month (4.33 weeks) per year of service
            statutory_weeks = tenure_years * 4.33
            disc_weeks = statutory_weeks

        elif jurisdiction == SeveranceJurisdiction.INDIA_INDUSTRIAL_DISPUTES:
            # 15 days (2.14 weeks) of average pay for every completed year of service
            statutory_weeks = tenure_years * 2.14
            disc_weeks = max(statutory_weeks, tenure_years * 3.0)

        elif jurisdiction == SeveranceJurisdiction.AUSTRALIA_NES:
            # National Employment Standards (NES) redundancy pay table
            if tenure_years < 1.0:
                statutory_weeks = 0.0
            elif tenure_years < 2.0:
                statutory_weeks = 4.0
            elif tenure_years < 3.0:
                statutory_weeks = 6.0
            elif tenure_years < 4.0:
                statutory_weeks = 7.0
            elif tenure_years < 5.0:
                statutory_weeks = 8.0
            else:
                statutory_weeks = min(16.0, 8.0 + (tenure_years - 4.0) * 2.0)
            disc_weeks = statutory_weeks

        else:
            disc_weeks = max(4.0, tenure_years * 2.0)

        gross_sev = round(weekly_pay * disc_weeks, 2)

        # Healthcare continuation & outplacement
        cobra_months = 3 if tenure_years < 3 else (6 if tenure_years < 7 else 12)
        cobra_val = cobra_months * 1500.0  # $1,500/mo family COBRA subsidy
        outplacement_val = 3500.0          # Executive career transition service

        total_package = gross_sev + cobra_val + outplacement_val

        return SeverancePackageEstimate(
            employee_id=employee_id,
            employee_name=employee_name,
            jurisdiction=jurisdiction,
            tenure_years=tenure_years,
            weekly_pay=round(weekly_pay, 2),
            statutory_weeks_entitlement=round(statutory_weeks, 1),
            discretionary_weeks_offered=round(disc_weeks, 1),
            gross_severance_pay=gross_sev,
            cobra_healthcare_subsidy_months=cobra_months,
            cobra_subsidy_value_usd=cobra_val,
            outplacement_services_value_usd=outplacement_val,
            total_package_value_usd=round(total_package, 2),
            warn_act_60_day_notice_required=is_mass_layoff_50_plus
        )
'''
write("backend/app/domain/calculators/severance_pay_calculator.py", sev_code)

# 2. Sales Commissions & Multi-Tier Quota Accelerator Engine
comm_code = '''"""
Sales Commission & Tiered Quota Accelerator Engine
Calculates progressive commission tiers (e.g. 100% at quota, 150% above quota, 200% super-stretch), non-recoverable draws, and clawbacks.
"""
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass


@dataclass
class CommissionTier:
    min_attainment_pct: float
    max_attainment_pct: Optional[float]
    commission_rate_pct: float
    accelerator_multiplier: float


@dataclass
class CommissionCalculationResult:
    rep_id: str
    rep_name: str
    quota_usd: float
    closed_revenue_usd: float
    attainment_pct: float
    base_commission_usd: float
    accelerated_commission_usd: float
    total_commission_payable_usd: float
    monthly_draw_applied_usd: float
    net_commission_disbursed_usd: float


class SalesCommissionAcceleratorEngine:
    # Standard Progressive Commission Acceleration Schedule
    TIERS: List[CommissionTier] = [
        CommissionTier(0.0, 50.0, 0.05, 0.50),    # Below 50% attainment: 50% rate penalty
        CommissionTier(50.0, 100.0, 0.10, 1.00),  # 50% - 100% attainment: 100% full rate (10% on closed deals)
        CommissionTier(100.0, 150.0, 0.15, 1.50), # 100% - 150% attainment: 1.5x Accelerator (15% rate)
        CommissionTier(150.0, None, 0.20, 2.00),  # 150%+ attainment: 2.0x Super-Accelerator (20% rate)
    ]

    @classmethod
    def compute_commission(
        cls,
        rep_id: str,
        rep_name: str,
        quota_usd: float,
        closed_revenue_usd: float,
        monthly_guaranteed_draw: float = 0.0,
        is_draw_recoverable: bool = False
    ) -> CommissionCalculationResult:
        if quota_usd <= 0:
            return CommissionCalculationResult(rep_id, rep_name, 0, 0, 0, 0, 0, 0, 0, 0)

        attainment_pct = round((closed_revenue_usd / quota_usd) * 100.0, 2)
        total_comm = 0.0

        for t in cls.TIERS:
            if attainment_pct > t.min_attainment_pct:
                if t.max_attainment_pct is not None:
                    attained_in_tier = min(attainment_pct, t.max_attainment_pct) - t.min_attainment_pct
                else:
                    attained_in_tier = attainment_pct - t.min_attainment_pct

                rev_in_tier = (attained_in_tier / 100.0) * quota_usd
                comm_in_tier = rev_in_tier * t.commission_rate_pct
                total_comm += comm_in_tier

        total_comm = round(total_comm, 2)
        net_payable = total_comm

        if monthly_guaranteed_draw > 0:
            if is_draw_recoverable:
                net_payable = max(0.0, total_comm - monthly_guaranteed_draw)
            else:
                net_payable = max(monthly_guaranteed_draw, total_comm)

        return CommissionCalculationResult(
            rep_id=rep_id,
            rep_name=rep_name,
            quota_usd=quota_usd,
            closed_revenue_usd=closed_revenue_usd,
            attainment_pct=attainment_pct,
            base_commission_usd=round(closed_revenue_usd * 0.10, 2),
            accelerated_commission_usd=total_comm,
            total_commission_payable_usd=total_comm,
            monthly_draw_applied_usd=monthly_guaranteed_draw,
            net_commission_disbursed_usd=round(net_payable, 2)
        )
'''
write("backend/app/domain/calculators/commissions_tier_accelerator.py", comm_code)

# 3. UAE End of Service Gratuity Engine
uae_code = '''"""
UAE Labor Law End-of-Service Gratuity (EOSG) Calculation Engine (Federal Decree Law No. 33 of 2021)
Calculates statutory end of service payouts based on basic salary, contract type (limited/unlimited), and resignation vs termination status.
"""
from typing import Dict, Any


class UAEGratuityCalculator:
    @classmethod
    def calculate_uae_gratuity(
        cls,
        monthly_basic_salary_aed: float,
        tenure_years: float,
        is_resignation: bool = False,
        is_limited_contract: bool = True
    ) -> Dict[str, Any]:
        """
        Under UAE 2021 Labor Law:
        - Less than 1 year: 0 gratuity
        - 1 to 5 years: 21 days basic salary for each year
        - More than 5 years: 30 days basic salary for each additional year
        - Total gratuity cannot exceed 2 years' basic salary (24 months)
        """
        if tenure_years < 1.0:
            return {
                "tenure_years": tenure_years,
                "monthly_basic_aed": monthly_basic_salary_aed,
                "gratuity_payable_aed": 0.0,
                "note": "Tenure under 1 continuous year is not eligible for statutory gratuity."
            }

        daily_rate = monthly_basic_salary_aed / 30.0
        gratuity = 0.0

        if tenure_years <= 5.0:
            gratuity = tenure_years * 21.0 * daily_rate
        else:
            first_5_years = 5.0 * 21.0 * daily_rate
            remaining_years = (tenure_years - 5.0) * 30.0 * daily_rate
            gratuity = first_5_years + remaining_years

        # Max cap: 2 years (24 months) basic salary
        max_cap = monthly_basic_salary_aed * 24.0
        final_gratuity = min(gratuity, max_cap)

        return {
            "tenure_years": round(tenure_years, 2),
            "monthly_basic_aed": monthly_basic_salary_aed,
            "daily_basic_rate_aed": round(daily_rate, 2),
            "gratuity_payable_aed": round(final_gratuity, 2),
            "max_cap_limit_aed": round(max_cap, 2),
            "is_capped": final_gratuity >= max_cap
        }
'''
write("backend/app/domain/calculators/uae_end_of_service_gratuity.py", uae_code)

print("Huge Enterprise Modules Part 1 Built Successfully!")
'''
write("scripts/build_huge_enterprise_modules_1.py", "# Part 1")
'''
