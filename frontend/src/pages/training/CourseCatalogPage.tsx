import React from 'react';
import { BookOpen, Clock, Award, CheckCircle2, Play, Sparkles } from 'lucide-react';

export const CourseCatalogPage: React.FC = () => {
  const courses = [
    { id: 'SEC-101', title: 'ISO 27001 & SOC2 Information Security Awareness', category: 'Security & Compliance', hours: 2.5, difficulty: 'Foundational', progress: 100 },
    { id: 'ENG-SYS-201', title: 'High-Scale Distributed Systems Architecture', category: 'Engineering', hours: 12.0, difficulty: 'Advanced', progress: 45 },
    { id: 'LDR-MGR-301', title: 'First-Time Manager Coaching & Radical Candor', category: 'Leadership', hours: 6.0, difficulty: 'Intermediate', progress: 0 },
    { id: 'AI-LLM-401', title: 'Production Retrieval-Augmented Generation (RAG)', category: 'Artificial Intelligence', hours: 10.0, difficulty: 'Advanced', progress: 10 },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">Enterprise Learning & Development Portal</h2>
        <p className="text-xs text-slate-500">
          Professional development curricula, certifications, and compliance credentials.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {courses.map((c) => (
          <div key={c.id} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-4 flex flex-col justify-between">
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-blue-50 text-blue-700 border border-blue-100">
                  {c.category}
                </span>
                <span className="text-[10px] font-semibold text-slate-400 flex items-center gap-1">
                  <Clock className="w-3 h-3" /> {c.hours} Hours
                </span>
              </div>
              <h3 className="font-bold text-sm text-slate-900 leading-snug">{c.title}</h3>
            </div>

            <div className="space-y-3 pt-2">
              <div className="space-y-1">
                <div className="flex justify-between text-[11px] font-semibold">
                  <span className="text-slate-500">Course Progress</span>
                  <span className="text-slate-900">{c.progress}%</span>
                </div>
                <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                  <div className="bg-blue-600 h-2 rounded-full transition-all" style={{ width: `${c.progress}%` }} />
                </div>
              </div>

              <button className="w-full py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-semibold text-xs flex items-center justify-center gap-2 transition-colors">
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>{c.progress === 100 ? 'Review Course Material' : c.progress > 0 ? 'Resume Lesson' : 'Start Course'}</span>
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
