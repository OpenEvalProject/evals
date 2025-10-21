#!/bin/bash

# Script to delete all cllm-generated files from manuscript subfolders
# This removes: claims.json, eval_llm.json, eval_peer.json, cmp.json, db_export.json
# and any metrics_*.json files

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANUSCRIPTS_DIR="${SCRIPT_DIR}/manuscripts"

echo "=========================================="
echo "Cleaning CLLM outputs from manuscripts"
echo "=========================================="
echo ""

# Counter for tracking
total_deleted=0

# Find all v1, v2, v3... version directories
for version_dir in "${MANUSCRIPTS_DIR}"/*/v*; do
    if [ -d "$version_dir" ]; then
        manuscript=$(basename "$(dirname "$version_dir")")
        version=$(basename "$version_dir")

        echo "📁 ${manuscript}/${version}/"

        # List of files to delete
        files_to_delete=(
            "claims.json"
            "eval_llm.json"
            "eval_peer.json"
            "cmp.json"
            "db_export.json"
            "metrics_extract.json"
            "metrics_eval_llm.json"
            "metrics_eval_peer.json"
            "metrics_cmp.json"
        )

        deleted_count=0
        for file in "${files_to_delete[@]}"; do
            filepath="${version_dir}/${file}"
            if [ -f "$filepath" ]; then
                rm "$filepath"
                echo "  ✓ Deleted: ${file}"
                ((deleted_count++))
                ((total_deleted++))
            fi
        done

        if [ $deleted_count -eq 0 ]; then
            echo "  ℹ️  No cllm files found"
        fi
        echo ""
    fi
done

echo "=========================================="
echo "✅ Cleanup complete!"
echo "Total files deleted: ${total_deleted}"
echo "=========================================="
