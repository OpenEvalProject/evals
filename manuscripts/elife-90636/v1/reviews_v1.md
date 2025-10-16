# Peer review - Round 1

Editors:
- Alexander Young, University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90636.3.sa0](https://doi.org/10.7554/eLife.90636.3.sa0)

This study presents a useful new approach for efficient computation of statistics on correlations between genetic variants (linkage disequilibrium, or LD), which the authors apply to quantify the extent of LD across chromosomes. The method and its derivation are solid. The authors document that cross-chromosome LD can be substantial, which has implications for geneticists who are interested in population structure and its impact on genetic association studies.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90636.3.sa1](https://doi.org/10.7554/eLife.90636.3.sa1)

Summary:

In this paper, the authors point out that the standard approach of estimating LD is inefficient for datasets with large numbers of SNPs, with a computational cost of O(nm^2), where n is the number of individuals and m is the number of SNPs. Using the known relationship between the LD matrix and the genomic-relatedness matrix, they can calculate the mean level of LD within the genome or across genomic segments with a computational cost of O(n^2m). Since in most datasets, n<

Strengths:

Generally, for computational papers like this, the proof is in the pudding, and the authors have been successful at their aim of producing an efficient computational tool. The most compelling evidence of this in the paper are Figure 2 and Supplementary Figure S2. In Figure 2, they report how well their X-LD estimates of LD compare to estimates based on the standard approach using PLINK. They appear to have very good agreement. In Figure S2, they report the computational runtime of X-LD vs PLINK, and as expected X-LD is faster than PLINK as long as it is evaluating LD for more than 8000 SNPs.

Weakness:

This method seems to be limited to calculating average levels of LD in broad regions of the genome. While it would be possible to make the regions more fine-grained, doing so appears to make this approach much less efficient. As such, applications of this method may be limited to those proposed in the paper, for questions where average LD of large chromosomal segments is informative.

Impact:

This approach seems to produce real gains for settings where broad average levels of LD are useful to know, but it will likely have less of an impact in settings where fine-grained levels are LD are necessary (e.g., accounting for LD in GWAS summary statistics).
