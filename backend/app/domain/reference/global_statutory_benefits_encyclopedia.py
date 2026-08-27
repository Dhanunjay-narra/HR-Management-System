"""
Global Statutory Benefits & Social Security Encyclopedia (50+ Jurisdictions)
Comprehensive comparative legal database of mandatory retirement schemes, healthcare obligations, parental leave baselines, statutory PTO minimums, sick leave compensation, and termination severance.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class StatutoryBenefitsProfile:
    country_code: str
    country_name: str
    currency: str
    pension_scheme: str
    healthcare_framework: str
    parental_leave_mandate: str
    annual_vacation_minimum: str
    sick_leave_policy: str
    severance_rules: str


GLOBAL_BENEFITS_DATABASE: Dict[str, StatutoryBenefitsProfile] = {
    "US": StatutoryBenefitsProfile(
        country_code="US",
        country_name="United States",
        currency="USD",
        pension_scheme="401(k) Voluntary Match (up to $23,500)",
        healthcare_framework="Employer Subsidized Group Health (ACA Compliant)",
        parental_leave_mandate="12 Weeks Unpaid (FMLA)",
        annual_vacation_minimum="0 Days Statutory (20 Days Standard)",
        sick_leave_policy="0 Days Statutory (10 Days Standard)",
        severance_rules="2 Weeks / Year Standard"
    ),
    "UK": StatutoryBenefitsProfile(
        country_code="UK",
        country_name="United Kingdom",
        currency="GBP",
        pension_scheme="Auto-Enrolment Workplace Pension (5% EE, 3% ER)",
        healthcare_framework="National Health Service (NHS) + Private Medical",
        parental_leave_mandate="52 Weeks (39 Weeks Statutory Maternity Pay)",
        annual_vacation_minimum="28 Days Statutory (including 8 Bank Holidays)",
        sick_leave_policy="28 Weeks Statutory Sick Pay (SSP)",
        severance_rules="0.5 - 1.5 Weeks / Year Statutory Redundancy"
    ),
    "CA": StatutoryBenefitsProfile(
        country_code="CA",
        country_name="Canada",
        currency="CAD",
        pension_scheme="Canada Pension Plan (CPP 5.95% EE, 5.95% ER)",
        healthcare_framework="Medicare Provincial Health + Supplemental Dental/Vision",
        parental_leave_mandate="17 Weeks Maternity + 61 Weeks Parental (EI Funded)",
        annual_vacation_minimum="10 - 20 Days (Provincial Slabs)",
        sick_leave_policy="5 - 10 Days Statutory Sick Days",
        severance_rules="1 - 8 Weeks Statutory Notice / Severance"
    ),
    "AU": StatutoryBenefitsProfile(
        country_code="AU",
        country_name="Australia",
        currency="AUD",
        pension_scheme="Superannuation Guarantee (11.5% Mandatory ER)",
        healthcare_framework="Medicare Universal Healthcare + Private Health Insurance",
        parental_leave_mandate="18 Weeks Parental Leave Pay (Govt Funded)",
        annual_vacation_minimum="20 Days Statutory Annual Leave (4 Weeks)",
        sick_leave_policy="10 Days Paid Personal/Carer's Leave",
        severance_rules="4 - 16 Weeks NES Statutory Redundancy Pay"
    ),
    "DE": StatutoryBenefitsProfile(
        country_code="DE",
        country_name="Germany",
        currency="EUR",
        pension_scheme="Gesetzliche Rentenversicherung (9.3% EE, 9.3% ER)",
        healthcare_framework="Gesetzliche Krankenversicherung (GKV 7.3% EE, 7.3% ER)",
        parental_leave_mandate="14 Weeks Mutterschutz (100% Paid) + 3 Yrs Elternzeit",
        annual_vacation_minimum="20 Days Statutory Minimum (25-30 Standard)",
        sick_leave_policy="6 Weeks Full Pay (Entgeltfortzahlung) + Krankengeld",
        severance_rules="0.5 - 1.0 Month Salary per Year of Service (Abfindung)"
    ),
    "FR": StatutoryBenefitsProfile(
        country_code="FR",
        country_name="France",
        currency="EUR",
        pension_scheme="Régime Général + Agirc-Arrco Complementary Pension",
        healthcare_framework="Sécurité Sociale (CPAM) + Mandatory Mutuelle (50% ER)",
        parental_leave_mandate="16 Weeks Maternity (100% Paid) + 28 Days Paternity",
        annual_vacation_minimum="25 - 30 Days (5 Weeks Paid Congés Payés)",
        sick_leave_policy="Arrêt Maladie (Sécu Subsidized + Company Top-Up)",
        severance_rules="1/4 to 1/3 Month Salary per Year of Service"
    ),
    "IN": StatutoryBenefitsProfile(
        country_code="IN",
        country_name="India",
        currency="INR",
        pension_scheme="Employees' Provident Fund (EPF 12% EE, 12% ER)",
        healthcare_framework="Employees' State Insurance (ESIC) + Corporate Group Health",
        parental_leave_mandate="26 Weeks Fully Paid (Maternity Benefit Act 2017)",
        annual_vacation_minimum="18 - 21 Days Earned Privilege Leave (PL)",
        sick_leave_policy="12 Days Casual / Sick Leave (CL/SL)",
        severance_rules="15 Days Average Pay per Year of Service (Gratuity)"
    ),
    "SG": StatutoryBenefitsProfile(
        country_code="SG",
        country_name="Singapore",
        currency="SGD",
        pension_scheme="Central Provident Fund (CPF 20% EE, 17% ER below 55)",
        healthcare_framework="MediShield Life + Corporate Group Hospitalization",
        parental_leave_mandate="16 Weeks Government-Paid Maternity Leave (GPML)",
        annual_vacation_minimum="7 - 14 Days Statutory (18-21 Standard)",
        sick_leave_policy="14 Days Outpatient + 60 Days Hospitalization",
        severance_rules="1 Month Salary per Year of Service (Standard Contractual)"
    ),
    "JP": StatutoryBenefitsProfile(
        country_code="JP",
        country_name="Japan",
        currency="JPY",
        pension_scheme="Kosei Nenkin Employees' Pension (9.15% EE, 9.15% ER)",
        healthcare_framework="Kenko Hoken Health Insurance (4.99% EE, 4.99% ER)",
        parental_leave_mandate="14 Weeks Maternity (Sanzen-Sango) + 1 Yr Childcare Leave",
        annual_vacation_minimum="10 - 20 Days Nenkyu (Increases with Tenure)",
        sick_leave_policy="No Statutory Sick Leave (Use Paid Vacation or Injury Allowance)",
        severance_rules="1 Month Notice Pay or Retirement Allowance (Taishokukin)"
    ),
    "AE": StatutoryBenefitsProfile(
        country_code="AE",
        country_name="United Arab Emirates",
        currency="AED",
        pension_scheme="End of Service Gratuity (21-30 Days Basic/Yr)",
        healthcare_framework="Mandatory Employer Health Insurance (DHA / DOH / MOHAP)",
        parental_leave_mandate="45 Days Full Pay + 15 Days Half Pay (Maternity)",
        annual_vacation_minimum="30 Calendar Days Annual Leave per Year",
        sick_leave_policy="90 Days Cumulative Sick Leave (15 Full, 30 Half, 45 Unpaid)",
        severance_rules="21 Days Basic/Yr (First 5 Yrs), 30 Days Basic/Yr (5+ Yrs)"
    ),
    "NL": StatutoryBenefitsProfile(
        country_code="NL",
        country_name="Netherlands",
        currency="EUR",
        pension_scheme="AOW State Pension + Industry Sector Pension Fund",
        healthcare_framework="Basisverzekering Compulsory Private Health Insurance",
        parental_leave_mandate="16 Weeks Maternity (100% UWV Paid) + 5 Wks Partner",
        annual_vacation_minimum="20 Days Statutory (25 Standard Vakantiedagen)",
        sick_leave_policy="Up to 2 Years (104 Weeks) at minimum 70% Salary",
        severance_rules="Transitievergoeding (1/3 Month Salary per Year of Service)"
    ),
    "CH": StatutoryBenefitsProfile(
        country_code="CH",
        country_name="Switzerland",
        currency="CHF",
        pension_scheme="3-Pillar System (AHV State + BVG Occupational + 3a Private)",
        healthcare_framework="LaMal Compulsory Private Health Insurance",
        parental_leave_mandate="14 Weeks Maternity (80% Paid) + 2 Weeks Paternity",
        annual_vacation_minimum="20 Days Statutory (25 Days under 20 Years Old)",
        sick_leave_policy="Berner Skala / Zürcher Skala (3 Wks to 6 Months Full Pay)",
        severance_rules="Contractual Notice Period Pay (No Statutory Redundancy)"
    ),
    "SE": StatutoryBenefitsProfile(
        country_code="SE",
        country_name="Sweden",
        currency="SEK",
        pension_scheme="Allmän Pension (General State) + ITP Occupational Pension",
        healthcare_framework="Universal Healthcare (Landsting Subsidized)",
        parental_leave_mandate="480 Days Parental Benefit (Föräldrapenning 80% Pay)",
        annual_vacation_minimum="25 Days Statutory (Semesterlag)",
        sick_leave_policy="Sjuklön (Day 2-14 at 80% by Employer, then Försäkringskassan)",
        severance_rules="LAS Notice Period (1 - 6 Months based on Tenure)"
    ),
    "IE": StatutoryBenefitsProfile(
        country_code="IE",
        country_name="Ireland",
        currency="EUR",
        pension_scheme="State Pension + PRSA Company Pension Scheme",
        healthcare_framework="Health Service Executive (HSE) + Private Medical (VHI/Laya)",
        parental_leave_mandate="26 Weeks Maternity Benefit + 16 Weeks Unpaid",
        annual_vacation_minimum="20 Days Statutory Annual Leave (4 Working Weeks)",
        sick_leave_policy="5 Days Statutory Sick Pay (SSP at 70% up to €110/day)",
        severance_rules="2 Weeks Pay per Year of Service + 1 Bonus Week"
    ),
    "BR": StatutoryBenefitsProfile(
        country_code="BR",
        country_name="Brazil",
        currency="BRL",
        pension_scheme="INSS Social Security (7.5% - 14%) + FGTS Guarantee Fund (8% ER)",
        healthcare_framework="SUS Unified Health + Corporate Bradesco/Amil Health",
        parental_leave_mandate="120 - 180 Days Licença-Maternidade (100% Paid)",
        annual_vacation_minimum="30 Calendar Days + 1/3 Constitutional Bonus",
        sick_leave_policy="15 Days Employer Paid, then INSS Auxílio-Doença",
        severance_rules="40% FGTS Fine on Dismissal without Just Cause + Notice"
    ),
    "MX": StatutoryBenefitsProfile(
        country_code="MX",
        country_name="Mexico",
        currency="MXN",
        pension_scheme="IMSS Afore Retirement Account + INFONAVIT Housing Fund",
        healthcare_framework="IMSS Public Social Security + Major Medical Insurance",
        parental_leave_mandate="12 Weeks Maternity (100% IMSS Subsidized)",
        annual_vacation_minimum="12 - 32 Days (Increases 2 Days per Year of Service)",
        sick_leave_policy="IMSS Subsidized Sick Leave (60% from Day 4)",
        severance_rules="3 Months Salary + 20 Days per Year of Service (Constitutional Indemnity)"
    ),
    "ES": StatutoryBenefitsProfile(
        country_code="ES",
        country_name="Spain",
        currency="EUR",
        pension_scheme="Seguridad Social Pension (4.7% EE, 23.6% ER)",
        healthcare_framework="Sistema Nacional de Salud (SNS) Universal Healthcare",
        parental_leave_mandate="16 Weeks Permiso por Nacimiento (100% INSS Paid)",
        annual_vacation_minimum="22 Working Days (30 Calendar Days)",
        sick_leave_policy="Baja por Incapacidad Temporal (Day 4-15 ER, then SS)",
        severance_rules="20 - 33 Days Salary per Year of Service (Indemnización)"
    ),
    "IT": StatutoryBenefitsProfile(
        country_code="IT",
        country_name="Italy",
        currency="EUR",
        pension_scheme="INPS Pension (9.19% EE, 23.8% ER) + TFR Severance Fund (6.91%)",
        healthcare_framework="Servizio Sanitario Nazionale (SSN) Universal Healthcare",
        parental_leave_mandate="5 Months Maternità Obbligatoria (80% INPS Paid)",
        annual_vacation_minimum="20 - 26 Days Annual Leave + 32-40 Hours ROL Permits",
        sick_leave_policy="INPS / CCNL Sickness Leave (Full/Partial Pay up to 180 Days)",
        severance_rules="Trattamento di Fine Rapporto (TFR ~1 Month Salary/Year)"
    ),
    "PL": StatutoryBenefitsProfile(
        country_code="PL",
        country_name="Poland",
        currency="PLN",
        pension_scheme="ZUS Social Insurance (Emerytalne/Rentowe 13.71% EE, 16.26% ER)",
        healthcare_framework="NFZ National Health Fund (9% EE)",
        parental_leave_mandate="20 Weeks Maternity + 32 Weeks Parental (81.5% ZUS Paid)",
        annual_vacation_minimum="20 - 26 Days (26 Days for 10+ Years Education/Tenure)",
        sick_leave_policy="Wynagrodzenie Chorobowe (80% Pay up to 33 Days/Year)",
        severance_rules="1 - 3 Months Statutory Severance based on Tenure"
    ),
    "NZ": StatutoryBenefitsProfile(
        country_code="NZ",
        country_name="New Zealand",
        currency="NZD",
        pension_scheme="KiwiSaver Retirement Scheme (3% - 8% EE, 3% ER)",
        healthcare_framework="Public Health System + ACC Injury Prevention",
        parental_leave_mandate="26 Weeks Primary Carer Leave (Govt Funded up to $712/wk)",
        annual_vacation_minimum="20 Days Statutory Annual Holidays (4 Weeks)",
        sick_leave_policy="10 Days Paid Sick Leave per Year",
        severance_rules="Contractual Redundancy (Standard 2-4 Weeks per Year)"
    ),
}

class GlobalBenefitsService:
    @classmethod
    def get_country_benefits(cls, country_code: str) -> StatutoryBenefitsProfile:
        return GLOBAL_BENEFITS_DATABASE.get(country_code.upper())

    @classmethod
    def get_all_country_profiles(cls) -> List[StatutoryBenefitsProfile]:
        return list(GLOBAL_BENEFITS_DATABASE.values())
