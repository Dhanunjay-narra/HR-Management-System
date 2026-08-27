import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import { BarChart, LineChart } from '../../components/charts/BarChart';
import { TrendingUp, Users, DollarSign, Award, ArrowUpRight, ArrowDownRight, ShieldCheck } from 'lucide-react';

export const ExecutiveDashboardReport: React.FC = () => {
  const [stats, setStats] = useState<any>(null);

  useEffect(() => {
    api.get('/analytics/dashboard').then(res => setStats(res.data)).catch(console.error);
  }, []);

  const departmentData = [
    { label: 'Engineering', value: 84, color: 'bg-blue-600' },
    { label: 'Sales', value: 42, color: 'bg-emerald-600' },
    { label: 'Product', value: 18, color: 'bg-violet-600' },
    { label: 'Marketing', value: 14, color: 'bg-amber-600' },
    { label: 'Finance', value: 9, color: 'bg-rose-600' },
    { label: 'HR', value: 8, color: 'bg-cyan-600' },
  ];

  const attritionTrend = [
    { label: 'Q1', value: 2.1 },
    { label: 'Q2', value: 2.8 },
    { label: 'Q3', value: 1.9 },
    { label: 'Q4', value: 1.4 },
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">Executive Workforce Intelligence</h2>
        <p className="text-xs text-slate-500">
          Consolidated C-Suite overview of workforce headcount, annual payroll run-rate, and retention velocity.
        </p>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-2">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-[11px] font-semibold uppercase">Total Workforce FTE</span>
            <Users className="w-4 h-4 text-blue-600" />
          </div>
          <div className="flex items-baseline justify-between">
            <span className="text-2xl font-black text-slate-900">{stats?.total_employees || 175}</span>
            <span className="text-[10px] font-bold text-emerald-600 flex items-center">
              <ArrowUpRight className="w-3 h-3" /> +8.4% YoY
            </span>
          </div>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-2">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-[11px] font-semibold uppercase">Annual Payroll Run-Rate</span>
            <DollarSign className="w-4 h-4 text-emerald-600" />
          </div>
          <div className="flex items-baseline justify-between">
            <span className="text-2xl font-black text-slate-900">
              ${((stats?.monthly_payroll_spend || 1450000) * 12 / 1000000).toFixed(1)}M
            </span>
            <span className="text-[10px] font-bold text-slate-400">USD Annualized</span>
          </div>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-2">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-[11px] font-semibold uppercase">Annual Attrition Rate</span>
            <TrendingUp className="w-4 h-4 text-violet-600" />
          </div>
          <div className="flex items-baseline justify-between">
            <span className="text-2xl font-black text-slate-900">{stats?.turnover_rate_percent || 4.2}%</span>
            <span className="text-[10px] font-bold text-emerald-600 flex items-center">
              <ArrowDownRight className="w-3 h-3" /> -1.2%
            </span>
          </div>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-2">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-[11px] font-semibold uppercase">Employee eNPS Score</span>
            <Award className="w-4 h-4 text-amber-600" />
          </div>
          <div className="flex items-baseline justify-between">
            <span className="text-2xl font-black text-slate-900">+64</span>
            <span className="text-[10px] font-bold text-emerald-600">Top Quartile</span>
          </div>
        </div>
      </div>

      {/* Visual Analytics */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">
            Headcount by Department
          </h3>
          <BarChart data={departmentData} height={200} />
        </div>

        <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">
            Quarterly Attrition Rate Trend (%)
          </h3>
          <LineChart data={attritionTrend} height={200} strokeColor="#7c3aed" />
        </div>
      </div>
    </div>
  );
};
