"""
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
