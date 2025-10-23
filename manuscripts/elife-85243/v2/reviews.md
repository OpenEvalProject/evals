# Peer review - Round 1

Editors:
- Claire M Gillan, https://ror.org/02tyrky19 Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85243.sa0](https://doi.org/10.7554/eLife.85243.sa0)

This important study combines behavior, computational modelling and magnetic resonance spectroscopy in a cross-sectional design to address the question of whether age-related differences in learning are driven by changes in working memory decay or deficiencies in the reinforcement learning (RL) system. The general approach is convincing, the data novel, and the analysis carefully executed. Future work requires a longitudinal design to separate aging from cohort effects and may address the generality of the effects to other RL/Working memory tasks.


---

# Peer review - Round 1

Editors:
- Claire M Gillan, https://ror.org/02tyrky19 Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85243.sa1](https://doi.org/10.7554/eLife.85243.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Age-related decline in prefrontal glutamate predicts failure to efficiently deploy working memory in the service of learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Claire M Gillan as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jonathan Roiser as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

We all enjoyed reading this paper, but all agreed that there were areas where the main claims perhaps went beyond the data. We hope that you find these recommendations helpful in strengthening the clarity of the paper and helping the reader take away what they need to.

1) The causal language (including in the title) should be tempered. Phrases such as 'is associated with' are preferred over 'predicts' given the nature of the data. Similarly, the reference to a 'decline' implies longitudinal data, where it is in fact a cross-sectional design.

2) The reviewers noted that no RL deficits were observed in this paper, so we did not feel it was justified to make broad claims about WM deficits 'explaining them' more generally. This bigger idea would need to be supported with data from a suite of RL tasks and would necessitate the basic observation of an RL deficit in older adults. We do not mean to say that additional data is required for publication, but absent it, the main claims need to be substantially toned down and qualified.

3) A mediation analysis is desirable to strengthen the contention that glutamate changes are responsible for WM deficits in older adults.

4) All reviewers queried the strength of the evidence for a working memory deficit – there was a change in decay but not deployment – can the authors support the interpretation of this as a deficit in efficient deployment of WM?

Reviewer #1 (Recommendations for the authors):

With respect to the computational modeling results, it would be helpful to explain to the reader (and me) a bit more about how the older adults can have faster decay of memory but it does not influence the trade-off with RL (ω parameter). Is that interpreted as – given their poorer memory / faster decay, they weight 'what they have' just as well as others. And if the model did not feature a decay (or fixed it), one would presume a difference in the weight would then be apparent. Is this the correct way to think about that result?

It appears to be a limitation that older adults were from the community while younger adults were from the Brown University participant pool. I understand the RBANs was taken, but absent major cognitive decline this is a coarse instrument (i.e. has ceiling effects in healthy samples). It does not appear there were any controls for level of education or IQ which might reasonably systemically vary across these samples. If this is the case, this may present an additional confound.

The section where the best fitting model is used to generate brain based predictions of performance was a bit hard to follow. It appears though that the effects of WM params are not just from glutamate but the other non-significant neural measures too. Why was this done? It seems the value of the two step analysis process is to identify the key contributor to performance (glutamate) and then focus on it? "WM parameters φ and ω capture the performance predictions based on glutamate (and remaining non-significant neural measures)"

The final section looking at how age factors into the relationship between WM and glutamate is interesting, but I wonder if it would be strengthened with a formal mediation model.

Reviewer #2 (Recommendations for the authors):

Included here are some analytical suggestions for addressing some of the points I raised in the public review.

1. The first point should be easy to address by conducting the same analysis using learning rates as the predicted variable [point 1].

2. To argue for specificity to *prefrontal* glutamate, it would be important to show Figure 3D including the STR measurement. The authors included that information in the text, but it's easy to miss especially because brain measurements were initially averaged [point 1].

3. For 3D, why not run a mixed effects model with Age Group, Glutamate, and Region regressed on WM decay? That seems like a more direct test of the question of whether PFC glutamate predicts WM decay, and whether this relationship interacts with age [point 5].

4. Provided the Age x Glutamate interaction effect above is significant (that is, glutamate predicts WM decay only in the OA group), it would strengthen the conclusion of the study to see a formal mediation analysis within the OA group, asking whether the WM effect on task performance is indeed modulated by glutamate [point 5].

Reviewer #3 (Recommendations for the authors):

1. The paper could benefit from a better description of the rationale for how RL versus WM contributions to learning are disentagled. The statements about the interpretation of set size difference Mentioned in the public review seem surprising in light of their little role in the papers conclusions.

1a. The authors do not statistically test the age-by-condition difference, which would be important to know. Judging from the plots, age differences in learning performance by condition seem biggest in the set size 6 condition, suggesting that in fact gradual RL computations are impaired quite markedly.

2. The rationale for emphasising the difference between learning and test performance was unclear too me. Doesn't the 20 min delay between learning and test suggest that what we see there is related to LTM consolidation, rather than WM capacity? In addition, the set size 3 vs 6 condition difference by age was marginal.

3. The statical approaches could be better explained and motivated. It was unsure why the analysis of model parameters didn't include p values or test statistics. Likewise, the motivation behind the analysis that investigates the factors that relate to the brain/MRS predicted task performance was unclear to me.

4. The task could be described in a bit more detail, in particular the test phase. The fact that this is only binary feedback rather than a

5. Does the fitting of β on the group level disadvantage one of the age groups? Or was this done separately for each group?

6. Which regressors were part of which model in the MRS analysis remained unclear. I was wondering in particular about issues of collinearity, which can impact the ability to interpret the β coefficients (which the paper relies on, rather then the model comparisons)

7. In the section investigating the relation between age, WM decay and glutamate, it be useful to see how strong the relation between glutamate and WM is after age has been factored out.
