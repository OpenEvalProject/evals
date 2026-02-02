# eLife Manuscript Evaluations

This repository contains the full eLife corpus processed with OpenEval, along with the code used to process the entire corpus.

## Overview

This repo processes 16,000+ eLife manuscripts through the complete OpenEval workflow:

1. **Organization** – XML manuscripts organized by article ID with version support  
2. **Conversion** – JATS XML converted to Markdown format with peer reviews extracted using [`jats`](https://github.com/OpenEvalProject/jats)  
3. **CLLM Analysis** – Claims extracted and evaluated by both LLM and peer reviewers using [`CLLM`](https://github.com/OpenEvalProject/cllm)   
4. **Database Export** – Results formatted for database import  

## Repository Structure

```
evals/
    manuscripts/                # Organized manuscript evaluations
        elife-XXXXX/           # One folder per article ID
            elife-XXXXX-v1.xml     # Symlink to source XML
            elife-XXXXX-v2.xml     # Multiple versions if available
            v1/                    # Version 1 outputs
                manuscript_v1.md       # Converted manuscript
                reviews_v1.md          # Peer reviews
                responses_v1.md        # Author responses
                claims.json            # Extracted claims
                eval_llm.json          # LLM evaluations
                eval_peer.json         # Peer evaluations
                cmp.json               # Concordance analysis
                db_export.json         # Database-ready format
            v2/                    # Version 2 outputs (if available)
                ...
    organize_manuscripts.py       # Organize XML files by article ID
    batch_convert.py              # Convert XML to Markdown
    batch_cllm.py                 # Run CLLM workflow
    create_db_export.py           # Helper for database export
```

## Scripts

### 1. organize_manuscripts.py

Organizes eLife XML files into structured folders with symlinks.

**Usage:**
```bash
python organize_manuscripts.py [--dry-run] [--articles] [--preprints]
```

**Prerequisites:**
- Source XML files must be in `../elife-article-xml/articles/` and/or `../elife-article-xml/preprints/`

### 2. batch_convert.py

Converts JATS XML manuscripts to Markdown using the jxp tool.

**Usage:**
```bash
# Process all manuscripts (skips already converted)
python batch_convert.py --continue-on-error

# Process in batches
python batch_convert.py --limit 100 --continue-on-error

# Force reconversion
python batch_convert.py --force --continue-on-error

# Dry run
python batch_convert.py --dry-run --limit 10
```

**Prerequisites:**
- jxp tool installed at `../jxp/.venv/bin/jxp`
- Manuscripts organized (run organize_manuscripts.py first)

### 3. batch_cllm.py

Runs the complete CLLM workflow on converted manuscripts.

**Workflow stages:**
1. Extract claims from manuscript
2. Evaluate claims with LLM
3. Evaluate claims with peer reviews (if available)
4. Compare LLM and peer evaluations
5. Create database export JSON

**Usage:**
```bash
# Process all manuscripts (skips already processed, 10 parallel by default)
python batch_cllm.py --continue-on-error

# Process with more parallelism
python batch_cllm.py --parallel 20 --continue-on-error

# Sequential processing (no parallelism)
python batch_cllm.py --parallel 1 --continue-on-error

# Process in batches
python batch_cllm.py --limit 100 --continue-on-error

# Force reprocessing
python batch_cllm.py --force --continue-on-error

# Quiet mode (no verbose CLLM logging)
python batch_cllm.py --quiet --continue-on-error
```

**Prerequisites:**
- CLLM tool installed at `../cllm/.venv/bin/cllm`
- CLLM configured with `.env` file (LLM_PROVIDER, API keys, etc.)
- Manuscripts converted to Markdown (run batch_convert.py first)

### 4. create_db_export.py

Helper script called by batch_cllm.py to create database-ready JSON exports.

**Note:** This script runs automatically as part of the batch_cllm.py workflow.

## Dependencies

External tools (must be installed separately):

- **jxp** – JATS XML parser for converting XML to Markdown  
  - Location: `../jxp/`  
  - Repository: [Your jxp repo URL]  

- **cllm** – Claim LLM tool for scientific claim verification  
  - Location: `../cllm/`  
  - Repository: [Your cllm repo URL]  

Python requirements:
- Python 3.10+
- All scripts use only standard library modules

## Workflow Example

Complete pipeline from XML to database-ready outputs:

```bash
# Step 1: Organize XML files into manuscript folders
python organize_manuscripts.py --articles

# Step 2: Convert XML to Markdown
python batch_convert.py --continue-on-error

# Step 3: Run CLLM analysis
python batch_cllm.py --continue-on-error
```

## Data Format

### Database Export (`db_export.json`)

Each manuscript version generates a `db_export.json` file containing:

- **Submission** – Manuscript metadata  
- **Content** – Full text (manuscript + peer reviews)  
- **Claims** – Extracted atomic factual claims  
- **Results** – Evaluation results (LLM + peer)  
- **Claim-Result Links** – Junction table linking claims to results  
- **Comparisons** – Concordance analysis between LLM and peer evaluations  
- **Prompts** – All prompts used (with deterministic hashing for deduplication)  

All entities use UUIDs for global uniqueness across submissions.

## Features

- **Parallel Processing** – Process up to 10 manuscripts concurrently by default (configurable with `--parallel`)
- **Incremental Processing** – Skips already processed manuscripts by default
- **Multi-version Support** – Handles manuscripts with multiple revision rounds
- **Peer Review Extraction** – Automatically extracts and processes peer reviews when available
- **Error Resilience** – Continues processing on errors with `--continue-on-error` flag
- **Dry Run Mode** – Preview operations without making changes
- **Batch Processing** – Process in chunks with `--limit` flag

## Status

- **Manuscripts organized:** 18,455 articles (30,738 XML files)
- **Manuscripts converted:** All 18,455 articles converted to Markdown
- **CLLM processing:** Ready to process all manuscripts

## Important Setup Note

⚠️ **After cloning this repository, you must re-run `organize_manuscripts.py` to recreate the symlinks:**

```bash
python organize_manuscripts.py --articles
```

This is necessary because:
- The `manuscripts/` folder is excluded from git (too large)
- Symlinks need to be created to link to the source XML files
- The script will organize all XML files and create the proper directory structure

## Notes

- Symlinks are used to avoid duplicating large XML files
- Each manuscript version is processed independently
- Processing is fully idempotent (safe to re-run)
- Database exports are self-contained (include all necessary data)

## License

[Your License]

## Contact

For questions or issues, please open an issue on GitHub.
