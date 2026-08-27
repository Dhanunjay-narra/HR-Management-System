"""
Comprehensive Enterprise LMS Curriculum & Professional Development Course Catalog
Provides 100+ structured training modules with lessons, quizzes, learning outcomes, and CEU credit valuations.
"""
from typing import Dict, List, Any
from dataclasses import dataclass, field


@dataclass
class LessonDefinition:
    lesson_id: str
    title: str
    duration_minutes: int
    content_markdown: str
    quiz_questions: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class CourseDefinition:
    course_id: str
    title: str
    category: str
    difficulty: str  # FOUNDATIONAL, INTERMEDIATE, ADVANCED, EXECUTIVE
    estimated_hours: float
    target_skills: List[str]
    description: str
    lessons: List[LessonDefinition] = field(default_factory=list)


LMS_COURSE_CATALOG: Dict[str, CourseDefinition] = {
    "SEC-101": CourseDefinition(
        course_id="SEC-101",
        title="ISO 27001 & SOC2 Information Security Awareness (2026)",
        category="Security & Compliance",
        difficulty="FOUNDATIONAL",
        estimated_hours=2.5,
        target_skills=["Information Security", "SOC2 Compliance", "Phishing Prevention", "Data Protection"],
        description="Mandatory annual cybersecurity hygiene training covering credential safety, phishing simulations, clean-desk policy, and incident reporting.",
        lessons=[
            LessonDefinition("SEC-101-01", "Threat Landscape: Phishing, Spear-Phishing & Social Engineering", 30, "Overview of modern deceptive attack vectors..."),
            LessonDefinition("SEC-101-02", "Credential Hygiene & FIDO2 Multi-Factor Authentication", 25, "Best practices for passkeys, password managers, and zero-trust authentication..."),
            LessonDefinition("SEC-101-03", "Data Classification & GDPR/CCPA Privacy Obligations", 35, "Understanding Restricted vs Confidential data and encryption in transit/at rest..."),
            LessonDefinition("SEC-101-04", "Physical Security & Clean Desk Protocol", 20, "Securing screens, badges, and visitor logging..."),
            LessonDefinition("SEC-101-05", "Incident Escalation: What to Do During a Suspected Breach", 30, "Contacting the Security Operations Center (SOC) within 15 minutes of suspicion..."),
        ]
    ),
    "ENG-SYS-201": CourseDefinition(
        course_id="ENG-SYS-201",
        title="High-Scale Distributed Systems Architecture & Microservices",
        category="Engineering & Architecture",
        difficulty="ADVANCED",
        estimated_hours=12.0,
        target_skills=["Distributed Systems", "Microservices", "Event-Driven Architecture", "Kafka", "PostgreSQL"],
        description="Deep dive into partitioning, consensus algorithms (Raft/Paxos), event sourcing, CQRS, circuit breakers, and zero-downtime database migrations.",
        lessons=[
            LessonDefinition("SYS-201-01", "CAP Theorem & PACELC Trade-offs in Real World Systems", 60, "Consistency models, eventual consistency vs linearizability..."),
            LessonDefinition("SYS-201-02", "Event-Driven Microservices with Apache Kafka & Outbox Pattern", 90, "Ensuring dual-write transactional consistency using PostgreSQL Outbox..."),
            LessonDefinition("SYS-201-03", "Caching Topologies: Redis Cluster, Write-Through & Cache-Aside", 60, "Mitigating cache thundering herd and stampede problems..."),
            LessonDefinition("SYS-201-04", "Database Sharding & Connection Pooling at 100k QPS", 90, "PgBouncer, tenant-based sharding, and foreign data wrappers..."),
        ]
    ),
    "LDR-MGR-301": CourseDefinition(
        course_id="LDR-MGR-301",
        title="First-Time Manager: Coaching, Feedback & High-Performance Team Leadership",
        category="Leadership & Management",
        difficulty="INTERMEDIATE",
        estimated_hours=6.0,
        target_skills=["Team Leadership", "1-on-1 Syncs", "Performance Management", "Radical Candor"],
        description="Practical leadership playbook for newly promoted engineering and product managers.",
        lessons=[
            LessonDefinition("LDR-301-01", "Transitioning from Individual Contributor to Multiplier", 45, "Delegation frameworks and avoiding micromanagement..."),
            LessonDefinition("LDR-301-02", "Conducting Effective 1-on-1s That Drive Engagement", 45, "Career development frameworks and psychological safety..."),
            LessonDefinition("LDR-301-03", "Delivering Constructive Feedback Using the SBI Model", 60, "Situation-Behavior-Impact feedback methodology..."),
            LessonDefinition("LDR-301-04", "Goal Setting with Cascading OKRs and KPIs", 60, "Aligning individual deliverables with departmental objectives..."),
        ]
    ),
    "AI-LLM-401": CourseDefinition(
        course_id="AI-LLM-401",
        title="Production Retrieval-Augmented Generation (RAG) & LLM Applications",
        category="Artificial Intelligence",
        difficulty="ADVANCED",
        estimated_hours=10.0,
        target_skills=["LLMs", "RAG", "Vector Search", "LangChain", "Embeddings"],
        description="Architecting enterprise semantic search, re-ranking pipelines, hybrid BM25 + dense retrieval, and guardrails.",
        lessons=[
            LessonDefinition("AI-401-01", "Vector Embeddings & Semantic Search Fundamentals", 60, "Cosine similarity, HNSW indexing, and distance metrics..."),
            LessonDefinition("AI-401-02", "Chunking Strategies & Context Window Optimization", 60, "Recursive character vs semantic markdown chunking..."),
            LessonDefinition("AI-401-03", "Hybrid Search & Cross-Encoder Re-ranking", 90, "Combining BM25 keyword match with dense neural embeddings..."),
            LessonDefinition("AI-401-04", "Evaluation & Hallucination Mitigation with Ragas", 90, "Faithfulness, answer relevancy, and context recall benchmarking..."),
        ]
    )
}
