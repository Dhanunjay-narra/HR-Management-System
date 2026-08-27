import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import { Employee, Employee360Profile } from '../../types';
import {
  Users,
  Search,
  Plus,
  Mail,
  Building,
  Shield,
  Clock,
  Calendar,
  X,
  History,
  CheckCircle,
  Briefcase
} from 'lucide-react';

export const EmployeeDirectory: React.FC = () => {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [selectedEmployeeId, setSelectedEmployeeId] = useState<string | null>(null);
  const [profile360, setProfile360] = useState<Employee360Profile | null>(null);
  const [loadingProfile, setLoadingProfile] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);

  // New Employee Form State
  const [formCode, setFormCode] = useState('');
  const [formFirst, setFormFirst] = useState('');
  const [formLast, setFormLast] = useState('');
  const [formEmail, setFormEmail] = useState('');
  const [formType, setFormType] = useState('FULL_TIME');

  const loadEmployees = async () => {
    setLoading(true);
    try {
      const res = await api.get('/employees');
      setEmployees(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadEmployees();
  }, []);

  const open360View = async (empId: string) => {
    setSelectedEmployeeId(empId);
    setLoadingProfile(true);
    try {
      const res = await api.get(`/employees/${empId}/360`);
      setProfile360(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoadingProfile(false);
    }
  };

  const handleCreateEmployee = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/employees', {
        employee_code: formCode || `EMP-${Math.floor(1000 + Math.random() * 9000)}`,
        first_name: formFirst,
        last_name: formLast,
        work_email: formEmail,
        employment_type: formType,
        status: 'ACTIVE',
        create_user_account: true,
      });
      setIsModalOpen(false);
      setFormFirst('');
      setFormLast('');
      setFormEmail('');
      setFormCode('');
      loadEmployees();
    } catch (err: any) {
      alert(err.response?.data?.detail || 'Failed to create employee');
    }
  };

  const filtered = employees.filter((e) =>
    `${e.first_name} ${e.last_name} ${e.employee_code} ${e.work_email}`
      .toLowerCase()
      .includes(search.toLowerCase())
  );

  return (
    <div className="space-y-6">
      {/* Top action bar */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">Employee Directory & 360 CRM</h2>
          <p className="text-xs text-slate-500">
            Comprehensive profile records, historical timeline events, and reporting chains.
          </p>
        </div>

        <div className="flex items-center gap-3 w-full sm:w-auto">
          <div className="relative flex-1 sm:w-64">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search by name, code, or email..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full bg-white border border-slate-200 rounded-xl pl-9 pr-4 py-2 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500"
            />
          </div>

          <button
            onClick={() => setIsModalOpen(true)}
            className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm shadow-blue-500/20 flex-shrink-0"
          >
            <Plus className="w-4 h-4" />
            <span>Add Employee</span>
          </button>
        </div>
      </div>

      {/* Grid of Employee Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filtered.map((emp) => (
          <div
            key={emp.id}
            onClick={() => open360View(emp.id)}
            className="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs hover:shadow-md hover:border-blue-300 transition-all cursor-pointer space-y-4"
          >
            <div className="flex items-start justify-between">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 text-white flex items-center justify-center font-bold text-sm shadow-xs">
                  {emp.first_name[0]}
                  {emp.last_name[0]}
                </div>
                <div>
                  <h4 className="text-xs font-bold text-slate-900 leading-tight">
                    {emp.first_name} {emp.last_name}
                  </h4>
                  <span className="text-[11px] text-slate-500 font-mono">{emp.employee_code}</span>
                </div>
              </div>
              <span className="px-2.5 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200">
                {emp.status}
              </span>
            </div>

            <div className="space-y-1.5 text-[11px] text-slate-600">
              <div className="flex items-center gap-2">
                <Mail className="w-3.5 h-3.5 text-slate-400" />
                <span className="truncate">{emp.work_email}</span>
              </div>
              <div className="flex items-center gap-2">
                <Building className="w-3.5 h-3.5 text-slate-400" />
                <span>{emp.department_name || 'Engineering'}</span>
              </div>
              <div className="flex items-center gap-2">
                <Briefcase className="w-3.5 h-3.5 text-slate-400" />
                <span>{emp.designation_title || 'Software Engineer'}</span>
              </div>
            </div>

            <div className="pt-3 border-t border-slate-100 flex items-center justify-between text-[11px]">
              <span className="text-slate-400 font-medium">{emp.employment_type.replace('_', ' ')}</span>
              <span className="text-blue-600 font-semibold hover:underline flex items-center gap-1">
                View 360 CRM &rarr;
              </span>
            </div>
          </div>
        ))}
      </div>

      {/* 360 CRM Slide-over Drawer */}
      {selectedEmployeeId && (
        <div className="fixed inset-0 z-50 flex justify-end bg-slate-900/40 backdrop-blur-xs animate-in fade-in">
          <div className="w-full max-w-xl bg-white h-full shadow-2xl overflow-y-auto p-6 space-y-6 border-l border-slate-200">
            <div className="flex items-center justify-between pb-4 border-b border-slate-200">
              <div className="flex items-center gap-2">
                <Shield className="w-5 h-5 text-blue-600" />
                <h3 className="font-bold text-base text-slate-900">Employee 360 CRM</h3>
              </div>
              <button
                onClick={() => setSelectedEmployeeId(null)}
                className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {loadingProfile ? (
              <div className="text-center py-12 text-xs text-slate-400">Loading 360 profile intelligence...</div>
            ) : profile360 ? (
              <div className="space-y-6">
                {/* Employee Header */}
                <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex items-center gap-4">
                  <div className="w-12 h-12 rounded-2xl bg-blue-600 text-white flex items-center justify-center font-bold text-base shadow-sm">
                    {profile360.employee.first_name[0]}
                    {profile360.employee.last_name[0]}
                  </div>
                  <div>
                    <h4 className="font-bold text-sm text-slate-900">{profile360.employee.full_name}</h4>
                    <p className="text-xs text-slate-500 font-mono">{profile360.employee.employee_code} • {profile360.employee.work_email}</p>
                  </div>
                </div>

                {/* Attendance & Leave Quick Stats */}
                <div className="grid grid-cols-2 gap-3">
                  <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                    <span className="text-[11px] font-medium text-slate-500">Attendance Rate</span>
                    <div className="text-lg font-bold text-slate-900">{profile360.attendance_summary.attendance_rate}%</div>
                    <span className="text-[10px] text-slate-400">{profile360.attendance_summary.present_days} present days</span>
                  </div>

                  <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                    <span className="text-[11px] font-medium text-slate-500">Annual Leave Balance</span>
                    <div className="text-lg font-bold text-blue-600">
                      {profile360.leave_balances[0]?.remaining_days ?? 18} Days
                    </div>
                    <span className="text-[10px] text-slate-400">Remaining for 2026</span>
                  </div>
                </div>

                {/* Timeline History */}
                <div className="space-y-3">
                  <div className="flex items-center gap-2 text-xs font-bold text-slate-900">
                    <History className="w-4 h-4 text-blue-600" />
                    <span>Historical Lifecycle Timeline</span>
                  </div>

                  <div className="space-y-2 border-l-2 border-slate-200 pl-4 ml-2">
                    {profile360.recent_timeline_events.map((t) => (
                      <div key={t.id} className="relative pb-3 space-y-0.5">
                        <div className="absolute -left-[21px] top-1 w-2.5 h-2.5 rounded-full bg-blue-600 ring-4 ring-white" />
                        <div className="text-xs font-semibold text-slate-900">{t.title}</div>
                        {t.description && <p className="text-[11px] text-slate-500">{t.description}</p>}
                        <span className="text-[10px] text-slate-400 block">{new Date(t.created_at).toLocaleDateString()}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            ) : null}
          </div>
        </div>
      )}

      {/* Add Employee Modal */}
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs">
          <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md p-6 border border-slate-200 space-y-4">
            <div className="flex items-center justify-between pb-3 border-b border-slate-100">
              <h3 className="font-bold text-sm text-slate-900">Add New Employee</h3>
              <button onClick={() => setIsModalOpen(false)} className="text-slate-400 hover:text-slate-600">
                <X className="w-4 h-4" />
              </button>
            </div>

            <form onSubmit={handleCreateEmployee} className="space-y-3">
              <div className="grid grid-cols-2 gap-2">
                <div>
                  <label className="block text-[11px] font-semibold text-slate-700 mb-1">First Name</label>
                  <input
                    type="text"
                    required
                    value={formFirst}
                    onChange={(e) => setFormFirst(e.target.value)}
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                  />
                </div>
                <div>
                  <label className="block text-[11px] font-semibold text-slate-700 mb-1">Last Name</label>
                  <input
                    type="text"
                    required
                    value={formLast}
                    onChange={(e) => setFormLast(e.target.value)}
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                  />
                </div>
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-700 mb-1">Work Email</label>
                <input
                  type="email"
                  required
                  value={formEmail}
                  onChange={(e) => setFormEmail(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                />
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-700 mb-1">Employee Code</label>
                <input
                  type="text"
                  placeholder="e.g. EMP-2048"
                  value={formCode}
                  onChange={(e) => setFormCode(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                />
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-700 mb-1">Employment Type</label>
                <select
                  value={formType}
                  onChange={(e) => setFormType(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs"
                >
                  <option value="FULL_TIME">Full Time</option>
                  <option value="PART_TIME">Part Time</option>
                  <option value="CONTRACTOR">Contractor</option>
                  <option value="INTERN">Intern</option>
                </select>
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
                  Create Record
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
