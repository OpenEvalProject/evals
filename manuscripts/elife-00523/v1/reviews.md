# Peer review - Round 1

Editors:
- Chris P Ponting, University of Oxford , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00523.023](https://doi.org/10.7554/eLife.00523.023)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for choosing to send your work entitled “Passive and active DNA methylation and the interplay with genetic variation in gene regulation” for consideration at eLife. Your article has been evaluated by a Senior editor and 2 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewer discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The study tackles an important and timely set of questions in the nexus of DNA methylation, gene regulation, and genetic variation. The genomics dataset collected in this study is exemplary and, indeed, is one of the first of the next generation of “genetics–genomics” studies, with three cell types (two of them primary) isolated from over 200 newborns, all genotyped, and profiled for expression (RNA-Seq) and DNA methylation.

In this sense, all of us would be delighted to see the data published, and with the appropriate analytics and conclusions this could be an important paper, well within the scope of eLife. Indeed, it is precisely because the dataset is likely to be broadly used, because the design could be deployed in many other contexts by other groups, and because the conclusions address fundamental questions in gene regulation, that we feel that it is critical that the analytics underlying the conclusion be very carefully and very strongly supported.

In this respect, unfortunately, we found the current manuscript lacking in two important ways:

1) Very strong and broad conclusions were drawn as we detail below, but they were not equally strongly supported in the actual analyses/data. These should be toned down to the appropriate level, with some probably removed or replaced with hypothesis level assertions; and

2) In multiple places throughout the work, the statistics need to be performed more carefully, with appropriate controls, which we detail specifically below.

3) Next, once the statistical analyses are done appropriately, the authors are likely to remain with a far fewer number of significant loci/genes, but those would be individually significant, and the authors should highlight some of those specific examples, instead of focusing solely on aggregate numbers as currently written.

4) Finally, since some of the study’s inherent value is as a resource, it is critical that the manuscript provides processed results in summary tables (as source data files), listing all genes, associated SNPs, and other traits. It is also critical to state clearly within the manuscript where and how the data can be obtained by others (with the expected constraints associated with human genotype data).

We further detail below how to address points 1 and 2, in the context of each of the seven major claims of the paper. We emphasize that without a serious analytic revision, the manuscript will not be appropriate for publication in eLife.

We identify seven major claims in the paper. We list each here and its extent of support, and make specific suggestions for how to address each analytic shortcoming.

* Claim 1 addresses eQTMs, the relation between variation in methylation and expression. The authors draw the conclusion that eQTMs are mostly independent of the mechanism involved in the repressive effect of DNA methylation on expression across genes. This is a strong conclusion, but is currently poorly supported. Specifically, the eQTMs were partitioned into only two bins (positive and negative effect). It might be, however, that most of the pos- and neg-eQTM effects are insignificant (around 0) and therefore some important inter-relations are masked within a sea of noise. Instead, the same plots should be regenerated for eQTMs split into a larger number of bins (e.g., 5 bins: very-neg, neg, no-sign, pos, very-pos-eQTMs), to show whether the negative correlation holds in all of these 5 bins, and more generally is not an artifact of the binning.

* Claim 2 addresses differentially methylated regions (DMRs) across cell types and asked whether DMRs are more often associated to eQTMs and mQTLs than non-DMRs.

First, the relation between DMRs and eQTMs might be a byproduct of their relation with the average methylation. This is because the higher the average, the higher the variance, and thus we may get a higher differentiation per methylation. To control for this possibility the authors should use a 'normalized differentiation in methylation' (i.e., use the residuals of differentiation per methylation after removing the effect of the methylation average), and then use these normalized (residual) values to repeat the same test relating (residual) differentiation with mQTLs and eQTMs.

Second, regardless of the validity of the test, the additional biological conclusions are over-stretched and should be toned down.

* Claim 3 associates mQTLs and eQTMs with different features. The differential association of mQTLs to CGI and non-CGI promoters is intriguing and well supported. The analysis of pos- and neg-eQTMs should be repeated with finer binning (as claim 1, above), but is otherwise satisfactory.

* Claim 4 shows lack of support for a contribution of methylation to allele specific expression, independent of sequence variation. This is a strong assertion, but is also a negative result. Our main concern is that it is hard to devise an appropriate control here. We urge the authors to remove this result, unless they can provide additional support.

* Claim 5 tests for synergistic interactions between genetic variants and DNA methylation on gene expression. Although the authors note that they “controlled” for artificial inflation, Figure 3C shows that there is a clear inflation in the resulting P-values. What is the reason for this inflation? Without correcting for this, it is impossible to judge the number of significant relations. We advise that the authors use at least bootstrapping for some empirical correction, and preferably correct for population structure and other confounders.

* Claim 6 concerns different causality models and their proportions in the different cell types. Each of the three models has a different number of parameters, and the correction with AIC is based on theoretical considerations and hence might not compensate for the different degrees of freedom. In addition, there is no evaluation of the significance of the resulting predicted models (which then precludes the authors – and future readers – from following up on individual findings). To correct for such potential artifacts, we suggest applying a direct evaluation of the distribution of relative likelihood for each pair of models based on data reshuffling (permutation test). Based on such tests, it is possible to (A) get a threshold for each of the likelihood comparisons using a common P-value threshold. This would allow comparing results from different cell types and models using a common systematic threshold; and (B) discriminate significant vs. non-significant relative likelihood scores. Once this is done the authors should report how many of the results are significant and what the statistics are when using significant predictions only, and, finally, they should highlight specific examples, which would enhance the paper's impact and biological relevance.

* Claim 7 tries to couch the findings in a mechanistic setting, claiming that TF levels modulate the effect of DNA sequence variation. This is an intriguing and important direction, but it has to be done carefully.

First, as above, it is not clear whether the reported P-values are corrected for the special characteristics of the data. Applying a permutation test and deriving a corrected P-value based on such an analysis would allow evaluating the statistical significance of the reported results. Furthermore, while we do not require the authors to conduct follow up biological experiments, in the absence of such follow up, the conclusions should be toned down significantly.
