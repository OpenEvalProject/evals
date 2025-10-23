# Peer review - Round 1

Editors:
- Raymond E Goldstein, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68679.sa0](https://doi.org/10.7554/eLife.68679.sa0)

This work proposes a method to obtain a reduced description of the collective dynamics of thousands of cells moving together during zebrafish gastrulation as a few fundamental modes, and to derive effective dynamics for these modes. This well-written work enables a simplified picture of the key features of cellular collective motion, that will be useful to physicists and biologists looking for a quantitative understanding of morphogenesis.


---

# Peer review - Round 1

Editors:
- Raymond E Goldstein, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68679.sa1](https://doi.org/10.7554/eLife.68679.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Learning developmental mode dynamics from single-cell trajectories" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sebastian Fürthauer (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) How good is the mode decomposition?

– It is not a priori clear that the mode decomposition suggested is a good representation of the data. It would be helpful if the authors quantified and discussed the error between the continuous low dimensional representation of the data and the raw data.

– Along the same lines, are there a conditions under which mode decomposition is expected to fail? The authors should give a clear idea on when the ideas presented here are applicable and when not.

2) How trustworthy are the inferred summary statistics?

The summary statistic ( defect numbers / fluctuations ) need to be tested against some ground truth. If this is not possible from the data used here it would be illuminating if the authors could test against artificial data.

3) How predictive is the inferred forward model?

– In Figure 3 the authors compare the inferred dynamics and the real data. This is very appealing and the strong point of the paper. We are, however, confused whether the matrix M is inferred using the full time course of the experiment, or just parts of the time course. In other words is M just a way of rewriting the coefficients in Equation 7?

– As it stands we are unclear of what is being learned in M since there is no clear separation between a 'training' and a 'test' set of samples.

4) The paper could greatly benefit if the authors used their method to infer the known dynamics of some artificial data. Then they could validate the inferred model against time courses generated from different initial conditions and against unseen data.

5) We understand that the integral of the field ρ on the surface is 1? We would suggest to mention this already in Equation 1. We also assume that with this definition, J is not actually a cell number flux, but a normalised cell number flux?

6) Because the effective Equations 2a and 2b are written for normalised densities, we understand that cell division and death are effectively absorbed in a flux. So if cells were undergoing cell division in some region of space, and cell apoptosis in another region, this would be interpreted as a net flux between the two regions. Isn't that a potential issue of the method? Can the authors further comment on this?

7) We would argue that one central conclusion of the manuscript is in Figure S6, showing that local rules of interaction cannot explain the dynamics of the system. That is also one potential weakness of the approach: what is exactly learned by the effective dynamics? There is a complex set of interactions between modes suggested by Figure 3D but what is their meaning, given that Figure S6 also indicates, as the authors also point out, that there are missing unresolved players in the equations? The whole approach would be more convincing if the authors could show that the effective learned model have some predictive value. For instance, would changing the initial condition in the integration of the effective system, gives a result that makes sense in regard to the developmental dynamics; indicating that the effective dynamics is not tied to one particular realisation of the biological system?

Reviewer #1:

The authors present ideas for obtaining a low dimensional representations of the complex and rich data obtained in cell tracking experiments on zebra fish gastrulation. They argue that such a low dimensional representation can be used to infer a dynamical model from the data. These ideas are potentially very important. However, the methods presented here need to be more explicitly validated.

Reviewer #2:

Romeo et al. describe a method for the analysis of the collective flow of cells and its decomposition into modes of motion. The authors start by defining a local density and a local flux by coarse-graining the discrete data in a consistent way. The density and flux fields are then projected onto scalar and vectorial spherical harmonics, and the authors show that a relatively small number of modes is sufficient to account for the flow field; the evolution of some of these modes with lower symmetry reflects major changes in the cell density pattern in the embryo. The authors then look for a linear mode coupling, first order dynamics model for the modes of lowest order they have kept in their analysis. This procedure defines an effective model for the dynamics of the system. Looking in real space at the spatial couplings shows that these effective couplings do not decay spatially, but are long-ranged; indicating that local rules for fluxes cannot capture the dynamics of the system.

The authors presents an elegant and solid work which is done with a very high level of care and rigour. The excellent level of clarity of the manuscript, which presents its concepts in a well-structured manner, makes it really nice to read. The method described by the authors, notably, gives a way to analyse cellular trajectories in a reduced dimensional space which is helpful to characterise the complex cellular flows.
