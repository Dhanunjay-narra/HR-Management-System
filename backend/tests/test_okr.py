from app.modules.performance.okr import aggregate_performance_review

def test_performance_okr_evaluation():
    res = aggregate_performance_review(peer_ratings=[4.5, 4.0, 5.0], manager_rating=4.5, okr_progress_pct=90.0)
    assert res["composite_score"] >= 4.2
    assert res["rating_band"] == "EXCEEDS_EXPECTATIONS"
