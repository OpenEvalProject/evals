# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22889.033](https://doi.org/10.7554/eLife.22889.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Probing protein flexibility reveals a mechanism for selective promiscuity" for consideration by eLife. Your article has been favorably evaluated by John Kuriyan (Senior Editor) and three reviewers, one of whom, Nir Ben-Tal (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Nikolay V Dokholyan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted the following remarks to elicit a response from you. Please consider the serious concerns in comments 1 and 2 below and respond with a plan of how you may be able to address these points by further theory or experiment, and indicate an approximate time from for the completion of such work. The editor and reviewers will evaluate your response and issue a binding recommendation.

Review:

The manuscript describes computational analyses of the ligand-responsiveness of the PD-1 immune checkpoint inhibitor. In spite of the availability of a crystal structure of bound PD-1, and NMR structures of the unbound (apo) protein, it is not understood how the receptor is able to bind more than one ligand with different binding modes but with specificity. The manuscript examines two possible pathways for ligand binding: conformational selection vs. induced fit. The binding dynamics is investigated using all-atom molecular dynamic simulations, where known NMR and co-crystal structures are used as the initial models for bound and unbound conformations. Various ligand-mimicking peptides are used to study the role of specific contacts between the protein and the ligand side chains. The conclusion is that binding follows the induced fit mechanism, which starts from the burying of the anchor motif of the ligand and follows by chronological sequence of pocket rearrangement in order to form and increase hydrophobic areas and form hydrogen bonds important for binding. The interesting aspect of this paper is the proposition that the initial docking of one or the other ligand triggers different conformational changes in the receptor that then ensures the appropriate specificity.

Given the enormous prominence of the checkpoint inhibitors as newly emerging treatments for a wide range of cancers, and in particular the efficacy of reagents capable of directing blockade of PD-1 associated processes, this report is potentially of wide spread interest and importance. Nevertheless, the reviewers and the editors have some serious reservations about the robustness of the results, and how general the principles are. We would like to give you the opportunity to revise the manuscript in order to address these reservations. You should note that these reservations are such that if they are not addressed adequately in the revision, then the paper may be deemed unsuitable for eLife. We note three essential points to address below. The first two refer to the most serious concerns, and will require additional computation, or perhaps even experiments. The third point is also essential, but we feel that you should be able to address it by revising the figures and accompanying text.

Essential issues to address:

1) While the computational results provide fertile ground for considering the detailed mechanisms underlying PD-L1 and PD-L2 recognition and potentially affinities, there are no prospective experimental studies to challenge and validate these interesting hypotheses. The lack of experimental support is further highlighted in the section describing the binding of a relatively high affinity (Kd ~1 nM) macrocycle developed by BMS. The PD-1 recognition surface assumed for this macrocycle is based on its sequence similarity with PD-L1, which is a reasonable hypothesis; however, there is no direct experimental support for this assumption in the current manuscript or anywhere in the literature. The reviewers are concerned that in its present form the paper does not present a reliable set of conclusions.

We recognize that your paper presents the results of a computational study, and that it may not be feasible for you to provide experimental data to support your concepts. In that case, please consider alternative ways to establish the robustness of your results.

For example, does PD-1 have more ligands beyond PD-L1 and PD-L2? "These three linear ligand motifs (XDY), shared by both PD-L1/2, comprise the molecular key[…]": Are there counter examples? That is, peptides that do not share the motif and were proved in experiments to not bind PD-1? If so, simulations with such negative controls should be added.

Other proteins in addition to PD-1 could be studied to examine how general the mechanism is.

2) Y123/112. Several tripeptides were used to examine the importance of this residue but these are just a small portion of the possible sample. How about other aromatic residues? Or HIS? Or other residues that could potentially support a hydrogen bond equivalent of OH_eta?

3) The illustrations in the paper need to be improved.

A diagram showing the intact receptor should be shown to provide context for the ligand interaction. In most figures the protein is shown using its molecular surface, without revealing the physicochemical nature and/or residues types underlying the surface. Thus, it is difficult to examine the fit of peptide binding. This is crucial since one of the main observations here is that the binding site shifts its polar nature upon binding. The current figures do not explain this clearly.

In Figure 2C it might be useful to zoom out a bit and show more of the binding pocket, so a reader can understand open/close residues orientation with respect to the pocket.

It might be useful to include the structures of the ligands themselves in Figure 3 for the comparison of mimicking motifs.

More information concerning the fractional overlap of atoms (Figure 4(D, E)) would be useful.

Other points to address:

1) "Interestingly, no small molecular weight inhibitor has been reported for this seemingly druggable interface cavity. This is likely due to our incomplete understanding of how PD-1's flexibility enables selectivity for two distinct ligand interfaces, only one of which stabilizes the hydrophobic pocket": Speculative. Perhaps nobody tried to target this interface? A reference should be added or the statement should be revised.

2) "PD-1 has proven to be a difficult target to disrupt using small molecules": A reference should be added or the statement should be deleted.

3) Figure 3D. Should be GGY rather than GGG.

4) Overall, there are far too many abbreviations in this paper, and we ask that you use only the most essential abbreviations, and keep these to a minimum. In the current form, the paper is challenging to read. Why abbreviate molecular dynamics simulations as "MDS"? Why use "PPI" as an abbreviation? Please consider the ease with which a reader can follow what you are trying to say.
