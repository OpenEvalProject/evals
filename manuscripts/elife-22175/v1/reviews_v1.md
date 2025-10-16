# Peer review - Round 1

Editors:
- Yibing Shan, DE Shaw Research , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22175.023](https://doi.org/10.7554/eLife.22175.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Molecular mechanism of canonical activation of p38α MAP kinase" for consideration by eLife. Your article has been favorably evaluated by John Kuriyan (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript reports simulation studies aiming to elucidate the activation mechanism of p38α kinase. Using unbiased molecular dynamics simulations and calculation of free energy surfaces of the system, the authors attempt to reconcile the apparent contradictions between the X-ray structures of p38α (showing large structural changes associated with kinase dual-phosphorylation) and the NMR findings (the phosphorylation does not lead to significant chemical shift perturbation).

Essential revisions:

1) The free energy surface (FES) of ATP-bound phosphorylated system shows that the active state is accessible now, but unbiased MD simulations showed that only with substrate binding the system is stable at the active basin. To complete the paper's argument, FES of phosphorylated p38α with ATP and substrate bound should be calculated besides the unbiased simulations at 380 K. Also, showing unbiased MD on the phosphorylated and ATP-bound system without substrate and mapping the trajectory to the two CVs analogous to Figure 4 would be helpful to this argument.

2) p38α should be simulated with its crystal contacts in unbiased simulations to support the notion that crystal contacts maintain apo p38α in its otherwise unstable active conformation in crystal environment.

3) The paper is descriptive of selected conformations representative of conformational ensembles at various free energy basins; but, it is not clear how the discussed conformations are selected to represent the ensemble of each basin. The selections should be justified based on characterization of the ensemble of the entire free-energy basin; this justification is missing as is.

Other important points:

1) For phosphorylated p38α, a histogram/time-series should be shown for R49-D112 salt-bridge (ascribed to occlude ATP binding). The regions in the free energy surface allowing ATP binding should also be shown. Reviewers are concerned that the free energy surfaces of the apo unphosphorylated system are very similar to the apo phosphorylated, but the latter system binds ATP much stronger than the former. (In Tokunaga et al., 2014, the ATP affinity is 430 μM, while Frantz et al., 1998 only reported the Km[ATP] to be 25 μM. Unphosphorylated systems binds ATP much weaker at millimolar affinity.) How is the μM ATP binding reconciled with the R49-D112 salt-bridge? Another concern is that, by the energy surface of the apo phosphorylated system, the ATP-bound X-ray structure is as much as 16~18 kcal/mol higher in free energy than the inactive conformation, which seems unlikely.

2) The manuscript reports certain structural features differ considerably from any of the known crystallographic structures (e.g. 3S3I, 3PY3, 2OKR and 1CM8), which calls to question the structural details extracted from the PT-metaD trajectories (e.g. the activation-loop helix (purple in Figure 3B, and the R49-D112 salt bridge, which requires D113 to move 18 Å from its positions in the X-ray structures). The reliability of these simulations generated conformations need be calibrated in Discussion.

3) Finally, how the simulation results explain the seemingly contradictory X-ray and NMR data needs to be further discussed in more explicit terms. The contradictory is understood to be the lack of chemical shift perturbation (CSP) between unphosphorylated and phosphorylated yet the x-ray structures are the closed and open alternative structures of the A-loop. The NMR study also shows a large CSP for ATP binding to phosphorylated p38α. The minima in the FE surfaces in Figure 2 differ between the 3 states (unphosphorylated, phosphorylated and ATP bound phosphorylated) yet have overlapping regions. The overlap could explain the lack of CSP for unphosphorylated and phosphorylated (as stated in the subsection “Dually phosphorylated p38α”), but how the large CSP for bound ATP is rationalized by the FE surface, since, as stated in the manuscript, "the representative structure of the global minimum [for ATP-bound] is still not too different from the dominant one in the apo phosphorylated state." This should be explained in more explicit terms.
