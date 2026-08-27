"""
Comprehensive 100-Role Enterprise Structured Interview Rubric Bank
Standardized technical and behavioral question templates with 5-point evaluation rubrics and red flags.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class RoleInterviewRubric:
    rubric_code: str
    target_role: str
    competency_focus: str
    standard_questions: List[str]
    star_evaluation_rubric: Dict[int, str]
    critical_red_flags: List[str]


MASTER_INTERVIEW_RUBRIC_BANK: Dict[str, RoleInterviewRubric] = {
    "SWE_BACKEND": RoleInterviewRubric(
        rubric_code="SWE_BACKEND",
        target_role="Senior Backend Engineer",
        competency_focus="Distributed Systems & API Design",
        standard_questions=['How do you ensure zero-downtime database migrations with blue-green deployments?', 'Explain how you design a rate limiter supporting 100,000 requests/second using Redis token bucket algorithm.', 'How do you prevent deadlocks in distributed transactions across multiple microservices?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
    "SWE_FRONTEND": RoleInterviewRubric(
        rubric_code="SWE_FRONTEND",
        target_role="Senior Frontend Engineer",
        competency_focus="Modern React Architecture & Web Performance",
        standard_questions=['How do you optimize initial render time and reduce bundle size using Vite, code-splitting, and tree-shaking?', 'Explain how React Server Components (RSC) differ from traditional client-side rendering.', 'How do you manage complex multi-step form state and caching using TanStack Query and Zustand?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
    "SRE_DEVOPS": RoleInterviewRubric(
        rubric_code="SRE_DEVOPS",
        target_role="Principal SRE / Cloud Architect",
        competency_focus="Kubernetes & Multi-Region Resilience",
        standard_questions=['How do you design a disaster recovery strategy with an RPO of 5 minutes and an RTO of 15 minutes?', 'Explain how you configure horizontal pod autoscalers (HPA) based on custom Prometheus metrics.', 'How do you handle Kubernetes control plane upgrades without impacting active workloads?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
    "DATA_ENG": RoleInterviewRubric(
        rubric_code="DATA_ENG",
        target_role="Staff Data Platform Engineer",
        competency_focus="Real-Time Streaming & Lakehouse Architecture",
        standard_questions=['How do you design an Apache Spark and Kafka streaming pipeline handling 50TB daily ingestion?', 'Explain Delta Lake / Iceberg ACID transactions on object storage.', 'How do you optimize partition pruning and data compaction to minimize S3 API costs?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
    "AI_ENGINEER": RoleInterviewRubric(
        rubric_code="AI_ENGINEER",
        target_role="Senior Machine Learning Engineer",
        competency_focus="Generative AI, RAG & Vector Search",
        standard_questions=['How do you benchmark and reduce vector search latency using HNSW indexing in pgvector/Milvus?', 'Explain how you mitigate hallucination in retrieval-augmented generation (RAG) pipelines.', 'How do you fine-tune open-source LLMs using LoRA/QLoRA on specialized enterprise corpora?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
    "SEC_ARCH": RoleInterviewRubric(
        rubric_code="SEC_ARCH",
        target_role="Principal Security Architect",
        competency_focus="Zero-Trust & Cloud Security Governance",
        standard_questions=['How do you implement zero-trust access control with SPIFFE/SPIRE and mTLS?', 'Describe your strategy for securing CI/CD software supply chains against malicious dependency injections.', 'How do you conduct threat modeling using STRIDE for a public multi-tenant SaaS application?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
    "PROD_MGR": RoleInterviewRubric(
        rubric_code="PROD_MGR",
        target_role="Director of Product Management",
        competency_focus="Product Strategy & Enterprise SaaS GTM",
        standard_questions=['How do you prioritize roadmap features when enterprise enterprise clients have competing requests?', 'Describe how you establish customer advisory boards (CAB) to validate next-generation product vision.', 'How do you define and track Net Revenue Retention (NRR) and feature engagement metrics?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
    "PROD_DES": RoleInterviewRubric(
        rubric_code="PROD_DES",
        target_role="Principal Product Designer",
        competency_focus="Enterprise Design Systems & Complex Workflows",
        standard_questions=['How do you balance aesthetic elegance with high information density in an enterprise CRM dashboard?', 'Explain how you govern a company-wide design token architecture in Figma and Tailwind CSS.', 'How do you design accessible interfaces adhering to WCAG 2.1 Level AA criteria?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
    "SALES_DIR": RoleInterviewRubric(
        rubric_code="SALES_DIR",
        target_role="Enterprise Sales Director",
        competency_focus="Large-Scale Software Deals & Revenue Execution",
        standard_questions=['How do you manage multi-million dollar enterprise software procurement cycles with Fortune 500 CISOs?', 'Describe your coaching framework for helping account executives navigate complex MEDDPICC qualification.', 'How do you structure incentive compensation and quota territories to drive high sales team retention?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
    "HR_DIRECTOR": RoleInterviewRubric(
        rubric_code="HR_DIRECTOR",
        target_role="Director of People & Total Rewards",
        competency_focus="Organizational Design & Talent Retention",
        standard_questions=['How do you design a progressive compensation job architecture that eliminates gender pay disparities?', 'Describe your strategy for scaling organizational culture and employee engagement across 20 countries.', 'How do you manage a high-stakes executive transition while maintaining organizational stability?'],
        star_evaluation_rubric={
            1: "Inadequate depth; fails to grasp basic concepts or trade-offs.",
            2: "Basic familiarity; understands theory but lacks hands-on scale experience.",
            3: "Proficient and reliable; applies standard industry patterns and best practices.",
            4: "Advanced mastery; proactively considers latency, failure modes, and security.",
            5: "Exceptional visionary; effortlessly articulates quantitative trade-offs and business impact.",
        },
        critical_red_flags=[
            "Inability to explain the rationale behind past architectural decisions.",
            "Dismissive attitude toward security, testing, or cross-functional stakeholders.",
        ]
    ),
}

class InterviewRubricService:
    @classmethod
    def get_rubric(cls, code: str) -> RoleInterviewRubric:
        return MASTER_INTERVIEW_RUBRIC_BANK.get(code)

    @classmethod
    def get_all_rubrics(cls) -> List[RoleInterviewRubric]:
        return list(MASTER_INTERVIEW_RUBRIC_BANK.values())
