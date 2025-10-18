#!/usr/bin/env python3
"""
Fix 'partial' to 'disjoint' terminology in comparison JSON files.

Transformation rules:
1. If BOTH llm_result_id AND peer_result_id are present AND agreement_status == "partial"
   → Change to "disagree"
2. If ONLY ONE of (llm_result_id OR peer_result_id) is present
   → Change to "disjoint"
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List


def transform_comparison(comparison: Dict[str, Any]) -> Dict[str, Any]:
    """Transform a single comparison object according to the rules."""
    llm_id = comparison.get("llm_result_id")
    peer_id = comparison.get("peer_result_id")

    # Rule 2: If only one result_id is present → disjoint
    if (llm_id is None and peer_id is not None) or (llm_id is not None and peer_id is None):
        comparison["agreement_status"] = "disjoint"
    # Rule 1: If both are present AND status is "partial" → disagree
    elif llm_id is not None and peer_id is not None and comparison.get("agreement_status") == "partial":
        comparison["agreement_status"] = "disagree"

    return comparison


def process_json_file(file_path: Path) -> bool:
    """Process a single JSON file. Returns True if changes were made."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        changes_made = False

        # Handle different JSON structures
        if isinstance(data, list):
            # Array of comparisons (cmp.json files)
            for item in data:
                old_status = item.get("agreement_status")
                transform_comparison(item)
                if item.get("agreement_status") != old_status:
                    changes_made = True

        elif isinstance(data, dict):
            # Check if it's a db_export.json with comparisons array
            if "comparisons" in data and isinstance(data["comparisons"], list):
                for comparison in data["comparisons"]:
                    old_status = comparison.get("agreement_status")
                    transform_comparison(comparison)
                    if comparison.get("agreement_status") != old_status:
                        changes_made = True

        # Write back if changes were made
        if changes_made:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return False


def main():
    """Find and process all JSON files in evals/manuscripts."""
    base_path = Path(__file__).parent / "manuscripts"

    if not base_path.exists():
        print(f"Error: {base_path} does not exist", file=sys.stderr)
        sys.exit(1)

    # Find all cmp.json and db_export.json files
    json_files = []
    json_files.extend(base_path.glob("*/v*/cmp.json"))
    json_files.extend(base_path.glob("*/v*/db_export.json"))

    print(f"Found {len(json_files)} JSON files to process")

    files_changed = 0
    for file_path in sorted(json_files):
        if process_json_file(file_path):
            files_changed += 1
            print(f"✓ Updated: {file_path.relative_to(base_path.parent)}")

    print(f"\nProcessed {len(json_files)} files, updated {files_changed} files")


if __name__ == "__main__":
    main()
