"""
Enterprise Healthcare Prescription Drug Master Formulary Database (500 Medications)
Prescribes drug tiers, patient copays, prior authorization requirements, and therapeutic categories.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class MasterFormularyDrugRecord:
    drug_id: str
    drug_name: str
    therapeutic_category: str
    tier: int
    copay_usd: float
    requires_pa: bool


MASTER_500_DRUG_FORMULARY: Dict[str, MasterFormularyDrugRecord] = {
    "DRUG-0001": MasterFormularyDrugRecord(
        drug_id="DRUG-0001",
        drug_name="Enterprise Medication Formulation DRUG-0001 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0002": MasterFormularyDrugRecord(
        drug_id="DRUG-0002",
        drug_name="Enterprise Medication Formulation DRUG-0002 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0003": MasterFormularyDrugRecord(
        drug_id="DRUG-0003",
        drug_name="Enterprise Medication Formulation DRUG-0003 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0004": MasterFormularyDrugRecord(
        drug_id="DRUG-0004",
        drug_name="Enterprise Medication Formulation DRUG-0004 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0005": MasterFormularyDrugRecord(
        drug_id="DRUG-0005",
        drug_name="Enterprise Medication Formulation DRUG-0005 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0006": MasterFormularyDrugRecord(
        drug_id="DRUG-0006",
        drug_name="Enterprise Medication Formulation DRUG-0006 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0007": MasterFormularyDrugRecord(
        drug_id="DRUG-0007",
        drug_name="Enterprise Medication Formulation DRUG-0007 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0008": MasterFormularyDrugRecord(
        drug_id="DRUG-0008",
        drug_name="Enterprise Medication Formulation DRUG-0008 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0009": MasterFormularyDrugRecord(
        drug_id="DRUG-0009",
        drug_name="Enterprise Medication Formulation DRUG-0009 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0010": MasterFormularyDrugRecord(
        drug_id="DRUG-0010",
        drug_name="Enterprise Medication Formulation DRUG-0010 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0011": MasterFormularyDrugRecord(
        drug_id="DRUG-0011",
        drug_name="Enterprise Medication Formulation DRUG-0011 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0012": MasterFormularyDrugRecord(
        drug_id="DRUG-0012",
        drug_name="Enterprise Medication Formulation DRUG-0012 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0013": MasterFormularyDrugRecord(
        drug_id="DRUG-0013",
        drug_name="Enterprise Medication Formulation DRUG-0013 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0014": MasterFormularyDrugRecord(
        drug_id="DRUG-0014",
        drug_name="Enterprise Medication Formulation DRUG-0014 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0015": MasterFormularyDrugRecord(
        drug_id="DRUG-0015",
        drug_name="Enterprise Medication Formulation DRUG-0015 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0016": MasterFormularyDrugRecord(
        drug_id="DRUG-0016",
        drug_name="Enterprise Medication Formulation DRUG-0016 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0017": MasterFormularyDrugRecord(
        drug_id="DRUG-0017",
        drug_name="Enterprise Medication Formulation DRUG-0017 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0018": MasterFormularyDrugRecord(
        drug_id="DRUG-0018",
        drug_name="Enterprise Medication Formulation DRUG-0018 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0019": MasterFormularyDrugRecord(
        drug_id="DRUG-0019",
        drug_name="Enterprise Medication Formulation DRUG-0019 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0020": MasterFormularyDrugRecord(
        drug_id="DRUG-0020",
        drug_name="Enterprise Medication Formulation DRUG-0020 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0021": MasterFormularyDrugRecord(
        drug_id="DRUG-0021",
        drug_name="Enterprise Medication Formulation DRUG-0021 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0022": MasterFormularyDrugRecord(
        drug_id="DRUG-0022",
        drug_name="Enterprise Medication Formulation DRUG-0022 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0023": MasterFormularyDrugRecord(
        drug_id="DRUG-0023",
        drug_name="Enterprise Medication Formulation DRUG-0023 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0024": MasterFormularyDrugRecord(
        drug_id="DRUG-0024",
        drug_name="Enterprise Medication Formulation DRUG-0024 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0025": MasterFormularyDrugRecord(
        drug_id="DRUG-0025",
        drug_name="Enterprise Medication Formulation DRUG-0025 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0026": MasterFormularyDrugRecord(
        drug_id="DRUG-0026",
        drug_name="Enterprise Medication Formulation DRUG-0026 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0027": MasterFormularyDrugRecord(
        drug_id="DRUG-0027",
        drug_name="Enterprise Medication Formulation DRUG-0027 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0028": MasterFormularyDrugRecord(
        drug_id="DRUG-0028",
        drug_name="Enterprise Medication Formulation DRUG-0028 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0029": MasterFormularyDrugRecord(
        drug_id="DRUG-0029",
        drug_name="Enterprise Medication Formulation DRUG-0029 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0030": MasterFormularyDrugRecord(
        drug_id="DRUG-0030",
        drug_name="Enterprise Medication Formulation DRUG-0030 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0031": MasterFormularyDrugRecord(
        drug_id="DRUG-0031",
        drug_name="Enterprise Medication Formulation DRUG-0031 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0032": MasterFormularyDrugRecord(
        drug_id="DRUG-0032",
        drug_name="Enterprise Medication Formulation DRUG-0032 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0033": MasterFormularyDrugRecord(
        drug_id="DRUG-0033",
        drug_name="Enterprise Medication Formulation DRUG-0033 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0034": MasterFormularyDrugRecord(
        drug_id="DRUG-0034",
        drug_name="Enterprise Medication Formulation DRUG-0034 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0035": MasterFormularyDrugRecord(
        drug_id="DRUG-0035",
        drug_name="Enterprise Medication Formulation DRUG-0035 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0036": MasterFormularyDrugRecord(
        drug_id="DRUG-0036",
        drug_name="Enterprise Medication Formulation DRUG-0036 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0037": MasterFormularyDrugRecord(
        drug_id="DRUG-0037",
        drug_name="Enterprise Medication Formulation DRUG-0037 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0038": MasterFormularyDrugRecord(
        drug_id="DRUG-0038",
        drug_name="Enterprise Medication Formulation DRUG-0038 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0039": MasterFormularyDrugRecord(
        drug_id="DRUG-0039",
        drug_name="Enterprise Medication Formulation DRUG-0039 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0040": MasterFormularyDrugRecord(
        drug_id="DRUG-0040",
        drug_name="Enterprise Medication Formulation DRUG-0040 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0041": MasterFormularyDrugRecord(
        drug_id="DRUG-0041",
        drug_name="Enterprise Medication Formulation DRUG-0041 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0042": MasterFormularyDrugRecord(
        drug_id="DRUG-0042",
        drug_name="Enterprise Medication Formulation DRUG-0042 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0043": MasterFormularyDrugRecord(
        drug_id="DRUG-0043",
        drug_name="Enterprise Medication Formulation DRUG-0043 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0044": MasterFormularyDrugRecord(
        drug_id="DRUG-0044",
        drug_name="Enterprise Medication Formulation DRUG-0044 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0045": MasterFormularyDrugRecord(
        drug_id="DRUG-0045",
        drug_name="Enterprise Medication Formulation DRUG-0045 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0046": MasterFormularyDrugRecord(
        drug_id="DRUG-0046",
        drug_name="Enterprise Medication Formulation DRUG-0046 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0047": MasterFormularyDrugRecord(
        drug_id="DRUG-0047",
        drug_name="Enterprise Medication Formulation DRUG-0047 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0048": MasterFormularyDrugRecord(
        drug_id="DRUG-0048",
        drug_name="Enterprise Medication Formulation DRUG-0048 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0049": MasterFormularyDrugRecord(
        drug_id="DRUG-0049",
        drug_name="Enterprise Medication Formulation DRUG-0049 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0050": MasterFormularyDrugRecord(
        drug_id="DRUG-0050",
        drug_name="Enterprise Medication Formulation DRUG-0050 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0051": MasterFormularyDrugRecord(
        drug_id="DRUG-0051",
        drug_name="Enterprise Medication Formulation DRUG-0051 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0052": MasterFormularyDrugRecord(
        drug_id="DRUG-0052",
        drug_name="Enterprise Medication Formulation DRUG-0052 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0053": MasterFormularyDrugRecord(
        drug_id="DRUG-0053",
        drug_name="Enterprise Medication Formulation DRUG-0053 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0054": MasterFormularyDrugRecord(
        drug_id="DRUG-0054",
        drug_name="Enterprise Medication Formulation DRUG-0054 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0055": MasterFormularyDrugRecord(
        drug_id="DRUG-0055",
        drug_name="Enterprise Medication Formulation DRUG-0055 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0056": MasterFormularyDrugRecord(
        drug_id="DRUG-0056",
        drug_name="Enterprise Medication Formulation DRUG-0056 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0057": MasterFormularyDrugRecord(
        drug_id="DRUG-0057",
        drug_name="Enterprise Medication Formulation DRUG-0057 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0058": MasterFormularyDrugRecord(
        drug_id="DRUG-0058",
        drug_name="Enterprise Medication Formulation DRUG-0058 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0059": MasterFormularyDrugRecord(
        drug_id="DRUG-0059",
        drug_name="Enterprise Medication Formulation DRUG-0059 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0060": MasterFormularyDrugRecord(
        drug_id="DRUG-0060",
        drug_name="Enterprise Medication Formulation DRUG-0060 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0061": MasterFormularyDrugRecord(
        drug_id="DRUG-0061",
        drug_name="Enterprise Medication Formulation DRUG-0061 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0062": MasterFormularyDrugRecord(
        drug_id="DRUG-0062",
        drug_name="Enterprise Medication Formulation DRUG-0062 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0063": MasterFormularyDrugRecord(
        drug_id="DRUG-0063",
        drug_name="Enterprise Medication Formulation DRUG-0063 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0064": MasterFormularyDrugRecord(
        drug_id="DRUG-0064",
        drug_name="Enterprise Medication Formulation DRUG-0064 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0065": MasterFormularyDrugRecord(
        drug_id="DRUG-0065",
        drug_name="Enterprise Medication Formulation DRUG-0065 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0066": MasterFormularyDrugRecord(
        drug_id="DRUG-0066",
        drug_name="Enterprise Medication Formulation DRUG-0066 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0067": MasterFormularyDrugRecord(
        drug_id="DRUG-0067",
        drug_name="Enterprise Medication Formulation DRUG-0067 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0068": MasterFormularyDrugRecord(
        drug_id="DRUG-0068",
        drug_name="Enterprise Medication Formulation DRUG-0068 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0069": MasterFormularyDrugRecord(
        drug_id="DRUG-0069",
        drug_name="Enterprise Medication Formulation DRUG-0069 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0070": MasterFormularyDrugRecord(
        drug_id="DRUG-0070",
        drug_name="Enterprise Medication Formulation DRUG-0070 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0071": MasterFormularyDrugRecord(
        drug_id="DRUG-0071",
        drug_name="Enterprise Medication Formulation DRUG-0071 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0072": MasterFormularyDrugRecord(
        drug_id="DRUG-0072",
        drug_name="Enterprise Medication Formulation DRUG-0072 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0073": MasterFormularyDrugRecord(
        drug_id="DRUG-0073",
        drug_name="Enterprise Medication Formulation DRUG-0073 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0074": MasterFormularyDrugRecord(
        drug_id="DRUG-0074",
        drug_name="Enterprise Medication Formulation DRUG-0074 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0075": MasterFormularyDrugRecord(
        drug_id="DRUG-0075",
        drug_name="Enterprise Medication Formulation DRUG-0075 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0076": MasterFormularyDrugRecord(
        drug_id="DRUG-0076",
        drug_name="Enterprise Medication Formulation DRUG-0076 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0077": MasterFormularyDrugRecord(
        drug_id="DRUG-0077",
        drug_name="Enterprise Medication Formulation DRUG-0077 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0078": MasterFormularyDrugRecord(
        drug_id="DRUG-0078",
        drug_name="Enterprise Medication Formulation DRUG-0078 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0079": MasterFormularyDrugRecord(
        drug_id="DRUG-0079",
        drug_name="Enterprise Medication Formulation DRUG-0079 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0080": MasterFormularyDrugRecord(
        drug_id="DRUG-0080",
        drug_name="Enterprise Medication Formulation DRUG-0080 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0081": MasterFormularyDrugRecord(
        drug_id="DRUG-0081",
        drug_name="Enterprise Medication Formulation DRUG-0081 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0082": MasterFormularyDrugRecord(
        drug_id="DRUG-0082",
        drug_name="Enterprise Medication Formulation DRUG-0082 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0083": MasterFormularyDrugRecord(
        drug_id="DRUG-0083",
        drug_name="Enterprise Medication Formulation DRUG-0083 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0084": MasterFormularyDrugRecord(
        drug_id="DRUG-0084",
        drug_name="Enterprise Medication Formulation DRUG-0084 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0085": MasterFormularyDrugRecord(
        drug_id="DRUG-0085",
        drug_name="Enterprise Medication Formulation DRUG-0085 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0086": MasterFormularyDrugRecord(
        drug_id="DRUG-0086",
        drug_name="Enterprise Medication Formulation DRUG-0086 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0087": MasterFormularyDrugRecord(
        drug_id="DRUG-0087",
        drug_name="Enterprise Medication Formulation DRUG-0087 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0088": MasterFormularyDrugRecord(
        drug_id="DRUG-0088",
        drug_name="Enterprise Medication Formulation DRUG-0088 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0089": MasterFormularyDrugRecord(
        drug_id="DRUG-0089",
        drug_name="Enterprise Medication Formulation DRUG-0089 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0090": MasterFormularyDrugRecord(
        drug_id="DRUG-0090",
        drug_name="Enterprise Medication Formulation DRUG-0090 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0091": MasterFormularyDrugRecord(
        drug_id="DRUG-0091",
        drug_name="Enterprise Medication Formulation DRUG-0091 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0092": MasterFormularyDrugRecord(
        drug_id="DRUG-0092",
        drug_name="Enterprise Medication Formulation DRUG-0092 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0093": MasterFormularyDrugRecord(
        drug_id="DRUG-0093",
        drug_name="Enterprise Medication Formulation DRUG-0093 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0094": MasterFormularyDrugRecord(
        drug_id="DRUG-0094",
        drug_name="Enterprise Medication Formulation DRUG-0094 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0095": MasterFormularyDrugRecord(
        drug_id="DRUG-0095",
        drug_name="Enterprise Medication Formulation DRUG-0095 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0096": MasterFormularyDrugRecord(
        drug_id="DRUG-0096",
        drug_name="Enterprise Medication Formulation DRUG-0096 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0097": MasterFormularyDrugRecord(
        drug_id="DRUG-0097",
        drug_name="Enterprise Medication Formulation DRUG-0097 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0098": MasterFormularyDrugRecord(
        drug_id="DRUG-0098",
        drug_name="Enterprise Medication Formulation DRUG-0098 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0099": MasterFormularyDrugRecord(
        drug_id="DRUG-0099",
        drug_name="Enterprise Medication Formulation DRUG-0099 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0100": MasterFormularyDrugRecord(
        drug_id="DRUG-0100",
        drug_name="Enterprise Medication Formulation DRUG-0100 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0101": MasterFormularyDrugRecord(
        drug_id="DRUG-0101",
        drug_name="Enterprise Medication Formulation DRUG-0101 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0102": MasterFormularyDrugRecord(
        drug_id="DRUG-0102",
        drug_name="Enterprise Medication Formulation DRUG-0102 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0103": MasterFormularyDrugRecord(
        drug_id="DRUG-0103",
        drug_name="Enterprise Medication Formulation DRUG-0103 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0104": MasterFormularyDrugRecord(
        drug_id="DRUG-0104",
        drug_name="Enterprise Medication Formulation DRUG-0104 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0105": MasterFormularyDrugRecord(
        drug_id="DRUG-0105",
        drug_name="Enterprise Medication Formulation DRUG-0105 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0106": MasterFormularyDrugRecord(
        drug_id="DRUG-0106",
        drug_name="Enterprise Medication Formulation DRUG-0106 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0107": MasterFormularyDrugRecord(
        drug_id="DRUG-0107",
        drug_name="Enterprise Medication Formulation DRUG-0107 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0108": MasterFormularyDrugRecord(
        drug_id="DRUG-0108",
        drug_name="Enterprise Medication Formulation DRUG-0108 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0109": MasterFormularyDrugRecord(
        drug_id="DRUG-0109",
        drug_name="Enterprise Medication Formulation DRUG-0109 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0110": MasterFormularyDrugRecord(
        drug_id="DRUG-0110",
        drug_name="Enterprise Medication Formulation DRUG-0110 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0111": MasterFormularyDrugRecord(
        drug_id="DRUG-0111",
        drug_name="Enterprise Medication Formulation DRUG-0111 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0112": MasterFormularyDrugRecord(
        drug_id="DRUG-0112",
        drug_name="Enterprise Medication Formulation DRUG-0112 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0113": MasterFormularyDrugRecord(
        drug_id="DRUG-0113",
        drug_name="Enterprise Medication Formulation DRUG-0113 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0114": MasterFormularyDrugRecord(
        drug_id="DRUG-0114",
        drug_name="Enterprise Medication Formulation DRUG-0114 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0115": MasterFormularyDrugRecord(
        drug_id="DRUG-0115",
        drug_name="Enterprise Medication Formulation DRUG-0115 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0116": MasterFormularyDrugRecord(
        drug_id="DRUG-0116",
        drug_name="Enterprise Medication Formulation DRUG-0116 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0117": MasterFormularyDrugRecord(
        drug_id="DRUG-0117",
        drug_name="Enterprise Medication Formulation DRUG-0117 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0118": MasterFormularyDrugRecord(
        drug_id="DRUG-0118",
        drug_name="Enterprise Medication Formulation DRUG-0118 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0119": MasterFormularyDrugRecord(
        drug_id="DRUG-0119",
        drug_name="Enterprise Medication Formulation DRUG-0119 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0120": MasterFormularyDrugRecord(
        drug_id="DRUG-0120",
        drug_name="Enterprise Medication Formulation DRUG-0120 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0121": MasterFormularyDrugRecord(
        drug_id="DRUG-0121",
        drug_name="Enterprise Medication Formulation DRUG-0121 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0122": MasterFormularyDrugRecord(
        drug_id="DRUG-0122",
        drug_name="Enterprise Medication Formulation DRUG-0122 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0123": MasterFormularyDrugRecord(
        drug_id="DRUG-0123",
        drug_name="Enterprise Medication Formulation DRUG-0123 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0124": MasterFormularyDrugRecord(
        drug_id="DRUG-0124",
        drug_name="Enterprise Medication Formulation DRUG-0124 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0125": MasterFormularyDrugRecord(
        drug_id="DRUG-0125",
        drug_name="Enterprise Medication Formulation DRUG-0125 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0126": MasterFormularyDrugRecord(
        drug_id="DRUG-0126",
        drug_name="Enterprise Medication Formulation DRUG-0126 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0127": MasterFormularyDrugRecord(
        drug_id="DRUG-0127",
        drug_name="Enterprise Medication Formulation DRUG-0127 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0128": MasterFormularyDrugRecord(
        drug_id="DRUG-0128",
        drug_name="Enterprise Medication Formulation DRUG-0128 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0129": MasterFormularyDrugRecord(
        drug_id="DRUG-0129",
        drug_name="Enterprise Medication Formulation DRUG-0129 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0130": MasterFormularyDrugRecord(
        drug_id="DRUG-0130",
        drug_name="Enterprise Medication Formulation DRUG-0130 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0131": MasterFormularyDrugRecord(
        drug_id="DRUG-0131",
        drug_name="Enterprise Medication Formulation DRUG-0131 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0132": MasterFormularyDrugRecord(
        drug_id="DRUG-0132",
        drug_name="Enterprise Medication Formulation DRUG-0132 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0133": MasterFormularyDrugRecord(
        drug_id="DRUG-0133",
        drug_name="Enterprise Medication Formulation DRUG-0133 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0134": MasterFormularyDrugRecord(
        drug_id="DRUG-0134",
        drug_name="Enterprise Medication Formulation DRUG-0134 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0135": MasterFormularyDrugRecord(
        drug_id="DRUG-0135",
        drug_name="Enterprise Medication Formulation DRUG-0135 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0136": MasterFormularyDrugRecord(
        drug_id="DRUG-0136",
        drug_name="Enterprise Medication Formulation DRUG-0136 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0137": MasterFormularyDrugRecord(
        drug_id="DRUG-0137",
        drug_name="Enterprise Medication Formulation DRUG-0137 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0138": MasterFormularyDrugRecord(
        drug_id="DRUG-0138",
        drug_name="Enterprise Medication Formulation DRUG-0138 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0139": MasterFormularyDrugRecord(
        drug_id="DRUG-0139",
        drug_name="Enterprise Medication Formulation DRUG-0139 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0140": MasterFormularyDrugRecord(
        drug_id="DRUG-0140",
        drug_name="Enterprise Medication Formulation DRUG-0140 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0141": MasterFormularyDrugRecord(
        drug_id="DRUG-0141",
        drug_name="Enterprise Medication Formulation DRUG-0141 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0142": MasterFormularyDrugRecord(
        drug_id="DRUG-0142",
        drug_name="Enterprise Medication Formulation DRUG-0142 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0143": MasterFormularyDrugRecord(
        drug_id="DRUG-0143",
        drug_name="Enterprise Medication Formulation DRUG-0143 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0144": MasterFormularyDrugRecord(
        drug_id="DRUG-0144",
        drug_name="Enterprise Medication Formulation DRUG-0144 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0145": MasterFormularyDrugRecord(
        drug_id="DRUG-0145",
        drug_name="Enterprise Medication Formulation DRUG-0145 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0146": MasterFormularyDrugRecord(
        drug_id="DRUG-0146",
        drug_name="Enterprise Medication Formulation DRUG-0146 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0147": MasterFormularyDrugRecord(
        drug_id="DRUG-0147",
        drug_name="Enterprise Medication Formulation DRUG-0147 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0148": MasterFormularyDrugRecord(
        drug_id="DRUG-0148",
        drug_name="Enterprise Medication Formulation DRUG-0148 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0149": MasterFormularyDrugRecord(
        drug_id="DRUG-0149",
        drug_name="Enterprise Medication Formulation DRUG-0149 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0150": MasterFormularyDrugRecord(
        drug_id="DRUG-0150",
        drug_name="Enterprise Medication Formulation DRUG-0150 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0151": MasterFormularyDrugRecord(
        drug_id="DRUG-0151",
        drug_name="Enterprise Medication Formulation DRUG-0151 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0152": MasterFormularyDrugRecord(
        drug_id="DRUG-0152",
        drug_name="Enterprise Medication Formulation DRUG-0152 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0153": MasterFormularyDrugRecord(
        drug_id="DRUG-0153",
        drug_name="Enterprise Medication Formulation DRUG-0153 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0154": MasterFormularyDrugRecord(
        drug_id="DRUG-0154",
        drug_name="Enterprise Medication Formulation DRUG-0154 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0155": MasterFormularyDrugRecord(
        drug_id="DRUG-0155",
        drug_name="Enterprise Medication Formulation DRUG-0155 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0156": MasterFormularyDrugRecord(
        drug_id="DRUG-0156",
        drug_name="Enterprise Medication Formulation DRUG-0156 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0157": MasterFormularyDrugRecord(
        drug_id="DRUG-0157",
        drug_name="Enterprise Medication Formulation DRUG-0157 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0158": MasterFormularyDrugRecord(
        drug_id="DRUG-0158",
        drug_name="Enterprise Medication Formulation DRUG-0158 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0159": MasterFormularyDrugRecord(
        drug_id="DRUG-0159",
        drug_name="Enterprise Medication Formulation DRUG-0159 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0160": MasterFormularyDrugRecord(
        drug_id="DRUG-0160",
        drug_name="Enterprise Medication Formulation DRUG-0160 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0161": MasterFormularyDrugRecord(
        drug_id="DRUG-0161",
        drug_name="Enterprise Medication Formulation DRUG-0161 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0162": MasterFormularyDrugRecord(
        drug_id="DRUG-0162",
        drug_name="Enterprise Medication Formulation DRUG-0162 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0163": MasterFormularyDrugRecord(
        drug_id="DRUG-0163",
        drug_name="Enterprise Medication Formulation DRUG-0163 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0164": MasterFormularyDrugRecord(
        drug_id="DRUG-0164",
        drug_name="Enterprise Medication Formulation DRUG-0164 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0165": MasterFormularyDrugRecord(
        drug_id="DRUG-0165",
        drug_name="Enterprise Medication Formulation DRUG-0165 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0166": MasterFormularyDrugRecord(
        drug_id="DRUG-0166",
        drug_name="Enterprise Medication Formulation DRUG-0166 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0167": MasterFormularyDrugRecord(
        drug_id="DRUG-0167",
        drug_name="Enterprise Medication Formulation DRUG-0167 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0168": MasterFormularyDrugRecord(
        drug_id="DRUG-0168",
        drug_name="Enterprise Medication Formulation DRUG-0168 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0169": MasterFormularyDrugRecord(
        drug_id="DRUG-0169",
        drug_name="Enterprise Medication Formulation DRUG-0169 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0170": MasterFormularyDrugRecord(
        drug_id="DRUG-0170",
        drug_name="Enterprise Medication Formulation DRUG-0170 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0171": MasterFormularyDrugRecord(
        drug_id="DRUG-0171",
        drug_name="Enterprise Medication Formulation DRUG-0171 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0172": MasterFormularyDrugRecord(
        drug_id="DRUG-0172",
        drug_name="Enterprise Medication Formulation DRUG-0172 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0173": MasterFormularyDrugRecord(
        drug_id="DRUG-0173",
        drug_name="Enterprise Medication Formulation DRUG-0173 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0174": MasterFormularyDrugRecord(
        drug_id="DRUG-0174",
        drug_name="Enterprise Medication Formulation DRUG-0174 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0175": MasterFormularyDrugRecord(
        drug_id="DRUG-0175",
        drug_name="Enterprise Medication Formulation DRUG-0175 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0176": MasterFormularyDrugRecord(
        drug_id="DRUG-0176",
        drug_name="Enterprise Medication Formulation DRUG-0176 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0177": MasterFormularyDrugRecord(
        drug_id="DRUG-0177",
        drug_name="Enterprise Medication Formulation DRUG-0177 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0178": MasterFormularyDrugRecord(
        drug_id="DRUG-0178",
        drug_name="Enterprise Medication Formulation DRUG-0178 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0179": MasterFormularyDrugRecord(
        drug_id="DRUG-0179",
        drug_name="Enterprise Medication Formulation DRUG-0179 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0180": MasterFormularyDrugRecord(
        drug_id="DRUG-0180",
        drug_name="Enterprise Medication Formulation DRUG-0180 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0181": MasterFormularyDrugRecord(
        drug_id="DRUG-0181",
        drug_name="Enterprise Medication Formulation DRUG-0181 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0182": MasterFormularyDrugRecord(
        drug_id="DRUG-0182",
        drug_name="Enterprise Medication Formulation DRUG-0182 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0183": MasterFormularyDrugRecord(
        drug_id="DRUG-0183",
        drug_name="Enterprise Medication Formulation DRUG-0183 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0184": MasterFormularyDrugRecord(
        drug_id="DRUG-0184",
        drug_name="Enterprise Medication Formulation DRUG-0184 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0185": MasterFormularyDrugRecord(
        drug_id="DRUG-0185",
        drug_name="Enterprise Medication Formulation DRUG-0185 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0186": MasterFormularyDrugRecord(
        drug_id="DRUG-0186",
        drug_name="Enterprise Medication Formulation DRUG-0186 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0187": MasterFormularyDrugRecord(
        drug_id="DRUG-0187",
        drug_name="Enterprise Medication Formulation DRUG-0187 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0188": MasterFormularyDrugRecord(
        drug_id="DRUG-0188",
        drug_name="Enterprise Medication Formulation DRUG-0188 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0189": MasterFormularyDrugRecord(
        drug_id="DRUG-0189",
        drug_name="Enterprise Medication Formulation DRUG-0189 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0190": MasterFormularyDrugRecord(
        drug_id="DRUG-0190",
        drug_name="Enterprise Medication Formulation DRUG-0190 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0191": MasterFormularyDrugRecord(
        drug_id="DRUG-0191",
        drug_name="Enterprise Medication Formulation DRUG-0191 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0192": MasterFormularyDrugRecord(
        drug_id="DRUG-0192",
        drug_name="Enterprise Medication Formulation DRUG-0192 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0193": MasterFormularyDrugRecord(
        drug_id="DRUG-0193",
        drug_name="Enterprise Medication Formulation DRUG-0193 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0194": MasterFormularyDrugRecord(
        drug_id="DRUG-0194",
        drug_name="Enterprise Medication Formulation DRUG-0194 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0195": MasterFormularyDrugRecord(
        drug_id="DRUG-0195",
        drug_name="Enterprise Medication Formulation DRUG-0195 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0196": MasterFormularyDrugRecord(
        drug_id="DRUG-0196",
        drug_name="Enterprise Medication Formulation DRUG-0196 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0197": MasterFormularyDrugRecord(
        drug_id="DRUG-0197",
        drug_name="Enterprise Medication Formulation DRUG-0197 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0198": MasterFormularyDrugRecord(
        drug_id="DRUG-0198",
        drug_name="Enterprise Medication Formulation DRUG-0198 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0199": MasterFormularyDrugRecord(
        drug_id="DRUG-0199",
        drug_name="Enterprise Medication Formulation DRUG-0199 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0200": MasterFormularyDrugRecord(
        drug_id="DRUG-0200",
        drug_name="Enterprise Medication Formulation DRUG-0200 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0201": MasterFormularyDrugRecord(
        drug_id="DRUG-0201",
        drug_name="Enterprise Medication Formulation DRUG-0201 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0202": MasterFormularyDrugRecord(
        drug_id="DRUG-0202",
        drug_name="Enterprise Medication Formulation DRUG-0202 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0203": MasterFormularyDrugRecord(
        drug_id="DRUG-0203",
        drug_name="Enterprise Medication Formulation DRUG-0203 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0204": MasterFormularyDrugRecord(
        drug_id="DRUG-0204",
        drug_name="Enterprise Medication Formulation DRUG-0204 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0205": MasterFormularyDrugRecord(
        drug_id="DRUG-0205",
        drug_name="Enterprise Medication Formulation DRUG-0205 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0206": MasterFormularyDrugRecord(
        drug_id="DRUG-0206",
        drug_name="Enterprise Medication Formulation DRUG-0206 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0207": MasterFormularyDrugRecord(
        drug_id="DRUG-0207",
        drug_name="Enterprise Medication Formulation DRUG-0207 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0208": MasterFormularyDrugRecord(
        drug_id="DRUG-0208",
        drug_name="Enterprise Medication Formulation DRUG-0208 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0209": MasterFormularyDrugRecord(
        drug_id="DRUG-0209",
        drug_name="Enterprise Medication Formulation DRUG-0209 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0210": MasterFormularyDrugRecord(
        drug_id="DRUG-0210",
        drug_name="Enterprise Medication Formulation DRUG-0210 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0211": MasterFormularyDrugRecord(
        drug_id="DRUG-0211",
        drug_name="Enterprise Medication Formulation DRUG-0211 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0212": MasterFormularyDrugRecord(
        drug_id="DRUG-0212",
        drug_name="Enterprise Medication Formulation DRUG-0212 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0213": MasterFormularyDrugRecord(
        drug_id="DRUG-0213",
        drug_name="Enterprise Medication Formulation DRUG-0213 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0214": MasterFormularyDrugRecord(
        drug_id="DRUG-0214",
        drug_name="Enterprise Medication Formulation DRUG-0214 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0215": MasterFormularyDrugRecord(
        drug_id="DRUG-0215",
        drug_name="Enterprise Medication Formulation DRUG-0215 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0216": MasterFormularyDrugRecord(
        drug_id="DRUG-0216",
        drug_name="Enterprise Medication Formulation DRUG-0216 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0217": MasterFormularyDrugRecord(
        drug_id="DRUG-0217",
        drug_name="Enterprise Medication Formulation DRUG-0217 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0218": MasterFormularyDrugRecord(
        drug_id="DRUG-0218",
        drug_name="Enterprise Medication Formulation DRUG-0218 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0219": MasterFormularyDrugRecord(
        drug_id="DRUG-0219",
        drug_name="Enterprise Medication Formulation DRUG-0219 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0220": MasterFormularyDrugRecord(
        drug_id="DRUG-0220",
        drug_name="Enterprise Medication Formulation DRUG-0220 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0221": MasterFormularyDrugRecord(
        drug_id="DRUG-0221",
        drug_name="Enterprise Medication Formulation DRUG-0221 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0222": MasterFormularyDrugRecord(
        drug_id="DRUG-0222",
        drug_name="Enterprise Medication Formulation DRUG-0222 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0223": MasterFormularyDrugRecord(
        drug_id="DRUG-0223",
        drug_name="Enterprise Medication Formulation DRUG-0223 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0224": MasterFormularyDrugRecord(
        drug_id="DRUG-0224",
        drug_name="Enterprise Medication Formulation DRUG-0224 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0225": MasterFormularyDrugRecord(
        drug_id="DRUG-0225",
        drug_name="Enterprise Medication Formulation DRUG-0225 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0226": MasterFormularyDrugRecord(
        drug_id="DRUG-0226",
        drug_name="Enterprise Medication Formulation DRUG-0226 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0227": MasterFormularyDrugRecord(
        drug_id="DRUG-0227",
        drug_name="Enterprise Medication Formulation DRUG-0227 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0228": MasterFormularyDrugRecord(
        drug_id="DRUG-0228",
        drug_name="Enterprise Medication Formulation DRUG-0228 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0229": MasterFormularyDrugRecord(
        drug_id="DRUG-0229",
        drug_name="Enterprise Medication Formulation DRUG-0229 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0230": MasterFormularyDrugRecord(
        drug_id="DRUG-0230",
        drug_name="Enterprise Medication Formulation DRUG-0230 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0231": MasterFormularyDrugRecord(
        drug_id="DRUG-0231",
        drug_name="Enterprise Medication Formulation DRUG-0231 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0232": MasterFormularyDrugRecord(
        drug_id="DRUG-0232",
        drug_name="Enterprise Medication Formulation DRUG-0232 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0233": MasterFormularyDrugRecord(
        drug_id="DRUG-0233",
        drug_name="Enterprise Medication Formulation DRUG-0233 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0234": MasterFormularyDrugRecord(
        drug_id="DRUG-0234",
        drug_name="Enterprise Medication Formulation DRUG-0234 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0235": MasterFormularyDrugRecord(
        drug_id="DRUG-0235",
        drug_name="Enterprise Medication Formulation DRUG-0235 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0236": MasterFormularyDrugRecord(
        drug_id="DRUG-0236",
        drug_name="Enterprise Medication Formulation DRUG-0236 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0237": MasterFormularyDrugRecord(
        drug_id="DRUG-0237",
        drug_name="Enterprise Medication Formulation DRUG-0237 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0238": MasterFormularyDrugRecord(
        drug_id="DRUG-0238",
        drug_name="Enterprise Medication Formulation DRUG-0238 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0239": MasterFormularyDrugRecord(
        drug_id="DRUG-0239",
        drug_name="Enterprise Medication Formulation DRUG-0239 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0240": MasterFormularyDrugRecord(
        drug_id="DRUG-0240",
        drug_name="Enterprise Medication Formulation DRUG-0240 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0241": MasterFormularyDrugRecord(
        drug_id="DRUG-0241",
        drug_name="Enterprise Medication Formulation DRUG-0241 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0242": MasterFormularyDrugRecord(
        drug_id="DRUG-0242",
        drug_name="Enterprise Medication Formulation DRUG-0242 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0243": MasterFormularyDrugRecord(
        drug_id="DRUG-0243",
        drug_name="Enterprise Medication Formulation DRUG-0243 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0244": MasterFormularyDrugRecord(
        drug_id="DRUG-0244",
        drug_name="Enterprise Medication Formulation DRUG-0244 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0245": MasterFormularyDrugRecord(
        drug_id="DRUG-0245",
        drug_name="Enterprise Medication Formulation DRUG-0245 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0246": MasterFormularyDrugRecord(
        drug_id="DRUG-0246",
        drug_name="Enterprise Medication Formulation DRUG-0246 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0247": MasterFormularyDrugRecord(
        drug_id="DRUG-0247",
        drug_name="Enterprise Medication Formulation DRUG-0247 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0248": MasterFormularyDrugRecord(
        drug_id="DRUG-0248",
        drug_name="Enterprise Medication Formulation DRUG-0248 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0249": MasterFormularyDrugRecord(
        drug_id="DRUG-0249",
        drug_name="Enterprise Medication Formulation DRUG-0249 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0250": MasterFormularyDrugRecord(
        drug_id="DRUG-0250",
        drug_name="Enterprise Medication Formulation DRUG-0250 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0251": MasterFormularyDrugRecord(
        drug_id="DRUG-0251",
        drug_name="Enterprise Medication Formulation DRUG-0251 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0252": MasterFormularyDrugRecord(
        drug_id="DRUG-0252",
        drug_name="Enterprise Medication Formulation DRUG-0252 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0253": MasterFormularyDrugRecord(
        drug_id="DRUG-0253",
        drug_name="Enterprise Medication Formulation DRUG-0253 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0254": MasterFormularyDrugRecord(
        drug_id="DRUG-0254",
        drug_name="Enterprise Medication Formulation DRUG-0254 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0255": MasterFormularyDrugRecord(
        drug_id="DRUG-0255",
        drug_name="Enterprise Medication Formulation DRUG-0255 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0256": MasterFormularyDrugRecord(
        drug_id="DRUG-0256",
        drug_name="Enterprise Medication Formulation DRUG-0256 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0257": MasterFormularyDrugRecord(
        drug_id="DRUG-0257",
        drug_name="Enterprise Medication Formulation DRUG-0257 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0258": MasterFormularyDrugRecord(
        drug_id="DRUG-0258",
        drug_name="Enterprise Medication Formulation DRUG-0258 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0259": MasterFormularyDrugRecord(
        drug_id="DRUG-0259",
        drug_name="Enterprise Medication Formulation DRUG-0259 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0260": MasterFormularyDrugRecord(
        drug_id="DRUG-0260",
        drug_name="Enterprise Medication Formulation DRUG-0260 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0261": MasterFormularyDrugRecord(
        drug_id="DRUG-0261",
        drug_name="Enterprise Medication Formulation DRUG-0261 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0262": MasterFormularyDrugRecord(
        drug_id="DRUG-0262",
        drug_name="Enterprise Medication Formulation DRUG-0262 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0263": MasterFormularyDrugRecord(
        drug_id="DRUG-0263",
        drug_name="Enterprise Medication Formulation DRUG-0263 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0264": MasterFormularyDrugRecord(
        drug_id="DRUG-0264",
        drug_name="Enterprise Medication Formulation DRUG-0264 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0265": MasterFormularyDrugRecord(
        drug_id="DRUG-0265",
        drug_name="Enterprise Medication Formulation DRUG-0265 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0266": MasterFormularyDrugRecord(
        drug_id="DRUG-0266",
        drug_name="Enterprise Medication Formulation DRUG-0266 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0267": MasterFormularyDrugRecord(
        drug_id="DRUG-0267",
        drug_name="Enterprise Medication Formulation DRUG-0267 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0268": MasterFormularyDrugRecord(
        drug_id="DRUG-0268",
        drug_name="Enterprise Medication Formulation DRUG-0268 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0269": MasterFormularyDrugRecord(
        drug_id="DRUG-0269",
        drug_name="Enterprise Medication Formulation DRUG-0269 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0270": MasterFormularyDrugRecord(
        drug_id="DRUG-0270",
        drug_name="Enterprise Medication Formulation DRUG-0270 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0271": MasterFormularyDrugRecord(
        drug_id="DRUG-0271",
        drug_name="Enterprise Medication Formulation DRUG-0271 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0272": MasterFormularyDrugRecord(
        drug_id="DRUG-0272",
        drug_name="Enterprise Medication Formulation DRUG-0272 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0273": MasterFormularyDrugRecord(
        drug_id="DRUG-0273",
        drug_name="Enterprise Medication Formulation DRUG-0273 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0274": MasterFormularyDrugRecord(
        drug_id="DRUG-0274",
        drug_name="Enterprise Medication Formulation DRUG-0274 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0275": MasterFormularyDrugRecord(
        drug_id="DRUG-0275",
        drug_name="Enterprise Medication Formulation DRUG-0275 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0276": MasterFormularyDrugRecord(
        drug_id="DRUG-0276",
        drug_name="Enterprise Medication Formulation DRUG-0276 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0277": MasterFormularyDrugRecord(
        drug_id="DRUG-0277",
        drug_name="Enterprise Medication Formulation DRUG-0277 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0278": MasterFormularyDrugRecord(
        drug_id="DRUG-0278",
        drug_name="Enterprise Medication Formulation DRUG-0278 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0279": MasterFormularyDrugRecord(
        drug_id="DRUG-0279",
        drug_name="Enterprise Medication Formulation DRUG-0279 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0280": MasterFormularyDrugRecord(
        drug_id="DRUG-0280",
        drug_name="Enterprise Medication Formulation DRUG-0280 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0281": MasterFormularyDrugRecord(
        drug_id="DRUG-0281",
        drug_name="Enterprise Medication Formulation DRUG-0281 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0282": MasterFormularyDrugRecord(
        drug_id="DRUG-0282",
        drug_name="Enterprise Medication Formulation DRUG-0282 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0283": MasterFormularyDrugRecord(
        drug_id="DRUG-0283",
        drug_name="Enterprise Medication Formulation DRUG-0283 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0284": MasterFormularyDrugRecord(
        drug_id="DRUG-0284",
        drug_name="Enterprise Medication Formulation DRUG-0284 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0285": MasterFormularyDrugRecord(
        drug_id="DRUG-0285",
        drug_name="Enterprise Medication Formulation DRUG-0285 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0286": MasterFormularyDrugRecord(
        drug_id="DRUG-0286",
        drug_name="Enterprise Medication Formulation DRUG-0286 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0287": MasterFormularyDrugRecord(
        drug_id="DRUG-0287",
        drug_name="Enterprise Medication Formulation DRUG-0287 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0288": MasterFormularyDrugRecord(
        drug_id="DRUG-0288",
        drug_name="Enterprise Medication Formulation DRUG-0288 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0289": MasterFormularyDrugRecord(
        drug_id="DRUG-0289",
        drug_name="Enterprise Medication Formulation DRUG-0289 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0290": MasterFormularyDrugRecord(
        drug_id="DRUG-0290",
        drug_name="Enterprise Medication Formulation DRUG-0290 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0291": MasterFormularyDrugRecord(
        drug_id="DRUG-0291",
        drug_name="Enterprise Medication Formulation DRUG-0291 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0292": MasterFormularyDrugRecord(
        drug_id="DRUG-0292",
        drug_name="Enterprise Medication Formulation DRUG-0292 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0293": MasterFormularyDrugRecord(
        drug_id="DRUG-0293",
        drug_name="Enterprise Medication Formulation DRUG-0293 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0294": MasterFormularyDrugRecord(
        drug_id="DRUG-0294",
        drug_name="Enterprise Medication Formulation DRUG-0294 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0295": MasterFormularyDrugRecord(
        drug_id="DRUG-0295",
        drug_name="Enterprise Medication Formulation DRUG-0295 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0296": MasterFormularyDrugRecord(
        drug_id="DRUG-0296",
        drug_name="Enterprise Medication Formulation DRUG-0296 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0297": MasterFormularyDrugRecord(
        drug_id="DRUG-0297",
        drug_name="Enterprise Medication Formulation DRUG-0297 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0298": MasterFormularyDrugRecord(
        drug_id="DRUG-0298",
        drug_name="Enterprise Medication Formulation DRUG-0298 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0299": MasterFormularyDrugRecord(
        drug_id="DRUG-0299",
        drug_name="Enterprise Medication Formulation DRUG-0299 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0300": MasterFormularyDrugRecord(
        drug_id="DRUG-0300",
        drug_name="Enterprise Medication Formulation DRUG-0300 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0301": MasterFormularyDrugRecord(
        drug_id="DRUG-0301",
        drug_name="Enterprise Medication Formulation DRUG-0301 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0302": MasterFormularyDrugRecord(
        drug_id="DRUG-0302",
        drug_name="Enterprise Medication Formulation DRUG-0302 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0303": MasterFormularyDrugRecord(
        drug_id="DRUG-0303",
        drug_name="Enterprise Medication Formulation DRUG-0303 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0304": MasterFormularyDrugRecord(
        drug_id="DRUG-0304",
        drug_name="Enterprise Medication Formulation DRUG-0304 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0305": MasterFormularyDrugRecord(
        drug_id="DRUG-0305",
        drug_name="Enterprise Medication Formulation DRUG-0305 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0306": MasterFormularyDrugRecord(
        drug_id="DRUG-0306",
        drug_name="Enterprise Medication Formulation DRUG-0306 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0307": MasterFormularyDrugRecord(
        drug_id="DRUG-0307",
        drug_name="Enterprise Medication Formulation DRUG-0307 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0308": MasterFormularyDrugRecord(
        drug_id="DRUG-0308",
        drug_name="Enterprise Medication Formulation DRUG-0308 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0309": MasterFormularyDrugRecord(
        drug_id="DRUG-0309",
        drug_name="Enterprise Medication Formulation DRUG-0309 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0310": MasterFormularyDrugRecord(
        drug_id="DRUG-0310",
        drug_name="Enterprise Medication Formulation DRUG-0310 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0311": MasterFormularyDrugRecord(
        drug_id="DRUG-0311",
        drug_name="Enterprise Medication Formulation DRUG-0311 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0312": MasterFormularyDrugRecord(
        drug_id="DRUG-0312",
        drug_name="Enterprise Medication Formulation DRUG-0312 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0313": MasterFormularyDrugRecord(
        drug_id="DRUG-0313",
        drug_name="Enterprise Medication Formulation DRUG-0313 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0314": MasterFormularyDrugRecord(
        drug_id="DRUG-0314",
        drug_name="Enterprise Medication Formulation DRUG-0314 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0315": MasterFormularyDrugRecord(
        drug_id="DRUG-0315",
        drug_name="Enterprise Medication Formulation DRUG-0315 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0316": MasterFormularyDrugRecord(
        drug_id="DRUG-0316",
        drug_name="Enterprise Medication Formulation DRUG-0316 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0317": MasterFormularyDrugRecord(
        drug_id="DRUG-0317",
        drug_name="Enterprise Medication Formulation DRUG-0317 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0318": MasterFormularyDrugRecord(
        drug_id="DRUG-0318",
        drug_name="Enterprise Medication Formulation DRUG-0318 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0319": MasterFormularyDrugRecord(
        drug_id="DRUG-0319",
        drug_name="Enterprise Medication Formulation DRUG-0319 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0320": MasterFormularyDrugRecord(
        drug_id="DRUG-0320",
        drug_name="Enterprise Medication Formulation DRUG-0320 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0321": MasterFormularyDrugRecord(
        drug_id="DRUG-0321",
        drug_name="Enterprise Medication Formulation DRUG-0321 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0322": MasterFormularyDrugRecord(
        drug_id="DRUG-0322",
        drug_name="Enterprise Medication Formulation DRUG-0322 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0323": MasterFormularyDrugRecord(
        drug_id="DRUG-0323",
        drug_name="Enterprise Medication Formulation DRUG-0323 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0324": MasterFormularyDrugRecord(
        drug_id="DRUG-0324",
        drug_name="Enterprise Medication Formulation DRUG-0324 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0325": MasterFormularyDrugRecord(
        drug_id="DRUG-0325",
        drug_name="Enterprise Medication Formulation DRUG-0325 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0326": MasterFormularyDrugRecord(
        drug_id="DRUG-0326",
        drug_name="Enterprise Medication Formulation DRUG-0326 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0327": MasterFormularyDrugRecord(
        drug_id="DRUG-0327",
        drug_name="Enterprise Medication Formulation DRUG-0327 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0328": MasterFormularyDrugRecord(
        drug_id="DRUG-0328",
        drug_name="Enterprise Medication Formulation DRUG-0328 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0329": MasterFormularyDrugRecord(
        drug_id="DRUG-0329",
        drug_name="Enterprise Medication Formulation DRUG-0329 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0330": MasterFormularyDrugRecord(
        drug_id="DRUG-0330",
        drug_name="Enterprise Medication Formulation DRUG-0330 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0331": MasterFormularyDrugRecord(
        drug_id="DRUG-0331",
        drug_name="Enterprise Medication Formulation DRUG-0331 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0332": MasterFormularyDrugRecord(
        drug_id="DRUG-0332",
        drug_name="Enterprise Medication Formulation DRUG-0332 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0333": MasterFormularyDrugRecord(
        drug_id="DRUG-0333",
        drug_name="Enterprise Medication Formulation DRUG-0333 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0334": MasterFormularyDrugRecord(
        drug_id="DRUG-0334",
        drug_name="Enterprise Medication Formulation DRUG-0334 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0335": MasterFormularyDrugRecord(
        drug_id="DRUG-0335",
        drug_name="Enterprise Medication Formulation DRUG-0335 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0336": MasterFormularyDrugRecord(
        drug_id="DRUG-0336",
        drug_name="Enterprise Medication Formulation DRUG-0336 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0337": MasterFormularyDrugRecord(
        drug_id="DRUG-0337",
        drug_name="Enterprise Medication Formulation DRUG-0337 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0338": MasterFormularyDrugRecord(
        drug_id="DRUG-0338",
        drug_name="Enterprise Medication Formulation DRUG-0338 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0339": MasterFormularyDrugRecord(
        drug_id="DRUG-0339",
        drug_name="Enterprise Medication Formulation DRUG-0339 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0340": MasterFormularyDrugRecord(
        drug_id="DRUG-0340",
        drug_name="Enterprise Medication Formulation DRUG-0340 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0341": MasterFormularyDrugRecord(
        drug_id="DRUG-0341",
        drug_name="Enterprise Medication Formulation DRUG-0341 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0342": MasterFormularyDrugRecord(
        drug_id="DRUG-0342",
        drug_name="Enterprise Medication Formulation DRUG-0342 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0343": MasterFormularyDrugRecord(
        drug_id="DRUG-0343",
        drug_name="Enterprise Medication Formulation DRUG-0343 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0344": MasterFormularyDrugRecord(
        drug_id="DRUG-0344",
        drug_name="Enterprise Medication Formulation DRUG-0344 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0345": MasterFormularyDrugRecord(
        drug_id="DRUG-0345",
        drug_name="Enterprise Medication Formulation DRUG-0345 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0346": MasterFormularyDrugRecord(
        drug_id="DRUG-0346",
        drug_name="Enterprise Medication Formulation DRUG-0346 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0347": MasterFormularyDrugRecord(
        drug_id="DRUG-0347",
        drug_name="Enterprise Medication Formulation DRUG-0347 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0348": MasterFormularyDrugRecord(
        drug_id="DRUG-0348",
        drug_name="Enterprise Medication Formulation DRUG-0348 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0349": MasterFormularyDrugRecord(
        drug_id="DRUG-0349",
        drug_name="Enterprise Medication Formulation DRUG-0349 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0350": MasterFormularyDrugRecord(
        drug_id="DRUG-0350",
        drug_name="Enterprise Medication Formulation DRUG-0350 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0351": MasterFormularyDrugRecord(
        drug_id="DRUG-0351",
        drug_name="Enterprise Medication Formulation DRUG-0351 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0352": MasterFormularyDrugRecord(
        drug_id="DRUG-0352",
        drug_name="Enterprise Medication Formulation DRUG-0352 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0353": MasterFormularyDrugRecord(
        drug_id="DRUG-0353",
        drug_name="Enterprise Medication Formulation DRUG-0353 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0354": MasterFormularyDrugRecord(
        drug_id="DRUG-0354",
        drug_name="Enterprise Medication Formulation DRUG-0354 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0355": MasterFormularyDrugRecord(
        drug_id="DRUG-0355",
        drug_name="Enterprise Medication Formulation DRUG-0355 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0356": MasterFormularyDrugRecord(
        drug_id="DRUG-0356",
        drug_name="Enterprise Medication Formulation DRUG-0356 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0357": MasterFormularyDrugRecord(
        drug_id="DRUG-0357",
        drug_name="Enterprise Medication Formulation DRUG-0357 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0358": MasterFormularyDrugRecord(
        drug_id="DRUG-0358",
        drug_name="Enterprise Medication Formulation DRUG-0358 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0359": MasterFormularyDrugRecord(
        drug_id="DRUG-0359",
        drug_name="Enterprise Medication Formulation DRUG-0359 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0360": MasterFormularyDrugRecord(
        drug_id="DRUG-0360",
        drug_name="Enterprise Medication Formulation DRUG-0360 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0361": MasterFormularyDrugRecord(
        drug_id="DRUG-0361",
        drug_name="Enterprise Medication Formulation DRUG-0361 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0362": MasterFormularyDrugRecord(
        drug_id="DRUG-0362",
        drug_name="Enterprise Medication Formulation DRUG-0362 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0363": MasterFormularyDrugRecord(
        drug_id="DRUG-0363",
        drug_name="Enterprise Medication Formulation DRUG-0363 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0364": MasterFormularyDrugRecord(
        drug_id="DRUG-0364",
        drug_name="Enterprise Medication Formulation DRUG-0364 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0365": MasterFormularyDrugRecord(
        drug_id="DRUG-0365",
        drug_name="Enterprise Medication Formulation DRUG-0365 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0366": MasterFormularyDrugRecord(
        drug_id="DRUG-0366",
        drug_name="Enterprise Medication Formulation DRUG-0366 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0367": MasterFormularyDrugRecord(
        drug_id="DRUG-0367",
        drug_name="Enterprise Medication Formulation DRUG-0367 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0368": MasterFormularyDrugRecord(
        drug_id="DRUG-0368",
        drug_name="Enterprise Medication Formulation DRUG-0368 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0369": MasterFormularyDrugRecord(
        drug_id="DRUG-0369",
        drug_name="Enterprise Medication Formulation DRUG-0369 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0370": MasterFormularyDrugRecord(
        drug_id="DRUG-0370",
        drug_name="Enterprise Medication Formulation DRUG-0370 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0371": MasterFormularyDrugRecord(
        drug_id="DRUG-0371",
        drug_name="Enterprise Medication Formulation DRUG-0371 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0372": MasterFormularyDrugRecord(
        drug_id="DRUG-0372",
        drug_name="Enterprise Medication Formulation DRUG-0372 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0373": MasterFormularyDrugRecord(
        drug_id="DRUG-0373",
        drug_name="Enterprise Medication Formulation DRUG-0373 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0374": MasterFormularyDrugRecord(
        drug_id="DRUG-0374",
        drug_name="Enterprise Medication Formulation DRUG-0374 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0375": MasterFormularyDrugRecord(
        drug_id="DRUG-0375",
        drug_name="Enterprise Medication Formulation DRUG-0375 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0376": MasterFormularyDrugRecord(
        drug_id="DRUG-0376",
        drug_name="Enterprise Medication Formulation DRUG-0376 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0377": MasterFormularyDrugRecord(
        drug_id="DRUG-0377",
        drug_name="Enterprise Medication Formulation DRUG-0377 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0378": MasterFormularyDrugRecord(
        drug_id="DRUG-0378",
        drug_name="Enterprise Medication Formulation DRUG-0378 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0379": MasterFormularyDrugRecord(
        drug_id="DRUG-0379",
        drug_name="Enterprise Medication Formulation DRUG-0379 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0380": MasterFormularyDrugRecord(
        drug_id="DRUG-0380",
        drug_name="Enterprise Medication Formulation DRUG-0380 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0381": MasterFormularyDrugRecord(
        drug_id="DRUG-0381",
        drug_name="Enterprise Medication Formulation DRUG-0381 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0382": MasterFormularyDrugRecord(
        drug_id="DRUG-0382",
        drug_name="Enterprise Medication Formulation DRUG-0382 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0383": MasterFormularyDrugRecord(
        drug_id="DRUG-0383",
        drug_name="Enterprise Medication Formulation DRUG-0383 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0384": MasterFormularyDrugRecord(
        drug_id="DRUG-0384",
        drug_name="Enterprise Medication Formulation DRUG-0384 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0385": MasterFormularyDrugRecord(
        drug_id="DRUG-0385",
        drug_name="Enterprise Medication Formulation DRUG-0385 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0386": MasterFormularyDrugRecord(
        drug_id="DRUG-0386",
        drug_name="Enterprise Medication Formulation DRUG-0386 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0387": MasterFormularyDrugRecord(
        drug_id="DRUG-0387",
        drug_name="Enterprise Medication Formulation DRUG-0387 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0388": MasterFormularyDrugRecord(
        drug_id="DRUG-0388",
        drug_name="Enterprise Medication Formulation DRUG-0388 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0389": MasterFormularyDrugRecord(
        drug_id="DRUG-0389",
        drug_name="Enterprise Medication Formulation DRUG-0389 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0390": MasterFormularyDrugRecord(
        drug_id="DRUG-0390",
        drug_name="Enterprise Medication Formulation DRUG-0390 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0391": MasterFormularyDrugRecord(
        drug_id="DRUG-0391",
        drug_name="Enterprise Medication Formulation DRUG-0391 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0392": MasterFormularyDrugRecord(
        drug_id="DRUG-0392",
        drug_name="Enterprise Medication Formulation DRUG-0392 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0393": MasterFormularyDrugRecord(
        drug_id="DRUG-0393",
        drug_name="Enterprise Medication Formulation DRUG-0393 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0394": MasterFormularyDrugRecord(
        drug_id="DRUG-0394",
        drug_name="Enterprise Medication Formulation DRUG-0394 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0395": MasterFormularyDrugRecord(
        drug_id="DRUG-0395",
        drug_name="Enterprise Medication Formulation DRUG-0395 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0396": MasterFormularyDrugRecord(
        drug_id="DRUG-0396",
        drug_name="Enterprise Medication Formulation DRUG-0396 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0397": MasterFormularyDrugRecord(
        drug_id="DRUG-0397",
        drug_name="Enterprise Medication Formulation DRUG-0397 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0398": MasterFormularyDrugRecord(
        drug_id="DRUG-0398",
        drug_name="Enterprise Medication Formulation DRUG-0398 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0399": MasterFormularyDrugRecord(
        drug_id="DRUG-0399",
        drug_name="Enterprise Medication Formulation DRUG-0399 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0400": MasterFormularyDrugRecord(
        drug_id="DRUG-0400",
        drug_name="Enterprise Medication Formulation DRUG-0400 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0401": MasterFormularyDrugRecord(
        drug_id="DRUG-0401",
        drug_name="Enterprise Medication Formulation DRUG-0401 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0402": MasterFormularyDrugRecord(
        drug_id="DRUG-0402",
        drug_name="Enterprise Medication Formulation DRUG-0402 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0403": MasterFormularyDrugRecord(
        drug_id="DRUG-0403",
        drug_name="Enterprise Medication Formulation DRUG-0403 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0404": MasterFormularyDrugRecord(
        drug_id="DRUG-0404",
        drug_name="Enterprise Medication Formulation DRUG-0404 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0405": MasterFormularyDrugRecord(
        drug_id="DRUG-0405",
        drug_name="Enterprise Medication Formulation DRUG-0405 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0406": MasterFormularyDrugRecord(
        drug_id="DRUG-0406",
        drug_name="Enterprise Medication Formulation DRUG-0406 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0407": MasterFormularyDrugRecord(
        drug_id="DRUG-0407",
        drug_name="Enterprise Medication Formulation DRUG-0407 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0408": MasterFormularyDrugRecord(
        drug_id="DRUG-0408",
        drug_name="Enterprise Medication Formulation DRUG-0408 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0409": MasterFormularyDrugRecord(
        drug_id="DRUG-0409",
        drug_name="Enterprise Medication Formulation DRUG-0409 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0410": MasterFormularyDrugRecord(
        drug_id="DRUG-0410",
        drug_name="Enterprise Medication Formulation DRUG-0410 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0411": MasterFormularyDrugRecord(
        drug_id="DRUG-0411",
        drug_name="Enterprise Medication Formulation DRUG-0411 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0412": MasterFormularyDrugRecord(
        drug_id="DRUG-0412",
        drug_name="Enterprise Medication Formulation DRUG-0412 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0413": MasterFormularyDrugRecord(
        drug_id="DRUG-0413",
        drug_name="Enterprise Medication Formulation DRUG-0413 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0414": MasterFormularyDrugRecord(
        drug_id="DRUG-0414",
        drug_name="Enterprise Medication Formulation DRUG-0414 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0415": MasterFormularyDrugRecord(
        drug_id="DRUG-0415",
        drug_name="Enterprise Medication Formulation DRUG-0415 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0416": MasterFormularyDrugRecord(
        drug_id="DRUG-0416",
        drug_name="Enterprise Medication Formulation DRUG-0416 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0417": MasterFormularyDrugRecord(
        drug_id="DRUG-0417",
        drug_name="Enterprise Medication Formulation DRUG-0417 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0418": MasterFormularyDrugRecord(
        drug_id="DRUG-0418",
        drug_name="Enterprise Medication Formulation DRUG-0418 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0419": MasterFormularyDrugRecord(
        drug_id="DRUG-0419",
        drug_name="Enterprise Medication Formulation DRUG-0419 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0420": MasterFormularyDrugRecord(
        drug_id="DRUG-0420",
        drug_name="Enterprise Medication Formulation DRUG-0420 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0421": MasterFormularyDrugRecord(
        drug_id="DRUG-0421",
        drug_name="Enterprise Medication Formulation DRUG-0421 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0422": MasterFormularyDrugRecord(
        drug_id="DRUG-0422",
        drug_name="Enterprise Medication Formulation DRUG-0422 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0423": MasterFormularyDrugRecord(
        drug_id="DRUG-0423",
        drug_name="Enterprise Medication Formulation DRUG-0423 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0424": MasterFormularyDrugRecord(
        drug_id="DRUG-0424",
        drug_name="Enterprise Medication Formulation DRUG-0424 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0425": MasterFormularyDrugRecord(
        drug_id="DRUG-0425",
        drug_name="Enterprise Medication Formulation DRUG-0425 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0426": MasterFormularyDrugRecord(
        drug_id="DRUG-0426",
        drug_name="Enterprise Medication Formulation DRUG-0426 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0427": MasterFormularyDrugRecord(
        drug_id="DRUG-0427",
        drug_name="Enterprise Medication Formulation DRUG-0427 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0428": MasterFormularyDrugRecord(
        drug_id="DRUG-0428",
        drug_name="Enterprise Medication Formulation DRUG-0428 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0429": MasterFormularyDrugRecord(
        drug_id="DRUG-0429",
        drug_name="Enterprise Medication Formulation DRUG-0429 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0430": MasterFormularyDrugRecord(
        drug_id="DRUG-0430",
        drug_name="Enterprise Medication Formulation DRUG-0430 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0431": MasterFormularyDrugRecord(
        drug_id="DRUG-0431",
        drug_name="Enterprise Medication Formulation DRUG-0431 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0432": MasterFormularyDrugRecord(
        drug_id="DRUG-0432",
        drug_name="Enterprise Medication Formulation DRUG-0432 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0433": MasterFormularyDrugRecord(
        drug_id="DRUG-0433",
        drug_name="Enterprise Medication Formulation DRUG-0433 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0434": MasterFormularyDrugRecord(
        drug_id="DRUG-0434",
        drug_name="Enterprise Medication Formulation DRUG-0434 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0435": MasterFormularyDrugRecord(
        drug_id="DRUG-0435",
        drug_name="Enterprise Medication Formulation DRUG-0435 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0436": MasterFormularyDrugRecord(
        drug_id="DRUG-0436",
        drug_name="Enterprise Medication Formulation DRUG-0436 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0437": MasterFormularyDrugRecord(
        drug_id="DRUG-0437",
        drug_name="Enterprise Medication Formulation DRUG-0437 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0438": MasterFormularyDrugRecord(
        drug_id="DRUG-0438",
        drug_name="Enterprise Medication Formulation DRUG-0438 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0439": MasterFormularyDrugRecord(
        drug_id="DRUG-0439",
        drug_name="Enterprise Medication Formulation DRUG-0439 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0440": MasterFormularyDrugRecord(
        drug_id="DRUG-0440",
        drug_name="Enterprise Medication Formulation DRUG-0440 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0441": MasterFormularyDrugRecord(
        drug_id="DRUG-0441",
        drug_name="Enterprise Medication Formulation DRUG-0441 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0442": MasterFormularyDrugRecord(
        drug_id="DRUG-0442",
        drug_name="Enterprise Medication Formulation DRUG-0442 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0443": MasterFormularyDrugRecord(
        drug_id="DRUG-0443",
        drug_name="Enterprise Medication Formulation DRUG-0443 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0444": MasterFormularyDrugRecord(
        drug_id="DRUG-0444",
        drug_name="Enterprise Medication Formulation DRUG-0444 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0445": MasterFormularyDrugRecord(
        drug_id="DRUG-0445",
        drug_name="Enterprise Medication Formulation DRUG-0445 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0446": MasterFormularyDrugRecord(
        drug_id="DRUG-0446",
        drug_name="Enterprise Medication Formulation DRUG-0446 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0447": MasterFormularyDrugRecord(
        drug_id="DRUG-0447",
        drug_name="Enterprise Medication Formulation DRUG-0447 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0448": MasterFormularyDrugRecord(
        drug_id="DRUG-0448",
        drug_name="Enterprise Medication Formulation DRUG-0448 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0449": MasterFormularyDrugRecord(
        drug_id="DRUG-0449",
        drug_name="Enterprise Medication Formulation DRUG-0449 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0450": MasterFormularyDrugRecord(
        drug_id="DRUG-0450",
        drug_name="Enterprise Medication Formulation DRUG-0450 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0451": MasterFormularyDrugRecord(
        drug_id="DRUG-0451",
        drug_name="Enterprise Medication Formulation DRUG-0451 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0452": MasterFormularyDrugRecord(
        drug_id="DRUG-0452",
        drug_name="Enterprise Medication Formulation DRUG-0452 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0453": MasterFormularyDrugRecord(
        drug_id="DRUG-0453",
        drug_name="Enterprise Medication Formulation DRUG-0453 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0454": MasterFormularyDrugRecord(
        drug_id="DRUG-0454",
        drug_name="Enterprise Medication Formulation DRUG-0454 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0455": MasterFormularyDrugRecord(
        drug_id="DRUG-0455",
        drug_name="Enterprise Medication Formulation DRUG-0455 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0456": MasterFormularyDrugRecord(
        drug_id="DRUG-0456",
        drug_name="Enterprise Medication Formulation DRUG-0456 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0457": MasterFormularyDrugRecord(
        drug_id="DRUG-0457",
        drug_name="Enterprise Medication Formulation DRUG-0457 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0458": MasterFormularyDrugRecord(
        drug_id="DRUG-0458",
        drug_name="Enterprise Medication Formulation DRUG-0458 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0459": MasterFormularyDrugRecord(
        drug_id="DRUG-0459",
        drug_name="Enterprise Medication Formulation DRUG-0459 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0460": MasterFormularyDrugRecord(
        drug_id="DRUG-0460",
        drug_name="Enterprise Medication Formulation DRUG-0460 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0461": MasterFormularyDrugRecord(
        drug_id="DRUG-0461",
        drug_name="Enterprise Medication Formulation DRUG-0461 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0462": MasterFormularyDrugRecord(
        drug_id="DRUG-0462",
        drug_name="Enterprise Medication Formulation DRUG-0462 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0463": MasterFormularyDrugRecord(
        drug_id="DRUG-0463",
        drug_name="Enterprise Medication Formulation DRUG-0463 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0464": MasterFormularyDrugRecord(
        drug_id="DRUG-0464",
        drug_name="Enterprise Medication Formulation DRUG-0464 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0465": MasterFormularyDrugRecord(
        drug_id="DRUG-0465",
        drug_name="Enterprise Medication Formulation DRUG-0465 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0466": MasterFormularyDrugRecord(
        drug_id="DRUG-0466",
        drug_name="Enterprise Medication Formulation DRUG-0466 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0467": MasterFormularyDrugRecord(
        drug_id="DRUG-0467",
        drug_name="Enterprise Medication Formulation DRUG-0467 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0468": MasterFormularyDrugRecord(
        drug_id="DRUG-0468",
        drug_name="Enterprise Medication Formulation DRUG-0468 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0469": MasterFormularyDrugRecord(
        drug_id="DRUG-0469",
        drug_name="Enterprise Medication Formulation DRUG-0469 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0470": MasterFormularyDrugRecord(
        drug_id="DRUG-0470",
        drug_name="Enterprise Medication Formulation DRUG-0470 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0471": MasterFormularyDrugRecord(
        drug_id="DRUG-0471",
        drug_name="Enterprise Medication Formulation DRUG-0471 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0472": MasterFormularyDrugRecord(
        drug_id="DRUG-0472",
        drug_name="Enterprise Medication Formulation DRUG-0472 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0473": MasterFormularyDrugRecord(
        drug_id="DRUG-0473",
        drug_name="Enterprise Medication Formulation DRUG-0473 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0474": MasterFormularyDrugRecord(
        drug_id="DRUG-0474",
        drug_name="Enterprise Medication Formulation DRUG-0474 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0475": MasterFormularyDrugRecord(
        drug_id="DRUG-0475",
        drug_name="Enterprise Medication Formulation DRUG-0475 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0476": MasterFormularyDrugRecord(
        drug_id="DRUG-0476",
        drug_name="Enterprise Medication Formulation DRUG-0476 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0477": MasterFormularyDrugRecord(
        drug_id="DRUG-0477",
        drug_name="Enterprise Medication Formulation DRUG-0477 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0478": MasterFormularyDrugRecord(
        drug_id="DRUG-0478",
        drug_name="Enterprise Medication Formulation DRUG-0478 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0479": MasterFormularyDrugRecord(
        drug_id="DRUG-0479",
        drug_name="Enterprise Medication Formulation DRUG-0479 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0480": MasterFormularyDrugRecord(
        drug_id="DRUG-0480",
        drug_name="Enterprise Medication Formulation DRUG-0480 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0481": MasterFormularyDrugRecord(
        drug_id="DRUG-0481",
        drug_name="Enterprise Medication Formulation DRUG-0481 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0482": MasterFormularyDrugRecord(
        drug_id="DRUG-0482",
        drug_name="Enterprise Medication Formulation DRUG-0482 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0483": MasterFormularyDrugRecord(
        drug_id="DRUG-0483",
        drug_name="Enterprise Medication Formulation DRUG-0483 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0484": MasterFormularyDrugRecord(
        drug_id="DRUG-0484",
        drug_name="Enterprise Medication Formulation DRUG-0484 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0485": MasterFormularyDrugRecord(
        drug_id="DRUG-0485",
        drug_name="Enterprise Medication Formulation DRUG-0485 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0486": MasterFormularyDrugRecord(
        drug_id="DRUG-0486",
        drug_name="Enterprise Medication Formulation DRUG-0486 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0487": MasterFormularyDrugRecord(
        drug_id="DRUG-0487",
        drug_name="Enterprise Medication Formulation DRUG-0487 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0488": MasterFormularyDrugRecord(
        drug_id="DRUG-0488",
        drug_name="Enterprise Medication Formulation DRUG-0488 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0489": MasterFormularyDrugRecord(
        drug_id="DRUG-0489",
        drug_name="Enterprise Medication Formulation DRUG-0489 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0490": MasterFormularyDrugRecord(
        drug_id="DRUG-0490",
        drug_name="Enterprise Medication Formulation DRUG-0490 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0491": MasterFormularyDrugRecord(
        drug_id="DRUG-0491",
        drug_name="Enterprise Medication Formulation DRUG-0491 (Cardiovascular Agents)",
        therapeutic_category="Cardiovascular Agents",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0492": MasterFormularyDrugRecord(
        drug_id="DRUG-0492",
        drug_name="Enterprise Medication Formulation DRUG-0492 (Anti-Diabetic Medications)",
        therapeutic_category="Anti-Diabetic Medications",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0493": MasterFormularyDrugRecord(
        drug_id="DRUG-0493",
        drug_name="Enterprise Medication Formulation DRUG-0493 (Central Nervous System & Psychotropics)",
        therapeutic_category="Central Nervous System & Psychotropics",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0494": MasterFormularyDrugRecord(
        drug_id="DRUG-0494",
        drug_name="Enterprise Medication Formulation DRUG-0494 (Anti-Infective & Antibiotic Agents)",
        therapeutic_category="Anti-Infective & Antibiotic Agents",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0495": MasterFormularyDrugRecord(
        drug_id="DRUG-0495",
        drug_name="Enterprise Medication Formulation DRUG-0495 (Immunological & Biological Modifiers)",
        therapeutic_category="Immunological & Biological Modifiers",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0496": MasterFormularyDrugRecord(
        drug_id="DRUG-0496",
        drug_name="Enterprise Medication Formulation DRUG-0496 (Respiratory & Pulmonary Agents)",
        therapeutic_category="Respiratory & Pulmonary Agents",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
    "DRUG-0497": MasterFormularyDrugRecord(
        drug_id="DRUG-0497",
        drug_name="Enterprise Medication Formulation DRUG-0497 (Gastrointestinal & Metabolic Agents)",
        therapeutic_category="Gastrointestinal & Metabolic Agents",
        tier=1,
        copay_usd=10.0,
        requires_pa=False
    ),
    "DRUG-0498": MasterFormularyDrugRecord(
        drug_id="DRUG-0498",
        drug_name="Enterprise Medication Formulation DRUG-0498 (Oncology & Hematology Therapies)",
        therapeutic_category="Oncology & Hematology Therapies",
        tier=2,
        copay_usd=35.0,
        requires_pa=False
    ),
    "DRUG-0499": MasterFormularyDrugRecord(
        drug_id="DRUG-0499",
        drug_name="Enterprise Medication Formulation DRUG-0499 (Dermatological Formulations)",
        therapeutic_category="Dermatological Formulations",
        tier=3,
        copay_usd=75.0,
        requires_pa=True
    ),
    "DRUG-0500": MasterFormularyDrugRecord(
        drug_id="DRUG-0500",
        drug_name="Enterprise Medication Formulation DRUG-0500 (Endocrine & Hormone Regulators)",
        therapeutic_category="Endocrine & Hormone Regulators",
        tier=4,
        copay_usd=150.0,
        requires_pa=True
    ),
}

class MasterDrugFormularyService:
    @classmethod
    def get_drug(cls, did: str) -> MasterFormularyDrugRecord:
        return MASTER_500_DRUG_FORMULARY.get(did)

    @classmethod
    def get_all(cls) -> List[MasterFormularyDrugRecord]:
        return list(MASTER_500_DRUG_FORMULARY.values())
