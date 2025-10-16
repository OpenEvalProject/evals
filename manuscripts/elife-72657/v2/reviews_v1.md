# Peer review - Round 1

Editors:
- Francesca Di Giallonardo, https://ror.org/03r8z3t63 University of New South Wales Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72657.sa0](https://doi.org/10.7554/eLife.72657.sa0)

The study by Magosi et al., evaluates the impact of targeted public health interventions on the HIV-1 transmission rate in Botswana. Using data from a large trial in Botswana, the authors found that HIV-1 transmission was more common to occur from control population groups into targeted population groups than vice-versa. The study is of public health interest, showing how some public health interventions are powerful in reducing HIV-1 transmission but only among the population targeted. This is a very comprehensive research study showing the advantages of using deep sequencing data in combination with phylogenetic tools to assess the positive impact of public health interventions in reducing HIV-1 transmission.


---

# Peer review - Round 1

Editors:
- Francesca Di Giallonardo, https://ror.org/03r8z3t63 University of New South Wales Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72657.sa1](https://doi.org/10.7554/eLife.72657.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Deep-sequence phylogenetics to quantify patterns of HIV transmission in the context of a universal testing and treatment trial – BCPP/ Ya Tsie trial" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Miles Davenport as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nadine Tschumi (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Overall, we think the study was well designed and using a large sample size is highly valuable. The study provides detailed information on the methods including the release of a new R package for calculating transmission flow among populations. This is highly valuable for the interpretation of public health interventions, particularly test-and-treat. However, we all agree that it is important to add some clarifications of the methods used.

1) The authors use a combination of HIV-TRACE and Cluster Picker as tools for cluster identification. As such, the authors implement a genetic threshold of 4.5% genetic diversity. This is the core outcome of the study; all the subsequent analyses are depended on the clusters identified. HIV-TRACE is often used instead of a phylogenetic tree, as the latter can be computational time-consuming with large data sets. However, the study also estimates a phylogenetic tree, thus we wish for more clarification on why both methods were used and how different the cluster outcomes are with each method.

2) The cluster analysis resulted in many infection pairs between same-sex couples, indicating missing data in the transmission chains. The study excluded these pairs from subsequent analysis, resulting in a small number of overall pairs for the final transmission flow count. We think that such 'missing link' pairs could still be included in the analysis of estimating transmission flow between geographic regions. We were wondering if the study has investigated this and believe a constructive discussion in that regard could be favorable. See comments of reviewer 2.

3) We agree that the study is overall well-presented and well-written, however, we think it would be useful to clarify some of the methods in the main text. We also agreed that the figures were overall informative and useful, however, we believe that some of the illustrations could be improved to aid with the understanding of the results. See comments of reviewer 3.

Reviewer #1 (Recommendations for the authors):

1. I think my concerns 8-11 above could be relatively easily addressed by sensitivity analyses showing that a change in respective definitions did not affect the main outcomes qualitatively.

2. The estimated proportion of HIV transmissions in the trial population flowing into intervention communities from control communities and vice-versa was a key finding of the manuscript. Since the number of probable transmission pairs is low, the confidence intervals are wide and overlapping. I appreciated / think that it is important and correct that you only considered probable transmission pairs for the age gap analysis. However, for this analysis I wouldn't see a problem for including pairs with probable unsampled intermediates. Was this attempted / why not?

Reviewer #2 (Recommendations for the authors):

The methods describing the initial sequence quality control and alignment need to be expanded. Currently, it is unclear how the shiver assembly software was run. While the sequencing and bioinformatics pipelines used here have been used in previous studies the possible impact of sequencing errors should be discussed. Ideally, replicates would be used to determine the expected rate of sequencing errors. However, other approaches such as the proportion of minority variants at different coding locations for different variant frequency cutoffs could also be used (Dyrdak et al., 2019). This is particularly important given that most trial participants were virally suppressed which could impact the overall quality of the sequencing data.

Much of the downstream analysis and results relies on the initial separation of sequenced samples into putative transmission clusters. As a result, the choice of the 4.5% genetic distance threshold and the decision to combine the results of HIV-trace and cluster-picker needs much stronger motivation. This is particularly so as Supplementary Figures 7 and 8 suggests that the two methods give quite different results. Whilst I realise cluster picker is commonly used, HIV trace does not rely on the accuracy of a provided phylogeny and as the following transmission analysis only considers pairwise relationships, HIV trace seems more appropriate.

I may have misunderstood but the method for calibrating the false discovery rate (FDR) for the inference of direct transmission described in Supplementary note 3 appears to consider all pairwise relationships (equation 6). This would only be possible if a person was able to be infected by multiple different transmitters. Assuming that the authors have only considered a single transmitter per infection then this would lead to an overestimate of the FDR. This should be clarified in the text.

Finally, it would be useful if the authors could discuss what impact high risk communities such as sex workers could have on these results and the estimates of intercommunity transmission.

– Many of the methods are described in the supplementary materials which makes the interpretation of the results challenging. The manuscript would be improved by moving some of the supplementary methods into the main text.

– The command line parameters used to run MAFFT and HIValign should be provided.

– While I was able to successfully download and install the 'bumblebee' R package I could not get a small trial example to run. Example data and a short 'how to guide' should be included as part of the package.

– Figure 7 is quite confusing and I think relatively little is gained by the use of an alluvial plot. I think it would be clearer to separate this plot into multiple bar plots of the total number of transmissions rather than the proportion within each category.

– It would be better to combine Figures 9 and 10 into a multi panel figure

– Lines 177, 184, 216, 219, 279, 342, 345 etc: The multiplication symbols look like a variable and should be removed.

– Line 262: I think this should say that the Goodman method estimates CIs for the parameters of the multinomial distribution.
