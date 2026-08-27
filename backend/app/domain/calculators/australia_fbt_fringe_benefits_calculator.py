"""
Australia Fringe Benefits Tax (FBT) & Type 1 / Type 2 Gross-Up Calculation Engine (ATO Regulations 2026)
Calculates employer FBT liability on car fringe benefits, expense payments, living-away-from-home allowances (LAFHA), and novated leases.
"""
from typing import Dict, Any


class AustraliaFringeBenefitsTaxCalculator:
    FBT_STATUTORY_RATE = 0.47  # 47% ATO FBT Rate
    TYPE_1_GROSS_UP_FACTOR = 2.0802  # Where employer is entitled to GST input tax credits
    TYPE_2_GROSS_UP_FACTOR = 1.8868  # Where employer is NOT entitled to GST input tax credits

    @classmethod
    def calculate_fbt_liability(
        cls,
        type_1_taxable_value_aud: float,
        type_2_taxable_value_aud: float
    ) -> Dict[str, Any]:
        grossed_up_type_1 = round(type_1_taxable_value_aud * cls.TYPE_1_GROSS_UP_FACTOR, 2)
        grossed_up_type_2 = round(type_2_taxable_value_aud * cls.TYPE_2_GROSS_UP_FACTOR, 2)

        total_fbt_taxable_amount = grossed_up_type_1 + grossed_up_type_2
        total_fbt_payable = round(total_fbt_taxable_amount * cls.FBT_STATUTORY_RATE, 2)

        return {
            "type_1_fringe_benefits_value_aud": type_1_taxable_value_aud,
            "type_2_fringe_benefits_value_aud": type_2_taxable_value_aud,
            "type_1_grossed_up_aud": grossed_up_type_1,
            "type_2_grossed_up_aud": grossed_up_type_2,
            "total_fbt_taxable_base_aud": total_fbt_taxable_amount,
            "total_employer_fbt_payable_aud": total_fbt_payable
        }
