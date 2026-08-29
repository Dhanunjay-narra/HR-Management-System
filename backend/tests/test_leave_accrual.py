from app.modules.leave.accrual import calculate_year_end_leave_carryover

def test_leave_carryover_calculation():
    res = calculate_year_end_leave_carryover(allocated=24.0, used=10.0, max_carryover=10.0)
    assert res["balance"] == 14.0
    assert res["carried_forward_days"] == 10.0
    assert res["lapsed_or_encashed_days"] == 4.0
