# Peer review - Round 1

Editors:
- Jian Xu, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51754.sa1](https://doi.org/10.7554/eLife.51754.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this study, Pina and colleagues combined chromatin profiling and single-cell transcriptomics of a conditional KO mouse of Kat2a/Gnc5, a histone acetyltransferase central for promoter activity, to study its role in normal hematopoiesis and leukemia development. They describe that hematopoietic selective Kat2a KO does not significantly affect normal hematopoiesis; however, Kat2a KO impairs MLL-AF9-induced murine acute myeloid leukemia in vitro and in vivo by affecting the maintenance of functional leukemia stem-like cells. The authors show that Kat2a loss impacts transcription factor binding and reduces transcriptional burst frequency in a subset of gene promoters, generating enhanced variability of transcript levels. The authors suggest a new mechanism that destabilizing transcriptional variability modulates self-renewal vs differentiation of leukemia stem-like cells in acute myeloid leukemia. This study places the conceptual framework linking transcriptional variability and chromatin dysregulation to leukemia stem cell function, which will have important implications in different tumors and/or distinct stages of cancer evolution.

Decision letter after peer review:

Thank you for submitting your article "Loss of Kat2a enhances transcriptional noise and depletes acute myeloid leukaemia stem like cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Maureen Murphy as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Pina and colleagues used conditional KO mouse of Kat2a/Gnc5, a histone acetyltransferase for H3K9ac, to study its role in hematopoiesis and MLL-AF9 induced leukemia development. They first find that hematopoietic selective (by Mx1-Cre) pIpC-inducible Kat2a KO does not significantly affect normal hematopoiesis; however, Kat2a KO impairs MLL-AF9-induced murine leukemia in vitro and in vivo by affecting the maintenance of functional leukemia stem cells (LSCs). By chromatin profiling ChIP-seq and scRNA-seq analyses, the authors show that Kat2a loss increases transcriptional burst frequency and impacts TF binding such as Myc and Gabpa. The authors suggest that the above mechanisms underlie the perturbations in self-renewal vs differentiation of LSCs. Kat2a target genes were enriched with protein translation associated genes. Additionally, Kat2a inhibition in human MOLM-13 cells significantly affects polysome formation. The authors conclude that Kat2a controls transcriptional bursting in LSCs, and that destabilization of Kat2a target genes shifts leukemia cell fate from self-renewal to differentiation.

Overall this study provides several interesting findings related to the functional and mechanistic requirement of Kat2a in MLL-AF9 leukemia. This manuscript places the conceptual framework linking transcriptional noise and chromatin mutation to the cancer field. The idea that chromatin disruption, operating via increased transcriptional noise, can destabilize cell states, with the increased heterogeneity contributing to cancer evolution and drug resistance has been a popular one – although with little real data to support it. In this study, the emphasis is more that the chromatin disruption destabilizes the cancer progression "program" by depleting the number of cancer stem cells, which is an interesting twist on the standard concepts. The study concludes by suggesting that the loss of the HAT can strongly drop the translational output of the cell, and in doing so, drive escape from the stem cell compartment.

The mouse genetic experiments were appropriately designed and the results were carefully analyzed. This study provides a nice addition to the existing literature, including several from the authors' group, on the function of Kat2a in regulating transcriptional variability in stem cells (Pina et al., 2012 NCB; Teles et al., 2013; Tzelepis et al., 2016; Moris et al., 2018; etc). The overall findings also support an important role of Kat2a in regulating stem cell self-renewal vs differentiation in different model systems. The authors made other important findings, including the effects of Kat2a KO on transcriptional bursting, TF binding, and polysome formation, that increase our understanding of this important histone acetyltransferase in leukemia development. There are several important questions that need to be addressed, as detailed below, to further strengthen the main conclusions. If the remaining questions can be adequately addressed, all of the reviewers felt that this work will have a strong impact and will be of great interest to the hematopoietic, leukemia, and gene regulation communities.

Essential revisions:

1) In assessing MLL-AF9 leukemia differentiation in vitro, the authors used serial replating of CFC assays (Figure 1). However, the description of phenotypes (e.g. compact, mixed, or dispersed) is somewhat vague and unclear, and it is important to include more quantitative measures such as flow cytometry of surface markers and/or expression of signature genes. Images of representative colonies should be provided.

2) Figure 3: pIpC-induced Kat2a gene deletion might not be 100%. Usually, it is not a big issue for bulk RNA-seq; however, for single cell RNA-seq, this raises the concern of whether or not incomplete deletion contributes to the increased heterogeneity and transcriptional noise. As a quality control, the authors are asked to evaluate the degree of Kat2a gene deletion in various cell clusters.

3) scRNA-seq analysis: Figure 4, it will be helpful to provide information about gene signatures and associated annotations (e.g. by GO and/or GSEA) that separate different cell clusters especially for cluster 7. This is to reveal the role for Kat2a in different cell types. In Figure 4—figure supplement 2C and D: are these effects specific to the computational method used? The authors should try one or two more trajectory plotting methods that involve different assumptions.

4) ChIP-seq analysis: it will be helpful to provide additional justifications on the selection of H3K9ac+ only group as the focus of this study. Based on subsection “ChIP-seq data analysis”, it appears that authors focused on H3K4me3 peaks with H3K9ac alone. The logic seems to be that Kat2a/Gnc5 is mainly responsible for promoter-associated H3K9ac. This decision needs to be better justified. The authors should also justify why peaks with H3K9ac+/H3K27ac+ were excluded. How about H3K9ac+ (regardless H3K27ac+ or H3K27ac-) at enhancers (H3K4me1+)? Figure 5C, the authors should comment why there is a similar burst frequency reduction for Kat2a acetylation targets and non-targets.

5) Analysis of polysome and protein translation: One concern is that the observed polysomal content reduction may be caused by off-target effects of the inhibitor on other HATs or ribosome function. These possibilities should be discussed, and the authors should confirm these results using genetic approaches. More importantly, the MOLM-13 leukemia cell line may not recapitulate LSCs. Since the main conclusion is that Kat2a loss impairs LSC maintenance through impaired transcriptional bursting and translation, the authors should perform the analyses on WT vs Kat2a KO MLL-AF9 leukemia cells. If the cell number is limiting for polysome analysis, the authors may consider measuring protein translation directly by OP-Puro incorporation assay using established protocols (e.g. PMID: 24670665) in LSCs (e.g. L-GMPs) in vivo. If the authors could show the significant effect of protein translation in LSCs in vivo upon Kat2a KO, then these findings and conclusions would be very significant and novel.
