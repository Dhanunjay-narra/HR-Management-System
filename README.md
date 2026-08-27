# PeoplePulse CRM

## Enterprise HR Management & Employee Relationship Intelligence Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-brightgreen.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-teal.svg)](https://fastapi.tiangolo.com/)
[![React 18](https://img.shields.io/badge/React-18-blue.svg)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)](https://www.typescriptlang.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

---

## 🌟 Overview

**PeoplePulse CRM** is an enterprise-grade Human Resource Management and Employee Relationship Intelligence platform. Moving beyond traditional "record-keeping" HRMS systems, PeoplePulse delivers an end-to-end **Employee 360° model**, intelligent talent workflows, recruitment pipelines, skills intelligence, configurable HR automation, and AI-assisted operations.

### Key Differentiators
1. **Employee 360° Life-Cycle Timeline:** Unified chronological history from recruitment to exit.
2. **Skills Intelligence & LMS Engine:** Automated skill gap detection with personalized learning path recommendations.
3. **Configurable HR Workflow Engine:** Trigger-Condition-Action automation without modifying source code.
4. **HR Service Desk CRM:** SLA-driven employee ticketing and request resolution.
5. **AI Knowledge Assistant:** Policy document question-answering with verifiable citations.
6. **Multi-Tenant Architecture:** Strong data isolation, tenant-level policies, and granular RBAC (`module.resource.action`).

---

## 🏗️ Architecture

PeoplePulse is engineered as a clean **Modular Monolith** designed for high velocity, clean domain boundaries, and seamless future microservice extraction.

```
                         ┌───────────────────────┐
                         │      Web Client       │
                         │ React + TypeScript    │
                         └───────────┬───────────┘
                                     │ HTTPS / WebSocket
                         ┌───────────▼───────────┐
                         │    FastAPI Gateway    │
                         └───────────┬───────────┘
        ┌────────────────────────────┼───────────────────────────┐
        ▼                            ▼                           ▼
 ┌──────────────┐            ┌──────────────┐            ┌──────────────┐
 │ Core HR      │            │ Employee CRM │            │ Recruitment  │
 └──────────────┘            └──────────────┘            └──────────────┘
        │                            │                           │
        ├───────────────┐            ├──────────────┐            │
        ▼               ▼            ▼              ▼            ▼
 Attendance          Leave       Engagement     Performance   Onboarding
 Payroll             Skills      Service Desk   Goals         AI Parser
                         ┌───────────────────────┐
                         │   Workflow Engine     │
                         └───────────┬───────────┘
                         ┌───────────▼───────────┐
                         │ Domain Event Bus      │
                         └───────────┬───────────┘
              ┌──────────────────────┼─────────────────────┐
              ▼                      ▼                     ▼
         Notifications          Analytics                AI RAG
```

---

## 📦 Domain Modules (30 Modules)

1. **Authentication & Identity:** JWT, Refresh rotation, MFA TOTP, password policies, audit sessions.
2. **Multi-Tenancy:** Isolation, tenant policies, subscription tracking.
3. **Organization Management:** Branches, departments, designations, job grades, org chart hierarchy.
4. **Employee Master:** Comprehensive profiles, contracts, emergency contacts, bank details.
5. **Employee 360°:** Unified CRM view aggregating performance, attendance, skills, assets, tickets.
6. **Employee Timeline:** Chronological audit & event timeline of career milestones.
7. **Recruitment CRM:** Requisitions, candidate pipeline Kanban, interview panels, scorecards, offers.
8. **Candidate Intelligence:** Resume skill extraction, job matching algorithm, duplicate detector.
9. **Onboarding:** Checklist workflows, IT/access provisioning tasks, 30/60/90-day reviews.
10. **Attendance:** Clock-in/out, GPS/IP geofencing, shift scheduling, overtime, corrections.
11. **Leave Management:** Accrual policies, leave requests, manager approvals, holiday calendars.
12. **Payroll:** Salary structures, statutory deductions, bonuses, pay runs, payslip generation.
13. **Performance Management:** Review cycles, 360° peer feedback, competency ratings, PIPs.
14. **Goals & OKRs:** Org -> Department -> Team -> Individual cascading goal trees.
15. **Skills Intelligence:** Skills taxonomy, proficiency tracking, gap analysis vs job role.
16. **Learning Management (LMS):** Courses, lessons, quizzes, learning paths, auto-assignment.
17. **Employee Engagement:** Pulse surveys, eNPS, sentiment analysis, peer recognition kudos wall.
18. **HR Service Desk:** SLA-driven ticket management, categorization, internal notes, resolution.
19. **Workflow Automation:** Configurable Trigger-Condition-Action automation engine.
20. **Approval Engine:** Multi-level sequential and parallel approval routing.
21. **Internal Communication:** Company broadcasts, announcements, scheduled notifications.
22. **Document Management:** Policy vault, employee document storage, expiry tracking.
23. **Expense Management:** Expense claims, receipt attachments, policy thresholds, reimbursements.
24. **Asset Management:** Hardware/software register, custody assignment, maintenance logs.
25. **Workforce Analytics:** Headcount, attrition, diversity, leave utilization, cost dashboards.
26. **AI Assistant:** Semantic query answering, natural language workforce queries.
27. **HR Knowledge Assistant:** Document RAG engine for employee policy self-service.
28. **AI Document Processing:** Resume parsing and receipt OCR extraction.
29. **Notification Engine:** In-app notification hub, template rendering, multi-channel dispatch.
30. **Audit & Security:** Immutable audit trail, diff tracking, actor logging, IP tracking.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.11+
- Node.js 18+ & npm
- Docker & Docker Compose (optional for containerized deployment)

### Backend Setup
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
python -m app.main
```
The FastAPI documentation will be available at `http://localhost:8000/docs`.

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
The application will launch at `http://localhost:5173`.

### Docker Deployment
```bash
docker-compose up --build -d
```

---

## 🧪 Testing

Run backend tests:
```bash
pytest backend/tests -v
```

Run frontend build & linting:
```bash
cd frontend && npm run build
```

---

## 📄 License
Released under the [MIT License](LICENSE).
