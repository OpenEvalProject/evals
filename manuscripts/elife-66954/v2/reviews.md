# Peer review - Round 1

Editors:
- Jiwon Shim, Hanyang University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66954.sa1](https://doi.org/10.7554/eLife.66954.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Unlike in classical model organisms, it has been challenging to comprehensively understand the biological attributes of cells in non-model systems such as in shrimps. This study takes advantage of single-cell RNA sequencing and profiles the diversity and putative lineages of shrimp hemocytes. The primary claims are well supported by the data, and this study will contribute substantially, not only to crustacean biology but also related areas.

Decision letter after peer review:

Thank you for submitting your article "Single-cell RNA-seq analysis reveals penaeid shrimp hemocyte subpopulations and cell differentiation process" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Utpal Banerjee as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

The reviewers agreed that the study was well-performed and analyzed and bears the potentials to improve understandings of shrimp immune systems. Reviewers raised several concerns and recognized that additional data QC is essential to make strong conclusions. Requirements on in vivo validation will further strengthen the paper; however, the reviewers agreed it would not be feasible to perform the experiments suggested. Please find the list below and details in reviewers' comments.

Data QC:

1. de novo assembly and correlation to reference genome

2. Cell viability and low UMI

3. Batch effects (similarities between triplicates) and doublets

4. Cutoff values for the number of UMI per cell

5. Mitochondrial contents

6. Additional analysis for subcluster clustering including Hem1 and Hem6

7. Re-validation of pseudotime and lineage analyses

in vivo validation:

The reviewers acknowledged that it is difficult to do in-depth in vivo verification with shrimps. The working model (e.g. Figure 7) could be modified or removed if additional in vivo validations are not provided. If possible, in vivo experiments could be supplied to keep the model.

Reviewer #1 (Recommendations for the authors):

1. Page 5 line 88, Cho et al. Nature Communications (2020) [PMID 32900993] sequenced Drosophila hemocytes in various conditions using the Drop-Seq platform.

2. Page 11 line 162, typo; TINGAL to TINAGL

3. In Figure 3B, please consider adding pseudotime density plots for each Hem cluster. I think this can clearly show where Hem clusters are located in the trajectory.

4. In Figure 6F, the authors showed that a subset of marker genes are differentially expressed in R1 or R2 groups with the use of qRT-PCR. However, it is not clear the data is statistically sound to claim the result. Additional statistical analysis is required to adequately support the authors' claim.

5. The authors used "top 3,000 most variable genes" in the PCA while the data have 3,334 commonly expressed genes. Are all these variable genes included in the "common genes"? This point should be confirmed.

Reviewer #2 (Recommendations for the authors):

It would help a reader to analyze the data if the Drosophila genes corresponding to the Mj genes in figure3 supplement 1 and figure 3 supplement 2 were included at the side in the "table".

Figure 7 is too speculative since no functional experiments (as RNAi) has been done to confirm the schedule, and therefore figure 7 should be removed.

The quality check should also be discussed more as well as the low number of UMI, and the percentage of mitochondrial genes should be included.

The last part with FACS sorting and qPCR could be removed, since this doesn't add any information or confirmation. The proposed lineages could also be discussed in a bit more critical way.

Reviewer #3 (Recommendations for the authors):

The following suggestions might help the authors to strength the science or improve the manuscript:

1. There is a small cluster of cells of Hem1 up of the label of 'Hem1' in Figure 1, but this small cluster was gone in all other analysis. Can you discuss about this particular cluster?

2. Previous study indicates phagocytosis by hemocyte is a crucial defense mechanism for the host against infections (PMID: 32194551). Those phagocytotic hemocytes should be terminally differentiated cells, and phagocytosis related genes should express in those cells. Can you check how those genes are expressed in the shrimp hemocytes? This could further confirm your differentiation hypothesis.

3. Two additional Drosophila hemocyte single-cell RNA sequencing papers should be cited (PMID: 32487456; PMID: 32162708).

4. The method used for the dye staining in Figure 6B and D should be presented in the Materials and methods part.

5. The primer sequence used for qRT-PCR should be presented in the Materials and methods part.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Single-cell RNA-seq analysis reveals penaeid shrimp hemocyte subpopulations and cell differentiation process" for further consideration by eLife. Your revised article has been evaluated by Utpal Banerjee (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

As you can find below comments, the reviewers agreed that the authors addressed most of the concerns by reanalyzing and processing the data. Yet, the new data raise additional points with regards to (1) considerably different conclusions obtained by alternative parameters and (2) multiple calls of the same gene transcripts in some analyses due to the lack of reference genome. These points need to be reanalyzed if possible or at least be discussed.

Reviewer #1 (Recommendations for the authors):

The authors performed additional analyses and successfully addressed all the major concerns. The authors substantially enhanced the quality of data by removing dead cells and increasing UMI/gene counts. Although overall numbers of UMI and genes are still lower than those of other model organisms, it would be potentially improved with a reference genome which is expected to be built shortly. The quality of clustering is also clear enough. Further, descriptions of in vivo experiments and models are simplified as suggested, and I hope to see in-depth validation in the near future.

Reviewer #2 (Recommendations for the authors):

The authors have responded to all questions but my main concern is that when they remade the analysis nearly completely, the results were so different with a new software and when new parameters are used. This is a bit worrying especially for the lineage determination. In the first version the conclusion was four lineages and now only two lineages. The authors need to explain why the resolution is so very different.

A problem that should at least be discussed is related to the lack of genome sequence, and this is evident for example in figure 8 figure supplement 1, where several transcripts seem to be from the same gene (AMH87234.1 = Mj-18245 + Mj-19281+ Mj-20968 and ABW88999.1=Mj-3787+Mj-19067+Mj-19338+Mj-28125). This is always a problem when using transcriptome instead of a fully annotated genome, and it is important to be aware of that single-cell RNA-seq provides only a snapshot of each individual cell and they may be in different stages of the cell cycle and / or turnover of RNA. Therefore, transcripts belonging to the same gene should be merged when possible. I realize that this is impossible for all transcripts, but for known important immune genes and/or cell cycle genes used in the clustering and lineage determination it should be done.

Regarding the validation at line 492 and forward, this is still not meaningful. The authors say that BrdU incorporation and in situ hybridization are not possible for shrimp hemocytes, but there are several published studies showing in situ hybridization of crustacean hemocytes so this answer is difficult to understand. The FACS-analysis is not a good enough separation, and in situ hybridization of some of the transcripts could be of value to show the morphology of the corresponding cell. Maybe morphology doesn't tell us so much, but this is important to show.

Reviewer #3 (Recommendations for the authors):

The authors did a great job in the revised manuscript to address all the concerns that I had for the first submission.
