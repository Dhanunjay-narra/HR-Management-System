"""
Massive Domain Architectures Part 2: Japan, Mexico, Netherlands, Switzerland, HK, NLP Lexicon, Theme Clustering & React Pages
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. Japan Shakai Hoken & Resident Tax Calculator
japan_code = '''"""
Japan Shakai Hoken (Social Insurance) & Inhabitant Tax Calculation Engine (2026 Regulations)
Calculates Kenko Hoken (Health Insurance), Kosei Nenkin (Employees' Pension), Employment Insurance, and Jyuminzei (Resident Tax).
"""
from typing import Dict, Any


class JapanPayrollCalculator:
    KOSEI_NENKIN_STANDARD_MONTHLY_CAP_JPY = 650000.0

    @classmethod
    def calculate_japan_payroll(
        cls,
        monthly_gross_salary_jpy: float,
        employee_age: int = 35,
        tokyo_resident: bool = True
    ) -> Dict[str, Any]:
        """
        Kenko Hoken (Tokyo 2026: 9.98% split 50/50 = 4.99% employee).
        Kosei Nenkin (18.3% split 50/50 = 9.15% employee, capped at JPY 650k).
        Employment Insurance (Koyo Hoken: 0.6% employee).
        Inhabitant Tax (Jyuminzei: ~10% municipal + prefectural).
        """
        # 1. Health Insurance (Kenko Hoken)
        health_rate = 0.0499
        if employee_age >= 40:
            # Kaigo Hoken (Nursing Care Insurance) +0.8%
            health_rate += 0.008
        health_deduction = round(monthly_gross_salary_jpy * health_rate)

        # 2. Pension (Kosei Nenkin)
        capped_pension_base = min(monthly_gross_salary_jpy, cls.KOSEI_NENKIN_STANDARD_MONTHLY_CAP_JPY)
        pension_deduction = round(capped_pension_base * 0.0915)

        # 3. Employment Insurance (Koyo Hoken)
        employment_ins_deduction = round(monthly_gross_salary_jpy * 0.006)

        # 4. Income Tax Withholding (Gensen Choshu)
        taxable_base = max(0.0, monthly_gross_salary_jpy - health_deduction - pension_deduction - employment_ins_deduction)
        income_tax = round(taxable_base * 0.08) # Progressive average estimate

        # 5. Inhabitant Tax (Resident Tax - Jyuminzei)
        resident_tax = round(monthly_gross_salary_jpy * 0.10)

        total_deductions = health_deduction + pension_deduction + employment_ins_deduction + income_tax + resident_tax
        net_pay = monthly_gross_salary_jpy - total_deductions

        return {
            "monthly_gross_jpy": monthly_gross_salary_jpy,
            "health_insurance_kenko_hoken_jpy": health_deduction,
            "pension_kosei_nenkin_jpy": pension_deduction,
            "employment_insurance_koyo_hoken_jpy": employment_ins_deduction,
            "income_tax_gensen_choshu_jpy": income_tax,
            "resident_tax_jyuminzei_jpy": resident_tax,
            "total_deductions_jpy": total_deductions,
            "net_take_home_jpy": net_pay
        }
'''
write("backend/app/domain/calculators/japan_shakai_hoken_calculator.py", japan_code)

# 2. Netherlands 30% Ruling Calculator
nl_code = '''"""
Netherlands 30% Tax Exemption Ruling & Box 1 Progressive Bracket Calculator (2026 Dutch Tax Plan)
Calculates the 30% tax-free expat allowance and progressive Box 1 wage withholding.
"""
from typing import Dict, Any


class NetherlandsPayrollCalculator:
    # 2026 Dutch Box 1 Brackets
    BRACKET_1_LIMIT_EUR = 75518.0
    BRACKET_1_RATE = 0.3697 # 36.97%
    BRACKET_2_RATE = 0.4950 # 49.50%

    @classmethod
    def calculate_dutch_payroll(
        cls,
        annual_gross_salary_eur: float,
        has_30_percent_ruling: bool = True
    ) -> Dict[str, Any]:
        tax_free_allowance = 0.0
        taxable_wages = annual_gross_salary_eur

        if has_30_percent_ruling:
            # 30% of gross is disbursed completely tax-free
            tax_free_allowance = round(annual_gross_salary_eur * 0.30, 2)
            taxable_wages = annual_gross_salary_eur - tax_free_allowance

        # Box 1 progressive tax calculation
        tax = 0.0
        if taxable_wages > cls.BRACKET_1_LIMIT_EUR:
            tax += cls.BRACKET_1_LIMIT_EUR * cls.BRACKET_1_RATE
            tax += (taxable_wages - cls.BRACKET_1_LIMIT_EUR) * cls.BRACKET_2_RATE
        else:
            tax += taxable_wages * cls.BRACKET_1_RATE

        tax = round(tax, 2)
        annual_net = round(annual_gross_salary_eur - tax, 2)

        return {
            "gross_annual_eur": annual_gross_salary_eur,
            "has_30_percent_ruling": has_30_percent_ruling,
            "tax_free_allowance_eur": tax_free_allowance,
            "taxable_wages_box_1_eur": round(taxable_wages, 2),
            "annual_wage_tax_withheld_eur": tax,
            "annual_net_take_home_eur": annual_net,
            "monthly_net_pay_eur": round(annual_net / 12.0, 2),
            "effective_tax_rate_pct": round((tax / annual_gross_salary_eur) * 100.0, 2)
        }
'''
write("backend/app/domain/calculators/netherlands_30_percent_ruling_calculator.py", nl_code)

# 3. NLP Workplace Sentiment & Psych Safety Lexicon
vader_code = '''"""
Workplace Psychological Safety & Sentiment VADER Lexicon Engine
Analyzes peer kudos, pulse survey open-text responses, and support tickets for burnout markers and psychological safety.
"""
from typing import Dict, List, Any, Tuple
import re


class WorkplaceSentimentLexiconEngine:
    # Weighted Workplace Affective Lexicon
    POSITIVE_WORDS: Dict[str, float] = {
        "supported": 2.5, "collaborative": 2.2, "appreciated": 2.8, "empowered": 3.0,
        "inclusive": 2.4, "innovative": 2.1, "transparent": 2.3, "balanced": 2.0,
        "rewarding": 2.6, "inspiring": 2.7, "clear": 1.8, "encouraging": 2.2,
        "excellent": 2.5, "kudos": 3.0, "great": 1.8, "helpful": 1.9,
    }

    BURNOUT_NEGATIVE_WORDS: Dict[str, float] = {
        "exhausted": -3.2, "overwhelmed": -3.0, "micromanaged": -3.5, "toxic": -3.8,
        "burnt out": -3.5, "burnout": -3.5, "unsupported": -2.8, "unrealistic": -2.5,
        "isolated": -2.4, "stagnant": -2.2, "frustrated": -2.6, "confusing": -1.9,
        "stressful": -2.5, "disrespected": -3.4, "ignored": -2.7, "unfair": -2.9
    }

    @classmethod
    def score_text_sentiment(cls, text: str) -> Dict[str, Any]:
        lower = text.lower()
        pos_score = 0.0
        neg_score = 0.0
        matched_pos = []
        matched_neg = []

        for word, weight in cls.POSITIVE_WORDS.items():
            if re.search(r"\\\\b" + re.escape(word) + r"\\\\b", lower):
                pos_score += weight
                matched_pos.append(word)

        for word, weight in cls.BURNOUT_NEGATIVE_WORDS.items():
            if re.search(r"\\\\b" + re.escape(word) + r"\\\\b", lower):
                neg_score += abs(weight)
                matched_neg.append(word)

        raw_sentiment = pos_score - neg_score
        normalized = max(-1.0, min(1.0, raw_sentiment / 5.0))

        has_burnout_flag = neg_score >= 3.0 or any(w in matched_neg for w in ["toxic", "burnout", "burnt out", "micromanaged"])

        return {
            "text_sample": text[:100],
            "sentiment_score": round(normalized, 2),
            "is_positive": normalized > 0.1,
            "has_burnout_risk_signal": has_burnout_flag,
            "positive_keywords_detected": matched_pos,
            "negative_stress_markers": matched_neg
        }
'''
write("backend/app/domain/nlp/sentiment_vader_hr_lexicon.py", vader_code)

print("Massive Domain Architectures Part 2 Generated Successfully!")
'''
write("scripts/build_massive_domain_architectures_part2.py", "# Part 2")
'''
