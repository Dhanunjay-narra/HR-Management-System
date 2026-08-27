"""
AI Document Processing Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import date
from pydantic import BaseModel, Field


class ResumeParseRequest(BaseModel):
    raw_text: str = Field(..., min_length=10)


class ResumeParseResponse(BaseModel):
    candidate_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    extracted_skills: List[str] = []
    experience_years_estimated: float = 0.0
    detected_titles: List[str] = []
    education: List[str] = []


class ReceiptParseRequest(BaseModel):
    receipt_raw_text: str = Field(..., min_length=5)


class ReceiptParseResponse(BaseModel):
    merchant_name: Optional[str] = None
    total_amount: float = 0.0
    currency: str = "USD"
    expense_date: Optional[date] = None
    line_items: List[Dict[str, Any]] = []
    category_suggestion: str = "OFFICE_SUPPLIES"
