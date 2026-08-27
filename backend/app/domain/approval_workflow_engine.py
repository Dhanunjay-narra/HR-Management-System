"""
Multi-Tier Enterprise Approval Chain & SLA Escalation State Machine
Supports sequential, parallel, quorum voting (e.g. 2 of 3 managers), conditional branching, and auto-delegation.
"""
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from enum import Enum


class ApprovalStepType(Enum):
    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL_ALL = "PARALLEL_ALL"
    PARALLEL_QUORUM = "PARALLEL_QUORUM"
    AUTO_APPROVE_CONDITIONAL = "AUTO_APPROVE_CONDITIONAL"


class ApprovalStatus(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    ESCALATED = "ESCALATED"
    SKIPPED = "SKIPPED"


@dataclass
class ApprovalStepResult:
    step_index: int
    approver_id: str
    approver_role: str
    status: ApprovalStatus
    decision_timestamp: Optional[datetime] = None
    comments: Optional[str] = None
    escalated_to_id: Optional[str] = None


@dataclass
class ApprovalInstance:
    instance_id: str
    workflow_id: str
    requester_id: str
    entity_type: str  # LEAVE, EXPENSE, PROMOTION, SALARY_REVISION, ASSET_REQUEST
    entity_id: str
    payload: Dict[str, Any]
    current_step: int = 0
    total_steps: int = 1
    status: ApprovalStatus = ApprovalStatus.PENDING
    history: List[ApprovalStepResult] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    sla_expires_at: Optional[datetime] = None


class AdvancedApprovalEngine:
    @classmethod
    def evaluate_next_step(
        cls,
        instance: ApprovalInstance,
        current_step_approvals: List[ApprovalStepResult],
        step_type: ApprovalStepType = ApprovalStepType.SEQUENTIAL,
        quorum_count: int = 1
    ) -> Tuple[ApprovalStatus, bool]:
        """
        Determines whether the approval instance advances, finishes, or gets rejected.
        Returns: (New Status, Is Final Finished)
        """
        # Check rejections
        rejections = [a for a in current_step_approvals if a.status == ApprovalStatus.REJECTED]
        if rejections:
            instance.status = ApprovalStatus.REJECTED
            return ApprovalStatus.REJECTED, True

        # Check approvals
        approvals = [a for a in current_step_approvals if a.status == ApprovalStatus.APPROVED]

        if step_type == ApprovalStepType.SEQUENTIAL:
            if len(approvals) >= 1:
                instance.current_step += 1
                if instance.current_step >= instance.total_steps:
                    instance.status = ApprovalStatus.APPROVED
                    return ApprovalStatus.APPROVED, True
                else:
                    return ApprovalStatus.PENDING, False

        elif step_type == ApprovalStepType.PARALLEL_QUORUM:
            if len(approvals) >= quorum_count:
                instance.current_step += 1
                if instance.current_step >= instance.total_steps:
                    instance.status = ApprovalStatus.APPROVED
                    return ApprovalStatus.APPROVED, True
                else:
                    return ApprovalStatus.PENDING, False

        elif step_type == ApprovalStepType.PARALLEL_ALL:
            if len(approvals) >= len(current_step_approvals):
                instance.current_step += 1
                if instance.current_step >= instance.total_steps:
                    instance.status = ApprovalStatus.APPROVED
                    return ApprovalStatus.APPROVED, True
                else:
                    return ApprovalStatus.PENDING, False

        return ApprovalStatus.PENDING, False

    @classmethod
    def check_sla_timeout_and_escalate(
        cls,
        instance: ApprovalInstance,
        escalation_manager_id: str
    ) -> bool:
        now = datetime.now(timezone.utc)
        if instance.sla_expires_at and now > instance.sla_expires_at and instance.status == ApprovalStatus.PENDING:
            instance.status = ApprovalStatus.ESCALATED
            instance.history.append(ApprovalStepResult(
                step_index=instance.current_step,
                approver_id="SYSTEM_SLA_WATCHDOG",
                approver_role="SYSTEM",
                status=ApprovalStatus.ESCALATED,
                decision_timestamp=now,
                comments="SLA expired without decision; automatically escalated to senior department head.",
                escalated_to_id=escalation_manager_id
            ))
            return True
        return False
