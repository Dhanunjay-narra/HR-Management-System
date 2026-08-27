"""
AI Knowledge Assistant & Policy RAG Engine
Provides semantic retrieval and grounded answer synthesis for employee policy queries.
"""
import re
import math
from typing import List, Dict, Any, Tuple


class PolicyRAGEngine:
    @staticmethod
    def tokenize(text: str) -> List[str]:
        """Normalize and tokenize text into distinct words."""
        cleaned = re.sub(r"[^\w\s]", " ", text.lower())
        return [w for w in cleaned.split() if len(w) > 2]

    @staticmethod
    def compute_similarity(query_tokens: List[str], chunk_text: str, chunk_keywords: List[str]) -> float:
        """
        Compute hybrid BM25 / keyword relevance score between user query and knowledge chunk.
        """
        chunk_tokens = PolicyRAGEngine.tokenize(chunk_text)
        if not chunk_tokens:
            return 0.0

        chunk_set = set(chunk_tokens)
        kw_set = {k.lower() for k in chunk_keywords}

        score = 0.0
        for token in query_tokens:
            if token in chunk_set:
                score += 1.5
            if token in kw_set:
                score += 3.0  # Extra weight on explicit keywords

        # Normalize score
        normalized = round(min(1.0, score / max(1.0, len(query_tokens) * 2.0)), 3)
        return normalized

    @staticmethod
    def synthesize_grounded_answer(query: str, retrieved_chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Synthesize answer and cite retrieved source chunks.
        """
        if not retrieved_chunks:
            return {
                "answer": "I could not locate specific company policy documentation answering your question. Please open an HR Service Desk ticket for personalized guidance.",
                "confidence": 0.2,
                "citations": []
            }

        top_chunk = retrieved_chunks[0]
        citations = [
            {
                "title": c["title"],
                "category": c["category"],
                "relevance_score": c["score"],
                "snippet": c["content"][:200] + "..."
            } for c in retrieved_chunks[:3]
        ]

        synthesized = (
            f"Based on **{top_chunk['title']}**:\n\n"
            f"{top_chunk['content']}\n\n"
            f"*(Reference: {top_chunk['title']}, Category: {top_chunk['category']})*"
        )

        return {
            "answer": synthesized,
            "confidence": top_chunk["score"],
            "citations": citations
        }
