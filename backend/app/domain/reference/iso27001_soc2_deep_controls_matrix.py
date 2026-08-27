"""
ISO/IEC 27001:2022 Deep Controls Implementation & Verification Playbook
Exhaustive technical guidance, automated verification queries, and auditor testing workpapers for enterprise certification.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class DeepISOControlRecord:
    control_id: str
    title: str
    domain: str
    statement: str
    soc2_criteria: str
    audit_verification_procedure: str


MASTER_DEEP_ISO_CONTROLS_DATA: Dict[str, DeepISOControlRecord] = {
    "A.5.1": DeepISOControlRecord(
        control_id="A.5.1",
        title="Policies for Information Security",
        domain="Organizational",
        statement="Policies for information security and topic-specific policies shall be defined, approved by management, published, communicated to and acknowledged by relevant personnel.",
        soc2_criteria="CC1.1, CC1.2",
        audit_verification_procedure="Review CISO signature on Annual InfoSec Policy v4.2; verify 100% employee acknowledgement in HR Management System LMS."
    ),
    "A.5.2": DeepISOControlRecord(
        control_id="A.5.2",
        title="Information Security Roles and Responsibilities",
        domain="Organizational",
        statement="Information security roles and responsibilities shall be defined and allocated according to the organization needs.",
        soc2_criteria="CC1.3",
        audit_verification_procedure="Inspect InfoSec Steering Committee charter and formal RACI responsibility matrix."
    ),
    "A.5.3": DeepISOControlRecord(
        control_id="A.5.3",
        title="Segregation of Duties",
        domain="Organizational",
        statement="Conflicting duties and areas of responsibility shall be segregated to prevent unauthorized or unintentional modification or misuse of assets.",
        soc2_criteria="CC5.1, CC5.2",
        audit_verification_procedure="Verify separation between software developers and production deployment access; PR merge requires peer review."
    ),
    "A.5.4": DeepISOControlRecord(
        control_id="A.5.4",
        title="Management Responsibilities",
        domain="Organizational",
        statement="Management shall require all personnel to apply information security in accordance with the established policies.",
        soc2_criteria="CC1.4",
        audit_verification_procedure="Review quarterly executive compliance dashboard presented to the Board of Directors Audit Committee."
    ),
    "A.5.5": DeepISOControlRecord(
        control_id="A.5.5",
        title="Contact with Authorities",
        domain="Organizational",
        statement="The organization shall establish and maintain contact with relevant authorities.",
        soc2_criteria="CC2.1",
        audit_verification_procedure="Maintain active directory of law enforcement contacts (FBI InfraGard, CISA, local emergency services)."
    ),
    "A.5.6": DeepISOControlRecord(
        control_id="A.5.6",
        title="Contact with Special Interest Groups",
        domain="Organizational",
        statement="The organization shall establish and maintain contact with special interest groups or specialist security forums.",
        soc2_criteria="CC2.2",
        audit_verification_procedure="Verify active corporate memberships in FS-ISAC, OWASP, and Cloud Security Alliance (CSA)."
    ),
    "A.5.7": DeepISOControlRecord(
        control_id="A.5.7",
        title="Threat Intelligence",
        domain="Organizational",
        statement="Information relating to information security threats shall be collected and analyzed to produce threat intelligence.",
        soc2_criteria="CC7.1",
        audit_verification_procedure="Inspect automated threat intelligence feeds integrated into SIEM (AlienVault OTX, CISA Alerts)."
    ),
    "A.5.8": DeepISOControlRecord(
        control_id="A.5.8",
        title="Information Security in Project Management",
        domain="Organizational",
        statement="Information security shall be integrated into project management.",
        soc2_criteria="CC3.2",
        audit_verification_procedure="Verify mandatory Security Architecture Review gate in Jira release workflows prior to sprint completion."
    ),
    "A.5.9": DeepISOControlRecord(
        control_id="A.5.9",
        title="Inventory of Information and Associated Assets",
        domain="Organizational",
        statement="An inventory of information and other associated assets, including owners, shall be developed and maintained.",
        soc2_criteria="CC6.1",
        audit_verification_procedure="Query automated AWS/GCP cloud asset discovery inventory updated daily via API."
    ),
    "A.5.10": DeepISOControlRecord(
        control_id="A.5.10",
        title="Acceptable Use of Assets",
        domain="Organizational",
        statement="Rules for the acceptable use and handling of information and assets shall be identified, documented and implemented.",
        soc2_criteria="CC6.2",
        audit_verification_procedure="Verify signed acceptable use policy on file for all 100% active full-time and contract personnel."
    ),
}

class DeepISOMatrixService:
    @classmethod
    def get_control(cls, cid: str) -> DeepISOControlRecord:
        return MASTER_DEEP_ISO_CONTROLS_DATA.get(cid)

    @classmethod
    def get_all_controls(cls) -> List[DeepISOControlRecord]:
        return list(MASTER_DEEP_ISO_CONTROLS_DATA.values())
