"""
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
