# Peer review - Round 1

Editors:
- Manuel Thery, CEA France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34695.022](https://doi.org/10.7554/eLife.34695.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Microtubules soften due to cross-sectional flattening" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a guest Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Gregory M Alushin (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. As you will see only one set of additional experiment is suggested. Other comments can be addressed by clarification and discussion in the main text.

Summary:

The manuscript addresses a long-standing problem in microtubule mechanics, namely the discrepancy between the estimation of mechanical parameters (especially the bending rigidity) from different methods (passive - thermal fluctuations versus active - AFM or optical trapping).

Here the mechanical response of microtubules to bending forces has been investigated using an optical trap setup combined with coarse grained molecular dynamics simulations.

The main results are:

- Microtubule lattice experiences softening under relatively large compressive strains.

- This behaviour can be fitted with a new 3D microtubule lattice model which takes into account lattice anisotropy and its hollow cylindrical geometry. In contrast, the 1D elastic beam model is unable to reproduce the experimental behavior for microtubules except for the regime of very small (compressive or tensile) strains.

- An engineered bacterial flagellum more akin to a classical 1D beam, displays the expected Euler-Bernoulli bending mechanics, confirming that the microtubule behavior is not an experimental artifact. In this case the 1D model fits the experimental data very well.

Overall, the manuscript is clearly written, and the results are interesting. Presented data offer a new interpretation for the large variety in microtubule mechanical data measured by different methods and point at the key role of microtubule flattening in the modulation of their apparent stiffness, which is likely to significantly impact our understanding of microtubule mechanics and microtubule network architecture.

Essential revisions:

- Although the present data is potentially too noisy, a step experimental protocol could likely be employed to test the "aging" hypothesis. Specifically, a microtubule could be subjected to a sufficient force to buckle and soften it, followed by a low force. If the microtubule remains soft for some time after buckling, the time between the two force applications could be varied to establish the time constant for "healing". If this is feasible, including these experiments would substantially strengthen the study.

- The authors should explain how they control the attachment between bead and microtubule to obtain a configuration as shown in Figure 1A. The cartoon implies that the beads attach to the side of the microtubule in the direction of the curvature. Can the authors indicate the bead position in the experimental example in Figure 1B to make the cartoon in Figure 1A more credible? Indicated trap positions seem not consistent with the cartoon. Please describe in more detail, how the bead-microtubule attachment is controlled.

- Please describe in more detail how the force strain curve is obtained. For example, is there some averaging for the bead-trap distance, or bead-bead distance?

- From the simulations in Figure 2, Figure 4 and Figure 5 it seems that even at very low compressive strain < 0.05 a hysteresis is still present, and the microtubule may exist in two different conformations, associated with two different forces acting on the optical bead. Is this an artefact of the simulation algorithm, that the lattice gets trapped in a local minimum or do the authors have a physical explanation for the persistence of the hysteresis at very low strains? How is the steady state determined?

- In Figure 4, did the authors test experimentally compressive strains beyond 0.3? Did microtubules break and if so, at which point?

- It is unclear why the authors used a 10 protofilament model rather than a 13 protofilament one. Would the computational expense be so much greater in the latter case? One issue is that this choice leads to unrealistic lateral interactions/distances etc. And usually in vitro lattices with 10 protofilaments differ substantially from the 13 protofilament ones as they can exhibit more than the 1 seam from the 13 case. An explanation is needed.

- A clear comparison of the calculated with the experimentally measured microtubule shapes to validate the presence of the kinking instability is missing.

It seems that the model parameters are determined from a fit against the experimental force-strain curves. Could the authors show, e.g. in additional plots in Figure 5, how the experimental microtubule shapes compare to the simulated microtubule shapes at the points a,b, and c from Figure 5A?

- Alternative explanations could be envisaged and discussed:

Can the authors exclude a twisting of the microtubule lattice? The model calculations (Figure 5) show, that the microtubule lattice undergoes very drastic deformations in the kinking region. Is it plausible, that the microtubule lattice can accommodate these high strains without undergoing structural damage?

Can the authors exclude, that a lattice perturbation at the point of attachment between optical bead and microtubule is responsible for the observed softening?

- The mechanical lattice model is as simple as possible, which is a good thing since it limits the number of microscopic parameters. However, it is unclear whether a single shearing interaction (i.e. $\kappa_s$) in an effective 2D lattice is sufficient to stabilize the deformation of the lattice at the kinking instability. Furthermore, there seems to be some ambiguity concerning the relations between microscopic and macroscopic elastic constants (i.e. two different effective tube wall thicknesses are postulated, see. Table 2), which limits the quality of the predicted macroscopic elastic constants. This problem could be avoided by using for example a double shell lattice (with some diagonal elastic elements) which naturally includes stability against shear and bending in all directions.
