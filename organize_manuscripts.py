#!/usr/bin/env python3
"""
Organize eLife XML files into manuscript folders.

This script scans the eLife XML directory (articles/ and preprints/),
groups files by article ID, and creates organized folders with symlinks.

Usage:
    python organize_manuscripts.py [--dry-run] [--articles] [--preprints]

Options:
    --dry-run, -n      Show what would be done without making changes
    --articles         Only process articles/ directory (default: both)
    --preprints        Only process preprints/ directory (default: both)
"""

import re
import sys
from collections import defaultdict
from pathlib import Path


def parse_elife_filename(filename: str) -> tuple[str, int] | None:
    """
    Parse eLife XML filename to extract article ID and version.

    Examples:
        elife-12345-v1.xml -> ("elife-12345", 1)
        elife-67890-v2.xml -> ("elife-67890", 2)
        elife-12345.xml -> ("elife-12345", 1)  # Assume v1 if no version

    Returns:
        (article_id, version) or None if not a valid eLife XML file
    """
    # Pattern: elife-XXXXX-vN.xml or elife-XXXXX.xml
    pattern = r'^(elife-\d+)(?:-v(\d+))?\.xml$'
    match = re.match(pattern, filename)

    if not match:
        return None

    article_id = match.group(1)
    version = int(match.group(2)) if match.group(2) else 1

    return article_id, version


def scan_xml_files(xml_dir: Path) -> dict[str, list[tuple[int, Path]]]:
    """
    Scan directory for eLife XML files and group by article ID.

    Args:
        xml_dir: Directory containing eLife XML files

    Returns:
        Dictionary mapping article_id -> [(version, filepath), ...]
    """
    articles = defaultdict(list)

    for xml_file in xml_dir.glob("*.xml"):
        parsed = parse_elife_filename(xml_file.name)
        if parsed:
            article_id, version = parsed
            articles[article_id].append((version, xml_file))

    # Sort versions for each article
    for article_id in articles:
        articles[article_id].sort()

    return dict(articles)


def organize_manuscripts(base_dir: Path, source_dirs: list[str], output_dir: Path, dry_run: bool = False):
    """
    Organize eLife XMLs into manuscript folders with symlinks.

    Args:
        base_dir: Base directory containing articles/ and preprints/
        source_dirs: List of subdirectories to scan (e.g., ['articles', 'preprints'])
        output_dir: Output directory (evals/manuscripts/)
        dry_run: If True, only print what would be done
    """
    all_articles = {}

    # Scan each source directory
    for source_name in source_dirs:
        source_path = base_dir / source_name

        if not source_path.exists():
            print(f"⚠️  Skipping {source_name}/ - directory not found")
            continue

        print(f"📂 Scanning {source_name}/ for eLife XML files...")
        articles = scan_xml_files(source_path)

        if not articles:
            print(f"   No files found in {source_name}/")
        else:
            print(f"   ✅ Found {len(articles)} articles with {sum(len(v) for v in articles.values())} XML files")
            all_articles.update(articles)

    if not all_articles:
        print("\n❌ No eLife XML files found in any directory!")
        return

    print(f"\n📊 Total: {len(all_articles)} unique articles with {sum(len(v) for v in all_articles.values())} XML files\n")

    # Create output directory
    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    # Organize each article
    for article_id, versions in sorted(all_articles.items()):
        article_dir = output_dir / article_id

        print(f"📄 {article_id} ({len(versions)} version{'s' if len(versions) > 1 else ''})")

        if not dry_run:
            article_dir.mkdir(exist_ok=True)

        for version, xml_path in versions:
            # Create symlink
            symlink_name = f"{article_id}-v{version}.xml"
            symlink_path = article_dir / symlink_name

            # Calculate relative path from symlink to target
            # symlink is in: evals/manuscripts/elife-12345/
            # target is in:  elife-article-xml/articles/elife-12345-v1.xml
            # relative path: ../../../elife-article-xml/articles/elife-12345-v1.xml
            relative_target = Path("../../../elife-article-xml") / xml_path.relative_to(base_dir)

            if dry_run:
                print(f"   → Would create: {symlink_name}")
                print(f"      Links to: {xml_path.relative_to(base_dir)}")
            else:
                # Remove existing symlink if it exists
                if symlink_path.exists() or symlink_path.is_symlink():
                    symlink_path.unlink()

                # Create new symlink
                symlink_path.symlink_to(relative_target)
                print(f"   ✓ {symlink_name} -> {xml_path.relative_to(base_dir)}")

        print()

    if dry_run:
        print("🔍 This was a dry run. Run without --dry-run to create symlinks.")
    else:
        print(f"✅ Organization complete! Files organized in {output_dir}")


def main():
    """Main entry point."""
    # Setup paths
    # Script is in evals/, XML sources are in ../elife-article-xml/
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent / "elife-article-xml"
    output_dir = script_dir / "manuscripts"

    # Parse command-line arguments
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    articles_only = "--articles" in sys.argv
    preprints_only = "--preprints" in sys.argv

    # Determine which source directories to scan
    if articles_only and not preprints_only:
        source_dirs = ["articles"]
    elif preprints_only and not articles_only:
        source_dirs = ["preprints"]
    else:
        # Default: scan both
        source_dirs = ["articles", "preprints"]

    print("=" * 60)
    print("eLife XML Manuscript Organizer")
    print("=" * 60)
    print(f"Base directory: {base_dir}")
    print(f"Source directories: {', '.join(source_dirs)}")
    print(f"Output directory: {output_dir}")
    if dry_run:
        print("Mode: DRY RUN (no changes will be made)")
    print("=" * 60)
    print()

    try:
        organize_manuscripts(base_dir, source_dirs, output_dir, dry_run=dry_run)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
