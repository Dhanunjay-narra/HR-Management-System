"""
Document API Endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.documents.schemas import DocumentVaultCreate, DocumentVaultResponse
from app.modules.documents.services import DocumentService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/documents", tags=["Document Vault"])


@router.get("", response_model=List[DocumentVaultResponse])
async def list_documents(
    category: Optional[str] = Query(None),
    is_public: Optional[bool] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    """List documents and company policy handbooks."""
    emp_id = None if (current_user.is_superuser or "document.view_all" in current_user.permissions) else current_user.id
    return await DocumentService.list_documents(
        db, current_user.tenant_id or "default", category=category, employee_id=emp_id, is_public=is_public, skip=skip, limit=limit
    )


@router.post("", response_model=DocumentVaultResponse, status_code=status.HTTP_201_CREATED)
async def upload_document(
    data: DocumentVaultCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("document.manage")),
):
    """Upload policy or employee document record."""
    return await DocumentService.upload_document(
        db, current_user.tenant_id or "default", current_user.id, data
    )
