# Peer review - Round 1

Editors:
- Gary H Karpen, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57212.sa1](https://doi.org/10.7554/eLife.57212.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript addresses an unusual and interesting observation initially made in 1987, showing that insertion of S. pombe yeast DNA into a mouse chromosome is associated with a visible 'thinning' of mitotic chromosome width. Here, the Allshire group use cutting-edge techniques to determine why the pombe chromatin assumes a centromere-like constriction that differs from the wider flanking mouse chromatin. They discover that enrichments for the heterochromatic histone modification H3K9me3, smaller loops and condensin complexes occur de novo upon introduction of either pombe DNA or chromatin into mammalian chromosomes. The authors propose that the characteristic constrictions associated with eukaryotic centromeres results from higher levels of condensin recruitment over heterochromatin, which produces smaller chromatin loops.

Decision letter after peer review:

Thank you for submitting your article "Large domains of heterochromatin direct the formation of short mitotic chromosome loops" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Gary H Karpen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Eric F Joyce (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This manuscript addresses an interesting observation initially made in 1987 showing that insertion of S. pombe DNA into a mouse chromosome was associated with a visible 'thinning' of the mitotic chromosome width. Most biologists would posit that inserting even a large (Mb) size piece of DNA from one organism into a distantly-related organism would not impact chromosome structure. The authors generate a large number of independent cell lines that reproduce the constriction phenomenon, then use molecular genetic tools (e.g. ChIP, Hi-C) to conclude that H3K9me enrichments, smaller loops and condensin complex enrichment occur de novo upon introduction of pombe DNA or chromatin into mammalian chromosomes. One interesting result is the demonstration that the pombe DNA constriction does not depend on pre-existing chromatin state, since the phenotype is observed upon insertion of naked DNA.

Overall, reviewers agree that the manuscript contains interesting and important information that would be of significant interest to the field, warranting publication in eLife once the following issues are addressed.

Essential revisions for this paper:

The primary results are generally sound and rigorous. However, the manuscript would benefit from text revisions (not new experiments) that clarify approaches and rationales used to support some conclusions, and distinguish solid conclusions from speculation.

1) Make the rationale and evidence supporting differences in sizes of loops, vs. other forms of compaction, clear. An increase in interactions identified by Hi-C does not a priori indicate loop formation. Figure 6C seems to show a decrease in contact probability for S. pombe DNA at the smallest genomic distance near the y-axis. Is this consistent with the authors' conclusions? They highlight an extended increase followed by a large dip at the largest genomic distance to suggest that loop sizes are reduced and that this must be driven by condensin activity. However, loops defined by Hi-C are typically represented by corner peaks in contact matrices. Are corner peaks observed in this dataset? What is the evidence that these interactions are even loops?

2) It would be useful to know if there is a higher density of CTCF sites in the pombe DNA. Of course CTCF ChIP seq or Cut and Tag would be even better, but a motif search would be sufficient for now.

It would also be useful to know if there are other sequence features (e.g. AT richness) that distinguish naked pombe DNA from mammalian DNA. One other reason this should be examined is that DAPI is used here for DNA quantitation, and has known preferences for AT-rich DNA.

3) Using primary and secondary antibody labeling to measure fluorescence intensity is typically difficult to accurately quantify and compare across experiments. The authors normalize their numbers across samples by comparing intensities to neighboring chromatin regions, which is reasonable. However, it was not clear how these "control" regions were selected, and the size and location of control regions changed across different experiments and figures. It seems that in some cases the control regions are equally spaced from the insert across different conditions (as in Figure 1B, E, and F) but not in other cases (Figure 2D and E). Please clarify how control regions were selected.

4) With regard to the conclusion that condensin concentration is increased on the inserted DNA, it was not clear whether condensin I/II ratios would be expected to be changed. The authors state that "neither the overall levels of condensin nor the ratio of condensin I to condensin II complexes differ." It may be premature to make this conclusion without testing a condensin II-specific subunit as well. As the authors point out in the Introduction, different ratios can account for different chromosome structures. For instance, decreased lateral distances and increased axial distances, as observed at the inserted locus, could be explained by an increase in Condensin I:II ratio.

5) The model presented at the end is too complicated and should be simplified (and smaller) (PS condensin is mis-spelled (condensin) in the middle panel). Most importantly, the model is certainly valid, but the authors should consider and incorporate alternative models that could also account for the observed structural changes. The conclusions about K9me and condensin rely on seeing protein enrichments, but in the absence of direct perturbations a role for e.g. condensin is speculative. It may be worthwhile to consider and cite Costantino et al., 2020, where micro-C analysis of S. cerevisiae identified small loops in mitosis, in this case driven by cohesin. Other possibilities include differences in distributions of sequence features or binding sites (e.g. base composition or CTCF sites), and other possibilities mentioned above.

Revisions expected in follow-up work:

As with all interesting studies, these findings raise more questions and future experiments. Why is more condensin loaded onto these regions? What is the role of the RNAi or piRNA pathways in generating H3K9me on this 'foreign DNA'? Finally, perturbations are required to demonstrate that the constriction disappears upon H3K9 demethylation or blocking methylation, or depletion of condensin.
