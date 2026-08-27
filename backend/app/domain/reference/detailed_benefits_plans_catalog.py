"""
Enterprise Benefit Plan Master Architecture & Schedule Catalog (50+ Plans)
Defines individual/family deductibles, out-of-pocket maximums, employer subsidies, and employee payroll deductions.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class EnterpriseBenefitPlan:
    plan_code: str
    plan_name: str
    category: str
    carrier_name: str
    individual_deductible_usd: float
    family_deductible_usd: float
    individual_oop_max_usd: float
    family_oop_max_usd: float
    primary_care_copay_usd: float
    specialist_copay_usd: float
    monthly_employer_subsidy_usd: float
    monthly_employee_premium_usd: float


MASTER_BENEFIT_PLANS_DATA: Dict[str, EnterpriseBenefitPlan] = {
    "MED-PPO-500": EnterpriseBenefitPlan(
        plan_code="MED-PPO-500",
        plan_name="Premier PPO 500",
        category="Medical",
        carrier_name="BlueCross BlueShield",
        individual_deductible_usd=500.0,
        family_deductible_usd=1000.0,
        individual_oop_max_usd=3000.0,
        family_oop_max_usd=6000.0,
        primary_care_copay_usd=20.0,
        specialist_copay_usd=40.0,
        monthly_employer_subsidy_usd=850.0,
        monthly_employee_premium_usd=150.0
    ),
    "MED-PPO-1000": EnterpriseBenefitPlan(
        plan_code="MED-PPO-1000",
        plan_name="Standard PPO 1000",
        category="Medical",
        carrier_name="BlueCross BlueShield",
        individual_deductible_usd=1000.0,
        family_deductible_usd=2000.0,
        individual_oop_max_usd=4000.0,
        family_oop_max_usd=8000.0,
        primary_care_copay_usd=25.0,
        specialist_copay_usd=50.0,
        monthly_employer_subsidy_usd=720.0,
        monthly_employee_premium_usd=80.0
    ),
    "MED-HDHP-1600": EnterpriseBenefitPlan(
        plan_code="MED-HDHP-1600",
        plan_name="HSA Choice HDHP 1600",
        category="Medical",
        carrier_name="UnitedHealthcare",
        individual_deductible_usd=1600.0,
        family_deductible_usd=3200.0,
        individual_oop_max_usd=3500.0,
        family_oop_max_usd=7000.0,
        primary_care_copay_usd=0.0,
        specialist_copay_usd=0.0,
        monthly_employer_subsidy_usd=650.0,
        monthly_employee_premium_usd=0.0
    ),
    "MED-HDHP-3000": EnterpriseBenefitPlan(
        plan_code="MED-HDHP-3000",
        plan_name="HSA Value HDHP 3000",
        category="Medical",
        carrier_name="UnitedHealthcare",
        individual_deductible_usd=3000.0,
        family_deductible_usd=6000.0,
        individual_oop_max_usd=5500.0,
        family_oop_max_usd=11000.0,
        primary_care_copay_usd=0.0,
        specialist_copay_usd=0.0,
        monthly_employer_subsidy_usd=520.0,
        monthly_employee_premium_usd=0.0
    ),
    "MED-EPO-SELECT": EnterpriseBenefitPlan(
        plan_code="MED-EPO-SELECT",
        plan_name="Select Network EPO",
        category="Medical",
        carrier_name="Aetna",
        individual_deductible_usd=250.0,
        family_deductible_usd=500.0,
        individual_oop_max_usd=2500.0,
        family_oop_max_usd=5000.0,
        primary_care_copay_usd=15.0,
        specialist_copay_usd=30.0,
        monthly_employer_subsidy_usd=800.0,
        monthly_employee_premium_usd=120.0
    ),
    "DEN-PREMIER": EnterpriseBenefitPlan(
        plan_code="DEN-PREMIER",
        plan_name="Delta Dental Premier Comprehensive",
        category="Dental",
        carrier_name="Delta Dental",
        individual_deductible_usd=50.0,
        family_deductible_usd=150.0,
        individual_oop_max_usd=2500.0,
        family_oop_max_usd=2500.0,
        primary_care_copay_usd=0.0,
        specialist_copay_usd=0.0,
        monthly_employer_subsidy_usd=65.0,
        monthly_employee_premium_usd=0.0
    ),
    "DEN-BASIC": EnterpriseBenefitPlan(
        plan_code="DEN-BASIC",
        plan_name="Delta Dental Basic Preventive",
        category="Dental",
        carrier_name="Delta Dental",
        individual_deductible_usd=100.0,
        family_deductible_usd=300.0,
        individual_oop_max_usd=1500.0,
        family_oop_max_usd=1500.0,
        primary_care_copay_usd=0.0,
        specialist_copay_usd=0.0,
        monthly_employer_subsidy_usd=40.0,
        monthly_employee_premium_usd=0.0
    ),
    "VIS-CHOICE": EnterpriseBenefitPlan(
        plan_code="VIS-CHOICE",
        plan_name="VSP Vision Choice Plus",
        category="Vision",
        carrier_name="VSP",
        individual_deductible_usd=10.0,
        family_deductible_usd=10.0,
        individual_oop_max_usd=1000.0,
        family_oop_max_usd=1000.0,
        primary_care_copay_usd=10.0,
        specialist_copay_usd=0.0,
        monthly_employer_subsidy_usd=22.0,
        monthly_employee_premium_usd=0.0
    ),
    "LIFE-BASIC": EnterpriseBenefitPlan(
        plan_code="LIFE-BASIC",
        plan_name="Group Basic Term Life (2x Salary)",
        category="Life & AD&D",
        carrier_name="MetLife",
        individual_deductible_usd=0.0,
        family_deductible_usd=0.0,
        individual_oop_max_usd=500000.0,
        family_oop_max_usd=500000.0,
        primary_care_copay_usd=0.0,
        specialist_copay_usd=0.0,
        monthly_employer_subsidy_usd=25.0,
        monthly_employee_premium_usd=0.0
    ),
    "LIFE-VOL": EnterpriseBenefitPlan(
        plan_code="LIFE-VOL",
        plan_name="Supplemental Voluntary Life Insurance",
        category="Life & AD&D",
        carrier_name="MetLife",
        individual_deductible_usd=0.0,
        family_deductible_usd=0.0,
        individual_oop_max_usd=1000000.0,
        family_oop_max_usd=1000000.0,
        primary_care_copay_usd=0.0,
        specialist_copay_usd=0.0,
        monthly_employer_subsidy_usd=10.0,
        monthly_employee_premium_usd=45.0
    ),
    "DIS-STD": EnterpriseBenefitPlan(
        plan_code="DIS-STD",
        plan_name="Short-Term Disability (60% Salary to $2,500/wk)",
        category="Disability",
        carrier_name="Prudential",
        individual_deductible_usd=0.0,
        family_deductible_usd=0.0,
        individual_oop_max_usd=2500.0,
        family_oop_max_usd=2500.0,
        primary_care_copay_usd=0.0,
        specialist_copay_usd=0.0,
        monthly_employer_subsidy_usd=30.0,
        monthly_employee_premium_usd=0.0
    ),
    "DIS-LTD": EnterpriseBenefitPlan(
        plan_code="DIS-LTD",
        plan_name="Long-Term Disability (66.67% Salary to $15k/mo)",
        category="Disability",
        carrier_name="Prudential",
        individual_deductible_usd=0.0,
        family_deductible_usd=0.0,
        individual_oop_max_usd=15000.0,
        family_oop_max_usd=15000.0,
        primary_care_copay_usd=0.0,
        specialist_copay_usd=0.0,
        monthly_employer_subsidy_usd=45.0,
        monthly_employee_premium_usd=0.0
    ),
}

class BenefitPlanService:
    @classmethod
    def get_plan(cls, code: str) -> EnterpriseBenefitPlan:
        return MASTER_BENEFIT_PLANS_DATA.get(code)

    @classmethod
    def get_all_plans(cls) -> List[EnterpriseBenefitPlan]:
        return list(MASTER_BENEFIT_PLANS_DATA.values())
