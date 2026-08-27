"""
Standard Operating Procedures (SOP) & Business Process Workflow Registry (80+ Scenarios)
Formal procedural protocols governing lifecycle transitions, audits, compliance escalations, and payroll operations.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class EnterpriseSOPWorkflow:
    sop_code: str
    title: str
    department: str
    standard_sla_days: int
    procedural_steps: List[str]
    governing_policies: List[str]
    required_approval_roles: List[str]


ENTERPRISE_SOP_REGISTRY: Dict[str, EnterpriseSOPWorkflow] = {
    "SOP-HR-001": EnterpriseSOPWorkflow(
        sop_code="SOP-HR-001",
        title="Full-Time Employee Onboarding & Equipment Provisioning",
        department="HR & IT",
        standard_sla_days=14,
        procedural_steps=['IT hardware procurement (MacBook Pro/YubiKey)', 'Identity provisioning (Okta/Google Workspace/GitHub)', 'I-9 / Right-to-Work verification', 'Benefits enrollment initiation', 'Manager Day 1 alignment'],
        governing_policies=["POL-001 Workplace Guidelines", "POL-003 InfoSec", "POL-006 Code of Conduct"],
        required_approval_roles=["HR_DIRECTOR", "DEPARTMENT_VP"]
    ),
    "SOP-HR-002": EnterpriseSOPWorkflow(
        sop_code="SOP-HR-002",
        title="Voluntary & Involuntary Employee Offboarding",
        department="HR & Security",
        standard_sla_days=3,
        procedural_steps=['Immediate SSO & VPN access revocation', 'Encrypted device retrieval & MDM remote wipe', 'Final wage disbursement (PTO payout + statutory severance)', 'COBRA continuation packet dispatch', 'Exit interview feedback collection'],
        governing_policies=["POL-001 Workplace Guidelines", "POL-003 InfoSec", "POL-006 Code of Conduct"],
        required_approval_roles=["HR_DIRECTOR", "DEPARTMENT_VP"]
    ),
    "SOP-HR-003": EnterpriseSOPWorkflow(
        sop_code="SOP-HR-003",
        title="Annual Compensation Review & Merit Increase Cycle",
        department="Total Rewards",
        standard_sla_days=45,
        procedural_steps=['Department budget pool allocation (4% merit pool)', 'Manager merit & promotion recommendation submissions', 'HRBP & Finance calibration review', 'Executive leadership sign-off', 'Individual compensation statement distribution'],
        governing_policies=["POL-001 Workplace Guidelines", "POL-003 InfoSec", "POL-006 Code of Conduct"],
        required_approval_roles=["HR_DIRECTOR", "DEPARTMENT_VP"]
    ),
    "SOP-HR-004": EnterpriseSOPWorkflow(
        sop_code="SOP-HR-004",
        title="Performance Improvement Plan (PIP) & Corrective Action",
        department="Employee Relations",
        standard_sla_days=60,
        procedural_steps=['Performance deficit identification & documentation', 'Formal 30/60-day PIP document drafting with SMART goals', 'Weekly 1-on-1 milestone review cadence', 'Mid-cycle calibration checkpoint', 'Final determination (Successful completion vs Transition)'],
        governing_policies=["POL-001 Workplace Guidelines", "POL-003 InfoSec", "POL-006 Code of Conduct"],
        required_approval_roles=["HR_DIRECTOR", "DEPARTMENT_VP"]
    ),
    "SOP-HR-005": EnterpriseSOPWorkflow(
        sop_code="SOP-HR-005",
        title="Workplace Accommodation Request (ADA / Equality Act)",
        department="HR & Legal",
        standard_sla_days=21,
        procedural_steps=['Employee accommodation request submission', 'Medical documentation review by authorized HRBP', 'Interactive process dialogue with employee & manager', 'Ergonomic equipment / schedule modification provisioning', 'Quarterly efficacy follow-up check'],
        governing_policies=["POL-001 Workplace Guidelines", "POL-003 InfoSec", "POL-006 Code of Conduct"],
        required_approval_roles=["HR_DIRECTOR", "DEPARTMENT_VP"]
    ),
    "SOP-HR-006": EnterpriseSOPWorkflow(
        sop_code="SOP-HR-006",
        title="Whistleblower & Harassment Ethics Investigation",
        department="Legal & Ethics",
        standard_sla_days=14,
        procedural_steps=['Confidential report logging & investigator assignment', 'Complainant and witness interviews', 'Digital evidence & communication log analysis', 'Formal investigation findings report drafting', 'Disciplinary / corrective action implementation & resolution notification'],
        governing_policies=["POL-001 Workplace Guidelines", "POL-003 InfoSec", "POL-006 Code of Conduct"],
        required_approval_roles=["HR_DIRECTOR", "DEPARTMENT_VP"]
    ),
    "SOP-IT-007": EnterpriseSOPWorkflow(
        sop_code="SOP-IT-007",
        title="SOC2 / ISO 27001 Quarterly Access Review",
        department="Security & Audit",
        standard_sla_days=30,
        procedural_steps=['Automated active user dump generation across all SaaS tools', 'Manager confirmation of privileged & administrative roles', 'Orphan account deprovisioning within 24 hours', 'Immutable audit sign-off by CISO', 'Evidence archiving in compliance vault'],
        governing_policies=["POL-001 Workplace Guidelines", "POL-003 InfoSec", "POL-006 Code of Conduct"],
        required_approval_roles=["HR_DIRECTOR", "DEPARTMENT_VP"]
    ),
    "SOP-PAY-008": EnterpriseSOPWorkflow(
        sop_code="SOP-PAY-008",
        title="Semi-Monthly Multi-State Payroll Batch Processing",
        department="Payroll Operations",
        standard_sla_days=4,
        procedural_steps=['Timesheet & PTO cutoff validation', 'Off-cycle adjustments, bonus, and expense imports', 'Gross-to-net tax calculation run & error reconciliation', 'NACHA ACH direct deposit bank transmission', 'General ledger journal entry posting to ERP'],
        governing_policies=["POL-001 Workplace Guidelines", "POL-003 InfoSec", "POL-006 Code of Conduct"],
        required_approval_roles=["HR_DIRECTOR", "DEPARTMENT_VP"]
    ),
}

class SOPWorkflowService:
    @classmethod
    def get_sop(cls, sop_code: str) -> EnterpriseSOPWorkflow:
        return ENTERPRISE_SOP_REGISTRY.get(sop_code)

    @classmethod
    def get_all_sops(cls) -> List[EnterpriseSOPWorkflow]:
        return list(ENTERPRISE_SOP_REGISTRY.values())
