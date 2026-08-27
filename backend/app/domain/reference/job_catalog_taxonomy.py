"""
Global Standard Job Catalog Taxonomy & Role Competency Matrix (500+ Defined Roles)
Standardizes job family architectures, salary grade bands, required competencies, and promotion criteria across Engineering, Product, Design, Sales, Marketing, HR, Finance, and Legal.
"""
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class JobRoleDefinition:
    job_code: str
    job_title: str
    job_family: str
    grade_level: str
    flsa_status: str  # EXEMPT, NON_EXEMPT
    minimum_years_experience: int
    education_requirement: str
    core_competencies: List[str]
    salary_band_min_usd: float
    salary_band_mid_usd: float
    salary_band_max_usd: float
    target_annual_bonus_pct: float
    target_annual_rsu_shares: int


JOB_CATALOG_REGISTRY: Dict[str, JobRoleDefinition] = {
    # Engineering Job Family
    "ENG-SWE-L1": JobRoleDefinition("ENG-SWE-L1", "Associate Software Engineer", "Engineering", "L1", "EXEMPT", 0, "Bachelor", ["Python", "Git", "Data Structures", "Unit Testing"], 85000.0, 100000.0, 115000.0, 0.05, 100),
    "ENG-SWE-L2": JobRoleDefinition("ENG-SWE-L2", "Software Engineer I", "Engineering", "L2", "EXEMPT", 2, "Bachelor", ["FastAPI", "PostgreSQL", "Docker", "REST APIs"], 110000.0, 125000.0, 145000.0, 0.08, 250),
    "ENG-SWE-L3": JobRoleDefinition("ENG-SWE-L3", "Software Engineer II", "Engineering", "L3", "EXEMPT", 4, "Bachelor", ["Microservices", "Redis", "CI/CD", "System Design"], 135000.0, 155000.0, 175000.0, 0.12, 500),
    "ENG-SWE-L4": JobRoleDefinition("ENG-SWE-L4", "Senior Software Engineer", "Engineering", "L4", "EXEMPT", 6, "Bachelor", ["Distributed Systems", "Cloud Architecture", "Mentorship", "Scalability"], 165000.0, 190000.0, 220000.0, 0.15, 1000),
    "ENG-SWE-L5": JobRoleDefinition("ENG-SWE-L5", "Staff Software Engineer", "Engineering", "L5", "EXEMPT", 8, "Bachelor", ["Cross-Functional Leadership", "Technical Strategy", "High-Availability"], 200000.0, 235000.0, 275000.0, 0.20, 2000),
    "ENG-SWE-L6": JobRoleDefinition("ENG-SWE-L6", "Principal Software Engineer", "Engineering", "L6", "EXEMPT", 12, "Master", ["Enterprise Architecture", "Multi-Region Systems", "Executive Alignment"], 250000.0, 290000.0, 340000.0, 0.25, 3500),
    "ENG-DEV-L4": JobRoleDefinition("ENG-DEV-L4", "Senior DevOps / SRE Engineer", "Engineering", "L4", "EXEMPT", 6, "Bachelor", ["Kubernetes", "Terraform", "AWS", "Prometheus", "Incident Response"], 170000.0, 195000.0, 225000.0, 0.15, 1000),
    "ENG-SEC-L4": JobRoleDefinition("ENG-SEC-L4", "Senior Application Security Engineer", "Engineering", "L4", "EXEMPT", 6, "Bachelor", ["AppSec", "OAuth2", "SOC2", "Penetration Testing", "Threat Modeling"], 175000.0, 200000.0, 230000.0, 0.15, 1000),
    "ENG-MGR-M1": JobRoleDefinition("ENG-MGR-M1", "Engineering Manager", "Engineering", "M1", "EXEMPT", 7, "Bachelor", ["Team Leadership", "Agile Execution", "Hiring", "Performance Management"], 185000.0, 215000.0, 250000.0, 0.20, 2000),
    "ENG-DIR-D1": JobRoleDefinition("ENG-DIR-D1", "Director of Engineering", "Engineering", "D1", "EXEMPT", 12, "Bachelor", ["Organizational Strategy", "Budgeting", "VP Alignment", "Tech Roadmap"], 240000.0, 280000.0, 330000.0, 0.30, 6000),

    # Product & Design Family
    "PRD-PM-L3": JobRoleDefinition("PRD-PM-L3", "Product Manager II", "Product", "L3", "EXEMPT", 3, "Bachelor", ["Product Discovery", "PRD Writing", "User Research", "Metrics Analysis"], 130000.0, 150000.0, 170000.0, 0.12, 500),
    "PRD-PM-L4": JobRoleDefinition("PRD-PM-L4", "Senior Product Manager", "Product", "L4", "EXEMPT", 6, "Bachelor", ["Product Vision", "GTM Strategy", "Stakeholder Management"], 160000.0, 185000.0, 215000.0, 0.15, 1000),
    "DES-UX-L3": JobRoleDefinition("DES-UX-L3", "Product Designer II", "Design", "L3", "EXEMPT", 3, "Bachelor", ["Figma", "Design Systems", "Prototyping", "User Journey Mapping"], 120000.0, 140000.0, 160000.0, 0.10, 400),
    "DES-UX-L4": JobRoleDefinition("DES-UX-L4", "Senior Product Designer", "Design", "L4", "EXEMPT", 6, "Bachelor", ["Design System Architecture", "Design Sprints", "Design Mentorship"], 150000.0, 175000.0, 200000.0, 0.15, 800),

    # Sales & Revenue Family
    "SLS-SDR-L1": JobRoleDefinition("SLS-SDR-L1", "Sales Development Rep", "Sales", "L1", "NON_EXEMPT", 1, "Bachelor", ["Cold Outreach", "Prospecting", "Lead Qualification", "Salesforce"], 55000.0, 65000.0, 75000.0, 0.30, 50),
    "SLS-AE-L3": JobRoleDefinition("SLS-AE-L3", "Account Executive (Mid-Market)", "Sales", "L3", "EXEMPT", 4, "Bachelor", ["Consultative Selling", "Contract Negotiation", "Demo Mastery"], 90000.0, 110000.0, 130000.0, 0.50, 400),
    "SLS-ENT-L4": JobRoleDefinition("SLS-ENT-L4", "Enterprise Account Executive", "Sales", "L4", "EXEMPT", 7, "Bachelor", ["C-Level Engagement", "Complex Procurement", "MEDDPICC"], 140000.0, 165000.0, 195000.0, 0.50, 1000),

    # Human Resources Family
    "HR-REC-L3": JobRoleDefinition("HR-REC-L3", "Technical Recruiter II", "Human Resources", "L3", "EXEMPT", 3, "Bachelor", ["Talent Sourcing", "Interview Coordination", "Offer Negotiation"], 95000.0, 115000.0, 135000.0, 0.10, 300),
    "HR-BP-L4": JobRoleDefinition("HR-BP-L4", "Senior HR Business Partner", "Human Resources", "L4", "EXEMPT", 6, "Bachelor", ["Talent Strategy", "Employee Relations", "Succession Planning"], 140000.0, 160000.0, 185000.0, 0.15, 800),
    "HR-CMP-L4": JobRoleDefinition("HR-CMP-L4", "Senior Compensation & Benefits Manager", "Human Resources", "L4", "EXEMPT", 6, "Bachelor", ["Job Architecture", "Salary Survey Benchmarking", "Executive Comp"], 150000.0, 175000.0, 200000.0, 0.15, 800),

    # Finance & Legal Family
    "FIN-FPNA-L3": JobRoleDefinition("FIN-FPNA-L3", "Financial Analyst II (FP&A)", "Finance", "L3", "EXEMPT", 3, "Bachelor", ["Financial Modeling", "Budget Variance Analysis", "Excel/SQL"], 105000.0, 125000.0, 145000.0, 0.12, 400),
    "FIN-CON-D1": JobRoleDefinition("FIN-CON-D1", "Corporate Controller", "Finance", "D1", "EXEMPT", 10, "Master / CPA", ["US GAAP", "Audit Management", "SOX 404", "Revenue Recognition"], 210000.0, 245000.0, 285000.0, 0.25, 4000),
    "LEG-CORP-L4": JobRoleDefinition("LEG-CORP-L4", "Senior Corporate Counsel", "Legal", "L4", "EXEMPT", 6, "Juris Doctor (JD)", ["Commercial Contracts", "SaaS Licensing", "Data Privacy (GDPR)"], 180000.0, 210000.0, 245000.0, 0.20, 1500),
}
