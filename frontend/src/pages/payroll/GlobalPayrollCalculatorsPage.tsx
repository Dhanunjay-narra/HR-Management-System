import React, { useState } from 'react';
import { Globe2, DollarSign, Calculator, ShieldCheck, ArrowRight, Download } from 'lucide-react';

export const GlobalPayrollCalculatorsPage: React.FC = () => {
  const [selectedCountry, setSelectedCountry] = useState('DE');
  const [grossSalary, setGrossSalary] = useState(85000);

  const countryPresets = [
    { code: 'US', name: 'United States', currency: 'USD', gross: 120000, taxRate: '24.2%', net: 90960, erBurden: '7.65% (FICA)' },
    { code: 'UK', name: 'United Kingdom', currency: 'GBP', gross: 75000, taxRate: '28.5%', net: 53625, erBurden: '13.8% (NIC)' },
    { code: 'DE', name: 'Germany', currency: 'EUR', gross: 85000, taxRate: '38.2%', net: 52530, erBurden: '21.0% (Social)' },
    { code: 'FR', name: 'France', currency: 'EUR', gross: 70000, taxRate: '26.8%', net: 51240, erBurden: '42.0% (URSSAF)' },
    { code: 'CH', name: 'Switzerland', currency: 'CHF', gross: 140000, taxRate: '18.4%', net: 114240, erBurden: '12.5% (BVG/AHV)' },
    { code: 'SG', name: 'Singapore', currency: 'SGD', gross: 110000, taxRate: '12.0%', net: 96800, erBurden: '17.0% (CPF)' },
    { code: 'JP', name: 'Japan', currency: 'JPY', gross: 10000000, taxRate: '22.5%', net: 7750000, erBurden: '15.5% (Shakai Hoken)' },
    { code: 'AU', name: 'Australia', currency: 'AUD', gross: 130000, taxRate: '29.1%', net: 92170, erBurden: '11.5% (Super)' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">International Gross-to-Net Payroll Estimator</h2>
        <p className="text-xs text-slate-500">
          Real-time statutory tax calculations, mandatory employee deductions, and total employer burden modeling across 30+ countries.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {countryPresets.map((c) => (
          <div
            key={c.code}
            onClick={() => { setSelectedCountry(c.code); setGrossSalary(c.gross); }}
            className={`p-5 rounded-2xl border cursor-pointer transition-all ${
              selectedCountry === c.code
                ? 'border-blue-600 bg-blue-50/40 ring-2 ring-blue-600/20 shadow-xs'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="font-bold text-xs text-slate-900 flex items-center gap-1.5">
                <Globe2 className="w-4 h-4 text-blue-600" /> {c.name}
              </span>
              <span className="text-[10px] font-bold text-slate-400">{c.currency}</span>
            </div>

            <div className="mt-4 space-y-1">
              <span className="text-[10px] uppercase font-semibold text-slate-400">Benchmark Gross</span>
              <p className="text-base font-black text-slate-900">
                {c.currency} {c.gross.toLocaleString()}
              </p>
            </div>

            <div className="mt-3 pt-3 border-t border-slate-100 flex justify-between text-[11px]">
              <span className="text-slate-500">Effective Tax: <strong className="text-slate-800">{c.taxRate}</strong></span>
              <span className="text-emerald-700 font-bold">Net: {c.currency} {c.net.toLocaleString()}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
