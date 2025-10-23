# Peer review - Round 1

Editors:
- Bérénice A Benayoun, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77974.sa0](https://doi.org/10.7554/eLife.77974.sa0)

In this study, Krasniewski and colleagues describe important findings leveraging single-cell transcriptomics to identify subpopulations of macrophages in the skeletal muscle of aging mice. They present solid evidence for the existence of several new resident subpopulations of skeletal muscle macrophages, spanning a range of polarization states using novel markers. Additionally, they identify a shift in relative abundances of these subpopulations with age, leading to a functional shift in inflammatory marker expression and phagocytic capacity. This work will be useful to researchers in the field of immune aging as a resource.


---

# Peer review - Round 1

Editors:
- Bérénice A Benayoun, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77974.sa1](https://doi.org/10.7554/eLife.77974.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Single-cell analysis of skeletal muscle macrophages reveals age- associated functional subpopulations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Carlos Isales as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers and I discussed the manuscript, and we believe that while some major revisions are needed, this manuscript could be appropriate for eLife after major revisions. The most salient are summarized below:

1. The choice of a supervised clustering approach for macrophage heterogeneity analysis was puzzling to reviewers, especially with the choice of using noncanonical markers – the rationale for not using an unsupervised approach was not well explained. In addition, the chosen non-standard nomenclature is confusing, and it is recommended to avoid shorthand to improve the reading experience. In a revised manuscript, the authors should start with an unsupervised approach, as is the gold standard of the field, which can then reveal specific markers that may be used to segregate functional subpopulations.

2. The manuscript needs to provide additional information about both wet and dry methods used to generate results for improved reproducibility: (i) better clarification of potential batch processing, (ii) more information on the functional enrichment analysis, (iii) support for using parametric tests (i.e. tests for normality), (iv) extensive information on package and software versions used for analysis, (v) catalog details for flow antibodies and information on the sorting schemes, (vI) deposition of all R processing scripts, etc.

3. Information about the provenance of the macrophages in the tissue (i.e. associated to blood vessels, inside the parenchyma, etc.) in relation to the diverse phenotypes identified using scRNAseq.

4. Many conclusions need to be toned down as most of the functional information is derived from genomic annotation and not functional assays (i.e. the "wound healing" discussion in the absence of healing assays or of efferocytosis assays) to reflect the degree of evidentiary support. It is also noted that lower numbers of DE genes in scRNAseq datasets is a common caveat of the method that should not be overinterpreted.

5. The reviewers were concerned about the lack of consideration of sex as a biological variable. It was discussed that, in the absence of scRNAseq data in female animals, either some functional experiments should be performed in females to confirm the broader applicability of results, or the male-specific nature of the paper should be explicitly discussed.

In general, all discussed data should be shown and conclusions should not reach beyond that which is directly supported by data unless explicitly stated to be speculation.

Reviewer #1 (Recommendations for the authors):

1. Aging and immunity are both very sex dimorphic. Since the authors profiled exclusively male animals, it will be important to explicitly discuss how these results may differ in female animals in the Discussion section.

2. When describing results from the flow cytometry-based phagocytosis assay (Figure 4), the authors find that LnHl macrophages are phagocytic to a lower proportion than other described subgroups (~49% compared to >85%), although the phagocytic macrophages show strikingly higher levels of phagocytosed cargo by MFI analysis. Although we agree that the significance of this is unclear with the current evidence, this suggests further heterogeneity in the LnHl group. It would thus be important to try to use unbiased SNN clustering of LnHl macrophages (not just of all macrophages as in Figure 6) and identify potential subpopulations that may explain this functional heterogeneity using the generated scRNAseq data (for instance as relating to phagocytosis-gene related mRNAs).

3. Based on experimental flow/description, it sounds like young and old samples may not have been processed in parallel, which may be problematic due to the known impact of batch effects in genomics. Can the authors clarify and explicitly discuss whether batching may be a problem?

4. There needs to be additional provided information about some of the bioinformatic tools and/or analyses.

a. Although the authors generally provide information about software/package versions or dates of access, some are missing (e.g. R, g:profiler). This needs to be updated for reproducibility.

b. Although a GO analysis with g:profiler is described in the text and figures, the method is not described in the method section. Since the nature/use of background lists in functional enrichment analysis is crucial, the authors should clarify the list of genes used as background for enrichment analysis (ideally all detected/expressed genes), as well as the FDR threshold for considering a term significantly enriched. A supplementary table with all enriched terms would also be invaluable.

c. For long-term reproducibility, it would be important to either deposit all R scripts to a public repository such as github or provide it as a supplemental archive to accompany the manuscript.

d. In the methods, the authors mention using Student's t-tests, but not tests to verify that data was normally distributed before use of the t-test. Please include the reference to any normality test used, or, if normality of data cannot be verified, please update to use non-parametric tests.

5. Please provide catalog numbers for the antibodies used in the flow phagocytosis assay, as is needed for reproducibility (methods, page 20).

Reviewer #2 (Recommendations for the authors):

1) Pg5 the authors rely on a limited number of markers to determine the macrophage polarization status (M1 vs M2) of the different subsets of macrophages characterized in the study. Can the authors investigate more exclusive markers (PMID: 26699615) to determine if MHCII and Lyve macrophage subsets are indeed skewed to one state or the other?

2) Lp+ macrophages were described in the study to express a transcriptomic program characterized by M2-like gene program involved in wound repair and healing. Thus, beyond investigating the phagocytic capacity of the macrophage using labeled E. coli, can the authors test the uptake of apoptotic cells using an efferocytosis assay, which seems more relevant for wound repair.

3) Pg7 "We found that MHCII mRNAs (encoding H2-Ab1, H2-Eb1) divided SKM macrophages into two groups, MHCII-high (Hh) and MHCII-low (Hl) in single-cell profiling analysis." Please provide a figure reference.

4) Pg 8, in the immunostaining are different subsets of macrophages localized to different sections of muscle tissues? i.e. more associated with endothelial cells, muscle cells or innervated areas?

5) Can the authors provide more insight into both old and young skeletal muscle to determine if an absolute number of macrophages change during aging (for example via flow cytometry) and also to determine using transcriptomics if the subpopulations of macrophages in the study are resident vs non-resident macrophages.

6) The study lacks analysis of skeletal muscle macrophages in female young and old mice, and would be more informative if they were included in the study to determine any sex differences. Perhaps qPCR or flow cytometry analysis of the four major subsets can be investigated in female mice, since performing single cell would be cost prohibitive.

7) Pg 11. "Cdk1 and Top2a mRNAs were expressed in an even lower number of macrophages (data not shown)." I am confused by data not shown since the data appears to be in table. If not please show.

Reviewer #3 (Recommendations for the authors):

1) Manuscript provides no functional insights of how changes in macrophages affect muscle-physiology/pathology in young and aged mice. Conclusion about functions are based on associations.

2) Please clarify what the percentage of macrophages in muscle in comparison to other CD45+ cells is.

3) Please clarify wheter the analyzed myeloid cells are present in vessels or in muscle parenchyma. How that affects muscle function is also unclear.

4) While the scRNAseq of skeletal muscle macrophages reveals interesting findings about their diversity and how aging affects their transcriptomic profile, the authors chose an unusual approach to analyze the data by defining subsets based on extracellular marker expression (Lyve1 and MHCII) and not transcriptomic profile. By starting with a supervised approach, the authors have missed an important part of their data regarding the high diversity of skeletal muscle macrophages, that cannot only be described through MHC-II and Lyve1 expression. The expression of extracellular markers does not necessarily allow to define functionally distinct subsets. A deeper and more detailed unsupervised analysis is required for scRNA seq data. Moreover, as a starting point, the clusters should be defined based on gene expression and then propose candidate markers to characterize the subpopulations and their functional properties

5) Several conclusions are not supported by the data – e.g.

a) Naming Lyve1+ and Lyve1- macrophages "healing" and pro-inflammatory" is premature as this has not been functionally tested.

b) Unless the authors have data showing the general health of the animals used for the scRNAseq, the low number of differentially expressed genes between young and old shouldn't be interpreted as a result of a "healthier" status of the aging cohort. It is rather a common caveat of scRNAseq that lacks sequencing depth. A bulk RNAseq of specific sorted population that changes in aging may be important.

6) Characterization of macrophages with polarization markers is inadequate and based on old literature. Hence, not very informative.

7) The unsupervised analysis of the scRNAseq lacks depth. Each cluster should be described independently of whether they belong to LpHl, LpHh, LnHh and LnHl. This analysis should come as the first figure. For example, do not dismiss the possibility of non-macrophage clusters as cells were only sorted on CD11b marker. Cluster 6 could be a granulocyte cluster.

8) Overall, the logic behind the direction taken for the analysis of the data is unclear:

– It is not clear why the authors chose to perform a scRNAseq. If the goals of the authors were to study macrophages subsets based on extracellular markers, sorting these subsets, and performing a bulk RNAseq would have been more adequate and would have provided and better sequencing depth.

– The choice of MHC-II and Lyve1 markers to divide macrophage subset seems arbitrary. It is not clear why the authors chose to use markers described for lung macrophages specifically.

– The data showing phagocytic capacities are interesting. Though, it is not clear why the authors chose to investigate this function. Is phagocytosis relevant to the physiological function of skeletal muscle tissues? Are there other functions highlighted in the GO annotations that can be tested? (endocytosis, inflammatory response, antigen presentation)

9) It is difficult to evaluate the solidity of the data. For quantification of populations by flow cytometry analysis and using the scRNAseq data, we suggest adding histograms representing n numbers and statistical significance when comparing the abundance of populations (Figure 3D, S3C, 5A, 6A). Moreover, instead of using tables to depict differentially expressed genes, heatmaps or volcanoplots are recommended (Figure 5C, S3C).

Figure 1C and Figure 2: Ln cells appear to be multiple clusters – with same features? How is that possible?

Figure 1D: The bioinformatic analyses used to characterize Lp/Ln cells lacks statistical validity.

Figure 3D: biological purpose to reveal new insights is lacking.

Figure 3E; Fails to provide spatial clarity of localization in muscle.

Figure 4: phagocytic analyses are superficial and fail to provide new insights.

Figure 6: is the most important figure. However, it is poorly put together in terms of data analyses and presentation. Identity of cluster 5 and 6 which change with age is the main finding – but their relevance is unknown

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Single-cell analysis of skeletal muscle macrophages reveals age-associated functional subpopulations" for further consideration by eLife. Your revised article has been evaluated by Carlos Isales (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Notably, after a new round of review/discussion, the reviewers felt like the issue of batching in the data needed further information/analyses to make sure that the reported results are not the result of batch and biology being confounded in 2 out of the 3 replicates for each age.

Upon discussion, the reviewers thought that this could be addressed with:

1. Doing an analysis paralleling the main manuscript but using only the 2 samples that were processed "unbatched" (i.e. the samples where 1 young and 1 old mouse were processed in parallel), and only these. If the main results of the study are conserved in this unbatched subset of the data, this would strengthen the likelihood that the batching did not grossly impact the conclusions. We would then recommend including this analysis as a supplement.

2. As highlighted by reviewer #3, it is crucial that the batching/experimental collection scheme be discussed explicitly in the manuscript.

3. Finally, please address Reviewer #1's remaining concern on the use of a background gene list for the g:profiler analysis.

Thank you!

Reviewer #1 (Recommendations for the authors):

Although the authors have addressed most of my concerns, some large concerns remain at this point.

1. A very large concern was revealed by their answer to one of my questions about the batchiness of the data. Indeed, the author's response revealed 3 batched: (i) only young samples, (ii) only old samples and (ii) one old and one young. Unfortunately, since batch and biological groups are confounded for groups i and ii, that data is meaningless (i.e. batch cannot be properly accounted for when it is confounded with biology). Since I understand that the authors may not be able to redo the entire experiment the way it should have been done, I believe it is imperative that all analyses also be done exclusively on batch 3 (the one where both groups were represented), to show that all results would hold in the absence of batch. The results should then be included and compared/discussed in the context of the paper as this is a big problem.

2. The authors still did not address the background list used for GO enrichment in g:profiler. This leads me to believe they used the default (all genes instead of detected genes in the dataset), which is incorrect and would lead to spurious enrichments. These analyses should be rerun with the correct background list.

Reviewer #2 (Recommendations for the authors):

We believe the authors have responded to the concerns of the reviewers sufficiently and the paper is significantly improved. Thus, in our opinion, the paper is suitable for publication.

Reviewer #3 (Recommendations for the authors):

The authors have addressed most of my prior concerns. Some issues remain, but in general given the importance of the topic, the manuscript is ready to forward in the process.

An important issue that remains unaddressed is that the scRNA analyses and cell sorting for young/old groups were done on different days. The authors responded to this issue and acknowledged this caveat, but do not describe the consequence of this on the data generation and conclusions.

Authors need to provide this information. This reviewer could not find it in the beginning of the Results section where the description of data generation is provided.
