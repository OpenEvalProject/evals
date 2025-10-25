#!/usr/bin/env python3
"""
Migrate openeval_status from boolean to enum.

Changes:
- 1 (True) -> "PROCESSED"
- 0 (False) -> "UNPROCESSED"
- Adds "QUEUED" as a third option
"""

import sqlite3
from pathlib import Path


def migrate_database(db_path: Path):
    """Migrate the database schema."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("Starting migration...")

    # Step 1: Create new table with updated schema
    print("Creating new jats_new table with enum status...")
    cursor.execute("""
        CREATE TABLE jats_new (
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

    # Step 2: Copy data with conversion
    print("Migrating data from old table to new table...")
    cursor.execute("""
        INSERT INTO jats_new
        SELECT
            id,
            doi,
            xml_rel_path,
            version,
            pub_date,
            size_bytes,
            peer_reviews,
            CASE
                WHEN openeval_status = 1 THEN 'PROCESSED'
                WHEN openeval_status = 0 THEN 'UNPROCESSED'
                ELSE 'UNPROCESSED'
            END as openeval_status,
            openeval_rel_path,
            paper_id
        FROM jats
    """)

    # Step 3: Drop old table and rename new table
    print("Replacing old table with new table...")
    cursor.execute("DROP TABLE jats")
    cursor.execute("ALTER TABLE jats_new RENAME TO jats")

    # Step 4: Recreate indexes
    print("Recreating indexes...")
    cursor.execute("CREATE INDEX idx_paper_id ON jats(paper_id)")
    cursor.execute("CREATE INDEX idx_openeval_status ON jats(openeval_status)")
    cursor.execute("CREATE INDEX idx_peer_reviews ON jats(peer_reviews)")

    conn.commit()

    # Verify migration
    cursor.execute("SELECT openeval_status, COUNT(*) FROM jats GROUP BY openeval_status")
    results = cursor.fetchall()

    print("\nMigration complete!")
    print("Status counts:")
    for status, count in results:
        print(f"  {status}: {count}")

    conn.close()


def main():
    db_path = Path(__file__).parent / 'evals.sqlite'

    if not db_path.exists():
        print(f"Error: Database not found at {db_path}")
        return

    # Backup the database first
    backup_path = db_path.parent / 'evals.sqlite.backup'
    print(f"Creating backup at {backup_path}...")
    import shutil
    shutil.copy2(db_path, backup_path)
    print("Backup created!")

    migrate_database(db_path)


if __name__ == '__main__':
    main()
