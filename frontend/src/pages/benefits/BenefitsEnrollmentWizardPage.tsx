import React, { useState } from 'react';
import { Heart, ShieldCheck, DollarSign, CheckCircle2, ArrowRight, Sparkles } from 'lucide-react';

export const BenefitsEnrollmentWizardPage: React.FC = () => {
  const [selectedMedical, setSelectedMedical] = useState('HDHP_HSA');
  const [selectedDental, setSelectedDental] = useState('COMPREHENSIVE');
  const [selectedVision, setSelectedVision] = useState('STANDARD');
  const [hsaContribution, setHsaContribution] = useState(350);
  const [contrib401k, setContrib401k] = useState(8); // 8%

  const plans = {
    medical: [
      { id: 'HDHP_HSA', name: 'High Deductible Health Plan (HDHP) + HSA', deductible: '$1,600 / $3,200', premium: '$0 / mo (100% Employer Paid)', hsaMatch: '$1,000 Employer Seed', desc: 'Best for low healthcare utilization with triple-tax-advantaged HSA savings.' },
      { id: 'PPO_PREMIUM', name: 'Premier Copay PPO 500', deductible: '$500 / $1,000', premium: '$120 / mo (Employee Portion)', hsaMatch: 'FSA Eligible Only', desc: 'Low copays ($20 primary / $40 specialist) with broad national in-network access.' },
    ],
    dental: [
      { id: 'COMPREHENSIVE', name: 'Delta Dental Premier Plus', coverage: '100% Preventive, 80% Basic, 50% Major ($2,500 Annual Max)', premium: '$0 / mo' },
    ],
    vision: [
      { id: 'STANDARD', name: 'VSP Vision Choice Plan', coverage: '$10 Copay Exam, $250 Frame Allowance every 12 months', premium: '$0 / mo' },
    ]
  };

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">Annual Benefits Open Enrollment (2026 Plan Year)</h2>
        <p className="text-xs text-slate-500">
          Select healthcare, dental, vision, HSA savings, and retirement 401(k) allocations for the upcoming calendar year.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Selection Columns */}
        <div className="lg:col-span-2 space-y-6">
          {/* Medical Selection */}
          <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
            <div className="flex items-center gap-2 text-blue-600">
              <Heart className="w-5 h-5" />
              <h3 className="font-bold text-sm text-slate-900">1. Medical & Prescription Drug Coverage</h3>
            </div>

            <div className="grid grid-cols-1 gap-3">
              {plans.medical.map((p) => (
                <div
                  key={p.id}
                  onClick={() => setSelectedMedical(p.id)}
                  className={`p-4 rounded-xl border cursor-pointer transition-all ${
                    selectedMedical === p.id
                      ? 'border-blue-600 bg-blue-50/50 ring-2 ring-blue-600/20'
                      : 'border-slate-200 hover:border-slate-300 bg-white'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <h4 className="font-bold text-xs text-slate-900">{p.name}</h4>
                    <span className="text-[11px] font-bold text-emerald-700">{p.premium}</span>
                  </div>
                  <p className="text-[11px] text-slate-500 mt-1">{p.desc}</p>
                  <div className="flex gap-4 mt-3 text-[10px] font-medium text-slate-600 pt-2 border-t border-slate-100">
                    <span>Deductible: <strong>{p.deductible}</strong></span>
                    <span>HSA / FSA: <strong>{p.hsaMatch}</strong></span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* 401k Allocation */}
          <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
            <div className="flex items-center gap-2 text-violet-600">
              <Sparkles className="w-5 h-5" />
              <h3 className="font-bold text-sm text-slate-900">2. Safe Harbor 401(k) Retirement Contribution</h3>
            </div>

            <div className="space-y-3">
              <div className="flex justify-between text-xs">
                <span className="text-slate-600">Pre-Tax Salary Contribution Rate</span>
                <span className="font-bold text-slate-900">{contrib401k}% of Base Salary</span>
              </div>
              <input
                type="range"
                min="0"
                max="25"
                value={contrib401k}
                onChange={(e) => setContrib401k(parseInt(e.target.value))}
                className="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-blue-600"
              />
              <div className="p-3 rounded-xl bg-violet-50 border border-violet-100 text-[11px] text-violet-900 flex items-center justify-between">
                <span>Employer Safe Harbor Match: <strong>100% match on first 4%</strong></span>
                <span className="font-bold text-emerald-700">+4.0% Free Company Match</span>
              </div>
            </div>
          </div>
        </div>

        {/* Summary Sidebar */}
        <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-6 flex flex-col justify-between h-fit">
          <div className="space-y-4">
            <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Enrollment Summary</h3>
            <div className="space-y-3 text-xs divide-y divide-slate-100">
              <div className="pt-2">
                <span className="text-[10px] text-slate-400 uppercase font-semibold">Medical</span>
                <p className="font-bold text-slate-900">{selectedMedical === 'HDHP_HSA' ? 'HDHP with $1k Seed' : 'Premier PPO'}</p>
              </div>
              <div className="pt-2">
                <span className="text-[10px] text-slate-400 uppercase font-semibold">401(k) Total Contribution</span>
                <p className="font-bold text-slate-900">{contrib401k + 4}% (Your {contrib401k}% + 4% Match)</p>
              </div>
              <div className="pt-2">
                <span className="text-[10px] text-slate-400 uppercase font-semibold">Total Monthly Payroll Deduction</span>
                <p className="text-xl font-black text-slate-900 mt-1">$0.00 / mo</p>
                <p className="text-[10px] text-emerald-600 font-medium">100% covered by employer health subsidy</p>
              </div>
            </div>
          </div>

          <button className="w-full py-3 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs flex items-center justify-center gap-2 shadow-sm shadow-blue-500/20">
            <CheckCircle2 className="w-4 h-4" />
            <span>Confirm & Electronically Sign</span>
          </button>
        </div>
      </div>
    </div>
  );
};
