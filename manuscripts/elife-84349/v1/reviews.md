# Peer review - Round 1

Editors:
- Adrian M Haith, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84349.sa0](https://doi.org/10.7554/eLife.84349.sa0)

This study provides a valuable new perspective on how motor learning occurring in one state generalizes to new states (for example, a different limb posture). The paper proposes a new model in which different potential coordinate systems for generalization are combined based on their relative reliability. The authors provide convincing evidence for this model, showing that it improves significantly on previous theories in its ability to predict patterns of generalization of motor learning in human subjects.


---

# Peer review - Round 1

Editors:
- Adrian M Haith, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84349.sa1](https://doi.org/10.7554/eLife.84349.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Error Prediction Determines the Coordinate System Used for Novel Dynamics Representation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Adrian M Haith as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Tamar Makin as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The reviewers all agree that the paper provides a novel perspective on an outstanding problem in motor adaptation and that the direction-dependent weighting approach presents a promising way forward for advancing our understanding of generalization. The experiments are all well-designed and conducted and the empirical patterns of behavior in the results are very clear and the model predictions are well-aligned with the data in most cases. Overall, the reviewers felt that the paper has significant promise. However, they also identified some substantial concerns.

One major concern is that the model is quite weakly motivated and is also not described in sufficient detail. There were some concerns about the conceptual foundation of the model, including whether the analogy to cue combination is justified. A clearer and more concrete presentation, including derivation of the model from underlying principles, would significantly improve the paper. Many aspects of the model were not presented clearly enough (more equations would be helpful) and some aspects of the model were hardly described at all (e.g. the 'decay' factor), making it difficult to completely evaluate the model.

A second set of concerns relates to the strength of evidence for the model. In most experiments, the model predicts participants' behavior quite well. However, ultimately the current evidence is correlational and there is no specific, critical test of the noise-based weighting model or its underlying assumptions. The conclusion currently rests on a model comparison between the noise-based weighting model and two alternative models. However, the alternative models considered are far from exhaustive. It seems very possible that the data could be equally well described by other models in which the weighting between coordinate frames is direction dependent, but based on a different premise. Indeed, the 'optimal' fitted model performs significantly better than the noise-based model. In general, there were concerns about the extent to which the model could be falsified, and about whether this specific proposal about how direction-dependent weights are obtained could be disambiguated from potential alternatives.

While we consider these to be significant weaknesses of the paper, it does seem that they may potentially be addressable. We would, therefore, be willing to consider a revised version of the manuscript. In this revision, we would expect you to:

1) Provide a clearer rationale for and presentation of the model. This should include a clear statement of any underlying assumptions (e.g. potentially normative principles) and derivation of the weighting rule from these. Mathematical details should also be more concretely provided in the form of equations.

2) Provide stronger evidence that alternative theories could not account for observed patterns of generalization equally well or better. This could be in the form of additional analyses of the existing data, or new data that test a more critical prediction of the noise-based weighting model.

Reviewer #1 (Recommendations for the authors):

The authors claim, on line 320, that: "Importantly, we show that the weight for each coordinate system is inversely proportional to the force error produced when using a specific coordinate system." I don't think this was shown. It was the core assumption behind the model, rather than something which was shown empirically. Actually showing this would require estimating the weights for each coordinate system, which wouldn't actually be possible when there are three coordinate systems. This gives two free parameters and only 1 observation per direction.

The weights for each coordinate frame vary as a function of direction in a complex and non-intuitive way. It would be very helpful to provide some better insight as to how these patterns arise. For instance, as an accompaniment to Figure 1, it would be useful to see how the variance for each coordinate frame varies with direction, and then how this is converted into a weighting.

The presentation of the theory inconsistently describes the noise sometimes as motor execution noise, and sometimes as noise in the estimation of the initial state of the limb. Some parts of the paper suggest that the noise is added to control variables (e.g. line 631, line 340), while the more detailed description in the methods suggests it is added to state (e.g. 632). These two concepts aren't the same, but they are used interchangeably. The paper needs to be clearer about this.

line 324: "Our idea suggests that the motor system is minimizing the variability in extrapolated force production". It's not clear to me how the proposed method achieves minimization of variability.

It's not clear how the 'same level of noise' was achieved across all coordinate systems. What was the exact criterion for setting the noise values? I don't think it's obvious how to equate them across coordinate systems.

line 662 – "we multiplied the force compensation profile of the combined model in [6] with a decay factor that was equal to the amplitude of the experimental force compensation profile". I don't find this clearly enough explained. It needs to be written out mathematically. If there is a decay factor that increases with distance from the learning location, shouldn't this be specific to each coordinate system, rather than applied to the composite force output?

In many cases, the weights and model predictions seem to fluctuate quite substantially across directions – more rapidly than the 22.5 deg separation between probe directions. It seems that it should be possible to generate predictions in a more fine-grained manner than this, and this might be helpful in identifying conditions that would provide a more stringent test of the model, as well as helping to strengthen intuition about how and why these weights vary as they do.

It may be interesting to consider how the model would compare to a model with random weights, perhaps constrained to be periodic.

Reviewer #2 (Recommendations for the authors):

I think the figures would look better if almost all the top and rightmost axis lines were removed.

Reviewer #3 (Recommendations for the authors):

1) To make this paper significant, I recommend the author also write the derivation process for the proposed optimization principle.

2) I recommend the author elaborate the theory more to refute the possibility that the model may not be falsifiable [based on the concerns outlined in the public review].

3) I recommend the author write the details of these models so that we can understand these models better.

4) The detail of alternative models (energy and smoothness) are not written enough for us to understand how fair these comparisons are. Even the definition of absolute bar_F is not clear. Is this average across directions? Similar plots of the weighting factor over the angle, such as Figure *E is necessary for these alternative models.

5) Figure 5E Top. The weight of the joint coordinate is not plotted. Even in this case where the joint does not move, the w_j should be computed with Equation 5. I could not find any description of this omission of w_j. Similarly was not plotted in Figure 6.

6) The mathematical definition of the object-based coordinated system is not clear enough. According to L581-587, this angle is determined by the angle of the hand. However, this definition is different from the object-based coordinate, which can be manipulated by the visual object as defined in Ahmed 2008. Calling this hand angle the object angle is misleading. Also, the hand angle is determined by the wrist. The simple examination of this hypothesis is to change the wrist angle between the training space and the test spaces. Was the angle of the wrist fixed by a splint? If so, what is the purpose of constraining it? I recommend the authors describe this point.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Error Prediction Determines the Coordinate System Used for the Representation of Novel Dynamics" for further consideration by eLife. Your revised article has been evaluated by Tamar Makin (Senior Editor) and a Reviewing Editor.

The model is explained much more clearly in the revised manuscript, and important details that were initially missing are now included. The majority of concerns raised by the reviewers have been addressed. The importance of direction-dependent weighting of coordinate frames is made very clear in the new experiment, and the Re-Dyn model represents a very reasonable and parsimonious version of a model that allows for this. One remaining concern relates to the rationale behind the model, which warrants a minor but important revision:

The revised manuscript now describes the model as related to "inverse optimal control", which I don't think is accurate and in fact it will be confusing to many readers. Inverse optimal control refers to the process of an observer trying to infer the cost function that is being optimized by an agent (as is the case in Berret et al. 2011). Lines 55-58 don't accurately describe the objective of inverse optimal control. The analogy to previous work on inverse optimal control seems more based on the specific approach in the Berret paper (estimating weights in a mixture model) rather than the actual problem being solved (determining mixture weights of a cost function in inverse optimal control, versus determining mixture weights for a policy/solution in this work).

So I don't believe the revision has entirely successfully addressed the need to "provide a clearer rationale for the model". The primary concern expressed previously was that there was no clear justification or derivation of the inverse-variance weightings – it was simply introduced in an ad-hoc manner, rather than being argued to stem a more fundamental principle such as minimizing a cost (note that this is the "derivation" the reviewers were asking for, not an analytical expression for the exact mixing weights). The crux of this issue is seen on line 77: "the motor system can set the relative contribution of each coordinate system by assigning different weights to each coordinate system, for example, using an inverse variance estimation" – and there is no further justification than this. It seems quite straightforward to justify the choice of inverse-variance estimation, but it is not explicitly stated anywhere and should be. For instance, one could simply argue that the motor system estimates/predicts the required forces based on three possible coordinate systems; there is noise in these predictions, and inverse-variance weighting is the optimal way to combine them in the sense of minimizing expected squared error or variance in the force output.
