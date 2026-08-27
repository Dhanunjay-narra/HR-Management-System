"""
Deep Recursive State Mutation & RFC 6902 JSON Patch Engine
Computes granular diffs and cryptographically verifies audit trails.
"""
import hashlib
import json
from typing import Dict, Any, List, Tuple


class DeepStateDiffEngine:
    @classmethod
    def diff_objects(
        cls,
        before: Dict[str, Any],
        after: Dict[str, Any],
        path: str = ""
    ) -> List[Dict[str, Any]]:
        """
        Recursively calculates differences between state dictionaries in RFC 6902 JSON Patch format.
        """
        patches: List[Dict[str, Any]] = []
        all_keys = set(before.keys()).union(set(after.keys()))

        for k in all_keys:
            curr_path = f"{path}/{k}" if path else f"/{k}"

            if k not in before:
                patches.append({"op": "add", "path": curr_path, "value": after[k]})
            elif k not in after:
                patches.append({"op": "remove", "path": curr_path, "old_value": before[k]})
            else:
                v_before = before[k]
                v_after = after[k]

                if isinstance(v_before, dict) and isinstance(v_after, dict):
                    patches.extend(cls.diff_objects(v_before, v_after, curr_path))
                elif v_before != v_after:
                    patches.append({
                        "op": "replace",
                        "path": curr_path,
                        "old_value": v_before,
                        "value": v_after
                    })

        return patches

    @staticmethod
    def generate_tamper_evident_hash(previous_hash: str, payload_dict: Dict[str, Any]) -> str:
        serialized = json.dumps(payload_dict, sort_keys=True, default=str)
        raw = f"{previous_hash}:{serialized}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
