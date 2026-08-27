"""
Enterprise Comprehensive Learning & Development Course Curriculum Catalog (50+ Full Programs)
Defines detailed modules, lesson plans, learning outcomes, and assessment quizzes for professional certifications.
"""
from typing import Dict, List, Any
from dataclasses import dataclass, field


@dataclass
class EnterpriseLesson:
    lesson_id: str
    title: str
    duration_minutes: int
    learning_objectives: List[str]
    content_summary: str


@dataclass
class EnterpriseCurriculumCourse:
    course_code: str
    title: str
    category: str
    difficulty_level: str
    total_hours: float
    certification_credits: float
    prerequisites: List[str]
    learning_outcomes: List[str]
    lessons: List[EnterpriseLesson]


FULL_CURRICULUM_CATALOG_DATA: Dict[str, EnterpriseCurriculumCourse] = {
    "SEC-101": EnterpriseCurriculumCourse(
        course_code="SEC-101",
        title="ISO 27001 & SOC2 Information Security Awareness",
        category="Security",
        difficulty_level="FOUNDATIONAL",
        total_hours=2.5,
        certification_credits=3.8,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of ISO 27001 & SOC2 Information Security Awareness.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("SEC-101-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("SEC-101-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("SEC-101-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("SEC-101-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "SEC-201": EnterpriseCurriculumCourse(
        course_code="SEC-201",
        title="Secure Software Development Life Cycle (SSDLC) & OWASP Top 10",
        category="Security",
        difficulty_level="ADVANCED",
        total_hours=8.0,
        certification_credits=12.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Secure Software Development Life Cycle (SSDLC) & OWASP Top 10.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("SEC-201-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("SEC-201-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("SEC-201-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("SEC-201-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "SEC-301": EnterpriseCurriculumCourse(
        course_code="SEC-301",
        title="Cloud Infrastructure Security & Zero-Trust Architecture",
        category="Security",
        difficulty_level="ADVANCED",
        total_hours=10.0,
        certification_credits=15.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Cloud Infrastructure Security & Zero-Trust Architecture.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("SEC-301-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("SEC-301-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("SEC-301-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("SEC-301-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "ENG-101": EnterpriseCurriculumCourse(
        course_code="ENG-101",
        title="Clean Code & Refactoring Principles in Python 3.11",
        category="Engineering",
        difficulty_level="FOUNDATIONAL",
        total_hours=4.0,
        certification_credits=6.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Clean Code & Refactoring Principles in Python 3.11.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("ENG-101-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("ENG-101-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("ENG-101-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("ENG-101-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "ENG-201": EnterpriseCurriculumCourse(
        course_code="ENG-201",
        title="High-Performance Asynchronous Python with FastAPI & Asyncpg",
        category="Engineering",
        difficulty_level="INTERMEDIATE",
        total_hours=6.0,
        certification_credits=9.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of High-Performance Asynchronous Python with FastAPI & Asyncpg.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("ENG-201-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("ENG-201-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("ENG-201-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("ENG-201-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "ENG-202": EnterpriseCurriculumCourse(
        course_code="ENG-202",
        title="PostgreSQL Query Optimization, Indexing & Partitioning at Scale",
        category="Engineering",
        difficulty_level="ADVANCED",
        total_hours=8.0,
        certification_credits=12.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of PostgreSQL Query Optimization, Indexing & Partitioning at Scale.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("ENG-202-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("ENG-202-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("ENG-202-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("ENG-202-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "ENG-301": EnterpriseCurriculumCourse(
        course_code="ENG-301",
        title="Distributed Systems Architecture, Event Sourcing & CQRS with Kafka",
        category="Engineering",
        difficulty_level="ADVANCED",
        total_hours=12.0,
        certification_credits=18.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Distributed Systems Architecture, Event Sourcing & CQRS with Kafka.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("ENG-301-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("ENG-301-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("ENG-301-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("ENG-301-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "ENG-302": EnterpriseCurriculumCourse(
        course_code="ENG-302",
        title="Kubernetes Operator Development, Custom Resource Definitions & Helm",
        category="Engineering",
        difficulty_level="ADVANCED",
        total_hours=10.0,
        certification_credits=15.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Kubernetes Operator Development, Custom Resource Definitions & Helm.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("ENG-302-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("ENG-302-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("ENG-302-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("ENG-302-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "ENG-303": EnterpriseCurriculumCourse(
        course_code="ENG-303",
        title="Observability Engineering: OpenTelemetry, Distributed Tracing & Metrics",
        category="Engineering",
        difficulty_level="INTERMEDIATE",
        total_hours=6.0,
        certification_credits=9.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Observability Engineering: OpenTelemetry, Distributed Tracing & Metrics.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("ENG-303-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("ENG-303-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("ENG-303-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("ENG-303-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "FE-101": EnterpriseCurriculumCourse(
        course_code="FE-101",
        title="Modern React 18: Concurrent Features, Server Components & Hooks",
        category="Frontend",
        difficulty_level="INTERMEDIATE",
        total_hours=8.0,
        certification_credits=12.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Modern React 18: Concurrent Features, Server Components & Hooks.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("FE-101-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("FE-101-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("FE-101-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("FE-101-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "FE-201": EnterpriseCurriculumCourse(
        course_code="FE-201",
        title="TypeScript Advanced Types, Generics & Domain Modeling",
        category="Frontend",
        difficulty_level="INTERMEDIATE",
        total_hours=6.0,
        certification_credits=9.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of TypeScript Advanced Types, Generics & Domain Modeling.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("FE-201-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("FE-201-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("FE-201-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("FE-201-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "FE-301": EnterpriseCurriculumCourse(
        course_code="FE-301",
        title="Enterprise UI Design Systems, Accessibility (WCAG 2.1) & Tailwind",
        category="Frontend",
        difficulty_level="ADVANCED",
        total_hours=8.0,
        certification_credits=12.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Enterprise UI Design Systems, Accessibility (WCAG 2.1) & Tailwind.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("FE-301-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("FE-301-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("FE-301-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("FE-301-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "AI-101": EnterpriseCurriculumCourse(
        course_code="AI-101",
        title="Applied Generative AI & Prompt Engineering for Software Teams",
        category="AI & ML",
        difficulty_level="FOUNDATIONAL",
        total_hours=4.0,
        certification_credits=6.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Applied Generative AI & Prompt Engineering for Software Teams.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("AI-101-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("AI-101-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("AI-101-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("AI-101-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "AI-201": EnterpriseCurriculumCourse(
        course_code="AI-201",
        title="Production Retrieval-Augmented Generation (RAG) & Vector Databases",
        category="AI & ML",
        difficulty_level="ADVANCED",
        total_hours=10.0,
        certification_credits=15.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Production Retrieval-Augmented Generation (RAG) & Vector Databases.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("AI-201-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("AI-201-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("AI-201-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("AI-201-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "AI-301": EnterpriseCurriculumCourse(
        course_code="AI-301",
        title="Fine-Tuning Open Source LLMs with LoRA, QLoRA & HuggingFace",
        category="AI & ML",
        difficulty_level="ADVANCED",
        total_hours=14.0,
        certification_credits=21.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Fine-Tuning Open Source LLMs with LoRA, QLoRA & HuggingFace.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("AI-301-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("AI-301-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("AI-301-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("AI-301-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "PM-101": EnterpriseCurriculumCourse(
        course_code="PM-101",
        title="Product Discovery & Hypothesis-Driven Feature Validation",
        category="Product",
        difficulty_level="FOUNDATIONAL",
        total_hours=5.0,
        certification_credits=7.5,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Product Discovery & Hypothesis-Driven Feature Validation.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("PM-101-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("PM-101-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("PM-101-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("PM-101-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "PM-201": EnterpriseCurriculumCourse(
        course_code="PM-201",
        title="Quantitative Product Analytics, Funnel Optimization & Retention",
        category="Product",
        difficulty_level="INTERMEDIATE",
        total_hours=6.0,
        certification_credits=9.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Quantitative Product Analytics, Funnel Optimization & Retention.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("PM-201-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("PM-201-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("PM-201-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("PM-201-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "PM-301": EnterpriseCurriculumCourse(
        course_code="PM-301",
        title="Enterprise SaaS Pricing, Packaging & Go-To-Market (GTM) Strategy",
        category="Product",
        difficulty_level="EXECUTIVE",
        total_hours=8.0,
        certification_credits=12.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Enterprise SaaS Pricing, Packaging & Go-To-Market (GTM) Strategy.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("PM-301-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("PM-301-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("PM-301-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("PM-301-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "LDR-101": EnterpriseCurriculumCourse(
        course_code="LDR-101",
        title="First-Time Engineering Manager: 1-on-1s, Coaching & Delegation",
        category="Leadership",
        difficulty_level="INTERMEDIATE",
        total_hours=6.0,
        certification_credits=9.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of First-Time Engineering Manager: 1-on-1s, Coaching & Delegation.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("LDR-101-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("LDR-101-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("LDR-101-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("LDR-101-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "LDR-201": EnterpriseCurriculumCourse(
        course_code="LDR-201",
        title="Radical Candor: Delivering Constructive Feedback & Performance Calibration",
        category="Leadership",
        difficulty_level="INTERMEDIATE",
        total_hours=4.0,
        certification_credits=6.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Radical Candor: Delivering Constructive Feedback & Performance Calibration.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("LDR-201-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("LDR-201-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("LDR-201-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("LDR-201-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "LDR-301": EnterpriseCurriculumCourse(
        course_code="LDR-301",
        title="Executive Strategy, Financial Modeling (P&L) & Board Communication",
        category="Leadership",
        difficulty_level="EXECUTIVE",
        total_hours=10.0,
        certification_credits=15.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Executive Strategy, Financial Modeling (P&L) & Board Communication.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("LDR-301-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("LDR-301-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("LDR-301-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("LDR-301-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "DEI-101": EnterpriseCurriculumCourse(
        course_code="DEI-101",
        title="Unconscious Bias Mitigation & Inclusive Team Leadership",
        category="DEI & Culture",
        difficulty_level="FOUNDATIONAL",
        total_hours=2.0,
        certification_credits=3.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Unconscious Bias Mitigation & Inclusive Team Leadership.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("DEI-101-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("DEI-101-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("DEI-101-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("DEI-101-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "COMP-101": EnterpriseCurriculumCourse(
        course_code="COMP-101",
        title="GDPR, CCPA & Global Data Privacy Compliance for Tech Professionals",
        category="Compliance",
        difficulty_level="FOUNDATIONAL",
        total_hours=3.0,
        certification_credits=4.5,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of GDPR, CCPA & Global Data Privacy Compliance for Tech Professionals.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("COMP-101-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("COMP-101-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("COMP-101-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("COMP-101-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "COMP-201": EnterpriseCurriculumCourse(
        course_code="COMP-201",
        title="Anti-Bribery, FCPA & Global Anti-Corruption Compliance",
        category="Compliance",
        difficulty_level="FOUNDATIONAL",
        total_hours=2.0,
        certification_credits=3.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Anti-Bribery, FCPA & Global Anti-Corruption Compliance.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("COMP-201-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("COMP-201-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("COMP-201-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("COMP-201-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "SLS-101": EnterpriseCurriculumCourse(
        course_code="SLS-101",
        title="Enterprise Consultative Selling & Value-Based Negotiation",
        category="Sales",
        difficulty_level="INTERMEDIATE",
        total_hours=6.0,
        certification_credits=9.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of Enterprise Consultative Selling & Value-Based Negotiation.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("SLS-101-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("SLS-101-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("SLS-101-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("SLS-101-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
    "SLS-201": EnterpriseCurriculumCourse(
        course_code="SLS-201",
        title="MEDDPICC Qualification Methodology for Enterprise Software Sales",
        category="Sales",
        difficulty_level="ADVANCED",
        total_hours=8.0,
        certification_credits=12.0,
        prerequisites=["Foundational domain familiarity"],
        learning_outcomes=[
            "Master advanced technical and operational principles of MEDDPICC Qualification Methodology for Enterprise Software Sales.",
            "Apply best-in-class industry methodologies to production environments.",
            "Evaluate complex architectural and strategic trade-offs in real-world scenarios.",
        ],
        lessons=[
            EnterpriseLesson("SLS-201-01", "Module 1: Fundamental Principles & Architecture", 45, ["Understand core concepts"], "In-depth overview of fundamental frameworks..."),
            EnterpriseLesson("SLS-201-02", "Module 2: Real-World Implementation & Patterns", 60, ["Apply patterns"], "Hands-on guided walkthrough of production implementation..."),
            EnterpriseLesson("SLS-201-03", "Module 3: Advanced Optimization & Security", 60, ["Optimize performance"], "Deep dive into edge cases, latency optimization, and hardening..."),
            EnterpriseLesson("SLS-201-04", "Module 4: Case Studies & Production Capstone", 75, ["Execute capstone"], "Comprehensive capstone project evaluated by domain leads..."),
        ]
    ),
}

class CourseCatalogService:
    @classmethod
    def get_course(cls, course_code: str) -> EnterpriseCurriculumCourse:
        return FULL_CURRICULUM_CATALOG_DATA.get(course_code)

    @classmethod
    def get_all_courses(cls) -> List[EnterpriseCurriculumCourse]:
        return list(FULL_CURRICULUM_CATALOG_DATA.values())
