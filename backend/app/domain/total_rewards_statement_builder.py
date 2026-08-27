"""
Employee Total Rewards & Comprehensive Compensation Statement Generator
Calculates the holistic monetary value of base salary, annual bonuses, equity grants, employer 401(k) match, health subsidies, and wellness perks.
"""
from typing import Dict, Any, List
from dataclasses import dataclass


@dataclass
class TotalRewardsSummary:
    employee_name: str
    job_title: str
    base_salary: float
    target_annual_bonus: float
    equity_annual_vesting_value: float
    employer_health_subsidy: float
    employer_401k_match: float
    wellness_and_education_stipends: float
    total_rewards_annual_value: float
    employer_benefits_multiplier_pct: float


class TotalRewardsStatementEngine:
    @classmethod
    def generate_statement(
        cls,
        base_salary: float,
        bonus_target: float,
        annual_equity_vest_value: float,
        employee_name: str = "Employee",
        job_title: str = "Senior Engineer",
        medical_plan_type: str = "FAMILY"
    ) -> TotalRewardsSummary:
        # Typical employer health insurance subsidy
        health_subsidy = 18000.0 if medical_plan_type == "FAMILY" else 7500.0
        match_401k = min(base_salary * 0.04, 23500.0 * 0.04) # 4% safe harbor match
        stipends = 2400.0  # $100/mo wellness + $1,200 annual learning stipend

        total_value = base_salary + bonus_target + annual_equity_vest_value + health_subsidy + match_401k + stipends
        benefits_only = health_subsidy + match_401k + stipends
        multiplier = round((benefits_only / max(1.0, base_salary)) * 100.0, 1)

        return TotalRewardsSummary(
            employee_name=employee_name,
            job_title=job_title,
            base_salary=round(base_salary, 2),
            target_annual_bonus=round(bonus_target, 2),
            equity_annual_vesting_value=round(annual_equity_vest_value, 2),
            employer_health_subsidy=round(health_subsidy, 2),
            employer_401k_match=round(match_401k, 2),
            wellness_and_education_stipends=round(stipends, 2),
            total_rewards_annual_value=round(total_value, 2),
            employer_benefits_multiplier_pct=multiplier
        )
