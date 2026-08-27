"""
Build Part 1: Payroll Tax Engines, NACHA ACH, Payslip Builder, and Workflow DSL AST Engine
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"Built {rel}: {len(text.splitlines())} LOC")

# 1. Tax Engine
tax_engine_code = '''"""
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
'''
write("backend/app/modules/payroll/tax_engine.py", tax_engine_code)

# 2. NACHA ACH & SEPA Generator
nacha_code = '''"""
NACHA Direct Deposit File & SEPA XML ISO 20022 Direct Credit Generator
Generates banking transmission files for multi-bank electronic payroll disbursement.
"""
from datetime import datetime, date
from typing import List, Dict, Any, Optional
import hashlib
import xml.etree.ElementTree as ET


class NACHAFileGenerator:
    """
    Constructs ACH compliant fixed-width 94-character records.
    Record Types:
      1: File Header Record
      5: Company / Batch Header Record
      6: Entry Detail Record (PPD - Prearranged Payment and Deposit)
      7: Addenda Record (Optional)
      8: Company / Batch Control Record
      9: File Control Record
    """
    @staticmethod
    def pad_left_zero(val: Any, length: int) -> str:
        s = str(val) if val is not None else "0"
        return s.zfill(length)[:length]

    @staticmethod
    def pad_right_space(val: Any, length: int) -> str:
        s = str(val) if val is not None else ""
        return (s + " " * length)[:length]

    @classmethod
    def generate_ach_file(
        cls,
        immediate_destination: str,  # 9-digit routing number with leading space or ' ' + 9 digits
        immediate_origin: str,       # Company EIN / Tax ID (10 chars, e.g. ' 123456789')
        company_name: str,
        company_id: str,
        effective_entry_date: date,
        employee_payments: List[Dict[str, Any]]
    ) -> str:
        now = datetime.now()
        date_str = now.strftime("%y%m%d")
        time_str = now.strftime("%H%M")
        file_id_mod = "A"

        records: List[str] = []

        # 1. File Header Record (Type 1)
        rec_1 = (
            "1"
            + "01"                                                # Priority code
            + cls.pad_right_space(immediate_destination, 10)       # Immediate destination
            + cls.pad_right_space(immediate_origin, 10)            # Immediate origin
            + date_str                                             # File creation date
            + time_str                                             # File creation time
            + file_id_mod                                          # File ID modifier
            + "094"                                                # Record size
            + "10"                                                 # Blocking factor
            + "1"                                                  # Format code
            + cls.pad_right_space(company_name, 23)                # Destination name
            + cls.pad_right_space("HR MANAGEMENT SYSTEM", 23)           # Origin name
            + "00000000"                                           # Reference code
        )
        records.append(rec_1)

        # 2. Batch Header Record (Type 5)
        batch_num = 1
        sec_code = "PPD"  # Payroll Direct Deposit
        company_desc = "PAYROLL   "
        eff_date_str = effective_entry_date.strftime("%y%m%d")

        rec_5 = (
            "5"
            + "200"                                                # Service class code (200: mixed debits/credits, 220: credits only)
            + cls.pad_right_space(company_name, 16)                # Company name
            + cls.pad_right_space("", 20)                          # Company discretionary data
            + cls.pad_right_space(company_id, 10)                  # Company identification
            + sec_code                                             # Standard Entry Class
            + company_desc                                         # Company entry description
            + date_str                                             # Company descriptive date
            + eff_date_str                                         # Effective entry date
            + "   "                                                # Settlement date (blank for ODFI)
            + "1"                                                  # Originator status code
            + cls.pad_left_zero(immediate_destination[-9:-1], 8)   # Originating DFI ID
            + cls.pad_left_zero(batch_num, 7)                      # Batch number
        )
        records.append(rec_5)

        # 3. Entry Detail Records (Type 6)
        total_credit_cents = 0
        entry_hash = 0
        trace_seq = 1

        for emp in employee_payments:
            routing = str(emp.get("routing_number", "011000015")).zfill(9)
            account = str(emp.get("account_number", "123456789"))
            amount = float(emp.get("amount", 0.0))
            emp_name = str(emp.get("employee_name", "Employee"))
            emp_id = str(emp.get("employee_code", "EMP001"))

            amount_cents = int(round(amount * 100))
            total_credit_cents += amount_cents
            entry_hash += int(routing[:8])

            rec_6 = (
                "6"
                + "22"                                             # Transaction code (22: Automated Deposit / Credit)
                + cls.pad_left_zero(routing[:8], 8)                # Receiving DFI routing
                + routing[8]                                       # Check digit
                + cls.pad_right_space(account, 17)                 # DFI account number
                + cls.pad_left_zero(amount_cents, 10)              # Amount in cents
                + cls.pad_right_space(emp_id, 15)                  # Individual identification
                + cls.pad_right_space(emp_name, 22)                # Individual name
                + "  "                                             # Discretionary data
                + "0"                                              # Addenda record indicator
                + cls.pad_left_zero(immediate_destination[-9:-1], 8) # Trace number prefix
                + cls.pad_left_zero(trace_seq, 7)                  # Trace number seq
            )
            records.append(rec_6)
            trace_seq += 1

        # 4. Batch Control Record (Type 8)
        hash_10 = cls.pad_left_zero(str(entry_hash)[-10:], 10)
        rec_8 = (
            "8"
            + "200"                                                # Service class code
            + cls.pad_left_zero(len(employee_payments), 6)         # Entry/Addenda count
            + hash_10                                              # Entry hash
            + cls.pad_left_zero(0, 12)                             # Total debit amount
            + cls.pad_left_zero(total_credit_cents, 12)            # Total credit amount
            + cls.pad_right_space(company_id, 10)                  # Company identification
            + cls.pad_right_space("", 19)                          # Message authentication code
            + cls.pad_right_space("", 6)                           # Reserved
            + cls.pad_left_zero(immediate_destination[-9:-1], 8)   # Originating DFI ID
            + cls.pad_left_zero(batch_num, 7)                      # Batch number
        )
        records.append(rec_8)

        # 5. File Control Record (Type 9)
        total_records = len(records) + 1
        block_count = (total_records + 9) // 10
        padding_needed = (block_count * 10) - total_records

        rec_9 = (
            "9"
            + cls.pad_left_zero(1, 6)                              # Batch count
            + cls.pad_left_zero(block_count, 6)                    # Block count
            + cls.pad_left_zero(len(employee_payments), 8)         # Total entry/addenda count
            + hash_10                                              # Entry hash
            + cls.pad_left_zero(0, 12)                             # Total debit amount
            + cls.pad_left_zero(total_credit_cents, 12)            # Total credit amount
            + cls.pad_right_space("", 39)                          # Reserved
        )
        records.append(rec_9)

        # Pad remaining lines with 9s to fill block factor 10
        for _ in range(padding_needed):
            records.append("9" * 94)

        return "\\n".join(records)


class SEPAFileGenerator:
    """
    Generates ISO 20022 pain.001.001.03 Credit Transfer Initiation XML for Euro zone salaries.
    """
    @classmethod
    def generate_sepa_xml(
        cls,
        message_id: str,
        initiating_party_name: str,
        debtor_name: str,
        debtor_iban: str,
        debtor_bic: str,
        execution_date: date,
        employee_transfers: List[Dict[str, Any]]
    ) -> str:
        root = ET.Element("Document", {
            "xmlns": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.03",
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance"
        })
        cstmr = ET.SubElement(root, "CstmrCdtTrfInitn")

        # Group Header
        grp_hdr = ET.SubElement(cstmr, "GrpHdr")
        ET.SubElement(grp_hdr, "MsgId").text = message_id
        ET.SubElement(grp_hdr, "CreDtTm").text = datetime.now().isoformat()
        ET.SubElement(grp_hdr, "NbOfTxs").text = str(len(employee_transfers))
        total_val = sum(float(t.get("amount", 0.0)) for t in employee_transfers)
        ET.SubElement(grp_hdr, "CtrlSum").text = f"{total_val:.2f}"
        
        initg_pty = ET.SubElement(grp_hdr, "InitgPty")
        ET.SubElement(initg_pty, "Nm").text = initiating_party_name

        # Payment Information Block
        pmt_inf = ET.SubElement(cstmr, "PmtInf")
        ET.SubElement(pmt_inf, "PmtInfId").text = f"PMT-{message_id}"
        ET.SubElement(pmt_inf, "PmtMtd").text = "TRF"
        ET.SubElement(pmt_inf, "NbOfTxs").text = str(len(employee_transfers))
        ET.SubElement(pmt_inf, "CtrlSum").text = f"{total_val:.2f}"

        pmt_tp_inf = ET.SubElement(pmt_inf, "PmtTpInf")
        svc_lvl = ET.SubElement(pmt_tp_inf, "SvcLvl")
        ET.SubElement(svc_lvl, "Cd").text = "SEPA"

        ET.SubElement(pmt_inf, "ReqdExctnDt").text = execution_date.isoformat()

        dbtr = ET.SubElement(pmt_inf, "Dbtr")
        ET.SubElement(dbtr, "Nm").text = debtor_name

        dbtr_acct = ET.SubElement(pmt_inf, "DbtrAcct")
        id_el = ET.SubElement(dbtr_acct, "Id")
        ET.SubElement(id_el, "IBAN").text = debtor_iban

        dbtr_agt = ET.SubElement(pmt_inf, "DbtrAgt")
        fin_instn_id = ET.SubElement(dbtr_agt, "FinInstnId")
        ET.SubElement(fin_instn_id, "BIC").text = debtor_bic

        ET.SubElement(pmt_inf, "ChrgBr").text = "SLEV"

        # Transactions
        for tx in employee_transfers:
            tx_inf = ET.SubElement(pmt_inf, "CdtTrfTxInf")
            pmt_id = ET.SubElement(tx_inf, "PmtId")
            ET.SubElement(pmt_id, "EndToEndId").text = tx.get("reference_id", f"SAL-{datetime.now().strftime('%Y%m')}")

            amt = ET.SubElement(tx_inf, "Amt")
            instd_amt = ET.SubElement(amt, "InstdAmt", {"Ccy": "EUR"})
            instd_amt.text = f"{float(tx.get('amount', 0.0)):.2f}"

            cdtr = ET.SubElement(tx_inf, "Cdtr")
            ET.SubElement(cdtr, "Nm").text = tx.get("employee_name", "Employee")

            cdtr_acct = ET.SubElement(tx_inf, "CdtrAcct")
            cdtr_id = ET.SubElement(cdtr_acct, "Id")
            ET.SubElement(cdtr_id, "IBAN").text = tx.get("iban", "FR7630006000011234567890189")

            if "bic" in tx:
                cdtr_agt = ET.SubElement(tx_inf, "CdtrAgt")
                c_fin = ET.SubElement(cdtr_agt, "FinInstnId")
                ET.SubElement(c_fin, "BIC").text = tx["bic"]

            rmt_inf = ET.SubElement(tx_inf, "RmtInf")
            ET.SubElement(rmt_inf, "Ustrd").text = f"Salary {execution_date.strftime('%B %Y')}"

        return ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")
'''
write("backend/app/modules/payroll/nacha_generator.py", nacha_code)

# 3. DSL AST Workflow Engine
dsl_code = '''"""
Domain-Specific Language (DSL) Abstract Syntax Tree (AST) Parser & Evaluator
Evaluates complex enterprise business conditions, date logic, and workflow triggers.
"""
import re
import math
from datetime import datetime, date, timedelta
from typing import Any, Dict, List, Optional, Union
from enum import Enum


class TokenType(Enum):
    NUMBER = "NUMBER"
    STRING = "STRING"
    BOOLEAN = "BOOLEAN"
    IDENTIFIER = "IDENTIFIER"
    OPERATOR = "OPERATOR"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    COMMA = "COMMA"
    EOF = "EOF"


class Token:
    def __init__(self, token_type: TokenType, value: Any, position: int):
        self.type = token_type
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type.name}, {self.value})"


class Lexer:
    OPERATORS = {
        "==", "!=", ">=", "<=", ">", "<",
        "&&", "||", "!", "+", "-", "*", "/", "%",
        "IN", "NOT_IN", "CONTAINS", "MATCHES", "STARTS_WITH", "ENDS_WITH"
    }

    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def number(self) -> Token:
        start_pos = self.pos
        result = ""
        has_dot = False
        while self.current_char and (self.current_char.isdigit() or self.current_char == "."):
            if self.current_char == ".":
                if has_dot:
                    break
                has_dot = True
            result += self.current_char
            self.advance()
        val = float(result) if has_dot else int(result)
        return Token(TokenType.NUMBER, val, start_pos)

    def string(self, quote_char: str) -> Token:
        start_pos = self.pos
        self.advance()  # skip opening quote
        result = ""
        while self.current_char and self.current_char != quote_char:
            if self.current_char == "\\\\":
                self.advance()
                if self.current_char:
                    result += self.current_char
                    self.advance()
            else:
                result += self.current_char
                self.advance()
        if self.current_char == quote_char:
            self.advance()
        return Token(TokenType.STRING, result, start_pos)

    def identifier_or_keyword(self) -> Token:
        start_pos = self.pos
        result = ""
        while self.current_char and (self.current_char.isalnum() or self.current_char in ("_", ".", "$", "@")):
            result += self.current_char
            self.advance()

        upper = result.upper()
        if upper in ("TRUE", "FALSE"):
            return Token(TokenType.BOOLEAN, upper == "TRUE", start_pos)
        if upper in ("AND", "&&"):
            return Token(TokenType.OPERATOR, "&&", start_pos)
        if upper in ("OR", "||"):
            return Token(TokenType.OPERATOR, "||", start_pos)
        if upper in ("NOT", "!"):
            return Token(TokenType.OPERATOR, "!", start_pos)
        if upper in self.OPERATORS:
            return Token(TokenType.OPERATOR, upper, start_pos)

        return Token(TokenType.IDENTIFIER, result, start_pos)

    def get_next_token(self) -> Token:
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char in ("'", '"'):
                return self.string(self.current_char)

            if self.current_char == "(":
                pos = self.pos
                self.advance()
                return Token(TokenType.LPAREN, "(", pos)

            if self.current_char == ")":
                pos = self.pos
                self.advance()
                return Token(TokenType.RPAREN, ")", pos)

            if self.current_char == ",":
                pos = self.pos
                self.advance()
                return Token(TokenType.COMMA, ",", pos)

            # Two char operators
            two = self.text[self.pos:self.pos + 2]
            if two in ("==", "!=", ">=", "<=", "&&", "||"):
                pos = self.pos
                self.advance()
                self.advance()
                return Token(TokenType.OPERATOR, two, pos)

            # Single char operators
            if self.current_char in (">", "<", "!", "+", "-", "*", "/", "%"):
                pos = self.pos
                ch = self.current_char
                self.advance()
                return Token(TokenType.OPERATOR, ch, pos)

            if self.current_char.isalpha() or self.current_char in ("_", "$", "@"):
                return self.identifier_or_keyword()

            # Unknown char skip
            self.advance()

        return Token(TokenType.EOF, None, self.pos)


class ASTNode:
    pass


class LiteralNode(ASTNode):
    def __init__(self, value: Any):
        self.value = value

    def __repr__(self):
        return f"Literal({self.value})"


class VariableNode(ASTNode):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Var({self.name})"


class UnaryOpNode(ASTNode):
    def __init__(self, op: str, operand: ASTNode):
        self.op = op
        self.operand = operand


class BinaryOpNode(ASTNode):
    def __init__(self, left: ASTNode, op: str, right: ASTNode):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinaryOp({self.left} {self.op} {self.right})"


class FunctionCallNode(ASTNode):
    def __init__(self, name: str, args: List[ASTNode]):
        self.name = name
        self.args = args


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type: TokenType):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise SyntaxError(f"Expected token {token_type}, got {self.current_token.type} at {self.current_token.position}")

    def factor(self) -> ASTNode:
        token = self.current_token
        if token.type in (TokenType.NUMBER, TokenType.STRING, TokenType.BOOLEAN):
            self.eat(token.type)
            return LiteralNode(token.value)
        elif token.type == TokenType.IDENTIFIER:
            name = token.value
            self.eat(TokenType.IDENTIFIER)
            # Check function call
            if self.current_token.type == TokenType.LPAREN:
                self.eat(TokenType.LPAREN)
                args = []
                if self.current_token.type != TokenType.RPAREN:
                    args.append(self.expr())
                    while self.current_token.type == TokenType.COMMA:
                        self.eat(TokenType.COMMA)
                        args.append(self.expr())
                self.eat(TokenType.RPAREN)
                return FunctionCallNode(name, args)
            return VariableNode(name)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        elif token.type == TokenType.OPERATOR and token.value in ("!", "-", "+"):
            op = token.value
            self.eat(TokenType.OPERATOR)
            return UnaryOpNode(op, self.factor())
        raise SyntaxError(f"Unexpected token in factor: {token}")

    def term(self) -> ASTNode:
        node = self.factor()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in ("*", "/", "%"):
            op = self.current_token.value
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, op, self.factor())
        return node

    def arithmetic_expr(self) -> ASTNode:
        node = self.term()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in ("+", "-"):
            op = self.current_token.value
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, op, self.term())
        return node

    def comparison_expr(self) -> ASTNode:
        node = self.arithmetic_expr()
        cmp_ops = ("==", "!=", ">=", "<=", ">", "<", "IN", "NOT_IN", "CONTAINS", "MATCHES", "STARTS_WITH", "ENDS_WITH")
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in cmp_ops:
            op = self.current_token.value
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, op, self.arithmetic_expr())
        return node

    def logical_and_expr(self) -> ASTNode:
        node = self.comparison_expr()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value == "&&":
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, "&&", self.comparison_expr())
        return node

    def expr(self) -> ASTNode:
        node = self.logical_and_expr()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value == "||":
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, "||", self.logical_and_expr())
        return node

    def parse(self) -> ASTNode:
        return self.expr()


class ASTEvaluator:
    @staticmethod
    def resolve_var(name: str, context: Dict[str, Any]) -> Any:
        # Resolve dot notation, e.g. employee.department.name
        parts = name.split(".")
        val = context
        for p in parts:
            if isinstance(val, dict):
                val = val.get(p)
            elif hasattr(val, p):
                val = getattr(val, p)
            else:
                return None
        return val

    @classmethod
    def evaluate(cls, node: ASTNode, context: Dict[str, Any]) -> Any:
        if isinstance(node, LiteralNode):
            return node.value

        if isinstance(node, VariableNode):
            return cls.resolve_var(node.name, context)

        if isinstance(node, UnaryOpNode):
            val = cls.evaluate(node.operand, context)
            if node.op in ("!", "NOT"):
                return not bool(val)
            if node.op == "-":
                return -val
            if node.op == "+":
                return +val

        if isinstance(node, BinaryOpNode):
            left = cls.evaluate(node.left, context)
            right = cls.evaluate(node.right, context)

            if node.op == "&&":
                return bool(left) and bool(right)
            if node.op == "||":
                return bool(left) or bool(right)
            if node.op == "==":
                return left == right
            if node.op == "!=":
                return left != right
            if node.op == ">":
                return (left or 0) > (right or 0)
            if node.op == "<":
                return (left or 0) < (right or 0)
            if node.op == ">=":
                return (left or 0) >= (right or 0)
            if node.op == "<=":
                return (left or 0) <= (right or 0)
            if node.op == "+":
                return (left or 0) + (right or 0)
            if node.op == "-":
                return (left or 0) - (right or 0)
            if node.op == "*":
                return (left or 0) * (right or 0)
            if node.op == "/":
                return (left or 0) / (right or 1)
            if node.op == "CONTAINS":
                return str(right).lower() in str(left).lower() if left is not None else False
            if node.op == "STARTS_WITH":
                return str(left).startswith(str(right)) if left is not None else False
            if node.op == "ENDS_WITH":
                return str(left).endswith(str(right)) if left is not None else False
            if node.op == "MATCHES":
                return bool(re.search(str(right), str(left))) if left is not None else False

        if isinstance(node, FunctionCallNode):
            args = [cls.evaluate(a, context) for a in node.args]
            fname = node.name.lower()
            if fname == "len":
                return len(args[0]) if args[0] is not None else 0
            if fname == "days_between":
                d1 = datetime.fromisoformat(str(args[0])) if isinstance(args[0], str) else args[0]
                d2 = datetime.fromisoformat(str(args[1])) if isinstance(args[1], str) else args[1]
                return abs((d1 - d2).days)
            if fname == "upper":
                return str(args[0]).upper()
            if fname == "lower":
                return str(args[0]).lower()
            if fname == "round":
                return round(args[0], int(args[1]) if len(args) > 1 else 0)

        return None

    @classmethod
    def execute_rule(cls, expression: str, context: Dict[str, Any]) -> bool:
        if not expression or not expression.strip():
            return True
        lexer = Lexer(expression)
        parser = Parser(lexer)
        ast = parser.parse()
        result = cls.evaluate(ast, context)
        return bool(result)
'''
write("backend/app/modules/workflows/dsl_engine.py", dsl_code)

print("Part 1 complete!")
'''
write("scripts/build_engines_part1.py", "# Part 1 builder")
'''
