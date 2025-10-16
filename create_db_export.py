#!/usr/bin/env python3
"""
Helper script to create database export from CLLM outputs.

This script is called from the CLLM venv to access its dependencies.

Usage:
    python create_db_export.py <version_dir>
"""

import json
import sys
from pathlib import Path


def create_db_export(version_dir: Path) -> bool:
    """Create database export JSON from CLLM workflow outputs."""
    try:
        # Import CLLM modules (must be run from CLLM venv)
        sys.path.insert(0, str(Path(__file__).parent.parent / "cllm"))

        from cllm.db_export import export_to_database_format, save_db_export
        from cllm.models import LLMClaimV3, LLMResultV3, LLMResultsConcordanceRow

        # Find files
        manuscript_file = list(version_dir.glob("manuscript_v*.md"))[0]
        claims_file = version_dir / "claims.json"
        eval_llm_file = version_dir / "eval_llm.json"
        eval_peer_file = version_dir / "eval_peer.json"
        cmp_file = version_dir / "cmp.json"
        peer_reviews_file = list(version_dir.glob("reviews_v*.md"))

        # Load manuscript text
        manuscript_text = manuscript_file.read_text(encoding='utf-8')

        # Load peer reviews text (if available)
        peer_review_text = None
        if peer_reviews_file and peer_reviews_file[0].exists():
            peer_review_text = peer_reviews_file[0].read_text(encoding='utf-8')

        # Load claims (direct list format)
        with open(claims_file) as f:
            claims_data = json.load(f)

        # Handle both list and dict formats
        if isinstance(claims_data, list):
            claims = [LLMClaimV3(**c) for c in claims_data]
        else:
            claims = [LLMClaimV3(**c) for c in claims_data.get('claims', [])]

        # Load LLM results (direct list format)
        with open(eval_llm_file) as f:
            llm_data = json.load(f)

        if isinstance(llm_data, list):
            llm_results = [LLMResultV3(**r) for r in llm_data]
        else:
            llm_results = [LLMResultV3(**r) for r in llm_data.get('results', [])]

        # Load peer results (if available)
        peer_results = None
        if eval_peer_file.exists():
            with open(eval_peer_file) as f:
                peer_data = json.load(f)

            if isinstance(peer_data, list):
                peer_results = [LLMResultV3(**r) for r in peer_data]
            else:
                peer_results = [LLMResultV3(**r) for r in peer_data.get('results', [])]

        # Load concordance (if available)
        concordance = None
        if cmp_file.exists():
            with open(cmp_file) as f:
                cmp_data = json.load(f)

            if isinstance(cmp_data, list):
                concordance = [LLMResultsConcordanceRow(**row) for row in cmp_data]
            else:
                concordance = [LLMResultsConcordanceRow(**row) for row in cmp_data.get('concordance', [])]

        # Build prompts dictionary with default placeholders
        # (CLLM output files don't include prompt metadata yet)
        prompts = {
            'extract': {
                'text': 'claim extraction prompt',  # Placeholder
                'model': 'claude-sonnet-4-5-20250929'
            },
            'eval_llm': {
                'text': 'llm evaluation prompt',  # Placeholder
                'model': 'claude-sonnet-4-5-20250929'
            }
        }

        if peer_results:
            prompts['eval_peer'] = {
                'text': 'peer evaluation prompt',  # Placeholder
                'model': 'claude-sonnet-4-5-20250929'
            }

        if concordance:
            prompts['compare'] = {
                'text': 'comparison prompt',  # Placeholder
                'model': 'claude-sonnet-4-5-20250929'
            }

        # Create database export
        db_export = export_to_database_format(
            manuscript_text=manuscript_text,
            peer_review_text=peer_review_text,
            claims=claims,
            llm_results=llm_results,
            peer_results=peer_results,
            concordance=concordance,
            prompts=prompts,
        )

        # Save to file
        db_export_file = version_dir / "db_export.json"
        save_db_export(db_export, db_export_file)

        print("✓ Database export created")
        return True

    except Exception as e:
        print(f"✗ DB export error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_db_export.py <version_dir>", file=sys.stderr)
        sys.exit(1)

    version_dir = Path(sys.argv[1])
    if not version_dir.exists():
        print(f"Error: Directory not found: {version_dir}", file=sys.stderr)
        sys.exit(1)

    success = create_db_export(version_dir)
    sys.exit(0 if success else 1)
