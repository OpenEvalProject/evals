# Peer review - Round 1

Editors:
- Thorsten Kahnt, https://ror.org/00fq5cm18 National Institute on Drug Abuse Intramural Research Program United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79661.sa0](https://doi.org/10.7554/eLife.79661.sa0)

This study provides novel evidence that a dopamine D2/D3 receptor antagonist enhances model-based control of behavior, whereas blocking opioid receptors has no effect. These conclusions are based on compelling behavioral and computational modeling data. The paper makes an important contribution to our understanding of how dopamine shifts the balance between two subsystems regulating behavior and may improve the understanding of motivational dysfunctions in mental disorders like addiction.


---

# Peer review - Round 1

Editors:
- Thorsten Kahnt, https://ror.org/00fq5cm18 National Institute on Drug Abuse Intramural Research Program United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79661.sa1](https://doi.org/10.7554/eLife.79661.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Effects of dopamine D2 and opioid receptor antagonism on the trade-off between model-based and model-free behaviour in healthy volunteers" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Michael Taffe as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers agree that your paper is solid, timely, and interesting but that a few issues have to be addressed.

Please address the comments in the individual reviews, with a particular emphasis on the following points:

1) Provide a better motivation for studying the effects of these two drugs and specific predictions for their effects.

2) Revise the statistical analysis to include additional random effects.

3) Discuss the issue that baseline and drug sessions are not counter-balanced as limitations.

4) Include drug serum levels in the analysis.

5) Elaborate on the detrimental effects of amisulpride on stay-choices when the first stage stays the same.

Reviewer #1 (Recommendations for the authors):

Please include serum levels for amisulpride and naltrexone should be included as covariates in the analysis.

It's not entirely clear to me how the detrimental effect of amisulpride on high-point repeat choices when the first stage stays the same (which I believe is captured by the inverse temperature) can be reconciled with the idea that blocking D2 receptors reduces flexibility and enhances the stability of prefrontal representations.

If I understand the models correctly, the only difference between the three models is the number of free learning rates. The learning rate in M1 is set to 1, and M2 and M3 allow two or one free learning rate. If this is correct, it would be easier to just describe it like that rather than presenting them as fundamentally different models.

Reviewer #2 (Recommendations for the authors):

1. One motivation for the study is that dopamine agonists yielded inconsistent results, but also the effects of D2 antagonists like amisulpride are not straightforward to interpret. This is because the administered dose of 400 mg can lead to either presynaptic effects (which increases dopaminergic activity) or postsynaptic effects (reducing dopaminergic activity, as assumed by the authors). Participants with a lower effective dose may show stronger presynaptic than postsynaptic effects, and vice versa for individuals with a higher effective dose. To control for the effective dose, the authors might use the measured plasma concentrations. If the current interpretation is correct, the impact of amisulpride on the weighing parameter should increase with higher plasma concentrations, suggesting that the observed mean effect would be driven by postsynaptic rather than presynaptic mechanisms.

2. According to supplementary Table 1, only the main effects of "session", "prev_state_diff", and "prev_points" were modelled as random slopes, whereas as fixed effects also all interaction terms were modelled. As it is generally recommended to maximize the random effects matrix in order to reduce the risk of false positives, I ask the authors to model also the interaction terms between these variables as random slopes. Does this change the observed amisulpride effects?

3. Why did the authors control for BMI (supplementary Table 5)? If the intention was to control for the effective individual dose, body weight would be more relevant than BMI.

4. The inverse temperature parameter in the computational model is described as an indicator of both exploratory behavior and decision noise. Is exploratory behavior the same as decision noise in the current task, or does one parameter indeed measure two dissociable constructs?

Reviewer #3 (Recommendations for the authors):

Here are two small comments about the analyses. First, why didn't the authors include stickiness parameters in the model? This is very popular in our field because it allows us to capture variance in choice induced by preferences that are not related to maximizing reward. Second, the behavioral analysis that tests the effect of a previous reward on choice is not quite ideal, because it doesn't take into account that the same scalar reward (e.g., +1 point) can elicit a negative prediction error (if you expected +5) or a positive prediction error (if you expected -3). This issue can be remedied by computing prediction errors for the second-stage reward and then using their sign as a predictor of staying behavior.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Effects of dopamine D2 and opioid receptor antagonism on the trade-off between model-based and model-free behaviour in healthy volunteers" for further consideration by eLife. Your revised article has been evaluated by Michael Taffe (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

As suggested by reviewer #2, please repeat the analyses using continuous rather than categorical plasma levels (or justify the use of a categorical variable), and also include plasma levels for the model-free behavioral analyses.

Reviewer #1 (Recommendations for the authors):

The authors have done a very nice job addressing my initial comments. I don't have any additional points.

Reviewer #2 (Recommendations for the authors):

The authors made a good job of revising the manuscript and successfully addressed almost all of my previous concerns. However, I still have some questions regarding the inclusion of plasma concentrations in the statistical analyses: First, I wondered why plasma concentrations were dichotomized into low versus high (and was this done based on the mean or the median)? It seems more straightforward to enter plasma concentrations as continuous predictors to the models, as this takes the full variation in plasma concentrations between individuals into account. Second, it seems that plasma concentrations were added only to the model-based computational analyses, but in order to be consistent the authors should do the same with their model-free behavioral analyses.
