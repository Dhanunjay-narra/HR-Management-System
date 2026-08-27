import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import { Layout } from './components/layout/Layout';
import { Login } from './pages/auth/Login';
import { DashboardOverview } from './pages/dashboard/DashboardOverview';
import { EmployeeDirectory } from './pages/employees/EmployeeDirectory';
import { RecruitmentKanbanPage } from './pages/recruitment/RecruitmentKanbanPage';
import { AttendancePage } from './pages/attendance/AttendancePage';
import { LeaveManagementPage } from './pages/leave/LeaveManagementPage';
import { SkillsMatrixPage } from './pages/skills/SkillsMatrixPage';
import { PayrollDashboardPage } from './pages/payroll/PayrollDashboardPage';
import { ServiceDeskPage } from './pages/servicedesk/ServiceDeskPage';
import { EngagementHubPage } from './pages/engagement/EngagementHubPage';

const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isAuthenticated, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div className="h-screen flex items-center justify-center bg-slate-900 text-white font-sans text-xs">
        Loading HR Management System...
      </div>
    );
  }

  return isAuthenticated ? <>{children}</> : <Navigate to="/login" replace />;
};

export const App: React.FC = () => {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <Layout />
              </ProtectedRoute>
            }
          >
            <Route index element={<DashboardOverview />} />
            <Route path="employees" element={<EmployeeDirectory />} />
            <Route path="organization" element={<EmployeeDirectory />} />
            <Route path="recruitment" element={<RecruitmentKanbanPage />} />
            <Route path="onboarding" element={<RecruitmentKanbanPage />} />
            <Route path="attendance" element={<AttendancePage />} />
            <Route path="leave" element={<LeaveManagementPage />} />
            <Route path="goals" element={<SkillsMatrixPage />} />
            <Route path="skills" element={<SkillsMatrixPage />} />
            <Route path="learning" element={<SkillsMatrixPage />} />
            <Route path="service-desk" element={<ServiceDeskPage />} />
            <Route path="engagement" element={<EngagementHubPage />} />
            <Route path="payroll" element={<PayrollDashboardPage />} />
            <Route path="expenses" element={<ServiceDeskPage />} />
            <Route path="assets" element={<ServiceDeskPage />} />
            <Route path="documents" element={<ServiceDeskPage />} />
          </Route>
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
};
