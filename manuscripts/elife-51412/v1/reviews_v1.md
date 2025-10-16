# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51412.sa1](https://doi.org/10.7554/eLife.51412.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work addresses how animals like snakes deal with the deformations they leave behind on the surface of deformable materials (sand, mud) on which they slither. Insights from studies of a variety of snakes and a "robophysical" model in which a slender plate is dragged through sand are combined with theoretical ideas from granular physics and the fluid mechanics of locomotion by slender objects to obtain a clear picture of the energetic tradeoffs necessary for efficient locomotion.

Decision letter after peer review:

Thank you for submitting your article "Mitigating memory effects during undulatory locomotion on hysteretic materials" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Michael J Shelley (Reviewer #2); Stephen Morris (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper presents an ambitious and rather comprehensive study of the locomotion of a wide selection of snake species across the surface of a granular medium. To my knowledge, such a broad study has not been attempted before. The main strength of the work is the broad and interdisciplinary approach, combining quantitative measurements, theory, connections to snake anatomy, field observations and robot models. As the authors point out, there is a very well-developed theory for propulsion in Newtonian fluids (like water), where resistive force theory (RFT) serves as a good approximation to the full hydrodynamic problem of viscous flow around slender objects. Here the question is what kind of local theory analogous to RFT might hold when the substrate on which the animal moves is permanently deformed by the motion. The physical model is convincingly validated with simple plate dragging experiments. The paper contains a wealth of interlocking details and observations, including identifying when and why the locomotion strategy fails for some non-adapted species. It provides a clear and insightful picture of snake locomotion that might be used to advance robotic analogs. In summary, this paper is a very good, interesting, and thorough study of a mostly unexplored topic of broad interest.

Essential revisions:

1) The paper presents a very detailed and comprehensive study, but one that is scattered over too many disconnected pieces, making the narrative difficult to follow. There is a Main Text, very detailed and compact figures with long captions, a huge array of appendices and supplementary information, and appended videos. The effect is to diffuse the information rather widely, making reading difficult. There is overlap and repetition. We have not previously encountered a relatively short paper with 9 appendices. The authors must reformat the paper to make use of figure supplements in order that the logic and results are more clearly spelled out.

Moreover, the authors cite the supplementary material as if it were a separate publication. It is thus cited differently than Appendix material! We found this quite confusing.

Some minor details of method and snake husbandry might be usefully combined into one Materials and methods appendix with short subsections, while other appendices and supplemental material should be put back into the Main Text. We consider the mechanical RFT model to be a main contribution of the paper and thus should be mostly found in the Main Text. The Introduction and conclusions need to provide a clearer roadmap to all the interlocking parts of the argument and results.

2) There is also a distinct lack of detail presented on the mathematical/physical modeling. A good example of this lack of detail is found in the section on the drag model. We found no detail in the paper about the form of the "static stress" σ0.

In addition to providing those details in the paper, we would suggest that the authors provide (at least) some heuristic arguments explaining the typical scale of surface stresses they obtain (say, 0.1 N/cm2). Surely this can be explained in terms of grain size, coefficient of static friction, gravity, etc. Without this, the reader has learned nothing from the fact that an unspecified model is consistent with the data.

3) The issue of the drag anisotropy is a fascinating one, particularly in comparison to the behavior of long slender objects in low Reynolds number Newtonian fluids. But here we were slightly confused about the results, and think the presentation needs to be reworked. Consider the following: in normal slender body hydrodynamics there are drag coefficients for motion normal (perpendicular) and tangential (parallel) to the filament, call them ζpara and ζperp, and one writes the total drag force F (per unit length) on a filament with velocity v as

F = (ζparatt + ζperpnn)dotv

where ζperp approximately 2 ζpara = 4 pi eta /(log(L/d)+const), where η is the viscosity, L the total length, and d the filament diameter, and the constant is order unity. The coefficients zeta (which are basically the Cn and Ct coefficients in subsection “Drag anisotropy is not strongly dependent on speed or depth”) thus do not depend on the angle of motion. So, we think the real question here is whether the experimental results in this paper are consistent with such constant zetas. Therefore, instead of (or in addition to) plotting the ratio σn/σt as a function of βd in Figure 6A, consider plotting versus tan(βd) and/or a plot of (σn/σt)/tan(βd) vs βd to see if a straight line emerges, which would be an indication of fluid-like behavior (or deviation from it). Also, the quantity Kfluid mentioned in the figure appears to be undefined.

4) Continuing with this point, the authors need to write down precisely a mathematical statement of resistive force theory for these systems. Is it like what is written above except for the definitions of the zetas (Cs), or something else?

5) The section comprising paragraph four-six in subsection “Surface resistive force theory model” is similarly in need of revision. It continually refers to supplemental material and simply says whether the model works or doesn’t but does not convey any real physical insight to the reader without turning to that material.

6) The authors may wish to note that another medium that has memory is a fluid moving at high Reynolds number. Recent work from the lab at Courant has shown that hysteresis arises in model experiments of flocks due to the finite lifetime of vortices shed by leading swimmers.

7) The authors frequently make reference and comparisons to subsurface locomotion and to low-Re swimmers, without really explaining what Reynolds number is. They seem to assume the reader is simply familiar with these cases, without explanation. It might be useful to briefly bring together these comparisons in the Introduction, so that later reference to them seem less disconnected.
