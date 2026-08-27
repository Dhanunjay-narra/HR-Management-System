"""
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
