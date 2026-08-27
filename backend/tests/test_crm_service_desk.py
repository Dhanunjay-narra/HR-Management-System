"""
Integration Tests for HR Service Desk CRM, Peer Kudos, and Announcements
"""
import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database.connection import init_db, close_db
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_service_desk_and_engagement_crm():
    await init_db()
    
    uid = uuid.uuid4().hex[:6]
    admin_token = create_access_token(
        subject=f"crm_admin_{uid}",
        tenant_id="tenant-test-1",
        role="hr_admin",
        permissions=["*"]
    )
    headers = {"Authorization": f"Bearer {admin_token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 1. Create Service Desk Category
        cat_payload = {
            "name": f"Payroll & Benefits Queue {uid}",
            "code": f"PAYROLL_Q_{uid}",
            "default_priority": "HIGH",
            "sla_response_hours": 12,
            "sla_resolution_hours": 48
        }
        res_cat = await client.post("/api/v1/service-desk/categories", json=cat_payload, headers=headers)
        assert res_cat.status_code == 201
        cat_id = res_cat.json()["id"]

        # 2. Submit HR Ticket
        ticket_payload = {
            "category_id": cat_id,
            "subject": "Tax Deduction Query on Q3 Payslip",
            "description": "Please review federal withholding breakdown on my latest salary pay run.",
            "priority": "HIGH"
        }
        res_tkt = await client.post("/api/v1/service-desk/tickets", json=ticket_payload, headers=headers)
        assert res_tkt.status_code == 201
        tkt_data = res_tkt.json()
        tkt_id = tkt_data["id"]
        assert tkt_data["ticket_number"].startswith("TKT-")
        assert tkt_data["status"] == "OPEN"

        # 3. Add Reply Comment
        comment_payload = {
            "comment_text": "We have verified your tax bracket calculations and updated your withholding record.",
            "is_internal_note": False
        }
        res_comment = await client.post(
            f"/api/v1/service-desk/tickets/{tkt_id}/comments",
            json=comment_payload,
            headers=headers
        )
        assert res_comment.status_code == 201

        # 4. Resolve Ticket
        res_res = await client.put(
            f"/api/v1/service-desk/tickets/{tkt_id}/status",
            json={"status": "RESOLVED", "resolution_summary": "Withholding tax adjusted."},
            headers=headers
        )
        assert res_res.status_code == 200
        assert res_res.json()["status"] == "RESOLVED"

        # 5. Create 2 test employees for Kudos
        res_e1 = await client.post(
            "/api/v1/employees",
            json={
                "employee_code": f"EMP-KD1-{uid}",
                "first_name": "Siddharth",
                "last_name": "Sharma",
                "work_email": f"sid_{uid}@kudos.example.com",
                "create_user_account": False
            },
            headers=headers
        )
        e1_id = res_e1.json()["id"]

        res_e2 = await client.post(
            "/api/v1/employees",
            json={
                "employee_code": f"EMP-KD2-{uid}",
                "first_name": "Amina",
                "last_name": "Al-Mansoor",
                "work_email": f"amina_{uid}@kudos.example.com",
                "create_user_account": False
            },
            headers=headers
        )
        e2_id = res_e2.json()["id"]

        # 6. Send Peer Recognition Kudos
        kudos_payload = {
            "receiver_employee_id": e2_id,
            "badge_type": "INNOVATION",
            "message": "Incredible work architecting the high-availability failover cluster!",
            "is_public": True
        }
        res_kd = await client.post("/api/v1/engagement/kudos", json=kudos_payload, headers=headers)
        assert res_kd.status_code == 201
        assert res_kd.json()["badge_type"] == "INNOVATION"

        # 7. Check Kudos Wall
        res_wall = await client.get("/api/v1/engagement/kudos/wall", headers=headers)
        assert res_wall.status_code == 200
        wall = res_wall.json()
        assert len(wall) >= 1

        # 8. Post Company Announcement
        ann_payload = {
            "title": f"Annual Innovation Summit 2026 {uid}",
            "content": "Join our virtual keynotes and team workshops this Friday.",
            "priority": "NORMAL",
            "is_pinned": True
        }
        res_ann = await client.post("/api/v1/communication/announcements", json=ann_payload, headers=headers)
        assert res_ann.status_code == 201
        assert res_ann.json()["is_pinned"] is True

    await close_db()
