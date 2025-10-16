# Peer review - Round 1

Editors:
- Sara Hägg, Karolinska Institutet Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59479.sa1](https://doi.org/10.7554/eLife.59479.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper by Jansen et al. investigates somatic and mental health using molecular substrates from the same individuals to create five different multi-omics biological aging clocks. This is exactly the kind of data needed to advance the field and to understand how different layers of data can be integrated to understand biological aging processes.

Decision letter after peer review:

Thank you for submitting your article "An integrative study of five biological clocks in somatic and mental health" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Sara Hägg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jessica Tyler as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Daniel W Belsky (Reviewer #2); Erik van den Akker (Reviewer #3); David G Le Couteur (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this article, Jansen et al. take some steps toward addressing a knowledge gap on different molecular data used to derive biological aging clocks. They train algorithms to predict chronological age based on several molecular substrates assayed from blood samples: DNA methylation, gene expression, metabolomics, proteomics, and also telomere length. They then test correlations among the several derived measures and compare their associations with various exposures and criterion endpoints relevant to the aging process. The main finding is that the age-correlated features of the different substrates are (a) not very well correlated with one another and (b) largely non-overlapping in their information about health and exposure history. The authors also show that combining information across substrates produces a superior measurement as compared to substrate-specific measures.

Revisions for this paper:

1) Using established clocks

The authors talk about the problem of using their results in other studies since the omics platforms are not always available in other cohorts. It is not clear why it was necessary to train the algorithms in the NESDA cohort. There are published "clocks" for all of the substrates analyzed here (many examples are cited in the Introduction). For example, is there any way that the authors can calculate some of the standard epigenetic clocks (Horvath, Hannum, PhenoAge, GrimAge etc) perhaps not using the online calculator but using standalone scripts for these clocks adapted to your data format? Then, the results would be much more interesting for a wider audience and generalizable to other studies as well. The manuscript would be substantially stronger if these clocks were used in place of bespoke versions derived from the data used for testing hypotheses. If it is not feasible to implement published clocks in the NESDA data, this needs to be explained to the reader.

2) Comments on the algorithms used

If established clocks cannot be used, the alternative strategy of training and testing clocks within a single dataset needs to be presented as the alternative along with specific acknowledgement of the limitations of this approach. The Ridge-regression method used to train the clocks requires the assumption that patterning of molecular markers across the chronological age distribution in the sample reflects biological changes that occur with aging. That assumption has important limitations in any sample, for example see Nelson et al., 2020 on mortality selection or discussion of cohort effects in Belsky et al., 2015 or 2020 . But, depending on how age relates to sampling in the NESDA, there could be further challenges here.

Please also specify whether the feature selection for CpGs/genes was done on the whole dataset, prior to cross-validation, or within the cross-validation loop. If the first, this would lead to reporting overoptimistic performances (overtraining), if the latter, OK; please state so in the manuscript. Please also indicate what step size was used.

Would Mahalanobis distance be a better/more interesting way of analysing the data (eg Bello and Dumancas, Curr Aging Sci, 2017)?

A further consideration to be addressed if the NESDA data are to be used in training the "clocks": prediction of chronological age is only one criterion endpoint used to develop biological aging measures. Recent DNA methylation algorithms including the PhenoAge Clock and the GrimAge Clock were developed from analysis of physiology and mortality data along with chronological age. Some acknowledgement is needed that chronological age is only one of several potential criteria on which to train these measures.

Finally, algorithms trained by applying machine learning analysis to fit high-dimensional molecular data to chronological age variation are hypothesized to measure biological processes of aging. But this is a hypothesis, not a fact. Before we can interpret a "clock" as a measure of biological aging, we must establish that it changes with advancing age, forecasts disease, disability, and mortality, and indicates more advanced/delayed aging in individuals with exposure histories linked to shorter/longer healthy lifespan. The authors should be commended for undertaking some of this testing in NESDA, although using established clocks would be a better alternative. Hence, caution is warranted in interpretation of findings.

3) The NESDA cohort

More detail on NESDA is required to help the reader understand its appropriateness as a setting for comparing measures of aging. How was the sample selected? When were biological measurements collected and what was the extent of attrition from the baseline sample at those time points? In addition, it is not clear when the various exposure and health outcome measurements were collected relative to the biological measurements used to compose the clocks. For each participant, were all the analyses done in a blood sample taken at the same time, or were the different methods applied to bloods taken at different times? How long ago were the samples taken? Are there any storage effects that might influence analyses? A figure illustrating the timeline of data collection would greatly improve clarity of the analysis design.

4) The composite index

The composite index of the 5 clocks was a nice addition to the results. Ideally, clocks, including the composite, are scaled prior to associations with outcomes, as effect sizes are directly compared in the paper. Please indicate whether this has been done; if not, evaluations should be made on the basis of significance only, if so, great! Please state so in the Materials and methods.

Would the results have been similar if the 5 clocks were used combined in multivariate models instead? For example, what happens when all five clocks are put in the same model as predictors with BMI as health outcome? Will they all still be important in the association or are some redundant? Alternatively, it might be useful to compare the current operationalization of the multi-substrate composite to one derived from a factor analysis instead. This is information that is useful to understand the stability of the results but now somehow missed using only one composite index.

5) The Results

The biggest concern with the study is the generalizability given that the samples come from a clinical cohort with individuals suffering from depression and anxiety disorders. About 26% of the study participants were healthy controls and should then be representing a more general population. Moreover, age range is 20-65 years, so probably misses the age groups where biological changes of old age become dominant. Different participants were analysed for each biomarker, and there was a full dataset on only a fraction (approx. 1/3) of the participants that had individual tests done. Any data on ethnicities in NESDA? It is important to perform sensitivity analyses in selected groups of NESDA addressing these concerns in all associations and conclude if the effects are similar or changed in any important way. This also needs to be addressed in the Discussion section.

Another issue is the direction of effects, since these samples and associations are based on cross-sectional data, the authors correctly state that no conclusion can be made on the cause and consequence pathways. However, the biological clocks are used as outcomes in the linear regression models, why? For somatic health and chronic conditions, these are often treated as outcomes in the models using biological age as predictors. In Figure 3, intuitively this is interpreted as the health determinants are the outcomes.

If NESDA is a longitudinal cohort collected about 15 years ago, is there no other follow-up data on somatic and mental health that can be used then using biological age as predictor and health as outcome?

The authors should be somewhat more circumspect in interpreting the clocks they derive. A conclusion of the article is that biological aging proceeds differently across different molecular substrates. This takes the derived measures too literally. Instead, the finding is that the correlates of chronological age in different molecular substrates are not very well correlated with one another.

Given metabolic syndrome and depression are often medicated conditions, are there any data on medications, or any suggestion that medications might influence biomarkers?

6) Data availability

The statement on data availability is not good enough. Why can some gene expression data be released but not other data on these individuals? Data that are anonymized (the identifier key is thrown away) are not considered as sensitive data and it should hence be possible to release more data in this manner.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "An integrative study of five biological clocks in somatic and mental health" for further consideration by eLife. Your revised article has been evaluated by Jessica Tyler (Senior Editor) and Sara Hägg (Reviewing Editor).

The current version of the manuscript represents a highly responsive revision that addressed most comments. There are some remaining issues that need to be addressed before acceptance, as outlined below:

– The mortality association should be mentioned already in the result section as an additional analysis.

– The biological aging indicator is not clearly described in all figure legends, if it is the residulized age version or not.

– State the direction of effect for the medication analysis in the result section, not just p-values.

– The metabolomic platform is "Brainshake" in Materials and methods?
