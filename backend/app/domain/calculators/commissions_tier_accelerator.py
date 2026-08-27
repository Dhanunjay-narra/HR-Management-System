"""
Sales Commission & Tiered Quota Accelerator Engine
Calculates progressive commission tiers (e.g. 100% at quota, 150% above quota, 200% super-stretch), non-recoverable draws, and clawbacks.
"""
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass


@dataclass
class CommissionTier:
    min_attainment_pct: float
    max_attainment_pct: Optional[float]
    commission_rate_pct: float
    accelerator_multiplier: float


@dataclass
class CommissionCalculationResult:
    rep_id: str
    rep_name: str
    quota_usd: float
    closed_revenue_usd: float
    attainment_pct: float
    base_commission_usd: float
    accelerated_commission_usd: float
    total_commission_payable_usd: float
    monthly_draw_applied_usd: float
    net_commission_disbursed_usd: float


class SalesCommissionAcceleratorEngine:
    # Standard Progressive Commission Acceleration Schedule
    TIERS: List[CommissionTier] = [
        CommissionTier(0.0, 50.0, 0.05, 0.50),    # Below 50% attainment: 50% rate penalty
        CommissionTier(50.0, 100.0, 0.10, 1.00),  # 50% - 100% attainment: 100% full rate (10% on closed deals)
        CommissionTier(100.0, 150.0, 0.15, 1.50), # 100% - 150% attainment: 1.5x Accelerator (15% rate)
        CommissionTier(150.0, None, 0.20, 2.00),  # 150%+ attainment: 2.0x Super-Accelerator (20% rate)
    ]

    @classmethod
    def compute_commission(
        cls,
        rep_id: str,
        rep_name: str,
        quota_usd: float,
        closed_revenue_usd: float,
        monthly_guaranteed_draw: float = 0.0,
        is_draw_recoverable: bool = False
    ) -> CommissionCalculationResult:
        if quota_usd <= 0:
            return CommissionCalculationResult(rep_id, rep_name, 0, 0, 0, 0, 0, 0, 0, 0)

        attainment_pct = round((closed_revenue_usd / quota_usd) * 100.0, 2)
        total_comm = 0.0

        for t in cls.TIERS:
            if attainment_pct > t.min_attainment_pct:
                if t.max_attainment_pct is not None:
                    attained_in_tier = min(attainment_pct, t.max_attainment_pct) - t.min_attainment_pct
                else:
                    attained_in_tier = attainment_pct - t.min_attainment_pct

                rev_in_tier = (attained_in_tier / 100.0) * quota_usd
                comm_in_tier = rev_in_tier * t.commission_rate_pct
                total_comm += comm_in_tier

        total_comm = round(total_comm, 2)
        net_payable = total_comm

        if monthly_guaranteed_draw > 0:
            if is_draw_recoverable:
                net_payable = max(0.0, total_comm - monthly_guaranteed_draw)
            else:
                net_payable = max(monthly_guaranteed_draw, total_comm)

        return CommissionCalculationResult(
            rep_id=rep_id,
            rep_name=rep_name,
            quota_usd=quota_usd,
            closed_revenue_usd=closed_revenue_usd,
            attainment_pct=attainment_pct,
            base_commission_usd=round(closed_revenue_usd * 0.10, 2),
            accelerated_commission_usd=total_comm,
            total_commission_payable_usd=total_comm,
            monthly_draw_applied_usd=monthly_guaranteed_draw,
            net_commission_disbursed_usd=round(net_payable, 2)
        )
