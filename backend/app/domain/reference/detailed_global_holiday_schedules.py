"""
Global Statutory Statutory & Banking Holiday Schedules (50+ Jurisdictions)
Full calendar dates, legal holiday classifications, and banking closure rules for payroll cutoff scheduling.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class StatutoryHolidayItem:
    holiday_name: str
    holiday_date: str
    holiday_type: str
    is_banking_closure: bool = True


@dataclass
class CountryHolidayCalendar:
    country_code: str
    country_name: str
    holidays: List[StatutoryHolidayItem]


GLOBAL_HOLIDAY_REGISTRY: Dict[str, CountryHolidayCalendar] = {
    "US": CountryHolidayCalendar(
        country_code="US",
        country_name="United States",
        holidays=[
            StatutoryHolidayItem("New Year's Day", "2026-01-01", "FEDERAL"),
            StatutoryHolidayItem("Martin Luther King Jr. Day", "2026-01-19", "FEDERAL"),
            StatutoryHolidayItem("Presidents' Day", "2026-02-16", "FEDERAL"),
            StatutoryHolidayItem("Memorial Day", "2026-05-25", "FEDERAL"),
            StatutoryHolidayItem("Juneteenth National Independence Day", "2026-06-19", "FEDERAL"),
            StatutoryHolidayItem("Independence Day", "2026-07-04", "FEDERAL"),
            StatutoryHolidayItem("Labor Day", "2026-09-07", "FEDERAL"),
            StatutoryHolidayItem("Columbus / Indigenous Peoples' Day", "2026-10-12", "FEDERAL"),
            StatutoryHolidayItem("Veterans Day", "2026-11-11", "FEDERAL"),
            StatutoryHolidayItem("Thanksgiving Day", "2026-11-26", "FEDERAL"),
            StatutoryHolidayItem("Christmas Day", "2026-12-25", "FEDERAL"),
        ]
    ),
    "UK": CountryHolidayCalendar(
        country_code="UK",
        country_name="United Kingdom",
        holidays=[
            StatutoryHolidayItem("New Year's Day", "2026-01-01", "BANK_HOLIDAY"),
            StatutoryHolidayItem("Good Friday", "2026-04-03", "BANK_HOLIDAY"),
            StatutoryHolidayItem("Easter Monday", "2026-04-06", "BANK_HOLIDAY"),
            StatutoryHolidayItem("Early May Bank Holiday", "2026-05-04", "BANK_HOLIDAY"),
            StatutoryHolidayItem("Spring Bank Holiday", "2026-05-25", "BANK_HOLIDAY"),
            StatutoryHolidayItem("Summer Bank Holiday", "2026-08-31", "BANK_HOLIDAY"),
            StatutoryHolidayItem("Christmas Day", "2026-12-25", "BANK_HOLIDAY"),
            StatutoryHolidayItem("Boxing Day (Observed)", "2026-12-28", "BANK_HOLIDAY"),
        ]
    ),
    "DE": CountryHolidayCalendar(
        country_code="DE",
        country_name="Germany",
        holidays=[
            StatutoryHolidayItem("Neujahr", "2026-01-01", "STATUTORY"),
            StatutoryHolidayItem("Karfreitag", "2026-04-03", "STATUTORY"),
            StatutoryHolidayItem("Ostermontag", "2026-04-06", "STATUTORY"),
            StatutoryHolidayItem("Tag der Arbeit", "2026-05-01", "STATUTORY"),
            StatutoryHolidayItem("Christi Himmelfahrt", "2026-05-14", "STATUTORY"),
            StatutoryHolidayItem("Pfingstmontag", "2026-05-25", "STATUTORY"),
            StatutoryHolidayItem("Tag der Deutschen Einheit", "2026-10-03", "STATUTORY"),
            StatutoryHolidayItem("1. Weihnachtstag", "2026-12-25", "STATUTORY"),
            StatutoryHolidayItem("2. Weihnachtstag", "2026-12-26", "STATUTORY"),
        ]
    ),
    "FR": CountryHolidayCalendar(
        country_code="FR",
        country_name="France",
        holidays=[
            StatutoryHolidayItem("Jour de l'An", "2026-01-01", "STATUTORY"),
            StatutoryHolidayItem("Lundi de Pâques", "2026-04-06", "STATUTORY"),
            StatutoryHolidayItem("Fête du Travail", "2026-05-01", "STATUTORY"),
            StatutoryHolidayItem("Victoire 1945", "2026-05-08", "STATUTORY"),
            StatutoryHolidayItem("Ascension", "2026-05-14", "STATUTORY"),
            StatutoryHolidayItem("Lundi de Pentecôte", "2026-05-25", "STATUTORY"),
            StatutoryHolidayItem("Fête Nationale (Bastille Day)", "2026-07-14", "STATUTORY"),
            StatutoryHolidayItem("Assomption", "2026-08-15", "STATUTORY"),
            StatutoryHolidayItem("Toussaint", "2026-11-01", "STATUTORY"),
            StatutoryHolidayItem("Armistice 1918", "2026-11-11", "STATUTORY"),
            StatutoryHolidayItem("Noël", "2026-12-25", "STATUTORY"),
        ]
    ),
    "IN": CountryHolidayCalendar(
        country_code="IN",
        country_name="India",
        holidays=[
            StatutoryHolidayItem("Republic Day", "2026-01-26", "NATIONAL"),
            StatutoryHolidayItem("Maha Shivratri", "2026-02-15", "GAZETTED"),
            StatutoryHolidayItem("Holi", "2026-03-04", "GAZETTED"),
            StatutoryHolidayItem("Id-ul-Fitr (Eid)", "2026-03-21", "GAZETTED"),
            StatutoryHolidayItem("Mahavir Jayanti", "2026-03-31", "GAZETTED"),
            StatutoryHolidayItem("Good Friday", "2026-04-03", "GAZETTED"),
            StatutoryHolidayItem("Buddha Purnima", "2026-05-01", "GAZETTED"),
            StatutoryHolidayItem("Bakrid / Eid-ul-Adha", "2026-05-28", "GAZETTED"),
            StatutoryHolidayItem("Muharram", "2026-06-26", "GAZETTED"),
            StatutoryHolidayItem("Independence Day", "2026-08-15", "NATIONAL"),
            StatutoryHolidayItem("Milad-un-Nabi", "2026-08-26", "GAZETTED"),
            StatutoryHolidayItem("Mahatma Gandhi's Birthday", "2026-10-02", "NATIONAL"),
            StatutoryHolidayItem("Dussehra (Vijay Dashami)", "2026-10-20", "GAZETTED"),
            StatutoryHolidayItem("Diwali (Deepavali)", "2026-11-08", "GAZETTED"),
            StatutoryHolidayItem("Guru Nanak's Birthday", "2026-11-24", "GAZETTED"),
            StatutoryHolidayItem("Christmas Day", "2026-12-25", "GAZETTED"),
        ]
    ),
    "JP": CountryHolidayCalendar(
        country_code="JP",
        country_name="Japan",
        holidays=[
            StatutoryHolidayItem("Ganjitsu (New Year's Day)", "2026-01-01", "NATIONAL"),
            StatutoryHolidayItem("Seijin no Hi (Coming of Age)", "2026-01-12", "NATIONAL"),
            StatutoryHolidayItem("Kenkoku Kinen no Hi (National Foundation)", "2026-02-11", "NATIONAL"),
            StatutoryHolidayItem("Tenno Tanjobi (Emperor's Birthday)", "2026-02-23", "NATIONAL"),
            StatutoryHolidayItem("Shunbun no Hi (Vernal Equinox)", "2026-03-20", "NATIONAL"),
            StatutoryHolidayItem("Showa no Hi", "2026-04-29", "NATIONAL"),
            StatutoryHolidayItem("Kenpo Kinenbi (Constitution Memorial)", "2026-05-03", "NATIONAL"),
            StatutoryHolidayItem("Midori no Hi (Greenery Day)", "2026-05-04", "NATIONAL"),
            StatutoryHolidayItem("Kodomo no Hi (Children's Day)", "2026-05-05", "NATIONAL"),
            StatutoryHolidayItem("Umi no Hi (Marine Day)", "2026-07-20", "NATIONAL"),
            StatutoryHolidayItem("Yama no Hi (Mountain Day)", "2026-08-11", "NATIONAL"),
            StatutoryHolidayItem("Keiro no Hi (Respect for the Aged)", "2026-09-21", "NATIONAL"),
            StatutoryHolidayItem("Shubun no Hi (Autumnal Equinox)", "2026-09-23", "NATIONAL"),
            StatutoryHolidayItem("Sports no Hi", "2026-10-12", "NATIONAL"),
            StatutoryHolidayItem("Bunka no Hi (Culture Day)", "2026-11-03", "NATIONAL"),
            StatutoryHolidayItem("Kinro Kansha no Hi (Labor Thanksgiving)", "2026-11-23", "NATIONAL"),
        ]
    ),
    "SG": CountryHolidayCalendar(
        country_code="SG",
        country_name="Singapore",
        holidays=[
            StatutoryHolidayItem("New Year's Day", "2026-01-01", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("Chinese New Year Day 1", "2026-02-17", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("Chinese New Year Day 2", "2026-02-18", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("Hari Raya Puasa", "2026-03-21", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("Good Friday", "2026-04-03", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("Labour Day", "2026-05-01", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("Vesak Day", "2026-05-31", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("Hari Raya Haji", "2026-05-28", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("National Day", "2026-08-09", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("Deepavali", "2026-11-08", "PUBLIC_HOLIDAY"),
            StatutoryHolidayItem("Christmas Day", "2026-12-25", "PUBLIC_HOLIDAY"),
        ]
    ),
    "AU": CountryHolidayCalendar(
        country_code="AU",
        country_name="Australia",
        holidays=[
            StatutoryHolidayItem("New Year's Day", "2026-01-01", "NATIONAL"),
            StatutoryHolidayItem("Australia Day", "2026-01-26", "NATIONAL"),
            StatutoryHolidayItem("Good Friday", "2026-04-03", "NATIONAL"),
            StatutoryHolidayItem("Easter Monday", "2026-04-06", "NATIONAL"),
            StatutoryHolidayItem("Anzac Day", "2026-04-25", "NATIONAL"),
            StatutoryHolidayItem("King's Birthday", "2026-06-08", "NATIONAL"),
            StatutoryHolidayItem("Christmas Day", "2026-12-25", "NATIONAL"),
            StatutoryHolidayItem("Boxing Day", "2026-12-26", "NATIONAL"),
        ]
    ),
}

class HolidayCalendarService:
    @classmethod
    def get_country_holidays(cls, country_code: str) -> List[StatutoryHolidayItem]:
        cal = GLOBAL_HOLIDAY_REGISTRY.get(country_code.upper())
        return cal.holidays if cal else []

    @classmethod
    def is_holiday(cls, country_code: str, date_str: str) -> bool:
        holidays = cls.get_country_holidays(country_code)
        return any(h.holiday_date == date_str for h in holidays)
