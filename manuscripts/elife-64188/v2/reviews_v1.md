# Peer review - Round 1

Editors:
- M Dawn Teare, Newcastle University United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64188.sa1](https://doi.org/10.7554/eLife.64188.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work presents a two-sample Mendelian Randomization (MR) analysis of smoking and alcohol consumption with ACE2 expression in multiple organs. The MR approach allows to explore a causal role of these modifiable lifestyle factors in ACE2 expression in 44 tissues/organs using data from the GCSCAN consortium and GTEx. The MR analysis finds interesting associations with smoking status and intensity and increased levels of ACE2 expression in organs that may go on to modify susceptibility to COVID-19. However, no evidence for an effect of alcohol was seen.

Decision letter after peer review:

Thank you for submitting your article "Mendelian randomization analysis provides causality of smoking on the expression of ACE2, a putative SARS-CoV-2 receptor" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Houfeng Zheng (Reviewer #1); Derrick Bennett (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data. Our expectation is that, where possible, the authors will eventually carry out the additional work and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This paper presents a two-sample Mendelian Randomization analysis of smoking and alcohol consumption with ACE2 expression in multiple organs using tissue samples made available through the GTEx dataset. The MR analysis found promising associations with smoking status and intensity and increased levels of ACE2 expression in organs that may go on to modify susceptibility to COVID-19. While the research is novel, the methods have been applied to only one data resource and some of the conclusions are not warranted by the data and analysis. In particular the causal inferences relating to COVID-19 susceptibility require additional data. Many conclusions are too strong based on the analyses performed.

Essential revisions:

1. The authors must include a detailed flowchart of how SNPs were selected/excluded for each IV. The information must be reported in sufficient detail so that the IVs could be recreated and the whole MR analysis could be replicated. If this requires substantial programming the annotated code could be made available through GitHub for example.

2. The authors report "Our results provide important clinical implications on that smokers might be more vulnerable to SARS-CoV-2 infection or severe disease." They have not directly assessed the relationship of their IV for smoking to SARS-CoV-2 infection so their conclusions need to be toned down. Did the authors consider obtaining SARS-COV-2 outcome data from the COVID-19 Host Genetics Initiative (https://doi.org/10.1038/s41431-020-0636-6)? This would greatly strengthen the report.

3. The MR studies have been conducted in a European population so are these results generalizable to other populations? While the resource used is impressive can this analysis be replicated in an independent data set? Even if some of the signals could be replicated this would add enormous value to the results.

4. Can you offer an explanation why ACE2 was highly expressed on brain, colon, liver et al., but not on respiratory tract and lung tissue? Is higher expression of ACE2 really susceptible factor for Covid19? What is the evidence?

5. The Discussion section seems to focus on evidence from China but the results from China may be affected by the sex-differences in smoking and alcohol prevalence. The patterns of smoking and alcohol in East Asian populations is very different from Western populations. Typically very few women smoke or drink in East Asia. The authors should comment on this.

6. Did the authors consider performing analyses separately for men and women in this study?

7. Table 2 shows the detectable difference with a fixed power of 80% and a significance level of 0.05. Should the significance level be modified to deal with multiple testing with sample from different organs? If not why not? The sample size calculation requires further clarification. It is preferable to mention the a priori power calculations in the methods section of the report not the results. Are the effect sizes detectable clinically relevant? How was this ascertained?

8. The authors need to report the associated F-statistics for their instrumental variables.

9. The authors mention that "Expression values for each gene were inverse quantile normalized to a standard normal distribution across samples". So this suggests that the results are based on a per standard deviation change but this is not clear from the results.

10. Only MR-Egger was used to assess horizontal pleiotropy. There are several other approaches that make different assumptions to MR-Egger that should be considered in order to triangulate the findings.

11. In the MR results, the significance from IVW approach were not replicated in MR-Egger regression, and vice versa. Can we believe these are real casual associations? Could you explain?

12. The abstract should communicate the size of the dataset (ie the number of samples) and report an effect size, 95% confidence interval and p-value for each signal reported in the abstract. Stating 'significant' or 'non-significant' is not appropriate for an abstract.

13. In Figures 1, 2 and 3 the x-axis needs clearer labelling. Isn't this a plot of β values per 1 SD change in ACE2 expression?
