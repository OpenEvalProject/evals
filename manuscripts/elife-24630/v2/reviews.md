# Peer review - Round 1

Editors:
- Baron Chanda, University of Wisconsin-Madison , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.24630.014](https://doi.org/10.7554/eLife.24630.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A selectivity filter at the intracellular end of the acid-sensing ion channel pore" for consideration by eLife. Your article has been favorably evaluated by Richard Aldrich (Senior Editor) and three reviewers, one of whom, Baron Chanda (Reviewer #3), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Lynagh et al. seek to explain the structural basis for the Na+ versus K+ selectivity of ASIC channels, by combining electrophysiological, unnatural amino acid mutagenesis with molecular simulations of ion selectivity. The outcome is an innovative and compelling study, which concludes that the 10-fold Na+ selectivity of this channel is not determined by the so-called 'G-A-S belt', as previously proposed. Instead, a set of acidic residues at the intracellular side of the pore, and regions near Leu7/Leu14, are found to be influential. The study illustrates that even though from a structural standpoint, the ions are likely to interact intimately with the protein at the constriction formed by the "G-A-S belt", the actual selectivity is due to residues at the vestibule. The reviewers agree that this is an important contribution to the field but have raised some concerns, which should be addressed in the revised version.

Essential revisions:

1) The Lennard-Jones parameters for K+ and Na+ used in the calculations are said to be those that optimize the representation of the cation-carbonyl interactions (subsection “System construction and molecular dynamics simulation”, third paragraph), in the context of the CHARMM22 force field. I deduce, therefore, that the authors have not considered subsequent improvements focused on the representation of cation-carboxyl interactions. These interactions were found to be too strong in standard CHARMM22, and to a greater degree for Na+ than K+ (see e.g. Luo & Roux, JPC Lett 2010; or Marinelli et al., PNAS 2014). Therefore, I believe it is pertinent to question whether free-energy profiles and DDG values calculated with a 'corrected' set of LJ parameters would be significantly different from those currently presented, and if so, whether they would alter the current conclusions of the theoretical study. For example, does the shape of the free-energy profiles in Figure 2B change? One might expect the profile would be shallower around E18/D21. Does the contribution of the constriction near L7, where the Na+/K+ selectivity is said to result from different carbonyl interactions and degree of dehydration, become more prominent, relative to that from the E18/D21?

I should note that the authors do not need to carry out any additional simulations to address this question – the task simply requires that they re-calculate the various probability distributions and ensemble averages involved in the derivation of the analysis currently presented, after introducing a 'weight' for each of the snapshots sampled in the existing MD trajectories. This weight is an exponential factor of the change in potential energy resulting from the modification of the force-field. It should be therefore very feasible to provide alternative plots to those shown in Figure 2BC and Figure 3BC, an alternative DDG values to those currently mentioned in the text – which I believe result from the calculations summarized in Figure 2—figure supplement 1B-E.

2) The authors focus their more detailed experimental and computational analyses on acidic residues on the intracellular side of the pore (E18, D18), and highlight these in the title and Abstract of the article. However, the data presented seems to show that the region near L7 is as influential. For example, according to Figure 4A, the L7A mutation makes the pore (slightly) K+ selective – consistent with this result, the existing free-energy profile in Figure 2A also shows that the L7 region is as important, if not more. If the new calculations with the 'corrected' forcefield parameters mentioned above confirm that the selectivity of the L7 site is similar, or more prominent, than that of the site near E18/D21, it would be necessary to examine the L7 site further, ideally through the same kind of experimental data as that presented in Figure 4D, for the acidic region; that is, do the L7A mutations have a progressive effect on the selectivity, like the E18Q mutations? Free-energy perturbation simulations for this site would also be required to rationalize the experimental result, particularly if single, double and triple mutations indeed have a distinct effect, as seen for the site near E18/D21.

3) Simulations that are consistent with the contribution of the side chains of E18' in determining Na/K selectivity were based on the structure of a non-conducting channel. What is the relevance of such simulations for the active open ASIC1?

4) Since the simulations based on the open chick ASIC1 cannot predict the role of E18 on ion selectivity, a logical consequence is that this crystal structure of the cASIC1/toxin complex does not represent the open conformation of the functional channel; this needs to be discussed.

5) What is the contribution of L14' in setting Na/K selectivity? This should be discussed.

6) Obviously other factors than the highly conserved E18 and D20 play a role in channel ion selectivity among the members of the ENaC/degenerins family, as suggested by ENaC that is highly selective (Na/K selectivity >100). This needs to be discussed.

7) Unnatural amino acid replacement is not perfect because it has been reported that under certain conditions, there is non-specific incorporation (Pless et al. (2014) JGP). Please provide appropriate controls to establish that there is no non-specific at the sites tested in this study.
