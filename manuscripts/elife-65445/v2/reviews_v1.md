# Peer review - Round 1

Editors:
- Naoshige Uchida, Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65445.sa1](https://doi.org/10.7554/eLife.65445.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors performed single cell RNA sequencing in combination with retrograde labeling from the anterior olfactory nucleus and the anterior piriform cortex, to reveal several distinct cell types of projection neurons in the olfactory bulb. The authors further characterized gene regulatory networks and the relationship between gene expressions and their axonal projections. This study provides foundational information and resource regarding the diversity of projection neurons in the olfactory bulb.

Decision letter after peer review:

Thank you for submitting your article "Molecular characterization of projection neuron subtypes in the mouse olfactory bulb" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Catherine Dulac as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Essential revisions:

Summary:

This study by Zeppilli et al. addresses the question whether the projection neurons in the olfactory bulb (OB) are different in their molecular identity. This is one of the major open questions in the olfaction field. The authors enriched the projection neuron population through retrograde tracing from the anterior olfactory nucleus (AON) and piriform cortex (PCX), and performed single nucleus RNA-Seq. They identified 3 mitral cell clusters and 5 tuft cell clusters. They further leveraged regulon analysis (Single-Cell Regulartory Network Inference and Clustering, SCENIC) and found more subtypes based on the transcription factor activities. They developed a simulation method and used bulk RNA-seq data traced from AON and PCX separately to infer that projection neurons of different molecular identity project differently to the targets (however, see Essential revision #1 below).

For the most part our understanding of these projection neurons from a molecular perspective rounds to nearly zero, and their diversity is likely critical for region-specific functions of the higher olfactory brain. The data will be a useful resource to the community, and we commend the authors on releasing the data along with interactive tools for exploring it. In addition, this paper appears to be a useful proof-of-concept for the use of single cell data to deconvolute bulk sequencing data.

Overall, all the reviewers thought that the data are presented clearly and the results are important. However, the reviewers raised several important concerns to which we hope the authors can address with additional experiments and analyses. Most importantly, the reviewers were concerned that the projection specificity predicted with simulated cells (Figure 6) is not validated with real data although projection patterns are one of the major subjects of the study. We hope that the authors can validate the results with additional experiments.

1) The AAVretro labeling strategy is supposed to enrich sequencing of OB projection neurons, which account for only a few percent of OB neurons. However, for unknown reason, only <24% of single nuclei are from projection neurons (mitral and tufted cells). The rest are all kinds including non-neuronal cells. While this does not affect the single-nucleus RNA-Seq analysis, as the authors can identify projection neurons based on known markers and only focus on those 24% cells, they also used the same AAVretro method to perform bulk RNA-Seq, which presumably has the same contamination issues. And in bulk RNA-Seq, RNAs from the other three-quarter cells cannot be distinguished from RNAs from projection neurons. No matter how sophisticated analysis they are doing, I just don't see how the authors could conclude projection patterns from two different retrograde AAV experiments given the above contamination. To make matters worse, the contamination is most likely due to AAV spread, and therefore the AON injection would have more contaminations of OB cells than PCX contaminations so these two bulk RNA-Seq samples contain (unknown) different amount of OB cells. To validate their conclusions of Figure 6, the authors need to either perform classical retrograde labeling together with RNAscope detection of cell-type-specific marker, or better yet to perform AAVretro-based single-nucleus RNA-Seq using separate AAVretro injection (perhaps a smaller volume) into AON and PCX (not sure why they injected two sites in the same animal for their main experiment). Alternatively, the authors could potentially use cell-type specific genetic labeling approaches using novel markers identified in the profiling and mapping target fields. As projection patterns are a framing question for this study, we would like to see at least one experimental verification on this.

2) The computational approach for sorting the contributions of projection neuron populations to the bulk sequencing data is novel and interesting, but not entirely convincing or well-validated. In addition to the issues discussed above, the extent to which simulated nuclei capture the diversity of the original single nucleus RNA-Seq data remains ambiguous since the simulated and actual data seem to form separate clusters in the shared UMAP space. It would be useful to see a simpler complimentary analysis of the bulk RNA-Seq data, perhaps via approaches that evaluate how much of the difference between the AON-projecting and PCX-projecting could be explained by over/under representation of certain clusters in each dataset.

3) In comparing the SCENIC data and analysis shown herein with the Seurat based analysis, there seem to be differences both at the gene level and at the cell type level. Can the authors more extensively characterize similarities and differences in these orthogonal modes of analysis? What explains the observed differences (for example, several of the marker genes shown in Figure 3 are not identified in regulons or TF networks in Figures 4 and 5)?

4) Given that SCENIC is a bioinformatic method, all of the conclusions about regulatory relationships are inferred; the authors should be careful not to assert mechanistic causality from these sorts of analyses (e.g., "continuous activity gradient of TFs is transformed in a non-linear manner into distinct transcriptome differences between mitral and tufted cell types"), which will ultimately require additional experiment. Some tempering of language is likely called for here.

5) A previous single cell RNA-Seq study (Tepe et al., 2018, Cell Report) from OB has identified 3 projection neuron types; those authors' approach resulted in significant labeling of non-projection neurons, about 78% of the data. Since the current method also does not strictly label projection neurons, the authors identified projection neurons from the data using known molecular markers. Therefore, the current method only offered moderate advantage over the previous study. How are the projection neuron cell types correlate with the previously identified 3 types? We note that the quality of the single-cell transcriptomes appears to be superior than the Tepe et al. based on genes detected per cell. Incidentally, it will be useful to plot parameters of snRNA-seq as supplement figure panels rather than bury them in Methods.

6) What is the rationale of using Seurat 0.3 resolution rather than higher or lower? Did the authors try higher or lower resolutions? What would happen to cell-type-specific marker expression? To the regulon analysis? It will be more reassuring, if variations of cluster resolution does not change the major conclusions.

7) It is unclear how the transcription factors identified in the regulon analysis specify these cell types. Their expression patterns do not seem to be cell type specific. Some of them are generic transcription factors and regulate functions in other cells. Examples are Sox10, Sp1, Fos, Jun, Egr1. The authors should examine the hub transcription factors using in situ or at least plot their expressions in their own dataset to make sure they do express in the projection neurons. In addition, the previously identified transcription factors, such as Tbr1, Tbr2 and Tbx21 genes are not in the analysis. The authors should discuss the relationship of the transcription factors identified here and the previously known projection neuron transcription factors.

8) The sub clustering of projection neurons from single nucleus RNA-Seq data is elegant and well-validated with convincing fluorescent in situ hybridization (FISH) data. However, some sort of quantification of overall labeling and overlap between different FISH probes would be useful. Related, it would be broadly beneficial to the field to provide such quantification, particularly for choosing cell-type specific markers in the future.

9) Although compelling, the authors may be somewhat stretching the extent to which the gene regulatory network (GRN) clustering recapitulates the transcriptomic clustering. To strengthen this, it may be useful to include some sort of quality measure for GRN clustering to evaluate if class changes are truly meaningful. This might be achieved by clustering based only on the GRN analysis which is not constrained by the originally identified cell classes. This seems important given that the authors use the rationale that there is heterogeneity of active GRNs within transcriptomically identified clusters to justify the sub clustering, and point out that gradual transitions may exist in active GRNs between clusters. This seems to be a fundamental distinction – whether the GRNs functionally define cell types or whether they are a separate axis along which to evaluate cell identity.

10) The methods and description of the simulated nuclei approach are somewhat under-described. There are multiple manipulations to the bulk sequencing gene expression (expanding the bulk sequencing data into many simulated nuclei by resampling the counts for regulon/target genes, transforming the simulated counts into Pearson residuals before performing PCA and multiple rounds of classification), but the rationale for and the effects of each of these transformations are relatively unclear. Comparisons to existing algorithms that can deconvolve bulk RNA sequencing data (e.g. Frishberg 2019 Nat Methods, Newman 2019 Nat Biotechnology), would also be useful.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Molecular characterization of projection neuron subtypes in the mouse olfactory bulb" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Catherine Dulac as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

All the reviewers commend the authors' thorough and thoughtful revisions. There are, however, some points that we would like you to address before publication of this work. You can find these points in the individual reviewers' comments. We expect that modifications of text will be sufficient to address these points. We hope that you can address these points within two weeks.

Reviewer #1 (Recommendations for the authors):

The authors have addressed many critiques of the reviewers quite thoroughly. Furthermore, they have performed new single-nucleus RNA-sequencing of mitral cells based on their projections into specific sites. The data provide some support of their previous predictions that specific mitral types have preference for specific target sites.

While I applaud the authors' effort to perform additional single nucleus RNAseq of mitral cells based on their projection to either PCx or AON, the numbers of recovered cells are quite small-they did not report any data on AON-projecting ones because the cell number is too small. Of the 57 cells from the sn-PCx data as projection neurons 44 were classified as M2 cells while 6 were classified as M1 cells. Thus, the heading "Targeted snRNA-seq validates predictions of selective connectivity for molecularly defined mitral cell types" is an overstatement: either the prediction is not completely accurate, or the selectivity is not absolute, or both. This heading and similar statements throughout the text need to be toned down.

Reviewer #2 (Recommendations for the authors):

This a thoughtful response to all previous reviewers with extensive new data analyses, figure modifications, and clarifications to the text. This is a vastly improved manuscript, and a timely contribution to the field. I commend the authors on a nice revision and fully endorse publication at eLife.

Reviewer #3 (Recommendations for the authors):

I commend the authors for performing a thorough revision of the paper that addressed our main concerns, especially for the validation data shown in Figure 7 and for the additional details regarding both clustering and the imputation of single nucleus transcriptomes. This paper will serve as an important catalog of molecular diversity in the bulb. I have one experimental request and two minor comments. The experimental request was made in our initial review but was not addressed – unless I missed it (and I may indeed have done so), the authors did not validate the expression of their three key hub genes in MT cells (Taf1, Bclaf1, Pbx3) by either in situ or by showing a UMAP plot describing their expression in the relevant cell types – this is really critical for believing the analysis shown in Figure 5 and should be provided. The two minor comments are 1. maybe consider not using the word "direct" in the abstract to describe OSN inputs onto projection neurons, given the complexity and 2. Line 1276 should define "PCC" – it took me a second to understand what that was on like 1277.
