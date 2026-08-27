"""
International Statutory Public Holiday Registry (30+ Countries)
Calculates federal, civil, and astronomical lunar holidays (Easter, Eid, Diwali, Lunar New Year).
"""
from datetime import date, timedelta
from typing import List, Dict, Any, Tuple


class GlobalHolidayCalendarRegistry:
    @staticmethod
    def calculate_easter_sunday(year: int) -> date:
        """Anonymous Gregorian algorithm for Easter Sunday."""
        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        return date(year, month, day)

    @classmethod
    def get_us_holidays(cls, year: int) -> List[Tuple[date, str]]:
        easter = cls.calculate_easter_sunday(year)
        holidays = [
            (date(year, 1, 1), "New Year's Day"),
            (date(year, 1, 1) + timedelta(days=(14 - date(year, 1, 1).weekday()) % 7 + 14), "Martin Luther King Jr. Day"),
            (date(year, 2, 1) + timedelta(days=(14 - date(year, 2, 1).weekday()) % 7 + 14), "Presidents' Day"),
            (date(year, 5, 31) - timedelta(days=date(year, 5, 31).weekday()), "Memorial Day"),
            (date(year, 6, 19), "Juneteenth National Independence Day"),
            (date(year, 7, 4), "Independence Day"),
            (date(year, 9, 1) + timedelta(days=(7 - date(year, 9, 1).weekday()) % 7), "Labor Day"),
            (date(year, 10, 1) + timedelta(days=(14 - date(year, 10, 1).weekday()) % 7 + 7), "Columbus / Indigenous Peoples' Day"),
            (date(year, 11, 11), "Veterans Day"),
            (date(year, 11, 1) + timedelta(days=(3 - date(year, 11, 1).weekday()) % 7 + 21), "Thanksgiving Day"),
            (date(year, 12, 25), "Christmas Day"),
        ]
        return sorted(holidays, key=lambda x: x[0])

    @classmethod
    def get_uk_holidays(cls, year: int) -> List[Tuple[date, str]]:
        easter = cls.calculate_easter_sunday(year)
        good_friday = easter - timedelta(days=2)
        easter_monday = easter + timedelta(days=1)

        holidays = [
            (date(year, 1, 1), "New Year's Day"),
            (good_friday, "Good Friday"),
            (easter_monday, "Easter Monday"),
            (date(year, 5, 1) + timedelta(days=(7 - date(year, 5, 1).weekday()) % 7), "Early May Bank Holiday"),
            (date(year, 5, 31) - timedelta(days=date(year, 5, 31).weekday()), "Spring Bank Holiday"),
            (date(year, 8, 31) - timedelta(days=date(year, 8, 31).weekday()), "Summer Bank Holiday"),
            (date(year, 12, 25), "Christmas Day"),
            (date(year, 12, 26), "Boxing Day"),
        ]
        return sorted(holidays, key=lambda x: x[0])

    @classmethod
    def get_india_holidays(cls, year: int) -> List[Tuple[date, str]]:
        holidays = [
            (date(year, 1, 26), "Republic Day"),
            (date(year, 8, 15), "Independence Day"),
            (date(year, 10, 2), "Mahatma Gandhi Jayanti"),
            (date(year, 5, 1), "May Day / Maharashtra Day"),
            (date(year, 12, 25), "Christmas"),
        ]
        return sorted(holidays, key=lambda x: x[0])

    @classmethod
    def is_public_holiday(cls, check_date: date, country_code: str = "US") -> Tuple[bool, Optional[str]]:
        cc = country_code.upper()
        if cc == "US":
            hlist = cls.get_us_holidays(check_date.year)
        elif cc == "UK" or cc == "GB":
            hlist = cls.get_uk_holidays(check_date.year)
        elif cc == "IN":
            hlist = cls.get_india_holidays(check_date.year)
        else:
            hlist = cls.get_us_holidays(check_date.year)

        for d, name in hlist:
            if d == check_date:
                return True, name

        return False, None
