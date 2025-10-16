# Peer review - Round 1

Editors:
- Jie Xiao, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76870.sa0](https://doi.org/10.7554/eLife.76870.sa0)

This work develops a new method to probe protein–protein interactions using proximity-assisted photo activation, in which a receiver fluorophore (longer wavelength) can be photoactivated by the excitation of a nearby sender fluorophore (shorter wavelength). This new method is validated through in-depth characterization, comparison with FRET, and application to known systems of protein–protein interactions. It will expand the tool kit for probing protein–protein interactions.


---

# Peer review - Round 1

Editors:
- Jie Xiao, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76870.sa1](https://doi.org/10.7554/eLife.76870.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Proximity-assisted photoactivation (PAPA): Detecting molecular interactions in live-cell single-molecule imaging" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: J. Christof M. Gebhardt (Reviewer #2); Helge Ewers (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please provide a side-by-side comparison of PAPA with smFRET for at least one set of experiments conducted in Figures 3, 4, or 5. For example, will the population percentages or diffusion coefficients (bound vs. unbound) detected using the two methods be the same or different? And why?

2) Please address the issue of how one could distinguish PAPA from DR at the level of single-molecule trajectories instead of relying on the statistics of population measurements or PAPA/RA ratios. This characterization could be done by using in vitro single-molecule imaging where the probability of PAPA and DR on the same molecule could be quantified.

3) Please provide a comparison either experimentally or textually of how PAPA detects protein-protein interactions in comparison with BiFC and other commonly used protein FRET sensors.

Reviewer #1 (Recommendations for the authors):

As the new method, PAPA basically benchmarks smFRET in the detection of molecular interactions in live cells, my comments and questions are mainly related to the advantage of PAPA over smFRET.

1. In the introduction, the authors comment that smFRET has proven technically challenging in cells due to the requirement for sparse double-labeling, the large size of genetically encoded tags relative to the working distance of FRET, and the brief observation time (tens of milliseconds) for fast-diffusing complexes. Regarding the requirement for sparse double-labeling, the authors propose that in PAPA, one interacting partner can be sparsely labeled with the receiver and the other densely labeled with the sender, permitting efficient detection of double-labeled complexes. While such labeling strategy can circumvent the tradeoff between labeling density and spectral crosstalk inherent in smFRET, it would increase the unspecific photoactivation in PAPA.

2. PAPA can operate at a longer average intermolecular distance than FRET (Figure 2). While such property may be used to decrease the potential interference from the fusion tag by elongating the linkers between Halo/SNAPf and the protein of interest, it could increase the unspecific photoactivation in PAPA.

3. Regarding "the brief observation time (tens of milliseconds) for fast-diffusing complexes" for smFRET, I think the authors need more characterization to demonstrate the advantage of PAPA in single-molecule measurements. Exploring the capacity of PAPA in detecting single molecules would make this work much more valuable: "Most proteins function by interacting with other proteins, yet we lack tools to study these potentially transient interactions at single-molecule resolution in live cells." Characterization of single-molecule detection may be conducted in vitro. In proof-of-concept experiments, PAPA detected the expected correlation between androgen receptor self-association and chromatin binding at the single-cell level. Single-molecule application could be conducted on nuclear pore complexes.

4. Overall, it is important to perform a direct comparison between PAPA and smFRET in protein-protein interaction measurements, including SMT, sub-population, and interaction dynamics. Actually, as PAPA is based on JF549 and JFX650, this pair of dyes not only be used as "sender" fluorophore and "receiver" fluorophore in PAPA but also be can be used as donor and receptor in smFRET at the same time. Therefore, besides detecting the ratio of green to violet reactivation, FRET signal could be also measured for experiments in Figures 3, 4, and 5, and such comparison is important for reinforcing the advantage of PAPA over smFRET in detecting dynamic protein-protein interactions in live cells, also essential for comparing unspecific activation in PAPA and crosstalk in smFRET.

5. Regarding the physical mechanism underlying PAPA, the authors propose a hypothesis that the excited sender reacts with some other molecule in the cell, producing a short-lived chemical species that diffuses a limited distance to react with and reactivate the receiver dark state. In Supplementary Figure 9, the authors showed that when JFX650-labeled cells were bathed in high concentrations of free JF549 dye, reactivation by green light occurred in proportion to the JF549 concentration. The activation dependence on the concentration of free senders might support the free radical hypotheses.

6. Lastly, as smBiFC is also an important approach for detecting single-molecule protein-protein interaction in live cells, it is necessary to include a few words in the introduction.

Reviewer #2 (Recommendations for the authors):

This is a valuable new method to assess protein-protein interactions in live cells. The paper is easy to read and experiments are performed and described comprehensively.

Methods based on split labels are able to provide comparable single-molecule insight into protein-protein interactions, for example, published in Makhija et al., ACS Chem. Biol, 2021 (https://doi.org/10.1021/acschembio.0c00925) and in particular Shao et al., Communications Biology, 2021 (https://doi.org/10.1038/s42003-021-01896-7).

Please compare PAPA to these methods and detail advantages and disadvantages of each method.

Reviewer #3 (Recommendations for the authors):

One straightforward experiment that would greatly improve this manuscript: Create and label transmembrane protein-Halo vs transmembrane protein Halo-SNAPf and then I would like to see dual-color video of the single molecules moving in both channels after DR and PAPA, respectively. And a direct quantification of how many molecules are detected in DR ad PAPA. It is a little strange to see a single molecule fluorescence manuscript without any hint of what the data look like.
