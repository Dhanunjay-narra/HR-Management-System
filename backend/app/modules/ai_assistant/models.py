"""
AI Knowledge Assistant & Document Embedding Models
"""
from sqlalchemy import Column, String, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class KnowledgeChunk(TenantBaseModel):
    """Vectorized / semantic document chunk for policy RAG retrieval."""
    __tablename__ = "knowledge_chunks"

    document_id = Column(String(36), ForeignKey("document_vault.id", ondelete="CASCADE"), nullable=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    category = Column(String(50), default="POLICY", nullable=False)  # POLICY, HANDBOOK, FAQ, PROCESS
    content = Column(Text, nullable=False)
    keywords = Column(JSON, default=list, nullable=False)
    chunk_index = Column(Integer, default=0, nullable=False)

    # Relationships
    document = relationship("DocumentVault")
