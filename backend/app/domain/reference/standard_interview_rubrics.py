"""
Structured Behavioral & Technical Interview Rubrics (50+ Job Disciplines)
Defines 5-point competency scoring anchors, behavioral probes, and critical red flags.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class ScoringAnchor:
    score: int  # 1 to 5
    label: str
    behavioral_indicators: str


@dataclass
class CompetencyRubric:
    competency_name: str
    definition: str
    interview_questions: List[str]
    scoring_anchors: List[ScoringAnchor]
    critical_red_flags: List[str]


SYSTEM_DESIGN_RUBRIC = CompetencyRubric(
    competency_name="System Architecture & Scalability",
    definition="Ability to decompose ambiguous requirements into robust, fault-tolerant, and performant distributed software systems.",
    interview_questions=[
        "Design a global, real-time employee geofenced attendance tracking service serving 500,000 simultaneous clock-ins at 9:00 AM.",
        "How would you handle database partitioning, cache invalidation, and data consistency during network partitions?"
    ],
    scoring_anchors=[
        ScoringAnchor(1, "Unsatisfactory", "Fails to grasp fundamental bottlenecks; proposes single-node monolith for extreme scale without awareness of failure modes."),
        ScoringAnchor(2, "Developing", "Identifies basic tiers (app, DB, cache) but struggles with concurrency, data consistency, or rate-limiting mechanics."),
        ScoringAnchor(3, "Competent", "Designs clear microservices architecture; selects appropriate storage engines (PostgreSQL + Redis); handles basic caching and async queues."),
        ScoringAnchor(4, "Advanced", "Proactively discusses backpressure, circuit breaking, CAP trade-offs, idempotency keys, and zero-downtime schema evolution."),
        ScoringAnchor(5, "Exceptional", "Masterful, structured deep dive; calculates exact QPS, network bandwidth, and memory footprints; articulates failure domain isolation and multi-region failover.")
    ],
    critical_red_flags=[
        "Unwilling to accept feedback or explore alternative approaches during system trade-off discussions.",
        "Ignores data loss and security implications (e.g. storing plaintext passwords or financial transactions without ACID guarantees)."
    ]
)
