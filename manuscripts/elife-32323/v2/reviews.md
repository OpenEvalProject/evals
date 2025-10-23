# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32323.016](https://doi.org/10.7554/eLife.32323.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "An incoherent feedforward loop facilitates adaptive tuning of gene expression" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal his identity: Kevin J Verstrepen (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors evolve yeast in nitrogen-limited conditions. They find that cells increase expression of MEP2, the ammonium permease either by increasing the gene copy number (reported before) or through mutations in the MEP2 transcription factor GAT1. Surprisingly, these mutations reduce the binding of Gat1 to the MEP2 promoter, but still increase the expression of MEP2 by decreasing the expression of its repressor DAL80. This is indeed an interesting and surprising discovery that shows how the connectivity of molecular circuits could impact on their ability to evolve.

Essential revisions:

1) Report expression and fitness for all lineages, as suggested by reviewer #3.

2) Change the model to include auto-regulation of GAT1, as requested below.

3) Discuss the ability to distinguish the contribution of DAL80 vs. GAT1 to the increased MEP2 expression.

4) Discuss the generality of the results.

Reviewer #1:

Gresham and colleagues examine the molecular basis of adaptive evolution in an experimental evolution setting. They evolve asexual yeast strains in nitrogen-limited conditions and use whole-genome population sequencing to identify the molecular changes associated with fitness gains. The major target of selection in this context is the expression level of MEP2, coding for an ammonium permease. One of the most advantageous changes at this locus is increase in copy number, which was dissected in previous papers. Other changes that occur are non-synonymous changes in GAT1, a transcription factor positively regulating MEP2. Surprisingly, through functional analyses, the authors show that these amino acid changes reduce the binding of Gat1 to the MEP2 promoter. The decreased binging affinity would contribute to increase the expression of MEP2 by decreasing the expression of DAL80, a repressor of MEP2.

This paper appears to be an important contribution because the evolution of gene expression is generally reduced to a very low level of complexity (including in my own work) by characterizing changes as being in cis or trans and as positive or negative. However, transcriptional networks are very complex and network motifs can produce expression levels and patterns that are not necessarily changing in a simple way, at least not in a way that would be expected based for instance on simple changes in TF affinities. The findings presented here are a good example of this and also illustrate the need to consider molecular changes in the context of molecular networks in order to be able to map fitness changes to phenotypes and genotypes. The experiments are well done, the paper is well written and clearly of interest to a large community.

My major comments would be regarding the interpretation of the data:

- It would be useful to eliminate effects that could come from outside the GAT1-DAL80-MEP2 motif and that could explain why MEP2 expression goes up when Gat1 affinity decreases. The gene expression data produced could be used for this purpose, for instance by showing that other potential MEP2 regulators are not affected in the Gat1 mutant backgrounds.

- Third paragraph of Discussion. It would be useful to have a stronger conclusion as to how the increased expression of MEP2 is achieved. The dynamic model constructed maybe useful in terms of supporting one mechanism or the other, for instance self-regulation of Gat1 versus weaker effect of GAT1 mutations on DAL80 than on MEP2.

Reviewer #2:

In this paper Hong and colleagues attempt to understand the functional significance of specific adaptive mutations that evolve in yeast under N2 limited chemostat growth. They find that a large number of early adaptive mutations – although not clear what proportion – are missense mutations in one particular TF (GAT1) that acts on multiple genes but in particular is a positive regulator of the N2 transporter. These mutations eventually get outcompeted by the expansion of the transporter itself (MEP2) but the early adaptation is (apparently) dominated by the GAT1 missense mutations.

Long story short their argument is that most of the GAT1 are loss (reduction) of function in terms of the binding affinity to the GAT1 binding site but because the downstream targets are regulated through an incoherent FF loop this reduction of binding leads to an increase in expression of MEP2 because the GAT1 mutations decrease the expression of the repressor of MEP2, the TF called DAL80.

I was very much prepared to like the paper but was left underwhelmed. The evidence that their model is correct in broad strokes is quite convincing. But they do not seem to be able to link the TF binding to fitness despite having a large number of mutants and do not in any way describe the difference between the two GAT1 mutants they study in great detail. One leads to a much stronger reduction of binding – what does that imply for function?

I am also unclear about the overall message. What do they mean by claiming that the incoherent FFL enhances the ability of yeast to adapt? Is it that in this context loss of function mutants in terms of binding that are more common can generate a gain of function phenotype in terms of expression of the key gene? Is this particular to this structure? What about the other properties of this structure – like the ability to generate a pulse of expression? I was left without a clear sense of how generalizable the findings are and what they mean broadly. Without this sense of general importance it is hard for me to see why this paper out to be published in eLife rather than in a more particular molecular biology journal.

Reviewer #3:

This study shows that evolution in ammonium-limited chemostats repeatedly selects for modulation of the DNA binding affinity of GAT1, one of the transcription factors controlling nitrogen catabolite repression. Due to it being a part of an incoherent type-1 feedforward loop, this alteration in binding affinity results in an increased expression of MEP2, a high-affinity ammonium transporter. This increase ultimately results in an improved fitness in ammonium-limited conditions. As such, network motifs like feedforward loops might facilitate adaptive tuning of gene expression.

This is an elegant study highlighting the importance of network motifs, such as feedforward loops, a nuance often overlooked up until now in the interpretation of experimental evolution data. One of the major strengths of this study is the reproducibility of the experimental evolution, exemplifying that this mechanism of adaptive gene expression tuning might be more general than previously thought. Granted the authors take some of the below-mentioned comments and concerns into account, this study will certainly improve our understanding of the dynamics of evolution.

• Something that is not really explored in this study, is the influence of GAT1 mutations on its own expression. The data suggest that its expression is also increased (even more than MEP2). This fact is never mentioned in the interpretation of the data, but it might be very important. It is also not included in the mathematical model, which seems a bit simple. As previously said, the expression of GAT1 also depends on the level of GAT1 itself and even on the expression of DAL80. On the other hand, DAL80 supposedly also influences its own expression, and this is also not included in the model. These are very important parts of the feedforward loop, so in my opinion a better model could be made, more resembling the real structure of a feedforward loop. These facts should also be incorporated in the interpretations and discussions.

• The authors suggest several times that the mutation of the DNA-binding domain of GAT1 is a quick way to increase the expression of MEP2 during evolution, before the expression can be increased even more by duplicating MEP2. However, MEP2 expression is never measured in lineages with MEP2 CNVs. As such, the proposed progression of MEP2 expression during evolution is never really shown. As this is one of the main underlying assumptions (increased MEP2 expression equals increased fitness, and CNV has the highest expression), this is a crucial experiment to do. Measure expression and fitness for all lineages, including those with CNVs. Then, correlate this expression with fitness.
