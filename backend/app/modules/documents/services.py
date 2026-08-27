"""
Document Management Service
"""
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc, or_

from app.modules.documents.models import DocumentVault
from app.modules.documents.schemas import DocumentVaultCreate
from app.core.exceptions import ResourceNotFoundException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class DocumentService:
    @staticmethod
    async def upload_document(
        db: AsyncSession,
        tenant_id: str,
        user_id: str,
        data: DocumentVaultCreate
    ) -> DocumentVault:
        doc = DocumentVault(
            tenant_id=tenant_id,
            uploaded_by_user_id=user_id,
            **data.model_dump()
        )
        db.add(doc)
        await db.flush()

        if doc.target_employee_id:
            db.add(EmployeeTimelineEvent(
                tenant_id=tenant_id,
                employee_id=doc.target_employee_id,
                actor_id=user_id,
                event_type="DOCUMENT_UPLOADED",
                title=f"Document Stored: {doc.title}",
                description=f"Uploaded {doc.category} ({doc.file_name}).",
                entity_type="DocumentVault",
                entity_id=doc.id
            ))
            await db.flush()

        return doc

    @staticmethod
    async def list_documents(
        db: AsyncSession,
        tenant_id: str,
        category: Optional[str] = None,
        employee_id: Optional[str] = None,
        is_public: Optional[bool] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[DocumentVault]:
        query = select(DocumentVault).where(DocumentVault.tenant_id == tenant_id, DocumentVault.is_deleted == False)
        if category:
            query = query.where(DocumentVault.category == category)
        if employee_id:
            query = query.where(
                or_(DocumentVault.target_employee_id == employee_id, DocumentVault.is_public_policy == True)
            )
        elif is_public is not None:
            query = query.where(DocumentVault.is_public_policy == is_public)

        query = query.order_by(desc(DocumentVault.created_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())
