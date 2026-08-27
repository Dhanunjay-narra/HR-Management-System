import React from 'react';
import { Laptop, ShieldCheck, Clock, CheckCircle2, User, ArrowRight } from 'lucide-react';

export const AssetCustodyTimelinePage: React.FC = () => {
  const custodyHistory = [
    { id: '1', asset: 'MacBook Pro 16" M3 Max (64GB/1TB)', serial: 'C02XYZ123456', assignee: 'Sarah Connor', role: 'Staff Software Engineer', assignedDate: '2025-01-15', status: 'IN_USE', mdmStatus: 'ENCRYPTED_OK' },
    { id: '2', asset: 'Dell UltraSharp 32" 4K Monitor', serial: 'DELL-998877', assignee: 'Sarah Connor', role: 'Staff Software Engineer', assignedDate: '2025-01-15', status: 'IN_USE', mdmStatus: 'N/A' },
    { id: '3', asset: 'YubiKey 5C NFC Security Key', serial: 'YK-55443322', assignee: 'Sarah Connor', role: 'Staff Software Engineer', assignedDate: '2025-01-15', status: 'IN_USE', mdmStatus: 'REGISTERED' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">IT Hardware Custody & Lifecycle Management</h2>
        <p className="text-xs text-slate-500">
          Tracks physical device provisioning, MDM encryption compliance (FileVault/BitLocker), and chain of custody.
        </p>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Assigned Equipment Roster</h3>
          <span className="text-xs text-slate-500 font-medium">{custodyHistory.length} active hardware units</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Hardware Item</th>
                <th className="py-3 px-4">Serial Number</th>
                <th className="py-3 px-4">Assigned To</th>
                <th className="py-3 px-4">Provisioned Date</th>
                <th className="py-3 px-4">MDM Encryption</th>
                <th className="py-3 px-4">Custody Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {custodyHistory.map((item) => (
                <tr key={item.id} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3.5 px-4 font-bold text-slate-900 flex items-center gap-2">
                    <Laptop className="w-4 h-4 text-blue-600" />
                    <span>{item.asset}</span>
                  </td>
                  <td className="py-3.5 px-4 font-mono text-slate-500">{item.serial}</td>
                  <td className="py-3.5 px-4 font-medium text-slate-800">{item.assignee}</td>
                  <td className="py-3.5 px-4 text-slate-600">{item.assignedDate}</td>
                  <td className="py-3.5 px-4">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800 flex items-center gap-1 w-fit">
                      <ShieldCheck className="w-3 h-3" /> {item.mdmStatus}
                    </span>
                  </td>
                  <td className="py-3.5 px-4">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-blue-100 text-blue-800">
                      {item.status}
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
