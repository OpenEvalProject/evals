# Peer review - Round 1

Editors:
- Howard Y Chang, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63632.sa1](https://doi.org/10.7554/eLife.63632.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Swanson et al. present TEA-seq that enables simultaneous profiling of chromatin accessibility, RNA, protein epitope profiling from the same individual cells. This method uses an optimized lysis protocol that retains cellular membranes but allows for the capture of high quality chromatin accessibility data. TEA-seq has been optimized and shown to work in blood cells.

Decision letter after peer review:

Thank you for submitting your article "TEA-seq: a trimodal assay for integrated single cell measurement of transcripts, epitopes, and chromatin accessibility" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Andrew C Adey (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

Swanson et al. present two novel methods, ICICLE-seq and TEA-seq, which both benefit from an optimized lysis protocol that retains cellular membranes but allows for the capture of high quality chromatin accessibility data. This enables the simultaneous profiling of chromatin accessibility and cellular epitopes (ICICLE-seq) and can be used in conjunction with the 10x Genomics Multiome kit to additionally acquire cellular epitopes. The strengths of the manuscript are the attention to detail, the clarity of the methods, and the availability of all data. The primary weakness is in the presentation of ICICLE-seq and TEA-seq as related methods and in the lack of analytical exploration of the TEA-seq data.

Essential revisions:

1) The differences and similarities between ICICLE-seq and TEA-seq are confusing and their presentation in a single paper seems convoluted. These are two different methods that are enabled by a specific lysis protocol. Given that the title exclusively focuses on TEA-seq but TEA-seq occupies a very small percentage of the manuscript's real estate and innovation, we think the manuscript could benefit from a clearer presentation of TEA-seq.

2) Extension of TEA-seq to samples beyond PBMC. The reported optimizations are highly specific to PBMCs and this could be made clearer. There are many reasons to think that these same optimizations might not hold up in other cell types. The authors should either (a) perform the same comparisons on different cell lines or cell types that have proven to be troublesome in previous ATAC-seq experiments or (b) at least make it more explicit that these optimizations may not hold for other cell types. A good example of the former is K562 cells which had very high mitochondrial DNA contamination and very low signal to noise in the original ATAC-seq protocol.

3) Deeper analysis leveraging the 3-way single cell data in TEA-seq. Some additional analysis as to the improvement of separation and identification of cell types using the 3-way manifold should be explored. i.e. perform clustering and cell type ID on each independently and then identify overlap / which cell types are poorly separated in one modality but not another and then how the 3-way manifold performs as a comparison. Overall it looks like the RNA performs fine for cell type ID when compared to the 3-way with the other modalities performing worse (though that is form UMAP visualizations which are not able to be quantitatively interpreted for these purposes). In addition,, given the tri-modal data derived from TEA-seq, the authors should have the ability to assess how well scATAC-seq or scRNA-seq correlate with protein levels, albeit for a small set of proteins biased for cell surface proteins.
