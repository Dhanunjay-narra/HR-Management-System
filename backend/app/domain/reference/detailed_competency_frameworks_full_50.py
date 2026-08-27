"""
Enterprise Master 50-Competency Architecture Framework (Complete Multi-Level Definitions)
Defines 5 proficiency tiers with behavioral indicators and milestones across engineering, leadership, product, sales, and operations.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class FullCompetencyTier:
    tier_level: int
    tier_title: str
    behavioral_indicators: List[str]
    developmental_milestones: List[str]


@dataclass
class MasterCompetencyRecord:
    competency_code: str
    competency_name: str
    job_family: str
    definition_summary: str
    tiers: List[FullCompetencyTier]


MASTER_50_COMPETENCIES_DATA: Dict[str, MasterCompetencyRecord] = {
    "COMP-ENG-01": MasterCompetencyRecord(
        competency_code="COMP-ENG-01",
        competency_name="Distributed System Resiliency & Fault Tolerance",
        job_family="Engineering & Technology",
        definition_summary="Mastery of Distributed System Resiliency & Fault Tolerance principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Distributed System Resiliency & Fault Tolerance concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Distributed System Resiliency & Fault Tolerance tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Distributed System Resiliency & Fault Tolerance outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-ENG-02": MasterCompetencyRecord(
        competency_code="COMP-ENG-02",
        competency_name="Clean Code Architecture & Domain-Driven Design",
        job_family="Engineering & Technology",
        definition_summary="Mastery of Clean Code Architecture & Domain-Driven Design principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Clean Code Architecture & Domain-Driven Design concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Clean Code Architecture & Domain-Driven Design tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Clean Code Architecture & Domain-Driven Design outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-ENG-03": MasterCompetencyRecord(
        competency_code="COMP-ENG-03",
        competency_name="Database Query Optimization & Partitioning",
        job_family="Engineering & Technology",
        definition_summary="Mastery of Database Query Optimization & Partitioning principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Database Query Optimization & Partitioning concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Database Query Optimization & Partitioning tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Database Query Optimization & Partitioning outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-ENG-04": MasterCompetencyRecord(
        competency_code="COMP-ENG-04",
        competency_name="Asynchronous Event Sourcing & Messaging",
        job_family="Engineering & Technology",
        definition_summary="Mastery of Asynchronous Event Sourcing & Messaging principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Asynchronous Event Sourcing & Messaging concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Asynchronous Event Sourcing & Messaging tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Asynchronous Event Sourcing & Messaging outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-ENG-05": MasterCompetencyRecord(
        competency_code="COMP-ENG-05",
        competency_name="Site Reliability Engineering & SLO Observability",
        job_family="Engineering & Technology",
        definition_summary="Mastery of Site Reliability Engineering & SLO Observability principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Site Reliability Engineering & SLO Observability concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Site Reliability Engineering & SLO Observability tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Site Reliability Engineering & SLO Observability outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-ENG-06": MasterCompetencyRecord(
        competency_code="COMP-ENG-06",
        competency_name="Application Security & Threat Modeling",
        job_family="Engineering & Technology",
        definition_summary="Mastery of Application Security & Threat Modeling principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Application Security & Threat Modeling concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Application Security & Threat Modeling tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Application Security & Threat Modeling outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-ENG-07": MasterCompetencyRecord(
        competency_code="COMP-ENG-07",
        competency_name="Cloud Infrastructure Automation & Terraform",
        job_family="Engineering & Technology",
        definition_summary="Mastery of Cloud Infrastructure Automation & Terraform principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Cloud Infrastructure Automation & Terraform concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Cloud Infrastructure Automation & Terraform tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Cloud Infrastructure Automation & Terraform outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-ENG-08": MasterCompetencyRecord(
        competency_code="COMP-ENG-08",
        competency_name="Modern Frontend Architecture & Web Performance",
        job_family="Engineering & Technology",
        definition_summary="Mastery of Modern Frontend Architecture & Web Performance principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Modern Frontend Architecture & Web Performance concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Modern Frontend Architecture & Web Performance tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Modern Frontend Architecture & Web Performance outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-ENG-09": MasterCompetencyRecord(
        competency_code="COMP-ENG-09",
        competency_name="Applied Machine Learning & Vector Search",
        job_family="Engineering & Technology",
        definition_summary="Mastery of Applied Machine Learning & Vector Search principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Applied Machine Learning & Vector Search concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Applied Machine Learning & Vector Search tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Applied Machine Learning & Vector Search outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-ENG-10": MasterCompetencyRecord(
        competency_code="COMP-ENG-10",
        competency_name="CI/CD Pipeline Security & Container Hardening",
        job_family="Engineering & Technology",
        definition_summary="Mastery of CI/CD Pipeline Security & Container Hardening principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline CI/CD Pipeline Security & Container Hardening concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine CI/CD Pipeline Security & Container Hardening tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality CI/CD Pipeline Security & Container Hardening outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-01": MasterCompetencyRecord(
        competency_code="COMP-PROD-01",
        competency_name="Product Discovery & Hypothesis Validation",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of Product Discovery & Hypothesis Validation principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Product Discovery & Hypothesis Validation concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Product Discovery & Hypothesis Validation tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Product Discovery & Hypothesis Validation outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-02": MasterCompetencyRecord(
        competency_code="COMP-PROD-02",
        competency_name="Quantitative Telemetry & Funnel Analysis",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of Quantitative Telemetry & Funnel Analysis principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Quantitative Telemetry & Funnel Analysis concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Quantitative Telemetry & Funnel Analysis tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Quantitative Telemetry & Funnel Analysis outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-03": MasterCompetencyRecord(
        competency_code="COMP-PROD-03",
        competency_name="Enterprise Roadmap Prioritization & ROI",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of Enterprise Roadmap Prioritization & ROI principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Enterprise Roadmap Prioritization & ROI concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Enterprise Roadmap Prioritization & ROI tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Enterprise Roadmap Prioritization & ROI outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-04": MasterCompetencyRecord(
        competency_code="COMP-PROD-04",
        competency_name="Design Token Systems & UI Accessibility",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of Design Token Systems & UI Accessibility principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Design Token Systems & UI Accessibility concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Design Token Systems & UI Accessibility tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Design Token Systems & UI Accessibility outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-05": MasterCompetencyRecord(
        competency_code="COMP-PROD-05",
        competency_name="User Experience Research & Persona Mapping",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of User Experience Research & Persona Mapping principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline User Experience Research & Persona Mapping concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine User Experience Research & Persona Mapping tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality User Experience Research & Persona Mapping outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-06": MasterCompetencyRecord(
        competency_code="COMP-PROD-06",
        competency_name="Technical Writing & Developer Documentation",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of Technical Writing & Developer Documentation principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Technical Writing & Developer Documentation concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Technical Writing & Developer Documentation tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Technical Writing & Developer Documentation outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-07": MasterCompetencyRecord(
        competency_code="COMP-PROD-07",
        competency_name="Competitive Intelligence & Market Positioning",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of Competitive Intelligence & Market Positioning principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Competitive Intelligence & Market Positioning concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Competitive Intelligence & Market Positioning tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Competitive Intelligence & Market Positioning outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-08": MasterCompetencyRecord(
        competency_code="COMP-PROD-08",
        competency_name="A/B Testing & Statistical Experimentation",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of A/B Testing & Statistical Experimentation principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline A/B Testing & Statistical Experimentation concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine A/B Testing & Statistical Experimentation tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality A/B Testing & Statistical Experimentation outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-09": MasterCompetencyRecord(
        competency_code="COMP-PROD-09",
        competency_name="Pricing, Packaging & SaaS Unit Economics",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of Pricing, Packaging & SaaS Unit Economics principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Pricing, Packaging & SaaS Unit Economics concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Pricing, Packaging & SaaS Unit Economics tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Pricing, Packaging & SaaS Unit Economics outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-PROD-10": MasterCompetencyRecord(
        competency_code="COMP-PROD-10",
        competency_name="Cross-Functional Release Management",
        job_family="Product, Design & Analytics",
        definition_summary="Mastery of Cross-Functional Release Management principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Cross-Functional Release Management concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Cross-Functional Release Management tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Cross-Functional Release Management outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-01": MasterCompetencyRecord(
        competency_code="COMP-LDR-01",
        competency_name="People Leadership & High-Performance Coaching",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of People Leadership & High-Performance Coaching principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline People Leadership & High-Performance Coaching concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine People Leadership & High-Performance Coaching tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality People Leadership & High-Performance Coaching outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-02": MasterCompetencyRecord(
        competency_code="COMP-LDR-02",
        competency_name="Radical Candor & Constructive Feedback",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of Radical Candor & Constructive Feedback principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Radical Candor & Constructive Feedback concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Radical Candor & Constructive Feedback tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Radical Candor & Constructive Feedback outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-03": MasterCompetencyRecord(
        competency_code="COMP-LDR-03",
        competency_name="Strategic Vision & Executive Communication",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of Strategic Vision & Executive Communication principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Strategic Vision & Executive Communication concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Strategic Vision & Executive Communication tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Strategic Vision & Executive Communication outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-04": MasterCompetencyRecord(
        competency_code="COMP-LDR-04",
        competency_name="Psychological Safety & Inclusive Team Culture",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of Psychological Safety & Inclusive Team Culture principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Psychological Safety & Inclusive Team Culture concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Psychological Safety & Inclusive Team Culture tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Psychological Safety & Inclusive Team Culture outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-05": MasterCompetencyRecord(
        competency_code="COMP-LDR-05",
        competency_name="Talent Sourcing & Interview Rigor",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of Talent Sourcing & Interview Rigor principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Talent Sourcing & Interview Rigor concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Talent Sourcing & Interview Rigor tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Talent Sourcing & Interview Rigor outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-06": MasterCompetencyRecord(
        competency_code="COMP-LDR-06",
        competency_name="Conflict Resolution & Alignment Building",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of Conflict Resolution & Alignment Building principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Conflict Resolution & Alignment Building concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Conflict Resolution & Alignment Building tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Conflict Resolution & Alignment Building outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-07": MasterCompetencyRecord(
        competency_code="COMP-LDR-07",
        competency_name="Organizational Design & Span of Control",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of Organizational Design & Span of Control principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Organizational Design & Span of Control concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Organizational Design & Span of Control tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Organizational Design & Span of Control outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-08": MasterCompetencyRecord(
        competency_code="COMP-LDR-08",
        competency_name="Crisis Leadership & Incident Command",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of Crisis Leadership & Incident Command principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Crisis Leadership & Incident Command concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Crisis Leadership & Incident Command tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Crisis Leadership & Incident Command outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-09": MasterCompetencyRecord(
        competency_code="COMP-LDR-09",
        competency_name="Budget Stewardship & Resource Allocation",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of Budget Stewardship & Resource Allocation principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Budget Stewardship & Resource Allocation concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Budget Stewardship & Resource Allocation tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Budget Stewardship & Resource Allocation outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-LDR-10": MasterCompetencyRecord(
        competency_code="COMP-LDR-10",
        competency_name="Succession Planning & Bench Strength Development",
        job_family="Leadership, Management & Culture",
        definition_summary="Mastery of Succession Planning & Bench Strength Development principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Succession Planning & Bench Strength Development concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Succession Planning & Bench Strength Development tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Succession Planning & Bench Strength Development outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-01": MasterCompetencyRecord(
        competency_code="COMP-GTM-01",
        competency_name="Enterprise Consultative Value Selling",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of Enterprise Consultative Value Selling principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Enterprise Consultative Value Selling concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Enterprise Consultative Value Selling tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Enterprise Consultative Value Selling outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-02": MasterCompetencyRecord(
        competency_code="COMP-GTM-02",
        competency_name="MEDDPICC Opportunity Qualification",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of MEDDPICC Opportunity Qualification principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline MEDDPICC Opportunity Qualification concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine MEDDPICC Opportunity Qualification tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality MEDDPICC Opportunity Qualification outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-03": MasterCompetencyRecord(
        competency_code="COMP-GTM-03",
        competency_name="Customer Onboarding & Value Realization",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of Customer Onboarding & Value Realization principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Customer Onboarding & Value Realization concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Customer Onboarding & Value Realization tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Customer Onboarding & Value Realization outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-04": MasterCompetencyRecord(
        competency_code="COMP-GTM-04",
        competency_name="Gross & Net Revenue Retention Optimization",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of Gross & Net Revenue Retention Optimization principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Gross & Net Revenue Retention Optimization concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Gross & Net Revenue Retention Optimization tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Gross & Net Revenue Retention Optimization outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-05": MasterCompetencyRecord(
        competency_code="COMP-GTM-05",
        competency_name="Product Marketing & Feature Launch Orchestration",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of Product Marketing & Feature Launch Orchestration principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Product Marketing & Feature Launch Orchestration concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Product Marketing & Feature Launch Orchestration tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Product Marketing & Feature Launch Orchestration outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-06": MasterCompetencyRecord(
        competency_code="COMP-GTM-06",
        competency_name="Multi-Channel Demand Generation",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of Multi-Channel Demand Generation principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Multi-Channel Demand Generation concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Multi-Channel Demand Generation tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Multi-Channel Demand Generation outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-07": MasterCompetencyRecord(
        competency_code="COMP-GTM-07",
        competency_name="Contract Negotiation & Executive Procurement",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of Contract Negotiation & Executive Procurement principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Contract Negotiation & Executive Procurement concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Contract Negotiation & Executive Procurement tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Contract Negotiation & Executive Procurement outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-08": MasterCompetencyRecord(
        competency_code="COMP-GTM-08",
        competency_name="Technical Solutions Engineering & POC Delivery",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of Technical Solutions Engineering & POC Delivery principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Technical Solutions Engineering & POC Delivery concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Technical Solutions Engineering & POC Delivery tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Technical Solutions Engineering & POC Delivery outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-09": MasterCompetencyRecord(
        competency_code="COMP-GTM-09",
        competency_name="Account Management & Strategic Upselling",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of Account Management & Strategic Upselling principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Account Management & Strategic Upselling concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Account Management & Strategic Upselling tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Account Management & Strategic Upselling outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-GTM-10": MasterCompetencyRecord(
        competency_code="COMP-GTM-10",
        competency_name="Partner Ecosystem & Channel Strategy",
        job_family="Sales, Marketing & Customer Success",
        definition_summary="Mastery of Partner Ecosystem & Channel Strategy principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Partner Ecosystem & Channel Strategy concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Partner Ecosystem & Channel Strategy tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Partner Ecosystem & Channel Strategy outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-01": MasterCompetencyRecord(
        competency_code="COMP-OPS-01",
        competency_name="Financial Planning & Analysis (FP&A) Modeling",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Financial Planning & Analysis (FP&A) Modeling principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Financial Planning & Analysis (FP&A) Modeling concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Financial Planning & Analysis (FP&A) Modeling tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Financial Planning & Analysis (FP&A) Modeling outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-02": MasterCompetencyRecord(
        competency_code="COMP-OPS-02",
        competency_name="Corporate General Ledger & Double-Entry Accounting",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Corporate General Ledger & Double-Entry Accounting principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Corporate General Ledger & Double-Entry Accounting concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Corporate General Ledger & Double-Entry Accounting tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Corporate General Ledger & Double-Entry Accounting outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-03": MasterCompetencyRecord(
        competency_code="COMP-OPS-03",
        competency_name="Total Rewards & Compensation Architecture",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Total Rewards & Compensation Architecture principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Total Rewards & Compensation Architecture concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Total Rewards & Compensation Architecture tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Total Rewards & Compensation Architecture outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-04": MasterCompetencyRecord(
        competency_code="COMP-OPS-04",
        competency_name="Statutory Labor Standards & Compliance Governance",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Statutory Labor Standards & Compliance Governance principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Statutory Labor Standards & Compliance Governance concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Statutory Labor Standards & Compliance Governance tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Statutory Labor Standards & Compliance Governance outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-05": MasterCompetencyRecord(
        competency_code="COMP-OPS-05",
        competency_name="Data Privacy & GDPR/CCPA Compliance",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Data Privacy & GDPR/CCPA Compliance principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Data Privacy & GDPR/CCPA Compliance concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Data Privacy & GDPR/CCPA Compliance tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Data Privacy & GDPR/CCPA Compliance outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-06": MasterCompetencyRecord(
        competency_code="COMP-OPS-06",
        competency_name="Global Benefits & Healthcare Plan Administration",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Global Benefits & Healthcare Plan Administration principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Global Benefits & Healthcare Plan Administration concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Global Benefits & Healthcare Plan Administration tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Global Benefits & Healthcare Plan Administration outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-07": MasterCompetencyRecord(
        competency_code="COMP-OPS-07",
        competency_name="Corporate Immigration & Work Authorization",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Corporate Immigration & Work Authorization principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Corporate Immigration & Work Authorization concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Corporate Immigration & Work Authorization tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Corporate Immigration & Work Authorization outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-08": MasterCompetencyRecord(
        competency_code="COMP-OPS-08",
        competency_name="Employee Relations & Workplace Investigations",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Employee Relations & Workplace Investigations principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Employee Relations & Workplace Investigations concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Employee Relations & Workplace Investigations tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Employee Relations & Workplace Investigations outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-09": MasterCompetencyRecord(
        competency_code="COMP-OPS-09",
        competency_name="Equity Compensation & Stock Option Valuations",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Equity Compensation & Stock Option Valuations principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Equity Compensation & Stock Option Valuations concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Equity Compensation & Stock Option Valuations tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Equity Compensation & Stock Option Valuations outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
    "COMP-OPS-10": MasterCompetencyRecord(
        competency_code="COMP-OPS-10",
        competency_name="Enterprise Risk Management & Internal Audit",
        job_family="Finance, Legal & People Operations",
        definition_summary="Mastery of Enterprise Risk Management & Internal Audit principles, methodologies, and cross-functional leadership.",
        tiers=[
            FullCompetencyTier(1, "Foundational", ["Understands baseline Enterprise Risk Management & Internal Audit concepts.", "Applies standard tools with guidance."], ["Complete foundational certification.", "Shadow senior peer on production deliverable."]),
            FullCompetencyTier(2, "Developing", ["Executes routine Enterprise Risk Management & Internal Audit tasks independently.", "Solves standard technical trade-offs."], ["Lead a mid-scale sprint deliverable.", "Present at team sync."]),
            FullCompetencyTier(3, "Proficient", ["Consistently delivers high-quality Enterprise Risk Management & Internal Audit outcomes.", "Mentors junior engineers."], ["Own a critical domain microservice.", "Draft team best practice guidelines."]),
            FullCompetencyTier(4, "Advanced", ["Subject matter expert across department.", "Anticipates architectural and operational bottlenecks."], ["Lead cross-team technical working group.", "Author architectural RFCs."]),
            FullCompetencyTier(5, "Expert / Visionary", ["Sets company-wide industry standards.", "Influences multi-year company strategy."], ["Keynote at global industry conferences.", "Design multi-year organizational architecture."]),
        ]
    ),
}

class MasterCompetencyService:
    @classmethod
    def get_competency(cls, code: str) -> MasterCompetencyRecord:
        return MASTER_50_COMPETENCIES_DATA.get(code)

    @classmethod
    def get_all(cls) -> List[MasterCompetencyRecord]:
        return list(MASTER_50_COMPETENCIES_DATA.values())
