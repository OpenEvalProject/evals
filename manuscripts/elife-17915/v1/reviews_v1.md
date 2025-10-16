# Peer review - Round 1

Editors:
- Jonathan Flint, University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.17915.036](https://doi.org/10.7554/eLife.17915.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A genomic ageing program that reorganises the young adult brain is targeted in schizophrenia and anxiety disorders" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors create a new method to quantify transcriptome trajectory turning points (TTTP) and apply this to human BrainCloud dataset and a new mouse brain transcriptome dataset across ages 58-600 days. The authors identify a peak age of TTTP around 25-30 years old, which they link to psychiatric disorders (schizophrenia and autism) and synaptic development. Overall the reviewers felt that this was an ambitious analysis covering a novel and interesting topic (complex brain gene expression trajectories).

Essential revisions:

1) The text needs attention. The Introduction is long and meandering and would be more accessible if shortened significantly. The authors need to explain what they have done with greater clarity. For example the model the authors propose (subsection “Transcriptome trajectories and schizophrenia” paragraph three) is so vague as to be nearly meaningless.

2) The authors need to explain better which models they used and why. There are several algorithms presented in this work (TTTP, peget, DeGET, AliGET), of which only TTTP is straightforward. It is hard to understand why the authors choose to use one over the other. Some of the models (such as Aliget) include parameters that do not have a clear biological justification and seem somewhat arbitrary. Comparison of units across species is also unclear – is a human "year" equivalent to a mouse "day"?

3) Correction for multiple testing needs to be made explicit. For the cell type analysis a Bonferoni correction is used, but it is not clear that appropriate corrections were made for other analyses (the multiple different enrichment tests).

4) A list of >600 de novo mutation-containing genes is used. However, this is not a list of genes with any level of reasonable statistical support – what is the FDR? Are these all mutations in genes never observed in controls? The anxiety gene list is not well statistically supported and has no place in such an analysis.

5) Some of the models include a δ-E term, which "negates the contribution of genes that merely fluctuate away from their mean." The δ-E term also likely biases analysis toward genes with certain levels of baseline expression, as well as the dynamic range of microarrays. In addition, the gene fluctuation issue should be adequately accounted for by using spline regressions and biological replicates.

6) With regard to the age classifier, it is unclear if this is developed using a test set and validation set, which is necessary to truly evaluate accuracy that would be generalizable and meaningful. If it is not, they must find an independent validation set to make this of any meaning. In this regard, the cell type analysis does use a validation set for example.

7) All models are based on the TTTP point, which is defined as the earliest age in which the first derivative of expression changes signs. It is not clear why the authors only use the earliest of such points when genes can clearly have multiple inflections across the lifetime (see Figure 2—figure supplement 1). By taking the earliest inflection point, this makes the analysis somewhat contingent on youngest sample in a dataset (which is not balanced between mouse and human experiments), as well as the resolution of samples at the younger timepoints, which is sparse for BrainCloud (see below). Finally, all models are highly contingent on (1) the quality and resolution of the input datasets and (2) the accuracy of the spline regression model. As shown in the supplement, choice of regression parameters can have dramatic effects on downstream analyses. There is no justification for the cubic spline model used or any assessment of the accuracy with which it fits the underlying data. The choice of parameters seems arbitrary.

8) Gender differences – Using the Braincloud dataset, the peak age of TTTP is reported to be delayed in females compared to males and this is used as an explanation for why psychiatric diseases occur later in F. However, the Braincloud data that this result is based on has already had sex effects regressed out prior to analysis. It is inappropriate to make any comment on sex effect without using the non-regressed dataset.

9) Braincloud is used to define the human TTTP trajectory and includes human prenatal and postnatal samples. The regressed and normalized data is downloaded from GEO. However, it is unclear whether measures of RNA quality and other sources of technical variability are taken into account in any of the analyses. There will likely be an interaction between age and RNA quality and therefore potentially more variability in gene expression signal seen during certain timepoints. Replication in the Kang et al. (GSE25219) dataset will be important as this is similar to BrainCloud in scope.

10) The authors used the cubic splines with 3 DOF to depict the gene expression trajectories, and the TTTPs were detected by searching slope changing points along the smooth curves. How well does this actually fit the data? Why were 3 DOF chosen? There should be some rigorous assessment of accuracy of regression model (compared with Loess, etc)

11) The degree of smooth curve and the number of binned intervals could affect the number of identified TTTPs. But in subsection “Detecting turning points (TTTPs” the author said "If multiple turning points were found in a single spline, then only the first was used". This strategy may result in the imprecisely predicting TTTPs, e.g., the differences shown in Figure 4—figure supplement 2 when using different parameters and different methods.

12) Human-Mouse comparisons: the authors find a peak of TTTP around age 160 days in mice which they imply is equivalent to 26-30 years in human. However, mice were not assessed before 58 days postnatally whereas human time-points include prenatal brain samples. Since TTTP is calculated as the earliest transition point (if multiple are detected in the sample gene) it is likely sensitive to the age windows assessed.

13) Age differences – the peak age of TTTP is reported to be in the range of 25-30 years in human. However, there are a relatively few number of samples in the 2-20 age groups compared with age 0 and 20+. The ability to identity changes in transcriptomic trajectory during this crucial period of brain development is strongly unpowered and could confound the age trajectory of TTTP.

14) Psychiatric enrichments – subsection “Psychiatric susceptibility genes in young adults”, paragraph two: "TTTP.…accurately predicted the age windows for the onset of schizophrenia and anxiety disorders." As shown in Figure 5—figure supplement 3, this is highly contingent on parameter choice of the model used to fit transcriptome data. Loess regression or cubic spline with 4 dof predicts much earlier onset of schizophrenia (~16 year old). The choice of parameters does not seem to be justified either biologically or in terms of fit to the dataset. As such, this conclusion cannot be considered robust.

15) Cell-type enrichment analyses are likely on very small numbers of genes, which is susceptible to bias. The Zeisel dataset was used to define single cell transcriptomes. However, this dataset is based on single-cell RNAseq with <3000 genes expressed in each cell. Genes were dropped from analysis that were not expressed in Zeisel and therefore the input set of genes is likely very small.

16) The author claimed the accuracies of age prediction are 6.5 years in human and 28 days in mice. If this prediction included fetal samples, the prediction is imprecise. One similar age prediction from DNA methylation reported the predicting difference is close to zero for embryonic samples (Genome Biology 2013, 14:R115). If this prediction did not include fetal samples, the authors should not state that, "Remarkably, they showed accurate age predictions across the entire range of ages in both species," as Braincloud includes 38 fetal samples. Similarly, the authors should make clear that they excluded these samples, and, in light of the dramatically higher temporal dynamics observed in fetal and infant periods in these samples (Nature 478, 519-523, Figure 2B), why they excluded these samples.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A genomic ageing program that reorganises the young adult brain is targeted in schizophrenia and anxiety disorders" for further consideration at eLife. Your revised article has been favorably evaluated by a Senior editor, a Reviewing editor, and one reviewer.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #1:

In my original review, I was very enthusiastic about the innovative approach and ideas contained in this paper, but was concerned about Methods and potential confounders, which were hard to understand and evaluate in the original paper. The other reviewer had very similar concerns. The authors now provide a detailed response to the critiques and a revised manuscript, which is much improved. They have rewritten, shortened many sections and improved clarity. They have done a good job of clarifying parameter choice and for some of algorithms, and shown the robustness of the methods to these choices.

I should emphasize that I still have my original enthusiasm about this innovative study. But although some of my concerns are well addressed, others regarding the robustness of the method and interpretation of the data are not and still need additional work. Because this study could illuminate some areas of disease susceptibility that have been mysterious, it could have high impact, but it is critical that it be methodologically solid in every respect. I think it is now believable that young adult is a time of interesting changes in gene expression trajectories, although as the authors acknowledge choice of spline parameters effects the actual age considerably. This is not a minor concern that needs acknowledgement, but a key point of their analysis. Better if the authors presented an interval of TTTP ranges based on parameter choices just to show what we can be certain about from these data. The major question that still remains is how is this related to disease specific factors.

Other concerns are as follows:

1) The main focus on the paper is defining transcripome trajectory turning points, which they then relate to disease. They have clarified the use of algorithms and Methods. Now that some of these issues are clarified, one major question still remains. If the TTTP indeed does define SZ onset at late adolescence with a peak at 25 years (although with some range depending on parameters chosen as mentioned above), it should be specific to schizophrenia and not to other disorders. The choice of gene sets to be compared is critical here, and in no way are the genetic studies of the brain disorders that are compared comparable. Some identify mostly common variants of small effect size, and others, such as ID and autism, mostly rare variants with large effect size. These mutations are under considerably different selection pressures as their effects sizes differ.

So, a major problem that still remains is that the choice of the 600 SZ de novo genes is not well supported by statistical genetic analysis. The authors’ response to this in the revision is not satisfactory. There is strong support for de novo mutations as a class in SZ and other neurodevelopmental disorders, and some pathways, more equivocally. But, the individual genes in this list are mostly not supported by evidence yet. It is not a question of finding mutations that occur only in SZ patients and not in controls; it is standard population genetics. de novo mutations occur frequently and many of these genes are almost certainly not risk genes. The authors should absorb some of the analyses in the following papers and should filter the list by metrics that are now well accepted in human genetics (PMID:27899611; PMID:25086666; PMID: 27535533; PMID:27533299; PMID:26439716; PMID:25684150).

Also in this regard, genome-wide significant genes for anxiety disorders have not been identified. Again, the use of a hodge podge of gene lists, without strong statistical support or rationale plagues this major aspect of the paper. The choice of gene lists is so important that it should be presented up-front and clarified. And when comparisons are made with these lists, they should be of equal power, or they don't support disease specificity. In other words, the gene lists should be the same size approximately, or better yet, account for a similar proportion of the population attributable genetic liability to account for the different effect sizes of mutations and common variants. Further, anxiety should certainly not be used at all, unless the authors can provide genome-wide statistical support for the genes identified.

If the authors want to use this SZ list of 600 genes that lacks statistical support or OR for most of the genes, they should definitely compare to a similarly filtered of genes that cause autism and intellectual disability, or list of brain enriched genes (2/3 fold?) to see if the trajectory that they see in SZ is meaningful, as mentioned above. In the gene lists there are 2- 3x more SZ genes than ASD genes (one list has 170, the other about 380), and there are only about 80 ID genes listed, when there are >400 known. At least the sensitivity of the TTTP analyses to the size of the gene list should be provided. Another ground truth would be to show that a similar sized list of PSD genes, or highly synaptically enriched genes not chosen for association with SZ did not show the same pattern. It simply may be that certain classes of synaptic genes are enriched for this pattern of trajectory switching and this creates a vulnerable period, but it is not due to an enrichment of SZ risk genes themselves.

3) The human-mouse comparison is really a tough area as the authors recognize, since it has been demonstrated that there is not a linear, constant scaling of stage comparability between these species across development when specific developmental processes are compared. The authors should at least cite some of the work that demonstrates this and discuss it more thoroughly as a caveat. Currently it is somewhat glib. They have done a very good job of dealing with this issue analytically, but the readers should know that it is a biological conundrum that is tough to address with any method mapping human development to mouse, and what the limitations are.
