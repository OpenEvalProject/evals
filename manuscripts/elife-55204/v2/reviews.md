# Peer review - Round 1

Editors:
- Jonas Obleser, University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55204.sa1](https://doi.org/10.7554/eLife.55204.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Stegmann et al. address an important and interesting question, namely whether social fear conditioning leads to changes in neural processing of fear-conditioned faces versus other faces that are more or less similar to the acquired one. They investigate whether sharpened visuo-cortical tuning, a phenomenon usually reported for low-level visual features such as orientation, also affects the neural processing of social threat cues. The study uses a relatively simple and straightforward fear-conditioning paradigm and an non-invasive measure of brain electric activity (so-called steady-state visual evoked potentials, SSVEPs) to measure visual-cortical processing as well as a series of self-report measures. The results suggest sharpened tuning, correlated with interindividual differences in social anxiety. The reviewers and the Reviewing Editor collectively found considerable merit in the approach and findings and agreed that a case in terms of a lateral inhibition-like situation can be made, also in the light of earlier literature.

Decision letter after peer review:

Thank you for submitting your article "Social aversive generalization learning sharpens the tuning of visuocortical neurons to facial identity cues" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Jonas Obleser, the Reviewing Editor, and Richard Ivry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Christian Keitel (Reviewer #1); Ulrike M. Krämer, PhD (Reviewer #3).

The reviewers and editors have discussed the reviews with one another, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers and the Reviewing Editor collectively found considerable merit in your approach and findings. We agreed that a case in terms of a lateral inhibition-like situation can be made, also in the light of earlier literature. However, there was clear consensus that the manuscript in its current form is not convincing yet and will require (1) refined statistical evidence being put forward, and (2) more detailed grounding in the principles of visual cortical processing and its modulation by (conditioned) fear, that is, a stronger framework behind the authors' assumptions and interpretations.

See below for further guidance to preparing a revised version.

Depending on revision and accompanying rebuttal letter, we will consult all or some of the present reviewers again.

Essential revisions:

– The degree to which the current data do show a sharpening of cortical tuning is contentious, at least. As such, title and Abstract may be misleading. SSVEPs are used, which measure population responses in visual cortex broadly (it is unclear whether the signals here are even stemming from face-specific areas – most likely not, as previous studies have shown that slower frequencies (<12Hz) are more effective in driving higher regions in visual cortex, see Baldauf and Desimone, 2014), and the "tuning" is inferred from a Bayesian model comparison that is rather indirect.

– While the study is trying to understand mechanisms of fear-conditioning, it lacks an account of how lateral inhibition in the processing of fear-conditioned faces would be implemented in the brain. The comparison to orientation tuning is challenging. Do the authors assume a face similarity map in visual cortex where similar faces are represented nearby each other, and so processing of similar faces can be attenuated through lateral inhibition? Would this happen via an attentional mechanisms, or through other connections? None of this seemed specified, and we struggled to understand of how such "tuning" would occur in fearful face representations.

– Related, the authors do not really come up with a suggestion how to link the sharpened tuning of the visuo-cortical responses on the one hand and the generalization of the subjective fear experience on the other hand. It is only stated that fear generalization is an "active and multifaceted process". As this is a central aspect of this study and pertains to the functional relevance of the observed enhanced tuning of the SSVEP response, one would like to see a bit more discussion of this discrepancy.

– For the generalization phase, the GS1-4 faces were treated as a single factor, which did not seem right to the reviewers. These should be separated into 4 different factors, given the authors' assumption that these 4 faces should show different modulations (i.e., lateral inhibition model and also linear decrease model).

– The support for lateral inhibition model only comes from a comparison of a series of different models to a random intercept model. This is weak evidence in favor of a lateral inhibition model. Before doing the modeling, it should first be tested whether the data for the GS1-4 faces differs reliably between each other (see last point), which is doubtful looking at the figure.

Second, a fair modeling approach would be to compare the models against each other (linear vs. lateral inhibition), and not take each model and compare it to the random intercept model, and then pick the model that shows the highest BF. Transitive BFs might be utilized here, accordingly.

– Each of the tested models does not appear to be well justified based on previous literature or any mechanistic accounts of fear conditioning, and it remains a bit unclear why these models were chosen.

– A potentially non-negligible difference (p = 0.07) between CS+ and CS- at baseline was noted, with the same directionality as the significant effect after fear condition. This seems problematic given that the difference remains relatively small after (and during) conditioning (though normalized effect sizes are not reported). We find such a small change extremely difficult to interpret. To be convinced that this is a real change in SNR through conditioning, we would want to see 1) statistics showing a reliable increase of the SSVEP response (so pre- and post training comparisons) which are currency lacking, and 2) effect sizes (at best with CIs for these, J.O.).

– The statistical results are in many places interpreted in a seeming all-or-none fashion, which does not seem appropriate. Effects with p-values of e.g. 0.05 are interpreted as true, while effects with p-values of e.g., 0.056 are interpreted as absent. Again, effect sizes should be reported, and a non-dichotomising interpretation of effects is encouraged.

– Related, the ANOVA results for the generalization show, if we understand correctly, a main effect for the CS-type but no main effect or interaction with social anxiety. The Bayesian linear models does find support for a full interaction model including a main effect and interaction with social anxiety. This discrepancy is not really resolved or discussed so far.

– Reviewers were not unequivocally convinced that the Current source density transforms are useful or adequate for SSVEPs. Please make sure to justify their use better (potentially also demonstrating their effect on overall conclusions/results, e.g. in a supplement). The authors should motivate their choice more strongly and report parameters λ/m.

– The authors have added an additional analysis that relates a measure of visuo-cortical tuning (i.e. the individual sharpening of response profiles after fear conditioning) to a measure of social anxiety. Indeed, they find a moderate positive correlation, strengthening their point that the individual sensitivity to threat cues can affect visuo-cortical tuning. Computing individual cortical tuning as weighted sum of SSVEP and model weights seems elegant. However, the reader is somewhat left at the authors' mercy to confide in the sensitivity of this measure. We strongly suggest to repeat this analysis with the weights of the Quadratic and Linear trend models and compare them with the lateral inhibition situation to show that there is no correlation in these cases.

– The manuscript is generally well-written and easy to read. The Results section however suffers from heavy in-text reporting of statistics. Reading flow will be improved by reporting stats in tables instead. Also consider the use of supplementary tables.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Social aversive generalization learning sharpens the tuning of visuocortical neurons to facial identity cues" for further consideration by eLife. Your revised article has been evaluated by Richard Ivry (Senior Editor) and a Reviewing Editor.

The manuscript has been improved considerably.

Your work addresses an important and interesting question, namely whether social fear conditioning leads to changes in neural processing of fear-conditioned faces versus other faces that are more or less similar to the acquired one.

Reviewers and myself collectively found considerable merit in the approach and findings. We agreed that a case in terms of a lateral inhibition-like situation can be made, also in the light of earlier literature. The authors did a compelling job in carefully addressing most and certainly all major questions from us reviewers and editors.

We do believe there remain two issues that require further attention.

We anticipate that the reviewing and senior editor should be able to act on the revision without consulting the reviewers.

Requested revisions:

1) One reviewer alerted us that one issue raised in the initial round of reviews was not addressed, the potentially quite important pre-post comparison for SSVEP amplitude (i.e., pre-and post-training). In our view, it would be an important analysis to ask if there is an effect over time. We think proper reporting (and discussion) of such a pre-post comparison is important for making inferences that these results point to a change in neural tuning due to habituation.

2) The other remaining issue if of lesser concern:

You have not done a direct comparison of the models to each other. Please consider reporting these comparisons. The reviewer provides the following guidance: "While I follow that there is some benefit in comparing all models against a random intercept model, I would still want to see whether the differences between the GS1-4 faces differs reliably from each other (follow-up paired t-test)."
