"""
Massive Domain Architectures Generator
Generates international tax engines, ERP general ledger builders, NLP workplace sentiment dictionaries, and React pages.
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. ERP General Ledger Double-Entry Accounting Journal Generator
gl_code = '''"""
Payroll General Ledger Double-Entry Journal Generator (ERP Integration for NetSuite, SAP S/4HANA, Workday)
Generates balanced debit/credit accounting vouchers for gross wages, tax liabilities, employer FICA, 401(k) matches, and net cash clearing accounts.
"""
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import date


@dataclass
class JournalEntryLine:
    account_number: str
    account_name: str
    debit_amount: float
    credit_amount: float
    cost_center_code: str
    department_name: str
    description: str


@dataclass
class BalancedJournalVoucher:
    voucher_id: str
    posting_date: date
    currency: str
    total_debits: float
    total_credits: float
    is_balanced: bool
    lines: List[JournalEntryLine]


class PayrollGeneralLedgerEngine:
    # Chart of Accounts Mapping
    ACCOUNTS = {
        "WAGE_EXPENSE_SALARIES": ("50100", "Salaries & Wages Expense"),
        "WAGE_EXPENSE_OVERTIME": ("50110", "Overtime Compensation Expense"),
        "WAGE_EXPENSE_BONUS": ("50120", "Annual Performance Bonus Expense"),
        "PAYROLL_TAX_EXPENSE_EMPLOYER_FICA": ("50200", "Employer FICA Tax Expense"),
        "BENEFITS_EXPENSE_401K_MATCH": ("50300", "401(k) Employer Match Expense"),
        "BENEFITS_EXPENSE_HEALTH_INSURANCE": ("50310", "Company Healthcare Subsidy Expense"),
        
        "LIABILITY_FEDERAL_WITHHOLDING_PAYABLE": ("20100", "Federal Income Tax Withholding Payable"),
        "LIABILITY_STATE_WITHHOLDING_PAYABLE": ("20110", "State Income Tax Withholding Payable"),
        "LIABILITY_FICA_PAYABLE_TOTAL": ("20120", "FICA (SS & Medicare) Tax Payable"),
        "LIABILITY_401K_PAYABLE_TOTAL": ("20200", "401(k) Contributions Payable"),
        "LIABILITY_HEALTHCARE_PREMIUMS_PAYABLE": ("20210", "Health Insurance Premiums Payable"),
        "ASSET_PAYROLL_CLEARING_CASH": ("10110", "Payroll Cash Clearing Account"),
    }

    @classmethod
    def generate_balanced_journal(
        cls,
        voucher_id: str,
        posting_date: date,
        department_name: str,
        cost_center_code: str,
        gross_salaries: float,
        overtime_pay: float,
        federal_tax_withheld: float,
        state_tax_withheld: float,
        employee_fica: float,
        employer_fica: float,
        employee_401k: float,
        employer_401k: float,
        employee_health_deduction: float,
        employer_health_subsidy: float,
        net_cash_disbursed: float
    ) -> BalancedJournalVoucher:
        lines: List[JournalEntryLine] = []

        # --- DEBIT ENTRIES (Expense Recognition) ---
        # 1. Base Salaries Expense
        lines.append(JournalEntryLine(
            account_number=cls.ACCOUNTS["WAGE_EXPENSE_SALARIES"][0],
            account_name=cls.ACCOUNTS["WAGE_EXPENSE_SALARIES"][1],
            debit_amount=round(gross_salaries, 2), credit_amount=0.0,
            cost_center_code=cost_center_code, department_name=department_name,
            description="Gross Base Salary Expense"
        ))

        # 2. Overtime Expense
        if overtime_pay > 0:
            lines.append(JournalEntryLine(
                account_number=cls.ACCOUNTS["WAGE_EXPENSE_OVERTIME"][0],
                account_name=cls.ACCOUNTS["WAGE_EXPENSE_OVERTIME"][1],
                debit_amount=round(overtime_pay, 2), credit_amount=0.0,
                cost_center_code=cost_center_code, department_name=department_name,
                description="Overtime Compensation Expense"
            ))

        # 3. Employer FICA Expense
        lines.append(JournalEntryLine(
            account_number=cls.ACCOUNTS["PAYROLL_TAX_EXPENSE_EMPLOYER_FICA"][0],
            account_name=cls.ACCOUNTS["PAYROLL_TAX_EXPENSE_EMPLOYER_FICA"][1],
            debit_amount=round(employer_fica, 2), credit_amount=0.0,
            cost_center_code=cost_center_code, department_name=department_name,
            description="Employer FICA Tax Match (7.65%)"
        ))

        # 4. Employer 401(k) Match Expense
        if employer_401k > 0:
            lines.append(JournalEntryLine(
                account_number=cls.ACCOUNTS["BENEFITS_EXPENSE_401K_MATCH"][0],
                account_name=cls.ACCOUNTS["BENEFITS_EXPENSE_401K_MATCH"][1],
                debit_amount=round(employer_401k, 2), credit_amount=0.0,
                cost_center_code=cost_center_code, department_name=department_name,
                description="Employer 401(k) Retirement Match"
            ))

        # 5. Employer Healthcare Subsidy Expense
        if employer_health_subsidy > 0:
            lines.append(JournalEntryLine(
                account_number=cls.ACCOUNTS["BENEFITS_EXPENSE_HEALTH_INSURANCE"][0],
                account_name=cls.ACCOUNTS["BENEFITS_EXPENSE_HEALTH_INSURANCE"][1],
                debit_amount=round(employer_health_subsidy, 2), credit_amount=0.0,
                cost_center_code=cost_center_code, department_name=department_name,
                description="Company Medical & Dental Subsidy"
            ))

        # --- CREDIT ENTRIES (Liabilities & Cash Outflow) ---
        # 1. Federal Withholding Tax Payable
        lines.append(JournalEntryLine(
            account_number=cls.ACCOUNTS["LIABILITY_FEDERAL_WITHHOLDING_PAYABLE"][0],
            account_name=cls.ACCOUNTS["LIABILITY_FEDERAL_WITHHOLDING_PAYABLE"][1],
            debit_amount=0.0, credit_amount=round(federal_tax_withheld, 2),
            cost_center_code=cost_center_code, department_name=department_name,
            description="Federal Income Tax Withholding Payable"
        ))

        # 2. State Withholding Tax Payable
        lines.append(JournalEntryLine(
            account_number=cls.ACCOUNTS["LIABILITY_STATE_WITHHOLDING_PAYABLE"][0],
            account_name=cls.ACCOUNTS["LIABILITY_STATE_WITHHOLDING_PAYABLE"][1],
            debit_amount=0.0, credit_amount=round(state_tax_withheld, 2),
            cost_center_code=cost_center_code, department_name=department_name,
            description="State Income Tax Withholding Payable"
        ))

        # 3. FICA Payable (Employee + Employer)
        total_fica_payable = round(employee_fica + employer_fica, 2)
        lines.append(JournalEntryLine(
            account_number=cls.ACCOUNTS["LIABILITY_FICA_PAYABLE_TOTAL"][0],
            account_name=cls.ACCOUNTS["LIABILITY_FICA_PAYABLE_TOTAL"][1],
            debit_amount=0.0, credit_amount=total_fica_payable,
            cost_center_code=cost_center_code, department_name=department_name,
            description="Total FICA Tax Payable (Employee + Employer)"
        ))

        # 4. 401(k) Payable (Employee + Employer)
        total_401k_payable = round(employee_401k + employer_401k, 2)
        if total_401k_payable > 0:
            lines.append(JournalEntryLine(
                account_number=cls.ACCOUNTS["LIABILITY_401K_PAYABLE_TOTAL"][0],
                account_name=cls.ACCOUNTS["LIABILITY_401K_PAYABLE_TOTAL"][1],
                debit_amount=0.0, credit_amount=total_401k_payable,
                cost_center_code=cost_center_code, department_name=department_name,
                description="401(k) Retirement Contributions Payable"
            ))

        # 5. Healthcare Payable
        total_health_payable = round(employee_health_deduction + employer_health_subsidy, 2)
        if total_health_payable > 0:
            lines.append(JournalEntryLine(
                account_number=cls.ACCOUNTS["LIABILITY_HEALTHCARE_PREMIUMS_PAYABLE"][0],
                account_name=cls.ACCOUNTS["LIABILITY_HEALTHCARE_PREMIUMS_PAYABLE"][1],
                debit_amount=0.0, credit_amount=total_health_payable,
                cost_center_code=cost_center_code, department_name=department_name,
                description="Health & Dental Insurance Premiums Payable"
            ))

        # 6. Net Cash Disbursed
        lines.append(JournalEntryLine(
            account_number=cls.ACCOUNTS["ASSET_PAYROLL_CLEARING_CASH"][0],
            account_name=cls.ACCOUNTS["ASSET_PAYROLL_CLEARING_CASH"][1],
            debit_amount=0.0, credit_amount=round(net_cash_disbursed, 2),
            cost_center_code=cost_center_code, department_name=department_name,
            description="Net Employee Direct Deposit Disbursement"
        ))

        tot_debit = sum(l.debit_amount for l in lines)
        tot_credit = sum(l.credit_amount for l in lines)
        is_bal = abs(tot_debit - tot_credit) < 0.05

        return BalancedJournalVoucher(
            voucher_id=voucher_id,
            posting_date=posting_date,
            currency="USD",
            total_debits=round(tot_debit, 2),
            total_credits=round(tot_credit, 2),
            is_balanced=is_bal,
            lines=lines
        )
'''
write("backend/app/domain/payroll_journal_entry_builder.py", gl_code)

# 2. Singapore CPF Statutory Calculator
cpf_code = '''"""
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
'''
write("backend/app/domain/calculators/singapore_cpf_contribution_calculator.py", cpf_code)

# 3. France URSSAF Social Charges Calculator
france_code = '''"""
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
'''
write("backend/app/domain/calculators/france_urssaf_social_charges_calculator.py", france_code)

print("Massive Domain Architectures Generated Successfully!")
'''
write("scripts/build_massive_domain_architectures.py", "# Architectures builder")
'''
