import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import { JobRequisition, Candidate } from '../../types';
import {
  UserPlus,
  Briefcase,
  Search,
  Sparkles,
  Plus,
  ArrowRight,
  CheckCircle,
  FileText,
  X
} from 'lucide-react';

const STAGES = [
  { id: 'APPLIED', name: 'Applied', color: 'bg-slate-100 border-slate-200' },
  { id: 'SCREENING', name: 'Screening', color: 'bg-blue-50 border-blue-200' },
  { id: 'TECH_INTERVIEW', name: 'Tech Interview', color: 'bg-indigo-50 border-indigo-200' },
  { id: 'FINAL_ROUND', name: 'Final Round', color: 'bg-purple-50 border-purple-200' },
  { id: 'OFFERED', name: 'Offered', color: 'bg-emerald-50 border-emerald-200' },
  { id: 'HIRED', name: 'Hired', color: 'bg-green-50 border-green-200' },
];

export const RecruitmentKanbanPage: React.FC = () => {
  const [jobs, setJobs] = useState<JobRequisition[]>([]);
  const [selectedJobId, setSelectedJobId] = useState<string>('');
  const [candidates, setCandidates] = useState<Candidate[]>([]);
  const [loading, setLoading] = useState(true);
  const [isCandidateModalOpen, setIsCandidateModalOpen] = useState(false);

  // New Candidate Form State
  const [first, setFirst] = useState('');
  const [last, setLast] = useState('');
  const [email, setEmail] = useState('');
  const [resumeText, setResumeText] = useState('');

  const loadJobs = async () => {
    try {
      const res = await api.get('/recruitment/jobs');
      setJobs(res.data);
      if (res.data.length > 0 && !selectedJobId) {
        setSelectedJobId(res.data[0].id);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const loadCandidates = async (jobId: string) => {
    if (!jobId) return;
    setLoading(true);
    try {
      const res = await api.get(`/recruitment/candidates?job_id=${jobId}`);
      setCandidates(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadJobs();
  }, []);

  useEffect(() => {
    if (selectedJobId) {
      loadCandidates(selectedJobId);
    }
  }, [selectedJobId]);

  const handleStageAdvance = async (candidateId: string, currentStage: string) => {
    const currentIndex = STAGES.findIndex((s) => s.id === currentStage);
    if (currentIndex < STAGES.length - 1) {
      const nextStage = STAGES[currentIndex + 1].id;
      try {
        await api.put(`/recruitment/candidates/${candidateId}/stage`, {
          pipeline_stage: nextStage,
          notes: `Advanced to ${nextStage} stage.`,
        });
        loadCandidates(selectedJobId);
      } catch (err) {
        console.error(err);
      }
    }
  };

  const handleCreateCandidate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedJobId) return;
    try {
      await api.post('/recruitment/candidates', {
        job_requisition_id: selectedJobId,
        first_name: first,
        last_name: last,
        email: email,
        raw_resume_text: resumeText,
        pipeline_stage: 'APPLIED',
      });
      setIsCandidateModalOpen(false);
      setFirst('');
      setLast('');
      setEmail('');
      setResumeText('');
      loadCandidates(selectedJobId);
    } catch (err: any) {
      alert(err.response?.data?.detail || 'Failed to add candidate');
    }
  };

  return (
    <div className="space-y-6">
      {/* Top Bar */}
      <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">Recruitment Pipeline & AI Matcher</h2>
          <p className="text-xs text-slate-500">
            Automated resume skill extraction, intelligent match scoring, and candidate stage management.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <select
            value={selectedJobId}
            onChange={(e) => setSelectedJobId(e.target.value)}
            className="bg-white border border-slate-200 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500/20"
          >
            {jobs.map((j) => (
              <option key={j.id} value={j.id}>
                {j.title} ({j.code})
              </option>
            ))}
          </select>

          <button
            onClick={() => setIsCandidateModalOpen(true)}
            className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm shadow-blue-500/20 flex-shrink-0"
          >
            <Plus className="w-4 h-4" />
            <span>Add Candidate</span>
          </button>
        </div>
      </div>

      {/* Kanban Board Columns */}
      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-4 overflow-x-auto pb-4">
        {STAGES.map((stage) => {
          const stageCandidates = candidates.filter((c) => c.pipeline_stage === stage.id);
          return (
            <div
              key={stage.id}
              className="bg-slate-100/70 rounded-2xl p-3 border border-slate-200/80 flex flex-col min-w-[220px]"
            >
              {/* Column Header */}
              <div className="flex items-center justify-between pb-2 mb-3 border-b border-slate-200 px-1">
                <span className="text-xs font-bold text-slate-800">{stage.name}</span>
                <span className="w-5 h-5 rounded-full bg-white text-slate-600 font-bold text-[10px] flex items-center justify-center border border-slate-200">
                  {stageCandidates.length}
                </span>
              </div>

              {/* Candidate Cards */}
              <div className="space-y-3 flex-1 overflow-y-auto max-h-[600px]">
                {stageCandidates.map((c) => (
                  <div
                    key={c.id}
                    className="bg-white rounded-xl p-3 border border-slate-200 shadow-2xs hover:shadow-sm transition-all space-y-2"
                  >
                    <div className="flex items-start justify-between">
                      <div>
                        <div className="text-xs font-bold text-slate-900 leading-tight">
                          {c.first_name} {c.last_name}
                        </div>
                        <div className="text-[10px] text-slate-400 truncate">{c.email}</div>
                      </div>
                      <div className="px-2 py-0.5 rounded-md bg-blue-50 border border-blue-200 text-blue-700 text-[10px] font-bold flex items-center gap-0.5">
                        <Sparkles className="w-2.5 h-2.5" />
                        {Math.round(c.match_score)}%
                      </div>
                    </div>

                    {/* Extracted Skills Badges */}
                    {c.extracted_skills && c.extracted_skills.length > 0 && (
                      <div className="flex flex-wrap gap-1">
                        {c.extracted_skills.slice(0, 3).map((sk, idx) => (
                          <span
                            key={idx}
                            className="px-1.5 py-0.5 rounded bg-slate-50 text-[9px] font-medium text-slate-600 border border-slate-200"
                          >
                            {sk}
                          </span>
                        ))}
                      </div>
                    )}

                    {/* Advance Action */}
                    <div className="pt-2 border-t border-slate-100 flex justify-end">
                      <button
                        onClick={() => handleStageAdvance(c.id, c.pipeline_stage)}
                        className="text-[10px] font-bold text-blue-600 hover:text-blue-800 flex items-center gap-1"
                      >
                        <span>Advance</span>
                        <ArrowRight className="w-3 h-3" />
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>

      {/* Add Candidate & Resume Parser Modal */}
      {isCandidateModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs">
          <div className="bg-white rounded-2xl shadow-2xl w-full max-w-lg p-6 border border-slate-200 space-y-4">
            <div className="flex items-center justify-between pb-3 border-b border-slate-100">
              <div className="flex items-center gap-2">
                <Sparkles className="w-4 h-4 text-blue-600" />
                <h3 className="font-bold text-sm text-slate-900">Add Candidate & AI Resume Screening</h3>
              </div>
              <button onClick={() => setIsCandidateModalOpen(false)} className="text-slate-400 hover:text-slate-600">
                <X className="w-4 h-4" />
              </button>
            </div>

            <form onSubmit={handleCreateCandidate} className="space-y-3">
              <div className="grid grid-cols-2 gap-2">
                <div>
                  <label className="block text-[11px] font-semibold text-slate-700 mb-1">First Name</label>
                  <input
                    type="text"
                    required
                    value={first}
                    onChange={(e) => setFirst(e.target.value)}
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                  />
                </div>
                <div>
                  <label className="block text-[11px] font-semibold text-slate-700 mb-1">Last Name</label>
                  <input
                    type="text"
                    required
                    value={last}
                    onChange={(e) => setLast(e.target.value)}
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                  />
                </div>
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-700 mb-1">Candidate Email</label>
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                />
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-700 mb-1">
                  Paste Resume / CV Text (for AI Matcher)
                </label>
                <textarea
                  rows={5}
                  value={resumeText}
                  onChange={(e) => setResumeText(e.target.value)}
                  placeholder="Paste text from candidate resume..."
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 text-xs focus:outline-none focus:ring-2 focus:ring-blue-500/20"
                />
              </div>

              <div className="pt-3 border-t border-slate-100 flex justify-end gap-2">
                <button
                  type="button"
                  onClick={() => setIsCandidateModalOpen(false)}
                  className="px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5"
                >
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Parse & Submit</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
