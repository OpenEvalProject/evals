#!/usr/bin/env python3
"""
Generate manuscript_metadata.json for all manuscripts.

For each elife-*-v*.xml file, generates a corresponding v*/manuscript_metadata.json
file containing DOI, title, and abstract.
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Generate metadata for all manuscripts."""
    base_path = Path(__file__).parent / "manuscripts"

    if not base_path.exists():
        print(f"Error: {base_path} does not exist", file=sys.stderr)
        sys.exit(1)

    # Find all XML files
    xml_files = list(base_path.glob("*/elife-*-v*.xml"))

    print(f"Found {len(xml_files)} XML files to process")

    # Path to jats command
    jats_path = Path(__file__).parent.parent / "jats" / ".venv" / "bin" / "jats"

    if not jats_path.exists():
        print(f"Error: jats not found at {jats_path}", file=sys.stderr)
        sys.exit(1)

    files_processed = 0
    files_failed = 0
    files_skipped = 0

    for xml_file in sorted(xml_files):
        # Extract manuscript ID and version from filename
        # e.g., elife-00003-v1.xml -> elife-00003-v1
        manuscript_id_with_version = xml_file.stem

        # Determine output directory (e.g., manuscripts/elife-00003/v1/)
        # Split on last hyphen to separate version
        parts = manuscript_id_with_version.rsplit('-', 1)
        manuscript_id = parts[0]  # e.g., elife-00003
        version = parts[1]  # e.g., v1

        output_dir = xml_file.parent / version
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "manuscript_metadata.json"

        # Skip if metadata already exists
        if output_file.exists():
            files_skipped += 1
            continue

        # Run jats metadata command
        try:
            result = subprocess.run(
                [str(jats_path), "metadata", str(xml_file), "-o", str(output_file)],
                capture_output=True,
                text=True,
                check=True
            )

            files_processed += 1
            print(f"✓ {manuscript_id_with_version} -> {output_file.relative_to(base_path.parent)}")

        except subprocess.CalledProcessError as e:
            files_failed += 1
            print(f"✗ Failed: {manuscript_id_with_version}", file=sys.stderr)
            print(f"  Error: {e.stderr}", file=sys.stderr)

    print(f"\nProcessed {files_processed} files successfully, {files_skipped} skipped (already exist), {files_failed} failed")


if __name__ == "__main__":
    main()
