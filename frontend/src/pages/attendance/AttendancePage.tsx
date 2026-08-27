import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import { AttendanceRecord } from '../../types';
import { Clock, CheckCircle2, AlertTriangle, ShieldCheck, MapPin, Play, Square } from 'lucide-react';

export const AttendancePage: React.FC = () => {
  const [records, setRecords] = useState<AttendanceRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [isClockedIn, setIsClockedIn] = useState(false);
  const [activeAttendanceId, setActiveAttendanceId] = useState<string | null>(null);

  const loadAttendance = async () => {
    setLoading(true);
    try {
      const res = await api.get('/attendance/records');
      setRecords(res.data);
      if (res.data.length > 0 && !res.data[0].clock_out) {
        setIsClockedIn(true);
        setActiveAttendanceId(res.data[0].id);
      } else {
        setIsClockedIn(false);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadAttendance();
  }, []);

  const handleClockIn = async () => {
    try {
      const res = await api.post('/attendance/clock-in', {
        latitude: 37.7749,
        longitude: -122.4194,
        source: 'WEB_PORTAL',
      });
      setIsClockedIn(true);
      setActiveAttendanceId(res.data.id);
      loadAttendance();
    } catch (err: any) {
      alert(err.response?.data?.detail || 'Clock-in failed');
    }
  };

  const handleClockOut = async () => {
    try {
      await api.post('/attendance/clock-out', {
        latitude: 37.7749,
        longitude: -122.4194,
      });
      setIsClockedIn(false);
      loadAttendance();
    } catch (err: any) {
      alert(err.response?.data?.detail || 'Clock-out failed');
    }
  };

  return (
    <div className="space-y-6">
      {/* Top Banner & Quick Clock-in Card */}
      <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-xs flex flex-col md:flex-row items-center justify-between gap-6">
        <div className="space-y-1 text-center md:text-left">
          <div className="flex items-center justify-center md:justify-start gap-2">
            <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-blue-50 text-blue-700 border border-blue-200">
              Shift Scheduling & Geofencing
            </span>
            <span className="text-xs text-slate-500 font-medium">Standard 9:00 AM - 6:00 PM</span>
          </div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">Time & Attendance Tracking</h2>
          <p className="text-xs text-slate-500 max-w-md">
            Biometric and browser GPS geofenced clocking with automated overtime, late deduction, and shift policy enforcement.
          </p>
        </div>

        {/* Action Button */}
        <div className="flex items-center gap-3">
          {isClockedIn ? (
            <button
              onClick={handleClockOut}
              className="px-6 py-3 rounded-2xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs flex items-center gap-2 shadow-lg shadow-rose-500/20 transition-all"
            >
              <Square className="w-4 h-4 fill-white" />
              <span>Clock Out of Shift</span>
            </button>
          ) : (
            <button
              onClick={handleClockIn}
              className="px-6 py-3 rounded-2xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs flex items-center gap-2 shadow-lg shadow-blue-500/20 transition-all"
            >
              <Play className="w-4 h-4 fill-white" />
              <span>Clock In (Geofenced GPS)</span>
            </button>
          )}
        </div>
      </div>

      {/* Attendance History Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Recent Attendance Records</h3>
          <span className="text-xs text-slate-500 font-medium">{records.length} shifts recorded</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Date</th>
                <th className="py-3 px-4">Clock In</th>
                <th className="py-3 px-4">Clock Out</th>
                <th className="py-3 px-4">Duration</th>
                <th className="py-3 px-4">Punctuality</th>
                <th className="py-3 px-4">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {records.map((r) => (
                <tr key={r.id} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3 px-4 font-semibold text-slate-900">{r.date}</td>
                  <td className="py-3 px-4 font-mono text-slate-600">
                    {r.clock_in ? new Date(r.clock_in).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : '-'}
                  </td>
                  <td className="py-3 px-4 font-mono text-slate-600">
                    {r.clock_out ? new Date(r.clock_out).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : 'Active'}
                  </td>
                  <td className="py-3 px-4 font-medium">{Math.round(r.total_work_minutes / 60 * 10) / 10} hrs</td>
                  <td className="py-3 px-4">
                    {r.is_late ? (
                      <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-50 text-amber-700 border border-amber-200">
                        Late Check-in
                      </span>
                    ) : (
                      <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                        On Time
                      </span>
                    )}
                  </td>
                  <td className="py-3 px-4">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-slate-100 text-slate-700">
                      {r.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
