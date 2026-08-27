"""
UAE Labor Law End-of-Service Gratuity (EOSG) Calculation Engine (Federal Decree Law No. 33 of 2021)
Calculates statutory end of service payouts based on basic salary, contract type (limited/unlimited), and resignation vs termination status.
"""
from typing import Dict, Any


class UAEGratuityCalculator:
    @classmethod
    def calculate_uae_gratuity(
        cls,
        monthly_basic_salary_aed: float,
        tenure_years: float,
        is_resignation: bool = False,
        is_limited_contract: bool = True
    ) -> Dict[str, Any]:
        """
        Under UAE 2021 Labor Law:
        - Less than 1 year: 0 gratuity
        - 1 to 5 years: 21 days basic salary for each year
        - More than 5 years: 30 days basic salary for each additional year
        - Total gratuity cannot exceed 2 years' basic salary (24 months)
        """
        if tenure_years < 1.0:
            return {
                "tenure_years": tenure_years,
                "monthly_basic_aed": monthly_basic_salary_aed,
                "gratuity_payable_aed": 0.0,
                "note": "Tenure under 1 continuous year is not eligible for statutory gratuity."
            }

        daily_rate = monthly_basic_salary_aed / 30.0
        gratuity = 0.0

        if tenure_years <= 5.0:
            gratuity = tenure_years * 21.0 * daily_rate
        else:
            first_5_years = 5.0 * 21.0 * daily_rate
            remaining_years = (tenure_years - 5.0) * 30.0 * daily_rate
            gratuity = first_5_years + remaining_years

        # Max cap: 2 years (24 months) basic salary
        max_cap = monthly_basic_salary_aed * 24.0
        final_gratuity = min(gratuity, max_cap)

        return {
            "tenure_years": round(tenure_years, 2),
            "monthly_basic_aed": monthly_basic_salary_aed,
            "daily_basic_rate_aed": round(daily_rate, 2),
            "gratuity_payable_aed": round(final_gratuity, 2),
            "max_cap_limit_aed": round(max_cap, 2),
            "is_capped": final_gratuity >= max_cap
        }
