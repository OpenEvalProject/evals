# Peer review - Round 1

Editors:
- Gordana Vunjak-Novakovic, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.39427.021](https://doi.org/10.7554/eLife.39427.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Ryanodine Receptor Dispersion Disrupts Ca2+ Release in Failing Cardiac Myocytes" for consideration by eLife. Your article has been reviewed by Harry Dietz as the Senior Editor, a Reviewing Editor, and three reviewers. The following individual involved in review of your submission has agreed to reveal his identity: David Baddeley (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an interesting and thoughtful manuscript that advances our understanding of the changes underlying the slower and weaker calcium transients in failing cardiac myocytes. The authors describe changes in the arrangement of ryanodine receptors, using super-resolution microscopy and simulations. The combination of structural cluster imaging, functional Ca2+ imaging and simulations has been used effectively, and the results are convincing. The main finding of the study is that RyR clusters are more dispersed in the failing than in normal cardiomyocytes.

Essential revisions:

1) Cluster fragmentation data (Figure 2) need to be shown more clearly and in greater detail. Some of the magnified unthresholded data and the scaled raw image data should be displayed (taking care not to saturate too much). A clear case should be made that the fragmentation is not a thresholding artifact, as it is known that threshold changes could cause apparent fragmentation for a given data set.

2) It is critical that the authors provide enough implementation detail for the simulation model so that a reader can use the simulation for stably dealing with the nonlinearities contained in a stochastic RyR switching model. If a custom code was used, it should be provided.

It should be clarified if the basic geometry is the same as in the Laver et al. 'induction decay' model, or if not – what is the scope and rationale for the changes made. Also, the authors should explain how they performed the numerical integration (was the time step fixed or adaptive; how were the sudden changes in transition rates incorporated in to the discretized solver?) The authors should also provide rationale for the data exclusions and clearly specify which data were used.

3) The method is based on the assumption that peripheral couplons are effectively 2D objects parallel to the cell surface and hence the imaging plane. It becomes increasingly hard to justify this assumption when moving away from surface where EM data shows that couplons take on complex 3D geometries, often wrapping around t-tubules. The absence of double-rows would imply that the images taken in this paper are not at the cell surface. While looking at the projected area will still give a reasonable estimate of relative numbers, it is likely that the absolute number of RyRs is underestimated for internal couplons. Regarding the projections to a regular 30nm grid, there is very limited evidence that RyRs form a regular grid in normal conditions within cardiomyocytes. Even if they do form a regular grid, it likely does not align with the imposed sub-sampled pixel grid. The authors should specifically discuss these important aspects of their model. It is also suggested to acknowledge that the estimated numbers are not necessarily very precise and discuss the effect that changing the RyR number would have on the simulation results.

4) With regard to the measured parameters, simple t-tests do not suffice. A hierarchical nested model should be used as p<0.05 is not satisfactory when there is large inter-group variability and the number of animals is small. The data needs to be reanalyzed, e.g. using methods described in a recent publication (Sikkel et al., 2017).
