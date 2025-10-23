# Peer review - Round 1

Editors:
- Philip Boonstra, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83116.sa0](https://doi.org/10.7554/eLife.83116.sa0)

This important retrospective analysis of nearly 500,000 hospitalized Danish patients sheds light on the possible relationships between blood type and susceptibility to a host of diseases. The Danish National Patient Register is a compelling data source, and the statistical methodology is solid. The findings reported herein provide evidence, supporting information, and potential hypotheses for researchers interested in the causes and etiology of diseases as they relate to blood type.


---

# Peer review - Round 1

Editors:
- Philip Boonstra, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83116.sa1](https://doi.org/10.7554/eLife.83116.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Associations of ABO and Rhesus D Blood Groups with Phenome-Wide Disease Incidence: A 41-year Retrospective Cohort Study of 482,914 Patients" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Philip Boonstra as Reviewing Editor and Reviewer #3, and the evaluation has been overseen by a Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Reviewers 1 and 3 both point out an issue regarding the A and O subgroups dominating the analyses due to their sample size. This seems to be a very important caveat to include in the comparison of the number of statistically significant findings per blood group.

2) Reviewer 1 comments on the lack of adjustment for patient ethnicity as a confounder (or a surrogate for other confounders). Please engage with this comment, which may involve explaining why this is unlikely, or which may involve actually trying to incorporate patient ethnicity into your models.

3) All of the reviewers raise many other good points in their Comments to the Authors, which I encourage you to read and engage with, potentially adjusting your analyses if you believe appropriate.

Reviewer #1 (Recommendations for the authors):

This study aims to address the important question of how different blood types are related to disease risk and age at diagnosis.

However, a major concern is that as per the comments in the public review, the lack of adjustment for confounding due to ethnicity represents a highly substantial limitation of this work. While it is briefly mentioned in the manuscript, this is a very major limitation that leads to very limited interpretability of the results. Incorporating ethnicity as a covariate into the analyses would be crucial.

Reviewer #2 (Recommendations for the authors):

Abstract/Intro

– "we determined the uniqueness" is a bit vague, could you more explicitly say you perform tests with A, AB, B, and O blood groups each as reference group as opposed to only O as the reference group?

– "diagnosis-wide" or "disease-wide" was used but perhaps more accurate to say "phenome wide" as in the title? Both disease-wide and diagnosis-wide are also used in the introduction before phecodes are introduced, and consistency might be better here.

– Age of disease onset specifically, not just disease onset, and perhaps age at first diagnosis is the most accurate (as is used in the introduction).

Methodological considerations

– ICD9 wasn't used? Most of the phecode mapping was done in ICD9/ICD10. Am I understanding ref 16 is in preparation? It would be important to describe how this is done and how it may bias your phecodes, particularly if ref 16 is not pre-printed yet. A good sanity check is how the prevalence/incidence of a handful of traits with this mapping compares to any other population-wide prevalence/incidence measures.

– It would be great to see a sensitivity analysis using either a mixed model to adjust for cryptic relatedness, close family structure, and population structure (presuming like other countries, the DNPR has many relatives). This may not statistically work with the quasi-Poisson model, so perhaps just restricting it to <3 degree individuals and comparing findings (of course this will decrease power, but nice to see if some of the main findings remain).

– I see it in the limitations, but please comment earlier in the manuscript on who gets a blood group determination in the hospital (e.g. people who made need a transplant sooner). Is it possible to characterize the disease prevalence in the subsection of the DNPR with a blood type and without so you can identify any major disease group biases?

– Was a power calculation used to determine the need for 100 cases?

– How is emigration recorded? National registers?

– The interquartile range would be a better descriptor of follow-up time rather than just the maximum (41 years) in the methods and in the limitations section.

– Why use a log-linear quasi-Poisson regression to estimate incidence rate ratios as opposed to logistic regression and odds ratios? It could be a valuable addition to the paper to provide odds ratios as well.

– It's good to adjust for ABO and RhD when testing RhD and ABO respectively, but is it possible to use interaction terms and consider these as well?

– It's great to use birth year to adjust for any "cohort effects" in society over time. Is attained age the age at end of the study period? Wouldn't birth year and attained age be too highly correlated to use both in the model? What is the rationale for using cubic splines for these variables rather than the numerical variables themselves? I see from the code that 20-year increments were used for the knots, any rationale for this methodology would be helpful.

– By excluding patients assigned a phecode at the start of the DNPR, would these be people who had the diagnosis previously and were recorded upon the inauguration of the register? Is there any kind of washout period you are using to define "start" of the DNPR?

– What is the ancestral breakdown of the cohort? Mostly European ancestries? While our current labels for genetic ancestry are quite rough, I think this is an important piece of information given the different distributions of blood groups across global populations.

– Excellent availability of code and summary data for tables/graphs.

Results

– The audience may be less interested in the number of significant phecodes and more in patterns. It could be good to comment on the shared phecodes between the 50, 38, 11, 53, and 28 found. What large-scale disease groupings (phewas disease categories) do these tend to fall in? Does one blood group have far more cardiovascular phecodes than another? Are any phecodes significant for more than 3 blood groups? Etc.

– Personally, I prefer p-values in scientific notation rather than <0.001 but I understand Table 2 is a lot of data to present.

– The figures could benefit from larger labels for readability.

– For the Manhattan plots, it would be good to specify -log10 FDR transformed adjusted p-values on the y-axis in addition to the figure legend.

– Were any blood groups associated with an earlier onset of outcomes?

Discussion

– What was used to identify "novel associations"? A systematic literature review? Comparison to Dahlén? I would refrain from using novel unless you define specifically how it was determined to be novel.

– A systematic comparison with what seems to be the closest study, Dahlén et al., would be beneficial as a type of replication.

– I would refrain from using the term linkage in the discussion as that may lead the reader to think of chromosomal linkage, but I think the authors mean a causal association.

– I don't think the findings support the discussion point on the selective pressure.

Reviewer #3 (Recommendations for the authors):

1. Could the authors justify why choosing to fit separate models comparing one blood type against all others, e.g. A vs. all others then AB vs. all others, is the more sensible choice than fitting one model that jointly tests for A vs. AB vs. B vs. O? I understand that there are various interpretative and statistical challenges to both, but fitting separate models is not internally consistent. The 'A vs. all others' model implicitly assumes that there is no difference in incidence in the AB, B, and O groups, but then the next model ('AB vs. all others') makes a different assumption, namely that there is no difference in incidence in the A, B, and O groups.

2. A natural limitation to this analysis is that there are more statistically significant findings in the O and A blood groups because they are the more prevalent groups, and statistical significance is driven by sample size. In this sense, it would be interesting if there were a way to account for the differences in sample size between the blood groups. Is it possible to investigate whether any of the groups have disproportionately more statistically significant findings after accounting for sample size?

3. Page 6, line 124: I think the use of the word 'confounder' here is not quite right in the technical sense, as I do not read this sentence to be claiming that sex is influencing blood type.

4. Regarding the legend for Figure 2:

a. It should have triangles rather than circles. Assuming this plot was made in ggplot2, this can be done using the override.aes argument in the guides function.

b. it would be helpful to show more than 3 values on the legend.

c. It would be helpful to use the same scale across the subfigures. What I mean is, in the bloodgroup AB figure, there is no discernible difference in size between a 1.1 and a 4.0 rate ratio.

d. I realize this is very pedantic but I believe the legend is technically not showing rate ratios but rather max(rate_ratio, 1/rate_ratio).

5. Do the authors have any intuition why Figure 1 is bimodal? My interpretation of this figure is that, among those who were hospitalized in Denmark between 2006 and 2018, the plurality was born either in the immediate post-WW2 era (makes sense to me) or the 80s (doesn't make as much sense to me).

6. Page 7, line 152: reference 20 is not related to FDR. Can the authors provide a reference for their specific approach to controlling FDR?
