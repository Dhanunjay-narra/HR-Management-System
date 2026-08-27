"""
Asset Inventory & Hardware Tracking Models
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Float, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class Asset(TenantBaseModel):
    """Company Asset Record."""
    __tablename__ = "assets"

    asset_tag = Column(String(50), nullable=False, unique=True, index=True)  # e.g., AST-MBP-0142
    name = Column(String(255), nullable=False)
    category = Column(String(50), default="LAPTOP", nullable=False, index=True)  # LAPTOP, DESKTOP, MONITOR, PHONE, ACCESS_CARD, LICENSE
    serial_number = Column(String(100), nullable=True)
    model_number = Column(String(100), nullable=True)
    purchase_date = Column(Date, nullable=True)
    purchase_cost = Column(Float, default=0.0, nullable=False)
    
    current_employee_id = Column(String(36), ForeignKey("employees.id", ondelete="SET NULL"), nullable=True, index=True)
    status = Column(String(50), default="IN_INVENTORY", nullable=False, index=True)  # IN_INVENTORY, ASSIGNED, MAINTENANCE, RETIRED

    # Relationships
    current_employee = relationship("Employee")
    assignment_history = relationship("AssetAssignmentHistory", back_populates="asset", cascade="all, delete-orphan")


class AssetAssignmentHistory(TenantBaseModel):
    """Custody allocation and return history."""
    __tablename__ = "asset_assignment_history"

    asset_id = Column(String(36), ForeignKey("assets.id", ondelete="CASCADE"), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    assigned_date = Column(Date, default=date.today, nullable=False)
    returned_date = Column(Date, nullable=True)
    condition_at_assignment = Column(String(100), default="EXCELLENT", nullable=False)
    condition_at_return = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)

    # Relationships
    asset = relationship("Asset", back_populates="assignment_history")
    employee = relationship("Employee")
