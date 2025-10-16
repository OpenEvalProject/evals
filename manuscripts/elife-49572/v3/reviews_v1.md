# Peer review - Round 1

Editors:
- Baron Chanda, University of Wisconsin–Madison United States

Reviewers:
- Rachelle Gaudet, Harvard University United States
- Youxing Jiang, University of Texas Southwestern Medical Center United States

## Review text

DOI: [10.7554/eLife.49572.041](https://doi.org/10.7554/eLife.49572.041)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Acceptance summary:

The manuscript by Hughes and colleagues describes the identification of inhibitors of the TRPV5 ion channel using a structure-based virtual screen as a starting point to identify a set of molecules to screen in functional assays. This resulted in the identification of new potent inhibitors of TRPV5, including one that is specific for TRPV5 (when compared to the highly similar TRPV6, and several additional TRP channels). The authors also determine new structures of TRPV5 with these inhibitors (ZINC17988990) and localize a novel binding site in S1-S4. Functional studies show that mutations at this binding site dramatically reduce inhibition by ZINC17988990. Together, these studies identify a new druggable site of TRPV5 channel.

Decision letter after peer review:

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Structure-based discovery of novel TRPV5 inhibitors" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Rachelle Gaudet (Reviewer #2); Youxing Jiang (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Your study describes the discovery and structural characterization of a novel drug binding site on the TRPV5 channels. As you see will see below the reviewers have some concerns about the cryo-EM studies but are mainly concerned about the functional aspects of this study which does not rule out alternate mechanisms. The second major concern is that the study if anything demonstrates in silico screening does a poor job predicting the drug binding site although in your case the compound acts as an inhibitor in functional studies.

As a part of feedback to the authors, I am also appending some of the comments that were made during our discussion.

1) Where I do worry is with the M491A functional data. That is a region where we know in other TRPs we can find gating mutations. And they don't look at the effect of this mutation on other stimuli. Combined with the unconvincing density for the S4-S5 linker site, and the fact that as modeled, there are few contacts with protein, I'm not convinced that this is a real site.

2) I do think that they could/should focus the manuscript more on the positive results (especially the compound that binds to the S1-S4 domain). It would also be good to know what happens if they try to dock the econazole in the same pocket.

Reviewer #1:

This manuscript by Hughes et al. described the results of an in silico screen to find compounds in a library that would interact with the econozole binding site of TRPV5. They characterized one lead compound and one derivative of this compound for inhibitory effects on TRPV5 and TRPV6. The lead compound had μM affinity for both TRPV5 and TRPV6 and the derivative had subμM affinity for TRPV5 with no inhibition of TRPV6. CryoEM studies of TRPV5 bound to both compounds revealed binding sites for both compounds that did not overlap with the econozole binding site, demonstrating that the structure-based virtual screening was not ultimately useful.

The CryoEM studies, although not definitive, seem likely to have identified binding sites for the two compounds studied. This is a strength of the manuscript. Unfortunately, the functional studies do not directly address whether the identified binding sites indeed are functionally relevant nor the mechanism by which they inhibit activation. Mutations that shift the apparent affinity for a ligand need not be within the ligand binding site. An extreme example of this phenomenon is the voltage-sensing domain of voltage-gated ion channels; mutations throughout the sequence, even outside the membrane's electric field, shift the voltage dependence of activation. The authors need to show that mutations have no effects on the ligand-free gating of the channels and that they specifically affect regulation by ligands that act within these particular binding sites and not others. As it stands, the mutagenesis studies provide no mechanistic insight into the inhibitory effects of the compounds nor on the selectivity of the derivative compound.

Reviewer #2:

The manuscript by Hughes and colleagues describes the identification of inhibitors of the TRPV5 ion channel using a structure-based virtual screen as a starting point to identify a set of molecules to screen in functional assays. This resulted in the identification of new inhibitors of TRPV5, including one that is specific for TRPV5 (when compared to the highly similar TRPV6, and several additional TRP channels). The authors also determine new structures of TRPV5 and identify some densities that they attributed to the inhibitors, attributions that they support with IC50 measurements of mutant TRPV5 proteins.

In the maps provided, the densities assigned to ZINC17988990: The one in the S1-S4 seems quite strong, comparable to the protein density, and includes two regions that fit the aromatic groups well, with an appropriate distance and orientation so that the chosen pose fits very well. There is no comparable density in the other TRPV5 structures, including those from other groups. It is interesting to note this site partially overlaps with density observed in the econazole structure that was attributed to lipid in the NSMB publication.

I find the discovery of the ZINC17988990 compound and its binding site within the TRPV5 S1-S4 region exciting and compelling. Some of the other conclusions, however, are not as strongly supported by the data and analysis.

In particular:

The density for the ligands at the S4-S5 regions are rather weak (the ZINC17988990in particular), essentially gone in 5-σ maps, and weaker than several other unmodeled blobs of comparable or larger size. The modeled ligand poses are also somewhat strangely positioned; they contact very few protein atoms.

None of the modeled lipids are in the provided PDB: the modeled lipids should either not be discussed and illustrated in the figures, or they should be included in the model deposited in the PDB. This is particularly important because the authors also describe a SBVS in which they included these modeled lipids. On that note, the densities attributed to lipids seem much wider that I expect for a linear chain of methylene groups.

One of the densities assigned to lipid in this manuscript is very similar, and in the same position, to the density assigned to econazole in the NSMB publication. Can the authors comment on this somewhere in this paper?

The discussion on structural differences in subsection “Insights into the mechanism of TRPV5 inhibition by novel exogenous compounds” and the related figures (Figure 7 and Figure 8, and Supplementary figure 16 and Figure 5) are difficult to follow and evaluate, because the authors do not describe how they performed the superpositions of the different structures. The movements should instead be described as relative to otherwise. Also, RMSD values should include units (typically Å) and basis (Cα carbons, all atoms, which region of the protein, etc.?).

Discussion of the S2-S3 linker and the difference between TRPV5 and TRPV6: (and Figure 5—figure supplement 2) if there is no sequence difference between the two channels in that linker, then there should be some other sequence (or structure) difference somewhere else that explains why this linker is disordered in TRPV6 but ordered in TRPV5. Can the authors provide some hypothesis to that effect?

The ZINC91555420-bound structure is derived from such a small number of particles (~22,000) in comparison to the starting point (>500,000). Do the authors have any idea why that is the case? Are there potentially other structures represented in the other particles? Are there other classes identified?

Subsection “In silico compound screening”: the authors mention that no compound with similarities to econazole was identified in the screen. Did the library contain econazole itself? If the authors dock econazole, how does it score in comparison to the top compounds identified in the screen?

Subsection “Functional validation of compound hits”: the authors should introduce the "monovalent currents through TRPV5" – at least reference previous work that uses similar assays.

Along the same lines: Why didn't the authors look for activation (rather than only potentiation)? With the protocol the authors used, is the open probability of TRPV5 known (i.e. to what extent is that signal "potentiatable")?

It would be useful to also test the activation of other TRPs (beside TRPV5 and TRPV6) with ZINC9155420: the authors find that it is not selective between TRPV5 and TRPV6, and that raises the interesting question of whether this compound can also activate other TRPVs, and/or other TRPs (How broad or narrow is the selectivity?).

Could the authors test the combination of D406A and M491A and how this affects inhibition by ZINC17988990?

Related: it would be useful to have Supplementary figure 14 part of one of the main figures instead. And what about Y415F with ZINC9155420? It should not be assumed that Y415F would have less of an effect (if any) on inhibition by ZINC9155420 because its effect of this on inhibition by ZINC17988990 was less than that of D409A. That is not a given considering the chemical differences between the two inhibitor molecules.

Reviewer #3:

In this study, Hughes et al. performed a structure-based virtual screening (SBVS) of a large compound library focusing on a previously identified TRPV5 inhibitor (econazole) binding pocket. They identified two novel inhibitors of TRPV5, one of which is specific for TRPV5. They also define the binding sites of both inhibitors by determining the structures of TRPV5 in complex with each inhibitor using single particle cryo-EM. Since the exact position/orientation of the bound compounds as well as the interacting residues cannot be properly defined from the structures due to the resolution limit, the authors validated the binding sites by mutagenesis. Structural comparison between the inhibitor-bound closed TRPV5 and the PI(4,5)P2-bound open TRPV5 also provide structural insights into the allosteric inhibition of TRPV5 by these two inhibitors. This is a solid study with a large amount of structural and functional data. I have a few minor concerns.

1) If I understand correctly, the structure-based virtual screening (SBVS) was performed focusing on the previously identified econazole-binding pocket of TRPV5. However, the compounds identified from this screening actually do not bind to the predicted region. I am not sure if this can be considered as a successful example of an in silico screen as the actual binding site is different from the predicted/targeted binding site.

2) The binding sites for both compounds appear to be more accessible from the cytosolic side of the channel, particularly the TRPV5-specific ZINC17988990 that binds at the S1-S4 pocket. Should the authors use inside-out patch for recording in order to have a faster response of inhibition as well as a better/more accurate measurement of the IC50? Related to this, some compounds that have been tested that show no effect could be due to the compounds' inability to cross the membrane.

3) Figure 4B shows multiple nearby residues at the ZINC9155420-binding site but the authors only show the mutation of M491. I wonder if they have also tested other residues within this binding pocket.
