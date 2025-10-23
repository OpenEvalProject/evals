# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University Medical Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23471.039](https://doi.org/10.7554/eLife.23471.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Modeling Hsp70/Hsp40 interaction by multi-scale molecular simulations and co-evolutionary sequence analysis" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arup Chakraborty as the Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, major revisions are required before the manuscript can be considered further. Please note that there is no guarantee for acceptance.

Summary:

Your paper aims to establish an integrative bioinformatic pipeline, bringing together co-evolutionary modeling with molecular simulations based on both coarse-grained and atomistic models. There is considerable discussion in the field as regards to the relevant interface between DnaK/DnaJ and homologous Hsp70/Hsp40 complexes. Crystal structures and NMR experiments have produced conflicting results. The simulations seem to generally support the conclusions drawn from the NMR studies of the DnaK/DnaJ complex. However, there is no further experimental validation of the computational results, and the study currently lacks new insights into the functional roles of the J protein/Hsp70 interaction. One reviewer commented that she/he could not reproduce the co-evolutionary analyses (although we do not have the MSA). Many other technical points noted below need to be addressed.

Essential revisions:

1) While we find the molecular simulation part very convincing, we are a bit perplexed, possibly due to lack of clarity in the manuscript, about the co-evolutionary analysis. In particular we failed to reproduce some of the results presented. Lacking the multiple sequence alignment (MSA) of the two protein families, we are not sure that we followed the same pipeline as you did. The MSA must be deposited and the pipeline used clearly described. Also, please provide more information about the alignments of the two proteins. How many species are included? What is the statistics of paralogs? How many species with unique copies of both proteins exist in the alignment (how are they correctly matched)? Are there cases of proteins coded in operons or of certified interaction which can be imposed in the matching? You cite Malinverni et al., 2015 for how the MSA was obtained, but this reference does not provide sufficient detail.

2) When you note: "We built two separate seeds containing Hsp70 and Hsp40 sequences, covering a broad portion of the tree of life" did you include sequences other than those for Prokaryotes? If you did so, how could you justify this inclusion as it well known, and also acknowledged by you in the fifth paragraph of the Introduction, that the Bacterial system seems to be incompatible with the Eukaryotic one?

3) Apart from the seed, it is also not clear if eventually non-bacterial sequences were removed from the final MSA. If you did not do so, it would be very important to present the same analysis only on bacterial sequences and discuss differences in the inference (if any).

On a related note, it would be interesting to verify your claim that the statistics over repeated random matchings is informative, by applying your method to PPI treated in past work where the operon-based matching is known. This will provide insights into the generalizability of the approach to other protein systems lacking operons. The same problem has been recently addressed by two papers by Bitbol et al. and by Gueudre et al. in PNAS (2016). Both propose rather involved matching schemes. Would the application of your methods improve the results? In case these papers provide their codes, this would be an easy analysis to be added. The paper has applied the selection criteria of Hopf et al., 2014 with a cutoff of 0.8. The quantity subject to this cutoff is not mentioned. Why should the cutoff established for operonic matchings be applicable to random matchings? We are rather surprised (positively) that a random matching produces similarly strong signal.

4) The method used to match the two protein families is interesting but recently two other methods have been published tackling the issue of concatenating MSAs with a new computational approach: Thomas Gueudré et al. "Simultaneous identification of specifically interacting paralogs and interprotein contacts by direct coupling analysis", vol. 113 no. 43, 12186-12191, doi:10.1073/pnas.1607570113, Published online before print October 11, 2016. Anne-Florence Bitbol, Robert S. Dwyer, Lucy J. Colwell, and Ned S. Wingreen Inferring interaction partners from protein sequences PNAS 2016 113 (43) 12180-12185; published ahead of print September 23, 2016, doi:10.1073/pnas.1606762113. We encourage you to try one or both of the methods mentioned to verify the robustness of the random matching.

5) Together with the selection criterion introduced in Hopf et al., 2014, it could be interesting to show in general a histogram across the 1000 stochastically concatenated MSAs of the original residue-residue score (Ekeberg, Hartonen and Aurell, 2014) in order to figure out whether the score is doing more than largely producing top-scoring pairs. Similarly, how many protein pairs typically have a score larger than 0.8?

6) The long all-atom MD runs are only performed for the HPD-IN conformation. Would runs on the HPD-OUT conformation confirm the preference for the IN conformation over the OUT conformation?

7) A critically important overarching question is what have we learned from this study that was not known previously? The interaction site on DnaK is not unexpected, the region on the J-domain, especially the HPD, was known to be key to this interaction, and the dynamic nature of the complex was expected. Thus, the work, while laudable, in its current form, does not move the field significantly forward. You need to attempt to address some of the functional underlying questions: how do J-proteins modulate Hsp70s to affect their allosteric cycle? What is the role of the diversity of J-proteins and how involved is the SBD?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Modeling Hsp70/Hsp40 interaction by multi-scale molecular simulations and co-evolutionary sequence analysis" for further consideration at eLife. Your revised article has been favorably evaluated by Arup Chakraborty (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) In previous literature (namely Feinauer et al., 2016; Gueudré et al., 2016), an empirical coevolutionary score for protein pairs was introduced: starting from the Average Product Corrected (APC) inter-protein residue pair score (i.e. the restriction of the APC coupling score to all pair of residues i, j for which i belongs to one protein and j to the second one), and consider the mean over the 4 largest. It would be extremely interesting to show this score for the random matching strategy and also for PPM and IPA to compare the "strength" the DnaJ/DnaK coupling in comparison with other known protein pairs presented in literature.

2) While it becomes clear from the manuscript and from the authors reply that the central interest is in the Hsp70/Hsp40 system and not in the development of a general-purpose methodology, two results reported in the rebuttal letter but not in the manuscript or its supplement should be reported in the supplement, with a short reference from the new last paragraph of the subsection “3. Random Paralog matching”:

The random matching procedure is successful even if applied to the two component system used in Bitbol et al., 2016 and Gueudré et al., 2016.

The matching procedure of Bitbol et al., 2016 and Gueudré et al., 2016 produces strongly overlapping results with the random-matching procedure.

3) A minor remark concerns the results of the 3701 always matched protein pairs, where both sequences are single copy in their genomes. It is interesting that this case recovers part of the strongest signal, but the sampling of random matchings is able to enhance the coevolutionary signal beyond the one found for the uniquely matched pairs. Again, this is a nice detail, it might be introduced at the beginning of the Methods section on random matching, or at the end of Sec. II.B. “Coevolutionary Analysis predicts conserved DnaK-DnaJ contacts”.

4) HMMer should be cited in the first paragraph of the subsection “1. Sequence Extraction and Preprocessing”.
