# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- Nir Ben-Tal, Tel Aviv University Israel
- Simon Scheuring, Weill Cornell Medical College United States

## Review text

DOI: [10.7554/eLife.50576.sa1](https://doi.org/10.7554/eLife.50576.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Conventional molecular dynamics simulations and a new enhanced sampling method, presented in another paper (in J Comp Chem), were used to examine the extent of lipid perturbation due to conformational changes of the Na+-aspartate symporter GltPh. This transporter, which follows the 'elevator mechanism', undergoes particularly large conformational changes upon substrate transport; the transition between the outward-facing and inward-facing conformations involves a 15Ang motion of the transport domain with respect to the stationary domain of the protein. Their simulations suggested that this transition radically perturbs the lipid bilayer, which is expected. However, very surprisingly, it leads to a large free energy penalty of about 20 kcal/mol, which of course needs to be balanced by internal components of the free energy. The manuscript addresses a fundamental and very interesting question in membrane biophysics.

Decision letter after peer review:

Thank you for submitting your article "Large-scale state-dependent membrane remodeling by a transporter protein" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Nir Ben-Tal as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Simon Scheuring (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

A new enhanced sampling simulation method, presented in another paper (in review with J Comp Chem), is used to examine the extent of lipid perturbation due to conformational changes of the Na+-aspartate symporter GltPh. This transporter, that typifies the 'elevator mechanism', undergoes particularly large conformational changes upon substrate transport; the transition between the outward-facing and inward-facing conformations involves a 15 Ang motion of the transport domain with respect to the stationary domain of the protein. The simulations suggest that this transition radically perturbs the lipid bilayer, which is expected. However, very surprisingly, it leads to a large free energy penalty of about 20 kcal/mol (which of course needs to be balanced by internal components of the free energy).

Opinion:

The manuscript addresses a fundamental and very interesting question in membrane biophysics. In this respect it is very suitable for publication in eLife. The problem is that it is unclear how trustworthy this large estimate is. The following suggestions may increase the credibility of the manuscript.

Essential revisions:

1) The in-plane distributions of the membrane deformations predicted by the simulations are inaccessible for experimental verifications. Moreover, the character of these deformations (types of strains in the case of 3D description or bending/stretching/chain tilting for a 2D description of the membrane) is not determined.

2) "In a recent breakthrough, we have developed and validated a promising free-energy simulation strategy to address this problem, which we refer to as Multi-Map (Fiorin, 2019)". The Fiorin paper is not in review here so we will not comment about it in detail. However, the draft that is included does not consolidate this bold statement. To our understanding it shows that the new formalism converges to the Helfrich-Canham theory and agrees with measurements at long distances (100Ang and more), as it should. However, we did not see any comparison regarding short distances which are relevant here. This statement should be removed.

3) The authors dismiss the Helfrich-Canham theory and its extensions, arguing that they do not hold for short distances. And yet, it would be insightful for the reader to know what values this approximate model and its extensions give for GltPh. At the very least it would indicate how high the 20 kcal/mol value is compared to existing theory.

4) The derived energies of the membrane deformations, which could be indeed important for understanding the effects of the membrane lipid composition on the protein function, are not supported by any independent estimations and remain, therefore, completely dependent on the parameters of the computational model (forcefield parameters), and other details of the simulations. The authors should admit to it or provide experimental measurements.

5) No analysis is provided either of the effects of membrane tension, which may dramatically change the protein-mediated deformations and their distribution, or of the presence in the membrane of specific lipids such as cholesterol, PIPs, DAGs, etc, whose redistribution to the protein vicinity may moderate the elastic energy. This decreases the general impact of the results.

6) Evidently, the authors are aware of the exceedingly high energy penalty due to lipid perturbation and try to explain it in Discussion. However, the arguments raised are not compelling. Thus, the tune of the manuscript should reflect the fact that all we have here is a computation that may or may not be correct.

7) Introduction, third paragraph: The question is nicely set between (1) "moving polar sidechains on their surface into the bilayer interior and exposing hydrophobic ones to the solvent" and (2) "the morphology of the lipid bilayer could adapt to the conformational state of the protein, and match the amino-acid make-up of the protein surface". The authors obviously come to the conclusion that the latter (2) is the case. However, at a considerable (20kcal/mol) cost. Given that the structure of all conformations are known, the authors should provide an estimate of the energetic cost for the rejected hypothesis (1).

The simulations:

8) The boundary conditions imposed on the membrane fragment are not specified. At the same time, in the absence of membrane tension, which seems to be the case here, the effects of the boundary conditions might be substantial.

9) The method is based on combining coarse-grained and all-atom simulations, which can be tricky. In particular, for the all-atom simulations, the authors take the course-grained system they simulated and convert it to all-atom, while also (naturally) changing force-fields. Then they let the system relax and report that the trends observed are consistent with the course-grain simulations. It is theoretically possible that transitioning the system from the course-grained to the all-atom parameters is not that trivial, and maybe the fact that they start from an already equilibrated state introduces some bias. Could it be examined somehow?

10) It is unfortunate that DPPC (transition temperature 41C) was chosen for many simulations. Why? Also, simulations using POPC (transition temperature -2C) are shown. The fact that the results are quasi identical seems rather worrying than comforting. Why these choices? Why not using a mixture, it is not unthinkable that in a mixture the protein would recruit specific lipids on these interfaces between transporter and scaffold domains. Please comment. Or, better, examine in simulations.

Presentation:

11) Introduction: "These perturbations develop to accommodate the amino-acid composition and specific structural features of the protein surface.": This deserves a reference to the Piezo channel, the only protein that displays clear structural features that force the membrane into bending, and for which a theory and experiments about how membrane bending (and flattening / the physics of the membrane) is exploited to gate the channel was presented.

12) The general reader might not know what the second-rank order parameter of the lipid alkyl chains is.

13) Figure 2, Figure 3 and associated, in the context of "Transport domains bend the membrane, while scaffold domains anchor it": While we understand the measurements, the results and the importance of all these results, the presentation is unclear with respect to the setting of the 0-level. From the captions "2(A) The deflection is quantified by calculating the mean value of the Z coordinate of the bilayer across the X-Y plane." and "(A) Deflection of the membrane mid-plane relative to a flat surface". For example, the image in 3A), all the membrane has negative deformation. Wouldn't that correspond to creation of a net elastic and potential energy? Shouldn't the bilayer as a whole still go towards flat and as a result one has negative deformation next to the transporter domains and positive deformation next to the scaffold domain. This does not change anything to the results in terms of local deformation, right? Is the bilayer held in place at the periphery of the simulation box?

14) Further on this: Why is the scaffold domain considered the 'anchor'? Why does the membrane next to the transporter domains (that are in the inward (down) orientation) move down, rather than the scaffold domain moving upwards? Overall – after sufficiently long relaxation of the all-inward structure – shouldn't the overall level of the membrane remain 0 and the membrane next to the transporter domains shift downwards, but the membrane next to the scaffold domains shift upwards? Especially, in light of Figure 3C, which seems to show that there are many more key amino acids in the transporter than in the scaffold domain, one would expect that the transport domain dominates the relative motion. It is unclear how in panels like Figure 2A left, 2A right, Figure 3A, all membrane deformation values can be positive or negative? Is this the reason why such huge energy penalties result from the analysis?

15) Discussion section: The authors find a large energetic penalty for the inward facing state due to membrane deformation. They note that the smFRET studies displayed almost zero energy difference between the states. In contrast the HS-AFM study revealed that the inward facing state indeed was the high energy state (like here). The authors mention that the HS-AFM study was performed in rather densely packed membrane where no such long range lipid relaxations are possible as in the study here, yet it is a flat membrane. In this context, it is also noticeable that the smFRET studies are performed either in detergent or on transporters in small vesicles that are tethered in outside-out configuration only – which goes against the bowl-shaped structure of GltPh – of which the authors see the preference for membrane bending in Figure 1 (side view), which might favor the adoption of the inward-facing state in the smFRET experiments.
