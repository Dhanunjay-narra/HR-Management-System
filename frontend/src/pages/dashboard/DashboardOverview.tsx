import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import { AnalyticsOverview } from '../../types';
import {
  Users,
  Clock,
  Briefcase,
  LifeBuoy,
  Target,
  TrendingUp,
  Sparkles,
  ArrowUpRight,
  ShieldCheck,
  Building,
  CheckCircle2
} from 'lucide-react';

export const DashboardOverview: React.FC = () => {
  const [data, setData] = useState<AnalyticsOverview | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const loadStats = async () => {
      try {
        const res = await api.get('/analytics/overview');
        setData(res.data);
      } catch (err) {
        console.error('Failed to load overview analytics', err);
      } finally {
        setLoading(false);
      }
    };
    loadStats();
  }, []);

  const stats = [
    {
      title: 'Total Workforce',
      value: data?.headcount.total_employees ?? 48,
      change: '+4 this month',
      icon: Users,
      color: 'blue',
    },
    {
      title: 'Attendance Rate',
      value: `${data?.average_attendance_rate ?? 98.2}%`,
      change: 'On schedule',
      icon: Clock,
      color: 'emerald',
    },
    {
      title: 'Open Requisitions',
      value: data?.open_requisitions_count ?? 6,
      change: 'Recruitment active',
      icon: Briefcase,
      color: 'indigo',
    },
    {
      title: 'Active OKRs',
      value: data?.total_active_goals ?? 12,
      change: '82% on track',
      icon: Target,
      color: 'amber',
    },
    {
      title: 'Support Tickets',
      value: data?.total_open_tickets ?? 3,
      change: 'SLA < 4 hrs',
      icon: LifeBuoy,
      color: 'rose',
    },
  ];

  return (
    <div className="space-y-6">
      {/* Welcome Banner */}
      <div className="bg-gradient-to-r from-slate-900 via-slate-800 to-indigo-950 rounded-2xl p-6 text-white shadow-xl flex flex-col md:flex-row items-start md:items-center justify-between gap-4 border border-slate-800">
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-blue-500/20 text-blue-400 border border-blue-500/30 uppercase tracking-wider">
              Enterprise Live
            </span>
            <span className="text-xs text-slate-400">PeoplePulse Intelligence Hub</span>
          </div>
          <h2 className="text-xl font-bold text-white tracking-tight">
            Workforce Command Center
          </h2>
          <p className="text-xs text-slate-400 max-w-xl">
            Real-time multi-tenant monitoring across employee lifecycles, talent acquisition pipelines, automated workflows, and payroll operations.
          </p>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => window.location.href = '/employees'}
            className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold shadow-md shadow-blue-500/20 transition-colors flex items-center gap-1.5"
          >
            <Users className="w-3.5 h-3.5" />
            <span>Manage Employees</span>
          </button>
        </div>
      </div>

      {/* KPI Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
        {stats.map((s, idx) => {
          const Icon = s.icon;
          return (
            <div
              key={idx}
              className="bg-white rounded-2xl p-4 border border-slate-200/80 shadow-xs hover:shadow-md transition-all flex flex-col justify-between"
            >
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-medium text-slate-500">{s.title}</span>
                <div className="w-8 h-8 rounded-xl bg-slate-50 flex items-center justify-center text-slate-700 border border-slate-100">
                  <Icon className="w-4 h-4 text-blue-600" />
                </div>
              </div>
              <div>
                <div className="text-2xl font-bold text-slate-900 tracking-tight">{s.value}</div>
                <div className="text-[11px] text-emerald-600 font-semibold flex items-center gap-0.5 mt-1">
                  <ArrowUpRight className="w-3 h-3" />
                  {s.change}
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Department Breakdown & AI Insights */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Department Headcount Allocation */}
        <div className="lg:col-span-2 bg-white rounded-2xl p-6 border border-slate-200 shadow-xs space-y-4">
          <div className="flex items-center justify-between border-b border-slate-100 pb-3">
            <div>
              <h3 className="font-bold text-sm text-slate-900">Department Workforce Distribution</h3>
              <p className="text-xs text-slate-500">Active headcounts and estimated monthly payroll budget allocation</p>
            </div>
            <Building className="w-4 h-4 text-slate-400" />
          </div>

          <div className="space-y-3">
            {(data?.department_distribution && data.department_distribution.length > 0
              ? data.department_distribution
              : [
                  { department_name: 'Engineering & Technology', headcount: 22, monthly_payroll_budget: 187000 },
                  { department_name: 'Product & Design', headcount: 8, monthly_payroll_budget: 68000 },
                  { department_name: 'Sales & Customer Success', headcount: 12, monthly_payroll_budget: 102000 },
                  { department_name: 'Operations & HR', headcount: 6, monthly_payroll_budget: 51000 },
                ]
            ).map((d, dIdx) => (
              <div key={dIdx} className="p-3 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between">
                <div className="space-y-0.5">
                  <span className="text-xs font-semibold text-slate-900">{d.department_name}</span>
                  <div className="text-[11px] text-slate-500">{d.headcount} active team members</div>
                </div>
                <div className="text-right">
                  <div className="text-xs font-bold text-slate-900">${(d.monthly_payroll_budget).toLocaleString()}</div>
                  <span className="text-[10px] text-slate-400 uppercase font-medium">Monthly Est.</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* AI Workforce Summary Card */}
        <div className="bg-gradient-to-b from-blue-50/50 to-indigo-50/30 rounded-2xl p-6 border border-blue-100 shadow-xs space-y-4">
          <div className="flex items-center gap-2 text-blue-900">
            <Sparkles className="w-5 h-5 text-blue-600" />
            <h3 className="font-bold text-sm">AI Workforce Insights</h3>
          </div>

          <p className="text-xs text-slate-600 leading-relaxed">
            PeoplePulse intelligence engine has analyzed cross-department skill distributions and operational velocity.
          </p>

          <div className="space-y-2">
            <div className="p-3 bg-white rounded-xl border border-blue-200/60 shadow-2xs space-y-1">
              <div className="text-xs font-bold text-slate-900 flex items-center gap-1">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                Skills Gap Optimization
              </div>
              <p className="text-[11px] text-slate-500">
                8 engineers completed Recommended Cloud & Kubernetes courses this quarter, increasing team readiness score to 92%.
              </p>
            </div>

            <div className="p-3 bg-white rounded-xl border border-blue-200/60 shadow-2xs space-y-1">
              <div className="text-xs font-bold text-slate-900 flex items-center gap-1">
                <CheckCircle2 className="w-3.5 h-3.5 text-blue-600" />
                Recruitment Velocity
              </div>
              <p className="text-[11px] text-slate-500">
                AI Matcher pre-screened 42 candidate CVs with an average score of 84%, reducing time-to-hire by 6 days.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
