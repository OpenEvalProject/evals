# Peer review - Round 1

Editors:
- Ben S Cooper, Mahidol University Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65131.sa1](https://doi.org/10.7554/eLife.65131.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper presents a detailed, model-based, characterisation of the efficacy of the only licensed dengue vaccine as a function of baseline serostatus and age. The results reinforce the hypothesis of "vaccination as a silent infection" and demonstrate the need for targeted vaccination using rapid diagnostic tests. Although this finding is not novel per se, having a precise characterisation of the time-varying risk is important for determining vaccine utility and optimal implementation strategies.

Decision letter after peer review:

Thank you for submitting your article "Efficacy profile of the CYD-TDV dengue vaccine revealed by Bayesian survival analysis of individual-level Phase III data" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: James A Watson (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

These revisions either reflect a need to temper some of the claims made in the paper or to improve clarity of the work.

1) The authors assume in their models that immunity wanes in seronegatives (over 1 year) and is stable in seropositives (maintained over time). It is unclear why these assumptions were made and clarification is needed.

2) The authors should adjust the statement "vaccinating seropositives gives greater long-lasting immunity than two natural infections" to reflect the fact that immunity in seropositives may also wane over time in a way that cannot be accurately measured with the current data.

3) On lines 329-330 the authors state "Therefore it may be more beneficial to vaccinate multitypic seropositives than simpler models have predicted [11]." How do the authors know it is the multitypics that benefit as opposed to those with primary immunity before vaccination?

4) It would be helpful if the authors further discussed age-effects and their relationship with being multitypic immune.

5) Please address reviewer 1's concern that the results of this manuscript do not support the claim on lines 311 – 315. Please also address concerns about lines 316-320.

6) Could the authors comment on whether the fact that serotype effects are more similar than might be expected based on previous articles on these data might relate to the way serotype effects are modeled, or whether this constitutes a major difference from what has been shown previously?

7) Please consider reviewer 1's suggestions to improve readability by defining KiD in the main text and revising table 1.

8) Line 349 – Where does the value of 0.7 for seropositives come from?

9) Please explain the big K notation in the Results section.

10) Please add a parameter table to the methods section and add a section on the data.

11) Please justify choice of priors and/or consider sensitivity of results to choice of priors.

12) Please provide access to the model code. The statement "Model code is available from the authors" does not meet eLife requirements: "Regardless of whether authors use original data or are reusing data available from public repositories, they must provide program code, scripts for statistical packages, and other documentation sufficient to allow an informed researcher to precisely reproduce all published results."

Reviewer #1:

Laydon et al. have conducted an elegant analysis that provides a clear and comprehensive guide to the mechanism of difference of CYD-TDV for dengue virus seropositive vs. seronegative vaccine recipients. The paper includes relevant hypothesis and model schemes as well as figures that show differences between seropositive and seronegative vaccine recipients across a range of covariates. The authors demonstrate, in a clearer way than has been shown before, that CYD-TDV increases disease across all ages in both trials in seronegatives. The authors also show that the enhancing effect is stronger against hospitalized disease than febrile disease. Many of these results have already been presented previously in other papers analyzing the same data, but the modeling approach does provide a new perspective that adds to the story of the CYD-TDV vaccine.

Overall, the paper is clearly written and easy to follow, especially given the complexity of the model and subject matter. However, numerous claims are made in the abstract and the discussion that inaccurately reflect the results presented in this paper. In particular, major conclusions of the paper relate to the benefit of the vaccine for seropositive individuals (lines 18-19, 327-328) and an increasing effect of vaccination for seropositive individuals with age (lines 286-290, 329-330). There are potential issues with the modeling approach and how it relates to these conclusions. Further, a discussion about the long-term effects of the vaccine for seronegatives is speculative and problematic (311-320).

Comments for the authors:

1) Lines 18-19. "Vaccinating seropositives gives greater long-lasting immunity than two natural infections." The claim that fixed-time immunity induced by vaccination of seropositives is maintained at a high level over time is not well supported. The authors assume in their models that immunity wanes in seronegatives (over 1 year) and is stable in seropositives (maintained over time). First, it is unclear why these assumptions were made. The reference for these model choices does not seem to cover immune kinetics over this period of time (Clapham et al. 2016 PLOS Comp Bio). Second, the authors actually tested different assumptions about waning immunity in supplement (lines 667 – 694), which are not described in the main text. In the supplement, the authors demonstrate waning immunity out to 4.5 years (with wide confidence intervals) in both seronegative and seropositive vaccinated individuals. In both cases, the duration of waning is outside of the observational period of the study, and the authors write: "We conclude that three years of follow up data from each patient is insufficient to infer durations." Thus, the authors should adjust the statement "vaccinating seropositives gives greater long-lasting immunity than two natural infections" to reflect the fact that immunity in seropositives may also wane over time in a way that cannot be accurately measured with the current data.

2) Lines 329-330. "Therefore it may be more beneficial to vaccinate multitypic seropositives than simpler models have predicted [11]." How do the authors know it is the multitypics that benefit as opposed to those with primary immunity before vaccination? It would be helpful if the authors could further support this statement by discussing the results that relate to this point. This is especially important in relation to the discussion about dengue rapid diagnostic tests (e.g. lines 23-24), which have very low sensitivity for detecting monotypic DENV immunes.

3) Lines 286 -290. "Interestingly, fixed-time immunity was found to increase with age in seropositives. In general, heterogeneity between countries' Kaplan-Meier curves can be explained by serotype and seroprevalence, although these factors are insufficient to explain differences in vaccine efficacy by age, for which age-specific effects (independent of serostatus) are required." The conclusion about the benefit of the vaccine even to multitypic immunes seems to be derived from the observation that fixed-effect immunity induced by the vaccine in seropositive individuals increases with age. The authors observe large age-specific fixed-time immunity differences by serostatus (Figure 5), although it is not clear there is much difference across age groups in vaccine efficacy (Figure 4). While the authors state that age specific effects are independent of serostatus, the age effects only occur in seropositives and thus are most plausibly related to more prior infections in children of older ages. It would be helpful if the authors further discussed age-effects and their relationship being multitypic immune.

4) Lines 311 – 315. "In high transmission settings where children would ordinarily receive at least two natural infections, we predict that even seronegatives would eventually benefit from vaccination, as they would experience one high risk infection, and all subsequent infections would have a much lower risk, in contrast to unvaccinated individuals who would ordinarily experience one moderate and one high risk infection [Figure 1]." The results of this manuscript do not support this claim. While the authors may expect this to be true based on the model scheme (referenced as Figure 1), the results, as currently described, do not prove this point. Further, the caveats provided afterward do not justify inclusion of this paragraph in the discussion (Lines 316-320): "Important caveats include first that disease risk would increase in the short term. Second, and more seriously, a small subset of symptomatic infections are fatal, in which case vaccination could shorten life in seronegatives. Finally, while the eventual benefit to seronegatives is predicted by our model and the model fits well, this remains a prediction yet to be validated by empirical data."). This paragraph should be removed or significantly reworked because it is largely a question of medical ethics.

5) Figure 4. It is not clear why vaccine efficacy increases over time in the trial for vaccinated seropositives, even across all age groups. It does not seem to be explained by age effects, waning immunity, or serotype distributions. Is it related to differences in disease outcomes measured in the trial over time (e.g. Figure S8)?

6) It is surprising that the serotype effects are more similar than might be expected based on previous articles on these data, especially previous observations of greater efficacy against DENV4. Here the authors observe strong enhancement of DENV4 at later timepoints in the trial. Could the authors comment on whether this might relate to the way serotype effects are modeled, or whether this constitutes a major difference from what has been shown previously?

7) Table 1 and its explanation in the text are confusing. Instead of a traditional presentation of relative risk, which is described in the text, the table presents the probability of disease expected relative to secondary infections. One option would be to present relative risk estimates in table, and clearly indicate the reference groups in the table. Additionally, while KiD is clearly defined in the methods, it would be helpful to add one sentence to the main text to define KiD, given that the main text uses this notation in multiple paragraphs without explaining its interpretation.

Reviewer #2:

This paper uses individual trial participant data from two large phase 3 dengue vaccine randomised clinical trials to fit a Bayesian survival model of symptomatic dengue illness that is dependent on case-control status (vaccine vs placebo), baseline serostatus, age, and dengue serotype. The main finding is a detailed characterisation of how the relative risk of symptomatic illness changes as a function of time since vaccination and baseline serostatus. As previously reported, children who are seronegative at baseline have a drastically increased risk of symptomatic illness in years 2 and 3 of follow-up. Although this finding is not novel per se, having a precise characterisation of the time-varying risk is important for determining vaccine utility and optimal implementation strategies.

The survival model is fairly complex but this complexity reflects the complexity of the trial data and the inference problem at hand (multiple countries with different proportions of dengue serotypes, active and passive follow-up periods, age-varying effects). I particularly like the use of Gibbs sampling to treat the missing baseline serostatus as a latent variable in the model. This is an elegant method that allows for the analysis of the whole dataset and not restricted to just those with serostatus data (only 10% of participants).

My main comments are about clarity of the manuscript and reproducibility:

1. The Results section needs to explain the big K notation which is fairly complicated (but I can't see any easy way of simplifying it!)

2. The Methods section really needs a section on the data (this could be quite short). Otherwise it's hard to know exactly what sort of data are being used (eg right censoring after first illness is mentioned in the model bit)

3. The Methods section really needs a parameter table. Table 1 gives a summary of model outputs which is useful, but these are not parameters. What I would find useful is a table with all the main model parameters using the same notation as in the text (eg K0,0) and the associated prior distributions. This would emphasize that the model has a lot of parameters. This would also be useful to emphasize which parameters were fixed in the model (eg Mb, sigma?).

4. It says all priors are uniform but this seems a bit odd. Maybe I am misunderstanding something, but the relative risk parameters can take values in (0, infinity) surely? A uniform prior is therefore improper. This is probably not the best choice (uniform priors are often not a good choice).

5. "Model code is available from the authors" and "The model was coded in C++" doesn't really meet eLife standards for reproducibility or inspire huge confidence. The paper is entirely based on the validity of the model fitting and this is a complex model that has been hand coded. I fully trust the competence of the authors, but I really think the code should be made available online (via a git repo for example) with a minimum working example for the fitting. If the authors can't make the full dataset openly accessible then a simulated dataset to test the model would be a good alternative.

6. Could you explain a bit more why the parameter Mb is fixed at 0.7? It says: "equal to 1 for seronegatives and 0.7 for seropositives, chosen to reflect seropositive participants' reduced disease risk due to their immunity to at least one serotype". I couldn't square this with fact that seropositives also can have increase risk as the secondary infection is more likely to be severe than the first? I get that you don't know how many infections a seropositive individual has had, but I can't really understand the justification for the 0.7.
