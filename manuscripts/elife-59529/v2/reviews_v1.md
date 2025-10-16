# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59529.sa1](https://doi.org/10.7554/eLife.59529.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Through a combination of experiments, theory, and computation, this paper uncovers several general rules that determine the relationship between cell shape and microtubule orientational order. It exploits the separation of time scales between fast microtubule dynamics (e.g. dynamic instability) and the much slower processes involved in cell shape changes to develop a minimal model that captures a wide range of experimental observations.

Decision letter after peer review:

Thank you for sending your article entitled "Robustness of bidirectional microtubule network self-organization" for peer review at eLife. Your article is being evaluated by Anna Akhmanova as the Senior Editor, a Reviewing Editor, and three reviewers.

Summary:

Plochocka et al., present a paper that deals with the affect of microtubule polymerization/depolymerization kinetics on the orientation of filaments in large arrays inside a closed cellular geometry. The authors find that the distribution of MT orientations is dependent on cell shape but independent of the kinetic parameters using both experiments and a geometric model of the MT array. Because of this independence, the authors write that this is an archetypal example of robustness in a complex biological system.

Essential revisions:

1) The authors use a purely geometric model of MT growth and the effects on MT kinetics. We are concerned that this is a step too far. First, crosslinking proteins and molecular motors play a huge part in the assemble of MT arrays and these are not considered at all in this work. E.g., does the orientation distribution change if motors are inhibited in the experiments? For the role of motors, see for example:

Zemel, Assaf and Mogilner, (2008).

Zemel, Assaf and Mogilner, (2009).

2) The authors' model treats the MTs as non-interacting which seems incorrect. In addition, it seems that the model is essentially guaranteed to give an alignment along the long axis of an elliptical enclosure because the catastrophe rate is governed by the contact angle between the MT and boundary. The particular form of that rate needs to be explained and justified better. The authors state that the simulation results are insensitive to the alphas and betas, but what about thetaC? What about proteins that lie on the cell surface and potentially affect MT kinetics in a spatial manner?

3) The authors analyze the MT organization only using the angular distribution across the whole cell. But in the cell, and in the more detailed simulation model, they could look at the local nematic order, and plot its spatial distribution. Surely this will reveal more details, which the detailed simulation should recover better than the "hairyball" model. Similarly, the spatial distribution of the zipped MTs, of the locations of catastrophes etc., as function of eccentricity.

4) The cells are approximated as ellipses, similar to the "spherical cow" simplification. However, cells are usually treated as polygons: do the multi-cell Y-junctions, play a role in the MT organization?

5) The assumption in the "hairyball" model that the MTs remain pointing to the ellipse center is not clear and not explained. is this an effective way to introduce the MT-MT interactions that are missing from this model?

6) In Figure 6 the multiple lines for the cell-shape/ellipse are difficult to discern. We suggest to plot them separately.

Except for the highest eccentricity, the simplest "hairyball" model fits best the experiments. Why? and does it include the non-uniform nucleation of MTs along the membrane?

7) We are concerned that the case for robustness is overstated. The authors should provide justification for the claims that their results (given the caveats above) would be generalizable to other kinds of MT array geometries (as claimed in the discussion). And it is important to emphasize what is being analyzed. The quantities of interest are the AVERAGED distributions, which by definition are taken on time scales long compared to the underlying microscopic dynamics.

As a general principle it is clear that once there is a separation of time scales

then the slow degrees of freedom dominate, and if reorientations occur at the boundary the law of reflection used will dictate the results. That there should be a strong dependence on the cell geometry (i.e. eccentricity) was already implicated in the work of Khuc Trong et al., (where it was MTs emanating from the boundary) and would follow from the dominance of the wall collisions.

In that sense, the present results are reminscent of much older work on wave pattern formation in the Faraday instability Gluckman et al., (1993) in which time averaging of the chaotic patterns revealed mean values that reflected the geometry of confinement. The work also reminds us of that of Dumais et al., on the relationship between cell geometry and cell division planes in plant cells, where microtubule orientations also play a role (Besson and Dumais, (2011)). But it seems to us that a claim of generality must be made after having demonstrated that the issues neglected above do not change the results.
