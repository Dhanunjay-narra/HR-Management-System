"""
Unit & Integration Tests for Foundation, Auth, and RBAC
"""
import pytest
import asyncio
import uuid
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database.connection import init_db, close_db
from app.core.security import verify_password, get_password_hash, create_access_token, decode_token
from app.core.permissions import has_permission, get_permissions_for_role


@pytest.mark.asyncio
async def test_password_hashing():
    pwd = "EnterprisePassword2026!"
    hashed = get_password_hash(pwd)
    assert hashed != pwd
    assert verify_password(pwd, hashed) is True
    assert verify_password("WrongPassword", hashed) is False


@pytest.mark.asyncio
async def test_jwt_token_generation():
    token = create_access_token(
        subject="user-12345",
        tenant_id="tenant-999",
        role="hr_admin",
        permissions=["employee.create", "employee.read"]
    )
    payload = decode_token(token)
    assert payload["sub"] == "user-12345"
    assert payload["tenant_id"] == "tenant-999"
    assert payload["role"] == "hr_admin"
    assert "employee.create" in payload["permissions"]


@pytest.mark.asyncio
async def test_rbac_permission_checker():
    admin_perms = list(get_permissions_for_role("hr_admin"))
    employee_perms = list(get_permissions_for_role("employee"))

    assert has_permission(admin_perms, "employee.create") is True
    assert has_permission(employee_perms, "employee.create") is False
    assert has_permission(employee_perms, "attendance.clock") is True
    assert has_permission(["*"], "anything.arbitrary.action") is True
    assert has_permission(["employee.*"], "employee.delete") is True


@pytest.mark.asyncio
async def test_api_health_and_registration():
    await init_db()
    unique_email = f"admin_{uuid.uuid4().hex[:6]}@peoplepulse.io"
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Healthcheck
        res = await client.get("/health")
        assert res.status_code == 200
        assert res.json()["status"] == "healthy"

        # Register platform admin
        reg_payload = {
            "email": unique_email,
            "password": "SuperSecurePassword123!",
            "first_name": "Alexander",
            "last_name": "Vance",
            "role": "platform_owner"
        }
        res_reg = await client.post("/api/v1/auth/register", json=reg_payload)
        assert res_reg.status_code == 201
        data = res_reg.json()
        assert data["email"] == unique_email
        assert data["full_name"] == "Alexander Vance"

        # Login
        login_payload = {
            "email": unique_email,
            "password": "SuperSecurePassword123!"
        }
        res_login = await client.post("/api/v1/auth/login", json=login_payload)
        assert res_login.status_code == 200
        token_data = res_login.json()
        assert "access_token" in token_data
        assert token_data["role"] == "platform_owner"
        token = token_data["access_token"]

        # Current User Profile (/auth/me)
        res_me = await client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token}"})
        assert res_me.status_code == 200
        me_data = res_me.json()
        assert me_data["email"] == unique_email

    await close_db()
