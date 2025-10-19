#!/usr/bin/env python3
"""
Script to generate visualization plots for manuscripts based on visualize_results.ipynb.

This script generates four types of plots for each manuscript:
1. Bar plot showing agreement status counts
2. Confusion matrix comparing peer vs LLM result statuses
3. Scatter plot showing claims per result
4. Combined stacked bar and Jaccard index plot

The plots are saved as PNG files in the manuscript's v1 directory.

Usage:
    python generate_plots.py [--manuscripts-dir DIR] [--manuscript MANUSCRIPT] [--verbose] [--dry-run]

Examples:
    # Generate plots for all manuscripts with required files
    python generate_plots.py --verbose
    
    # Generate plots for a specific manuscript
    python generate_plots.py --manuscript elife-00003 --verbose
    
    # Dry run to see what would be processed
    python generate_plots.py --dry-run --verbose
"""

import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path
from typing import Dict, Any, Optional, List
import argparse
import sys


def find_manuscripts_with_required_files(manuscripts_dir: Path) -> List[Path]:
    """Find all manuscript directories that have v1 subdirectories with the required JSON files."""
    manuscripts = []
    
    for manuscript_dir in manuscripts_dir.iterdir():
        if not manuscript_dir.is_dir():
            continue
            
        v1_dir = manuscript_dir / "v1"
        if not v1_dir.exists():
            continue
            
        # Check for required files in the v1 directory
        required_files = ["eval_llm.json", "eval_peer.json", "cmp.json", "claims.json"]
        if all((v1_dir / file).exists() for file in required_files):
            manuscripts.append(manuscript_dir)
    
    return sorted(manuscripts)


def load_manuscript_data(v1_dir: Path) -> Optional[Dict[str, Any]]:
    """Load all required JSON files for a manuscript from its v1 directory."""
    try:
        data = {}
        files = ["eval_llm.json", "eval_peer.json", "cmp.json", "claims.json"]
        
        for file in files:
            with open(v1_dir / file, "r") as f:
                data[file.replace(".json", "")] = json.load(f)
        
        return data
    except Exception as e:
        print(f"Error loading data from {v1_dir}: {e}")
        return None


def calculate_jaccard_index(set1: set, set2: set) -> float:
    """Calculate Jaccard index between two sets."""
    if not set1 and not set2:
        return 1.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0


def generate_plots(manuscript_dir: Path, v1_dir: Path, data: Dict[str, Any], verbose: bool = False) -> bool:
    """Generate all four plots for a manuscript and save them in the v1 directory."""
    manuscript_name = manuscript_dir.name
    
    try:
        # Extract data
        eval_llm = data["eval_llm"]
        eval_peer = data["eval_peer"]
        cmp_data = data["cmp"]
        claims_data = data["claims"]
        
        if verbose:
            print(f"Generating plots for {manuscript_name}...")
            print(f"  LLM results: {len(eval_llm)}")
            print(f"  Peer results: {len(eval_peer)}")
            print(f"  Concordance rows: {len(cmp_data)}")
            print(f"  Claims: {len(claims_data)}")
        
        # Set up the plotting style and configure matplotlib
        plt.style.use('default')
        plt.rcParams['figure.max_open_warning'] = 0  # Disable the warning
        
        # Convert to DataFrames like in the original notebook
        df_llm = pd.DataFrame(eval_llm)
        df_peer = pd.DataFrame(eval_peer)
        df_cmp = pd.DataFrame(cmp_data)
        
        # Color configurations from original notebook
        bar_color = "#6baed6"
        colors = {
            "Agree": "#31a354",
            "Partial": "#fdae6b", 
            "Disagree": "#e34a33",
            "Disjoint": "#6e6e6e"
        }
        status_colors = colors
        
        colors_stacked = {
            "shared": "#6497b1",
            "llm_only": "#b3cde0", 
            "peer_only": "#03396c"
        }
        jaccard_color = "#6497b1"
        
        fontsize = 11
        
        # Proper agreement category order and capitalization
        desired_agree_order = ["Agree", "Partial", "Disagree", "Disjoint"]
        df_cmp["agreement_status"] = df_cmp["agreement_status"].astype(str).str.capitalize()
        
        # Calculate intersection fraction (Jaccard denominator is max(n_llm, n_peer))
        df_cmp["intersection_fraction"] = df_cmp["n_itx"] / df_cmp[["n_llm", "n_peer"]].max(axis=1)
        
        def safe_int(s):
            return s.where(pd.notnull(s) & np.isfinite(s), 0).astype(int)
        
        df_cmp["n_peer_int"] = safe_int(df_cmp["n_peer"])
        df_cmp["n_llm_int"] = safe_int(df_cmp["n_llm"])
        
        # --- 1. Bar plot: agreement status count ---
        fig_agree, ax_agree = plt.subplots(figsize=(5.2, 5))
        agreement_counts = df_cmp["agreement_status"].value_counts()
        agreement_counts = agreement_counts.reindex(desired_agree_order, fill_value=0)
        ax_agree.bar(agreement_counts.index, agreement_counts.values, color=bar_color)
        ax_agree.grid(axis='y', linestyle="--", color="#cccccc", linewidth=1, alpha=0.7, zorder=0)
        ax_agree.set_axisbelow(True)
        ax_agree.set_title("OpenEval vs Peer Evaluation Agreement", fontsize=fontsize+2)
        ax_agree.set_xlabel("Agreement Status", fontsize=fontsize+2)
        ax_agree.set_ylabel("# Results", fontsize=fontsize+2)
        ax_agree.set_xticks(range(len(desired_agree_order)))
        ax_agree.set_xticklabels(agreement_counts.index, fontsize=fontsize)
        ax_agree.set_yticklabels(ax_agree.get_yticks(), fontsize=fontsize)
        for i, val in enumerate(agreement_counts.values):
            ax_agree.text(i, val + 0.05, str(val), ha="center", va="bottom", fontsize=fontsize)
        plt.tight_layout()
        fig_agree.savefig(v1_dir / "figure_eval_agreement_bar.png", dpi=300, bbox_inches='tight')
        plt.close()
        
        # --- 2. Confusion Matrix: Peer vs LLM result status ---
        fig_conf, ax_conf = plt.subplots(figsize=(6.3, 6.3))
        df_cmp["peer_status"] = df_cmp["peer_status"].fillna("Unknown").replace("Unknown", "Not reviewed")
        df_cmp["llm_status"] = df_cmp["llm_status"].fillna("Unknown").replace("Unknown", "Not reviewed")
        ordered_statuses = ["Supported", "Uncertain", "Unsupported", "Not reviewed"]
        df_cmp["peer_status"] = df_cmp["peer_status"].astype(str).str.capitalize()
        df_cmp["llm_status"] = df_cmp["llm_status"].astype(str).str.capitalize()
        df_cmp["peer_status"] = pd.Categorical(df_cmp["peer_status"], categories=ordered_statuses, ordered=True)
        df_cmp["llm_status"] = pd.Categorical(df_cmp["llm_status"], categories=ordered_statuses, ordered=True)
        conf_mat = pd.crosstab(df_cmp["peer_status"], df_cmp["llm_status"]).reindex(
            index=ordered_statuses, columns=ordered_statuses, fill_value=0
        )
        im = ax_conf.imshow(conf_mat.T, cmap="Blues", aspect="equal")
        ax_conf.set_title("OpenEval vs Peer Result Evaluation", fontsize=fontsize+2)
        ax_conf.set_xlabel("Peer Status", fontsize=fontsize+2)
        ax_conf.set_ylabel("OpenEval Status", fontsize=fontsize+2)
        ax_conf.set_xticks(range(len(ordered_statuses)))
        ax_conf.set_yticks(range(len(ordered_statuses)))
        ax_conf.set_xticklabels(ordered_statuses, rotation=45, ha="right", fontsize=fontsize)
        ax_conf.set_yticklabels(ordered_statuses, fontsize=fontsize)
        for i in range(len(ordered_statuses)):
            for j in range(len(ordered_statuses)):
                ax_conf.text(j, i, conf_mat.iloc[j, i], ha="center", va="center", color="black", fontsize=10)
        cbar = fig_conf.colorbar(im, ax=ax_conf, fraction=0.046, pad=0.04)
        cbar.set_label("# Results", fontsize=fontsize)
        ax_conf.set_aspect('equal', adjustable='box')
        plt.tight_layout()
        fig_conf.savefig(v1_dir / "figure_evals_confusion_matrix.png", dpi=300, bbox_inches='tight')
        plt.close()
        
        # --- 3. Scatter plot: claims per result (color by agreement) ---
        fig_scatter, ax_scatter = plt.subplots(figsize=(6.3, 6.3))
        ax_scatter.grid(axis='both', linestyle="--", color="#cccccc", linewidth=1, alpha=0.7, zorder=0)
        ax_scatter.set_axisbelow(True)
        for status in desired_agree_order:
            group = df_cmp[df_cmp["agreement_status"] == status]
            if not group.empty:
                ax_scatter.scatter(
                    group["n_peer_int"], group["n_llm_int"], s=110,
                    label=status, color=colors.get(status, "gray"), edgecolors="black"
                )
                for _, row in group.iterrows():
                    ax_scatter.text(row["n_peer_int"] + 0.2, row["n_llm_int"] + 0.2, 
                                   str(row["llm_result_id"]) + "/" + str(row["peer_result_id"]), fontsize=8)
        min_val = min(df_cmp["n_peer_int"].min(), df_cmp["n_llm_int"].min())
        max_val = max(df_cmp["n_peer_int"].max(), df_cmp["n_llm_int"].max())
        xlim = (-1, max_val + 1)
        ylim = (-1, max_val + 1)
        ax_scatter.set_xlim(xlim)
        ax_scatter.set_ylim(ylim)
        ax_scatter.set_aspect('equal', adjustable='box')
        line_min = min(xlim[0], ylim[0])
        line_max = max(xlim[1], ylim[1])
        ax_scatter.plot([line_min, line_max], [line_min, line_max], "--", color="gray", lw=1, zorder=1)
        ax_scatter.set_title("# Claims per Result", fontsize=fontsize+2)
        ax_scatter.set_xlabel("# Claims (Peer)", fontsize=fontsize+2)
        ax_scatter.set_ylabel("# Claims (OpenEval)", fontsize=fontsize+2)
        xticks = yticks = range(int(line_min), int(line_max) + 1)
        
        def hide_minus1_ticklabels(ticks):
            return ['' if str(tick) == '-1' else str(tick) for tick in ticks]
        
        ax_scatter.set_xticks(xticks)
        ax_scatter.set_yticks(yticks)
        ax_scatter.set_xticklabels(hide_minus1_ticklabels(xticks), fontsize=fontsize)
        ax_scatter.set_yticklabels(hide_minus1_ticklabels(yticks), fontsize=fontsize)
        ax_scatter.legend(title="Agreement Status", fontsize=fontsize, title_fontsize=fontsize, loc="best")
        plt.tight_layout()
        fig_scatter.savefig(v1_dir / "figure_claims_per_result_scatter.png", dpi=300, bbox_inches='tight')
        plt.close()
        
        # --- 4. Combined stacked bar and Jaccard index plot (shared x-axis) ---
        # Prepare values for stacked & Jaccard bar charts
        mask = (~df_cmp["n_peer"].isna()) & (~df_cmp["n_llm"].isna())
        df_overlap = df_cmp[mask].reset_index(drop=True)
        
        sort_agree = desired_agree_order
        def sort_key(row):
            status = str(row["agreement_status"]).capitalize()
            order = sort_agree.index(status) if status in sort_agree else 99
            jaccard = row["intersection_fraction"] if not pd.isnull(row["intersection_fraction"]) else 0
            return (order, -jaccard)
        
        if "agreement_status" in df_overlap.columns and "intersection_fraction" in df_overlap.columns:
            df_overlap = df_overlap.copy()
            df_overlap["agreement_status"] = df_overlap["agreement_status"].astype(str).str.capitalize()
            df_overlap["__sort__"] = df_overlap.apply(sort_key, axis=1)
            df_overlap = df_overlap.sort_values("__sort__").reset_index(drop=True)
            df_overlap = df_overlap.drop(columns="__sort__")
        
        df_overlap["n_llm_only"] = df_overlap["n_llm"] - df_overlap["n_itx"]
        df_overlap["n_peer_only"] = df_overlap["n_peer"] - df_overlap["n_itx"]
        df_overlap["n_shared"] = df_overlap["n_itx"]
        df_overlap["jaccard"] = df_overlap["intersection_fraction"]
        llm_only_counts = df_overlap["n_llm_only"].values
        peer_only_counts = df_overlap["n_peer_only"].values
        shared_counts = df_overlap["n_shared"].values
        jaccard_vals = df_overlap["jaccard"].values
        bar_width = 0.85
        indices = np.arange(len(df_overlap))
        
        if ("llm_result_id" in df_overlap.columns) and ("peer_result_id" in df_overlap.columns):
            xtick_labels = [f"{llm_id}/{peer_id}" for llm_id, peer_id in zip(df_overlap["llm_result_id"], df_overlap["peer_result_id"])]
        else:
            xtick_labels = indices.astype(str)
        
        xtick_label_colors = []
        if "agreement_status" in df_overlap.columns:
            for status in df_overlap["agreement_status"]:
                status_cap = str(status).capitalize()
                xtick_label_colors.append(status_colors.get(status_cap, "#000000"))
        else:
            xtick_label_colors = ["#000000"] * len(xtick_labels)
        
        fig_comb, (ax_stacked, ax_jaccard) = plt.subplots(
            2, 1, 
            figsize=(max(6.5, 0.5*len(indices)), 5),
            sharex=True, 
            gridspec_kw={"height_ratios": [2, 1], "hspace": 0.02}
        )
        
        # Stacked bar: shared / llm only / peer only claims per comparison
        p_shared = ax_stacked.bar(
            indices,
            shared_counts,
            width=bar_width,
            color=colors_stacked["shared"],
            label="Shared",
            edgecolor="black"
        )
        p_llm_only = ax_stacked.bar(
            indices,
            llm_only_counts,
            bottom=shared_counts,
            width=bar_width,
            color=colors_stacked["llm_only"],
            label="LLM Only",
            edgecolor="black"
        )
        p_peer_only = ax_stacked.bar(
            indices,
            peer_only_counts,
            bottom=shared_counts + llm_only_counts,
            width=bar_width,
            color=colors_stacked["peer_only"],
            label="Peer Only",
            edgecolor="black"
        )
        
        ax_stacked.set_title("# Shared Claims per Comparison", fontsize=fontsize+2, pad=10)
        ax_stacked.set_ylabel("# Claims", fontsize=fontsize+2)
        ax_stacked.set_xticks(indices)
        ax_stacked.set_xticklabels([])
        ax_stacked.tick_params(axis='x', length=0)
        ax_stacked.set_yticklabels(ax_stacked.get_yticks(), fontsize=fontsize)
        ax_stacked.legend(fontsize=fontsize, title_fontsize=fontsize, loc='upper left')
        ax_stacked.grid(axis='y', linestyle="--", color="#cccccc", linewidth=1, alpha=0.7, zorder=0)
        ax_stacked.set_axisbelow(True)
        ax_stacked.margins(x=0.01)
        
        # Jaccard index bar plot (bottom)
        bars_jaccard = ax_jaccard.bar(
            indices, jaccard_vals, width=bar_width, color=jaccard_color, edgecolor="black"
        )
        ax_jaccard.set_ylabel("Jaccard Index", fontsize=fontsize+2)
        ax_jaccard.set_xlabel("LLM Result ID / Peer Result ID", fontsize=fontsize+2, labelpad=6)
        ax_jaccard.set_xticks(indices)
        tick_objs = ax_jaccard.set_xticklabels(xtick_labels, fontsize=fontsize, rotation=90)
        for lbl, color in zip(ax_jaccard.get_xticklabels(), xtick_label_colors):
            lbl.set_color(color)
        ax_jaccard.set_ylim(0, 1.05)
        ax_jaccard.set_yticklabels(ax_jaccard.get_yticks(), fontsize=fontsize)
        for idx, val in enumerate(jaccard_vals):
            ax_jaccard.text(idx, val + 0.01, f"{val:.2f}", ha='center', va='bottom', fontsize=8)
        ax_jaccard.grid(axis='y', linestyle="--", color="#cccccc", linewidth=1, alpha=0.7, zorder=0)
        ax_jaccard.set_axisbelow(True)
        ax_jaccard.margins(x=0.01)
        
        plt.tight_layout()
        fig_comb.savefig(v1_dir / "figure_claim_overlap_per_result_bar.png", dpi=300, bbox_inches='tight')
        plt.close()
        
        if verbose:
            print(f"Generated 4 plots for {manuscript_name} in v1 directory")
        
        return True
        
    except Exception as e:
        print(f"Error generating plots for {manuscript_name}: {e}")
        return False


def process_manuscript(manuscript_dir: Path, verbose: bool = False, dry_run: bool = False) -> bool:
    """Process a single manuscript to generate plots."""
    manuscript_name = manuscript_dir.name
    v1_dir = manuscript_dir / "v1"
    
    if dry_run:
        print(f"Would generate plots for {manuscript_name} in v1 directory")
        return True
    
    # Load manuscript data from v1 directory
    data = load_manuscript_data(v1_dir)
    if data is None:
        print(f"Failed to load data for {manuscript_name}")
        return False
    
    # Generate plots and save in v1 directory
    success = generate_plots(manuscript_dir, v1_dir, data, verbose=verbose)
    
    if success:
        print(f"Successfully generated plots for {manuscript_name}")
    else:
        print(f"Failed to generate plots for {manuscript_name}")
    
    return success


def main():
    parser = argparse.ArgumentParser(description="Generate visualization plots for manuscripts and save in v1 directories")
    parser.add_argument("--manuscripts-dir", type=Path, 
                       default=Path(__file__).parent / "manuscripts",
                       help="Directory containing manuscript directories")
    parser.add_argument("--manuscript", type=str, 
                       help="Process only a specific manuscript (e.g., 'elife-00003')")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Enable verbose output")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be done without actually doing it")
    parser.add_argument("--max-manuscripts", type=int,
                       help="Maximum number of manuscripts to process (for testing)")
    
    args = parser.parse_args()
    
    manuscripts_dir = args.manuscripts_dir
    if not manuscripts_dir.exists():
        print(f"Error: Manuscripts directory {manuscripts_dir} does not exist")
        return 1
    
    # Find manuscripts to process
    if args.manuscript:
        manuscript_dir = manuscripts_dir / args.manuscript
        if not manuscript_dir.exists():
            print(f"Error: Manuscript {args.manuscript} not found")
            return 1
        manuscripts = [manuscript_dir]
    else:
        manuscripts = find_manuscripts_with_required_files(manuscripts_dir)
        if args.max_manuscripts:
            manuscripts = manuscripts[:args.max_manuscripts]
    
    print(f"Found {len(manuscripts)} manuscripts with required files to process")
    
    if args.dry_run:
        print("DRY RUN MODE - No plots will be generated")
    
    # Process each manuscript
    successful = 0
    failed = 0
    
    for manuscript_dir in manuscripts:
        try:
            if process_manuscript(manuscript_dir, verbose=args.verbose, dry_run=args.dry_run):
                successful += 1
            else:
                failed += 1
        except KeyboardInterrupt:
            print("\nInterrupted by user")
            break
        except Exception as e:
            print(f"Unexpected error processing {manuscript_dir.name}: {e}")
            failed += 1
    
    print(f"\nSummary:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total: {successful + failed}")
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
