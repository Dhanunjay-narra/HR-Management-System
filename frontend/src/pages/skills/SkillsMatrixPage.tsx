import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import { Employee, SkillGapAnalysis } from '../../types';
import {
  Sparkles,
  Award,
  BookOpen,
  CheckCircle2,
  AlertCircle,
  TrendingUp,
  ArrowRight
} from 'lucide-react';

export const SkillsMatrixPage: React.FC = () => {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [selectedEmpId, setSelectedEmpId] = useState<string>('');
  const [gapAnalysis, setGapAnalysis] = useState<SkillGapAnalysis | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const loadEmps = async () => {
      try {
        const res = await api.get('/employees');
        setEmployees(res.data);
        if (res.data.length > 0) {
          setSelectedEmpId(res.data[0].id);
        }
      } catch (err) {
        console.error(err);
      }
    };
    loadEmps();
  }, []);

  const runAnalysis = async (empId: string) => {
    if (!empId) return;
    setLoading(true);
    try {
      const res = await api.get(`/skills/employee/${empId}/gap-analysis`);
      setGapAnalysis(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (selectedEmpId) {
      runAnalysis(selectedEmpId);
    }
  }, [selectedEmpId]);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">Skills Intelligence & Gap Matrix</h2>
          <p className="text-xs text-slate-500">
            Compare employee proficiencies against job role requirements with personalized course recommendations.
          </p>
        </div>

        <select
          value={selectedEmpId}
          onChange={(e) => setSelectedEmpId(e.target.value)}
          className="bg-white border border-slate-200 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500/20"
        >
          {employees.map((e) => (
            <option key={e.id} value={e.id}>
              {e.first_name} {e.last_name} ({e.employee_code})
            </option>
          ))}
        </select>
      </div>

      {loading ? (
        <div className="py-12 text-center text-xs text-slate-400">Evaluating skill gap matrix...</div>
      ) : gapAnalysis ? (
        <div className="space-y-6">
          {/* Readiness KPI Cards */}
          <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
            <div className="bg-white rounded-2xl p-5 border border-slate-200 shadow-xs space-y-1">
              <span className="text-xs font-medium text-slate-500">Role Readiness Score</span>
              <div className="text-2xl font-bold text-blue-600">{gapAnalysis.overall_readiness_score}%</div>
              <span className="text-[11px] text-slate-400">{gapAnalysis.designation_title || 'Software Engineer'}</span>
            </div>

            <div className="bg-white rounded-2xl p-5 border border-slate-200 shadow-xs space-y-1">
              <span className="text-xs font-medium text-slate-500">Skills Assessed</span>
              <div className="text-2xl font-bold text-slate-900">{gapAnalysis.skills_assessed_count}</div>
              <span className="text-[11px] text-slate-400">Total requirements</span>
            </div>

            <div className="bg-white rounded-2xl p-5 border border-slate-200 shadow-xs space-y-1">
              <span className="text-xs font-medium text-slate-500">Skills Met</span>
              <div className="text-2xl font-bold text-emerald-600">{gapAnalysis.skills_met_count}</div>
              <span className="text-[11px] text-slate-400">Proficiency satisfied</span>
            </div>

            <div className="bg-white rounded-2xl p-5 border border-slate-200 shadow-xs space-y-1">
              <span className="text-xs font-medium text-slate-500">Skill Gaps</span>
              <div className="text-2xl font-bold text-amber-600">{gapAnalysis.skills_gap_count}</div>
              <span className="text-[11px] text-slate-400">Recommended for upskilling</span>
            </div>
          </div>

          {/* Gap Matrix Breakdown */}
          <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
            <div className="p-4 border-b border-slate-100">
              <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">
                Individual Skill Gap Matrix & Course Links
              </h3>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs text-slate-600">
                <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
                  <tr>
                    <th className="py-3 px-4">Skill Domain</th>
                    <th className="py-3 px-4">Category</th>
                    <th className="py-3 px-4">Current Level</th>
                    <th className="py-3 px-4">Required Level</th>
                    <th className="py-3 px-4">Gap Status</th>
                    <th className="py-3 px-4">Recommended Training</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {gapAnalysis.gap_matrix.map((g, idx) => (
                    <tr key={idx} className="hover:bg-slate-50/60 transition-colors">
                      <td className="py-3 px-4 font-bold text-slate-900">{g.skill_name}</td>
                      <td className="py-3 px-4">
                        <span className="px-2 py-0.5 rounded text-[10px] font-medium bg-slate-100 text-slate-700">
                          {g.category}
                        </span>
                      </td>
                      <td className="py-3 px-4 font-semibold text-slate-800">Level {g.current_proficiency} / 5</td>
                      <td className="py-3 px-4 font-semibold text-slate-800">Level {g.required_proficiency} / 5</td>
                      <td className="py-3 px-4">
                        {g.is_met ? (
                          <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200 flex items-center gap-1 w-fit">
                            <CheckCircle2 className="w-3 h-3" /> Met
                          </span>
                        ) : (
                          <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-amber-50 text-amber-700 border border-amber-200 flex items-center gap-1 w-fit">
                            <AlertCircle className="w-3 h-3" /> Gap (-{g.gap_level})
                          </span>
                        )}
                      </td>
                      <td className="py-3 px-4">
                        {g.recommended_course ? (
                          <div className="flex items-center gap-2">
                            <span className="font-semibold text-blue-600">{g.recommended_course.title}</span>
                            <span className="text-[10px] text-slate-400">({g.recommended_course.duration_hours} hrs)</span>
                          </div>
                        ) : (
                          <span className="text-slate-400">No training required</span>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      ) : null}
    </div>
  );
};
