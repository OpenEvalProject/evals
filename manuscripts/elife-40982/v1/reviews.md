# Peer review - Round 1

Editors:
- Pamela J Bjorkman, California Institute of Technology United States
- Philip A Cole, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40982.027](https://doi.org/10.7554/eLife.40982.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Affinity capture of polyribosomes followed by RNAseq (ACAPseq), a discovery platform for protein-protein interactions" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Philip Cole as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kai Zinn (Reviewer #2); Rachelle Gaudet (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript by Peng and colleagues provides a thorough evaluation of an RNAseq method, which they name ACAPseq, to identify protein-protein interactions using a large panel of extracellular domains of proteins as a test set. The methodology combines pulldown of polyribosomes from frozen tissue using Fc-tagged proteins as bait and the highly-multiplexed mRNA sequencing of the pulldown. Overall the experiments are convincing and the analyses appropriate. As described in the Discussion, this method has both strengths and weaknesses, but when implemented carefully and with understanding of the system's limitations it can provide useful information about potential protein-protein interactions of a protein of interest. Because many of the well-established techniques for discovery of protein-protein interactions do not work well for extracellular proteins, ACAPseq can fill a void in the protein-protein interaction discovery space. The method also has some clear advantages absent from other competing technologies: for example, the ability to link binding to specific splice variants.

Essential revisions:

We have the following suggestions to improve the manuscript.

1) 1209 candidate interactors seems like a lot to examine; but the authors might wish to point out that number is as high as it is mostly because a few baits identify many partners. It is likely that most of the interactions with baits that identify >10 partners are artifacts and indicate that the baits are "sticky." If you add up all the interactions for baits that identify <10 partners, there are only 187 of those, which is a more manageable number.

2) The authors might wish to indicate how much the sequencing cost. This looks like a lot of lanes, but I couldn't estimate how many samples were done. The cost of this method might be beyond the resources available to most labs. Related to this, can the authors provide an indication of the throughput? What was the size grouping for sequencing? Did they always sequence a pair (test bait plus EFNA-1 control)? Any recommendations based on their experience?

3) Two reviewers noted that Figures 9-11 don't really belong in this paper, as they are investigations of the binding sites on some of the candidates. These are probably included because they didn't have data for full papers on APP-CNTN3 (for example) and the other interactions and wanted to have a format in which to publish them. These figures make the paper rather long and unwieldy, and distract a bit from the description of the method. However the reviewers did not insist that they be removed. Perhaps the APP-CNTN3 section, which is particularly long, could be deleted or shortened.

4) Subsection “ACAPseq with diverse mammalian ECD baits”, second paragraph:

Supplementary file 1 should include additional columns for (1) database entry code for the relevant cDNA sequence and (2) the corresponding start and end positions of the cDNA (or corresponding translated protein) used in the bait construct.

5) "… in which domain 2 pairs with itself (in the domain 3 deletion mutant), domain 3 pairs with itself (in the domain 2 deletion mutant)…” etc.: these are unwarranted inferences, because the authors do not know which domain interacts with which domain in their constructs, only that the construct is or isn't sufficient to cause bead aggregation. This paragraph should thus be carefully reworded. A more conservative conclusion: it seems that the data in Figure 11 suggest that construct pairs in which a domain 1 – domain 4 interaction is possible have the strongest binding?
