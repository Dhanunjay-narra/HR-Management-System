import React from 'react';
import { useAuth } from '../../context/AuthContext';
import { Bell, Search, LogOut, ShieldCheck, Sparkles } from 'lucide-react';

interface HeaderProps {
  onOpenAIModal: () => void;
}

export const Header: React.FC<HeaderProps> = ({ onOpenAIModal }) => {
  const { user, logout } = useAuth();

  return (
    <header className="h-16 bg-white border-b border-slate-200 px-6 flex items-center justify-between sticky top-0 z-30 shadow-xs">
      {/* Search Input & AI Shortcut */}
      <div className="flex items-center gap-4 flex-1 max-w-lg">
        <div className="relative w-full">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search employees, documents, requisitions, tickets..."
            className="w-full bg-slate-50 border border-slate-200 rounded-lg pl-9 pr-4 py-1.5 text-xs text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all"
          />
        </div>
        <button
          onClick={onOpenAIModal}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-blue-50 hover:bg-blue-100 text-blue-700 text-xs font-semibold border border-blue-200 shadow-xs transition-colors flex-shrink-0"
        >
          <Sparkles className="w-3.5 h-3.5 text-blue-600" />
          <span>Ask AI</span>
        </button>
      </div>

      {/* User Status & Profile */}
      <div className="flex items-center gap-4">
        {/* Live Notification Indicator */}
        <button className="relative p-2 rounded-lg text-slate-500 hover:text-slate-700 hover:bg-slate-100 transition-colors">
          <Bell className="w-4 h-4" />
          <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-blue-600 animate-pulse" />
        </button>

        <div className="h-6 w-px bg-slate-200" />

        {/* User Pill */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-600 text-white flex items-center justify-center font-bold text-xs shadow-xs">
            {user?.first_name ? user.first_name[0].toUpperCase() : 'U'}
          </div>
          <div className="hidden md:block text-left">
            <div className="text-xs font-semibold text-slate-900 leading-tight flex items-center gap-1">
              {user?.full_name || 'Admin User'}
              <ShieldCheck className="w-3.5 h-3.5 text-blue-600" />
            </div>
            <div className="text-[11px] text-slate-500 uppercase font-medium">
              {user?.role?.replace('_', ' ') || 'Super Administrator'}
            </div>
          </div>

          <button
            onClick={logout}
            title="Sign out"
            className="p-2 rounded-lg text-slate-400 hover:text-red-600 hover:bg-red-50 transition-colors ml-1"
          >
            <LogOut className="w-4 h-4" />
          </button>
        </div>
      </div>
    </header>
  );
};
