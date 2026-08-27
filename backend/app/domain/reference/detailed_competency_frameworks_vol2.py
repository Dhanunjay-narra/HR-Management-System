"""
Enterprise Competency Architecture Volume 2 (Advanced & Specialized Capabilities)
Extends the competency library with modern MLOps, FinOps, Lakehouse, and SLSA supply chain skills.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class AdvancedCompetencyRecord:
    code: str
    name: str
    job_family: str
    summary: str
    observable_behaviors: List[str]


ADVANCED_COMPETENCY_REGISTRY: Dict[str, AdvancedCompetencyRecord] = {
    "COMP-DATA-ARCH": AdvancedCompetencyRecord(
        code="COMP-DATA-ARCH",
        name="Enterprise Data Architecture & Lakehouse Governance",
        job_family="Data Engineering",
        summary="Designs scalable lakehouse architectures using Apache Iceberg/Delta Lake with column-level access controls.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in Enterprise Data Architecture & Lakehouse Governance.",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
    "COMP-STREAM": AdvancedCompetencyRecord(
        code="COMP-STREAM",
        name="Real-Time Event Stream Processing",
        job_family="Data Engineering",
        summary="Architects low-latency streaming pipelines with Kafka, Apache Flink, and schema registries with exactly-once semantics.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in Real-Time Event Stream Processing.",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
    "COMP-ML-OPS": AdvancedCompetencyRecord(
        code="COMP-ML-OPS",
        name="MLOps & Continuous Model Delivery",
        job_family="AI/ML",
        summary="Automates model training, feature store registration (Feast), canary deployment, and drift monitoring.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in MLOps & Continuous Model Delivery.",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
    "COMP-LLM-RAG": AdvancedCompetencyRecord(
        code="COMP-LLM-RAG",
        name="LLM Evaluation, RAG & Vector Retrieval",
        job_family="AI/ML",
        summary="Builds hybrid retrieval pipelines combining sparse BM25 with dense embeddings and cross-encoder re-ranking.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in LLM Evaluation, RAG & Vector Retrieval.",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
    "COMP-FINOPS": AdvancedCompetencyRecord(
        code="COMP-FINOPS",
        name="Cloud FinOps & Infrastructure Unit Economics",
        job_family="Operations",
        summary="Analyzes AWS/GCP cost allocation tags, implements spot instance strategies, and tracks gross margin impact.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in Cloud FinOps & Infrastructure Unit Economics.",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
    "COMP-CHAOS": AdvancedCompetencyRecord(
        code="COMP-CHAOS",
        name="Chaos Engineering & Fault Injection",
        job_family="SRE",
        summary="Conducts controlled game days and automated chaos experiments using LitmusChaos/Chaos Mesh to validate blast radius.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in Chaos Engineering & Fault Injection.",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
    "COMP-IAM-GOV": AdvancedCompetencyRecord(
        code="COMP-IAM-GOV",
        name="Identity Governance & Privilege Access Management (PAM)",
        job_family="Security",
        summary="Governs zero-standing-privilege access workflows, ephemeral JIT credentials, and continuous access evaluation.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in Identity Governance & Privilege Access Management (PAM).",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
    "COMP-APPSEC": AdvancedCompetencyRecord(
        code="COMP-APPSEC",
        name="Software Supply Chain Security (SLSA)",
        job_family="Security",
        summary="Enforces cryptographic artifact signing with Sigstore/Cosign, automated SBOM generation, and dependency pinning.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in Software Supply Chain Security (SLSA).",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
    "COMP-DESIGN-SYS": AdvancedCompetencyRecord(
        code="COMP-DESIGN-SYS",
        name="Multi-Brand Design Token Architecture",
        job_family="Product Design",
        summary="Scales Figma-to-code design token pipelines supporting light/dark themes and WCAG AAA contrast accessibility.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in Multi-Brand Design Token Architecture.",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
    "COMP-EXP-SALES": AdvancedCompetencyRecord(
        code="COMP-EXP-SALES",
        name="Strategic Expansion & Enterprise Upselling",
        job_family="Sales & CS",
        summary="Identifies expansion use cases, negotiates multi-year master service agreements (MSAs), and expands ARR.",
        observable_behaviors=[
            "Demonstrates subject matter expertise in Strategic Expansion & Enterprise Upselling.",
            "Authors team-wide architectural guidelines and technical specifications.",
            "Conducts knowledge sharing sessions and mentors cross-functional team members.",
        ]
    ),
}

class AdvancedCompetencyService:
    @classmethod
    def get_competency(cls, code: str) -> AdvancedCompetencyRecord:
        return ADVANCED_COMPETENCY_REGISTRY.get(code)

    @classmethod
    def get_all(cls) -> List[AdvancedCompetencyRecord]:
        return list(ADVANCED_COMPETENCY_REGISTRY.values())
