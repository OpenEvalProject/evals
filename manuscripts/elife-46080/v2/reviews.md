# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University Feinberg School of Medicine United States

Reviewers:
- Lesley K Fellows, McGill University Canada
- Sebastian Gluth, University of Basel Switzerland

## Review text

DOI: [10.7554/eLife.46080.044](https://doi.org/10.7554/eLife.46080.044)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A role for the hippocampus in value-based decisions: evidence from fMRI and amnesic patients" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Thorsten Kahnt as the Reviewing Editor, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individuals involved in review of your submission have also agreed to reveal their identity: Lesley K Fellows (Reviewer #2); Sebastian Gluth (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes two complementary experiments on the role of hippocampus in value-based decision making. The focus is on information sampling towards a bound which is hypothesized to rely on the hippocampus. The first study shows that fMRI responses in healthy human subjects correlate with response times in value-based but not perceptual tasks. This is interpreted as evidence for a role of hippocampus in retrieving information to guide value-based choice. The second study shows that patients with hippocampal lesions take longer for value-based choices and make more errors. This is interpreted as causal evidence for a role of hippocampus in value-base choice.

The reviewers agreed that the topic is of general interest and that the paper is clearly-written. They also agreed that it is a clear strength that both studies involve a perceptual choice task as a control, and that the key results are specific to value-based choice. Reviewers also identified a few major issues that should be addressed in a revised version. These include questions regarding alternative models or implementations of the drift diffusion model, the method used for multiple comparison correction of the fMRI data, and the unclear location and extent of the lesions in patients.

Essential revisions:

1) The authors fit a drift diffusion model (DDM) to the behavioral data. However, because no other model or parameterization is considered, it is unclear whether this model provides a particularly good account for the data. Arguably, a number of different models might provide a similar or perhaps even better description of the data. (For instance, the value data look like they would also be fit by a somewhat noisy process that is more-or-less flat except the extreme differences, i.e. the lowest and highest value difference choices are relatively fast. The extremes might be heuristics/rule-based (i.e. if X (my favorite) is available, always choose it; it Y is available, never choose it). It would be good if the authors would compare their model to at least one different class of models. In addition, the power-law transformation of the value difference in the drift rate and the collapsing bound parameters add flexibility to the DDM, but these choices were not justified on theoretical grounds or by means of a model comparison. The authors should consider a formal model comparison including simpler versions of the DDM (e.g. with plaw set to 1 and without collapsing bounds). In addition, a parameter recovery analysis of the winning model would be important to support the meaningfulness of the parameters. Alternatively, because it appears that the model is not essential to support the current conclusions, the authors may instead choose to significantly de-emphasize the focus on DDM throughout the paper.

2) Significance testing of the fMRI results was based on whole-brain cluster-wise correction. Examination of the whole-brain maps shows that the hippocampal activity modulated by RT is part of a very large cluster (53545 voxels), which ranges from occipital lobe through the whole brain up to orbitofrontal cortex, thereby including parahippocampal gyrus and hippocampus. Importantly, local peaks appear in separate brain regions, suggesting that the task activated several brain regions that are spatially distinct, but are treated as if they would come from the same cluster. Thus, the fact that the effect in the hippocampus is significant could be driven by signals in other parts of the brain. Given the anatomical hypothesis tested here, the reviewers think it would be more appropriate to perform correction within an anatomical ROI of the hippocampus (voxel-wise or cluster-wise). This way, only voxels within hippocampus can contribute to the significance of the effect. The reviewers also discourage the use of a mask of the striatum in Figure 4 to "mask out" other activations.

3) It would be important to include anatomical brain images from the patient population. These should show the extent and overlap of the lesions, and show whether the damaged regions overlap with the hippocampal region identified in the fMRI study.

4) Finally, it is unclear why the PPI analysis used a median split for RT rather than a parametric modulation. The gPPI package used here allows parametric regressors to be used as the psychological variable to construct PPI regressors. This approach would be preferable, as it would allow a more direct test of the hypothesis that hippocampus-striatum connectivity is correlated with RT.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The hippocampus supports deliberation during value based decisions" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Frank as the Senior Editor, and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

As you can see, reviewer #3 makes additional suggestions, which all reviewers agree should be considered. In particular, this reviewer points out that the parameter recovery analysis (an Essential point in the initial review) was not included in the revised manuscript and also encourages you to include the model comparison in the manuscript (point 1). Moreover, this reviewer makes suggestions for how to approach the model comparison (point 2), which you may want to consider. Finally, and most importantly, the Abstract should be changed to better reflect the findings (point 3).

Reviewer #1:

The authors have adequately addressed all essential points.

Reviewer #2:

The authors have been very thorough and thoughtful in their response to reviews. This version of the paper is well-argued and very interesting. I have no further comments or modifications to suggest. I recommend it for publication. Thanks for giving me the opportunity to serve as a reviewer.

Reviewer #3:

Bakkour and colleagues have done a quite good job addressing most of the reviewers' points, in particular the concerns about the multiple-comparison correction, the lesion information of patients, the analysis of chosen value signals, and the PPI analysis.

However, there are still some issues with the revised manuscript, so that we do not think that it can already be accepted in its current state.

1) In their rebuttal, the authors state that they compared their DDM version to simpler versions without power transformation and without a collapsing bound and found that (at least on the group level) their DDM version wins this comparison. However, none of this is reported in the manuscript, and we are wondering why. We strongly suggest that these comparisons should be reported, in particular, because the more conceptual justifications that are given are not convincing (e.g., the authors say "there is no reason to assume that the relationship [between value and drift] is linear"; speaking with Occam's Razor, we'd say "there is no reason NOT to assume a linear relationship"). Furthermore, the authors do not report a parameter recovery analysis that was asked for in the previous essential revisions.

2) The authors added a comparison of the DDM with a heuristic model. In general, we appreciate this interesting comparison. However, there are two issues that we have with this comparison.

First, for the heuristic model the authors draw RTs from a normal distribution. The authors may consider verifying whether the RTs in their task were indeed normally distributed. This may be the case given the 3 sec time limit, but often RTs are skewed. In that case, the authors may consider more appropriate distributions such as log-normal or ex-Gaussian to make the model comparison fair.

Second, the authors appear to struggle with the quantitative comparison between the two models, because they do not have a good error model for what they call "trivial" decisions. There is a simple (and very common) solution to this problem. Instead of punishing errors in "trivial" decisions by assuming a probability of p =.01, one would treat this probability p as a free parameter (i.e., assuming a so-called "trembling hand" error rate of p in trivial decisions). This "trembling hand" error is very common in research on strategy selection (e.g., Rieskamp and Otto, 2006, JEP General). Allowed values for p might be restricted to some plausible range (e.g., p <.1). This would render calling the comparison an "unsatisfactory exercise" unnecessary. Note, however, that we still think that the (also very interesting) qualitative comparison should remain in the paper, too.

3) Looking at the new ROI analyses reported in Figure 3—figure supplement 3E-H (and the associated Table 3—source data 8), we saw that there is actually hippocampal activity related to RT in the perceptual task. We think that this requires rephrasing the Abstract, in which it is stated that this relationship would be "not observed in a perceptual decision task". Instead, the significantly stronger relationship in value-based compared to perceptual decision making should be emphasized.
