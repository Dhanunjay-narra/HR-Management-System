"""
AI Knowledge Assistant API Endpoints
"""
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.ai_assistant.schemas import (
    AIChatQuery, AIChatResponse, KnowledgeChunkCreate, KnowledgeChunkResponse
)
from app.modules.ai_assistant.services import AIAssistantService
from app.middleware.auth_deps import get_current_user, require_permission, CurrentUser

router = APIRouter(prefix="/ai/assistant", tags=["AI Knowledge Assistant"])


@router.post("/chat", response_model=AIChatResponse)
async def query_ai_assistant(
    data: AIChatQuery,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("ai.assistant.use")),
):
    """Query AI knowledge assistant for corporate policy, benefits, and HR self-service."""
    return await AIAssistantService.query_knowledge_assistant(
        db, current_user.tenant_id or "default", data
    )


@router.post("/chunks", response_model=KnowledgeChunkResponse, status_code=status.HTTP_201_CREATED)
async def index_knowledge_chunk(
    data: KnowledgeChunkCreate,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_permission("ai.admin")),
):
    """Manually index or embed a policy chunk for knowledge base retrieval."""
    chunk = await AIAssistantService.index_knowledge_chunk(db, current_user.tenant_id or "default", data)
    return chunk
