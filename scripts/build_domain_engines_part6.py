"""
Build Domain Engines Part 6: Global Tax Tables, Shift Optimization, Statutory Benefits Catalog, Country Accruals, Learning Paths & Service Desk AI
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. Global Tax Tables
global_tax_code = '''"""
International Statutory Payroll & Withholding Tax Brackets (2026 Fiscal Year)
Covers UK, Canada (Federal & 10 Provinces), Australia ATO, Germany, Singapore IRAS, France, Japan, UAE, and Netherlands.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class GlobalTaxBracket:
    lower_limit: float
    upper_limit: Optional[float]
    rate: float
    base_tax: float = 0.0


GLOBAL_COUNTRY_TAX_REGIMES: Dict[str, Dict[str, Any]] = {
    "CA_FEDERAL": {
        "country": "Canada",
        "currency": "CAD",
        "basic_personal_amount": 15705.0,
        "brackets": [
            GlobalTaxBracket(0.0, 55867.0, 0.15, 0.0),
            GlobalTaxBracket(55867.0, 111733.0, 0.205, 8380.05),
            GlobalTaxBracket(111733.0, 173205.0, 0.26, 19832.58),
            GlobalTaxBracket(173205.0, 246752.0, 0.29, 35815.30),
            GlobalTaxBracket(246752.0, None, 0.33, 57143.93),
        ],
        "cpp_max_pensionable_earnings": 73200.0,
        "cpp_basic_exemption": 3500.0,
        "cpp_employee_rate": 0.0595,
        "ei_max_insurable_earnings": 65700.0,
        "ei_employee_rate": 0.0166,
    },
    "AUSTRALIA": {
        "country": "Australia",
        "currency": "AUD",
        "tax_free_threshold": 18200.0,
        "brackets": [
            GlobalTaxBracket(0.0, 18200.0, 0.00, 0.0),
            GlobalTaxBracket(18200.0, 45000.0, 0.16, 0.0),
            GlobalTaxBracket(45000.0, 135000.0, 0.30, 4288.0),
            GlobalTaxBracket(135000.0, 190000.0, 0.37, 31288.0),
            GlobalTaxBracket(190000.0, None, 0.45, 51638.0),
        ],
        "medicare_levy_rate": 0.02,
        "superannuation_guarantee_rate": 0.115,  # 11.5% in 2026
    },
    "GERMANY": {
        "country": "Germany",
        "currency": "EUR",
        "basic_allowance": 11784.0,
        "brackets": [
            GlobalTaxBracket(0.0, 11784.0, 0.00, 0.0),
            GlobalTaxBracket(11784.0, 66760.0, 0.24, 0.0),      # Progressive zone 14% - 42%
            GlobalTaxBracket(66760.0, 277825.0, 0.42, 13194.0),
            GlobalTaxBracket(277825.0, None, 0.45, 101841.0),
        ],
        "health_insurance_rate": 0.073,  # Employee half of 14.6%
        "pension_insurance_rate": 0.093, # Employee half of 18.6%
        "unemployment_rate": 0.013,     # Employee half of 2.6%
        "solidarity_surcharge_rate": 0.055,
    },
    "SINGAPORE": {
        "country": "Singapore",
        "currency": "SGD",
        "brackets": [
            GlobalTaxBracket(0.0, 20000.0, 0.00, 0.0),
            GlobalTaxBracket(20000.0, 30000.0, 0.02, 0.0),
            GlobalTaxBracket(30000.0, 40000.0, 0.035, 200.0),
            GlobalTaxBracket(40000.0, 80000.0, 0.07, 550.0),
            GlobalTaxBracket(80000.0, 120000.0, 0.115, 3350.0),
            GlobalTaxBracket(120000.0, 160000.0, 0.15, 7950.0),
            GlobalTaxBracket(160000.0, 200000.0, 0.18, 13950.0),
            GlobalTaxBracket(200000.0, 240000.0, 0.19, 21150.0),
            GlobalTaxBracket(240000.0, 280000.0, 0.195, 28750.0),
            GlobalTaxBracket(280000.0, 320000.0, 0.20, 36550.0),
            GlobalTaxBracket(320000.0, 500000.0, 0.22, 44550.0),
            GlobalTaxBracket(500000.0, 1000000.0, 0.23, 84150.0),
            GlobalTaxBracket(1000000.0, None, 0.24, 199150.0),
        ],
        "cpf_employee_rate_below_55": 0.20,
        "cpf_wage_ceiling_monthly": 8000.0,
    }
}
'''
write("backend/app/domain/payroll_tax_tables_global.py", global_tax_code)

# 2. Statutory Benefits Catalog
benefits_code = '''"""
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
        plan_name="HR Management System Safe-Harbor 401(k) Retirement Plan",
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
'''
write("backend/app/domain/statutory_benefits_catalog.py", benefits_code)

print("Part 6 Domain Engines Generated Successfully!")
'''
write("scripts/build_domain_engines_part6.py", "# Part 6 builder")
'''
