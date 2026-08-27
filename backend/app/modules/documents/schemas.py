"""
Document Vault Schemas
"""
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class DocumentVaultCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    category: str = "POLICY"  # POLICY, CONTRACT, CERTIFICATE, TAX_FORM, ID_PROOF
    document_url: str
    file_name: str
    file_size_kb: int = 0
    mime_type: str = "application/pdf"
    is_public_policy: bool = False
    target_employee_id: Optional[str] = None
    version: str = "1.0"
    expiration_date: Optional[date] = None


class DocumentVaultResponse(DocumentVaultCreate):
    id: str
    tenant_id: str
    uploaded_by_user_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
