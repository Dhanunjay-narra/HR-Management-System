"""
Enterprise Information Security Incident Response Runbooks (NIST SP 800-61 / ISO 27035)
Defines step-by-step containment, eradication, recovery, and communication protocols for critical security scenarios.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class SecurityIncidentRunbook:
    runbook_id: str
    title: str
    severity_level: str
    action_steps: List[str]


MASTER_SECURITY_RUNBOOKS: Dict[str, SecurityIncidentRunbook] = {
    "RB-SEC-01": SecurityIncidentRunbook(
        runbook_id="RB-SEC-01",
        title="Spear-Phishing & Credential Compromise Response",
        severity_level="HIGH",
        action_steps=['Isolate affected user session across Okta/Google Workspace.', 'Force password reset and revoke all OAuth refresh tokens.', 'Query SIEM audit logs for unauthorized mailbox delegation or forwarders.', 'Audit endpoint via EDR (CrowdStrike) for malware execution.', 'Issue targeted phishing awareness retraining to user.']
    ),
    "RB-SEC-02": SecurityIncidentRunbook(
        runbook_id="RB-SEC-02",
        title="Production Database Unauthorized Access / Data Leak",
        severity_level="CRITICAL",
        action_steps=['Immediately sever active connection pool from suspect IP addresses.', 'Rotate database master credentials and application connection strings in AWS Secrets Manager.', 'Snapshot DB audit log tables and archive immutably for digital forensics.', 'Engage legal counsel and prepare GDPR/CCPA 72-hour breach disclosure if PII was exposed.', 'Conduct root cause analysis and implement tighter VPC security groups.']
    ),
    "RB-SEC-03": SecurityIncidentRunbook(
        runbook_id="RB-SEC-03",
        title="Ransomware Infection & Host Isolation Runbook",
        severity_level="CRITICAL",
        action_steps=['Network isolate infected endpoint via MDM/EDR API immediately.', 'Disable SMB file share access to prevent lateral network traversal.', 'Identify blast radius and restore unaffected data from immutable S3 backups.', 'Analyze initial access vector (exploited CVE or malicious attachment).', 'Conduct clean re-imaging of physical device hardware.']
    ),
    "RB-SEC-04": SecurityIncidentRunbook(
        runbook_id="RB-SEC-04",
        title="Distributed Denial of Service (DDoS) Mitigation",
        severity_level="HIGH",
        action_steps=['Enable Cloudflare / AWS Shield Advanced under-attack rate-limiting mode.', 'Engage Cloudflare WAF bot management heuristics and challenge suspect ASN traffic.', 'Scale backend Kubernetes pod replicas and Aurora read-replicas.', 'Verify synthetic uptime monitors and communicate incident status via statuspage.io.']
    ),
    "RB-SEC-05": SecurityIncidentRunbook(
        runbook_id="RB-SEC-05",
        title="Malicious Insider & Unauthorized Data Exfiltration",
        severity_level="HIGH",
        action_steps=['Revoke all corporate VPN, cloud console, and SaaS access tokens instantly.', 'Freeze employee hardware and preserve disk forensic image.', 'Review Git push logs, Google Drive external shares, and DLP audit trails.', 'Escalate investigation findings to Legal Counsel and People Operations.']
    ),
}

class SecurityRunbookService:
    @classmethod
    def get_runbook(cls, runbook_id: str) -> SecurityIncidentRunbook:
        return MASTER_SECURITY_RUNBOOKS.get(runbook_id)

    @classmethod
    def get_all_runbooks(cls) -> List[SecurityIncidentRunbook]:
        return list(MASTER_SECURITY_RUNBOOKS.values())
