"""
AI Document Processing API Endpoints
"""
from fastapi import APIRouter, Depends
from app.modules.ai_documents.schemas import (
    ResumeParseRequest, ResumeParseResponse, ReceiptParseRequest, ReceiptParseResponse
)
from app.modules.ai_documents.parser_service import AIDocumentParserService
from app.middleware.auth_deps import require_permission, CurrentUser

router = APIRouter(prefix="/ai/documents", tags=["AI Document Processing"])


@router.post("/parse-resume", response_model=ResumeParseResponse)
async def parse_candidate_resume(
    data: ResumeParseRequest,
    current_user: CurrentUser = Depends(require_permission("ai.documents.parse")),
):
    """Extract candidate skills, contact info, and experience from unformatted CV text."""
    return AIDocumentParserService.parse_resume(data.raw_text)


@router.post("/parse-receipt", response_model=ReceiptParseResponse)
async def parse_expense_receipt(
    data: ReceiptParseRequest,
    current_user: CurrentUser = Depends(require_permission("ai.documents.parse")),
):
    """Extract merchant, total amount, and line items from expense receipts."""
    return AIDocumentParserService.parse_receipt(data.receipt_raw_text)
