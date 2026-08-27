import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import { PayrollRun } from '../../types';
import { DollarSign, CheckCircle2, Play, Calendar, Download, TrendingUp } from 'lucide-react';

export const PayrollDashboardPage: React.FC = () => {
  const [runs, setRuns] = useState<PayrollRun[]>([]);
  const [loading, setLoading] = useState(true);
  const [processing, setProcessing] = useState(false);

  const loadRuns = async () => {
    setLoading(true);
    try {
      const res = await api.get('/payroll/runs');
      setRuns(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadRuns();
  }, []);

  const handleExecutePayroll = async () => {
    const today = new Date();
    setProcessing(true);
    try {
      await api.post('/payroll/process', {
        month: today.getMonth() + 1,
        year: today.getFullYear(),
        pay_period_start: new Date(today.getFullYear(), today.getMonth(), 1).toISOString().split('T')[0],
        pay_period_end: today.toISOString().split('T')[0],
      });
      loadRuns();
    } catch (err: any) {
      alert(err.response?.data?.detail || 'Failed to process payroll run');
    } finally {
      setProcessing(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Top Banner */}
      <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
              Statutory Tax & Compliance
            </span>
            <span className="text-xs text-slate-500 font-medium">Automatic PF & TDS Deductions</span>
          </div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">Enterprise Payroll Management</h2>
          <p className="text-xs text-slate-500 max-w-md">
            Execute batch salary computations, generate compliant digital payslips, and disburse employee compensation.
          </p>
        </div>

        <button
          onClick={handleExecutePayroll}
          disabled={processing}
          className="px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white text-xs font-bold flex items-center gap-2 shadow-sm shadow-blue-500/20 transition-all flex-shrink-0"
        >
          <Play className="w-3.5 h-3.5 fill-white" />
          <span>{processing ? 'Calculating...' : 'Run Monthly Payroll'}</span>
        </button>
      </div>

      {/* Payroll Runs Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Payroll Processing Batches</h3>
          <span className="text-xs text-slate-500 font-medium">{runs.length} batches executed</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Period</th>
                <th className="py-3 px-4">Employees</th>
                <th className="py-3 px-4">Total Gross Payout</th>
                <th className="py-3 px-4">Statutory Deductions</th>
                <th className="py-3 px-4">Total Net Disbursed</th>
                <th className="py-3 px-4">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {runs.map((r) => (
                <tr key={r.id} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3 px-4 font-bold text-slate-900">
                    {r.month}/{r.year}
                  </td>
                  <td className="py-3 px-4 font-medium">{r.total_employees_count} staff</td>
                  <td className="py-3 px-4 font-mono font-medium text-slate-900">${r.total_gross_payout.toLocaleString()}</td>
                  <td className="py-3 px-4 font-mono text-rose-600">-${r.total_deductions.toLocaleString()}</td>
                  <td className="py-3 px-4 font-mono font-bold text-emerald-600">${r.total_net_payout.toLocaleString()}</td>
                  <td className="py-3 px-4">
                    <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200 flex items-center gap-1 w-fit">
                      <CheckCircle2 className="w-3 h-3" /> {r.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
