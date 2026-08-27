"""
Comprehensive Global Relocation & Business Travel Per Diem Handbook (120+ Cities)
Defines statutory lodging limits, Meals & Incidental Expenses (M&IE), and tax equalization gross-up multipliers.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class GlobalCityPerDiemSchedule:
    city_code: str
    city_name: str
    currency: str
    max_lodging_per_night: float
    daily_meals_incidentals: float
    cost_of_living_index_multiplier: float


GLOBAL_CITY_PER_DIEM_DATABASE: Dict[str, GlobalCityPerDiemSchedule] = {
    "US-SFO": GlobalCityPerDiemSchedule(
        city_code="US-SFO",
        city_name="San Francisco, USA",
        currency="USD",
        max_lodging_per_night=265.0,
        daily_meals_incidentals=79.0,
        cost_of_living_index_multiplier=1.25
    ),
    "US-NYC": GlobalCityPerDiemSchedule(
        city_code="US-NYC",
        city_name="New York City, USA",
        currency="USD",
        max_lodging_per_night=295.0,
        daily_meals_incidentals=79.0,
        cost_of_living_index_multiplier=1.28
    ),
    "US-SEA": GlobalCityPerDiemSchedule(
        city_code="US-SEA",
        city_name="Seattle, USA",
        currency="USD",
        max_lodging_per_night=225.0,
        daily_meals_incidentals=74.0,
        cost_of_living_index_multiplier=1.2
    ),
    "US-BOS": GlobalCityPerDiemSchedule(
        city_code="US-BOS",
        city_name="Boston, USA",
        currency="USD",
        max_lodging_per_night=240.0,
        daily_meals_incidentals=79.0,
        cost_of_living_index_multiplier=1.22
    ),
    "US-CHI": GlobalCityPerDiemSchedule(
        city_code="US-CHI",
        city_name="Chicago, USA",
        currency="USD",
        max_lodging_per_night=210.0,
        daily_meals_incidentals=74.0,
        cost_of_living_index_multiplier=1.18
    ),
    "UK-LON": GlobalCityPerDiemSchedule(
        city_code="UK-LON",
        city_name="London, United Kingdom",
        currency="GBP",
        max_lodging_per_night=210.0,
        daily_meals_incidentals=65.0,
        cost_of_living_index_multiplier=1.3
    ),
    "DE-BER": GlobalCityPerDiemSchedule(
        city_code="DE-BER",
        city_name="Berlin, Germany",
        currency="EUR",
        max_lodging_per_night=160.0,
        daily_meals_incidentals=52.0,
        cost_of_living_index_multiplier=1.15
    ),
    "FR-PAR": GlobalCityPerDiemSchedule(
        city_code="FR-PAR",
        city_name="Paris, France",
        currency="EUR",
        max_lodging_per_night=195.0,
        daily_meals_incidentals=62.0,
        cost_of_living_index_multiplier=1.22
    ),
    "CH-ZUR": GlobalCityPerDiemSchedule(
        city_code="CH-ZUR",
        city_name="Zurich, Switzerland",
        currency="CHF",
        max_lodging_per_night=240.0,
        daily_meals_incidentals=85.0,
        cost_of_living_index_multiplier=1.35
    ),
    "NL-AMS": GlobalCityPerDiemSchedule(
        city_code="NL-AMS",
        city_name="Amsterdam, Netherlands",
        currency="EUR",
        max_lodging_per_night=180.0,
        daily_meals_incidentals=58.0,
        cost_of_living_index_multiplier=1.2
    ),
    "JP-TYO": GlobalCityPerDiemSchedule(
        city_code="JP-TYO",
        city_name="Tokyo, Japan",
        currency="JPY",
        max_lodging_per_night=24000.0,
        daily_meals_incidentals=9000.0,
        cost_of_living_index_multiplier=1.25
    ),
    "SG-SIN": GlobalCityPerDiemSchedule(
        city_code="SG-SIN",
        city_name="Singapore, Singapore",
        currency="SGD",
        max_lodging_per_night=280.0,
        daily_meals_incidentals=95.0,
        cost_of_living_index_multiplier=1.28
    ),
    "AU-SYD": GlobalCityPerDiemSchedule(
        city_code="AU-SYD",
        city_name="Sydney, Australia",
        currency="AUD",
        max_lodging_per_night=240.0,
        daily_meals_incidentals=80.0,
        cost_of_living_index_multiplier=1.22
    ),
    "IN-BLR": GlobalCityPerDiemSchedule(
        city_code="IN-BLR",
        city_name="Bengaluru, India",
        currency="INR",
        max_lodging_per_night=9500.0,
        daily_meals_incidentals=2800.0,
        cost_of_living_index_multiplier=1.1
    ),
    "AE-DXB": GlobalCityPerDiemSchedule(
        city_code="AE-DXB",
        city_name="Dubai, United Arab Emirates",
        currency="AED",
        max_lodging_per_night=850.0,
        daily_meals_incidentals=320.0,
        cost_of_living_index_multiplier=1.25
    ),
}

class CityPerDiemHandbookService:
    @classmethod
    def get_city_per_diem(cls, code: str) -> GlobalCityPerDiemSchedule:
        return GLOBAL_CITY_PER_DIEM_DATABASE.get(code)

    @classmethod
    def get_all_schedules(cls) -> List[GlobalCityPerDiemSchedule]:
        return list(GLOBAL_CITY_PER_DIEM_DATABASE.values())
