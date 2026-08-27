"""
Black-Scholes Stock Option Valuation & Equity Fair Value Engine
Calculates employee stock option fair market value (FMV) for ASC 718 / IFRS 2 share-based payment accounting.
"""
import math
from typing import Dict, Any


class BlackScholesOptionValuator:
    @staticmethod
    def standard_normal_cdf(x: float) -> float:
        """Approximation of standard normal cumulative distribution function."""
        return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

    @classmethod
    def calculate_option_fair_value(
        cls,
        stock_price: float,         # S: Current share fair market value
        strike_price: float,        # K: Option exercise strike price
        time_to_maturity_years: float, # T: Expected option life (e.g. 5.0 years)
        risk_free_interest_rate: float, # r: US Treasury yield (e.g. 0.042 for 4.2%)
        annual_volatility: float    # sigma: Historical stock volatility (e.g. 0.45 for 45%)
    ) -> Dict[str, Any]:
        if stock_price <= 0 or strike_price <= 0 or time_to_maturity_years <= 0 or annual_volatility <= 0:
            return {"option_value_per_share": 0.0, "total_grant_value": 0.0}

        sigma_sqrt_t = annual_volatility * math.sqrt(time_to_maturity_years)
        d1 = (
            math.log(stock_price / strike_price)
            + (risk_free_interest_rate + 0.5 * annual_volatility ** 2) * time_to_maturity_years
        ) / sigma_sqrt_t
        d2 = d1 - sigma_sqrt_t

        nd1 = cls.standard_normal_cdf(d1)
        nd2 = cls.standard_normal_cdf(d2)

        call_value = (
            stock_price * nd1
            - strike_price * math.exp(-risk_free_interest_rate * time_to_maturity_years) * nd2
        )

        val_per_share = max(0.0, round(call_value, 4))

        return {
            "stock_price": stock_price,
            "strike_price": strike_price,
            "time_to_maturity_years": time_to_maturity_years,
            "risk_free_rate": risk_free_interest_rate,
            "volatility": annual_volatility,
            "d1": round(d1, 4),
            "d2": round(d2, 4),
            "option_value_per_share": val_per_share,
        }
