"""
Enterprise Master Job Architecture Catalog Volume 2 (Specialized Technical & Leadership Roles)
Extends the job catalog with specialized distributed systems, AI safety, FinOps, and mobile engineering profiles.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class SpecializedJobProfile:
    job_code: str
    job_title: str
    department: str
    grade_level: str
    min_experience_years: int
    target_salary_min_usd: float
    target_salary_mid_usd: float
    target_salary_max_usd: float
    annual_target_bonus_pct: float
    annual_rsu_target_shares: int
    core_competencies: List[str]
    key_responsibilities: List[str]


SPECIALIZED_JOB_CATALOG_DATA: Dict[str, SpecializedJobProfile] = {
    "SRE_ARCH": SpecializedJobProfile(
        job_code="SRE_ARCH",
        job_title="Site Reliability Architecture & Chaos Engineering",
        department="Engineering",
        grade_level="L5",
        min_experience_years=8,
        target_salary_min_usd=210000.0,
        target_salary_mid_usd=245000.0,
        target_salary_max_usd=285000.0,
        annual_target_bonus_pct=0.2,
        annual_rsu_target_shares=2500,
        core_competencies=["Site Reliability Architecture & Chaos Engineering Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in Engineering.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "RUST_CORE": SpecializedJobProfile(
        job_code="RUST_CORE",
        job_title="Rust High-Performance Systems Core Engineer",
        department="Engineering",
        grade_level="L4",
        min_experience_years=6,
        target_salary_min_usd=175000.0,
        target_salary_mid_usd=205000.0,
        target_salary_max_usd=235000.0,
        annual_target_bonus_pct=0.15,
        annual_rsu_target_shares=1500,
        core_competencies=["Rust High-Performance Systems Core Engineer Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in Engineering.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "GO_PLATFORM": SpecializedJobProfile(
        job_code="GO_PLATFORM",
        job_title="Go Distributed Microservices Platform Engineer",
        department="Engineering",
        grade_level="L4",
        min_experience_years=5,
        target_salary_min_usd=170000.0,
        target_salary_mid_usd=195000.0,
        target_salary_max_usd=225000.0,
        annual_target_bonus_pct=0.15,
        annual_rsu_target_shares=1200,
        core_competencies=["Go Distributed Microservices Platform Engineer Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in Engineering.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "IOS_STAFF": SpecializedJobProfile(
        job_code="IOS_STAFF",
        job_title="Staff iOS Applications Architect (Swift/SwiftUI)",
        department="Mobile Engineering",
        grade_level="L5",
        min_experience_years=8,
        target_salary_min_usd=200000.0,
        target_salary_mid_usd=230000.0,
        target_salary_max_usd=265000.0,
        annual_target_bonus_pct=0.2,
        annual_rsu_target_shares=2200,
        core_competencies=["Staff iOS Applications Architect (Swift/SwiftUI) Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in Mobile Engineering.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "AND_STAFF": SpecializedJobProfile(
        job_code="AND_STAFF",
        job_title="Staff Android Platform Architect (Kotlin/Compose)",
        department="Mobile Engineering",
        grade_level="L5",
        min_experience_years=8,
        target_salary_min_usd=200000.0,
        target_salary_mid_usd=230000.0,
        target_salary_max_usd=265000.0,
        annual_target_bonus_pct=0.2,
        annual_rsu_target_shares=2200,
        core_competencies=["Staff Android Platform Architect (Kotlin/Compose) Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in Mobile Engineering.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "MLOPS_LEAD": SpecializedJobProfile(
        job_code="MLOPS_LEAD",
        job_title="Lead MLOps Infrastructure & Model Serving Engineer",
        department="AI/ML",
        grade_level="L5",
        min_experience_years=8,
        target_salary_min_usd=205000.0,
        target_salary_mid_usd=240000.0,
        target_salary_max_usd=275000.0,
        annual_target_bonus_pct=0.2,
        annual_rsu_target_shares=2400,
        core_competencies=["Lead MLOps Infrastructure & Model Serving Engineer Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in AI/ML.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "AI_SAFETY": SpecializedJobProfile(
        job_code="AI_SAFETY",
        job_title="AI Safety, Evaluation & Guardrail Specialist",
        department="AI/ML",
        grade_level="L4",
        min_experience_years=5,
        target_salary_min_usd=165000.0,
        target_salary_mid_usd=190000.0,
        target_salary_max_usd=220000.0,
        annual_target_bonus_pct=0.15,
        annual_rsu_target_shares=1200,
        core_competencies=["AI Safety, Evaluation & Guardrail Specialist Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in AI/ML.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "FINOPS_LEAD": SpecializedJobProfile(
        job_code="FINOPS_LEAD",
        job_title="Cloud FinOps & Infrastructure Unit Economics Lead",
        department="Finance & IT",
        grade_level="L4",
        min_experience_years=6,
        target_salary_min_usd=155000.0,
        target_salary_mid_usd=180000.0,
        target_salary_max_usd=210000.0,
        annual_target_bonus_pct=0.15,
        annual_rsu_target_shares=1000,
        core_competencies=["Cloud FinOps & Infrastructure Unit Economics Lead Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in Finance & IT.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "SOC_LEAD": SpecializedJobProfile(
        job_code="SOC_LEAD",
        job_title="Security Operations Center (SOC) Incident Commander",
        department="Security",
        grade_level="L4",
        min_experience_years=6,
        target_salary_min_usd=160000.0,
        target_salary_mid_usd=185000.0,
        target_salary_max_usd=215000.0,
        annual_target_bonus_pct=0.15,
        annual_rsu_target_shares=1000,
        core_competencies=["Security Operations Center (SOC) Incident Commander Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in Security.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "PRIVACY_ENG": SpecializedJobProfile(
        job_code="PRIVACY_ENG",
        job_title="Lead Privacy & Data Governance Engineer",
        department="Security & Legal",
        grade_level="L4",
        min_experience_years=6,
        target_salary_min_usd=165000.0,
        target_salary_mid_usd=190000.0,
        target_salary_max_usd=220000.0,
        annual_target_bonus_pct=0.15,
        annual_rsu_target_shares=1100,
        core_competencies=["Lead Privacy & Data Governance Engineer Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in Security & Legal.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "COMP_DIR": SpecializedJobProfile(
        job_code="COMP_DIR",
        job_title="Director of Global Compensation & Equity Planning",
        department="Total Rewards",
        grade_level="D1",
        min_experience_years=12,
        target_salary_min_usd=230000.0,
        target_salary_mid_usd=270000.0,
        target_salary_max_usd=315000.0,
        annual_target_bonus_pct=0.3,
        annual_rsu_target_shares=5000,
        core_competencies=["Director of Global Compensation & Equity Planning Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in Total Rewards.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
    "DEI_DIR": SpecializedJobProfile(
        job_code="DEI_DIR",
        job_title="Director of Diversity, Inclusion & Belonging",
        department="People & Culture",
        grade_level="D1",
        min_experience_years=10,
        target_salary_min_usd=210000.0,
        target_salary_mid_usd=245000.0,
        target_salary_max_usd=285000.0,
        annual_target_bonus_pct=0.25,
        annual_rsu_target_shares=4000,
        core_competencies=["Director of Diversity, Inclusion & Belonging Mastery", "Enterprise Reliability", "Scalable System Design"],
        key_responsibilities=[
            "Lead high-impact architectural initiatives in People & Culture.",
            "Ensure strict adherence to enterprise security, performance, and compliance standards.",
            "Mentor senior engineers and collaborate cross-functionally with executive leaders.",
        ]
    ),
}

class SpecializedJobCatalogService:
    @classmethod
    def get_role(cls, code: str) -> SpecializedJobProfile:
        return SPECIALIZED_JOB_CATALOG_DATA.get(code)

    @classmethod
    def get_all_specialized_roles(cls) -> List[SpecializedJobProfile]:
        return list(SPECIALIZED_JOB_CATALOG_DATA.values())
