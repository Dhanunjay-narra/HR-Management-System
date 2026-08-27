"""
Enterprise 360 Performance Review Prompt & Scoring Guide Bank (250 Prompts)
Defines role-specific review questions, evaluation anchors 1-5, and developmental feedback guidance.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class ReviewPromptRecord:
    prompt_id: str
    domain_family: str
    competency_area: str
    prompt_question: str
    scoring_anchors: Dict[int, str]
    development_action: str


MASTER_250_REVIEW_PROMPTS: Dict[str, ReviewPromptRecord] = {
    "PRM-ENG-001": ReviewPromptRecord(
        prompt_id="PRM-ENG-001",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #1?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-002": ReviewPromptRecord(
        prompt_id="PRM-ENG-002",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #2?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-003": ReviewPromptRecord(
        prompt_id="PRM-ENG-003",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #3?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-004": ReviewPromptRecord(
        prompt_id="PRM-ENG-004",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #4?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-005": ReviewPromptRecord(
        prompt_id="PRM-ENG-005",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #5?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-006": ReviewPromptRecord(
        prompt_id="PRM-ENG-006",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #6?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-007": ReviewPromptRecord(
        prompt_id="PRM-ENG-007",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #7?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-008": ReviewPromptRecord(
        prompt_id="PRM-ENG-008",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #8?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-009": ReviewPromptRecord(
        prompt_id="PRM-ENG-009",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #9?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-010": ReviewPromptRecord(
        prompt_id="PRM-ENG-010",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #10?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-011": ReviewPromptRecord(
        prompt_id="PRM-ENG-011",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #11?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-012": ReviewPromptRecord(
        prompt_id="PRM-ENG-012",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #12?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-013": ReviewPromptRecord(
        prompt_id="PRM-ENG-013",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #13?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-014": ReviewPromptRecord(
        prompt_id="PRM-ENG-014",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #14?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-015": ReviewPromptRecord(
        prompt_id="PRM-ENG-015",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #15?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-016": ReviewPromptRecord(
        prompt_id="PRM-ENG-016",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #16?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-017": ReviewPromptRecord(
        prompt_id="PRM-ENG-017",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #17?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-018": ReviewPromptRecord(
        prompt_id="PRM-ENG-018",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #18?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-019": ReviewPromptRecord(
        prompt_id="PRM-ENG-019",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #19?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-020": ReviewPromptRecord(
        prompt_id="PRM-ENG-020",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #20?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-021": ReviewPromptRecord(
        prompt_id="PRM-ENG-021",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #21?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-022": ReviewPromptRecord(
        prompt_id="PRM-ENG-022",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #22?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-023": ReviewPromptRecord(
        prompt_id="PRM-ENG-023",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #23?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-024": ReviewPromptRecord(
        prompt_id="PRM-ENG-024",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #24?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-025": ReviewPromptRecord(
        prompt_id="PRM-ENG-025",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #25?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-026": ReviewPromptRecord(
        prompt_id="PRM-ENG-026",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #26?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-027": ReviewPromptRecord(
        prompt_id="PRM-ENG-027",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #27?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-028": ReviewPromptRecord(
        prompt_id="PRM-ENG-028",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #28?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-029": ReviewPromptRecord(
        prompt_id="PRM-ENG-029",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #29?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-030": ReviewPromptRecord(
        prompt_id="PRM-ENG-030",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #30?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-031": ReviewPromptRecord(
        prompt_id="PRM-ENG-031",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #31?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-032": ReviewPromptRecord(
        prompt_id="PRM-ENG-032",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #32?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-033": ReviewPromptRecord(
        prompt_id="PRM-ENG-033",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #33?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-034": ReviewPromptRecord(
        prompt_id="PRM-ENG-034",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #34?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-035": ReviewPromptRecord(
        prompt_id="PRM-ENG-035",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #35?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-036": ReviewPromptRecord(
        prompt_id="PRM-ENG-036",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #36?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-037": ReviewPromptRecord(
        prompt_id="PRM-ENG-037",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #37?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-038": ReviewPromptRecord(
        prompt_id="PRM-ENG-038",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #38?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-039": ReviewPromptRecord(
        prompt_id="PRM-ENG-039",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #39?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-040": ReviewPromptRecord(
        prompt_id="PRM-ENG-040",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #40?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-041": ReviewPromptRecord(
        prompt_id="PRM-ENG-041",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #41?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-042": ReviewPromptRecord(
        prompt_id="PRM-ENG-042",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #42?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-043": ReviewPromptRecord(
        prompt_id="PRM-ENG-043",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #43?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-044": ReviewPromptRecord(
        prompt_id="PRM-ENG-044",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #44?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-045": ReviewPromptRecord(
        prompt_id="PRM-ENG-045",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #45?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-046": ReviewPromptRecord(
        prompt_id="PRM-ENG-046",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #46?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-047": ReviewPromptRecord(
        prompt_id="PRM-ENG-047",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #47?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-048": ReviewPromptRecord(
        prompt_id="PRM-ENG-048",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #48?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-049": ReviewPromptRecord(
        prompt_id="PRM-ENG-049",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #49?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-ENG-050": ReviewPromptRecord(
        prompt_id="PRM-ENG-050",
        domain_family="Software Engineering & Architecture",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Software Engineering & Architecture deliverable #50?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-001": ReviewPromptRecord(
        prompt_id="PRM-PROD-001",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #1?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-002": ReviewPromptRecord(
        prompt_id="PRM-PROD-002",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #2?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-003": ReviewPromptRecord(
        prompt_id="PRM-PROD-003",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #3?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-004": ReviewPromptRecord(
        prompt_id="PRM-PROD-004",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #4?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-005": ReviewPromptRecord(
        prompt_id="PRM-PROD-005",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #5?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-006": ReviewPromptRecord(
        prompt_id="PRM-PROD-006",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #6?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-007": ReviewPromptRecord(
        prompt_id="PRM-PROD-007",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #7?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-008": ReviewPromptRecord(
        prompt_id="PRM-PROD-008",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #8?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-009": ReviewPromptRecord(
        prompt_id="PRM-PROD-009",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #9?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-010": ReviewPromptRecord(
        prompt_id="PRM-PROD-010",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #10?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-011": ReviewPromptRecord(
        prompt_id="PRM-PROD-011",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #11?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-012": ReviewPromptRecord(
        prompt_id="PRM-PROD-012",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #12?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-013": ReviewPromptRecord(
        prompt_id="PRM-PROD-013",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #13?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-014": ReviewPromptRecord(
        prompt_id="PRM-PROD-014",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #14?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-015": ReviewPromptRecord(
        prompt_id="PRM-PROD-015",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #15?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-016": ReviewPromptRecord(
        prompt_id="PRM-PROD-016",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #16?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-017": ReviewPromptRecord(
        prompt_id="PRM-PROD-017",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #17?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-018": ReviewPromptRecord(
        prompt_id="PRM-PROD-018",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #18?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-019": ReviewPromptRecord(
        prompt_id="PRM-PROD-019",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #19?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-020": ReviewPromptRecord(
        prompt_id="PRM-PROD-020",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #20?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-021": ReviewPromptRecord(
        prompt_id="PRM-PROD-021",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #21?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-022": ReviewPromptRecord(
        prompt_id="PRM-PROD-022",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #22?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-023": ReviewPromptRecord(
        prompt_id="PRM-PROD-023",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #23?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-024": ReviewPromptRecord(
        prompt_id="PRM-PROD-024",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #24?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-025": ReviewPromptRecord(
        prompt_id="PRM-PROD-025",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #25?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-026": ReviewPromptRecord(
        prompt_id="PRM-PROD-026",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #26?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-027": ReviewPromptRecord(
        prompt_id="PRM-PROD-027",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #27?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-028": ReviewPromptRecord(
        prompt_id="PRM-PROD-028",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #28?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-029": ReviewPromptRecord(
        prompt_id="PRM-PROD-029",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #29?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-030": ReviewPromptRecord(
        prompt_id="PRM-PROD-030",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #30?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-031": ReviewPromptRecord(
        prompt_id="PRM-PROD-031",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #31?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-032": ReviewPromptRecord(
        prompt_id="PRM-PROD-032",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #32?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-033": ReviewPromptRecord(
        prompt_id="PRM-PROD-033",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #33?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-034": ReviewPromptRecord(
        prompt_id="PRM-PROD-034",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #34?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-035": ReviewPromptRecord(
        prompt_id="PRM-PROD-035",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #35?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-036": ReviewPromptRecord(
        prompt_id="PRM-PROD-036",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #36?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-037": ReviewPromptRecord(
        prompt_id="PRM-PROD-037",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #37?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-038": ReviewPromptRecord(
        prompt_id="PRM-PROD-038",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #38?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-039": ReviewPromptRecord(
        prompt_id="PRM-PROD-039",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #39?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-040": ReviewPromptRecord(
        prompt_id="PRM-PROD-040",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #40?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-041": ReviewPromptRecord(
        prompt_id="PRM-PROD-041",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #41?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-042": ReviewPromptRecord(
        prompt_id="PRM-PROD-042",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #42?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-043": ReviewPromptRecord(
        prompt_id="PRM-PROD-043",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #43?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-044": ReviewPromptRecord(
        prompt_id="PRM-PROD-044",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #44?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-045": ReviewPromptRecord(
        prompt_id="PRM-PROD-045",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #45?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-046": ReviewPromptRecord(
        prompt_id="PRM-PROD-046",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #46?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-047": ReviewPromptRecord(
        prompt_id="PRM-PROD-047",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #47?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-048": ReviewPromptRecord(
        prompt_id="PRM-PROD-048",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #48?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-049": ReviewPromptRecord(
        prompt_id="PRM-PROD-049",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #49?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-PROD-050": ReviewPromptRecord(
        prompt_id="PRM-PROD-050",
        domain_family="Product Strategy & Design",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Product Strategy & Design deliverable #50?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-001": ReviewPromptRecord(
        prompt_id="PRM-LDR-001",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #1?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-002": ReviewPromptRecord(
        prompt_id="PRM-LDR-002",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #2?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-003": ReviewPromptRecord(
        prompt_id="PRM-LDR-003",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #3?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-004": ReviewPromptRecord(
        prompt_id="PRM-LDR-004",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #4?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-005": ReviewPromptRecord(
        prompt_id="PRM-LDR-005",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #5?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-006": ReviewPromptRecord(
        prompt_id="PRM-LDR-006",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #6?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-007": ReviewPromptRecord(
        prompt_id="PRM-LDR-007",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #7?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-008": ReviewPromptRecord(
        prompt_id="PRM-LDR-008",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #8?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-009": ReviewPromptRecord(
        prompt_id="PRM-LDR-009",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #9?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-010": ReviewPromptRecord(
        prompt_id="PRM-LDR-010",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #10?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-011": ReviewPromptRecord(
        prompt_id="PRM-LDR-011",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #11?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-012": ReviewPromptRecord(
        prompt_id="PRM-LDR-012",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #12?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-013": ReviewPromptRecord(
        prompt_id="PRM-LDR-013",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #13?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-014": ReviewPromptRecord(
        prompt_id="PRM-LDR-014",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #14?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-015": ReviewPromptRecord(
        prompt_id="PRM-LDR-015",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #15?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-016": ReviewPromptRecord(
        prompt_id="PRM-LDR-016",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #16?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-017": ReviewPromptRecord(
        prompt_id="PRM-LDR-017",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #17?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-018": ReviewPromptRecord(
        prompt_id="PRM-LDR-018",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #18?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-019": ReviewPromptRecord(
        prompt_id="PRM-LDR-019",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #19?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-020": ReviewPromptRecord(
        prompt_id="PRM-LDR-020",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #20?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-021": ReviewPromptRecord(
        prompt_id="PRM-LDR-021",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #21?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-022": ReviewPromptRecord(
        prompt_id="PRM-LDR-022",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #22?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-023": ReviewPromptRecord(
        prompt_id="PRM-LDR-023",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #23?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-024": ReviewPromptRecord(
        prompt_id="PRM-LDR-024",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #24?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-025": ReviewPromptRecord(
        prompt_id="PRM-LDR-025",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #25?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-026": ReviewPromptRecord(
        prompt_id="PRM-LDR-026",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #26?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-027": ReviewPromptRecord(
        prompt_id="PRM-LDR-027",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #27?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-028": ReviewPromptRecord(
        prompt_id="PRM-LDR-028",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #28?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-029": ReviewPromptRecord(
        prompt_id="PRM-LDR-029",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #29?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-030": ReviewPromptRecord(
        prompt_id="PRM-LDR-030",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #30?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-031": ReviewPromptRecord(
        prompt_id="PRM-LDR-031",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #31?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-032": ReviewPromptRecord(
        prompt_id="PRM-LDR-032",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #32?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-033": ReviewPromptRecord(
        prompt_id="PRM-LDR-033",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #33?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-034": ReviewPromptRecord(
        prompt_id="PRM-LDR-034",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #34?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-035": ReviewPromptRecord(
        prompt_id="PRM-LDR-035",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #35?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-036": ReviewPromptRecord(
        prompt_id="PRM-LDR-036",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #36?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-037": ReviewPromptRecord(
        prompt_id="PRM-LDR-037",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #37?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-038": ReviewPromptRecord(
        prompt_id="PRM-LDR-038",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #38?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-039": ReviewPromptRecord(
        prompt_id="PRM-LDR-039",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #39?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-040": ReviewPromptRecord(
        prompt_id="PRM-LDR-040",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #40?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-041": ReviewPromptRecord(
        prompt_id="PRM-LDR-041",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #41?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-042": ReviewPromptRecord(
        prompt_id="PRM-LDR-042",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #42?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-043": ReviewPromptRecord(
        prompt_id="PRM-LDR-043",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #43?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-044": ReviewPromptRecord(
        prompt_id="PRM-LDR-044",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #44?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-045": ReviewPromptRecord(
        prompt_id="PRM-LDR-045",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #45?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-046": ReviewPromptRecord(
        prompt_id="PRM-LDR-046",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #46?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-047": ReviewPromptRecord(
        prompt_id="PRM-LDR-047",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #47?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-048": ReviewPromptRecord(
        prompt_id="PRM-LDR-048",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #48?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-049": ReviewPromptRecord(
        prompt_id="PRM-LDR-049",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #49?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-LDR-050": ReviewPromptRecord(
        prompt_id="PRM-LDR-050",
        domain_family="Leadership & People Management",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Leadership & People Management deliverable #50?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-001": ReviewPromptRecord(
        prompt_id="PRM-GTM-001",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #1?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-002": ReviewPromptRecord(
        prompt_id="PRM-GTM-002",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #2?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-003": ReviewPromptRecord(
        prompt_id="PRM-GTM-003",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #3?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-004": ReviewPromptRecord(
        prompt_id="PRM-GTM-004",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #4?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-005": ReviewPromptRecord(
        prompt_id="PRM-GTM-005",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #5?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-006": ReviewPromptRecord(
        prompt_id="PRM-GTM-006",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #6?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-007": ReviewPromptRecord(
        prompt_id="PRM-GTM-007",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #7?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-008": ReviewPromptRecord(
        prompt_id="PRM-GTM-008",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #8?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-009": ReviewPromptRecord(
        prompt_id="PRM-GTM-009",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #9?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-010": ReviewPromptRecord(
        prompt_id="PRM-GTM-010",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #10?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-011": ReviewPromptRecord(
        prompt_id="PRM-GTM-011",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #11?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-012": ReviewPromptRecord(
        prompt_id="PRM-GTM-012",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #12?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-013": ReviewPromptRecord(
        prompt_id="PRM-GTM-013",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #13?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-014": ReviewPromptRecord(
        prompt_id="PRM-GTM-014",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #14?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-015": ReviewPromptRecord(
        prompt_id="PRM-GTM-015",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #15?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-016": ReviewPromptRecord(
        prompt_id="PRM-GTM-016",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #16?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-017": ReviewPromptRecord(
        prompt_id="PRM-GTM-017",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #17?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-018": ReviewPromptRecord(
        prompt_id="PRM-GTM-018",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #18?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-019": ReviewPromptRecord(
        prompt_id="PRM-GTM-019",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #19?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-020": ReviewPromptRecord(
        prompt_id="PRM-GTM-020",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #20?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-021": ReviewPromptRecord(
        prompt_id="PRM-GTM-021",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #21?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-022": ReviewPromptRecord(
        prompt_id="PRM-GTM-022",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #22?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-023": ReviewPromptRecord(
        prompt_id="PRM-GTM-023",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #23?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-024": ReviewPromptRecord(
        prompt_id="PRM-GTM-024",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #24?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-025": ReviewPromptRecord(
        prompt_id="PRM-GTM-025",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #25?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-026": ReviewPromptRecord(
        prompt_id="PRM-GTM-026",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #26?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-027": ReviewPromptRecord(
        prompt_id="PRM-GTM-027",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #27?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-028": ReviewPromptRecord(
        prompt_id="PRM-GTM-028",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #28?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-029": ReviewPromptRecord(
        prompt_id="PRM-GTM-029",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #29?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-030": ReviewPromptRecord(
        prompt_id="PRM-GTM-030",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #30?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-031": ReviewPromptRecord(
        prompt_id="PRM-GTM-031",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #31?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-032": ReviewPromptRecord(
        prompt_id="PRM-GTM-032",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #32?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-033": ReviewPromptRecord(
        prompt_id="PRM-GTM-033",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #33?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-034": ReviewPromptRecord(
        prompt_id="PRM-GTM-034",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #34?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-035": ReviewPromptRecord(
        prompt_id="PRM-GTM-035",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #35?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-036": ReviewPromptRecord(
        prompt_id="PRM-GTM-036",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #36?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-037": ReviewPromptRecord(
        prompt_id="PRM-GTM-037",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #37?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-038": ReviewPromptRecord(
        prompt_id="PRM-GTM-038",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #38?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-039": ReviewPromptRecord(
        prompt_id="PRM-GTM-039",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #39?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-040": ReviewPromptRecord(
        prompt_id="PRM-GTM-040",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #40?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-041": ReviewPromptRecord(
        prompt_id="PRM-GTM-041",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #41?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-042": ReviewPromptRecord(
        prompt_id="PRM-GTM-042",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #42?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-043": ReviewPromptRecord(
        prompt_id="PRM-GTM-043",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #43?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-044": ReviewPromptRecord(
        prompt_id="PRM-GTM-044",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #44?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-045": ReviewPromptRecord(
        prompt_id="PRM-GTM-045",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #45?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-046": ReviewPromptRecord(
        prompt_id="PRM-GTM-046",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #46?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-047": ReviewPromptRecord(
        prompt_id="PRM-GTM-047",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #47?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-048": ReviewPromptRecord(
        prompt_id="PRM-GTM-048",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #48?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-049": ReviewPromptRecord(
        prompt_id="PRM-GTM-049",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #49?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-GTM-050": ReviewPromptRecord(
        prompt_id="PRM-GTM-050",
        domain_family="Sales & Customer Success",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Sales & Customer Success deliverable #50?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-001": ReviewPromptRecord(
        prompt_id="PRM-OPS-001",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #1?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-002": ReviewPromptRecord(
        prompt_id="PRM-OPS-002",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #2?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-003": ReviewPromptRecord(
        prompt_id="PRM-OPS-003",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #3?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-004": ReviewPromptRecord(
        prompt_id="PRM-OPS-004",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #4?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-005": ReviewPromptRecord(
        prompt_id="PRM-OPS-005",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #5?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-006": ReviewPromptRecord(
        prompt_id="PRM-OPS-006",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #6?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-007": ReviewPromptRecord(
        prompt_id="PRM-OPS-007",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #7?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-008": ReviewPromptRecord(
        prompt_id="PRM-OPS-008",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #8?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-009": ReviewPromptRecord(
        prompt_id="PRM-OPS-009",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #9?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-010": ReviewPromptRecord(
        prompt_id="PRM-OPS-010",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #10?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-011": ReviewPromptRecord(
        prompt_id="PRM-OPS-011",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #11?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-012": ReviewPromptRecord(
        prompt_id="PRM-OPS-012",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #12?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-013": ReviewPromptRecord(
        prompt_id="PRM-OPS-013",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #13?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-014": ReviewPromptRecord(
        prompt_id="PRM-OPS-014",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #14?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-015": ReviewPromptRecord(
        prompt_id="PRM-OPS-015",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #15?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-016": ReviewPromptRecord(
        prompt_id="PRM-OPS-016",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #16?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-017": ReviewPromptRecord(
        prompt_id="PRM-OPS-017",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #17?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-018": ReviewPromptRecord(
        prompt_id="PRM-OPS-018",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #18?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-019": ReviewPromptRecord(
        prompt_id="PRM-OPS-019",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #19?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-020": ReviewPromptRecord(
        prompt_id="PRM-OPS-020",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #20?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-021": ReviewPromptRecord(
        prompt_id="PRM-OPS-021",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #21?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-022": ReviewPromptRecord(
        prompt_id="PRM-OPS-022",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #22?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-023": ReviewPromptRecord(
        prompt_id="PRM-OPS-023",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #23?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-024": ReviewPromptRecord(
        prompt_id="PRM-OPS-024",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #24?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-025": ReviewPromptRecord(
        prompt_id="PRM-OPS-025",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #25?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-026": ReviewPromptRecord(
        prompt_id="PRM-OPS-026",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #26?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-027": ReviewPromptRecord(
        prompt_id="PRM-OPS-027",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #27?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-028": ReviewPromptRecord(
        prompt_id="PRM-OPS-028",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #28?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-029": ReviewPromptRecord(
        prompt_id="PRM-OPS-029",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #29?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-030": ReviewPromptRecord(
        prompt_id="PRM-OPS-030",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #30?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-031": ReviewPromptRecord(
        prompt_id="PRM-OPS-031",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #31?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-032": ReviewPromptRecord(
        prompt_id="PRM-OPS-032",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #32?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-033": ReviewPromptRecord(
        prompt_id="PRM-OPS-033",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #33?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-034": ReviewPromptRecord(
        prompt_id="PRM-OPS-034",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #34?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-035": ReviewPromptRecord(
        prompt_id="PRM-OPS-035",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #35?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-036": ReviewPromptRecord(
        prompt_id="PRM-OPS-036",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #36?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-037": ReviewPromptRecord(
        prompt_id="PRM-OPS-037",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #37?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-038": ReviewPromptRecord(
        prompt_id="PRM-OPS-038",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #38?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-039": ReviewPromptRecord(
        prompt_id="PRM-OPS-039",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #39?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-040": ReviewPromptRecord(
        prompt_id="PRM-OPS-040",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #40?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-041": ReviewPromptRecord(
        prompt_id="PRM-OPS-041",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #41?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-042": ReviewPromptRecord(
        prompt_id="PRM-OPS-042",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #42?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-043": ReviewPromptRecord(
        prompt_id="PRM-OPS-043",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #43?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-044": ReviewPromptRecord(
        prompt_id="PRM-OPS-044",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #44?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-045": ReviewPromptRecord(
        prompt_id="PRM-OPS-045",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #45?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-046": ReviewPromptRecord(
        prompt_id="PRM-OPS-046",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #46?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-047": ReviewPromptRecord(
        prompt_id="PRM-OPS-047",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #47?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-048": ReviewPromptRecord(
        prompt_id="PRM-OPS-048",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #48?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-049": ReviewPromptRecord(
        prompt_id="PRM-OPS-049",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #49?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
    "PRM-OPS-050": ReviewPromptRecord(
        prompt_id="PRM-OPS-050",
        domain_family="Operations, Finance & Compliance",
        competency_area="Core Functional Excellence",
        prompt_question="How effectively did this individual demonstrate excellence in Operations, Finance & Compliance deliverable #50?",
        scoring_anchors={
            1: "Performance falls significantly below role expectations; requires close remediation.",
            2: "Partially meets expectations; inconsistent execution on complex deliverables.",
            3: "Consistently meets high performance standard for current grade level.",
            4: "Regularly exceeds targets and provides mentorship to cross-functional peers.",
            5: "Exemplary role model and visionary multiplier across the organization.",
        },
        development_action="Set targeted 6-month developmental milestone in individual growth plan."
    ),
}

class MasterReviewPromptService:
    @classmethod
    def get_prompt(cls, pid: str) -> ReviewPromptRecord:
        return MASTER_250_REVIEW_PROMPTS.get(pid)

    @classmethod
    def get_all(cls) -> List[ReviewPromptRecord]:
        return list(MASTER_250_REVIEW_PROMPTS.values())
