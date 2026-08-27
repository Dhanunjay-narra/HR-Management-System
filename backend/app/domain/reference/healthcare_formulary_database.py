"""
Enterprise Healthcare Prescription Formulary & Copay Tier Database
Prescribes drug tiers (Tier 1 Generic to Tier 4 Specialty Biologic), 30-day supply copays, and clinical prior authorization requirements.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class PrescriptionFormularyItem:
    drug_name: str
    therapeutic_class: str
    medical_domain: str
    copay_tier: int  # 1=Generic, 2=Preferred Brand, 3=Non-Preferred, 4=Specialty
    patient_copay_usd: float
    requires_prior_authorization: bool


MASTER_HEALTHCARE_FORMULARY: Dict[str, PrescriptionFormularyItem] = {
    "Lisinopril": PrescriptionFormularyItem(
        drug_name="Lisinopril",
        therapeutic_class="ACE Inhibitor",
        medical_domain="Cardiovascular",
        copay_tier=1,
        patient_copay_usd=10.0,
        requires_prior_authorization=False
    ),
    "Atorvastatin": PrescriptionFormularyItem(
        drug_name="Atorvastatin",
        therapeutic_class="HMG-CoA Reductase Inhibitor",
        medical_domain="Cardiovascular",
        copay_tier=1,
        patient_copay_usd=12.0,
        requires_prior_authorization=False
    ),
    "Metoprolol Succinate": PrescriptionFormularyItem(
        drug_name="Metoprolol Succinate",
        therapeutic_class="Beta Blocker",
        medical_domain="Cardiovascular",
        copay_tier=1,
        patient_copay_usd=15.0,
        requires_prior_authorization=False
    ),
    "Amlodipine Besylate": PrescriptionFormularyItem(
        drug_name="Amlodipine Besylate",
        therapeutic_class="Calcium Channel Blocker",
        medical_domain="Cardiovascular",
        copay_tier=1,
        patient_copay_usd=10.0,
        requires_prior_authorization=False
    ),
    "Losartan Potassium": PrescriptionFormularyItem(
        drug_name="Losartan Potassium",
        therapeutic_class="Angiotensin II Receptor Antagonist",
        medical_domain="Cardiovascular",
        copay_tier=1,
        patient_copay_usd=14.0,
        requires_prior_authorization=False
    ),
    "Eliquis (Apixaban)": PrescriptionFormularyItem(
        drug_name="Eliquis (Apixaban)",
        therapeutic_class="Factor Xa Inhibitor (Anticoagulant)",
        medical_domain="Cardiovascular",
        copay_tier=2,
        patient_copay_usd=45.0,
        requires_prior_authorization=True
    ),
    "Entresto": PrescriptionFormularyItem(
        drug_name="Entresto",
        therapeutic_class="Sacubitril / Valsartan",
        medical_domain="Cardiovascular",
        copay_tier=2,
        patient_copay_usd=50.0,
        requires_prior_authorization=True
    ),
    "Repatha (Evolocumab)": PrescriptionFormularyItem(
        drug_name="Repatha (Evolocumab)",
        therapeutic_class="PCSK9 Inhibitor",
        medical_domain="Cardiovascular",
        copay_tier=4,
        patient_copay_usd=150.0,
        requires_prior_authorization=True
    ),
    "Metformin HCl": PrescriptionFormularyItem(
        drug_name="Metformin HCl",
        therapeutic_class="Biguanide",
        medical_domain="Endocrine & Diabetes",
        copay_tier=1,
        patient_copay_usd=10.0,
        requires_prior_authorization=False
    ),
    "Glipizide ER": PrescriptionFormularyItem(
        drug_name="Glipizide ER",
        therapeutic_class="Sulfonylurea",
        medical_domain="Endocrine & Diabetes",
        copay_tier=1,
        patient_copay_usd=10.0,
        requires_prior_authorization=False
    ),
    "Jardiance (Empagliflozin)": PrescriptionFormularyItem(
        drug_name="Jardiance (Empagliflozin)",
        therapeutic_class="SGLT2 Inhibitor",
        medical_domain="Endocrine & Diabetes",
        copay_tier=2,
        patient_copay_usd=40.0,
        requires_prior_authorization=False
    ),
    "Ozempic (Semaglutide)": PrescriptionFormularyItem(
        drug_name="Ozempic (Semaglutide)",
        therapeutic_class="GLP-1 Receptor Agonist",
        medical_domain="Endocrine & Diabetes",
        copay_tier=2,
        patient_copay_usd=50.0,
        requires_prior_authorization=True
    ),
    "Humalog (Insulin Lispro)": PrescriptionFormularyItem(
        drug_name="Humalog (Insulin Lispro)",
        therapeutic_class="Rapid-Acting Insulin",
        medical_domain="Endocrine & Diabetes",
        copay_tier=2,
        patient_copay_usd=35.0,
        requires_prior_authorization=False
    ),
    "Lantus (Insulin Glargine)": PrescriptionFormularyItem(
        drug_name="Lantus (Insulin Glargine)",
        therapeutic_class="Long-Acting Insulin",
        medical_domain="Endocrine & Diabetes",
        copay_tier=2,
        patient_copay_usd=35.0,
        requires_prior_authorization=False
    ),
    "Mounjaro (Tirzepatide)": PrescriptionFormularyItem(
        drug_name="Mounjaro (Tirzepatide)",
        therapeutic_class="GIP/GLP-1 Receptor Agonist",
        medical_domain="Endocrine & Diabetes",
        copay_tier=2,
        patient_copay_usd=50.0,
        requires_prior_authorization=True
    ),
    "Methotrexate": PrescriptionFormularyItem(
        drug_name="Methotrexate",
        therapeutic_class="Disease-Modifying Antirheumatic Drug",
        medical_domain="Immunology & Rheumatology",
        copay_tier=1,
        patient_copay_usd=15.0,
        requires_prior_authorization=False
    ),
    "Hydroxychloroquine": PrescriptionFormularyItem(
        drug_name="Hydroxychloroquine",
        therapeutic_class="Antimalarial / Immunomodulator",
        medical_domain="Immunology & Rheumatology",
        copay_tier=1,
        patient_copay_usd=20.0,
        requires_prior_authorization=False
    ),
    "Humira (Adalimumab)": PrescriptionFormularyItem(
        drug_name="Humira (Adalimumab)",
        therapeutic_class="TNF-Alpha Inhibitor Biologic",
        medical_domain="Immunology & Rheumatology",
        copay_tier=4,
        patient_copay_usd=150.0,
        requires_prior_authorization=True
    ),
    "Enbrel (Etanercept)": PrescriptionFormularyItem(
        drug_name="Enbrel (Etanercept)",
        therapeutic_class="TNF-Alpha Inhibitor Biologic",
        medical_domain="Immunology & Rheumatology",
        copay_tier=4,
        patient_copay_usd=150.0,
        requires_prior_authorization=True
    ),
    "Stelara (Ustekinumab)": PrescriptionFormularyItem(
        drug_name="Stelara (Ustekinumab)",
        therapeutic_class="IL-12/23 Inhibitor Biologic",
        medical_domain="Immunology & Rheumatology",
        copay_tier=4,
        patient_copay_usd=200.0,
        requires_prior_authorization=True
    ),
    "Skyrizi (Risankizumab)": PrescriptionFormularyItem(
        drug_name="Skyrizi (Risankizumab)",
        therapeutic_class="IL-23 Inhibitor Biologic",
        medical_domain="Immunology & Rheumatology",
        copay_tier=4,
        patient_copay_usd=200.0,
        requires_prior_authorization=True
    ),
    "Dupixent (Dupilumab)": PrescriptionFormularyItem(
        drug_name="Dupixent (Dupilumab)",
        therapeutic_class="IL-4/13 Inhibitor Biologic",
        medical_domain="Immunology & Rheumatology",
        copay_tier=4,
        patient_copay_usd=175.0,
        requires_prior_authorization=True
    ),
    "Sertraline HCl": PrescriptionFormularyItem(
        drug_name="Sertraline HCl",
        therapeutic_class="SSRI Antidepressant",
        medical_domain="Neurology & Mental Health",
        copay_tier=1,
        patient_copay_usd=10.0,
        requires_prior_authorization=False
    ),
    "Escitalopram Oxalate": PrescriptionFormularyItem(
        drug_name="Escitalopram Oxalate",
        therapeutic_class="SSRI Antidepressant",
        medical_domain="Neurology & Mental Health",
        copay_tier=1,
        patient_copay_usd=10.0,
        requires_prior_authorization=False
    ),
    "Duloxetine HCl": PrescriptionFormularyItem(
        drug_name="Duloxetine HCl",
        therapeutic_class="SNRI Antidepressant",
        medical_domain="Neurology & Mental Health",
        copay_tier=1,
        patient_copay_usd=15.0,
        requires_prior_authorization=False
    ),
    "Bupropion XL": PrescriptionFormularyItem(
        drug_name="Bupropion XL",
        therapeutic_class="NDRI Antidepressant",
        medical_domain="Neurology & Mental Health",
        copay_tier=1,
        patient_copay_usd=15.0,
        requires_prior_authorization=False
    ),
    "Lamotrigine": PrescriptionFormularyItem(
        drug_name="Lamotrigine",
        therapeutic_class="Anticonvulsant / Mood Stabilizer",
        medical_domain="Neurology & Mental Health",
        copay_tier=1,
        patient_copay_usd=12.0,
        requires_prior_authorization=False
    ),
    "Nurtec ODT (Rimegepant)": PrescriptionFormularyItem(
        drug_name="Nurtec ODT (Rimegepant)",
        therapeutic_class="CGRP Receptor Antagonist (Migraine)",
        medical_domain="Neurology & Mental Health",
        copay_tier=2,
        patient_copay_usd=45.0,
        requires_prior_authorization=True
    ),
    "Vraylar (Cariprazine)": PrescriptionFormularyItem(
        drug_name="Vraylar (Cariprazine)",
        therapeutic_class="Atypical Antipsychotic",
        medical_domain="Neurology & Mental Health",
        copay_tier=3,
        patient_copay_usd=90.0,
        requires_prior_authorization=True
    ),
    "Albuterol Sulfate HFA": PrescriptionFormularyItem(
        drug_name="Albuterol Sulfate HFA",
        therapeutic_class="Short-Acting Beta Agonist (Rescue)",
        medical_domain="Respiratory & Pulmonology",
        copay_tier=1,
        patient_copay_usd=15.0,
        requires_prior_authorization=False
    ),
    "Fluticasone Propionate": PrescriptionFormularyItem(
        drug_name="Fluticasone Propionate",
        therapeutic_class="Inhaled Corticosteroid",
        medical_domain="Respiratory & Pulmonology",
        copay_tier=1,
        patient_copay_usd=20.0,
        requires_prior_authorization=False
    ),
    "Symbicort (Budesonide/Formoterol)": PrescriptionFormularyItem(
        drug_name="Symbicort (Budesonide/Formoterol)",
        therapeutic_class="ICS / LABA Combination",
        medical_domain="Respiratory & Pulmonology",
        copay_tier=2,
        patient_copay_usd=40.0,
        requires_prior_authorization=False
    ),
    "Trelegy Ellipta": PrescriptionFormularyItem(
        drug_name="Trelegy Ellipta",
        therapeutic_class="ICS / LAMA / LABA Triple Therapy",
        medical_domain="Respiratory & Pulmonology",
        copay_tier=2,
        patient_copay_usd=50.0,
        requires_prior_authorization=True
    ),
    "Fasenra (Benralizumab)": PrescriptionFormularyItem(
        drug_name="Fasenra (Benralizumab)",
        therapeutic_class="Interleukin-5 Receptor Antagonist",
        medical_domain="Respiratory & Pulmonology",
        copay_tier=4,
        patient_copay_usd=200.0,
        requires_prior_authorization=True
    ),
}

class HealthcareFormularyService:
    @classmethod
    def get_drug(cls, name: str) -> PrescriptionFormularyItem:
        return MASTER_HEALTHCARE_FORMULARY.get(name)

    @classmethod
    def get_all_drugs(cls) -> List[PrescriptionFormularyItem]:
        return list(MASTER_HEALTHCARE_FORMULARY.values())
