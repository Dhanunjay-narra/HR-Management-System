import React, { useState } from 'react';
import { Globe2, ShieldCheck, Clock, Calendar, AlertCircle, FileText, CheckCircle2 } from 'lucide-react';

export const GlobalLaborStandardsPage: React.FC = () => {
  const [selectedCountry, setSelectedCountry] = useState('US');

  const standards = [
    { code: 'US', name: 'United States', hours: 40, pto: 0, sick: 0, maternity: '0 wks (FMLA unpaid)', notice: 'At-will (0 days)' },
    { code: 'UK', name: 'United Kingdom', hours: 37.5, pto: 28, sick: 28, maternity: '52 wks (39 paid)', notice: '1-12 weeks' },
    { code: 'DE', name: 'Germany', hours: 38.5, pto: 20, sick: 30, maternity: '14 wks (100% paid)', notice: '4 weeks - 7 months' },
    { code: 'FR', name: 'France', hours: 35.0, pto: 25, sick: 30, maternity: '16 wks (100% paid)', notice: '1-3 months' },
    { code: 'CA', name: 'Canada (Federal)', hours: 40.0, pto: 10, sick: 5, maternity: '17 wks (EI subsidized)', notice: '2-8 weeks' },
    { code: 'IN', name: 'India', hours: 48.0, pto: 18, sick: 12, maternity: '26 wks (100% paid)', notice: '30-90 days' },
    { code: 'AU', name: 'Australia', hours: 38.0, pto: 20, sick: 10, maternity: '18 wks (PLP funded)', notice: '1-5 weeks' },
    { code: 'SG', name: 'Singapore', hours: 44.0, pto: 7, sick: 14, maternity: '16 wks (GPML funded)', notice: '1 day - 4 weeks' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">Global Labor Standards & Statutory Compliance Matrix</h2>
        <p className="text-xs text-slate-500">
          International statutory employment benchmarks, working time limitations, and mandatory benefits baselines.
        </p>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Statutory Jurisdictions</h3>
          <span className="text-xs text-slate-500 font-medium">8 Key Markets Displayed</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Jurisdiction</th>
                <th className="py-3 px-4">Standard Workweek</th>
                <th className="py-3 px-4">Min. Annual Leave</th>
                <th className="py-3 px-4">Statutory Sick Days</th>
                <th className="py-3 px-4">Maternity Leave</th>
                <th className="py-3 px-4">Statutory Notice</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {standards.map((s) => (
                <tr key={s.code} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3.5 px-4 font-bold text-slate-900 flex items-center gap-2">
                    <Globe2 className="w-4 h-4 text-blue-600" />
                    <span>{s.name}</span>
                  </td>
                  <td className="py-3.5 px-4 font-semibold text-slate-700">{s.hours} Hours / Wk</td>
                  <td className="py-3.5 px-4 font-bold text-emerald-600">{s.pto} Days Minimum</td>
                  <td className="py-3.5 px-4 font-medium text-slate-600">{s.sick} Days</td>
                  <td className="py-3.5 px-4 font-medium text-slate-800">{s.maternity}</td>
                  <td className="py-3.5 px-4 text-slate-500">{s.notice}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
