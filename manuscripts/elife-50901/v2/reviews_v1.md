# Peer review - Round 1

Editors:
- Hugo J Bellen, Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50901.sa1](https://doi.org/10.7554/eLife.50901.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "A genetic, genomic, and computational resource for exploring neural circuit function" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The three reviewers are in agreement that this work is a very valuable contribution to the literature and that it should be published in eLife. I am also of the same opinion. However, they all three raised issue that will require some textual changes, better explanations of the modeling. Here is a summary of the most important issues.

Summary

In this manuscript Davis et al. have used different enhancer combinations to mark diverse subtypes of cells, mostly from the visual system, and conduct RNA-seq analysis on isolated nuclei to assign gene expression patterns observed in 67 cell types. The authors first refined the INTACT method, which helps to isolate nuclei specified by a GAL4 expression pattern. In the new method (TAPIN) the authors add tandem affinity purification to the nucleus isolation pipeline. The authors show that this modification increases sensitivity of detection of transcripts and specificity of isolated nuclei compared to the previous methodology. The authors convert the often-graded expression levels to two normal distributions of binary on-off states. They then convert this data to probability of expression scores by using mathematical modeling. The accuracy of this modelling approach is demonstrated in multiple examples. The authors compare the expression patterns that they obtained to the recently available single cell sequencing data sets. Interestingly very few expression patterns directly map to a single cell transcription profile. Nevertheless, this comparison helped to determine the identity of many single cell sequencing clusters obtained in previous studies. Finally, the authors analyze the expression patterns of neurotransmitters and their receptors. By combining high resolution connectome obtained by EM with the expression patterns obtained by TAPIN and INTACT methods the authors find multiple wiring paradigms in the Drosophila brain.

The authors try to find relationships between cell types. They unsurprisingly find grouping of cell types with similar developmental origins and structures. They compare their results to published single-cell sequencing datasets from the optic lobes and the brain and confirmed that the single-cell datasets consisted of clusters that include more than one cell types, which was already known based on the number of clusters itself. They manage to annotate and correct some of the single-cell clusters, showing that bulk transcriptomes can be used to interpret single-cell clusters. They go on to analyze neurotransmitter and neurotransmitter receptor expression in different cell types, before finally trying to interpret connectomic data in the light of their transcriptomes.

Major comments:

– There are issues that need to be discussed more openly. For instance, in many instances the RNA expression pattern of a cell type is referred to a cells expression pattern. This would assume that the expression pattern is homogenous in a given cell type. This is a big assumption. The fact that the TAPIN expression patterns do not directly correlate with the single cell expression profiles can indicate that the cells from a cell type can have divergence in their expression profile. This has implications about the cell types that show multiple neurotransmitters. This issue should be more clearly discussed.

– Another issue is that the authors use the RNA levels and protein levels interchangeably, disregarding the possibility of post transcriptional regulation (This is more pronounced when they use the RNA expression data about cell adhesion molecules in Figure 4—figure supplement 1). This should also be addressed.

– The extent to which single cell sequencing clusters can be compared to TAPIN profiles should be better discussed. The TAPIN profiles are RNA expression of cells that share one or two enhancers (by the use of GAL4 or splitGAL4). Unbiased clustering of single cell sequencing data is based on multiple principle components. The manuscript compares the two approaches and suggest one is better than the other. These are complementary approaches and the data are different and difficult to compare (due to possible RNA expression heterogeneity within cell types). This is reflected in the fact that mid-level hierarchical clustering was not well supported by the TAPIN data (Figure 4A) whereas discrete clustering can be observed in single cell sequencing data. The best experiment to address this would be to do single cell sequencing on TAPIN isolated population of neurons nuclei for one or two cell types. I am not requiring this but they should discuss this better

– Although this is a resource paper, the resource is not accessible to people with limited programming or computational skills. In the web portal opticlobe.com, a simple heatmap can be generated based on the user input. This visualization can hardly reflect the depth and complexity of the data. Please refer to https://gtexportal.org/home/ as a reference to add more tools for general users.

– The description of the mixture model is confusing. The lowercase and uppercase p is mixed for different probabilistic events. Do they denote different functions? Conditioned on "bimodal", the posterior probability equation in subsection “Inferring expression state from transcript abundance” is very confusing. Did you integrate out the p(bimodal)? If not, how is the Bayesian rule applied here? The math equations are not well defined.

– On the model selection section, the first equation used sums of probability, the second equation uses a log sum of probability. Is there a reference or proof for such modeling choices from STAT or machine learning literature?

– The mixture model is well studied in both Bayesian and Frequentist framework, how does this approach compare to the standard Bayesian Gaussian mixture model?

– Figure 3C is the main result of the mixture model and the lower heatmap showed about HALF of the cells in the matrix are read and the other half is blue across all the genes and samples. This is likely due to an artifact of the customized mixture modeling. Since most of the results in the manuscript depend on the probability estimated from the mixture model, it is crucial to show mathematically that the model is correct.
