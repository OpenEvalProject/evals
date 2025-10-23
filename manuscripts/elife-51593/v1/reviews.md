# Peer review - Round 1

Editors:
- Roger J Davis, University of Massachusetts Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51593.sa1](https://doi.org/10.7554/eLife.51593.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors examine whether individuals with a history of suicide attempt differ in interoceptive processing, relative to a matched psychiatric reference sample. The study includes a battery of interoceptive tasks (breath-hold, cold-pressor, heartbeat perception, and fMRI). The results indicate that suicide attempters show increased tolerance for aversive respiratory/nociceptive signals, reduced cardiac interoceptive accuracy, and a decreased insula signal during interoception. The findings suggest that blunted awareness of interoceptive sensations and attenuated responses to bodily threat may help to distinguish individuals at risk of suicide. The reviewers and I are enthusiastic about the work.

Decision letter after peer review:

Thank you for submitting your article "Diminished responses to bodily threat and blunted cardiac interoception in suicide attempters" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Alexander Shackman) and a Senior Editor (Christian Büchel). The following individual involved in review of your submission has agreed to reveal their identity: Nils Kroemer (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The two reviewers were enthusiastic about the work:

• I think this is a very strong and important paper. Its key strength is the convergence of multiple methods. This helps address critiques that might be levelled at individual measures. I am impressed by how well the groups are matched in terms of key variables. Some would view differences in psychotropic medication between the groups to be a major flaw, but I think the approach the authors have taken is sensible. Overall, this paper is well guided by theory, methodologically strong, and potentially important clinically.

• This is a very important topic that is notoriously difficult to investigate well so I would like to commend the authors. This is arguably one of the best studies on this topic that I am aware of.

Essential Revisions:

1) Stats.

a) The description of the statistical analysis in the manuscript is currently not sufficient. I was happy to look at the code, but it should not be necessary to know R to understand what exactly the authors did. Therefore, more details on the models should be provided in the Materials and methods or the supporting information.

b) Relatedly, it was not obvious to me why the authors used the lme function for some analyses but not others (although it was even passed to a _gls variable) and sometimes the summary function or the anova function was used, not both.

c) In the manuscript, it was not clear to me which results were reported. Thus, it would be preferable to be a bit more precise in terms of the statistical descriptions and to include the output of the estimated models in the supporting information.

2) Cold pressor challenge.

a) The authors write: "Examination of fixed effects revealed that, while there were no significant group differences in the amount of time elapsed prior to reaching mild, moderate, and peak pain, suicide attempters kept their hands submerged in the cold water for significantly longer (18 seconds on average, SD = 25) than non-attempters after reaching peak pain (t(276)=2.8, p = 0.006, Cohen's d = .34)."

b) First, does the average refer to the group difference in duration and the SD to the pooled SD across groups?

c) Second, if it only refers to this category, why are the degrees of freedom so high that it appears as if a fixed effect across all repeated measurements was taken for the comparison?

d) Third, how was Cohen's d calculated because the study would not be large enough to find significant group differences of this magnitude if the degrees of freedom are calculated correctly (1-β = .36 for d = .34, n1 = 34, n2 = 68). This indicates that a formula was used to estimate d from t, which is only valid for non-nested t-contrasts ("simple" two-sample t-tests).

3) Relations amongst measures.

a) At the moment, DeVille et al. are not fully capitalizing on the strength of the design provided by the complementary measures of interoceptive awareness because the correlations between the interoceptive measures are not reported.

b) The authors report associations between percent signal change in the insula and their behavioral measures of interoceptive awareness, but not between the behavioral measures only.

c) However, the associations between insular signal changes and interoceptive measures are weak and inconsistent. Why would the signal related to the heartbeat detection task show a stronger correlation with the breath-hold duration than with behavioral measures on the same task?

d) The selective report of the significant difference in the manuscript is misleading and should be rephrased. Without a conclusive indication of behavioral loadings on a latent awareness factor, I would be very cautious to interpret such correlations at all. Moreover, the absence of loadings on a shared factor should also be reflected in the Discussion which emphasizes the relevance of interoceptive awareness for the risk of suicide attempts.
