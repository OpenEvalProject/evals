# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56500.sa1](https://doi.org/10.7554/eLife.56500.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper by Hillringhaus et al. studies the invasion of red blood cells by malaria parasites (merozoites), a key element of their reproduction cycle during the blood stage of the disease. Building on earlier work demonstrating the importance of geometrical alignment of merozoites with the cell, adhesion to the cell membrane and binding by filaments, the present work develops a computational model that incorporates stochastic deformations of the cell membrane and the discrete nature of the adhesive bonds. By exploring the influence of various parameters, such as the bond kinetics and RBC membrane stiffness, it is shown that alignment times similar to those observed experimentally can be obtained purely by a passive mechanism that balances adhesion and membrane elasticity.

Decision letter after peer review:

Thank you for submitting your article "Stochastic bond dynamics facilitates alignment of malaria parasite at erythrocyte membrane upon invasion" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Suzanne Pfeffer as the Senior Editor The following individuals involved in review of your submission have agreed to reveal their identity: Michael Gomez (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This manuscript studies the invasion of red blood cells (RBCs) by malaria parasites (merozoites), a key element of their reproduction cycle during the blood stage of the disease. While initial attachment of merozoites to RBCs occurs rapidly, the major factor that limits successful invasion is that the merozoite must align almost perpendicularly at its apex to the RBC membrane. Using static models, previous work (e.g. Dusgupta et al., 2014 and Hillringhaus et al., 2019) has demonstrated the importance of adhesion (arising from filaments on the merozoite surface that bind to the RBC membrane) and elasticity of the RBC membrane: together these enable partial wrapping of the membrane around the merozoite to aid alignment. This manuscript builds upon these studies to address the dynamics of alignment, developing a computational model that incorporates stochastic deformations of the RBC membrane and the discrete nature of the adhesive bonds. By exploring the influence of various parameters, such as the bond kinetics and RBC membrane stiffness, they demonstrate that alignment times similar to those observed experimentally can be obtained purely by a passive mechanism, namely the balance between adhesion and membrane elasticity.

The manuscript is very well written and discusses the details of the model and its results thoroughly and clearly. The inclusion of dynamic effects and discrete bonds resolves major shortfalls of previous models. The resolution of the simulations is very impressive and enables new insight into what governs the timescale of alignment and hence the invasion process. In addition, it is clear that the framework developed here can be adapted and built upon in future work to explore other effects, as well as informing further experimental studies in this area. I therefore strongly recommend publication.

The reviewers request that you address the following issues to enhance the present story.

1) A numerical parameter that could potentially strongly influence the results is the repulsion distance σ. It must be very carefully checked how a variation in σ affects (or not) the results. This is particularly important since the authors do not only aim at a qualitative explanation, but a fully quantitative prediction of the biophysical alignment process.

2) The authors very briefly state in the Discussion that “simulations with only short bonds show that the parasite is quickly arrested…". The authors might include some data on that. Also, it triggers the question what happens if there are only long bonds? Or, to state the question somewhat deeper: is the two-bond combination really necessary to reproduce the alignment? Or can one imagine that a single bond, of whatever nature, reproduces the alignment equally well?

3) Again, in the Discussion the authors mention the “stochastic motion observed experimentally”. Figure 2B only shows the average fixed-time displacement, it does not indicate whether that motion is directed or truly stochastic. The authors should find a way to substantiate their claim that the experimental motion is truly stochastic and not somehow directed. For example, one might try to identify the (signed) distribution of Δ d within some meaningful local coordinates and see if the average is 0. Other ways to demonstrate the stochastic nature are certainly possible as well.

4) The effect of bond kinetics on alignment is discussed in detail, but what about the influence of the bond spring stiffnesses, i.e. λlong and λshort (defined in Equation 12)? I would guess that for a given bond number, the ratio of these stiffnesses to the membrane bending stiffness controls the degree of wrapping, similar to the dimensionless adhesion strength defined by Dusgupta et al., 2014. I appreciate much remains unknown about the properties of the binding filaments, but at the very least the values of λlong and λshort chosen in the model (Table 2) need some discussion (for example are they varied as part of the fitting procedure discussed in subsection “Calibration of RBC-parasite interactions”?).

5) Similarly, it would be good to know what influences the most-likely values of dapex and θ for the distributions in Figures 3A-B. I understand that these peaks correspond to a configuration with maximum contact area (as discussed in subsection “Membrane deformation and parasite dynamics”). Are the associated values of dapex and θ then just determined by the egg-like geometry of the parasite and RBC, or do they also depend on the mechanical properties? Since these most-likely values (and their closeness to the values needed for alignment) play a key role in determining whether alignment occurs, it would be good to discuss what parameters control these values. I appreciate a thorough exploration of parameter space is not possible due to the computational time, but it would be worth at least having a qualitative idea.

6) Did the authors examine where on the RBC membrane alignment is most likely to occur? I would expect it to be the region near the centre of the RBC where the membrane is concave-outward, since here the membrane would naturally curve towards the merozoite so that wrapping requires less bending energy. This concave-outward region only exists on one side of sickle-shaped RBCs, which could be a contributing factor (as well as the increased membrane stiffness) as to why sickle cell anemia gives some resistance to malaria.

7) Similarly, is it possible to speculate on the influence of the merozoite shape on achieving alignment? For example, as well as providing an obvious advantage for initiating invasion, the egg shape means that the apex is titled towards the membrane in the most-likely configuration with maximum contact area (i.e. the peak of the distribution in Figure 3B is well above θ = π/2). This is not the case for a spherical shape, for which there is no preferred orientation, so that the merozoite may become more easily arrested with its apex pointing away from the RBC. Moreover, the tapering near the apex means there is naturally less material in its vicinity, so that alignment potentially could be achieved with an apex angle θ further from π.

8) Figure 4B: Why are there so many instances of very short alignment times, below the lower bound of 7 seconds observed experimentally by Yahata et al., 2012? Is this due to an effect being neglected or overestimated, or can the discrepancy be improved simply by tightening the alignment criteria (e.g. requiring θ > 0.9π rather than 0.8π)?

9) One concern is the sensitivity of the results to the discretisation used. This is because alignment requires that the distance between the merozoite apex and RBC membrane is very small and may become comparable to the discretisation length of the RBC membrane. The alignment criteria also necessitate examining small changes in the apex angle θ from π. For example, the change in the angle of the normal vector to the RBC membrane from one triangular face to the next scales as l/R, where l is the characteristic size of the triangles and R is the typical radius of curvature of the membrane. For the change in angle to be small (so that discretisation effects are negligible) requires l << R. However, the schematic in Figure 3A suggests that if the discretisation length is halved so that each segment becomes two segments, the value of θ could easily change by an amount comparable to the tolerance in the alignment criterion, i.e. 0.2π. Could the authors comment on this?
