# Peer review - Round 1

Editors:
- Michael R Green, Howard Hughes Medical Institute, University of Massachusetts Medical School , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04024.002](https://doi.org/10.7554/eLife.04024.002)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Registered report: Transcriptional Amplification in Tumor Cells with Elevated c-Myc” for consideration at eLife. Your article has been evaluated by Sean Morrison (Senior editor), a Reviewing editor, and 3 reviewers, one of whom is a biostatistician.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

As detailed below, the reviewers raised a number of major concerns that need to be addressed in a revised Registered report.

Major comments:

1) Any replication of the Lin et al. paper needs to include both RNA profiling and ChIP-seq experiments. The Lin et al. paper has been quite controversial and was based in very large part on ChIP-seq data and its interpretation. Many of the conclusions were based on very subtle changes in data profiles. Subsequently, two papers were published in Nature (Walz et al. and Sabo et al.) that challenge the global claims of Lin et al. In both papers, the authors worked hard to accumulate comprehensive ChIP-seq and RNA expression data in carefully designed experimental systems. While some aspects of the Lin et al. paper may be correct, both Nature papers conclude that there is a set of defined target genes that are far more Myc responsive than others. Hence, reproducing only a subset of the Lin et al. experiments is unlikely to add anything new or resolve controversial claims.

The authors do not propose to reproduce the critical ChIP-seq data and they do not propose any analysis of RNAPII profiles that would support or conflict with the conclusions of the Lin et al. paper, namely that Myc promotes genome-wide transcriptional elongation. The proposal only focuses on RNA profiling without integration with binding of Myc and RNAPII.

2) More comprehensive RNA-seq analysis would determine global RNA expression in response to Myc and not be limited to a subset of genes represented by NanoString.

3) The cell line P493-6 has been established 15 years ago. The proliferation of these cells depends on c-Myc expression and the presence of serum. Serum is a major variable in this system and the majority of genes in stimulated cells are regulated by serum and not by c-Myc (Schlosser et al., Oncogene, 2005). The impact of different serum changes on P493-6 cells is highly significant. In some serum batches the cells barely grow after c-Myc activation. Unfortunately, the impact of various serum batches on P493-6 cells has never been systematically analyzed. Moreover, meanwhile many batches of P493-6 cells are distributed worldwide. These cells have been cultured with different types of serum in different laboratories. Exposure to different sera probably has altered the epigenetic state of P493-6 cells further contributing to variation in gene expression.

From the scientific view, it would be more helpful to study the stability of this biological system, e.g. by culturing P493-6 cells over longer periods of time in different batches of serum followed by a subsequent transcriptome analysis +/- Myc. At minimum, the authors should perform their experiments using multiple batches of serum to assess whether this significantly alters their results.

Statistical comments to the authors:

4) For protocol 1 and 2, authors propose to use ANOVA to analyze the data. Please make sure that the data do not violate the assumptions of the ANOVA: normality and homoscedasiticity. If the data do not fit the assumptions well enough, try to find a data transformation that makes them fit. If this doesn't work, you will need to apply a nonparametric counterpart of ANOVA such as Kruskal-Wallis test. In addition, performing contrast within the framework of ANOVA is more powerful than performing a separate t-test if the assumption of ANOVA is valid.

5) Authors used G*Power to calculate the power. I think that power calculation for protocol 3 & 4 is probably based on the test family t-test implemented in G*Power since there is no Wilcoxon sum rank test implemented in the G*Power. I suggest using t-tests as test family and matched pairs as statistical test to recalculate the power for protocol 3 and 4 (see below for justification). You will need to re-compute the effect size by calculating the SD for paired design, although mean difference between two groups will stay the same regardless.

6) Authors propose to use two-tailed Wilcoxon sum rank test, which has been used in the original paper. I suggest use either two-tailed Wilcoxon signed rank test or two-tailed paired t-test. If you prefer use G* Power to calculate power, then you will be left with two-tailed paired t-test option. The reason why paired analysis is needed is that expressions of the same gene across different conditions are not independent.

7) One major conclusion from the original paper (Lin et al., 2012) is that elevated c-Myc in tumor cells leads to amplification of the expression of actively transcribed genes, but has no effect on silent genes. I am wondering whether the authors will perform the same test to the silent genes, as well as the actively transcribed genes, to confirm the results from the original paper.

8) While it is very useful to leverage the previously reported effects to compute minimum power a priori, what you really need is to guarantee a minimum power on your own data. This can be done, a priori, by including some cross-study variation. This will be helpful for you to plan on the number of replicates and so forth. Papers by Giovanni Parmigiani and collaborators at the Dana–Farber provide some estimates about cross-study variation that could be used for this purpose. Worst case, you should budget some additional variability because of cross-study reproducibility, and increase the sample size as appropriate. We also want you to compute and report power post-hoc/on-the-fly on your own data. Some minimum power should be guaranteed using summaries of your own data.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Registered report: Transcriptional Amplification in Tumor Cells with Elevated c-Myc” for further consideration at eLife. Your revised article has been favorably evaluated by Sean Morrison (Senior editor), a Reviewing editor, and the original reviewers. As you might expect, there was a mixed response from the reviewers regarding the changes. On balance, we would like to move forward but would ask you to make one additional change. Different serum batches have only been included for the c-Myc off situation. To complete this control, please also include different serum batches for the c-Myc on situation.
