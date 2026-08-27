"""
Integration Tests for Organization, Employee Master, and Employee 360 CRM
"""
import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database.connection import init_db, close_db
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_organization_and_employee_360_lifecycle():
    await init_db()
    
    # Generate admin token
    admin_token = create_access_token(
        subject="admin-user-id",
        tenant_id="tenant-test-1",
        role="hr_admin",
        permissions=["*"]
    )
    headers = {"Authorization": f"Bearer {admin_token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 1. Create Organization Profile
        org_payload = {
            "name": "Acme Global Technologies",
            "code": "ACME",
            "website": "https://acme.example.com",
            "contact_email": "hr@acme.example.com"
        }
        res_org = await client.post("/api/v1/organization", json=org_payload, headers=headers)
        assert res_org.status_code == 201
        org_data = res_org.json()
        org_id = org_data["id"]

        # 2. Create Department
        dept_payload = {
            "name": "Core Platform Engineering",
            "code": "ENG-PLAT",
            "organization_id": org_id,
        }
        res_dept = await client.post("/api/v1/organization/departments", json=dept_payload, headers=headers)
        assert res_dept.status_code == 201
        dept_id = res_dept.json()["id"]

        # 3. Create Designation
        desig_payload = {
            "title": "Principal AI Systems Architect",
            "code": "ARCH-L6",
            "level": 6,
            "job_family": "Engineering"
        }
        res_desig = await client.post("/api/v1/organization/designations", json=desig_payload, headers=headers)
        assert res_desig.status_code == 201
        desig_id = res_desig.json()["id"]

        # 4. Create Employee Master Record
        uid = uuid.uuid4().hex[:6]
        emp_payload = {
            "employee_code": f"EMP-{uid}",
            "first_name": "Elena",
            "last_name": "Rostova",
            "work_email": f"elena_{uid}@acme.example.com",
            "department_id": dept_id,
            "designation_id": desig_id,
            "employment_type": "FULL_TIME",
            "status": "ACTIVE",
            "create_user_account": True,
            "user_role": "employee"
        }
        res_emp = await client.post("/api/v1/employees", json=emp_payload, headers=headers)
        assert res_emp.status_code == 201
        emp_data = res_emp.json()
        emp_id = emp_data["id"]
        assert emp_data["full_name"] == "Elena Rostova"
        assert emp_data["department_name"] == "Core Platform Engineering"

        # 5. Fetch Employee 360 Profile
        res_360 = await client.get(f"/api/v1/employees/{emp_id}/360", headers=headers)
        assert res_360.status_code == 200
        data_360 = res_360.json()
        assert data_360["employee_code"].startswith("EMP-")
        assert len(data_360["recent_timeline"]) >= 1
        assert data_360["recent_timeline"][0]["event_type"] == "JOINED"

        # 6. Fetch Employee Timeline
        res_timeline = await client.get(f"/api/v1/employees/{emp_id}/timeline", headers=headers)
        assert res_timeline.status_code == 200
        events = res_timeline.json()
        assert len(events) >= 1
        assert "joined as FULL_TIME" in events[0]["description"]

    await close_db()
