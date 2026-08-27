"""
Onboarding Service
"""
from datetime import date, datetime, timedelta, timezone
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc
from sqlalchemy.orm import selectinload

from app.modules.onboarding.models import OnboardingWorkflow, OnboardingTask, MilestoneReview
from app.modules.onboarding.schemas import OnboardingWorkflowCreate, MilestoneReviewCreate
from app.core.exceptions import ResourceNotFoundException, DuplicateResourceException, ValidationException
from app.events.event_bus import event_bus, DomainEvent
from app.modules.employee_360.models import EmployeeTimelineEvent


STANDARD_ONBOARDING_TASKS = [
    {"title": "Submit Signed Employment Contract & ID Proofs", "category": "DOCUMENTATION", "days_offset": 2},
    {"title": "Submit Bank Account & Tax Filing Details", "category": "DOCUMENTATION", "days_offset": 3},
    {"title": "Provision Developer Laptop & Hardware Setup", "category": "IT_HARDWARE", "days_offset": 1},
    {"title": "Grant GitHub, Slack, and Google Workspace Access", "category": "ACCESS_CREDENTIALS", "days_offset": 1},
    {"title": "Complete Mandatory Security & Compliance Training", "category": "TRAINING", "days_offset": 14},
    {"title": "Initial 1-on-1 Manager Alignment & Goal Setting", "category": "MANAGER_1ON1", "days_offset": 7},
]


class OnboardingService:
    @staticmethod
    async def create_workflow(
        db: AsyncSession,
        tenant_id: str,
        data: OnboardingWorkflowCreate,
        actor_id: Optional[str] = None
    ) -> OnboardingWorkflow:
        existing = await db.execute(
            select(OnboardingWorkflow).where(
                OnboardingWorkflow.employee_id == data.employee_id,
                OnboardingWorkflow.tenant_id == tenant_id,
                OnboardingWorkflow.is_deleted == False
            )
        )
        if existing.scalar_one_or_none():
            raise DuplicateResourceException("OnboardingWorkflow", "employee_id", data.employee_id)

        today = date.today()
        target_date = today + timedelta(days=data.target_completion_days)

        workflow = OnboardingWorkflow(
            tenant_id=tenant_id,
            employee_id=data.employee_id,
            template_name=data.template_name,
            start_date=today,
            target_completion_date=target_date,
            status="IN_PROGRESS"
        )
        db.add(workflow)
        await db.flush()

        # Seed standard onboarding tasks
        for item in STANDARD_ONBOARDING_TASKS:
            task = OnboardingTask(
                tenant_id=tenant_id,
                workflow_id=workflow.id,
                title=item["title"],
                category=item["category"],
                due_date=today + timedelta(days=item["days_offset"]),
                is_completed=False
            )
            db.add(task)

        # Seed 30/60/90 day milestone reviews
        for days, name in [(30, "DAY_30"), (60, "DAY_60"), (90, "DAY_90")]:
            review = MilestoneReview(
                tenant_id=tenant_id,
                employee_id=data.employee_id,
                milestone=name,
                due_date=today + timedelta(days=days),
                status="PENDING"
            )
            db.add(review)

        # Record timeline event
        db.add(EmployeeTimelineEvent(
            tenant_id=tenant_id,
            employee_id=data.employee_id,
            actor_id=actor_id,
            event_type="ONBOARDING_STARTED",
            title="Onboarding Journey Commenced",
            description=f"Initialized {data.template_name} with {len(STANDARD_ONBOARDING_TASKS)} checklist tasks.",
            metadata_json={"workflow_id": workflow.id}
        ))

        await db.flush()

        await event_bus.publish(DomainEvent(
            event_type="onboarding.started",
            tenant_id=tenant_id,
            actor_id=actor_id,
            payload={"workflow_id": workflow.id, "employee_id": data.employee_id}
        ))

        return workflow

    @staticmethod
    async def get_by_employee(db: AsyncSession, tenant_id: str, employee_id: str) -> Optional[OnboardingWorkflow]:
        result = await db.execute(
            select(OnboardingWorkflow)
            .options(selectinload(OnboardingWorkflow.tasks), selectinload(OnboardingWorkflow.employee))
            .where(
                OnboardingWorkflow.employee_id == employee_id,
                OnboardingWorkflow.tenant_id == tenant_id,
                OnboardingWorkflow.is_deleted == False
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def complete_task(
        db: AsyncSession,
        tenant_id: str,
        task_id: str,
        actor_id: Optional[str] = None
    ) -> OnboardingTask:
        result = await db.execute(
            select(OnboardingTask).where(
                OnboardingTask.id == task_id,
                OnboardingTask.tenant_id == tenant_id,
                OnboardingTask.is_deleted == False
            )
        )
        task = result.scalar_one_or_none()
        if not task:
            raise ResourceNotFoundException("OnboardingTask", task_id)

        task.is_completed = True
        task.completed_at = datetime.now(timezone.utc)
        await db.flush()

        # Check if all tasks in workflow are completed
        res_tasks = await db.execute(
            select(OnboardingTask).where(
                OnboardingTask.workflow_id == task.workflow_id,
                OnboardingTask.is_deleted == False
            )
        )
        all_tasks = list(res_tasks.scalars().all())
        if all(t.is_completed for t in all_tasks):
            wf_res = await db.execute(select(OnboardingWorkflow).where(OnboardingWorkflow.id == task.workflow_id))
            wf = wf_res.scalar_one_or_none()
            if wf:
                wf.status = "COMPLETED"
                wf.completed_at = datetime.now(timezone.utc)
                await db.flush()

        return task
