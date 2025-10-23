# Author response - Round 1

Authors:
- Caroline Bull ([ORCID: 0000-0002-2176-5120](https://orcid.org/0000-0002-2176-5120))
- Emma Hazelwood ([ORCID: 0000-0002-4888-6037](https://orcid.org/0000-0002-4888-6037))
- Joshua A Bell
- Vanessa Tan ([ORCID: 0000-0001-7938-127X](https://orcid.org/0000-0001-7938-127X))
- Andrei-Emil Constantinescu
- Carolina Borges
- Danny Legge ([ORCID: 0000-0002-3897-5861](https://orcid.org/0000-0002-3897-5861))
- Kimberley Burrows
- Jeroen R Huyghe ([ORCID: 0000-0001-6027-9806](https://orcid.org/0000-0001-6027-9806))
- Hermann Brenner
- Sergi Castellvi-Bel
- Andrew T Chan
- Sun-Seog Kweon
- Loic Le Marchand
- Li Li
- Iona Cheng
- Rish K Pai
- Jane C Figueiredo
- Neil Murphy
- Marc J Gunter
- Nicholas J Timpson
- Emma E Vincent ([ORCID: 0000-0002-8917-7384](https://orcid.org/0000-0002-8917-7384))

## Response text

DOI: [10.7554/eLife.87894.3.sa2](https://doi.org/10.7554/eLife.87894.3.sa2)

The following is the authors’ response to the original reviews.

We would like to thank the reviewers for their helpful comments which we have addressed, point-by-point, below:

Reviewer #1:

1. It might be useful to add more details to the methods (especially lines 191-196) to make them a bit more user-friendly for an audience who still may be unfamiliar with the relatively new and complex Mendelian randomisation technique.

The following information has been included in this section of the methods, to describe the different MR models in more detail:

“The IVW MR model will produce biased effect estimates in the presence of horizontal pleiotropy, i.e. where one or more genetic variant(s) included in the instrument affect the outcome by a pathway other than through the exposure. In the weighted median model, each genetic variant is weighted according to its distance from the median effect of all genetic variants. Thus, the weighted median model will provide an unbiased estimate when at least 50% of the information in an instrument comes from genetic variants that are not horizontally pleiotropic. The weighted mode model uses a similar approach but weights genetic instruments according to the mean effect. In this model, over 50% of the weight of the genetic instrument can be contributed to by genetic variants which are horizontally pleiotropic, but the most common amount of pleiotropy must be zero (known as the Zero Modal Pleiotropy Assumption (ZEMPA))[Hartwig et al., 2017].”

2. I was just wondering why MR egger was not carried out as part of this analysis?

We did consider also employing the MR Egger model as a further sensitivity analysis. However, given we were already employing the weighted median and weighted mode models, and given that MR-Egger suffers from reduced statistical power in comparison to the other models, we reasoned that adding in a further MR model would not add further clarity to our analyses, particularly given the relatively small sample size.

3. Although it is included in Figure 1 flowchart, I think it is also important to explain clearly in the written text way only n=6,118 of n=13,988 children in ALSPAC study were included in this study and the reason for this.

The following information has been included in the paragraph describing the ALSPAC study in the methods:

“Sufficient information was available on 6,221 of these individuals to be included in our analysis, as metabolomics was not performed for all individuals in the ALSPAC study.”

4. It is mentioned within the discussion 'the NMR metabolomics platform utilised in the analyses outlined here has limited coverage of fatty acids'. I think it might be useful to also add this detail into the methods section to aid readers when they are making their own interpretation whilst reading the results section.

The following sentence has been included in the methods section:

“This metabolomics platform has limited coverage of fatty acids.”

5. However, I feel that the conclusion should be tempered slightly as although this study alongside other similar MR studies provides evidence of an association between genetic liability to CRC and levels of metabolites at certain ages, I do not think there is enough evidence at this stage to say that genetic liability for CRC actually alters the levels of metabolites.

The first sentence of the conclusion has been changed to:

“Our analysis provides evidence that genetic liability to CRC is associated with altered levels of metabolites at certain ages, some of which may have a causal role in CRC development.”

Reviewer #2:

1. The background is lacking introduction to the different components of the metabolic features tested. For instance, there is a broader discussion about polyunsaturated fatty acids (PUFA) in the discussion, however, this should have been introduced and defined already before that. What metabolites are included in that term (PUFA)? Are there other studies on PUFA and CRC?

The following information has been included in the background section:

“In particular, previous work has highlighted polyunsaturated fatty acids (PUFA) as potentially having a role in colorectal cancer development. The term PUFA includes omega-3 and -6 fatty acids. Recent MR work has highlighted a possible link between PUFAs, in particular omega 6 PUFAs, and colorectal cancer risk.”

2. There seem to be indications for horizontal pleiotropy given the changed estimates when genetic variants in the FADS loci are removed. Could multivariable MR methods have been used to account for pleiotropy and differentiate individual fatty acid effects?

Multivariable MR can be employed to investigate the effects of horizontal pleiotropy. However, the multiple exposures must have sufficiently distinct underlying genetic architecture in order to instrument each one whilst adjusting for the other, as determined by conditional F-statistics. Given the correlations across metabolite levels, this is unlikely to be the case.

3. The ALSPAC sample sizes are decreasing across the different age groups, which is not strange given the longitudinal collection. However, does the altered sample composition affect the results? Have sensitivity analyses been done on the complete set of individuals from age 8-25?

The altered sample composition could be affecting results. The limitations section of the discussion has been amended to reflect this:

“Secondly, mostly due to the longitudinal nature of the ASLAPC study, our sample at each time point is composed of slightly different individuals. This could be influencing our results, and should be taken into account when comparing across time points.”

We have not completed any sensitivity analyses to investigate this.

4. Although beyond the scope of this paper, sex-stratified GWAS analyses on metabolites can easily be done in UK Biobank.

We thank the reviewer for this suggestion, and agree that this would be an interesting future analysis. We have amended the discussion to mention this:

“Fourthly, our analysis would benefit from being repeated with sex-stratified data. Although such GWAS results for metabolites are not currently available, the data to perform such GWAS are available in UK Biobank for future analyses.”

5. Very minor, there is a difference in reporting a number of decimals in ALSPAC results.There is also a difference in reporting the units for the results comparing text and figures (per SD higher CRC liability or per doubling). Please include sample sizes and data sources in the figure legends as they should be stand-alone items.

We have amended the ALSPAC results to all have two decimal places, reporting units have been altered and figure legends to include sample sizes and data sources.
