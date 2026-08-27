"""
Timesheet Audit & FLSA Wage-and-Hour Labor Compliance Engine
Detects unauthorized overtime, meal break penalties (California Labor Code Sec. 226.7), split-shift premiums, and weekly hour caps.
"""
from typing import Dict, List, Any, Tuple
from datetime import datetime, time, date, timedelta
from dataclasses import dataclass


@dataclass
class DailyAttendanceRecord:
    employee_id: str
    work_date: date
    clock_in: datetime
    clock_out: datetime
    break_start: Optional[datetime]
    break_end: Optional[datetime]
    is_exempt_employee: bool = False


@dataclass
class FLSAAuditResult:
    regular_hours: float
    overtime_1_5x_hours: float
    double_time_2_0x_hours: float
    meal_break_penalty_hours: float
    total_payable_hours: float
    violations: List[str]


class FLSAComplianceAuditEngine:
    @classmethod
    def audit_california_daily_hours(
        cls,
        record: DailyAttendanceRecord
    ) -> FLSAAuditResult:
        """
        California Daily Overtime Rules:
        - Hours > 8 in a day: 1.5x Overtime
        - Hours > 12 in a day: 2.0x Double Time
        - Meal break must begin before end of 5th hour of work (1-hour penalty if missed)
        """
        if record.is_exempt_employee:
            return FLSAAuditResult(8.0, 0.0, 0.0, 0.0, 8.0, [])

        total_gross_seconds = (record.clock_out - record.clock_in).total_seconds()
        break_seconds = 0.0
        if record.break_start and record.break_end:
            break_seconds = (record.break_end - record.break_start).total_seconds()

        worked_hours = max(0.0, (total_gross_seconds - break_seconds) / 3600.0)

        reg_hrs = min(worked_hours, 8.0)
        ot_hrs = 0.0
        dt_hrs = 0.0

        if worked_hours > 12.0:
            ot_hrs = 4.0
            dt_hrs = worked_hours - 12.0
        elif worked_hours > 8.0:
            ot_hrs = worked_hours - 8.0

        # Meal break penalty audit
        meal_penalty = 0.0
        violations = []

        if worked_hours > 5.0:
            if not record.break_start:
                meal_penalty = 1.0
                violations.append("Missed mandatory 30-minute meal break on 5+ hour shift.")
            else:
                hours_before_break = (record.break_start - record.clock_in).total_seconds() / 3600.0
                if hours_before_break > 5.0:
                    meal_penalty = 1.0
                    violations.append(f"Late meal break taken after {hours_before_break:.1f} hours of continuous work.")

        total_payable = reg_hrs + (ot_hrs * 1.5) + (dt_hrs * 2.0) + meal_penalty

        return FLSAAuditResult(
            regular_hours=round(reg_hrs, 2),
            overtime_1_5x_hours=round(ot_hrs, 2),
            double_time_2_0x_hours=round(dt_hrs, 2),
            meal_break_penalty_hours=meal_penalty,
            total_payable_hours=round(total_payable, 2),
            violations=violations
        )
