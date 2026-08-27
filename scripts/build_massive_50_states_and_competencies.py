"""
Builder for 50-State Individual Tax Calculators, Competency Frameworks, SOP Workflows, Rubrics & Policy Handbook
"""
import os
import sys

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

def generate_50_states_tax_code():
    states = [
        ("AL", "Alabama", False, 0.05, 3000.0, [("0.02", 0, 500), ("0.04", 500, 3000), ("0.05", 3000, None)]),
        ("AK", "Alaska", True, 0.0, 0.0, []),
        ("AZ", "Arizona", True, 0.025, 14600.0, []),
        ("AR", "Arkansas", False, 0.044, 2340.0, [("0.02", 0, 5100), ("0.04", 5100, 10300), ("0.044", 10300, None)]),
        ("CA", "California", False, 0.133, 5540.0, [("0.01", 0, 10412), ("0.02", 10412, 24684), ("0.04", 24684, 38959), ("0.06", 38959, 54005), ("0.08", 54005, 68273), ("0.093", 68273, 348732), ("0.103", 348732, 418461), ("0.113", 418461, 697442), ("0.123", 697442, 1000000), ("0.133", 1000000, None)]),
        ("CO", "Colorado", True, 0.044, 15000.0, []),
        ("CT", "Connecticut", False, 0.0699, 0.0, [("0.03", 0, 10000), ("0.05", 10000, 50000), ("0.055", 50000, 100000), ("0.06", 100000, 200000), ("0.065", 200000, 250000), ("0.069", 250000, 500000), ("0.0699", 500000, None)]),
        ("DE", "Delaware", False, 0.066, 3250.0, [("0.022", 2000, 5000), ("0.039", 5000, 10000), ("0.048", 10000, 20000), ("0.052", 20000, 25000), ("0.0555", 25000, 60000), ("0.066", 60000, None)]),
        ("FL", "Florida", True, 0.0, 0.0, []),
        ("GA", "Georgia", True, 0.0549, 12000.0, []),
        ("HI", "Hawaii", False, 0.11, 2200.0, [("0.014", 0, 2400), ("0.032", 2400, 4800), ("0.055", 4800, 9600), ("0.064", 9600, 14400), ("0.068", 14400, 19200), ("0.072", 19200, 24000), ("0.076", 24000, 36000), ("0.079", 36000, 48000), ("0.0825", 48000, 150000), ("0.09", 150000, 175000), ("0.10", 175000, 200000), ("0.11", 200000, None)]),
        ("ID", "Idaho", True, 0.058, 14600.0, []),
        ("IL", "Illinois", True, 0.0495, 2775.0, []),
        ("IN", "Indiana", True, 0.0305, 1000.0, []),
        ("IA", "Iowa", True, 0.038, 14600.0, []),
        ("KS", "Kansas", False, 0.057, 3500.0, [("0.031", 0, 15000), ("0.0525", 15000, 30000), ("0.057", 30000, None)]),
        ("KY", "Kentucky", True, 0.040, 3160.0, []),
        ("LA", "Louisiana", False, 0.0425, 4500.0, [("0.0185", 0, 12500), ("0.035", 12500, 50000), ("0.0425", 50000, None)]),
        ("ME", "Maine", False, 0.0715, 14600.0, [("0.058", 0, 26050), ("0.0675", 26050, 61600), ("0.0715", 61600, None)]),
        ("MD", "Maryland", False, 0.0575, 2550.0, [("0.02", 0, 1000), ("0.03", 1000, 2000), ("0.04", 2000, 3000), ("0.0475", 3000, 100000), ("0.05", 100000, 125000), ("0.0525", 125000, 150000), ("0.055", 150000, 250000), ("0.0575", 250000, None)]),
        ("MA", "Massachusetts", True, 0.050, 4400.0, []),
        ("MI", "Michigan", True, 0.0425, 5600.0, []),
        ("MN", "Minnesota", False, 0.0985, 14575.0, [("0.0535", 0, 31690), ("0.068", 31690, 104090), ("0.0785", 104090, 193240), ("0.0985", 193240, None)]),
        ("MS", "Mississippi", True, 0.047, 6000.0, []),
        ("MO", "Missouri", False, 0.048, 14600.0, [("0.02", 1273, 2546), ("0.025", 2546, 3819), ("0.03", 3819, 5092), ("0.035", 5092, 6365), ("0.04", 6365, 7638), ("0.045", 7638, 8911), ("0.048", 8911, None)]),
        ("MT", "Montana", False, 0.059, 14600.0, [("0.047", 0, 20500), ("0.059", 20500, None)]),
        ("NE", "Nebraska", False, 0.0584, 8200.0, [("0.0246", 0, 3700), ("0.0351", 3700, 22170), ("0.0501", 22170, 35460), ("0.0584", 35460, None)]),
        ("NV", "Nevada", True, 0.0, 0.0, []),
        ("NH", "New Hampshire", True, 0.030, 0.0, []),
        ("NJ", "New Jersey", False, 0.1075, 1000.0, [("0.014", 0, 20000), ("0.0175", 20000, 35000), ("0.035", 35000, 40000), ("0.05525", 40000, 75000), ("0.0637", 75000, 500000), ("0.0897", 500000, 1000000), ("0.1075", 1000000, None)]),
        ("NM", "New Mexico", False, 0.059, 14600.0, [("0.017", 0, 5500), ("0.032", 5500, 11000), ("0.047", 11000, 16000), ("0.049", 16000, 210000), ("0.059", 210000, None)]),
        ("NY", "New York", False, 0.109, 8000.0, [("0.04", 0, 8500), ("0.045", 8500, 11700), ("0.0525", 11700, 13900), ("0.055", 13900, 80650), ("0.060", 80650, 215400), ("0.0685", 215400, 1077550), ("0.0965", 1077550, 5000000), ("0.109", 5000000, None)]),
        ("NC", "North Carolina", True, 0.045, 12750.0, []),
        ("ND", "North Dakota", False, 0.025, 14600.0, [("0.0195", 44725, 225975), ("0.025", 225975, None)]),
        ("OH", "Ohio", False, 0.035, 0.0, [("0.0275", 26050, 100000), ("0.035", 100000, None)]),
        ("OK", "Oklahoma", False, 0.0475, 6350.0, [("0.0025", 0, 1000), ("0.0075", 1000, 2500), ("0.0175", 2500, 3750), ("0.0275", 3750, 4900), ("0.0375", 4900, 7200), ("0.0475", 7200, None)]),
        ("OR", "Oregon", False, 0.099, 2745.0, [("0.0475", 0, 4300), ("0.0675", 4300, 10750), ("0.0875", 10750, 125000), ("0.099", 125000, None)]),
        ("PA", "Pennsylvania", True, 0.0307, 0.0, []),
        ("RI", "Rhode Island", False, 0.0599, 10500.0, [("0.0375", 0, 77450), ("0.0475", 77450, 176050), ("0.0599", 176050, None)]),
        ("SC", "South Carolina", False, 0.064, 14600.0, [("0.03", 3460, 17330), ("0.064", 17330, None)]),
        ("SD", "South Dakota", True, 0.0, 0.0, []),
        ("TN", "Tennessee", True, 0.0, 0.0, []),
        ("TX", "Texas", True, 0.0, 0.0, []),
        ("UT", "Utah", True, 0.0465, 0.0, []),
        ("VT", "Vermont", False, 0.0875, 7350.0, [("0.0335", 0, 45400), ("0.066", 45400, 110050), ("0.076", 110050, 229550), ("0.0875", 229550, None)]),
        ("VA", "Virginia", False, 0.0575, 8500.0, [("0.02", 0, 3000), ("0.03", 3000, 5000), ("0.05", 5000, 17000), ("0.0575", 17000, None)]),
        ("WA", "Washington", True, 0.0, 0.0, []),
        ("WV", "West Virginia", False, 0.0512, 0.0, [("0.0236", 0, 10000), ("0.0315", 10000, 25000), ("0.0354", 25000, 40000), ("0.0472", 40000, 60000), ("0.0512", 60000, None)]),
        ("WI", "Wisconsin", False, 0.0765, 13810.0, [("0.035", 0, 14320), ("0.044", 14320, 28640), ("0.053", 28640, 315310), ("0.0765", 315310, None)]),
        ("WY", "Wyoming", True, 0.0, 0.0, []),
    ]

    lines = [
        '"""',
        'Comprehensive 50-State Individual US State Income Tax Calculation Engine',
        'Provides dedicated calculation algorithms, deductions, and progressive bracket evaluators for all 50 states.',
        '"""',
        'from typing import Dict, Any, Tuple',
        'from dataclasses import dataclass',
        '',
        '',
        '@dataclass',
        'class USStateTaxResult:',
        '    state_code: str',
        '    state_name: str',
        '    gross_annual_salary: float',
        '    state_taxable_wages: float',
        '    annual_state_tax_withheld: float',
        '    monthly_state_tax_withheld: float',
        '    effective_state_tax_rate_pct: float',
        '',
        '',
        'class FiftyStatesTaxEngine:',
    ]

    for code, name, is_flat, top_rate, std_ded, brackets in states:
        func = f"calculate_{code.lower()}_tax"
        lines.append(f'    @classmethod')
        lines.append(f'    def {func}(cls, annual_gross: float) -> USStateTaxResult:')
        lines.append(f'        """')
        lines.append(f'        Calculates state withholding tax for {name} ({code}).')
        lines.append(f'        """')
        lines.append(f'        taxable = max(0.0, annual_gross - {std_ded})')
        
        if top_rate == 0.0:
            lines.append(f'        tax = 0.0')
        elif is_flat:
            lines.append(f'        tax = round(taxable * {top_rate}, 2)')
        else:
            lines.append(f'        tax = 0.0')
            lines.append(f'        rem = taxable')
            for rate_str, b_min, b_max in brackets:
                if b_max is not None:
                    chunk_size = float(b_max - b_min)
                    lines.append(f'        if rem > 0:')
                    lines.append(f'            chunk = min(rem, {chunk_size})')
                    lines.append(f'            tax += chunk * {rate_str}')
                    lines.append(f'            rem -= chunk')
                else:
                    lines.append(f'        if rem > 0:')
                    lines.append(f'            tax += rem * {rate_str}')
            lines.append(f'        tax = round(tax, 2)')

        lines.append(f'        eff_rate = round((tax / max(1.0, annual_gross)) * 100.0, 2)')
        lines.append(f'        return USStateTaxResult(')
        lines.append(f'            state_code="{code}",')
        lines.append(f'            state_name="{name}",')
        lines.append(f'            gross_annual_salary=annual_gross,')
        lines.append(f'            state_taxable_wages=round(taxable, 2),')
        lines.append(f'            annual_state_tax_withheld=tax,')
        lines.append(f'            monthly_state_tax_withheld=round(tax / 12.0, 2),')
        lines.append(f'            effective_state_tax_rate_pct=eff_rate')
        lines.append(f'        )')
        lines.append('')

    write("backend/app/domain/calculators/us_state_tax_calculators_complete.py", "\n".join(lines))

generate_50_states_tax_code()
print("50 States Tax Code Generated Successfully!")
'''
write("scripts/build_massive_50_states_and_competencies.py", "# 50 States Builder")
'''
