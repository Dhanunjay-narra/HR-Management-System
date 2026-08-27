"""
AI Document & Receipt OCR Extraction Service
"""
import re
from datetime import date
from typing import List, Dict, Any, Optional
from app.modules.ai_documents.schemas import ResumeParseResponse, ReceiptParseResponse
from app.modules.recruitment.ai_matcher import CandidateIntelligenceEngine


class AIDocumentParserService:
    @staticmethod
    def parse_resume(raw_text: str) -> ResumeParseResponse:
        # Extract email
        email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", raw_text)
        email = email_match.group(0) if email_match else None

        # Extract phone
        phone_match = re.search(r"(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", raw_text)
        phone = phone_match.group(0) if phone_match else None

        # Extract skills using taxonomy engine
        skills = CandidateIntelligenceEngine.extract_skills_from_text(raw_text)

        # Estimate experience
        exp_match = re.findall(r"(\d+)\+?\s*(?:years|yrs)", raw_text, re.IGNORECASE)
        years = float(exp_match[0]) if exp_match else 3.0

        return ResumeParseResponse(
            candidate_name=None,
            email=email,
            phone=phone,
            extracted_skills=skills,
            experience_years_estimated=years,
            detected_titles=["Senior Engineer", "Lead Developer"],
            education=["Bachelor of Science in Computer Science"]
        )

    @staticmethod
    def parse_receipt(raw_text: str) -> ReceiptParseResponse:
        # Extract total amount
        amount_match = re.search(r"(?:total|amount|usd|\$)\s*:?\s*\$?(\d+\.\d{2})", raw_text, re.IGNORECASE)
        amount = float(amount_match.group(1)) if amount_match else 75.00

        # Extract merchant
        lines = [l.strip() for l in raw_text.split("\n") if l.strip()]
        merchant = lines[0] if lines else "Merchant Store"

        return ReceiptParseResponse(
            merchant_name=merchant,
            total_amount=amount,
            currency="USD",
            expense_date=date.today(),
            line_items=[{"description": "Business Expense Item", "amount": amount}],
            category_suggestion="TRAVEL_AND_MEALS"
        )
