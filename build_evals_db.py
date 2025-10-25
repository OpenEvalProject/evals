#!/usr/bin/env python3
"""
Build SQLite database to track JATS XML files and their processing status.

This script scans the manuscripts directory and creates/updates a SQLite database
with metadata about each XML file and its associated OpenEval processing.
"""

import sqlite3
import json
import os
import re
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any


def create_database(db_path: Path) -> sqlite3.Connection:
    """Create the SQLite database with the required schema."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create paper table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS paper (
            id TEXT PRIMARY KEY
        )
    """)

    # Create jats table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jats (
            id TEXT PRIMARY KEY,
            doi TEXT,
            xml_rel_path TEXT NOT NULL,
            version INTEGER NOT NULL,
            pub_date INTEGER,
            size_bytes INTEGER NOT NULL,
            peer_reviews BOOLEAN NOT NULL,
            openeval_status TEXT NOT NULL CHECK(openeval_status IN ('PROCESSED', 'UNPROCESSED', 'QUEUED')),
            openeval_rel_path TEXT,
            paper_id TEXT NOT NULL,
            FOREIGN KEY (paper_id) REFERENCES paper (id)
        )
    """)

    # Create indexes for common queries
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_paper_id ON jats(paper_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_openeval_status ON jats(openeval_status)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_peer_reviews ON jats(peer_reviews)")

    conn.commit()
    return conn


def parse_jats_id(xml_filename: str) -> tuple[str, int]:
    """
    Parse JATS ID and version from filename.

    Example: 'elife-00003-v1.xml' -> ('elife-00003-v1', 1)
    """
    match = re.match(r'(elife-\d+)-v(\d+)\.xml', xml_filename)
    if not match:
        raise ValueError(f"Invalid JATS filename format: {xml_filename}")

    jats_id = f"{match.group(1)}-v{match.group(2)}"
    version = int(match.group(2))

    return jats_id, version


def parse_paper_id(xml_filename: str) -> str:
    """
    Parse paper ID from filename.

    Example: 'elife-00003-v1.xml' -> 'elife-00003'
    """
    match = re.match(r'(elife-\d+)-v\d+\.xml', xml_filename)
    if not match:
        raise ValueError(f"Invalid JATS filename format: {xml_filename}")

    return match.group(1)


def get_jats_metadata_from_file(openeval_dir: Path) -> Optional[Dict[str, Any]]:
    """
    Get metadata from manuscript_metadata.json file if it exists.

    Returns dict with 'doi' and 'pub_date' keys, or None if metadata cannot be retrieved.
    """
    metadata_file = openeval_dir / 'manuscript_metadata.json'

    if not metadata_file.exists():
        return None

    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)

        # Parse pub_date to unix timestamp
        pub_date_unix = None
        if 'pub_date' in metadata and metadata['pub_date']:
            try:
                dt = datetime.strptime(metadata['pub_date'], '%Y-%m-%d')
                pub_date_unix = int(dt.timestamp())
            except Exception as e:
                # Try without time parsing if format is different
                pass

        return {
            'doi': metadata.get('doi'),
            'pub_date': pub_date_unix
        }

    except Exception as e:
        print(f"Warning: Error reading metadata from {metadata_file}: {e}")
        return None


def check_peer_reviews(openeval_dir: Path) -> bool:
    """Check if peer reviews exist (reviews.md file)."""
    if not openeval_dir.exists():
        return False

    reviews_file = openeval_dir / 'reviews.md'
    return reviews_file.exists()


def check_openeval_status(openeval_dir: Path) -> str:
    """
    Check OpenEval workflow status.

    Returns:
        "PROCESSED" if claims.json and eval_llm.json exist
        "UNPROCESSED" otherwise
    """
    if not openeval_dir.exists():
        return "UNPROCESSED"

    claims_file = openeval_dir / 'claims.json'
    eval_file = openeval_dir / 'eval_llm.json'

    if claims_file.exists() and eval_file.exists():
        return "PROCESSED"
    else:
        return "UNPROCESSED"


def process_xml_file(
    xml_path: Path,
    manuscripts_dir: Path,
    conn: sqlite3.Connection
) -> None:
    """Process a single XML file and add/update its record in the database."""
    cursor = conn.cursor()

    # Parse IDs
    jats_id, version = parse_jats_id(xml_path.name)
    paper_id = parse_paper_id(xml_path.name)

    # Get XML file size
    size_bytes = xml_path.stat().st_size

    # Get relative path from manuscripts directory
    xml_rel_path = os.path.relpath(xml_path, manuscripts_dir.parent)

    # Determine OpenEval directory path
    paper_dir = xml_path.parent
    openeval_dir = paper_dir / f"v{version}"
    openeval_rel_path = os.path.relpath(openeval_dir, manuscripts_dir.parent)

    # Get metadata from manuscript_metadata.json file
    metadata = get_jats_metadata_from_file(openeval_dir)
    doi = metadata['doi'] if metadata else None
    pub_date = metadata['pub_date'] if metadata else None

    # Check for peer reviews and OpenEval status
    peer_reviews = check_peer_reviews(openeval_dir)
    openeval_status = check_openeval_status(openeval_dir)

    # Insert paper if not exists
    cursor.execute(
        "INSERT OR IGNORE INTO paper (id) VALUES (?)",
        (paper_id,)
    )

    # Insert or replace JATS record
    cursor.execute("""
        INSERT OR REPLACE INTO jats
        (id, doi, xml_rel_path, version, pub_date, size_bytes, peer_reviews,
         openeval_status, openeval_rel_path, paper_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        jats_id,
        doi,
        xml_rel_path,
        version,
        pub_date,
        size_bytes,
        peer_reviews,
        openeval_status,
        openeval_rel_path,
        paper_id
    ))

    conn.commit()


def scan_and_populate(
    manuscripts_dir: Path,
    db_path: Path,
    verbose: bool = True
) -> Dict[str, int]:
    """
    Scan manuscripts directory and populate database.

    Returns dict with statistics about the scan.
    """
    conn = create_database(db_path)

    # Find all XML files
    xml_files = list(manuscripts_dir.glob('*/elife-*-v*.xml'))

    stats = {
        'total_files': len(xml_files),
        'processed': 0,
        'errors': 0
    }

    for xml_path in xml_files:
        try:
            if verbose and stats['processed'] % 100 == 0:
                print(f"Processing {stats['processed']}/{stats['total_files']}...")

            process_xml_file(xml_path, manuscripts_dir, conn)
            stats['processed'] += 1

        except Exception as e:
            print(f"Error processing {xml_path}: {e}")
            stats['errors'] += 1

    conn.close()
    return stats


def main():
    """Main entry point."""
    # Set up paths
    script_dir = Path(__file__).parent
    manuscripts_dir = script_dir / 'manuscripts'
    db_path = script_dir / 'evals.sqlite'

    print(f"Building database: {db_path}")
    print(f"Scanning manuscripts in: {manuscripts_dir}")
    print()

    # Scan and populate
    stats = scan_and_populate(manuscripts_dir, db_path, verbose=True)

    print()
    print("=" * 60)
    print(f"Database build complete!")
    print(f"  Total XML files found: {stats['total_files']}")
    print(f"  Successfully processed: {stats['processed']}")
    print(f"  Errors: {stats['errors']}")
    print(f"  Database location: {db_path}")
    print("=" * 60)

    # Print some summary statistics
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM paper")
    paper_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats")
    jats_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE peer_reviews = 1")
    peer_reviews_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE openeval_status = 'PROCESSED'")
    processed_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE openeval_status = 'QUEUED'")
    queued_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jats WHERE openeval_status = 'UNPROCESSED'")
    unprocessed_count = cursor.fetchone()[0]

    print()
    print("Summary Statistics:")
    print(f"  Total papers: {paper_count}")
    print(f"  Total JATS versions: {jats_count}")
    print(f"  With peer reviews: {peer_reviews_count}")
    print(f"  Status breakdown:")
    print(f"    PROCESSED: {processed_count}")
    print(f"    QUEUED: {queued_count}")
    print(f"    UNPROCESSED: {unprocessed_count}")

    conn.close()


if __name__ == '__main__':
    main()
