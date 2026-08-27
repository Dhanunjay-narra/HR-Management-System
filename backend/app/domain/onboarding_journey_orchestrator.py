"""
Employee Onboarding Journey & Automated Lifecycle Orchestrator
Provisions role-specific IT hardware, security credentials, compliance trainings, buddy assignments, and 30-60-90 milestones.
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class OnboardingTaskDefinition:
    task_code: str
    title: str
    category: str  # IT_SETUP, HR_COMPLIANCE, TEAM_INTEGRATION, TRAINING, MANAGER_SYNC
    assignee_role: str  # EMPLOYEE, IT_ADMIN, HR_SPECIALIST, HIRING_MANAGER, BUDDY
    due_offset_days: int
    is_mandatory_for_probation_clearance: bool


DEPARTMENT_ONBOARDING_TEMPLATES: Dict[str, List[OnboardingTaskDefinition]] = {
    "ENGINEERING": [
        OnboardingTaskDefinition("IT-01", "Provision encrypted MacBook Pro & YubiKey 5C", "IT_SETUP", "IT_ADMIN", -3, True),
        OnboardingTaskDefinition("IT-02", "Grant GitHub Enterprise, AWS IAM & Datadog access", "IT_SETUP", "IT_ADMIN", 0, True),
        OnboardingTaskDefinition("HR-01", "Complete I-9 Verification / Right-to-Work documentation", "HR_COMPLIANCE", "HR_SPECIALIST", 3, True),
        OnboardingTaskDefinition("HR-02", "Sign Proprietary Information & Inventions Agreement (PIIA)", "HR_COMPLIANCE", "EMPLOYEE", 1, True),
        OnboardingTaskDefinition("TR-01", "Complete ISO 27001 Security Awareness & Phishing Training", "TRAINING", "EMPLOYEE", 7, True),
        OnboardingTaskDefinition("TEAM-01", "First Day Welcome Lunch with Assigned Peer Buddy", "TEAM_INTEGRATION", "BUDDY", 0, False),
        OnboardingTaskDefinition("MGR-01", "Day 1 Role Alignment & 30-Day Expectations Setting", "MANAGER_SYNC", "HIRING_MANAGER", 0, True),
        OnboardingTaskDefinition("MGR-30", "30-Day Milestone Check-in & Initial Project Review", "MANAGER_SYNC", "HIRING_MANAGER", 30, True),
        OnboardingTaskDefinition("MGR-60", "60-Day Mid-Probation Competency Calibration", "MANAGER_SYNC", "HIRING_MANAGER", 60, True),
        OnboardingTaskDefinition("MGR-90", "90-Day Formal Probation Confirmation & Review", "MANAGER_SYNC", "HIRING_MANAGER", 90, True),
    ],
    "SALES": [
        OnboardingTaskDefinition("IT-01", "Provision Dell Latitude & Salesforce Enterprise License", "IT_SETUP", "IT_ADMIN", -3, True),
        OnboardingTaskDefinition("HR-01", "Complete Tax Withholding (W-4 / W-8BEN) & Direct Deposit", "HR_COMPLIANCE", "EMPLOYEE", 2, True),
        OnboardingTaskDefinition("TR-01", "Product Suite Certification & Pitch Deck Mastery", "TRAINING", "EMPLOYEE", 14, True),
        OnboardingTaskDefinition("MGR-30", "30-Day Pipeline Building & Territory Plan Review", "MANAGER_SYNC", "HIRING_MANAGER", 30, True),
        OnboardingTaskDefinition("MGR-90", "90-Day Quota Attainment & Ramp Evaluation", "MANAGER_SYNC", "HIRING_MANAGER", 90, True),
    ]
}


class OnboardingJourneyOrchestrator:
    @classmethod
    def generate_journey_for_hire(
        cls,
        employee_id: str,
        employee_name: str,
        department: str,
        start_date: date
    ) -> List[Dict[str, Any]]:
        tasks_def = DEPARTMENT_ONBOARDING_TEMPLATES.get(
            department.upper(),
            DEPARTMENT_ONBOARDING_TEMPLATES["ENGINEERING"]
        )

        journey = []
        for t in tasks_def:
            due_dt = start_date + timedelta(days=t.due_offset_days)
            journey.append({
                "employee_id": employee_id,
                "employee_name": employee_name,
                "task_code": t.task_code,
                "title": t.title,
                "category": t.category,
                "assignee_role": t.assignee_role,
                "due_date": due_dt.isoformat(),
                "is_mandatory": t.is_mandatory_for_probation_clearance,
                "status": "PENDING"
            })

        return journey
