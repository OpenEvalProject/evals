# Author response - Round 1

Authors:
- Yanyan Ding ([ORCID: 0000-0002-3416-2273](https://orcid.org/0000-0002-3416-2273))
- Yuzhe Li
- Ziqian Zhao
- Qiangfeng Cliff Zhang
- Feng Liu ([ORCID: 0000-0003-3228-0943](https://orcid.org/0000-0003-3228-0943))

## Response text

DOI: [10.7554/eLife.72557.sa2](https://doi.org/10.7554/eLife.72557.sa2)

Essential revisions:

1. Figure 3, the electron microscopy studies provide strong evidence for the abnormal organelle morphology including disintegration of mitochondria in Smarca5-deficent RBCs. It would be helpful to provide some quantitative analysis of the size/area and/or number of mitochondria in control and Smarca5-deficent RBCs.

Thanks for this comment. We have performed the quantitative analysis of the area and number of mitochondria in control and smarca5-deficent RBCs. The results showed that the area of mitochondria was not significantly changed and the number of mitochondria was slightly increased but not significantly changed in smarca5-deficent RBCs. These data were added in Figure 3F and G in the revision.

2. Figure 5C, it is somewhat surprising that many of the differentially expressed genes did not show significantly changes in ATAC-seq-based chromatin accessibility. Since the analysis is based on promoter regions, it is possible that many of the differentially expressed genes may be subject to regulation by distal elements such as transcriptional enhancers. It would be helpful to perform additional analysis to include gene-distal ATAC-seq peaks (e.g. +/-100 kb of the TSS) or at least discuss this possibility to explain the lack of overlap between changes in gene expression and ATAC-seq signals.

We greatly appreciate the reviewer’s inspiring comment and the helpful guidance. We agree with the reviewer that it is possible that many of the differentially expressed genes may be subject to regulation by distal elements such as transcriptional enhancers. We therefore followed the reviewer’s guidance, and examined the genes in which the chromatin accessibility at distal regions and their transcription were both increased or decreased after smarca5 deletion (see Figure 5-figure supplement 1E). We found that the overlap between changes in gene expression and ATAC-seq signals increased when taking the distal regions into consideration, indicating that some of the differentially expressed genes may be subject to the regulation by distal ATAC-seq peaks.

We think the possible reasons for the lack of overlap between changes in gene expression and ATAC-seq signals are as follows.

First, gene expression is regulated by a variety of regulatory factors, such as trans-regulatory elements and cis-regulatory elements (Wittkopp, Haerum, and Clark, 2004). In general, complex interactions between cis-regulatory elements and trans-regulatory elements control gene expression (Gibson and Weir, 2005; Hill, Vande Zande, and Wittkopp, 2021; Wittkopp, 2005). However, the peak annotation strategy is based on the distance from peak to the TSS (transcriptional start site) of its nearest gene (Yu, Wang, and He, 2015), which may lead to a situation that the peak is annotated as gene A because it is closest to the gene A but it actually regulates gene B expression. If the peak is differentially accessible and only gene B is differentially expressed, we are not able to find the overlap between changes in gene B expression and the peak (annotated as gene A) signal.

Second, cells exhibit signiﬁcant variations in gene expression and the underlying regulation of chromatin because of intrinsic and extrinsic factors (Ma et al., 2020). A recent study that applies single cell multi-omics sequencing (SHARE-seq) found that during lineage commitment, chromatin accessibility at domains of regulatory chromatin (DORCs) precedes gene expression, indicating that changes in chromatin accessibility may prime cells for lineage commitment (Ma et al., 2020). DORCs were defined as high-density peak-gene-associated regions.

The authors systematically analyzed the cuticle/cortex trajectory and revealed that DORCs generally become accessible prior to onset of their associated genes’ expression. For example, they observed sequential activation of peaks in the Wnt3 DORC, with individual enhancer peaks activating much earlier than the Wnt3 promoter, followed by activation of nascent RNA expression (estimated by intron counts) and, ﬁnally, mature RNA expression (estimated by exon counts). Therefore, the accessibility of peaks and the expression of genes are not exactly matched, which may contribute to explaining the lack of overlap between changes in gene expression and ATAC-seq signals. We have added the related discussion about these possibilities in the revision (Page 20-21, line 365-373, in red).

3. The authors showed that the expression of hmox1a is changed in smarca5 mutants. A variety of genes have been shown to be controlled by Nrf2. More genes should be examined to lend evidence that Nrf2 signaling is indeed perturbed in smarca5 mutants.

Thanks for this thoughtful comment. Besides hmox1a, gclc, ggt1b, gsr, gstp1and gstk1, more target genes of Nrf2, including fbp1a, gsto2, prdx1, pgd and g6pd were further examined in RBCs from smarca5zko1049a and their siblings. The results showed that most of these genes were perturbed in RBCs after smarca5 deletion, indicting the perturbed Nrf2 signaling in smarca5 mutants.
