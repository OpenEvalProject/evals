#!/usr/bin/env python3
"""
Clean OpenEval output files for papers with PROCESSED status.

This script:
1. Queries the database for all PROCESSED papers
2. Deletes their OpenEval output files (claims.json, eval_llm.json, etc.)
3. Updates their status to UNPROCESSED
"""

import sqlite3
import shutil
from pathlib import Path
from typing import List, Dict, Any
import argparse


DB_PATH = Path(__file__).parent / 'evals.sqlite'
EVALS_DIR = Path(__file__).parent


def get_processed_papers() -> List[Dict[str, Any]]:
    """Get all papers with PROCESSED status."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, openeval_rel_path
        FROM jats
        WHERE openeval_status = 'PROCESSED'
        ORDER BY id
    """)

    results = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return results


def delete_openeval_files(openeval_dir: Path, dry_run: bool = False) -> Dict[str, int]:
    """
    Delete OpenEval output files in a directory.

    Returns dict with counts of deleted files.
    """
    if not openeval_dir.exists():
        return {'files_deleted': 0, 'error': 'Directory does not exist'}

    stats = {
        'files_deleted': 0,
        'files_kept': 0,
        'error': None
    }

    # Files to delete (OpenEval outputs)
    files_to_delete = [
        'claims.json',
        'eval_llm.json',
        'eval_peer.json',
        'cmp.json',
        'db_export.json',
    ]

    # Also delete generated figures
    figure_patterns = [
        'figure_*.png',
        'figure_*.pdf',
    ]

    try:
        # Delete specific JSON files
        for filename in files_to_delete:
            filepath = openeval_dir / filename
            if filepath.exists():
                if not dry_run:
                    filepath.unlink()
                stats['files_deleted'] += 1

        # Delete figure files
        for pattern in figure_patterns:
            for filepath in openeval_dir.glob(pattern):
                if not dry_run:
                    filepath.unlink()
                stats['files_deleted'] += 1

        # Keep: manuscript.md, manuscript_metadata.json, reviews.md, response.md

    except Exception as e:
        stats['error'] = str(e)

    return stats


def clean_processed_papers(dry_run: bool = False, verbose: bool = True):
    """
    Clean all PROCESSED papers.

    Args:
        dry_run: If True, don't actually delete files or update database
        verbose: Print progress information
    """
    papers = get_processed_papers()

    if verbose:
        print(f"Found {len(papers)} PROCESSED papers")
        if dry_run:
            print("DRY RUN - No files will be deleted")
        print()

    total_stats = {
        'papers_processed': 0,
        'files_deleted': 0,
        'errors': 0
    }

    for paper in papers:
        jats_id = paper['id']
        openeval_rel_path = paper['openeval_rel_path']
        openeval_dir = EVALS_DIR / openeval_rel_path

        if verbose:
            print(f"Processing {jats_id}...")

        stats = delete_openeval_files(openeval_dir, dry_run)

        if stats.get('error'):
            print(f"  ✗ Error: {stats['error']}")
            total_stats['errors'] += 1
        else:
            if verbose:
                print(f"  ✓ Deleted {stats['files_deleted']} files")
            total_stats['papers_processed'] += 1
            total_stats['files_deleted'] += stats['files_deleted']

    # Update database status
    if not dry_run:
        if verbose:
            print()
            print("Updating database status...")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE jats
            SET openeval_status = 'UNPROCESSED'
            WHERE openeval_status = 'PROCESSED'
        """)

        updated_count = cursor.rowcount
        conn.commit()
        conn.close()

        if verbose:
            print(f"  Updated {updated_count} records to UNPROCESSED")

    # Print summary
    if verbose:
        print()
        print("=" * 60)
        print("Summary:")
        print(f"  Papers processed: {total_stats['papers_processed']}")
        print(f"  Total files deleted: {total_stats['files_deleted']}")
        print(f"  Errors: {total_stats['errors']}")
        if dry_run:
            print()
            print("DRY RUN COMPLETE - No changes were made")
        print("=" * 60)

    return total_stats


def main():
    parser = argparse.ArgumentParser(
        description='Clean OpenEval output files for PROCESSED papers'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be deleted without actually deleting'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress verbose output'
    )

    args = parser.parse_args()

    verbose = not args.quiet

    if not args.dry_run:
        # Confirm before deleting
        print("WARNING: This will delete OpenEval output files for all PROCESSED papers.")
        print("The following files will be deleted from each processed paper:")
        print("  - claims.json")
        print("  - eval_llm.json")
        print("  - eval_peer.json")
        print("  - cmp.json")
        print("  - db_export.json")
        print("  - figure_*.png")
        print()
        print("The following files will be KEPT:")
        print("  - manuscript.md")
        print("  - manuscript_metadata.json")
        print("  - reviews.md")
        print("  - response.md")
        print()

        response = input("Are you sure you want to proceed? (yes/no): ")
        if response.lower() != 'yes':
            print("Aborted.")
            return

    clean_processed_papers(dry_run=args.dry_run, verbose=verbose)


if __name__ == '__main__':
    main()
