# Peer review - Round 1

Editors:
- Ben S Cooper, Mahidol University Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54795.sa1](https://doi.org/10.7554/eLife.54795.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

A metapopulation is a group geographically separated sub-populations of a species where there are interactions between the sub-populations. The concept has been usefully applied to understand the impact of patient movements on the spread of drug-resistant bacteria in healthcare settings on a number of previous occasions, but this paper represents the first application of the concept to a large data-set including multiple bacterial species and detailed data on antibiotic usage, another key driver of the spread of resistance. The analysis provides important new insights about how patterns of patient movement within healthcare settings and antibiotic exposures both contribute to the spread of antimicrobial resistance.

Decision letter after peer review:

Thank you for submitting your article "Metapopulation ecology links antibiotic resistance, consumption and patient transfers in a network of hospital wards" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eduardo Franco as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tjibbe Donker (Reviewer #1); Rene Niehus (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analysis may be required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because of disruptions to normal working life for many, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this work, the authors study the very important question of how population level antibiotic resistance in clinically important bacterial taxa is driven by ward-level antibiotic use and patient transfer between wards. For this the authors use clinical specimen data, antibiotic use data and ward-connectivity data aggregated across one year. They perform a between ward comparison by applying ecological metapopulation methods to correct for confounding. They find, in agreement with previous evidence, that nosocomial and carbapenem resistance pathogen incidence is positively associated with connectivity, and that antibiotics have varying effects depending on the pathogen variant, with Piperacillin-tazobactam appearing to select most strongly for pathogens resistant to empirical treatment. More broadly, this would mean that different pathogen variants require either antibiotic stewardship or patient isolation interventions.

Essential revisions:

Currently the description of the methods is incomplete and makes it difficult to assess the validity of the results. Specifics are described below.

1) Is this incidence control value (Incidence(Variant|Ward) ) calculated for each of the 357 wards, or for each of the 3 ward types? This should be made clearer in the text, and also by introducing indexing into the mathematical expressions.

2) The authors build a method to account for

i) variants being associated with diff anatomical sites P(Variant|Location)

ii) different wards differing in which anatomical sites are typically sampled, and in how many samples are typically taken per patient P( No Variant | N, Ward )

From the definition of P( No Variant | N, Ward ) it is not clear whether the authors also account for the fact that samples from one patient are not independent (in terms of the sampled anatomical site) and a definition of N(I,Ward) is missing. Is this the number of samples specific from a patient with index i, being disaggregated into location and ward, or is it the total number of samples in the ward disaggregated into the different anatomical sites? The difference is important: if N(I,ward) is the total number of ward samples disaggregated into anatomical sites, then the expression P(No Variant|N, Ward) assumes that samples taken from a patient i are independent.

3) In Data collection and compilation the authors say that clinical samples are deduplicated, resulting in one sample per patient, but in the section after it seems that multiple samples per patient are used for to compute incidence control. It is correct that for the incidence control value samples where used without deduplication, but for the regression model fit were deduplicated counts used? This should be made clearer.

4) Using a priori expected selective antibiotic-variant pairs the authors show that the model manages to pick up more of those pairs than others. This is expected: even when substantial confounding increases all individual antibiotic-variant associations, a direct causal effect in a abxA-variantX pair is expected to make it easier to pick up this association. It is not clear from the Materials and methods whether a multivariate model was used here. Please provide the regression equation in the Materials and methods to allow the reader to follow what was done. If it is univariate, it is to be expected that looking into different individual antibiotics will introduce a lot of new confounding from association with other antibiotic treatments. What would be useful here is a multivariate analysis of individual antibiotics (asking about the effect of each, given the effect of all the other treatment), and importantly including a few additional predictors (treatments) that one would expect to NOT be correlated with AMR (negative control). A zero-centred distribution of the negative control β parameters would then indicate lack of confounding.

5) A Poisson model was used. Typically Negative Binomial models will fit these type of data better as there's usually some overdispersion. The effect will be wider confidence intervals. It would be helpful to compare fits of Poisson and Neg Bin and go with the best fitting model.

6) The repeated dichotomising between "significant" and "non-significant findings" in the paper is at odds with current statistical thinking (see, for example, the American Statistical Association consensus statement on p-values https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf). We strongly suggest the authors drop this terminology and instead of reporting results as significant or not, report point estimates and confidence intervals for everything.

7) The exclusion of rarely used antibiotics from the analysis makes sense, but it wasn't clear why narrow spectrum antibiotics or those used in combination were also excluded. We think including these in the analysis would improve the paper.

8) There was a consensus that the conclusions were too strong e.g. "Our data establish that.…". As these are observational data, with lots of unmeasured confounding likely, the conclusions should better reflect the uncertainty.

9) "Hospital-based antibiotic stewardship is a cornerstone strategy to combat AMR, based on the assumption that AMR evolves in hospitals. Yet, there is surprisingly limited evidence to support this assumption47-49"

It's not completely clear what this statement means (there are lots of examples where antibiotic use in hospitalised patients clearly selects for resistant variants e.g. fusidic acid resistance in staphylococci), but if it's referring to population wide selection mediated by antibiotic use there are several additional papers that could be cited ( eg several papers by José-María López Lozano and Timothy Lawes, such as their Nature Micriobiology 2019 paper or more recently Tom Crellen's 2019 paper on Klebsiella in eLife).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Metapopulation ecology links antibiotic resistance, consumption, and patient transfers in a network of hospital wards" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tjibbe Donker (Reviewer #1); Ben S Cooper (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript is much improved both methodologically and in terms of readability, and key points raised in the first round of reviews have been addressed. There are, however some remaining concerns which are important to address.

Essential revisions:

1) In many places the paper refers to multivariate (or bivariate) models. Though this terminology is widely misused, multivariate (still) means models with multiple dependent variables. Models with multiple independent variables but a single dependent variable are *multivariable* models. The models used here seem to be multivariable and not multivariate.

2) In most places the authors have rightly been cautious about reaching causal conclusions based on the associations found in the observational data. However there are still a small number of places where results are presented using causal language (i.e. language that many readers are likely to interpret as implying a direct causal relationship) that is not fully justified e.g "with every doubling of antibiotic use increasing incidence by 49%", "connectivity had a larger effect on the incidence". The manuscript would be improved by rephrasing results to report these as associations, and the discussion can then consider the plausibility of a causal interpretation (as has already been done in most cases).

3) "This nearly zero-centered distribution of coefficients in associations not expected to represent direct selection suggests that residual confounding in the models was negligible….": We would suggest revising this sentence to make it easier to understand.

4) "If the resistant infections in a ward mostly result from the admission of already colonized patients, antibiotic restrictions may have a limited impact on AMR compared to infection control measures that prevent the further dissemination of the pathogens" This makes sense if "limited impact on AMR" refers to colonisation with AMR (though it's not clear that it does given that the paper is concerned with clinical infection rather than carriage data), but antibiotics can also act to select for resistance within hosts increasing (or reducing) the chance of clinical infection with resistant organisms (see, for example, Niehus et al., 2020 and references therein). We strongly encourage the authors to rephrase to acknowledge that antibiotics can also have a big impact on within host dynamics and that antibiotic restrictions (or other changes) can also have an important impact even if most infections occur in already colonised patients.

5) "the influence of connectivity on the incidence of a pathogen variant is expected to be higher if the variant is endemic to the hospital". This seems intuitive but if the level of endemicity is so high that all patients are colonised (as we would expect for E coli) then surely we would expect connectivity to have no effect on the incidence of infection with the pathogen variant. So is this statement generally true?

6) "Consistent with this theoretical interpretation of connectivity, we found that its influence was strongest in the typical nosocomial pathogens P. aeruginosa and E. faecium." Though isn't it also the case that there was little evidence of an association between connectivity and MRSA infection incidence, but MRSA (or, at least, many lineages of MRSA) also represents a "typical nosocomial pathogen". It seems as important to highlight results that don't fit with this theoretical interpretation as those that do.

7) "Further research based on time-series analyses is required.." This seems too restrictive. Several analytical frameworks not commonly referred to as "time-series analysis" (e.g. various flavours of multistate models) would also be appropriate. As written this could be mis-interpreted as saying that ARIMA models are the only way to go here.

8) Subsection “Sampling bias control” "prevalence" or incidence?

9) Subsection “Sampling bias control” third paragraph "from a same sample"

10) Fourth paragraph , shouldn't "M6" be "M7"?

11) Final paragraph in subsection “Sampling bias control”. The logic of this is not clear. This seems to be saying that the incidence control value (A) is correlated with sampling effort (B), and that A is also correlated with antibiotic usage (C), and this will lead to spurious correlation between incidence and antibiotic use in unadjusted models. This may be correct (if we interpret spurious correlation to mean correlation between two variables in the absence of a direct causal relationship), but it is not clear from the text why it should be so. Can this be rephrased to make it clearer. A DAG may also help here (see, for example, Judea Pearl's The Book of Why for an introduction to DAGs in representing causal relationships) as unless there is a backdoor path, there won't be "spurious correlation".

12) Is an R2 of 0.34 really "strong correlation"?

13) Subsection “Connectivity and other ward characteristics”. The coding of fragility is confusing. The text says that an ordinal scale was used implying that it is treated as a categorical variable but with a natural ordering (but with no values associated with the distances between levels). However, it is then reported that numerical values were assigned to the levels. If it is an ordinal scale, the coding is arbitrary, but, as written, it sounds as though a numeric scale might actually have been used here. This needs to be clarified, and if a numeric scale has been used (i.e. the assumption has been made that patients in intensive care units have precisely twice the "fragility" as those in intermediate care units ) this either needs to be justified or (in the absence of clear rationale) the analysis revised, e.g. treating ward type as a categorical variable and not making any strong assumption in how patients differ in their vulnerability to infection.

14) "…exponentiated coefficients can be interpreted as the percentage increase of the incidence for every doubling of the predictor, when all other predictors are held at their reference value". Taken literally, this sentence is not accurate, even in the special case where the independent variable is log2 of the predictor. The sentence after this one is accurate and has all the information needed, so deleting the above sentence would be fine. Note that it is more usual to report results of a Poisson regression as incidence rate ratios (exponentiating the regression coefficients) which have a simple interpretation and will be familiar to many readers, and it's not clear why the conversion reported in the second sentence is preferred here.

15) Subsection “Pooled analysis of CTX/CRO- and IPM/MEM-resistant variants” The sentence beginning "The rationale.…" is very hard to make sense of, and we strongly suggest it is rewritten to make the meaning clearer.

16) The authors removed the ESKAPE2 acronym from the Abstract. It could also be removed from the conclusion in a similar way.
