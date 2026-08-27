import React from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  Users,
  Network,
  Clock,
  CalendarCheck,
  UserPlus,
  Compass,
  Target,
  GraduationCap,
  Sparkles,
  LifeBuoy,
  HeartHandshake,
  DollarSign,
  Receipt,
  Monitor,
  FolderLock,
  Bot
} from 'lucide-react';

const navigation = [
  { name: 'Dashboard', href: '/', icon: LayoutDashboard },
  { name: 'Employees 360', href: '/employees', icon: Users },
  { name: 'Org Hierarchy', href: '/organization', icon: Network },
  { name: 'Attendance & Shifts', href: '/attendance', icon: Clock },
  { name: 'Leave & PTO', href: '/leave', icon: CalendarCheck },
  { name: 'Recruitment CRM', href: '/recruitment', icon: UserPlus },
  { name: 'Onboarding Journey', href: '/onboarding', icon: Compass },
  { name: 'Goals & OKRs', href: '/goals', icon: Target },
  { name: 'Skills Matrix', href: '/skills', icon: Sparkles },
  { name: 'Learning & LMS', href: '/learning', icon: GraduationCap },
  { name: 'HR Service Desk', href: '/service-desk', icon: LifeBuoy },
  { name: 'Engagement & Kudos', href: '/engagement', icon: HeartHandshake },
  { name: 'Payroll & Payslips', href: '/payroll', icon: DollarSign },
  { name: 'Expense Claims', href: '/expenses', icon: Receipt },
  { name: 'IT Asset Inventory', href: '/assets', icon: Monitor },
  { name: 'Document Vault', href: '/documents', icon: FolderLock },
];

export const Sidebar: React.FC = () => {
  return (
    <aside className="w-64 bg-slate-900 text-slate-300 flex flex-col flex-shrink-0 h-screen border-r border-slate-800 select-none">
      {/* Brand Header */}
      <div className="h-16 flex items-center px-6 gap-3 border-b border-slate-800/80 bg-slate-950/40">
        <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-500 flex items-center justify-center text-white shadow-lg shadow-blue-500/30">
          <Sparkles className="w-5 h-5" />
        </div>
        <div>
          <h1 className="font-bold text-sm text-white tracking-tight leading-none">
            HR Management System
          </h1>
          <span className="text-[10px] text-blue-400 font-medium uppercase tracking-wider">Enterprise Platform</span>
        </div>
      </div>

      {/* Navigation Links */}
      <div className="flex-1 overflow-y-auto py-4 px-3 space-y-1">
        <div className="px-3 py-1 text-[11px] font-semibold text-slate-400 uppercase tracking-wider">
          Modules
        </div>
        {navigation.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.name}
              to={item.href}
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2 text-xs font-medium rounded-lg transition-all duration-150 ${
                  isActive
                    ? 'bg-blue-600 text-white font-semibold shadow-sm'
                    : 'text-slate-400 hover:text-slate-100 hover:bg-slate-800/60'
                }`
              }
            >
              <Icon className="w-4 h-4 flex-shrink-0" />
              <span>{item.name}</span>
            </NavLink>
          );
        })}
      </div>

      {/* AI Assistant Quick Trigger */}
      <div className="p-3 border-t border-slate-800 bg-slate-950/30">
        <div className="bg-gradient-to-r from-blue-900/40 to-indigo-900/40 border border-blue-500/20 rounded-xl p-3">
          <div className="flex items-center gap-2 text-blue-300 text-xs font-semibold mb-1">
            <Bot className="w-4 h-4 text-blue-400" />
            Policy RAG Assistant
          </div>
          <p className="text-[11px] text-slate-400 mb-2">Instant answers to company policies and benefits.</p>
        </div>
      </div>
    </aside>
  );
};
