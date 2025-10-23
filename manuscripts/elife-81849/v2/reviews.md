# Peer review - Round 1

Editors:
- Isabel Rodriguez-Barraquer, https://ror.org/043mz5j54 University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81849.sa0](https://doi.org/10.7554/eLife.81849.sa0)

This manuscript provides a valuable and policy-relevant contribution to our understanding of SARS-CoV-2 viral kinetics in the Omicron era. The authors exploit a rich and unique dataset from the National Basketball Association to describe post-infection viral kinetics, including rebounds, and to explore evidence for differential kinetics by immune history and demographics. The authors show (as others have) that most people remain with high viral loads 5 days post positive test and that older individuals and those who were boosted (but had a poor initial antibody response to the primary vaccine series) were more likely to remain with high viral loads longer after an Omicron infection.


---

# Peer review - Round 1

Editors:
- Isabel Rodriguez-Barraquer, https://ror.org/043mz5j54 University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81849.sa1](https://doi.org/10.7554/eLife.81849.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Quantifying the impact of immune history and variant on SARS-CoV-2 viral kinetics and infection rebound: a retrospective cohort study" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Neil Ferguson as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Andrew Azman (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please add a description (table?) of the demographics of the participants (e.g. age, sex, co-morbidities), stratified by important factors (i.e. vaccination status, exposure history, antibody titer class).

2) It would be helpful to add the models with age effects (uni and multivariate) to model performance comparison in Tables S3/4.

3) While the analyses stratified by antibody levels are interesting, the differences in kinetics that remain, even after stratifying, are also intriguing. It might not be possible to present an analysis stratified by antibody level and age, but it would be useful to discuss to what extent age might explain these differences. Presenting a figure (like Figure 2b) stratified by age could also be useful. Authors should also discuss alternative hypotheses for differences in kinetics between boosted and unboosted individuals.

4) Please clarify whether any of the participants took antivirals.

Reviewer #1 (Recommendations for the authors):

Although the effect of age as a confounder is accounted for and discussed, I would have found it helpful to see it considered from the beginning as a potentially important factor and tested along with a cumulative number of exposures, lineage, days since previous exposure and vaccination status. It would be interesting to see a model that in addition to the baseline spline also accounts for a single predictor of age in the results presented in Tables S3 and S4. In addition, I would consider showing some of the results for age and Omicron in the main text.

I found the methods and results for the logistic regression a bit difficult to follow at some points, with most of the results presented in the supplementary information, implying going back and forth between the two files.

– It would be helpful to add a list (or Table) with all possible factors (predictors) considered and the values (or categories of values) they can take (e.g. age: <30, 30-50, >50).

– How is the effect of each factor modelled? It is written in the methods section that "additional logistic regression models, adding additional spline terms capturing the effect of vaccination status, cumulative number of previous exposures or days since previous exposure, and/or lineage with days since detection". Does it mean an additional spline is added for each possible category of each variable? If so, how is "days since previous exposure" treated? I understand that for the models that include more than one predictor, those are always considered to interact – is that true? Please clarify.

– The caption of Figure S9 needs to be rewritten and more precise. First, panel (A) only shows the results for a subset of the data (BA.1 infected and boosted individuals). Therefore, I would avoid saying "conditioning on vaccination status and lineage", which suggests that the whole dataset has been used to fit the model. Similar for panel (B). Second, it would be helpful to make clearer which model has been used for the results in panel (A) and which one for the results in panel (B). Now it is only said at the end of the caption. Third, the model for panel (B) is described as including an interaction between days since detection with vaccination status and variant. However, as far as I understand, only Omicron infections are considered here, which means that variant is in practice not used as a covariate, and therefore, the model only has 2 splines (one for boosted and one for non-boosted individuals).

– In most figures, results are presented for the frequent testing group and the delayed detection group. Are the logistic models fitted jointly to the whole dataset or independently to each of the two groups? I understand that the latter. In that case, I think it is not correct to say "stratified". Instead, I would just say that the model has been independently fitted to X and Y.

Methods section, Viral kinetic model (lines 589-604). (Again) when the authors say they "stratify" the model by a certain variable, what do they mean? Do they just simply fit the model independently to each subset of data, or something else? Please clarify.

Methods section, Incidence of rebounds (lines 145-169). Although it might seem obvious, I think it would be good to make clear they talk about consecutive days in the definition of a rebound.

For consistency throughout the manuscript, I would suggest using either: (1) variant or lineage, (2) vaccination status and vaccination history, (3) Omicron or BA.1.

I have not seen any statement about the availability of the data. Please clarify.

Reviewer #2 (Recommendations for the authors):

– It seems like the authors suggest that no one took antivirals after infection in this cohort but I don't see this explicitly stated here. Do you have data on this or it is assumed?

– Throughout reading this I found myself wanting to see a better description of the characteristics of the participants (eg, age, sex, co-morbidities [which there probably aren't many of]), ideally stratified by important factors like vaccination and exposure history and titer class (high/low).

– In the models predicting Pr(Ct<30), it is not clear why cross-validation is not being used for AUC and classification accuracy measures. Not an issue with EPLD shown in the supplemental table.

– It would be helpful to add the models with age effects to model performance comparison in Tables S3/4.

– Figure 2C – 95%CrI shown horizontally seems strange. Are these not meant to be aligned with the y-axis?

– Figure S11 is hard to read and I do not believe the legend and caption fully describe what is going on. Would be helpful to update this.

– line 131 – can you add the n to this?

– Code on github is easy to use and pretty well documented, thank you!
