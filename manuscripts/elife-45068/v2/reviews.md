# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- Nir Ben-Tal, Tel Aviv University Israel
- Luke O´Neill

## Review text

DOI: [10.7554/eLife.45068.041](https://doi.org/10.7554/eLife.45068.041)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Functional cross-talk between allosteric effects of activating and inhibiting ligands underlies PKM2 regulation" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Nir Ben-Tal as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Marletta as the Senior Editor. The following individual involved in review of your submission has also agreed to reveal his identity: Luke O´Neill (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Experiments and computations are used to study the allosteric cross-talk between two ligand binding, FBP and Phe, on the activity of PKM2 (the glycolytic enzyme pyruvate kinase M2). FPB is an activating allosteric ligand, while Phe binding prevents maximal activation of the FBP bound PKM2.

In the first part of the manuscript the authors describe the simultaneous binding of multiple ligands to PKM2 in different cell lines and their influence on PKM2 activity. Particularly they measure the affinity of PKM2 for FBP, Phe and Ser in vitro, showing that the fractional saturation of PKM2 with FBP is close to 1 in all conditions while the fraction saturation of Phe and Ser are partial and dependent on the conditions. Thus, the activity of PKM2 is not regulated by FBP but by the amino acids. For example they show that Ser results in a decrease of the Km of PEP and an increased enzymatic activity, whereas Phe increases the Km for PEP and decreased the enzymatic activity. They next show that FBP drives PKM2 to be a tetramer, and that Phe enhances FBP-induced tetramerisation, indicating a functional synergism between the two allosteric ligands, with Phe inhibiting FBP-bound PKM2 without causing PKM2 tetramer dissociation. This second part is done with purified proteins. To understand the molecular basis of FBP-induced PKM2 allostery they conduct molecular dynamics simulations. For this they developed the AlloHubMat method to predict allosteric hub fragments from the network of dynamic correlated motions. From here they identify mutants that disrupt FBP-induced activation of PKM2 or its sensitivity to Phe. They produce and purify 7 such mutants and evaluate their activity. Indeed, they show that these mutants introduced various effects on PKM2 (as predicted by the simulation). For example, they show that residues A327 and C358 have a role in coupling the allosteric effect of Phe with that of FBP. Conversely, K305Q and F307P result in decrease in the intensity of tetramer and dimer peaks for PKM2.

Opinion:

It is an interesting problem, and the manuscript presents extensive experimental and also computational work to study the allostery between these two ligand-binding sites and the active site. Major revisions are needed to address the issues listed below.

Essential revisions:

1) The relation between the first part of the manuscript (the in cell measurements) and the other parts (MD simulations, oligomerization state and mutant analysis) is not clear. It should be further emphasized and strengthened.

2) The data on PKM2 oligomerisation are weak. More extensive cross linking analysis is needed as well as the use of gel filtration to examine the stoichiometry of PKM2, both wild type and mutant forms, to confirm what is being proposed.

3) Although the emphasis is on biochemistry, the authors need to consider other approaches, otherwise the paper will have a more limited audience. Can the authors test the physiological relevance of their findings? This could be done by reconstituting PKM2-deficient cells with some of the mutants and assessing PKM2 function in glycolysis or in its nuclear roles. More information on how the regulation reported here might be relevant to cell proliferation or cytokine production is needed. Such experiments would greatly improve the manuscript.

4) The AlloGHubMat method described is based on the GSATools that some of the authors have developed to explore allosteric communication in proteins (GSATools: analysis of allosteric communication and functional local motions using a structural alphabet", Bioinformatics. 2013;29(16):2053-5). The authors should clarify novelty, if any, compared to the 2013 publication.

5) AlloGGubMAT analysis of replica exchange molecular dynamics simulations suggests 32 allosteric positions, of which the authors identified 7 to experimentally explore. They argue that these are allosteric sites, disseminated from FBP, but it looks like the mutations are mainly around the active site, and one at FBP, which is actually a binding site. The authors should explain why they consider their results to be indicative of allostery.

6) The authors should clearly indicate where the Phe binding site is. (We assume that it binds in the same site as Ser in another PDB structure.)

7) They should also include figures, perhaps also PyMOL sessions or something, to highlight the known binding/active sites and the location of the putative allosteric sites to make it clear that the orthosteric and allosteric sites are separated from each other.

8) The difference between the apo and FBP bound mutual information gives positions within the subunit/monomer. What about inter-subunit cooperativity or intersubunit allosteric ligand cooperativity? The absence of large conformational changes doesn't exclude the inter-subunit dynamics.

9) The manuscript states that apo and holo states are similar and there are no large tertiary or quaternary structure changes, with no evidence of global conformational changes. Is it so? Perhaps there are no large global conformational changes, but it seems that there is a global rearrangement. A simple alignment of the two pdb structures (3bjt and 3bjf) shows some global structural adjustment from the apo to PFB bound states that possibly may come up with some dynamic changes that could involve an allostery among monomers within the tetramer.

10) The reference to the available structures is confusing. 3u2z in the method and 3bjf in the simulation table are referred for the FBP bound structures. Since the crosstalk between Phe and FBP is examined, why shouldn't the Phe bound structure be used? Or at least dock the Phe? (Maybe it was done and we missed it?) And PDB 4b2d, where Ser and FBP are bound, should be referred to, perhaps used. Are there other relevant structures?

11) In the Introduction the authors refer to low affinity T- and high affinity R-state tetramers. However, they don't relate these to the known structures. Maybe, the transition between these two states would also be informative?

12) In the beginning, the manuscript says that it is possible that the allostery has enthalpic motion: "we found no significant difference in the time-dependent configurational entropy of the PKM2 apo and PKM2FBP simulated trajectories". However, then it talks about positional entropy? And never get back to enthalpy in discussions. All of these discussions are not that clear. What is the conclusion in terms of enthalpy vs. entropy?
