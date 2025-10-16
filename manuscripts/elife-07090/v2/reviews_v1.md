# Peer review - Round 1

Editors:
- Helen McNeill, The Samuel Lunenfeld Research Institute , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07090.042](https://doi.org/10.7554/eLife.07090.042)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Interplay of cell dynamics and epithelial tension during morphogenesis of the Drosophila pupal wing” for consideration at eLife. Your article has been favorably evaluated by Naama Barkai (Senior editor), a Reviewing editor, and three reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

In general all of the reviewers felt the body of work was very impressive, and brings important new information to the field. Using live imaging, genetic/physical perturbations, quantitative data analysis and modelling they explore morphogenesis of the Drosophila pupal wing and how tissue shape changes in the Drosophila wing are related to cell shapes and mechanics. It also reveals the importance of Dumpy-dependent attachment of the disk to the cuticle. The authors develop a method to extract cell-level contributions to tissue area changes and tissue shear, and demonstrate that the various drivers of tissue shape are changing with time in interesting and robust patterns. In addition, the authors develop a fairly simple continuum model for tissue shape changes that can fit all the data in WT, mutants, and ablated embryos. This work demonstrates that both external boundary conditions as well as internal force generation are necessary to generate the WT cell shape. The deformation of wing tissues in normal and dumpy mutants is decomposed into contributions from cell growth, rearrangement and mitosis. An effort is made to distinguish autonomous cell behaviours from responses to stresses that arise from hinge reshaping and pinning of the blade margins. The experiments have been done carefully and bring important new information to the field.

In their revised version of the manuscript the authors should address the following points raised by the reviewers.

1) Calling ṽ the change in the “shear” is not precise. Some people use “shear” to refer to “shear stress” instead of shear strain. Why not call it the shear strain?

2) Why is there no autonomous active pressure in Equation 3, which is the analogue to the active shear stress in Equation 4?

3) Why does Equation 52 in the supplemental include a viscous contribution to the pressure (and that's what the authors say they fit), but Equation 3 includes no such term? It is not clear when the dissipative term is included and when it is not.

4) Given that several main results in this paper rely on the fact that there is a delay (τd) between the cellular topological changes (R) and the cell elongation (Q), and that this delay seems to be about 4 hours, it would be extremely useful to have some discussion of what is generating that delay. Naively, I would expect that cell elongation would drive rearrangements instantaneously—changes to shape should immediately generate T1s in fairly generic geometries. I find the existence of τd to be incredibly surprising (although the data is convincing that it exists.) So this 4 hour timescale must be something having to do with a signaling cascade specific to biological systems? Are there any candidates for this?

5) Building upon this, it would be useful to provide a sentence or two (or a reference) for why the functional form of Equation 5 is chosen. There are other ways to incorporate delays into partial differential equations—why is this the correct way to do it?

6) It was not clear why the authors choose to use shear to characterize deformation (subsection headed “A method to quantify cellular contributions to wing blade deformation”). The authors might consider that elongation in the proximal-distal (PD) direction might be a more natural and easily understood measure. Shear is notoriously difficult to interpret mechanically. What defines its positive sense? An examination of Mohr's circle or some other strain clarification tool highlights the challenges associated with its definition and interpretation, even for mechanicians, never mind biologists and others lacking that specific training. By describing the deformations in terms of elongations, these unnecessary complications might be avoided. For example, one of the reviewers struggles greatly with the authors defining shear in terms of “the negative change in average triangle elongation” (in the third paragraph of the aforementioned subsection and then seemingly contradicted in the fourth paragraph). If a triangle elongates in the PD direction, that motion could be just as easily assigned to positive or negative shear (a square whose top moves to the right or to the left, respectively) suggesting that the correspondence is arbitrary, and not meaningful. Modern continuum mechanics texts and a few biologically-motivated articles provide shear definitions that are mathematically-motivated and rigorous.

7) While using shear strain is okay (and is natural for a physics audience) it is not as natural for a solid mechanician. All the reviewers agree that the description of what is meant by “shear” is confusing at present in the manuscript, and could benefit from making more connections to the engineering literature. When using Hooke's law, it and other constitutive equations should be qualified with a statement that points out it is a simple and appropriate starting point, but that nonlinear elasticity may play a role.

8) The authors are missing references to other cell mechanics models, including those by Brodland et al. and comparison with previous cell-based computational models and constitutive equations that address how tissue deformation is related to mitosis, cell rearrangement and growth, and other factors. The paper has the potential to bring much understanding of tissue reshaping, and defining the deformations and their contributions in terms of elongation (normal strain) rather than shear (shear strain) would represent a tremendous improvement to its presentation, rigor and accessibility. It would also remove many of the hand-waving machinations that clutter an otherwise lovely story. It furthermore seems a shame that an article that could serve as a major reference to future researchers does not bring clarity and simplicity to the mechanical analysis and lead future investigators in that direction.

9) Wing area is determined by mass accumulation, tissue (cell) height and cell loss, not by other parameters. This should be made clear and discussed (in the subsection “Cellular contributions to wing area changes” and in the Discussion), i.e. there is probably no growth (Figure 3D-E).

10) It is surprising to see how similar tissue tension is in the wild type and Dumpy mutant tissue, as measured by both the isotropic and anisotropic components of wound opening following a cut. This suggests that the tissue is able to re-establish the force balance when uncoupled from the cuticle.

This is surprising and should be discussed more fully in the text (subsection headed “Dumpy-dependent physical constraints at the margin maintain epithelial tension in EDH the wing”).

Is it correct that cell shape anisotropy is better aligned with tension anisotropy in the mutant as suggested by Figure 2I-I’ and Figure 2–figure supplement 3?

11) There are several striking findings that are not that fully explained in the text in the wild type, cell division is shut down by 22.5h APF. This is not the case in the mutant. Interestingly, this is exactly when the shift in the T1 cell contribution to shear occurs (Figure 8A and B). Is it possible that this is related to DILP8 function? If not, what is it that happens at 22.5h?

12) The biggest behaviour change in the mutant is the increase in the rate of cell extrusion and in area compression. This implies that area compression and extrusion are mechanistically related (i.e. extrusion is driven by compression) and are subject to extrinsic regulation. If this is the case (i.e. if the rate of compression is proportional to rate of extrusion with a delay), this should be made clear. In Figure 3–figure supplement 1F and G and Figure 3–figure supplement 2D-F it appears that extrusion varies most between wildtype animals and perturbations.

Again, this suggests that extrusion is not subject to intrinsic control but is regulated by tissue mechanics, as previously suggested. Division appears largely insensitive to mechanics, despite what is stated in the text (in the last paragraph of the subsection headed “Cellular contributions to wing area changes”). Interestingly, extrusion does not contribute to shear. This may suggest that it is driven by isotropic forces, e.g. isotropic compression. Please discuss (e.g. in the Discussion: “This suggests that cells may measure epithelial tension to communicate with each other and reproducibly control tissue area despite variable contributions of cell division, cell extrusion and cell area).

13) The authors suggest that the precision of the wildtype tissue is greater than that of individual cellular processes. This is a very important point. While the data suggest that this may the case, it would be good to come up with a quantitative measure of precision and variation by which to test this idea with, i.e. compare cell number/cell area/division/extrusion precision/variation with that of tissue area and/or tissue shape precision/variation. Importantly, if there is no growth during the experiment, area precision may simply reflect the absence of cell mass accumulation. If this is the case, it is a trivial result.
