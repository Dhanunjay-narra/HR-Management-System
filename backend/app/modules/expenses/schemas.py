"""
Expense Schemas
"""
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class ExpenseCategoryCreate(BaseModel):
    name: str
    code: str
    max_limit: float = 1000.0
    requires_receipt: bool = True
    description: Optional[str] = None


class ExpenseCategoryResponse(ExpenseCategoryCreate):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ExpenseClaimCreate(BaseModel):
    category_id: Optional[str] = None
    expense_date: date = Field(default_factory=date.today)
    amount: float = Field(..., gt=0.0)
    currency: str = "USD"
    merchant_name: str
    description: str
    receipt_url: Optional[str] = None


class ExpenseClaimResponse(ExpenseClaimCreate):
    id: str
    tenant_id: str
    claim_number: str
    employee_id: str
    employee_name: Optional[str] = None
    category_name: Optional[str] = None
    status: str
    approver_id: Optional[str] = None
    rejection_reason: Optional[str] = None
    reimbursed_at: Optional[datetime] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
