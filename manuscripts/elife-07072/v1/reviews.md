# Peer review - Round 1

Editors:
- Christopher Glass, University of California, San Diego , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07072.002](https://doi.org/10.7554/eLife.07072.002)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Registered report: BET bromodomain inhibition as a therapeutic strategy to target c-Myc” for consideration at eLife. Your article has been favorably evaluated by Charles Sawyers (Senior editor), a Reviewing editor, and three reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

This Registered Report submission proposes to replicate key findings in Delmore et al., 2011, which reported the ability of the BRD inhibitor JQ1 to suppress MYC expression in a myeloma cell line and to extend survival of mice transplanted with this cell line. There was general agreement among the three Referees that the proposed studies will assess the major findings of Delmore et al., and will be highly relevant. The referees made the following recommendations to improve the protocols.

Protocol 1:

One reviewer noted that one of the main strengths of the published study (Delmore et al., 2011) was that JQ1 treatment led to downregulation of Myc was not limited to MM1.S cells, and that the effect was observed in several MM cell lines (Figure 3H and 3I). This is a key observation and we recommend that the qPCR analyses be extended to the MM cell types indicated in Figures 2A and 3I.

Addition of one more time point is recommended, the 1h treatment with 500 nM (+)-JQ1. This will indicate whether the Myc downregulation by JQ1 is as dynamic as reported.

In addition to the qPCR primers for Myc and GAPDH mentioned, the exact qPCR primers used by (Delmore et al., 2011) should be included.

One reviewer requested scripts and a detailed description of the calculation performed with R. For example in Protocol 1, in the subsection headed “Test family”, the following sentence can be added: F test statistic (interaction) has been calculated following Cohen (2002) and the partial η2 has been calculated following Lakens (2013).

This reviewer disagrees with the choice of a simple two-way ANOVA. In the original paper (Figure 3B) paired Student's t-tests were used. Since the replicated experiments are similar to the original ones a repeated measures anova is more appropriate. A carefully chosen repeated measures ANOVA is a natural extension of the paired t-test and can simplify the implementation of the proposed meta-analysis. A drawback with a repeated measures ANOVA is that it can be more difficult to set the parameters to determine the power. In such a case a sensitivity analysis can be performed with the G* power software.

Protocol 2:

Weight of mice should be recorded at day-0/day of injection.

In this protocol the analyses following an ANOVA have been performed using Fisher's LSD correction and alpha error = 0.05. In its basic form (I think the one used in the protocol) the LSD correction is not taking into account that multiple comparisons will be performed and therefore a Bonferroni correction (or other corrections) must be employed. For Protocol 2 this brings alpha to 0.025 and in practice is not dramatically changing the power calculations. As an alternative to Fisher's LSD followed by Bonferroni, the Hayter-Fisher's LSD procedure (Hayter, 1986) controls the MFWER (maximum family wise error rate).

Fisher's LSD correction has been reported also for survival data but it doesn't apply to this kind of data. Also here we need a (Bonferroni) correction. For the survival data, power calculations were performed with the Sample Size Calculator, however I do not have a clear link to the software. The authors should provide all the used parameters and references.

References:

Anthony J. Hayter. The maximum familywise error rate of fisher's least significant difference test. Journal of the American Statistical Association, 81(396):1000–1004, 1986. doi:10.1080/01621459.1986.10478364
