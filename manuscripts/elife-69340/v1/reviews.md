# Peer review - Round 1

Editors:
- Joshua T Schiffer, Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69340.sa1](https://doi.org/10.7554/eLife.69340.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper uses a simulation approach to demonstrate that a personalized viral load based testing approach has the potential to limit the duration of unnecessary isolation among infected people while not increasing the risk of releasing an infectious person. This work could influence policies regarding duration of isolation is hospitals and at home.

Decision letter after peer review:

Thank you for submitting your article "Revisiting the guidelines for ending isolation for COVID-19 patients" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Joshua T Schiffer as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

As is customary in eLife, the reviewers have discussed their critiques with one another and with the editors. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly.

Essential Revisions:

1) Please enhance the literature review to discuss the relevance of this paper in light of new, less expensive testing strategies including rapid antigen testing. Please also discuss more specifically how different countries around the world are differing in terms of isolation policies.

2) Please test different intra-host models against the data using residuals and AIC and see if different models alter conclusions about optimal isolation guidelines in anyway.

Reviewer #1:

1) Overall, the paper is under referenced and state of the art testing approaches are not described in sufficient detail in the intro or discussion. A brief review of national practices that incorporate one strategy or the other to inform the reader of the current standard would be helpful to highlight the importance of the work.

2) There is no mention of the use of antigen tests which are less sensitive for viral RNA but more specific for infectious virus. These are far less expensive, have far less turnaround and are now widely used in many countries. Antigen tests should be contextualized given the results of this modeling. Saliva testing is also widespread in many places. Modeling of both approaches is available in the literature and should be cited.

3) Several groups have published intra-host viral dynamic models (the Guedj and Schiffer groups) with slightly different mechanistic assumptions. These models should be discussed and in particular it should be mentioned whether their slightly different structures could alter the paper's conclusions. Similarly, a couple of research groups have made estimates of viral load thresholds required for transmission and these should be referenced as well.

4) The model is fit to very little data (as very little is available) and while the posterior sampling method to generate 1000 in silico patients is reasonable, it is no substitute for real data. The authors should acknowledge that confidence intervals reported in the paper are quite speculative in the sense that the extent and quality of relevant viral load data for intra-host modeling is unfortunately quite limited. If the model is misclassified based on non-representative input data, then estimations about duration of isolation could be biased.

5) For the test-based strategy, are there any assumptions about when the first test might occur? Can this only occur after development of symptoms or after a certain number of days of infection? This section of the methods should provide more detail.

Reviewer #2:

Jeong et al., examined the important question of the guidelines for ending the isolation of COVID-19 patients. Two types of guidelines are commonly used: 1) A fixed duration (10 days or 2 weeks) of isolation following the development of symptoms, which the authors call 'one-size-fits-all'. 2) Two successive RT/PCR negative test results separated by 24 hours for ending isolation, which the authors term 'personalized'. In the former, a long duration would lead to unnecessarily long isolation periods, whereas a short duration may end up releasing individuals still able to transmit the disease. The latter avoids these pitfalls, but requires multiple tests, increasing costs and the burden on healthcare staff. To identify which of these strategies is better, the authors develop a mathematical model of within-host SARS-CoV-2 dynamics and apply it to data of viral load changes post infection from untreated patients. Using the parameters estimated, they create a pool of 1000 virtual patients and simulate dynamics in these patients and assess the consequences of the two isolation ending approaches by calculating the probability that a patient released is still able to transmit and the excess or unwarranted duration of isolation. They find that in general the personalized approach fares better on both metrics.

The question is important and timely given the raging COVID-19 pandemic. The conceptual approach developed is novel and is also likely to be applicable beyond the current pandemic. The application of the approach and the resulting inferences drawn, however, need stronger justification. My reasons are below.

1. In the personalized approach, where RT/PCR tests are used, the chance that a person who is infectious is declared non-infectious (or vice versa) is due to measurement error. This error is estimated in the study as the variance of the normal distribution fit to the residuals of the best-fits of the mathematical model to the patient data of viral load changes (see lines 464 and 473). The error is thus strongly dependent on the model. One could use a model with more parameters and obtain a 'better' fit to the data, with smaller residuals, which could then presumably change the inferences above. Indeed, many other models have been developed to describe SARS-CoV-2 dynamics and have been applied to some of the datasets the present study has used.

2. A second concern, which the authors too recognize, is that the data used is all from hospitalized patients, which may not be representative of the vast fraction of infected individuals undergoing (home or institutional, but not hospital) isolation following mild/moderate symptoms. The required durations of isolation may then be even shorter than predicted. Would guidelines that account for this heterogeneity in disease severity be easier to implement? In other words, individuals could be categorized into disease severity classes (say asymptomatic, mild, moderate, or severe) and have fixed but different durations of isolation for each class. For personalized treatments, one could still use these categories to decide when to start measurements. In the present study, when to start measurements in the personalized approach is not mentioned and it appears that measurements are assumed to be made daily from the time of isolation, which may be unnecessary and impractical.

3. Finally, the two approaches are compared at 5% and 1% probabilities of ending isolation prematurely (Figure 4). While 1% appears small, whether it is small enough from an epidemiological perspective remains to be addressed. In other words, whether 1% 'leakage' of infectious individuals from isolation is tolerable would depend on the setting, particularly, the population density and the propensity for risky behavior. If at an epidemiologically identified threshold, the difference between the two approaches is small, the fixed duration approach may have the advantage of simplicity and of doing away with additional tests.

1. One way to address comment 1 above could be to compare alternative models and identify the best model based on estimates of AIC, or other such metrics, and use it to estimate the measurement error. Alternatively, if experimental uncertainties in RT/PCR measurements are known, using them instead of the variance of the normal distribution fit to residuals could provide an independent verification of the inferences.

2. The authors should show fits of the model to the data and list the model parameter values estimated; this would help appreciate the inferences drawn better.
