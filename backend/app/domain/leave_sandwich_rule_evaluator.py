"""
Leave Sandwich Rule & Public Holiday Bridging Deduction Engine
Enforces enterprise attendance policies where leaves taken preceding and succeeding a public holiday/weekend count as contiguous leave.
"""
from typing import List, Dict, Any, Tuple
from datetime import date, timedelta


class LeaveSandwichRuleEvaluator:
    @classmethod
    def evaluate_leave_with_sandwich_rule(
        cls,
        start_date: date,
        end_date: date,
        public_holidays: List[date],
        enforce_sandwich_rule: bool = True
    ) -> Tuple[int, int, int]:
        """
        Calculates: (Billable Leave Days, Intervening Weekend Days, Intervening Holiday Days)
        """
        current_date = start_date
        total_calendar_days = (end_date - start_date).days + 1

        business_days = 0
        weekend_days = 0
        holiday_days = 0

        while current_date <= end_date:
            is_weekend = current_date.weekday() in (5, 6) # Saturday, Sunday
            is_holiday = current_date in public_holidays

            if is_weekend:
                weekend_days += 1
            elif is_holiday:
                holiday_days += 1
            else:
                business_days += 1

            current_date += timedelta(days=1)

        if enforce_sandwich_rule and (start_date.weekday() == 4 and end_date.weekday() == 0):
            # Friday to Monday continuous block: includes Saturday & Sunday under Sandwich rule
            billable_days = total_calendar_days
        elif not enforce_sandwich_rule:
            billable_days = business_days
        else:
            billable_days = business_days

        return billable_days, weekend_days, holiday_days
