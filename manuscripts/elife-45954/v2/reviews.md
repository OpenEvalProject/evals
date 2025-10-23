# Peer review - Round 1

Editors:
- Kevin J Verstrepen, VIB-KU Leuven Center for Microbiology Belgium

Reviewers:
- Matthew Anderson

## Review text

DOI: [10.7554/eLife.45954.039](https://doi.org/10.7554/eLife.45954.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Genome plasticity in Candida albicans is driven by long repeat sequences" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Matthew Anderson (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We appreciate how your study details the role of repetitive sequences in the C. albicans genome on production of genetic variation, which is a significant step towards understanding how genetic variation is produced in the plastic C. albicans genome. More specifically, they show that changes in copy number and loss of heterozygosity associate with the repeats, which often exist as multi-copy sequences found at a range of distances across the genome. Repeats covering ORFs are enriched for LOH, CNV breakpoints, and inversions.

As you can see in the individual reviewer's reports (below), all reviewers agree that your study is solid and interesting. After discussing the reviews among the reviewers and editors, we suggest the following essential changes to the manuscript.

1) We think it is important to add a more detailed description (in the Materials and methods section) and critical discussion (in the Results or Discussion section) on how the repeats were mapped starting from short-read sequences.

2) We suggest more elaborate statistical testing and/or a clearer description of what exactly is tested, and how, to assess the significance of repeat enrichment.

While the other issues and suggestions raised by the individual reviewers were not deemed crucial, we suggest you still consider adapting the manuscript accordingly.

Reviewer #1:

This study investigates the occurrence and sequence context of structural variation in the Candida albicans genome. The authors find several instances of inversions, deletions, LOH and translocation events that are associated with repeat sequences spread across the C. albicans genome, including centromeric and telomeric repeats, as well as repeats in ORFs. The breakpoints of these events were often at regions of higher and longer sequence identity.

Overall, this is a nice comprehensive study describing the importance of repeated sequences in genome plasticity.

My only concern is that the study does perhaps not offer much novel biological insight – repeats / regions with high sequence identity have already often been reported to form the breakpoints of structural variation in genomes. That said, the strength of this paper is that it gives a more comprehensive view on the phenomenon, which in itself has merit.

Reviewer #2:

The manuscript by Todd et al. details the role of repetitive sequences in the C. albicans genome on production of genetic variation, which is a significant step towards understanding how genetic variation is produced in the plastic C. albicans genome. More specifically, they show that changes in copy number and loss of heterozygosity associate with the repeats, which often exist as multi-copy sequences found at a range of distances across the genome. Repeats covering ORFs are enriched for LOH, CNV breakpoints, and inversions.

The inverted CEN4 breaks apart the CENP-A binding site. It would be interesting to know if CENP-A still binds the fragment of the binding region not disrupted during inversion in Chr4B and which homolog (A or B) built the i(4R) chromosome. This has implications in the potential for future recombination and accurate segregation of the i(4R), which, as the authors noted, is quite high compared to other trisomies. While it is stated in the Discussion that knowing this could be of interest in the future, it has implication on the current study.

A statistical test to show enrichment of CNBs within repeats would be helpful when introduced. While it is expected there to be enrichment, if repeat regions span a significant portion of the genome, 13 events may not be sufficient to see enrichment. A CNB between two repeats spaced by 70 kb is not particularly unexpected if when taking into consideration the distance between all repeats begins to approach the full genome size. What may help the reader see the association of the CNB better to the repeats themselves is to zoom in to ~nucleotide resolution and using a sliding window to show that the general copy number changes occur over the repeat as would be expected if they are involved in the recombination itself. Figure 3C does this well but Figure 3B does not. It is difficult to discern any of this from Figure 3—figure supplement 1. An amalgamated panel of all CNBs or LOH relative to their repeat may be best to summarize the findings concisely.

CNBs such as that displayed for AMS3053 on Chr3L that occur across long repeated sequenced with very high (99+%) identity would be hard to map by Illumina short-read sequencing. This is seen somewhat in the IGV snapshot where the repeat regions have an increase in read coverage compared to the internal unique sequence. It would worth including long-range sequencing (MinION or otherwise) for a few select events such as this to demonstrate that the proposed rearrangements are reflected in contiguous pieces of DNA that can span these repeats. Additionally, if these repeats contain genes and are 99+% identical, are the CDS within these regions similarly identical, indicating parologous gene duplications?

Segmental duplications including centromeres are unexpected as this may promote chromosome instability by including multiple kinetochore attachments on the same DNA molecule. Give that 2 strains contained these or their novelty; it would be worth testing if chromosome segregation is distorted in these strains as a result of centromere duplication. Alternatively, one may be activated, which could be tested by CENP-A ChIP-PCR. These events should be tied more closely to the SSA mechanism described in the Discussion.

A critical piece of information missing from the Materials and methods is how reads that could be mapped to multiple places were dealt with during alignment. As some repeats are 99+% identical, it would be hard to map those regions uniquely. The spike in heterozygosity at repeats could be due to random assignment of reads to one or the other repeat resulting in a het call at a homozygous position for each.

The selective pressures promoting retention of segmental deletions are interesting as these are often expected to have greater deleterious consequences than segmental amplifications. While not necessary, it would be helpful to know the fitness consequences of this deletion in the context of OPC in which AMS3420 or CEC2871 was obtained, a bloodstream model of infection, or a commensal colonization model. In short, why would loss of HGT1 and HGT2 benefit the cell during infection enough to be observed?

Breakpoints removed from ALS genes may be due less to poor mapping than rearrangements. How similar was the frequency of called breakpoints in comparable regions encoding tri- or di-nucleotide repeats as are found in the ALS sequences?

Are there features that distinguish between repeat-rich (Chr3R) and repeat-poor (Chr7L) chromosome arms? E.g., GC content, gene density, UTR length, etc., this will be begin to provide predictive correlates to repeats and recombination potential.

Reviewer #3:

In this paper Todd et al. analyse of the role that multi-copy genes play in generating structural variation in the Candida albicansgenome. Through a comprehensive annotation of the reference genome and an analysis of structural variation in "evolved" strains the authors convincingly show that various repetitive elements have created genomic variation, some of which are associated with adaptive traits.

Overall, the authors have used appropriate methods, drawn reasonable conclusions and produced a well-written manuscript. I think the results will be an important contribution to the study of C. albicans in particular and genome evolution in general. I do have a number of small issues that I think could improve the paper, which I detail below.

Much is made in both the Results and Discussion section about thelarge 'spacer distance' between intra-chromosomal repeats (e.g. subsection “Identification of long repeat sequences throughout the C. albicans genome”, second paragraph). This is certainly an interesting result, and the raw data makes it clear this is a real phenomenon. However, I think the manuscript could do with some more clarity about:

a) Why this statistic is of interest;b) Precisely what hypothesis is being tested in this "1-way ANOVA withposttest…"

I suggest a sentence in the Results section describing the motivation forcalculating this distance. I am not sure what we are mean to glean from the factspacer-distance is not (significantly) correlated with chromosome size (given the small number of chromosomes). It would be good to make the biological motivation for this test explicit or reconsider the test. If the implication is that the repeat-copies are approximately uniformly distributed across chromosomes then a statistical test for this (rather than trend with chromosome size) may be a better test? Alternatively, it may be helpful to simply visualize the distribution of spacer-sizes in each chromosome via a histogram or 1-D kernel estimate).

I found myself being slightly tripped up by terminology re LTRs andretrotransposons. Presumably, the large number of repeats identified as "LTRS"

(e.g. subsection “Identification of long repeat sequences throughout the C. albicans genome”, last paragraph) are long terminal repeats that lack ORFs (non-autonomous or "lone" LTRs) while the small number of retrotransposons will include complete LTR retrotransposons. Perhaps a statement or edit to the Results section making this clear will help readers.
