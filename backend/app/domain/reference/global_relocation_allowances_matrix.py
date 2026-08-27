"""
Global Employee Relocation Benefit Packages & Mobility Policy Schedules
Prescribes tiered relocation allowances, temporary corporate housing durations, shipment subsidies, and tax gross-up formulas.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class RelocationPackageTier:
    tier_code: str
    tier_title: str
    target_grades: str
    total_budget_cap_usd: float
    temporary_housing_days: int
    household_goods_shipment_cap_usd: float
    miscellaneous_relocation_allowance_usd: float
    policy_inclusions: str


MASTER_RELOCATION_PACKAGES: Dict[str, RelocationPackageTier] = {
    "RELOC-TIER-1": RelocationPackageTier(
        tier_code="RELOC-TIER-1",
        tier_title="Executive International Relocation Package",
        target_grades="VP & C-Level",
        total_budget_cap_usd=65000.0,
        temporary_housing_days=90,
        household_goods_shipment_cap_usd=15000.0,
        miscellaneous_relocation_allowance_usd=12000.0,
        policy_inclusions="Full International Moving & White Glove Packing, 90 Days Temporary Housing, Destination School Search, Spouse Career Coaching, Complete Tax Equalization."
    ),
    "RELOC-TIER-2": RelocationPackageTier(
        tier_code="RELOC-TIER-2",
        tier_title="Senior Specialist / Staff Engineer Package",
        target_grades="Senior / Staff (L4-L5)",
        total_budget_cap_usd=35000.0,
        temporary_housing_days=60,
        household_goods_shipment_cap_usd=8000.0,
        miscellaneous_relocation_allowance_usd=6000.0,
        policy_inclusions="Full Container Household Goods Shipment, 60 Days Temporary Housing, Immigration Visa Expediting, Destination Home Finding Tour."
    ),
    "RELOC-TIER-3": RelocationPackageTier(
        tier_code="RELOC-TIER-3",
        tier_title="Standard Professional Relocation Package",
        target_grades="Mid-Level (L2-L3)",
        total_budget_cap_usd=18000.0,
        temporary_housing_days=30,
        household_goods_shipment_cap_usd=4000.0,
        miscellaneous_relocation_allowance_usd=3000.0,
        policy_inclusions="Self-Directed Lump Sum Stipend with Tax Gross-Up, 30 Days Corporate Apartment, Flight Booking Assistance."
    ),
    "RELOC-TIER-4": RelocationPackageTier(
        tier_code="RELOC-TIER-4",
        tier_title="Early Career / Graduate Relocation Package",
        target_grades="Entry-Level (L1)",
        total_budget_cap_usd=7500.0,
        temporary_housing_days=14,
        household_goods_shipment_cap_usd=1500.0,
        miscellaneous_relocation_allowance_usd=1000.0,
        policy_inclusions="Direct Relocation Allowance Lump Sum ($7,500 Grossed-Up), 14 Days Hotel Stay, Relocation Concierge Support."
    ),
}

class RelocationPackageService:
    @classmethod
    def get_package(cls, code: str) -> RelocationPackageTier:
        return MASTER_RELOCATION_PACKAGES.get(code)

    @classmethod
    def get_all_packages(cls) -> List[RelocationPackageTier]:
        return list(MASTER_RELOCATION_PACKAGES.values())
