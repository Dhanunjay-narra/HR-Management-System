"""
Singapore Central Provident Fund (CPF) Statutory Contribution Engine (2026 Regulations)
Calculates employee and employer contribution splits across Ordinary Account (OA), Special Account (SA), and MediSave Account (MA) based on age tiers.
"""
from typing import Dict, Any


class SingaporeCPFCalculator:
    # Monthly Wage Ceiling in 2026: SGD 8,000
    CPF_MONTHLY_WAGE_CEILING = 8000.0

    @classmethod
    def calculate_cpf(
        cls,
        monthly_ordinary_wage_sgd: float,
        employee_age: int
    ) -> Dict[str, Any]:
        capped_wage = min(monthly_ordinary_wage_sgd, cls.CPF_MONTHLY_WAGE_CEILING)

        if employee_age <= 55:
            ee_rate = 0.20
            er_rate = 0.17
            oa_split = 0.6217
            sa_split = 0.1621
            ma_split = 0.2162
        elif employee_age <= 60:
            ee_rate = 0.15
            er_rate = 0.145
            oa_split = 0.4068
            sa_split = 0.2373
            ma_split = 0.3559
        elif employee_age <= 65:
            ee_rate = 0.095
            er_rate = 0.11
            oa_split = 0.1707
            sa_split = 0.3171
            ma_split = 0.5122
        elif employee_age <= 70:
            ee_rate = 0.07
            er_rate = 0.085
            oa_split = 0.0645
            sa_split = 0.3226
            ma_split = 0.6129
        else:
            ee_rate = 0.05
            er_rate = 0.075
            oa_split = 0.08
            sa_split = 0.08
            ma_split = 0.84

        ee_contrib = round(capped_wage * ee_rate, 2)
        er_contrib = round(capped_wage * er_rate, 2)
        total_cpf = ee_contrib + er_contrib

        oa_amount = round(total_cpf * oa_split, 2)
        sa_amount = round(total_cpf * sa_split, 2)
        ma_amount = round(total_cpf - oa_amount - sa_amount, 2)

        net_take_home = round(monthly_ordinary_wage_sgd - ee_contrib, 2)

        return {
            "gross_ordinary_wage_sgd": monthly_ordinary_wage_sgd,
            "capped_wage_subject_to_cpf": capped_wage,
            "employee_age": employee_age,
            "employee_contribution_rate_pct": round(ee_rate * 100.0, 1),
            "employer_contribution_rate_pct": round(er_rate * 100.0, 1),
            "employee_cpf_deduction_sgd": ee_contrib,
            "employer_cpf_contribution_sgd": er_contrib,
            "total_cpf_remittance_sgd": total_cpf,
            "account_breakdown": {
                "ordinary_account_oa_sgd": oa_amount,
                "special_account_sa_sgd": sa_amount,
                "medisave_account_ma_sgd": ma_amount
            },
            "net_monthly_pay_sgd": net_take_home
        }
