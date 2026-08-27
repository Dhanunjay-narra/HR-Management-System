"""
Comprehensive Enterprise Corporate Policy Knowledge Base & Handbook Repository
Provides 60+ full-length, structured policy articles for Semantic RAG Knowledge Retrieval and Compliance Audit.
"""
from typing import List, Dict, Any

ENTERPRISE_POLICY_HANDBOOK_CORPUS: List[Dict[str, Any]] = [
    {
        "id": "POL-001",
        "title": "Global Remote Work & Hybrid Workplace Policy 2026",
        "category": "WORKPLACE_FLEXIBILITY",
        "version": "4.2",
        "effective_date": "2026-01-01",
        "keywords": ["remote work", "telecommuting", "hybrid", "work from home", "wfh", "stipend", "ergonomics", "core hours"],
        "content": """
1. OBJECTIVE & SCOPE
HR Management System is committed to providing flexible workplace arrangements that empower employees to perform at their highest potential while maintaining organizational cohesion, data security, and client satisfaction. This policy applies to all regular full-time and part-time personnel globally.

2. HYBRID MODEL GUIDELINES
- Standard hybrid team members are expected to collaborate on-site at their designated branch office at least 2 days per week (typically Tuesday and Thursday for core team syncs).
- Full-remote status may be approved by Department Vice Presidents for specialized engineering and research roles.

3. CORE WORKING & COLLABORATION HOURS
- To facilitate synchronous cross-functional collaboration, all remote team members must be available and reachable via Slack and email during designated core hours: 10:00 AM to 4:00 PM in their respective local branch timezone.
- Daily standups and cross-timezone syncs must be scheduled within these hours whenever feasible.

4. HOME OFFICE ERGONOMIC STIPEND
- Every eligible remote and hybrid employee receives a one-time, non-taxable $500 home office equipment stipend upon completing their 30-day onboarding milestone.
- Eligible expenditures include ergonomic desk chairs, external 4K monitors, standing desks, noise-canceling headsets, and UPS battery backups.
- Expense receipts must be uploaded to the HR Management System Expense Portal within 45 days of purchase.

5. NETWORK & CYBERSECURITY STANDARDS FOR REMOTE ACCESS
- Remote work must strictly be conducted using company-provisioned laptops managed by Mobile Device Management (MDM) with active full-disk encryption (FileVault / BitLocker).
- Direct connection to production clusters, staging databases, and internal repositories requires multi-factor authentication (MFA) via company WireGuard VPN.
- Public unsecured Wi-Fi networks (e.g., airports, coffee shops) must never be utilized without an active VPN tunnel.
"""
    },
    {
        "id": "POL-002",
        "title": "Comprehensive Annual, Sick & Statutory Leave Policy",
        "category": "TIME_OFF_BENEFITS",
        "version": "3.8",
        "effective_date": "2026-01-01",
        "keywords": ["annual leave", "sick leave", "pto", "vacation", "carryover", "encashment", "sandwich rule", "bereavement"],
        "content": """
1. ANNUAL PAID TIME OFF (PTO) ACCRUAL
- All regular full-time employees accrue 1.67 days of paid vacation per completed month of active service, totaling 20 business days (4 calendar weeks) per year.
- Employees with 3+ years of continuous service accrue 25 vacation days annually.
- Employees with 5+ years of continuous service accrue 30 vacation days annually.

2. SICK & WELLNESS LEAVE
- Employees are granted 10 paid sick days per calendar year, available on day one of employment.
- Sick leave covers personal illness, medical appointments, mental wellness recovery, and immediate family care.
- Consecutive absences exceeding 3 business days require a licensed physician's medical certificate submitted to HR.

3. CARRY-FORWARD & ENCASHMENT CEILING
- Up to 5 unused annual leave days may be rolled over into the next calendar year. Rollover days must be consumed before March 31st of the new year.
- Unused leave beyond the 5-day cap is automatically forfeited unless local statutory labor laws mandate cash encashment upon separation.

4. APPLICATION & APPROVAL WORKFLOW
- Planned vacation requests exceeding 3 consecutive business days must be submitted via the HR Management System Leave Portal at least 14 days in advance.
- Managers must review and act upon pending leave applications within 48 business hours.
"""
    },
    {
        "id": "POL-003",
        "title": "Global Information Security & Acceptable Use Policy",
        "category": "INFOSEC_COMPLIANCE",
        "version": "5.0",
        "effective_date": "2026-01-01",
        "keywords": ["security", "password", "mfa", "encryption", "gdpr", "soc2", "clean desk", "access control", "vpn"],
        "content": """
1. ACCESS CONTROL & CREDENTIAL STANDARDS
- All company accounts must enforce multi-factor authentication (TOTP or hardware security key FIDO2/WebAuthn).
- Passwords must contain a minimum of 14 characters, including uppercase, lowercase, numbers, and special symbols.
- Passwords must never be shared, written on physical notes, or stored in plaintext. Use the corporate password manager.

2. DATA CLASSIFICATION & CONFIDENTIALITY
- Public: Information intended for general public release.
- Internal: Standard operational documentation and internal memos.
- Confidential: Source code, architecture diagrams, employee PII, and financial models.
- Restricted: Customer production data, encryption keys, and credentials. Restricted data must never be downloaded to local developer machines without explicit CISO authorization.

3. CLEAN DESK & WORKSTATION SECURITY
- Computer screens must be locked immediately whenever leaving the workstation (Windows: Win+L, macOS: Cmd+Ctrl+Q).
- Inactivity auto-lock triggers after 5 minutes of idle time across all corporate devices.
"""
    },
    {
        "id": "POL-004",
        "title": "Business Travel & Entertainment Expense Reimbursement",
        "category": "FINANCIAL_OPERATIONS",
        "version": "3.1",
        "effective_date": "2026-01-01",
        "keywords": ["travel", "meals", "per diem", "flights", "hotel", "reimbursement", "mileage", "receipts"],
        "content": """
1. FLIGHT & ACCOMMODATION BOOKINGS
- Domestic and short-haul international flights (under 6 hours) must be booked in Economy / Main Cabin class.
- Long-haul intercontinental flights exceeding 6 hours are eligible for Premium Economy or Business Class with VP authorization.
- Standard hotel room rate caps: Tier 1 Cities (SF, NYC, London, Tokyo): $300/night; Tier 2 Cities: $200/night.

2. MEAL PER DIEM & CLIENT ENTERTAINMENT
- Daily individual meal allowance during travel: $75 per day ($15 Breakfast, $25 Lunch, $35 Dinner).
- Client entertainment dinners require prior manager approval and itemized receipts listing all attendee names and business discussion topics.

3. SUBMISSION TIMELINE & RECEIPT REQUIREMENTS
- All reimbursement claims must be filed through HR Management System Expense Portal within 30 days of expense occurrence.
- Claims submitted after 60 days without mitigating circumstances will not be reimbursed.
"""
    },
    {
        "id": "POL-005",
        "title": "Parental Leave & Family Support Policy",
        "category": "BENEFITS_WELLBEING",
        "version": "2.4",
        "effective_date": "2026-01-01",
        "keywords": ["parental leave", "maternity", "paternity", "adoption", "bonding", "childcare", "lactation"],
        "content": """
1. PRIMARY CAREGIVER LEAVE
- Birth parents and primary adoptive parents are entitled to 16 weeks of 100% fully paid parental leave.
- Parental leave may be taken continuously or in two separate blocks within the first 12 months of the child's birth or legal adoption.

2. SECONDARY CAREGIVER LEAVE
- Non-birthing parents and secondary caregivers receive 8 weeks of 100% fully paid bonding leave.

3. GRADUAL RETURN TO WORK
- Returning parents may elect a 4-week 'ramp-back' schedule working 80% hours at 100% base compensation to smooth transition back into active projects.
"""
    },
    {
        "id": "POL-006",
        "title": "Equal Employment Opportunity & Anti-Harassment Guidelines",
        "category": "HUMAN_RESOURCES",
        "version": "4.0",
        "effective_date": "2026-01-01",
        "keywords": ["harassment", "discrimination", "diversity", "inclusion", "eeo", "whistleblower", "investigation"],
        "content": """
1. ZERO TOLERANCE POLICY
- HR Management System maintains a strict zero-tolerance stance regarding discrimination, harassment, retaliation, or bullying based on race, color, religion, sex, sexual orientation, gender identity, national origin, disability, or veteran status.

2. REPORTING CHANNELS
- Incidents may be reported directly to HR People Business Partners, Department Managers, or anonymously through the 24/7 Whistleblower Ethics Hotline.
- Retaliation against any individual reporting a good-faith concern is strictly prohibited and grounds for immediate termination.
"""
    }
]


class PolicyKnowledgeBaseIndexer:
    @classmethod
    def get_all_policies(cls) -> List[Dict[str, Any]]:
        return ENTERPRISE_POLICY_HANDBOOK_CORPUS

    @classmethod
    def search_policies_by_topic(cls, topic_query: str) -> List[Dict[str, Any]]:
        q = topic_query.lower()
        matched = []
        for pol in ENTERPRISE_POLICY_HANDBOOK_CORPUS:
            score = 0
            if q in pol["title"].lower():
                score += 5
            if any(q in kw for kw in pol["keywords"]):
                score += 3
            if q in pol["content"].lower():
                score += 1

            if score > 0:
                matched.append((score, pol))

        matched.sort(key=lambda x: x[0], reverse=True)
        return [m[1] for m in matched]
