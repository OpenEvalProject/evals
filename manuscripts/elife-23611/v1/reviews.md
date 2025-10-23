# Peer review - Round 1

Editors:
- Beth Stevens, Boston Children's Hospital, Harvard Medical School , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23611.028](https://doi.org/10.7554/eLife.23611.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A novel Drosophila injury model reveals severed axons are cleared through a Draper/MMP-1 signaling cascade" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal his identity: Oren Schuldiner (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, Purice et al. examine the molecular mechanisms underlying glial clearance of neuronal debris following neuronal injury. The authors show that a transcriptional program mediated by the cell surface receptor Draper and its downstream target, a STAT protein, occurs following a number of neuronal injury paradigms. They use the prevalence of the response to characterize gene expression changes in nerve cords where most neurons are undergoing degeneration, and identify targets. Analysis reveals that one gene, encoding a matrix metalloprotease MMP-1, is upregulated and secreted by glia. MMP-1 is required for morphological changes in glia, and for efficient engulfment of neuronal debris, and represents the first known functional target of the Draper injury signaling pathway.

How glia react to neuron injury is an important and active field of research as it lies at the heart of development, plasticity, and disease of the nervous system. The work in this paper takes an important step forward in identifying a strategy to explore underlying molecular mechanisms, and in identifying a specific molecular effector. The paper is very clearly written, the experiments appear well controlled, and overall the conclusions justified. However, several points and concerns should be addressed as summarized below.

Essential revisions:

1) The data demonstrate that ensheathing glial MMP1 is required for the clearance of severed axons as well as glial membrane expansion in response to nerve injury. While the data show that it is ensheathing glial MMP that has a regulatory role in the injury response, it appears that by 3 days post injury, MMP1 is not localized to ensheathing glia (Figure 8). It is a bit unclear how the authors are envisioning how MMP1 is acting to regulate membrane expansion. Is the idea that MMP1 is secreted by ensheathing glia and that by 3 days post injury, ensheathing glial MMP1 is binding to/acting on a different cell type? The data seem to suggest that this could be a very likely possibility. To explore this further, the authors should provide some high magnification images at 3 days post injury of MMP1 stains with counter stains for other tissue types like astrocytes, neuronal debris, and healthy neurons.

2) The analysis of glial subtypes is a bit simplistic and could be clarified. Please include a magnified image of the anti-Drpr and CD8 driven by the TIFR and Alrm-Gal4s to provide more convincing evidence that indeed Draper is expressed in ensheathing glia. To strengthen the claim that these cells are ensheathing and not astrocytes, then cell specific RNAi followed by draper staining is needed. Otherwise this should be toned down in the text.

3) Figure 10 is important. However, the statements in the paper claim to have identified a Stat/Drpr/MMP1 cascade – for this, I think it is important to at least try to rescue the draper-/- phenotype with overexpression of MMP1 by ensheathing glia.

4) A more rigorous analysis of the RNASeq data is needed as well as more details and clarity on methods and decision on cutoffs and better presentation of data is needed. While no additional experiments are necessary, this is important as the RNASeq data are a key part of the paper and would significantly improve the logic of the connection between the two parts of the study.

*Specific comments and suggestions from one reviewer are included below.

Please include the raw data and explain what is a read and other necessary details of method and analyses. For example: how many genes were considered as "expressed" and how was this determined (is one read sufficient? Ten reads?). How were these reads normalized? At low expression levels the noise is very high – therefore, have the authors performed any thresholding to decide which expression data are reliable enough to actually compare – resulting in the total number of genes actually compared (one way to figure out a reasonable threshold would be to scatter plot – on log axes – two repeats and see from what expression levels they actually look similar); all these analyses should result in one big xls file that is well annotated and can be easily read – together, this would be the "data" which would be used for the comparisons.

Comparison of the expression before and after injury: why was 1.2 fold chosen? this seems a bit low and p-values seem small, raising the possibility that the flow of the analysis needs to be reevaluated. All this results in a volcano plot in which the data is spread out and it is thus unclear how many genes are "grey" – thus not statistically changing their expression? This is also evident in Figure 4—source data 5 – all the genes that are expressed in the data set are unregulated. Seems unlikely that there are no genes that are present but not up or down regulated. The Y-axis for the volcano plot needs to be corrected to -log10 (p-value). The KEGG/GO analysis is not informative at all – what do we learn from this?

Table 1 – the Annokey algorithm is not very informative (and therefore not very heavily used.) I understand that the authors want to find a meaningful way to transition from the RNAseq data to MMP1.; however, this transition could be improved. One suggestion is to focus on one group of genes (which should obviously include MMP1, #13 in the entire list) and then check a few candidates and finally focus on MMP1.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A novel Drosophila injury model reveals severed axons are cleared through a Draper/MMP-1 signaling cascade" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior Editor), a Reviewing Editor, and one reviewer.

The manuscript has been improved but there is one remaining issue that needs to be addressed before acceptance that relates to the analyses of the RNAseq data as outlined below.

We suggest considering using a more conventional 2-fold change cut off for the analyses. However if a 1.2 fold change cut off is used, please provide ample explanation and justification as suggested by reviewer #2 below. Given the heterogeneity of the system, it is possible that key genes involved in glial response to injury may only be modestly upregulated in this transcriptional screen, but still be biologically relevant, as pointed out in your response to reviewer comment 2.

Reviewer #2:

In this revised manuscript the authors have significantly improved many aspects and have addressed most of my concerns. However, one point still bothers me quite substantially. I even consulted with an expert on analyses of RNA seq and he agreed with me that:

1) If the authors feel very strong about the 1.2 FC then they should explain their rationale within the text. I discourage the authors for going here – as one key reason for the low FC of some genes is the heterogeneity of the sample, in which some people might say – so why didn't they sort the glial cells to get a "tighter" expression pattern.

2) Use a 2FC – in reality, almost all of the genes that the authors want to highlight, like those in Figure 4C ARE induced by a factor of more than two – with the exception of Dor and Ced-6. I think it's a reasonable price to pay. You get a much tighter list of about 350 DE genes. MMP is also unregulated by MORE than 2FC. So I really don't see a good reason why not to opt for this solution.

3) A compromise might be the following: Do most of the analysis as suggested in #2 but then explain that many more potentially DE genes might exhibit a less than 2FC because the tissue is heterogeneous and for that reason, the authors are also providing another list of DE genes with a FC of 1.5 or 1.2 or whatever.
