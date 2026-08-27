"""
SQLAlchemy Base & Declarative Mixins
Provides UUID primary keys, audit timestamps, soft-delete, and multi-tenant scoping.
"""
import uuid
from datetime import datetime, timezone
from typing import Any, Dict
from sqlalchemy import Column, String, DateTime, Boolean, Index
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    """Declarative Base Class for all HR Management System ORM entities."""
    pass


class PrimaryKeyMixin:
    """Provides a standard UUID string primary key."""
    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True,
        nullable=False,
    )


class TimestampMixin:
    """Provides created_at and updated_at UTC timestamps."""
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


class SoftDeleteMixin:
    """Provides soft-delete capability with deletion timestamp."""
    is_deleted = Column(Boolean, default=False, nullable=False, index=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def soft_delete(self) -> None:
        self.is_deleted = True
        self.deleted_at = datetime.now(timezone.utc)


class TenantMixin:
    """Enforces multi-tenant data isolation."""
    @declared_attr
    def tenant_id(cls):
        return Column(String(36), nullable=False, index=True)


class BaseModel(Base, PrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    """
    Standard base model for non-tenant entities (e.g., Tenants, Platform Users).
    """
    __abstract__ = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert ORM instance attributes to dictionary."""
        return {
            c.name: getattr(self, c.name)
            for c in self.__table__.columns
        }


class TenantBaseModel(Base, PrimaryKeyMixin, TimestampMixin, SoftDeleteMixin, TenantMixin):
    """
    Standard base model for all tenant-scoped entities.
    Every record automatically includes UUID, timestamps, soft-delete, and tenant_id.
    """
    __abstract__ = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            c.name: getattr(self, c.name)
            for c in self.__table__.columns
        }


# Register all domain models for SQLAlchemy relationships
try:
    import app.modules.tenants.models  # noqa
    import app.modules.auth.models  # noqa
    import app.modules.organization.models  # noqa
    import app.modules.employees.models  # noqa
    import app.modules.employee_360.models  # noqa
    import app.modules.attendance.models  # noqa
    import app.modules.leave.models  # noqa
    import app.modules.recruitment.models  # noqa
    import app.modules.onboarding.models  # noqa
    import app.modules.goals.models  # noqa
    import app.modules.skills.models  # noqa
    import app.modules.learning.models  # noqa
    import app.modules.service_desk.models  # noqa
    import app.modules.engagement.models  # noqa
    import app.modules.communication.models  # noqa
    import app.modules.workflows.models  # noqa
    import app.modules.approvals.models  # noqa
    import app.modules.payroll.models  # noqa
    import app.modules.expenses.models  # noqa
    import app.modules.assets.models  # noqa
    import app.modules.documents.models  # noqa
    import app.modules.notifications.models  # noqa
    import app.modules.audit.models  # noqa
except ImportError:
    pass
