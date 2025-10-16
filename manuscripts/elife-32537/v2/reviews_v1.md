# Peer review - Round 1

Editors:
- Timothy W Nilsen, Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32537.021](https://doi.org/10.7554/eLife.32537.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The kinetics of pre-mRNA splicing in the Drosophila genome: influence of gene architecture" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Timothy Nilsen as the Reviewing Editor and James Manley as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Andrew G Clark (Reviewer #2); Manuel Irimia (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All of the reviewers were quite positive about the work; all agreed that it provided substantive new insight into splicing kinetics in vivo. All also agreed that the paper was in principle suitable for publication in eLife. Nevertheless, each referee raised a few, largely overlapping, concerns that must be addressed via revision. In this regard, it was agreed that these points could be dealt with by revisions to the text both acknowledging some potential caveats to interpretation of the data and explanation of some items that were not clear. In lieu of providing a list of essential revision, we are providing you with the complete reviews with the understanding that all points raised will be thoroughly addressed.

Reviewer #1:

Overall, this is an excellent paper. The careful use and description of the simulations is to be commended. The authors make several interesting observations about rates and accuracy of exon defined and intron defined splicing events. Their results are certainly the most complete treatment of gene structure and splicing in Drosophila. There are, however, a few issues that should be addressed.

1) The analysis makes the explicit assumption that transcription rates are uniform across genes. This is probably close to true for Drosophila but I would think that this could be tested using the data from these experiments and earlier ones from, for example, the Lis lab. I would be most concerned about how non-homogeneous transcription rates might affect some of the conclusions made regarding effects at the ends of genes.

2) A related issue is the unstated but important assumption that 4s-U labeling is instantaneous and uniform. There must be a lag, and perhaps a significant lag, in labeling, particularly in the 5-minute time point, during which the uridine pool is reaching a new equilibrium. There is significant literature on this issue in cultured cells (although perhaps not in S2 cells) from which to make reasonable approximations. From what I can tell, this effect was not modeled in the simulation and it is not clear to what extent this might affect the rates of splicing observed. While most of the analyses in the paper are comparative rather than absolute, the authors do make claims about real-time rates. They should address this point and perhaps show that their measured rates are valid when this issue is included.

3) The discussion of developmental and stress response genes being enriched for exon definition does not seem complete. Exon definition genes are longer and so take longer to transcribe. Splicing appears to be faster for such genes but what is the actual rate limiting step in their synthesis? It could even be 3' end formation rather than elongation or splicing.

4) The authors note that the first introns are often more slowly spliced than subsequent introns. What about last introns and, in particular, exon defined last introns that may rely on different mechanisms?

Reviewer #2:

This paper was a delight to review! By labeling nascent RNA transcripts with 4-tiouridine, the authors were able to infer which transcripts retained introns and which had already spliced out the introns. They allowed for modeling of the full dynamics of the splicing process to estimate rates of splicing of every intron in the transcriptome. The goal was to learn how intron and exon lengths impact splicing dynamics. The find that exon-spanning introns are more efficiently spliced than intron-spanning splice sites, and suggest that genes that require rapid activation (such as stress response) have evolved the exon-spanning definition. Also genes that are very highly expressed tend to use the exon definition mode, consistent with the need for faster transcript processing.

The paper is well written and very well motivated. Intron-defined and exon-defined splice sites are clearly spelled out, and the unknowns regarding relative use of these splicing kinetic pathways drive the need for studies like this. The use of 4-thiouracil (4sU) incorporation provided a means to estimate the half-life for the splicing time of essentially every intron in the 5600 most highly expressed genes.

The authors do a good job showing how the method will work in silico, through simulations of the 4sU labeling processes and the inferred splicing half-lives of introns obtained from labeled transcripts with and without introns spliced out.

By doing 5, 10, and 20 min labeling with 4sU, followed by RNA sequencing and supplementing this with RNA-seq data of mature transcripts. The relative ratio of intron-exon junction reads to exon-exon junction reads was highest at the 5 min labeling period and decreased rapidly to low levels at longer times The method would appear at first to rely heavily on the assumption that all transcription proceeds at 1.5 kb/min, a figure that has good empirical support for the average, but which likely varies considerably. Simulations do an adequate job showing that the splicing half-lives are nevertheless well estimated over a reasonably broad range of transcription rates (although presumably if transcription rate were related to splicing progress in some aberrant way, the method could falter).

The data presented here clearly supports the notion that short introns that have relatively long flanking introns will tend to employ the intron definition splicing mode, whereas those with longer introns than the average of the flanking exons will tend to employ the exon definition splicing mode.

One technical detail could be made a bit more clear. The Materials and methods section succeeds very well in describing the way that splicing kinetics are learned from the relative abundances of spliced and unspliced introns in transcripts of different lengths. The contrast of several methods for quantitative analysis is good, and makes the logic clear. But the way that the data provide inference of the distinction between the exon-defined and intron-defined splicing could be more clearly spelled out. It appears to be based solely on RIME value, and while this is a sensible starting point, one would like to know if there is any other confirmation of these calls. In other words, one would like to know error rates for this inference.

An overall assessment of goodness-of-fit of the decay model to data would be good to see.

Given the unusually slow kinetics of splicing of the first intron (which often hold enhancer elements), it does appear to be sensible to drop the first intron in the analysis of the factors that determine splice mode.

Arguments that the splicing modes are a product of natural selection are speculative and are not based on either comparative (interspecific) analysis or on population genetic analysis. The former seems more likely to be feasible, but would entail a radical increase in the work (and so is not recommended here!). And the latter cannot be done without a battery of S2-like cells from different lines, which don't exist. Probably the relatively low frequency of polymorphism in splice sites would erode the power of any population genetic approach. So the suggestion is to make clear in the wording about the claims of selection that these are speculative inferences not based on specific evidence of past action of selection. To this reviewer, this lack does not erode the value of the paper, and the speculative remarks about natural selection do help the reader understand the nature of the question and the meaning of the results.

The splicing dichotomy poses an evolutionary puzzle that might warrant some discussion. Namely, the data appear to support the idea that the splicing modes driven by the relative lengths of introns and flanking exons. But natural selection in turn can also adjust these parameters. So, is there any adaptive argument to be made why Drosophila are balanced between the use of both modes?

It is somewhat of a limitation that the entire study was done in S2 cells. Is there any hope of getting 4sU into whole organisms to get at tissue-specific characteristics?

There are a few issues that are not addressed and might be of interest. Drosophila make great use of alternatively spliced exons and yet alternative splicing gets very short mention in the paper. Similarly nested genes would be expected to have odd splicing dynamics, and it might be a good sanity check to see this. I expected to see more discussion of the super short introns (<50 bp) found in Drosophila – are they all intron-defined and super-rapidly spliced? Is it necessary to invoke different splicing machinery for these?

Reviewer #3:

Pai and co-workers investigated genome-wide splicing rates in Drosophila S2 cells and how these rates relate to different modes of splicing (i.e. intron and exon definition). For this, the authors employed metabolic labeling coupled to RNA sequencing, combined with elegant mathematical modeling. The study reports several interesting results, including a local maximum for splicing rates for 60-70 nt long introns (the most common length in Drosophila) and the unexpected finding that exons surrounded by very long introns are spliced the fastest and most accurately.

Overall, I enjoyed the manuscript and I do not have any major concern. The following are specific comments/suggestions:

1) The fact that introns with similar rates tend to more often co-occur within the same genes seems to make sense. However, I wonder whether this could be driven, at least in part, by the different elongation rates among genes. If I understood it correctly, the model they developed assumes a single elongation rate for all genes. Therefore, it is possible that some gene-level biases are introduced because of this. While this should not affect most of the conclusions in the study, the bias may be strong enough as to create patterns of significant co-occurrence within genes (all introns within a gene will have the same bias and this will be different to most other introns). This is of course difficult to test. Perhaps the authors could use their data, consisting of three time points, to roughly estimate elongation rates and group genes based on these. Irrespectively, I may be a good idea to add a brief note about it.

2) Figure 4B: given the results in Figure 4C, it would be good to also have a comparison of half-life SDs for randomly sampled introns within groups of similar lengths, to see if this is the main feature driving the signal (rather than gene co-occurrence).

3) Subsection “Exon definition is associated with faster and more accurate splicing” and Figure 3C: this plot and the associated description in the text are not very easy to understand. The reference to stripes is ambiguous. I do not have a better suggestion on how to represent the data, but at least the wording in the text could be improved. It may help to label/highlight the sections of interest in the plot.
