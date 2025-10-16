#!/usr/bin/env python3
"""
Batch run CLLM on converted manuscripts.

This script processes converted manuscript folders, running the full CLLM
workflow (extract, eval LLM, eval peer, compare, db_export) and saving
all outputs to prepare for database import.

Usage:
    python batch_cllm.py [--dry-run] [--limit N] [--continue-on-error] [--force]

Options:
    --dry-run, -n          Show what would be done without processing
    --limit N, -l N        Only process first N manuscript versions
    --continue-on-error    Continue processing even if CLLM fails
    --force, -f            Overwrite existing CLLM outputs
"""

import json
import re
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path

# Path to CLLM tool in its venv
CLLM_BIN = Path(__file__).parent.parent / "cllm" / ".venv" / "bin" / "cllm"


def has_peer_reviews(version_dir: Path) -> bool:
    """Check if this version has peer reviews."""
    # Look for reviews_v*.md files
    review_files = list(version_dir.glob("reviews_v*.md"))
    if not review_files:
        return False

    # Check if file has content (not empty)
    for review_file in review_files:
        if review_file.stat().st_size > 100:  # More than 100 bytes
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

    Returns:
        True if workflow succeeded, False otherwise
    """
    # Output file paths
    claims_file = version_dir / "claims.json"
    eval_llm_file = version_dir / "eval_llm.json"
    eval_peer_file = version_dir / "eval_peer.json"
    cmp_file = version_dir / "cmp.json"
    db_export_file = version_dir / "db_export.json"

    if dry_run:
        print(f"      → Would run CLLM workflow:")
        print(f"        1. Extract claims -> {claims_file.name}")
        print(f"        2. Evaluate (LLM) -> {eval_llm_file.name}")
        if peer_reviews_file:
            print(f"        3. Evaluate (peer) -> {eval_peer_file.name}")
            print(f"        4. Compare -> {cmp_file.name}")
        print(f"        5. Database export -> {db_export_file.name}")
        return True

    if not CLLM_BIN.exists():
        print(f"      ✗ CLLM binary not found at {CLLM_BIN}")
        return False

    verbose_flag = ["-v"] if verbose else []

    try:
        # Stage 1: Extract claims
        print(f"      [1/4] Extracting claims...")
        result = subprocess.run(
            [
                str(CLLM_BIN),
                "extract",
                str(manuscript_file),
                "-o", str(claims_file),
                *verbose_flag,
            ],
            capture_output=True,
            text=True,
            timeout=300,
        )

        if result.returncode != 0:
            print(f"      ✗ Claim extraction failed: {result.stderr}")
            return False

        # Stage 2: Evaluate with LLM
        print(f"      [2/4] Evaluating claims (LLM)...")
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
            timeout=300,
        )

        if result.returncode != 0:
            print(f"      ✗ LLM evaluation failed: {result.stderr}")
            return False

        # Stage 3: Evaluate with peer reviews (if available)
        if peer_reviews_file:
            print(f"      [3/4] Evaluating claims (peer reviews)...")
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
                timeout=300,
            )

            if result.returncode != 0:
                print(f"      ✗ Peer evaluation failed: {result.stderr}")
                return False

            # Stage 4: Compare evaluations
            print(f"      [4/4] Comparing evaluations...")
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
                timeout=300,
            )

            if result.returncode != 0:
                print(f"      ✗ Comparison failed: {result.stderr}")
                return False
        else:
            print(f"      [3/4] Skipping peer evaluation (no reviews)")
            print(f"      [4/4] Skipping comparison (no peer evaluation)")

        # Stage 5: Create database export
        print(f"      [5/5] Creating database export...")
        success = create_db_export(version_dir)

        if not success:
            print(f"      ✗ Database export failed")
            return False

        print(f"      ✓ CLLM workflow completed")
        print(f"        Files: {claims_file.name}, {eval_llm_file.name}", end="")
        if peer_reviews_file:
            print(f", {eval_peer_file.name}, {cmp_file.name}, {db_export_file.name}")
        else:
            print(f", {db_export_file.name}")

        return True

    except subprocess.TimeoutExpired:
        print(f"      ✗ CLLM workflow timed out")
        return False
    except Exception as e:
        print(f"      ✗ Error: {e}")
        return False


def process_manuscript_versions(
    manuscripts_dir: Path,
    limit: int | None = None,
    dry_run: bool = False,
    continue_on_error: bool = False,
    force: bool = False,
    verbose: bool = True,
) -> tuple[int, int, int]:
    """
    Process all manuscript version folders.

    Args:
        manuscripts_dir: Directory containing organized manuscript folders
        limit: Optional limit on number of versions to process
        dry_run: If True, only print what would be done
        continue_on_error: If True, continue processing even if CLLM fails
        force: If True, overwrite existing CLLM outputs
        verbose: Enable verbose CLLM logging

    Returns:
        (total_processed, successful, failed, skipped)
    """
    # Get all manuscript directories
    manuscript_dirs = sorted([d for d in manuscripts_dir.iterdir() if d.is_dir()])

    # Build list of all version directories
    version_dirs = []
    for manuscript_dir in manuscript_dirs:
        # Find all version directories (v1, v2, etc.)
        for version_dir in sorted(manuscript_dir.glob("v*")):
            if version_dir.is_dir():
                # Check if this version has a manuscript file
                manuscript_files = list(version_dir.glob("manuscript_v*.md"))
                if manuscript_files:
                    version_dirs.append((manuscript_dir.name, version_dir, manuscript_files[0]))

    if limit:
        version_dirs = version_dirs[:limit]

    total = len(version_dirs)
    successful = 0
    failed = 0
    skipped = 0

    print(f"\n📊 Processing {total} manuscript versions...\n")

    for i, (article_id, version_dir, manuscript_file) in enumerate(version_dirs, 1):
        version_name = version_dir.name  # e.g., "v1"

        # Check if already processed (look for claims.json)
        claims_file = version_dir / "claims.json"
        if not force and claims_file.exists():
            print(f"📄 [{i}/{total}] {article_id}/{version_name}")
            print(f"      ⏭️  Already processed (use --force to overwrite)")
            skipped += 1
            print()
            continue

        print(f"📄 [{i}/{total}] {article_id}/{version_name}")

        # Check for peer reviews
        peer_reviews_file = None
        review_files = list(version_dir.glob("reviews_v*.md"))
        if review_files and has_peer_reviews(version_dir):
            peer_reviews_file = review_files[0]
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
        )

        if success:
            successful += 1
        else:
            failed += 1
            if not continue_on_error:
                print(f"\n❌ Stopping due to error. Use --continue-on-error to continue.\n")
                return i, successful, failed, skipped

        print()

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
    if args.limit:
        print(f"Limit: {args.limit} versions")
    if args.dry_run:
        print("Mode: DRY RUN (no processing will be performed)")
    if args.continue_on_error:
        print("Error handling: Continue on error")
    if args.force:
        print("Mode: FORCE (overwriting existing outputs)")
    else:
        print("Mode: Skip already processed (use --force to overwrite)")
    print("=" * 70)

    try:
        total, successful, failed, skipped = process_manuscript_versions(
            manuscripts_dir,
            limit=args.limit,
            dry_run=args.dry_run,
            continue_on_error=args.continue_on_error,
            force=args.force,
            verbose=not args.quiet,
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
