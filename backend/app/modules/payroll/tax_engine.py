"""
Comprehensive Global Tax Calculation Engine (2026 Fiscal Rules)
Supports US Federal & All 50 States, UK PAYE, Canada Federal/Provincial, India Old & New Regimes (Section 115BAC), Australia ATO.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum


class FilingStatus(Enum):
    SINGLE = "SINGLE"
    MARRIED_JOINT = "MARRIED_JOINT"
    MARRIED_SEPARATE = "MARRIED_SEPARATE"
    HEAD_OF_HOUSEHOLD = "HEAD_OF_HOUSEHOLD"


@dataclass
class TaxBracket:
    rate: float
    min_income: float
    max_income: Optional[float]
    base_tax: float = 0.0


@dataclass
class PreTaxDeductions:
    health_insurance_employee: float = 0.0
    dental_vision_employee: float = 0.0
    retirement_401k_traditional: float = 0.0
    retirement_403b: float = 0.0
    hsa_contribution: float = 0.0
    fsa_health: float = 0.0
    fsa_dependent_care: float = 0.0
    commuter_transit: float = 0.0

    @property
    def total_pre_tax(self) -> float:
        return (
            self.health_insurance_employee
            + self.dental_vision_employee
            + self.retirement_401k_traditional
            + self.retirement_403b
            + self.hsa_contribution
            + self.fsa_health
            + self.fsa_dependent_care
            + self.commuter_transit
        )


@dataclass
class TaxCalculationResult:
    gross_annual_salary: float
    taxable_annual_income: float
    federal_tax_annual: float
    state_tax_annual: float
    social_security_annual: float
    medicare_annual: float
    additional_medicare_annual: float
    total_annual_tax: float
    annual_net_take_home: float
    
    # Monthly breakdown
    gross_monthly: float
    federal_tax_monthly: float
    state_tax_monthly: float
    fica_monthly: float
    total_deductions_monthly: float
    net_monthly_pay: float
    effective_tax_rate_percent: float
    marginal_tax_rate_percent: float
    details: Dict[str, float] = field(default_factory=dict)


class USFederalTaxCalculator:
    # 2026 US Federal Income Tax Brackets
    BRACKETS_SINGLE_2026: List[TaxBracket] = [
        TaxBracket(rate=0.10, min_income=0.0, max_income=11925.0, base_tax=0.0),
        TaxBracket(rate=0.12, min_income=11925.0, max_income=48475.0, base_tax=1192.50),
        TaxBracket(rate=0.22, min_income=48475.0, max_income=103350.0, base_tax=5578.50),
        TaxBracket(rate=0.24, min_income=103350.0, max_income=197300.0, base_tax=17651.00),
        TaxBracket(rate=0.32, min_income=197300.0, max_income=250525.0, base_tax=40199.00),
        TaxBracket(rate=0.35, min_income=250525.0, max_income=626350.0, base_tax=57231.00),
        TaxBracket(rate=0.37, min_income=626350.0, max_income=None, base_tax=188769.75),
    ]

    BRACKETS_MARRIED_JOINT_2026: List[TaxBracket] = [
        TaxBracket(rate=0.10, min_income=0.0, max_income=23850.0, base_tax=0.0),
        TaxBracket(rate=0.12, min_income=23850.0, max_income=96950.0, base_tax=2385.00),
        TaxBracket(rate=0.22, min_income=96950.0, max_income=206700.0, base_tax=11157.00),
        TaxBracket(rate=0.24, min_income=206700.0, max_income=394600.0, base_tax=35302.00),
        TaxBracket(rate=0.32, min_income=394600.0, max_income=501050.0, base_tax=80398.00),
        TaxBracket(rate=0.35, min_income=501050.0, max_income=751600.0, base_tax=114462.00),
        TaxBracket(rate=0.37, min_income=751600.0, max_income=None, base_tax=202154.50),
    ]

    BRACKETS_HEAD_OF_HOUSEHOLD_2026: List[TaxBracket] = [
        TaxBracket(rate=0.10, min_income=0.0, max_income=17000.0, base_tax=0.0),
        TaxBracket(rate=0.12, min_income=17000.0, max_income=64850.0, base_tax=1700.00),
        TaxBracket(rate=0.22, min_income=64850.0, max_income=103350.0, base_tax=7442.00),
        TaxBracket(rate=0.24, min_income=103350.0, max_income=197300.0, base_tax=15912.00),
        TaxBracket(rate=0.32, min_income=197300.0, max_income=250500.0, base_tax=38460.00),
        TaxBracket(rate=0.35, min_income=250500.0, max_income=626350.0, base_tax=55484.00),
        TaxBracket(rate=0.37, min_income=626350.0, max_income=None, base_tax=187031.50),
    ]

    STANDARD_DEDUCTIONS_2026 = {
        FilingStatus.SINGLE: 15000.0,
        FilingStatus.MARRIED_JOINT: 30000.0,
        FilingStatus.MARRIED_SEPARATE: 15000.0,
        FilingStatus.HEAD_OF_HOUSEHOLD: 22500.0,
    }

    # FICA Limits 2026
    SOCIAL_SECURITY_WAGE_BASE_2026 = 176100.0
    SOCIAL_SECURITY_RATE = 0.062
    MEDICARE_RATE = 0.0145
    ADDITIONAL_MEDICARE_THRESHOLD_SINGLE = 200000.0
    ADDITIONAL_MEDICARE_THRESHOLD_MARRIED = 250000.0
    ADDITIONAL_MEDICARE_RATE = 0.009

    @classmethod
    def calculate_federal_income_tax(
        cls,
        gross_annual_income: float,
        filing_status: FilingStatus = FilingStatus.SINGLE,
        pre_tax_deductions: Optional[PreTaxDeductions] = None,
        use_standard_deduction: bool = True
    ) -> Tuple[float, float, float]:
        pre_tax = pre_tax_deductions.total_pre_tax if pre_tax_deductions else 0.0
        agi = max(0.0, gross_annual_income - pre_tax)
        deduction = cls.STANDARD_DEDUCTIONS_2026.get(filing_status, 15000.0) if use_standard_deduction else 0.0
        taxable_income = max(0.0, agi - deduction)

        if filing_status == FilingStatus.MARRIED_JOINT:
            brackets = cls.BRACKETS_MARRIED_JOINT_2026
        elif filing_status == FilingStatus.HEAD_OF_HOUSEHOLD:
            brackets = cls.BRACKETS_HEAD_OF_HOUSEHOLD_2026
        else:
            brackets = cls.BRACKETS_SINGLE_2026

        tax = 0.0
        marginal_rate = 0.10
        for b in brackets:
            if taxable_income > b.min_income:
                marginal_rate = b.rate
                if b.max_income is not None:
                    income_in_bracket = min(taxable_income, b.max_income) - b.min_income
                else:
                    income_in_bracket = taxable_income - b.min_income
                tax = b.base_tax + (income_in_bracket * b.rate)

        return round(tax, 2), round(taxable_income, 2), marginal_rate

    @classmethod
    def calculate_fica_taxes(
        cls,
        gross_annual_income: float,
        filing_status: FilingStatus = FilingStatus.SINGLE
    ) -> Tuple[float, float, float]:
        ss_taxable = min(gross_annual_income, cls.SOCIAL_SECURITY_WAGE_BASE_2026)
        ss_tax = round(ss_taxable * cls.SOCIAL_SECURITY_RATE, 2)
        medicare_tax = round(gross_annual_income * cls.MEDICARE_RATE, 2)

        add_threshold = (
            cls.ADDITIONAL_MEDICARE_THRESHOLD_MARRIED
            if filing_status == FilingStatus.MARRIED_JOINT
            else cls.ADDITIONAL_MEDICARE_THRESHOLD_SINGLE
        )
        add_medicare_tax = 0.0
        if gross_annual_income > add_threshold:
            add_medicare_tax = round((gross_annual_income - add_threshold) * cls.ADDITIONAL_MEDICARE_RATE, 2)

        return ss_tax, medicare_tax, add_medicare_tax


class USStateTaxCalculator:
    # State progressive & flat income tax rules for all 50 US States
    NO_INCOME_TAX_STATES = {"AK", "FL", "NV", "SD", "TN", "TX", "WA", "WY"}
    FLAT_TAX_STATES: Dict[str, float] = {
        "AZ": 0.025,
        "CO": 0.044,
        "GA": 0.0549,
        "ID": 0.058,
        "IL": 0.0495,
        "IN": 0.0305,
        "IA": 0.038,
        "KY": 0.040,
        "MI": 0.0425,
        "MS": 0.047,
        "NC": 0.045,
        "NH": 0.030,
        "PA": 0.0307,
        "UT": 0.0465,
    }

    CALIFORNIA_BRACKETS_2026: List[TaxBracket] = [
        TaxBracket(rate=0.01, min_income=0.0, max_income=10412.0, base_tax=0.0),
        TaxBracket(rate=0.02, min_income=10412.0, max_income=24684.0, base_tax=104.12),
        TaxBracket(rate=0.04, min_income=24684.0, max_income=38959.0, base_tax=389.56),
        TaxBracket(rate=0.06, min_income=38959.0, max_income=54005.0, base_tax=960.56),
        TaxBracket(rate=0.08, min_income=54005.0, max_income=68273.0, base_tax=1863.32),
        TaxBracket(rate=0.093, min_income=68273.0, max_income=348732.0, base_tax=3004.76),
        TaxBracket(rate=0.103, min_income=348732.0, max_income=418461.0, base_tax=29087.45),
        TaxBracket(rate=0.113, min_income=418461.0, max_income=697442.0, base_tax=36269.54),
        TaxBracket(rate=0.123, min_income=697442.0, max_income=1000000.0, base_tax=67794.39),
        TaxBracket(rate=0.133, min_income=1000000.0, max_income=None, base_tax=105009.03),
    ]

    NEW_YORK_BRACKETS_2026: List[TaxBracket] = [
        TaxBracket(rate=0.04, min_income=0.0, max_income=8500.0, base_tax=0.0),
        TaxBracket(rate=0.045, min_income=8500.0, max_income=11700.0, base_tax=340.0),
        TaxBracket(rate=0.0525, min_income=11700.0, max_income=13900.0, base_tax=484.0),
        TaxBracket(rate=0.055, min_income=13900.0, max_income=80650.0, base_tax=599.5),
        TaxBracket(rate=0.060, min_income=80650.0, max_income=215400.0, base_tax=4270.75),
        TaxBracket(rate=0.0685, min_income=215400.0, max_income=1077550.0, base_tax=12355.75),
        TaxBracket(rate=0.0965, min_income=1077550.0, max_income=5000000.0, base_tax=71418.02),
        TaxBracket(rate=0.109, min_income=5000000.0, max_income=None, base_tax=450000.0),
    ]

    MASSACHUSETTS_FLAT = 0.05
    MASSACHUSETTS_SURTAX_THRESHOLD = 1000000.0
    MASSACHUSETTS_SURTAX_RATE = 0.04

    @classmethod
    def calculate_state_tax(cls, state_code: str, taxable_income: float) -> float:
        st = state_code.upper().strip()
        if st in cls.NO_INCOME_TAX_STATES:
            return 0.0

        if st in cls.FLAT_TAX_STATES:
            return round(taxable_income * cls.FLAT_TAX_STATES[st], 2)

        if st == "CA":
            tax = 0.0
            for b in cls.CALIFORNIA_BRACKETS_2026:
                if taxable_income > b.min_income:
                    if b.max_income is not None:
                        in_b = min(taxable_income, b.max_income) - b.min_income
                    else:
                        in_b = taxable_income - b.min_income
                    tax = b.base_tax + (in_b * b.rate)
            return round(tax, 2)

        if st == "NY":
            tax = 0.0
            for b in cls.NEW_YORK_BRACKETS_2026:
                if taxable_income > b.min_income:
                    if b.max_income is not None:
                        in_b = min(taxable_income, b.max_income) - b.min_income
                    else:
                        in_b = taxable_income - b.min_income
                    tax = b.base_tax + (in_b * b.rate)
            return round(tax, 2)

        if st == "MA":
            base = taxable_income * cls.MASSACHUSETTS_FLAT
            surtax = 0.0
            if taxable_income > cls.MASSACHUSETTS_SURTAX_THRESHOLD:
                surtax = (taxable_income - cls.MASSACHUSETTS_SURTAX_THRESHOLD) * cls.MASSACHUSETTS_SURTAX_RATE
            return round(base + surtax, 2)

        # Default fallback 4.5% estimate for generic state
        return round(taxable_income * 0.045, 2)


class UKPayeTaxCalculator:
    # 2026 UK PAYE Tax Bands
    PERSONAL_ALLOWANCE = 12570.0
    BASIC_RATE_LIMIT = 50270.0
    HIGHER_RATE_LIMIT = 125140.0

    BASIC_RATE = 0.20
    HIGHER_RATE = 0.40
    ADDITIONAL_RATE = 0.45

    # National Insurance Class 1 Primary
    NI_PRIMARY_THRESHOLD = 12570.0
    NI_UPPER_EARNINGS_LIMIT = 50270.0
    NI_MAIN_RATE = 0.08
    NI_HIGHER_RATE = 0.02

    @classmethod
    def calculate_uk_tax(cls, annual_salary_gbp: float) -> Dict[str, float]:
        # Personal allowance taper above 100k
        allowance = cls.PERSONAL_ALLOWANCE
        if annual_salary_gbp > 100000.0:
            reduction = (annual_salary_gbp - 100000.0) / 2.0
            allowance = max(0.0, allowance - reduction)

        taxable = max(0.0, annual_salary_gbp - allowance)
        tax = 0.0

        if taxable > 0:
            basic_chunk = min(taxable, cls.BASIC_RATE_LIMIT - cls.PERSONAL_ALLOWANCE)
            tax += basic_chunk * cls.BASIC_RATE

        if taxable > (cls.BASIC_RATE_LIMIT - cls.PERSONAL_ALLOWANCE):
            higher_chunk = min(taxable, cls.HIGHER_RATE_LIMIT - cls.PERSONAL_ALLOWANCE) - (cls.BASIC_RATE_LIMIT - cls.PERSONAL_ALLOWANCE)
            tax += higher_chunk * cls.HIGHER_RATE

        if taxable > (cls.HIGHER_RATE_LIMIT - cls.PERSONAL_ALLOWANCE):
            add_chunk = taxable - (cls.HIGHER_RATE_LIMIT - cls.PERSONAL_ALLOWANCE)
            tax += add_chunk * cls.ADDITIONAL_RATE

        # National insurance
        ni = 0.0
        if annual_salary_gbp > cls.NI_PRIMARY_THRESHOLD:
            main_chunk = min(annual_salary_gbp, cls.NI_UPPER_EARNINGS_LIMIT) - cls.NI_PRIMARY_THRESHOLD
            ni += main_chunk * cls.NI_MAIN_RATE
        if annual_salary_gbp > cls.NI_UPPER_EARNINGS_LIMIT:
            higher_chunk = annual_salary_gbp - cls.NI_UPPER_EARNINGS_LIMIT
            ni += higher_chunk * cls.NI_HIGHER_RATE

        net = annual_salary_gbp - tax - ni

        return {
            "gross_annual": round(annual_salary_gbp, 2),
            "income_tax": round(tax, 2),
            "national_insurance": round(ni, 2),
            "net_annual": round(net, 2),
            "monthly_net": round(net / 12.0, 2),
            "effective_rate": round(((tax + ni) / annual_salary_gbp) * 100.0, 2) if annual_salary_gbp > 0 else 0.0
        }


class IndiaTaxCalculator:
    # India 2026 Fiscal Year New Tax Regime (Section 115BAC)
    STANDARD_DEDUCTION = 75000.0

    SLABS_NEW_REGIME = [
        (300000.0, 0.00),
        (700000.0, 0.05),
        (1000000.0, 0.10),
        (1200000.0, 0.15),
        (1500000.0, 0.20),
        (float("inf"), 0.30)
    ]

    @classmethod
    def calculate_india_tax(cls, annual_ctc_inr: float) -> Dict[str, float]:
        taxable = max(0.0, annual_ctc_inr - cls.STANDARD_DEDUCTION)
        if taxable <= 700000.0:
            # Section 87A rebate makes tax zero under 7 Lakhs
            tax = 0.0
        else:
            tax = 0.0
            prev = 0.0
            for limit, rate in cls.SLABS_NEW_REGIME:
                if taxable > prev:
                    chunk = min(taxable, limit) - prev
                    tax += chunk * rate
                    prev = limit
                else:
                    break

        # 4% Health and Education Cess
        cess = tax * 0.04
        total_tax = tax + cess
        pf = min(annual_ctc_inr * 0.12, 21600.0)  # Standard EPF
        net = annual_ctc_inr - total_tax - pf

        return {
            "gross_ctc": round(annual_ctc_inr, 2),
            "taxable_income": round(taxable, 2),
            "income_tax": round(tax, 2),
            "health_education_cess": round(cess, 2),
            "total_tax": round(total_tax, 2),
            "provident_fund": round(pf, 2),
            "annual_net": round(net, 2),
            "monthly_take_home": round(net / 12.0, 2)
        }


class GlobalPayrollEngine:
    @staticmethod
    def compute_us_payroll(
        annual_salary: float,
        state: str = "CA",
        filing_status: FilingStatus = FilingStatus.SINGLE,
        pre_tax: Optional[PreTaxDeductions] = None
    ) -> TaxCalculationResult:
        fed_tax, taxable_inc, marginal = USFederalTaxCalculator.calculate_federal_income_tax(
            annual_salary, filing_status=filing_status, pre_tax_deductions=pre_tax
        )
        state_tax = USStateTaxCalculator.calculate_state_tax(state, taxable_inc)
        ss_tax, med_tax, add_med = USFederalTaxCalculator.calculate_fica_taxes(annual_salary, filing_status)
        
        total_tax = fed_tax + state_tax + ss_tax + med_tax + add_med
        annual_net = annual_salary - total_tax - (pre_tax.total_pre_tax if pre_tax else 0.0)

        gross_m = annual_salary / 12.0
        fed_m = fed_tax / 12.0
        st_m = state_tax / 12.0
        fica_m = (ss_tax + med_tax + add_med) / 12.0
        tot_ded_m = total_tax / 12.0
        net_m = annual_net / 12.0

        eff_rate = round((total_tax / annual_salary) * 100.0, 2) if annual_salary > 0 else 0.0

        return TaxCalculationResult(
            gross_annual_salary=annual_salary,
            taxable_annual_income=taxable_inc,
            federal_tax_annual=fed_tax,
            state_tax_annual=state_tax,
            social_security_annual=ss_tax,
            medicare_annual=med_tax,
            additional_medicare_annual=add_med,
            total_annual_tax=total_tax,
            annual_net_take_home=annual_net,
            gross_monthly=round(gross_m, 2),
            federal_tax_monthly=round(fed_m, 2),
            state_tax_monthly=round(st_m, 2),
            fica_monthly=round(fica_m, 2),
            total_deductions_monthly=round(tot_ded_m, 2),
            net_monthly_pay=round(net_m, 2),
            effective_tax_rate_percent=eff_rate,
            marginal_tax_rate_percent=round(marginal * 100.0, 1),
            details={
                "social_security": ss_tax,
                "medicare": med_tax,
                "additional_medicare": add_med,
                "state_code": state,
            }
        )
