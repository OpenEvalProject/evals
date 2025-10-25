#!/usr/bin/env python3
"""
Query the evals SQLite database.

Provides convenience functions for common queries.
"""

import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional
import argparse


DB_PATH = Path(__file__).parent / 'evals.sqlite'


def get_connection() -> sqlite3.Connection:
    """Get database connection."""
    return sqlite3.connect(DB_PATH)


def dict_factory(cursor, row):
    """Convert SQLite row to dict."""
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


# ============================================================================
# QUERY FUNCTIONS
# ============================================================================

def get_stats() -> Dict[str, int]:
    """Get overall database statistics."""
    conn = get_connection()
    cursor = conn.cursor()

    stats = {}

    cursor.execute("SELECT COUNT(*) FROM paper")
    stats['total_papers'] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats")
    stats['total_jats'] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE peer_reviews = 1")
    stats['with_peer_reviews'] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE openeval_status = 'PROCESSED'")
    stats['status_processed'] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE openeval_status = 'QUEUED'")
    stats['status_queued'] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE openeval_status = 'UNPROCESSED'")
    stats['status_unprocessed'] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE doi IS NOT NULL")
    stats['with_doi'] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE pub_date IS NOT NULL")
    stats['with_pub_date'] = cursor.fetchone()[0]

    conn.close()
    return stats


def get_papers_by_status(
    peer_reviews: Optional[bool] = None,
    openeval_status: Optional[str] = None,
    limit: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    Get papers filtered by status.

    Args:
        peer_reviews: Filter by peer review availability
        openeval_status: Filter by status ('PROCESSED', 'QUEUED', 'UNPROCESSED')
        limit: Maximum number of results
    """
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    query = "SELECT * FROM jats WHERE 1=1"
    params = []

    if peer_reviews is not None:
        query += " AND peer_reviews = ?"
        params.append(1 if peer_reviews else 0)

    if openeval_status is not None:
        query += " AND openeval_status = ?"
        params.append(openeval_status)

    query += " ORDER BY id"

    if limit:
        query += f" LIMIT {limit}"

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return results


def get_paper_versions(paper_id: str) -> List[Dict[str, Any]]:
    """Get all versions of a paper."""
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM jats WHERE paper_id = ? ORDER BY version",
        (paper_id,)
    )
    results = cursor.fetchall()
    conn.close()

    return results


def get_candidates_for_processing(
    require_peer_reviews: bool = True,
    exclude_processed: bool = True,
    exclude_queued: bool = True,
    limit: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    Get candidate papers for OpenEval processing.

    Args:
        require_peer_reviews: Only return papers with peer reviews
        exclude_processed: Exclude papers already processed by OpenEval
        exclude_queued: Exclude papers that are queued for processing
        limit: Maximum number of results
    """
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    query = "SELECT * FROM jats WHERE 1=1"
    params = []

    if require_peer_reviews:
        query += " AND peer_reviews = 1"

    if exclude_processed and exclude_queued:
        query += " AND openeval_status = 'UNPROCESSED'"
    elif exclude_processed:
        query += " AND openeval_status IN ('UNPROCESSED', 'QUEUED')"
    elif exclude_queued:
        query += " AND openeval_status IN ('UNPROCESSED', 'PROCESSED')"

    query += " ORDER BY id"

    if limit:
        query += f" LIMIT {limit}"

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return results


def search_by_doi(doi: str) -> Optional[Dict[str, Any]]:
    """Find paper by DOI."""
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jats WHERE doi = ?", (doi,))
    result = cursor.fetchone()
    conn.close()

    return result


def get_random_sample(
    n: int = 10,
    peer_reviews: Optional[bool] = None,
    openeval_status: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get random sample of papers.

    Args:
        n: Number of samples to return
        peer_reviews: Filter by peer review availability
        openeval_status: Filter by status ('PROCESSED', 'QUEUED', 'UNPROCESSED')
    """
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    query = "SELECT * FROM jats WHERE 1=1"
    params = []

    if peer_reviews is not None:
        query += " AND peer_reviews = ?"
        params.append(1 if peer_reviews else 0)

    if openeval_status is not None:
        query += " AND openeval_status = ?"
        params.append(openeval_status)

    query += f" ORDER BY RANDOM() LIMIT {n}"

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return results


# ============================================================================
# CLI
# ============================================================================

def main():
    """CLI interface."""
    parser = argparse.ArgumentParser(description='Query evals database')
    parser.add_argument('command', choices=[
        'stats',
        'candidates',
        'processed',
        'sample',
        'versions'
    ], help='Query command')
    parser.add_argument('--limit', type=int, help='Limit results')
    parser.add_argument('--paper-id', help='Paper ID for versions query')

    args = parser.parse_args()

    if args.command == 'stats':
        stats = get_stats()
        print("Database Statistics")
        print("=" * 60)
        for key, value in stats.items():
            print(f"  {key}: {value:,}")

    elif args.command == 'candidates':
        candidates = get_candidates_for_processing(limit=args.limit)
        print(f"Found {len(candidates)} candidates for processing")
        print("=" * 60)
        for paper in candidates[:10]:
            print(f"  {paper['id']}: {paper['xml_rel_path']}")
        if len(candidates) > 10:
            print(f"  ... and {len(candidates) - 10} more")

    elif args.command == 'processed':
        processed = get_papers_by_status(openeval_status='PROCESSED', limit=args.limit)
        print(f"Found {len(processed)} processed papers")
        print("=" * 60)
        for paper in processed[:10]:
            print(f"  {paper['id']}: {paper['xml_rel_path']}")
        if len(processed) > 10:
            print(f"  ... and {len(processed) - 10} more")

    elif args.command == 'sample':
        limit = args.limit or 10
        sample = get_random_sample(n=limit, peer_reviews=True, openeval_status='UNPROCESSED')
        print(f"Random sample of {len(sample)} papers with peer reviews (unprocessed)")
        print("=" * 60)
        for paper in sample:
            print(f"  {paper['id']}: {paper['xml_rel_path']}")

    elif args.command == 'versions':
        if not args.paper_id:
            print("Error: --paper-id required for versions command")
            return
        versions = get_paper_versions(args.paper_id)
        print(f"Found {len(versions)} versions of {args.paper_id}")
        print("=" * 60)
        for paper in versions:
            print(f"  Version {paper['version']}: {paper['id']}")
            print(f"    Peer reviews: {bool(paper['peer_reviews'])}")
            print(f"    OpenEval: {bool(paper['openeval_status'])}")


if __name__ == '__main__':
    main()
