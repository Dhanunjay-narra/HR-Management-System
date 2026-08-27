"""
Integration Tests for Recruitment CRM and Onboarding Journey
"""
import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database.connection import init_db, close_db
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_recruitment_to_onboarding_lifecycle():
    await init_db()
    
    uid = uuid.uuid4().hex[:6]
    admin_token = create_access_token(
        subject=f"recruiter_{uid}",
        tenant_id="tenant-test-1",
        role="hr_admin",
        permissions=["*"]
    )
    headers = {"Authorization": f"Bearer {admin_token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 1. Create Job Opening Requisition
        job_payload = {
            "title": "Senior Distributed Systems Engineer",
            "code": f"REQ-{uid}",
            "positions_count": 2,
            "min_experience_years": 4.0,
            "max_experience_years": 8.0,
            "required_skills": ["Python", "FastAPI", "Kubernetes", "PostgreSQL", "Docker"],
            "job_description": "We are seeking a senior backend engineer to architect distributed multi-tenant services.",
            "salary_min": 130000.0,
            "salary_max": 180000.0,
            "status": "OPEN"
        }
        res_job = await client.post("/api/v1/recruitment/jobs", json=job_payload, headers=headers)
        assert res_job.status_code == 201
        job_id = res_job.json()["id"]

        # 2. Add Candidate with Raw Resume Text
        candidate_payload = {
            "job_requisition_id": job_id,
            "first_name": "Marcus",
            "last_name": "Aurelius",
            "email": f"marcus_{uid}@talent.example.com",
            "phone_number": "+1-415-555-0199",
            "current_company": "CloudScale Inc",
            "experience_years": 5.5,
            "raw_resume_text": """
                Senior Software Engineer with 5+ years of experience building high throughput APIs using Python, FastAPI, Docker, and Kubernetes.
                Extensive database design with PostgreSQL, Redis caching, and microservices CI/CD.
            """,
            "pipeline_stage": "APPLIED"
        }
        res_cand = await client.post("/api/v1/recruitment/candidates", json=candidate_payload, headers=headers)
        assert res_cand.status_code == 201
        cand_data = res_cand.json()
        cand_id = cand_data["id"]
        
        # Verify AI Match Scoring & Skill Extraction
        assert "Python" in cand_data["extracted_skills"]
        assert "Fastapi" in cand_data["extracted_skills"] or "FASTAPI" in cand_data["extracted_skills"]
        assert cand_data["match_score"] >= 80.0

        # 3. Advance Candidate to TECH_INTERVIEW
        res_stage = await client.put(
            f"/api/v1/recruitment/candidates/{cand_id}/stage",
            json={"pipeline_stage": "TECH_INTERVIEW", "notes": "Impressive resume match, advancing to tech round."},
            headers=headers
        )
        assert res_stage.status_code == 200
        assert res_stage.json()["pipeline_stage"] == "TECH_INTERVIEW"

        # 4. Create Employee from candidate and launch Onboarding
        emp_payload = {
            "employee_code": f"EMP-HIRE-{uid}",
            "first_name": "Marcus",
            "last_name": "Aurelius",
            "work_email": f"marcus_{uid}@company.example.com",
            "employment_type": "FULL_TIME",
            "status": "ACTIVE",
            "create_user_account": True,
            "user_role": "employee"
        }
        res_emp = await client.post("/api/v1/employees", json=emp_payload, headers=headers)
        assert res_emp.status_code == 201
        emp_id = res_emp.json()["id"]

        # 5. Launch Onboarding Workflow
        onboarding_payload = {
            "employee_id": emp_id,
            "template_name": "Senior Engineering Onboarding",
            "target_completion_days": 30
        }
        res_onboard = await client.post("/api/v1/onboarding/workflows", json=onboarding_payload, headers=headers)
        assert res_onboard.status_code == 201
        ob_data = res_onboard.json()
        assert len(ob_data["tasks"]) >= 4
        assert ob_data["status"] == "IN_PROGRESS"

        # 6. Complete a task
        first_task_id = ob_data["tasks"][0]["id"]
        res_task = await client.post(f"/api/v1/onboarding/tasks/{first_task_id}/complete", headers=headers)
        assert res_task.status_code == 200
        assert res_task.json()["is_completed"] is True

    await close_db()
