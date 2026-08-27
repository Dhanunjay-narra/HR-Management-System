import React from 'react';
import { Users, ShieldCheck, ArrowRight, Award, AlertTriangle, Sparkles } from 'lucide-react';

export const SuccessionPlanningPage: React.FC = () => {
  const criticalRoles = [
    {
      title: 'VP of Infrastructure & Platform Engineering',
      incumbent: 'David Hassel',
      flightRisk: 'LOW',
      benchScore: 85,
      successors: [
        { name: 'Sarah Connor', currentRole: 'Staff Software Engineer', readiness: 'READY_NOW', fitScore: 92 },
        { name: 'Michael Chang', currentRole: 'Principal SRE', readiness: 'READY_IN_1_YEAR', fitScore: 84 },
      ]
    },
    {
      title: 'Director of Product Management (Enterprise)',
      incumbent: 'Rachel Green',
      flightRisk: 'ELEVATED',
      benchScore: 65,
      successors: [
        { name: 'Alex Mercer', currentRole: 'Senior Product Manager', readiness: 'READY_IN_1_YEAR', fitScore: 78 },
      ]
    },
    {
      title: 'Chief Information Security Officer (CISO)',
      incumbent: 'Arthur Dent',
      flightRisk: 'LOW',
      benchScore: 40,
      successors: [
        { name: 'Elena Rostova', currentRole: 'Security Lead', readiness: 'READY_IN_2_YEARS', fitScore: 68 },
      ]
    }
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">Succession Planning & Leadership Bench</h2>
        <p className="text-xs text-slate-500">
          Evaluates leadership continuity, single-point-of-failure vulnerabilities, and candidate readiness tiers.
        </p>
      </div>

      <div className="grid grid-cols-1 gap-6">
        {criticalRoles.map((role, idx) => (
          <div key={idx} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
              <div>
                <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">Critical Leadership Position</span>
                <h3 className="font-bold text-sm text-slate-900">{role.title}</h3>
                <p className="text-xs text-slate-500">Current Incumbent: <strong className="text-slate-700">{role.incumbent}</strong></p>
              </div>

              <div className="flex items-center gap-3">
                <div className="text-right">
                  <span className="text-[10px] font-semibold text-slate-400 uppercase">Bench Strength</span>
                  <p className="text-base font-black text-blue-600">{role.benchScore}/100</p>
                </div>
              </div>
            </div>

            {/* Successors */}
            <div className="space-y-2">
              <h4 className="text-[11px] font-bold text-slate-700 uppercase tracking-wider">Identified Succession Pipeline</h4>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {role.successors.map((s, sIdx) => (
                  <div key={sIdx} className="p-3.5 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between">
                    <div>
                      <p className="font-bold text-xs text-slate-900">{s.name}</p>
                      <p className="text-[10px] text-slate-500">{s.currentRole}</p>
                    </div>
                    <div className="text-right">
                      <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                        s.readiness === 'READY_NOW' ? 'bg-emerald-100 text-emerald-800' : 'bg-blue-100 text-blue-800'
                      }`}>
                        {s.readiness.replace(/_/g, ' ')}
                      </span>
                      <p className="text-[10px] font-medium text-slate-400 mt-0.5">{s.fitScore}% Competency Fit</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
