import React from 'react';
import { Heart, TrendingUp, AlertTriangle, Users, Smile, Frown, Meh } from 'lucide-react';

export const SentimentHeatmapPage: React.FC = () => {
  const departments = [
    { name: 'Engineering', score: 0.82, status: 'HIGH_SAFETY', respondents: 82, topDriver: 'Autonomy & Tech Stack' },
    { name: 'Product', score: 0.74, status: 'HIGH_SAFETY', respondents: 18, topDriver: 'Cross-Team Trust' },
    { name: 'Sales', score: 0.61, status: 'MODERATE_PRESSURE', respondents: 40, topDriver: 'Quota Attainment Pace' },
    { name: 'Customer Success', score: 0.58, status: 'ELEVATED_STRESS', respondents: 24, topDriver: 'Ticket Volume Spikes' },
    { name: 'Marketing', score: 0.79, status: 'HIGH_SAFETY', respondents: 14, topDriver: 'Creative Freedom' },
    { name: 'Finance & Legal', score: 0.88, status: 'HIGH_SAFETY', respondents: 16, topDriver: 'Clarity of Mandate' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">Workplace Psychological Safety & Sentiment Heatmap</h2>
        <p className="text-xs text-slate-500">
          NLP-driven sentiment analysis decomposing pulse surveys, peer kudos, and engagement velocity.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {departments.map((dept, idx) => (
          <div key={idx} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4">
            <div className="flex items-center justify-between">
              <h3 className="font-bold text-sm text-slate-900">{dept.name}</h3>
              <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold ${
                dept.score >= 0.75 ? 'bg-emerald-100 text-emerald-800' : dept.score >= 0.60 ? 'bg-blue-100 text-blue-800' : 'bg-amber-100 text-amber-800'
              }`}>
                {dept.status.replace(/_/g, ' ')}
              </span>
            </div>

            <div className="flex items-baseline justify-between">
              <div className="text-2xl font-black text-slate-900">
                +{(dept.score * 100).toFixed(0)} <span className="text-xs text-slate-400 font-normal">/ 100 Sentiment Index</span>
              </div>
            </div>

            <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
              <div className={`h-2 rounded-full ${
                dept.score >= 0.75 ? 'bg-emerald-500' : dept.score >= 0.60 ? 'bg-blue-500' : 'bg-amber-500'
              }`} style={{ width: `${dept.score * 100}%` }} />
            </div>

            <div className="pt-2 border-t border-slate-100 text-[11px] text-slate-500 flex justify-between">
              <span>Primary Driver: <strong className="text-slate-700">{dept.topDriver}</strong></span>
              <span>{dept.respondents} responses</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
