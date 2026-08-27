"""
Directed Acyclic Graph (DAG) Matrix Organization Hierarchy Engine
Resolves matrix reporting lines, dotted-line managers, organizational depth, and span of control.
"""
from typing import Dict, List, Any, Optional, Set
from collections import deque


class DAGOrgChartEngine:
    @staticmethod
    def build_reporting_graph(
        employees: List[Dict[str, Any]]
    ) -> Tuple[Dict[str, List[str]], Dict[str, Optional[str]], Set[str]]:
        """
        Constructs adjacency lists for direct reports and parent managers.
        Returns: (manager_to_reports, report_to_manager, root_leader_ids)
        """
        manager_to_reports: Dict[str, List[str]] = {}
        report_to_manager: Dict[str, Optional[str]] = {}
        all_ids: Set[str] = set()

        for emp in employees:
            e_id = emp["id"]
            m_id = emp.get("manager_id")
            all_ids.add(e_id)
            report_to_manager[e_id] = m_id
            if m_id:
                manager_to_reports.setdefault(m_id, []).append(e_id)

        # Roots are employees without a manager or whose manager is not in the dataset
        roots = {e_id for e_id in all_ids if not report_to_manager.get(e_id) or report_to_manager.get(e_id) not in all_ids}
        return manager_to_reports, report_to_manager, roots

    @classmethod
    def calculate_span_of_control(
        cls,
        employees: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        mgr_reports, _, roots = cls.build_reporting_graph(employees)
        emp_map = {e["id"]: e for e in employees}

        spans: Dict[str, int] = {}
        depths: Dict[str, int] = {}
        max_depth = 0

        # BFS for depth calculation
        queue = deque([(r, 1) for r in roots])
        while queue:
            curr_id, depth = queue.popleft()
            depths[curr_id] = depth
            max_depth = max(max_depth, depth)

            reports = mgr_reports.get(curr_id, [])
            spans[curr_id] = len(reports)
            for child in reports:
                queue.append((child, depth + 1))

        avg_span = sum(spans.values()) / max(1, len(spans))

        return {
            "total_employees": len(employees),
            "max_hierarchy_depth": max_depth,
            "average_span_of_control": round(avg_span, 2),
            "root_executives_count": len(roots),
            "spans_by_manager": {emp_map[k]["full_name"] if k in emp_map else k: v for k, v in spans.items() if v > 0}
        }
