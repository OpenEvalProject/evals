# Peer review - Round 1

Editors:
- Nicholas Mancuso, University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91360.2.sa0](https://doi.org/10.7554/eLife.91360.2.sa0)

In the last 15 years, large-scale association studies (GWAS) have served to estimate the association between genome-wide common variants and a large number of disparate traits and diseases in humans. This valuable method provides a new way to find correlations between the genetic component of a phenotype of interest, and all this wealth of genetic information. This software adds as a new tool to investigate genetic correlation between traits, and to generate new mechanistic hypotheses and dissect the role of the observed associations in disease heterogeneity. The results of the application of their method are solid and generally agree with what others have seen using similar AD and UKB data.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91360.2.sa1](https://doi.org/10.7554/eLife.91360.2.sa1)

The major aim of the paper was a method for determining genetic associations between two traits using common variants tested in genome-wide association studies. The work includes a software implementation and application of their approach. The results of the application of their method generally agree with what others have seen using similar AD and UKB data.

The paper has several distinct portions. The first is a method for testing genetic associations between two or more traits using genome-wide association tests statistics. The second is a python implementation of the method. The last portion is the results of their method using GWAS from AD and UK Biobank.

Regarding the method, it seems like it has similarities to LDSC, and it is not clear how it differs from LDSC or other similar methods. The implementation of the method used python 2.7 (or at least was reportedly tested using that version) that was retired in 2020. The implementation was committed between Wed Oct 3 15:21:49 2018 to Mon Jan 28 09:18:09 2019 using data that existed at the time so it was a bit surprising it used python 2.7 since it was initially going to be set for end-of-life in 2015. Anyway, trying to run the package resulted in unmet dependency errors, which I think are related to an internal package not getting installed. I would expect that published software could be installed using standard tooling for the language, and, ideally, software should have automated testing of key portions.

Regarding the main results, they find what has largely been shown by others using the same data or similar data, which add prima facie validity to the work The portions of the work dealing with AD subgroups, pathology, biomarkers, and cognitive traits of interest. I was puzzled why the authors suggested surprise regarding parental history and high cholesterol not associated with MCI or cognitive composite scores since the this would seem like the likely fallout of selection of the WRAP cohort. The discussion paragraph that started "What's more, environmental factors may play a big role in the identified associations." confused me. I think what the authors are referring to are how selection, especially in a biobank dataset, can induce correlations, which is not what I think of as an environmental effect.

Overall, the work has merit, but I am left without a clear impression of the improvement in the approach over similar methods. Likewise, the results are interesting, but similar findings are described with the data that was used in the study, which are over 5 years old at the time of this review.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91360.2.sa2](https://doi.org/10.7554/eLife.91360.2.sa2)

Summary:

Yan, Hu, and colleagues introduce BADGERS, a new method for biobank-wide scanning to find associations between a phenotype of interest, and the genetic component of a battery of candidate phenotypes. Briefly, BADGERS capitalizes on publicly available weights of genetic variants for a myriad of traits to estimate polygenic risk scores for each trait, and then identify associations with the trait of interest. Of note, the method works using summary statistics for the trait of interest, which is especially beneficial for running in population-based cohorts that are not enriched for any particular phenotype (ie. with few actual cases of the phenotype of interest).

Here, they apply BADGERS on Alzheimer's disease (AD) as the trait of interest, and a battery of circa 2,000 phenotypes with publicly available precalculated genome-wide summary statistics from the UK Biobank. They run it on two AD cohorts, to discover at least 14 significant associations between AD and traits. These include expected associations with dementia, cognition (educational attainment), and socioeconomic status-related phenotypes. Through multivariate modelling, they distinguish between (1) clearly independent components associated with AD, from (2) by-product associations that are inflated in the original bivariate analysis. Analyses stratified according to APOE inclusion show that this region does not seem to play a role in the association of some of the identified phenotypes. Of note, they observe overlap but significant differences in the associations identified with BADGERS and other Mendelian randomization (MR), hinting at BADGERS being more powerful than classical top variant-based MR approaches. They then extend BADGERS to other AD-related phenotypes, which serves to refine the hypotheses about the underlying mechanisms accounting for the genetic correlation patterns originally identified for AD. Finally, they run BADGERS on a pre-clinical cohort with mild cognitive impairment. They observe important differences in the association patterns, suggesting that this preclinical phenotype (at least in this cohort) has a different genetic architecture than general AD.

Strengths:

BADGERS is an interesting new addition to a stream of attempts to "squeeze" biobank data beyond pure association studies for diagnosis. Increasingly available biobank cohorts do not usually focus on specific diseases. However, they tend to be data-rich, opening for deep explorations that can be useful to refine our knowledge of the latent factors that lead to diagnosis. Indeed, the possibility of running genetic correlation studies in specific sub-settings of interest (e.g. preclinical cohorts) is arguably the most interesting aspect of BADGERS. Classical methods like LDSC or two-sample MR capitalize on publicly available summary statistics from large cohorts, or having access to individual genotype data of large cohorts to ensure statistical power. Seemingly, BADGERS provides a balanced opportunity to dissect the correlation between traits of interest in settings with small sample size in which other methods do not work well.

Weaknesses:

However, the increased statistical power is just hinted, and for instance, they do not explore if LDSC would have identified these associations. Although I suspect that is the case, this evidence is important to ensure that the abovementioned balance is right. Finally, as discussed by the authors, the reliance on polygenic risk scoring necessarily undermines the causality evidence gained through BADGERS. In this sense, BADGERS provides an alternative to strict instrumental-variable based analysis, which can be particularly useful to generate new mechanistic hypotheses.

In summary, after 15 years of focus on diagnosis that would require having individual access to large patient cohorts, BADGERS can become an excellent tool to dig into trait heterogeneity, especially if it turns out to be more powerful than other available methodologies.
