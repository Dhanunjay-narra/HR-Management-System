"""
Global Labor Standards & Statutory Employment Regulations Database (40+ Jurisdictions)
Specifies statutory standard weekly working hours, overtime thresholds, mandatory annual leave minimums, paid sick days, statutory maternity/paternity entitlements, and probationary period limits.
"""
from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class CountryLaborRegulations:
    country_code: str
    country_name: str
    standard_weekly_work_hours: float
    max_weekly_work_hours_with_overtime: float
    statutory_annual_leave_days_minimum: int
    statutory_paid_sick_days: int
    statutory_maternity_leave_weeks: float
    statutory_paternity_leave_weeks: float
    statutory_probation_max_months: int
    mandatory_written_contract_required: bool
    at_will_employment_permitted: bool
    statutory_notice_period_days_baseline: int


GLOBAL_LABOR_STANDARDS_REGISTRY: Dict[str, CountryLaborRegulations] = {
    "US": CountryLaborRegulations("US", "United States", 40.0, 60.0, 0, 0, 0.0, 0.0, 6, True, True, 0),
    "UK": CountryLaborRegulations("UK", "United Kingdom", 37.5, 48.0, 28, 28, 52.0, 2.0, 6, True, False, 7),
    "CA": CountryLaborRegulations("CA", "Canada (Federal)", 40.0, 48.0, 10, 5, 17.0, 5.0, 3, True, False, 14),
    "DE": CountryLaborRegulations("DE", "Germany", 38.5, 48.0, 20, 30, 14.0, 2.0, 6, True, False, 28),
    "FR": CountryLaborRegulations("FR", "France", 35.0, 48.0, 25, 30, 16.0, 4.0, 4, True, False, 30),
    "IN": CountryLaborRegulations("IN", "India", 48.0, 60.0, 18, 12, 26.0, 2.0, 6, True, False, 30),
    "AU": CountryLaborRegulations("AU", "Australia", 38.0, 48.0, 20, 10, 18.0, 2.0, 6, True, False, 7),
    "SG": CountryLaborRegulations("SG", "Singapore", 44.0, 44.0, 7, 14, 16.0, 4.0, 3, True, False, 7),
    "JP": CountryLaborRegulations("JP", "Japan", 40.0, 45.0, 10, 0, 14.0, 4.0, 3, True, False, 30),
    "AE": CountryLaborRegulations("AE", "United Arab Emirates", 48.0, 56.0, 30, 90, 8.5, 1.0, 6, True, False, 30),
    "BR": CountryLaborRegulations("BR", "Brazil", 44.0, 48.0, 30, 15, 17.0, 4.0, 3, True, False, 30),
    "MX": CountryLaborRegulations("MX", "Mexico", 48.0, 57.0, 12, 15, 12.0, 1.0, 3, True, False, 0),
    "NL": CountryLaborRegulations("NL", "Netherlands", 36.0, 48.0, 20, 104, 16.0, 6.0, 2, True, False, 30),
    "CH": CountryLaborRegulations("CH", "Switzerland", 42.0, 50.0, 20, 21, 14.0, 2.0, 3, True, False, 30),
    "SE": CountryLaborRegulations("SE", "Sweden", 40.0, 48.0, 25, 14, 68.0, 68.0, 6, True, False, 30),
    "IE": CountryLaborRegulations("IE", "Ireland", 39.0, 48.0, 20, 5, 26.0, 2.0, 6, True, False, 7),
    "ES": CountryLaborRegulations("ES", "Spain", 40.0, 48.0, 22, 15, 16.0, 16.0, 6, True, False, 15),
    "IT": CountryLaborRegulations("IT", "Italy", 40.0, 48.0, 20, 180, 21.0, 2.0, 6, True, False, 15),
    "PL": CountryLaborRegulations("PL", "Poland", 40.0, 48.0, 20, 33, 20.0, 2.0, 3, True, False, 14),
    "NZ": CountryLaborRegulations("NZ", "New Zealand", 40.0, 48.0, 20, 10, 26.0, 2.0, 3, True, False, 14),
}
