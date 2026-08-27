"""
Enterprise Compensation Planning & Merit Increase Matrix Engine
Calculates performance-based merit salary increases, market compa-ratio adjustments, STI/LTI bonus multipliers, and equity grant models.
"""
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class PerformanceTier(Enum):
    UNSATISFACTORY = 1
    DEVELOPING = 2
    STRONG_PERFORMER = 3
    EXCEEDS_EXPECTATIONS = 4
    ROLE_MODEL_TOP_TALENT = 5


class CompaRatioQuartile(Enum):
    QUARTILE_1_BELOW_80 = 1    # Underpaid relative to band
    QUARTILE_2_80_TO_100 = 2   # Lower target band
    QUARTILE_3_100_TO_120 = 3  # Upper target band
    QUARTILE_4_ABOVE_120 = 4   # Above market ceiling


@dataclass
class CompensationPlanningProposal:
    employee_id: str
    employee_name: str
    job_title: str
    department: str
    current_base_salary: float
    grade_min: float
    grade_midpoint: float
    grade_max: float
    compa_ratio: float
    compa_quartile: CompaRatioQuartile
    performance_rating: PerformanceTier
    merit_increase_pct: float
    market_adjustment_pct: float
    proposed_new_base_salary: float
    proposed_sti_bonus_target: float
    proposed_lti_rsu_grant_shares: int
    total_cash_compensation: float
    annual_budget_impact: float


class CompensationPlanningMatrixEngine:
    # Merit Grid Matrix (Performance Rating vs Compa-Ratio Quartile)
    # Rewards top performers below market median with highest salary increases
    MERIT_INCREASE_GRID: Dict[Tuple[PerformanceTier, CompaRatioQuartile], float] = {
        (PerformanceTier.ROLE_MODEL_TOP_TALENT, CompaRatioQuartile.QUARTILE_1_BELOW_80): 0.12,  # 12%
        (PerformanceTier.ROLE_MODEL_TOP_TALENT, CompaRatioQuartile.QUARTILE_2_80_TO_100): 0.10, # 10%
        (PerformanceTier.ROLE_MODEL_TOP_TALENT, CompaRatioQuartile.QUARTILE_3_100_TO_120): 0.08, # 8%
        (PerformanceTier.ROLE_MODEL_TOP_TALENT, CompaRatioQuartile.QUARTILE_4_ABOVE_120): 0.05,  # 5% (or lump-sum)

        (PerformanceTier.EXCEEDS_EXPECTATIONS, CompaRatioQuartile.QUARTILE_1_BELOW_80): 0.09,
        (PerformanceTier.EXCEEDS_EXPECTATIONS, CompaRatioQuartile.QUARTILE_2_80_TO_100): 0.07,
        (PerformanceTier.EXCEEDS_EXPECTATIONS, CompaRatioQuartile.QUARTILE_3_100_TO_120): 0.05,
        (PerformanceTier.EXCEEDS_EXPECTATIONS, CompaRatioQuartile.QUARTILE_4_ABOVE_120): 0.03,

        (PerformanceTier.STRONG_PERFORMER, CompaRatioQuartile.QUARTILE_1_BELOW_80): 0.06,
        (PerformanceTier.STRONG_PERFORMER, CompaRatioQuartile.QUARTILE_2_80_TO_100): 0.04,
        (PerformanceTier.STRONG_PERFORMER, CompaRatioQuartile.QUARTILE_3_100_TO_120): 0.03,
        (PerformanceTier.STRONG_PERFORMER, CompaRatioQuartile.QUARTILE_4_ABOVE_120): 0.015,

        (PerformanceTier.DEVELOPING, CompaRatioQuartile.QUARTILE_1_BELOW_80): 0.02,
        (PerformanceTier.DEVELOPING, CompaRatioQuartile.QUARTILE_2_80_TO_100): 0.01,
        (PerformanceTier.DEVELOPING, CompaRatioQuartile.QUARTILE_3_100_TO_120): 0.00,
        (PerformanceTier.DEVELOPING, CompaRatioQuartile.QUARTILE_4_ABOVE_120): 0.00,

        (PerformanceTier.UNSATISFACTORY, CompaRatioQuartile.QUARTILE_1_BELOW_80): 0.00,
        (PerformanceTier.UNSATISFACTORY, CompaRatioQuartile.QUARTILE_2_80_TO_100): 0.00,
        (PerformanceTier.UNSATISFACTORY, CompaRatioQuartile.QUARTILE_3_100_TO_120): 0.00,
        (PerformanceTier.UNSATISFACTORY, CompaRatioQuartile.QUARTILE_4_ABOVE_120): 0.00,
    }

    # Bonus Multipliers by Grade
    BONUS_PERCENTAGE_BY_GRADE = {
        "L1": 0.05, "L2": 0.08, "L3": 0.12, "L4": 0.15,
        "L5": 0.20, "L6": 0.25, "L7": 0.30, "L8": 0.40,
        "DIRECTOR": 0.35, "VP": 0.50, "SVP": 0.60, "C_LEVEL": 0.80
    }

    # RSU Annual Refresh Grant Target Shares by Level
    EQUITY_RSU_GRANT_BY_GRADE = {
        "L1": 100, "L2": 250, "L3": 500, "L4": 1000,
        "L5": 2000, "L6": 3500, "L7": 6000, "L8": 10000,
        "DIRECTOR": 15000, "VP": 30000, "SVP": 50000, "C_LEVEL": 100000
    }

    @classmethod
    def determine_compa_quartile(cls, current_salary: float, grade_min: float, grade_max: float) -> CompaRatioQuartile:
        spread = grade_max - grade_min
        if spread <= 0:
            return CompaRatioQuartile.QUARTILE_2_80_TO_100

        pos = (current_salary - grade_min) / spread
        if pos < 0.25:
            return CompaRatioQuartile.QUARTILE_1_BELOW_80
        elif pos < 0.50:
            return CompaRatioQuartile.QUARTILE_2_80_TO_100
        elif pos < 0.75:
            return CompaRatioQuartile.QUARTILE_3_100_TO_120
        else:
            return CompaRatioQuartile.QUARTILE_4_ABOVE_120

    @classmethod
    def calculate_merit_proposal(
        cls,
        employee_id: str,
        employee_name: str,
        job_title: str,
        department: str,
        grade_code: str,
        current_base_salary: float,
        grade_min: float,
        grade_max: float,
        performance_rating_score: int
    ) -> CompensationPlanningProposal:
        grade_mid = (grade_min + grade_max) / 2.0
        compa_ratio = round(current_base_salary / max(1.0, grade_mid), 3)

        quartile = cls.determine_compa_quartile(current_base_salary, grade_min, grade_max)
        try:
            perf_enum = PerformanceTier(performance_rating_score)
        except ValueError:
            perf_enum = PerformanceTier.STRONG_PERFORMER

        merit_pct = cls.MERIT_INCREASE_GRID.get((perf_enum, quartile), 0.03)

        # Extra equity adjustment if severely below band minimum
        market_adj_pct = 0.0
        if current_base_salary < grade_min:
            market_adj_pct = round((grade_min - current_base_salary) / current_base_salary, 3)

        total_increase_pct = merit_pct + market_adj_pct
        new_base = round(current_base_salary * (1.0 + total_increase_pct), 2)
        annual_impact = new_base - current_base_salary

        bonus_pct = cls.BONUS_PERCENTAGE_BY_GRADE.get(grade_code.upper(), 0.10)
        proposed_bonus = round(new_base * bonus_pct, 2)
        rsu_shares = cls.EQUITY_RSU_GRANT_BY_GRADE.get(grade_code.upper(), 500)

        # Performance multiplier on RSU grants
        if perf_enum == PerformanceTier.ROLE_MODEL_TOP_TALENT:
            rsu_shares = int(rsu_shares * 1.5)
        elif perf_enum == PerformanceTier.EXCEEDS_EXPECTATIONS:
            rsu_shares = int(rsu_shares * 1.2)
        elif perf_enum in (PerformanceTier.DEVELOPING, PerformanceTier.UNSATISFACTORY):
            rsu_shares = 0

        return CompensationPlanningProposal(
            employee_id=employee_id,
            employee_name=employee_name,
            job_title=job_title,
            department=department,
            current_base_salary=current_base_salary,
            grade_min=grade_min,
            grade_midpoint=grade_mid,
            grade_max=grade_max,
            compa_ratio=compa_ratio,
            compa_quartile=quartile,
            performance_rating=perf_enum,
            merit_increase_pct=round(merit_pct * 100.0, 2),
            market_adjustment_pct=round(market_adj_pct * 100.0, 2),
            proposed_new_base_salary=new_base,
            proposed_sti_bonus_target=proposed_bonus,
            proposed_lti_rsu_grant_shares=rsu_shares,
            total_cash_compensation=round(new_base + proposed_bonus, 2),
            annual_budget_impact=round(annual_impact, 2)
        )
