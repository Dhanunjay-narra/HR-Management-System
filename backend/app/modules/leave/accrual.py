def calculate_year_end_leave_carryover(allocated: float, used: float, max_carryover: float = 10.0) -> dict:
    balance = max(0.0, allocated - used)
    carry_forward = min(balance, max_carryover)
    encashed = max(0.0, balance - carry_forward)
    return {
        "balance": balance,
        "carried_forward_days": carry_forward,
        "lapsed_or_encashed_days": encashed
    }
