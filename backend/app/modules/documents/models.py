"""
Document Vault & Policy Models
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class DocumentVault(TenantBaseModel):
    """Organization Policy or Employee Document."""
    __tablename__ = "document_vault"

    title = Column(String(255), nullable=False, index=True)
    category = Column(String(50), default="POLICY", nullable=False, index=True)  # POLICY, CONTRACT, CERTIFICATE, TAX_FORM, ID_PROOF
    document_url = Column(String(500), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_size_kb = Column(Integer, default=0, nullable=False)
    mime_type = Column(String(100), default="application/pdf", nullable=False)
    
    is_public_policy = Column(Boolean, default=False, nullable=False, index=True)
    target_employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=True, index=True)
    
    version = Column(String(20), default="1.0", nullable=False)
    expiration_date = Column(Date, nullable=True)
    uploaded_by_user_id = Column(String(36), nullable=False)

    # Relationships
    target_employee = relationship("Employee")
