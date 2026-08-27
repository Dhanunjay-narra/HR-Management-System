"""
Standard Enterprise 30-60-90 Day Departmental Onboarding Journey Roadmaps
Structured milestone checklists, mentor pairing protocols, and ramp-up competency assessments.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class OnboardingTaskItem:
    task_title: str
    task_description: str
    mandatory_for_probation_signoff: bool = True


@dataclass
class DepartmentOnboardingRoadmap:
    department_code: str
    department_name: str
    milestone_tasks: List[OnboardingTaskItem]


DEPARTMENT_ONBOARDING_ROADMAPS: Dict[str, DepartmentOnboardingRoadmap] = {
    "Engineering": DepartmentOnboardingRoadmap(
        department_code="Engineering",
        department_name="Software & Infrastructure Engineering",
        milestone_tasks=[
            OnboardingTaskItem("Day 1: Hardware Setup & Zero-Trust MFA Registration", "Provision MacBook Pro M3, register YubiKey FIDO2 token, configure 1Password vault."),
            OnboardingTaskItem("Day 2: Local Development Environment & Git Workflow", "Clone repository, run Docker Compose stack, verify local Pytest and Vite build pass."),
            OnboardingTaskItem("Day 3: Architecture & Security Overview with Tech Lead", "Review architecture decision records (ADRs), DB schema ERDs, and ISO 27001 policies."),
            OnboardingTaskItem("Week 1: First Good-First-Issue Pull Request", "Complete starter bug fix or feature enhancement, pass CI/CD pipeline, deploy to staging."),
            OnboardingTaskItem("Day 30 Milestone: Core Service Ownership", "Own specific microservice domain, participate in weekly sprint planning and backlog grooming."),
            OnboardingTaskItem("Day 60 Milestone: Secondary On-Call Rotation", "Shadow primary on-call engineer during pager duty rotation, review incident runbooks."),
            OnboardingTaskItem("Day 90 Milestone: Independent Production Feature Launch", "Lead full lifecycle design, implementation, and canary release of high-impact feature."),
        ]
    ),
    "Product_Management": DepartmentOnboardingRoadmap(
        department_code="Product_Management",
        department_name="Product & User Experience",
        milestone_tasks=[
            OnboardingTaskItem("Day 1: Tooling & Customer Analytics Access", "Access Amplitude, FullStory, Jira, Linear, Figma, and customer feedback repository."),
            OnboardingTaskItem("Day 3: Product Vision & Strategic OKR Immersion", "Meet with VP of Product to align on company themes, roadmap themes, and key metrics."),
            OnboardingTaskItem("Week 1: Customer Call Shadowing (5 Enterprise Clients)", "Attend live customer discovery and executive business review (EBR) sessions."),
            OnboardingTaskItem("Day 30 Milestone: Feature Specification (PRD) Authoring", "Draft comprehensive Product Requirements Document (PRD) with user stories and wireframes."),
            OnboardingTaskItem("Day 60 Milestone: Sprint Execution & Design Handoff", "Partner with Engineering Leads and Product Designers to deliver sprint commitments."),
            OnboardingTaskItem("Day 90 Milestone: Beta Feature Launch & Telemetry Review", "Launch beta feature to customer cohort, analyze adoption funnel and NPS feedback."),
        ]
    ),
    "Sales_GTM": DepartmentOnboardingRoadmap(
        department_code="Sales_GTM",
        department_name="Enterprise Software Sales & Solutions",
        milestone_tasks=[
            OnboardingTaskItem("Day 1: CRM & Sales Intelligence Tooling Setup", "Configure Salesforce/HR Management System, LinkedIn Sales Navigator, Outreach, and ZoomInfo."),
            OnboardingTaskItem("Day 3: Value Proposition & Competitive Battlecards", "Master product positioning, competitive differentiators, and ROI justification frameworks."),
            OnboardingTaskItem("Week 1: Pitch Certification & Roleplay Simulation", "Deliver mock enterprise product pitch and demo to Sales Director; pass certification."),
            OnboardingTaskItem("Day 30 Milestone: Territory Pipeline Prospecting", "Build pipeline of 50 qualified target accounts; initiate outbound sequence campaigns."),
            OnboardingTaskItem("Day 60 Milestone: Live Customer Discovery & Demo Delivery", "Lead live enterprise discovery calls with VP/C-level economic buyers."),
            OnboardingTaskItem("Day 90 Milestone: Closed-Won Deal / Quarter Quota Execution", "Advance enterprise deal through procurement, security review, and contract execution."),
        ]
    ),
}

class OnboardingRoadmapService:
    @classmethod
    def get_roadmap(cls, dept_code: str) -> DepartmentOnboardingRoadmap:
        return DEPARTMENT_ONBOARDING_ROADMAPS.get(dept_code)

    @classmethod
    def get_all_roadmaps(cls) -> List[DepartmentOnboardingRoadmap]:
        return list(DEPARTMENT_ONBOARDING_ROADMAPS.values())
