// Domain TypeScript definitions for HR Management System

export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
  full_name: string;
  role: string;
  permissions: string[];
  tenant_id: string;
  is_active: boolean;
  avatar_url?: string;
}

export interface Employee {
  id: string;
  tenant_id: string;
  employee_code: string;
  first_name: string;
  last_name: string;
  full_name: string;
  work_email: string;
  phone_number?: string;
  department_id?: string;
  department_name?: string;
  designation_id?: string;
  designation_title?: string;
  branch_id?: string;
  branch_name?: string;
  employment_type: string;
  status: string;
  date_of_joining: string;
  avatar_url?: string;
}

export interface Employee360Profile {
  employee: Employee;
  manager?: { id: string; full_name: string; designation?: string; email: string };
  direct_reports: Array<{ id: string; full_name: string; designation?: string }>;
  peers: Array<{ id: string; full_name: string; designation?: string }>;
  attendance_summary: {
    total_days: number;
    present_days: number;
    late_days: number;
    half_days: number;
    attendance_rate: number;
  };
  leave_balances: Array<{
    leave_type_code: string;
    leave_type_name: string;
    allocated_days: number;
    used_days: number;
    remaining_days: number;
  }>;
  recent_timeline_events: Array<{
    id: string;
    event_type: string;
    title: string;
    description?: string;
    created_at: string;
  }>;
}

export interface AttendanceRecord {
  id: string;
  employee_id: string;
  employee_name?: string;
  date: string;
  status: string;
  clock_in?: string;
  clock_out?: string;
  total_work_minutes: number;
  is_late: boolean;
  is_overtime: boolean;
}

export interface LeaveRequest {
  id: string;
  employee_id: string;
  employee_name?: string;
  leave_type_name?: string;
  start_date: string;
  end_date: string;
  days_count: number;
  reason: string;
  status: string;
  reviewer_comments?: string;
  created_at: string;
}

export interface JobRequisition {
  id: string;
  title: string;
  code: string;
  department_name?: string;
  positions_count: number;
  min_experience_years: number;
  max_experience_years: number;
  required_skills: string[];
  job_description: string;
  salary_min?: number;
  salary_max?: number;
  status: string;
  candidates_count: number;
  created_at: string;
}

export interface Candidate {
  id: string;
  job_requisition_id: string;
  first_name: string;
  last_name: string;
  full_name: string;
  email: string;
  phone_number?: string;
  current_company?: string;
  experience_years: number;
  extracted_skills: string[];
  match_score: number;
  pipeline_stage: string;
  created_at: string;
}

export interface OnboardingWorkflow {
  id: string;
  employee_id: string;
  employee_name?: string;
  template_name: string;
  status: string;
  start_date: string;
  target_completion_date: string;
  progress_percentage: number;
  tasks: Array<{
    id: string;
    title: string;
    category: string;
    due_date: string;
    is_completed: boolean;
    completed_at?: string;
  }>;
}

export interface Goal {
  id: string;
  title: string;
  description?: string;
  level: string;
  target_value: number;
  current_value: number;
  unit: string;
  deadline: string;
  status: string;
  progress_percentage: number;
  key_results: Array<{
    id: string;
    title: string;
    target_value: number;
    current_value: number;
    unit: string;
  }>;
}

export interface SkillGapAnalysis {
  employee_id: string;
  employee_name: string;
  designation_title?: string;
  overall_readiness_score: number;
  skills_assessed_count: number;
  skills_met_count: number;
  skills_gap_count: number;
  gap_matrix: Array<{
    skill_id: string;
    skill_name: string;
    category: string;
    current_proficiency: number;
    required_proficiency: number;
    gap_level: number;
    is_met: boolean;
    recommended_course?: { id: string; title: string; duration_hours: number };
  }>;
}

export interface Course {
  id: string;
  title: string;
  code: string;
  category: string;
  description: string;
  duration_hours: number;
  level: string;
  provider: string;
  lessons: Array<{
    id: string;
    title: string;
    content_type: string;
    duration_minutes: number;
  }>;
}

export interface HRTicket {
  id: string;
  ticket_number: string;
  category_name?: string;
  employee_id: string;
  employee_name?: string;
  subject: string;
  description: string;
  priority: string;
  status: string;
  due_date?: string;
  created_at: string;
  comments: Array<{
    id: string;
    author_name?: string;
    comment_text: string;
    created_at: string;
  }>;
}

export interface Kudos {
  id: string;
  sender_name?: string;
  receiver_name?: string;
  badge_type: string;
  message: string;
  created_at: string;
}

export interface Announcement {
  id: string;
  title: string;
  content: string;
  priority: string;
  is_pinned: boolean;
  author_name?: string;
  publish_at: string;
}

export interface PayrollRun {
  id: string;
  month: number;
  year: number;
  status: string;
  total_employees_count: number;
  total_gross_payout: number;
  total_deductions: number;
  total_net_payout: number;
  created_at: string;
}

export interface ExpenseClaim {
  id: string;
  claim_number: string;
  employee_name?: string;
  category_name?: string;
  expense_date: string;
  amount: number;
  currency: string;
  merchant_name: string;
  description: string;
  status: string;
  created_at: string;
}

export interface Asset {
  id: string;
  asset_tag: string;
  name: string;
  category: string;
  serial_number?: string;
  purchase_cost: number;
  status: string;
  current_employee_name?: string;
}

export interface DocumentItem {
  id: string;
  title: string;
  category: string;
  document_url: string;
  file_name: string;
  file_size_kb: number;
  is_public_policy: boolean;
  created_at: string;
}

export interface AnalyticsOverview {
  headcount: {
    total_employees: number;
    active_employees: number;
    probation_employees: number;
    on_leave_employees: number;
    contractors_count: number;
    attrition_rate_percent: number;
  };
  department_distribution: Array<{
    department_id: string;
    department_name: string;
    headcount: number;
    monthly_payroll_budget: number;
  }>;
  gender_diversity: Record<string, number>;
  average_attendance_rate: number;
  open_requisitions_count: number;
  total_open_tickets: number;
  total_active_goals: number;
}

export interface Payslip {
  id: string;
  employee_id: string;
  employee_name: string;
  designation?: string;
  department?: string;
  month: number;
  year: number;
  gross_salary: number;
  deductions: number;
  net_salary: number;
  payment_status: string;
  basic_salary?: number;
  hra?: number;
  allowances?: number;
  gross_earnings?: number;
  pf_deduction?: number;
  tax_deduction?: number;
  other_deductions?: number;
  total_deductions?: number;
}

export interface TotalRewardsSummary {
  base_salary: number;
  bonus_target: number;
  equity_value: number;
  health_subsidy: number;
  match_401k: number;
  wellness_perks: number;
  total_rewards_value: number;
}
