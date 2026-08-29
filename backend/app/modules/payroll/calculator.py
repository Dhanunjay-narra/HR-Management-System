def calculate_monthly_salary_breakdown(annual_ctc: float) -> dict:
    monthly_gross = annual_ctc / 12.0
    basic_salary = round(monthly_gross * 0.50, 2)
    hra = round(monthly_gross * 0.25, 2)
    special_allowance = round(monthly_gross - basic_salary - hra, 2)
    
    epf_deduction = round(min(basic_salary, 15000.0) * 0.12, 2)
    professional_tax = 200.0
    tds_estimated = round(monthly_gross * 0.10, 2) if annual_ctc > 750000 else 0.0
    
    total_deductions = epf_deduction + professional_tax + tds_estimated
    net_in_hand = round(monthly_gross - total_deductions, 2)
    
    return {
        "monthly_gross": round(monthly_gross, 2),
        "basic_salary": basic_salary,
        "hra": hra,
        "special_allowance": special_allowance,
        "epf_deduction": epf_deduction,
        "total_deductions": total_deductions,
        "net_in_hand": net_in_hand
    }
