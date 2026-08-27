"""
Integration Tests for Analytics KPIs, Policy RAG AI Assistant, and AI Document Parser
"""
import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database.connection import init_db, close_db
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_analytics_and_ai_services():
    await init_db()
    
    uid = uuid.uuid4().hex[:6]
    admin_token = create_access_token(
        subject=f"ai_admin_{uid}",
        tenant_id="tenant-test-1",
        role="hr_admin",
        permissions=["*"]
    )
    headers = {"Authorization": f"Bearer {admin_token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 1. Query Workforce Analytics Overview
        res_an = await client.get("/api/v1/analytics/overview", headers=headers)
        assert res_an.status_code == 200
        an_data = res_an.json()
        assert "headcount" in an_data
        assert "department_distribution" in an_data
        assert an_data["average_attendance_rate"] > 0

        # 2. Query AI Knowledge Assistant on Leave Policy
        chat_payload = {
            "query": "How many days of paid vacation and sick leave do I get?",
            "conversation_history": []
        }
        res_ai = await client.post("/api/v1/ai/assistant/chat", json=chat_payload, headers=headers)
        assert res_ai.status_code == 200
        ai_data = res_ai.json()
        assert "20 days" in ai_data["answer"] or "Annual" in ai_data["answer"]
        assert len(ai_data["citations"]) >= 1
        assert ai_data["confidence"] > 0.0

        # 3. Query AI Knowledge Assistant on Remote Work
        res_ai2 = await client.post(
            "/api/v1/ai/assistant/chat",
            json={"query": "What is our policy for remote work and home office stipend?", "conversation_history": []},
            headers=headers
        )
        assert res_ai2.status_code == 200
        ai2_data = res_ai2.json()
        assert "$500" in ai2_data["answer"] or "remote" in ai2_data["answer"].lower()

        # 4. Parse Resume with AI Document Parser
        cv_text = """
        Dhanunjay Narra
        Email: dhanunjay@example.com | Phone: (555) 234-5678
        Professional Summary:
        Experienced Software Architect with 6+ years building microservices with Python, FastAPI, Docker, Kubernetes, PostgreSQL, and React.
        """
        res_cv = await client.post(
            "/api/v1/ai/documents/parse-resume",
            json={"raw_text": cv_text},
            headers=headers
        )
        assert res_cv.status_code == 200
        cv_data = res_cv.json()
        assert cv_data["email"] == "dhanunjay@example.com"
        assert "Python" in cv_data["extracted_skills"]
        assert "Kubernetes" in cv_data["extracted_skills"]

        # 5. Parse Expense Receipt with OCR parser
        receipt_text = """
        Office Depot #412
        Date: 2026-08-20
        Ergonomic Keyboard & Mouse combo - $129.99
        Total: $129.99
        USD
        """
        res_rc = await client.post(
            "/api/v1/ai/documents/parse-receipt",
            json={"receipt_raw_text": receipt_text},
            headers=headers
        )
        assert res_rc.status_code == 200
        rc_data = res_rc.json()
        assert rc_data["total_amount"] == 129.99

    await close_db()
