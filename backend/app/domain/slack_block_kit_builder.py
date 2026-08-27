"""
Slack Block Kit Interactive Message & Approval Card Builder
Constructs rich JSON blocks for interactive leave approvals, expense reviews, kudos feeds, and incident notifications.
"""
from typing import Dict, List, Any


class SlackBlockKitBuilder:
    @staticmethod
    def build_leave_approval_card(
        employee_name: str,
        leave_type: str,
        start_date: str,
        end_date: str,
        days_count: float,
        reason: str,
        approval_id: str
    ) -> Dict[str, Any]:
        return {
            "blocks": [
                {
                    "type": "header",
                    "text": {"type": "plain_text", "text": "🏖️ New Leave Request Pending Review", "emoji": True}
                },
                {
                    "type": "section",
                    "fields": [
                        {"type": "mrkdwn", "text": f"*Employee:*\\n{employee_name}"},
                        {"type": "mrkdwn", "text": f"*Leave Type:*\\n{leave_type}"},
                        {"type": "mrkdwn", "text": f"*Period:*\\n{start_date} to {end_date}"},
                        {"type": "mrkdwn", "text": f"*Duration:*\\n{days_count} Business Days"}
                    ]
                },
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"*Reason:*\\n_{reason}_"}
                },
                {"type": "divider"},
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Approve Request", "emoji": True},
                            "style": "primary",
                            "value": f"approve_{approval_id}",
                            "action_id": "btn_approve_leave"
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Reject", "emoji": True},
                            "style": "danger",
                            "value": f"reject_{approval_id}",
                            "action_id": "btn_reject_leave"
                        }
                    ]
                }
            ]
        }
