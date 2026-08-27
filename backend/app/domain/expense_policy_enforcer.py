"""
Enterprise Expense Policy & Anomaly Detection Engine
Enforces daily meal per-diems, receipt limits, duplicate hash matching, and foreign currency normalizations.
"""
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
import hashlib


@dataclass
class ExpenseViolation:
    rule_code: str
    severity: str  # WARNING, BLOCKING
    message: str
    overage_amount: float = 0.0


class ExpensePolicyEnforcementEngine:
    CATEGORY_DAILY_CAPS = {
        "MEALS": 75.0,
        "LODGING_TIER_1": 300.0,
        "LODGING_TIER_2": 200.0,
        "TRANSPORTATION_TAXI": 100.0,
        "OFFICE_SUPPLIES": 150.0,
        "TEAM_ENTERTAINMENT": 500.0
    }

    FX_RATES_TO_USD = {
        "USD": 1.0,
        "EUR": 1.08,
        "GBP": 1.28,
        "CAD": 0.74,
        "AUD": 0.66,
        "INR": 0.012,
        "JPY": 0.0065,
        "SGD": 0.76,
        "AED": 0.272
    }

    @classmethod
    def normalize_to_usd(cls, amount: float, currency: str) -> float:
        rate = cls.FX_RATES_TO_USD.get(currency.upper(), 1.0)
        return round(amount * rate, 2)

    @classmethod
    def audit_expense_claim(
        cls,
        category: str,
        amount: float,
        currency: str,
        receipt_hash: Optional[str],
        previous_claim_hashes: List[str],
        has_itemized_receipt: bool,
        days_since_incurred: int
    ) -> List[ExpenseViolation]:
        violations: List[ExpenseViolation] = []
        usd_amount = cls.normalize_to_usd(amount, currency)

        # 1. Receipt requirement
        if usd_amount > 25.0 and not has_itemized_receipt:
            violations.append(ExpenseViolation(
                rule_code="EXP-001",
                severity="BLOCKING",
                message="Itemized receipt is mandatory for expenditures exceeding $25.00 USD."
            ))

        # 2. Duplicate receipt fraud check
        if receipt_hash and receipt_hash in previous_claim_hashes:
            violations.append(ExpenseViolation(
                rule_code="EXP-002",
                severity="BLOCKING",
                message="Duplicate receipt detected. This document was previously submitted in another claim."
            ))

        # 3. Category cap overage
        cap = cls.CATEGORY_DAILY_CAPS.get(category.upper(), 500.0)
        if usd_amount > cap:
            overage = usd_amount - cap
            violations.append(ExpenseViolation(
                rule_code="EXP-003",
                severity="WARNING",
                message=f"Claim amount (${usd_amount:.2f} USD) exceeds standard daily policy threshold (${cap:.2f} USD). Requires Director approval.",
                overage_amount=round(overage, 2)
            ))

        # 4. Late submission
        if days_since_incurred > 60:
            violations.append(ExpenseViolation(
                rule_code="EXP-004",
                severity="BLOCKING",
                message=f"Claim submitted {days_since_incurred} days after occurrence (limit: 60 days)."
            ))
        elif days_since_incurred > 30:
            violations.append(ExpenseViolation(
                rule_code="EXP-005",
                severity="WARNING",
                message=f"Claim submitted beyond standard 30-day window ({days_since_incurred} days)."
            ))

        return violations
