# Peer review - Round 1

Editors:
- Matt Kaeberlein, University of Washington United States

Reviewers:
- Wolfgang Wagner, RWTH Aachen University Germany
- Peter Adams, Beatson Institute United Kingdom

## Review text

DOI: [10.7554/eLife.40675.046](https://doi.org/10.7554/eLife.40675.046)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A whole lifespan mouse multi-tissue DNA methylation clock" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Peter Adams (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers appreciated the value of the whole lifespan mouse multi-tissue DNA methylation clock (WLMT clock) and agree in principle that this is suitable as an eLife Tools and Resources article. Some concerns were raised however, and after consultation, we have identified several places where the manuscript could be improved. Most notably, all three reviewers felt that it is important to show how well the WLMT clock performs on additional data sets that have not been pre-selected to include all of the clock CpGs. The authors also must confirm that the raw data have been deposited at GEO and provide the GEO ID or a reviewer access link.

Essential Revisions:

1) While the WLMT clock performs well on samples from the test and training sets the precision appears to be much lower on other samples. This is probably due to the fact that not all of the relevant 435 clock sites are covered in these completely independent samples (while the test set was preselected to cover all 435 sites). The authors should assess how the WLMT performs on completely independent datasets. Furthermore, the authors should describe how to adjust for missing clock sites. Otherwise the method won't be useful for other researchers to apply to new datasets. Perhaps some new datasets could be generated or publicly available datasets should be used to address this important issue.

2) A major question about the novel clock is how it differs from other clocks. There are a couple of additional analyses that should be performed to address this important question.

a) The authors should compute correlations among the different epigenetic clocks and also among their age-acceleration-residuals/delta-age values (i.e. the difference between epigenetic age and chronological age).

b) Comparison of the WLMT clock with other clocks was done with different subsets of samples since almost all samples turned out to be included into one or another clock training set. However, for a fair comparison only completely independent datasets from different tissues should be used.

3) The most important results in the paper are contained in Figure 4, and these are not very easy to interpret from the graph or the accompanying text. Most interest in epigenetic clocks is driven by the hypothesis that differences between epigenetic age and chronological age (called "delta-age" or "epigenetic age acceleration residual", depending on how computed) reflect processes of biological aging. The authors present tests of this hypothesis in Figure 4 by comparing delta-age values of mice exposed to different longevity-enhancing or mortality-risk-increasing interventions. The result of this analysis is that the blood-based clock often shows differences in delta-age values, whereas results are less consistent for other clocks. This result is not transparent from the figure nor is it all that transparent from the text. It needs to be clarified. For example, it would be easier to see the result if the intervention and control group data for each clock were presented side by side so the visual comparison suggested by the figure matched the statistical analysis performed.

4) There are several places where it was felt that the authors overstate or overinterpret their results. Please correct these as suggested:

a) The authors state that Figure 3A is "is biased towards a better performance of the other clocks because the biological ages of a combination of their test and training samples are estimated, thus artificially improving apparent performance", whereas WLMT is only measured against its test set (not its training set). I think this may underestimate the inter-lab qualitative variations in RRBS datasets. One reason the human clocks work so well across datasets is, I think, the high technical consistency of the Illumina arrays between labs. WLMT is compared to RRBS data generated largely in the same lab, while the other datasets are compared to WLMT data generated in a different lab. The inter-lab comparisons my bias against the other clocks due to qualitative variations in RRBS data between labs. RRBS in different labs likely has different coverage of different CpGs, for example. Hence, I think this statement should be moderated.

b) The authors state "DNAm clocks remain the most precise markers of biological age". I think here the authors mean "chronological" age not "biological" age. First, in the Introduction the authors support this statement by reference to measures of chronological age, not biological age. Second, there is no consensus as to how to best measure biological age, so it is an overstatement to say that DNAm clocks are the best. Chronological and biological age are not the same and the terms should not be used interchangeably.

c) The statement that "DNA methylation is a relatively new evolutionary mechanism to control gene expression; among animals, it appears in vertebrates […]" (Discussion paragraph two) is not covered by Lokk et al., 2014 and it might not be correct.

d) The authors indicated that "the constructed multi tissue DNAm clock can also be applied to mice of different genetic backgrounds" (Discussion final paragraph), but this has not been systematically analyzed in this study.

e) The authors assert their multi-tissue clock is unique from previous tissue specific clocks partly on the basis that few of the CpGs included in the multi-tissue clock are included in tissue-specific clocks (Discussion paragraph two). The elastic net run on the same data against the same criterion with slightly different parameters may select different CpGs from one run to the next. The question is whether the different CpGs are more or less statistically independent of one another. The authors should test this if they wish to make claims about the uniqueness of the CpGs in their multi-tissue clock or the discussion should be appropriately modified.
