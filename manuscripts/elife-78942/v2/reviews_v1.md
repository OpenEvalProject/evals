# Peer review - Round 1

Editors:
- David M Parichy, https://ror.org/0153tk833 University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78942.sa0](https://doi.org/10.7554/eLife.78942.sa0)

This valuable study advances our understanding of heterogeneous transcriptomic states and genetic requirements of skin-resident pigment cells and pigment cell progenitors in adult zebrafish, relevant to regenerative biology and melanoma origins. The single-cell and bioinformatic analyses and the use of mutants and regeneration assays are carefully done and appropriately interpreted. The work provides useful new observations that will be of interest to researchers focused on the basic biology of adult pigmentary phenotypes and their homeostasis, as well as those pursuing translational aspects of regeneration and melanoma origins and treatments.


---

# Peer review - Round 1

Editors:
- David M Parichy, https://ror.org/0153tk833 University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78942.sa1](https://doi.org/10.7554/eLife.78942.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Stem cell heterogeneity and reiteration of developmental signaling underlie melanocyte regeneration in zebrafish" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Melissa L. Harris (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The consensus opinion is that the work is interesting, makes a valuable contribution to the field, and is appropriate for publication in eLife. The reviews are thorough and identify several issues needing clarification, minor modifications, additional citations, etc., all of which are reasonable and all of which will improve the paper in its final version.

The one major sticking point that is essential to address concerns the identity of mitfa+ aox5-hi cells as the reviewers (and I) are not convinced these are bona fide McSC as opposed to "cryptic" xanthophores. Indeed one might expect cryptic xanthophores to have the transcriptomic profile shown here, clustering with other xanthophores, and to proliferate after melanocyte ablation simply because there is space to do so. The ambiguity could be addressed by tempering relevant portions of the text OR by providing experimental evidence that shows the differentiation of these cells into melanophores (which would be exciting, if true).

Reviewer #2 (Recommendations for the authors):

1) Identity/Xanthophores: The authors list 14 clusters that identify as xanthophores and call them mitfa+aox5+ cells on the UMAP (Figure 1). Later the authors follow mitfa+aox5+ cells dividing by scRNA-seq, and in the stripes and interpret these as McSCs (Figure 6, Figure 7). It seems likely these are simply dividing xanthophores? More evidence is required to link these cells to melanocytes, and melanocyte stem cells.

2) scRNA-seq analysis: Please explain some of the choices taken in the scRNA-seq pipeline.

a. Cells with 200 expressed genes are considered high quality. Can the authors justify this figure?

b. We wonder whether the integration between WT and Kita datasets missed any other major differences between WT and mutant cells? Were the datasets so similar even before the integration?

3) Statistics: Although the authors used appropriate statistical tools in the analysis of the scRNA-seq datasets, we are concerned about the stats used in the plots generated with GraphPad Prism. The Student's t-test can be used when comparing the mean of two datasets with normal distribution. However, it cannot be used for multiple comparisons. Please review the choice of their statistical test for Figures 3C, 4A, 4E, 5B, 5D, 5F, and S5B, and indicate the missing statistical test in Figures S1C, S2D, S6B.

[Please use ANOVA or similar for initial analyses to assess whether significant differences are present overall, and appropriate post hoc comparisons, like Tukey-Kramer, if warranted. Include values of test statistics (e.g., F) with degrees of freedom for overall tests. -Parichy]

4) Context in the field:

a. The authors directly examine adult skin, which has not been done in depth before, and provide an important dataset resource. However, it is important to interpret the data within the context of the wider melanocyte stem cell field (i.e. DRG-associated and daughter cells lining the peripheral nerves as shown by Budi et al., 2011; Singh et al., 2014; Singh et al., 2016, Brombin et al., 2022). These cells are also kit-dependent (Dooley et al., 2013). It is important to address how the melanocyte adult skin progenitors relate to the DRG-associated progenitors. One idea is that the cells that line nerves are a source of melanocytes. Not all the pigment progenitors described by Saunders and colleagues are skin-associated. Could these progenitors contribute to the regeneration in adult fish as previously shown (Budi et al., 2011)?

b. We have concerns with the use of the term "stem cell", and believe the data is more in line with "Progenitor" as they have previously called these cells in Iyengar et al., 2015.

c. For their cycling differentiation cells, it might be appropriate to cite other work showing division of differentiating melanocytes as well (e.g. Taylor et al. 2011)

5) Melanoma: As the authors rightfully claim, the study of McSC might be beneficial to the understanding of how these contribute to melanoma, however, they do not make an actual link to melanoma signatures. Perhaps they could cite and discuss some of the papers that show McSCs and progenitors in zebrafish are relevant to melanoma?

Reviewer #3 (Recommendations for the authors):

This study uses a nice combination of -omics and zebrafish genetics/lineage tracing to heighten our understanding of McSCs and their potential. The manuscript extends our understanding of existing mechanisms (e.g., KIT signaling in McSCs) but also makes small leaps to novel discovery (e.g., identification and function of axo5 self-renewing McSCs). The extensive single-cell datasets generated by this study will be of interest to researchers interested in pigment regeneration, stem cell-based therapeutics for pigment disorders, and the basic biology of stem cells and their heterogeneity. Overall, the data presented seems to support the claims.
