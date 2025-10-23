# Peer review - Round 1

Editors:
- Molly Przeworski, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27344.027](https://doi.org/10.7554/eLife.27344.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Biased gene conversion drives codon usage in human and precludes selection on translation efficiency" for consideration by eLife, and apologies for the delay. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you will see from the specific comments below, both reviewers agree that the analysis is convincing and ultimately worth publishing in eLife. However, they feel, and the reviewing editor agrees, that the results would be of more general interest if framed less as a response to a specific paper and more against the background of a long standing argument about the role of mutation and selection in shaping codon bias.

The two reviewers also made a number of specific suggestions that we would like you to address in revising your manuscript.

Finally, while you report an interesting association of recombination rates and expression levels, you present no evidence that the two are causally linked. Notably, the relationship could be mediated by histone marks, such as H3K4me3, associated with both recombination and expression, and it would be interesting to understand how H3K4me3 and PRDM9 binding sites mediate the observed effects. It is also unclear whether the idea of recombination interfering with transcription is plausible. In yeast and in birds, there is a weak positive association between meiotic expression levels and recombination. In mice, in turn, there is almost no recombination at promoters in meiosis (see Brick et al., 2012). In general, there are a number of papers on the determinants of recombination in human meiosis that may be relevant to this discussion (e.g., Pratto et al., 2014, as well as work by Bernard de Massy and Scott Keeney). We would therefore ask that you revise the text (and Abstract) accordingly.

Reviewer #1 (major comments):

For many years it has been debated whether codon usage bias in human genes reflects natural selection or non-selective evolutionary processes such as mutation rates or biased gene conversion. Recently it was proposed that differences in codon usage bias between different functional categories of genes is evidence for selection for optimal codon usage and translational efficiency (Ginghold et al., 2014). Specifically Gingold et al. found that genes in GO categories related to "proliferation" have a much different codon usage than genes in GO categories related to "differentiation". In this manuscript by Pouyet et al., the authors test whether differences in codon usage between functional gene categories can be explained by GC-biased biased gene conversion (gBGC) rather than natural selection.

The authors make several strong arguments that gBGC is a much better explanation for the observed differences in codon usage bias between different genes than natural selection. They find that codon usage bias described by Ginghold et al. (PC1 of a PCA) is almost perfectly correlated with the GC content of 3rd codon positions (GC3). GC3 is in turn very well predicted by a combination of intronic GC content, flanking GC content, recombination rate and meiotic gene expression. After controlling for these variables, the functional gene category explains very little of the variation in GC3.

Overall the paper is very clearly written and makes a convincing case that differences in synonymous codon usage between different GO categories is driven by gBGC. This result is not especially surprising given previous work showing that GC3 is well-correlated with regional GC content (isochores), but given the recent high-profile argument for selection by Ginghold et al. I feel that it is important to publish this finding. In addition, the paper is novel in that it proposes a mechanistic explanation for differences in GC3 between gene categories-that meiotic gene expression suppresses recombination so that genes with high meiotic gene expression undergo less gBGC and have lower GC content.

Comments:

The per-gene GC3 variance explained by meiotic expression is modest (R^2=8.3%) compared to that of intronic or flanking GC content (62% and 48%). If meiotic expression and reduction in rec. rate explain GC3 and variation codon usage, why is the correlation with meiotic expression so much weaker than the correlations with GCi and GCflank? It would be useful to include some acknowledgement and discussion of this in the paper. As shown in Figure 5, the correlation with meiotic expression and GC3 is far stronger at the level of gene categories. Is the explanation for the low R^2 for individual genes that individual gene estimates of meiotic expression are noisy? Or could it be that meiotic gene expression of broad gene categories has remained fairly consistent during evolution, even though the expression of individual genes has changed substantially?

The difference in R^2 between panels A and D of Figure 5 is puzzling. Why is the correlation between rec rate and GC3 so much stronger than the correlation between rec. rate and GCi? I would expect estimates of GCi to be more precise than those of GC3, since more sites can be used in the estimate, so differences in noise is not a good explanation. Is the better correlation with GC3 driven by the first exon (does the strength of correlation vary with distance from the promoter)? If so, this might suggest something about mechanism. E.g. gBGC might be highest near the promoter.

In the Abstract the authors say that meiotic transcription interferes with the formation of crossovers. While this might be true, the mechanism is uncertain and speculative. It would be better to draw a less speculative conclusion like "genes with higher meiotic transcription have lower recombination rates".

Reviewer #2 (major comments):

This article provides strong evidence that gene expression level during meiosis determines which synonymous codons are most likely to appear in human gene sequences. Compared to genes that are not expressed during meiosis, housekeeping genes that are highly expressed during meiosis are less likely to recombine, undergo GC-biased gene conversion, or have high GC content at synonymous sites. This conclusion is well supported by the analyses presented in the paper, which refute a claim by Gingold, et al. that a difference in human synonymous codon usage between "proliferation-related" and "differentiation-related" genes is driven by selection for translation efficiency.

The main weakness of this paper, in my view, is that it reads more like a response to Gingold, et al. than a standalone piece of work. To avoid the impression that the paper is a niche product that will only interest readers who have some kind of prior stake in the Gingold, et al. results, it would be helpful for the authors to convey a better sense of how Gingold, et al. sits in the broader landscape of selectionist explanations for codon bias, and what these new results mean for that work in general. In showing that selection on translation efficiency does not drive the contrast between codon bias in proliferation genes versus differentiation genes, are the authors only refuting the hypothesis of one particular paper, or of a broader set of papers claiming that selection for translation efficiency drives codon bias in the human genome?

Along the same lines, the title statement that "biased gene conversion drives codon usage" strikes me as underselling the results a bit. It doesn't give any hints about the intriguing and surprising observation that intron GC content and meiotic gene expression explain codon distribution so much better than isochore structure does. Once these results start being discussed in detail, the paper starts seeming less like a contradictory results response paper and more like a very interesting standalone paper, but this transition happens quite late in the manuscript.
