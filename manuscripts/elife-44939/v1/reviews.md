# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University Feinberg School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.44939.032](https://doi.org/10.7554/eLife.44939.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The dorsomedial prefrontal cortex computes task-invariant relative subjective value for self and other" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study examines common representations of subjective value in vmPFC and dmPFC, for two types of decision-making tasks (intertemporal and risky choices), and for decisions made with either the self or another individual. The emphasis is on regions such as the dmPFC that share a representation of relative subjective value across all combinations of conditions. This is an important goal, and the results support the notion that dmPFC activity encodes relative subjective value, regardless of whether the decision is made for oneself or another, and across decision task types.

Overall, there was a lot of enthusiasm for this paper. However, the reviewers also raised a number of major and minor concerns which need to be addressed. These condensed points are listed below.

Essential revisions:

1) All analyses are based on "relative subjective value" (RSV, |value left option – value right option|), defined as the absolute difference between the two choice options, rather than "relative chosen value", defined as the signed difference between the value of the chosen minus unchosen option (chosen value – unchosen value). Because the RSV signal is closely related to conflict or choice difficulty, there is a concern is that this signal might not identify brain areas involved in valuation per se, but more likely to identify areas involved in conflict or response selection, which are more likely to be shared across choice types even if the underlying valuation mechanism is different. Whereas chosen value – unchosen value is to some degree also correlated with choice difficulty, it is currently a reasonably well-established analysis, and it is the analysis of choice in most of the papers cited by the authors. The reviewers agreed that it would be important to reanalyze the data focusing on chosen value – unchosen value instead of RSV. In addition, the authors could focus on value sum (chosen + unchosen value), which is less related to conflict and difficulty. If those analyses failed to replicate previous studies, this could be still really interesting, and the authors may want to consider carefully why they do or do not replicate other previously reported effects.

2) Empirically determined chance null performance for all decoding analyses in which the classifier is trained and tested on the same trial types is systematically above 50%, indicating that the classifier is biased. This may be related to the fact that cross-validation was performed agnostic to run structure, or because of a potential non-independence in optimizing the lambda parameter. It would be important to reanalyze the data using a leave one run out cross-validation approach. If the median split is applied within each run, potential differences in mean value across runs should not affect classifier performance.

3) Please explore and report the behavioral data more thoroughly. For instance, it would be important to include plots depicting the relationship between value and choices for both self and others, indicating that value is indeed driving choices. Second, response times could be analyzed more comprehensively and displayed in appropriate graphs. For instance, were there differences in overall RT when deciding for self and others?

4) There are a number of issues with the correlation analysis of decoding accuracy and social attitudes that should be addressed. First, please compute these correlations without duplicating data points from the 10 subjects who participated in both sessions (for instance by averaging decoding accuracy in these subjects across both tasks). Second, please report how antisocial attitudes are related to behavioral performance, as one might expect that participants with more antisocial attitudes also show reduced correspondence between their decisions for the other person and the other person's preferences, or are less accurate when learning the other's preferences. Third, the authors use the "normalized" decoding accuracy, subtracting accuracy for self from accuracy for other. It might be interesting to know what is driving the effect, if they did not subtract one from the other.

5) It is possible that choice stochasticity differs between self and other trials. It would therefore be important to also test models that include separate beta parameters for self and other trials.
