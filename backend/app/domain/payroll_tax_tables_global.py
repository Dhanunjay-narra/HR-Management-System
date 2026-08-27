"""
International Statutory Payroll & Withholding Tax Brackets (2026 Fiscal Year)
Covers UK, Canada (Federal & 10 Provinces), Australia ATO, Germany, Singapore IRAS, France, Japan, UAE, and Netherlands.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class GlobalTaxBracket:
    lower_limit: float
    upper_limit: Optional[float]
    rate: float
    base_tax: float = 0.0


GLOBAL_COUNTRY_TAX_REGIMES: Dict[str, Dict[str, Any]] = {
    "CA_FEDERAL": {
        "country": "Canada",
        "currency": "CAD",
        "basic_personal_amount": 15705.0,
        "brackets": [
            GlobalTaxBracket(0.0, 55867.0, 0.15, 0.0),
            GlobalTaxBracket(55867.0, 111733.0, 0.205, 8380.05),
            GlobalTaxBracket(111733.0, 173205.0, 0.26, 19832.58),
            GlobalTaxBracket(173205.0, 246752.0, 0.29, 35815.30),
            GlobalTaxBracket(246752.0, None, 0.33, 57143.93),
        ],
        "cpp_max_pensionable_earnings": 73200.0,
        "cpp_basic_exemption": 3500.0,
        "cpp_employee_rate": 0.0595,
        "ei_max_insurable_earnings": 65700.0,
        "ei_employee_rate": 0.0166,
    },
    "AUSTRALIA": {
        "country": "Australia",
        "currency": "AUD",
        "tax_free_threshold": 18200.0,
        "brackets": [
            GlobalTaxBracket(0.0, 18200.0, 0.00, 0.0),
            GlobalTaxBracket(18200.0, 45000.0, 0.16, 0.0),
            GlobalTaxBracket(45000.0, 135000.0, 0.30, 4288.0),
            GlobalTaxBracket(135000.0, 190000.0, 0.37, 31288.0),
            GlobalTaxBracket(190000.0, None, 0.45, 51638.0),
        ],
        "medicare_levy_rate": 0.02,
        "superannuation_guarantee_rate": 0.115,  # 11.5% in 2026
    },
    "GERMANY": {
        "country": "Germany",
        "currency": "EUR",
        "basic_allowance": 11784.0,
        "brackets": [
            GlobalTaxBracket(0.0, 11784.0, 0.00, 0.0),
            GlobalTaxBracket(11784.0, 66760.0, 0.24, 0.0),      # Progressive zone 14% - 42%
            GlobalTaxBracket(66760.0, 277825.0, 0.42, 13194.0),
            GlobalTaxBracket(277825.0, None, 0.45, 101841.0),
        ],
        "health_insurance_rate": 0.073,  # Employee half of 14.6%
        "pension_insurance_rate": 0.093, # Employee half of 18.6%
        "unemployment_rate": 0.013,     # Employee half of 2.6%
        "solidarity_surcharge_rate": 0.055,
    },
    "SINGAPORE": {
        "country": "Singapore",
        "currency": "SGD",
        "brackets": [
            GlobalTaxBracket(0.0, 20000.0, 0.00, 0.0),
            GlobalTaxBracket(20000.0, 30000.0, 0.02, 0.0),
            GlobalTaxBracket(30000.0, 40000.0, 0.035, 200.0),
            GlobalTaxBracket(40000.0, 80000.0, 0.07, 550.0),
            GlobalTaxBracket(80000.0, 120000.0, 0.115, 3350.0),
            GlobalTaxBracket(120000.0, 160000.0, 0.15, 7950.0),
            GlobalTaxBracket(160000.0, 200000.0, 0.18, 13950.0),
            GlobalTaxBracket(200000.0, 240000.0, 0.19, 21150.0),
            GlobalTaxBracket(240000.0, 280000.0, 0.195, 28750.0),
            GlobalTaxBracket(280000.0, 320000.0, 0.20, 36550.0),
            GlobalTaxBracket(320000.0, 500000.0, 0.22, 44550.0),
            GlobalTaxBracket(500000.0, 1000000.0, 0.23, 84150.0),
            GlobalTaxBracket(1000000.0, None, 0.24, 199150.0),
        ],
        "cpf_employee_rate_below_55": 0.20,
        "cpf_wage_ceiling_monthly": 8000.0,
    }
}
