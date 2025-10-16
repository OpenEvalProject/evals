# Peer review - Round 1

Editors:
- Chi Van Dang, University of Pennsylvania , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.17044.007](https://doi.org/10.7554/eLife.17044.007)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Replication Study: Discovery and Preclinical Validation of Drug Indications using Compendia of Public Gene Expression Data" for further consideration at eLife. Your article has been evaluated by Charles Sawyers as the Senior Editor, a Reviewing Editor, and three reviewers.

There are issues that need to be addressed in a resubmission, as outlined below:

In this manuscript, Kandela and colleagues attempt to replicate prior work by Sirota et al. on the validation of computationally predicted sensitivity to the drug cimetidine in lung but not in renal cancer xenografts. They conclude that the sensitivity to cimetidine of xenografts from A549 lung cancer cells, compared to media control cannot be assessed at a statistically significant level. The authors' results show a trend of response to cimetidine as the original findings but possibly less potent (less significant).

1) It is notable that there are variables such as: circadian biological responses to therapy, mouse strain stocks, and the microbiome of recipient mice that may affect the growth of xenografts. As such, it is suggested that the authors provide a discussion that includes variables that were not specifically addressed or could not be easily controlled.

2) The original study observed a statistically significant reduction in A549 tumor volume while the current study did not, although the direction and magnitude of changes are similar. The number of mice in the study was inferred based on the original study, based on smaller tumor volume measurement errors. The current study conducted pre-planned contrasts on log transformed data within the framework of ANOVA, and the p-values are Bonferroni corrected, while the previous study performed t-tests on un-transformed data without Bonferroni correction. Why is Bonferroni correction used in the new study as opposed to testing directly the single original hypothesis, i.e. that tumor growth of cimetidine treated mice at the highest concentration is reduced compared to PBS/vehicle treatment? We don't see the rationale here for introducing a Bonferroni correction. In addition, it is well known that Bonferroni is an ultra-conservative way to account for multiple hypothesis testing. Without Bonferroni correction, the p-value is significant (p = 0.035) despite the larger error size. Please explain and discuss.

3) Please note that there are more effective models in which the curves can be easily fit by regression analysis (e.g. MANOVA or Regression with RE/AR errors). Such models could be used here. Using the last time point is especially sensitive to measurement errors. It is evident by comparing Figure 1A to the original plot that the measurement errors incurred by the reproducibility study are substantially larger than those in the original study (Figure 4C). This is a problem also because the same errors were substantially reduced when comparing cimetidine activity to PBS/vehicle in ACHN cells (Figure 1B). This raises the concern regarding the accuracy of caliper measurements and tumor volume assessment by Kandela et al. Please explain these issues and provide the data plotted as individual xenografts rather than averages in the supplemental data so that readers can examine the extent of mouse to mouse variations.

4) Please address the following minor issues. There are substantial variability sources in the study that may cause small effect changes. These include:

a) Drift in the A549 cell line: was this authenticated in the repeated study compared to the original one?

b) Different compound potency from different stock solutions: were titration curves performed to assess whether the EC50 of the compounds recapitulated those in the original study? This is especially critical since the growth curves at 50mg/kg and 100mg/kg were dramatically different. Thus even a minimal difference in compound potency could induce profound differences in the measurements.

c) Site of injection: Were the sites identical?
