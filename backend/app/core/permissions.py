"""
Role-Based Access Control (RBAC) & Permission Engine
Defines granular enterprise permissions (module.resource.action) and pre-configured role profiles.
"""
from enum import Enum
from typing import List, Set, Dict


class SystemRole(str, Enum):
    PLATFORM_OWNER = "platform_owner"
    ORG_OWNER = "org_owner"
    HR_ADMIN = "hr_admin"
    HR_MANAGER = "hr_manager"
    RECRUITER = "recruiter"
    HIRING_MANAGER = "hiring_manager"
    DEPT_MANAGER = "dept_manager"
    TEAM_LEAD = "team_lead"
    FINANCE_ADMIN = "finance_admin"
    IT_ADMIN = "it_admin"
    EMPLOYEE = "employee"
    AUDITOR = "auditor"


# Standard Permission Definitions across all 30 Modules
ALL_PERMISSIONS: List[str] = [
    # Auth & Tenants
    "auth.user.create", "auth.user.read", "auth.user.update", "auth.user.delete",
    "tenant.config.read", "tenant.config.update", "tenant.manage",
    
    # Organization
    "org.structure.read", "org.structure.manage", "org.chart.view",
    "dept.read", "dept.manage", "position.manage",
    
    # Employees & Employee 360
    "employee.create", "employee.read", "employee.read_sensitive", "employee.update", "employee.delete",
    "employee_360.view", "employee.timeline.view", "employee.timeline.manage",
    
    # Attendance & Leave
    "attendance.clock", "attendance.view_own", "attendance.view_team", "attendance.manage",
    "leave.apply", "leave.view_own", "leave.view_team", "leave.approve", "leave.manage_policies",
    
    # Recruitment & Onboarding
    "recruitment.job.create", "recruitment.job.read", "recruitment.job.manage",
    "recruitment.candidate.read", "recruitment.candidate.manage", "recruitment.interview.conduct",
    "onboarding.template.manage", "onboarding.task.view", "onboarding.task.manage",
    
    # Goals & Performance
    "goal.view_own", "goal.view_team", "goal.manage",
    "performance.review_own", "performance.review_team", "performance.manage_cycles",
    "skills.view", "skills.manage", "skills.gap_analysis",
    "learning.course.view", "learning.course.enroll", "learning.course.manage",
    
    # Engagement & Service Desk
    "engagement.survey.participate", "engagement.survey.manage", "engagement.kudos.send",
    "service_desk.ticket.create", "service_desk.ticket.view_own", "service_desk.ticket.manage", "service_desk.admin",
    
    # Workflows & Approvals
    "workflow.view", "workflow.manage", "workflow.execute",
    "approval.request.create", "approval.request.approve", "approval.chain.manage",
    
    # Payroll, Expenses, Assets, Docs
    "payroll.view_own", "payroll.view_all", "payroll.process", "payroll.approve",
    "expense.claim.create", "expense.claim.view_own", "expense.claim.approve", "expense.manage",
    "asset.view_own", "asset.view_all", "asset.manage",
    "document.view_own", "document.view_all", "document.manage",
    
    # Communication, Analytics, AI & Audit
    "communication.broadcast.send", "communication.announcement.manage",
    "analytics.dashboard.view", "analytics.workforce.view", "analytics.financial.view",
    "ai.assistant.use", "ai.admin",
    "audit.log.view",
]

# Role-to-Permissions Mapping Matrix
ROLE_PERMISSIONS: Dict[str, List[str]] = {
    SystemRole.PLATFORM_OWNER: ["*"],
    
    SystemRole.ORG_OWNER: [
        "*",  # Full control within their tenant organization
    ],
    
    SystemRole.HR_ADMIN: [
        "auth.user.create", "auth.user.read", "auth.user.update",
        "tenant.config.read", "org.structure.read", "org.structure.manage", "org.chart.view",
        "dept.read", "dept.manage", "position.manage",
        "employee.create", "employee.read", "employee.read_sensitive", "employee.update", "employee.delete",
        "employee_360.view", "employee.timeline.view", "employee.timeline.manage",
        "attendance.clock", "attendance.view_own", "attendance.view_team", "attendance.manage",
        "leave.apply", "leave.view_own", "leave.view_team", "leave.approve", "leave.manage_policies",
        "recruitment.job.create", "recruitment.job.read", "recruitment.job.manage",
        "recruitment.candidate.read", "recruitment.candidate.manage", "recruitment.interview.conduct",
        "onboarding.template.manage", "onboarding.task.view", "onboarding.task.manage",
        "goal.view_own", "goal.view_team", "goal.manage",
        "performance.review_own", "performance.review_team", "performance.manage_cycles",
        "skills.view", "skills.manage", "skills.gap_analysis",
        "learning.course.view", "learning.course.enroll", "learning.course.manage",
        "engagement.survey.participate", "engagement.survey.manage", "engagement.kudos.send",
        "service_desk.ticket.create", "service_desk.ticket.view_own", "service_desk.ticket.manage", "service_desk.admin",
        "workflow.view", "workflow.manage", "workflow.execute",
        "approval.request.create", "approval.request.approve", "approval.chain.manage",
        "payroll.view_own", "payroll.view_all", "payroll.process",
        "expense.claim.create", "expense.claim.view_own", "expense.claim.approve", "expense.manage",
        "asset.view_own", "asset.view_all", "asset.manage",
        "document.view_own", "document.view_all", "document.manage",
        "communication.broadcast.send", "communication.announcement.manage",
        "analytics.dashboard.view", "analytics.workforce.view",
        "ai.assistant.use", "audit.log.view",
    ],
    
    SystemRole.HR_MANAGER: [
        "auth.user.read", "org.structure.read", "org.chart.view", "dept.read",
        "employee.create", "employee.read", "employee.read_sensitive", "employee.update",
        "employee_360.view", "employee.timeline.view", "employee.timeline.manage",
        "attendance.clock", "attendance.view_own", "attendance.view_team", "attendance.manage",
        "leave.apply", "leave.view_own", "leave.view_team", "leave.approve",
        "recruitment.job.create", "recruitment.job.read", "recruitment.candidate.read", "recruitment.candidate.manage",
        "onboarding.task.view", "onboarding.task.manage",
        "goal.view_own", "goal.view_team", "goal.manage",
        "performance.review_own", "performance.review_team", "performance.manage_cycles",
        "skills.view", "skills.manage", "skills.gap_analysis",
        "learning.course.view", "learning.course.enroll", "learning.course.manage",
        "engagement.survey.participate", "engagement.survey.manage", "engagement.kudos.send",
        "service_desk.ticket.create", "service_desk.ticket.view_own", "service_desk.ticket.manage",
        "approval.request.create", "approval.request.approve",
        "document.view_own", "document.view_all", "document.manage",
        "communication.announcement.manage",
        "analytics.dashboard.view", "analytics.workforce.view",
        "ai.assistant.use",
    ],
    
    SystemRole.RECRUITER: [
        "recruitment.job.create", "recruitment.job.read", "recruitment.job.manage",
        "recruitment.candidate.read", "recruitment.candidate.manage", "recruitment.interview.conduct",
        "onboarding.task.view", "onboarding.task.manage",
        "skills.view",
        "attendance.clock", "attendance.view_own",
        "leave.apply", "leave.view_own",
        "service_desk.ticket.create", "service_desk.ticket.view_own",
        "ai.assistant.use",
    ],
    
    SystemRole.HIRING_MANAGER: [
        "recruitment.job.read", "recruitment.candidate.read", "recruitment.interview.conduct",
        "employee.read", "attendance.clock", "attendance.view_own", "leave.apply", "leave.view_own",
        "service_desk.ticket.create", "service_desk.ticket.view_own", "ai.assistant.use",
    ],
    
    SystemRole.DEPT_MANAGER: [
        "org.structure.read", "org.chart.view", "dept.read",
        "employee.read", "employee_360.view", "employee.timeline.view",
        "attendance.clock", "attendance.view_own", "attendance.view_team",
        "leave.apply", "leave.view_own", "leave.view_team", "leave.approve",
        "goal.view_own", "goal.view_team", "goal.manage",
        "performance.review_own", "performance.review_team",
        "skills.view", "skills.gap_analysis",
        "learning.course.view", "learning.course.enroll",
        "engagement.survey.participate", "engagement.kudos.send",
        "service_desk.ticket.create", "service_desk.ticket.view_own",
        "approval.request.create", "approval.request.approve",
        "expense.claim.create", "expense.claim.view_own", "expense.claim.approve",
        "asset.view_own", "document.view_own",
        "analytics.dashboard.view", "ai.assistant.use",
    ],
    
    SystemRole.TEAM_LEAD: [
        "org.structure.read", "org.chart.view",
        "employee.read", "employee.timeline.view",
        "attendance.clock", "attendance.view_own", "attendance.view_team",
        "leave.apply", "leave.view_own", "leave.view_team",
        "goal.view_own", "goal.view_team",
        "performance.review_own", "performance.review_team",
        "skills.view", "learning.course.view", "learning.course.enroll",
        "engagement.survey.participate", "engagement.kudos.send",
        "service_desk.ticket.create", "service_desk.ticket.view_own",
        "approval.request.create", "approval.request.approve",
        "expense.claim.create", "expense.claim.view_own",
        "asset.view_own", "document.view_own", "ai.assistant.use",
    ],
    
    SystemRole.FINANCE_ADMIN: [
        "payroll.view_own", "payroll.view_all", "payroll.process", "payroll.approve",
        "expense.claim.create", "expense.claim.view_own", "expense.claim.approve", "expense.manage",
        "employee.read", "attendance.view_all", "leave.view_all",
        "analytics.dashboard.view", "analytics.financial.view",
        "service_desk.ticket.create", "service_desk.ticket.view_own", "service_desk.ticket.manage",
        "approval.request.create", "approval.request.approve",
        "ai.assistant.use",
    ],
    
    SystemRole.IT_ADMIN: [
        "asset.view_own", "asset.view_all", "asset.manage",
        "onboarding.task.view", "onboarding.task.manage",
        "employee.read",
        "service_desk.ticket.create", "service_desk.ticket.view_own", "service_desk.ticket.manage",
        "attendance.clock", "attendance.view_own",
        "leave.apply", "leave.view_own",
        "approval.request.create", "ai.assistant.use",
    ],
    
    SystemRole.EMPLOYEE: [
        "attendance.clock", "attendance.view_own",
        "leave.apply", "leave.view_own",
        "goal.view_own",
        "performance.review_own",
        "skills.view",
        "learning.course.view", "learning.course.enroll",
        "engagement.survey.participate", "engagement.kudos.send",
        "service_desk.ticket.create", "service_desk.ticket.view_own",
        "payroll.view_own",
        "expense.claim.create", "expense.claim.view_own",
        "asset.view_own",
        "document.view_own",
        "approval.request.create",
        "ai.assistant.use",
    ],
    
    SystemRole.AUDITOR: [
        "auth.user.read", "tenant.config.read", "org.structure.read", "dept.read",
        "employee.read", "employee_360.view", "employee.timeline.view",
        "attendance.view_all", "leave.view_all",
        "recruitment.job.read", "recruitment.candidate.read",
        "payroll.view_all", "expense.manage", "asset.view_all",
        "document.view_all", "audit.log.view", "analytics.dashboard.view",
    ]
}


def get_permissions_for_role(role_name: str) -> Set[str]:
    """Retrieve set of permissions for a role."""
    perms = ROLE_PERMISSIONS.get(role_name, [])
    return set(perms)


def has_permission(user_permissions: List[str], required_permission: str) -> bool:
    """Evaluate whether the user's permission set satisfies the required permission."""
    if "*" in user_permissions:
        return True
    if required_permission in user_permissions:
        return True
    
    # Check wildcards e.g. "employee.*" matching "employee.read"
    req_parts = required_permission.split(".")
    if len(req_parts) >= 2:
        prefix_wildcard = f"{req_parts[0]}.*"
        if prefix_wildcard in user_permissions:
            return True
        if len(req_parts) == 3:
            mid_wildcard = f"{req_parts[0]}.{req_parts[1]}.*"
            if mid_wildcard in user_permissions:
                return True
    return False
