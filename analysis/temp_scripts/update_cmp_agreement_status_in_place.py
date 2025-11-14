#!/usr/bin/env python3
"""
Script to update cmp.json files in place in v1 directories with updated agreement_status logic.

This script applies the updated agreement_status calculation logic from the compare_results function
directly to existing cmp.json files in v1 directories, without creating v2 directories.

Usage:
    python update_cmp_agreement_status_in_place.py [--manuscript MANUSCRIPT] [--verbose] [--dry-run]

Examples:
    # Update all manuscripts with cmp.json files
    python update_cmp_agreement_status_in_place.py --verbose
    
    # Update a specific manuscript
    python update_cmp_agreement_status_in_place.py --manuscript elife-00003 --verbose
    
    # Dry run to see what would be updated
    python update_cmp_agreement_status_in_place.py --dry-run --verbose
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
import argparse


def calculate_agreement_status(llm_status: Optional[str], peer_status: Optional[str]) -> str:
    """Calculate agreement_status based on llm_status and peer_status.
    
    This implements the updated logic from compare_results function:
    - "agree": Both statuses are identical
    - "disagree": SUPPORTED vs UNSUPPORTED (or vice versa)
    - "partial": One is UNCERTAIN and the other is SUPPORTED/UNSUPPORTED
    - "error comparing statuses": Unknown status values
    - "disjoint": One or both statuses are missing
    """
    if llm_status is not None and peer_status is not None:
        # Both statuses present - normalize for comparison
        s1 = llm_status.strip().upper()
        s2 = peer_status.strip().upper()

        if s1 == s2:
            return "agree"
        elif (
            (s1 == "SUPPORTED" and s2 == "UNSUPPORTED") or
            (s1 == "UNSUPPORTED" and s2 == "SUPPORTED")
        ):
            return "disagree"
        elif (
            (s1 == "SUPPORTED" and s2 == "UNCERTAIN") or
            (s1 == "UNCERTAIN" and s2 == "SUPPORTED") or
            (s1 == "UNSUPPORTED" and s2 == "UNCERTAIN") or
            (s1 == "UNCERTAIN" and s2 == "UNSUPPORTED")
        ):
            return "partial"
        else:
            # Handles cases like unknown status values
            return "error comparing statuses"
    else:
        # One or both statuses missing
        return "disjoint"


def find_manuscripts_with_cmp_json(manuscripts_dir: Path) -> List[Path]:
    """Find all manuscript directories that have v1 subdirectories with cmp.json files."""
    manuscripts = []
    
    for manuscript_dir in manuscripts_dir.iterdir():
        if not manuscript_dir.is_dir():
            continue
            
        v1_dir = manuscript_dir / "v1"
        if not v1_dir.exists():
            continue
            
        # Check for cmp.json file
        cmp_file = v1_dir / "cmp.json"
        if cmp_file.exists():
            manuscripts.append(manuscript_dir)
    
    return sorted(manuscripts)


def update_cmp_json_in_place(v1_dir: Path, verbose: bool = False) -> bool:
    """Update cmp.json in place by applying the new agreement_status logic."""
    cmp_file = v1_dir / "cmp.json"
    
    if not cmp_file.exists():
        print(f"Warning: cmp.json not found in {v1_dir}")
        return False
    
    try:
        # Load the existing cmp.json
        with open(cmp_file, 'r', encoding='utf-8') as f:
            cmp_data = json.load(f)
        
        if verbose:
            print(f"Loaded {len(cmp_data)} concordance rows")
        
        # Update agreement_status for each row
        updated_count = 0
        for row in cmp_data:
            old_agreement_status = row.get("agreement_status")
            new_agreement_status = calculate_agreement_status(
                row.get("llm_status"), 
                row.get("peer_status")
            )
            
            row["agreement_status"] = new_agreement_status
            
            if old_agreement_status != new_agreement_status:
                updated_count += 1
                if verbose:
                    print(f"  Updated row {row.get('llm_result_id', '?')}-{row.get('peer_result_id', '?')}: "
                          f"{old_agreement_status} -> {new_agreement_status}")
        
        if verbose:
            print(f"Updated {updated_count} agreement_status values")
        
        # Save the updated cmp.json back to the same file
        with open(cmp_file, 'w', encoding='utf-8') as f:
            json.dump(cmp_data, f, indent=2, ensure_ascii=False)
        
        return True
        
    except Exception as e:
        print(f"Error processing {cmp_file}: {e}")
        return False


def process_manuscript(manuscript_dir: Path, verbose: bool = False, dry_run: bool = False) -> bool:
    """Process a single manuscript to update cmp.json in v1 directory."""
    manuscript_name = manuscript_dir.name
    v1_dir = manuscript_dir / "v1"
    
    print(f"Processing {manuscript_name}...")
    
    if dry_run:
        print(f"Would update cmp.json in v1 directory for {manuscript_name}")
        return True
    
    # Update cmp.json in place
    success = update_cmp_json_in_place(v1_dir, verbose=verbose)
    
    if success:
        print(f"Successfully updated cmp.json for {manuscript_name}")
    else:
        print(f"Failed to update cmp.json for {manuscript_name}")
    
    return success


def main():
    parser = argparse.ArgumentParser(description="Update cmp.json files in v1 directories with new agreement_status logic")
    parser.add_argument("--manuscripts-dir", type=Path, 
                       default=Path(__file__).parent / "manuscripts",
                       help="Directory containing manuscript directories")
    parser.add_argument("--manuscript", type=str, 
                       help="Process only a specific manuscript (e.g., 'elife-00003')")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Enable verbose output")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be done without actually doing it")
    parser.add_argument("--max-manuscripts", type=int,
                       help="Maximum number of manuscripts to process (for testing)")
    
    args = parser.parse_args()
    
    manuscripts_dir = args.manuscripts_dir
    if not manuscripts_dir.exists():
        print(f"Error: Manuscripts directory {manuscripts_dir} does not exist")
        return 1
    
    # Find manuscripts to process
    if args.manuscript:
        manuscript_dir = manuscripts_dir / args.manuscript
        if not manuscript_dir.exists():
            print(f"Error: Manuscript {args.manuscript} not found")
            return 1
        manuscripts = [manuscript_dir]
    else:
        manuscripts = find_manuscripts_with_cmp_json(manuscripts_dir)
        if args.max_manuscripts:
            manuscripts = manuscripts[:args.max_manuscripts]
    
    print(f"Found {len(manuscripts)} manuscripts with cmp.json files to process")
    
    if args.dry_run:
        print("DRY RUN MODE - No files will be modified")
    
    # Process each manuscript
    successful = 0
    failed = 0
    
    for manuscript_dir in manuscripts:
        try:
            if process_manuscript(manuscript_dir, verbose=args.verbose, dry_run=args.dry_run):
                successful += 1
            else:
                failed += 1
        except KeyboardInterrupt:
            print("\nInterrupted by user")
            break
        except Exception as e:
            print(f"Unexpected error processing {manuscript_dir.name}: {e}")
            failed += 1
    
    print(f"\nSummary:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total: {successful + failed}")
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
