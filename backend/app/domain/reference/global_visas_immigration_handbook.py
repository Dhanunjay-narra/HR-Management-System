"""
Global Work Authorization & Corporate Immigration Regulatory Handbook
Specifies sponsorship eligibility criteria, maximum stay durations, prevailing wage benchmarks, and renewal schedules for US, UK, EU, Canada, and Australia work visas.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class VisaCategoryRegulation:
    country_code: str
    visa_class: str
    visa_title: str
    target_role_type: str
    max_duration_years: float
    is_dual_intent_permitted: bool
    requires_labor_market_test: bool
    prevailing_wage_mandatory: bool
    filing_window_timeline: str
    renewal_extension_limits: str


GLOBAL_VISA_REGULATIONS_REGISTRY: Dict[str, VisaCategoryRegulation] = {
    "US-H1B": VisaCategoryRegulation(
        country_code="US",
        visa_class="H-1B",
        visa_title="Specialty Occupation Professional Worker",
        target_role_type="Software Engineers, Data Scientists, Product Managers",
        max_duration_years=6.0,
        is_dual_intent_permitted=True,
        requires_labor_market_test=False,  # LCA filing with DOL
        prevailing_wage_mandatory=True,
        filing_window_timeline="Annual March lottery window; petition filing April 1 - June 30.",
        renewal_extension_limits="Initial 3-year term, renewable for 3 additional years (6-year maximum without approved I-140)."
    ),
    "US-L1A": VisaCategoryRegulation(
        country_code="US",
        visa_class="L-1A",
        visa_title="Intracompany Transferee Executive or Manager",
        target_role_type="Engineering Directors, Department VPs, Regional General Managers",
        max_duration_years=7.0,
        is_dual_intent_permitted=True,
        requires_labor_market_test=False,
        prevailing_wage_mandatory=False,
        filing_window_timeline="Year-round petition filing; eligible for Blanket L program.",
        renewal_extension_limits="Initial 3-year term (1 year for new offices), renewable up to 7-year cumulative maximum."
    ),
    "US-TN": VisaCategoryRegulation(
        country_code="US",
        visa_class="TN",
        visa_title="USMCA Professional Worker (Canada & Mexico Citizens)",
        target_role_type="Software Engineers, Systems Analysts, Management Consultants",
        max_duration_years=3.0,
        is_dual_intent_permitted=False,
        requires_labor_market_test=False,
        prevailing_wage_mandatory=False,
        filing_window_timeline="Border pre-flight inspection for Canadians; consular processing for Mexicans.",
        renewal_extension_limits="Renewable indefinitely in 3-year increments provided non-immigrant intent is maintained."
    ),
    "UK-SW": VisaCategoryRegulation(
        country_code="UK",
        visa_class="Skilled Worker",
        visa_title="UK Skilled Worker Sponsor Visa",
        target_role_type="Tech professionals with Certificate of Sponsorship (CoS)",
        max_duration_years=5.0,
        is_dual_intent_permitted=True,
        requires_labor_market_test=False,
        prevailing_wage_mandatory=True,
        filing_window_timeline="Continuous online processing with defined CoS quota allocation.",
        renewal_extension_limits="Eligible for Indefinite Leave to Remain (ILR) settlement after 5 years continuous residence."
    ),
    "EU-BLUE": VisaCategoryRegulation(
        country_code="DE",
        visa_class="EU Blue Card",
        visa_title="European Union Highly Qualified Specialist Blue Card",
        target_role_type="STEM graduates, software architects, AI researchers",
        max_duration_years=4.0,
        is_dual_intent_permitted=True,
        requires_labor_market_test=False,
        prevailing_wage_mandatory=True,
        filing_window_timeline="Continuous consular processing with minimum salary threshold (~EUR 45,300 in bottleneck tech fields).",
        renewal_extension_limits="Fast-track German Permanent Settlement Permit (Niederlassungserlaubnis) after 21 months with B1 German."
    )
}
