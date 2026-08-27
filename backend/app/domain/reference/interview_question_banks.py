"""
Enterprise Standard Interview Question Bank & 5-Point STAR Rubric Guide
Structured behavioral and technical questions mapped to core competencies with sample responses and red flags.
"""
from typing import Dict, List, Any
from dataclasses import dataclass, field


@dataclass
class InterviewQuestion:
    question_id: str
    discipline: str
    question_text: str
    competency_tested: str
    keywords: List[str]
    scoring_guide_star_1_poor: str
    scoring_guide_star_3_competent: str
    scoring_guide_star_5_exceptional: str


INTERVIEW_QUESTION_BANK_DATA: Dict[str, InterviewQuestion] = {
    "Q-Engineering_Backend-001": InterviewQuestion(
        question_id="Q-Engineering_Backend-001",
        discipline="Backend & Distributed Systems",
        question_text="Explain the difference between optimistic and pessimistic concurrency control. When would you use each?",
        competency_tested="Database Concurrency",
        keywords=['ACID', 'Transactions', 'Locks', 'MVCC'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Engineering_Backend-002": InterviewQuestion(
        question_id="Q-Engineering_Backend-002",
        discipline="Backend & Distributed Systems",
        question_text="How do you design an idempotent payment processing API to prevent duplicate charges upon network timeouts?",
        competency_tested="API Idempotency",
        keywords=['Idempotency Keys', 'Tokenization', 'Distributed Locks', 'Atomic Inserts'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Engineering_Backend-003": InterviewQuestion(
        question_id="Q-Engineering_Backend-003",
        discipline="Backend & Distributed Systems",
        question_text="Describe how you would debug a memory leak in a long-running production Python/Node backend service.",
        competency_tested="Troubleshooting & SRE",
        keywords=['Profiling', 'Heap Dumps', 'Garbage Collection', 'Memory Leaks'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Engineering_Backend-004": InterviewQuestion(
        question_id="Q-Engineering_Backend-004",
        discipline="Backend & Distributed Systems",
        question_text="How would you partition a PostgreSQL database table with 500 million rows for sub-10ms query latency?",
        competency_tested="Database Scaling",
        keywords=['Range Partitioning', 'Hash Partitioning', 'Indexes', 'Query Planning'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Engineering_Backend-005": InterviewQuestion(
        question_id="Q-Engineering_Backend-005",
        discipline="Backend & Distributed Systems",
        question_text="Explain the Raft consensus algorithm and how leader election and log replication work under network partitions.",
        competency_tested="Distributed Consensus",
        keywords=['Raft', 'Paxos', 'Quorum', 'Split-Brain Prevention'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Engineering_Frontend-006": InterviewQuestion(
        question_id="Q-Engineering_Frontend-006",
        discipline="Frontend & Web Performance",
        question_text="How does React 18 Concurrent Mode and Fiber architecture work under the hood to prevent main-thread blocking?",
        competency_tested="React Internals",
        keywords=['Fiber', 'Reconciliation', 'Time-Slicing', 'Transitions'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Engineering_Frontend-007": InterviewQuestion(
        question_id="Q-Engineering_Frontend-007",
        discipline="Frontend & Web Performance",
        question_text="Describe your strategy for optimizing Web Vitals (LCP, FID/INP, CLS) on a data-dense enterprise dashboard.",
        competency_tested="Core Web Vitals",
        keywords=['LCP', 'CLS', 'Code Splitting', 'Tree Shaking', 'Virtualization'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Engineering_Frontend-008": InterviewQuestion(
        question_id="Q-Engineering_Frontend-008",
        discipline="Frontend & Web Performance",
        question_text="How do you design a resilient multi-tenant design system with theme tokens and full WCAG 2.1 AA accessibility?",
        competency_tested="UI Architecture",
        keywords=['Design Tokens', 'ARIA', 'Contrast Ratios', 'Keyboard Navigation'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Engineering_Frontend-009": InterviewQuestion(
        question_id="Q-Engineering_Frontend-009",
        discipline="Frontend & Web Performance",
        question_text="Explain the differences between SSR, SSG, ISR, and Client-Side SPA architectures in terms of caching and scalability.",
        competency_tested="Rendering Topologies",
        keywords=['SSR', 'Next.js', 'Edge Caching', 'Hydration'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Leadership_Management-010": InterviewQuestion(
        question_id="Q-Leadership_Management-010",
        discipline="Engineering & People Leadership",
        question_text="Tell me about a time you had to deliver critical constructive feedback to a senior engineer who was underperforming.",
        competency_tested="Constructive Feedback",
        keywords=['Radical Candor', 'SBI Model', 'Psychological Safety', 'PIP'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Leadership_Management-011": InterviewQuestion(
        question_id="Q-Leadership_Management-011",
        discipline="Engineering & People Leadership",
        question_text="How do you resolve a deep technical disagreement between two principal architects regarding database technology choices?",
        competency_tested="Conflict Resolution",
        keywords=['Consensus Building', 'RFCs', 'POC Benchmarks', 'Trade-Off Analysis'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Leadership_Management-012": InterviewQuestion(
        question_id="Q-Leadership_Management-012",
        discipline="Engineering & People Leadership",
        question_text="Describe your framework for building a high-performing, psychologically safe, and diverse engineering team culture.",
        competency_tested="Team Culture",
        keywords=['Inclusion', 'Mentorship', 'Blameless Postmortems', 'Career Ladders'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Leadership_Management-013": InterviewQuestion(
        question_id="Q-Leadership_Management-013",
        discipline="Engineering & People Leadership",
        question_text="How do you balance technical debt remediation with aggressive product feature delivery commitments to the business?",
        competency_tested="Tech Debt Prioritization",
        keywords=['Sprint Allocation', 'Business Impact', 'Architecture Reviews'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Product_Management-014": InterviewQuestion(
        question_id="Q-Product_Management-014",
        discipline="Enterprise Product Strategy",
        question_text="Walk me through how you prioritize a product roadmap when multiple enterprise customers have competing feature demands.",
        competency_tested="Roadmap Prioritization",
        keywords=['RICE Score', 'Kano Model', 'Revenue Impact', 'Strategic Alignment'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Product_Management-015": InterviewQuestion(
        question_id="Q-Product_Management-015",
        discipline="Enterprise Product Strategy",
        question_text="How do you measure product-market fit and feature adoption for a newly launched B2B HR intelligence module?",
        competency_tested="Metrics & Telemetry",
        keywords=['Adoption Rate', 'Retention', 'Cohort Analysis', 'CSAT/NPS'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Product_Management-016": InterviewQuestion(
        question_id="Q-Product_Management-016",
        discipline="Enterprise Product Strategy",
        question_text="Describe a situation where qualitative user feedback contradicted your quantitative product analytics data. How did you resolve it?",
        competency_tested="Data-Driven Discovery",
        keywords=['User Interviews', 'Funnel Drop-off', 'Triangulation'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Security_Infosec-017": InterviewQuestion(
        question_id="Q-Security_Infosec-017",
        discipline="Information Security & DevSecOps",
        question_text="How do you implement Zero-Trust network architecture and mutual TLS (mTLS) in a Kubernetes microservices mesh?",
        competency_tested="Zero Trust Architecture",
        keywords=['mTLS', 'Istio', 'SPIFFE/SPIRE', 'Identity Verification'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Security_Infosec-018": InterviewQuestion(
        question_id="Q-Security_Infosec-018",
        discipline="Information Security & DevSecOps",
        question_text="Describe your response procedure during a zero-day remote code execution (RCE) vulnerability disclosure in a production dependency.",
        competency_tested="Incident Response",
        keywords=['Patching', 'WAF Rules', 'Blast Radius Containment', 'Post-Incident Review'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
    "Q-Security_Infosec-019": InterviewQuestion(
        question_id="Q-Security_Infosec-019",
        discipline="Information Security & DevSecOps",
        question_text="How do you structure an enterprise RBAC and ABAC permissions engine to enforce tenant boundary isolation?",
        competency_tested="Access Control",
        keywords=['RBAC', 'ABAC', 'Tenant Isolation', 'Least Privilege'],
        scoring_guide_star_1_poor="Vague response; lacks concrete examples; demonstrates no awareness of system failure modes or empathy.",
        scoring_guide_star_3_competent="Provides clear STAR example with measurable result; understands standard trade-offs and best practices.",
        scoring_guide_star_5_exceptional="Exceptional structured storytelling; articulates non-obvious second-order effects, quantitative metrics, and organizational lessons learned."
    ),
}

class InterviewQuestionBankService:
    @classmethod
    def get_questions_by_discipline(cls, discipline: str) -> List[InterviewQuestion]:
        return [q for q in INTERVIEW_QUESTION_BANK_DATA.values() if discipline.lower() in q.discipline.lower()]

    @classmethod
    def get_all_questions(cls) -> List[InterviewQuestion]:
        return list(INTERVIEW_QUESTION_BANK_DATA.values())
