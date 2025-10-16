# Peer review - Round 1

Editors:
- Jiwon Shim, https://ror.org/046865y68 Hanyang University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79363.sa0](https://doi.org/10.7554/eLife.79363.sa0)

This study generated an important single-cell transcriptome dataset using young/aged hematopoietic stem/progenitor cells obtained from normal individuals and those with MDS. The new resource provides a convincing dataset to understand a unique transcriptional landscape in elderly individuals, compared to young individuals, proving the hematopoietic aging at a transcriptome level. This manuscript will be of interest to readers in the field of hematopoiesis and associated diseases, aging, and single-cell RNA sequencing.


---

# Peer review - Round 1

Editors:
- Jiwon Shim, https://ror.org/046865y68 Hanyang University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79363.sa1](https://doi.org/10.7554/eLife.79363.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Uncovering perturbations in human hematopoiesis associated with healthy aging and myeloid malignancies at single cell resolution" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Utpal Banerjee as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Jong Kyoung Kim (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Validate GLMnet and apply a consistent analysis platform throughout (e.g. STREAM or Palantir for pseudotime, manual annotation): All reviewers

2. Substantiate and clarify MDS analysis: (1) Same analytical strategy should be applied for young/old and MDS patients, (2) a detailed comparison between MDS-aging, (3) add clinical details: All reviewers

3. Additional supports required for the HSC population analysis, clarify young/elderly data analysis from the clonal hematopoiesis perspective: Reviewers 1 and 2

4. Consistent data description and additional validation for age-dependent cell type changes: Reviewers 1 and 3

5. Additional data/quantitation/explanation required for GRN analysis between young and old: Reviewers 2 and 3

Reviewer #1 (Recommendations for the authors):

1. In Figure 1b and d, elderly2 individual expresses a significantly higher HSC proportion than the other two with reductions in other populations, which can skew an entire landscape of elderly populations. Is there any other data supporting that the proportions of HSCs from elderly donors shown in Figures 1b,d are representative?

2. Regarding the above concern, what is the age distribution of elderly individuals? In a very recent study showing the clonal diversity of HSC/MPP cells in humans (for example, Mitchell et al., Nature 2022), it has been shown that the elderly over 65 yrs dramatically reduce the clonal diversity and this might be contributed to the biased HSC proportions shown in elderly2 data. Brief information, at least an age, of individuals needs to be provided as in sup table 5 for healthy donors, if possible, and discuss the extreme bias generated in elderly2 data.

3. In Figure 1e, the authors concluded that Myc is downregulated, and proliferative activity is decreased in cells of elderly individuals. However, some of the populations are rather expanded in elderly individuals; for example, the numbers of HSC or MEP are rather higher in elderly individuals. How would the authors explain such discrepancies?

4. As a nonexpert, it is not clear to me why Seurat or GLMnet-based labeling results in dissimilar proportions of cell populations. Would differing cutoffs or measurements of Seurat have given similar numbers to GLMnet? Or would it be possible to acquire numbers similar to Seurat or GLMnet with an alternative method? It would become a much-valued resource for the community if the data presented here, from young, and elderly to MDS, are analyzed in a consistent platform with a clear rationale.

5. In Figure 3e, the authors claim that HSCs from young donors show enriched terms related to differentiation of hematopoietic lineages while elderly donors do not display such an increase. However, it is not clear whether changes in the gene expression of HSCs from young donors are attributed to uniform alterations in HSC gene expressions or due to changes in the composition of HSC subsets.

1) The gene regulatory network of HSCs in elderly donors might have undergone a global change, but it is also possible that a landscape of HSC subsets (for example, long-term, short-term, or different subsets segregated by different niche interactions) could change, consequently leading to altered gene expressions.

2) Is it possible to subcategorize HSCs, for example, cells with high differentiation genes versus low, and compare them between young versus elderly?

3) Are HSCs in both young and elderly clear enough? It is possible that intermediate/committed cells, simultaneously holding stem cell characteristics, are mixed in HSC populations.

6. Even though this paper is a resource article, explanations of the MDS data are not clear enough and additional analysis may be required to better understand the disease.

1) Are the same cell types annotated when the same method used in young/elderly is applied to MDS patients?

2) It is reasonable to conclude that MDS cases show high heterogeneity of the GRN levels and each patient has specific regulons for the disease development. If so, do the four MDS patients show differential trajectories of HSC differentiation? And how are these single-cell landscapes from 4 patients associated with genetic mutations in each case (shown in sup table5)?

3) If MDS is a heterogenic disease, what would be a common idea, which can be used for future studies and therapeutics, extracted from single-cell RNA analyses?

Reviewer #2 (Recommendations for the authors):

I do not recommend this manuscript for publication form based on the following reasons:

1. The main claims derived from computational predictions were not well supported by the data presented and were not experimentally validated (Major points 1 to 6 of the Public Review).

2. I think if the authors address Major point 7 of the Public Review, the value of the single-cell dataset as a resource for understanding the age-associated cellular and molecular alterations during human hematopoiesis will be greatly improved. However, I agree that this would be beyond the scope of this manuscript.

If the manuscript is revised to address these concerns, I can reconsider my recommendation.

Reviewer #3 (Recommendations for the authors):

1. Section 'GRNs guiding young and elderly hematopoiesis' focuses on differences in transcription factor regulatory networks between young and old. Whilst an elegant analysis, it does not appear to add much more insight than the previous sections which identify expanded HSC and impaired differentiation in the elderly datasets. We would consider reducing this section and merging it with the previous one.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Uncovering perturbations in human hematopoiesis associated with healthy aging and myeloid malignancies at single cell resolution" for further consideration by eLife. Your revised article has been evaluated by Utpal Banerjee (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Although the authors addressed most of the concerns, some of the major comments require additional changes to warrant publication in eLife. Please find the concerns raised by reviewer 2, especially ones regarding the previous major comments 2 and 3.

Reviewer #1 (Recommendations for the authors):

The authors performed additional analyses and experiments and adequately addressed all of my major concerns.

Reviewer #2 (Recommendations for the authors):

The authors should specify or highlight changes in their manuscript and rebuttal. It is difficult for me to follow changes in this revised manuscript. The revised manuscript addressed some of my previous concerns but failed to address the following points:

1. Previous major comment 2 (cell-type composition changes): The newly added flow cytometry data did not support an expansion of MEPs and a reduction of GMPs in elderly individuals predicted by scRNA-seq analysis. The sentence at line 178-179 ("We used Flow Activated Cell Sorting (FACS) as an orthogonal method to support our findings (Figure 1—figure supplement 3) and observed similar results.") should be toned down accordingly.

2. Previous major comment 3 (STREAM and Palantir): I strongly disagree with the authors's opinion that mixing the results of two different methods in the same figure can be helpful for deciding which method is better suited to specific problems. Figure 2F and G can be equally well presented with pseudotime computed by STREAM as the authors showed that pseudotime values from two methods are highly correlated. To avoid any confusion and be consistent, the authors should not mix the results of two different methods in the same figure. The results generated by Palantir should be presented in a supplementary figure to demonstrate the robustness of pseudotime analysis.

3. Previous major comment 5: What does "independent network" mean?

4. Previous major comment 6: Even though this manuscript was submitted as a "Tools and Resources" article, the authors should demonstrate the robustness of their constructed GRNs. All research papers should convincingly show that the results and predictions presented in the manuscript are robust and consistent regardless of the category of the submitted manuscript. The benchmarking papers and other research papers have already shown that all methods for constructing GRNs from scRNA-seq data (including SCENIC) have an issue of false positive and negative predictions.

Reviewer #3 (Recommendations for the authors):

The authors comprehensively addressed the comments. I have no further concerns.
