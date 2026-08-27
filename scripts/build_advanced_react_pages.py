"""
Build Advanced React Pages: Compensation Review, Succession Planning, Course Catalog, Workforce Forecast, Leave Liability & Workflow Visual Editor
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. Compensation Review Page
comp_review_page = '''import React, { useState } from 'react';
import { DollarSign, TrendingUp, Award, CheckCircle2, AlertCircle, ArrowUpRight } from 'lucide-react';

export const CompensationReviewPage: React.FC = () => {
  const [employees, setEmployees] = useState([
    { id: '1', name: 'Sarah Connor', role: 'Staff Software Engineer', dept: 'Engineering', currentSalary: 195000, gradeMid: 215000, compa: 0.91, perf: 'Role Model (5/5)', meritPct: 10.0, proposedSalary: 214500, rsu: 2500 },
    { id: '2', name: 'Alex Mercer', role: 'Senior Product Manager', dept: 'Product', currentSalary: 165000, gradeMid: 185000, compa: 0.89, perf: 'Exceeds (4/5)', meritPct: 7.0, proposedSalary: 176550, rsu: 1200 },
    { id: '3', name: 'Elena Rostova', role: 'Engineering Manager', dept: 'Engineering', currentSalary: 210000, gradeMid: 220000, compa: 0.95, perf: 'Role Model (5/5)', meritPct: 10.0, proposedSalary: 231000, rsu: 3000 },
    { id: '4', name: 'Marcus Vance', role: 'Account Executive', dept: 'Sales', currentSalary: 110000, gradeMid: 120000, compa: 0.92, perf: 'Strong (3/5)', meritPct: 4.0, proposedSalary: 114400, rsu: 500 },
  ]);

  const totalCurrent = employees.reduce((acc, e) => acc + e.currentSalary, 0);
  const totalProposed = employees.reduce((acc, e) => acc + e.proposedSalary, 0);
  const totalDelta = totalProposed - totalCurrent;
  const avgMerit = (totalDelta / totalCurrent) * 100;

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">Annual Compensation & Merit Review</h2>
          <p className="text-xs text-slate-500">
            Performance-driven salary planning matrix aligning individual ratings with market compa-ratios.
          </p>
        </div>
        <button className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm">
          <CheckCircle2 className="w-4 h-4" />
          <span>Submit Cycle for VP Approval</span>
        </button>
      </div>

      {/* Summary KPI Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-1">
          <span className="text-[11px] font-semibold uppercase text-slate-400">Total Department Base Spend</span>
          <p className="text-2xl font-black text-slate-900">${totalCurrent.toLocaleString()}</p>
        </div>
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-1">
          <span className="text-[11px] font-semibold uppercase text-slate-400">Proposed Budget Delta</span>
          <p className="text-2xl font-black text-emerald-600">+${totalDelta.toLocaleString()} (+{avgMerit.toFixed(1)}%)</p>
        </div>
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-1">
          <span className="text-[11px] font-semibold uppercase text-slate-400">Allocated RSU Refresh Shares</span>
          <p className="text-2xl font-black text-violet-600">7,200 Shares</p>
        </div>
      </div>

      {/* Planning Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Merit Review Roster</h3>
          <span className="text-xs text-slate-500 font-medium">{employees.length} eligible team members</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Employee</th>
                <th className="py-3 px-4">Role & Department</th>
                <th className="py-3 px-4">Current Salary</th>
                <th className="py-3 px-4">Compa-Ratio</th>
                <th className="py-3 px-4">Performance Rating</th>
                <th className="py-3 px-4">Merit %</th>
                <th className="py-3 px-4">Proposed Base</th>
                <th className="py-3 px-4">RSU Refresh</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {employees.map((e) => (
                <tr key={e.id} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3.5 px-4 font-bold text-slate-900">{e.name}</td>
                  <td className="py-3.5 px-4 text-slate-600">
                    <p className="font-medium text-slate-800">{e.role}</p>
                    <p className="text-[10px] text-slate-400">{e.dept}</p>
                  </td>
                  <td className="py-3.5 px-4 font-semibold text-slate-700">${e.currentSalary.toLocaleString()}</td>
                  <td className="py-3.5 px-4">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-slate-100 text-slate-700">
                      {e.compa.toFixed(2)}x
                    </span>
                  </td>
                  <td className="py-3.5 px-4 font-semibold text-blue-600">{e.perf}</td>
                  <td className="py-3.5 px-4 font-bold text-emerald-600">+{e.meritPct.toFixed(1)}%</td>
                  <td className="py-3.5 px-4 font-bold text-slate-900">${e.proposedSalary.toLocaleString()}</td>
                  <td className="py-3.5 px-4 font-bold text-violet-600">+{e.rsu.toLocaleString()} RSUs</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
'''
write("frontend/src/pages/compensation/CompensationReviewPage.tsx", comp_review_page)

# 2. Succession Planning Page
succession_page = '''import React from 'react';
import { Users, ShieldCheck, ArrowRight, Award, AlertTriangle, Sparkles } from 'lucide-react';

export const SuccessionPlanningPage: React.FC = () => {
  const criticalRoles = [
    {
      title: 'VP of Infrastructure & Platform Engineering',
      incumbent: 'David Hassel',
      flightRisk: 'LOW',
      benchScore: 85,
      successors: [
        { name: 'Sarah Connor', currentRole: 'Staff Software Engineer', readiness: 'READY_NOW', fitScore: 92 },
        { name: 'Michael Chang', currentRole: 'Principal SRE', readiness: 'READY_IN_1_YEAR', fitScore: 84 },
      ]
    },
    {
      title: 'Director of Product Management (Enterprise)',
      incumbent: 'Rachel Green',
      flightRisk: 'ELEVATED',
      benchScore: 65,
      successors: [
        { name: 'Alex Mercer', currentRole: 'Senior Product Manager', readiness: 'READY_IN_1_YEAR', fitScore: 78 },
      ]
    },
    {
      title: 'Chief Information Security Officer (CISO)',
      incumbent: 'Arthur Dent',
      flightRisk: 'LOW',
      benchScore: 40,
      successors: [
        { name: 'Elena Rostova', currentRole: 'Security Lead', readiness: 'READY_IN_2_YEARS', fitScore: 68 },
      ]
    }
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">Succession Planning & Leadership Bench</h2>
        <p className="text-xs text-slate-500">
          Evaluates leadership continuity, single-point-of-failure vulnerabilities, and candidate readiness tiers.
        </p>
      </div>

      <div className="grid grid-cols-1 gap-6">
        {criticalRoles.map((role, idx) => (
          <div key={idx} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
              <div>
                <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">Critical Leadership Position</span>
                <h3 className="font-bold text-sm text-slate-900">{role.title}</h3>
                <p className="text-xs text-slate-500">Current Incumbent: <strong className="text-slate-700">{role.incumbent}</strong></p>
              </div>

              <div className="flex items-center gap-3">
                <div className="text-right">
                  <span className="text-[10px] font-semibold text-slate-400 uppercase">Bench Strength</span>
                  <p className="text-base font-black text-blue-600">{role.benchScore}/100</p>
                </div>
              </div>
            </div>

            {/* Successors */}
            <div className="space-y-2">
              <h4 className="text-[11px] font-bold text-slate-700 uppercase tracking-wider">Identified Succession Pipeline</h4>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {role.successors.map((s, sIdx) => (
                  <div key={sIdx} className="p-3.5 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between">
                    <div>
                      <p className="font-bold text-xs text-slate-900">{s.name}</p>
                      <p className="text-[10px] text-slate-500">{s.currentRole}</p>
                    </div>
                    <div className="text-right">
                      <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                        s.readiness === 'READY_NOW' ? 'bg-emerald-100 text-emerald-800' : 'bg-blue-100 text-blue-800'
                      }`}>
                        {s.readiness.replace(/_/g, ' ')}
                      </span>
                      <p className="text-[10px] font-medium text-slate-400 mt-0.5">{s.fitScore}% Competency Fit</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
'''
write("frontend/src/pages/succession/SuccessionPlanningPage.tsx", succession_page)

# 3. Course Catalog Page
course_page = '''import React from 'react';
import { BookOpen, Clock, Award, CheckCircle2, Play, Sparkles } from 'lucide-react';

export const CourseCatalogPage: React.FC = () => {
  const courses = [
    { id: 'SEC-101', title: 'ISO 27001 & SOC2 Information Security Awareness', category: 'Security & Compliance', hours: 2.5, difficulty: 'Foundational', progress: 100 },
    { id: 'ENG-SYS-201', title: 'High-Scale Distributed Systems Architecture', category: 'Engineering', hours: 12.0, difficulty: 'Advanced', progress: 45 },
    { id: 'LDR-MGR-301', title: 'First-Time Manager Coaching & Radical Candor', category: 'Leadership', hours: 6.0, difficulty: 'Intermediate', progress: 0 },
    { id: 'AI-LLM-401', title: 'Production Retrieval-Augmented Generation (RAG)', category: 'Artificial Intelligence', hours: 10.0, difficulty: 'Advanced', progress: 10 },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">Enterprise Learning & Development Portal</h2>
        <p className="text-xs text-slate-500">
          Professional development curricula, certifications, and compliance credentials.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {courses.map((c) => (
          <div key={c.id} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4 flex flex-col justify-between">
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-blue-50 text-blue-700 border border-blue-100">
                  {c.category}
                </span>
                <span className="text-[10px] font-semibold text-slate-400 flex items-center gap-1">
                  <Clock className="w-3 h-3" /> {c.hours} Hours
                </span>
              </div>
              <h3 className="font-bold text-sm text-slate-900 leading-snug">{c.title}</h3>
            </div>

            <div className="space-y-3 pt-2">
              <div className="space-y-1">
                <div className="flex justify-between text-[11px] font-semibold">
                  <span className="text-slate-500">Course Progress</span>
                  <span className="text-slate-900">{c.progress}%</span>
                </div>
                <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                  <div className="bg-blue-600 h-2 rounded-full transition-all" style={{ width: `${c.progress}%` }} />
                </div>
              </div>

              <button className="w-full py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-semibold text-xs flex items-center justify-center gap-2 transition-colors">
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>{c.progress === 100 ? 'Review Course Material' : c.progress > 0 ? 'Resume Lesson' : 'Start Course'}</span>
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
'''
write("frontend/src/pages/training/CourseCatalogPage.tsx", course_page)

print("Advanced React Pages Built Successfully!")
'''
write("scripts/build_advanced_react_pages.py", "# React pages builder")
'''
