# Peer review - Round 1

Editors:
- Sara Hägg, https://ror.org/056d84691 Karolinska Institutet Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74915.sa0](https://doi.org/10.7554/eLife.74915.sa0)

The study describes a single-cell analysis of the mammalian ovary in young, adult, and old mice, and is an important contribution to the field identifying clusters of immune cell populations across the different ages. The combination of single-cell RNA sequencing and flow cytometry used is a robust and unbiased approach that provides compelling evidence of immune cell alterations in aged ovaries.


---

# Peer review - Round 1

Editors:
- Sara Hägg, https://ror.org/056d84691 Karolinska Institutet Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74915.sa1](https://doi.org/10.7554/eLife.74915.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Single-cell analysis of the aged ovarian immune system reveals a shift towards adaptive immunity and attenuated cell function" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ricardo Azziz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Figure 1-2 begins to tell an interesting story of changes in macrophage and an ovary specific CD3+ CD4- CD8- double negative T-cell abundances in aging. While the flow cytometry here backs up their claims, the statistical rigor of the single-cell analysis itself is questionable. Rather than further probing gene expression differences in these specific subpopulations, the next sections proceeds to do (1) a global analysis of gene expression changes, (2) a CCC analysis (independent of existing tools) that claims decreased inflammation (see below points about doubts regarding this), and (3) an analysis of SASP recognition that is very limited.

2. Results for Figure 1-3 can be published with some changes. Figure 4 would need a lot of additional analyses and changes. The SASP section with no main figure associated shouldn't be included.

3. Code for computational analyses should at least be available on Github, preferably on CodeOcean for reproducible runs.

4. My concern regarding the single-cell results is that there does not seem to be a formal batch correction step. Figure 2A visually seems to show minimal batch effects, and a big positive is that flow cytometry results align with the single-cell observations. Unfortunately, it is impossible to rigorously claim from the scRNAseq that the cluster 12 frequency change is due to aging without a formal batch correction.

5. The problem with applying a batch correction now, even if there aren't major batch effects, would be that it can change downstream results at some resolution (e.g. p-values and effect sizes). A solution would be to add a supplemental section demonstrating that there are not batch effects. This may be done by applying a batch correction (e.g., Harmony or Seurat integration), and demonstrating that downstream clustering patterns remain similar (indicating that the informative transcriptional space of the cells are consistent).

6. A separate but complementary point regarding the question of frequency change in cluster 12 using scRNAseq: unlike microbiome, which has comprehensive compositional analysis methods, the question of cell abundance changes in single-cell is just recently beginning to be addressed. To more rigorously present these results, a few things would be useful:

6.1 Higher resolution in Figure 2C,D – specifically, gating on the CD3+ lymphocyte subpopulations, as well as some control cell types that do not show a change in single-cell (preferably, all cell type frequencies validated with flow).

6.2 More quantification of effect size or statistical assessment of Figure 1B using recently published tools. Some tools have been published on differential abundance testing in single-cell in the last couple years include scDC, MILO, and DA-seq.

7. As a side note, MELD does not give a differential abundance p-value, but does quantify the likelihood of observing a given cell in a given condition at single-cell resolution and allows you to further partition the data based on those values. This can allow for higher resolution differential expression testing and may be useful to you for future analyses.

8. There is a lack of multiple test correction (or stating of such correction) throughout statistical analyses which must be addressed.

9. It is difficult to trust the "skewed" DE patterns, especially for DNT cells (Figure 3A) -- a global downregulation of genes?

10. The claim regarding a decreased inflammatory state in aging is unconvincing. Currently, the results indicate a global downregulation of the transcriptome in aging, and so when you visualize just chemokines and cytokines, visually, it looks like inflammation is downregulated. The enrichment analysis would be better in supporting this claim -- the story could go: inflammatory response is a consistently enriched term in cell types X, Y, Z [the Results section regarding Figure 3], so we then focused on communicatory immune networks [Results section regarding Figure 4]. I had formatting issues in Supplementary Table 2, but it looks like the inflammatory response GO Term is only enriched in macrophages. Further discussion should be had to back up this claim.

11. Senescent cells section seems like an afterthought. It is not sufficient to make the claim of increased senescent cell recognition by immune cells via single-cell analysis of immune cells alone, and even if it was, these analyses are not rigorous enough.

12. There is no visualization of canonical SASP receptors expression changes across young vs old.

13. Analysis is not systematic: should start with a comprehensive list of canonical SASP receptors, rather than choosing some from literature.

14. Supplementary Figure S5 is an unorthodox analysis of gene expression changes. Were these genes differentially expressed in old macrophages?

15. Throughout the paper, it is important to show (by either experiments or using publicly available resources) that the changes observed are indeed specific to the ovaries.

16. The authors start the paper by discussing the reduced fertility as a function of age, so any of these results suggest a mechanisms for that? Some discussion of this point will be useful.

17. Because the scRNA-seq data presented by the authors show that the CD4- CD8- double-negative T cell subset co-express Trbc2 (TCRb) and Tcrgc2 (TCRg) genes, it would be important to test if these cells also co-express TCRb and TCRg/d at the protein levels. Pro-inflammatory CD4- CD8- double-negative T cells co-expressing TCRb and TCRg/d have been found in mice (Edwards et al., J Ex Med 2020), and it would be interesting to test whether the ovarian DNT cells show phenotypical or functional similarities with this cell type.

18. To better understand the function of double-negative T cell subset in aging ovaries, one possible way would be to purify these cells and measure which cytokines they produce after TCR activation in vitro and/or co-culture these cells with activated CD4/CD8 T cells in vitro to test if they are capable of suppressing T cell proliferation.

19. For the cluster annotation of scRNA-seq data, it would be interesting to perform additional gene expression analyses to test whether the two clusters of dendritic cells correspond to cDC1 and cDC2 populations.

20. Flow cytometry validation of scRNA-seq data in larger groups of mice presented in this study is chiefly limited by CD3+ T cells and CD11b+ cells. Additional flow cytometry experiments that validate alterations of central ovarian immune cell populations in old competed to adult mice would be helpful. Gating strategies for all flow cytometry experiments should be shown.

21. It would be interesting to compare the scRNA-seq data generated by the authors with published datasets on the immune aging in various mouse tissue (e.g., Almanzar et al., Nature 2019; Kimmel et al., Genome Res 2019; Mogilenko et al., Immunity 2021) to identify common and tissue-specific immune changes in aging ovaries.

22. Predicted changes in cytokine and chemokine expression levels and the crosstalk between immune and senescent cells presented in this study are based on scRNA-seq data but are lacking additional validation. For example, protein-level confirmation for some of these pathways would add important information about the mechanism of immune aging in the ovaries.

23. In Methods: antibody clone 17A2 is used for CD3 and CD4 detection (possible mistake).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Single-cell analysis of the aged ovarian immune system reveals a shift towards adaptive immunity and attenuated cell function" for further consideration by eLife. Your revised article has been evaluated by Ricardo Azziz (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

In this study, the authors present an exciting work that lies at the intersection of immunology, aging, and single-cell RNA-sequencing analysis. It provides a valuable and well-annotated single-cell resource for other researchers in the community to use. It provides solid analyses to probe mechanistic changes in ovarian immune cell functions. More specifically, it leverages single-cell RNA sequencing to probe changes in various immune functions within the ovary in aging. The data provided is the most comprehensive of ovarian immune cells at the resolution of single-cell transcriptomics to date and will be valuable to other researchers. The authors explore four distinct immune functions:

1. Among other cell types, the authors identify macrophages and a unique CD3+ CD8- CD4- T-cell (DNT) subpopulation that changes in abundance with aging. The cell-type compositional analysis results are comprehensive and convincing.

2. The authors also analyze changes in global gene expression across cell types using an enrichment analysis; Figure 3B summarizes potential global and cell-type specific changes in gene expression programs during aging.

3. The authors infer differences in cell-cell communication mediated by various chemokines and cytokines, reasonably demonstrating a decreased inflammatory response.

4. The authors provide evidence that the fraction of macrophages and neutrophils recognizing secretory-associated senescence phenotype (SASP) molecules increases with age.

Both the data and biology presented are quite interesting. The distinction between an aging-associated decreased inflammatory response and cytokine/chemokine communication and an increase in SASP recognition in some cell types, particularly macrophages, demonstrates the complexities of the immune response that are amenable to further exploration. The role of the unique DNT population, which demonstrates substantial compositional changes with aging, in these systemic changes will also be interesting to further dissect.

Overall, while the authors have extensively addressed most of my concerns regarding the compositional analysis, the claims around a decreased inflammatory state with aging (particularly Figure 4B and the response regarding GO terms including both positive and negative regulators), and cell-cell communication analysis. I find the distinction between Figure 5 and Figure 5—figure supplement 1 to be interesting, with SASP recognition seemingly affecting a larger fraction of macrophages but not the average expression between the conditions. I also find it interesting that this same cell type decreases in abundance with age, possibly indicating that a subpopulation of macrophages that are retained with age are those exhibiting SASP recognition as an alternative explanation to the more natural conclusion that macrophages overall increase SASP recognition over time. While I am excited about this work, there are still some outstanding concerns, that I present below.

– Were the log-normalized data scaled prior to dimensionality reduction? PCA typically takes scaled data as input.

– Reading through the methods, it is unclear whether the p-values used in DE testing were multiple tests corrected. Line 364 of the Related Manuscript File "100652_1_related_ms_2716393_rmry4f.pdf" states "all other" statistical analyses applied an FDR correction, implying that this wasn't applied to the DE and other statistical tests discussed in the "Statistical analyses" subsection of the Methods. Furthermore, in the Supplementary Table reporting DE results, there is only the column "pVal" indicating that this is not a multiple test corrected significance value. If multiple test correction was not applied to differential expression output p-values, they must be. Similar concerns for the GO enrichment results and MILO results, which also include many tests. Furthermore, given the LFC threshold filter, I wouldn't expect results to change drastically. However, if there are similar concerns to my original comments regarding how batch correction will affect downstream effect sizes, a demonstration that applying the multiple test correction does not change the results is a necessary minimum. I would suggest demonstrating that the genes identified as significantly differentially expressed with multiple test correction (perhaps with FDR ≤ 0.1) are consistent with those in the current list. This could be done by showing that the gene list sizes are similar and have a high Jaccard index.

Reviewer #3 (Recommendations for the authors):

The authors made substantial improvements to the manuscript by cross-referencing the data and adding validation experiments. However, limitations of this revised manuscript still include not optimal validation strategies: e.g., in flow cytometry validation experiments, the authors defined dendritic cells as CD45+ CD11c+ subset, which might include a variety of CD11c+ macrophages; ILC1s were defined as CD45+ NK1.1+ cells, which might consist of NKT cells. These limitations prevent direct comparison of scRNA-seq data with the results of biological validation experiments.
