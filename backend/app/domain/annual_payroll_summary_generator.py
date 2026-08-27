"""
Annual Payroll Tax & Wage Reconciliation Report Generator (IRS Form W-2 / UK P60 / India Form 16)
Consolidates cumulative annual gross wages, FICA wages, federal/state tax withheld, and retirement contributions.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class FormW2Record:
    employee_ssn_masked: str
    employee_name: str
    employee_address: str
    employer_ein: str
    employer_name: str
    tax_year: int
    box_1_wages_tips_other_comp: float
    box_2_federal_income_tax_withheld: float
    box_3_social_security_wages: float
    box_4_social_security_tax_withheld: float
    box_5_medicare_wages_and_tips: float
    box_6_medicare_tax_withheld: float
    box_12a_code_d_401k: float
    box_12b_code_w_hsa: float
    box_14_other_state_disability: float
    box_15_state_code: str
    box_16_state_wages: float
    box_17_state_income_tax_withheld: float


class AnnualTaxFormGenerator:
    @classmethod
    def compile_w2_annual_statement(
        cls,
        employee_info: Dict[str, Any],
        annual_payroll_summary: Dict[str, Any],
        tax_year: int = 2026
    ) -> FormW2Record:
        gross = annual_payroll_summary.get("total_gross_earnings", 0.0)
        pre_tax_401k = annual_payroll_summary.get("total_401k_contributions", 0.0)
        pre_tax_hsa = annual_payroll_summary.get("total_hsa_contributions", 0.0)
        pre_tax_health = annual_payroll_summary.get("total_health_premiums", 0.0)

        # Box 1 is taxable federal wages after pre-tax retirement & cafeteria plan deductions
        box_1 = max(0.0, gross - pre_tax_401k - pre_tax_hsa - pre_tax_health)
        
        # Social security wages capped at annual base ($176,100 in 2026)
        ss_wages = min(176100.0, max(0.0, gross - pre_tax_hsa - pre_tax_health))
        ss_tax = round(ss_wages * 0.062, 2)

        med_wages = max(0.0, gross - pre_tax_hsa - pre_tax_health)
        med_tax = round(med_wages * 0.0145, 2)

        fed_tax = annual_payroll_summary.get("federal_tax_withheld", 0.0)
        state_tax = annual_payroll_summary.get("state_tax_withheld", 0.0)

        return FormW2Record(
            employee_ssn_masked="XXX-XX-" + str(employee_info.get("ssn_last4", "1234")),
            employee_name=employee_info.get("full_name", "Employee"),
            employee_address=employee_info.get("address", "123 Corporate Blvd, San Francisco, CA"),
            employer_ein="XX-XXXXXXX",
            employer_name="PeoplePulse Global Enterprise Inc.",
            tax_year=tax_year,
            box_1_wages_tips_other_comp=round(box_1, 2),
            box_2_federal_income_tax_withheld=round(fed_tax, 2),
            box_3_social_security_wages=round(ss_wages, 2),
            box_4_social_security_tax_withheld=ss_tax,
            box_5_medicare_wages_and_tips=round(med_wages, 2),
            box_6_medicare_tax_withheld=med_tax,
            box_12a_code_d_401k=round(pre_tax_401k, 2),
            box_12b_code_w_hsa=round(pre_tax_hsa, 2),
            box_14_other_state_disability=round(annual_payroll_summary.get("sdi_withheld", 0.0), 2),
            box_15_state_code=employee_info.get("state_code", "CA"),
            box_16_state_wages=round(box_1, 2),
            box_17_state_income_tax_withheld=round(state_tax, 2)
        )
