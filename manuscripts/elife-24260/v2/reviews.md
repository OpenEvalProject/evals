# Peer review - Round 1

Editors:
- M Dawn Teare, University of Sheffield United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.24260.019](https://doi.org/10.7554/eLife.24260.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Standardized mean differences cause funnel plot distortion in publication bias assessments" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom, M Dawn Teare (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Marcus Munafo (Reviewer #2); Jack Vevea (Reviewer #3).

The reviewers have recognised this is an important topic but you have not really presented what the impact of this problem is. There are many queries relating to selection of simulation parameters, choice of statistic and test, and what the impact is in realistic practice.

Addressing these issues will likely exceed the time span for major revisions in eLife (two-three months), so we are rejecting the paper now but would welcome a resubmission in the future, with no guarantees of acceptance or re-review. This should be a de novo submission, and we would endeavour to recruit the same editors to assess the revisions.

Reviewer #1:

This manuscript identifies an important potential problem when using the SMD in meta-analyses. When sample sizes are small and effect sizes large, funnel plots using SMD vs. SE can show asymmetry and hence suggest evidence of publication bias when there is none.

The authors demonstrate that this issue should not be so surprising as the SMD SE is a function of the effect size and hence studies with small sample sizes will tend to show a bias. Meta analyses that contain large numbers of studies are therefore more likely to show this effect. This could be an important issue as the meta-analysis may over correct the SMD and actually lead to an underestimate of an effect size.

This manuscript has a clear simple message that using funnel plots of the SMD vs. 1/√n do not result in the same bias.

I do have a number of concerns with the paper especially as they do not tackle the issue of what is the impact on the overall estimate of the effect size resulting from such meta-analyses. My understanding is that the funnel plot, trim and fill is used to estimate corrected effect sizes (so if publication bias is suspected the SMD is adjusted). This manuscript has not really focused on the impact on the overall estimates coming out of meta-analyses.

1) Hedges' g is often reported for studies of small sample size rather than Cohen's d, but the authors appear to have not performed their simulations using this version. (Apart from a single figure shown in the supplementary methods). It seems odd not to have fully evaluated the performance of both summary measures.

2) The simulations have only been performed under quite a limited number of scenarios, the null, for one very large effect size and then for a specific form of publication bias. Though a range of sample sizes has been explored. While this is helpful to show the weakness in the method researchers will want to know when it is important. Is an effect size of 1SD a realistic effect size in practice? Surely if an effect size is so large as that not many studies will be required to confirm it. Table 3 shows scant details of the 5 meta-analyses. It seems intriguing that one of these meta-analyses included almost 1400 studies? I have looked up that reference and while they have looked for evidence of publication bias in all the various studies, it does not seem sensible to have pooled all of the studies for this analysis.

3) Much more detail on the meta analyses and why they were selected. What was the impact on the estimates of SMD using the different funnel plots? What was the distributions of sample sizes and SMDs in the studies making up each meta-analysis?

Reviewer #2:

The authors highlight an interesting aspect of commonly used tests to assess for the presence of small study bias, which may be caused by publication bias. This is supported by analyses of simulated and real data.

My main comment is that there are other tests (e.g. Begg and Mazumdar). Do the issues described here apply to all tests, and if so does the extent to which they do so differ (in which case, which is superior)?

It may also be worth briefly discussing other approaches, such as the Excess Significance Test developed by Ioannidis, that rely on different assumptions and therefore allow triangulation of methods.

Reviewer #3:

This manuscript presents a simulation study looking at the identification of publication bias for measures of effect size based on the difference between means: standardized mean difference (SMD), raw mean difference (RMD), and normalized mean difference (NMD). Using Egger's regression and Duval and Tweedie's trim and fill analysis to detect funnel plot asymmetry, the authors discover a problem of overidentification for SMD when analysis is based on funnel plots of SMD against standard error. Overidentification of publication bias was found to be much greater for SMD in comparison to RMD and NMD. This problem was found to be mitigated by plotting SMD against 1/√n.

The authors provide a good description of the different types of measures of effect size. However, they provide only a mention of Hedges' g in the fourth paragraph of Section 1.1. Many practitioners incorrectly use the term g and d interchangeably, and a description of how these two estimates are different will be beneficial. Related to this, in the following sentence the paper describes the shortcomings of SMD when the sample size is small. It would be useful to point out that Hedges' bias-corrected estimate is meant to address bias when sample sizes are small (Hedges, 1981).

In Section 1.2, the authors describe the relationship between funnel plot asymmetry and publication bias. It would also be worth pointing out that funnel plot asymmetry does not necessarily indicate publication bias. There are other reasons why funnel plots may appear asymmetrical, such as systematic heterogeneity related to the inclusion of two different modes of inquiry that differ both in effect magnitude and in typical standard error.

There are two sections of the paper with the heading "Data Simulations" (Section 2.2 and Section 4.1). Results of the simulations are in Section 2.2. Section 4.1 is at the end of the paper and describes the process for simulating the data. This organization is confusing. It would be better if the description of the simulation were provided before these results, as it provides context for understanding the outcome of the author's simulation. Also, headings that clearly define these different sections will make it easier for readers to navigate the article.

In the third paragraph of Section 2.2 the authors state that results were similar for Cohen's d and Hedges' g effect-size estimates. Based on the information in the paper (Figure 3 legend and Figure 3—figure supplement 2), it appears that the comparisons for these estimates were only made using large sample sizes. In this case, similar results would be expected. They would be more likely to have different results in cases where sample sizes are small, as d and g are more-or-less identical for large sample sizes. The authors should address this scenario as well and make it clear that the information provided uses the Hedges’ g bias-corrected estimate of effect size.

In the fourth paragraph of Section 2.2 the authors use SMD-1/√n to refer to their analysis of funnel plots looking at SMD with 1/√n on the y axis. The hyphen could be interpreted as arithmetic minus sign, so additional clarity of notation is needed.

In the fourth paragraph of Section 2.2 the authors state that the distortion is not seen in plot D of Figure 4. Visual interpretation of funnel plots is subjective. To some readers, the plot will continue to appear asymmetric, but flatter. The authors should explain what details of the plot lead them to the conclusion that the plot was symmetric as well as plots A and C, which are also described as not indicating distortion.

In Table 2, the authors of this study operationalize publication bias by removing all studies with a p-value ≥.10. This operation means that studies with a p-value above the cutoff have no chance of being published, and all studies with a p-value below (e.g. p=.09 and p=.01) have equal certainty of publication. This specification is not a good reflection of how publication bias functions in the real world. The authors should provide justification for using a simple cutoff of a p-value, rather than a model with diminishing probability such as a step function or a decaying continuous function. The authors should also include their reasoning for setting the cutoff at p ≥}.10, as well as information on how many studies were excluded based on this cutoff, such as the average number of studies remaining in the analysis.

In Section 2.3, the authors compare the results of the analyses using examples from real-world studies. Providing this shows how their research may be applicable in real world settings. It would also be useful to report effect-size estimate from the original meta-analysis.

The Discussion section is missing a discussion of the limitations of the current study. The simulation had a limited number of conditions. Providing limitations identifies the scope of the presented findings. Also, the authors should include a rationale explaining why they got these results Without that, the findings atheoretical; entirely empirical methodological findings are harder to accept with confidence.

In the first paragraph of Section 4.1, the authors describe the process for obtaining individual study sample sizes in the simulation. They should provide a rationale for sampling study sample sizes from a uniform distribution. Sample sizes typically do not follow a uniform distribution; rather they tend to be positively skewed. This brings into question the relevance of the simulations.

In Table 4 legend the authors describe the magnitudes for the effect sizes included in the simulation. They should provide a reasoning for using an effect magnitude of SMD=1. By many standards, this would be considered a very large effect. It is possible that the method would perform better (or worse) under conditions where the population magnitude is small or moderate.

Also, the simulation did not include heterogeneity of studies in the model: all studies were sampled from exactly the same fixed-effect distribution. Studies conducted in the real world tend to have heterogeneity. Conditions of heterogeneity often lead to failure of trim and fill and Eggers regression, and would influence the outcome of an analysis of publication bias.
