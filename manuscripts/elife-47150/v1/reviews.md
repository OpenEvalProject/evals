# Peer review - Round 1

Editors:
- Lucy Forrest, National Institute of Neurological Disorders and Stroke United States

Reviewers:
- Baruch Kanner, Hebrew Univ of Jerusalem Israel

## Review text

DOI: [10.7554/eLife.47150.028](https://doi.org/10.7554/eLife.47150.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Identification of an allosteric binding site on the Glycine Transporter, GlyT2, for bioactive lipid analgesics" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Baruch Kanner (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Mostyn et al., describes the characterization of a novel allosteric binding site in a glycine transporter, GlyT2, targeted by bioactive lipid analgesics, using biochemistry, electrophysiology, homology modeling, docking and molecular dynamics simulations. Previous studies had identified a region of the protein, extracellular loop 4, that was responsible for specificity of endogeonous lipid to GlyT2 compared to GlyT1, and had developed a class of bioactive lipid inhibitors based thereon. This study uses this information as a starting-point for docking and simulations to a homology model of GlyT2 (based on the Drosophila dopamine transporter, dDAT), and tests those predictions experimentally. The results provide opportunities for the synthesis of novel drugs for pain treatment. Furthermore, this work could be exploited to modulate the activity of other related neurotransmitter transporters in related allosteric sites.

Essential revisions:

1) A key conclusion of this study is that the inhibitors do not bind the known allosteric site used by citalopram. However, the authors did not perform any site-directed mutagenesis analysis on the citalopram binding site similar to that performed on the newly discovered site. Such analysis would help rule out binding to the other allosteric site.

2) An additional concern relates to the conformational changes of the ligands, which are elongated lipids with several rotatable bonds, posing a significant challenge to docking. These ligands move deeper into the pocket during molecular dynamics simulations, raising the possibility that the docking was not sufficiently robust. For example, the results might differ if a larger box were included. Therefore, important details regarding the docking analysis and careful analysis of the predicted mode of binding must be provided to support the conclusions. How were the binding site boundary identified? How were the ligands prepared for docking? How was the docking pose selected (i.e. was it the top scoring pose)? Were the top-scoring docking poses similar to each other? Using another docking method (such as a flexible docking algorithm) is an optional additional strategy that would provide alternative solutions and further support the relevance of these results.

3) The authors performed MD simulations on a single ligand-docked model. How much would the ligand insertions observed during the simulations depend on the initial conformation of the predicted complex? As described in point (2), there should have been several possible docking solutions, and each may have resulted in a different conformation after the MD simulations. Therefore, similar analysis should be carried out for more than one docking solution to see whether the final poses converge. Repeats of the MD simulations (n>=3) would also establish robustness and reproducibility. In particular, interpretations of differences between compounds should not be based on the outcome of a single trajectory (e.g. Figure 3).

4) Another concern is the potential unreliability of calculations based on a homology model in an apo conformation, i.e. without ions or a ligand in the central pocket, which is potentially unstable during MD. Completely ligand-free structures of e.g. LeuT have been shown to adopt a similar overall occluded conformation, but only after Leu99 has rotated and inserted into the central pocket. Please provide further evidence for the robustness of this choice with more detailed analysis of the stability of the system (such as RMSDs during MD) and provide some discussion of the choice. The simulation repeats mentioned in (3) should help.

5) To further establish the confidence of each predicted simulation result, please provide better quantitation of computed docking interactions, and/or visualizations that indicate the variability/spread of the results during a trajectory (e.g., using density/occupancy maps).

6) The phrase "experimentally validated", used to describe the homology model, is too vague. Some description of how the homology model was validated or why the model is accurate enough for this work is required. This should include the sequence identity of the model to the template and the corresponding expected accuracy, as well as the overall level of conservation in EL4 between the target and template.

7) The first item of the Results section (Figure 1A) shows the inhibition of glycine transport by OLCarn (the name of this compound should be given also in the Legend) in several mutants. The rationale for selecting these mutants is not clear. Several of the residues chosen are identical in GlyT2 and GlyT1, which is not sensitive to the biolipids. Moreover, it is not explained what the reason is for selecting the substitutions. For example, why is Pro-561 mutated to Ser out of 19 possible substitutions? To help clarify the choice of mutations, it might make more sense to show simulation data first and base the selection of mutations on this information. Alternatively, the authors could first analyze those residues which differ between the two GlyT's, such as the important GlyT2-I545L mutant.

8) The authors mention they identified a binding pocket unique to GlyT2 vs GlyT1, but the description is vague. A figure with explanation would help. In addition, Ile-545 of GlyT2 is a major determinant for the selectivity of the biolipids and there are steric implications when it is replaced by Leu, as in GlyT1. It would be important to put Figure 2A and B side-by side with Supplmentary Figure 8A and B and enhance visualization using, for example, stick representations.

9) The authors deduce a mechanism of OLSer binding from the docking and MD simulations (Discussion section), speculating that the "Bioactive lipids may therefore navigate the aqueous solution or interact with the cell membrane before inserting into the allosteric site, tail first". This proposed mechanism is too speculative to be included in the Discussion section, as these movements likely resulted from initial incorrect docking poses. Please revise or remove.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Identification of an allosteric binding site on the human Glycine Transporter, GlyT2, for bioactive lipid analgesics" for further consideration at eLife. Your revised article has been favorably evaluated by Richard Aldrich (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues (or new ones that arose due to the inclusion of new data) that need to be addressed before acceptance, as outlined below:

- In subsection “Computational analysis of the proposed GlyT2 binding site”, it is stated that the initial docked position of the inhibitors is not maintained in a number of cases. Please provide evidence and quantitation for these data. Along the same lines, in subsection “Acyl-amino acid docking and molecular dynamics system setup”, it is stated that the poses were "categorized based on their general orientations and one pose was simulated". Was this by clustering or by manual inspection? Please be transparent, and quantitative where possible.

- We recommend computing the distance of the tail end to a set of points at the bottom of the cavity as a means to quantify the insertion of the lipids.
