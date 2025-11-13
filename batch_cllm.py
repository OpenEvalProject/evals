#!/usr/bin/env python3
"""
Batch run CLLM on converted manuscripts.

This script processes converted manuscript folders, running the full CLLM
workflow (extract, eval LLM, eval peer, compare, db_export) and saving
all outputs to prepare for database import.

Usage:
    python batch_cllm.py [--dry-run] [--limit N] [--continue-on-error] [--force] [--parallel N] [--reverse]

Options:
    --dry-run, -n          Show what would be done without processing
    --limit N, -l N        Only process first N manuscript versions
    --continue-on-error    Continue processing even if CLLM fails
    --force, -f            Overwrite existing CLLM outputs
    --parallel N, -p N     Process N manuscripts in parallel (default: 10, use 1 for sequential)
    --reverse, -r          Process manuscripts in reverse order (newest first)
"""

import json
import re
import sqlite3
import subprocess
import sys
import threading
from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

# Path to CLLM tool in its venv
CLLM_BIN = Path(__file__).parent.parent / "cllm" / ".venv" / "bin" / "cllm"

# Path to database
DB_PATH = Path(__file__).parent / "evals.sqlite"

# Global lock for thread-safe printing
print_lock = threading.Lock()


def safe_print(*args, **kwargs):
    """Thread-safe print function."""
    with print_lock:
        print(*args, **kwargs)


def get_queued_papers_from_db():
    """
    Get list of papers with QUEUED status from database.

    Returns:
        List of dicts with jats_id and openeval_rel_path
    """
    if not DB_PATH.exists():
        return None

    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, openeval_rel_path
            FROM jats
            WHERE openeval_status = 'QUEUED'
            ORDER BY pub_date
        """)

        results = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return results
    except Exception as e:
        print(f"Warning: Failed to read database: {e}")
        return None


def update_paper_status(jats_id: str, new_status: str):
    """
    Update paper status in database.

    Args:
        jats_id: JATS ID (e.g., "elife-00003-v1")
        new_status: New status ('PROCESSED', 'QUEUED', 'UNPROCESSED')
    """
    if not DB_PATH.exists():
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE jats
            SET openeval_status = ?
            WHERE id = ?
        """, (new_status, jats_id))

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Warning: Failed to update database status for {jats_id}: {e}")


def has_peer_reviews(version_dir: Path) -> bool:
    """Check if this version has peer reviews."""
    # Look for reviews.md file
    reviews_file = version_dir / "reviews.md"
    if not reviews_file.exists():
        return False

    # Check if file has content (not empty)
    if reviews_file.stat().st_size > 100:  # More than 100 bytes
        return True

    return False


def create_db_export(version_dir: Path) -> bool:
    """
    Create database export JSON from CLLM workflow outputs.

    Calls the helper script using CLLM's venv Python to access dependencies.

    Args:
        version_dir: Version directory containing CLLM outputs

    Returns:
        True if export succeeded, False otherwise
    """
    try:
        # Path to helper script and CLLM venv Python
        helper_script = Path(__file__).parent / "create_db_export.py"
        cllm_python = Path(__file__).parent.parent / "cllm" / ".venv" / "bin" / "python"

        if not cllm_python.exists():
            print(f"      ✗ CLLM Python not found at {cllm_python}")
            return False

        # Run helper script in CLLM venv
        result = subprocess.run(
            [str(cllm_python), str(helper_script), str(version_dir)],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
            print(f"      ✗ DB export failed: {result.stderr}")
            return False

        return True

    except subprocess.TimeoutExpired:
        print(f"      ✗ DB export timed out")
        return False
    except Exception as e:
        print(f"      ✗ DB export error: {e}")
        return False


def run_cllm_workflow(
    version_dir: Path,
    manuscript_file: Path,
    peer_reviews_file: Path | None,
    dry_run: bool = False,
    verbose: bool = True,
    metrics: bool = False,
    use_safe_print: bool = False,
    enable_filter: bool = True,
) -> bool:
    """
    Run the full CLLM workflow on a manuscript version.

    Workflow stages:
    1. Extract claims from manuscript
    2. Evaluate claims with LLM
    3. Evaluate claims with peer reviews (if available)
    4. Compare LLM and peer evaluations (if peer reviews available)
    5. Create database export JSON

    Args:
        version_dir: Version directory (e.g., elife-00003/v1/)
        manuscript_file: Path to manuscript markdown file
        peer_reviews_file: Path to peer reviews file (optional)
        dry_run: If True, only print what would be done
        verbose: Enable verbose logging
        metrics: Enable metrics generation (automatically enables verbose)
        use_safe_print: If True, use thread-safe printing
        enable_filter: If True, filter claims to only include those with sources in JATS XML

    Returns:
        True if workflow succeeded, False otherwise
    """
    _print = safe_print if use_safe_print else print

    # Detect XML file for claim filtering
    xml_file = None
    if enable_filter:
        # Look for XML symlink in the parent directory (article directory)
        article_dir = version_dir.parent
        # Pattern: elife-XXXXX-vX.xml (symlink)
        xml_symlinks = list(article_dir.glob("elife-*-v*.xml"))

        # Filter to find the one matching this version
        version_name = version_dir.name  # e.g., "v1"
        for xml_symlink in xml_symlinks:
            # Check if symlink name contains the version
            if version_name in xml_symlink.name and xml_symlink.is_symlink():
                xml_file = xml_symlink
                break

        if not xml_file:
            _print(f"      ⚠️  Warning: No XML file found for filtering, filtering disabled")
            enable_filter = False
    # Output file paths
    claims_file = version_dir / "claims.json"
    eval_llm_file = version_dir / "eval_llm.json"
    eval_peer_file = version_dir / "eval_peer.json"
    cmp_file = version_dir / "cmp.json"
    db_export_file = version_dir / "db_export.json"

    if dry_run:
        _print(f"      → Would run CLLM workflow:")
        _print(f"        1. Extract claims -> {claims_file.name}")
        if metrics:
            _print(f"           Metrics: metrics_extract.json")
        _print(f"        2. Evaluate (LLM) -> {eval_llm_file.name}")
        if metrics:
            _print(f"           Metrics: metrics_eval_openeval.json")
        if peer_reviews_file:
            _print(f"        3. Evaluate (peer) -> {eval_peer_file.name}")
            if metrics:
                _print(f"           Metrics: metrics_eval_peer.json")
            _print(f"        4. Compare -> {cmp_file.name}")
            if metrics:
                _print(f"           Metrics: metrics_cmp.json")
        _print(f"        5. Database export -> {db_export_file.name}")
        return True

    if not CLLM_BIN.exists():
        _print(f"      ✗ CLLM binary not found at {CLLM_BIN}")
        return False

    # Metrics flag automatically enables verbose for all commands
    verbose_flag = ["-v"] if (verbose or metrics) else []

    try:
        # Stage 1: Extract claims
        _print(f"      [1/5] Extracting claims...")

        # Build extract command with optional filtering
        extract_cmd = [
            str(CLLM_BIN),
            "extract",
            str(manuscript_file),
            "-o", str(claims_file),
            *verbose_flag,
        ]

        # Add filtering flags if enabled
        if enable_filter and xml_file:
            extract_cmd.extend(["--filter", "--xml", str(xml_file)])

        result = subprocess.run(
            extract_cmd,
            capture_output=True,
            text=True,
            timeout=600,
        )

        if result.returncode != 0:
            _print(f"      ✗ Claim extraction failed: {result.stderr}")
            return False

        # Stage 2: Evaluate with LLM
        _print(f"      [2/5] Evaluating claims (LLM)...")
        result = subprocess.run(
            [
                str(CLLM_BIN),
                "eval",
                str(manuscript_file),
                "-c", str(claims_file),
                "-o", str(eval_llm_file),
                *verbose_flag,
            ],
            capture_output=True,
            text=True,
            timeout=600,
        )

        if result.returncode != 0:
            _print(f"      ✗ LLM evaluation failed: {result.stderr}")
            return False

        # Stage 3: Evaluate with peer reviews (if available)
        if peer_reviews_file:
            _print(f"      [3/5] Evaluating claims (peer reviews)...")
            result = subprocess.run(
                [
                    str(CLLM_BIN),
                    "eval",
                    str(manuscript_file),
                    "-c", str(claims_file),
                    "-p", str(peer_reviews_file),
                    "-o", str(eval_peer_file),
                    *verbose_flag,
                ],
                capture_output=True,
                text=True,
                timeout=600,
            )

            if result.returncode != 0:
                _print(f"      ✗ Peer evaluation failed: {result.stderr}")
                return False

            # Stage 4: Compare evaluations
            _print(f"      [4/5] Comparing evaluations...")
            result = subprocess.run(
                [
                    str(CLLM_BIN),
                    "cmp",
                    str(eval_peer_file),
                    str(eval_llm_file),
                    "-o", str(cmp_file),
                    *verbose_flag,
                ],
                capture_output=True,
                text=True,
                timeout=600,
            )

            if result.returncode != 0:
                _print(f"      ✗ Comparison failed: {result.stderr}")
                return False
        else:
            _print(f"      [3/5] Skipping peer evaluation (no reviews)")
            _print(f"      [4/5] Skipping comparison (no peer evaluation)")

        # Stage 5: Create database export
        _print(f"      [5/5] Creating database export...")
        success = create_db_export(version_dir)

        if not success:
            _print(f"      ✗ Database export failed")
            return False

        _print(f"      ✓ CLLM workflow completed")
        _print(f"        Files: {claims_file.name}, {eval_llm_file.name}", end="")
        if peer_reviews_file:
            _print(f", {eval_peer_file.name}, {cmp_file.name}, {db_export_file.name}")
        else:
            _print(f", {db_export_file.name}")

        return True

    except subprocess.TimeoutExpired:
        _print(f"      ✗ CLLM workflow timed out")
        return False
    except Exception as e:
        _print(f"      ✗ Error: {e}")
        return False


def process_single_manuscript(args):
    """
    Wrapper function to process a single manuscript (used for parallel processing).

    Args:
        args: Tuple of (index, total, jats_id, article_id, version_dir, manuscript_file, force, dry_run, verbose, metrics, enable_filter)

    Returns:
        Tuple of (jats_id, article_id, version_name, status, message)
        where status is 'success', 'skipped', or 'failed'
    """
    i, total, jats_id, article_id, version_dir, manuscript_file, force, dry_run, verbose, metrics, enable_filter = args
    version_name = version_dir.name

    # Check if already processed (look for db_export.json - the final output file)
    db_export_file = version_dir / "db_export.json"
    if not force and db_export_file.exists():
        safe_print(f"📄 [{i}/{total}] {article_id}/{version_name} ({jats_id})")
        safe_print(f"      ⏭️  Already processed (use --force to overwrite)")
        safe_print()
        return (jats_id, article_id, version_name, 'skipped', 'Already processed')

    safe_print(f"📄 [{i}/{total}] {article_id}/{version_name} ({jats_id})")

    # Check for peer reviews
    peer_reviews_file = None
    reviews_file = version_dir / "reviews.md"
    if reviews_file.exists() and has_peer_reviews(version_dir):
        peer_reviews_file = reviews_file
        safe_print(f"      📝 Peer reviews: {peer_reviews_file.name}")
    else:
        safe_print(f"      📝 No peer reviews")

    # Run CLLM workflow
    success = run_cllm_workflow(
        version_dir,
        manuscript_file,
        peer_reviews_file,
        dry_run=dry_run,
        verbose=verbose,
        metrics=metrics,
        use_safe_print=True,
        enable_filter=enable_filter,
    )

    # Update database status
    if success and not dry_run:
        update_paper_status(jats_id, 'PROCESSED')
        safe_print(f"      ✓ Updated database status to PROCESSED")

    safe_print()

    if success:
        return (jats_id, article_id, version_name, 'success', 'Completed')
    else:
        return (jats_id, article_id, version_name, 'failed', 'Workflow failed')


def process_manuscript_versions(
    manuscripts_dir: Path,
    limit: int | None = None,
    dry_run: bool = False,
    continue_on_error: bool = False,
    force: bool = False,
    verbose: bool = True,
    parallel: int = 1,
    reverse: bool = False,
    use_database: bool = True,
    metrics: bool = False,
    enable_filter: bool = True,
) -> tuple[int, int, int, int]:
    """
    Process manuscript version folders.

    Args:
        manuscripts_dir: Directory containing organized manuscript folders
        limit: Optional limit on number of versions to process
        dry_run: If True, only print what would be done
        continue_on_error: If True, continue processing even if CLLM fails
        force: If True, overwrite existing CLLM outputs
        verbose: Enable verbose CLLM logging
        parallel: Number of manuscripts to process in parallel (1 for sequential)
        reverse: If True, process manuscripts in reverse order (newest first)
        use_database: If True, only process papers with QUEUED status from database
        metrics: If True, generate metrics files for each workflow stage
        enable_filter: If True, filter claims to only include those with sources in JATS XML

    Returns:
        (total_processed, successful, failed, skipped)
    """
    # Build list of papers to process
    version_dirs = []

    if use_database:
        # Get QUEUED papers from database
        queued_papers = get_queued_papers_from_db()

        if queued_papers is None:
            print("❌ Error: Could not read database. Use --no-db to process all papers.")
            return 0, 0, 0, 0

        print(f"📊 Found {len(queued_papers)} QUEUED papers in database")

        # Build paths from database entries
        for paper in queued_papers:
            jats_id = paper['id']
            openeval_rel_path = paper['openeval_rel_path']

            # Construct the version directory path
            version_dir = manuscripts_dir.parent / openeval_rel_path
            manuscript_file = version_dir / "manuscript.md"

            if not version_dir.exists():
                print(f"⚠️  Warning: Directory not found for {jats_id}: {version_dir}")
                continue

            if not manuscript_file.exists():
                print(f"⚠️  Warning: Manuscript file not found for {jats_id}: {manuscript_file}")
                continue

            # Extract article_id from jats_id (e.g., "elife-00003-v1" -> "elife-00003")
            article_id = '-'.join(jats_id.split('-')[:-1])

            version_dirs.append((jats_id, article_id, version_dir, manuscript_file))

    else:
        # Get all manuscript directories (original behavior)
        manuscript_dirs_list = sorted([d for d in manuscripts_dir.iterdir() if d.is_dir()])

        # Build list of all version directories
        for manuscript_dir in manuscript_dirs_list:
            article_id = manuscript_dir.name
            # Find all version directories (v1, v2, etc.)
            for version_dir in sorted(manuscript_dir.glob("v*")):
                if version_dir.is_dir():
                    # Check if this version has a manuscript file
                    manuscript_file = version_dir / "manuscript.md"
                    if manuscript_file.exists():
                        # Construct jats_id from article_id and version
                        version_name = version_dir.name  # e.g., "v1"
                        jats_id = f"{article_id}-{version_name}"
                        version_dirs.append((jats_id, article_id, version_dir, manuscript_file))

    # Reverse order if requested
    if reverse:
        version_dirs = version_dirs[::-1]

    if limit:
        version_dirs = version_dirs[:limit]

    total = len(version_dirs)
    successful = 0
    failed = 0
    skipped = 0

    print(f"\n📊 Processing {total} manuscript versions...")
    if parallel > 1:
        print(f"⚡ Parallel mode: {parallel} concurrent processes\n")
    else:
        print()

    # Choose sequential or parallel processing
    if parallel <= 1:
        # Sequential processing
        for i, (jats_id, article_id, version_dir, manuscript_file) in enumerate(version_dirs, 1):
            version_name = version_dir.name  # e.g., "v1"

            # Check if already processed (look for db_export.json - the final output file)
            db_export_file = version_dir / "db_export.json"
            if not force and db_export_file.exists():
                print(f"📄 [{i}/{total}] {article_id}/{version_name} ({jats_id})")
                print(f"      ⏭️  Already processed (use --force to overwrite)")
                skipped += 1
                print()
                continue

            print(f"📄 [{i}/{total}] {article_id}/{version_name} ({jats_id})")

            # Check for peer reviews
            peer_reviews_file = None
            reviews_file = version_dir / "reviews.md"
            if reviews_file.exists() and has_peer_reviews(version_dir):
                peer_reviews_file = reviews_file
                print(f"      📝 Peer reviews: {peer_reviews_file.name}")
            else:
                print(f"      📝 No peer reviews")

            # Run CLLM workflow
            success = run_cllm_workflow(
                version_dir,
                manuscript_file,
                peer_reviews_file,
                dry_run=dry_run,
                verbose=verbose,
                metrics=metrics,
                enable_filter=enable_filter,
            )

            # Update database status
            if success and not dry_run:
                update_paper_status(jats_id, 'PROCESSED')
                print(f"      ✓ Updated database status to PROCESSED")

            if success:
                successful += 1
            else:
                failed += 1
                if not continue_on_error:
                    print(f"\n❌ Stopping due to error. Use --continue-on-error to continue.\n")
                    return i, successful, failed, skipped

            print()
    else:
        # Parallel processing
        # Prepare arguments for each manuscript
        tasks = [
            (i, total, jats_id, article_id, version_dir, manuscript_file, force, dry_run, verbose, metrics, enable_filter)
            for i, (jats_id, article_id, version_dir, manuscript_file) in enumerate(version_dirs, 1)
        ]

        # Process in parallel
        with ProcessPoolExecutor(max_workers=parallel) as executor:
            # Submit all tasks
            futures = {executor.submit(process_single_manuscript, task): task for task in tasks}

            # Collect results as they complete
            for future in as_completed(futures):
                try:
                    jats_id, article_id, version_name, status, message = future.result()

                    if status == 'success':
                        successful += 1
                    elif status == 'skipped':
                        skipped += 1
                    elif status == 'failed':
                        failed += 1
                        if not continue_on_error:
                            # Cancel remaining tasks
                            for f in futures:
                                f.cancel()
                            safe_print(f"\n❌ Stopping due to error. Use --continue-on-error to continue.\n")
                            # Return current counts
                            processed = successful + skipped + failed
                            return processed, successful, failed, skipped

                except Exception as e:
                    safe_print(f"❌ Error processing manuscript: {e}")
                    failed += 1
                    if not continue_on_error:
                        safe_print(f"\n❌ Stopping due to error. Use --continue-on-error to continue.\n")
                        processed = successful + skipped + failed
                        return processed, successful, failed, skipped

    return total, successful, failed, skipped


def main():
    """Main entry point."""
    parser = ArgumentParser(
        description="Batch run CLLM workflow on converted manuscripts."
    )

    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would be done without processing"
    )

    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=None,
        help="Only process first N manuscript versions"
    )

    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue processing even if CLLM fails"
    )

    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Overwrite existing CLLM outputs (default: skip already processed)"
    )

    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Disable verbose CLLM logging"
    )

    parser.add_argument(
        "--parallel", "-p",
        type=int,
        default=10,
        help="Process N manuscripts in parallel (default: 10, use 1 for sequential)"
    )

    parser.add_argument(
        "--reverse", "-r",
        action="store_true",
        help="Process manuscripts in reverse order (newest first)"
    )

    parser.add_argument(
        "--no-db",
        action="store_true",
        help="Don't use database filtering (process all manuscripts in filesystem)"
    )

    parser.add_argument(
        "--metrics", "-m",
        action="store_true",
        help="Generate metrics files for each workflow stage (enables verbose mode)"
    )

    parser.add_argument(
        "--no-filter",
        action="store_true",
        help="Disable claim filtering (by default, claims are filtered to only include those with sources in JATS XML)"
    )

    args = parser.parse_args()

    # Setup paths
    base_dir = Path(__file__).parent
    manuscripts_dir = base_dir / "manuscripts"

    if not manuscripts_dir.exists():
        print(f"❌ Error: Manuscripts directory not found: {manuscripts_dir}")
        print("   Run batch_convert.py first!")
        sys.exit(1)

    print("=" * 70)
    print("CLLM Batch Processor")
    print("=" * 70)
    print(f"Manuscripts directory: {manuscripts_dir}")
    if args.no_db:
        print("Selection mode: Filesystem-based (processing all manuscripts)")
    else:
        print("Selection mode: Database-filtered (processing QUEUED papers only)")
    if args.limit:
        print(f"Limit: {args.limit} versions")
    if args.parallel > 1:
        print(f"Parallel processing: {args.parallel} concurrent processes")
    else:
        print(f"Sequential processing")
    if args.reverse:
        print("Order: Reverse (newest first)")
    else:
        print("Order: Forward (oldest first)")
    if args.dry_run:
        print("Mode: DRY RUN (no processing will be performed)")
    if args.continue_on_error:
        print("Error handling: Continue on error")
    if args.force:
        print("Mode: FORCE (overwriting existing outputs)")
    else:
        print("Mode: Skip already processed (use --force to overwrite)")
    if args.metrics:
        print("Metrics: Enabled (generating metrics files for each stage)")
    if args.no_filter:
        print("Claim filtering: Disabled (--no-filter)")
    else:
        print("Claim filtering: Enabled (sources verified in JATS XML)")
    print("=" * 70)

    try:
        total, successful, failed, skipped = process_manuscript_versions(
            manuscripts_dir,
            limit=args.limit,
            dry_run=args.dry_run,
            continue_on_error=args.continue_on_error,
            force=args.force,
            verbose=not args.quiet,
            parallel=args.parallel,
            reverse=args.reverse,
            use_database=not args.no_db,
            metrics=args.metrics,
            enable_filter=not args.no_filter,
        )

        print("=" * 70)
        print("CLLM Batch Processing Summary")
        print("=" * 70)
        print(f"Total versions: {total}")
        print(f"Successful: {successful}")
        print(f"Skipped: {skipped}")
        print(f"Failed: {failed}")
        print("=" * 70)

        if failed > 0:
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
