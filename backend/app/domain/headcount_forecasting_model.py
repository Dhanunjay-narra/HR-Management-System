"""
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
