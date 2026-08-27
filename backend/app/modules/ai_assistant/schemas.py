"""
AI Assistant Schemas
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class KnowledgeChunkCreate(BaseModel):
    title: str = Field(..., min_length=2)
    category: str = "POLICY"
    content: str = Field(..., min_length=10)
    keywords: List[str] = []
    document_id: Optional[str] = None


class KnowledgeChunkResponse(KnowledgeChunkCreate):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AIChatQuery(BaseModel):
    query: str = Field(..., min_length=2)
    conversation_history: List[Dict[str, str]] = []


class CitationItem(BaseModel):
    title: str
    category: str
    relevance_score: float
    snippet: str


class AIChatResponse(BaseModel):
    query: str
    answer: str
    confidence: float
    citations: List[CitationItem] = []
    suggested_actions: List[str] = []
