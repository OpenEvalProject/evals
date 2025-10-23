# Peer review - Round 1

Editors:
- Philipp Khaitovich, Partner Institute for Computational Biology , China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04775.015](https://doi.org/10.7554/eLife.04775.015)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Genes associated with ant social behavior show distinct transcriptional and evolutionary patterns” for consideration at eLife. Your article has been favorably evaluated by Diethard Tautz (Senior editor), a Reviewing Editor, and three reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

While all three reviewers are enthusiastic about the study, several important concerns were voiced by all of them. All reviewers pointed out that this paper does not provide the necessary statistical details to be able to assess the quality of the work. This is certainly the most important concern, as hypothesis acceptance/rejection—which is the central message of the study—fully depends on gene expression analysis and its interpretation. The respective comments are combined below and it will be necessary to address them before a final decision about acceptance can be reached.

More specifically:

The authors investigate the “novel social genes” vs the “gene toolkit” hypotheses. This is certainly interesting and worthwhile. However, one general issue I have with this (and most other) studies on the topic is that it is not clear what “exactly” constitutes evidence for one hypothesis or the other.

For example, the authors here state that the percentage of genes differentially expressed in the same context in the two ants is small (∼3%). However, the overlap is marginally significant (fifth paragraph of the Results section). So the question is, what percent overlap exactly would constitute support for the toolkit hypothesis? 50%? 25%? 10% 5%?

The point is that it isn't clear how and when authors reject or fail to reject the toolkit/novel hypotheses because there is never an explicit significance or overlap threshold provided. The authors are not alone in having to deal with this issue, and so I don't want to lay this completely at their feet, but it would be nice if they stated explicitly what exactly would constitute evidence, or lack thereof, for the toolkit hypothesis somewhere before they get to the results.

Related to this issue, I wanted more detail about the analyses comparing expression patterns between taxa. Did the authors just ask if the same genes were differentially expressed between behavioral types in the two taxa to be viewed as 'consistent' with the toolkit model? Or did a particular gene have to be differentially expressed in the same direction in both taxa? (The latter, I think, although this wasn't clear.) And did a gene need to be significantly differentially expressed to be counted? Or was it sufficient that it show the same directionality in expression, regardless of significance? Directionality without significance is as important as significance, given that the studies in the taxa had different power, used different methods, etc. These are not trivial issues and they may affect the outcome and interpretation of the results. I urge the authors to look into this more closely.

In the third paragraph: The authors state they are interested in the “molecular mechanisms of social interactions (e.g. social signal production, reception and response)”. They refer to genes related to social behavior throughout the manuscript. But are their expression profiles indeed reflecting social information producing/processing skills? Or morphological changes related to other functions, such as exposure to exterior environments? They do not state they used whole ants or just ant heads for transcriptome profiling, which is highly crucial for interpreting the results (especially given that some other studies have used the animal head).

In the third paragraph of the Results section: “Of these contrasts, only foragers and nurses had significantly different gene expression patterns.” This is not well explained. Four categories are compared and 2 of these are said to have different expression. What is the reference here; are the other two categories (grooming and trophallaxis) not different from these two? Or perhaps I am missing something?

This can be partly followed in the Supplementary Material, but should be referred in the main text, e.g. it seems as if all samples were grouped together in the DE analysis. The foragers and nurses were most different as they represent the youngest and oldest. I would have stated this explicitly.

I am also concerned somewhat about the PCA in the Supplementary Material: There seems to be two groups emerging, but this is likely technical (I would guess sample processing dates). It might be difficult to control for this, but if possible, could improve DE analysis significantly.

In the third paragraph of the Results section: “There were 1217 forager- and 1247 nurse-upregulated genes”. What was the p-value cutoff? How did the authors control for multiple-testing? (This can also be followed in the Supplementary Material, but should be referred in the main text.)

In the fourth paragraph of the Results section: “(…) it separated workers into two distinct classes based on age”. If I understand what was done, I think the authors might be overinterpreting: the algorithm will separate the profiles into 2 classes if k=2, and n classes if k=n. Thus, without additional analysis I think one cannot decide on the existence of distinct classes. The authors could consider applying some other test; e.g. check the slope of the expression-age curve.

In the fifth and sixth paragraphs of the Results section: In the gene expression conservation analysis, we are given no information how many genes are used in the comparisons (i.e, the number of genes showing DE in both this and the other datasets, as well as background genes). If the numbers are low, they could instead check the effect size of orthologous genes identified as DE for honeybee, for example. Was the honeybee data generated by Manfredini et al., 2014? If not, the authors should state that.

Most importantly, if the honeybee data was generated from the brain (as done by quite a few studies) and the data in this study from the whole body, this could also be a reason for finding limited overlap.

In comparisons with the Fisher's exact test, it would be useful to state what the background is (non-DE genes, genes up-regulated in the other category, or both?).

The expression “whether genes differentially expressed in these categories of workers were more likely conserved” is a bit confusing, as it also implies sequence conservation, but I think the authors mean conservation with respect to correlated changes.

In the seventh paragraph of the Results section: Connectivity—this could be more explicitly defined, such as emphasizing that the prediction comes from transcription data correlations (e.g. not protein-protein interaction data), and that it depends on how the modules are defined. I think the authors could also discuss potential biases here. Depending on the signal/noise ratio of a gene and the module size, how would connectivity be affected? One would want to make sure that these factors are not influential on the reported result.

Figure 2: Would it not be informative to add a violin plot (similar to A and B) for dN/dS? Especially so, as lower conservation among up-regulated genes is one of the paper's main points. But no information is given regarding the magnitude of the effect. The authors could also plot expression versus connectivity.

In the sixth paragraph of the Results section: There is little discussion on the GO analysis. Does the UV response pathway have to do with sudden exposure to the sun? At least would one not expect to see the same pathway up-regulated in foragers of other taxa?

Please indicate the p-value cutoffs for the GO analysis. This is also found in the Supplementary Material, but should be in the main text or Methods.

It would be helpful if the authors addressed the following:

What is the estimated genome size? What was the CEGMA assembly score for the de novo genome assembly? What was the average coverage per sample for the genomic and transcriptomic data?

The main conclusion that “genes unregulated in foragers and nurses were on average less connected and more rapidly evolving” (ninth paragraph of the Results section) relies heavily on the assumption that they are working with a high-quality transcriptome and that their orthology assignments are correct.

How did they evaluate this? A table with summary statistics would be very useful. How many transcripts had homology to the fire ant and/or the honey bee? How was the paralog problem dealt with, particularly with respect to the molecular evolution analyses?

Similarly, for the network analyses: Were these co-expression networks calculated only on significant transcripts or on all transcripts? How was a significant “network” determined? Two of the modules had > 8000 transcripts in each of them. Does that mean all 8000 transcripts show tightly-correlated expression levels?

Finally, why didn't the authors include Polistes in their comparative analyses? There are at least 2 studies on Polistes, both of which are already cited in this manuscript. This seems like it would be another independent data point worth discussing.
