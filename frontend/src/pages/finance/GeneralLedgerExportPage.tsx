import React, { useState } from 'react';
import { Landmark, Download, FileSpreadsheet, CheckCircle2, ShieldCheck, ArrowRight, DollarSign } from 'lucide-react';
import { useExportData } from '../../hooks/useTableSort';

export const GeneralLedgerExportPage: React.FC = () => {
  const { exportToCSV } = useExportData();

  const journalEntries = [
    { account: '50100', name: 'Salaries & Wages Expense', type: 'DEBIT', dept: 'Engineering', debit: 645000, credit: 0 },
    { account: '50100', name: 'Salaries & Wages Expense', type: 'DEBIT', dept: 'Product', debit: 185000, credit: 0 },
    { account: '50100', name: 'Salaries & Wages Expense', type: 'DEBIT', dept: 'Sales', debit: 290000, credit: 0 },
    { account: '50200', name: 'Employer FICA Tax Expense', type: 'DEBIT', dept: 'Corporate', debit: 85680, credit: 0 },
    { account: '50300', name: '401(k) Employer Match Expense', type: 'DEBIT', dept: 'Corporate', debit: 44800, credit: 0 },
    { account: '50310', name: 'Company Healthcare Subsidy', type: 'DEBIT', dept: 'Corporate', debit: 112500, credit: 0 },
    { account: '20100', name: 'Federal Withholding Tax Payable', type: 'CREDIT', dept: 'Corporate', debit: 0, credit: 245000 },
    { account: '20110', name: 'State Withholding Tax Payable', type: 'CREDIT', dept: 'Corporate', debit: 0, credit: 98500 },
    { account: '20120', name: 'FICA Tax Payable (Total)', type: 'CREDIT', dept: 'Corporate', debit: 0, credit: 171360 },
    { account: '20200', name: '401(k) Contributions Payable', type: 'CREDIT', dept: 'Corporate', debit: 0, credit: 89600 },
    { account: '10110', name: 'Payroll Cash Clearing Account', type: 'CREDIT', dept: 'Treasury', debit: 0, credit: 758520 },
  ];

  const totalDebits = journalEntries.reduce((acc, l) => acc + l.debit, 0);
  const totalCredits = journalEntries.reduce((acc, l) => acc + l.credit, 0);
  const isBalanced = totalDebits === totalCredits;

  const handleExport = () => {
    exportToCSV('Payroll_GL_Journal_Voucher_2026', journalEntries);
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">ERP General Ledger Payroll Accounting</h2>
          <p className="text-xs text-slate-500">
            Balanced double-entry journal vouchers for SAP S/4HANA, NetSuite, and Workday ERP synchronization.
          </p>
        </div>
        <button
          onClick={handleExport}
          className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm shadow-blue-500/20"
        >
          <Download className="w-4 h-4" />
          <span>Export ERP CSV Voucher</span>
        </button>
      </div>

      {/* Balance Verification Card */}
      <div className={`p-6 rounded-2xl border flex items-center justify-between ${
        isBalanced ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : 'bg-rose-50 border-rose-200 text-rose-900'
      }`}>
        <div className="flex items-center gap-3">
          <div className={`w-10 h-10 rounded-xl flex items-center justify-center ${
            isBalanced ? 'bg-emerald-600 text-white' : 'bg-rose-600 text-white'
          }`}>
            <CheckCircle2 className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-bold text-sm">
              {isBalanced ? 'Journal Voucher Perfectly Balanced' : 'Accounting Out of Balance'}
            </h3>
            <p className="text-xs opacity-80">
              Total Debits: ${totalDebits.toLocaleString()} | Total Credits: ${totalCredits.toLocaleString()}
            </p>
          </div>
        </div>
        <span className="px-3 py-1 rounded-full text-xs font-black bg-white/80 border border-emerald-300">
          DELTA: $0.00
        </span>
      </div>

      {/* Journal Lines Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Double-Entry Journal Lines</h3>
          <span className="text-xs text-slate-500 font-medium">{journalEntries.length} line items</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Account Code</th>
                <th className="py-3 px-4">Account Description</th>
                <th className="py-3 px-4">Cost Center / Dept</th>
                <th className="py-3 px-4 text-right">Debit (USD)</th>
                <th className="py-3 px-4 text-right">Credit (USD)</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {journalEntries.map((l, i) => (
                <tr key={i} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3 px-4 font-mono font-bold text-slate-900">{l.account}</td>
                  <td className="py-3 px-4 font-medium text-slate-800">{l.name}</td>
                  <td className="py-3 px-4 text-slate-500">{l.dept}</td>
                  <td className="py-3 px-4 text-right font-mono font-bold text-slate-900">
                    {l.debit > 0 ? `$${l.debit.toLocaleString()}` : '-'}
                  </td>
                  <td className="py-3 px-4 text-right font-mono font-bold text-slate-900">
                    {l.credit > 0 ? `$${l.credit.toLocaleString()}` : '-'}
                  </td>
                </tr>
              ))}
            </tbody>
            <tfoot className="bg-slate-50 border-t border-slate-200 font-bold text-slate-900">
              <tr>
                <td colSpan={3} className="py-3 px-4 uppercase text-[11px]">Total Voucher Balance</td>
                <td className="py-3 px-4 text-right font-mono">${totalDebits.toLocaleString()}</td>
                <td className="py-3 px-4 text-right font-mono">${totalCredits.toLocaleString()}</td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>
    </div>
  );
};
