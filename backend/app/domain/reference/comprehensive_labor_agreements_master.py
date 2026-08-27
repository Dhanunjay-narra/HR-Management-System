"""
Master Collective Bargaining Agreements (CBA) Database
Prescribes negotiated working conditions, seniority progressions, and grievance arbitration tiers.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class CBAMasterRecord:
    cba_code: str
    union_name: str
    industry_sector: str
    articles: List[str]


MASTER_CBA_DATABASE: Dict[str, CBAMasterRecord] = {
    "CBA-MFR-01": CBAMasterRecord(
        cba_code="CBA-MFR-01",
        union_name="United Auto Workers (UAW) / Advanced Manufacturing",
        industry_sector="Manufacturing & Hardware",
        articles=['Article 1: Bargaining Unit Definition & Seniority Rights', 'Article 2: Tiered Wage Scale Progression with 4-Year Full Rate Parity', 'Article 3: Cost of Living Allowance (COLA) Formula linked to CPI-W Index', 'Article 4: Overtime Scheduling Rules (Maximum 10 Hours Daily Cap)', 'Article 5: Plant Investment & Job Security Commitments']
    ),
    "CBA-MED-02": CBAMasterRecord(
        cba_code="CBA-MED-02",
        union_name="National Nurses Organizing Committee (NNOC)",
        industry_sector="Healthcare & Life Sciences",
        articles=['Article 1: Safe Patient Handling & Mandatory Staffing Ratios', 'Article 2: 15% Night Shift and 20% Weekend Differential Pay', 'Article 3: Comprehensive Zero-Cost Health & Wellness Benefit Coverage', 'Article 4: Paid Continuing Professional Education Leave']
    ),
    "CBA-EDU-03": CBAMasterRecord(
        cba_code="CBA-EDU-03",
        union_name="Higher Education Faculty & Researchers Union",
        industry_sector="Education & Research",
        articles=['Article 1: Academic Freedom & Intellectual Property Ownership', 'Article 2: Multi-Year Contract Appointments for Non-Tenure Track Faculty', 'Article 3: Sabbatical Leave Eligibility & Research Travel Stipends']
    ),
}

class CBAMasterService:
    @classmethod
    def get_cba(cls, code: str) -> CBAMasterRecord:
        return MASTER_CBA_DATABASE.get(code)

    @classmethod
    def get_all(cls) -> List[CBAMasterRecord]:
        return list(MASTER_CBA_DATABASE.values())
