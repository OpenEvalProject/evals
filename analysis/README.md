# Claim Analysis Tools

This directory contains tools for analyzing and searching scientific claims using semantic embeddings.

## Scripts

### 1. embed_claims.py
Generates OpenAI embeddings for all claims in the manuscripts directory.

**Usage:**
```bash
# Embed all claims (requires OPENAI_API_KEY)
export OPENAI_API_KEY="your-api-key"
python embed_claims.py

# Test with limited manuscripts
python embed_claims.py --limit 10
```

**Output:**
- `claim_embeddings/embeddings.json` - Claim embedding vectors
- `claim_embeddings/metadata.json` - Claim metadata (article_id, version, claim_text, etc.)

**Requirements:**
- `pip install openai`
- OPENAI_API_KEY environment variable

### 2. query_claims.py
Search for similar claims using cosine similarity.

**Usage:**
```bash
# Find top 10 most similar claims
python query_claims.py "your query text"

# Find top 20 similar claims
python query_claims.py "your query text" --top-k 20

# Output as JSON
python query_claims.py "your query text" --json
```

**Example:**
```bash
python query_claims.py "CRISPR gene editing in embryos" --top-k 5
```

**Requirements:**
- `pip install openai numpy`
- OPENAI_API_KEY environment variable
- Pre-computed embeddings (run embed_claims.py first)

## Workflow

1. **Generate embeddings** (one-time, or when new claims are added):
   ```bash
   export OPENAI_API_KEY="your-api-key"
   python embed_claims.py
   ```

2. **Query claims** (as many times as needed):
   ```bash
   python query_claims.py "your search query"
   ```

## Technical Details

- **Embedding Model**: OpenAI's `text-embedding-3-small` (1536 dimensions)
- **Similarity Metric**: Cosine similarity
- **Batch Size**: 100 claims per API call (for embedding generation)
- **Format**: JSON files for easy loading and processing

## Data Structure

### embeddings.json
Array of embedding vectors:
```json
[
  [0.123, -0.456, ...],  // 1536-dimensional vector
  [0.789, 0.012, ...],
  ...
]
```

### metadata.json
Array of claim metadata:
```json
[
  {
    "article_id": "elife-00003",
    "version": "v1",
    "claim_index": 0,
    "claim_id": "uuid-string",
    "claim_text": "The actual claim text..."
  },
  ...
]
```

## Notes

- Embeddings are stored as JSON for simplicity and portability
- Query script uses numpy for fast cosine similarity computation
- Both scripts handle errors gracefully and provide progress updates
- Embeddings can be regenerated at any time (idempotent operation)
