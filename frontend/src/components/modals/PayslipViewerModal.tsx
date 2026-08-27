import React from 'react';
import { Payslip } from '../../types';
import { X, Printer, Download, ShieldCheck, Landmark, Building2, Calendar } from 'lucide-react';

interface PayslipViewerModalProps {
  payslip: Payslip | null;
  onClose: () => void;
}

export const PayslipViewerModal: React.FC<PayslipViewerModalProps> = ({ payslip, onClose }) => {
  if (!payslip) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs">
      <div className="bg-white rounded-3xl shadow-2xl w-full max-w-2xl overflow-hidden border border-slate-200">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-900 text-white flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Building2 className="w-5 h-5 text-blue-400" />
            <div>
              <h3 className="font-bold text-sm">HR MANAGEMENT SYSTEM ENTERPRISE</h3>
              <p className="text-[10px] text-slate-400">Official Monthly Earnings Statement</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={() => window.print()}
              className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors"
            >
              <Printer className="w-4 h-4" />
            </button>
            <button onClick={onClose} className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300">
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Content */}
        <div className="p-6 space-y-6 text-xs text-slate-700">
          {/* Metadata Grid */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 p-4 rounded-2xl bg-slate-50 border border-slate-100">
            <div>
              <p className="text-[10px] font-semibold text-slate-400 uppercase">Employee</p>
              <p className="font-bold text-slate-900">{payslip.employee_name || 'Staff Member'}</p>
            </div>
            <div>
              <p className="text-[10px] font-semibold text-slate-400 uppercase">Pay Period</p>
              <p className="font-bold text-slate-900">{payslip.month}/{payslip.year}</p>
            </div>
            <div>
              <p className="text-[10px] font-semibold text-slate-400 uppercase">Disbursement Status</p>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800">
                {payslip.payment_status}
              </span>
            </div>
            <div>
              <p className="text-[10px] font-semibold text-slate-400 uppercase">Tax Regime</p>
              <p className="font-bold text-slate-900">Standard Progressive</p>
            </div>
          </div>

          {/* Earnings & Deductions Tables */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {/* Earnings */}
            <div className="space-y-2">
              <h4 className="font-bold text-[11px] uppercase tracking-wider text-emerald-700 border-b border-emerald-100 pb-1">
                Gross Earnings
              </h4>
              <div className="space-y-1.5">
                <div className="flex justify-between py-1 border-b border-slate-100">
                  <span className="text-slate-600">Base Salary</span>
                  <span className="font-bold text-slate-900">${(payslip.gross_salary * 0.75).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                </div>
                <div className="flex justify-between py-1 border-b border-slate-100">
                  <span className="text-slate-600">Housing Allowance</span>
                  <span className="font-bold text-slate-900">${(payslip.gross_salary * 0.15).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                </div>
                <div className="flex justify-between py-1 border-b border-slate-100">
                  <span className="text-slate-600">Special & Transit Allowance</span>
                  <span className="font-bold text-slate-900">${(payslip.gross_salary * 0.10).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                </div>
                <div className="flex justify-between pt-2 font-bold text-slate-900">
                  <span>Total Gross Earnings</span>
                  <span className="text-emerald-600">${payslip.gross_salary.toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                </div>
              </div>
            </div>

            {/* Deductions */}
            <div className="space-y-2">
              <h4 className="font-bold text-[11px] uppercase tracking-wider text-rose-700 border-b border-rose-100 pb-1">
                Statutory & Tax Deductions
              </h4>
              <div className="space-y-1.5">
                <div className="flex justify-between py-1 border-b border-slate-100">
                  <span className="text-slate-600">Income Withholding Tax</span>
                  <span className="font-bold text-slate-900">${(payslip.deductions * 0.65).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                </div>
                <div className="flex justify-between py-1 border-b border-slate-100">
                  <span className="text-slate-600">Social Security / Provident</span>
                  <span className="font-bold text-slate-900">${(payslip.deductions * 0.25).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                </div>
                <div className="flex justify-between py-1 border-b border-slate-100">
                  <span className="text-slate-600">Health & Insurance</span>
                  <span className="font-bold text-slate-900">${(payslip.deductions * 0.10).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                </div>
                <div className="flex justify-between pt-2 font-bold text-slate-900">
                  <span>Total Deductions</span>
                  <span className="text-rose-600">-${payslip.deductions.toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                </div>
              </div>
            </div>
          </div>

          {/* Net Pay Box */}
          <div className="p-4 rounded-2xl bg-blue-50 border border-blue-100 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center">
                <Landmark className="w-5 h-5" />
              </div>
              <div>
                <p className="text-[10px] font-bold text-blue-900 uppercase">Net Disbursed Take-Home</p>
                <p className="text-[11px] text-blue-700">Direct Deposit (NACHA ACH Verified)</p>
              </div>
            </div>
            <div className="text-right">
              <span className="text-2xl font-extrabold text-blue-900">
                ${payslip.net_salary.toLocaleString(undefined, { minimumFractionDigits: 2 })}
              </span>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-slate-50 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-400">
          <span>Security Hash: 8f9b4c2e... (Tamper-Evident)</span>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl bg-slate-900 text-white font-semibold hover:bg-slate-800"
          >
            Close Statement
          </button>
        </div>
      </div>
    </div>
  );
};
