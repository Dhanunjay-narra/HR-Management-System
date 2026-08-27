"""
Fixed Asset Depreciation Schedule Engine
Calculates Straight-Line (SLD), Double Declining Balance (DDB 200%), 150% DB, and US MACRS Half-Year Convention tables.
"""
from typing import List, Dict, Any


class AssetDepreciationEngine:
    MACRS_5_YEAR = [0.20, 0.32, 0.192, 0.1152, 0.1152, 0.0576]
    MACRS_7_YEAR = [0.1429, 0.2449, 0.1749, 0.1249, 0.0893, 0.0892, 0.0893, 0.0446]

    @classmethod
    def calculate_straight_line(
        cls,
        initial_cost: float,
        salvage_value: float,
        useful_life_years: int
    ) -> List[Dict[str, Any]]:
        depreciable_base = initial_cost - salvage_value
        annual_depreciation = round(depreciable_base / useful_life_years, 2)
        accumulated = 0.0
        book_value = initial_cost
        schedule = []

        for year in range(1, useful_life_years + 1):
            accumulated += annual_depreciation
            book_value = max(salvage_value, round(initial_cost - accumulated, 2))
            schedule.append({
                "year": year,
                "depreciation_expense": annual_depreciation,
                "accumulated_depreciation": round(accumulated, 2),
                "ending_book_value": book_value
            })

        return schedule

    @classmethod
    def calculate_double_declining_balance(
        cls,
        initial_cost: float,
        salvage_value: float,
        useful_life_years: int
    ) -> List[Dict[str, Any]]:
        rate = 2.0 / useful_life_years
        book_value = initial_cost
        accumulated = 0.0
        schedule = []

        for year in range(1, useful_life_years + 1):
            expense = round(book_value * rate, 2)
            if book_value - expense < salvage_value:
                expense = max(0.0, round(book_value - salvage_value, 2))

            accumulated += expense
            book_value = max(salvage_value, round(book_value - expense, 2))

            schedule.append({
                "year": year,
                "depreciation_expense": expense,
                "accumulated_depreciation": round(accumulated, 2),
                "ending_book_value": book_value
            })

        return schedule
