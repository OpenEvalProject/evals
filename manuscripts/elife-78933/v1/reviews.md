# Peer review - Round 1

Editors:
- Dobromir Dimitrov, https://ror.org/007ps6h72 Fred Hutchinson Cancer Center Seattle United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78933.sa0](https://doi.org/10.7554/eLife.78933.sa0)

This paper proposes a modeling framework that can be used to track the complex behavioral and immunological landscape of the COVID-19 pandemic over multiple surges and variants in South Africa, which has been validated previously for other regions and time periods. This work may be useful for infectious disease modelers, epidemiologists, and public health officials as they navigate the next phase of the pandemic or seek to understand the history of the epidemic in South Africa.


---

# Peer review - Round 1

Editors:
- Dobromir Dimitrov, https://ror.org/007ps6h72 Fred Hutchinson Cancer Center Seattle United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78933.sa1](https://doi.org/10.7554/eLife.78933.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "COVID-19 pandemic dynamics in South Africa and epidemiological characteristics of three variants of concern (Β, Δ, and Omicron)" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Bavesh Kana as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Mia Moore (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Authors need to clarify how their modeling analysis supports stated conclusions.

2) The paper will benefit from a more detailed explanation and sensitivity analyses that show how model assumptions influence presented results.

3) The authors should elaborate on the time-dependent results for all hidden parameters estimated as part of the model

Reviewer #1 (Recommendations for the authors):

1) Figure 1A is difficult to read but looks like the model underestimates many of the mortality peaks. Authors should discuss this.

2) Figure 1B: unclear what data is shown. y-label suggests it is a ratio of cum. inf over seroprevalence as %. However, this ratio should be >1 yes? Most of the key quantitative metrics used in the paper include cumulative inf. rate, seroprevalence, susceptibility, transmissibility, etc. should be clearly defined to avoid confusion.

3) Using increased susceptibility and immune erosion interchangeably (as in rows 123-126) is troubling if attributed to the properties of different variants only. It should at least partially due to waning immunity, independent of what variants are prevalent. Several studies suggest that waning may not be the same for protection acquired from vaccines or from prior infection. I understand that these effects are not easy to be disentangled but their feasibility needs to be considered.

4) Large attack rate in rows 137-138 is attributed to the high transmissibility of Δ. What about waning immunity? What is the estimated reinfection rate?

5) Immunity erosion is a key metric reported in the results. What is the mechanism of this erosion? More susceptible, more likely to get a severe infection or something else? Do you assume the same erosion after prior infection and after vaccination? What about waning over time? A more precise definition will help readers.

6) Many assumptions including those in rows 311-315 are critical. Will be nice to show how sensitive the results are to them.

7) Having seasonality in the model is interesting and useful. Authors should elaborate if this is related to proportions of contacts occurring indoors or something else? That will help applicability to other settings.

8) Figure 3E Sharp increase in detection rate during Omicron rate is difficult to believe. Other explanation?

9) Figure 4D The term "relative change" here is confusing. Need more precise definitions. For instance, does it mean that Β is ~50% as transmissible as the ancestral or does it mean that Β is ~50% more transmissible than ancestral?

10) Not sure the IFR estimates by province on p. 38 make sense to me. In my view, they should be similar across regions if health systems are comparably effective. Is it assumed different rates for previously infected and/or vaccinated?

Reviewer #2 (Recommendations for the authors):

In general very good work, but I think you need to make the logic that leads from your analysis to your conclusions a little clearer, ie what is it about what you found that makes you view large future waves as possible. I would consider focusing on the long-term trends that you can see, specifically with regard to transmission and susceptibility.

I'm also concerned about the potential lack of identifiability in the fitting scheme with all of these different parameters. In particular, I'm concerned that the drastic changes in infection detection rate may be masking changes elsewhere, in particular during the Omicron wave. I would consider a sensitivity that leaves this variable constant.

Transmissibility and Susceptibility need a more precise definition when introduced. These are assumed to be time-varying parameters or are they derived from other quantities?

Fit: Cases and Deaths, Validation: Hospitalization, Excess Deaths, Seroprevalence, retrospective predictions of δ and omicron waves

Reviewer #3 (Recommendations for the authors):

The authors have presented an extremely well-written and comprehensive analysis of the South African COVID-19 pandemic using an intricate epidemiological model. I am having some trouble fully evaluating the model, though, because of the numerous time-dependent variables estimated as part of the fitting process. I would suggest that the authors consider adding in a figure (at least from one example region) showcasing the time-dependent results for all hidden parameters estimated as part of the model (i.e. Zt, Dt, Lt, et, from Equation 1 as well as rt, IFRt and other parameters from the observation model). There is likely to be a high correlation between many of these parameters over time, so such plots would allow for proper diagnosis of the fitting procedure and ensure that all parameters are within the realistic parameter ranges at all times. As a note, it was not clear whether the prior distributions in Table S4 were actual Bayesian prior distributions, or merely the initial range of starting conditions for T0, and it would be helpful to clarify how they integrate with model fitting. Additionally, I suggest that the authors expand their Results section to include additional analyses from these hidden parameters such as how the latent period has changed over time (e.g. there is some evidence that omicron progressed quicker than previous variants) and/or the impact that mobility has had on transmission over time (incorporating the impact of et). Other analyses have found degradation of the relationship between mobility and transmission over time in limited contexts, so it would be useful to compare the current results (e.g. https://www.pnas.org/doi/10.1073/pnas.2111870119)

The authors use seasonal patterns based on historic climate data from South Africa as a means to modulate COVID-19 transmission, but there doesn't appear to be any reference for the actual climate data for South Africa from the same time period. Are there any data from the modeling time period the authors could use as validation that their assumed seasonal curves match the actual climatic conditions?

The use of retrospective forecasts is used as a means to validate that the model is accurately capturing transmission, behavioral, and immunological status in the model. While I agree that overall, the 1-2 week forecasts look satisfactory, most forecast hubs are asking for forecasts up to 4 weeks (e.g. covid forecast hub), and accurate forecasts over a longer time horizon would dramatically strengthen the validation of the model estimates. I suggest that the authors attempt 3-4 week forecasts as part of a supplemental analysis to understand the limitations of the model and forecast ability.
