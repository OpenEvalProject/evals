# Peer review - Round 1

Editors:
- Amy Wesolowski, Johns Hopkins Bloomberg School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82611.sa0](https://doi.org/10.7554/eLife.82611.sa0)

While it has been demonstrated that for SARS-CoV-2, a small fraction of individuals contributes to the majority of onward transmission, this heterogeneity is driven by multiple factors that span both biological and behavioral causes. By performing a solid meta-analysis of household transmission studies, the authors fit a household transmission model to the curated data to estimate variation in infectiousness which provides a valuable contribution to the existing knowledge base. By collating data from multiple studies, they are able to more fully investigate individual variability.


---

# Peer review - Round 1

Editors:
- Amy Wesolowski, Johns Hopkins Bloomberg School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82611.sa1](https://doi.org/10.7554/eLife.82611.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "The effect of variation of individual infectiousness on SARS-CoV-2 transmission in households" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Both reviewers have highlighted a number of areas where additional clarification (particularly for σ_var) which currently does not have sufficient detail/interpretation to warrant publication.

2) Questions about parameter identifiability and model validation were not sufficiently addressed – particularly in light of the many individual-level parameters estimated in the analysis.

3) Additional exploration of empirical relationships (such as individual infectiousness and household size, as an example) should be explored. For example, how much of the heterogeneity is driven by biological factors (such as being the primary case).

4) Additional work should be done to help disentangle differences between biological or behavioral factors since this will greatly change the interpretation of inferred parameters. In addition, more contextual information should be provided (socio-economic status and the implications of this as a confounder, a more detailed exploration of interventions that were in place and their implications) should be done.

Reviewer #1 (Recommendations for the authors):

Tsang et al. evaluate the degree of transmission heterogeneity among COVID-19 cases using data compiled from 17 household transmission studies. Transmission heterogeneity and super spreading are important but incompletely understood drivers of epidemic dynamics. While it is clear that substantial heterogeneity exists among infectors, but the relative contribution of behavior (e.g. the number of contacts), timing (e.g. large number of social interactions near the peak of infectiousness), and intrinsic biological differences in infectiousness are not resolved.

Tsang et al. compiled household transmission data from 17 published studies. They independently fit a model to each data set in order to quantify transmission heterogeneity arising from intrinsic biological differences in infectiousness, after controlling for differences in the number of contacts (i.e. household size), and timing (via the inferred time since infection). Repeated application of the same model to multiple datasets is a strength of this study because it allows the authors to assess associations between the inferred parameters and aspects of study design that can influence case ascertainment.

The authors estimate substantial intrinsic transmission heterogeneity via the parameter σ_var, which could be attributed to individual differences in viral loads or differences in the infector's contact intensity with others in the household. They show that intrinsic, within-household variation is associated with other population-level metrics of transmission heterogeneity, including p_80 and p_0.

Although the study focuses on the household size as a confounder of heterogeneity in infectiousness, the ways that the model controls for household size and the interpretation of the inferred heterogeneity parameter, σ_var could be explained more clearly. Furthermore, it seems that basic empirical relationships between individual infectiousness (δ_i) and household size are not explored. Finally, questions about parameter identifiability and model validation could be addressed more extensively, especially in light of the many individual-level parameters estimated in the analysis.

Overall, the study design is sound and the analysis of multiple datasets is a strength. However, the modeling approach and the biological interpretation/significance of the results could be more clearly explained. Also, given the large number of individual-level parameters estimated, it would be ideal to see a direct assessment of parameter identifiability (e.g. correlation plots), and model validation on simulated data (i.e. can the model estimate known parameters from simulated data?). The latter shouldn't be too difficult, given that the authors already have a simulation model for tests of model adequacy.

Specific comments:

1. Please explain assumptions about the individual infectiousness profile f(.) (from section 2 of the Materials and methods). What is the assumed shape of this function? How is it parameterized? How could the inclusion of this function in the model interact with inferred individual times of infection, especially if times of infection are inaccurate? On a related note, the authors might consider introducing the concept of contact timing as a factor that can influence heterogeneity in transmission.

2. The household size is a key conceptual focus of the study, but the main text methods/results don't explain clearly how the model accounts for household size or contact number. My interpretation is that the model accounts for household size in two ways. First. the model estimates the per-contact hazard of infection, which implicitly controls for household size/contact number. Second, the model includes a parameter, β, which represents a dilution effect, wherein the transmission hazard might be diluted in larger households due to less per-individual contact intensity. I'm not sure that the dilution effect is currently explained anywhere in the main text, and it could also be explained more clearly that the model is designed to estimate transmission heterogeneity after adjusting for household size.

2a. It would be helpful if the authors could discuss the distinction between contact number, contact frequency, and contact duration somewhere in the text.

3. Given the focus on household size and the number of contacts, it seems there are missed opportunities to explore how the inferred level of individual infectiousness (δ_i) co-varies with metrics like household size.

4. Please explain in more detail the meta-regression sensitivity analyses.

5. I'm not sure that tables S6-S9 are cross-referenced anywhere in the main text, and their legends aren't sufficiently detailed to fully communicate how to interpret these tables in the context of the broader study.

Reviewer #2 (Recommendations for the authors):

Transmission heterogeneity and superspreading of SARS-CoV-2 have been demonstrated repeatedly through real-world observational studies, with a small fraction of individuals accounting for the majority of onward transmission. However, this observed transmission heterogeneity is likely a superposition of accumulated variations from multiple factors, including but not limited to host behavioral factors such as the variation in contact numbers contact duration, and contact settings; variations in the adoption of preventive measures (mask-wearing, physical distancing, etc.); the effects of NPIs (case isolations and contact quarantines, population-level lockdowns); as well as biological factors including differences in shedding duration and intensity of the primary case, variation in susceptibility among close contacts. Fewer studies, however, attempted to isolate the effects of individual factors contributing to the overall transmission heterogeneity, while controlling for other factors. In the manuscript entitled "The effect of variation of individual infectiousness on SARS-CoV-2 transmission in households", the authors aim at characterizing the variation in individual infectiousness of SARS-CoV-2, controlling for other host factors. To achieve this, the authors performed a meta-analysis of household transmission studies conducted during or not too longer after the initial SARS-CoV-2 wave caused by the ancestral strain across the globe. The authors fitted a household transmission model to the curated data and estimated the variation in infectiousness by introducing random effects of individual infectiousness and its population-level distribution.

The study has several strengths. First, by choosing analyzing data from the household study, the authors were able to control for several key factors contributing to the overall transmission heterogeneity but not variation in individual infectiousness, including the number of contacts as well the setting of transmission (household). The authors also incorporated an additional parameter in the household transmission model to adjust for the impact of household size on household transmission risk, which has been identified as an important risk factor for SARS-CoV-2 transmission within the household across multiple studies. The authors also curated the studies during the early stage of the pandemic so that most household contacts would remain naïve during the study period, and the immune status of the household contact (either due to prior infection or vaccination) would be unlikely to confound the results of the study.

However, the study also has a few limitations. First, it is difficult to disentangle if the observed variation in infectiousness is due to biological factors or behavioral factors. During the study period of interest, public health agencies across the globe were recommending at-home isolation guidelines aiming at reducing transmission within the household, including mask-wearing when in contact with other household members, using separate bedrooms/bathrooms, avoiding having meals together, etc. The differences in the guidelines across nationals/regions as well as the level of compliance with guidelines at the household level would also impact individual household transmission risk. Second, the risk of acquiring infections from the community could be heavily influenced by the socio-economic status, since multiple studies have clearly demonstrated stark disparity of COVID-19 burden, factors such as occupation (essential workers tend to be low-wage jobs) assess to PPE and healthcare were likely to contribute to the observed disparity. Lastly, it is also difficult to entangle if the observed heterogeneity is due to the biological factors of the primary case (i.e., variation in shedding duration/intensity) or the contact (variation in susceptibility). The current formulation of the transmission model only addresses the former not the latter.

For the household transmission model concerning imputation of the timing of infection, it is unclear if the timing of infection is partially missing, or if the timing of infection were unavailable for all studies. If it is the former case, the authors should give a more detailed description of the imputation process in a study-by-study fashion and report the proportion of infection time that was imputed. If it is the latter case, I do not understand the benefit of explicitly modeling the temporal infectiousness profile, thus I would recommend the authors use a simpler chain-binomial model fitting to only the binary outcome (of infected or not) unless the authors make a convincing case otherwise.

Both p80 and p0 are poor statistics to characterize household transmission due to the discrete nature of household contact numbers. For example, it is unintuitive to interpret and compare p80 for a household size of 2 vs 10 (for a household size of 2 conditional on an index case within the household this could only be interpreted as the proportion of households with secondary infections, which is cross-household level statistics, while for a household size of 10, it can be interpreted as a meaningful statistical for each household). Furthermore, the interpretation of p80 as a metric for transmission heterogeneity becomes even murkier if multi-generation transmission within the household is considered, especially for a larger household. For p0, this metric is heavily dependent on household size. For example, one would expect the p0 for a household size of 10 (with on index) to be way smaller than p0 household size of 2 (assuming no dilution effects on transmission with the increase of household size), as in the former case p0 characterize the probability of all 9 uninfected contacts escaping infection from the index, while in the latter p0 characterizes the probability to escape infection by only 1 household contact. Thus, it is meaningless to compare p0 without controlling for household size across studies. For the arguments above, I recommend the authors remove both p80 and p0 from the paper.

Through the formulation of the household transmission model, the authors essentially assume a lognormal distribution of individual infectiousness, which is a long-tailed distribution by nature. I think this is an important point that needs to be highlighted. Has the author tried a normal distribution instead of a log-normal distribution? Would a normal distribution fit better or worse to the data than the log-normal one? I recommend the authors conduct a sensitivity analysis of a normal distribution of the individual infectiousness (i.e., not taking the exponential of the σ term for the hazard of infection function on page 7).

Table S5 is cropped.
