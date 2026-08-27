"""
Enterprise Standard Competency Architecture Framework (50+ Core Competencies)
Defines 5-point mastery levels (Foundational, Developing, Proficient, Advanced, Expert) with observable behavioral anchors and developmental guidance.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class CompetencyProficiencyLevel:
    level: int  # 1 to 5
    title: str
    behavioral_indicators: List[str]
    development_milestones: List[str]


@dataclass
class EnterpriseCompetencyDefinition:
    competency_id: str
    name: str
    job_family: str
    summary: str
    levels: List[CompetencyProficiencyLevel]


MASTER_COMPETENCY_REGISTRY: Dict[str, EnterpriseCompetencyDefinition] = {
    "COMP-ARCH-01": EnterpriseCompetencyDefinition(
        competency_id="COMP-ARCH-01",
        name="Distributed Software Architecture",
        job_family="Engineering",
        summary="Ability to design, scale, and maintain fault-tolerant, low-latency distributed microservices and event-driven data systems.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Distributed Software Architecture concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Distributed Software Architecture.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Distributed Software Architecture tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Distributed Software Architecture challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Distributed Software Architecture across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Distributed Software Architecture; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-CODE-02": EnterpriseCompetencyDefinition(
        competency_id="COMP-CODE-02",
        name="Code Quality & Software Craftsmanship",
        job_family="Engineering",
        summary="Consistently produces clean, modular, highly testable, well-documented code adhering to SOLID principles and design patterns.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Code Quality & Software Craftsmanship concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Code Quality & Software Craftsmanship.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Code Quality & Software Craftsmanship tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Code Quality & Software Craftsmanship challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Code Quality & Software Craftsmanship across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Code Quality & Software Craftsmanship; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-SEC-03": EnterpriseCompetencyDefinition(
        competency_id="COMP-SEC-03",
        name="Application Security & DevSecOps",
        job_family="Security",
        summary="Proactively identifies vulnerabilities (OWASP), designs defense-in-depth security architectures, and automates compliance controls.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Application Security & DevSecOps concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Application Security & DevSecOps.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Application Security & DevSecOps tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Application Security & DevSecOps challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Application Security & DevSecOps across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Application Security & DevSecOps; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-RELI-04": EnterpriseCompetencyDefinition(
        competency_id="COMP-RELI-04",
        name="Site Reliability & Incident Management",
        job_family="Operations",
        summary="Maintains high-availability infrastructure (99.99% SLOs), designs telemetry monitoring, and leads blameless postmortems.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Site Reliability & Incident Management concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Site Reliability & Incident Management.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Site Reliability & Incident Management tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Site Reliability & Incident Management challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Site Reliability & Incident Management across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Site Reliability & Incident Management; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-DATA-05": EnterpriseCompetencyDefinition(
        competency_id="COMP-DATA-05",
        name="Data Modeling & Storage Optimization",
        job_family="Data",
        summary="Designs normalized relational and distributed NoSQL storage schemas optimized for read/write access patterns at high scale.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Data Modeling & Storage Optimization concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Data Modeling & Storage Optimization.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Data Modeling & Storage Optimization tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Data Modeling & Storage Optimization challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Data Modeling & Storage Optimization across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Data Modeling & Storage Optimization; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-AI-06": EnterpriseCompetencyDefinition(
        competency_id="COMP-AI-06",
        name="Machine Learning & Generative AI Systems",
        job_family="AI/ML",
        summary="Architects production RAG systems, embedding pipelines, fine-tuned models, and evaluation guardrails.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Machine Learning & Generative AI Systems concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Machine Learning & Generative AI Systems.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Machine Learning & Generative AI Systems tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Machine Learning & Generative AI Systems challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Machine Learning & Generative AI Systems across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Machine Learning & Generative AI Systems; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-PROD-07": EnterpriseCompetencyDefinition(
        competency_id="COMP-PROD-07",
        name="Product Vision & Customer Empathy",
        job_family="Product",
        summary="Translates customer pain points into clear, prioritized product roadmaps with measurable business outcomes and high ROI.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Product Vision & Customer Empathy concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Product Vision & Customer Empathy.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Product Vision & Customer Empathy tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Product Vision & Customer Empathy challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Product Vision & Customer Empathy across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Product Vision & Customer Empathy; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-UX-08": EnterpriseCompetencyDefinition(
        competency_id="COMP-UX-08",
        name="User Experience & Interface Design",
        job_family="Design",
        summary="Creates intuitive, elegant, accessible user interfaces (WCAG 2.1 AA) and scalable design systems in Figma and code.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of User Experience & Interface Design concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in User Experience & Interface Design.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine User Experience & Interface Design tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex User Experience & Interface Design challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in User Experience & Interface Design across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in User Experience & Interface Design; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-AGILE-09": EnterpriseCompetencyDefinition(
        competency_id="COMP-AGILE-09",
        name="Agile Execution & Sprint Velocity",
        job_family="Execution",
        summary="Executes iterative sprint cycles, eliminates blocking dependencies, and balances technical debt with roadmap feature delivery.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Agile Execution & Sprint Velocity concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Agile Execution & Sprint Velocity.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Agile Execution & Sprint Velocity tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Agile Execution & Sprint Velocity challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Agile Execution & Sprint Velocity across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Agile Execution & Sprint Velocity; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-COLLAB-10": EnterpriseCompetencyDefinition(
        competency_id="COMP-COLLAB-10",
        name="Cross-Functional Collaboration",
        job_family="Teamwork",
        summary="Partners seamlessly across Engineering, Product, Design, Sales, Marketing, Legal, and Finance to deliver unified business value.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Cross-Functional Collaboration concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Cross-Functional Collaboration.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Cross-Functional Collaboration tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Cross-Functional Collaboration challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Cross-Functional Collaboration across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Cross-Functional Collaboration; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-LEAD-11": EnterpriseCompetencyDefinition(
        competency_id="COMP-LEAD-11",
        name="People Leadership & Talent Mentorship",
        job_family="Leadership",
        summary="Coaches and develops high-performing teams, conducts impactful 1-on-1s, and fosters psychological safety and inclusion.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of People Leadership & Talent Mentorship concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in People Leadership & Talent Mentorship.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine People Leadership & Talent Mentorship tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex People Leadership & Talent Mentorship challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in People Leadership & Talent Mentorship across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in People Leadership & Talent Mentorship; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-FEED-12": EnterpriseCompetencyDefinition(
        competency_id="COMP-FEED-12",
        name="Radical Candor & Feedback Delivery",
        job_family="Communication",
        summary="Delivers timely, actionable, compassionate constructive feedback using the Situation-Behavior-Impact (SBI) framework.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Radical Candor & Feedback Delivery concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Radical Candor & Feedback Delivery.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Radical Candor & Feedback Delivery tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Radical Candor & Feedback Delivery challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Radical Candor & Feedback Delivery across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Radical Candor & Feedback Delivery; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-STRAT-13": EnterpriseCompetencyDefinition(
        competency_id="COMP-STRAT-13",
        name="Strategic Thinking & Business Acumen",
        job_family="Strategy",
        summary="Understands SaaS economics (LTV, CAC, NRR, Gross Margin), competitive dynamics, and long-term market trends.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Strategic Thinking & Business Acumen concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Strategic Thinking & Business Acumen.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Strategic Thinking & Business Acumen tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Strategic Thinking & Business Acumen challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Strategic Thinking & Business Acumen across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Strategic Thinking & Business Acumen; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-SALES-14": EnterpriseCompetencyDefinition(
        competency_id="COMP-SALES-14",
        name="Consultative Solution Selling",
        job_family="Sales",
        summary="Discovers customer business needs, articulates ROI, and manages multi-stakeholder enterprise procurement negotiations.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Consultative Solution Selling concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Consultative Solution Selling.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Consultative Solution Selling tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Consultative Solution Selling challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Consultative Solution Selling across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Consultative Solution Selling; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-CS-15": EnterpriseCompetencyDefinition(
        competency_id="COMP-CS-15",
        name="Customer Retention & Value Realization",
        job_family="Customer Success",
        summary="Drives customer onboarding adoption, minimizes churn, and identifies expansion opportunities to maximize Net Retention Rate.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Customer Retention & Value Realization concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Customer Retention & Value Realization.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Customer Retention & Value Realization tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Customer Retention & Value Realization challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Customer Retention & Value Realization across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Customer Retention & Value Realization; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-MKTG-16": EnterpriseCompetencyDefinition(
        competency_id="COMP-MKTG-16",
        name="Growth & Demand Generation",
        job_family="Marketing",
        summary="Architects multi-channel acquisition funnels, optimizes conversion metrics, and builds brand authority in the enterprise SaaS market.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Growth & Demand Generation concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Growth & Demand Generation.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Growth & Demand Generation tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Growth & Demand Generation challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Growth & Demand Generation across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Growth & Demand Generation; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-FIN-17": EnterpriseCompetencyDefinition(
        competency_id="COMP-FIN-17",
        name="Financial Modeling & Budget Stewardship",
        job_family="Finance",
        summary="Constructs rigorous FP&A financial projections, manages departmental cost centers, and ensures capital allocation efficiency.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Financial Modeling & Budget Stewardship concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Financial Modeling & Budget Stewardship.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Financial Modeling & Budget Stewardship tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Financial Modeling & Budget Stewardship challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Financial Modeling & Budget Stewardship across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Financial Modeling & Budget Stewardship; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-LEGAL-18": EnterpriseCompetencyDefinition(
        competency_id="COMP-LEGAL-18",
        name="Regulatory Compliance & Risk Governance",
        job_family="Legal",
        summary="Navigates international labor standards, data privacy laws (GDPR/CCPA), intellectual property protection, and SOC2/ISO audit controls.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Regulatory Compliance & Risk Governance concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Regulatory Compliance & Risk Governance.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Regulatory Compliance & Risk Governance tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Regulatory Compliance & Risk Governance challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Regulatory Compliance & Risk Governance across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Regulatory Compliance & Risk Governance; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-DECIS-19": EnterpriseCompetencyDefinition(
        competency_id="COMP-DECIS-19",
        name="Data-Driven Decision Making",
        job_family="Analytics",
        summary="Leverages quantitative data, statistical significance, and telemetry metrics to make unbiased, high-impact business choices.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Data-Driven Decision Making concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Data-Driven Decision Making.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Data-Driven Decision Making tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Data-Driven Decision Making challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Data-Driven Decision Making across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Data-Driven Decision Making; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
    "COMP-CRISIS-20": EnterpriseCompetencyDefinition(
        competency_id="COMP-CRISIS-20",
        name="Crisis Management & Organizational Resilience",
        job_family="Operations",
        summary="Maintains composure, clear communication, and decisive leadership during system outages, security breaches, or market turbulence.",
        levels=[
            CompetencyProficiencyLevel(1, "Foundational", ["Demonstrates basic understanding of Crisis Management & Organizational Resilience concepts.", "Requires regular oversight and guidance from senior peers.", "Applies standard tools and templates without deep customization."], ["Complete introductory certification in Crisis Management & Organizational Resilience.", "Shadow senior team member on real-world deliverable."]),
            CompetencyProficiencyLevel(2, "Developing", ["Executes routine Crisis Management & Organizational Resilience tasks independently.", "Identifies common bottlenecks and applies known resolution patterns.", "Collaborates effectively with immediate team members."], ["Lead a mid-sized operational project.", "Present findings at department sprint review."]),
            CompetencyProficiencyLevel(3, "Proficient", ["Consistently delivers high-quality outcomes across complex Crisis Management & Organizational Resilience challenges.", "Mentors junior colleagues and documents best practices.", "Proactively optimizes workflows and reduces cycle times."], ["Own end-to-end domain deliverable.", "Author team-wide architectural guidelines."]),
            CompetencyProficiencyLevel(4, "Advanced", ["Recognized subject matter expert in Crisis Management & Organizational Resilience across the department.", "Anticipates architectural and organizational risks 6-12 months in advance.", "Drives cross-functional initiatives and strategic pivots."], ["Sponsor cross-departmental technical working group.", "Lead external vendor / partner evaluation."]),
            CompetencyProficiencyLevel(5, "Expert", ["Industry-leading visionary in Crisis Management & Organizational Resilience; sets company-wide standards.", "Aligns multi-year technical roadmap with board-level business strategy.", "Mentors directors and principals; shapes external community standards."], ["Publish whitepapers / speak at global industry conferences.", "Design multi-year organizational transformation."]),
        ]
    ),
}

class CompetencyFrameworkService:
    @classmethod
    def get_competency(cls, competency_id: str) -> EnterpriseCompetencyDefinition:
        return MASTER_COMPETENCY_REGISTRY.get(competency_id)

    @classmethod
    def get_competencies_by_family(cls, family: str) -> List[EnterpriseCompetencyDefinition]:
        return [c for c in MASTER_COMPETENCY_REGISTRY.values() if family.lower() in c.job_family.lower()]

    @classmethod
    def get_all_competencies(cls) -> List[EnterpriseCompetencyDefinition]:
        return list(MASTER_COMPETENCY_REGISTRY.values())
