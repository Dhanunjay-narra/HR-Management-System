"""
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
