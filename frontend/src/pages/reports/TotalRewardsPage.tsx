import React, { useState } from 'react';
import { TotalRewardsSummary } from '../../types';
import { DollarSign, ShieldCheck, Heart, Award, Sparkles, Building2, Download, Printer } from 'lucide-react';

export const TotalRewardsPage: React.FC = () => {
  const [baseSalary, setBaseSalary] = useState(165000);
  const [bonusTarget, setBonusTarget] = useState(24750);
  const [equityValue, setEquityValue] = useState(35000);
  const [planType, setPlanType] = useState('FAMILY');

  const healthSubsidy = planType === 'FAMILY' ? 18000 : 7500;
  const match401k = Math.min(baseSalary * 0.04, 23500 * 0.04);
  const wellnessStipend = 2400;

  const totalRewards = baseSalary + bonusTarget + equityValue + healthSubsidy + match401k + wellnessStipend;
  const benefitsValue = healthSubsidy + match401k + wellnessStipend;
  const benefitsMultiplier = ((benefitsValue / baseSalary) * 100).toFixed(1);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">Total Rewards & Compensation Statement</h2>
          <p className="text-xs text-slate-500">
            Comprehensive annual statement illustrating the complete value of your cash, equity, retirement, and healthcare investment.
          </p>
        </div>
        <button
          onClick={() => window.print()}
          className="px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm"
        >
          <Printer className="w-4 h-4" />
          <span>Print Official Statement</span>
        </button>
      </div>

      {/* Hero Card */}
      <div className="p-8 rounded-3xl bg-gradient-to-br from-blue-900 via-indigo-900 to-slate-900 text-white shadow-xl space-y-6">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div>
            <span className="text-[11px] font-bold tracking-wider uppercase text-blue-300">
              Total Annual Investment in You
            </span>
            <h3 className="text-4xl font-black tracking-tight mt-1">
              ${totalRewards.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
            </h3>
            <p className="text-xs text-slate-300 mt-1">
              Includes base compensation, performance incentives, long-term equity, and ${benefitsValue.toLocaleString()} in company-sponsored benefits (+{benefitsMultiplier}% over base).
            </p>
          </div>
          <div className="p-4 rounded-2xl bg-white/10 backdrop-blur-md border border-white/10 text-right">
            <span className="text-[10px] font-bold uppercase text-blue-200">Employer Benefits Value</span>
            <p className="text-2xl font-bold text-emerald-400">+${benefitsValue.toLocaleString()}</p>
          </div>
        </div>
      </div>

      {/* Compensation Components Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Direct Cash */}
        <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
          <div className="flex items-center gap-3 text-blue-600">
            <div className="p-2.5 rounded-xl bg-blue-50">
              <DollarSign className="w-5 h-5" />
            </div>
            <div>
              <h4 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Direct Cash Pay</h4>
              <p className="text-[11px] text-slate-500">Base & Short-Term Incentives</p>
            </div>
          </div>
          <div className="space-y-2 text-xs divide-y divide-slate-100">
            <div className="flex justify-between pt-2">
              <span className="text-slate-600">Annual Base Salary</span>
              <span className="font-bold text-slate-900">${baseSalary.toLocaleString()}</span>
            </div>
            <div className="flex justify-between pt-2">
              <span className="text-slate-600">Target STI Bonus (15%)</span>
              <span className="font-bold text-slate-900">${bonusTarget.toLocaleString()}</span>
            </div>
            <div className="flex justify-between pt-2 font-bold text-blue-600">
              <span>Total Direct Cash</span>
              <span>${(baseSalary + bonusTarget).toLocaleString()}</span>
            </div>
          </div>
        </div>

        {/* Equity */}
        <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
          <div className="flex items-center gap-3 text-violet-600">
            <div className="p-2.5 rounded-xl bg-violet-50">
              <Sparkles className="w-5 h-5" />
            </div>
            <div>
              <h4 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Long-Term Equity</h4>
              <p className="text-[11px] text-slate-500">Restricted Stock Units (RSUs)</p>
            </div>
          </div>
          <div className="space-y-2 text-xs divide-y divide-slate-100">
            <div className="flex justify-between pt-2">
              <span className="text-slate-600">Annual RSU Vesting</span>
              <span className="font-bold text-slate-900">${equityValue.toLocaleString()}</span>
            </div>
            <div className="flex justify-between pt-2">
              <span className="text-slate-600">Vesting Schedule</span>
              <span className="font-bold text-slate-900">4-Year Quarterly</span>
            </div>
            <div className="flex justify-between pt-2 font-bold text-violet-600">
              <span>Annualized Equity Value</span>
              <span>${equityValue.toLocaleString()}</span>
            </div>
          </div>
        </div>

        {/* Benefits & Subsidies */}
        <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
          <div className="flex items-center gap-3 text-emerald-600">
            <div className="p-2.5 rounded-xl bg-emerald-50">
              <Heart className="w-5 h-5" />
            </div>
            <div>
              <h4 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Company Benefits</h4>
              <p className="text-[11px] text-slate-500">Health, 401(k) & Perks</p>
            </div>
          </div>
          <div className="space-y-2 text-xs divide-y divide-slate-100">
            <div className="flex justify-between pt-2">
              <span className="text-slate-600">Healthcare Premium Subsidy</span>
              <span className="font-bold text-slate-900">${healthSubsidy.toLocaleString()}</span>
            </div>
            <div className="flex justify-between pt-2">
              <span className="text-slate-600">401(k) Safe Harbor Match (4%)</span>
              <span className="font-bold text-slate-900">${match401k.toLocaleString()}</span>
            </div>
            <div className="flex justify-between pt-2">
              <span className="text-slate-600">Wellness & Learning Stipends</span>
              <span className="font-bold text-slate-900">${wellnessStipend.toLocaleString()}</span>
            </div>
            <div className="flex justify-between pt-2 font-bold text-emerald-600">
              <span>Total Benefits Value</span>
              <span>${benefitsValue.toLocaleString()}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
