# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37945.019](https://doi.org/10.7554/eLife.37945.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Variance Adaptation in Navigational Decision Making" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Gepner et al. present data showing that larval navigational behavior adapts to the variance of various stimuli. They use optical stimuli to probe visual pathways naturally and olfactory pathways via channelrhodopsin; both pathways show contrast adaptation, but not cross-adaptation between the two pathways. (A very elegant experiment with correlated vs. uncorrelated noise between the two channels showed some mild interactions.) They measure the timescale of the adaptation and show that the different kinetics for adapting to contrast increments vs. decrements are consistent with an optimal detection theory. The authors also used a more natural stimulus paradigm to show that this sort of adaptation is not purely a function of their artificial stimuli.

Throughout, the authors fit their data to a variety of models. They showed that their data were best explained by input rescaling, that their data were consistent with a model in which a Bayes' optimal estimate of variance occurs on timescales of ~1s, and that signals are combined with a potentially multiplicative interaction.

The experiments are well done and the analysis is convincing.

Essential revisions:

Two major concerns arose in consultation:

1) The protocol for contrast adaptation looks different from the classical ones in the field, and reviewer #1, point 1 requests clarification and a new experiment that should be doable in a short time.

2) We would like to see a quantification of how filter shape depends on stimulus variance, and reviewer #2, point 1 provides details of the analyses needed.

Reviewer #1:

1) If I understand it correctly, the change in stimulus variance is related to a change in correlation time of the light intensity, rather than in its variance about a mean, in order to get the derivatives to scale as intended. Does this cause any problems? What if you just do it the naïve way, by scaling the entire light intensity trace contrast, so that the derivatives and deviations both scale up? Is the answer the same? I think this is potentially important because contrast adaptation is crucially dependent on the timescale on which one computes contrast, and by changing the timescale of the stimulus correlations, one might change regimes. (As an extreme case, if fluctuations were made incredibly slow, one would presumably begin to measure adaptation to the mean, rather than to the contrast.)

2) The authors frame the adaptation as rescaling the nonlinearity, but what if adaptation rescales the linear filter amplitude. These are mathematically equivalent, and if you do the rescaling of the linear filter amplitude, then the Figure 8B model seems like it could be reconciled with the independent adaptation of the two channels. Is this a problem for excluding Figure 8B for this reason?

3) The multiplicative model is different from additive in the case of polynomial terms of order >1 in the exponential. However, if you expand everything in Taylor series, is the multiplication just allowing a few more higher order interactions between the terms? The relative coefficients of those higher order terms is restricted by this multiplication step. But what happens if you fit models that just allow up-to-cubic interactions between the xO and xL filtered terms before applying the exponential? (This would be a nonlinear interaction before applying the second nonlinearity.) Can you do better than multiplication? If so, would that imply that there's some kind of nonlinear summation of the terms with potentially small nonlinearities that is in fact the best fit? Or is multiplicative really a better model because it requires fewer fitting terms? A BIC evaluation seems like it could resolve this.

Reviewer #2:

1) A major point of confusion for me was that the authors claim that the linear filters are conserved across different values of stimulus variance. Unless I missed it, there is no quantification of this (except for the claim of 'having established that the kernel shape did not depend on the input variance', subsection “Larvae Adapt Their Turn-Rate to the Variance in Visual and Olfactory Sensory In-puts”), and the figures shown (Figure 1D, Figure 3A) suggest that there actually is a consistent effect of increasing variance on filter shape – namely the relative height of the left shoulder of the filter. While this is not a qualitative change in filter shape, it does change to what extent larvae take into account information about the stimulus further away from the turn. Hence, I would like to see a quantification of how filter shape depends on stimulus variance (e.g., by plotting f_hi vs f_low – if filter shape is preserved across variances, all points should be close to the diagonal – it looks as if filter values close to the peak will lie on the diagonal, but filter values around -6 to -4 seconds prior to the turn should lie off diagonal). Using the actual filter shape for each variance, rather than the filter derived from pooled data, might affect (in both directions) the reported effects of variance on the shape of the nonlinearity.

2) There were also some issues with the writing. For example, the abstract is lacking a description of the niche this work aims to fill, and a statement on the general relevance of the findings – as another example, the authors don't example why it is interesting that multisensory integration involves a multiplicative step and what the implication is for behavior. I also often had to go back to their previous paper (Gepner et al., 2015) and dig into the details of their model or look up details on the coordinate transform (see comment below). The rationale for each plot is not made sufficiently clear to the reader. It would help if the authors show more raw data to provide an intuition for the derived plots – e.g., what happens to animal turning following the switch in variance from low to high or high to low (such as in Figure 3)?
