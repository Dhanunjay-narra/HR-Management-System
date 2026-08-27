import React from 'react';
import { ShieldCheck, Download, Users, CheckCircle2, FileSpreadsheet } from 'lucide-react';
import { useExportData } from '../../hooks/useTableSort';

export const EEO1ComplianceReportPage: React.FC = () => {
  const { exportToCSV } = useExportData();

  const eeoData = [
    { category: 'Executive / Senior Officials', total: 6, male: 4, female: 2, minorityPct: '33.3%' },
    { category: 'First / Mid-Level Managers', total: 24, male: 15, female: 9, minorityPct: '41.7%' },
    { category: 'Professionals (Engineering / Product)', total: 120, male: 78, female: 42, minorityPct: '48.3%' },
    { category: 'Sales Workers', total: 35, male: 20, female: 15, minorityPct: '37.1%' },
    { category: 'Administrative Support', total: 15, male: 5, female: 10, minorityPct: '46.7%' },
  ];

  const handleExport = () => {
    exportToCSV('EEO1_Component1_Workforce_Report_2026', eeoData);
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">EEOC EEO-1 Component 1 Compliance Report</h2>
          <p className="text-xs text-slate-500">
            Mandatory annual workforce demographic disclosure categorized by federal job classification bands.
          </p>
        </div>
        <button
          onClick={handleExport}
          className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm shadow-blue-500/20"
        >
          <Download className="w-4 h-4" />
          <span>Export EEOC CSV Filing</span>
        </button>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">EEO-1 Job Category Distribution</h3>
          <span className="text-xs text-slate-500 font-medium">200 Total Full-Time Employees</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Federal Job Category</th>
                <th className="py-3 px-4 text-center">Total Headcount</th>
                <th className="py-3 px-4 text-center">Male</th>
                <th className="py-3 px-4 text-center">Female</th>
                <th className="py-3 px-4 text-right">Minority Representation</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {eeoData.map((row, i) => (
                <tr key={i} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3.5 px-4 font-bold text-slate-900">{row.category}</td>
                  <td className="py-3.5 px-4 text-center font-bold text-slate-800">{row.total}</td>
                  <td className="py-3.5 px-4 text-center text-slate-600">{row.male}</td>
                  <td className="py-3.5 px-4 text-center text-slate-600">{row.female}</td>
                  <td className="py-3.5 px-4 text-right font-bold text-blue-600">{row.minorityPct}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
