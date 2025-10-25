#!/usr/bin/env python3
"""
Sample papers uniformly by publication date.

Selects the most recent version of each paper where peer_reviews=TRUE,
sampling uniformly across years (~2 papers per month).
"""

import sqlite3
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any
from collections import defaultdict
import random


DB_PATH = Path(__file__).parent / 'evals.sqlite'


def get_papers_with_peer_reviews() -> List[Dict[str, Any]]:
    """
    Get papers with peer reviews, selecting most recent version only.

    Returns list of papers with pub_date, paper_id, jats_id, version.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get the most recent version of each paper with peer reviews
    cursor.execute("""
        SELECT
            j.id as jats_id,
            j.paper_id,
            j.version,
            j.pub_date,
            j.doi,
            j.xml_rel_path
        FROM jats j
        INNER JOIN (
            SELECT paper_id, MAX(version) as max_version
            FROM jats
            WHERE peer_reviews = 1
            AND pub_date IS NOT NULL
            AND openeval_status = 'UNPROCESSED'
            GROUP BY paper_id
        ) latest ON j.paper_id = latest.paper_id AND j.version = latest.max_version
        WHERE j.peer_reviews = 1
        AND j.pub_date IS NOT NULL
        AND j.openeval_status = 'UNPROCESSED'
        ORDER BY j.pub_date
    """)

    results = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return results


def group_papers_by_month(papers: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Group papers by year-month.

    Returns dict mapping "YYYY-MM" to list of papers.
    """
    monthly_groups = defaultdict(list)

    for paper in papers:
        pub_date = datetime.fromtimestamp(paper['pub_date'])
        month_key = pub_date.strftime('%Y-%m')
        monthly_groups[month_key].append(paper)

    return dict(monthly_groups)


def sample_papers_uniformly(
    papers: List[Dict[str, Any]],
    papers_per_month: int = 2,
    seed: int = 42
) -> List[Dict[str, Any]]:
    """
    Sample papers uniformly across months.

    Args:
        papers: List of papers to sample from
        papers_per_month: Target number of papers per month
        seed: Random seed for reproducibility

    Returns:
        List of sampled papers
    """
    random.seed(seed)

    # Group papers by month
    monthly_groups = group_papers_by_month(papers)

    # Sample from each month
    sampled_papers = []

    for month_key in sorted(monthly_groups.keys()):
        month_papers = monthly_groups[month_key]

        # Sample up to papers_per_month from this month
        n_to_sample = min(papers_per_month, len(month_papers))
        sampled = random.sample(month_papers, n_to_sample)
        sampled_papers.extend(sampled)

    return sampled_papers


def get_sampling_statistics(papers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Get statistics about the sampling."""
    if not papers:
        return {}

    monthly_groups = group_papers_by_month(papers)

    pub_dates = [datetime.fromtimestamp(p['pub_date']) for p in papers]
    min_date = min(pub_dates)
    max_date = max(pub_dates)

    yearly_counts = defaultdict(int)
    for month_key in monthly_groups:
        year = month_key.split('-')[0]
        yearly_counts[year] += len(monthly_groups[month_key])

    return {
        'total_papers': len(papers),
        'total_months': len(monthly_groups),
        'date_range': (min_date.strftime('%Y-%m-%d'), max_date.strftime('%Y-%m-%d')),
        'papers_per_month': {k: len(v) for k, v in monthly_groups.items()},
        'papers_per_year': dict(yearly_counts),
    }


def mark_papers_as_queued(paper_ids: List[str], dry_run: bool = False) -> int:
    """
    Mark papers as QUEUED in the database.

    Args:
        paper_ids: List of JATS IDs to mark as queued
        dry_run: If True, don't actually update the database

    Returns:
        Number of papers updated
    """
    if dry_run:
        return len(paper_ids)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Update in batches
    placeholders = ','.join(['?'] * len(paper_ids))
    cursor.execute(f"""
        UPDATE jats
        SET openeval_status = 'QUEUED'
        WHERE id IN ({placeholders})
    """, paper_ids)

    updated_count = cursor.rowcount
    conn.commit()
    conn.close()

    return updated_count


def save_sampled_papers(papers: List[Dict[str, Any]], output_path: Path):
    """Save sampled paper IDs to a file."""
    with open(output_path, 'w') as f:
        for paper in papers:
            f.write(f"{paper['jats_id']}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Sample papers uniformly by publication date'
    )
    parser.add_argument(
        '--papers-per-month',
        type=int,
        default=2,
        help='Target number of papers per month (default: 2)'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help='Random seed for reproducibility (default: 42)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('sampled_papers.txt'),
        help='Output file for sampled paper IDs (default: sampled_papers.txt)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be selected without updating database'
    )
    parser.add_argument(
        '--show-stats',
        action='store_true',
        help='Show detailed statistics about available papers before sampling'
    )

    args = parser.parse_args()

    print("=" * 80)
    print("Paper Sampling by Publication Date")
    print("=" * 80)
    print()

    # Get available papers
    print("Fetching papers with peer reviews (most recent version only)...")
    all_papers = get_papers_with_peer_reviews()
    print(f"Found {len(all_papers)} papers available for sampling")
    print()

    # Show statistics about available papers
    if args.show_stats or args.dry_run:
        available_stats = get_sampling_statistics(all_papers)
        print("Available Papers Statistics:")
        print(f"  Date range: {available_stats['date_range'][0]} to {available_stats['date_range'][1]}")
        print(f"  Total months covered: {available_stats['total_months']}")
        print(f"  Papers by year:")
        for year in sorted(available_stats['papers_per_year'].keys()):
            count = available_stats['papers_per_year'][year]
            print(f"    {year}: {count} papers")
        print()

    # Sample papers
    print(f"Sampling papers (target: {args.papers_per_month} per month, seed: {args.seed})...")
    sampled_papers = sample_papers_uniformly(
        all_papers,
        papers_per_month=args.papers_per_month,
        seed=args.seed
    )
    print(f"Selected {len(sampled_papers)} papers")
    print()

    # Show statistics about sampled papers
    sampled_stats = get_sampling_statistics(sampled_papers)
    print("Sampled Papers Statistics:")
    print(f"  Date range: {sampled_stats['date_range'][0]} to {sampled_stats['date_range'][1]}")
    print(f"  Total months covered: {sampled_stats['total_months']}")
    print(f"  Papers by year:")
    for year in sorted(sampled_stats['papers_per_year'].keys()):
        count = sampled_stats['papers_per_year'][year]
        avg_per_month = count / 12  # Approximate
        print(f"    {year}: {count} papers (~{avg_per_month:.1f} per month)")
    print()

    # Show sample of selected papers
    print("Sample of selected papers (first 10):")
    for paper in sampled_papers[:10]:
        pub_date = datetime.fromtimestamp(paper['pub_date']).strftime('%Y-%m-%d')
        print(f"  {paper['jats_id']:20s} {pub_date} {paper['doi']}")
    if len(sampled_papers) > 10:
        print(f"  ... and {len(sampled_papers) - 10} more")
    print()

    if args.dry_run:
        print("DRY RUN - No changes made to database")
        print(f"Would save paper IDs to: {args.output}")
    else:
        # Save to file
        save_sampled_papers(sampled_papers, args.output)
        print(f"✓ Saved paper IDs to: {args.output}")

        # Mark as QUEUED
        paper_ids = [p['jats_id'] for p in sampled_papers]
        updated = mark_papers_as_queued(paper_ids, dry_run=False)
        print(f"✓ Marked {updated} papers as QUEUED in database")

    print()
    print("=" * 80)


if __name__ == '__main__':
    main()
