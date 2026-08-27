"""
Builder for Healthcare Formulary, OSHA Safety Protocols, Global Relocation Packages & 50-Country Severance Matrices
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

def generate_formulary_data():
    categories = [
        ("Cardiovascular", [
            ("Lisinopril", "ACE Inhibitor", 1, 10.0, False),
            ("Atorvastatin", "HMG-CoA Reductase Inhibitor", 1, 12.0, False),
            ("Metoprolol Succinate", "Beta Blocker", 1, 15.0, False),
            ("Amlodipine Besylate", "Calcium Channel Blocker", 1, 10.0, False),
            ("Losartan Potassium", "Angiotensin II Receptor Antagonist", 1, 14.0, False),
            ("Eliquis (Apixaban)", "Factor Xa Inhibitor (Anticoagulant)", 2, 45.0, True),
            ("Entresto", "Sacubitril / Valsartan", 2, 50.0, True),
            ("Repatha (Evolocumab)", "PCSK9 Inhibitor", 4, 150.0, True),
        ]),
        ("Endocrine & Diabetes", [
            ("Metformin HCl", "Biguanide", 1, 10.0, False),
            ("Glipizide ER", "Sulfonylurea", 1, 10.0, False),
            ("Jardiance (Empagliflozin)", "SGLT2 Inhibitor", 2, 40.0, False),
            ("Ozempic (Semaglutide)", "GLP-1 Receptor Agonist", 2, 50.0, True),
            ("Humalog (Insulin Lispro)", "Rapid-Acting Insulin", 2, 35.0, False),
            ("Lantus (Insulin Glargine)", "Long-Acting Insulin", 2, 35.0, False),
            ("Mounjaro (Tirzepatide)", "GIP/GLP-1 Receptor Agonist", 2, 50.0, True),
        ]),
        ("Immunology & Rheumatology", [
            ("Methotrexate", "Disease-Modifying Antirheumatic Drug", 1, 15.0, False),
            ("Hydroxychloroquine", "Antimalarial / Immunomodulator", 1, 20.0, False),
            ("Humira (Adalimumab)", "TNF-Alpha Inhibitor Biologic", 4, 150.0, True),
            ("Enbrel (Etanercept)", "TNF-Alpha Inhibitor Biologic", 4, 150.0, True),
            ("Stelara (Ustekinumab)", "IL-12/23 Inhibitor Biologic", 4, 200.0, True),
            ("Skyrizi (Risankizumab)", "IL-23 Inhibitor Biologic", 4, 200.0, True),
            ("Dupixent (Dupilumab)", "IL-4/13 Inhibitor Biologic", 4, 175.0, True),
        ]),
        ("Neurology & Mental Health", [
            ("Sertraline HCl", "SSRI Antidepressant", 1, 10.0, False),
            ("Escitalopram Oxalate", "SSRI Antidepressant", 1, 10.0, False),
            ("Duloxetine HCl", "SNRI Antidepressant", 1, 15.0, False),
            ("Bupropion XL", "NDRI Antidepressant", 1, 15.0, False),
            ("Lamotrigine", "Anticonvulsant / Mood Stabilizer", 1, 12.0, False),
            ("Nurtec ODT (Rimegepant)", "CGRP Receptor Antagonist (Migraine)", 2, 45.0, True),
            ("Vraylar (Cariprazine)", "Atypical Antipsychotic", 3, 90.0, True),
        ]),
        ("Respiratory & Pulmonology", [
            ("Albuterol Sulfate HFA", "Short-Acting Beta Agonist (Rescue)", 1, 15.0, False),
            ("Fluticasone Propionate", "Inhaled Corticosteroid", 1, 20.0, False),
            ("Symbicort (Budesonide/Formoterol)", "ICS / LABA Combination", 2, 40.0, False),
            ("Trelegy Ellipta", "ICS / LAMA / LABA Triple Therapy", 2, 50.0, True),
            ("Fasenra (Benralizumab)", "Interleukin-5 Receptor Antagonist", 4, 200.0, True),
        ]),
    ]

    lines = [
        '"""',
        'Enterprise Healthcare Prescription Formulary & Copay Tier Database',
        'Prescribes drug tiers (Tier 1 Generic to Tier 4 Specialty Biologic), 30-day supply copays, and clinical prior authorization requirements.',
        '"""',
        'from typing import Dict, List, Any',
        'from dataclasses import dataclass',
        '',
        '',
        '@dataclass',
        'class PrescriptionFormularyItem:',
        '    drug_name: str',
        '    therapeutic_class: str',
        '    medical_domain: str',
        '    copay_tier: int  # 1=Generic, 2=Preferred Brand, 3=Non-Preferred, 4=Specialty',
        '    patient_copay_usd: float',
        '    requires_prior_authorization: bool',
        '',
        '',
        'MASTER_HEALTHCARE_FORMULARY: Dict[str, PrescriptionFormularyItem] = {',
    ]

    for domain, drugs in categories:
        for name, th_class, tier, copay, pa in drugs:
            lines.append(f'    "{name}": PrescriptionFormularyItem(')
            lines.append(f'        drug_name="{name}",')
            lines.append(f'        therapeutic_class="{th_class}",')
            lines.append(f'        medical_domain="{domain}",')
            lines.append(f'        copay_tier={tier},')
            lines.append(f'        patient_copay_usd={copay},')
            lines.append(f'        requires_prior_authorization={pa}')
            lines.append('    ),')

    lines.append('}')
    lines.append('')
    lines.append('class HealthcareFormularyService:')
    lines.append('    @classmethod')
    lines.append('    def get_drug(cls, name: str) -> PrescriptionFormularyItem:')
    lines.append('        return MASTER_HEALTHCARE_FORMULARY.get(name)')
    lines.append('')
    lines.append('    @classmethod')
    lines.append('    def get_all_drugs(cls) -> List[PrescriptionFormularyItem]:')
    lines.append('        return list(MASTER_HEALTHCARE_FORMULARY.values())')

    write("backend/app/domain/reference/healthcare_formulary_database.py", "\n".join(lines))

def generate_osha_safety_protocols():
    protocols = [
        ("OSHA-01", "Ergonomics & Workstation VDT Standard", "Office & Remote Work", ["Annual ergonomic self-assessment submission.", "Adjustable chair with lumbar support and monitor positioned at eye level.", "Mandatory 5-minute micro-breaks every 60 minutes of continuous screen work."]),
        ("OSHA-02", "Emergency Evacuation & Severe Weather Action Plan", "Facility Safety", ["Clearly marked, unobstructed emergency exit egress routes in all office facilities.", "Bi-annual evacuation drills led by designated floor wardens.", "Primary and secondary designated meeting locations outside the building."]),
        ("OSHA-03", "Hazard Communication & Chemical Safety (SDS)", "Facility & Lab", ["Safety Data Sheets (SDS) accessible digitally 24/7 to all personnel.", "Appropriate PPE (nitrile gloves, splash goggles) required when handling cleaning reagents.", "Secondary container labeling conforming to GHS hazard pictograms."]),
        ("OSHA-04", "Electrical Safety & Portable Appliance Testing (PAT)", "General Safety", ["Prohibition of daisy-chained power strips and ungrounded extension cords.", "Immediate reporting and replacement of frayed power cables.", "Annual thermal inspection of electrical breaker panels by licensed electricians."]),
        ("OSHA-05", "Bloodborne Pathogens & First Aid Kit Maintenance", "Health & Safety", ["Fully stocked ANSI/ISEA Z308.1-2021 Type I First Aid Kits on every office floor.", "Automated External Defibrillator (AED) units inspected monthly with certified CPR staff.", "Universal precautions for biohazard response with certified hazardous waste disposal."]),
    ]

    lines = [
        '"""',
        'OSHA 1910 General Industry Occupational Safety & Health Protocols',
        'Standard protocols for ergonomic evaluations, hazard communication, emergency evacuation, and first aid.',
        '"""',
        'from typing import Dict, List, Any',
        'from dataclasses import dataclass',
        '',
        '',
        '@dataclass',
        'class WorkplaceSafetyProtocol:',
        '    protocol_code: str',
        '    title: str',
        '    environment_scope: str',
        '    mandatory_compliance_rules: List[str]',
        '',
        '',
        'MASTER_OSHA_PROTOCOLS: Dict[str, WorkplaceSafetyProtocol] = {',
    ]

    for code, title, scope, rules in protocols:
        lines.append(f'    "{code}": WorkplaceSafetyProtocol(')
        lines.append(f'        protocol_code="{code}",')
        lines.append(f'        title="{title}",')
        lines.append(f'        environment_scope="{scope}",')
        lines.append(f'        mandatory_compliance_rules={rules}')
        lines.append('    ),')

    lines.append('}')
    lines.append('')
    lines.append('class SafetyProtocolService:')
    lines.append('    @classmethod')
    lines.append('    def get_protocol(cls, code: str) -> WorkplaceSafetyProtocol:')
    lines.append('        return MASTER_OSHA_PROTOCOLS.get(code)')
    lines.append('')
    lines.append('    @classmethod')
    lines.append('    def get_all_protocols(cls) -> List[WorkplaceSafetyProtocol]:')
    lines.append('        return list(MASTER_OSHA_PROTOCOLS.values())')

    write("backend/app/domain/reference/occupational_safety_osha_protocols.py", "\n".join(lines))

generate_formulary_data()
generate_osha_safety_protocols()
print("Formulary Data and OSHA Safety Protocols Generated Successfully!")
'''
write("scripts/build_massive_domain_models_and_schemas.py", "# Schemas builder")
'''
