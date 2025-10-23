# Author response - Round 1

Authors:
- Kristina M Wright ([ORCID: 0000-0003-1446-3009](https://orcid.org/0000-0003-1446-3009))
- Thomas C Jhou ([ORCID: 0000-0001-8811-0156](https://orcid.org/0000-0001-8811-0156))
- Daniel Pimpinelli
- Michael A McDannald ([ORCID: 0000-0001-8525-1260](https://orcid.org/0000-0001-8525-1260))

## Response text

DOI: [10.7554/eLife.50054.013](https://doi.org/10.7554/eLife.50054.013)

Essential revisions:

The reviewers had a concern regarding the statistical analyses. Specifically, the authors sometimes violate statistical conventions in analyzing the data. If the authors choose to violate conventions, they must justify them.

Results, second paragraph and subsection “Flip and Sustain populations show differential cue firing”: Conduct posthoc tests, instead of t-tests, after a significant main effect of the ANOVAs on trial type. t-Tests do not account for family-wise errors.

We agree, and hope you find the adjustments we have made suitable in addressing this concern. As data were analyzed using SPSS, posthoc options were not available due to the lack of between subject comparisons. In place of all t-tests, we now use bootstrapping to construct 95% confidence intervals for each of the instances mentioned above. Confidence intervals allow us to make between-cue comparisons without assuming a normal distribution and also help circumvent the problem of multiple comparisons.

Figure 4F legend: Bonferroni correction was performed for 14 t-tests. However, for Figure 4A, it should be done in 28 t-tests, which include both regressors. For Figure 4D, t-tests should not be performed separately between the regressors for each 1-s bin, because the ANOVA indicates just a main significant effect on interval without interaction between interval and regressor. Having that said, there appear to be difference between the regressors during the post cue period, suggesting that insufficient power to detect such interaction with the ANOVA. The authors may want to consider performing three ANOVAs: one for baseline, one during the cue, and one after cue.

Thank you for pointing this out, in place of t-tests, we now use bootstrapping and construct 95% confidence intervals to indicate where β coefficients for each regressor differ from zero. We feel this provides a clearer demonstration of the overall pattern, which is supported by the scatter plots in Figure 4. As suggested, we have adjusted our ANOVA approach and performed three ANOVAs for baseline, cue and post-cue periods. Due to this new approach, we are able to detect the post-cue main effect of regressor for Sustain neurons.
