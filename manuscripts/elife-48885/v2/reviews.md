# Peer review - Round 1

Editors:
- Aleksandra M Walczak, École Normale Supérieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48885.sa1](https://doi.org/10.7554/eLife.48885.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper describes the morphology of a two-species bacterial colony on soft agar, composed of twitching Acinetobacter bayli and non-motile Escherichia coli. When co-cultured, these colonies exhibit a flower-like pattern that is absent in pure cultures. The authors find that the type IV secretion system of A. baylyi is not essential for the observed morphology, whereas agar concentration strongly affects the pattern. Using continuous models of colony morphology they conclude differences in cell motility and growth are sufficient to explain the observed pattern.

Decision letter after peer review:

Thank you for submitting your article "Flower-like patterns in multi-species bacterial colonies" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Agnese Seminara (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The paper describes the morphology of a two-species bacterial colony on soft agar, composed of twitching Acinetobacter bayli and non-motile Escherichia coli. When co-cultured, these colonies exhibit a flower-like pattern that is absent in pure cultures. The authors find that the type IV secretion system of A. baylyi is not essential for the observed morphology, whereas agar concentration strongly affects the pattern. Using continuous models of colony morphology they conclude differences in cell motility and growth are sufficient to explain the observed pattern.

Overall, all the reviewers where very positive about the work. However, they raise a number of both experimental (mix motile/non-motile A. baylyi) and theoretical questions. Addressing all of these will greatly help the readers. I am attaching the reviews in full; please respond to all the points. As you see many of the theoretical points are similar between reviewers.

Reviewer #1:

In this manuscript, Xiong et al. describe how complex pattern formation arises within a 2-species bacterial biofilm. Specifically, they show that combining E. coli and A. baylyi results in flower-like patterns while neither species individually produces this effect. They use genetic perturbations to show that this effect requires motility (mixed biofilms with non-motile A. baylyi do not produce patterns) and does not depend on T6SS. They go on to reproduce the patterns using a mathematical model that captures the differences in motility between the 2 strains.

Overall, I thought this was a very nice and clearly presented study. The phenotype is quite interesting and the authors do a good job of providing a plausible explanation (mechanical effect resulting from differences in motility). I have only one experimental suggestion to confirm this explanation. Can the authors mix motile and non-motile A. baylyi and produce the patterns in a single species A. baylyi biofilm? If the floral patterns are really a result of motility differences (and not other unknown interspecies effects) than this should be possible. They have already created the non-motile A. baylyi mutant so it should be straightforward to try this experiment. If they observe this result, then I am enthusiastic for publishing the manuscript.

Reviewer #2:

I find the results interesting and convincing; I have a series of comments that I would like the authors to address before I can recommend this manuscript for publication. I am mainly concerned with justifying the choices made for the physical modeling and provide ideas to corroborate hitchhiking as a relevant evolutionary determinant. Below I detail my concerns, and suggest ways to improve clarity and strength of the results.

The experiments describing the evolution of the flower like pattern are clear and convincing. E. coli accumulates at boundaries and causes the colony to bend inward and fold onto this decelerating region creating cusps and branches. The speed of the boundary is anti-correlated with E. coli concentration and to curvature, corroborating the picture.

Flower like patterns are recovered by a simple model tracking the shape of the leading edge, assuming that each portion of the interface expands by a balance of friction, surface tension and an expanding force due to motility. Friction is proportional to concentration of (non-motile) E Coli, which causes instability.

1) It would be helpful to discuss the origin of the expansion force, since only part of the colony is motile. Are twitching cells pushing the other strain through cell-to-cell contact? (Can the authors provide a high-resolution image to show that cells are highly packed?) Or – given that an extracellular matrix is mentioned – is it entropically driven? (Is an extracellular matrix knock-out available to the authors?)

2) Are wetting forces negligible? An order-of-magnitude estimate of the different forces or experimental evidence would justify choice of these and not other forces.

3) In the more refined model, 2D concentrations of the two strains and of the phase field are evolved in time. I would imagine the two strains move relative to one another (E. coli remains attached to the substrate whereas A baylyi twitches). A two-fluid mixture appears a natural choice; the authors consider instead a single velocity field carrying all cells, and I am unclear what this velocity represents. Is there a way to relate it to actual velocities measurable experimentally, e.g. a weighted average of velocities of the two strains? Because I am confused about the meaning of v, I do not have an intuition why it follows Stokes equation.

4) The authors predict that at low friction, the colony expands quicker with no flower like pattern, unless a large concentration of E. coli is inoculated. Assuming agar concentration affects friction, these predictions are verified experimentally. A discussion is missing about the choice of ξ and β, which appears to me quite arbitrary. Also: is the value of η obtained by fitting the expansion rate a plausible value for a bacterial colony?

5) Hitchhiking is an appealing evolutionary advantage. The discussion would benefit from two additional points. First: the authors imply that flower-like patterns are directly related to hitchhiking. However from Figure 3A it looks like E. coli hitchhikes even in round colonies maybe less so than in flower-like colonies? Could you quantify this aspect? Second: what are the parameters that switch hitchhiking on/off in the model? Are there evidences that these parameters vary in different strains? Could genes control these parameters? This would help elucidate whether hitchhiking may be actively controlled (e.g. strains turning off motility would benefit from correspondingly turning on hitchhiking)

Reviewer #3:

The authors studied interactions between a motile and a non-motile bacterial species in growing colonies, and observed the development of complex patterns that were not present in colonies consisting only of one of these species. These patterns included an undulated interface of the colony that correlated with branched structures inside of the colony. The authors provided several lines of evidence that the speed of colony expansion correlates negatively with the local concentration of the non-motile bacteria. Based on these findings, they showed that a quite simple model describing the dynamics of the 1D colony interface can account for the formation of undulations and branches. This model essentially describes the advection and dilution of the non-motile species with the motion of the front of the motile bacteria, where a local friction increases with the concentration of non-motile bacteria. To additionally account for growth and diffusion of the bacteria, the authors further introduce a more complex 2D phase field model. Similar to the 1D interface model, patterns similar to the experimentally observed ones could be qualitatively reproduced.

While I am not an expert on biofilms, I found this manuscript interesting and well written. I found particularly intriguing that pattern formation based on the collective motion of two different bacteria species can be at least qualitatively accounted for by a simple 1D model.

In the following, I will focus on discussing the mechanical modeling part, which falls more in my area of expertise. While the interface model has appeal due to its simplicity, there are a few things that need to be better clarified if not corrected about it (see below). The phase field modeling seems to be mostly appropriate with respect to the assumptions made, but also here at least some clarifications would be good, mostly related to the field Φ (see below).

More detailed comments:

1) A brief discussion on possibilities of where the force F0 and the "active pressure" in Equation 22 could originate would be good (also in the initial phase where the colony is not expanding (Figure 1D)). In subsection “Pattern-forming instability originates at the colony interface” the authors suggest some kind of active pressure created by the A. Baylyi motility. However, it is not clear to me how this alone could explain an initial phase where the colony is not expanding at all (Figure 1D). The latter seems to be more consistent with a picture of nutrient consumption combined with chemotaxis (as proposed in earlier work, Discussion section paragraph two), which could also effectively create such an F0.

2) There are problems or at least a lack of clarity related to the way the friction force Fr is included in both 1D models describing the interface behavior.

a) The authors assume Fr to be proportional to the concentration of E. coli, c, but independent of velocity. As a consequence, if the concentration is high enough, the surface would move inward (even without surface tension Fs=0), driven by this friction force. How realistic is such a friction force?

b) The normal velocity F[κ, g] is computed directly as a difference of normal forces (Equation 8). Apparently, the authors have implicitly assumed some additional, velocity-dependent friction here (and set the friction coefficient to one). It would be good to comment on how this additional friction is motivated.

c) As an alternative, one could assume Fr itself to depend linearly on velocity, a common assumption for motile cells on a substrate, which is also used in the authors' phase-field model (Equation 22). In this case and without additional friction, through force balance (F0-Fs-Fr=0) the normal velocity F[κ, g] would be given by a quotient between F0-Fs and a friction coefficient that is a function of c.

3) Even though the phase field approach is similar to previous work, some explanations, in particular related to the field Φ would make the manuscript more self-contained.

a) In subsection “Phase-field model of flower-like pattern formation” the authors state that Φ is introduced to avoid computational difficulties of dealing with the boundary. However, these difficulties and hence the necessity of Φ is nowhere explained in more detail. Why are ρA and ρE not sufficient?

b) Explanations on Equation 19 can be expanded on. In particular, brief comments on the second, diffusion-like term and the last term on the right-hand side could be helpful for readers.

c) The last term in Equation 19 is known to cancel the surface tension effect created by the second term (e.g. Biben and Misbah, 2003). Why do the authors explicitly remove surface tension in their phase field model while it is present in their interface models?
