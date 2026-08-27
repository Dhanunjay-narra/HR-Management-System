import React, { useState } from 'react';
import { Play, Plus, Zap, ArrowRight, CheckCircle2, ShieldCheck, Settings2, Trash2 } from 'lucide-react';

export const WorkflowVisualEditorPage: React.FC = () => {
  const [workflows, setWorkflows] = useState([
    { id: 'WF-01', name: 'Auto-Approve Low-Risk Expense Claims (<$50)', trigger: 'EXPENSE_SUBMITTED', condition: 'claim.amount <= 50.0 && claim.has_receipt == true', action: 'AUTO_APPROVE & NOTIFY_EMPLOYEE', status: 'ACTIVE' },
    { id: 'WF-02', name: 'Escalate Overdue Leave Approval (48h Timeout)', trigger: 'LEAVE_REQUEST_PENDING', condition: 'days_between(now(), leave.submitted_at) >= 2', action: 'ESCALATE_TO_SKIP_LEVEL_DIRECTOR', status: 'ACTIVE' },
    { id: 'WF-03', name: 'Trigger IT Deprovisioning on Separation Event', trigger: 'EMPLOYEE_TERMINATED', condition: 'employee.status == "OFFBOARDING"', action: 'REVOKE_OKTA_SSO & INITIATE_MDM_WIPE', status: 'ACTIVE' },
    { id: 'WF-04', name: 'Send Milestone Kudos on 1-Year Anniversary', trigger: 'TENURE_ANNIVERSARY', condition: 'employee.tenure_years >= 1.0', action: 'BROADCAST_KUDOS_WALL & AWARD_500_POINTS', status: 'ACTIVE' },
  ]);

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">Event-Driven Automation Workflow Engine</h2>
          <p className="text-xs text-slate-500">
            Configure automated Trigger-Condition-Action state machines across HR, Payroll, IT, and Approvals.
          </p>
        </div>
        <button className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm shadow-blue-500/20">
          <Plus className="w-4 h-4" />
          <span>Create New Workflow</span>
        </button>
      </div>

      <div className="grid grid-cols-1 gap-4">
        {workflows.map((wf) => (
          <div key={wf.id} className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-3">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="p-2 rounded-xl bg-blue-50 text-blue-600">
                  <Zap className="w-4 h-4" />
                </span>
                <div>
                  <h3 className="font-bold text-xs text-slate-900">{wf.name}</h3>
                  <p className="text-[10px] font-mono text-slate-400">{wf.id}</p>
                </div>
              </div>
              <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800">
                {wf.status}
              </span>
            </div>

            <div className="p-3 rounded-xl bg-slate-50 border border-slate-100 grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
              <div>
                <span className="text-[10px] font-bold text-slate-400 uppercase">Trigger Event</span>
                <p className="font-mono font-bold text-blue-700 mt-0.5">{wf.trigger}</p>
              </div>
              <div>
                <span className="text-[10px] font-bold text-slate-400 uppercase">Condition (DSL AST)</span>
                <p className="font-mono text-slate-800 mt-0.5 truncate">{wf.condition}</p>
              </div>
              <div>
                <span className="text-[10px] font-bold text-slate-400 uppercase">Automated Action</span>
                <p className="font-mono font-bold text-emerald-700 mt-0.5">{wf.action}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
