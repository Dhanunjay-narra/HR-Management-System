"""
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
