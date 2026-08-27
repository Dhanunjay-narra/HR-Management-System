"""
Enterprise Collective Bargaining Agreement (CBA) & Trade Union Registry
Prescribes negotiated wage scales, overtime premium multipliers, shift differentials, and formal grievance arbitration timelines.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class UnionCollectiveAgreement:
    cba_code: str
    union_name: str
    industry_sector: str
    negotiated_clauses: List[str]


MASTER_CBA_REGISTRY: Dict[str, UnionCollectiveAgreement] = {
    "CBA-TECH-01": UnionCollectiveAgreement(
        cba_code="CBA-TECH-01",
        union_name="Communications Workers of America (CWA) / CODE-CWA",
        industry_sector="Software & Game Development",
        negotiated_clauses=['Article 1: Union Recognition & Bargaining Unit Scope (All Full-Time Software Engineers and QA)', 'Article 2: Standard 37.5-Hour Workweek with 1.5x Overtime Pay for Weekend On-Call Deployment Work', 'Article 3: Guaranteed 3.5% Annual Base Wage Cost-of-Living Adjustment (COLA)', 'Article 4: 12-Week Paid Parental Leave with Complete Health Insurance Maintenance', 'Article 5: Just Cause Disciplinary Escalation and 3-Tier Grievance Arbitration Protocol', 'Article 6: $2,000 Annual Ergonomic Home-Office & Hardware Refresh Allowance', 'Article 7: Intellectual Property Carve-Out for Personal Independent Open Source Projects']
    ),
    "CBA-HLTH-02": UnionCollectiveAgreement(
        cba_code="CBA-HLTH-02",
        union_name="National Nurses United / SEIU Healthcare",
        industry_sector="Clinical & Healthcare Operations",
        negotiated_clauses=['Article 1: Mandatory Safe Staffing Ratios (1:4 Nurse-to-Patient in Medical-Surgical)', 'Article 2: Double-Time (2.0x) Premium Pay for Consecutive 12-Hour Shift Call-Ins', 'Article 3: Comprehensive Zero-Cost Comprehensive PPO Healthcare for Nurses & Dependents', 'Article 4: Workplace Violence Prevention Protocols and Mandatory Security Coverage', 'Article 5: Fully Funded Continuing Nursing Education (CNE) and Specialty Certification Reimbursement']
    ),
    "CBA-AERO-03": UnionCollectiveAgreement(
        cba_code="CBA-AERO-03",
        union_name="International Association of Machinists (IAMAW)",
        industry_sector="Aerospace & High-Tech Manufacturing",
        negotiated_clauses=['Article 1: Precision Machinist Seniority Progression and Skill-Tier Wage Multipliers', 'Article 2: Defined Benefit Pension Multiplier ($105/month per year of accredited service)', 'Article 3: Triple-Time (3.0x) Pay on Federal Statutory Holidays', 'Article 4: Mandatory Apprenticeship Training and Tool Replacement Subsidy', 'Article 5: 90-Day Advance Notification for Plant Modernization or Automated Tooling']
    ),
    "CBA-LOG-04": UnionCollectiveAgreement(
        cba_code="CBA-LOG-04",
        union_name="International Brotherhood of Teamsters",
        industry_sector="Supply Chain & Logistics Operations",
        negotiated_clauses=['Article 1: Driver Safety, Maximum Daily Driving Hours (DOT 11-Hour Cap), and Rest Breaks', 'Article 2: 100% Employer-Paid Teamsters Health & Welfare Trust Fund Coverage', 'Article 3: Longevity Bonus Pay ($0.50/hour increase per 5 years continuous service)', 'Article 4: Severe Weather Route Cancellation Protections with Full Shift Pay Guarantee', 'Article 5: Seniority-Based Preferred Shift and Route Bidding Process']
    ),
}

class CBAService:
    @classmethod
    def get_cba(cls, code: str) -> UnionCollectiveAgreement:
        return MASTER_CBA_REGISTRY.get(code)

    @classmethod
    def get_all_cbas(cls) -> List[UnionCollectiveAgreement]:
        return list(MASTER_CBA_REGISTRY.values())
