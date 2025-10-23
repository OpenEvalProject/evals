# Author response - Round 1

Authors:
- William E Diehl
- Nirali Patel
- Kate Halm
- Welkin E Johnson ([ORCID: 0000-0001-5991-5414](https://orcid.org/0000-0001-5991-5414))

## Response text

DOI: [10.7554/eLife.12704.026](https://doi.org/10.7554/eLife.12704.026)

A highly knowledgeable reviewer (#3) questions if the conclusions are fully supported and raises a key issue about the analysis: s/he requests further bootstrap analysis of subsets of the sequences (as I understand it – see the review), to show how robust the trees and conclusions are. One would want to know that the same basic story falls out, no matter what subset is used in the analysis. Along these lines, we need to know if the same general conclusion follows with analysis of a few specific genomes, instead of the consensus.

We were very pleased with the positive comments of all three reviewers, and we are grateful for their constructive critiques. We have modified the manuscript in order to incorporate their suggestions, which amounted to small modifications to the figures, textual edits (to improve readability, as requested) and inclusion of some additional supplemental material. The suggestions made by reviewer #3 were particularly helpful in strengthening the reliability of our overall conclusions, and we begin by providing our responses to his/her comments:

Reviewer #3:

The authors present a comparative study tracing the descent of an endogenous retrovirus lineage (ERV-Fc) through mammalian species over an estimated 30 million years. Regular and iterative BLAST searches were used to identify ERV-Fc sequences. Consensus sequences were inferred for Gag, Pol, Env, as possible, and phylogenetic and related evolutionary analysis was performed on consensus alignments. The authors' analysis suggests rapid viral spread to diverse species involving frequent cross-species transmission and recombination events, in addition to vertical transmission following endogenization. While cross-species transmission and recombination among ERVs is known, the study is interesting for its comprehensive focus on a specific ERV lineage and the manuscript is generally well presented. Unfortunately it is not clear from major parts of the analysis how well the conclusions are supported. It isn't clear the quality of the consensus sequences generated and how much they were altered to "undo" mutations and create amino acid alignments used for phylogenetic analysis.

This was a key concern from the beginning of our study – while reconstructing accurate reading frames was essential, we also recognized that it was important to do so without introducing unintentional biasinto the sequences. The consensus sequences used in our analyses (referred to here as “inferred” consensus) were very conservatively changed from that of the “strict” consensus sequences. In order to illustrate how nearly identical the inferred and strict consensus sequences are, we produced a full-length Pol derived phylogeny that includes “strict” consensus sequences for all ERV-Fc lineages (Figure 4—figure supplement 1; the source alignment is included as Figure 4—source data 7). In all cases, the matching “inferred” and “strict” consensus sequences cluster, with only very small length differences appearing in the tip branches, which represent those minor differences that were introduced intentionally when we “undid” mutations to make the inferred consensus reconstructions.

Perhaps the bigger issue is a lack of bootstrap analysis, or indication of posterior probabilities for Bayesian trees, for the phylogenetic analysis using maximum likelihood, which puts the inferences of cross-species transmission into question and many of the proposed recombination events into question if the phylogenetic arrangements are not robust.

We apologize for the oversight. We now include the bootstrap support values for the nodes on all phylogenetic trees.

Similar concerns apply to the 'supertree' combining arrangements of CA or Gag sequences.

The reviewer raised a very important point, prompting a careful reevaluation of the supertree and associated analyses. While we felt that a single supertree was a convenient way to present all the underlying analyses, reexamination suggests that this is not as robust as using the original individual CA and Gag source trees. The method (Average consensus, or AvCon) uses pairwise evolutionary distances between taxa to create phylogenies that are blind to the phylogenetic relationships present in the source trees, and the resulting phylogenies did have differences from the CA and Gag source trees – specifically, the generated supertrees had altered placement of ERV-Fc sequences from the tarsier and little brown bat genomes. Due to this, the supertree in Figure 4A has been replaced with an ML phylogeny based on ERV-Fc Gag.

As the tanglegram presented in Figure 5A was based on the same AvCon phylogeny as Figure 4A, this was also replaced in the revision. Here, we utilized a supertree generated using matrix representation parsimony. In this case, the resulting supertree faithfully represents the topology of the source trees and was suitable for the tanglegram analysis shown in the figure (this tree was not used in Figure 4A because it lacks branch length information).

Related to this, alignments should be made available as a supplementary dataset.

We now include the alignments for Gag, CA, Pol, RT, and TM as supplemental data files. Additionally, we have uploaded un-aligned, full-length Env sequences, including both consensus Env sequences as well as all intact Env open reading frames (ORFs).

Additionally, was similar, independent analysis considered with at least a subset of recovered ERV-Fc sequences versus consensus sequences?

To address the possibility that our “inferred consensus” sequences might impart bias, we did two things: first, we compared our results to trees built with strict consensus sequences (see response to the first comment above), and second, we did as the reviewer suggests for our detailed examination of the relationship between individual recovered sequences from carnivores (see Figures 6 & 7), which gave the same result as using inferred consensus sequences.

In addition, in response Reviewer #1, the text of the Results and Discussion has been edited to be more concise.
