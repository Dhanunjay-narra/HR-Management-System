"""
Employee Master & Relationship Models
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Boolean, ForeignKey, Integer, Float, JSON
from sqlalchemy.orm import relationship as sa_relationship
from app.database.base import TenantBaseModel


class Employee(TenantBaseModel):
    """Core Employee Record (Single Source of Truth across all sub-modules)."""
    __tablename__ = "employees"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=True, unique=True, index=True)
    employee_code = Column(String(50), nullable=False, unique=True, index=True)  # e.g., EMP-00102
    
    # Personal info
    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    work_email = Column(String(255), nullable=False, unique=True, index=True)
    personal_email = Column(String(255), nullable=True)
    phone_number = Column(String(50), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String(20), nullable=True)  # Male, Female, Non-Binary, Other, PreferNotToSay
    marital_status = Column(String(20), nullable=True)  # Single, Married, Divorced, Widowed
    national_id = Column(String(100), nullable=True)
    avatar_url = Column(String(500), nullable=True)
    bio = Column(String(1000), nullable=True)

    # Employment details
    joining_date = Column(Date, nullable=False, default=date.today)
    probation_end_date = Column(Date, nullable=True)
    confirmation_date = Column(Date, nullable=True)
    exit_date = Column(Date, nullable=True)
    employment_type = Column(String(50), default="FULL_TIME", nullable=False)  # FULL_TIME, PART_TIME, CONTRACTOR, INTERN
    status = Column(String(50), default="ACTIVE", nullable=False, index=True)  # ACTIVE, PROBATION, ON_LEAVE, NOTICE_PERIOD, TERMINATED, RESIGNED

    # Organizational placement
    department_id = Column(String(36), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True, index=True)
    team_id = Column(String(36), ForeignKey("teams.id", ondelete="SET NULL"), nullable=True, index=True)
    designation_id = Column(String(36), ForeignKey("designations.id", ondelete="SET NULL"), nullable=True, index=True)
    branch_id = Column(String(36), ForeignKey("branches.id", ondelete="SET NULL"), nullable=True, index=True)
    work_location_id = Column(String(36), ForeignKey("work_locations.id", ondelete="SET NULL"), nullable=True, index=True)
    job_grade_id = Column(String(36), ForeignKey("job_grades.id", ondelete="SET NULL"), nullable=True, index=True)
    manager_id = Column(String(36), ForeignKey("employees.id", ondelete="SET NULL"), nullable=True, index=True)

    # Relationships
    user = sa_relationship("User", back_populates="employee")
    department = sa_relationship("Department", back_populates="employees")
    team = sa_relationship("Team", back_populates="employees")
    designation = sa_relationship("Designation", back_populates="employees")
    branch = sa_relationship("Branch", back_populates="employees")
    work_location = sa_relationship("WorkLocation", back_populates="employees")
    job_grade = sa_relationship("JobGrade", back_populates="employees")
    
    # Manager & Direct Reports
    manager = sa_relationship("Employee", remote_side="Employee.id", backref="direct_reports")
    
    # Nested Detail Relationships
    emergency_contacts = sa_relationship("EmergencyContact", back_populates="employee", cascade="all, delete-orphan")
    employment_history = sa_relationship("EmploymentHistory", back_populates="employee", cascade="all, delete-orphan")
    bank_details = sa_relationship("EmployeeBankDetail", back_populates="employee", uselist=False, cascade="all, delete-orphan")
    timeline_events = sa_relationship("EmployeeTimelineEvent", back_populates="employee", cascade="all, delete-orphan")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()


class EmergencyContact(TenantBaseModel):
    """Employee emergency contact details."""
    __tablename__ = "emergency_contacts"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    contact_relationship = Column("relationship", String(100), nullable=False)  # Spouse, Parent, Sibling, Friend
    phone_number = Column(String(50), nullable=False)
    alternative_phone = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True)
    is_primary = Column(Boolean, default=True, nullable=False)

    # Relationships
    employee = sa_relationship("Employee", back_populates="emergency_contacts")


class EmploymentHistory(TenantBaseModel):
    """Previous employment record."""
    __tablename__ = "employment_history"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    company_name = Column(String(255), nullable=False)
    designation = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    reason_for_leaving = Column(String(500), nullable=True)
    last_drawn_salary = Column(Float, nullable=True)

    # Relationships
    employee = sa_relationship("Employee", back_populates="employment_history")


class EmployeeBankDetail(TenantBaseModel):
    """Bank account and tax identifiers for payroll."""
    __tablename__ = "employee_bank_details"

    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    bank_name = Column(String(255), nullable=False)
    account_number = Column(String(100), nullable=False)
    routing_number = Column(String(100), nullable=True)
    swift_code = Column(String(50), nullable=True)
    account_type = Column(String(50), default="CHECKING", nullable=False)  # CHECKING, SAVINGS
    tax_identification_number = Column(String(100), nullable=True)

    # Relationships
    employee = sa_relationship("Employee", back_populates="bank_details")
