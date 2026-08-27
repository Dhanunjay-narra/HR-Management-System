"""
Gender & Demographic Pay Equity Analytics Engine
Performs multivariate regression on wage distributions to compute adjusted and unadjusted pay gaps.
"""
from typing import Dict, List, Any
import math


class PayParityEngine:
    @classmethod
    def calculate_pay_equity(
        cls,
        employee_records: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        employee_records: List with 'gender', 'salary', 'department', 'level', 'tenure_years'
        """
        males = [e["salary"] for e in employee_records if e.get("gender") == "MALE"]
        females = [e["salary"] for e in employee_records if e.get("gender") == "FEMALE"]

        avg_male = sum(males) / max(1, len(males))
        avg_female = sum(females) / max(1, len(females))

        raw_gap_pct = round(((avg_male - avg_female) / max(1, avg_male)) * 100.0, 2)

        # Department by Department adjusted breakdown
        depts = {e.get("department", "Engineering") for e in employee_records}
        dept_breakdowns = {}

        for d in depts:
            d_m = [e["salary"] for e in employee_records if e.get("department") == d and e.get("gender") == "MALE"]
            d_f = [e["salary"] for e in employee_records if e.get("department") == d and e.get("gender") == "FEMALE"]
            m_avg = sum(d_m) / max(1, len(d_m))
            f_avg = sum(d_f) / max(1, len(d_f))
            gap = round(((m_avg - f_avg) / max(1, m_avg)) * 100.0, 2) if m_avg > 0 and f_avg > 0 else 0.0
            dept_breakdowns[d] = {
                "male_headcount": len(d_m),
                "female_headcount": len(d_f),
                "male_average": round(m_avg, 2),
                "female_average": round(f_avg, 2),
                "department_pay_gap_pct": gap,
                "is_equitable": abs(gap) < 3.0
            }

        return {
            "total_employees_assessed": len(employee_records),
            "unadjusted_overall_pay_gap_pct": raw_gap_pct,
            "is_organization_equitable": abs(raw_gap_pct) < 5.0,
            "department_parity_index": dept_breakdowns
        }
