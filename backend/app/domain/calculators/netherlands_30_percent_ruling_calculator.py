"""
Netherlands 30% Tax Exemption Ruling & Box 1 Progressive Bracket Calculator (2026 Dutch Tax Plan)
Calculates the 30% tax-free expat allowance and progressive Box 1 wage withholding.
"""
from typing import Dict, Any


class NetherlandsPayrollCalculator:
    # 2026 Dutch Box 1 Brackets
    BRACKET_1_LIMIT_EUR = 75518.0
    BRACKET_1_RATE = 0.3697 # 36.97%
    BRACKET_2_RATE = 0.4950 # 49.50%

    @classmethod
    def calculate_dutch_payroll(
        cls,
        annual_gross_salary_eur: float,
        has_30_percent_ruling: bool = True
    ) -> Dict[str, Any]:
        tax_free_allowance = 0.0
        taxable_wages = annual_gross_salary_eur

        if has_30_percent_ruling:
            # 30% of gross is disbursed completely tax-free
            tax_free_allowance = round(annual_gross_salary_eur * 0.30, 2)
            taxable_wages = annual_gross_salary_eur - tax_free_allowance

        # Box 1 progressive tax calculation
        tax = 0.0
        if taxable_wages > cls.BRACKET_1_LIMIT_EUR:
            tax += cls.BRACKET_1_LIMIT_EUR * cls.BRACKET_1_RATE
            tax += (taxable_wages - cls.BRACKET_1_LIMIT_EUR) * cls.BRACKET_2_RATE
        else:
            tax += taxable_wages * cls.BRACKET_1_RATE

        tax = round(tax, 2)
        annual_net = round(annual_gross_salary_eur - tax, 2)

        return {
            "gross_annual_eur": annual_gross_salary_eur,
            "has_30_percent_ruling": has_30_percent_ruling,
            "tax_free_allowance_eur": tax_free_allowance,
            "taxable_wages_box_1_eur": round(taxable_wages, 2),
            "annual_wage_tax_withheld_eur": tax,
            "annual_net_take_home_eur": annual_net,
            "monthly_net_pay_eur": round(annual_net / 12.0, 2),
            "effective_tax_rate_pct": round((tax / annual_gross_salary_eur) * 100.0, 2)
        }
