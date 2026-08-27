"""
AI Assistant Service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_

from app.modules.ai_assistant.models import KnowledgeChunk
from app.modules.ai_assistant.schemas import KnowledgeChunkCreate, AIChatQuery, AIChatResponse, CitationItem
from app.modules.ai_assistant.rag_engine import PolicyRAGEngine

DEFAULT_ENTERPRISE_POLICIES = [
    {
        "title": "Annual & Sick Leave Policy",
        "category": "LEAVE",
        "keywords": ["leave", "vacation", "sick", "annual", "pto", "holiday", "time off"],
        "content": "All full-time employees are entitled to 20 days of paid Annual Vacation leave per year, plus 10 days of Paid Sick Leave. Up to 5 unused annual leave days can be carried forward to the following calendar year. Leave applications must be submitted via PeoplePulse portal and approved by your direct manager."
    },
    {
        "title": "Remote Work & Hybrid Workplace Guidelines",
        "category": "POLICY",
        "keywords": ["remote", "work from home", "wfh", "hybrid", "flexible", "hours"],
        "content": "Employees may work remotely up to 3 days per week with manager coordination. Core collaboration hours are 10:00 AM to 4:00 PM local time. Remote workers receive a one-time $500 home office ergonomics setup stipend."
    },
    {
        "title": "Health Insurance & Wellness Benefits",
        "category": "BENEFITS",
        "keywords": ["health", "insurance", "medical", "dental", "vision", "doctor", "hospital", "wellness"],
        "content": "Comprehensive health, dental, and vision insurance begins on your first day of employment. Premium coverage is 100% employer-sponsored for employees and 80% for eligible dependents. In addition, employees receive an annual $1,000 gym and wellness subsidy."
    },
    {
        "title": "Expense Claim & Travel Reimbursement Policy",
        "category": "EXPENSES",
        "keywords": ["expense", "claim", "reimbursement", "travel", "flight", "hotel", "meal", "receipt"],
        "content": "All business-related expenses must be submitted within 30 days of occurrence along with itemized receipts. Daily meal per-diem during business travel is capped at $75 per day. Claims under $1,000 require manager approval; claims exceeding $1,000 require finance director sign-off."
    }
]


class AIAssistantService:
    @staticmethod
    async def seed_default_knowledge_if_empty(db: AsyncSession, tenant_id: str) -> None:
        res = await db.execute(select(KnowledgeChunk).where(KnowledgeChunk.tenant_id == tenant_id))
        if not res.scalars().first():
            for p in DEFAULT_ENTERPRISE_POLICIES:
                chunk = KnowledgeChunk(
                    tenant_id=tenant_id,
                    title=p["title"],
                    category=p["category"],
                    keywords=p["keywords"],
                    content=p["content"],
                    chunk_index=0
                )
                db.add(chunk)
            await db.flush()

    @staticmethod
    async def index_knowledge_chunk(db: AsyncSession, tenant_id: str, data: KnowledgeChunkCreate) -> KnowledgeChunk:
        chunk = KnowledgeChunk(tenant_id=tenant_id, **data.model_dump())
        db.add(chunk)
        await db.flush()
        return chunk

    @staticmethod
    async def query_knowledge_assistant(
        db: AsyncSession,
        tenant_id: str,
        data: AIChatQuery
    ) -> AIChatResponse:
        await AIAssistantService.seed_default_knowledge_if_empty(db, tenant_id)

        # Retrieve all tenant chunks
        res = await db.execute(
            select(KnowledgeChunk).where(KnowledgeChunk.tenant_id == tenant_id, KnowledgeChunk.is_deleted == False)
        )
        chunks = list(res.scalars().all())

        query_tokens = PolicyRAGEngine.tokenize(data.query)

        scored_chunks: List[Dict[str, Any]] = []
        for ch in chunks:
            sim = PolicyRAGEngine.compute_similarity(query_tokens, ch.content, ch.keywords or [])
            if sim > 0.1:
                scored_chunks.append({
                    "id": ch.id,
                    "title": ch.title,
                    "category": ch.category,
                    "content": ch.content,
                    "score": sim
                })

        scored_chunks.sort(key=lambda x: x["score"], reverse=True)
        rag_output = PolicyRAGEngine.synthesize_grounded_answer(data.query, scored_chunks)

        suggestions = [
            "How do I apply for annual leave?",
            "What is the remote work stipend amount?",
            "How do I submit an expense reimbursement?"
        ]

        return AIChatResponse(
            query=data.query,
            answer=rag_output["answer"],
            confidence=rag_output["confidence"],
            citations=[
                CitationItem(
                    title=c["title"],
                    category=c["category"],
                    relevance_score=c["relevance_score"],
                    snippet=c["snippet"]
                ) for c in rag_output["citations"]
            ],
            suggested_actions=suggestions
        )
