"""
Global Relocation & Talent Mobility Master Matrix (Complete)
Defines international moving budgets, settling-in allowances, statutory tax gross-up rates, and temporary housing durations.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class CityRelocationPolicy:
    city_id: str
    city_name: str
    currency: str
    max_lump_sum_budget: float
    settling_in_stipend: float
    estimated_tax_gross_up_rate: float
    temporary_housing_days: int
    relocation_notes: str


COMPLETE_RELOCATION_DATABASE: Dict[str, CityRelocationPolicy] = {
    "LOC-USA-SF": CityRelocationPolicy(
        city_id="LOC-USA-SF",
        city_name="San Francisco, USA",
        currency="USD",
        max_lump_sum_budget=25000.0,
        settling_in_stipend=7500.0,
        estimated_tax_gross_up_rate=0.42,
        temporary_housing_days=60,
        relocation_notes="High cost of living premium with comprehensive housing subsidy."
    ),
    "LOC-USA-NY": CityRelocationPolicy(
        city_id="LOC-USA-NY",
        city_name="New York City, USA",
        currency="USD",
        max_lump_sum_budget=25000.0,
        settling_in_stipend=7500.0,
        estimated_tax_gross_up_rate=0.43,
        temporary_housing_days=60,
        relocation_notes="Tier 1 relocation package with full moving allowance."
    ),
    "LOC-USA-AT": CityRelocationPolicy(
        city_id="LOC-USA-AT",
        city_name="Austin, USA",
        currency="USD",
        max_lump_sum_budget=18000.0,
        settling_in_stipend=5000.0,
        estimated_tax_gross_up_rate=0.32,
        temporary_housing_days=45,
        relocation_notes="Standard US domestic transfer package."
    ),
    "LOC-GBR-LO": CityRelocationPolicy(
        city_id="LOC-GBR-LO",
        city_name="London, UK",
        currency="GBP",
        max_lump_sum_budget=18000.0,
        settling_in_stipend=4500.0,
        estimated_tax_gross_up_rate=0.4,
        temporary_housing_days=60,
        relocation_notes="UK international relocation with Certificate of Sponsorship."
    ),
    "LOC-DEU-BE": CityRelocationPolicy(
        city_id="LOC-DEU-BE",
        city_name="Berlin, Germany",
        currency="EUR",
        max_lump_sum_budget=15000.0,
        settling_in_stipend=4000.0,
        estimated_tax_gross_up_rate=0.45,
        temporary_housing_days=60,
        relocation_notes="EU Blue Card relocation and temporary apartment."
    ),
    "LOC-CHE-ZU": CityRelocationPolicy(
        city_id="LOC-CHE-ZU",
        city_name="Zurich, Switzerland",
        currency="CHF",
        max_lump_sum_budget=22000.0,
        settling_in_stipend=6000.0,
        estimated_tax_gross_up_rate=0.28,
        temporary_housing_days=60,
        relocation_notes="Swiss Cantonal work permit relocation support."
    ),
    "LOC-SGP-SI": CityRelocationPolicy(
        city_id="LOC-SGP-SI",
        city_name="Singapore, Singapore",
        currency="SGD",
        max_lump_sum_budget=20000.0,
        settling_in_stipend=5500.0,
        estimated_tax_gross_up_rate=0.22,
        temporary_housing_days=45,
        relocation_notes="Employment Pass (EP) processing with flight allowance."
    ),
    "LOC-JPN-TO": CityRelocationPolicy(
        city_id="LOC-JPN-TO",
        city_name="Tokyo, Japan",
        currency="JPY",
        max_lump_sum_budget=2000000.0,
        settling_in_stipend=500000.0,
        estimated_tax_gross_up_rate=0.3,
        temporary_housing_days=60,
        relocation_notes="Engineer/Specialist in Humanities visa transfer."
    ),
    "LOC-AUS-SY": CityRelocationPolicy(
        city_id="LOC-AUS-SY",
        city_name="Sydney, Australia",
        currency="AUD",
        max_lump_sum_budget=22000.0,
        settling_in_stipend=5000.0,
        estimated_tax_gross_up_rate=0.35,
        temporary_housing_days=60,
        relocation_notes="TSS 482 visa sponsorship and settling-in stipend."
    ),
    "LOC-IND-BL": CityRelocationPolicy(
        city_id="LOC-IND-BL",
        city_name="Bengaluru, India",
        currency="INR",
        max_lump_sum_budget=600000.0,
        settling_in_stipend=150000.0,
        estimated_tax_gross_up_rate=0.3,
        temporary_housing_days=30,
        relocation_notes="Domestic metro transfer with corporate guest house."
    ),
}

class CityRelocationService:
    @classmethod
    def get_city_policy(cls, city_id: str) -> CityRelocationPolicy:
        return COMPLETE_RELOCATION_DATABASE.get(city_id)

    @classmethod
    def get_all_cities(cls) -> List[CityRelocationPolicy]:
        return list(COMPLETE_RELOCATION_DATABASE.values())
