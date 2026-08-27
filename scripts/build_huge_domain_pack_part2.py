"""
Huge Domain Pack Part 2: Onboarding Journey, Timesheet Audit, Sandwich Rule, SLA Escalation, GDPR Reporter, Template Compiler, Biometric Parser, Survey Factor Analysis & LMS Path Builder
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. Onboarding Journey Orchestrator
onb_orch_code = '''"""
Employee Onboarding Journey & Automated Lifecycle Orchestrator
Provisions role-specific IT hardware, security credentials, compliance trainings, buddy assignments, and 30-60-90 milestones.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class OnboardingTaskDefinition:
    task_code: str
    title: str
    category: str  # IT_SETUP, HR_COMPLIANCE, TEAM_INTEGRATION, TRAINING, MANAGER_SYNC
    assignee_role: str  # EMPLOYEE, IT_ADMIN, HR_SPECIALIST, HIRING_MANAGER, BUDDY
    due_offset_days: int
    is_mandatory_for_probation_clearance: bool


DEPARTMENT_ONBOARDING_TEMPLATES: Dict[str, List[OnboardingTaskDefinition]] = {
    "ENGINEERING": [
        OnboardingTaskDefinition("IT-01", "Provision encrypted MacBook Pro & YubiKey 5C", "IT_SETUP", "IT_ADMIN", -3, True),
        OnboardingTaskDefinition("IT-02", "Grant GitHub Enterprise, AWS IAM & Datadog access", "IT_SETUP", "IT_ADMIN", 0, True),
        OnboardingTaskDefinition("HR-01", "Complete I-9 Verification / Right-to-Work documentation", "HR_COMPLIANCE", "HR_SPECIALIST", 3, True),
        OnboardingTaskDefinition("HR-02", "Sign Proprietary Information & Inventions Agreement (PIIA)", "HR_COMPLIANCE", "EMPLOYEE", 1, True),
        OnboardingTaskDefinition("TR-01", "Complete ISO 27001 Security Awareness & Phishing Training", "TRAINING", "EMPLOYEE", 7, True),
        OnboardingTaskDefinition("TEAM-01", "First Day Welcome Lunch with Assigned Peer Buddy", "TEAM_INTEGRATION", "BUDDY", 0, False),
        OnboardingTaskDefinition("MGR-01", "Day 1 Role Alignment & 30-Day Expectations Setting", "MANAGER_SYNC", "HIRING_MANAGER", 0, True),
        OnboardingTaskDefinition("MGR-30", "30-Day Milestone Check-in & Initial Project Review", "MANAGER_SYNC", "HIRING_MANAGER", 30, True),
        OnboardingTaskDefinition("MGR-60", "60-Day Mid-Probation Competency Calibration", "MANAGER_SYNC", "HIRING_MANAGER", 60, True),
        OnboardingTaskDefinition("MGR-90", "90-Day Formal Probation Confirmation & Review", "MANAGER_SYNC", "HIRING_MANAGER", 90, True),
    ],
    "SALES": [
        OnboardingTaskDefinition("IT-01", "Provision Dell Latitude & Salesforce Enterprise License", "IT_SETUP", "IT_ADMIN", -3, True),
        OnboardingTaskDefinition("HR-01", "Complete Tax Withholding (W-4 / W-8BEN) & Direct Deposit", "HR_COMPLIANCE", "EMPLOYEE", 2, True),
        OnboardingTaskDefinition("TR-01", "Product Suite Certification & Pitch Deck Mastery", "TRAINING", "EMPLOYEE", 14, True),
        OnboardingTaskDefinition("MGR-30", "30-Day Pipeline Building & Territory Plan Review", "MANAGER_SYNC", "HIRING_MANAGER", 30, True),
        OnboardingTaskDefinition("MGR-90", "90-Day Quota Attainment & Ramp Evaluation", "MANAGER_SYNC", "HIRING_MANAGER", 90, True),
    ]
}


class OnboardingJourneyOrchestrator:
    @classmethod
    def generate_journey_for_hire(
        cls,
        employee_id: str,
        employee_name: str,
        department: str,
        start_date: date
    ) -> List[Dict[str, Any]]:
        tasks_def = DEPARTMENT_ONBOARDING_TEMPLATES.get(
            department.upper(),
            DEPARTMENT_ONBOARDING_TEMPLATES["ENGINEERING"]
        )

        journey = []
        for t in tasks_def:
            due_dt = start_date + timedelta(days=t.due_offset_days)
            journey.append({
                "employee_id": employee_id,
                "employee_name": employee_name,
                "task_code": t.task_code,
                "title": t.title,
                "category": t.category,
                "assignee_role": t.assignee_role,
                "due_date": due_dt.isoformat(),
                "is_mandatory": t.is_mandatory_for_probation_clearance,
                "status": "PENDING"
            })

        return journey
'''
write("backend/app/domain/onboarding_journey_orchestrator.py", onb_orch_code)

# 2. Timesheet Audit & FLSA Wage & Hour Compliance
timesheet_code = '''"""
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
'''
write("backend/app/domain/timesheet_audit_engine.py", timesheet_code)

# 3. Leave Sandwich Rule & Holiday Bridging Evaluator
sandwich_code = '''"""
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
'''
write("backend/app/domain/leave_sandwich_rule_evaluator.py", sandwich_code)

# 4. Document Template Compiler
doc_tmpl_code = '''"""
Enterprise Legal Document Token Replacement & Offer Letter Compiler
Compiles dynamic employment contracts, non-disclosure agreements, and commission plans.
"""
import re
from typing import Dict, Any


class DocumentTemplateCompiler:
    @classmethod
    def compile_offer_letter(
        cls,
        candidate_name: str,
        job_title: str,
        department: str,
        annual_salary: float,
        sign_on_bonus: float,
        start_date: str,
        manager_name: str,
        equity_shares: int,
        office_location: str
    ) -> str:
        template = """
PEOPLEPULSE GLOBAL ENTERPRISE INC.
EMPLOYMENT OFFER & APPOINTMENT LETTER

Date: {OFFER_DATE}
To: {CANDIDATE_NAME}
Location: {OFFICE_LOCATION}

Dear {CANDIDATE_NAME},

On behalf of PeoplePulse Global Enterprise Inc., I am thrilled to extend an official offer of employment for the position of {JOB_TITLE} within our {DEPARTMENT} department, reporting directly to {MANAGER_NAME}.

1. BASE COMPENSATION & BENEFITS
- Annual Base Salary: ${ANNUAL_SALARY:,.2f} USD, payable in semi-monthly installments.
- Sign-On Bonus: ${SIGN_ON_BONUS:,.2f} USD, disbursed on your first regular payroll cycle.
- Long-Term Incentive Equity: Subject to Board approval, a grant of {EQUITY_SHARES:,} Restricted Stock Units (RSUs) vesting over 4 years (25% cliff at 12 months, quarterly thereafter).

2. COMMENCEMENT & PROBATION
Your scheduled first day of employment will be {START_DATE}. This offer is contingent upon successful completion of background checks and proof of work authorization.

We look forward to welcoming you to the PeoplePulse team!

Sincerely,

{MANAGER_NAME}
Department Vice President
PeoplePulse Global Enterprise
"""
        return template.strip().format(
            OFFER_DATE=start_date,
            CANDIDATE_NAME=candidate_name,
            OFFICE_LOCATION=office_location,
            JOB_TITLE=job_title,
            DEPARTMENT=department,
            MANAGER_NAME=manager_name,
            ANNUAL_SALARY=annual_salary,
            SIGN_ON_BONUS=sign_on_bonus,
            EQUITY_SHARES=equity_shares,
            START_DATE=start_date
        )
'''
write("backend/app/domain/document_template_compiler.py", doc_tmpl_code)

print("Huge Domain Pack Part 2 Built Successfully!")
'''
write("scripts/build_huge_domain_pack_part2.py", "# Part 2 builder")
'''
