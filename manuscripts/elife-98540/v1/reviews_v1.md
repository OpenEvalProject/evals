# Peer review - Round 1

Editors:
- Aaron Frank, Arrakis Therapeutics United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98540.3.sa0](https://doi.org/10.7554/eLife.98540.3.sa0)

This important work substantially advances our understanding of RNA structure analysis by introducing an innovative method that extends DMS probing to include guanosine residues, thereby enhancing our ability to detect complex tertiary interactions. The evidence supporting the conclusions is compelling, with detailed analyses demonstrating the method's capacity to differentiate structural contexts and improve RNA structure predictions. This work will be of broad interest to RNA structural biology, biochemistry, and biophysics researchers.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98540.3.sa1](https://doi.org/10.7554/eLife.98540.3.sa1)

Summary:

DMS-MaP is a sequencing-based method for assessing RNA folding by detecting methyl adducts on unpaired A and C residues created by treatment with dimethylsulfate (DMS). DMS also creates methyl adducts on the N7 position of G, which could be sensitive to tertiary interactions with that atom, but N7-methyl adducts cannot be detected directly by sequencing. In this work, the authors adopt a previously developed method for converting N7-methyl-G to an abasic site to make it detectable by sequencing and then show that the ability of DMS to form an N7-methyl-G adduct is sensitive to RNA structural context. In particular, they look at the G-quadruplex structure motif, which is dense with N7-G interactions, is biologically important, and lacks conclusive methods for in-cell structural analysis.

Strengths:

- The authors clearly show that established methods for detecting N7-methyl-G adducts can be used to detect those adducts from DMS and that the formation of those adducts is sensitive to structural context, particularly G-quadruplexes.

- The authors assess the N7-methyl-G signal through a wide range of useful probing analyses, including standard folding, adduct correlations, mutate-and-map, and single-read clustering.

- The authors show encouraging preliminary results toward the detection of G-quadruplexes in cells using their method. Reliable detection of RNA G-quadruplexes in cells is a major limitation for the field and this result could lead to a significant advance.

- Overall, the work shows convincingly that N7-methyl-G adducts from DMS provide valuable structural information and that established data analyses can be adapted to incorporate the information.

Weaknesses:

- Most of the validation work is done on the spinach aptamer and it and polyUG RNA are the only RNAs tested that have a known 3D structure. Although it is a useful model for validating this method, it does not provide a comprehensive view of what results to expect across varied RNA structures.

- It's not clear from this work what the predictive power of BASH-MaP would be when trying to identify G-quadruplexes in RNA sequences of unknown structure. Although clusters of G's with low reactivity and correlated mutations seem to be a strong signal for G-quadruplexes, no effort was made to test a range of G-rich sequences that are known to form G-quadruplexes or not. Having this information would be critical for assessing the ability of BASH-MaP to identify G-quadruplexes in cells.

- Although the authors present interesting results from various types of analysis, the code currently available on Github lacks the documentation and examples necessary to be useful to the broader community.

- There are aspects of the DAGGER analysis that could limit its robustness or utility for different RNAs:

(1) Folding of the RNA based on individual reads does not represent single-molecule folding since each read contains only a small fraction of the possible adducts that could have formed on that molecule. As a result, each fold will largely be driven by the naive folding algorithm. The DANCE-MaP algorithm that was also used by the authors addresses this concern.

(2) G residues in a loop will have a different impact on RNA folding than those in a G-quadruplex. This difference could reduce the accuracy of CONTRAfold predictions when forcing G-quadruplex residues to be unpaired. That said, predicting secondary structure around G-quadruplexes is a challenge for folding algorithms.

(3) Incorporation of the G mutations requires prior knowledge of the RNA 3D structure, limiting the utility of the method to predicting alternative conformations in structures that are already well characterized.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98540.3.sa2](https://doi.org/10.7554/eLife.98540.3.sa2)

Summary:

In this study the authors aim to develop an experimental/computational pipeline to assess the modification status of an RNA following treatment with dimethylsulfate (DMS). Building upon the more common DMS Map method, which predominantly assesses the modification status of the Watson-Crick-Franklin face of A's and C's, the authors insert a chemical processing step in the workflow prior to deep sequencing that enables detection of methylation at the N7 position of guanosine residues. This approach, termed BASH MaP, provides a more complete assessment of the true modification status of an RNA following DMS treatment, and this new information provides a powerful set of constraints for assessing the secondary structure and conformational state of an RNA. In developing this work, the authors use Spinach as a model RNA. Spinach is a fluorogenic RNA that binds and activates the fluorescence of a small molecule ligand. Crystal structures of this RNA with ligand bound show that it contains a G-quadruplex motif. In applying BASH MaP to Spinach, the authors also perform the more standard DMS MaP for comparison. They show that the BASH MaP workflow appears to retain the information yielded by DMS MaP while providing new information about guanosine modifications. In Spinach, the G-quadruplex G's have the least reactive N7 positions, consistent with the engagement of N7 in hydrogen bonding interactions at G's involved in quadruplex formation. Moreover, because the inclusion of data corresponding to G increases the number of misincorporations per transcript, BASH MaP is more amenable to analysis of co-occurring misincorporations through statistical analysis, especially in combination with site-specific mutations. These co-occurring misincorporations provide information regarding what nucleotides are structurally coupled within an RNA conformation. By deploying a likelihood-ratio statistical test on BASH MaP data, the authors can identify Gs in G-quadruplexes, deconvolute G-G correlation networks, base-triple interactions and even stacking interactions. Further, the authors develop a pipeline to use the BASH MaP-derived G-modification data to assist in the prediction of RNA secondary structure and identify alternative conformations adopted by a particular RNA. This seems to help with the prediction of secondary structure for Spinach RNA.

Strengths:

The BASH Map procedure and downstream data analysis pipeline more fully identifies the complement of methylations to be identified from DMS treatment of RNA, thereby enriching the information content. This in turn allows for more robust computational/statistical analysis, which likely will lead to more accurate structure predictions. This seems to be the case for the Spinach RNA.

Weaknesses:

The authors demonstrate that their method can detect G-quadruplexes in Spinach and some other RNAs both in vitro and in cells. While application to other RNAs is beyond the scope of the current manuscript, the performance of BASH MaP and associated computational analysis in the context of other RNAs remains to be determined.
