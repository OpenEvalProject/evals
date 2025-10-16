# Peer review - Round 1

Editors:
- Timothy Behrens, Oxford University , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06678.006](https://doi.org/10.7554/eLife.06678.006)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Tuning the speed-accuracy trade-off to maximize reward rate in multisensory decision-making” for consideration at eLife. Your article has been favorably evaluated by Timothy Behrens (Senior editor) and two reviewers, one of whom, Bruno Averbeck, has agreed to share his identity.

The editor and the reviewers discussed their comments before we reached this decision, and agree that the study potentially represents an important advance on your previous work.

For example:

“This manuscript is essentially a continuation of the work that these authors published recently in eLife on multisensory decision making, and as such is an appropriate update/complement to those results.

The current study presents model fits to the original psychophysical data specifically investigating whether the behavior of the subjects was consistent with a strategy to maximize the reward rate. This is indeed an important point because the answer is not entirely obvious given the original observations: in a reaction time (RT) paradigm, when subjects based their perceptual choices on information from two sensory modalities (visual and vestibular) rather than a single one, they generally chose more rapidly rather than more accurately. What the authors found was: (1) that the subjects' behavior across experimental conditions (difficulty x modality) was indeed consistent with reward-rate maximization, and (2) that the observed deviations from optimality were small and can be explained as the consequence of incomplete or imperfect learning.”

However, there are some key points that the reviewers would like addressed before we can reach a final decision.

Most critically, there are: (a) questions about how the model relate to the experimental data:

Reviewer 1:

The demonstration that the reward rate is higher in the multimodal than the single-modality conditions is given in Figure 1B, and the demonstration that the SAT setting affects the reward rate is given in Figure 2, and there are two important issues about how these key results relate to each other.

In Figure 2 the baseline condition or null hypothesis is the set of red bars, which represent an extreme situation in which decisions are made randomly and as fast as possible; accuracy doesn't matter at all (presumably this corresponds to a zero, or very low bound). It is fine to show that, but the question is whether the SAT is tuned, not whether it exists at all. The relevant comparison is the condition in which the bound is not zero but just constant across conditions; i.e., when the SAT setting is simply fixed. The key piece of information is, how large is the discrepancy between the maximum reward rate obtainable with a variable SAT (i.e., adjustable bound) and one obtainable with a constant SAT (non-adjustable bound)?

A second, related issue, is how those model results square with the experimental data. In particular, suppose you take the best-fitting model with fixed bounds (constant SAT) and make a plot of the model results identical to that in Figure 1B. What will it look like? If it matches the real data, then no SAT tuning is necessary across conditions, and conversely, if it does not match the real data then it will provide compelling evidence that the SAT setting does vary across conditions. Then, assuming that the fixed bound is indeed insufficient (which is difficult to infer from the current results), a similar plots can be constructed for the best-fitting model with adjustable bounds. This would directly answer the question of whether the SAT setting is likely to be tuned based on the experimental data, regardless of whether the setting is the optimal one or not. This distinction would be very useful.

Reviewer 2:

1) What would the fraction correct look like in Figure 1A for the bound that optimizes reward rate?

2) The SAT is explicitly linked to the bound height in the Introduction and then referred to as SAT throughout. But this was slightly confusing. If one explicitly unpacks the speed-accuracy trade-off then it's not clear what it means to use one for all conditions. Perhaps at times it would be useful to link it back to the bound, or to just say bound when talking about the SAT across conditions. This is particularly confusing because in the final paragraph, the paragraph starts by talking about adjusting the SAT from trial-to-trial and later suggests that one SAT is used across conditions. If this is discussed in terms of the bound it makes sense, but discussing it in terms of the SAT is hard to follow. Also, during the modeling the bounds are allowed to vary by condition. So why is it suggested that a single bound is used? How much do the bounds vary by condition? How close to optimal do the subjects get if a single bound is used across modalities?

and (b) questions about potential circularities in the analysis:

Reviewer 2:

The gradient analysis seems circular. Or rather it seems like the results of the gradient analysis are consistent with the subjects doing relatively well. If they set parameters far from optimal in dimensions where the gradient has high curvature they would be quite suboptimal. In fact, it should be possible to relate the total deviation of the subject parameters from optimal, normalized by the hessian to the performance of the subject. In other words, take the difference between the optimal bound parameters and the subject's actual bound parameters (call this delta_b) and multiply them by the inverse of the Hessian. Specifically, delta_b * inv(H) * delta_b. Does this predict how well the subjects do?

However, it is also important that you address the following substantive issues:

The SAT is also confusing because it is in diffusion particle space and not in belief space. If the SAT was in belief space, and various assumptions are met (lack of side bias etc.) then accuracy should be on average the same across conditions, and the speed should be the only thing that changes as information increases, correct? This should perhaps be made more clear and developed in a bit more detail.

Isn't there an explicit link between increasing drift rate (i.e. information rate) and whether speed and/or accuracy both increases for a fixed bound?

Is there a significant difference between subject reward rate and random choices for the cost 0.2 condition? These appear to differ by the least amount.
