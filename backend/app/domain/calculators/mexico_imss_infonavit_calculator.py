"""
Mexico Labor Law (Ley Federal del Trabajo) IMSS Social Security, INFONAVIT Housing & Aguinaldo Engine
Calculates Salario Diario Integrado (SDI), Cuotas Obrero-Patronales (IMSS), and mandatory 15-day Christmas Aguinaldo bonus.
"""
from typing import Dict, Any


class MexicoLaborLawCalculator:
    # 2026 UMA (Unidad de Medida y Actualización) = ~MXN 115.00 daily
    DAILY_UMA_2026 = 115.00

    @classmethod
    def calculate_mexico_compensation(
        cls,
        monthly_gross_salary_mxn: float,
        tenure_years: float = 2.0
    ) -> Dict[str, Any]:
        daily_salary = monthly_gross_salary_mxn / 30.0

        # Vacation days: 12 days year 1, +2 days each subsequent year
        vacation_days = min(32, 12 + int(tenure_years - 1) * 2) if tenure_years >= 1 else 12
        prima_vacacional = (vacation_days * daily_salary) * 0.25  # 25% statutory vacation premium

        # Aguinaldo: Minimum 15 days of salary
        aguinaldo_bonus = round(daily_salary * 15.0, 2)

        # Salario Diario Integrado (SDI) factor
        sdi_factor = 1.0 + (15.0 / 365.0) + (vacation_days * 0.25 / 365.0)
        sdi = round(daily_salary * sdi_factor, 2)

        # Employee IMSS deductions (~2.75% of SDI)
        imss_employee = round(sdi * 30.0 * 0.0275, 2)

        # ISR Income Tax Withholding (~18% progressive estimate)
        isr_tax = round(monthly_gross_salary_mxn * 0.18, 2)

        net_monthly_pay = round(monthly_gross_salary_mxn - imss_employee - isr_tax, 2)

        # Employer obligations: INFONAVIT 5% + IMSS Employer (~22% of SDI)
        infonavit_employer = round(sdi * 30.0 * 0.05, 2)
        imss_employer = round(sdi * 30.0 * 0.22, 2)

        return {
            "monthly_gross_mxn": monthly_gross_salary_mxn,
            "daily_base_salary_mxn": round(daily_salary, 2),
            "salario_diario_integrado_sdi_mxn": sdi,
            "statutory_aguinaldo_christmas_bonus_mxn": aguinaldo_bonus,
            "statutory_prima_vacacional_mxn": round(prima_vacacional, 2),
            "imss_employee_deduction_mxn": imss_employee,
            "isr_income_tax_withheld_mxn": isr_tax,
            "net_monthly_take_home_mxn": net_monthly_pay,
            "employer_infonavit_housing_mxn": infonavit_employer,
            "employer_imss_contributions_mxn": imss_employer,
            "total_company_burden_cost_mxn": round(monthly_gross_salary_mxn + infonavit_employer + imss_employer, 2)
        }
