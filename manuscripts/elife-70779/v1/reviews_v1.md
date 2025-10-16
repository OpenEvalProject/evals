# Peer review - Round 1

Editors:
- Genevieve Konopka, https://ror.org/00t9vx427 University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70779.sa0](https://doi.org/10.7554/eLife.70779.sa0)

This manuscript describes a new method of identifying disease-relevant risk genes from genome wide association studies by using a conditional gene-based method (named eDESE). The authors apply this new approach in an analysis of schizophrenia datasets, and identify meaningful biological processes and potential drug repurposing candidates. Thus, this new method could provide improved gene prioritization for fine-mapping and functional studies of specific diseases.


---

# Peer review - Round 1

Editors:
- Genevieve Konopka, https://ror.org/00t9vx427 University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70779.sa1](https://doi.org/10.7554/eLife.70779.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "MCGA: a multi-strategy conditional gene-based association framework integrating with isoform-level expression profiles reveals new susceptible and druggable candidate genes of schizophrenia" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Molly Przeworski as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Systematic comparisons with existing methods are needed to demonstrate the potential gain in biological insight from this method. How do the results from MGCA_Dist, MGCA_eQTL, and MGCA_isoQTL compare with MAGMA? Can you include a direct comparison of MGCA with MAGMA, including the gene-based results, biological pathway enrichments, and drug repositioning analyses? Can the authors compare MGCA_eQTL to other eQTL-based approaches such as S-PrediXcan?

2) When comparing MCGA-eQTL and MCGA-sQTL, only power is considered. The authors should include analyses to demonstrate the performance in control for false positives.

3) When choosing a favorable exponent value c (1.432 chosen in the study), the authors found that the c value is robust to trait type, sample size or variant size, but the authors didn't explain what factors affect the choosing of c. Considering the potential application of MCGA method in other studies, the authors should explain what factor affects c value, and provide the guidance how to choose an optimal c. Can the authors show via simulations the relationship between the coefficient used to adjust the chi square statistic correlations, $c$, and the strength of association signals?

Reviewer #1 (Recommendations for the authors):

– How do the results from MGCA_Dist, MGCA_eQTL, and MGCA_isoQTL compare with MAGMA? Can you include a direct comparison of MGCA with MAGMA, including the gene-based results, biological pathway enrichments, and drug repositioning analyses?

– Similarly, can you compare MGCA_eQTL to other eQTL-based approaches such as S-PrediXcan? I would like to see a systematic comparison with existing methods to see if novel biological insights can be derived from your results.

– Does MCGA provide information on tissue-specific eQTLs/isoQTLs? This information is available in GTEx but is not reported for association results in supplementary tables. Tissue-specific effects for each tissue might improve the interpretation of results.

– Can you provide more information on WGCNA results? Are MCGA susceptibility genes enriched in a particular co-expression module? Are synaptic signalling related biological pathways enriched in a particular module? How did the network modules compare across brain tissues? Is it possible to build a consensus network for the top five brain regions (or indeed all brain regions in GTEx) to simplify the results?

– The drug repositioning analysis could be improved by drawing on comprehensive drug-gene information from hetionet (https://doi.org/10.7554/eLife.26726.001). This resource might further refine some of your top associations by accounting for anatomies, biological processes, side-effects, and symptoms.

Reviewer #2 (Recommendations for the authors):

GTEx v8 data contains samples from multiple tissues, and the significant gene-trait association in some tissue may be non-causal driven by gene expression correlation with causal tissues. It should be interesting to come up a new method to remove those false positive.

Reviewer #3 (Recommendations for the authors):

My major concern is a lack of innovation as a new method. MCGA is based on DES, which integrates expression data with GWAS; and DESE relies on ECS to compute gene-level association evidence. Both DESE and ECS were developed by the authors in the past and published elsewhere. The only innovation in the MCGA methodology seems the improved control of type I error by formally assessing the null distribution of the conditional test statistic for ECS and adjust the test statistic. This improvement is definitely crucial to ECS. But in my view, this is a fix to a long standing issue of ECS rather than a new method in itself. Even with this improvement, the ECS is still not a completely statistically solid method because it still involves heuristic procedures to determine how much the ECS statistics should be adjusted. There is still no methodological guarantee of controlled type I error.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A conditional gene-based association framework integrating isoform-level eQTL data reveals new susceptibility genes for schizophrenia" for further consideration by eLife. Your revised article has been evaluated by Molly Przeworski (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #3 has 2 remaining issues that we would like you to more fully address before we would consider accepting the manuscript. Please read these comments carefully and revise accordingly. Thank you.

Reviewer #1 (Recommendations for the authors):

I would like to thank the authors for their detailed response to my questions and concerns. I have no further comments on the manuscript.

Reviewer #2 (Recommendations for the authors):

The authors have resolved all my concerns. Nice job.

Reviewer #3 (Recommendations for the authors):

The revised manuscript was submitted in PDF format with track changes. Although it clearly shows what's been changed since the original submission, it is therefore very difficult to read the complete article for a second overall assessment. I will therefore focus on comments I raised in my first review.

Two major issues remain.

1. The authors failed to respond properly to my comment on the overall concern that conditional analysis may not be the best approach for this type of problem. Figure 1 of SuSiE paper illustrates the exact scenarios why this could be a bad idea, which motivated my A-B-C genes example. Also incidentally, it is not true that SuSiE cannot work with summary statistics.

2. The response to the question of the choice of c (from another reviewer and myself) is still not satisfactory. It seems the favorable c still was computed in very specific scenarios. In fact, the new Figure 9 exactly demonstrates my concern: optimal choice of c depends greatly on LD and effect size, and for variants with small effects (OR < 1.4 which would be the case for most GWAS signals) the range of optimal c is wide. Given this result, I remain unconvinced that the tests are calibrated under current choice of c. From Figure 9 I would conclude that a conservative c = 1.8 should be used in general, which is different from the recommended choice from the authors.
