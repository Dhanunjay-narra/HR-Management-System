"""
Integration Tests for Goals/OKRs, Skills Intelligence Gap Matrix, and LMS
"""
import pytest
import uuid
from datetime import date, timedelta
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database.connection import init_db, close_db
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_goals_skills_and_learning_lifecycle():
    await init_db()
    
    uid = uuid.uuid4().hex[:6]
    admin_token = create_access_token(
        subject=f"perf_admin_{uid}",
        tenant_id="tenant-test-1",
        role="hr_admin",
        permissions=["*"]
    )
    headers = {"Authorization": f"Bearer {admin_token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 1. Create a Goal with Key Results
        goal_payload = {
            "title": f"Scale Microservice Platform {uid}",
            "level": "DEPARTMENT",
            "target_value": 100.0,
            "current_value": 0.0,
            "deadline": str(date.today() + timedelta(days=90)),
            "key_results": [
                {"title": "Achieve 99.99% API Uptime", "target_value": 99.99, "unit": "PERCENT"},
                {"title": "Reduce Latency to sub 50ms", "target_value": 50.0, "unit": "NUMBER"}
            ]
        }
        res_goal = await client.post("/api/v1/goals", json=goal_payload, headers=headers)
        assert res_goal.status_code == 201
        goal_id = res_goal.json()["id"]

        # 2. Check in Goal Progress
        res_ci = await client.post(
            f"/api/v1/goals/{goal_id}/check-in",
            json={"new_value": 65.0, "confidence_score": 5, "notes": "Caching optimizations deployed"},
            headers=headers
        )
        assert res_ci.status_code == 200
        assert res_ci.json()["progress_percentage"] == 65.0

        # 3. Create Skills Catalog
        res_sk1 = await client.post(
            "/api/v1/skills/catalog",
            json={"name": "Kubernetes Architecture", "code": f"K8S_{uid}", "category": "TECHNICAL"},
            headers=headers
        )
        assert res_sk1.status_code == 201
        k8s_skill_id = res_sk1.json()["id"]

        res_sk2 = await client.post(
            "/api/v1/skills/catalog",
            json={"name": "PostgreSQL Optimization", "code": f"PG_{uid}", "category": "TECHNICAL"},
            headers=headers
        )
        assert res_sk2.status_code == 201
        pg_skill_id = res_sk2.json()["id"]

        # 4. Create Designation and Requirements
        res_desig = await client.post(
            "/api/v1/organization/designations",
            json={"title": f"Staff Infrastructure Engineer {uid}", "code": f"STAFF_INFRA_{uid}", "level": 5},
            headers=headers
        )
        assert res_desig.status_code == 201
        desig_id = res_desig.json()["id"]

        await client.post(
            "/api/v1/skills/requirements",
            json={"designation_id": desig_id, "skill_id": k8s_skill_id, "required_proficiency_level": 4},
            headers=headers
        )
        await client.post(
            "/api/v1/skills/requirements",
            json={"designation_id": desig_id, "skill_id": pg_skill_id, "required_proficiency_level": 5},
            headers=headers
        )

        # 5. Create Employee with Designation
        res_emp = await client.post(
            "/api/v1/employees",
            json={
                "employee_code": f"EMP-SKILL-{uid}",
                "first_name": "Valerie",
                "last_name": "Novak",
                "work_email": f"valerie_{uid}@infra.example.com",
                "designation_id": desig_id,
                "create_user_account": False
            },
            headers=headers
        )
        assert res_emp.status_code == 201
        emp_id = res_emp.json()["id"]

        # 6. Set Employee Skills (K8s level 4, PG level 2 -> gap on PG!)
        await client.post(
            f"/api/v1/skills/employee/{emp_id}",
            json={
                "skills": [
                    {"skill_id": k8s_skill_id, "proficiency_level": 4, "years_of_experience": 3.0},
                    {"skill_id": pg_skill_id, "proficiency_level": 2, "years_of_experience": 1.0},
                ]
            },
            headers=headers
        )

        # 7. Create Course mapped to PostgreSQL
        res_course = await client.post(
            "/api/v1/learning/courses",
            json={
                "title": "Advanced PostgreSQL Indexing & Performance Tuning",
                "code": f"CRS-PG-{uid}",
                "category": "ENGINEERING",
                "description": "Master query plans, indexing strategies, and connection pooling.",
                "duration_hours": 12.0,
                "target_skill_id": pg_skill_id,
                "lessons": [
                    {"title": "Explaining EXPLAIN ANALYZE", "duration_minutes": 30, "order_index": 1}
                ]
            },
            headers=headers
        )
        assert res_course.status_code == 201
        course_id = res_course.json()["id"]

        # 8. Run Automated Skill Gap Analysis
        res_gap = await client.get(f"/api/v1/skills/employee/{emp_id}/gap-analysis", headers=headers)
        assert res_gap.status_code == 200
        gap_data = res_gap.json()
        assert gap_data["overall_readiness_score"] == 50.0  # 1 of 2 requirements met
        assert gap_data["skills_met_count"] == 1
        assert gap_data["skills_gap_count"] == 1
        
        # Check course recommendation on gap
        pg_gap = next(g for g in gap_data["gap_matrix"] if g["skill_id"] == pg_skill_id)
        assert pg_gap["is_met"] is False
        assert pg_gap["recommended_course"] is not None
        assert pg_gap["recommended_course"]["id"] == course_id

        # 9. Enroll in Recommended Course & Complete Progress
        res_enroll = await client.post(
            "/api/v1/learning/enroll",
            json={"course_id": course_id, "employee_id": emp_id},
            headers=headers
        )
        assert res_enroll.status_code == 201
        enrollment_id = res_enroll.json()["id"]

        res_prog = await client.put(
            f"/api/v1/learning/enrollments/{enrollment_id}/progress?progress=100.0",
            headers=headers
        )
        assert res_prog.status_code == 200
        assert res_prog.json()["status"] == "COMPLETED"
        assert res_prog.json()["certificate_url"] is not None

    await close_db()
