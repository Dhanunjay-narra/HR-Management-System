"""
Massive Domain Expansion Part 2: Security Runbooks, Relocation Per Diems, IT Hardware Specs & Reports
"""
import os
import sys

BASE_DIR = r"c:\Users\DHANUNJAY\OneDrive\Desktop\git2"

def write(rel, text):
    path = os.path.join(BASE_DIR, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"[OK] {rel} ({len(text.splitlines())} lines)")

def generate_security_runbooks():
    runbooks = [
        ("RB-SEC-01", "Spear-Phishing & Credential Compromise Response", "HIGH", ["Isolate affected user session across Okta/Google Workspace.", "Force password reset and revoke all OAuth refresh tokens.", "Query SIEM audit logs for unauthorized mailbox delegation or forwarders.", "Audit endpoint via EDR (CrowdStrike) for malware execution.", "Issue targeted phishing awareness retraining to user."]),
        ("RB-SEC-02", "Production Database Unauthorized Access / Data Leak", "CRITICAL", ["Immediately sever active connection pool from suspect IP addresses.", "Rotate database master credentials and application connection strings in AWS Secrets Manager.", "Snapshot DB audit log tables and archive immutably for digital forensics.", "Engage legal counsel and prepare GDPR/CCPA 72-hour breach disclosure if PII was exposed.", "Conduct root cause analysis and implement tighter VPC security groups."]),
        ("RB-SEC-03", "Ransomware Infection & Host Isolation Runbook", "CRITICAL", ["Network isolate infected endpoint via MDM/EDR API immediately.", "Disable SMB file share access to prevent lateral network traversal.", "Identify blast radius and restore unaffected data from immutable S3 backups.", "Analyze initial access vector (exploited CVE or malicious attachment).", "Conduct clean re-imaging of physical device hardware."]),
        ("RB-SEC-04", "Distributed Denial of Service (DDoS) Mitigation", "HIGH", ["Enable Cloudflare / AWS Shield Advanced under-attack rate-limiting mode.", "Engage Cloudflare WAF bot management heuristics and challenge suspect ASN traffic.", "Scale backend Kubernetes pod replicas and Aurora read-replicas.", "Verify synthetic uptime monitors and communicate incident status via statuspage.io."]),
        ("RB-SEC-05", "Malicious Insider & Unauthorized Data Exfiltration", "HIGH", ["Revoke all corporate VPN, cloud console, and SaaS access tokens instantly.", "Freeze employee hardware and preserve disk forensic image.", "Review Git push logs, Google Drive external shares, and DLP audit trails.", "Escalate investigation findings to Legal Counsel and People Operations."]),
    ]

    lines = [
        '"""',
        'Enterprise Information Security Incident Response Runbooks (NIST SP 800-61 / ISO 27035)',
        'Defines step-by-step containment, eradication, recovery, and communication protocols for critical security scenarios.',
        '"""',
        'from typing import Dict, List, Any',
        'from dataclasses import dataclass',
        '',
        '',
        '@dataclass',
        'class SecurityIncidentRunbook:',
        '    runbook_id: str',
        '    title: str',
        '    severity_level: str',
        '    action_steps: List[str]',
        '',
        '',
        'MASTER_SECURITY_RUNBOOKS: Dict[str, SecurityIncidentRunbook] = {',
    ]

    for rid, title, sev, steps in runbooks:
        lines.append(f'    "{rid}": SecurityIncidentRunbook(')
        lines.append(f'        runbook_id="{rid}",')
        lines.append(f'        title="{title}",')
        lines.append(f'        severity_level="{sev}",')
        lines.append(f'        action_steps={steps}')
        lines.append('    ),')

    lines.append('}')
    lines.append('')
    lines.append('class SecurityRunbookService:')
    lines.append('    @classmethod')
    lines.append('    def get_runbook(cls, runbook_id: str) -> SecurityIncidentRunbook:')
    lines.append('        return MASTER_SECURITY_RUNBOOKS.get(runbook_id)')
    lines.append('')
    lines.append('    @classmethod')
    lines.append('    def get_all_runbooks(cls) -> List[SecurityIncidentRunbook]:')
    lines.append('        return list(MASTER_SECURITY_RUNBOOKS.values())')

    write("backend/app/domain/reference/enterprise_security_incident_runbooks.py", "\n".join(lines))

def generate_relocation_per_diems():
    destinations = [
        ("US-SFO", "San Francisco, CA", "USD", 245.0, 79.0),
        ("US-NYC", "New York City, NY", "USD", 280.0, 79.0),
        ("US-SEA", "Seattle, WA", "USD", 215.0, 74.0),
        ("US-AUS", "Austin, TX", "USD", 175.0, 69.0),
        ("UK-LON", "London", "GBP", 195.0, 65.0),
        ("DE-BER", "Berlin", "EUR", 150.0, 50.0),
        ("FR-PAR", "Paris", "EUR", 185.0, 60.0),
        ("CH-ZUR", "Zurich", "CHF", 230.0, 80.0),
        ("JP-TYO", "Tokyo", "JPY", 22000.0, 8500.0),
        ("SG-SIN", "Singapore", "SGD", 260.0, 90.0),
        ("AU-SYD", "Sydney", "AUD", 220.0, 75.0),
        ("IN-BLR", "Bengaluru", "INR", 8500.0, 2500.0),
    ]

    lines = [
        '"""',
        'Global Business Travel & Relocation Per Diem Standard Rates (GSA / IRS & International)',
        'Prescribes standard lodging caps and Meals & Incidental Expense (M&IE) per diems across key business hubs.',
        '"""',
        'from typing import Dict, List, Any',
        'from dataclasses import dataclass',
        '',
        '',
        '@dataclass',
        'class CityPerDiemRate:',
        '    city_code: str',
        '    city_name: str',
        '    currency: str',
        '    max_lodging_rate_per_night: float',
        '    daily_meal_incidental_allowance: float',
        '',
        '',
        'GLOBAL_PER_DIEM_REGISTRY: Dict[str, CityPerDiemRate] = {',
    ]

    for code, name, curr, lodge, mie in destinations:
        lines.append(f'    "{code}": CityPerDiemRate(')
        lines.append(f'        city_code="{code}",')
        lines.append(f'        city_name="{name}",')
        lines.append(f'        currency="{curr}",')
        lines.append(f'        max_lodging_rate_per_night={lodge},')
        lines.append(f'        daily_meal_incidental_allowance={mie}')
        lines.append('    ),')

    lines.append('}')
    lines.append('')
    lines.append('class PerDiemRateService:')
    lines.append('    @classmethod')
    lines.append('    def get_city_rate(cls, city_code: str) -> CityPerDiemRate:')
    lines.append('        return GLOBAL_PER_DIEM_REGISTRY.get(city_code)')
    lines.append('')
    lines.append('    @classmethod')
    lines.append('    def get_all_rates(cls) -> List[CityPerDiemRate]:')
    lines.append('        return list(GLOBAL_PER_DIEM_REGISTRY.values())')

    write("backend/app/domain/reference/global_relocation_per_diems_and_allowances.py", "\n".join(lines))

generate_security_runbooks()
generate_relocation_per_diems()

# React Views
asset_timeline_code = '''import React from 'react';
import { Laptop, ShieldCheck, Clock, CheckCircle2, User, ArrowRight } from 'lucide-react';

export const AssetCustodyTimelinePage: React.FC = () => {
  const custodyHistory = [
    { id: '1', asset: 'MacBook Pro 16" M3 Max (64GB/1TB)', serial: 'C02XYZ123456', assignee: 'Sarah Connor', role: 'Staff Software Engineer', assignedDate: '2025-01-15', status: 'IN_USE', mdmStatus: 'ENCRYPTED_OK' },
    { id: '2', asset: 'Dell UltraSharp 32" 4K Monitor', serial: 'DELL-998877', assignee: 'Sarah Connor', role: 'Staff Software Engineer', assignedDate: '2025-01-15', status: 'IN_USE', mdmStatus: 'N/A' },
    { id: '3', asset: 'YubiKey 5C NFC Security Key', serial: 'YK-55443322', assignee: 'Sarah Connor', role: 'Staff Software Engineer', assignedDate: '2025-01-15', status: 'IN_USE', mdmStatus: 'REGISTERED' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900 tracking-tight">IT Hardware Custody & Lifecycle Management</h2>
        <p className="text-xs text-slate-500">
          Tracks physical device provisioning, MDM encryption compliance (FileVault/BitLocker), and chain of custody.
        </p>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">Assigned Equipment Roster</h3>
          <span className="text-xs text-slate-500 font-medium">{custodyHistory.length} active hardware units</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Hardware Item</th>
                <th className="py-3 px-4">Serial Number</th>
                <th className="py-3 px-4">Assigned To</th>
                <th className="py-3 px-4">Provisioned Date</th>
                <th className="py-3 px-4">MDM Encryption</th>
                <th className="py-3 px-4">Custody Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {custodyHistory.map((item) => (
                <tr key={item.id} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3.5 px-4 font-bold text-slate-900 flex items-center gap-2">
                    <Laptop className="w-4 h-4 text-blue-600" />
                    <span>{item.asset}</span>
                  </td>
                  <td className="py-3.5 px-4 font-mono text-slate-500">{item.serial}</td>
                  <td className="py-3.5 px-4 font-medium text-slate-800">{item.assignee}</td>
                  <td className="py-3.5 px-4 text-slate-600">{item.assignedDate}</td>
                  <td className="py-3.5 px-4">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800 flex items-center gap-1 w-fit">
                      <ShieldCheck className="w-3 h-3" /> {item.mdmStatus}
                    </span>
                  </td>
                  <td className="py-3.5 px-4">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-blue-100 text-blue-800">
                      {item.status}
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
'''
write("frontend/src/pages/assets/AssetCustodyTimelinePage.tsx", asset_timeline_code)

eeo1_code = '''import React from 'react';
import { ShieldCheck, Download, Users, CheckCircle2, FileSpreadsheet } from 'lucide-react';
import { useExportData } from '../../hooks/useTableSort';

export const EEO1ComplianceReportPage: React.FC = () => {
  const { exportToCSV } = useExportData();

  const eeoData = [
    { category: 'Executive / Senior Officials', total: 6, male: 4, female: 2, minorityPct: '33.3%' },
    { category: 'First / Mid-Level Managers', total: 24, male: 15, female: 9, minorityPct: '41.7%' },
    { category: 'Professionals (Engineering / Product)', total: 120, male: 78, female: 42, minorityPct: '48.3%' },
    { category: 'Sales Workers', total: 35, male: 20, female: 15, minorityPct: '37.1%' },
    { category: 'Administrative Support', total: 15, male: 5, female: 10, minorityPct: '46.7%' },
  ];

  const handleExport = () => {
    exportToCSV('EEO1_Component1_Workforce_Report_2026', eeoData);
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 tracking-tight">EEOC EEO-1 Component 1 Compliance Report</h2>
          <p className="text-xs text-slate-500">
            Mandatory annual workforce demographic disclosure categorized by federal job classification bands.
          </p>
        </div>
        <button
          onClick={handleExport}
          className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm shadow-blue-500/20"
        >
          <Download className="w-4 h-4" />
          <span>Export EEOC CSV Filing</span>
        </button>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 border-b border-slate-100 flex items-center justify-between">
          <h3 className="font-bold text-xs text-slate-900 uppercase tracking-wider">EEO-1 Job Category Distribution</h3>
          <span className="text-xs text-slate-500 font-medium">200 Total Full-Time Employees</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase">
              <tr>
                <th className="py-3 px-4">Federal Job Category</th>
                <th className="py-3 px-4 text-center">Total Headcount</th>
                <th className="py-3 px-4 text-center">Male</th>
                <th className="py-3 px-4 text-center">Female</th>
                <th className="py-3 px-4 text-right">Minority Representation</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {eeoData.map((row, i) => (
                <tr key={i} className="hover:bg-slate-50/60 transition-colors">
                  <td className="py-3.5 px-4 font-bold text-slate-900">{row.category}</td>
                  <td className="py-3.5 px-4 text-center font-bold text-slate-800">{row.total}</td>
                  <td className="py-3.5 px-4 text-center text-slate-600">{row.male}</td>
                  <td className="py-3.5 px-4 text-center text-slate-600">{row.female}</td>
                  <td className="py-3.5 px-4 text-right font-bold text-blue-600">{row.minorityPct}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
'''
write("frontend/src/pages/reports/EEO1ComplianceReportPage.tsx", eeo1_code)

print("Part 2 Built Successfully!")
'''
write("scripts/build_massive_domain_expansion_part2.py", "# Expansion part 2")
'''
