# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87301.2.sa0](https://doi.org/10.7554/eLife.87301.2.sa0)

Tilk and colleagues present a computational analysis of tumor transcriptomes to investigate the hypothesis that the large number of somatic mutations in some tumors is detrimental such that these detrimental effects are mitigated by an up-regulation by pathways and mechanisms that prevent protein misfolding. The authors address this question by fitting a model that explains the log expression of a gene as a linear function of the log number of mutations in the tumor and show that specific categories of genes (proteasome, chaperones, ...) tend to be upregulated in tumors with a large number of somatic mutations. Some of the associations presented could arise through confounding, but overall the authors present solid evidence that mutational load is associated with higher expression of genes involved in mitigation of protein misfolding – an important finding with general implications for our understanding of cancer evolution.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87301.2.sa1](https://doi.org/10.7554/eLife.87301.2.sa1)

Tilk and colleagues present a computational investigation of tumor transcriptomes to investigate the hypothesis that the large number of somatic mutations in some tumors is detrimental and that these detrimental effects are mitigated by an up-regulation by pathways and mechanisms that prevent protein misfolding.

The authors address this question by fitting a model that explains the log expression of a gene as a linear function of the log number of mutations in the tumor and additional effects for tumor homogeneity and type. This analysis identified a large number of genes (5000) that are more highly expressed at high mutational load at a FDR of 0.05. These genes are enriched in many core categories, most prominently in the proteasome, translation, and mitochondral translation. The authors then proceed to investigate specific categories of upregulated genes further.

The individual reviews, and the discussion among the reviewers, raised several issues that could potentially undermine or weaken some of the findings presented in this paper.

1. Systematic differences in expression of some genes from one tumor class to another might generate spurious associations with mutational load (ML), which would affect the results presented in Figs 1 and 3. The case of a causal link between ML and over-expression of genes that mitigate deleterious effects of misfolding would be stronger if these results were replicated within single cancer types with many samples with different ML (similar to how Fig S6 relates to Fig 3). A related concern might be an association between increased variance of expression and ML. The compositional nature of expression data could generate trends like the ones shown in Fig. 2 with changing variance.

2. Fig 4, Fig S5 and Fig S8 show results for the regression coefficient of expression on ML after leaving out one cancer at a time. All of us initially read this as results for 'one cancer at a time', rather than 'leave-one-out'. These figures are used to argue that the results are not driven by specific cancer types. However, this analysis would not reveal if the signal was driven by a (small) subset of cancer types. To justify claims like "significant negative relationship between mutational load and cell viability across almost all cancer types", one needs to analyze individual cancer types. Results for specific genes, rather than broad groups would also help interpret these results.

3. You use different model architecture for the TCGA and CCLE analysis because you suspect that the sample size imbalance in the latter might mean that a GLMM can not capture the different variance components accurately. Did you test this? Could you downsample to avoid this? Cancer type is likely a strong confounder of ML.

4. In the splicing analysis (Fig 2 and Fig S4), you report a 10% variation in splicing for a 100-fold variation in ML. This weak trend is replicated in very similar ways for many different types of alternative splicing events. It is not clear why different events (exon skipping, intron retention, etc) should respond in the same way to ML. A weak but homogeneous effect like the one shown here might result from some common confounder (see point 1). Similarly, it is not clear why with increasing intron retention PSI threshold the fraction of under-expressed transcripts would decrease and not increase.
