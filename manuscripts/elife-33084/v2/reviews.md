# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33084.052](https://doi.org/10.7554/eLife.33084.052)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Silencing of transposable elements may not be a major driver of regulatory evolution in primate iPSCs" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Christopher Brown (Reviewer #2); Geoffrey Faulkner (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript provides a comparative study of transposable element (TE) silencing in primates, profiling H3K9me3 using ChIP-seq in 17 induced pluripotent stem cell (iPSC) lines from humans and chimps. The authors compare these profiles across the individuals and species to identify sets of TEs that are consistently and divergently marked between species. The majority of orthologous TEs are consistently marked in both species. The authors interpret this as implying that there are few functional differences in TE silencing between humans and chimps. They further support this conclusion by analyzing RNA-seq data from the same cell lines. They find no association between differential silencing of TEs and the expression levels of nearby genes. They also demonstrate that shorter TEs, older TEs (based on distance to consensus), and TEs closer to gene starts are more likely to be differentially silenced. They further demonstrate that differentially silenced TEs not associated with large differences in gene expression.

The manuscript is well written, the experiments are well designed, the analyses are well conducted, and the manuscript's conclusions follow logically from the presented analyses. The findings will be of significance to those interested in cis-regulatory evolution, gene expression, and transposable element biology. However, there are aspects of the analyses that would benefit from further clarification. In addition, we all agreed that the work needs a more balanced presentation of conclusions, as well as discussion of experimental caveats and discussion of alternative conclusions.

Essential revisions:

1) A more balanced presentation of the Results and Discussion sections

Throughout the manuscript the levels of difference in H3K9me3 at orthologous TEs between humans and chimpanzees are characterized as remarkably conserved. These claims would be much stronger if the authors could provide a sense of how much difference in the H3K9me3 profiles would be required to count as meaningfully diverged. For example, the read count correlations between species are lower than within species (Results section), and 11% (16,238) of tested regions are differentially enriched. From one perspective, that's quite a bit of divergence, even if only a small fraction influences gene regulation. Indeed, 66 genes with species-specific H3K9me3 within 1 kb or the TSS show differential expression. Couldn't 66 such genes be functionally meaningful, especially given the similarity of humans and chimps?

How much differential methylation/expression is necessary to count as significant? Repeatedly, statistics are presented that could easily be interpreted the other way. For example, in subsection “Majority of orthologous TEs are similarly silenced in human and chimpanzee”: "Indeed, while ultimately most TEs (88%) do not overlap H3K9me3 regions, when TEs do overlap H3K9me3 regions, we are generally (for 82% of TEs) unable to find evidence that these TEs are silenced differently across species.” Equally one could read that as 18% of TEs (1000s of individual elements) being differentially silenced, right? This is a recurrent theme in the manuscript, that one could just as easily interpret this result the other way. Also, in subsection “Orthologous TEs tend to be silenced more often than species-specific TEs”: "We considered the ChIP-seq data in the context of the orthologous TEs, and observed that only 12% of orthologous TEs overlap an orthologous H3K9me3 region with at least 50% of their length" That's 12% of 4,248,188 (~500,000) right? That's a lot. Perhaps the issue here is an exclusive reliance on percentages rather than considering that the absolute number of elements involved is still very high, and that tends to disagree with the main message about TE silencing not being a major driver of regulatory innovation in primates.

2) Careful framing of the scope of the conclusions in the context of mechanisms which often silence TEs

The authors demonstrate that longer TEs are preferentially silenced. Why is this indicative of regulatory potential? What about being more likely to contain sequences that recruit silencing machinery? Have they performed a motif analysis or assessment of other genomic features? Are there features besides length, age, and distance to TSS that are associated with silencing of TEs? Open chromatin (available ATAC seq data), active histone mods (available), local TE density? Doesn't the fact that TEs that are further from the TSS are more likely to be silenced argue against the 'regulatory potential' hypothesis?

There are other means by which TEs are silenced. As the authors note, mutations to TE sequences commonly disrupt their activity and ability to influence transcription. Without accounting for sequence-level differences, it is challenging to interpret differences in the activity of orthologous TEs between species. For example, an orthologous TE may be inactive in both species while only marked in one due to an inactivating mutation in the other. This could account for the lack of correlation between H3K9me3 state and expression. Also, isn't it possible that the regulatory effect of the TE could be repressive, so silencing of the TE would not necessarily only lead to repression. Furthermore, as the authors note, these conclusions may not extend beyond the embryonic stem cell context.

Finally, the conclusion that TEs do not contribute to the regulatory divergence between species (e.g., in the Discussion section and other areas) is too strong given the data presented. The authors show that differences in H3K9me3 near the TSSes of genes do not strongly correlate with differences in expression between species. There are many other ways TEs could influence expression. In many cases, TEs have enhancer activity and differences in the silencing of enhancer TEs that influence expression would not be detected here given the focus on TSS proximal TEs. The authors could use enhancer maps to perform similar analyses of differentially silenced enhancer TEs or make clear that their analyses do not address this potential regulatory mechanism.

3) Address and clarify the technical concerns about the methods raised surrounding power, peak calling, TSS focus, and definition of orthologous peaks

For example, have the authors used their input data as a covariate in their differential silencing analyses? It is unclear as written. As written, it is unclear if peaks called in individuals are merged prior to differential expression analysis. If no merging was performed, are all DESEQ tests independent? The minimum read count threshold seems very low. Have the authors demonstrated that there is not substantial loss in power to detect differential histone modification at this low end?

Does this approach (Results section): "We defined orthologous H3K9me3 ChIP-seq regions as those where a ChIP-seq peak, contained within orthologous human-chimpanzee genomic regions, was identified in at least one individual, in either species in our study (see Methods)." exclude any regions that are polymorphic within chimp or human (I assume so).

The authors should note the caveat that using H3K9me3 as a mark of repression, whilst being reasonable, is not uniformly indicative of repression and, if other markers were used instead, some of the discordant TEs in chimp versus human may be concordant for these other markers.

Re: the use of sequence divergence from consensus scaled by mutation rate as an estimate of TE age. There are many factors that could confound this analysis, including differences in the mutation rate of different TE families and differences in mutation rate over different evolutionary epochs. If this metric is to be called age, I would want to see more benchmarking of its accuracy. How variable in this statistic for members of the same TE family and type? How does this accord with what we know about their periods of activity? Furthermore, Dfam provides estimates of the origin of all TE models based on their presence across different clades. Do the results hold when stratifying by TE origin? Otherwise, I would recommend reporting these results in terms of sequence divergence from consensus rather than age.

4) Better framing of these results in the context of somewhat contradictory studies

In the Discussion section, the authors should note more explicitly that their conclusions appear to contradict those made by several other studies in this area in recent years. For example, Wang et al., 2014 finds that LTRs are an essential part of pluripotency regulation in primates. Cordaux and Batzer, 2009 makes similar conclusions about L1. Jacques, Jeyakani and Bourque, 2013 suggests TEs are actually very important for regulatory innovation in primates. Considering how long the manuscript is, the authors should dedicate a section to, in a balanced and fair way, address why their findings are at odds with these other papers. I also do not think that anecdotal examples should be dismissed (e.g. " Overall, while studies have shown the effect of TE derived enhancers on gene expression divergence at single loci (81), or tens of loci (23), genome wide effects on global gene expression divergence have been less clear"), as these single locus examples can be important and instructive.

5) (Optional) The authors clearly demonstrate that most TEs are not silenced by H3K9me3 and that most silenced TEs are equivalently silenced in both species. I think it would be particularly interesting to ask a complementary set of questions: Are differentially silenced loci enriched for TEs? For species-specific TE insertions?
