import React from 'react';
import { Calendar, DollarSign, Download, ShieldCheck, TrendingUp } from 'lucide-react';
import { useExportData } from '../../hooks/useTableSort';

export const LeaveLiabilityReportPage: React.FC = () => {
  const { exportToCSV } = useExportData();

  const liabilityData = [
    { dept: 'Engineering', headcount: 85, accruedDays: 680, avgDailyRate: 650, totalLiabilityUSD: 442000 },
    { dept: 'Product & Design', headcount: 22, accruedDays: 154, avgDailyRate: 580, totalLiabilityUSD: 89320 },
    { dept: 'Sales & Success', headcount: 45, accruedDays: 270, avgDailyRate: 480, totalLiabilityUSD: 129600 },
    { dept: 'Marketing', headcount: 16, accruedDays: 112, avgDailyRate: 450, totalLiabilityUSD: 50400 },
    { dept: 'Finance & Legal', headcount: 18, accruedDays: 144, avgDailyRate: 520, totalLiabilityUSD: 74880 },
    { dept: 'People Operations', headcount: 14, accruedDays: 98, avgDailyRate: 420, totalLiabilityUSD: 41160 },
  ];

  const totalAccruedDays = liabilityData.reduce((acc, r) => acc + r.accruedDays, 0);
  const totalLiability = liabilityData.reduce((acc, r) => acc + r.totalLiabilityUSD, 0);

  const handleExport = () => {
    exportToCSV('GAAP_ASC_710_Leave_Liability_Accrual_Report_2026', liabilityData);
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">GAAP ASC 710 Leave Liability & Accrual Report</h2>
          <p className="text-xs text-slate-500">
            Calculates balance sheet financial liability for earned unused paid time off (PTO) across departments.
          </p>
        </div>
        <button
          onClick={handleExport}
          className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm shadow-blue-500/20"
        >
          <Download className="w-4 h-4" />
          <span>Export GAAP CSV Report</span>
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-1">
          <span className="text-[11px] font-semibold uppercase text-slate-400">Total Unused Accrued PTO</span>
          <p className="text-2xl font-black text-slate-900">{totalAccruedDays.toLocaleString()} Days</p>
        </div>
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-1">
          <span className="text-[11px] font-semibold uppercase text-slate-400">Total Balance Sheet Accrued Liability</span>
          <p className="text-2xl font-black text-rose-600">${totalLiability.toLocaleString()}</p>
        </div>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Departmental Breakdown</h3>
          <span className="text-xs text-slate-500 font-medium">200 Total Full-Time Employees</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Department</th>
                <th className="py-3 px-4 text-center">Headcount</th>
                <th className="py-3 px-4 text-center">Accrued Unused Days</th>
                <th className="py-3 px-4 text-right">Avg. Daily Wage Rate</th>
                <th className="py-3 px-4 text-right">Financial Accrual Liability (USD)</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {liabilityData.map((row, i) => (
                <tr key={i} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3.5 px-4 font-bold text-slate-900">{row.dept}</td>
                  <td className="py-3.5 px-4 text-center font-semibold text-slate-700">{row.headcount}</td>
                  <td className="py-3.5 px-4 text-center font-bold text-blue-600">{row.accruedDays} Days</td>
                  <td className="py-3.5 px-4 text-right font-mono text-slate-700">${row.avgDailyRate}/day</td>
                  <td className="py-3.5 px-4 text-right font-mono font-bold text-slate-900">${row.totalLiabilityUSD.toLocaleString()}</td>
                </tr>
              ))}
            </tbody>
            <tfoot className="bg-slate-50 border-t border-slate-200 font-bold text-slate-900">
              <tr>
                <td colSpan={2} className="py-3 px-4 uppercase text-[11px]">Total GAAP Accrual</td>
                <td className="py-3 px-4 text-center font-mono">{totalAccruedDays.toLocaleString()} Days</td>
                <td className="py-3 px-4 text-right font-mono">-</td>
                <td className="py-3 px-4 text-right font-mono text-rose-600">${totalLiability.toLocaleString()}</td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>
    </div>
  );
};
