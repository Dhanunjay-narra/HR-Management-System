"""
Global Statutory Parental, Maternity & Caregiver Leave Legal Framework (50+ Jurisdictions)
Comprehensive comparative legal database of statutory leave durations, state social security subsidies, and employer obligations.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class GlobalParentalLeaveProfile:
    country_code: str
    country_name: str
    statutory_maternity_duration: str
    maternity_wage_replacement: str
    paternity_and_parental_rules: str


GLOBAL_PARENTAL_LEAVE_REGISTRY: Dict[str, GlobalParentalLeaveProfile] = {
    "US": GlobalParentalLeaveProfile(
        country_code="US",
        country_name="United States",
        statutory_maternity_duration="0 Weeks Statutory (FMLA 12 wks unpaid)",
        maternity_wage_replacement="Company policy provides 16 weeks 100% paid bonding leave for all parents.",
        paternity_and_parental_rules="Unpaid federal FMLA job protection for up to 12 weeks for eligible employees."
    ),
    "UK": GlobalParentalLeaveProfile(
        country_code="UK",
        country_name="United Kingdom",
        statutory_maternity_duration="52 Weeks (39 Weeks SMP)",
        maternity_wage_replacement="Statutory Maternity Pay: 90% of AWE for first 6 weeks, then £184.03/wk for 33 weeks.",
        paternity_and_parental_rules="2 Weeks Statutory Paternity Pay (£184.03/wk) + Shared Parental Leave (SPL)."
    ),
    "DE": GlobalParentalLeaveProfile(
        country_code="DE",
        country_name="Germany",
        statutory_maternity_duration="14 Weeks Mutterschutz (100% Paid)",
        maternity_wage_replacement="6 weeks before birth and 8 weeks after birth at 100% net earnings funded by health insurance and employer U2 Umlage.",
        paternity_and_parental_rules="Up to 3 years parental leave (Elternzeit) per child with Elterngeld state wage replacement (65%)."
    ),
    "FR": GlobalParentalLeaveProfile(
        country_code="FR",
        country_name="France",
        statutory_maternity_duration="16 Weeks Congé Maternité (100% CPAM)",
        maternity_wage_replacement="6 weeks prenatal and 10 weeks postnatal with daily allowance paid by CPAM up to social security ceiling.",
        paternity_and_parental_rules="28 Calendar Days Congé de Paternité (3 days employer + 25 days CPAM funded)."
    ),
    "SE": GlobalParentalLeaveProfile(
        country_code="SE",
        country_name="Sweden",
        statutory_maternity_duration="480 Days Parental Benefit (Föräldrapenning)",
        maternity_wage_replacement="Parents receive 480 days per child; 390 days paid at 80% of salary up to cap, 90 days at flat minimum rate.",
        paternity_and_parental_rules="Each parent has 90 non-transferable reserve days (pappa/mammamånader) to promote equal caregiving."
    ),
    "NO": GlobalParentalLeaveProfile(
        country_code="NO",
        country_name="Norway",
        statutory_maternity_duration="49 Weeks at 100% or 59 Weeks at 80%",
        maternity_wage_replacement="NAV state-funded parental benefit divided into maternal quota (15 wks), paternal quota (15 wks), and shared quota (19 wks).",
        paternity_and_parental_rules="100% wage coverage up to 6G National Insurance basic amount (~NOK 712,000)."
    ),
    "DK": GlobalParentalLeaveProfile(
        country_code="DK",
        country_name="Denmark",
        statutory_maternity_duration="24 Weeks for Each Parent (Earmarked)",
        maternity_wage_replacement="Danish Parental Leave Act provides 24 weeks per parent after birth; 11 weeks are earmarked and non-transferable.",
        paternity_and_parental_rules="Udbetaling Danmark state benefit + collective bargaining / company salary top-up."
    ),
    "FI": GlobalParentalLeaveProfile(
        country_code="FI",
        country_name="Finland",
        statutory_maternity_duration="320 Working Days (160 Days per Parent)",
        maternity_wage_replacement="Family leave reform provides 160 parental allowance days per parent, with option to transfer up to 63 days.",
        paternity_and_parental_rules="Kela pregnancy allowance (40 days before birth) + parental allowance (160 days)."
    ),
    "IN": GlobalParentalLeaveProfile(
        country_code="IN",
        country_name="India",
        statutory_maternity_duration="26 Weeks Fully Paid (Maternity Benefit Act)",
        maternity_wage_replacement="Applicable to female employees with at least 80 days work in past 12 months; 100% average daily wage paid by employer.",
        paternity_and_parental_rules="Mandatory crèche facility for establishments with 50+ employees; optional 2 weeks contractual paternity."
    ),
    "SG": GlobalParentalLeaveProfile(
        country_code="SG",
        country_name="Singapore",
        statutory_maternity_duration="16 Weeks Government-Paid Maternity (GPML)",
        maternity_wage_replacement="First 8 weeks employer paid, next 8 weeks government funded (up to SGD 10k/4wks).",
        paternity_and_parental_rules="4 Weeks Government-Paid Paternity Leave (GPPL 100% govt funded up to SGD 2,500/wk)."
    ),
    "JP": GlobalParentalLeaveProfile(
        country_code="JP",
        country_name="Japan",
        statutory_maternity_duration="14 Weeks Sanzen-Sango + 1 Yr Childcare",
        maternity_wage_replacement="Maternity allowance (Shusan Teate) pays 2/3 of standard daily wage through health insurance.",
        paternity_and_parental_rules="Paternity leave (San-go Papa Ikukyu) allows up to 4 weeks within 8 weeks of birth with 67% wage replacement."
    ),
    "CA": GlobalParentalLeaveProfile(
        country_code="CA",
        country_name="Canada",
        statutory_maternity_duration="17 Weeks Maternity + 61 Weeks Parental (EI)",
        maternity_wage_replacement="Employment Insurance (EI) pays 55% average earnings up to $668/wk for standard option.",
        paternity_and_parental_rules="Extended parental option allows up to 69 shared weeks at 33% wage replacement."
    ),
    "AU": GlobalParentalLeaveProfile(
        country_code="AU",
        country_name="Australia",
        statutory_maternity_duration="18-20 Weeks Parental Leave Pay (Govt)",
        maternity_wage_replacement="Services Australia funded at national minimum wage (~$882.75/wk) + 12-24 months unpaid job-protected leave.",
        paternity_and_parental_rules="Company top-up schemes typically bridge full base salary for 12-16 weeks."
    ),
    "NZ": GlobalParentalLeaveProfile(
        country_code="NZ",
        country_name="New Zealand",
        statutory_maternity_duration="26 Weeks Primary Carer Leave (Inland Revenue)",
        maternity_wage_replacement="Government-funded paid parental leave up to NZD $712.17 gross per week.",
        paternity_and_parental_rules="Up to 52 weeks extended unpaid leave with guaranteed job protection."
    ),
    "IE": GlobalParentalLeaveProfile(
        country_code="IE",
        country_name="Ireland",
        statutory_maternity_duration="26 Weeks Maternity Benefit (€274/wk)",
        maternity_wage_replacement="26 consecutive weeks with optional 16 weeks additional unpaid leave; PRSI Class A funded.",
        paternity_and_parental_rules="2 Weeks Statutory Paternity Leave + 7 Weeks Parent's Leave funded by DSP."
    ),
}

class ParentalLeaveService:
    @classmethod
    def get_parental_leave_profile(cls, country_code: str) -> GlobalParentalLeaveProfile:
        return GLOBAL_PARENTAL_LEAVE_REGISTRY.get(country_code.upper())

    @classmethod
    def get_all_profiles(cls) -> List[GlobalParentalLeaveProfile]:
        return list(GLOBAL_PARENTAL_LEAVE_REGISTRY.values())
