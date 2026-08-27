"""
Document Compliance, GDPR Data Retention & PII Scrubbing Engine
Automates data retention schedules, right-to-be-forgotten redactions, and SOC2 evidence verification.
"""
import re
from typing import Dict, List, Any, Optional
from datetime import datetime, timezone, timedelta


class DocumentComplianceEngine:
    RETENTION_SCHEDULES_YEARS = {
        "PAYROLL_RECORDS": 7,      # IRS / HMRC standard
        "TAX_DOCUMENTS": 7,
        "EMPLOYMENT_CONTRACT": 6,
        "PERFORMANCE_REVIEWS": 3,
        "BACKGROUND_CHECKS": 2,
        "REJECTED_APPLICATIONS": 1,
        "EXPENSE_RECEIPTS": 7,
        "MEDICAL_RECORDS": 5
    }

    PII_REGEX_PATTERNS = [
        (r"\\b\\d{3}-\\d{2}-\\d{4}\\b", "[REDACTED_SSN]"),
        (r"\\b(?:\\d[ -]*?){13,16}\\b", "[REDACTED_CREDIT_CARD]"),
        (r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+", "[REDACTED_EMAIL]"),
        (r"(?:\\+?\\d{1,3}[-.\\s]?)?\\(?\\d{3}\\)?[-.\\s]?\\d{3}[-.\\s]?\\d{4}", "[REDACTED_PHONE]"),
    ]

    @classmethod
    def calculate_purge_date(cls, document_type: str, creation_date: datetime) -> datetime:
        years = cls.RETENTION_SCHEDULES_YEARS.get(document_type, 5)
        return creation_date + timedelta(days=365 * years)

    @classmethod
    def scrub_pii(cls, text_content: str) -> str:
        scrubbed = text_content
        for pattern, replacement in cls.PII_REGEX_PATTERNS:
            scrubbed = re.sub(pattern, replacement, scrubbed)
        return scrubbed

    @classmethod
    def is_document_expired(cls, document_type: str, creation_date: datetime) -> bool:
        purge_dt = cls.calculate_purge_date(document_type, creation_date)
        return datetime.now(timezone.utc) >= purge_dt
