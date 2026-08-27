"""
Integration Tests for Attendance and Leave Management
"""
import pytest
import uuid
from datetime import date, timedelta
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database.connection import init_db, close_db
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_attendance_and_leave_workflow():
    await init_db()
    
    unique_user = f"emp_{uuid.uuid4().hex[:6]}"
    admin_token = create_access_token(
        subject=unique_user,
        tenant_id="tenant-test-1",
        role="hr_admin",
        permissions=["*"]
    )
    headers = {"Authorization": f"Bearer {admin_token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 1. Clock In
        clock_in_res = await client.post(
            "/api/v1/attendance/clock-in",
            json={"notes": "Working from office hub", "latitude": 37.7749, "longitude": -122.4194},
            headers=headers
        )
        assert clock_in_res.status_code == 200
        rec_data = clock_in_res.json()
        assert rec_data["status"] == "PRESENT"

        # 2. Check today's status
        status_res = await client.get("/api/v1/attendance/today", headers=headers)
        assert status_res.status_code == 200
        assert status_res.json()["clock_in_time"] is not None

        # 3. Clock Out
        clock_out_res = await client.post(
            "/api/v1/attendance/clock-out",
            json={"notes": "Day completed"},
            headers=headers
        )
        assert clock_out_res.status_code == 200
        assert clock_out_res.json()["clock_out_time"] is not None

        # 4. Create Leave Type
        code_uid = uuid.uuid4().hex[:4]
        lt_payload = {
            "name": f"Annual Vacation {code_uid}",
            "code": f"ANNUAL_{code_uid}",
            "annual_allowance_days": 20.0,
            "is_paid": True
        }
        res_lt = await client.post("/api/v1/leave/types", json=lt_payload, headers=headers)
        assert res_lt.status_code == 201
        lt_id = res_lt.json()["id"]

        # 5. Apply for Leave
        today = date.today()
        leave_payload = {
            "leave_type_id": lt_id,
            "start_date": str(today + timedelta(days=5)),
            "end_date": str(today + timedelta(days=7)),
            "reason": "Family vacation",
            "is_half_day": False
        }
        res_apply = await client.post("/api/v1/leave/apply", json=leave_payload, headers=headers)
        assert res_apply.status_code == 201
        req_id = res_apply.json()["id"]
        assert res_apply.json()["status"] == "PENDING"
        assert res_apply.json()["total_days"] == 3.0

        # 6. Approve Leave Request
        res_review = await client.post(
            f"/api/v1/leave/requests/{req_id}/review",
            json={"status": "APPROVED", "comments": "Approved. Have a great vacation!"},
            headers=headers
        )
        assert res_review.status_code == 200
        assert res_review.json()["status"] == "APPROVED"

    await close_db()
