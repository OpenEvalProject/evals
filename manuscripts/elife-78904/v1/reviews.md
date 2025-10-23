# Peer review - Round 1

Editors:
- Morgan Barense, https://ror.org/03dbr7087 University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78904.sa0](https://doi.org/10.7554/eLife.78904.sa0)

In this paper, Ekman and colleagues present compelling fMRI evidence from a visual sequence task that both the early visual cortex (V1) and the hippocampus represent perceptual sequences in the form of a predictive "successor" representation, where the current state is represented in terms of its future (successor) states in a temporally discounted fashion. In both brain structures, there was evidence for upcoming, but not preceding steps in the sequence, and these results were found only in the temporal but not spatial domain. This study offers the fundamental suggestion that both the hippocampus and V1 represent temporally structured information in a predictive, future-oriented manner.


---

# Peer review - Round 1

Editors:
- Morgan Barense, https://ror.org/03dbr7087 University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78904.sa1](https://doi.org/10.7554/eLife.78904.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Successor-like representation guides the prediction of future events in human visual cortex and hippocampus" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Helen Barron (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers detail their essential revisions below. Our discussion converged on three key points:

1) We ask that the authors keep all model comparisons consistent across regions and tasks.

2) Additional analyses appear necessary to clarify the relationship between the hippocampus and V1.

3) In the revision it will be important to consider the successor representation model proposed here to other predictive sequence models.

Reviewer #1 (Recommendations for the authors):

1) If SR is the best name for the discussed model, it should be clarified why this is the case and, importantly, any difference with the SR as defined in the RL literature should be discussed. Otherwise, another term might be more appropriate.

2) It would be interesting to discuss in the discussion the distinction between the SR model and more complex models that might fit human behaviors and representations just as good or better. For example, with the current design, the SR model can't be disentangled from a more complex model in which all one-step transitions are stored and perhaps in which predictions are iteratively updated based on additional evidence (appearing items). A design in which each state is associated with multiple possible states (with different probabilities) might allow disentangling such additional possibilities.

3) There should be an additional analysis to investigate the relationship between the hippocampus and V1. I understand the limitations of fMRI and of the current experimental design, but there are still possible analyses, even if they are indirect and the results non-definitive (for example, a correlation of the hippocampal and V1 effects across individuals, as in Hindy et al., 2016, Nat Neurosci).

4) The goal of the tuning analysis and the interpretation of its result should be clarified.

5) It should be clarified whether the screen during the ITI is the same as during the omitted items of the partial sequence trials. If this is the case, the potential implications should be discussed.

6) It is unclear from the methods how the tuning analysis was performed exactly. It is a bit circular to define voxels sensitive to a given dot location based on the localizer data and then evaluate on that same data which dot representations were activated on a given trial. Was there some form of cross-validation performed? I could not find it in the code. Even if this was done correctly without double dipping, it seems strange conceptually to use the localizer data for both the fitting and testing purposes here because implicitly, the authors would both assume that the localizer data is independent of the learned associations (to determine the voxels sensitive to a given dot) and dependent on it (to assess temporal tuning). Relatedly, this somewhat applies to the other analyses too: since the localizer was performed after the main task, could it be that the authors did not select the right set, or the complete set, of voxels that are normally sensitive to a given dot location?

7) There seems to be a trend toward the last dot leading to a greater BOLD activity (Figure 3a). I'm wondering if this is because of the task, which is specific to the last dot. I don't think this explains the successor vs predecessor effect though, as you show in Figure 3c. However, this could explain the result of the current only statistical test performed in the "Anticipated stimulus sequences in V1" section. To formally exclude this possibility, the authors should test the difference in the activation of a given dot (B or C) when it is a successor vs when it is a predecessor.

8) The second important prediction of the SR model, in addition to the greater activation for successors than for predecessors, is the decreasing trend in activation for further successors. Although it is visible in the figures, it would be nice if this trend was also statistically tested and reported in the "Anticipated stimulus sequences in V1" section.

9) I don't find the time-resolved hippocampus analysis very convincing: couldn't this transient temporal profile be in response to the start of the trial rather than the missing dot (but see recommendation 5)? It would be best to perform the same analyses suggested above (recommendations 7 and 8) to really test whether the hippocampus exhibits the properties of the SR.

10) Continuing from above, concerning the time-resolved decoding: since trials are very short and ITI are jittered, it seems to me that the activity from previous trials could affect the results. Performing the decoding analysis on regression coefficients from a single-trial GLM analysis would help avoid this confound.

11) Could you show a similar figure as Figure 3c but in Figure 5 for the hippocampus? It would be helpful to see the activation related to each dot location (including the shown dot).

12) Background about predictions and predictive effects in V1 should be added to the introduction, this is currently lacking.

13) There is no mention of corrections for multiple comparisons in the paper. For example, are the tests for the significance of each item in Figure 3b corrected? This should be indicated at all relevant places in the manuscript and figure legends, along with whether the tests are one-tailed or two-tailed.

14) Concerning the model fitting analysis, I'm unsure whether the H0 model can be compared to the other two models using RMSE, since it seems to have fewer parameters. A criterion like BIC or AIC should be used in this case.

Reviewer #2 (Recommendations for the authors):

I had two thoughts, but I leave it to the authors to decide how to address these.

1. While I agree with the authors that this is the first evidence for SR in visual sequences (to the best of my knowledge), there is another set of studies that comes to mind looking at hippocampal contributions to sequence and duration coding of perceptual sequences, which the authors may wish to discuss:

Thavabalasingam, S., O'Neil, E. B., Tay, J., Nestor, A., and Lee, A. C. (2019). Evidence for the incorporation of temporal duration information in human hippocampal long-term memory sequence representations. Proceedings of the National Academy of Sciences, 116(13), 6407-6414.

Thavabalasingam, S., O'Neil, E. B., and Lee, A. C. (2018). Multivoxel pattern similarity suggests the integration of temporal duration in hippocampal event sequence representations. NeuroImage, 178, 136-146.

2. In the model fitting procedure, what exactly does it mean that the discount parameter γ was a free parameter (p. 18)? It would be helpful to provide a bit more clarity on this, but it's also potentially theoretically interesting in light of evidence that different neural structures represent information in line with different values of γ.

Reviewer #3 (Recommendations for the authors):

1. SR versus other predictive sequence models: It remains unclear to me whether the predictive activity observed in V1 is best explained by an SR model or by other models that capture predictive sequences (of which there are many). To assess whether the data is best explained by an SR model, it seems necessary to check whether two adjacent states that predict divergent future states have dissimilar representations, while two states that predict similar future states have similar representations. The data presented here is unfortunately not designed to test this comparison. Can the authors nevertheless distinguish between an SR model (e.g. Figure 4A) and a 'flat prediction' model where each stimulus predicts all possible successor states equally without any temporal discounting (i.e. A predicts B, C, and D with equal probability; B predicts C and D with equal probability but does not predict A; etc..)? It seems important to report this comparison and discuss how it may be difficult to distinguish between an SR model and a 'flat prediction' using the BOLD signal.

2. Related to point 1, it remains unclear to me why the authors consider this data to reflect an SR model, while in their previous data they characterise predictive sequences as reflecting preplay. Can the authors provide a clearer explanation for why this data is best described as an SR model rather than preplay, while Ekman et al., 2017 reflect preplay? Or do the authors consider these codes to be equivalent?

3. It is not clear to me how the ROIs are being used in Figure 3 and 4? If V1 activity reflects an SR, within a given ROI it should be possible to see evidence for backward skew in the representation of each location (consistent with Mehta et al., 2000), while at the population level there is a forward skew?

4. The authors seem to apply different models to data from different brain regions and to data from the task and localiser data. Why? For consistency and clarity would it be possible for the authors to apply the same set of models throughout, to both V1 and hippocampus, and to both task and localiser data? i.e. SR model, 'flat prediction' model, CO model, H0 model, spatial model, temporal model.

5. Related to point 4, in Figure 6 it seems that V1 data from the localiser scan does not support an SR model? This suggests that the task itself is driving the predictive sequence activity in Figures 3-4? This important difference in evidence for an SR-like code during the task and localiser scan should be emphasised and discussed.

6. How specific are these findings to V1 and hippocampus? If the authors use a searchlight analysis to look for multivariate patterns consistent with an SR model, do they not find that many brain regions show evidence for an SR representation?

7. In general, several of the reported analyses are not clearly explained. For example, how do the authors generate the reconstruction maps in Figure 2? Why was pRF mapping only performed in 7 subjects? Why were the data from the pRF maps not used to generate ROIs?

8. Statistics:

a) Can the authors clarify how they corrected for multiple comparisons when performing model comparisons?

b) The authors say they performed a one-sided t-test using data from Figure 5b. Can they clarify what they did here?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Successor-like representation guides the prediction of future events in human visual cortex and hippocampus" for further consideration by eLife. Your revised article has been evaluated by Chris Baker (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there is one remaining issue that needs to be addressed, as outlined by Reviewer #1. Specifically, we thought it would be helpful to provide a bit more detail on the differences between the predictions of an SR versus model-based algorithm:

Reviewer #1 (Recommendations for the authors):

The authors have considerably revised their paper and they have addressed most of my comments satisfactorily. However, I remain uncertain about point 1.1.

I understand that there are no rewards in your task and that the SR algorithm can apply in the absence of rewards. I am not sure however that a model-based (MB) algorithm would make different predictions than SR in the context of your experiment. Indeed, it can be difficult to distinguish SR and MB in many contexts, especially if there is no reevaluation of the transition matrix during the experiment (Momennejad et al., 2017, Nat Hum Behav). Could the authors perhaps test what the predictions of a MB algorithm would be in their experiment (see, e.g., the equation reported in the Methods of the Momennejad paper), or otherwise explain why this would be irrelevant?

Reviewer #2 (Recommendations for the authors):

The authors have done a thorough job of addressing my comments. I don't have any further suggestions.
