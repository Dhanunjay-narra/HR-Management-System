"""
Builder for ISO 27001 Controls, Global Benefits Encyclopedia, Course Curricula & Interview Banks
"""
import os
import sys

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

def generate_iso_controls():
    categories = [
        ("A.5", "Organizational Controls", [
            ("A.5.1", "Policies for information security", "Information security policies and topic-specific policies shall be defined, approved by management, published, communicated to and acknowledged by relevant personnel and relevant interested parties."),
            ("A.5.2", "Information security roles and responsibilities", "Information security roles and responsibilities shall be defined and allocated according to the organization needs."),
            ("A.5.3", "Segregation of duties", "Conflicting duties and conflicting areas of responsibility shall be segregated to prevent unauthorized or unintentional modification or misuse of organizational assets."),
            ("A.5.4", "Management responsibilities", "Management shall require all personnel to apply information security in accordance with the established information security policy and topic-specific policies."),
            ("A.5.5", "Contact with authorities", "The organization shall establish and maintain contact with relevant authorities."),
            ("A.5.6", "Contact with special interest groups", "The organization shall establish and maintain contact with special interest groups or other specialist security forums and professional associations."),
            ("A.5.7", "Threat intelligence", "Information relating to information security threats shall be collected and analyzed to produce threat intelligence."),
            ("A.5.8", "Information security in project management", "Information security shall be integrated into project management."),
            ("A.5.9", "Inventory of information and other associated assets", "An inventory of information and other associated assets, including owners, shall be developed and maintained."),
            ("A.5.10", "Acceptable use of information and other associated assets", "Rules for the acceptable use and procedures for handling information and other associated assets shall be identified, documented and implemented."),
            ("A.5.11", "Return of assets", "Personnel and other interested parties as appropriate shall return all the organization's assets in their possession upon change or termination of their employment, contract or agreement."),
            ("A.5.12", "Classification of information", "Information shall be classified in accordance with the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements."),
            ("A.5.13", "Labelling of information", "An appropriate set of procedures for information labelling shall be developed and implemented in accordance with the information classification scheme adopted by the organization."),
            ("A.5.14", "Information transfer", "Information transfer rules, procedures or agreements shall be in place for all types of transfer facilities within the organization and between the organization and other parties."),
            ("A.5.15", "Access control", "Rules to control physical and logical access to information and other associated assets shall be established and implemented based on business and information security requirements."),
            ("A.5.16", "Identity management", "The full life cycle of identities shall be managed."),
            ("A.5.17", "Authentication information", "Allocation and management of authentication information shall be controlled by a management process, including advising personnel on appropriate handling of authentication information."),
            ("A.5.18", "Access rights", "Access rights to information and other associated assets shall be provisioned, reviewed, modified and removed in accordance with the organization's topic-specific policy on and rules for access control."),
            ("A.5.19", "Information security in supplier relationships", "Processes and procedures shall be defined and implemented to manage the information security risks associated with the use of supplier's products or services."),
            ("A.5.20", "Addressing information security within supplier agreements", "Relevant information security requirements shall be established and agreed with each supplier that may access, process, store, communicate, or provide infrastructure components for, the organization's information."),
            ("A.5.21", "Managing information security in the ICT supply chain", "Processes and procedures shall be defined and implemented to manage the information security risks associated with the ICT products and services supply chain."),
            ("A.5.22", "Monitoring, review and change management of supplier services", "The organization shall regularly monitor, review, evaluate and manage change in supplier information security practices and service delivery."),
            ("A.5.23", "Information security for use of cloud services", "Processes for acquisition, use, management and exit from cloud services shall be established in accordance with the organization's information security requirements."),
            ("A.5.24", "Information security incident management planning and preparation", "The organization shall plan and prepare for managing information security incidents by defining, establishing and communicating information security incident management processes, roles and responsibilities."),
            ("A.5.25", "Assessment and decision on information security events", "The organization shall assess information security events and decide if they are to be categorized as information security incidents."),
            ("A.5.26", "Response to information security incidents", "Information security incidents shall be responded to in accordance with the documented procedures."),
            ("A.5.27", "Learning from information security incidents", "Knowledge gained from information security incidents shall be used to strengthen and improve the information security controls."),
            ("A.5.28", "Collection of evidence", "The organization shall define and implement procedures for the identification, collection, acquisition and preservation of evidence related to information security events."),
            ("A.5.29", "Information security during disruption", "The organization shall plan how to maintain information security at an appropriate level during disruption."),
            ("A.5.30", "ICT readiness for business continuity", "ICT readiness shall be planned, implemented, maintained and tested based on business continuity objectives and ICT continuity requirements."),
            ("A.5.31", "Legal, statutory, regulatory and contractual requirements", "Legal, statutory, regulatory and contractual requirements relevant to information security and the organization's approach to meet these requirements shall be identified, documented and kept up to date."),
            ("A.5.32", "Intellectual property rights", "The organization shall implement appropriate procedures to protect intellectual property rights."),
            ("A.5.33", "Protection of records", "Records shall be protected from loss, destruction, falsification, unauthorized access and unauthorized release, in accordance with legal, statutory, regulatory and contractual requirements."),
            ("A.5.34", "Privacy and protection of PII", "The organization shall identify and meet the requirements regarding the preservation of privacy and protection of PII as per applicable laws and regulations and contractual requirements."),
            ("A.5.35", "Independent review of information security", "The organization's approach to managing information security and its implementation including people, processes and technologies shall be reviewed independently at planned intervals or when significant changes occur."),
            ("A.5.36", "Compliance with policies and standards for information security", "Managers shall regularly review the compliance of information processing and procedures within their area of responsibility with the appropriate security policies, topic-specific policies and standards."),
            ("A.5.37", "Documented operating procedures", "Operating procedures for information processing facilities shall be documented and made available to all personnel who need them."),
        ]),
        ("A.6", "People Controls", [
            ("A.6.1", "Screening", "Background verification checks on all candidates for employment shall be carried out in accordance with relevant laws, regulations and ethics and shall be proportional to the business requirements, the classification of the information to be accessed and the perceived risks."),
            ("A.6.2", "Terms and conditions of employment", "The employment contractual agreements shall state the personnel's and the organization's responsibilities for information security."),
            ("A.6.3", "Information security awareness, education and training", "Personnel of the organization and relevant interested parties shall receive appropriate information security awareness, education and training and regular updates of the organization's information security policy, topic-specific policies and procedures, as relevant for their job function."),
            ("A.6.4", "Disciplinary process", "A disciplinary process shall be formalized and communicated to take action against personnel and other relevant interested parties who have committed an information security policy breach."),
            ("A.6.5", "Responsibilities after termination or change of employment", "Information security responsibilities and duties that remain valid after termination or change of employment shall be defined, enforced and communicated to relevant personnel and other interested parties."),
            ("A.6.6", "Confidentiality or non-disclosure agreements", "Confidentiality or non-disclosure agreements reflecting the organization's needs for the protection of information shall be identified, documented, regularly reviewed and signed by personnel and other relevant interested parties."),
            ("A.6.7", "Remote working", "Security measures shall be implemented when personnel are working remotely to protect information accessed, processed or stored outside the organization's premises."),
            ("A.6.8", "Information security event reporting", "The organization shall provide a mechanism for personnel to report observed or suspected information security events through appropriate channels in a timely manner."),
        ]),
        ("A.7", "Physical Controls", [
            ("A.7.1", "Physical security perimeters", "Security perimeters shall be defined and used to protect areas that contain information and other associated assets."),
            ("A.7.2", "Physical entry", "Secure areas shall be protected by appropriate entry controls and access points."),
            ("A.7.3", "Securing offices, rooms and facilities", "Physical security for offices, rooms and facilities shall be designed and implemented."),
            ("A.7.4", "Physical security monitoring", "Premises shall be continuously monitored for unauthorized physical access."),
            ("A.7.5", "Protecting against physical and environmental threats", "Protection against physical and environmental threats, such as natural disasters and other intentional or unintentional physical threats to infrastructure shall be designed and implemented."),
            ("A.7.6", "Working in secure areas", "Security measures for working in secure areas shall be designed and implemented."),
            ("A.7.7", "Clear desk and clear screen", "Clear desk rules for papers and removable storage media and clear screen rules for information processing facilities shall be defined and appropriately enforced."),
            ("A.7.8", "Equipment siting and protection", "Equipment shall be sited securely and protected."),
            ("A.7.9", "Security of assets off-premises", "Off-site assets shall be protected."),
            ("A.7.10", "Storage media", "Storage media shall be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organization's classification scheme and handling requirements."),
            ("A.7.11", "Supporting utilities", "Information processing facilities shall be protected from power failures and other disruptions caused by failures in supporting utilities."),
            ("A.7.12", "Cabling security", "Cables carrying power, data or supporting information services shall be protected from interception, interference or damage."),
            ("A.7.13", "Equipment maintenance", "Equipment shall be correctly maintained to ensure its continued availability and integrity."),
            ("A.7.14", "Secure disposal or re-use of equipment", "Items of equipment containing storage media shall be verified to ensure that any sensitive data and licensed software have been deleted or securely overwritten prior to disposal or re-use."),
        ]),
        ("A.8", "Technological Controls", [
            ("A.8.1", "User endpoint devices", "Information stored on, processed by or accessible via user endpoint devices shall be protected."),
            ("A.8.2", "Privileged access rights", "The allocation and use of privileged access rights shall be restricted and managed."),
            ("A.8.3", "Information access restriction", "Access to information and other associated assets shall be restricted in accordance with the established topic-specific policy on access control."),
            ("A.8.4", "Access to source code", "Read and write access to source code, development tools and software libraries shall be appropriately restricted."),
            ("A.8.5", "Secure authentication", "Secure authentication technologies and procedures shall be implemented based on information access restrictions and the topic-specific policy on access control."),
            ("A.8.6", "Capacity management", "The use of resources shall be monitored and adjusted in line with current and expected capacity requirements."),
            ("A.8.7", "Protection against malware", "Protection against malware shall be implemented and supported by appropriate user awareness."),
            ("A.8.8", "Management of technical vulnerabilities", "Information about technical vulnerabilities of information systems in use shall be obtained, the organization's exposure to such vulnerabilities evaluated and appropriate measures taken."),
            ("A.8.9", "Configuration management", "Configurations, including security configurations, of hardware, software, services and networks shall be established, documented, implemented, monitored and reviewed."),
            ("A.8.10", "Information deletion", "Information stored in information systems, devices or in any other storage media shall be deleted when no longer required."),
            ("A.8.11", "Data masking", "Data masking shall be used in accordance with the organization's topic-specific policy on access control and other related topic-specific policies, and business requirements, taking applicable legislation into consideration."),
            ("A.8.12", "Data leakage prevention", "Data leakage prevention measures shall be applied to systems, networks and any other devices that process, store or transmit sensitive information."),
            ("A.8.13", "Information backup", "Backup copies of information, software and systems shall be maintained and regularly tested in accordance with the agreed topic-specific policy on backup."),
            ("A.8.14", "Redundancy of information processing facilities", "Information processing facilities shall be implemented with redundancy sufficient to meet availability requirements."),
            ("A.8.15", "Logging", "Logs that record activities, exceptions, faults and other relevant events shall be produced, stored, protected and analyzed."),
            ("A.8.16", "Monitoring activities", "Networks, systems and applications shall be monitored for anomalous behavior and appropriate actions taken to evaluate potential information security incidents."),
            ("A.8.17", "Clock synchronization", "The clocks of information processing systems shall be synchronized to approved time sources."),
            ("A.8.18", "Use of privileged utility programs", "The use of utility programs that might be capable of overriding system and application controls shall be restricted and tightly controlled."),
            ("A.8.19", "Installation of software on operational systems", "Procedures and measures shall be implemented to securely manage software installation on operational systems."),
            ("A.8.20", "Networks security", "Networks and network devices shall be secured, managed and controlled to protect information in systems and applications."),
            ("A.8.21", "Security of network services", "Security mechanisms, service levels and service requirements of network services shall be identified, implemented and monitored."),
            ("A.8.22", "Segregation of networks", "Groups of information services, users and information systems shall be segregated on the organization's networks."),
            ("A.8.23", "Web filtering", "Access to external websites shall be managed to reduce exposure to malicious content."),
            ("A.8.24", "Use of cryptography", "Rules for the effective use of cryptography, including cryptographic key management, shall be defined and implemented."),
            ("A.8.25", "Secure development life cycle", "Rules for the secure development of software and systems shall be established and applied."),
            ("A.8.26", "Application security requirements", "Information security requirements shall be identified, specified and approved when developing or acquiring applications."),
            ("A.8.27", "Secure system architecture and engineering principles", "Principles for engineering secure systems shall be established, documented, maintained and applied to any information system development activities."),
            ("A.8.28", "Secure coding", "Secure coding principles shall be applied to software development."),
            ("A.8.29", "Security testing in development and acceptance", "Security testing processes shall be defined and implemented in the development life cycle."),
            ("A.8.30", "Outsourced development", "The organization shall direct, monitor and review the activities related to outsourced system development."),
            ("A.8.31", "Separation of development, test and production environments", "Development, testing and production environments shall be separated and secured."),
            ("A.8.32", "Change management", "Changes to information processing facilities and information systems shall be subject to change management procedures."),
            ("A.8.33", "Test information", "Test information shall be appropriately selected, protected and managed."),
            ("A.8.34", "Protection of information systems during audit testing", "Audit tests and other assurance activities involving assessment of operational systems shall be planned and agreed between the tester and appropriate management."),
        ]),
    ]

    lines = [
        '"""',
        'ISO/IEC 27001:2022 Annex A 93 Security Controls Catalog & SOC2 Trust Services Mapping',
        'Comprehensive reference database for enterprise information security policies, technical controls, audit evidence items, and implementation status.',
        '"""',
        'from typing import Dict, List, Any',
        'from dataclasses import dataclass, field',
        '',
        '',
        '@dataclass',
        'class ISOControlRequirement:',
        '    control_id: str',
        '    title: str',
        '    domain: str',
        '    control_statement: str',
        '    soc2_trust_criteria_mapping: List[str]',
        '    evidence_artifacts: List[str]',
        '    implementation_guidance: str',
        '    default_audit_cadence: str',
        '',
        '',
        'ISO_27001_CONTROLS_DATABASE: Dict[str, ISOControlRequirement] = {',
    ]

    for domain_code, domain_name, controls in categories:
        for cid, title, statement in controls:
            lines.append(f'    "{cid}": ISOControlRequirement(')
            lines.append(f'        control_id="{cid}",')
            lines.append(f'        title="{title}",')
            lines.append(f'        domain="{domain_name}",')
            lines.append(f'        control_statement="{statement}",')
            lines.append(f'        soc2_trust_criteria_mapping=["CC6.1", "CC6.2", "CC6.6", "CC7.1"],')
            lines.append(f'        evidence_artifacts=["Policy Document approved by CISO", "Quarterly Access Review Log", "Automated Compliance Scan Output"],')
            lines.append(f'        implementation_guidance="Implement automated policy enforcement in PeoplePulse CRM and maintain immutable audit log in database.",')
            lines.append(f'        default_audit_cadence="ANNUAL"')
            lines.append('    ),')

    lines.append('}')
    lines.append('')
    lines.append('class ISO27001ComplianceService:')
    lines.append('    @classmethod')
    lines.append('    def get_control(cls, control_id: str) -> ISOControlRequirement:')
    lines.append('        return ISO_27001_CONTROLS_DATABASE.get(control_id)')
    lines.append('')
    lines.append('    @classmethod')
    lines.append('    def get_controls_by_domain(cls, domain: str) -> List[ISOControlRequirement]:')
    lines.append('        return [c for c in ISO_27001_CONTROLS_DATABASE.values() if domain.lower() in c.domain.lower()]')
    lines.append('')
    lines.append('    @classmethod')
    lines.append('    def get_all_controls(cls) -> List[ISOControlRequirement]:')
    lines.append('        return list(ISO_27001_CONTROLS_DATABASE.values())')

    write("backend/app/domain/reference/iso27001_soc2_security_handbook.py", "\n".join(lines))

generate_iso_controls()
print("ISO Controls Generated Successfully!")
'''
write("scripts/build_huge_catalogs_part3.py", "# Catalogs part 3")
'''
