# Peer review - Round 1

Editors:
- Xiaobing Shi, Van Andel Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61965.sa1](https://doi.org/10.7554/eLife.61965.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study discovered inflammatory signal induced transcriptional memory, which is dependent on signal induced transcription factor activation and active DNA demethylation. Such transcriptional memory offers more rapid, more strong and more sensitive subsequent signal response. And this is likely a general principle that can be applied to other signaling systems.

Decision letter after peer review:

Thank you for submitting your article "Sustained TNF-α stimulation induces transcriptional memory that provides 100-fold more sensitive subsequent induction" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Xiaobing Shi as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This manuscript explores the impact of DNA methylation on TNF-α-stimulated transcriptional memory. Transcriptional memory is a phenomenon that leads to heritable increase in the transcriptional response of certain genes to a stimulus that has been experienced previously. Transcriptional memory has been studied in many systems and has been shown to require transcription factors, co-activators, histone variants, histone modifications and physical interaction with nuclear pore proteins. The authors find that a GFP reporter under the control of a methylated NFkB-responsive CMV promoter exhibits a distinct form of transcriptional memory; after 10 days following previous exposure to TNF-α, the reporter shows both higher basal expression and greater responsiveness to TNF-α. This effect increases as the length of the previous treatment increases. Furthermore, the DNA methylation of the CMV promoter decreased over 12 days of TNF-α treatment. This loss of methylation and the increase in expression requires TET2 and, to some extent, TET3. From this, the authors propose that recruitment of TET2 (and perhaps TET3) to the CMV promoter during the initial induction demethylates the promoter, removing a heritable repressive mark and enhancing its responsiveness to TNF-α in the future. RNAseq experiments identified a small number of genes that behave like the CMV reporter. They focused on CALCB, a neuropeptide that stimulates vasodilation and has been implicated in migrane. TNF-α activates CALCB through NFkB and the level of expression increased over the course of 8 days of TNF-α treatment. Inactivation of TET2 reduced the accumulation for CALCB between 9h and 12d and these cells did not show memory. The authors find that two p65 binding sites near CALCB become demethylated during TNF-α treatment and remain less methylated for weeks. They propose that this promotes better binding by p65, leading to greater responsiveness. Finally, based on analysis of 10 p65 peaks near five genes that exhibit memory, the authors propose that highly methylated p65 binding sites with greater number of CpGs nearby are most affected by long-term treatment with TNF-α.

Overall, this is a very interesting study reporting a novel mechanism of TNF-α induced inflammatory transcriptional memory mediated by DNA demethylation. The involvement of DNA methylation in heritable changes in transcriptional regulation in response to environmental signals is of broad interest. The data is of high quality and generally supports the conclusions. However, there are a few concerns that need to be experimentally addressed to strengthen the paper.

Revisions for this paper:

1) The alternative mechanism to genomic/chromatin-based memory is that the physiological state of the cells or the activation status of the signaling pathways is different at the times of the first and second inductions. These possibilities need to be thoroughly tested.

2) It is possible that the loss of DNA methylation is due to non-specific effects of transcription on DNA methylation rather than specific demethylation. To distinguish between these possibilities, it is important to determine whether there is a direct protein-protein interaction between p65 and TET2, whether TET2 is recruited to p65 binding sites and if so, whether TET2 recruitment is dependent on p65.

3) The authors observed that TET deficient cells showed loss of transcription memory. Whether this loss of transcriptional memory is purely dependent on DNA methylation or requires p65 is not clear. P65 ChIP-seq or ChIP-qPCR at CALCB loci and / or CMV promoter in WT and TET-TKO cells will help to address this point.

4) Knock down TET2 after previously treating with TNF-α but before retreatment. If this disrupts memory (and leads to increased DNA methylation), it would argue that TET2-mediated demethylation is continuously important for proper inheritance. If it does not disrupt memory, it would argue that TET2-mediated demethylation occurs during the primary TNF-α treatment and that the low DNA methylation state is heritable afterward.

5) The expression of TET proteins and the 5hmC level are quite low in HEK293 cells. It is important to examine the endogenous TET protein and 5hmC levels in HEK293F cells used in this study during TNF-a stimulation. It would greatly strengthen the paper if the authors could validate the findings observed in this study in another system with relatively high TET expression, such as T cells, in which the epigenetic memory is important for cytokine production.

6) Does the memory feature apply to more genes than the few being examined in this study? The data suggesting a change in p65 occupancy or H3K27ac is primarily observed through averaging many sites and is less convincing for the sites that were studied functionally. The occupancy of p65 from the ChIP-seq experiments should be quantified and unbiased, statistical methods should be used to identify genes, in addition to the few being examined in this study, that have changed between the primary and secondary TNF-α treatment. Actually, for all the omics studies (RNA-seq, ChIP-seq, methyl-seq), it would be necessary to perform unbiased global analysis and provide the lists of differentially expressed gene (DEG), methylated sites, or enriched regions as part of QC. It seems that basic data QC information is missing in the supplementary materials. For example, how many reads were collected for each sample, what is the bisulfite conversion efficiency of methyl-seq, and what is the percentage of reads within identified peaks? All are essential for determining the qualify and rigor of these datasets.
