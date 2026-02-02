#!/usr/bin/env python3
"""
Query claims using cosine similarity search.

This script loads pre-computed claim embeddings and allows querying
to find the most similar claims based on cosine similarity.

Usage:
    python query_claims.py "your query text" [--top-k N]

Options:
    --top-k N    Return top N most similar claims (default: 10)
    --json       Output results as JSON instead of formatted text

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
    import numpy as np
except ImportError:
    print("❌ Error: Required packages not installed")
    print("   Install with: pip install openai numpy")
    sys.exit(1)


def cosine_similarity(a, b):
    """Calculate cosine similarity between two vectors."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def load_embeddings(embeddings_dir: Path):
    """
    Load pre-computed embeddings and metadata.

    Args:
        embeddings_dir: Directory containing embeddings.json and metadata.json

    Returns:
        Tuple of (embeddings_array, metadata_list)
    """
    embeddings_file = embeddings_dir / "embeddings.json"
    metadata_file = embeddings_dir / "metadata.json"

    if not embeddings_file.exists():
        print(f"❌ Error: Embeddings file not found: {embeddings_file}")
        print("   Run embed_claims.py first!")
        sys.exit(1)

    if not metadata_file.exists():
        print(f"❌ Error: Metadata file not found: {metadata_file}")
        sys.exit(1)

    print("📂 Loading embeddings...")

    with open(embeddings_file) as f:
        embeddings_list = json.load(f)

    with open(metadata_file) as f:
        metadata_list = json.load(f)

    # Convert to numpy array for faster computation
    embeddings_array = np.array(embeddings_list)

    print(f"   ✓ Loaded {len(embeddings_list)} claim embeddings")
    print(f"   ✓ Embedding dimension: {embeddings_array.shape[1]}")

    return embeddings_array, metadata_list


def embed_query(query: str):
    """
    Generate embedding for query text using OpenAI API.

    Args:
        query: Query text to embed

    Returns:
        numpy array of query embedding
    """
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    print(f"\n🔍 Embedding query: \"{query}\"")

    try:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=[query]
        )

        query_embedding = np.array(response.data[0].embedding)
        print("   ✓ Query embedded")

        return query_embedding

    except Exception as e:
        print(f"❌ Error embedding query: {e}")
        sys.exit(1)


def search_similar_claims(query_embedding, embeddings_array, metadata_list, top_k: int = 10):
    """
    Find top-k most similar claims using cosine similarity.

    Args:
        query_embedding: Query embedding vector
        embeddings_array: Array of claim embeddings
        metadata_list: List of claim metadata
        top_k: Number of results to return

    Returns:
        List of tuples (similarity_score, metadata_dict)
    """
    print(f"\n🔎 Finding top {top_k} most similar claims...")

    # Calculate cosine similarities
    similarities = []
    for i, claim_embedding in enumerate(embeddings_array):
        similarity = cosine_similarity(query_embedding, claim_embedding)
        similarities.append((similarity, metadata_list[i]))

    # Sort by similarity (descending)
    similarities.sort(key=lambda x: x[0], reverse=True)

    # Return top-k
    return similarities[:top_k]


def display_results(results, output_json: bool = False):
    """
    Display search results.

    Args:
        results: List of (similarity_score, metadata_dict) tuples
        output_json: If True, output as JSON
    """
    if output_json:
        # JSON output
        output = [
            {
                'rank': i + 1,
                'similarity': float(score),
                'article_id': meta['article_id'],
                'version': meta['version'],
                'claim_id': meta['claim_id'],
                'claim_text': meta['claim_text'],
            }
            for i, (score, meta) in enumerate(results)
        ]
        print(json.dumps(output, indent=2))
    else:
        # Formatted text output
        print("\n" + "=" * 80)
        print("SEARCH RESULTS")
        print("=" * 80)

        for i, (score, meta) in enumerate(results, 1):
            print(f"\n[{i}] Similarity: {score:.4f}")
            print(f"    Article: {meta['article_id']} ({meta['version']})")
            print(f"    Claim ID: {meta['claim_id']}")
            print(f"    Text: {meta['claim_text']}")

        print("\n" + "=" * 80)


def main():
    """Main entry point."""
    parser = ArgumentParser(
        description="Query claims using cosine similarity search."
    )

    parser.add_argument(
        "query",
        type=str,
        help="Query text to search for similar claims"
    )

    parser.add_argument(
        "--top-k", "-k",
        type=int,
        default=10,
        help="Return top N most similar claims (default: 10)"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON instead of formatted text"
    )

    args = parser.parse_args()

    # Setup paths
    script_dir = Path(__file__).parent
    embeddings_dir = script_dir / "claim_embeddings"

    if not embeddings_dir.exists():
        print(f"❌ Error: Embeddings directory not found: {embeddings_dir}")
        print("   Run embed_claims.py first!")
        sys.exit(1)

    print("=" * 80)
    print("Claim Similarity Search")
    print("=" * 80)
    print(f"Embeddings directory: {embeddings_dir}")
    print(f"Top-K: {args.top_k}")
    print("=" * 80)

    try:
        # Load pre-computed embeddings
        embeddings_array, metadata_list = load_embeddings(embeddings_dir)

        # Embed query
        query_embedding = embed_query(args.query)

        # Search for similar claims
        results = search_similar_claims(
            query_embedding,
            embeddings_array,
            metadata_list,
            top_k=args.top_k
        )

        # Display results
        display_results(results, output_json=args.json)

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
