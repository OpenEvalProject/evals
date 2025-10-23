# Peer review - Round 1

Editors:
- Talía Malagón, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59755.sa1](https://doi.org/10.7554/eLife.59755.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Infection with Opithorchis viverrini is a neglected tropical disease endemic to Southeast Asian countries. This study is particularly interesting in that it compiles data from decades of prevalence surveys of O. viverrini infection to produce high resolution maps of infection prevalence in Southeast Asia over the past few decades, identifying regions where prevalence has decreased and increased, and the systemic factors that have influenced the prevalence over time. Such high resolution geographical data will be highly valuable for public health efforts aimed at treating and preventing this disease.

Decision letter after peer review:

Thank you for submitting your article "Model-based spatial-temporal mapping of opisthorchiasis in endemic countries of Southeast Asia" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and, and the evaluation has been overseen by Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This paper examined the prevalence of opisthorchiasis in Southeast Asian countries using survey data obtained through an extensive literature search. The data comprised both aerial and point-referenced data. The authors then fitted a Bayesian fusion spatiotemporal model to map the prevalence of the disease at 5x5 km resolution. The estimates were also aggregated to different administrative units within the study countries. This work applies state-of-the-art modelling techniques to an interesting application.

Essential revisions:

1) Many of the publications studied only in areas where Opisthorchis viverrini is endemic. The prevalence in surveys these are likely to be overestimated due to the preferential sampling of areas. The authors have used a method to test for this (Monte Carlo test using R package PStestR) and claim that they did not detect any preferential sampling. However, the reviewers did not find this very convincing given the clustering of points in Figure 2. We would like the authors to give further details regarding the analysis method they used to test for preferential sampling (Monte Carlo test using R package PStestR), show the results of this analysis, and also to include some further discussion regarding the impact of preferential sampling on the validity of results.

2) The authors stratified predictions by 10-year periods; this is a very coarse time frame for predictions given that incidence of infection can vary from year to year. This limitation should be fully acknowledged by the authors if shorter time frames cannot be used.

3) The reviewers criticized the imputation of sample size in order to convert prevalences to binomial data in papers where sample size was unavailable. While the authors included a sensitivity analysis of the impact of this imputation in Figure 3—source data 3 to help assess this point, this was not considered sufficient to address this issue. The reviewers suggest instead that if the data were originally available as prevalence estimates, these should be treated as such and modelled using a β likelihood or a normal likelihood (on the logit scale) and not converted artificially to binomial data.

4) The authors should describe how they dealt statistically when they encountered multiple estimates from the same area within each of the 10-year periods.

5) Surveys often have complex designs, using weighting to calculate the prevalence over an entire area. How did the authors account for this weighting in their analysis?

6) The authors treated surveys aggregated over ADM2 or ADM3 areas as points, whereas those aggregated over ADM1 areas were treated as areal data. This is a very rough way to handle spatial misalignment. If the data were associated with areas, these should be left as areal data in the analysis and should not be treated as points as one would be enforcing non-existent geographical precision in the data in doing so. The authors should justify this choice, or discuss how it may impact the accuracy of results.

7) The authors used the AUC statistic to validate their model. This is an inappropriate use of the AUC; ROC and AUC are normally used to check the discrimination ability of logistic regression models and not binomial regression models. The authors mention other metrics which are useful for evaluating binomial regression models such as MSE and MAE, but the values of these metrics are not discussed or presented in the manuscript. Please discard the AUC analysis, and instead include a table showing the values of these other metrics in the main manuscript, as well as the bias and 95% coverage rates of the fitted model.

8) The authors discuss differences in test sensitivity as a source of heterogeneity between surveys, which they ignored by assuming similar sensitivity across all surveys. It is unclear how much this may have affected results. Please give estimates of the magnitude of the difference of sensitivity of different diagnostic tests, as this could heavily influence differences in prevalence across surveys if these differences in sensitivity are very large. Is there a reason why the authors did not assess the diagnostic method as a covariate in their model?

9) The authors used as an exclusion criteria surveys using the smear method to detect opisthorchiasis due to its lack of sensitivity. However, in nearly half of all reports, the diagnostic test used was not reported or missing. How do the authors then know that these records did not use the smear method to detect disease?

10) The authors need to provide a list of citations of all their included studies as an appendix, consistent with GATHER item 5 and PRISMA item 18. GATHER also suggests providing a table with each data source used, reference information or contact name/institution, population represented, data collection method, year(s) of data collection, sex and age range, diagnostic criteria or measurement method, and sample size, as relevant.

11) The interpretation of the estimated regression coefficients of the categorical variables was poorly done. In particular for model results Table 2: since the authors used a logit link function, the model results can be converted into odds ratios by exponentiating the model coefficients. Please convert all coefficients in this table into odds ratios. Model coefficients have very little inherent interpretability, while odds ratios can be interpreted by readers as measures of relative risk comparing the reference category and the category in question in relation to the outcome variable. The authors may also want to consider dropping the other non-coefficient model parameters from this table (spatial range, correlation coefficient, spatial variance) and report them in the text instead as their units are not consistent with the rest of the table. For the probability %, this would be reinterpreted as the probability that the odds ratio is >1 for risk factors increasing the prevalence of disease, and <1 for risk factors decreasing the prevalence of disease (distance to nearest open body of water and precipitation). Also, for the variables that were modeled as continuous (precipitation, HII), we need the unit size increase associated with each increase in prevalence (i.e. what increase in annual precipitation is associated with the 0.14 decrease in the logit?)

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Model-based spatial-temporal mapping of opisthorchiasis in endemic countries of Southeast Asia" for further consideration by eLife. Your revised article has been evaluated by Miles Davenport (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) For Figure 5, negative values are conventionally interpreted as decreases and positive values as increases, so the numbers in this figure are likely to lead to confusion. Please change the calculations instead to (𝑝𝑝𝑠𝑡j − 𝑝𝑝𝑠𝑡i )/𝑝𝑝𝑠𝑡𝑖, which should lead to an inversion of the sign without changing the numbers, and will increase the interpretability of the figure.

2) In Table 2, the exponent of the intercept of the model cannot be interpreted as an odds ratio, as it represents the odds of the prevalence at the reference value of all categories. Please leave the cells for OR and prob(%) blank for this row, as these quantities are not relevant for the intercept.
