"""
ISO/IEC 27001:2022 Annex A 93 Security Controls Catalog & SOC2 Trust Services Mapping
Comprehensive reference database for enterprise information security policies, technical controls, audit evidence items, and implementation status.
"""
from typing import Dict, List, Any
from dataclasses import dataclass, field


@dataclass
class ISOControlRequirement:
    control_id: str
    title: str
    domain: str
    control_statement: str
    soc2_trust_criteria_mapping: List[str]
    evidence_artifacts: List[str]
    implementation_guidance: str
    default_audit_cadence: str


ISO_27001_CONTROLS_DATABASE: Dict[str, ISOControlRequirement] = {
    "A.5.1": ISOControlRequirement(
        control_id="A.5.1",
        title="Policies for information security",
        domain="Organizational Controls",
        control_statement="Information security policies and topic-specific policies shall be defined, approved by management, published, communicated to and acknowledged by relevant personnel and relevant interested parties.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.2": ISOControlRequirement(
        control_id="A.5.2",
        title="Information security roles and responsibilities",
        domain="Organizational Controls",
        control_statement="Information security roles and responsibilities shall be defined and allocated according to the organization needs.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.3": ISOControlRequirement(
        control_id="A.5.3",
        title="Segregation of duties",
        domain="Organizational Controls",
        control_statement="Conflicting duties and conflicting areas of responsibility shall be segregated to prevent unauthorized or unintentional modification or misuse of organizational assets.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.4": ISOControlRequirement(
        control_id="A.5.4",
        title="Management responsibilities",
        domain="Organizational Controls",
        control_statement="Management shall require all personnel to apply information security in accordance with the established information security policy and topic-specific policies.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.5": ISOControlRequirement(
        control_id="A.5.5",
        title="Contact with authorities",
        domain="Organizational Controls",
        control_statement="The organization shall establish and maintain contact with relevant authorities.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.6": ISOControlRequirement(
        control_id="A.5.6",
        title="Contact with special interest groups",
        domain="Organizational Controls",
        control_statement="The organization shall establish and maintain contact with special interest groups or other specialist security forums and professional associations.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.7": ISOControlRequirement(
        control_id="A.5.7",
        title="Threat intelligence",
        domain="Organizational Controls",
        control_statement="Information relating to information security threats shall be collected and analyzed to produce threat intelligence.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.8": ISOControlRequirement(
        control_id="A.5.8",
        title="Information security in project management",
        domain="Organizational Controls",
        control_statement="Information security shall be integrated into project management.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.9": ISOControlRequirement(
        control_id="A.5.9",
        title="Inventory of information and other associated assets",
        domain="Organizational Controls",
        control_statement="An inventory of information and other associated assets, including owners, shall be developed and maintained.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.10": ISOControlRequirement(
        control_id="A.5.10",
        title="Acceptable use of information and other associated assets",
        domain="Organizational Controls",
        control_statement="Rules for the acceptable use and procedures for handling information and other associated assets shall be identified, documented and implemented.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.11": ISOControlRequirement(
        control_id="A.5.11",
        title="Return of assets",
        domain="Organizational Controls",
        control_statement="Personnel and other interested parties as appropriate shall return all the organization's assets in their possession upon change or termination of their employment, contract or agreement.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.12": ISOControlRequirement(
        control_id="A.5.12",
        title="Classification of information",
        domain="Organizational Controls",
        control_statement="Information shall be classified in accordance with the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.13": ISOControlRequirement(
        control_id="A.5.13",
        title="Labelling of information",
        domain="Organizational Controls",
        control_statement="An appropriate set of procedures for information labelling shall be developed and implemented in accordance with the information classification scheme adopted by the organization.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.14": ISOControlRequirement(
        control_id="A.5.14",
        title="Information transfer",
        domain="Organizational Controls",
        control_statement="Information transfer rules, procedures or agreements shall be in place for all types of transfer facilities within the organization and between the organization and other parties.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.15": ISOControlRequirement(
        control_id="A.5.15",
        title="Access control",
        domain="Organizational Controls",
        control_statement="Rules to control physical and logical access to information and other associated assets shall be established and implemented based on business and information security requirements.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.16": ISOControlRequirement(
        control_id="A.5.16",
        title="Identity management",
        domain="Organizational Controls",
        control_statement="The full life cycle of identities shall be managed.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.17": ISOControlRequirement(
        control_id="A.5.17",
        title="Authentication information",
        domain="Organizational Controls",
        control_statement="Allocation and management of authentication information shall be controlled by a management process, including advising personnel on appropriate handling of authentication information.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.18": ISOControlRequirement(
        control_id="A.5.18",
        title="Access rights",
        domain="Organizational Controls",
        control_statement="Access rights to information and other associated assets shall be provisioned, reviewed, modified and removed in accordance with the organization's topic-specific policy on and rules for access control.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.19": ISOControlRequirement(
        control_id="A.5.19",
        title="Information security in supplier relationships",
        domain="Organizational Controls",
        control_statement="Processes and procedures shall be defined and implemented to manage the information security risks associated with the use of supplier's products or services.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.20": ISOControlRequirement(
        control_id="A.5.20",
        title="Addressing information security within supplier agreements",
        domain="Organizational Controls",
        control_statement="Relevant information security requirements shall be established and agreed with each supplier that may access, process, store, communicate, or provide infrastructure components for, the organization's information.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.21": ISOControlRequirement(
        control_id="A.5.21",
        title="Managing information security in the ICT supply chain",
        domain="Organizational Controls",
        control_statement="Processes and procedures shall be defined and implemented to manage the information security risks associated with the ICT products and services supply chain.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.22": ISOControlRequirement(
        control_id="A.5.22",
        title="Monitoring, review and change management of supplier services",
        domain="Organizational Controls",
        control_statement="The organization shall regularly monitor, review, evaluate and manage change in supplier information security practices and service delivery.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.23": ISOControlRequirement(
        control_id="A.5.23",
        title="Information security for use of cloud services",
        domain="Organizational Controls",
        control_statement="Processes for acquisition, use, management and exit from cloud services shall be established in accordance with the organization's information security requirements.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.24": ISOControlRequirement(
        control_id="A.5.24",
        title="Information security incident management planning and preparation",
        domain="Organizational Controls",
        control_statement="The organization shall plan and prepare for managing information security incidents by defining, establishing and communicating information security incident management processes, roles and responsibilities.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.25": ISOControlRequirement(
        control_id="A.5.25",
        title="Assessment and decision on information security events",
        domain="Organizational Controls",
        control_statement="The organization shall assess information security events and decide if they are to be categorized as information security incidents.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.26": ISOControlRequirement(
        control_id="A.5.26",
        title="Response to information security incidents",
        domain="Organizational Controls",
        control_statement="Information security incidents shall be responded to in accordance with the documented procedures.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.27": ISOControlRequirement(
        control_id="A.5.27",
        title="Learning from information security incidents",
        domain="Organizational Controls",
        control_statement="Knowledge gained from information security incidents shall be used to strengthen and improve the information security controls.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.28": ISOControlRequirement(
        control_id="A.5.28",
        title="Collection of evidence",
        domain="Organizational Controls",
        control_statement="The organization shall define and implement procedures for the identification, collection, acquisition and preservation of evidence related to information security events.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.29": ISOControlRequirement(
        control_id="A.5.29",
        title="Information security during disruption",
        domain="Organizational Controls",
        control_statement="The organization shall plan how to maintain information security at an appropriate level during disruption.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.30": ISOControlRequirement(
        control_id="A.5.30",
        title="ICT readiness for business continuity",
        domain="Organizational Controls",
        control_statement="ICT readiness shall be planned, implemented, maintained and tested based on business continuity objectives and ICT continuity requirements.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.31": ISOControlRequirement(
        control_id="A.5.31",
        title="Legal, statutory, regulatory and contractual requirements",
        domain="Organizational Controls",
        control_statement="Legal, statutory, regulatory and contractual requirements relevant to information security and the organization's approach to meet these requirements shall be identified, documented and kept up to date.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.32": ISOControlRequirement(
        control_id="A.5.32",
        title="Intellectual property rights",
        domain="Organizational Controls",
        control_statement="The organization shall implement appropriate procedures to protect intellectual property rights.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.33": ISOControlRequirement(
        control_id="A.5.33",
        title="Protection of records",
        domain="Organizational Controls",
        control_statement="Records shall be protected from loss, destruction, falsification, unauthorized access and unauthorized release, in accordance with legal, statutory, regulatory and contractual requirements.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.34": ISOControlRequirement(
        control_id="A.5.34",
        title="Privacy and protection of PII",
        domain="Organizational Controls",
        control_statement="The organization shall identify and meet the requirements regarding the preservation of privacy and protection of PII as per applicable laws and regulations and contractual requirements.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.35": ISOControlRequirement(
        control_id="A.5.35",
        title="Independent review of information security",
        domain="Organizational Controls",
        control_statement="The organization's approach to managing information security and its implementation including people, processes and technologies shall be reviewed independently at planned intervals or when significant changes occur.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.36": ISOControlRequirement(
        control_id="A.5.36",
        title="Compliance with policies and standards for information security",
        domain="Organizational Controls",
        control_statement="Managers shall regularly review the compliance of information processing and procedures within their area of responsibility with the appropriate security policies, topic-specific policies and standards.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.5.37": ISOControlRequirement(
        control_id="A.5.37",
        title="Documented operating procedures",
        domain="Organizational Controls",
        control_statement="Operating procedures for information processing facilities shall be documented and made available to all personnel who need them.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.6.1": ISOControlRequirement(
        control_id="A.6.1",
        title="Screening",
        domain="People Controls",
        control_statement="Background verification checks on all candidates for employment shall be carried out in accordance with relevant laws, regulations and ethics and shall be proportional to the business requirements, the classification of the information to be accessed and the perceived risks.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.6.2": ISOControlRequirement(
        control_id="A.6.2",
        title="Terms and conditions of employment",
        domain="People Controls",
        control_statement="The employment contractual agreements shall state the personnel's and the organization's responsibilities for information security.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.6.3": ISOControlRequirement(
        control_id="A.6.3",
        title="Information security awareness, education and training",
        domain="People Controls",
        control_statement="Personnel of the organization and relevant interested parties shall receive appropriate information security awareness, education and training and regular updates of the organization's information security policy, topic-specific policies and procedures, as relevant for their job function.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.6.4": ISOControlRequirement(
        control_id="A.6.4",
        title="Disciplinary process",
        domain="People Controls",
        control_statement="A disciplinary process shall be formalized and communicated to take action against personnel and other relevant interested parties who have committed an information security policy breach.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.6.5": ISOControlRequirement(
        control_id="A.6.5",
        title="Responsibilities after termination or change of employment",
        domain="People Controls",
        control_statement="Information security responsibilities and duties that remain valid after termination or change of employment shall be defined, enforced and communicated to relevant personnel and other interested parties.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.6.6": ISOControlRequirement(
        control_id="A.6.6",
        title="Confidentiality or non-disclosure agreements",
        domain="People Controls",
        control_statement="Confidentiality or non-disclosure agreements reflecting the organization's needs for the protection of information shall be identified, documented, regularly reviewed and signed by personnel and other relevant interested parties.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.6.7": ISOControlRequirement(
        control_id="A.6.7",
        title="Remote working",
        domain="People Controls",
        control_statement="Security measures shall be implemented when personnel are working remotely to protect information accessed, processed or stored outside the organization's premises.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.6.8": ISOControlRequirement(
        control_id="A.6.8",
        title="Information security event reporting",
        domain="People Controls",
        control_statement="The organization shall provide a mechanism for personnel to report observed or suspected information security events through appropriate channels in a timely manner.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.1": ISOControlRequirement(
        control_id="A.7.1",
        title="Physical security perimeters",
        domain="Physical Controls",
        control_statement="Security perimeters shall be defined and used to protect areas that contain information and other associated assets.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.2": ISOControlRequirement(
        control_id="A.7.2",
        title="Physical entry",
        domain="Physical Controls",
        control_statement="Secure areas shall be protected by appropriate entry controls and access points.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.3": ISOControlRequirement(
        control_id="A.7.3",
        title="Securing offices, rooms and facilities",
        domain="Physical Controls",
        control_statement="Physical security for offices, rooms and facilities shall be designed and implemented.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.4": ISOControlRequirement(
        control_id="A.7.4",
        title="Physical security monitoring",
        domain="Physical Controls",
        control_statement="Premises shall be continuously monitored for unauthorized physical access.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.5": ISOControlRequirement(
        control_id="A.7.5",
        title="Protecting against physical and environmental threats",
        domain="Physical Controls",
        control_statement="Protection against physical and environmental threats, such as natural disasters and other intentional or unintentional physical threats to infrastructure shall be designed and implemented.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.6": ISOControlRequirement(
        control_id="A.7.6",
        title="Working in secure areas",
        domain="Physical Controls",
        control_statement="Security measures for working in secure areas shall be designed and implemented.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.7": ISOControlRequirement(
        control_id="A.7.7",
        title="Clear desk and clear screen",
        domain="Physical Controls",
        control_statement="Clear desk rules for papers and removable storage media and clear screen rules for information processing facilities shall be defined and appropriately enforced.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.8": ISOControlRequirement(
        control_id="A.7.8",
        title="Equipment siting and protection",
        domain="Physical Controls",
        control_statement="Equipment shall be sited securely and protected.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.9": ISOControlRequirement(
        control_id="A.7.9",
        title="Security of assets off-premises",
        domain="Physical Controls",
        control_statement="Off-site assets shall be protected.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.10": ISOControlRequirement(
        control_id="A.7.10",
        title="Storage media",
        domain="Physical Controls",
        control_statement="Storage media shall be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organization's classification scheme and handling requirements.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.11": ISOControlRequirement(
        control_id="A.7.11",
        title="Supporting utilities",
        domain="Physical Controls",
        control_statement="Information processing facilities shall be protected from power failures and other disruptions caused by failures in supporting utilities.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.12": ISOControlRequirement(
        control_id="A.7.12",
        title="Cabling security",
        domain="Physical Controls",
        control_statement="Cables carrying power, data or supporting information services shall be protected from interception, interference or damage.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.13": ISOControlRequirement(
        control_id="A.7.13",
        title="Equipment maintenance",
        domain="Physical Controls",
        control_statement="Equipment shall be correctly maintained to ensure its continued availability and integrity.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.7.14": ISOControlRequirement(
        control_id="A.7.14",
        title="Secure disposal or re-use of equipment",
        domain="Physical Controls",
        control_statement="Items of equipment containing storage media shall be verified to ensure that any sensitive data and licensed software have been deleted or securely overwritten prior to disposal or re-use.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.1": ISOControlRequirement(
        control_id="A.8.1",
        title="User endpoint devices",
        domain="Technological Controls",
        control_statement="Information stored on, processed by or accessible via user endpoint devices shall be protected.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.2": ISOControlRequirement(
        control_id="A.8.2",
        title="Privileged access rights",
        domain="Technological Controls",
        control_statement="The allocation and use of privileged access rights shall be restricted and managed.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.3": ISOControlRequirement(
        control_id="A.8.3",
        title="Information access restriction",
        domain="Technological Controls",
        control_statement="Access to information and other associated assets shall be restricted in accordance with the established topic-specific policy on access control.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.4": ISOControlRequirement(
        control_id="A.8.4",
        title="Access to source code",
        domain="Technological Controls",
        control_statement="Read and write access to source code, development tools and software libraries shall be appropriately restricted.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.5": ISOControlRequirement(
        control_id="A.8.5",
        title="Secure authentication",
        domain="Technological Controls",
        control_statement="Secure authentication technologies and procedures shall be implemented based on information access restrictions and the topic-specific policy on access control.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.6": ISOControlRequirement(
        control_id="A.8.6",
        title="Capacity management",
        domain="Technological Controls",
        control_statement="The use of resources shall be monitored and adjusted in line with current and expected capacity requirements.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.7": ISOControlRequirement(
        control_id="A.8.7",
        title="Protection against malware",
        domain="Technological Controls",
        control_statement="Protection against malware shall be implemented and supported by appropriate user awareness.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.8": ISOControlRequirement(
        control_id="A.8.8",
        title="Management of technical vulnerabilities",
        domain="Technological Controls",
        control_statement="Information about technical vulnerabilities of information systems in use shall be obtained, the organization's exposure to such vulnerabilities evaluated and appropriate measures taken.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.9": ISOControlRequirement(
        control_id="A.8.9",
        title="Configuration management",
        domain="Technological Controls",
        control_statement="Configurations, including security configurations, of hardware, software, services and networks shall be established, documented, implemented, monitored and reviewed.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.10": ISOControlRequirement(
        control_id="A.8.10",
        title="Information deletion",
        domain="Technological Controls",
        control_statement="Information stored in information systems, devices or in any other storage media shall be deleted when no longer required.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.11": ISOControlRequirement(
        control_id="A.8.11",
        title="Data masking",
        domain="Technological Controls",
        control_statement="Data masking shall be used in accordance with the organization's topic-specific policy on access control and other related topic-specific policies, and business requirements, taking applicable legislation into consideration.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.12": ISOControlRequirement(
        control_id="A.8.12",
        title="Data leakage prevention",
        domain="Technological Controls",
        control_statement="Data leakage prevention measures shall be applied to systems, networks and any other devices that process, store or transmit sensitive information.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.13": ISOControlRequirement(
        control_id="A.8.13",
        title="Information backup",
        domain="Technological Controls",
        control_statement="Backup copies of information, software and systems shall be maintained and regularly tested in accordance with the agreed topic-specific policy on backup.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.14": ISOControlRequirement(
        control_id="A.8.14",
        title="Redundancy of information processing facilities",
        domain="Technological Controls",
        control_statement="Information processing facilities shall be implemented with redundancy sufficient to meet availability requirements.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.15": ISOControlRequirement(
        control_id="A.8.15",
        title="Logging",
        domain="Technological Controls",
        control_statement="Logs that record activities, exceptions, faults and other relevant events shall be produced, stored, protected and analyzed.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.16": ISOControlRequirement(
        control_id="A.8.16",
        title="Monitoring activities",
        domain="Technological Controls",
        control_statement="Networks, systems and applications shall be monitored for anomalous behavior and appropriate actions taken to evaluate potential information security incidents.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.17": ISOControlRequirement(
        control_id="A.8.17",
        title="Clock synchronization",
        domain="Technological Controls",
        control_statement="The clocks of information processing systems shall be synchronized to approved time sources.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.18": ISOControlRequirement(
        control_id="A.8.18",
        title="Use of privileged utility programs",
        domain="Technological Controls",
        control_statement="The use of utility programs that might be capable of overriding system and application controls shall be restricted and tightly controlled.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.19": ISOControlRequirement(
        control_id="A.8.19",
        title="Installation of software on operational systems",
        domain="Technological Controls",
        control_statement="Procedures and measures shall be implemented to securely manage software installation on operational systems.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.20": ISOControlRequirement(
        control_id="A.8.20",
        title="Networks security",
        domain="Technological Controls",
        control_statement="Networks and network devices shall be secured, managed and controlled to protect information in systems and applications.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.21": ISOControlRequirement(
        control_id="A.8.21",
        title="Security of network services",
        domain="Technological Controls",
        control_statement="Security mechanisms, service levels and service requirements of network services shall be identified, implemented and monitored.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.22": ISOControlRequirement(
        control_id="A.8.22",
        title="Segregation of networks",
        domain="Technological Controls",
        control_statement="Groups of information services, users and information systems shall be segregated on the organization's networks.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.23": ISOControlRequirement(
        control_id="A.8.23",
        title="Web filtering",
        domain="Technological Controls",
        control_statement="Access to external websites shall be managed to reduce exposure to malicious content.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.24": ISOControlRequirement(
        control_id="A.8.24",
        title="Use of cryptography",
        domain="Technological Controls",
        control_statement="Rules for the effective use of cryptography, including cryptographic key management, shall be defined and implemented.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.25": ISOControlRequirement(
        control_id="A.8.25",
        title="Secure development life cycle",
        domain="Technological Controls",
        control_statement="Rules for the secure development of software and systems shall be established and applied.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.26": ISOControlRequirement(
        control_id="A.8.26",
        title="Application security requirements",
        domain="Technological Controls",
        control_statement="Information security requirements shall be identified, specified and approved when developing or acquiring applications.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.27": ISOControlRequirement(
        control_id="A.8.27",
        title="Secure system architecture and engineering principles",
        domain="Technological Controls",
        control_statement="Principles for engineering secure systems shall be established, documented, maintained and applied to any information system development activities.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.28": ISOControlRequirement(
        control_id="A.8.28",
        title="Secure coding",
        domain="Technological Controls",
        control_statement="Secure coding principles shall be applied to software development.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.29": ISOControlRequirement(
        control_id="A.8.29",
        title="Security testing in development and acceptance",
        domain="Technological Controls",
        control_statement="Security testing processes shall be defined and implemented in the development life cycle.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.30": ISOControlRequirement(
        control_id="A.8.30",
        title="Outsourced development",
        domain="Technological Controls",
        control_statement="The organization shall direct, monitor and review the activities related to outsourced system development.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.31": ISOControlRequirement(
        control_id="A.8.31",
        title="Separation of development, test and production environments",
        domain="Technological Controls",
        control_statement="Development, testing and production environments shall be separated and secured.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.32": ISOControlRequirement(
        control_id="A.8.32",
        title="Change management",
        domain="Technological Controls",
        control_statement="Changes to information processing facilities and information systems shall be subject to change management procedures.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.33": ISOControlRequirement(
        control_id="A.8.33",
        title="Test information",
        domain="Technological Controls",
        control_statement="Test information shall be appropriately selected, protected and managed.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
    "A.8.34": ISOControlRequirement(
        control_id="A.8.34",
        title="Protection of information systems during audit testing",
        domain="Technological Controls",
        control_statement="Audit tests and other assurance activities involving assessment of operational systems shall be planned and agreed between the tester and appropriate management.",
        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],
        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],
        implementation_guidance="Implement automated policy enforcement in HR Management System and maintain immutable audit log in database.",
        default_audit_cadence="ANNUAL"
    ),
}

class ISO27001ComplianceService:
    @classmethod
    def get_control(cls, control_id: str) -> ISOControlRequirement:
        return ISO_27001_CONTROLS_DATABASE.get(control_id)

    @classmethod
    def get_controls_by_domain(cls, domain: str) -> List[ISOControlRequirement]:
        return [c for c in ISO_27001_CONTROLS_DATABASE.values() if domain.lower() in c.domain.lower()]

    @classmethod
    def get_all_controls(cls) -> List[ISOControlRequirement]:
        return list(ISO_27001_CONTROLS_DATABASE.values())
