# Peer review - Round 1

Editors:
- Juan Carlos Zúñiga-Pflücker, https://ror.org/03dbr7087 University of Toronto, Sunnybrook Research Institute Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76339.sa0](https://doi.org/10.7554/eLife.76339.sa0)

This paper uses single-cell genomics to examine the heterogeneity of virus-specific CD4 T cells over time in both acute and chronic viral infection. Further, the authors build a comprehensive atlas of the transcriptional evolution of virus-specific CD4 T cell responses that could be used as a reference tool to interpret other datasets. This work characterizes how the antiviral CD4 T cell transcriptional landscape changes with time and will be of broad interest to those that study acute and chronic CD4 T cell responses.


---

# Peer review - Round 1

Editors:
- Juan Carlos Zúñiga-Pflücker, https://ror.org/03dbr7087 University of Toronto, Sunnybrook Research Institute Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76339.sa1](https://doi.org/10.7554/eLife.76339.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A CD4+ T cell reference atlas delineates subtype-specific adaptation during acute and chronic viral infections" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tadatsugu Taniguchi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Laura M Snell (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The reviewers agreed that additional details, clarity, validation, and broader integration of the proposed atlas would strengthen the conclusions and usefulness of the study. However, if these additional analyses lead to altered interpretation or utility of the atlas then the authors should revise the work accordingly.

2) Please pay close attention to the detailed recommendations provided by Rev #2.

Reviewer #1 (Recommendations for the authors):

1) Viral titers should be paired to the different antiviral CD4 T cell transcriptional outcomes. Although LCMV Armstrong is quickly cleared, the clearance kinetics of LCMV Clone 13 can vary dramatically from laboratory to laboratory. The paper simply says that LCMV Clone 13 persists, but it is important to demonstrate how close the virus is to being cleared at the late chronic timepoint, as viral titer will impact transcriptional phenotypes. It will be relevant to have this information when using the reference atlas on other LCMV datasets which may clear with slightly altered kinetics.

2) Gene expression in Th1, Tfh and Tcm(p) is well characterized across time. Does gene expression in the Th1 memory, Tfh memory and Tcm change across early memory to late memory during acute infection? How does gene expression in the Tfh memory in late chronic infection compare to that of early memory (day 21 in both models)?

3) While the changes in proportions of the cell clusters across time and in acute versus chronic viral infection are demonstrated, a big contraction of virus-specific CD4 T cell numbers would be expected between Day 7 and Day 21 in both acute and chronic infection. As such, it would be relevant to also show the absolute number of cells in each cluster across the timepoints to get an accurate depiction of whether the enhancement in proportions of memory clusters also translated to an enhancement in absolute numbers of these clusters, or whether the numbers of memory cells in each cluster are simply maintained across the timepoints.

4) The text says that the atlas with the reference projection algorithm can enable interpretation of CD4 states across models, although all the examples given were based on LCMV datasets. Can the reference atlas accurately determine Th1/Tfh phenotypes from non-LCMV CD4 datasets? Many other models also drive Th1/Tfh differentiation. Single-cell analysis has been done on the discrimination of Th1/Tfh in malaria for instance: Lonnberg T et al. Sci Immunol. 2017 etc. and new data is emerging characterizing CD4s in various cancer models. Does the reference atlas hold up when determining CD4 subsets from data that is not LCMV-based?

5) The figure legends could benefit from more detail. In figure 1 for instance it is unclear if the UMAPs are based on a representative sample or the merged data of all samples. Also, the tissue of origin where the cells were sorted from should be mentioned for the reader's clarity.

Reviewer #2 (Recommendations for the authors):

1) The sequencing batches used to construct the 'atlas' contain biologically distinct samples (Figure 1A-B). Therefore, prior to integration, both technical and biological differences will drive cell separation. In such instances it is useful to have at least one cell population present in all batches to verify integration performance – cells from equivalent populations should produce a joint overlapping cluster whereas biologically distinct populations such as central memory T cells and exhausted T cells should produce distinct clusters. By difficult to understand experimental design, this paper does not seem to have any such populations so the performance of the integration is difficult to assess. Even so, the authors could quantify the degree of alignment between clusters in the d21 Clone 13 samples present in batches 2 and 3, and the d7 Arm samples present in Batch 1 and 2. Based on Figure S2A which is the only data related to integration performance, there is significant heterogeneity between biological replicates. For example, Tregs are virtually absent from the second Late Chronic biological replicate whereas the 'Tfh memory' subset is highly abundant compared to the first replicate. Similarly, the cluster frequencies of the low-frequency clusters look very different between replicates in the Early Memory (d21 Arm) group. Given this uncertainty about integration performance, it is difficult to interpret the subsequent data as it could be partially explained by technical variation between batches.

2) The TCR analysis does not address prior work by Khatun et al. (JEM 2020) which showed that the Tfh bias of certain TCR sequences could be predicted in independent mice. The authors' analysis is limited to stating the degree of bias in each clonotype frequency group. Did the authors attempt to replicate the observation by Khatun et al.? What was the overlap between CDR3 motifs? What was the overlap in motifs between Khatun et al. and this study?

3) The 'atlas' functionality is limited to a superficial demonstration of projecting several LCMV CD4 T cell dataset onto the authors' dataset. There is no data quantifying the performance of this integration in absolute terms or relative to other methods. For example, given that the 9 clusters defined by the authors are previously known CD4 T cell subsets, what is the advantage of using this method compared to quantifying the expression of existing marker gene sets in the primary datasets? What is the performance of this method compared to manual integration of individual datasets?

4) What is the effect of sequencing depth on integration performance? Would low-depth datasets produce annotation results with the most central clusters dominant due to lack of specific, cluster-defining lowly expressed genes? What is the minimum depth at which technical effects would not drive integration? This type of information is essential if the 'atlas' is to be used as a tool, otherwise the resulting misannotations could do more harm than good to the users.

5) It is unclear how the removal of cell cycle genes from the initial dataset affects interpretation and integration. Given that cell cycle state and cell fate are causally linked in T cells, would the removal of cell cycle genes not obscure some meaningful transcriptomic differences between populations? Are the cell cycle genes in dividing effector cells the same as in dividing early memory cells?

6) The experimental validation of this dataset is limited to showing that CD4 T cells in persistent infection express more EOMES than T cells in acutely infected mice and that they express lower levels of THPOK. However, what is the global alignment between flow cytometry data presented in Figure 1 and the scRNAseq data? Were any of the cluster frequencies predicted by the scRNAseq data validated using a protein panel?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A CD4+ T cell reference map delineates subtype-specific adaptation during acute and chronic viral infections" for further consideration by eLife. Your revised article has been evaluated by Tadatsugu Taniguchi (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there is one remaining issue that needs to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

In general this reviewer is satisfied with the revisions to the manuscript, however, one point needs to be better clarified. When the tumor-specific CD4 T cells from TILs were projected into the reference map 40-50% of them mapped into Th1 effectors. Yet upon further analysis and reclustering, these cells ended up being a completely distinct population of cells from the viral effector Th1. Thus, this reviewer is worried this could lead to misinterpretation and incorrect identification of subsets when using the reference map on other systems with unrepresented subsets not in the reference map. Could the authors comment on/clarify this point? It would be helpful to discuss the additional steps needed to verify that the corresponding states determined from projecting one's data into the reference map have similar gene profiles, and if they do not, how to address and identify these novel populations not represented in the map.

Reviewer #2 (Recommendations for the authors):

The authors have addressed my concerns. I can now recommend publication.
