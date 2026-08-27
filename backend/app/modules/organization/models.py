from sqlalchemy import Column, String, ForeignKey, Integer, Float, JSON
from sqlalchemy.orm import relationship, foreign
from app.database.base import TenantBaseModel, BaseModel


class Organization(TenantBaseModel):
    """Top-level company entity within a tenant."""
    __tablename__ = "organizations"

    name = Column(String(255), nullable=False, index=True)
    code = Column(String(50), nullable=False, index=True)
    tax_id = Column(String(100), nullable=True)
    registration_number = Column(String(100), nullable=True)
    website = Column(String(255), nullable=True)
    address = Column(String(500), nullable=True)
    contact_email = Column(String(255), nullable=True)
    contact_phone = Column(String(50), nullable=True)

    # Relationships
    tenant = relationship("Tenant", back_populates="organizations", primaryjoin="foreign(Organization.tenant_id) == Tenant.id")
    branches = relationship("Branch", back_populates="organization", cascade="all, delete-orphan")
    departments = relationship("Department", back_populates="organization", cascade="all, delete-orphan")


class Branch(TenantBaseModel):
    """Company office branch or facility."""
    __tablename__ = "branches"

    organization_id = Column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    code = Column(String(50), nullable=False)
    address = Column(String(500), nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    postal_code = Column(String(50), nullable=True)
    timezone = Column(String(50), default="UTC", nullable=False)

    # Relationships
    organization = relationship("Organization", back_populates="branches")
    departments = relationship("Department", back_populates="branch")
    employees = relationship("Employee", back_populates="branch")


class Department(TenantBaseModel):
    """Department within the organization hierarchy."""
    __tablename__ = "departments"

    organization_id = Column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    branch_id = Column(String(36), ForeignKey("branches.id", ondelete="SET NULL"), nullable=True, index=True)
    parent_department_id = Column(String(36), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True, index=True)
    
    name = Column(String(255), nullable=False)
    code = Column(String(50), nullable=False)
    cost_center = Column(String(100), nullable=True)
    manager_id = Column(String(36), nullable=True)  # Employee ID of Dept Head

    # Relationships
    organization = relationship("Organization", back_populates="departments")
    branch = relationship("Branch", back_populates="departments")
    parent_department = relationship("Department", remote_side="Department.id", backref="sub_departments")
    teams = relationship("Team", back_populates="department", cascade="all, delete-orphan")
    employees = relationship("Employee", back_populates="department")


class Team(TenantBaseModel):
    """Operational team within a department."""
    __tablename__ = "teams"

    department_id = Column(String(36), ForeignKey("departments.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    code = Column(String(50), nullable=True)
    team_lead_id = Column(String(36), nullable=True)  # Employee ID of Team Lead

    # Relationships
    department = relationship("Department", back_populates="teams")
    employees = relationship("Employee", back_populates="team")


class Designation(TenantBaseModel):
    """Job Title / Designation catalog."""
    __tablename__ = "designations"

    title = Column(String(255), nullable=False, index=True)
    code = Column(String(50), nullable=False)
    level = Column(Integer, default=1, nullable=False)
    job_family = Column(String(100), nullable=True)  # e.g., Engineering, Sales, HR
    description = Column(String(1000), nullable=True)

    # Relationships
    employees = relationship("Employee", back_populates="designation")


class JobGrade(TenantBaseModel):
    """Salary Band and Job Grade level."""
    __tablename__ = "job_grades"

    grade_name = Column(String(50), nullable=False)  # e.g., L1, L2, L3, Senior, Executive
    band = Column(String(50), nullable=True)
    min_salary = Column(Float, default=0.0, nullable=False)
    max_salary = Column(Float, default=0.0, nullable=False)
    currency = Column(String(10), default="USD", nullable=False)

    # Relationships
    employees = relationship("Employee", back_populates="job_grade")


class WorkLocation(TenantBaseModel):
    """Physical office or remote work site with geofence bounds."""
    __tablename__ = "work_locations"

    name = Column(String(255), nullable=False)
    address = Column(String(500), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    geofence_radius_meters = Column(Integer, default=200, nullable=False)
    ip_subnet = Column(String(100), nullable=True)
    is_remote = Column(String(20), default="OFFICE", nullable=False)  # OFFICE, REMOTE, HYBRID

    # Relationships
    employees = relationship("Employee", back_populates="work_location")
