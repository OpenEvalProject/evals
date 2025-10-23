# Peer review - Round 1

Editors:
- Diethard Tautz, Max-Planck Institute for Evolutionary Biology Germany

Reviewers:
- Neel Prabh, MPI for Evolutionary Biology Germany
- Eve Syrkin Wurtele

## Review text

DOI: [10.7554/eLife.53500.sa1](https://doi.org/10.7554/eLife.53500.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

When the first orphan genes were discovered in the yeast genome project, there was a discussion that suggested that genes that do not match with other genes in the database would become fewer over time, once the databases are better filled. Now the databases are filled, but orphan genes are still identified in every evolutionary lineage. Hence, the discussion turned into the assumption that this is due to a lack of sensitivity of detecting remote homologues and that better algorithms need to be devised. Vakirlis et al. now argue that a careful analysis of syntenic genome stretches allows to distinguish between fast sequence divergence beyond recognition and de novo evolution out of non-coding stretches of DNA. By running this comparison in three major evolutionary lineages, they show that only about a third of the genes may be orphans due to rapid divergence, while the remainder are likely truly newly evolved orphan genes.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Synteny-based analyses indicate that sequence divergence is not the dominant source of orphan genes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Eve Syrkin Wurtele (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Unfortunately, we have to reject the paper at this stage, since the submission did not include the results tables that were used to generate the figures and conclusions. Please note that all primary results that are required to reproduce your conclusion need to be accessible and properly listed in the manuscript.

Apart of this, the reviewers were mostly positive, although some critical issues need close attention. In addition to the points raised by the reviewers, the following points need to be addressed for a possible re-submission (please provide line numbers in you next submission):

Taxon choice:

The Drosophila set includes C. elegans as an outgroup, which is not very appropriate. Although both belong to Ecdysozoa, the actual divergence of C. elegans to humans is probably less than to Drosophila, since evolutionary rates in the vertebrate lineage are much smaller than in the insect lineage (as it is also shown in the present analysis). Hence, C. elegans comparisons need to be removed.

The part on "Selecting the optimal E-value cutoff" is not really novel and has also no new results. It should be moved to supplementary material (with the updates suggested by Tomi).

"(we find no, or very limited, difference in evolutionary rate between the two groups in terms of dN, dS, dN/dS; see Materials and methods and Supplementary figure 4)." – this is a key statement that needs to be properly presented in the text, including appropriate statistics. To make it valid, it would have to consider the possibility of different rates in different pairwise comparisons. (See also the comments by reviewer #2)

"We therefore searched ENSEMBL and UniProt for phenotypes and involvement in

disease for the ten genes within micro-synteny regions that we predict originated through complete divergence along the human lineage" – this is a standard orphan gene search, unclear what it adds to the message in the present paper.

"We find that at most 33% of orphans and TRGs have possibly originated by complete

divergence." – it is not completely clear where this number comes from.. It needs to be properly justified, given that it is the key message of the paper.

Reviewer #1:

This is important work that tries to estimate relative contribution of sequence divergence in the origin of novel genes (also known as orphan genes or taxonomically restricted genes). To my knowledge this is the first study entirely focused on this question which is essential for understanding which mechanism (divergence or de novo route) prevails in creating evolutionary innovations at the genome/proteome level. The authors devised a very neat protocol that detects conserved synteny regions between species and then looks for proteins that lack sequence similarity in the target genome but are otherwise embedded within these conserved synteny regions. By extrapolating the findings from the conserved synteny regions to the whole genome the authors conclude that divergence mechanism accounts for at most a third of eukaryotic novel genes.

1) Subsection “Selecting optimal BLAST E-value cut-offs”, Figure 3A – It is really elegant how the authors estimated the proportion of false positive and false negative homologues. From their figures it is clear that the proportion of false positives changes quite differently from the proportion of false negatives depending on the e-value. The authors mention this in the text, but they don't discuss that controlling of false positives is more critical when deciding on the appropriate e-value cutoffs. This is evident from the shape of the Figure 3A curves, where false negatives show linear-like dependence and false positives exponential-like dependence, plus the false positive curves are not dependent on the evolutionary distance. In practice, this means that failing to properly control for false positives would generate spurious sequence similarity hits all over the place, whereas not perfectly adjusted e-value would not have a such profound effect on false negatives, especially in the phylogenetic context.

2) Linked to the previous comment: The authors discuss the BLAST "false negatives" debate but miss the balance by omitting to cite Domazet-Loso et al., 2017 paper which stresses the importance of evaluating BLAST "false positives". Given that the manuscript specifically deals with the false positives this paper should be cited.

3) Subsection “Calculation of undetectable and false homologies and definition of optimal E-values” – I had problems to understand how Mathews Correlation Coefficient was used to decide on the E-value cut-off. Could you please describe the protocol in more details here?

4) Subsection “The rate of “divergence beyond recognition” and its contribution to the

total pool of genes without similarity” – Presentation of the results in Figure 4B and 4C (Figure 6—figure supplement 2) is quite confusing.

5) Subsection “Calculation of proportion of orphan genes due to processes other than sequence divergence” – "This is done by taking…" This part were phylogeny-based proportions are obtained was not comprehensible to me. Could you please make some schematic representation of this part of the protocol?

Reviewer #2:

The authors have made a comprehensive attempt to quantify the contribution of sequence divergence as a source of orphan genes. They have ingeniously used micro-synteny to identify the orphan genes created by divergence. They estimate that at most one-third of the genes within the micro-syntenic regions result from sequence divergence. Subsequently, they extrapolate this result to the entire genome and conclude that the majority of orphan genes are not formed through sequence divergence. Although several studies have investigated orphan genes in various organisms, the relative contribution of processes such as de novo gene creation and sequence divergence in the formation of orphan genes remains largely unexplored. Hence, I consider that this work can significantly contribute to the progress of the field.

Major concern:

The authors assume that the similar distribution of evolutionary rates within and outside the syntenic blocks indicates that the proportion of orphan genes created through sequence divergence within the syntenic block can be extrapolated to the whole genome (Subsection “The rate of “divergence beyond recognition” and its contribution to the total pool of genes without similarity” paragraph 2). Given that the evolutionary rates cannot be estimated for the orphan genes lacking detectable homologs, the assumption made by the authors about the comparability of evolutionary rates across the genome is most likely based on a dataset that excludes such genes. Thus, their argument, although correct for the overall distribution of evolutionary rates, should not be used to extrapolate the proportion of orphan genes originated by divergence within the syntenic blocks to the whole genome.

Reviewer #3:

Orphan genes are an exciting addition to our understanding of speciation and adaptation of organisms to new environments. This research represents a unique and important approach to validate that rapidly-changing genes exist. The manuscript is well-written and clearly presents a very complex set of concepts.

The authors did something new. Rather than assuming (as many have done, but with no basis for this assumption) that any orphan gene that cannot positively be IDed as de novo is "rapidly changing divergent duplicates" the research in this manuscript take the opposite tact, and directly IDs the orphans genes that have arisen by rapid evolution. Indeed, this manuscript is the best evidence for orphans that arose via a " rapidly changing divergent duplicate gene mechanism".

Providing positive evidence for the set of genes that have rapidly diverged is particularly important because it opens the path for researchers to explore the mechanisms whereby particular genes can evolve so much more quickly than the typical gene.

The table with the abbreviations (e.g., ggor) should be moved from supplementary to the main text. That way the reader doesn't need to access supplementary to understand Figure 6.

In both yeast and Arabidopsis, ~50% of orphan genes are NOT located in (micro) syntenic regions of near relatives (Arendsee et al., 2019). These genes (and how they arose) are really interesting as well. The authors might want to mentioned this in the Discussion.

The manuscript mentions genes with "retention of structural similarity " that "suggest the possibility of conservation of ancestral signals in the absence of sequence similarity." Keeping at least some of a structure but losing homology!! Cool. How might this fit into evolution? or is it just a quirk?

The vocabulary the authors use (e.g., "twilight zone", "freefall") adds to the paper.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Synteny-based analyses indicate that sequence divergence is not the main source of orphan genes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Diethard Tautz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Neel Prabh (Reviewer #2); Eve Syrkin Wurtele (Reviewer #3).

The reviewers have discussed the reviews with one another and have come to the conclusion that the manuscript is basically acceptable. Only one reviewer has some small concerns and this review is provided in full below. Given that you had already indicated in your response letter that this issue is minor, we would hope that you can easily integrate this into your manuscript and that no further reviewing will be necessary.

Reviewer #2:

The authors have made a sincere effort to highlight the caveats of their method and adjusted their manuscript as requested by the reviewers. The only remaining concern I have is with the formula used to calculate the contribution of divergence (Figure 6—figure supplement 1). It’s a ratio of two ratios. The numerator is the ratio of orphan genes to all genes within the syntenic blocks, and the denominator is the ratio of orphan genes to all genes across the genome. Here, the criterion to define a syntenic block is pivotal, and to ensure that false positives are excluded the authors limit the block to minimum two homologues on either side of the focal gene separated by either one or two genes. This criterion leaves the majority of genes outside the syntenic blocks in all pairwise comparisons, especially the "match not found" genes (Figure 2—figure supplement 1, Figure 3—source data 3: Figure 3—figure supplement 1).

The authors accept that the proportion of orphan genes within the syntenic blocks decreases as the criterion is made more stringent. They suggest this is because a lesser number of genes were found within the syntenic regions, but the indicated change in the proportion of orphan genes suggests that as more genes are included within syntenic blocks, the proportion of orphan genes within the blocks rises. This is quite intuitive because in many pairwise comparisons (19/48) the number of "match not found" within syntenic blocks is in single-digit and can potentially increase many folds by the mere addition of few more genes (Supplementary Table: Figure 3—figure supplement 1).

Thus, with more relaxed criteria, the calculated divergence contribution will increase as higher fractions of orphan genes are included within syntenic blocks, but the total fraction of orphan genes does not change. Here, the compatibility of the evolutionary rates within and outside the blocks can still be maintained, while the calculated contribution made by divergence will vary.

In the rebuttal, the authors write:

"Note that, although, as expected, stricter synteny criteria led to fewer genes being found in conserved micro-syntenic blocks, overall results changed minimally between the two versions and hence can be considered robust."

It has to be clearly shown, that increasing the stringency of the synteny criterion does not specifically exclude "match not found" genes and their proportion within the syntenic blocks is not a function of this criterion. The authors are advised to make this clarification within the manuscript before making genome level extrapolation. The method established by the authors is robust, and certainly, it will be extensively used in the future. However, the formula used for the genome-level extrapolation appears extremely sensitive to the synteny criterion, unless shown otherwise. Given that the authors have data supporting that synteny criterion does not affect the overall result, they should show it.
