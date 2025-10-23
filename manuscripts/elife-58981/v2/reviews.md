# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58981.sa1](https://doi.org/10.7554/eLife.58981.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

During embryonic development, morphogen gradients provide positional information to differentiating cells. Experiments have demonstrated that the precision by which these gradients are created and read out is often very high, raising the question of the fundamental limits by which nuclei and cells can obtain positional information.

Fancher and Mugler compare two mechanisms for gradient formation, direct-transport and synthesis-diffusion-clearance, and show that the former is favoured for steep gradients and the latter at shallow gradients, in good qualitative agreement with observations.

Decision letter after peer review:

Thank you for submitting your article "Diffusion vs. direct transport in the precision of morphogen readout" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Marianne Bronner as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The authors present theoretical results concerning two canonical, alternative mechanisms for patterning of cells by morphogen gradients. The issue is that cells know about their positions in the organism, and thus their intended cell fates, from measurements of morphogen concentrations. There will necessarily be uncertainty due noise in this concentration, and evolution has presumably favored mechanisms that reduce this noise (in particular relative to signal – namely the average difference in morphogen levels between adjacent cells). The first mechanism is direct transport (DT) of morphogen from a source cell to target cells via specific channels (e.g. cytonemes). The second mechanism is simple diffusion with degradation, which they call synthesis-diffusion-clearance (SDC). By rigorously formulating noise models for these different schemes, the authors draw several interesting conclusions. First, the transport process associated with DT does not in itself contribute to the noise. This follows from the assumption that morphogen molecules are independent so that the details of transport only yield a the net rate of arrival of molecules at the target cell. More importantly, the authors discover that there is a cross-over as a function of profile length from DT as the preferred mechanism to SDC as the preferred mechanism. The authors do an excellent job of presenting intuitive arguments for this and other results. (In this case, the essential disadvantage of the DT mechanism is that cells can only glean information from the morphogens that they absorb, whereas in the SDC mechanism cells can sense all molecules that pass by them.) The authors follow up this theoretical study with an analysis of multiple developmental morphogen systems. The results are impressively consistent with their theoretical predictions concerning which mechanism has higher signal-to-noise given the profile lengths. Overall, this is an exemplary paper: it identifies an important unrecognized question, rigorously formulates and solves theoretical models to address the question, and carefully applies the results to gain original insights into well-studied developmental systems.

Essential revisions:

1) We find the notation in the paper is unnecessarily complicated. For example, all the overbars in Equation 1 are not needed if the quantities are defined to be the mean. Otherwise, we have symbols with three labels, the bar, the j and +/-. Notation in a biology journal must be very carefully chosen for maximum simplicity and clarity. Likewise, the δ functions in these equations could more clearly be shifted to statements about boundary conditions, which would be more intuitive. Remember, very few biologists understand δ functions!

2) The argument presented in the third paragraph of the subsection “Direct Transport Model” is a key one, but we find that it could be explained more clearly. Perhaps by reference to a more detailed diagram?

3) The lack of parallel construction between the presentations of the two models is odd. The DT model is presented as a set of deterministic ODEs for mean concentrations, while the diffusive model (itself an averaged equation) has noise terms added. We would have expected the statement about the noise effect in the DT model to be deduced from some underlying master equation of which the presented model is simply the first moment(s), but that higher order moments are necessary to calculate to draw conclusions about the model.

4) Stepping back from the calculations we are struck by the following question. If, as stated: "We see that regardless of the form of p(τ), the probability of a morphogen molecule entering the target cell in any given small time window δt is simply βδt. This result holds regardless of the mechanism by which morphogen molecules go

from the source cell to the target cell, as the only effect such a mechanism can have is on p(τ)", then why can't we substitute a diffusive mechanism and deduce the same thing?

5) The authors assume that once a morphogen molecule has reached the end of the cytoneme, it is immediately absorbed by the target cell. How realistic is this assumption and how important is it? Would relaxing it change the results qualitatively?

6) In comparing the precision of the two models, it would be good to discuss in a bit more detail how the comparison is made: which parameters are kept the same, which are optimized over, which are varied systematically, and why is this choice the most natural one? For example, the authors chose to study the precision ratio as a function of the gradient length, while optimizing over the DT shape φ. Βut we could also imagine a comparison in which the production and degradation rates are kept the same for both models (because production and degradation are energetically costly), but that over all other parameters the precision is optimized. Would that give a qualitatively different result? Why would the gradient range λ be of special importance (the comparison is made on the footing of equal gradient range)? Should not only the precision matter (such that it would be fine that the gradients in the DT and SDC model are different)? In other words, how do the maximal precisions that can be reached given reasonable constraints (such as production and degradation rates) compare, as a function of the distance to the source?

7) And in making this comparison, does the SDC model exhibit an optimal diffusion constant that maximizes the precision? Understanding this is probably important, because when, in the current comparison, the SDC model is more precise, it is because of the higher protein clearance rate due to diffusion. Yet, a higher diffusion constant also lowers the steepness of the gradient, decreasing the precision,

8) The key mechanism by which the SDC model can become superior is indeed diffusion. Could adding diffusion to the DT model improve the performance of the latter model? Is there evidence for diffusion in experimental systems that employ directed transport?

9) In DT systems, is it clear that molecule transport is independent? How could correlated transport be included in the DT model?

10) Also, in the DT model could noise be reduced by cells measuring arrivals of particles rather than averaging over internal concentration of particles? This would presumably only change the resulting expression for precision by a numerical factor, but could this factor shift the balance in favor of DT in some cases?
