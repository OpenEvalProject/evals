# Peer review - Round 1

Editors:
- Yogesh K Gupta, https://ror.org/02f6dcw23 The University of Texas Health Science Center at San Antonio United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83928.sa0](https://doi.org/10.7554/eLife.83928.sa0)

In this useful study, the authors utilize state-of-the-art computational methods complemented with some experimental validation to investigate the dynamics of flexible loops of the L1 Metallo-β-lactamase enzyme, resulting in a better understanding of the various conformational states useful for the rational design of superior β-lactamase inhibitors/antibiotics. The evidence supporting the claims is solid, and the work will be of interest to computational, experimental biologists, and drug designers working on antibiotic resistance.


---

# Peer review - Round 1

Editors:
- Yogesh K Gupta, https://ror.org/02f6dcw23 The University of Texas Health Science Center at San Antonio United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83928.sa1](https://doi.org/10.7554/eLife.83928.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Gating interactions steer loop conformational changes in the active site of the L1 metallo β-lactamase" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Volker Dötsch as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Davide Provasi (Reviewer #2).

Essential revisions:

Please address the concerns of three reviewers, which are appended below.

Reviewer #1 (Recommendations for the authors):

1. Authors mention "D150c" in several parts of the paper and in figure labels. Authors should clarify this nomenclature for a broader audience.

2. Figure 2A needs a legend.

3. On line 237, the authors state residue 150 is S, whereas throughout the rest of the paper they discuss it as D150. Please clarify and correct.

4. Lines 303-308 have 39 mentioned in the text -please correct.

5. In the experimental testing step – a larger diversity of residues being tested would enable a broader understanding of the active site. This study would be further enhanced by double mutant variants to enable the authors to understand whether the bond type is important for the active site or if different bond types can exist to stabilize these loops (H-Bonding instead of pi-pi stacking as an example). This enhances the claim of the paper being useful for drug design. Further, there are several amino acids mentioned as being important at the beginning of the manuscript, yet we do not see their trajectories later in the manuscript. These would enhance the authors' claims as well.

6. How were the 22 residues identified and which are they? Understanding this is important for manuscript flow and would improve the narrative of the study. Further, data split results, and reducing input data matrix below 22 residues are all factors that should be tested for the validity of study results.

Reviewer #2 (Recommendations for the authors):

As outlined in the public review, I think that the combination of CVAE and dihedral featurisation is confusing. If sophisticated CVAE embedding is necessary to resolve the relevant dynamical features, then it should be used instead of the dihedrals+tICA to build the MSM. Microstates for the MSM analysis could be easily defined based on k-means clustering of the 14-dimensional CVAE latent space, providing a unified description of the dynamics. If, on the other hand, the dihedral+tICA featurisation is enough to obtain a descriptive and converged model, what is the additional insight offered by the deep learning approach?

Another concern is that presently, all results from the CVAE are analysed and presented after a further projection with tSNE. What is the effect of the compression to 2 dimensions from the original dimensions of the VAE latent space?

The description of the methods is unclear or insufficient on several points:

1) System preparation. The system preparation strategies should be justified better. The authors simulate a homo-tetramer, building the complex from the monomer crystal structure. This choice should be justified, and the result of the tetramer modeling validated. Why should we trust the complex structure if there are no experimental structures of the tetramer?

2) Adaptive Simulations. the adaptive simulation strategy is not described. The authors just mention that "Multiple short Markov State Model (MSM)-based adaptively sampled simulations were run". How? What were the criteria to build the MSM used to re-spawn adaptively the simulations? Was it the same as the one used for the analysis?

3) MSM. It should be made more clear in the methods that the dynamics of each of the four tetrameric units are used by considering the four units to be independent and featuring the dynamics of each unit, and not of the full tetramer. This is a good strategy to increase the available data for kinetic modeling, but it means that no conclusions can be extracted from cooperative effects across subunits. The CK test results should probably be reported as figure supplements.

For the results and discussions section:

1) confidence intervals should be reported for timescales (Figure 2A), mean first-passage times (Figure 2C), probabilities, and free-energies (Figure 2D). Error bars should be reported for the experimental data too (the authors mention triplicate experiments but only report one value per condition).

2) The description of the MSM results can be greatly improved and streamlined. For instance, the description of the structural features of the 7 macrostates (paragraph "The α3-β7 and β12-α5 loops exist in open, intermediate and closed states") should come before the description of the most probable paths connecting the different states. Furthermore, to clarify and facilitate the identification of the structural features of the 7 macrostates, the distributions (or averages and percentiles) of the key distances mentioned in the results (e.g., D150c-R236, H151-Y227), etc. should be reported for each state, similar to what has been done in Figure 3D.

3) "States 3, 5, and 6 are sub-states of the closed conformation, with differences in the conformations of loops joining β-sheets 10 and 11, far away from the active site". It's unclear how the macrostates, which were defined based on features describing only the α3-β7 and β12-α5 loops, could resolve structural features unrelated to these two regions.

Reviewer #3 (Recommendations for the authors):

Although a very thoughtful and detailed MD study, several additional inputs would further strengthen the study. They are described below:

1) Using orthologs, it will be good to provide the percentage of MBLs (e.g., say at 85% sequence identity) that have elongated alpha3-beta7 and beta12-alpha5 types of loops. AlphaFold2 structures of such sequences can further facilitate loop content estimation. This will enhance the relevance of the study, i.e., applicable to not just one (Stenotrophomonas maltophilia MBL L1) but to MBLs of other pathogens. If the percent of MBLs with elongated loops is say < 10%, should this study be carried out? In that case (i.e., if the elongated loops in MBLs are uncommon.), the threat from Stenotrophomonas maltophilia will need to be emphasized further for the significance of the study.

2) As a nonpolar surface patch is responsible for MBL L1 multimerization, can alphafold2 also help in estimating the number of multimeric MBLs that are possible based on the non-polar surface patches of alphafold2 modeled MBL proteins? That is, an estimate of the proportion of expected multimeric MBLs with elongated loops would help enhance the relevance of the study to a wider collection of MBLs.

3) In describing the conformational landscape of the loops, is mutagenesis the right experiment to capture the essence of the interacting loop residues? To illustrate this point, let there be two situations: (a) only one conformation for a loop which is held in place by a salt bridge, (b) two conformations for the loop, (1/3rd time in conformation-i and 2/3rd time in conformation-j) where conformation-i is held in place by the salt bridge. Can mutagenesis of the salt bridge residues distinguish scenario (a) from that of (b)?

4) Alternatively, let us say the following scenarios: (a) only one conformation for a loop (i.e., an open conformation) with no specific interaction, (b) two conformations for the loop (1/3rd time in conformation-i and 2/3rd time in conformation-j) where conformation-i is held in place by the salt bridge. Can mutagenesis of the salt bridge residues distinguish scenario (a) from that of (b)? It is better to describe the scenarios as in (3) or (4) or some others that are being probed and how mutagenesis captures or distinguishes the different scenarios. From Figure 1B, the impression is that scenarios (in (3) above) are likely the case and it is obvious that mutagenesis of the salt bridge residues will have an impact even if the conformational states were not identified by the current study. [In Figure 1, label '(C)' should be in place of label '(B)' in the legend]

5) As the ultimate goal of such a study is to identify better inhibitors, would the following investigation be a better way to utilize the conformational states of the loops? For example, let us say there are 3 loop conformations, i, j, and k that are captured by the enhanced MD sampling and MSM methods. Can each conformation (i.e., i, j, and k) be utilized separately for virtual screening of small molecules (e.g., using Schrodinger such as in ) to demonstrate that searching with each conformation independently (i.e., as three pocket volumes were observed in Figure 3D) provides higher success in the virtual screen than that of the single conformation of the experimental structure?

6) Authors mention specific interactions of the closed state (e.g., salt bridge R236-D150c, pi-pi stacking Y227-H151, and Q310 sidechain-mainchain hydrogen bond). These interactions are lost in the open state. How does the loss of the 3 interaction energies of the closed state get compensated in the open state? What is the population density of each of the open, intermediate, and closed states? Can the difference (i.e., loss or gain) in the energies due to the 3 interactions (R236-D150c, Y227-H151, and Q310) help explain the population densities of each state?

7) The authors mention Y227-H151 pi-pi stacking. The surface-exposed H151 residue can be protonated as well. That is, Y227-H151 could be a cation-pi too. Can the protonation status of H151 further influence the observed outcome?
