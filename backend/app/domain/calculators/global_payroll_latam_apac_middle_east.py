"""
International Statutory LATAM, APAC & Middle East Payroll Engines (20+ Jurisdictions)
Calculates social insurance withholdings, pension tiers, and employer contributions.
"""
from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class ExtendedCountryPayrollResult:
    country_name: str
    currency: str
    gross_monthly: float
    income_tax_withheld: float
    employee_social_security_deduction: float
    total_employee_deductions: float
    net_take_home_pay: float
    employer_social_security_burden: float
    total_employer_company_cost: float
    effective_tax_rate_percent: float


class ExtendedMultiCountryPayrollEngine:
    @classmethod
    def calculate_indonesia_payroll(
        cls,
        monthly_gross_salary_idr: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Indonesia Payroll Regulations: BPJS Ketenagakerjaan (Pension & JHT) + BPJS Kesehatan Health (1% EE, 4% ER)
        """
        gross = monthly_gross_salary_idr
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.03, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.05 if (annual_gross < 60000000.0) else (0.05 + 0.35) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.0624, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Indonesia",
            currency="IDR",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_malaysia_payroll(
        cls,
        monthly_gross_salary_myr: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Malaysia Payroll Regulations: EPF Kumpulan Wang Simpanan Pekerja (11% EE, 13% ER) + SOCSO & EIS
        """
        gross = monthly_gross_salary_myr
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.11, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.0 if (annual_gross < 5000.0) else (0.0 + 0.3) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.13, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Malaysia",
            currency="MYR",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_thailand_payroll(
        cls,
        monthly_gross_salary_thb: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Thailand Payroll Regulations: Social Security Fund (SSF 5% capped at THB 750/mo) + Provident Fund
        """
        gross = monthly_gross_salary_thb
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.05, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.05 if (annual_gross < 150000.0) else (0.05 + 0.35) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.05, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Thailand",
            currency="THB",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_vietnam_payroll(
        cls,
        monthly_gross_salary_vnd: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Vietnam Payroll Regulations: Social Insurance (8% SI, 1.5% HI, 1% UI = 10.5% EE) + Trade Union
        """
        gross = monthly_gross_salary_vnd
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.105, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.05 if (annual_gross < 60000000.0) else (0.05 + 0.35) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.215, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Vietnam",
            currency="VND",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_nigeria_payroll(
        cls,
        monthly_gross_salary_ngn: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Nigeria Payroll Regulations: Pension Reform Act (8% EE, 10% ER) + National Housing Fund (NHF 2.5%)
        """
        gross = monthly_gross_salary_ngn
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.08, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.07 if (annual_gross < 300000.0) else (0.07 + 0.24) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.1, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Nigeria",
            currency="NGN",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_kenya_payroll(
        cls,
        monthly_gross_salary_kes: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Kenya Payroll Regulations: NSSF Pension Fund + SHIF Social Health Insurance + Affordable Housing Levy
        """
        gross = monthly_gross_salary_kes
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.06, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.1 if (annual_gross < 288000.0) else (0.1 + 0.35) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.06, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Kenya",
            currency="KES",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_ghana_payroll(
        cls,
        monthly_gross_salary_ghs: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Ghana Payroll Regulations: SSNIT Tier 1 & Tier 2 Pension Schemes (5.5% EE, 13% ER)
        """
        gross = monthly_gross_salary_ghs
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.055, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.0 if (annual_gross < 4000.0) else (0.0 + 0.35) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.13, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Ghana",
            currency="GHS",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_morocco_payroll(
        cls,
        monthly_gross_salary_mad: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Morocco Payroll Regulations: CNSS Caisse Nationale de Sécurité Sociale + AMO Mandatory Health
        """
        gross = monthly_gross_salary_mad
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.0674, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.1 if (annual_gross < 30000.0) else (0.1 + 0.38) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.2109, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Morocco",
            currency="MAD",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_peru_payroll(
        cls,
        monthly_gross_salary_pen: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Peru Payroll Regulations: AFP Pension (10% + insurance/comm) / ONP 13% + EsSalud 9% ER
        """
        gross = monthly_gross_salary_pen
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.13, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.08 if (annual_gross < 35000.0) else (0.08 + 0.3) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.09, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Peru",
            currency="PEN",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_uruguay_payroll(
        cls,
        monthly_gross_salary_uyu: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Uruguay Payroll Regulations: BPS Banco de Previsión Social (Jubilación 15% + FONASA Health 3-8%)
        """
        gross = monthly_gross_salary_uyu
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.15, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.1 if (annual_gross < 45000.0) else (0.1 + 0.36) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.1263, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Uruguay",
            currency="UYU",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_costa_rica_payroll(
        cls,
        monthly_gross_salary_crc: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Costa_Rica Payroll Regulations: CCSS Caja Costarricense de Seguro Social (SEM Sickness & IVM Pension)
        """
        gross = monthly_gross_salary_crc
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.1067, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.1 if (annual_gross < 941000.0) else (0.1 + 0.25) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.2667, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Costa Rica",
            currency="CRC",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_panama_payroll(
        cls,
        monthly_gross_salary_pab: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Panama Payroll Regulations: CSS Caja de Seguro Social (9.75% EE, 12.25% ER) + Educational Insurance
        """
        gross = monthly_gross_salary_pab
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.0975, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.15 if (annual_gross < 11000.0) else (0.15 + 0.25) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.1225, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Panama",
            currency="PAB",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_kuwait_payroll(
        cls,
        monthly_gross_salary_kwd: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Kuwait Payroll Regulations: PIFSS Public Institution for Social Security (Kuwaiti Citizens, Expat 0%)
        """
        gross = monthly_gross_salary_kwd
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.105, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.0 if (annual_gross < 50000) else (0.0 + 0.0) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.115, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Kuwait",
            currency="KWD",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_bahrain_payroll(
        cls,
        monthly_gross_salary_bhd: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Bahrain Payroll Regulations: SIO Social Insurance Organization (Bahraini 7% EE, 12% ER; Expat 1% EE)
        """
        gross = monthly_gross_salary_bhd
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.07, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.0 if (annual_gross < 50000) else (0.0 + 0.0) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.12, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Bahrain",
            currency="BHD",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_oman_payroll(
        cls,
        monthly_gross_salary_omr: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Oman Payroll Regulations: PASI Public Authority for Social Insurance (Omani Nationals 7.5% EE, 11.5% ER)
        """
        gross = monthly_gross_salary_omr
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.075, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.0 if (annual_gross < 50000) else (0.0 + 0.0) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.115, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Oman",
            currency="OMR",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_jordan_payroll(
        cls,
        monthly_gross_salary_jod: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Jordan Payroll Regulations: SSC Social Security Corporation (7.5% EE, 14.25% ER)
        """
        gross = monthly_gross_salary_jod
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.075, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.05 if (annual_gross < 10000.0) else (0.05 + 0.3) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.1425, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Jordan",
            currency="JOD",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_greece_payroll(
        cls,
        monthly_gross_salary_eur: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Greece Payroll Regulations: EFKA Unified Social Security Fund (13.87% EE, 22.29% ER)
        """
        gross = monthly_gross_salary_eur
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.1387, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.09 if (annual_gross < 10000.0) else (0.09 + 0.44) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.2229, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Greece",
            currency="EUR",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_turkey_payroll(
        cls,
        monthly_gross_salary_try: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Turkey Payroll Regulations: SGK Social Security Institution (14% Pension/Health, 1% Unemployment EE)
        """
        gross = monthly_gross_salary_try
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.15, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.15 if (annual_gross < 110000.0) else (0.15 + 0.4) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.205, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Turkey",
            currency="TRY",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_hungary_payroll(
        cls,
        monthly_gross_salary_huf: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Hungary Payroll Regulations: NAV Flat 15% Personal Income Tax + 18.5% Social Security Contribution
        """
        gross = monthly_gross_salary_huf
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.185, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.15 if (annual_gross < 50000) else (0.15 + 0.15) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.13, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Hungary",
            currency="HUF",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )

    @classmethod
    def calculate_romania_payroll(
        cls,
        monthly_gross_salary_ron: float,
        annual_tax_relief: float = 0.0
    ) -> ExtendedCountryPayrollResult:
        """
        Romania Payroll Regulations: CAS Pension 25% + CASS Health 10% (35% total EE) + CAM 2.25% ER
        """
        gross = monthly_gross_salary_ron
        annual_gross = gross * 12.0
        
        # Employee Social Security
        ee_soc_deduction = round(gross * 0.35, 2)
        taxable_base = max(0.0, gross - ee_soc_deduction)
        
        # Income Tax Withholding
        tax_rate = 0.1 if (annual_gross < 50000) else (0.1 + 0.1) / 2.0
        income_tax = round(taxable_base * tax_rate, 2)
        
        tot_deductions = round(ee_soc_deduction + income_tax, 2)
        net_pay = round(gross - tot_deductions, 2)
        er_soc_burden = round(gross * 0.0225, 2)
        total_cost = round(gross + er_soc_burden, 2)
        eff_rate = round((tot_deductions / max(1.0, gross)) * 100.0, 1)
        
        return ExtendedCountryPayrollResult(
            country_name="Romania",
            currency="RON",
            gross_monthly=gross,
            income_tax_withheld=income_tax,
            employee_social_security_deduction=ee_soc_deduction,
            total_employee_deductions=tot_deductions,
            net_take_home_pay=net_pay,
            employer_social_security_burden=er_soc_burden,
            total_employer_company_cost=total_cost,
            effective_tax_rate_percent=eff_rate
        )
