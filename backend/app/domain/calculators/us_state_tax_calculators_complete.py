"""
Comprehensive 50-State Individual US State Income Tax Calculation Engine
Provides dedicated calculation algorithms, deductions, and progressive bracket evaluators for all 50 states.
"""
from typing import Dict, Any, Tuple
from dataclasses import dataclass


@dataclass
class USStateTaxResult:
    state_code: str
    state_name: str
    gross_annual_salary: float
    state_taxable_wages: float
    annual_state_tax_withheld: float
    monthly_state_tax_withheld: float
    effective_state_tax_rate_pct: float


class FiftyStatesTaxEngine:
    @classmethod
    def calculate_al_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Alabama (AL).
        """
        taxable = max(0.0, annual_gross - 3000.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 500.0)
            tax += chunk * 0.02
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 2500.0)
            tax += chunk * 0.04
            rem -= chunk
        if rem > 0:
            tax += rem * 0.05
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="AL",
            state_name="Alabama",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ak_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Alaska (AK).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="AK",
            state_name="Alaska",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_az_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Arizona (AZ).
        """
        taxable = max(0.0, annual_gross - 14600.0)
        tax = round(taxable * 0.025, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="AZ",
            state_name="Arizona",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ar_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Arkansas (AR).
        """
        taxable = max(0.0, annual_gross - 2340.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 5100.0)
            tax += chunk * 0.02
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 5200.0)
            tax += chunk * 0.04
            rem -= chunk
        if rem > 0:
            tax += rem * 0.044
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="AR",
            state_name="Arkansas",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ca_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for California (CA).
        """
        taxable = max(0.0, annual_gross - 5540.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 10412.0)
            tax += chunk * 0.01
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 14272.0)
            tax += chunk * 0.02
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 14275.0)
            tax += chunk * 0.04
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 15046.0)
            tax += chunk * 0.06
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 14268.0)
            tax += chunk * 0.08
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 280459.0)
            tax += chunk * 0.093
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 69729.0)
            tax += chunk * 0.103
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 278981.0)
            tax += chunk * 0.113
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 302558.0)
            tax += chunk * 0.123
            rem -= chunk
        if rem > 0:
            tax += rem * 0.133
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="CA",
            state_name="California",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_co_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Colorado (CO).
        """
        taxable = max(0.0, annual_gross - 15000.0)
        tax = round(taxable * 0.044, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="CO",
            state_name="Colorado",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ct_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Connecticut (CT).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 10000.0)
            tax += chunk * 0.03
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 40000.0)
            tax += chunk * 0.05
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 50000.0)
            tax += chunk * 0.055
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 100000.0)
            tax += chunk * 0.06
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 50000.0)
            tax += chunk * 0.065
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 250000.0)
            tax += chunk * 0.069
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0699
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="CT",
            state_name="Connecticut",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_de_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Delaware (DE).
        """
        taxable = max(0.0, annual_gross - 3250.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 3000.0)
            tax += chunk * 0.022
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 5000.0)
            tax += chunk * 0.039
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 10000.0)
            tax += chunk * 0.048
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 5000.0)
            tax += chunk * 0.052
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 35000.0)
            tax += chunk * 0.0555
            rem -= chunk
        if rem > 0:
            tax += rem * 0.066
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="DE",
            state_name="Delaware",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_fl_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Florida (FL).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="FL",
            state_name="Florida",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ga_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Georgia (GA).
        """
        taxable = max(0.0, annual_gross - 12000.0)
        tax = round(taxable * 0.0549, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="GA",
            state_name="Georgia",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_hi_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Hawaii (HI).
        """
        taxable = max(0.0, annual_gross - 2200.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 2400.0)
            tax += chunk * 0.014
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 2400.0)
            tax += chunk * 0.032
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 4800.0)
            tax += chunk * 0.055
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 4800.0)
            tax += chunk * 0.064
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 4800.0)
            tax += chunk * 0.068
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 4800.0)
            tax += chunk * 0.072
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 12000.0)
            tax += chunk * 0.076
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 12000.0)
            tax += chunk * 0.079
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 102000.0)
            tax += chunk * 0.0825
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 25000.0)
            tax += chunk * 0.09
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 25000.0)
            tax += chunk * 0.10
            rem -= chunk
        if rem > 0:
            tax += rem * 0.11
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="HI",
            state_name="Hawaii",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_id_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Idaho (ID).
        """
        taxable = max(0.0, annual_gross - 14600.0)
        tax = round(taxable * 0.058, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="ID",
            state_name="Idaho",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_il_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Illinois (IL).
        """
        taxable = max(0.0, annual_gross - 2775.0)
        tax = round(taxable * 0.0495, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="IL",
            state_name="Illinois",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_in_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Indiana (IN).
        """
        taxable = max(0.0, annual_gross - 1000.0)
        tax = round(taxable * 0.0305, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="IN",
            state_name="Indiana",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ia_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Iowa (IA).
        """
        taxable = max(0.0, annual_gross - 14600.0)
        tax = round(taxable * 0.038, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="IA",
            state_name="Iowa",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ks_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Kansas (KS).
        """
        taxable = max(0.0, annual_gross - 3500.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 15000.0)
            tax += chunk * 0.031
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 15000.0)
            tax += chunk * 0.0525
            rem -= chunk
        if rem > 0:
            tax += rem * 0.057
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="KS",
            state_name="Kansas",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ky_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Kentucky (KY).
        """
        taxable = max(0.0, annual_gross - 3160.0)
        tax = round(taxable * 0.04, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="KY",
            state_name="Kentucky",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_la_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Louisiana (LA).
        """
        taxable = max(0.0, annual_gross - 4500.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 12500.0)
            tax += chunk * 0.0185
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 37500.0)
            tax += chunk * 0.035
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0425
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="LA",
            state_name="Louisiana",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_me_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Maine (ME).
        """
        taxable = max(0.0, annual_gross - 14600.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 26050.0)
            tax += chunk * 0.058
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 35550.0)
            tax += chunk * 0.0675
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0715
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="ME",
            state_name="Maine",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_md_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Maryland (MD).
        """
        taxable = max(0.0, annual_gross - 2550.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 1000.0)
            tax += chunk * 0.02
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1000.0)
            tax += chunk * 0.03
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1000.0)
            tax += chunk * 0.04
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 97000.0)
            tax += chunk * 0.0475
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 25000.0)
            tax += chunk * 0.05
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 25000.0)
            tax += chunk * 0.0525
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 100000.0)
            tax += chunk * 0.055
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0575
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="MD",
            state_name="Maryland",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ma_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Massachusetts (MA).
        """
        taxable = max(0.0, annual_gross - 4400.0)
        tax = round(taxable * 0.05, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="MA",
            state_name="Massachusetts",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_mi_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Michigan (MI).
        """
        taxable = max(0.0, annual_gross - 5600.0)
        tax = round(taxable * 0.0425, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="MI",
            state_name="Michigan",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_mn_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Minnesota (MN).
        """
        taxable = max(0.0, annual_gross - 14575.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 31690.0)
            tax += chunk * 0.0535
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 72400.0)
            tax += chunk * 0.068
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 89150.0)
            tax += chunk * 0.0785
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0985
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="MN",
            state_name="Minnesota",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ms_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Mississippi (MS).
        """
        taxable = max(0.0, annual_gross - 6000.0)
        tax = round(taxable * 0.047, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="MS",
            state_name="Mississippi",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_mo_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Missouri (MO).
        """
        taxable = max(0.0, annual_gross - 14600.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 1273.0)
            tax += chunk * 0.02
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1273.0)
            tax += chunk * 0.025
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1273.0)
            tax += chunk * 0.03
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1273.0)
            tax += chunk * 0.035
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1273.0)
            tax += chunk * 0.04
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1273.0)
            tax += chunk * 0.045
            rem -= chunk
        if rem > 0:
            tax += rem * 0.048
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="MO",
            state_name="Missouri",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_mt_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Montana (MT).
        """
        taxable = max(0.0, annual_gross - 14600.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 20500.0)
            tax += chunk * 0.047
            rem -= chunk
        if rem > 0:
            tax += rem * 0.059
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="MT",
            state_name="Montana",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ne_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Nebraska (NE).
        """
        taxable = max(0.0, annual_gross - 8200.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 3700.0)
            tax += chunk * 0.0246
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 18470.0)
            tax += chunk * 0.0351
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 13290.0)
            tax += chunk * 0.0501
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0584
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="NE",
            state_name="Nebraska",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_nv_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Nevada (NV).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="NV",
            state_name="Nevada",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_nh_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for New Hampshire (NH).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = round(taxable * 0.03, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="NH",
            state_name="New Hampshire",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_nj_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for New Jersey (NJ).
        """
        taxable = max(0.0, annual_gross - 1000.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 20000.0)
            tax += chunk * 0.014
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 15000.0)
            tax += chunk * 0.0175
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 5000.0)
            tax += chunk * 0.035
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 35000.0)
            tax += chunk * 0.05525
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 425000.0)
            tax += chunk * 0.0637
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 500000.0)
            tax += chunk * 0.0897
            rem -= chunk
        if rem > 0:
            tax += rem * 0.1075
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="NJ",
            state_name="New Jersey",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_nm_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for New Mexico (NM).
        """
        taxable = max(0.0, annual_gross - 14600.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 5500.0)
            tax += chunk * 0.017
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 5500.0)
            tax += chunk * 0.032
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 5000.0)
            tax += chunk * 0.047
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 194000.0)
            tax += chunk * 0.049
            rem -= chunk
        if rem > 0:
            tax += rem * 0.059
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="NM",
            state_name="New Mexico",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ny_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for New York (NY).
        """
        taxable = max(0.0, annual_gross - 8000.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 8500.0)
            tax += chunk * 0.04
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 3200.0)
            tax += chunk * 0.045
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 2200.0)
            tax += chunk * 0.0525
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 66750.0)
            tax += chunk * 0.055
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 134750.0)
            tax += chunk * 0.060
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 862150.0)
            tax += chunk * 0.0685
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 3922450.0)
            tax += chunk * 0.0965
            rem -= chunk
        if rem > 0:
            tax += rem * 0.109
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="NY",
            state_name="New York",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_nc_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for North Carolina (NC).
        """
        taxable = max(0.0, annual_gross - 12750.0)
        tax = round(taxable * 0.045, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="NC",
            state_name="North Carolina",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_nd_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for North Dakota (ND).
        """
        taxable = max(0.0, annual_gross - 14600.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 181250.0)
            tax += chunk * 0.0195
            rem -= chunk
        if rem > 0:
            tax += rem * 0.025
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="ND",
            state_name="North Dakota",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_oh_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Ohio (OH).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 73950.0)
            tax += chunk * 0.0275
            rem -= chunk
        if rem > 0:
            tax += rem * 0.035
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="OH",
            state_name="Ohio",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ok_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Oklahoma (OK).
        """
        taxable = max(0.0, annual_gross - 6350.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 1000.0)
            tax += chunk * 0.0025
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1500.0)
            tax += chunk * 0.0075
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1250.0)
            tax += chunk * 0.0175
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 1150.0)
            tax += chunk * 0.0275
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 2300.0)
            tax += chunk * 0.0375
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0475
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="OK",
            state_name="Oklahoma",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_or_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Oregon (OR).
        """
        taxable = max(0.0, annual_gross - 2745.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 4300.0)
            tax += chunk * 0.0475
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 6450.0)
            tax += chunk * 0.0675
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 114250.0)
            tax += chunk * 0.0875
            rem -= chunk
        if rem > 0:
            tax += rem * 0.099
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="OR",
            state_name="Oregon",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_pa_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Pennsylvania (PA).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = round(taxable * 0.0307, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="PA",
            state_name="Pennsylvania",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ri_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Rhode Island (RI).
        """
        taxable = max(0.0, annual_gross - 10500.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 77450.0)
            tax += chunk * 0.0375
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 98600.0)
            tax += chunk * 0.0475
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0599
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="RI",
            state_name="Rhode Island",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_sc_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for South Carolina (SC).
        """
        taxable = max(0.0, annual_gross - 14600.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 13870.0)
            tax += chunk * 0.03
            rem -= chunk
        if rem > 0:
            tax += rem * 0.064
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="SC",
            state_name="South Carolina",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_sd_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for South Dakota (SD).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="SD",
            state_name="South Dakota",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_tn_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Tennessee (TN).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="TN",
            state_name="Tennessee",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_tx_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Texas (TX).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="TX",
            state_name="Texas",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_ut_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Utah (UT).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = round(taxable * 0.0465, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="UT",
            state_name="Utah",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_vt_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Vermont (VT).
        """
        taxable = max(0.0, annual_gross - 7350.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 45400.0)
            tax += chunk * 0.0335
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 64650.0)
            tax += chunk * 0.066
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 119500.0)
            tax += chunk * 0.076
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0875
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="VT",
            state_name="Vermont",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_va_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Virginia (VA).
        """
        taxable = max(0.0, annual_gross - 8500.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 3000.0)
            tax += chunk * 0.02
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 2000.0)
            tax += chunk * 0.03
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 12000.0)
            tax += chunk * 0.05
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0575
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="VA",
            state_name="Virginia",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_wa_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Washington (WA).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="WA",
            state_name="Washington",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_wv_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for West Virginia (WV).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 10000.0)
            tax += chunk * 0.0236
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 15000.0)
            tax += chunk * 0.0315
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 15000.0)
            tax += chunk * 0.0354
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 20000.0)
            tax += chunk * 0.0472
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0512
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="WV",
            state_name="West Virginia",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_wi_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Wisconsin (WI).
        """
        taxable = max(0.0, annual_gross - 13810.0)
        tax = 0.0
        rem = taxable
        if rem > 0:
            chunk = min(rem, 14320.0)
            tax += chunk * 0.035
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 14320.0)
            tax += chunk * 0.044
            rem -= chunk
        if rem > 0:
            chunk = min(rem, 286670.0)
            tax += chunk * 0.053
            rem -= chunk
        if rem > 0:
            tax += rem * 0.0765
        tax = round(tax, 2)
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="WI",
            state_name="Wisconsin",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )

    @classmethod
    def calculate_wy_tax(cls, annual_gross: float) -> USStateTaxResult:
        """
        Calculates state withholding tax for Wyoming (WY).
        """
        taxable = max(0.0, annual_gross - 0.0)
        tax = 0.0
        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)
        return USStateTaxResult(
            state_code="WY",
            state_name="Wyoming",
            gross_annual_salary=annual_gross,
            state_taxable_wages=round(taxable, 2),
            annual_state_tax_withheld=tax,
            monthly_state_tax_withheld=round(tax / 12.0, 2),
            effective_state_tax_rate_pct=eff_rate
        )
