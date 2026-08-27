"""
Markov Chain Workforce Talent Mobility & Career Transition Engine
Simulates promotion, lateral transfer, and attrition transition probability matrices across organization levels (L1 through VP).
"""
from typing import Dict, List, Any
import math


class MarkovTalentMobilityEngine:
    LEVELS = ["L1", "L2", "L3", "L4", "L5", "L6", "DIRECTOR", "VP", "EXITED"]

    # Annual Transition Probability Matrix (Row = Current Level, Col = Next Year Level)
    TRANSITION_PROBABILITY_MATRIX: Dict[str, Dict[str, float]] = {
        "L1": {"L1": 0.65, "L2": 0.25, "EXITED": 0.10},
        "L2": {"L2": 0.70, "L3": 0.20, "EXITED": 0.10},
        "L3": {"L3": 0.72, "L4": 0.18, "EXITED": 0.10},
        "L4": {"L4": 0.75, "L5": 0.15, "EXITED": 0.10},
        "L5": {"L5": 0.78, "L6": 0.12, "EXITED": 0.10},
        "L6": {"L6": 0.80, "DIRECTOR": 0.10, "EXITED": 0.10},
        "DIRECTOR": {"DIRECTOR": 0.82, "VP": 0.08, "EXITED": 0.10},
        "VP": {"VP": 0.88, "EXITED": 0.12},
    }

    @classmethod
    def simulate_future_distribution(
        cls,
        current_headcount_by_level: Dict[str, int],
        years: int = 3
    ) -> List[Dict[str, Any]]:
        history = [{"year": 0, "distribution": current_headcount_by_level.copy()}]
        state = {k: float(v) for k, v in current_headcount_by_level.items()}

        for yr in range(1, years + 1):
            next_state: Dict[str, float] = {lvl: 0.0 for lvl in cls.LEVELS}

            for curr_lvl, count in state.items():
                if curr_lvl == "EXITED":
                    next_state["EXITED"] += count
                    continue

                transitions = cls.TRANSITION_PROBABILITY_MATRIX.get(curr_lvl, {curr_lvl: 0.90, "EXITED": 0.10})
                for dest_lvl, prob in transitions.items():
                    next_state[dest_lvl] += count * prob

            # Round state
            state = {k: round(v, 1) for k, v in next_state.items()}
            history.append({"year": yr, "distribution": state.copy()})

        return history
