"""
Global Business Travel & Relocation Per Diem Standard Rates (GSA / IRS & International)
Prescribes standard lodging caps and Meals & Incidental Expense (M&IE) per diems across key business hubs.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class CityPerDiemRate:
    city_code: str
    city_name: str
    currency: str
    max_lodging_rate_per_night: float
    daily_meal_incidental_allowance: float


GLOBAL_PER_DIEM_REGISTRY: Dict[str, CityPerDiemRate] = {
    "US-SFO": CityPerDiemRate(
        city_code="US-SFO",
        city_name="San Francisco, CA",
        currency="USD",
        max_lodging_rate_per_night=245.0,
        daily_meal_incidental_allowance=79.0
    ),
    "US-NYC": CityPerDiemRate(
        city_code="US-NYC",
        city_name="New York City, NY",
        currency="USD",
        max_lodging_rate_per_night=280.0,
        daily_meal_incidental_allowance=79.0
    ),
    "US-SEA": CityPerDiemRate(
        city_code="US-SEA",
        city_name="Seattle, WA",
        currency="USD",
        max_lodging_rate_per_night=215.0,
        daily_meal_incidental_allowance=74.0
    ),
    "US-AUS": CityPerDiemRate(
        city_code="US-AUS",
        city_name="Austin, TX",
        currency="USD",
        max_lodging_rate_per_night=175.0,
        daily_meal_incidental_allowance=69.0
    ),
    "UK-LON": CityPerDiemRate(
        city_code="UK-LON",
        city_name="London",
        currency="GBP",
        max_lodging_rate_per_night=195.0,
        daily_meal_incidental_allowance=65.0
    ),
    "DE-BER": CityPerDiemRate(
        city_code="DE-BER",
        city_name="Berlin",
        currency="EUR",
        max_lodging_rate_per_night=150.0,
        daily_meal_incidental_allowance=50.0
    ),
    "FR-PAR": CityPerDiemRate(
        city_code="FR-PAR",
        city_name="Paris",
        currency="EUR",
        max_lodging_rate_per_night=185.0,
        daily_meal_incidental_allowance=60.0
    ),
    "CH-ZUR": CityPerDiemRate(
        city_code="CH-ZUR",
        city_name="Zurich",
        currency="CHF",
        max_lodging_rate_per_night=230.0,
        daily_meal_incidental_allowance=80.0
    ),
    "JP-TYO": CityPerDiemRate(
        city_code="JP-TYO",
        city_name="Tokyo",
        currency="JPY",
        max_lodging_rate_per_night=22000.0,
        daily_meal_incidental_allowance=8500.0
    ),
    "SG-SIN": CityPerDiemRate(
        city_code="SG-SIN",
        city_name="Singapore",
        currency="SGD",
        max_lodging_rate_per_night=260.0,
        daily_meal_incidental_allowance=90.0
    ),
    "AU-SYD": CityPerDiemRate(
        city_code="AU-SYD",
        city_name="Sydney",
        currency="AUD",
        max_lodging_rate_per_night=220.0,
        daily_meal_incidental_allowance=75.0
    ),
    "IN-BLR": CityPerDiemRate(
        city_code="IN-BLR",
        city_name="Bengaluru",
        currency="INR",
        max_lodging_rate_per_night=8500.0,
        daily_meal_incidental_allowance=2500.0
    ),
}

class PerDiemRateService:
    @classmethod
    def get_city_rate(cls, city_code: str) -> CityPerDiemRate:
        return GLOBAL_PER_DIEM_REGISTRY.get(city_code)

    @classmethod
    def get_all_rates(cls) -> List[CityPerDiemRate]:
        return list(GLOBAL_PER_DIEM_REGISTRY.values())
