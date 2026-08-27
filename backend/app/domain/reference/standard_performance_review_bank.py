"""
Enterprise 360 Performance Review Competency & Question Bank
Standardized self-evaluations, manager reviews, and peer feedback rubrics.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class PerformanceCompetencyProfile:
    competency_code: str
    title: str
    behavioral_indicators: List[str]
    rating_scale_1_to_5: Dict[int, str]


PERFORMANCE_REVIEW_COMPETENCIES: Dict[str, PerformanceCompetencyProfile] = {
    "PERF-01": PerformanceCompetencyProfile(
        competency_code="PERF-01",
        title="Technical Execution & Delivery",
        behavioral_indicators=['Consistently delivers production code on schedule with high test coverage.', 'Proactively addresses technical debt and refactoring opportunities.', 'Maintains clear documentation and architecture decision records (ADRs).'],
        rating_scale_1_to_5={
            1: "Unsatisfactory - Consistently fails to meet expectations.",
            2: "Developing - Meets some expectations but requires improvement.",
            3: "Strong Performer - Consistently meets all role expectations.",
            4: "Exceeds Expectations - Regularly surpasses goals and lifts team standards.",
            5: "Role Model - Exceptional leader and multiplier across the organization.",
        }
    ),
    "PERF-02": PerformanceCompetencyProfile(
        competency_code="PERF-02",
        title="System Ownership & Reliability",
        behavioral_indicators=['Takes end-to-end ownership of services from design to production monitoring.', 'Acts as an effective incident commander during system outages.', 'Ensures SLOs and latency benchmarks are met or exceeded.'],
        rating_scale_1_to_5={
            1: "Unsatisfactory - Consistently fails to meet expectations.",
            2: "Developing - Meets some expectations but requires improvement.",
            3: "Strong Performer - Consistently meets all role expectations.",
            4: "Exceeds Expectations - Regularly surpasses goals and lifts team standards.",
            5: "Role Model - Exceptional leader and multiplier across the organization.",
        }
    ),
    "PERF-03": PerformanceCompetencyProfile(
        competency_code="PERF-03",
        title="Mentorship & Team Multiplier",
        behavioral_indicators=['Invests time in mentoring junior and mid-level engineers.', 'Conducts thorough, empathetic, and constructive code reviews.', 'Fosters psychological safety and inclusive team discussions.'],
        rating_scale_1_to_5={
            1: "Unsatisfactory - Consistently fails to meet expectations.",
            2: "Developing - Meets some expectations but requires improvement.",
            3: "Strong Performer - Consistently meets all role expectations.",
            4: "Exceeds Expectations - Regularly surpasses goals and lifts team standards.",
            5: "Role Model - Exceptional leader and multiplier across the organization.",
        }
    ),
    "PERF-04": PerformanceCompetencyProfile(
        competency_code="PERF-04",
        title="Strategic Alignment & Business Impact",
        behavioral_indicators=['Aligns daily engineering tasks with high-level company OKRs.', 'Understands the commercial impact of technical architecture choices.', 'Identifies opportunities to reduce cloud infrastructure costs.'],
        rating_scale_1_to_5={
            1: "Unsatisfactory - Consistently fails to meet expectations.",
            2: "Developing - Meets some expectations but requires improvement.",
            3: "Strong Performer - Consistently meets all role expectations.",
            4: "Exceeds Expectations - Regularly surpasses goals and lifts team standards.",
            5: "Role Model - Exceptional leader and multiplier across the organization.",
        }
    ),
    "PERF-05": PerformanceCompetencyProfile(
        competency_code="PERF-05",
        title="Cross-Functional Collaboration",
        behavioral_indicators=['Partners effectively with Product, Design, Sales, and Support.', 'Communicates technical complexity clearly to non-technical stakeholders.', 'Resolves inter-team dependencies smoothly without escalation.'],
        rating_scale_1_to_5={
            1: "Unsatisfactory - Consistently fails to meet expectations.",
            2: "Developing - Meets some expectations but requires improvement.",
            3: "Strong Performer - Consistently meets all role expectations.",
            4: "Exceeds Expectations - Regularly surpasses goals and lifts team standards.",
            5: "Role Model - Exceptional leader and multiplier across the organization.",
        }
    ),
    "PERF-06": PerformanceCompetencyProfile(
        competency_code="PERF-06",
        title="Continuous Learning & Innovation",
        behavioral_indicators=['Stays abreast of emerging industry technologies and best practices.', 'Conducts research spikes and prototypes to validate new approaches.', 'Shares learnings through internal tech talks and documentation.'],
        rating_scale_1_to_5={
            1: "Unsatisfactory - Consistently fails to meet expectations.",
            2: "Developing - Meets some expectations but requires improvement.",
            3: "Strong Performer - Consistently meets all role expectations.",
            4: "Exceeds Expectations - Regularly surpasses goals and lifts team standards.",
            5: "Role Model - Exceptional leader and multiplier across the organization.",
        }
    ),
    "PERF-07": PerformanceCompetencyProfile(
        competency_code="PERF-07",
        title="Security & Compliance Adherence",
        behavioral_indicators=['Strictly follows ISO 27001 and SOC2 security control procedures.', 'Proactively identifies and remediates OWASP vulnerabilities.', 'Ensures proper data classification and PII protection.'],
        rating_scale_1_to_5={
            1: "Unsatisfactory - Consistently fails to meet expectations.",
            2: "Developing - Meets some expectations but requires improvement.",
            3: "Strong Performer - Consistently meets all role expectations.",
            4: "Exceeds Expectations - Regularly surpasses goals and lifts team standards.",
            5: "Role Model - Exceptional leader and multiplier across the organization.",
        }
    ),
    "PERF-08": PerformanceCompetencyProfile(
        competency_code="PERF-08",
        title="Leadership & Operational Excellence",
        behavioral_indicators=['Sets a high standard of craftsmanship and accountability for the team.', 'Drives continuous improvement in CI/CD pipelines and deployment velocity.', 'Demonstrates calm, decisive leadership during high-pressure situations.'],
        rating_scale_1_to_5={
            1: "Unsatisfactory - Consistently fails to meet expectations.",
            2: "Developing - Meets some expectations but requires improvement.",
            3: "Strong Performer - Consistently meets all role expectations.",
            4: "Exceeds Expectations - Regularly surpasses goals and lifts team standards.",
            5: "Role Model - Exceptional leader and multiplier across the organization.",
        }
    ),
}

class PerformanceReviewBankService:
    @classmethod
    def get_competency(cls, code: str) -> PerformanceCompetencyProfile:
        return PERFORMANCE_REVIEW_COMPETENCIES.get(code)

    @classmethod
    def get_all_competencies(cls) -> List[PerformanceCompetencyProfile]:
        return list(PERFORMANCE_REVIEW_COMPETENCIES.values())
