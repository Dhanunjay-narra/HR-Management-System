"""
France URSSAF Social Security Charges & Cadres Pension Calculator (2026 Plafond SS Rules)
Computes employee (CSG/CRDS, Retraite Complémentaire Agirc-Arrco) and employer cotisations patronales.
"""
from typing import Dict, Any


class FranceUrssafCalculator:
    # 2026 Plafond Mensuel de la Sécurité Sociale (PMSS) = EUR 3,925
    PMSS_2026 = 3925.0

    @classmethod
    def calculate_french_payroll(
        cls,
        monthly_gross_salary_eur: float,
        is_cadre: bool = True
    ) -> Dict[str, Any]:
        """
        Computes French employee social deductions (~22% of gross) and employer charges (~45% of gross).
        """
        # CSG & CRDS (9.7% on 98.25% of gross)
        csg_crds_base = monthly_gross_salary_eur * 0.9825
        csg_deductible = round(csg_crds_base * 0.068, 2)
        csg_non_deductible_crds = round(csg_crds_base * 0.029, 2)

        # Retraite de base (capped & uncapped)
        tranche_1 = min(monthly_gross_salary_eur, cls.PMSS_2026)
        retraite_base_t1 = round(tranche_1 * 0.069, 2)
        retraite_base_total = round(monthly_gross_salary_eur * 0.004, 2)

        # Retraite complémentaire Agirc-Arrco Tranche 1 (3.15%) and Tranche 2 (8.64%)
        agirc_t1 = round(tranche_1 * 0.0315, 2)
        tranche_2 = max(0.0, min(monthly_gross_salary_eur, cls.PMSS_2026 * 8) - cls.PMSS_2026)
        agirc_t2 = round(tranche_2 * 0.0864, 2)

        # Prévoyance Cadres
        prevoyance = round(tranche_1 * 0.015, 2) if is_cadre else 0.0

        total_employee_charges = (
            csg_deductible
            + csg_non_deductible_crds
            + retraite_base_t1
            + retraite_base_total
            + agirc_t1
            + agirc_t2
            + prevoyance
        )

        # Employer social charges (~42% average across sickness, family, pension, accident)
        employer_charges = round(monthly_gross_salary_eur * 0.42, 2)
        net_before_tax = round(monthly_gross_salary_eur - total_employee_charges, 2)

        return {
            "monthly_gross_salary_eur": monthly_gross_salary_eur,
            "is_cadre_status": is_cadre,
            "total_employee_social_deductions_eur": round(total_employee_charges, 2),
            "effective_employee_charge_rate_pct": round((total_employee_charges / monthly_gross_salary_eur) * 100.0, 1),
            "net_salary_before_income_tax_eur": net_before_tax,
            "total_employer_cotisations_patronales_eur": employer_charges,
            "total_super_gross_company_cost_eur": round(monthly_gross_salary_eur + employer_charges, 2),
            "charge_breakdown": {
                "csg_crds": round(csg_deductible + csg_non_deductible_crds, 2),
                "retraite_base": round(retraite_base_t1 + retraite_base_total, 2),
                "retraite_complementaire_agirc_arrco": round(agirc_t1 + agirc_t2, 2),
                "prevoyance_cadre": prevoyance
            }
        }
