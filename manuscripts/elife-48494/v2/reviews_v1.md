# Peer review - Round 1

Editors:
- Stephanie Palmer, University of Chicago United States

Reviewers:
- Ann M Hermundstad, Howard Hughes Medical Institute United States

## Review text

DOI: [10.7554/eLife.48494.019](https://doi.org/10.7554/eLife.48494.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Velocity coupling of grid modules enables stable embedding of a low dimensional variable in a high dimensional attractor" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal her identity: Ann M Hermundstad (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper develops a model in which grid modules are formed by a standard attractor mechanism, and are also coupled together by recurrent interactions to coordinate stochastic drift (caused by noisy velocity inputs and/or spiking noise) between the modules. Independent drift in grid modules would severely impair the fidelity of their spatial representation (as is shown elegantly in this work), so that if grid cells represent space, it is critical to coordinate the drift in modules. The authors show that a simple mechanism – excitatory interaction between modules – can solve this problem, and suggest experimental tests of the theory. In particular, the theory makes interesting predictions arising from the inactivation of a subset of the modules (e.g. self-motion integration in the remaining modules should be affected in a specific way).

Essential revisions:

1) The choice of readout mechanisms might affect the results – hence this key aspect should be better explored.

2) The system's performance and error should be better characterized – as these are the main observables used to draw conclusions about the effectiveness of the proposed model.

Specific points concerning these first two essential revisions (followed by more essential revisions below):

a) It would be good to provide further intuition on the structure of the C_ij that achieved "satisfactory" performance. In particular, even if one constrains the coupling to lie between neighboring modules, the structure of the C_ij was not entirely clear. Is it all-to-all? Does this coupling vary in any interesting way with separation on the neural sheet? Can this coupling be constrained to be somewhat local on the neural sheet and still achieve good results?

b) The manuscript's main argument is that small differences in the phases of individual modules can lead to large errors in the estimate of position that is read out from these modules; by choosing the appropriate coupling between modules, one can reduce deviations in the phases between different modules, and in turn reduce the frequency of large readout errors. It appears that the existence and degree of these discontinuities is due at least in part to the choice of readout. As argued in the framing of the paper and shown in Figures 4D, 5B, these discontinuities are not present in the phases of individual modules, but rather arise in the readout stage. These discontinuities occur within a single timestep (at least as far as one can tell from Figure 5B), suggesting that a readout with a slightly longer timescale could potentially alleviate some of these errors. The form of the readout was derived by the same authors in a previous paper; in that paper, it was shown that the optimal readout should have different timescales for grid modules with different spacings, ranging from 1ms to 600ms. However, here a readout with a single timescale of 10ms was chosen for all modules. Based on this previous work, it's not clear why this choice was made, and what implications this has for the extent of readout errors that are shown in Figure 5B. To make the strongest argument possible, an optimal version of the readout should be used (with appropriately-chosen timescales for different modules) in order to construct the strongest null model in the absence of coupling. As it is now, it's unclear whether the observed readout errors arise from the construction of readout itself, rather than the lack of couplings. Given that this is the primary argument for necessitating couplings between modules, this should be addressed.

c) The paper would be stronger if the analyses provided a better characterization of performance and error. As it's written now, it's difficult to gain an intuition as to why catastrophic errors are occurring when they do, and how much gradual error is accumulated between these catastrophic errors. There are some small fixes that could help (see minor points). Beyond these, there are some larger points that could be made more clear. Why does the first catastrophic error occur when it does (i.e., what is the significance of the timescale marked by the dotted line in Figure 5C-D)? This timescale might have been expected to relate to the distance that must be traveled before the three grid spacings are likely to overlap, given the scale of the noise; is this the case? If so, one would have expected a sharper drop off in the percentage of successes in Figure 5C. If not, is there an intuition as to why the errors occur when they do? Does gradual drift accumulate much more rapidly in the uncoupled model that in the coupled model? This itself is interesting and would be valuable to quantify.

d) Finally, how does performance scale with the number of modules? A general theoretical model was derived for m modules but results are shown for only 2 and 3 modules (and because these two cases were illustrated in one and two dimensions, respectively, it's not possible to compare directly between them). Larger numbers of modules could presumably lead to a couple of different scenarios that might impact the conclusions in different ways: i) more modules could lead to a reduction in readout errors (even in the absence of coupling), because the readout is averaging over inconsistencies among modules; this would suggest that some of observed error could be alleviated with additional modules, or ii) more modules could lead to an increase in readout errors via the additional inter-module recurrence (e.g. in cases where assumptions about linearity or small input velocity break down). It would be useful to report more on these type of analyses and show how they depend on the source/magnitude of noise. Can these findings be interpreted in terms of the actual numbers of modules in mEC (which would be helpful to report somewhere)?

3) Provide, in the main text, more details/intuition about the choice of inter- and intra-module couplings, which is indeed a fundamental aspect of the work. (See also point 1 and 2a above.)

A key point of the theory is that modules should be coupled in a phase-independent manner, and that the coupling should only depend on the rate of change of the phase. There are two things that could be shown, perhaps in Figure 1 and incorporated into Figure 2:

– show the detrimental effect of phase-dependent coupling for position encoding

– recap the properties of self-motion integration networks (e.g. Seung's model used throughout the paper), showing the velocity dependent tuning of the left and right network and how a simple set of synaptic weights between modules can extract this information.

4) Discuss the role of landmarks (e.g. boundaries) in path integration – this important aspect did not receive enough attention throughout the manuscript.

For example, the section on "Intrinsic neural noise" shows how the coupling between modules coordinates their drift. An alternate idea might have been to largely shut down the drift via interaction with border cells (or more generally with boundaries and landmarks). A comment on this alternative would be in order in the Results and in the Discussion since there has been a good bit of work on it lately. These kinds of error correction mechanisms that people have considered so far still work separately on each module, and so a coordination mechanism such as the one in the present paper will still be necessary because even a small amount of independent drift between modules can cause problems with the spatial representation.

5) An additional figure should be added at the end of the paper, illustrating the non-trivial prediction related to the inactivation of one or more grid cell modules. This would help make the work for broadly accessible, and would strengthen the discussion.

6) Discuss the possibility that other (published) mechanisms might be at work for the self-organized emergence of modular structure (which is otherwise assumed in the current manuscript).

In particular, a potential overlap is with recent work on the role of interactions with borders and landmarks in anchoring and reducing drift in the grid system (e.g. Keinath et al., eLife; Ocko et al., PNAS; Hardcastle et al., Neuron; Pollock et al., bioRxiv). The present paper is complementary in that it suggests a way of coordinating drift between modules, rather than reducing the overall amount of the drift. Indeed the border interaction mechanisms may not reduce drift enough on their own, and the coordination mechanism described in the present paper may be necessary also – both mechanisms could be in play. Some commentary would be worthwhile in the Discussion as an interesting direction for the future is to ask how border interactions and inter-module interactions could work together.
