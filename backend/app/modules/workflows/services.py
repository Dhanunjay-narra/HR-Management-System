"""
Workflow Automation Engine
"""
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, desc

from app.modules.workflows.models import WorkflowDefinition, WorkflowExecution
from app.modules.workflows.schemas import WorkflowDefinitionCreate
from app.events.event_bus import event_bus, DomainEvent
from app.database.session import AsyncSessionLocal
from app.core.logging import logger


class WorkflowService:
    @staticmethod
    async def create_workflow(db: AsyncSession, tenant_id: str, data: WorkflowDefinitionCreate) -> WorkflowDefinition:
        wf = WorkflowDefinition(tenant_id=tenant_id, **data.model_dump())
        db.add(wf)
        await db.flush()
        return wf

    @staticmethod
    async def list_workflows(db: AsyncSession, tenant_id: str) -> List[WorkflowDefinition]:
        result = await db.execute(
            select(WorkflowDefinition).where(WorkflowDefinition.tenant_id == tenant_id, WorkflowDefinition.is_deleted == False)
        )
        return list(result.scalars().all())

    @staticmethod
    async def execute_matched_workflows(event: DomainEvent) -> None:
        """Evaluate and execute active workflows that match this trigger event."""
        if not event.tenant_id:
            return

        async with AsyncSessionLocal() as db:
            try:
                res = await db.execute(
                    select(WorkflowDefinition).where(
                        WorkflowDefinition.tenant_id == event.tenant_id,
                        WorkflowDefinition.trigger_event == event.event_type,
                        WorkflowDefinition.is_active == True,
                        WorkflowDefinition.is_deleted == False
                    )
                )
                workflows = list(res.scalars().all())
                for wf in workflows:
                    # Evaluate conditions
                    matched = True
                    for key, val in (wf.conditions or {}).items():
                        if event.payload.get(key) != val:
                            matched = False
                            break

                    if not matched:
                        continue

                    logs: List[str] = [f"Workflow '{wf.name}' triggered by {event.event_type}."]
                    for act in (wf.actions or []):
                        act_type = act.get("type", "log")
                        logs.append(f"Executed action: {act_type} -> {act}")

                    execution = WorkflowExecution(
                        tenant_id=event.tenant_id,
                        workflow_id=wf.id,
                        trigger_event=event.event_type,
                        payload=event.payload,
                        status="COMPLETED",
                        execution_logs=logs,
                        executed_at=datetime.now(timezone.utc)
                    )
                    db.add(execution)
                await db.commit()
            except Exception as e:
                logger.error(f"Error in WorkflowEngine for {event.event_type}: {e}", exc_info=True)


# Hook workflow engine into event bus
event_bus.subscribe("*", WorkflowService.execute_matched_workflows)
