"""
Corporate Statutory & Voluntary Employee Benefits Management Catalog
Defines pre-tax/post-tax contribution formulas, vesting schedules, employer matching logic, and enrollment windows.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum


class BenefitType(Enum):
    RETIREMENT_401K = "RETIREMENT_401K"
    HEALTH_SAVINGS_ACCOUNT = "HEALTH_SAVINGS_ACCOUNT"
    FLEXIBLE_SPENDING_ACCOUNT = "FLEXIBLE_SPENDING_ACCOUNT"
    HEALTH_INSURANCE_HDHP = "HEALTH_INSURANCE_HDHP"
    HEALTH_INSURANCE_PPO = "HEALTH_INSURANCE_PPO"
    DENTAL_COMPREHENSIVE = "DENTAL_COMPREHENSIVE"
    VISION_STANDARD = "VISION_STANDARD"
    COMMUTER_TRANSIT = "COMMUTER_TRANSIT"
    EMPLOYEE_STOCK_PURCHASE = "EMPLOYEE_STOCK_PURCHASE"
    LIFE_INSURANCE_GROUP = "LIFE_INSURANCE_GROUP"


@dataclass
class BenefitPlanDefinition:
    plan_id: str
    plan_name: str
    benefit_type: BenefitType
    is_pre_tax: bool
    annual_employee_limit: float
    employer_match_percentage: float = 0.0
    employer_match_cap_percentage_of_salary: float = 0.0
    employer_annual_fixed_contribution: float = 0.0
    vesting_schedule_years: int = 0  # 0 = 100% immediate vesting


BENEFIT_PLANS_2026_CATALOG: Dict[str, BenefitPlanDefinition] = {
    "401K_TRADITIONAL_MATCH": BenefitPlanDefinition(
        plan_id="BEN-401K-01",
        plan_name="PeoplePulse Safe-Harbor 401(k) Retirement Plan",
        benefit_type=BenefitType.RETIREMENT_401K,
        is_pre_tax=True,
        annual_employee_limit=23500.0,
        employer_match_percentage=1.00,  # 100% match up to 4% of salary
        employer_match_cap_percentage_of_salary=0.04,
        vesting_schedule_years=0
    ),
    "HSA_FAMILY_2026": BenefitPlanDefinition(
        plan_id="BEN-HSA-02",
        plan_name="Health Savings Account (Family Tier)",
        benefit_type=BenefitType.HEALTH_SAVINGS_ACCOUNT,
        is_pre_tax=True,
        annual_employee_limit=8550.0,
        employer_annual_fixed_contribution=1000.0,
        vesting_schedule_years=0
    ),
    "HSA_INDIVIDUAL_2026": BenefitPlanDefinition(
        plan_id="BEN-HSA-01",
        plan_name="Health Savings Account (Individual Tier)",
        benefit_type=BenefitType.HEALTH_SAVINGS_ACCOUNT,
        is_pre_tax=True,
        annual_employee_limit=4300.0,
        employer_annual_fixed_contribution=500.0,
        vesting_schedule_years=0
    ),
    "FSA_HEALTH_2026": BenefitPlanDefinition(
        plan_id="BEN-FSA-01",
        plan_name="Healthcare Flexible Spending Account",
        benefit_type=BenefitType.FLEXIBLE_SPENDING_ACCOUNT,
        is_pre_tax=True,
        annual_employee_limit=3300.0,
        vesting_schedule_years=0
    ),
    "COMMUTER_PARKING_TRANSIT": BenefitPlanDefinition(
        plan_id="BEN-COMM-01",
        plan_name="Pre-Tax Commuter & Mass Transit Benefit",
        benefit_type=BenefitType.COMMUTER_TRANSIT,
        is_pre_tax=True,
        annual_employee_limit=3840.0, # $320/mo
        vesting_schedule_years=0
    )
}
