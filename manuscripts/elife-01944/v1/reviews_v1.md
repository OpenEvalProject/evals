# Peer review - Round 1

Editors:
- Ruslan Medzhitov, Yale University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01944.017](https://doi.org/10.7554/eLife.01944.017)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Dissecting how T cells translate individual/quantal antigen responses into collective/analog scaling in IL-2 secretion” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

This is a very interesting paper, where experiments and synergistic computational models are used to understand how IL-2 may regulate population-level responses of T cells. The connections between single cell behavior and that of the population are interesting. The main empirical result is that IL-2 production is weakly dependent on the number of T cells and strongly dependent on antigen amount, and this relationship obeys a scaling law. Since this result does not emerge from the existing models of IL-2 signaling, the authors carry out a careful set of studies to provide new mechanistic insights. They find that an interesting coupling between a coherent feed-forward loop and different time dependence of IL-2 production on antigen quantity and number of T cells can recapitulate the experimental findings. These and other findings reported in this long paper are interesting. We believe this paper is publishable in eLife, provided the authors properly address the following issues.

1) In the Results section entitled “Population-size independent scaling of IL-2 accumulation with antigen dose”, it is stated that IL-2 production varied by three orders of magnitude with antigen dose. However, when I look at Figure 1D, the ratio of the magnitudes at the peaks (filled points) appears to be no more than 300-fold. This makes no qualitative difference to the authors' arguments, but what did I read wrong in Figure 1D?

2) The scaling law reported in Equation 1 is a very nice result. On a critical note, however, the primary experimental evidence of the scaling laws is presented in a less than optimal manner (Figure 1F, 1E, 1D). It is pretty hard to really know what is going on with the three dimensional plot in Figure 1F, as the depth of deviation from power law is difficult to see. It seems important to present the scaling laws so critical to the rest of the paper via improved figures and data analyses. Perhaps 2-dimensional projections that clearly show the slope of the fitted line (exponent) on logarithmic coordinates, as is typically done in the physics literature, might be appropriate.

3) Equation 2 does not seem to predict saturation of antigen dependence. Yet, it is stated that the known model predicts saturation at 10 pm. If indeed the model does predict saturation (not clear from Equation 2), it would be good to give a qualitative reason as to why the topology of the network results in saturation.

4) In the Results section entitled “Computational model of the IL-2 pathway demonstrates the significance of experimentally characterised feedbacks”, the fact that the computational model recovers qualitative features based on the topology of the network is a nice result. But, the authors go on to note that it predicts the scaling exponents (and other features) in a fairly quantitative manner. This raises the following important question. Are all the parameters in the complex model shown in Figure 4 known? For example, how can the parameters associated with the phenomenological “Boost” variable's time-dependent activation be known from experiments? This important point needs clarification.

5) Also in the Results section entitled “Computational model of the IL-2 pathway demonstrates the significance of experimentally characterised feedbacks”, while there is nothing wrong with using differential equations for this model, some commentary on why stochastic effects are unimportant (e.g., large T cell populations) should be noted.

6) The equation following the line “Simple algebra (Figure S5E) demonstrates how the cue-signal-response to IL-2 in a mixed population of cells predicts the distribution of stimulating antigens” suggests that the ratio on the left should be 1 if antigen 1 and antigen 2 are presented in equal amounts, since the function, f, on the right is the same for both antigens. It is difficult to tell from Figure 6C whether, for the cases corresponding to the diagonal elements of the Tables below, the slope of the curve is indeed 1. If not, how different are they from unity? How do the experiments and model compare for these cases? This is important to note in order to support the claim that the model predictions follow the equation, and that the experiments mirror this.

7) Finally, a non-technical point that the authors might wish to consider is including a few more references for completeness. Regarding digital signaling in T cells, perhaps, the contribution from the Weiss and Chakraborty labs (e.g., Cell, 2009) may also be noted? Several scientists have used computational models fruitfully to study other aspects of immunology, such as host-pathogen dynamics (e.g., Perelson, deBoer labs), constraints on viral mutability and vaccine design (e.g., Chakraborty lab), and characterization of antibody and T cell repertoires (e.g., Quake, Callen labs). In the Introduction where the authors describe the value of computational studies in immunology, it may be worth mentioning such studies so as to give a complete picture of the role of computation and theory. Mentioning studies that span scales is especially significant, as in their paper, the authors span scales in a nice way.
