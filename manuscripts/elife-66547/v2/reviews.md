# Peer review - Round 1

Editors:
- Doris K Wu, NIDCD, NIH United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66547.sa1](https://doi.org/10.7554/eLife.66547.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The transcription factor, Atoh1, is capable of regenerating hair cells in neonatal but not mature mammalian cochleae after hair cell loss. Here, Sun et al. demonstrated that a combination of Atoh1 and a transcription factor important for specifying outer hair cell (OHC) fate, Ikzf2, can convert supporting cells in damaged adult cochleae to form hair cells that exhibit OHC characteristics. This experimental approach is a positive step towards the goal of alleviating hearing loss.

Decision letter after peer review:

Thank you for submitting your article "Dual expression of Atoh1 and Ikzf2 promotes transformation of adult cochlear supporting cells into outer hair cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Doris Wu as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kathryn Cheah as the Senior Editor.

Essential revisions:

All three reviewers agreed that the ability of Atoh1 and Ikzf2 to drive supporting cells towards outer hair cell fates are interesting and represent an important milestone in hearing restoration research. We felt the number of samples used in the RNA-seq results were small and could confound the interpretations of the results. Considering additional source material is difficult and time consuming to obtain, advice from experts on how to gain more confidence in the analyses conducted was solicited. Please refer to Reviewer#3's comments for specifics. It is important that the suggestions be followed closely.

Reviewer #1 (Recommendations for the authors):

– IHCs overexpressing Atoh1 and Ikzf2 express Prestin, do they express other OHC properties? Do they lose IHC properties?

– Figure 2, make the shape of arrowhead more asymmetric in F-F" so it will be easier to tell what the authors are pointing at for F and F'.

– Figure 4G would benefit from a z-axis view of OHC-like cell in HC and SC levels.

Reviewer #2 (Recommendations for the authors):

The authors note almost as an aside that inducing Ikzf2 alone in SCs causes a loss of the endogenous OHCs. This non-autonomous effect is not explored or discussed. It makes one wonder why co-expression of Atoh1 with Ikzf2 in this experimental series was inefficient in inducing OHC-like production, since that worked when OHCs were deliberately killed. Is there something different about the different modes of cell killing? Or is something different about the timing of transcription factor expression and OHC expression? This issue should be addressed.

The confocal imaging data in this paper are beautiful and convincing. The characterization of the new mouse strains is extensive, but the authors should be sure to indicate a public repository for their mice, so that others can make use of them.

The P2A-DTR knocked into the Prestin stop codon strain represents a significant advance over the Pou4f3-DTR strain, which kills all HCs, and is often reported to have lethal off-target effects. The description of the characterization of this strain could be improved by adding information whether there are similar off-target effects.

The fact that the OHC-like cells are more like nascent hair cells could be due to the inability to down regulate Atoh1, which is only a transient factor in normal HC development. The authors need to address this possibility.

The scRNA-seq results did not offer a clear path forward. The authors suggest Emx2 as a possible factor to test, but the rationale is not well developed.

Line 120: Please change "and did not display any apparent phenotypes" to something like "and did not display any abnormalities" or "and did not display any abnormal phenotypes". Every genetic condition has a phenotype, which can be normal or abnormal.

Line 126: For clarity "wild-type OHCs" should be changed to "endogenous OHCs" or "pre-existing OHCs".

Line 168: Technically at this point it is not been demonstrated that the system is suitable for expressing Ikzf2 in adult SCs, it would be best to say that the system is suitable for expressing Ikzf2 in Cre-expressing cells.

Line 176: Although expression of tdTom indicates that the first part of the bicistonic transcript was translated, it does not guarantee that the first protein (Atoh1 in this case) is stable. Please provide information on HA expression or if it was already demonstrated in the previous work, just edit this description to clarify that you are sure that Atoh1 is being expressed.

Lines 358-359: Why were the wild type HCs and SCs picked at different ages (P30 vs. P60, respectively)?

Lines 988-989 (Figure 3 legend). This title makes it sound like we are looking at two different means of killing cells, one that is genetic and one that is a drug, when I think what is meant is that DT is the "pharmacologic" agent that triggers killing in the correct genetic background. Please edit to clarify.

Figure 1, Panel D: The legend for this panel does not indicate the type of error bars, nor the statistical test that produced the p-values. Later figures are also lacking the information on the statistical test. If this is the style of the journal, OK, but most readers would like to see the information.

Figure 2, Panel F: The variation should probably be described as not statistically significant, if that is the case.

Figure 4, Panels G: If all of the induced OHC-like cells in a single could be indicated, this would be helpful. Otherwise, it could appear that there is only one induced OHC-like cell in this view.

Figure 4, Panel H: The Y-axis title would be clearer if it were "% SCs transformed to OHC-like".

Figure 6, It is not clear why the color scheme for panel F and G are not the same.

Reviewer #3 (Recommendations for the authors):

1. The authors should perform unsupervised graph-based clustering of the data shown in Figure 6D to see if the cells that are outlined cluster with the OHCs. The analysis may have been performed but needs to be shown in the main figures.

2. Although the three cell types may not segregate cleanly, they do seem to spread out in interesting ways in Figure 6D, with more nascent HCs and "failed " SCs closer to the SC cluster and more OHC-like cells closer to the OHC cluster. This is encouraging and supports their main point. More interestingly, this spread is suggestive of a developmental trajectory, with intermediate cell states. With this in mind, they should perform a trajectory analysis, using a tool such as Monocle or Cell Trails, agnostic to their own assessment of cell type. It is also important to show that this spread is not due to technical heterogeneity, such as the number of genes detected, sequencing depth, or the proportion of mitochondrial genes. The authors should overlay this information on the UMAP plot in Figure 6D to demonstrate whether the spread is caused by technical artifacts.

3. The comparison to published data is informative and seems to have been performed appropriately using new tools in Seurat. It is strange, though, that the "semi-converted" cells overlap with only one of the P1 OHC clusters. The authors should add some more information about what distinguishes those clusters and how they interpret the fact that their cells overlap with one and not the other. These data would also be shown more appropriately as trajectories, again as determined using tools such as Monocle, Cell Trails, or Waterfall. Along these lines, the authors should include all of the data from the Kelley lab, not just the subsets they selected in Figure 6 supplemental Figure 4. The whole point is to place the converting cells within the context of normally developing hair cells, so it is best to include cells at multiple stages in this comparison.

4. The small samples sizes limit what one can conclude about differential gene expression. The problem is that there can be a very high false discovery rate when there are so few cells in each population. It would be better to lower the cut-off to an FDR-adjusted p-value of 0.001 or even lower. This would provide a more accurate view of the nature of differential gene expression for all of the comparisons. It is likely that the numbers of differentially expressed genes (thousands when comparing SCs and HCs and hundreds when comparing semi-converted cells to WT cells) will decrease with a more rigorous cut-off and thus provide a more accurate view of gene expression differences.

5. Along the same lines, rather than repeating the analysis in Figure 6E with other cell types, the authors should simply document the expression of known IHC or vestibular HC enriched genes. Presumably, there isn't a big enough cohort of non-OHC genes (either the number of genes or the level of expression) to drive the converting cells out of the OHC cluster. However, this does not mean that highly relevant genes associated with other hair cell types are not expressed at all. A reasonable list of genes can be compiled from the literature and then shown in a heat map for the three cell types. This is particularly important given that Atoh1 acts across hair cell types and there is a substantial Prestin-negative population. It is important to know if there is some heterogeneity here, in terms of the nature of HC identity taken on.

6. The authors need to soften their discussion of the GO analysis. Many of the terms they mention in the text are not actually statistically significant (i.e. p<0.05) in Figure 6 (Figure supp 1) and Figure 6 (supp 2). Only terms that are significantly enriched should be discussed.

7. I am surprised that only ABR results are reported, when DPOAEs offer a specific measure of OHC function. However, this would not significantly alter conclusions, would just be a nice confirmation.

8. Line 62: "transition" is not the right word to use here. Perhaps the authors mean "transmission"?

9. Line 1072: "compliment" should be "complement".

10. Figure 6- supplement 4: Please explain what the dots labeled 1 and 2 indicate. I found this figure hard to understand. There is also a typo in "apical". There should also be a clearer explanation of what the "pseudotime" scale is (arbitrary units??).

11. Line 537: "or to repress the IHC fate": this doesn't need to be an either/or statement. Many transcription factors both induce one fate and repress another.

12. Line 642: There is an extra "were" in this sentence.

13. Line 643: "whole-amount" should be "whole-mount".

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Dual expression of Atoh1 and Ikzf2 promotes transformation of adult cochlear supporting cells into outer hair cells" for further consideration by eLife. Your revised article has been evaluated by Kathryn Cheah (Senior Editor) and a Reviewing Editor.

All three reviewers thought you have made a good-faith effort in incorporating all the suggestions. However, there are still some outstanding issues from all three reviewers, and the Reviewing Editor has drafted this to help you prepare a revised submission.

This manuscript demonstrated the effectiveness of combined activation of Atoh1 and Ikzf2 in converting adult supporting cells to outer hair cell (OHC)-like cells in a mouse model, in which the OHCs have been selectively ablated with diphtheria toxin. The authors showed that while the number of regenerated hair cells was low and there was no functional recovery based on ABR, these OHC-like cells do express prestin and exhibit a genetic profile that resemble nascent hair cells. This paper will be of great interest to researchers interested in hearing restoration as well as regenerative biology.

Essential revisions:Reviewer #1:

Figure 4 still needs improvement. I thought a z-axis view will help readers to see where the OHC-like cells are located, at the normal HC level as depicted by Figure 4B or they remained at the SC level or both. The added insets of Z axis did not clarify this point. If the OHC-like cells were located at different positions, then better illustrations and quantification are needed.

The diagram in 4B could also be modified to indicate the OHC-like cells came from td-labeled SCs, using hatched black and red colors, for example.

Reviewer #3:

Overall, the authors have done a decent job of incorporating our suggested changes, but the changes do not persuade me that their conversion is as complete as they make it seem. I remain puzzled by the scRNA-seq results, which to me indicate a far from complete conversion that undermines the suggestion that they have even been able to make P1-ish OHCs from adult SCs. For instance, the new hierarchical clustering data in Figure 6 show that 5 cell types form 2 clusters, which tells me that there isn't enough power in the study to make fine distinctions, likely because of the nature of gene expression changes involved. The new trajectories underscore this point, in that the cells that receive Atoh1/Ikzf2 follow their own trajectory and just barely converge with the mature OHCs, not with the P1-ish OHCs. I was glad to see some plots of known IHC genes and one vestibular gene, but really they just show a handful of genes. It would have been much better to show a heat map of ~50 enriched markers for each. I would also be curious to see if the OHC-like cells are like P1 vestibular cells, with the OHC nature driven mostly by expression of Prestin. Also, the new data for oncomodulin expression and synaptic ribbon number are not germane to the argument, as they are shown only for overexpression of Ikzf2 alone in IHC; the heat maps in Figure 6- supplement 6 in fact show that oncomodulin is just barely induced in a handful of OHC-like cells. The discussion contradicts this data and states that the OHC-like cells do express oncomodulin (p. 28, line 19), so this needs to be clarified.

To be clear, I do not think that it is reasonable to expect complete conversion of mature SCs into functional OHCs upon sustained overexpression of Atoh1 and Ikzf2. In the regeneration field, one can learn just as much from incomplete conversions and in fact, that is an important goal since it tells us how far certain combinations can take us while uncovering new roadblocks that we should tackle in the future. The authors made a good attempt to discuss this at the end of the discussion. My request to the authors is to be more restrained in how they present these data. I am not yet convinced that the OHC-like cells are basically like P1 OHCs so much as hybrid HC/SCs that have been able to turn on a few developmentally regulated HC genes and enough prestin to make them cluster with OHCs. I feel that the extent of the conversion needs to be discussed more explicitly, maybe just with a quick summary paragraph outlining how many OHC genes come up, how many SC genes go down, what key genes are missing, plus the extent of similarity to P1 OHCs (how many genes are differentially expressed between P1 OHC and their OHC-like cells and what are those genes?). The authors make some interesting points, such as lack of expression of functionally relevant genes, but still don't provide any meta-analysis that could help others to think about what might be limiting the extent of conversion. I would like to see a more concrete discussion of what the results mean, aside from what we already knew (Atoh1 is good at turning on HC genes and Ikzf2 is pretty good at turning on Prestin).

Finally, all three reviewers thought the manuscript could use some in-depth editing from a trusted colleague who understands the science as well as a master of the English language.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Dual expression of Atoh1 and Ikzf2 promotes transformation of adult cochlear supporting cells into outer hair cells" for further consideration by eLife. Your revised article has been evaluated by Kathryn Cheah (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

1) The RNA seq data are acceptable. However, some sentences need clarification.

Line 569, We concluded that OHC-like cells were, based on their characteristic gene profiles, unlike neonatal IHCs or utricle HCs, instead ~50% similar with neonatal OHCs.

This sentence is awkward, and it is not clear whether the approximately 50% meant 50% in similarity between OHC-like cells and neonatal OHCs based on the selected 53 OHC genes analyzed or 50% of the OHC-like cells were more like the neonatal OHCs. Either clarify or simplify. For example: Taken together all the gene profiling results, we concluded that OHC-like cells resemble neonatal OHCs and not neonatal IHCs or utricle HCs.

Similar clarification is needed for the sentence on line 726.

2) The positions of OHC-like cells within the epithelium still need further clarification. Despite the nice video and the added supplemental figure, it remains difficult to distinguish the location of all the OHC-like cells shown in Figure 4G. A simple fix would be to use the blue and gold color arrows in Figure 4G to point out which are the HCs located in the HC layer versus SC layer. The supplemental figure can then be used to illustrate the two different locations of HCs in more detail.

Line 340, In addition, ~82.6% of OHC-like cells (i.e. arrows in Figure 4G') migrated up (toward the HC layer), and the rest remaining in the bottom (SC layer).

Is it necessary to instil the phrase of "migrated up" considering the cellular organization of the epithelium appears to be somewhat disrupted? "Migrated-up" suggests some active process on the part of the OHC-like cells. Consider replacing the sentence with: "In addition, ~82.6% of OHC-like cells were located in the top HC layer (blue arrows in Figure 4G', supple figure), whereas the rest remained in the bottom SC layer (gold arrows in Figure 4G", Supl figure ).
