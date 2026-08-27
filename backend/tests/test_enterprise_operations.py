"""
Integration Tests for Enterprise Operations: Workflows, Approvals, Payroll, Expenses, Assets, Documents
"""
import pytest
import uuid
from datetime import date, timedelta
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database.connection import init_db, close_db
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_enterprise_operations_and_payroll():
    await init_db()
    
    uid = uuid.uuid4().hex[:6]
    admin_token = create_access_token(
        subject=f"ops_admin_{uid}",
        tenant_id="tenant-test-1",
        role="hr_admin",
        permissions=["*"]
    )
    headers = {"Authorization": f"Bearer {admin_token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 1. Create Workflow Definition
        wf_payload = {
            "name": f"New Hire IT Hardware Provisioning {uid}",
            "trigger_event": "employee.joined",
            "conditions": {},
            "actions": [
                {"type": "create_asset_ticket", "category": "LAPTOP"},
                {"type": "send_welcome_email"}
            ]
        }
        res_wf = await client.post("/api/v1/workflows", json=wf_payload, headers=headers)
        assert res_wf.status_code == 201
        assert res_wf.json()["trigger_event"] == "employee.joined"

        # 2. Create Multi-Step Approval Chain
        chain_payload = {
            "name": f"Executive Expense Approval Chain {uid}",
            "module_name": "EXPENSE",
            "steps": [
                {"step": 1, "role": "dept_manager", "description": "Manager Review"},
                {"step": 2, "role": "finance_admin", "description": "Finance Disbursement"}
            ]
        }
        res_chain = await client.post("/api/v1/approvals/chains", json=chain_payload, headers=headers)
        assert res_chain.status_code == 201
        chain_id = res_chain.json()["id"]

        # 3. Create Employee
        res_emp = await client.post(
            "/api/v1/employees",
            json={
                "employee_code": f"EMP-PAY-{uid}",
                "first_name": "Gabriel",
                "last_name": "Stone",
                "work_email": f"gabriel_{uid}@enterprise.example.com",
                "create_user_account": False
            },
            headers=headers
        )
        assert res_emp.status_code == 201
        emp_id = res_emp.json()["id"]

        # 4. Configure Salary Structure
        sal_payload = {
            "employee_id": emp_id,
            "base_salary": 10000.0,
            "house_rent_allowance": 3000.0,
            "special_allowance": 2000.0,
            "transport_allowance": 500.0,
            "medical_allowance": 500.0,
            "provident_fund_percentage": 10.0,
            "professional_tax": 200.0,
            "income_tax_tds": 1500.0,
            "health_insurance_deduction": 300.0
        }
        res_sal = await client.post("/api/v1/payroll/salary-structure", json=sal_payload, headers=headers)
        assert res_sal.status_code == 200
        sal_data = res_sal.json()
        assert sal_data["gross_monthly_salary"] == 16000.0
        assert sal_data["net_monthly_salary"] == 13000.0  # 16000 - (1000 + 200 + 1500 + 300) = 13000

        # 5. Execute Monthly Payroll Run
        today = date.today()
        run_payload = {
            "month": today.month,
            "year": today.year,
            "pay_period_start": str(today.replace(day=1)),
            "pay_period_end": str(today)
        }
        res_run = await client.post("/api/v1/payroll/process", json=run_payload, headers=headers)
        assert res_run.status_code == 201
        run_data = res_run.json()
        assert run_data["status"] == "APPROVED"
        assert run_data["total_net_payout"] >= 13000.0

        # 6. Submit Expense Claim and Approval Action
        claim_payload = {
            "amount": 450.0,
            "currency": "USD",
            "merchant_name": "AWS Cloud Services",
            "description": "Dev environment server hosting",
            "expense_date": str(today)
        }
        res_claim = await client.post("/api/v1/expenses/claims", json=claim_payload, headers=headers)
        assert res_claim.status_code == 201
        claim_id = res_claim.json()["id"]

        # Approve and Reimburse Expense
        res_app_claim = await client.put(
            f"/api/v1/expenses/claims/{claim_id}/review?action_status=REIMBURSED",
            headers=headers
        )
        assert res_app_claim.status_code == 200
        assert res_app_claim.json()["status"] == "REIMBURSED"

        # 7. Create and Assign IT Asset
        asset_payload = {
            "asset_tag": f"AST-M3MAX-{uid}",
            "name": "Apple MacBook Pro 16 M3 Max",
            "category": "LAPTOP",
            "serial_number": f"C02{uid.upper()}123",
            "purchase_cost": 3499.0
        }
        res_asset = await client.post("/api/v1/assets", json=asset_payload, headers=headers)
        assert res_asset.status_code == 201
        asset_id = res_asset.json()["id"]

        res_assign = await client.post(
            f"/api/v1/assets/{asset_id}/assign",
            json={"employee_id": emp_id, "condition": "BRAND_NEW"},
            headers=headers
        )
        assert res_assign.status_code == 200
        assert res_assign.json()["status"] == "ASSIGNED"

        # 8. Upload Policy Document into Vault
        doc_payload = {
            "title": "Global Information Security Policy 2026",
            "category": "POLICY",
            "document_url": "https://storage.example.com/policies/sec-2026.pdf",
            "file_name": "sec-2026.pdf",
            "file_size_kb": 1240,
            "is_public_policy": True
        }
        res_doc = await client.post("/api/v1/documents", json=doc_payload, headers=headers)
        assert res_doc.status_code == 201
        assert res_doc.json()["is_public_policy"] is True

    await close_db()
