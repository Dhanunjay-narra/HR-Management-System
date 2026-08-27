"""
ISO/IEC 27001 & SOC2 Type II Auditor Testing Checklists & Workpaper Procedures
Prescribes objective audit verification test steps, sampling guidelines, and acceptable evidence criteria.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class AuditorChecklistProcedure:
    audit_procedure_id: str
    domain_title: str
    test_steps: List[str]


MASTER_AUDIT_CHECKLISTS: Dict[str, AuditorChecklistProcedure] = {
    "AUD-01": AuditorChecklistProcedure(
        audit_procedure_id="AUD-01",
        domain_title="Access Control & Identity Lifecycle (A.5.15 - A.5.18)",
        test_steps=['Verify automated offboarding script revokes Okta/Google Workspace accounts within 60 seconds.', 'Sample 25 new hires; inspect signed acceptable use policies and completed background check certificates.', 'Review quarterly privileged access review logs; ensure 100% manager sign-off compliance.', 'Inspect MFA configuration; verify SMS/Voice 2FA is disabled and only FIDO2 WebAuthn/TOTP is enforced.']
    ),
    "AUD-02": AuditorChecklistProcedure(
        audit_procedure_id="AUD-02",
        domain_title="Cryptography & Key Management (A.8.24)",
        test_steps=['Verify all PostgreSQL database instances enforce TLS 1.3 with AES-256 in-transit encryption.', 'Confirm AWS Secrets Manager / KMS automatic 90-day cryptographic key rotation is enabled.', 'Verify zero plaintext credentials or API tokens exist across Git commits via pre-commit trufflehog scans.']
    ),
    "AUD-03": AuditorChecklistProcedure(
        audit_procedure_id="AUD-03",
        domain_title="Vulnerability Management & SSDLC (A.8.8, A.8.25 - A.8.29)",
        test_steps=['Inspect weekly automated container vulnerability scans (Trivy/Snyk); verify zero unpatched Critical CVEs > 14 days.', 'Sample 10 production pull requests; verify at least one peer approval and passing automated Pytest/CI pipeline.', 'Review annual third-party external network and web application penetration test report.']
    ),
    "AUD-04": AuditorChecklistProcedure(
        audit_procedure_id="AUD-04",
        domain_title="Business Continuity & Disaster Recovery (A.5.29 - A.5.30)",
        test_steps=['Inspect annual DR simulation report; verify multi-region RDS failover succeeded in < 15 minutes.', 'Sample 5 database backups; test automated restore to isolated sandbox and verify data integrity checksum.', 'Review business impact analysis (BIA) and confirm critical system RPO (1 hour) and RTO (4 hours) objectives.']
    ),
}

class AuditChecklistService:
    @classmethod
    def get_checklist(cls, aid: str) -> AuditorChecklistProcedure:
        return MASTER_AUDIT_CHECKLISTS.get(aid)

    @classmethod
    def get_all_checklists(cls) -> List[AuditorChecklistProcedure]:
        return list(MASTER_AUDIT_CHECKLISTS.values())
