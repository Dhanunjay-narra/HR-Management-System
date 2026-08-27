"""
Advanced Workforce Intelligence & Demographic Forecasting Engine
Includes cohort retention analysis, salary compa-ratio distribution, predictive headcount growth, and attrition decomposition.
"""
from typing import Dict, List, Any, Tuple
import math


class WorkforceAnalyticsIntelligenceEngine:
    @staticmethod
    def calculate_cohort_retention(
        joining_records: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculates 1-year, 2-year, and 3-year survival probability rates by hiring cohort year.
        """
        cohorts: Dict[int, List[Dict[str, Any]]] = {}
        for r in joining_records:
            yr = r["joining_year"]
            cohorts.setdefault(yr, []).append(r)

        retention_matrix = {}
        for yr, emps in cohorts.items():
            total = len(emps)
            retained_1yr = sum(1 for e in emps if e.get("tenure_months", 0) >= 12)
            retained_2yr = sum(1 for e in emps if e.get("tenure_months", 0) >= 24)
            retained_3yr = sum(1 for e in emps if e.get("tenure_months", 0) >= 36)

            retention_matrix[str(yr)] = {
                "cohort_size": total,
                "retention_rate_12_months": round((retained_1yr / total) * 100.0, 1) if total > 0 else 100.0,
                "retention_rate_24_months": round((retained_2yr / total) * 100.0, 1) if total > 0 else 100.0,
                "retention_rate_36_months": round((retained_3yr / total) * 100.0, 1) if total > 0 else 100.0,
            }

        return retention_matrix

    @staticmethod
    def calculate_compa_ratios(
        salaries_and_bands: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculates salary compa-ratios (Actual Salary / Grade Midpoint).
        Identifies overpaid (>1.15) and underpaid (<0.85) workforce anomalies.
        """
        underpaid = []
        target_band = []
        overpaid = []

        total_ratio_sum = 0.0
        for s in salaries_and_bands:
            actual = s["base_salary"]
            midpoint = s["grade_midpoint"]
            ratio = round(actual / max(1.0, midpoint), 3)
            total_ratio_sum += ratio

            entry = {"employee_id": s["employee_id"], "name": s.get("name", "Employee"), "compa_ratio": ratio, "salary": actual}
            if ratio < 0.85:
                underpaid.append(entry)
            elif ratio > 1.15:
                overpaid.append(entry)
            else:
                target_band.append(entry)

        total = len(salaries_and_bands)
        avg_ratio = round(total_ratio_sum / max(1, total), 3)

        return {
            "total_evaluated": total,
            "average_organization_compa_ratio": avg_ratio,
            "underpaid_below_band_count": len(underpaid),
            "target_aligned_count": len(target_band),
            "overpaid_above_band_count": len(overpaid),
            "underpaid_employees": underpaid,
            "overpaid_employees": overpaid
        }
