"""
Enterprise Master Policy Handbook Corpus (80+ Chapters)
Authoritative corporate policies for automated compliance enforcement and semantic RAG knowledge retrieval.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class EnterprisePolicyChapter:
    policy_id: str
    title: str
    category: str
    effective_date: str
    summary: str
    full_text: str


FULL_POLICY_HANDBOOK_CORPUS: Dict[str, EnterprisePolicyChapter] = {
    "POL-01": EnterprisePolicyChapter(
        policy_id="POL-01",
        title="Global Remote Work & Hybrid Schedule Framework",
        category="Workplace Flexibility",
        effective_date="2026-01-01",
        summary="Guidelines on core hours (10 AM - 4 PM), equipment stipends ($500 home office), ergonomics, and branch office collaboration days.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Guidelines on core hours (10 AM - 4 PM), equipment stipends ($500 home office), ergonomics, and branch office collaboration days.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-02": EnterprisePolicyChapter(
        policy_id="POL-02",
        title="Annual Paid Time Off (PTO) & Statutory Vacation Accruals",
        category="Time Off",
        effective_date="2026-01-01",
        summary="Accrual schedules (1.67 days/mo for 20 days/yr baseline), 5-day rollover limits, and mandatory advance notice for extended absences.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Accrual schedules (1.67 days/mo for 20 days/yr baseline), 5-day rollover limits, and mandatory advance notice for extended absences.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-03": EnterprisePolicyChapter(
        policy_id="POL-03",
        title="Paid Sick Leave, Wellness & Bereavement Absence",
        category="Time Off",
        effective_date="2026-01-01",
        summary="10 annual paid wellness/sick days from Day 1, medical certificate requirements for absences over 3 days, and compassionate leave schedules.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. 10 annual paid wellness/sick days from Day 1, medical certificate requirements for absences over 3 days, and compassionate leave schedules.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-04": EnterprisePolicyChapter(
        policy_id="POL-04",
        title="Parental Bonding, Maternity & Primary Caregiver Leave",
        category="Benefits",
        effective_date="2026-01-01",
        summary="16 weeks 100% paid parental leave for birth/adoptive parents, 8 weeks for secondary caregivers, and 4-week 80% ramp-back program.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. 16 weeks 100% paid parental leave for birth/adoptive parents, 8 weeks for secondary caregivers, and 4-week 80% ramp-back program.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-05": EnterprisePolicyChapter(
        policy_id="POL-05",
        title="Global Information Security & Acceptable Use of Technology",
        category="Security",
        effective_date="2026-01-01",
        summary="Enforces password complexity (14+ chars), MFA, MDM device encryption (BitLocker/FileVault), zero-trust VPN, and clean-desk policy.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Enforces password complexity (14+ chars), MFA, MDM device encryption (BitLocker/FileVault), zero-trust VPN, and clean-desk policy.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-06": EnterprisePolicyChapter(
        policy_id="POL-06",
        title="Code of Business Conduct & Ethics",
        category="Compliance",
        effective_date="2026-01-01",
        summary="Zero tolerance for bribery, FCPA compliance, conflicts of interest disclosures, outside employment guidelines, and gift receipt limits ($50 cap).",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Zero tolerance for bribery, FCPA compliance, conflicts of interest disclosures, outside employment guidelines, and gift receipt limits ($50 cap).\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-07": EnterprisePolicyChapter(
        policy_id="POL-07",
        title="Equal Employment Opportunity & Anti-Harassment Guidelines",
        category="People & Culture",
        effective_date="2026-01-01",
        summary="Strict zero-tolerance policy against discrimination, harassment, retaliation; defines mandatory reporting channels and investigator protocols.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Strict zero-tolerance policy against discrimination, harassment, retaliation; defines mandatory reporting channels and investigator protocols.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-08": EnterprisePolicyChapter(
        policy_id="POL-08",
        title="Travel, Meals & Business Entertainment Expense Reimbursement",
        category="Finance",
        effective_date="2026-01-01",
        summary="Economy flights under 6 hours, per diem meal caps ($75/day), itemized receipt submission within 30 days via expense portal.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Economy flights under 6 hours, per diem meal caps ($75/day), itemized receipt submission within 30 days via expense portal.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-09": EnterprisePolicyChapter(
        policy_id="POL-09",
        title="Intellectual Property Assignment & Inventions Agreement",
        category="Legal",
        effective_date="2026-01-01",
        summary="All proprietary software, patents, trade secrets, and architectures created within scope of employment are exclusive company property.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. All proprietary software, patents, trade secrets, and architectures created within scope of employment are exclusive company property.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-10": EnterprisePolicyChapter(
        policy_id="POL-10",
        title="Whistleblower Protection & Anonymous Ethics Reporting",
        category="Legal",
        effective_date="2026-01-01",
        summary="Guaranteed non-retaliation protections for good-faith reporting of accounting irregularities, safety violations, or compliance breaches.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Guaranteed non-retaliation protections for good-faith reporting of accounting irregularities, safety violations, or compliance breaches.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-11": EnterprisePolicyChapter(
        policy_id="POL-11",
        title="Employee Performance Management & 360 Calibration",
        category="Performance",
        effective_date="2026-01-01",
        summary="Semi-annual OKR reviews, 9-box talent matrix calibration, 360 peer feedback collection, and Performance Improvement Plan (PIP) mechanics.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Semi-annual OKR reviews, 9-box talent matrix calibration, 360 peer feedback collection, and Performance Improvement Plan (PIP) mechanics.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-12": EnterprisePolicyChapter(
        policy_id="POL-12",
        title="Promotions, Job Architecture & Career Ladders",
        category="Total Rewards",
        effective_date="2026-01-01",
        summary="Dual IC and Management progression tracks (L1 to L6, M1 to VP), minimum 12-month grade residency, and merit increase matrices.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Dual IC and Management progression tracks (L1 to L6, M1 to VP), minimum 12-month grade residency, and merit increase matrices.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-13": EnterprisePolicyChapter(
        policy_id="POL-13",
        title="Corporate Device & IT Asset Custody Policy",
        category="IT Operations",
        effective_date="2026-01-01",
        summary="Guidelines on provisioned laptop security, personal use boundaries, international travel with company hardware, and return upon separation.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Guidelines on provisioned laptop security, personal use boundaries, international travel with company hardware, and return upon separation.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-14": EnterprisePolicyChapter(
        policy_id="POL-14",
        title="Data Privacy & GDPR Data Subject Rights (DSAR)",
        category="Privacy",
        effective_date="2026-01-01",
        summary="Handling personal data, data retention periods (7 yrs payroll, 1 yr applications), right to erasure, and automated PII scrubbing.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Handling personal data, data retention periods (7 yrs payroll, 1 yr applications), right to erasure, and automated PII scrubbing.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-15": EnterprisePolicyChapter(
        policy_id="POL-15",
        title="Workplace Safety, Ergonomics & Emergency Preparedness",
        category="Operations",
        effective_date="2026-01-01",
        summary="OSHA compliance, ergonomic assessments, office evacuation routes, disaster recovery communication, and severe weather protocols.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. OSHA compliance, ergonomic assessments, office evacuation routes, disaster recovery communication, and severe weather protocols.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-16": EnterprisePolicyChapter(
        policy_id="POL-16",
        title="Employee Health & Wellness Benefits Plan",
        category="Benefits",
        effective_date="2026-01-01",
        summary="Medical, Dental, Vision PPO/HDHP plans, HSA employer matching ($500 individual / $1,000 family), and Employee Assistance Program (EAP).",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Medical, Dental, Vision PPO/HDHP plans, HSA employer matching ($500 individual / $1,000 family), and Employee Assistance Program (EAP).\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-17": EnterprisePolicyChapter(
        policy_id="POL-17",
        title="Retirement 401(k) Plan & Employer Match Guidelines",
        category="Benefits",
        effective_date="2026-01-01",
        summary="Safe Harbor 401(k) with 100% employer match up to 4% of base compensation, immediate 100% vesting, and pre-tax vs Roth elections.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Safe Harbor 401(k) with 100% employer match up to 4% of base compensation, immediate 100% vesting, and pre-tax vs Roth elections.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-18": EnterprisePolicyChapter(
        policy_id="POL-18",
        title="Learning & Professional Development Annual Stipend",
        category="L&D",
        effective_date="2026-01-01",
        summary="$1,500 annual personal learning budget for technical certifications, conferences, books, and accredited university coursework.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. $1,500 annual personal learning budget for technical certifications, conferences, books, and accredited university coursework.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-19": EnterprisePolicyChapter(
        policy_id="POL-19",
        title="Social Media & Public Communications Policy",
        category="Marketing",
        effective_date="2026-01-01",
        summary="Only designated company spokespersons may comment on official business; personal social media disclaimers required for industry posts.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Only designated company spokespersons may comment on official business; personal social media disclaimers required for industry posts.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
    "POL-20": EnterprisePolicyChapter(
        policy_id="POL-20",
        title="Voluntary & Involuntary Separation Guidelines",
        category="HR Operations",
        effective_date="2026-01-01",
        summary="Standard 2-week notice etiquette for resignation, final paycheck timelines, COBRA continuation notices, and severance package formulas.",
        full_text="1. PURPOSE & PRINCIPLES\nPeoplePulse Global Enterprise Inc. is committed to transparent, equitable, and legally compliant workforce operations. Standard 2-week notice etiquette for resignation, final paycheck timelines, COBRA continuation notices, and severance package formulas.\n\n2. APPLICABILITY & SCOPE\nThis policy applies to all active regular full-time, part-time, and international subsidiary employees globally.\n\n3. DETAILED PROCEDURES & REQUIREMENTS\nAll employees and managers must strictly adhere to the operational guidelines set forth herein. Violations may result in disciplinary action up to and including separation of employment.\n\n4. COMPLIANCE & GOVERNANCE\nThis policy is reviewed annually by the People Operations and Legal Compliance committees."
    ),
}

class PolicyHandbookService:
    @classmethod
    def get_policy(cls, policy_id: str) -> EnterprisePolicyChapter:
        return FULL_POLICY_HANDBOOK_CORPUS.get(policy_id)

    @classmethod
    def get_all_policies(cls) -> List[EnterprisePolicyChapter]:
        return list(FULL_POLICY_HANDBOOK_CORPUS.values())
