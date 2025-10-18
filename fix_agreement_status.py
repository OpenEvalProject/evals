#!/usr/bin/env python3
"""
Fix agreement_status based on actual status comparison.

Rule: When both llm_result_id and peer_result_id exist:
- If llm_status == peer_status → agreement_status = "agree"
- If llm_status != peer_status → agreement_status = "disagree"
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict


def fix_comparison(comparison: Dict[str, Any]) -> bool:
    """Fix a single comparison object. Returns True if changed."""
    llm_id = comparison.get("llm_result_id")
    peer_id = comparison.get("peer_result_id")
    llm_status = comparison.get("llm_status")
    peer_status = comparison.get("peer_status")
    current_agreement = comparison.get("agreement_status")

    # Only fix if both results exist
    if llm_id is not None and peer_id is not None:
        # Determine correct agreement status
        correct_status = "agree" if llm_status == peer_status else "disagree"

        # Update if incorrect
        if current_agreement != correct_status:
            comparison["agreement_status"] = correct_status
            return True

    return False


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
                if fix_comparison(item):
                    changes_made = True

        elif isinstance(data, dict):
            # Check if it's a db_export.json with comparisons array
            if "comparisons" in data and isinstance(data["comparisons"], list):
                for comparison in data["comparisons"]:
                    if fix_comparison(comparison):
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
