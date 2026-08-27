"""
Workplace Psychological Safety & Sentiment VADER Lexicon Engine
Analyzes peer kudos, pulse survey open-text responses, and support tickets for burnout markers and psychological safety.
"""
from typing import Dict, List, Any, Tuple
import re


class WorkplaceSentimentLexiconEngine:
    # Weighted Workplace Affective Lexicon
    POSITIVE_WORDS: Dict[str, float] = {
        "supported": 2.5, "collaborative": 2.2, "appreciated": 2.8, "empowered": 3.0,
        "inclusive": 2.4, "innovative": 2.1, "transparent": 2.3, "balanced": 2.0,
        "rewarding": 2.6, "inspiring": 2.7, "clear": 1.8, "encouraging": 2.2,
        "excellent": 2.5, "kudos": 3.0, "great": 1.8, "helpful": 1.9,
    }

    BURNOUT_NEGATIVE_WORDS: Dict[str, float] = {
        "exhausted": -3.2, "overwhelmed": -3.0, "micromanaged": -3.5, "toxic": -3.8,
        "burnt out": -3.5, "burnout": -3.5, "unsupported": -2.8, "unrealistic": -2.5,
        "isolated": -2.4, "stagnant": -2.2, "frustrated": -2.6, "confusing": -1.9,
        "stressful": -2.5, "disrespected": -3.4, "ignored": -2.7, "unfair": -2.9
    }

    @classmethod
    def score_text_sentiment(cls, text: str) -> Dict[str, Any]:
        lower = text.lower()
        pos_score = 0.0
        neg_score = 0.0
        matched_pos = []
        matched_neg = []

        for word, weight in cls.POSITIVE_WORDS.items():
            if re.search(r"\\b" + re.escape(word) + r"\\b", lower):
                pos_score += weight
                matched_pos.append(word)

        for word, weight in cls.BURNOUT_NEGATIVE_WORDS.items():
            if re.search(r"\\b" + re.escape(word) + r"\\b", lower):
                neg_score += abs(weight)
                matched_neg.append(word)

        raw_sentiment = pos_score - neg_score
        normalized = max(-1.0, min(1.0, raw_sentiment / 5.0))

        has_burnout_flag = neg_score >= 3.0 or any(w in matched_neg for w in ["toxic", "burnout", "burnt out", "micromanaged"])

        return {
            "text_sample": text[:100],
            "sentiment_score": round(normalized, 2),
            "is_positive": normalized > 0.1,
            "has_burnout_risk_signal": has_burnout_flag,
            "positive_keywords_detected": matched_pos,
            "negative_stress_markers": matched_neg
        }
