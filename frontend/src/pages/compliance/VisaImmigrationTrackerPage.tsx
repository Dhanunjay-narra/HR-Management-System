import React from 'react';
import { Globe2, Calendar, AlertTriangle, ShieldCheck, CheckCircle2, Clock } from 'lucide-react';

export const VisaImmigrationTrackerPage: React.FC = () => {
  const visas = [
    { id: '1', name: 'Rajesh Kumar', role: 'Staff Software Engineer', country: 'India', visaType: 'H-1B Specialty', expiryDate: '2027-09-30', i140Status: 'APPROVED (Priority: 2022)', daysRemaining: 580, status: 'VALID' },
    { id: '2', name: 'Guillaume Dubois', role: 'Principal ML Architect', country: 'France', visaType: 'O-1A Extraordinary Ability', expiryDate: '2026-11-15', i140Status: 'N/A', daysRemaining: 80, status: 'RENEWAL_IN_PROGRESS' },
    { id: '3', name: 'Chen Wei', role: 'Senior SRE', country: 'China', visaType: 'H-1B Specialty', expiryDate: '2026-10-01', i140Status: 'PERM Certified', daysRemaining: 35, status: 'URGENT_ACTION' },
    { id: '4', name: 'Liam O’Connor', role: 'VP of Product', country: 'Ireland', visaType: 'L-1A Executive', expiryDate: '2028-06-30', i140Status: 'EB-1C Pending', daysRemaining: 850, status: 'VALID' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">Corporate Immigration & Work Authorization Registry</h2>
        <p className="text-xs text-slate-500">
          Tracks international visa validity (H-1B, L-1, O-1, TN, UK Skilled Worker), PERM labor certifications, and I-140 green card priority dates.
        </p>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Active Sponsored Foreign Nationals</h3>
          <span className="text-xs text-slate-500 font-medium">{visas.length} active petitions</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Employee</th>
                <th className="py-3 px-4">Role & Citizenship</th>
                <th className="py-3 px-4">Visa Classification</th>
                <th className="py-3 px-4">Expiration Date</th>
                <th className="py-3 px-4">Permanent Residency (I-140)</th>
                <th className="py-3 px-4">Compliance Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {visas.map((v) => (
                <tr key={v.id} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3.5 px-4 font-bold text-slate-900">{v.name}</td>
                  <td className="py-3.5 px-4">
                    <p className="font-medium text-slate-800">{v.role}</p>
                    <p className="text-[10px] text-slate-400 flex items-center gap-1">
                      <Globe2 className="w-3 h-3 text-blue-500" /> {v.country}
                    </p>
                  </td>
                  <td className="py-3.5 px-4 font-semibold text-blue-700">{v.visaType}</td>
                  <td className="py-3.5 px-4 font-medium text-slate-700">
                    {v.expiryDate} <span className="text-[10px] text-slate-400">({v.daysRemaining} days)</span>
                  </td>
                  <td className="py-3.5 px-4 font-medium text-slate-800">{v.i140Status}</td>
                  <td className="py-3.5 px-4">
                    <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold ${
                      v.status === 'VALID' ? 'bg-emerald-100 text-emerald-800' : v.status === 'RENEWAL_IN_PROGRESS' ? 'bg-blue-100 text-blue-800' : 'bg-rose-100 text-rose-800'
                    }`}>
                      {v.status.replace(/_/g, ' ')}
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
