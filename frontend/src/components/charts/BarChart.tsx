import React from 'react';

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
