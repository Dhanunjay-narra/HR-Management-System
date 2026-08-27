"""
9-Box Talent Assessment & Succession Planning Engine
Calculates employee placement on 3x3 Performance vs Potential matrix and normalizes organization-wide distributions.
"""
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass


class TalentBoxCategory:
    # 9-Box Grid Classifications
    LOW_POTENTIAL_LOW_PERF = "UNDERPERFORMER"            # 1,1
    LOW_POTENTIAL_MED_PERF = "EFFECTIVE_PRO"             # 1,2
    LOW_POTENTIAL_HIGH_PERF = "TRUSTED_SPECIALIST"       # 1,3
    
    MED_POTENTIAL_LOW_PERF = "DILEMMA_QUESTION_MARK"     # 2,1
    MED_POTENTIAL_MED_PERF = "CORE_PLAYER"               # 2,2
    MED_POTENTIAL_HIGH_PERF = "HIGH_IMPACT_PERFORMER"    # 2,3
    
    HIGH_POTENTIAL_LOW_PERF = "ENIGMA_ROUGH_DIAMOND"     # 3,1
    HIGH_POTENTIAL_MED_PERF = "HIGH_POTENTIAL_FUTURE"    # 3,2
    HIGH_POTENTIAL_HIGH_PERF = "STAR_EXECUTIVE_TALENT"   # 3,3


@dataclass
class NineBoxPosition:
    employee_id: str
    employee_name: str
    performance_score: float  # 1.0 to 5.0
    potential_score: float    # 1.0 to 5.0
    grid_x: int               # 1 (Low), 2 (Med), 3 (High)
    grid_y: int               # 1 (Low), 2 (Med), 3 (High)
    box_category: str
    recommended_action: str
    retention_risk: str       # LOW, MEDIUM, HIGH, CRITICAL


class NineBoxMatrixEngine:
    GRID_MAPPING = {
        (1, 1): (TalentBoxCategory.LOW_POTENTIAL_LOW_PERF, "Performance improvement plan (PIP) or exit transition.", "CRITICAL"),
        (2, 1): (TalentBoxCategory.LOW_POTENTIAL_MED_PERF, "Retain in current role; recognize steady contributions.", "LOW"),
        (3, 1): (TalentBoxCategory.LOW_POTENTIAL_HIGH_PERF, "Reward expertise; avoid promoting into general management.", "LOW"),
        
        (1, 2): (TalentBoxCategory.MED_POTENTIAL_LOW_PERF, "Address motivational barriers; targeted skill coaching.", "HIGH"),
        (2, 2): (TalentBoxCategory.MED_POTENTIAL_MED_PERF, "Continuous development; assign cross-functional projects.", "MEDIUM"),
        (3, 2): (TalentBoxCategory.MED_POTENTIAL_HIGH_PERF, "Fast-track promotion readiness; assign strategic initiatives.", "HIGH"),
        
        (1, 3): (TalentBoxCategory.HIGH_POTENTIAL_LOW_PERF, "Realign role to intrinsic strengths; provide senior mentor.", "HIGH"),
        (2, 3): (TalentBoxCategory.HIGH_POTENTIAL_MED_PERF, "High future capability; prepare for team leadership.", "HIGH"),
        (3, 3): (TalentBoxCategory.STAR_EXECUTIVE_TALENT, "Top tier succession candidate; retention stock grants & executive sponsor.", "CRITICAL"),
    }

    @staticmethod
    def map_score_to_tier(score: float) -> int:
        if score < 2.8:
            return 1
        elif score < 4.0:
            return 2
        else:
            return 3

    @classmethod
    def evaluate_employee(
        cls,
        employee_id: str,
        employee_name: str,
        performance_score: float,
        potential_score: float
    ) -> NineBoxPosition:
        perf_tier = cls.map_score_to_tier(performance_score)
        pot_tier = cls.map_score_to_tier(potential_score)

        box_cat, action, risk = cls.GRID_MAPPING.get(
            (perf_tier, pot_tier),
            (TalentBoxCategory.MED_POTENTIAL_MED_PERF, "Maintain steady growth trajectory.", "MEDIUM")
        )

        return NineBoxPosition(
            employee_id=employee_id,
            employee_name=employee_name,
            performance_score=round(performance_score, 2),
            potential_score=round(potential_score, 2),
            grid_x=perf_tier,
            grid_y=pot_tier,
            box_category=box_cat,
            recommended_action=action,
            retention_risk=risk
        )

    @classmethod
    def analyze_organization_distribution(
        cls,
        evaluations: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        positions: List[NineBoxPosition] = []
        grid_counts: Dict[str, int] = {}

        for ev in evaluations:
            pos = cls.evaluate_employee(
                employee_id=ev["employee_id"],
                employee_name=ev.get("employee_name", "Employee"),
                performance_score=float(ev.get("performance_score", 3.0)),
                potential_score=float(ev.get("potential_score", 3.0))
            )
            positions.append(pos)
            grid_counts[pos.box_category] = grid_counts.get(pos.box_category, 0) + 1

        total = len(positions)
        star_count = grid_counts.get(TalentBoxCategory.STAR_EXECUTIVE_TALENT, 0)
        pip_count = grid_counts.get(TalentBoxCategory.LOW_POTENTIAL_LOW_PERF, 0)

        return {
            "total_assessed": total,
            "stars_percentage": round((star_count / total) * 100.0, 1) if total > 0 else 0.0,
            "at_risk_percentage": round((pip_count / total) * 100.0, 1) if total > 0 else 0.0,
            "grid_distribution": grid_counts,
            "positions": [p.__dict__ for p in positions]
        }
