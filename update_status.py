#!/usr/bin/env python3
"""
Update openeval_status for papers in the database.

Useful for marking papers as QUEUED or updating their status.
"""

import sqlite3
import argparse
from pathlib import Path
from typing import List


DB_PATH = Path(__file__).parent / 'evals.sqlite'


def update_status(jats_ids: List[str], new_status: str, verbose: bool = True):
    """
    Update status for one or more JATS entries.

    Args:
        jats_ids: List of JATS IDs to update (e.g., ["elife-00003-v1", "elife-00005-v1"])
        new_status: New status ('PROCESSED', 'QUEUED', 'UNPROCESSED')
        verbose: Print update information
    """
    if new_status not in ['PROCESSED', 'QUEUED', 'UNPROCESSED']:
        raise ValueError(f"Invalid status: {new_status}. Must be one of: PROCESSED, QUEUED, UNPROCESSED")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    updated_count = 0
    not_found = []

    for jats_id in jats_ids:
        # Check if exists
        cursor.execute("SELECT id, openeval_status FROM jats WHERE id = ?", (jats_id,))
        result = cursor.fetchone()

        if result:
            old_status = result[1]
            cursor.execute(
                "UPDATE jats SET openeval_status = ? WHERE id = ?",
                (new_status, jats_id)
            )
            updated_count += 1

            if verbose:
                print(f"✓ {jats_id}: {old_status} → {new_status}")
        else:
            not_found.append(jats_id)
            if verbose:
                print(f"✗ {jats_id}: Not found in database")

    conn.commit()
    conn.close()

    if verbose:
        print()
        print(f"Updated: {updated_count}/{len(jats_ids)}")
        if not_found:
            print(f"Not found: {len(not_found)}")

    return updated_count, not_found


def bulk_update_from_file(filepath: Path, new_status: str, verbose: bool = True):
    """
    Update status for JATS IDs listed in a file.

    Args:
        filepath: Path to file containing JATS IDs (one per line)
        new_status: New status ('PROCESSED', 'QUEUED', 'UNPROCESSED')
        verbose: Print update information
    """
    with open(filepath, 'r') as f:
        jats_ids = [line.strip() for line in f if line.strip()]

    if verbose:
        print(f"Found {len(jats_ids)} JATS IDs in {filepath}")
        print(f"Updating to status: {new_status}")
        print()

    return update_status(jats_ids, new_status, verbose)


def main():
    parser = argparse.ArgumentParser(
        description='Update openeval_status for papers in the database'
    )
    parser.add_argument(
        'status',
        choices=['PROCESSED', 'QUEUED', 'UNPROCESSED'],
        help='New status to set'
    )
    parser.add_argument(
        '--ids',
        nargs='+',
        help='JATS IDs to update (space-separated)'
    )
    parser.add_argument(
        '--file',
        type=Path,
        help='File containing JATS IDs (one per line)'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress verbose output'
    )

    args = parser.parse_args()

    if not args.ids and not args.file:
        parser.error("Either --ids or --file must be provided")

    verbose = not args.quiet

    if args.file:
        bulk_update_from_file(args.file, args.status, verbose)
    else:
        update_status(args.ids, args.status, verbose)


if __name__ == '__main__':
    main()
