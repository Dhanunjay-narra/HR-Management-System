import React, { useState } from 'react';
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
