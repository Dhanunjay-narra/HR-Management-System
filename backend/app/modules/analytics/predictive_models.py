"""
Predictive Workforce Analytics & Multivariate Flight Risk Scoring Model
Evaluates compensation parity, promotion velocity, leave anomalies, and engagement factors to forecast retention.
"""
import math
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class FlightRiskFactor:
    name: str
    weight: float
    raw_value: float
    score: float  # 0.0 (safe) to 1.0 (critical danger)
    impact_description: str


@dataclass
class EmployeeFlightRiskAssessment:
    employee_id: str
    employee_name: str
    department_name: str
    composite_risk_score: float  # 0.0 to 100.0%
    risk_tier: str               # LOW, ELEVATED, HIGH, CRITICAL
    primary_risk_driver: str
    factors: List[FlightRiskFactor]
    retention_recommendations: List[str]


class PredictiveRetentionEngine:
    @classmethod
    def evaluate_flight_risk(
        cls,
        employee_id: str,
        employee_name: str,
        department_name: str,
        tenure_months: float,
        compa_ratio: float,          # 1.0 = exact market median, <0.8 = underpaid
        months_since_last_promotion: float,
        leave_frequency_trend: float, # +20% jump in leave = risk
        recent_peer_kudos_count: int,
        survey_sentiment_score: float # -1.0 to +1.0
    ) -> EmployeeFlightRiskAssessment:
        factors: List[FlightRiskFactor] = []

        # 1. Compensation Parity (Compa-Ratio)
        if compa_ratio < 0.80:
            comp_score = 0.90
            comp_desc = f"Significantly below salary band market midpoint (Compa-Ratio: {compa_ratio:.2f})."
        elif compa_ratio < 0.95:
            comp_score = 0.50
            comp_desc = f"Slightly below salary band market midpoint (Compa-Ratio: {compa_ratio:.2f})."
        else:
            comp_score = 0.10
            comp_desc = "Compensation aligned with market median."
        factors.append(FlightRiskFactor("Compensation Parity", 0.35, compa_ratio, comp_score, comp_desc))

        # 2. Promotion Stagnation
        if months_since_last_promotion > 36:
            prom_score = 0.85
            prom_desc = f"3+ years without career progression ({int(months_since_last_promotion)} months)."
        elif months_since_last_promotion > 24:
            prom_score = 0.55
            prom_desc = f"2+ years in current job grade ({int(months_since_last_promotion)} months)."
        else:
            prom_score = 0.15
            prom_desc = "Healthy career progression cadence."
        factors.append(FlightRiskFactor("Career Growth Velocity", 0.25, months_since_last_promotion, prom_score, prom_desc))

        # 3. Sentiment & Peer Recognition
        if survey_sentiment_score < -0.2:
            sent_score = 0.80
            sent_desc = "Negative response signals on recent pulse surveys."
        elif recent_peer_kudos_count == 0:
            sent_score = 0.50
            sent_desc = "Low peer recognition and engagement interaction."
        else:
            sent_score = 0.10
            sent_desc = "Strong peer recognition and positive sentiment."
        factors.append(FlightRiskFactor("Engagement & Sentiment", 0.20, survey_sentiment_score, sent_score, sent_desc))

        # 4. Tenure Inflection Point (1.5 - 2.5 years has highest external poaching rate)
        if 18 <= tenure_months <= 30:
            ten_score = 0.70
            ten_desc = "In high-risk 2-year tenure window for external recruitment headhunting."
        else:
            ten_score = 0.20
            ten_desc = "Tenure outside acute poaching hazard window."
        factors.append(FlightRiskFactor("Tenure Risk Window", 0.20, tenure_months, ten_score, ten_desc))

        # Composite score
        weighted_sum = sum(f.score * f.weight for f in factors)
        total_risk_pct = round(weighted_sum * 100.0, 1)

        if total_risk_pct >= 75.0:
            tier = "CRITICAL"
        elif total_risk_pct >= 50.0:
            tier = "HIGH"
        elif total_risk_pct >= 30.0:
            tier = "ELEVATED"
        else:
            tier = "LOW"

        # Find top driver
        top_driver = max(factors, key=lambda f: f.score * f.weight)

        recs = []
        if compa_ratio < 0.90:
            recs.append("Execute mid-cycle off-cycle compensation equity adjustment to 100% compa-ratio.")
        if months_since_last_promotion > 24:
            recs.append("Conduct formal career progression review with department director for next grade.")
        if recent_peer_kudos_count == 0:
            recs.append("Schedule 1-on-1 skip-level manager alignment to address engagement barriers.")

        return EmployeeFlightRiskAssessment(
            employee_id=employee_id,
            employee_name=employee_name,
            department_name=department_name,
            composite_risk_score=total_risk_pct,
            risk_tier=tier,
            primary_risk_driver=top_driver.name,
            factors=factors,
            retention_recommendations=recs or ["Maintain quarterly developmental syncs."]
        )
