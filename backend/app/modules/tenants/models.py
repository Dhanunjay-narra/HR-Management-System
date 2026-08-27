from sqlalchemy import Column, String, Boolean, JSON, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship, foreign
from app.database.base import BaseModel


class Tenant(BaseModel):
    """Multi-tenant organization account entity."""
    __tablename__ = "tenants"

    name = Column(String(255), nullable=False, unique=True, index=True)
    slug = Column(String(100), nullable=False, unique=True, index=True)
    domain = Column(String(255), nullable=True, unique=True)
    is_active = Column(Boolean, default=True, nullable=False)
    subscription_plan = Column(String(50), default="enterprise", nullable=False)
    max_employees = Column(Integer, default=500, nullable=False)
    logo_url = Column(String(500), nullable=True)
    primary_color = Column(String(20), default="#4F46E5", nullable=True)
    timezone = Column(String(50), default="UTC", nullable=False)
    currency = Column(String(10), default="USD", nullable=False)
    settings = Column(JSON, default=dict, nullable=False)

    # Relationships with explicit foreign keys / primaryjoin
    users = relationship("User", back_populates="tenant", primaryjoin="Tenant.id == User.tenant_id", cascade="all, delete-orphan")
    organizations = relationship("Organization", back_populates="tenant", primaryjoin="Tenant.id == foreign(Organization.tenant_id)", cascade="all, delete-orphan")
