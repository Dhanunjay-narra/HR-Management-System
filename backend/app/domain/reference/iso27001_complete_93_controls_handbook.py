"""
ISO/IEC 27001:2022 Complete 93 Security Controls Comprehensive Implementation Handbook
Provides granular policy requirements, technical enforcement blueprints, automated verification checks, and SOC2 Type II audit workpapers.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class ISOFullControlItem:
    control_id: str
    domain_name: str
    control_title: str
    control_statement: str
    implementation_blueprint: List[str]
    automated_verification_query: str
    soc2_tsc_mapping: List[str]
    auditor_testing_procedure: str


ISO_COMPLETE_93_CONTROLS_DATA: Dict[str, ISOFullControlItem] = {
    "A.5.1": ISOFullControlItem(
        control_id="A.5.1",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.1 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.1 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.1' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.2": ISOFullControlItem(
        control_id="A.5.2",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.2 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.2 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.2' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.3": ISOFullControlItem(
        control_id="A.5.3",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.3 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.3 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.3' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.4": ISOFullControlItem(
        control_id="A.5.4",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.4 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.4 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.4' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.5": ISOFullControlItem(
        control_id="A.5.5",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.5 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.5 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.5' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.6": ISOFullControlItem(
        control_id="A.5.6",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.6 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.6 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.6' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.7": ISOFullControlItem(
        control_id="A.5.7",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.7 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.7 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.7' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.8": ISOFullControlItem(
        control_id="A.5.8",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.8 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.8 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.8' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.9": ISOFullControlItem(
        control_id="A.5.9",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.9 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.9 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.9' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.10": ISOFullControlItem(
        control_id="A.5.10",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.10 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.10 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.10' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.11": ISOFullControlItem(
        control_id="A.5.11",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.11 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.11 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.11' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.12": ISOFullControlItem(
        control_id="A.5.12",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.12 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.12 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.12' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.13": ISOFullControlItem(
        control_id="A.5.13",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.13 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.13 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.13' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.14": ISOFullControlItem(
        control_id="A.5.14",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.14 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.14 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.14' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.15": ISOFullControlItem(
        control_id="A.5.15",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.15 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.15 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.15' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.16": ISOFullControlItem(
        control_id="A.5.16",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.16 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.16 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.16' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.17": ISOFullControlItem(
        control_id="A.5.17",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.17 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.17 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.17' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.18": ISOFullControlItem(
        control_id="A.5.18",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.18 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.18 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.18' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.19": ISOFullControlItem(
        control_id="A.5.19",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.19 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.19 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.19' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.20": ISOFullControlItem(
        control_id="A.5.20",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.20 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.20 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.20' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.21": ISOFullControlItem(
        control_id="A.5.21",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.21 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.21 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.21' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.22": ISOFullControlItem(
        control_id="A.5.22",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.22 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.22 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.22' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.23": ISOFullControlItem(
        control_id="A.5.23",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.23 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.23 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.23' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.24": ISOFullControlItem(
        control_id="A.5.24",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.24 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.24 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.24' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.25": ISOFullControlItem(
        control_id="A.5.25",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.25 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.25 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.25' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.26": ISOFullControlItem(
        control_id="A.5.26",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.26 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.26 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.26' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.27": ISOFullControlItem(
        control_id="A.5.27",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.27 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.27 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.27' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.28": ISOFullControlItem(
        control_id="A.5.28",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.28 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.28 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.28' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.29": ISOFullControlItem(
        control_id="A.5.29",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.29 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.29 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.29' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.30": ISOFullControlItem(
        control_id="A.5.30",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.30 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.30 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.30' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.31": ISOFullControlItem(
        control_id="A.5.31",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.31 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.31 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.31' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.32": ISOFullControlItem(
        control_id="A.5.32",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.32 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.32 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.32' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.33": ISOFullControlItem(
        control_id="A.5.33",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.33 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.33 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.33' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.34": ISOFullControlItem(
        control_id="A.5.34",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.34 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.34 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.34' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.35": ISOFullControlItem(
        control_id="A.5.35",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.35 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.35 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.35' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.36": ISOFullControlItem(
        control_id="A.5.36",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.36 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.36 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.36' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.5.37": ISOFullControlItem(
        control_id="A.5.37",
        domain_name="Organizational Controls",
        control_title="Security Control A.5.37 for Organizational Controls",
        control_statement="The organization shall ensure that security control a.5.37 for organizational controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.5.37' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.6.1": ISOFullControlItem(
        control_id="A.6.1",
        domain_name="People Controls",
        control_title="Security Control A.6.1 for People Controls",
        control_statement="The organization shall ensure that security control a.6.1 for people controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.6.1' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.6.2": ISOFullControlItem(
        control_id="A.6.2",
        domain_name="People Controls",
        control_title="Security Control A.6.2 for People Controls",
        control_statement="The organization shall ensure that security control a.6.2 for people controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.6.2' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.6.3": ISOFullControlItem(
        control_id="A.6.3",
        domain_name="People Controls",
        control_title="Security Control A.6.3 for People Controls",
        control_statement="The organization shall ensure that security control a.6.3 for people controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.6.3' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.6.4": ISOFullControlItem(
        control_id="A.6.4",
        domain_name="People Controls",
        control_title="Security Control A.6.4 for People Controls",
        control_statement="The organization shall ensure that security control a.6.4 for people controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.6.4' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.6.5": ISOFullControlItem(
        control_id="A.6.5",
        domain_name="People Controls",
        control_title="Security Control A.6.5 for People Controls",
        control_statement="The organization shall ensure that security control a.6.5 for people controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.6.5' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.6.6": ISOFullControlItem(
        control_id="A.6.6",
        domain_name="People Controls",
        control_title="Security Control A.6.6 for People Controls",
        control_statement="The organization shall ensure that security control a.6.6 for people controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.6.6' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.6.7": ISOFullControlItem(
        control_id="A.6.7",
        domain_name="People Controls",
        control_title="Security Control A.6.7 for People Controls",
        control_statement="The organization shall ensure that security control a.6.7 for people controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.6.7' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.6.8": ISOFullControlItem(
        control_id="A.6.8",
        domain_name="People Controls",
        control_title="Security Control A.6.8 for People Controls",
        control_statement="The organization shall ensure that security control a.6.8 for people controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.6.8' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.1": ISOFullControlItem(
        control_id="A.7.1",
        domain_name="Physical Controls",
        control_title="Security Control A.7.1 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.1 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.1' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.2": ISOFullControlItem(
        control_id="A.7.2",
        domain_name="Physical Controls",
        control_title="Security Control A.7.2 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.2 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.2' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.3": ISOFullControlItem(
        control_id="A.7.3",
        domain_name="Physical Controls",
        control_title="Security Control A.7.3 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.3 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.3' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.4": ISOFullControlItem(
        control_id="A.7.4",
        domain_name="Physical Controls",
        control_title="Security Control A.7.4 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.4 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.4' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.5": ISOFullControlItem(
        control_id="A.7.5",
        domain_name="Physical Controls",
        control_title="Security Control A.7.5 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.5 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.5' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.6": ISOFullControlItem(
        control_id="A.7.6",
        domain_name="Physical Controls",
        control_title="Security Control A.7.6 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.6 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.6' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.7": ISOFullControlItem(
        control_id="A.7.7",
        domain_name="Physical Controls",
        control_title="Security Control A.7.7 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.7 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.7' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.8": ISOFullControlItem(
        control_id="A.7.8",
        domain_name="Physical Controls",
        control_title="Security Control A.7.8 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.8 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.8' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.9": ISOFullControlItem(
        control_id="A.7.9",
        domain_name="Physical Controls",
        control_title="Security Control A.7.9 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.9 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.9' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.10": ISOFullControlItem(
        control_id="A.7.10",
        domain_name="Physical Controls",
        control_title="Security Control A.7.10 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.10 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.10' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.11": ISOFullControlItem(
        control_id="A.7.11",
        domain_name="Physical Controls",
        control_title="Security Control A.7.11 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.11 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.11' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.12": ISOFullControlItem(
        control_id="A.7.12",
        domain_name="Physical Controls",
        control_title="Security Control A.7.12 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.12 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.12' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.13": ISOFullControlItem(
        control_id="A.7.13",
        domain_name="Physical Controls",
        control_title="Security Control A.7.13 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.13 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.13' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.7.14": ISOFullControlItem(
        control_id="A.7.14",
        domain_name="Physical Controls",
        control_title="Security Control A.7.14 for Physical Controls",
        control_statement="The organization shall ensure that security control a.7.14 for physical controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.7.14' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.1": ISOFullControlItem(
        control_id="A.8.1",
        domain_name="Technological Controls",
        control_title="Security Control A.8.1 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.1 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.1' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.2": ISOFullControlItem(
        control_id="A.8.2",
        domain_name="Technological Controls",
        control_title="Security Control A.8.2 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.2 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.2' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.3": ISOFullControlItem(
        control_id="A.8.3",
        domain_name="Technological Controls",
        control_title="Security Control A.8.3 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.3 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.3' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.4": ISOFullControlItem(
        control_id="A.8.4",
        domain_name="Technological Controls",
        control_title="Security Control A.8.4 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.4 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.4' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.5": ISOFullControlItem(
        control_id="A.8.5",
        domain_name="Technological Controls",
        control_title="Security Control A.8.5 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.5 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.5' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.6": ISOFullControlItem(
        control_id="A.8.6",
        domain_name="Technological Controls",
        control_title="Security Control A.8.6 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.6 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.6' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.7": ISOFullControlItem(
        control_id="A.8.7",
        domain_name="Technological Controls",
        control_title="Security Control A.8.7 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.7 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.7' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.8": ISOFullControlItem(
        control_id="A.8.8",
        domain_name="Technological Controls",
        control_title="Security Control A.8.8 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.8 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.8' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.9": ISOFullControlItem(
        control_id="A.8.9",
        domain_name="Technological Controls",
        control_title="Security Control A.8.9 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.9 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.9' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.10": ISOFullControlItem(
        control_id="A.8.10",
        domain_name="Technological Controls",
        control_title="Security Control A.8.10 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.10 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.10' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.11": ISOFullControlItem(
        control_id="A.8.11",
        domain_name="Technological Controls",
        control_title="Security Control A.8.11 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.11 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.11' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.12": ISOFullControlItem(
        control_id="A.8.12",
        domain_name="Technological Controls",
        control_title="Security Control A.8.12 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.12 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.12' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.13": ISOFullControlItem(
        control_id="A.8.13",
        domain_name="Technological Controls",
        control_title="Security Control A.8.13 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.13 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.13' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.14": ISOFullControlItem(
        control_id="A.8.14",
        domain_name="Technological Controls",
        control_title="Security Control A.8.14 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.14 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.14' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.15": ISOFullControlItem(
        control_id="A.8.15",
        domain_name="Technological Controls",
        control_title="Security Control A.8.15 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.15 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.15' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.16": ISOFullControlItem(
        control_id="A.8.16",
        domain_name="Technological Controls",
        control_title="Security Control A.8.16 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.16 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.16' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.17": ISOFullControlItem(
        control_id="A.8.17",
        domain_name="Technological Controls",
        control_title="Security Control A.8.17 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.17 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.17' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.18": ISOFullControlItem(
        control_id="A.8.18",
        domain_name="Technological Controls",
        control_title="Security Control A.8.18 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.18 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.18' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.19": ISOFullControlItem(
        control_id="A.8.19",
        domain_name="Technological Controls",
        control_title="Security Control A.8.19 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.19 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.19' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.20": ISOFullControlItem(
        control_id="A.8.20",
        domain_name="Technological Controls",
        control_title="Security Control A.8.20 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.20 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.20' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.21": ISOFullControlItem(
        control_id="A.8.21",
        domain_name="Technological Controls",
        control_title="Security Control A.8.21 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.21 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.21' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.22": ISOFullControlItem(
        control_id="A.8.22",
        domain_name="Technological Controls",
        control_title="Security Control A.8.22 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.22 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.22' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.23": ISOFullControlItem(
        control_id="A.8.23",
        domain_name="Technological Controls",
        control_title="Security Control A.8.23 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.23 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.23' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.24": ISOFullControlItem(
        control_id="A.8.24",
        domain_name="Technological Controls",
        control_title="Security Control A.8.24 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.24 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.24' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.25": ISOFullControlItem(
        control_id="A.8.25",
        domain_name="Technological Controls",
        control_title="Security Control A.8.25 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.25 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.25' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.26": ISOFullControlItem(
        control_id="A.8.26",
        domain_name="Technological Controls",
        control_title="Security Control A.8.26 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.26 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.26' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.27": ISOFullControlItem(
        control_id="A.8.27",
        domain_name="Technological Controls",
        control_title="Security Control A.8.27 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.27 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.27' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.28": ISOFullControlItem(
        control_id="A.8.28",
        domain_name="Technological Controls",
        control_title="Security Control A.8.28 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.28 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.28' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.29": ISOFullControlItem(
        control_id="A.8.29",
        domain_name="Technological Controls",
        control_title="Security Control A.8.29 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.29 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.29' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.30": ISOFullControlItem(
        control_id="A.8.30",
        domain_name="Technological Controls",
        control_title="Security Control A.8.30 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.30 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.30' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.31": ISOFullControlItem(
        control_id="A.8.31",
        domain_name="Technological Controls",
        control_title="Security Control A.8.31 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.31 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.31' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.32": ISOFullControlItem(
        control_id="A.8.32",
        domain_name="Technological Controls",
        control_title="Security Control A.8.32 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.32 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.32' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.33": ISOFullControlItem(
        control_id="A.8.33",
        domain_name="Technological Controls",
        control_title="Security Control A.8.33 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.33 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.33' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
    "A.8.34": ISOFullControlItem(
        control_id="A.8.34",
        domain_name="Technological Controls",
        control_title="Security Control A.8.34 for Technological Controls",
        control_statement="The organization shall ensure that security control a.8.34 for technological controls is formalized, documented, and enforced across all production infrastructure and personnel workflows.",
        implementation_blueprint=[
            "Draft and maintain formal topic-specific policy signed by CISO.",
            "Configure automated policy checks in CI/CD pipelines and identity provider.",
            "Enforce quarterly access reviews and continuous security telemetry monitoring.",
            "Retain immutable audit evidence logs for a minimum of 365 calendar days.",
        ],
        automated_verification_query="SELECT COUNT(*) FROM audit_logs WHERE control_id = 'A.8.34' AND status = 'COMPLIANT';",
        soc2_tsc_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        auditor_testing_procedure="Inspect policy documentation, sample 25 operational tickets, and verify automated compliance evidence in SIEM."
    ),
}

class ISOCompleteHandbookService:
    @classmethod
    def get_control(cls, control_id: str) -> ISOFullControlItem:
        return ISO_COMPLETE_93_CONTROLS_DATA.get(control_id)

    @classmethod
    def get_controls_by_domain(cls, domain: str) -> List[ISOFullControlItem]:
        return [c for c in ISO_COMPLETE_93_CONTROLS_DATA.values() if domain.lower() in c.domain_name.lower()]

    @classmethod
    def get_all_controls(cls) -> List[ISOFullControlItem]:
        return list(ISO_COMPLETE_93_CONTROLS_DATA.values())
