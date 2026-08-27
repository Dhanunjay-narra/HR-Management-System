"""
Goals & OKR Service
"""
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.goals.models import Goal, KeyResult, GoalCheckIn
from app.modules.goals.schemas import GoalCreate, GoalCheckInCreate
from app.core.exceptions import ResourceNotFoundException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


class GoalService:
    @staticmethod
    async def create_goal(db: AsyncSession, tenant_id: str, data: GoalCreate, actor_id: Optional[str] = None) -> Goal:
        krs = data.key_results
        goal_data = data.model_dump(exclude={"key_results"})

        goal = Goal(tenant_id=tenant_id, **goal_data)
        db.add(goal)
        await db.flush()

        for kr in krs:
            kr_item = KeyResult(tenant_id=tenant_id, goal_id=goal.id, **kr.model_dump())
            db.add(kr_item)

        await db.flush()

        if goal.owner_employee_id:
            db.add(EmployeeTimelineEvent(
                tenant_id=tenant_id,
                employee_id=goal.owner_employee_id,
                actor_id=actor_id,
                event_type="GOAL_CREATED",
                title=f"Goal Created: {goal.title}",
                description=f"Assigned {goal.level} goal due {goal.deadline}.",
                entity_type="Goal",
                entity_id=goal.id
            ))

        await event_bus.publish(DomainEvent(
            event_type="goal.created",
            tenant_id=tenant_id,
            actor_id=actor_id,
            payload={"goal_id": goal.id, "title": goal.title, "owner_id": goal.owner_employee_id}
        ))
        return goal

    @staticmethod
    async def get_by_id(db: AsyncSession, tenant_id: str, goal_id: str) -> Goal:
        result = await db.execute(
            select(Goal)
            .options(selectinload(Goal.key_results), selectinload(Goal.check_ins))
            .where(Goal.id == goal_id, Goal.tenant_id == tenant_id, Goal.is_deleted == False)
        )
        goal = result.scalar_one_or_none()
        if not goal:
            raise ResourceNotFoundException("Goal", goal_id)
        return goal

    @staticmethod
    async def list_goals(
        db: AsyncSession,
        tenant_id: str,
        owner_id: Optional[str] = None,
        level: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[Goal]:
        query = (
            select(Goal)
            .options(selectinload(Goal.key_results))
            .where(Goal.tenant_id == tenant_id, Goal.is_deleted == False)
        )
        if owner_id:
            query = query.where(Goal.owner_employee_id == owner_id)
        if level:
            query = query.where(Goal.level == level)

        query = query.order_by(desc(Goal.created_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def record_check_in(
        db: AsyncSession,
        tenant_id: str,
        goal_id: str,
        user_id: str,
        data: GoalCheckInCreate
    ) -> Goal:
        goal = await GoalService.get_by_id(db, tenant_id, goal_id)
        prev = goal.current_value
        goal.current_value = data.new_value

        if goal.current_value >= goal.target_value:
            goal.status = "COMPLETED"
            if goal.owner_employee_id:
                db.add(EmployeeTimelineEvent(
                    tenant_id=tenant_id,
                    employee_id=goal.owner_employee_id,
                    actor_id=user_id,
                    event_type="GOAL_ACHIEVED",
                    title=f"Goal Achieved: {goal.title}",
                    description=f"100% target outcome accomplished.",
                    entity_type="Goal",
                    entity_id=goal.id
                ))

        check_in = GoalCheckIn(
            tenant_id=tenant_id,
            goal_id=goal.id,
            author_user_id=user_id,
            previous_value=prev,
            new_value=data.new_value,
            confidence_score=data.confidence_score,
            notes=data.notes
        )
        db.add(check_in)
        await db.flush()
        return goal
