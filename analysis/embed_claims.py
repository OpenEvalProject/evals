#!/usr/bin/env python3
"""
Embed all claims using OpenAI's text-embedding API.

This script reads all claims.json files from the manuscripts directory,
extracts claim text, generates embeddings using OpenAI's API, and saves
them for later retrieval.

Usage:
    python embed_claims.py [--limit N]

Options:
    --limit N    Only process first N manuscripts (for testing)

Environment:
    OPENAI_API_KEY must be set
"""

import json
import os
import sys
from argparse import ArgumentParser
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("❌ Error: openai package not installed")
    print("   Install with: pip install openai")
    sys.exit(1)


def load_claims_from_manuscripts(manuscripts_dir: Path, limit: int | None = None):
    """
    Load all claims from manuscripts directory.

    Args:
        manuscripts_dir: Path to manuscripts directory
        limit: Optional limit on number of manuscripts to process

    Yields:
        Tuple of (article_id, version, claim_index, claim_text, claim_id)
    """
    manuscript_dirs = sorted([d for d in manuscripts_dir.iterdir() if d.is_dir()])

    if limit:
        manuscript_dirs = manuscript_dirs[:limit]

    total_claims = 0

    for manuscript_dir in manuscript_dirs:
        article_id = manuscript_dir.name

        # Process each version
        for version_dir in sorted(manuscript_dir.glob("v*")):
            if not version_dir.is_dir():
                continue

            claims_file = version_dir / "claims.json"
            if not claims_file.exists():
                continue

            # Load claims
            try:
                with open(claims_file) as f:
                    data = json.load(f)

                # Handle both list and dict formats
                claims = data if isinstance(data, list) else data.get('claims', [])

                version = version_dir.name

                for i, claim in enumerate(claims):
                    claim_text = claim.get('claim', '')
                    claim_id = claim.get('id', f"{article_id}_{version}_claim_{i}")

                    if claim_text:
                        total_claims += 1
                        yield (article_id, version, i, claim_text, claim_id)

            except Exception as e:
                print(f"⚠️  Error loading {article_id}/{version_dir.name}: {e}")
                continue

    print(f"\n📊 Total claims loaded: {total_claims}")


def embed_claims(claims_iter, output_dir: Path, batch_size: int = 100):
    """
    Generate embeddings for all claims using OpenAI API.

    Args:
        claims_iter: Iterator of (article_id, version, claim_index, claim_text, claim_id)
        output_dir: Directory to save embeddings
        batch_size: Number of claims to process in each batch
    """
    # Initialize OpenAI client
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    # Prepare output files
    embeddings_file = output_dir / "embeddings.json"
    metadata_file = output_dir / "metadata.json"

    embeddings_list = []
    metadata_list = []

    batch = []
    batch_metadata = []
    processed = 0

    print("\n🔄 Generating embeddings...")

    for article_id, version, claim_idx, claim_text, claim_id in claims_iter:
        batch.append(claim_text)
        batch_metadata.append({
            'article_id': article_id,
            'version': version,
            'claim_index': claim_idx,
            'claim_id': claim_id,
            'claim_text': claim_text,
        })

        # Process batch when full
        if len(batch) >= batch_size:
            try:
                response = client.embeddings.create(
                    model="text-embedding-3-small",
                    input=batch
                )

                # Extract embeddings
                for i, embedding_obj in enumerate(response.data):
                    embeddings_list.append(embedding_obj.embedding)
                    metadata_list.append(batch_metadata[i])
                    processed += 1

                print(f"   ✓ Processed {processed} claims...")

            except Exception as e:
                print(f"   ✗ Error processing batch: {e}")

            # Clear batch
            batch = []
            batch_metadata = []

    # Process remaining claims
    if batch:
        try:
            response = client.embeddings.create(
                model="text-embedding-3-small",
                input=batch
            )

            for i, embedding_obj in enumerate(response.data):
                embeddings_list.append(embedding_obj.embedding)
                metadata_list.append(batch_metadata[i])
                processed += 1

            print(f"   ✓ Processed {processed} claims (final batch)")

        except Exception as e:
            print(f"   ✗ Error processing final batch: {e}")

    # Save embeddings and metadata
    print(f"\n💾 Saving embeddings and metadata...")

    with open(embeddings_file, 'w') as f:
        json.dump(embeddings_list, f)

    with open(metadata_file, 'w') as f:
        json.dump(metadata_list, f, indent=2)

    print(f"   ✓ Embeddings saved to: {embeddings_file}")
    print(f"   ✓ Metadata saved to: {metadata_file}")
    print(f"\n✅ Total claims embedded: {len(embeddings_list)}")


def main():
    """Main entry point."""
    parser = ArgumentParser(
        description="Embed all claims using OpenAI embeddings API."
    )

    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=None,
        help="Only process first N manuscripts (for testing)"
    )

    args = parser.parse_args()

    # Setup paths
    script_dir = Path(__file__).parent
    manuscripts_dir = script_dir.parent / "manuscripts"
    output_dir = script_dir / "claim_embeddings"

    if not manuscripts_dir.exists():
        print(f"❌ Error: Manuscripts directory not found: {manuscripts_dir}")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Claim Embeddings Generator")
    print("=" * 70)
    print(f"Manuscripts directory: {manuscripts_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Model: text-embedding-3-small")
    if args.limit:
        print(f"Limit: {args.limit} manuscripts")
    print("=" * 70)

    try:
        # Load claims
        claims_iter = load_claims_from_manuscripts(manuscripts_dir, limit=args.limit)

        # Generate embeddings
        embed_claims(claims_iter, output_dir)

    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
