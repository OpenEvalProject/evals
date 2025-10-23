# Peer review - Round 1

Editors:
- Janet Rossant, University of Toronto , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15657.023](https://doi.org/10.7554/eLife.15657.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "An integrative transcriptomic atlas of organogenesis in human embryos" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Janet Rossant as the Senior Editor and Reviewing Editor. One of the three reviewers has agreed to reveal their identity: Majlinda Lako.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Given the nature of this contribution, we would like to consider it in the category of a Tools and Resources paper.

This paper provides transcriptional profiles from different tissues during early human embryogenesis and as such represents a significant and novel contribution. To date most of our knowledge on human embryogenesis is based on extrapolation from model animals. These new data will provide a resource to the community enabling more understanding of tissue differentiation and organogenesis. It will also help with identification of new disease genes and understanding developmental defects.

Essential revisions:

1) There are some important issues raised by two of the reviewers with regard to the statistical analysis of the data. These concerns are provided in detail below and must be addressed in the revised manuscript.

2) The linkage of the transcriptional data to developmental disorders is not well validated. There is considerable mouse developmental and phenotype data available in databases that could be mined to enhance the value of your findings and help determine whether the genes identified are truly key regulators of tissue development.

3) The claim that novel transcripts are likely lncRNAs was questioned and needs to be analyzed more carefully.

Statistical issues:

There are concerns of the methodology that would require further clarification:

For the NMF, while the implementation of the methods is likely to be appropriate, there may be a potential flaw in the interpretation of what the analysis may achieved. Regarding "non-overlapping" metagenes, by default, genes can be represented in multiple metagenes, based on the Brunet algorithm in the NMF R package (also the default algorithm). The Methods state that this algorithm has been used, so following on from that, the assertion that "non-overlapping metagenes" could be extracted from the complete dataset and the "potential of coordinated deployment of overlapping genes" is ignored may be incorrect. Furthermore, the critique that "NMF failed to discriminate transcriptional signatures for a number or organs or tissues, or discern the relationships between them… " may also apply to the outcome of lgPCA. Therefore, this is not a compelling argument for discarding the NMF.

The analysis could have been taken further to examine the enrichment of all the metagenes, similarly to the one for liver (Figure 1—figure supplement 3B) for all the specific tissue metagenes (“clear tissue-specific signals for thyroid, liver, RPE, brain, heart and adrenal gland”), and a similar approach could be taken for the downstream functional analysis of lgPCA.

For lgPCA, while the interpretation of the results would be correct, there is confusion in the nomenclature of loading and scores, which are fundamental concepts in PCA. PC scores refer to the eigenvalues (magnitude of variance) which determine the separation between the samples (as can be gleaned from Figure 2B). PC loadings are eigenvectors and describe the contribution of the variables (in this case genes) that causes the separation of the samples. Therefore, PC scores should rightly be PCA loadings (main text, third and fourth paragraphs). This confusion should be attended to. Additionally, it would be helpful to mention at least once in the main text that when referring to "PC1 low" for example, this is meant to be low/negative PC1 scores.

Both NMF and lgPCA are doing similar things, i.e. clustering samples based on gene expression to find which genes drive sample separation. The differences are that NMF can reveal the similarity between gene expression patterns for samples, which are clustered with the same metagenes, in this case kidney and testis to metagene 3, (Figure 2—figure supplement 3B). LgPCA can discern the differences in gene expression between certain samples (for example Brain and liver in PC2 of Figure 2B). If it was intended to include the NMF analysis in this study, a point should be made as the rationale of which samples are to be clustered together and why, before the results may be compared to those from the lgPCA. Alternatively, the NMF analysis can be omitted since the lgPCA method is sufficient to accomplish the data analysis.

The analysis presented in Figure 1C compares the authors' data with that presented in the fetal datasets from the NIH Roadmap. The authors claim substantial up-regulation of sets of genes in their dataset but this is not quantified statistically (instead an arbitrary cut-off of >2-fold enrichment was employed). While there is relatively little data from which to perform a rigorous analysis it should be possible to use appropriate models (gaining power across genes such as GSEA) to find enriched categories in a more robust manner than presented here (i.e., this would allow appropriate correction for multiple testing).
