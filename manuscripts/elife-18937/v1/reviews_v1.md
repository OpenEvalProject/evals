# Peer review - Round 1

Editors:
- Michael J Frank, Brown University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18937.022](https://doi.org/10.7554/eLife.18937.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Autocorrelation structure at rest predicts value correlates of single neurons during reward-guided choice" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Daeyeol Lee (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper builds on the authors' earlier analysis of the single-neuron data previously collected in three different regions of the primate prefrontal cortex (DLPFC, ACC, and OFC), now focusing on the relationship between the intrinsic timescale (time constant) of spiking activity and their role in value-based decision making. In particular, they found that neurons in the ACC and OFC with longer time constants during fixation (as measured by spike rate autocorrelation) are more likely to encode chosen value signals. Moreover, OFC neurons tended to encode the chosen value signals more strongly during the outcome period compared to the neurons in the DLPFC and ACC. The cross temporal correlation analysis also revealed that the chosen value coding in the OFC during the choice and outcome epochs was consistent. The authors suggested that this might be important for the proposed role of the OFC in resolving temporal credit assignment.

Essential revisions:

Overall, the findings reported in this manuscript are very timely. They are nice additions to the previous work from the authors, and provide important new insights into the neural mechanism of decision making. Also, the manuscript is written clearly and easy to follow. Nevertheless, both reviewers identified some important issues that need to be clarified.

1) It is not clear how the persistent coding of chosen value signals can be used for, or reflect, the resolution of the temporal credit assignment problem. For resolving the temporal credit assignment problem, the brain must recognize one of the previous actions or previously visited states that is related to a particular outcome after a delay. How can the chosen value signals, rather than the signals directly related to previous actions or states, can be used for this purpose? The focus on the temporal credit assignment problem also seems a bit inconsistent with the prediction of the authors from the Wang model about the relationship between the timescale and value coding. In other words, their model of mutual inhibition predicts this relationship, even though it is not clear how that model resolves the temporal credit assignment problem.

2) Similarly, the Discussion focuses mostly on the function of the OFC, but the results from this manuscript and Murray et al. showed that the longest time scale is seen in the ACC. Therefore, it might be helpful to include some discussion about the possible function of the long time scale of ACC activity. One possibility is that ACC might play a more important role in integrating signals across multiple trials, as suggested by Seo and Lee (2007) and Bernacchia et al. (2011).

3) Tests of the association between time constant and chosen-value coding mainly use a median split on the time constant tau. However, it doesn't look like tau values fall into discrete high and low clusters (there's no apparent discontinuity at the median in Figure 3A, right-hand side). The rank correlation test mentioned in the third paragraph of the Results seems like a much more natural approach. What's the justification for not using the rank correlation for all the analyses, i.e. the tests of the entire time course, of individual brain regions, and of the outcome phase? As it stands the correlation analysis is confined to a single time point, and the criterion for choosing this time point is vague ("maximal population response"). Does this mean (1) maximum spike rate, (2) maximum population-average CPD, or (3) maximum high-versus-low effect in Figure 3B? #1 seems like the most natural reading, but #2 is what I would guess given the context (#3 would be circular).

4) In a few places the paper infers differences because an effect reaches significance in one condition but not another. A direct contrast between the two conditions is generally more appropriate in such cases. This applies to: (1) greater outcome-related value coding in OFC than in DLPFC/ACC (Results, fourth paragraph); (2) greater reactivation coding in high-tau than low-tau neurons (Results, last paragraph); (3) greater reactivation coding in OFC than in DLPFC/ACC (Figure 5—figure supplement 1–2).

5) For the cross-temporal correlation analysis, the authors draw a distinction between "sustained" and "reactivation" coding. But this distinction sometimes gets blurry. The evidence mainly supports reactivation coding, but the conclusion is that OFC is "maintaining a representation of chosen value until an expected outcome is experienced" (Results, last paragraph), which sounds more like sustained coding. Similarly, earlier (Results, fourth paragraph) the paper concludes that OFC codes value through the choice-outcome interval, but only a post-outcome epoch is actually tested.

6) The paper should at least briefly address the distinction between "chosen value" and what one might call "outcome value" – the size of the juice reward. These aren't identical, since chosen value also incorporates an effort/delay requirement. But they may be correlated. Can the authors rule out that OFC is merely encoding the juice magnitude in the outcome phase? That is, is there direct evidence it also encodes the (already completed) effort or delay requirement?
