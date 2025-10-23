# Peer review - Round 1

Editors:
- Jeff Smith, University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53127.sa1](https://doi.org/10.7554/eLife.53127.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study provides an interesting explanation for why yeast cells lacking specific ribosomal proteins, in this case Rpl22a, have a longer lifespan. The resulting reduction in one-carbon metabolism pathway, coupled with the longer replicative lifespan in cells defective for this pathway, suggests it could be a potential target for longevity interventions.

Decision letter after peer review:

Thank you for submitting your article "Translational control of one-carbon metabolism underpins ribosomal protein phenotypes in cell division and longevity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editors and by Jessica Tyler as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper follows up on interesting findings that certain deletion mutants of individual ribosomal protein genes extend replicative lifespan of Saccharomyces cerevisiae, while others do not. They focus on the RPL22A/B paralogous gene pair, where rpl22a∆ mutants are long lived compared to WT and the rpl22b∆ mutant. Their goal was to determine the underlying mechanism of RLS extension induced by the rpl22a∆ paralog mutation. They clearly show that longevity does not correlate with doubling time, ribosome abundance or content, or critical cell size. Using carefully done riboseq analysis, the authors demonstrate downregulated translation of mRNAs related to 1C metabolism in the rpl22a∆ mutant. The reduced 1C metabolism was also supported by excellent metabolite profiling. Together, these results support the hypothesis that extended RLS in the absence of the Rpl22a paralog is correlated with reduced activity of the 1C pathway. However, the results on directly tying reduced 1C activity as causative to lifespan regulation in the rpl22a∆ mutant are not fully convincing at this time.

Essential revisions:

The reviewers identified a number of concerns that are listed below, and should be addressed through experimentation and/or rewriting where appropriate. One of the key issues was that authors are using comparisons of certain pairs of strains to make conclusions about the differences between other pairs, rather than doing direct comparisons. Streamlining the presentation is essential and should help clarify some the specific concerns.

1) Since rpl22a deletion influences many aspects of cell physiology, it is not clear whether the lifespan-extending effect of rpl22a deletion is completely through the repression of 1-C pathways, or it is just one of the contributing factors. I would suggest additional experiments to examine the lifespans of double mutants, such as rpl22aΔ, shm1Δ and rpl22aΔ, ade1Δ. If the double mutants can further extend lifespan compared to rpl22aΔ alone, a discussion of this result would be needed.

2) In Figure 6, the effects of shm1∆ and shm2∆ deletion mutants on RLS are modest, with the shm2 mutant only separating from BY4742 after 35 days. There is no statistical analysis provided, or an indication of whether the results were reproducible. This is a key result arguing that inhibiting 1C metabolism pathways extend RLS, so it is critical to convincingly demonstrate this.

3) The ade17∆ mutant also extended RLS and is included as another example of a 1C mutant. However, the Ade17 enzyme is actually part of the de novo purine biosynthesis pathway. It is therefore surprising that another de novo pathway mutant, ade2∆, had no effect on RLS. How can these disparate results be reconciled?

4) If 1C metabolism is truly mediating the effects of the rpl22a deletion, then supplementing with 1C inputs and products could potentially suppress the long RLS of the rpl22a mutant, thus supporting the overall hypothesis of the paper.

5) In Figure 8—figure supplement 1, SHM2 translation efficiency is reduced in the rpl22a/rpl22a diploid mutant as expected from earlier figures, but now it looks like the translation efficiency is also reduced in the rpl22b/rpl22b diploid mutant, which does not have extended lifespan. This result does not seem to support the overall conclusion of specificity for the rpl22a mutant. How do the authors interpret this result? Minimally, a better explanation of the data and conclusion are needed.

6) Related to this point, while the translational differences between rpl22aΔ and rpl22bΔ are clearly presented in Figure 4, the differences between the mutants and WT (Figure 5—figure supplement 3) are very hard to follow due to the quality of presentation. Please enlarge Figure 5—figure supplement 3 and make the gene names readable. This figure might be quite important to support the claim about quantitative differences. Also for the same point, a WT control would be needed for Figure 4C. It is clear that Met3 expression is lower in rpl22aΔ than that in rpl22bΔ, but it would be good to know how those compare to the level in WT.

7) In Figure 8, there is clearly shown an increased cell size for an shm2∆ ade3∆ double mutant, without any significant change in DNA content, suggesting that loss of these two 1C enzymes impinges on multiple cell cycle phases. However, this is not linked back with lifespan regulation. Do shm1∆ or shm2∆ mutants also affect multiple cell cycle phases? Does this double mutant, or an ade3∆ single mutant extend RLS? The ade3∆ mutant is especially relevant because this mutation impacts both 1C and de novo purine biosynthesis, unlike the ade2 and ade17 mutants in Figure 6.

8) The authors also investigate differences between the rpl34aΔ and rpl34bΔ deletion mutants (comparing them to WT as well), which increases complexity of the presentation without too much additional benefit. If I understand correctly, the Rpl34 strains are used as a kind of "control" for the RNAseq and TE experiments to verify that the assays pick up real differences between rpl22aΔ and rpl22bΔ. However, the authors also compare the Rpl34 deletion strains to WT and make remarks about them, which further complicate the whole picture and generate more questions than they answer. For example, can we conclude that 1C metabolism underlies the increased longevity of the Rpl34 mutants relative to WT? What is the importance of the differences between the Rpl22 and Rpl34 mutants described on Figure 3B and Figure 5—figure supplement 1B?

9) The authors briefly comment that the rpl22a,bΔ strain is not long-lived (subsection “Loss of Rpl22Ap reduces overall protein synthesis”), but do not explore this observation further. What should be concluded out of this comparison? Is 1C metabolism similarly perturbed in the double deletion strain, or is Rpl22b deletion somehow "reversing" the effect of the lack of Rpl22a? What is the RLS of rpl22a,bΔ and how does it compare to WT?

10) Regarding a technical aspect of the work: the authors conclude that the synchrony of their elutriated cultures is good (subsection “Generating RNAseq and Riboseq libraries from synchronous, dividing cells lacking ribosomal protein paralogs”, second paragraph). However, Figure 2B shows that the budding index is starting to increase a bit too fast (compare Figure 1B of Blank et a., 2017). Also, Clb2 seems to ramp up a bit too early, and I cannot really detect a peak in Hhf1 expression. However, my main concern with the elutriation data is related to what the authors state: cells with the same volume across all mutants may very well be in different cell cycle phases (for example, G1 of rpl22aΔ is clearly longer than the G1 of the other strains). The authors compare RNAseq and TE measurements of different strains across different volumes and report genes that differ in expression even at a single time point. Yet, given the approach they follow, some of the differences they uncover could be simply caused by this shift in cell cycle phases rather than differences in expression at the same cell cycle phase. How can one make sure that the reported differences really reflect changes in cell cycle expression and not just differences in timing? Perhaps the authors could show more time series such as the one of Figure 8—figure supplement 1 (e.g. for Ade17, Shm1, Met3) to demonstrate the differences across mutants in a visually clear manner.

11) On which criteria was the selection of 1C enzyme deletions (subsection “Genetic interventions in 1C metabolism that extend longevity”) made? What is their effect on RLS compared to MET3? (i.e. what is the increase in RLS caused by MET3 deletion? Are the numbers comparable?). Does metabolomics support the fact that these deletions extend RLS through 1C metabolism?
