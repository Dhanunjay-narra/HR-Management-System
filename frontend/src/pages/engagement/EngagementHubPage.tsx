import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import { Kudos, Employee } from '../../types';
import { HeartHandshake, Sparkles, Award, Plus, X, MessageCircle } from 'lucide-react';

export const EngagementHubPage: React.FC = () => {
  const [kudosList, setKudosList] = useState<Kudos[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const [receiverId, setReceiverId] = useState('');
  const [badgeType, setBadgeType] = useState('INNOVATION');
  const [message, setMessage] = useState('');

  const loadData = async () => {
    setLoading(true);
    try {
      const [kudosRes, empRes] = await Promise.all([
        api.get('/engagement/kudos/wall'),
        api.get('/employees'),
      ]);
      setKudosList(kudosRes.data);
      setEmployees(empRes.data);
      if (empRes.data.length > 0) {
        setReceiverId(empRes.data[0].id);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleSendKudos = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/engagement/kudos', {
        receiver_employee_id: receiverId,
        badge_type: badgeType,
        message,
        is_public: true,
      });
      setIsModalOpen(false);
      setMessage('');
      loadData();
    } catch (err: any) {
      alert(err.response?.data?.detail || 'Failed to send recognition kudos');
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">Employee Engagement & Kudos Wall</h2>
          <p className="text-xs text-slate-500">
            Celebrate peer achievements, recognize outstanding contributions, and foster corporate culture.
          </p>
        </div>

        <button
          onClick={() => setIsModalOpen(true)}
          className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm shadow-blue-500/20 flex-shrink-0"
        >
          <Award className="w-4 h-4" />
          <span>Give Recognition</span>
        </button>
      </div>

      {/* Kudos Feed Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {kudosList.map((k) => (
          <div
            key={k.id}
            className="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs hover:shadow-md transition-all space-y-3"
          >
            <div className="flex items-center justify-between">
              <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-indigo-50 text-indigo-700 border border-indigo-200 flex items-center gap-1">
                <Sparkles className="w-3 h-3" />
                {k.badge_type.replace('_', ' ')}
              </span>
              <span className="text-[10px] text-slate-400">{new Date(k.created_at).toLocaleDateString()}</span>
            </div>

            <p className="text-xs text-slate-700 italic font-serif leading-relaxed">
              "{k.message}"
            </p>

            <div className="pt-3 border-t border-slate-100 flex items-center justify-between text-[11px]">
              <div>
                <span className="text-slate-400">Awarded to </span>
                <span className="font-bold text-slate-900">{k.receiver_name || 'Valued Colleague'}</span>
              </div>
              <span className="text-slate-400 text-[10px]">by {k.sender_name || 'Team Member'}</span>
            </div>
          </div>
        ))}
      </div>

      {/* Send Kudos Modal */}
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs">
          <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md p-6 border border-slate-200 space-y-4">
            <div className="flex items-center justify-between pb-3 border-b border-slate-100">
              <h3 className="font-bold text-sm text-slate-900">Send Peer Kudos Recognition</h3>
              <button onClick={() => setIsModalOpen(false)} className="text-slate-400 hover:text-slate-600">
                <X className="w-4 h-4" />
              </button>
            </div>

            <form onSubmit={handleSendKudos} className="space-y-3">
              <div>
                <label className="block text-[11px] font-semibold text-slate-700 mb-1">Select Colleague</label>
                <select
                  value={receiverId}
                  onChange={(e) => setReceiverId(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                >
                  {employees.map((e) => (
                    <option key={e.id} value={e.id}>
                      {e.first_name} {e.last_name} ({e.work_email})
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-700 mb-1">Badge Type</label>
                <select
                  value={badgeType}
                  onChange={(e) => setBadgeType(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                >
                  <option value="INNOVATION">Innovation & Technical Excellence</option>
                  <option value="TEAM_PLAYER">Team Player & Collaboration</option>
                  <option value="LEADERSHIP">Mentorship & Leadership</option>
                  <option value="CUSTOMER_CHAMPION">Customer First Champion</option>
                </select>
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-700 mb-1">Recognition Message</label>
                <textarea
                  rows={4}
                  required
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  placeholder="Express why their work made a difference..."
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 text-xs focus:outline-none"
                />
              </div>

              <div className="pt-3 border-t border-slate-100 flex justify-end gap-2">
                <button
                  type="button"
                  onClick={() => setIsModalOpen(false)}
                  className="px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold"
                >
                  Post to Wall
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
