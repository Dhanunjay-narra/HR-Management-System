"""
Candidate Intelligence & Resume Skill Extraction Engine
Provides semantic skill matching against job requirements.
"""
import re
from typing import List, Dict, Any, Tuple

# Comprehensive Technical & Domain Skills Catalog for Match Scoring
SKILLS_TAXONOMY = {
    "python", "fastapi", "django", "flask", "sqlalchemy", "postgresql", "mysql", "mongodb", "redis",
    "rabbitmq", "celery", "docker", "kubernetes", "aws", "gcp", "azure", "react", "typescript",
    "javascript", "html", "css", "tailwind", "node.js", "graphql", "rest api", "ci/cd", "git",
    "linux", "microservices", "unit testing", "pytest", "machine learning", "pytorch", "tensorflow",
    "nlp", "scikit-learn", "agile", "scrum", "project management", "system design", "leadership"
}


class CandidateIntelligenceEngine:
    @staticmethod
    def extract_skills_from_text(text: str) -> List[str]:
        """Extract matched domain skills from raw resume or profile text."""
        if not text:
            return []
        
        lower_text = text.lower()
        extracted: List[str] = []
        
        for skill in SKILLS_TAXONOMY:
            # Check whole word match
            pattern = rf"\b{re.escape(skill)}\b"
            if re.search(pattern, lower_text):
                extracted.append(skill.title() if len(skill) > 3 else skill.upper())
                
        return sorted(list(set(extracted)))

    @staticmethod
    def calculate_match_score(candidate_skills: List[str], required_skills: List[str], candidate_exp_years: float, min_exp_years: float) -> float:
        """
        Calculate 0.0 - 100.0% match score based on skill overlap and experience relevance.
        """
        if not required_skills:
            return 85.0

        cand_set = {s.lower() for s in candidate_skills}
        req_set = {s.lower() for s in required_skills}

        overlap = len(cand_set.intersection(req_set))
        skill_score = (overlap / len(req_set)) * 70.0  # 70% weight on skills

        # Experience score (30% weight)
        exp_score = 30.0
        if min_exp_years > 0:
            exp_ratio = min(1.0, candidate_exp_years / min_exp_years)
            exp_score = exp_ratio * 30.0

        total_score = round(min(100.0, skill_score + exp_score), 1)
        return total_score
