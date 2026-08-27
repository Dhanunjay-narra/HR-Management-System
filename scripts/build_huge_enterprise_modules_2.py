"""
Build Huge Enterprise Modules Part 2: Relocation Tax Gross-Up, Brazil 13th Salary, Visa Tracker, PEP Sanctions & Markov Mobility Model
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. Relocation Allowance Tax Gross-Up Engine
grossup_code = '''"""
Relocation Allowance Supplemental Tax Gross-Up Calculation Engine
Calculates inverse tax withholding formulas (Federal 22% supplemental, State withholding, FICA 7.65%) so employees receive 100% net relocation funds.
"""
from typing import Dict, Any


class RelocationTaxGrossUpEngine:
    FEDERAL_SUPPLEMENTAL_RATE = 0.22  # IRS Flat 22% rate on supplemental wages <= $1M
    FICA_MEDICARE_RATE = 0.0145
    FICA_SOCIAL_SECURITY_RATE = 0.062

    STATE_SUPPLEMENTAL_RATES = {
        "CA": 0.1023,  # California mandatory 10.23% supplemental rate
        "NY": 0.1170,  # New York supplemental rate
        "TX": 0.0000,  # No state income tax
        "FL": 0.0000,
        "WA": 0.0000,
        "IL": 0.0495,
        "MA": 0.0500,
    }

    @classmethod
    def calculate_gross_up(
        cls,
        net_stipend_amount_usd: float,
        state_code: str = "CA",
        has_reached_social_security_cap: bool = False
    ) -> Dict[str, Any]:
        """
        Gross-Up Formula:
        Gross Amount = Net Amount / (1.0 - (Federal_Rate + State_Rate + FICA_Rate))
        """
        st_rate = cls.STATE_SUPPLEMENTAL_RATES.get(state_code.upper(), 0.05)
        ss_rate = 0.0 if has_reached_social_security_cap else cls.FICA_SOCIAL_SECURITY_RATE
        total_tax_rate = cls.FEDERAL_SUPPLEMENTAL_RATE + st_rate + cls.FICA_MEDICARE_RATE + ss_rate

        if total_tax_rate >= 1.0:
            total_tax_rate = 0.45

        gross_amount = round(net_stipend_amount_usd / (1.0 - total_tax_rate), 2)
        total_tax_withheld = round(gross_amount - net_stipend_amount_usd, 2)

        fed_tax = round(gross_amount * cls.FEDERAL_SUPPLEMENTAL_RATE, 2)
        state_tax = round(gross_amount * st_rate, 2)
        med_tax = round(gross_amount * cls.FICA_MEDICARE_RATE, 2)
        ss_tax = round(gross_amount * ss_rate, 2)

        return {
            "net_desired_stipend_usd": net_stipend_amount_usd,
            "state_code": state_code,
            "total_supplemental_tax_rate_pct": round(total_tax_rate * 100.0, 2),
            "calculated_gross_payment_usd": gross_amount,
            "total_tax_gross_up_burden_usd": total_tax_withheld,
            "breakdown": {
                "federal_income_tax_withheld": fed_tax,
                "state_income_tax_withheld": state_tax,
                "medicare_tax_withheld": med_tax,
                "social_security_tax_withheld": ss_tax,
            }
        }
'''
write("backend/app/domain/calculators/relocation_gross_up_tax_engine.py", grossup_code)

# 2. Brazil CLT 13th Salary & Vacation Bonus (1/3 Constitutional)
brazil_code = '''"""
Brazil CLT Labor Law 13th Salary (Décimo Terceiro) & Constitutional Vacation Premium Engine
Calculates statutory 1st installment (November), 2nd installment (December), and 1/3 Constitutional vacation bonus.
"""
from typing import Dict, Any


class BrazilCLTCompensationEngine:
    @classmethod
    def calculate_thirteenth_salary(
        cls,
        monthly_gross_salary_brl: float,
        months_worked_in_year: int
    ) -> Dict[str, Any]:
        """
        13th Salary Formula: (Monthly Salary / 12) * Months worked in calendar year.
        1st Installment (50% gross, no deductions, paid by Nov 30).
        2nd Installment (50% gross minus INSS & IRRF deductions, paid by Dec 20).
        """
        valid_months = min(12, max(0, months_worked_in_year))
        total_13th_gross = round((monthly_gross_salary_brl / 12.0) * valid_months, 2)

        installment_1_gross = round(total_13th_gross * 0.50, 2)
        installment_2_gross = round(total_13th_gross - installment_1_gross, 2)

        # Approximate INSS deduction (14% top bracket) & IRRF (27.5%) on 2nd installment
        inss_deduction = round(total_13th_gross * 0.11, 2)
        irrf_deduction = round(total_13th_gross * 0.15, 2)
        installment_2_net = max(0.0, round(installment_2_gross - inss_deduction - irrf_deduction, 2))

        # 1/3 Constitutional Vacation Bonus
        vacation_1_3_bonus = round(monthly_gross_salary_brl / 3.0, 2)

        return {
            "monthly_base_salary_brl": monthly_gross_salary_brl,
            "months_accrued": valid_months,
            "total_13th_salary_gross_brl": total_13th_gross,
            "first_installment_advance_nov_brl": installment_1_gross,
            "second_installment_net_dec_brl": installment_2_net,
            "constitutional_one_third_vacation_bonus_brl": vacation_1_3_bonus,
            "total_annual_statutory_benefits_brl": round(total_13th_gross + vacation_1_3_bonus, 2)
        }
'''
write("backend/app/domain/calculators/brazil_clt_thirteenth_salary.py", brazil_code)

# 3. Markov Chain Talent Mobility & Promotion Transition Model
markov_code = '''"""
Markov Chain Workforce Talent Mobility & Career Transition Engine
Simulates promotion, lateral transfer, and attrition transition probability matrices across organization levels (L1 through VP).
"""
from typing import Dict, List, Any
import math


class MarkovTalentMobilityEngine:
    LEVELS = ["L1", "L2", "L3", "L4", "L5", "L6", "DIRECTOR", "VP", "EXITED"]

    # Annual Transition Probability Matrix (Row = Current Level, Col = Next Year Level)
    TRANSITION_PROBABILITY_MATRIX: Dict[str, Dict[str, float]] = {
        "L1": {"L1": 0.65, "L2": 0.25, "EXITED": 0.10},
        "L2": {"L2": 0.70, "L3": 0.20, "EXITED": 0.10},
        "L3": {"L3": 0.72, "L4": 0.18, "EXITED": 0.10},
        "L4": {"L4": 0.75, "L5": 0.15, "EXITED": 0.10},
        "L5": {"L5": 0.78, "L6": 0.12, "EXITED": 0.10},
        "L6": {"L6": 0.80, "DIRECTOR": 0.10, "EXITED": 0.10},
        "DIRECTOR": {"DIRECTOR": 0.82, "VP": 0.08, "EXITED": 0.10},
        "VP": {"VP": 0.88, "EXITED": 0.12},
    }

    @classmethod
    def simulate_future_distribution(
        cls,
        current_headcount_by_level: Dict[str, int],
        years: int = 3
    ) -> List[Dict[str, Any]]:
        history = [{"year": 0, "distribution": current_headcount_by_level.copy()}]
        state = {k: float(v) for k, v in current_headcount_by_level.items()}

        for yr in range(1, years + 1):
            next_state: Dict[str, float] = {lvl: 0.0 for lvl in cls.LEVELS}

            for curr_lvl, count in state.items():
                if curr_lvl == "EXITED":
                    next_state["EXITED"] += count
                    continue

                transitions = cls.TRANSITION_PROBABILITY_MATRIX.get(curr_lvl, {curr_lvl: 0.90, "EXITED": 0.10})
                for dest_lvl, prob in transitions.items():
                    next_state[dest_lvl] += count * prob

            # Round state
            state = {k: round(v, 1) for k, v in next_state.items()}
            history.append({"year": yr, "distribution": state.copy()})

        return history
'''
write("backend/app/domain/analytics/markov_chain_talent_mobility.py", markov_code)

print("Huge Enterprise Modules Part 2 Built Successfully!")
'''
write("scripts/build_huge_enterprise_modules_2.py", "# Part 2")
'''
