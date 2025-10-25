# Evals Database

SQLite database tracking JATS XML manuscripts and their OpenEval processing status.

## Database Location

`evals.sqlite` in this directory.

## Schema

### `paper` table
- `id` (TEXT, PRIMARY KEY): Paper ID (e.g., "elife-00003")

### `jats` table
- `id` (TEXT, PRIMARY KEY): JATS version ID (e.g., "elife-00003-v1")
- `doi` (TEXT): Digital Object Identifier
- `xml_rel_path` (TEXT): Relative path to XML file from project root
- `version` (INTEGER): Version number (extracted from filename)
- `pub_date` (INTEGER): Publication date as Unix timestamp
- `size_bytes` (INTEGER): Size of XML file in bytes
- `peer_reviews` (BOOLEAN): Whether peer reviews exist (reviews.md file)
- `openeval_status` (TEXT): Processing status - one of:
  - `PROCESSED`: OpenEval workflow completed (claims.json + eval_llm.json exist)
  - `QUEUED`: Marked for processing
  - `UNPROCESSED`: Not yet processed
- `openeval_rel_path` (TEXT): Relative path to OpenEval output directory
- `paper_id` (TEXT, FOREIGN KEY): Reference to paper table

## Building/Updating the Database

Run the build script to create or update the database:

```bash
python3 build_evals_db.py
```

This scans all XML files in `manuscripts/` and:
1. Extracts metadata from existing `manuscript_metadata.json` files
2. Checks for peer reviews (`reviews.md` files)
3. Checks for OpenEval processing status (claims/results JSON files)
4. Populates the database

## Querying the Database

### Using the query script

```bash
# Get statistics
python3 query_evals_db.py stats

# Get random sample of unprocessed papers with peer reviews
python3 query_evals_db.py sample --limit 10

# List all processed papers
python3 query_evals_db.py processed

# List candidates for processing
python3 query_evals_db.py candidates --limit 100

# Check all versions of a paper
python3 query_evals_db.py versions --paper-id elife-00003
```

### Direct SQL queries

```bash
# Papers with peer reviews but not processed
sqlite3 evals.sqlite "SELECT id, doi FROM jats WHERE peer_reviews = 1 AND openeval_status = 'UNPROCESSED' LIMIT 10"

# Papers by status
sqlite3 evals.sqlite "SELECT openeval_status, COUNT(*) FROM jats GROUP BY openeval_status"

# Papers by publication year
sqlite3 evals.sqlite "SELECT strftime('%Y', datetime(pub_date, 'unixepoch')) as year, COUNT(*) FROM jats GROUP BY year ORDER BY year"

# Papers with multiple versions
sqlite3 evals.sqlite "SELECT paper_id, COUNT(*) as versions FROM jats GROUP BY paper_id HAVING versions > 1 ORDER BY versions DESC LIMIT 10"
```

## Updating Paper Status

Use the `update_status.py` script to mark papers as QUEUED or update their status:

```bash
# Mark papers as queued for processing
python3 update_status.py QUEUED --ids elife-00003-v1 elife-00005-v1

# Mark papers as processed
python3 update_status.py PROCESSED --ids elife-00003-v1

# Bulk update from file (one JATS ID per line)
python3 update_status.py QUEUED --file papers_to_queue.txt
```

## Python API

```python
from query_evals_db import (
    get_stats,
    get_candidates_for_processing,
    get_paper_versions,
    search_by_doi
)

# Get stats
stats = get_stats()
print(f"Total papers: {stats['total_papers']}")

# Get 100 candidates for processing
candidates = get_candidates_for_processing(limit=100)
for paper in candidates:
    print(f"{paper['id']}: {paper['xml_rel_path']}")

# Find paper by DOI
paper = search_by_doi("10.7554/eLife.00003")
print(paper)
```

## Statistics (as of last build)

- Total papers: 18,480
- Total JATS versions: 30,765
- With peer reviews: 18,553
- Status breakdown:
  - PROCESSED: 244
  - QUEUED: 0
  - UNPROCESSED: 30,521
- With DOI: 30,738
- With pub_date: 30,738

## Notes

- The database uses relative paths from the project root for portability
- Metadata is loaded from existing `manuscript_metadata.json` files (created by `jats convert`)
- Run `build_evals_db.py` periodically to update the database as new manuscripts are processed
- The database is ~6MB in size
