"""
Enterprise Payroll Processing Models
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Float, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class SalaryStructure(TenantBaseModel):
    """Employee Compensation & Statutory Deductions breakdown."""
    __tablename__ = "salary_structures"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    currency = Column(String(10), default="USD", nullable=False)
    
    # Monthly Earnings
    base_salary = Column(Float, default=0.0, nullable=False)
    house_rent_allowance = Column(Float, default=0.0, nullable=False)
    special_allowance = Column(Float, default=0.0, nullable=False)
    transport_allowance = Column(Float, default=0.0, nullable=False)
    medical_allowance = Column(Float, default=0.0, nullable=False)
    
    # Monthly Statutory & Tax Deductions
    provident_fund_percentage = Column(Float, default=12.0, nullable=False)
    professional_tax = Column(Float, default=0.0, nullable=False)
    income_tax_tds = Column(Float, default=0.0, nullable=False)
    health_insurance_deduction = Column(Float, default=0.0, nullable=False)
    
    effective_from = Column(Date, default=date.today, nullable=False)

    # Relationships
    employee = relationship("Employee")

    @property
    def gross_monthly_salary(self) -> float:
        return (
            self.base_salary
            + self.house_rent_allowance
            + self.special_allowance
            + self.transport_allowance
            + self.medical_allowance
        )

    @property
    def total_monthly_deductions(self) -> float:
        pf = (self.base_salary * (self.provident_fund_percentage / 100.0))
        return pf + self.professional_tax + self.income_tax_tds + self.health_insurance_deduction

    @property
    def net_monthly_salary(self) -> float:
        return self.gross_monthly_salary - self.total_monthly_deductions


class PayrollRun(TenantBaseModel):
    """Monthly Payroll Processing Execution."""
    __tablename__ = "payroll_runs"

    month = Column(Integer, nullable=False, index=True)  # 1 to 12
    year = Column(Integer, nullable=False, index=True)
    pay_period_start = Column(Date, nullable=False)
    pay_period_end = Column(Date, nullable=False)
    
    status = Column(String(50), default="DRAFT", nullable=False, index=True)  # DRAFT, PROCESSING, APPROVED, PAID
    total_employees_count = Column(Integer, default=0, nullable=False)
    total_gross_payout = Column(Float, default=0.0, nullable=False)
    total_deductions = Column(Float, default=0.0, nullable=False)
    total_net_payout = Column(Float, default=0.0, nullable=False)
    
    approved_by_user_id = Column(String(36), nullable=True)
    paid_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    payslips = relationship("Payslip", back_populates="payroll_run", cascade="all, delete-orphan")


class Payslip(TenantBaseModel):
    """Individual Employee Monthly Payslip."""
    __tablename__ = "payslips"

    payroll_run_id = Column(String(36), ForeignKey("payroll_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    working_days = Column(Float, default=22.0, nullable=False)
    paid_days = Column(Float, default=22.0, nullable=False)
    
    gross_earnings = Column(Float, nullable=False)
    total_deductions = Column(Float, nullable=False)
    net_pay = Column(Float, nullable=False)
    
    earnings_breakdown = Column(JSON, default=dict, nullable=False)
    deductions_breakdown = Column(JSON, default=dict, nullable=False)
    status = Column(String(50), default="GENERATED", nullable=False)  # GENERATED, PUBLISHED, PAID

    # Relationships
    payroll_run = relationship("PayrollRun", back_populates="payslips")
    employee = relationship("Employee")
