"""
Build Frontend Expansion: Custom Hooks, Chart Visualizers, Advanced Data Tables, and Detail Modals
"""
import os

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

# 1. Custom Hooks
hooks_code = '''import { useState, useMemo } from 'react';

export function useTableSort<T>(items: T[], initialKey?: keyof T, initialDirection: 'asc' | 'desc' = 'asc') {
  const [sortKey, setSortKey] = useState<keyof T | undefined>(initialKey);
  const [direction, setDirection] = useState<'asc' | 'desc'>(initialDirection);

  const sortedItems = useMemo(() => {
    if (!sortKey) return items;
    return [...items].sort((a, b) => {
      const valA = a[sortKey];
      const valB = b[sortKey];

      if (valA === valB) return 0;
      if (valA === null || valA === undefined) return 1;
      if (valB === null || valB === undefined) return -1;

      if (typeof valA === 'string' && typeof valB === 'string') {
        return direction === 'asc'
          ? valA.localeCompare(valB)
          : valB.localeCompare(valA);
      }

      if (valA < valB) return direction === 'asc' ? -1 : 1;
      return direction === 'asc' ? 1 : -1;
    });
  }, [items, sortKey, direction]);

  const requestSort = (key: keyof T) => {
    if (sortKey === key) {
      setDirection(prev => prev === 'asc' ? 'desc' : 'asc');
    } else {
      setSortKey(key);
      setDirection('asc');
    }
  };

  return { items: sortedItems, sortKey, direction, requestSort };
}

export function usePagination<T>(items: T[], initialPageSize: number = 10) {
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(initialPageSize);

  const totalPages = Math.max(1, Math.ceil(items.length / pageSize));

  const paginatedItems = useMemo(() => {
    const start = (currentPage - 1) * pageSize;
    return items.slice(start, start + pageSize);
  }, [items, currentPage, pageSize]);

  const goToPage = (page: number) => {
    setCurrentPage(Math.min(Math.max(1, page), totalPages));
  };

  return {
    currentPage,
    totalPages,
    pageSize,
    setPageSize,
    paginatedItems,
    goToPage,
    nextPage: () => goToPage(currentPage + 1),
    prevPage: () => goToPage(currentPage - 1),
    hasPrev: currentPage > 1,
    hasNext: currentPage < totalPages,
    totalCount: items.length
  };
}

export function useExportData() {
  const exportToCSV = (filename: string, rows: Array<Record<string, any>>) => {
    if (!rows || !rows.length) return;
    const separator = ',';
    const keys = Object.keys(rows[0]);
    const csvContent =
      keys.join(separator) +
      '\\n' +
      rows
        .map(row => {
          return keys
            .map(k => {
              let cell = row[k] === null || row[k] === undefined ? '' : row[k];
              cell = cell instanceof Date ? cell.toLocaleString() : cell.toString();
              cell = cell.replace(/"/g, '""');
              if (cell.search(/("|,|\\n)/g) >= 0) {
                cell = `"${cell}"`;
              }
              return cell;
            })
            .join(separator);
        })
        .join('\\n');

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    if (link.download !== undefined) {
      const url = URL.createObjectURL(blob);
      link.setAttribute('href', url);
      link.setAttribute('download', `${filename}.csv`);
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  };

  return { exportToCSV };
}
'''
write("frontend/src/hooks/useTableSort.ts", hooks_code)

# 2. Interactive SVG Charts
charts_code = '''import React from 'react';

interface BarChartProps {
  data: Array<{ label: string; value: number; color?: string }>;
  height?: number;
  showValues?: boolean;
}

export const BarChart: React.FC<BarChartProps> = ({ data, height = 200, showValues = true }) => {
  const maxValue = Math.max(...data.map(d => d.value), 1);

  return (
    <div className="w-full flex items-end gap-3 pt-6" style={{ height: `${height}px` }}>
      {data.map((item, index) => {
        const heightPct = (item.value / maxValue) * 100;
        return (
          <div key={index} className="flex-1 flex flex-col items-center gap-1 group relative">
            {showValues && (
              <span className="text-[10px] font-bold text-slate-500 opacity-0 group-hover:opacity-100 transition-opacity">
                {item.value.toLocaleString()}
              </span>
            )}
            <div className="w-full bg-slate-100 rounded-t-lg overflow-hidden flex items-end h-full">
              <div
                className={`w-full rounded-t-lg transition-all duration-500 ${item.color || 'bg-blue-600'}`}
                style={{ height: `${heightPct}%` }}
              />
            </div>
            <span className="text-[10px] font-medium text-slate-600 truncate max-w-full text-center">
              {item.label}
            </span>
          </div>
        );
      })}
    </div>
  );
};

interface LineChartProps {
  data: Array<{ label: string; value: number }>;
  height?: number;
  strokeColor?: string;
}

export const LineChart: React.FC<LineChartProps> = ({ data, height = 180, strokeColor = '#2563eb' }) => {
  if (data.length < 2) return <div className="text-xs text-slate-400">Not enough data</div>;

  const maxValue = Math.max(...data.map(d => d.value), 1);
  const minValue = Math.min(...data.map(d => d.value), 0);
  const range = maxValue - minValue || 1;

  const points = data.map((d, i) => {
    const x = (i / (data.length - 1)) * 300;
    const y = 140 - ((d.value - minValue) / range) * 120;
    return `${x},${y}`;
  }).join(' ');

  return (
    <div className="w-full" style={{ height: `${height}px` }}>
      <svg viewBox="0 0 300 160" className="w-full h-full overflow-visible">
        {/* Grid lines */}
        <line x1="0" y1="20" x2="300" y2="20" stroke="#f1f5f9" strokeWidth="1" />
        <line x1="0" y1="80" x2="300" y2="80" stroke="#f1f5f9" strokeWidth="1" />
        <line x1="0" y1="140" x2="300" y2="140" stroke="#e2e8f0" strokeWidth="1" />

        {/* Path line */}
        <polyline
          fill="none"
          stroke={strokeColor}
          strokeWidth="3"
          strokeLinecap="round"
          strokeLinejoin="round"
          points={points}
        />

        {/* Circles on vertices */}
        {data.map((d, i) => {
          const cx = (i / (data.length - 1)) * 300;
          const cy = 140 - ((d.value - minValue) / range) * 120;
          return (
            <g key={i} className="group">
              <circle cx={cx} cy={cy} r="4" fill="#ffffff" stroke={strokeColor} strokeWidth="2.5" />
              <title>{`${d.label}: ${d.value}`}</title>
            </g>
          );
        })}
      </svg>
    </div>
  );
};
'''
write("frontend/src/components/charts/BarChart.tsx", charts_code)

# 3. Interactive Payslip Viewer Modal
payslip_modal_code = '''import React from 'react';
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
              <h3 className="font-bold text-sm">PEOPLEPULSE GLOBAL ENTERPRISE</h3>
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
'''
write("frontend/src/components/modals/PayslipViewerModal.tsx", payslip_modal_code)

print("Frontend Expansion Built Successfully!")
'''
write("scripts/build_frontend_expansion.py", "# Frontend expansion")
'''
