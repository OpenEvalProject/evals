# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92574.3.sa0](https://doi.org/10.7554/eLife.92574.3.sa0)

This valuable paper presents a new approach for association testing, using the output of neural networks that have been trained to predict functional changes from DNA sequences. As such, the approach is an interesting addition to statistical genetics, and the evidence for the presented method being able to identify trait-associations in regions where GWASs are typically underpowered is solid. A limitation is, however, that it is unclear how the quality of these associations compares to those detected using conventional methods. Additional work assessing this method's power and characterizing false positives / false negative regions would be critical to ensure that the method is broadly adopted by the field.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92574.3.sa1](https://doi.org/10.7554/eLife.92574.3.sa1)

Summary:

In this paper, Song, Shi, and Lin use an existing deep learning-based sequence model to derive a score for each haplotype within a genomic region, and then perform association tests between these scores and phenotypes of interest. The authors then perform some downstream analyses (fine-mapping, various enrichment analyses, building polygenic scores) to ensure that these associations are meaningful. The authors find that their approach allows them to find additional associations, the associations have biologically interpretable enrichments in terms of tissues and pathways, and can slightly improve polygenic scores when combined with standard SNP-based PRS.

Strengths:

- I found the central idea of the paper to be conceptually straightforward and an appealing way to use the power of sequence models in an association testing framework.

- The findings are largely biologically interpretable, and it seems like this could be a promising approach to boost power for some downstream applications.

Weaknesses:

- While not a weakness of the manuscript, the proposed method is computationally intensive.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92574.3.sa2](https://doi.org/10.7554/eLife.92574.3.sa2)

Summary:

In this work, Song et al. propose a locus-based framework for performing GWAS and related downstream analyses including finemapping and polygenic risk score (PRS) estimation. GWAS are not sufficiently powered to detect phenotype associations with low-frequency variants. To overcome this limitation, the manuscript proposes a method to aggregate variant impacts on chromatin and transcription across a 4096 base pair (bp) loci in the form of a haplotype function score (HFS). At each locus, an association is computed between the HFS and trait. Computing associations at the level of imputed functional genomic scores enables integration of information across variants spanning the allele frequency spectrum and bolster the power of GWAS.

The HFS for each locus is derived from a sequence-based predictive model - Sei. Sei predicts 21,907 chromatin and TF binding tracks, which can be projected onto 40 pre-defined sequence classes ( representing promoters, enhancers etc.). For each 4096 bp haplotype in their UKB cohort, the proposed method uses the Sei sequence class scores to derive the haplotype function score (HFS). The authors apply their method to 14 polygenic traits, identifying ~16,500 HFS-trait associations. They finemap these trait-associated loci with SuSie, as well perform target gene/pathway discovery and PRS estimation.

Strengths:

Sequence-based deep learning predictors of chromatin status and TF binding have become increasingly accurate over the past few years. Imputing aggregated variant impact using Sei, and then performing an HFS-trait association is therefore an interesting approach to bolster power in GWAS discovery. The manuscript demonstrates that region-level associations can be identified at the level of an aggregated functional score using sequence-based deep learning models. The finemapping and pathway identification analyses suggest that HFS-based associations identify relevant causal pathways and genes from an association study. Identifying associations at the level of functional genomics increases portability of PRSs across populations. Imputing functional genomic predictions using a sequence-based deep learning model does not suffer from the limitation of TWAS where gene expression is imputed from a limited size reference panel such as GTEx and is an interesting direction to bolster discovery power.

However, a few limitations to this method in its current form are:

(1) HFS-based association is going to miss coding variation as well as noncoding regulatory variants such as splicing variants/polyadenylation variants which are not modeled by Sei. This will lead to false negatives in the HFS-based association and additionally false negatives + associated false positives in the finemapping. Going forward, it'll therefore be important to characterize how this influences the genome-wide finemapping.

(2) Sei predicts chromatin status / ChIP-seq peaks in the center of a 4kb region. It is thus not clear therefore whether the functional effects of variants not in the center of the 4kb region would be captured in a single Sei score. It also remains unclear how much the choice of window affects the association tests / finemapping.

(3) There are going to be cases where there's an association driven by a variant that is correlated with a Sei prediction in a neighboring window. These would represent false positives for the method, it would be useful to identify or characterize these cases.

Minor Concerns:

(1) Sequence based deep learning model predictions can be miscalibrated for insertions and deletions (INDELs) as compared to SNPs. It'll be important to note that model INDEL scores may not be calibrated, which might also lead to false positives / false negatives in the finemapping.
