"""
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
