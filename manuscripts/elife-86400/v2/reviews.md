# Peer review - Round 1

Editors:
- Raymond E Goldstein, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86400.sa0](https://doi.org/10.7554/eLife.86400.sa0)

This important work presents a hydrodynamic description of confluent epithelial monolayers that captures different forms of orientational order in a scale dependent fashion and couples this order with flows driven by active stresses. Solid evidence for the validity of this approach is provided by detailed numerical simulations of different model tissues. This work should be of interest to a broad range of biophysicists interested in tissue mechanics and active matter.


---

# Peer review - Round 1

Editors:
- Raymond E Goldstein, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86400.sa1](https://doi.org/10.7554/eLife.86400.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Hydrodynamics and multiscale order in confluent epithelia" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. We regret the long delay in furnishing this decision letter.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. As you can see from the reviews, the referees are indeed supportive of your work, but in their very detailed reports, they request clarification on a number of points.

Essential revisions:

1) We find the tensorial notation used by the authors complicated, and would prefer to see tensor terms written with indices for clarity, but I acknowledge that this may be a matter of personal preference.

2) Page 6 – the manuscript is referring to panel 2d which we think is not in the figure.

3) We are not sure about the statement that the p-dependent structure makes the multi-scale nature of the system « enormously more dramatic »; as in many physical problems, several characteristic length scales are involved; It is unclear what the authors mean with this strong statement.

4) We are unconvinced by the argument that the short wavelength scaling of density fluctuations is necessarily a fingerprint of small-scale hexatic order. The claim is all the more problematic if Eq. 8 is a small q expansion, in which case it is unclear if we should trust the large q-scaling. It is also entirely unclear how and why other non-hydrodynamic modes will not contribute to the scaling at large q. Eventually, at a single-cell level, all orientational modes should become important, not just the nematic and the hexatic ones. One way to point out the distinct imprint of hexatic order is to not simply plot S(q) for fixed qx=qy or angle-averaged, but rather to consider the full 2D plot in q-space. The nematic contribution has a characteristic singularity ~ qx qy/q4 at small q. The hexatic contribution should also give rise to a particular anisotropic structure in S(q) that could serve as a diagnostic and strengthen the point made in the paper.

A useful reference and point of comparison in the equilibrium context is – Aeppli, G., and R. Bruinsma. "Hexatic order and liquid density fluctuations." Physical Review Letters 53.22 (1984): 2133.

5) The paper can also benefit by making a stronger comparison with existing literature on models for equilibrium liquid crystals with coupled order parameters that offer a null model. Some references are mentioned below.

Dynamics, thermodynamics, and optical scattering of tilted hexatics (coupled hexatic+polar tilt order, but much of the physics is very similar)

Dierker, S. B., and R. Pindak. "Dynamics of thin tilted hexatic liquid crystal films." Physical review letters 59.9 (1987): 1002.

Sprunt, S., and J. D. Litster. "Light-scattering study of bond orientational order in a tilted hexatic liquid-crystal film." Physical review letters 59.23 (1987): 2682.

Selinger, Jonathan V. "Dynamics of tilted hexatic phases in liquid-crystal films." Journal de Physique II 1.11 (1991): 1363-1373

Selinger, Jonathan V., and David R. Nelson. "Theory of transitions among tilted hexatic phases in liquid crystals." Physical Review A 39.6 (1989): 3135.

6) Coupled hexatic-nematic models appear in certain liquid crystals (see e.g., Bruinsma, R., and G. Aeppli. "Hexatic order and herring-bone packing in liquid crystals." Physical Review Letters 48.23 (1982): 1625.) These models can have unusual emergent Potts phases, where both order parameters are disordered with finite correlation lengths, but the relative angles between hexatic-nematic order parameters remain ordered – see recent work.

Drouin-Touchette, Victor, et al. "Emergent potts order in a coupled hexatic-nematic xy model." Physical Review X 12.1 (2022): 011043.

It may be interesting to ask if similar phenomena can occur in the active variant studied in this paper and if it may be potentially relevant for tissues.

7) It is extremely unclear how the hexatic order parameter is microscopically defined; there seems to be no description given. Is the hexatic order parameter constructed from cell shape or from the distribution of `bonds' to neighboring cells? Are the two definitions equivalent when confluent? Presumably, the shape and bond angle hexatic order parameters can differ in a dense system of deformable particles that are not close-packed/confluent. The authors should comment on what the origin of the hexatic ordering is and how one may compute such an order parameter in reality.

On a related point, we fail to see why order parameter correlations are not measured and plotted to demonstrate in a straightforward way the claim of hexatic and nematic order being present on different length scales. Such calculations are presented elsewhere in recent preprints by some of the authors when analyzing experimental data though.

8) Although emphasizing multiscale aspects, the model crucially neglects any mechanism of feedback. Active couplings other than the active stress, e.g., nonreciprocal cross terms aligning the two order parameters, are neglected, though they are likely to be more dominant in a gradient expansion compared to the hexatic contribution to the active stress.

Furthermore, while substrate friction is included, traction forces (polar active forces) that are commonly exerted by cells are also neglected, which could presumably also dominate over hexatic degrees of freedom, even when randomized.

9) Equation 3-5: It would be helpful if the notation could be fixed and either σa or Pi is used. The relationship between the two is quite confusing at the moment.

Also, sign conventions should be explained: is α2>0 contractile, and if so then does the relation with f have an extra minus sign? Also, Eq. 5 suggests that α6 should have the same sign as α2, yet in the simulations opposite signs are chosen. What is its meaning and the relation between isotropic/hexatic and nematic extensile or contractile activity?

It would also help to point out how the ratio of l2 and l6 (Eq. 7) differ by a ratio of the cell size to the conventional active nematic length (l2).

The sign of ξ2,6 affects the alignment between Q2 and Q6, how does its sign affect the density and orientational correlations?
