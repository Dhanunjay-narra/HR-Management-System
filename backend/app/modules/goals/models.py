"""
Goals & OKR Models
Cascading OKR hierarchy (Organization -> Department -> Team -> Employee) with Key Results and Check-ins.
"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime, Float, Boolean, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.database.base import TenantBaseModel


class Goal(TenantBaseModel):
    """Cascading OKR Goal entity."""
    __tablename__ = "goals"

    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    level = Column(String(50), default="INDIVIDUAL", nullable=False)  # COMPANY, DEPARTMENT, TEAM, INDIVIDUAL
    parent_goal_id = Column(String(36), ForeignKey("goals.id", ondelete="SET NULL"), nullable=True, index=True)
    
    owner_employee_id = Column(String(36), ForeignKey("employees.id", ondelete="CASCADE"), nullable=True, index=True)
    department_id = Column(String(36), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True, index=True)
    
    target_value = Column(Float, default=100.0, nullable=False)
    current_value = Column(Float, default=0.0, nullable=False)
    unit = Column(String(50), default="PERCENT", nullable=False)  # PERCENT, CURRENCY, NUMBER, MILESTONE
    weight = Column(Float, default=1.0, nullable=False)
    
    start_date = Column(Date, default=date.today, nullable=False)
    deadline = Column(Date, nullable=False, index=True)
    status = Column(String(50), default="IN_PROGRESS", nullable=False, index=True)  # NOT_STARTED, IN_PROGRESS, ON_TRACK, AT_RISK, COMPLETED

    # Relationships
    parent_goal = relationship("Goal", remote_side="Goal.id", backref="sub_goals")
    owner = relationship("Employee", foreign_keys=[owner_employee_id])
    department = relationship("Department")
    key_results = relationship("KeyResult", back_populates="goal", cascade="all, delete-orphan")
    check_ins = relationship("GoalCheckIn", back_populates="goal", cascade="all, delete-orphan")

    @property
    def progress_percentage(self) -> float:
        if self.target_value <= 0:
            return 0.0
        return round(min(100.0, (self.current_value / self.target_value) * 100.0), 1)


class KeyResult(TenantBaseModel):
    """Specific measurable outcome underpinning a goal."""
    __tablename__ = "key_results"

    goal_id = Column(String(36), ForeignKey("goals.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    target_value = Column(Float, default=100.0, nullable=False)
    current_value = Column(Float, default=0.0, nullable=False)
    unit = Column(String(50), default="PERCENT", nullable=False)

    # Relationships
    goal = relationship("Goal", back_populates="key_results")


class GoalCheckIn(TenantBaseModel):
    """Progress check-in log and commentary."""
    __tablename__ = "goal_check_ins"

    goal_id = Column(String(36), ForeignKey("goals.id", ondelete="CASCADE"), nullable=False, index=True)
    author_user_id = Column(String(36), nullable=False)
    previous_value = Column(Float, nullable=False)
    new_value = Column(Float, nullable=False)
    confidence_score = Column(Integer, default=4, nullable=False)  # 1 to 5
    notes = Column(Text, nullable=False)

    # Relationships
    goal = relationship("Goal", back_populates="check_ins")
