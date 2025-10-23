# Peer review - Round 1

Editors:
- Christian R Landry, Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62669.sa1](https://doi.org/10.7554/eLife.62669.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors devised a new approach based on oligo synthesis, a transcriptional reporter and barcode sequencing to identify likely causal variants underlying cis regulatory variation in yeast. The results show that some promoter regions often have multiple SNPs affecting gene expression. The authors find that some of these regulatory SNPs show epistatic interactions and that natural selection may keep regulatory SNPs at low frequency in natural populations. SNPs affecting gene expression are enriched in known transcription factor binding sites. This study is a spectacular example of how the combination of emerging and established technologies can be exploited to gain a refined picture of genotype-phenotype maps and this, genome wide.

Decision letter after peer review:

Thank you for submitting your article "Massively parallel identification of causal variants underlying gene expression differences in a yeast cross" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The authors devised a new approach based on oligo synthesis, a transcriptional reporter and barcode sequencing to identify causal variants underlying cis regulatory variation in yeast. The results show that some promoter regions often have multiple SNPs affecting gene expression. The authors find that some of these regulatory SNPs show epistatic interactions and that natural selection may keep regulatory SNPs at low frequency in natural populations. SNPs affecting gene expression are also enriched in known transcription factor binding sites.

The three reviews are highly positive. However, for the paper to be considered further, it would be important to perform some additional analyses and revise some of the interpretations of the results. This is particularly the case for some of the recommended analyses aimed at disentangling the relationships between different factors associating with regulatory SNPs because these often covary. If it is impossible to completely estimate their independent contribution, this issue should at least be addressed in the Results and Discussion.

I have kept the three full reports below because they are complementary and well detailed. We expect no additional experiments at this point.

Reviewer #1:

This study investigates the molecular origin of differential transcription in the well-studied BY-RM cross. SNPs and indels in promoters between these two strains were reciprocally exchanged in order to measure their effects by sequencing barcoded transcripts. The authors use this method to do a deep dive into the genetic determinants of local eQTLs, in which they identify causal variants and give examples of proximal variants with non-additive interactions. They also explore the nature of the causal variants and work to predict variants and expression. In my opinion, this article is very well written, well measured, well explained, and well thought through. I have no major comments.

Reviewer #2:

The paper by Renganaath et al. uses a reporter assay and Illumina sequencing to estimate the effects on gene expression of thousands of naturally occurring promoter variants between two yeast strains. They identify a large number of variants that have significant effects on expression, greatly expanding the catalog of known individual regulatory variants. They use this catalog to test long standing ideas about the molecular and evolutionary nature of these regulatory variants. Overall, the experiments use a good design with the necessary controls and replication to identify variants with moderate and large effects on gene expression. In general I think the work makes a good contribution to the field and I only have a few comments and concern about the models used and the strength of the conclusions made from these models.

1) First, the authors have a number of potential explanatory variables and test each one individually for association with whether a variant significantly alters gene expression or not. The results from these regression analyses are taken as is, with no attempt to account for correlations among the factors themselves. The authors seem to be aware of this issue; one of the largest individual correlates is gene essentiality which the authors note is often associated with some of the other covariates used. Because of this issue, significant associations cannot be interpreted as meaning a particular covariate is important, and causal connections can't be made from this kind of analysis. Furthermore, the authors take a number of significant covariates and interpret them as being consistent with negative selection, but whether these covariates are all significant once others are accounted for is unknown. The different covariates may be detecting similar signals, in which case they are not independent. A more comprehensive modeling scheme would allow the most important covariates to be identified and lead to a better understanding of what signals actually exist in the data. For example, using regularization techniques (which the authors do use later in another analysis) on a model including all of the covariates would help to avoid non-independent covariates.

2) Similar arguments can be made for the regression analyses that incorporate transcription factor binding; the PWMs of TFs are not independent and many have similarities due to similar modes of binding. In addition, the data does not clearly show 'evidence that causal variations often perturb TF binding'. Instead, the data shows that variants predicted to alter the binding of TFs are correlated with whether a variant is causal. Again, direct causality from this type of analysis is difficult to do. This is made even more difficult to follow with the “weak” TF binding as it appears that the authors are arguing for a model where individual single nucleotide variants affect expression by altering the binding of multiple TFs, each of which has a low individual probability of being bound. While it is well known that many weak TFBS are present in DNA, I'm not familiar with changes to these weak TFBS being proposed in the literature as a major route by which gene expression is altered in nature. Two things could help make this claim stronger. First, it would help to see a clear example that was found in the data, e.g. of a causal variant that was predicted to alter a single strong TFBS and one that was predicted to affect multiple weak TFBS. Second, functional validation of some of these variants as affecting the predicted TF binding (and not some other, unknown and untested factor) would significantly increase the impact of this section. This later route would likely require substantial effort, but at the very least, that such functional analysis has not been done needs to be recognized and the claims moderated in this section.

Reviewer #3:

Renganaath and colleagues described a high-throughput assay for testing how natural genetic variants influence gene expression, as well as finding patterns that allow us to predict such effects. The main novelty of their approach is in its single-variant resolution. Other methods such as eQTL mapping and allele-specific expression (ASE) do not have this level of resolution, so MPRA is a valuable addition to the yeast genetics toolkit. The ability to test epistatic interactions of neighboring variants is also a nice feature.

1) The role of individual variants in contributing to ASE is key to understanding cis-regulatory logic. The authors designed MPRA oligos focusing on previously identified ASE genes and added randomly selected genes as controls. It would be interesting to see an aggregated statistic on whether ASE genes are more likely to harbor causal variants than non-ASE genes; and if upstream variants differ from TSS variants in such patterns.

2) Prediction of causal regulatory variants is a holy grail of functional genomics. In this study, the predictions show slightly (but significantly) better than random performance. It is worth noting that there are more non-causal variants that causal variants, resulting in imbalanced classification problem. Oversampling of the minority labels could be a good start to balance data distribution and improve prediction performance.
