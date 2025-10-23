# Peer review - Round 1

Editors:
- Shimon Sakaguchi, https://ror.org/035t8zc32 Osaka University Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73998.sa0](https://doi.org/10.7554/eLife.73998.sa0)

This report shows by scRNAs-seq and scATAC-seq the presence of a population of proliferating medullary thymic epithelial cells (mTECs) with a specific chromatin structure and high expression of Aire and CD80. Such Aire-expressing transit-amplifying mTECs may play a key role in establishing immunological self-tolerance.


---

# Peer review - Round 1

Editors:
- Shimon Sakaguchi, https://ror.org/035t8zc32 Osaka University Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73998.sa1](https://doi.org/10.7554/eLife.73998.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Integrative analysis of scRNAs-seq and scATAC-seq revealed transit-amplifying thymic epithelial cells expressing autoimmune regulator" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Betty Diamond as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The scATACseq experiment included a relatively low number (n=2) of mice. Understandably this is a complicated experiment, however, the variation between individual animals remains unknown and may influence the interpretation of the results. The authors are advised to show the clustering analysis for the two animals separately in a supplement to confirm that the changes are seen in both animals, not just in one. Similarly, the individual scRNA-seq UMAPs of the three animals should be included in the supplement. The authors should discuss the limitations of small groups in single-cell experiments in Discussion. Technically the integration of scATAC and scRNA seq results may be feasible.

2. Genes expressed in clusters should be provided in the supplement. Without this information, it is difficult to see the feasibility of the cluster annotations and to compare them with other similar studies. The authors should give an unbiased list of all genes expressed in mTECs, in particular those genes that are expressed in TACs. To harmonize the findings in the field, it would be useful for the readers if the authors would compare their cluster-specific genes for the overlap with TEC single-cell clusters from other studies (Bornstein et al., 2018, Dhalla et al., 2020, Baran-Gale et al., 2020, Wells et al., 2020). In addition, Wells et al., 2020 reported mTEC TACs to be mTEClo preceding Aire expression and giving rise to both Aire+ and Ccl21a+ cells. How do the authors reconcile their results (TAC as Aire+) with Wells et al., paper (TACs as Aire-)? How do they interpret the finding that Wells et al., find Ki67 significantly higher in mTEClo than in mTEChi, implying that cell division precedes high the expression of Aire?

4. The candidate cell population for TACs, cluster R1 expresses Aire and the proliferating cell marker Mki67. R1 also expresses Ccl21a. The authors did subclustering of R1 and found that R1A-D express Aire whereas R1E has a higher expression of Ccl21a. The authors note that "Thus, it is possible that TECs expressing cell-cycle-related genes, proposed by scRNA-seq analysis, contain at least two proliferating TECs subsets having different chromatin accessibilities and gene expression profiles." To confirm that both R1A-D and R1E subsets are proliferating TACs, the authors might show the proliferating gene markers in these subsets. Was Mki67 expressed among all R1 subpopulations? Would this argue for the presence of TAC among both Aire+ and Aire- cell populations? Assuming that TACs as a proliferating cell type should express multiple genes associated with cell cycling, the authors focus on Mki67 only, but did R1 TAC express other proliferating cell markers which would support the claim that these are indeed actively dividing cells?

6. The authors focus their study on the CD80high cycling cells (Aire+). Figure 4 show transcription profiles of the isolated cycling CD80+ mTECs. Dots in the "TSA genes" panel (right) don't appear in the "All genes" panel (left). Are those lost dots of TSA genes?

In Figure 4E (left) low expressed genes seem to be skewed towards Venus- mTEChi (in comparison to high expressed genes). A statistical assessment for the comparisons of the TSA, Aire-dep TSA and Aire-indep TSA profiles to the general profile (Figure 4E and 4G), considering expression levels, would confirm the visual assessment.

They should also discuss the reason why m-cherry low cells express a lower level of tissue-specific antigens even though they express Aire? Is Aire expression alone insufficient for TSA expression? Does the transcriptome data provide any mechanistic insight? In Fig4F, Aire expression is similar between Venus+ and Venus-. Is it compatible with Figure 4A showing less Aire-expressing cells in Venus+ than in Venus-?

7. In Figure 6, they showed that RTOC culture of mCherry-low cells produced mCherry-high cells, thereby they claimed that mCherry-low cells differentiated into mCherry-high cells. To substantiate this notion, they should rule out the possibility of selective cell survival of possibly contaminated mCherry-high cells or that transferring adult mTECs into the embryonic cell environment may trigger other signaling pathways that induce the upregulation of the cell cycle and mCherry expression? For example, what about the expression profiles of cell-death/apoptosis-related genes in mCherry low and high cells? What about the cell number of mCherry high cells after RTOC culture using mCherry-high cells alone as a control group? Is the cellularity of survivors comparable to RTOC culture using mCherry-low as shown in figure 6A? Would the same happen if they would transfer these cells to the adult thymus?

8. The authors nicely confirm, by the fine analysis of their scRNA-seq data, that the TAC population contains Aire+ cells and Ccl21+ cells in a visually mutually exclusive manner. However, they don't formally clarify whether the Ccl21-expressing TACs have differences in their chromatin accessibility pattern compared to the Aire-expressing TACs.

It's also worth showing the expression of CD80 in the scRNA-seq UMAP of TACs alone and in the one of all TECs (Figure 2). This would notably allow to determine whether CD80 expression is restricted to Aire-positive TACs or encompasses Aire-negative TACs (Ccl21+).

Also, projection of the R1A-E scRNAseq clusters onto the scATAC-seq UMPA would be enlightening.

9. Trajectory analyses provide a nice confirmation of published results identifying a trajectory from TACs to mTEChi. However, the authors don't discuss whether their data support a potential trajectory from TACs to mTEClo (already suggested/ reported) which seems to be present in Figure 3-Figure sup 2B. Would this mean that some TACs could mature into Ccl21+ mTECs (mTEClo)? and if so, how Aire and Ccl21 are expressed in these TACs? Which TAC sub-cluster do they belong to?

10. In figure S7, the data of fetal thymi showed that proliferating fetal mTECs might have a gene expression profile different from the adult counterpart. One caveat of the interpretation of the data is that the difference between the public data and the authors' data might be attributed to a batch effect because the clusters from two data sets seemed almost completely discrete. They should mention how they processed the data to diminish the risk of such artifacts. Or, it is better to add the data of fetal thymi obtained by the authors themselves, if possible.

Reviewer #1 (Recommendations for the authors):

Regarding figure 4, they should discuss the reason why m-cherry low cells express a lower level of tissue-specific antigens even though they express Aire? Is Aire expression alone insufficient for TSA expression? Does the transcriptome data provide any mechanistic insight?

In figure 6, they showed that RTOC culture of mCherry-low cells produced mCherry-high cells, thereby they claimed that mCherry-low cells differentiated into mCherry-high cells. To substantiate this notion, they should rule out the possibility of selective cell survival of possibly contaminated mCherry-high cells. For example, what about the expression profiles of cell-death/apoptosis-related genes in mCherry low and high cells? What about the cell number of mCherry high cells after RTOC culture using mCherry-high cells alone as a control group? Is the cellularity of survivors comparable to RTOC culture using mCherry-low as shown in figure 6A?

In figure S7, the data of fetal thymi showed that proliferating fetal mTECs might have a gene expression profile different from the adult counterpart. One caveat of the interpretation of the data is that the difference between the public data and the authors' data might be attributed to a batch effect because the clusters from two data sets seemed almost completely discrete. They should mention how they processed the data to diminish the risk of such artifacts. Or, it is better to add the data of fetal thymi obtained by the authors themselves, if possible.

Reviewer #2 (Recommendations for the authors):

– Figure 2A has 2 Ic populations but lacks Ia?

– Figure 1c Y axis is shown as "expression level", this should be rather "accessibility level"?

– The Fucci system incorporates genetically encoded Cherry and Venus probes that highlight G1 and S/G2/M phases of the cell cycle in animal cells. Did the authors control for the transgene inactivation in these mice as in some cases the expression of the transgenes may change?

Reviewer #3 (Recommendations for the authors):

Related to point (1): projection of the R1A-E scRNAseq clusters onto the scATAC-seq UMPA would be enlightening.
