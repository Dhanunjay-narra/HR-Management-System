"""
Huge Domain Pack Builder
Constructs 20 deep backend domain services and 15 rich frontend React TypeScript modules.
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. Compensation Planning Matrix
comp_matrix_code = '''"""
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
'''
write("backend/app/domain/compensation_planning_matrix.py", comp_matrix_code)

# 2. Succession Planning & Talent Bench Strength
succession_code = '''"""
Succession Planning & Critical Role Talent Bench Strength Analytics
Evaluates key-person vacancy risk, talent pipeline readiness (Ready Now, 1-2 Years, Emergency), and leadership diversity.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class SuccessionReadiness(Enum):
    READY_NOW = "READY_NOW"
    READY_IN_1_YEAR = "READY_IN_1_YEAR"
    READY_IN_2_YEARS = "READY_IN_2_YEARS"
    EMERGENCY_INTERIM = "EMERGENCY_INTERIM"


@dataclass
class SuccessionCandidate:
    candidate_id: str
    candidate_name: str
    current_role: str
    readiness: SuccessionReadiness
    competency_fit_score: float  # 0.0 to 100.0%
    retention_risk: str          # LOW, MEDIUM, HIGH
    development_needs: List[str] = field(default_factory=list)


@dataclass
class CriticalRoleSuccessionPlan:
    role_id: str
    role_title: str
    department: str
    current_incumbent_name: str
    incumbent_flight_risk: str
    is_critical_single_point_of_failure: bool
    pipeline_bench_strength_score: float  # 0 to 100
    succession_candidates: List[SuccessionCandidate] = field(default_factory=list)


class SuccessionPlanningEngine:
    @classmethod
    def calculate_bench_strength(cls, candidates: List[SuccessionCandidate]) -> float:
        """
        Computes composite talent bench strength based on candidate readiness tiers.
        Ready Now = 40 pts, 1 Year = 25 pts, 2 Years = 15 pts, Interim = 10 pts.
        """
        total_score = 0.0
        for c in candidates:
            if c.readiness == SuccessionReadiness.READY_NOW:
                total_score += 40.0 * (c.competency_fit_score / 100.0)
            elif c.readiness == SuccessionReadiness.READY_IN_1_YEAR:
                total_score += 25.0 * (c.competency_fit_score / 100.0)
            elif c.readiness == SuccessionReadiness.READY_IN_2_YEARS:
                total_score += 15.0 * (c.competency_fit_score / 100.0)
            elif c.readiness == SuccessionReadiness.EMERGENCY_INTERIM:
                total_score += 10.0 * (c.competency_fit_score / 100.0)

        return min(100.0, round(total_score, 1))

    @classmethod
    def audit_organization_succession_health(
        cls,
        critical_roles: List[CriticalRoleSuccessionPlan]
    ) -> Dict[str, Any]:
        uncovered_roles = []
        weak_pipeline = []
        healthy_pipeline = []

        for role in critical_roles:
            score = cls.calculate_bench_strength(role.succession_candidates)
            role.pipeline_bench_strength_score = score

            if len(role.succession_candidates) == 0:
                uncovered_roles.append(role.role_title)
            elif score < 50.0:
                weak_pipeline.append({"title": role.role_title, "bench_score": score})
            else:
                healthy_pipeline.append({"title": role.role_title, "bench_score": score})

        total = len(critical_roles)
        healthy_pct = round((len(healthy_pipeline) / max(1, total)) * 100.0, 1)

        return {
            "total_critical_roles_audited": total,
            "succession_health_index_pct": healthy_pct,
            "zero_coverage_critical_roles": uncovered_roles,
            "vulnerable_roles_below_target": weak_pipeline,
            "robust_coverage_roles": healthy_pipeline
        }
'''
write("backend/app/domain/succession_pipeline_engine.py", succession_code)

# 3. Headcount Capacity Planning & Forecasting
headcount_code = '''"""
Headcount Capacity Planning & Staffing Demand Forecasting Engine
Projects departmental staffing requirements, hiring velocity, ramp-up lag, and seasonal attrition churn.
"""
from typing import Dict, List, Any
import math


class HeadcountForecastingEngine:
    @staticmethod
    def project_quarterly_headcount(
        starting_headcount: int,
        quarterly_growth_target_pct: float,
        historical_annual_attrition_rate: float,
        average_time_to_hire_days: int,
        average_ramp_up_months: float,
        quarters_to_forecast: int = 4
    ) -> List[Dict[str, Any]]:
        forecast = []
        curr_headcount = starting_headcount
        quarterly_attrition_rate = (1.0 + historical_annual_attrition_rate) ** (0.25) - 1.0

        for q in range(1, quarters_to_forecast + 1):
            organic_departures = int(round(curr_headcount * quarterly_attrition_rate))
            target_net_adds = int(round(curr_headcount * (quarterly_growth_target_pct / 100.0)))
            gross_hires_needed = target_net_adds + organic_departures

            ending_headcount = curr_headcount + target_net_adds
            effective_productive_capacity = round(
                (curr_headcount - organic_departures) + (gross_hires_needed * (1.0 - (average_ramp_up_months / 6.0))),
                1
            )

            forecast.append({
                "quarter": f"Q{q}",
                "starting_headcount": curr_headcount,
                "projected_attrition_exits": organic_departures,
                "target_net_expansion": target_net_adds,
                "gross_requisitions_to_open": gross_hires_needed,
                "ending_headcount": ending_headcount,
                "effective_productive_capacity_fte": effective_productive_capacity,
                "recruiting_capacity_pressure": "HIGH" if gross_hires_needed > 20 else "MANAGEABLE"
            })
            curr_headcount = ending_headcount

        return forecast
'''
write("backend/app/domain/headcount_forecasting_model.py", headcount_code)

print("Huge Domain Pack Part 1 Built Successfully!")
'''
write("scripts/build_huge_domain_pack.py", "# Huge Domain Pack builder")
'''
