from typing import List, Dict

def aggregate_performance_review(peer_ratings: List[float], manager_rating: float, okr_progress_pct: float) -> dict:
    avg_peer = sum(peer_ratings) / len(peer_ratings) if peer_ratings else 3.0
    # 40% Manager, 30% Peer 360, 30% OKR score
    composite_score = round((manager_rating * 0.40) + (avg_peer * 0.30) + ((okr_progress_pct / 20.0) * 0.30), 2)
    rating_band = "EXCEEDS_EXPECTATIONS" if composite_score >= 4.2 else "MEETS_EXPECTATIONS" if composite_score >= 3.0 else "NEEDS_IMPROVEMENT"
    return {
        "avg_peer_rating": round(avg_peer, 2),
        "manager_rating": manager_rating,
        "okr_progress_pct": okr_progress_pct,
        "composite_score": composite_score,
        "rating_band": rating_band
    }
