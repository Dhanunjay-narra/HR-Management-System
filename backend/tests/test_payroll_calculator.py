from app.modules.payroll.calculator import calculate_monthly_salary_breakdown

def test_payroll_tax_breakdown():
    res = calculate_monthly_salary_breakdown(annual_ctc=1200000.0)
    assert res["monthly_gross"] == 100000.0
    assert res["basic_salary"] == 50000.0
    assert res["net_in_hand"] > 80000.0
