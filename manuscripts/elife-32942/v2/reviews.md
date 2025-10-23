# Peer review - Round 1

Editors:
- Arup K Chakraborty, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32942.029](https://doi.org/10.7554/eLife.32942.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Single-cell transcriptional dynamics of flavivirus infection" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arup Chakraborty as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Your manuscript utilizes a novel method of single cell RNAseq (viscRNA-seq) to examine the relationship between the host transcriptome and the genome replication of two flaviviruses, DENV and ZIKV. This method generates individual RNAseq libraries from hundreds of infected cells and allows the relative quantification of both host transcripts and viral genomes within individual cells. You use this method to identify host transcripts that correlate with viral genome abundance at different times post-infection. This study identifies a handful of pro- and anti-viral factors, some of which had not been previously reported, and confirms many of these hits through targeted gene knockdowns and overexpression experiments. A comparison of DENV and ZIKV shows that the two viruses differ significantly in their specific patterns of host factor correlation, an intriguing and unexpected finding given how closely related these viruses are.

The main strength of this paper is that it details a novel and compelling approach for leveraging single cell RNAseq to dissect viral infection processes and host interactions in higher resolution than what is possible with bulk methods. As you point out, this method can be adapted to examine host factors that correlate with the replication of other virus families with only slight modifications to the method. Another strength is the comparison of DENV and ZIKV to define host factors that are common or unique to the two viruses.

The primary weakness of the study is that the interpretation of the results does not adequately account for the potential effects of cell death and multi-round replication. As a result, some of the conclusions need to be better tailored to suit the experimental results. Addressing the comments below is likely to ameliorate this weakness.

Essential revisions:

1) In interpreting their results, the authors do not appear to have accounted for cell death and secondary spread of the virus at late time points. Failing to synchronize infections and limit them to a single round means that there will be cells at many stages of the replicative cycle at late time points, making comparisons of viral genome content between individual cells difficult. This point is briefly noted in the discussion but warrants more serious consideration. Further, the death of infected cells at late time points may also skew results since only survivors will make it into the analysis.

2) The causality underlying the correlations is handled a little loosely. Do host transcripts correlate with viral genomes because cells with higher pre-existing expression of those factors are more permissive (and are thus "pro-viral"), or are those genes simply up-regulated in a dose dependent fashion by viral replication? This issue could also factor into the "time-switcher" phenotype.

3) Was the DENV experiment done more than once? The number of individual cells examined contributes an enormous amount of power within a single experiment, but it is important to define the amount of variation across experiments. Ideally, a correlation plot like Figure 3A could be shown for two independent DENV infections to demonstrate that correlations are reproducible for a given virus.

4) Another major comment that needs to be addressed is the lack of uncertainty estimates. The association between the viral RNA and relative gene expression levels is at the heart of the presented work, and it is not clear as to what fraction of the observed associations and trends can be attributed to chance. This impacts many of the presented results. Most notably:

a) Figure 2A. Significance levels should be assessed based on the inter-plate variability (simply applying a Spearman rank correlation test will likely overestimate the significance). As significance levels will depend on the number of observations, an alternative representation of the figure may be needed – for instance, using a signed Z score on x axis (adjusted for multiple hypotheses).

b) Profile graphs in Figure 2G and Figure 4C need error bars. Some graphs may be too dense to show all the error bars, so the representation may need to be changed.

c) Relevant portions of the text where the numbers of associated genes are being assessed need to be suitably changed to reflect quantification.

d) A simpler confidence interval would also be useful for the individual rho estimates (e.g. Figure 2F).
