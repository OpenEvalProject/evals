#!/usr/bin/env python3
"""
Batch convert eLife XML manuscripts to Markdown.

This script processes organized manuscript folders, converting each XML file
to Markdown format using the jxp tool. It handles multiple versions per
manuscript and extracts peer review materials when available.

Usage:
    python batch_convert.py [--dry-run] [--limit N] [--continue-on-error]

Options:
    --dry-run, -n          Show what would be done without converting
    --limit N, -l N        Only process first N manuscripts
    --continue-on-error    Continue processing even if a conversion fails
"""

import re
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path

# Path to jxp tool in its venv
JXP_BIN = Path(__file__).parent.parent / "jxp" / ".venv" / "bin" / "jxp"


def convert_manuscript(xml_path: Path, output_dir: Path, dry_run: bool = False, force: bool = False) -> bool:
    """
    Convert a single XML manuscript to Markdown using jxp.

    Args:
        xml_path: Path to XML file (symlink)
        output_dir: Directory to write markdown files (manuscript folder)
        dry_run: If True, only print what would be done
        force: If True, overwrite existing conversions

    Returns:
        True if conversion succeeded, False otherwise
    """
    # Extract version from filename (e.g., elife-12345-v1.xml -> v1)
    version_match = re.search(r'-v(\d+)\.xml$', xml_path.name)
    if not version_match:
        print(f"   ✗ Could not extract version from {xml_path.name}")
        return False

    version_num = version_match.group(1)
    version_dir = output_dir / f"v{version_num}"

    # Output paths within version directory
    manuscript_output = version_dir / f"manuscript_v{version_num}.md"
    reviews_output = version_dir / "reviews"

    # Check if already converted (skip if manuscript file exists)
    if not force and manuscript_output.exists():
        print(f"   ⏭️  Already converted: {xml_path.name} (use --force to overwrite)")
        return True

    if dry_run:
        if manuscript_output.exists():
            print(f"   → Would skip (already exists): {xml_path.name}")
        else:
            print(f"   → Would convert: {xml_path.name}")
        print(f"      Output dir: {version_dir.name}/")
        print(f"      Files: manuscript_v{version_num}.md, reviews_v{version_num}.md, responses_v{version_num}.md (if available)")
        return True

    # Check if jxp binary exists
    if not JXP_BIN.exists():
        print(f"   ✗ jxp binary not found at {JXP_BIN}")
        return False

    try:
        # Create version directory
        version_dir.mkdir(parents=True, exist_ok=True)

        # Build jxp command
        # jxp convert <xml> -o <output> -r <review_base>
        cmd = [
            str(JXP_BIN),
            "convert",
            str(xml_path),
            "-o", str(manuscript_output) + ".md",
            "-r", str(reviews_output),
        ]

        # Run conversion
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
        )

        if result.returncode == 0:
            # Print jxp's stderr output (which contains the success messages)
            if result.stderr:
                for line in result.stderr.strip().split('\n'):
                    print(f"   {line}")
            return True
        else:
            print(f"   ✗ Conversion failed: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print(f"   ✗ Conversion timed out after 60s")
        return False
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False


def process_manuscripts(
    manuscripts_dir: Path,
    limit: int | None = None,
    dry_run: bool = False,
    continue_on_error: bool = False,
    force: bool = False,
) -> tuple[int, int, int, int]:
    """
    Process all manuscript folders.

    Args:
        manuscripts_dir: Directory containing organized manuscript folders
        limit: Optional limit on number of manuscripts to process
        dry_run: If True, only print what would be done
        continue_on_error: If True, continue processing even if conversion fails
        force: If True, overwrite existing conversions

    Returns:
        (total_processed, successful, failed, skipped)
    """
    # Get all manuscript directories
    manuscript_dirs = sorted([d for d in manuscripts_dir.iterdir() if d.is_dir()])

    if limit:
        manuscript_dirs = manuscript_dirs[:limit]

    total = len(manuscript_dirs)
    successful = 0
    failed = 0
    skipped = 0

    print(f"\n📊 Processing {total} manuscripts...\n")

    for i, manuscript_dir in enumerate(manuscript_dirs, 1):
        article_id = manuscript_dir.name

        # Get all XML versions in this folder
        xml_files = sorted(manuscript_dir.glob("*.xml"))

        if not xml_files:
            print(f"⚠️  [{i}/{total}] {article_id}: No XML files found")
            continue

        print(f"📄 [{i}/{total}] {article_id} ({len(xml_files)} version{'s' if len(xml_files) > 1 else ''})")

        # Process each version
        all_succeeded = True
        any_skipped = False
        for xml_file in xml_files:
            # Check if this version was skipped (already exists)
            version_match = re.search(r'-v(\d+)\.xml$', xml_file.name)
            if version_match and not force:
                version_num = version_match.group(1)
                manuscript_output = manuscript_dir / f"v{version_num}" / f"manuscript_v{version_num}.md"
                if manuscript_output.exists() and not dry_run:
                    any_skipped = True

            success = convert_manuscript(xml_file, manuscript_dir, dry_run=dry_run, force=force)

            if not success:
                all_succeeded = False
                if not continue_on_error:
                    print(f"\n❌ Stopping due to error. Use --continue-on-error to continue.\n")
                    return i, successful, failed + 1, skipped

        if all_succeeded:
            if any_skipped and not force:
                skipped += 1
            else:
                successful += 1
        else:
            failed += 1

        print()

    return total, successful, failed, skipped


def main():
    """Main entry point."""
    parser = ArgumentParser(
        description="Batch convert eLife XML manuscripts to Markdown using jxp."
    )

    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would be done without converting"
    )

    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=None,
        help="Only process first N manuscripts"
    )

    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue processing even if a conversion fails"
    )

    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Overwrite existing conversions (default: skip already converted)"
    )

    args = parser.parse_args()

    # Setup paths
    base_dir = Path(__file__).parent
    manuscripts_dir = base_dir / "manuscripts"

    if not manuscripts_dir.exists():
        print(f"❌ Error: Manuscripts directory not found: {manuscripts_dir}")
        print("   Run organize_manuscripts.py first!")
        sys.exit(1)

    print("=" * 70)
    print("eLife XML to Markdown Batch Converter")
    print("=" * 70)
    print(f"Manuscripts directory: {manuscripts_dir}")
    if args.limit:
        print(f"Limit: {args.limit} manuscripts")
    if args.dry_run:
        print("Mode: DRY RUN (no conversions will be performed)")
    if args.continue_on_error:
        print("Error handling: Continue on error")
    if args.force:
        print("Mode: FORCE (overwriting existing conversions)")
    else:
        print("Mode: Skip existing conversions (use --force to overwrite)")
    print("=" * 70)

    try:
        total, successful, failed, skipped = process_manuscripts(
            manuscripts_dir,
            limit=args.limit,
            dry_run=args.dry_run,
            continue_on_error=args.continue_on_error,
            force=args.force,
        )

        print("=" * 70)
        print("Batch Conversion Summary")
        print("=" * 70)
        print(f"Total processed: {total}")
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
