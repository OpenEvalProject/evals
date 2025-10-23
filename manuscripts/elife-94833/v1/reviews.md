# Peer review - Round 1

Editors:
- Siming Zhao, https://ror.org/049s0rh22 Dartmouth College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94833.4.sa0](https://doi.org/10.7554/eLife.94833.4.sa0)

This study presents an important computational tool for the quantification of the cellular composition of human tissues profiled with ATAC-seq. The methodology and its application results on breast cancer tumor tissues are convincing. It advances existing methods by utilizing a comprehensive reference profile for major cancer-relevant cell types, compatible with a widely-used cell type deconvolution tool.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94833.4.sa1](https://doi.org/10.7554/eLife.94833.4.sa1)

Summary:

Building upon their famous tool for the deconvolution of human transcriptomics data (EPIC), Gabriel et al. implemented a new methodology for the quantification of the cellular composition of samples profiled with Assay for Transposase-Accessible Chromatin sequencing (ATAC-seq). To build a signature for ATAC-seq deconvolution, they first created a compendium of ATAC-seq data and derived chromatin accessibility marker peaks and reference profiles for 12 cell types, encompassing immune cells, endothelial cells, and fibroblasts. Then, they coupled this novel signature with the EPIC deconvolution framework based on constrained least-square regression to derive a dedicated tool called EPIC-ATAC. The method was then assessed using real and pseudo-bulk ATAC-seq data from human peripheral blood mononuclear cells (PBMC) and, finally, applied to ATAC-seq data from breast cancer tumors to show it accurately quantifies their immune contexture.

Strengths:

Overall, the work is of very high quality. The proposed tool is timely; its implementation, characterization, and validation are based on rigorous methodologies and results in robust estimates. The newly-generated, validation data and the code are publicly available and well-documented. Therefore, I believe this work and the associated resources will greatly benefit the scientific community.

Weaknesses:

In the benchmarking analysis, EPIC-ATAC was compared also to deconvolution methods that were originally developed for transcriptomics and not for ATAC-seq data. However, the authors described in detail the specific settings used to analyze this different data modality as robustly as possible, and they discussed possible limitations and ideas for future improvement.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94833.4.sa2](https://doi.org/10.7554/eLife.94833.4.sa2)

Summary:

The manuscript expands the current bulk sequencing data deconvolution toolkit to include ATAC-seq. The EPIC-ATAC tool successfully predicts accurate proportions of immune cells in bulk tumour samples and EPIC-ATAC seems to perform well in benchmarking analyses. The authors achieve their aim of developing a new bulk ATAC-seq deconvolution tool.

Strengths:

The manuscript describes simple and understandable experiments to demonstrate the accuracy of EPIC-ATAC. They have also been incredibly thorough with their reference dataset collections and have been robust in their benchmarking endeavours and measured EPIC-ATAC against multiple datasets and tools. This tool will be valuable to the community it serves.
