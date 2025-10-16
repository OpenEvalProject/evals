# Peer review - Round 1

Editors:
- Caroline Colijn, https://ror.org/0213rcc28 Simon Fraser University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78089.sa0](https://doi.org/10.7554/eLife.78089.sa0)

This paper is interesting, timely, and important because it presents a way to understand the transmission potential of a virus even when there are very few local cases. This has a high public health communication and preparedness value. The paper is clearly written, and the results fit with the known epidemiology of outbreaks that occurred in Australia in 2020. The results are convincing and likely to be of broad interest within and outside the field of epidemiological modelling.


---

# Peer review - Round 1

Editors:
- Caroline Colijn, https://ror.org/0213rcc28 Simon Fraser University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78089.sa1](https://doi.org/10.7554/eLife.78089.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A modelling approach to estimate the transmissibility of SARS-CoV-2 during periods of high, low, and zero case incidence" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Michael Plank (Reviewer #1); Amy Hurford (Reviewer #2).

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

We all agree that this work is of interest and is likely to be suitable for publication in eLife.

1) Most of the reviewer questions are clarifications. Could you please address these more detailed comments?

2) We had some discussion about the terminology re: micro-distancing, whether it's really about distancing, mask use, ventilation etc. In particular, one reviewer noted that the focus on 1.5m distancing should be better justified given what we know about airborne transmission – presumably, this survey question should be interpreted as a proxy for precautionary micro-behaviour (which may include mask use, preference for outdoor or well ventilated locations,) rather than a mechanistic metric for transmission risk which we know is not primarily determined by distance.

Would you consider potential alternative terminology to make it clear it's about more than just distance per se? E.g. some modelling groups use the term "precautionary behaviour" for a similar inferred quantity.

We are aware, though, that these terms may be established in Australia, and we don't wish to introduce more confusion.

(3) A clear statement of the minimal data requirements or implications of implementing the framework with reduced data availability would be a helpful addition.

Reviewer #1 (Recommendations for the authors):

For the VIC second wave, the observation that Reff>TP is explained as being due to the nature of the sub-population the virus was predominantly spread in. That's certainly plausible epidemiologically. However another interpretation is presumably that the TP model is systematically underestimating TP. Can this be ruled out based on the result of the model?

The model description in the supplementary left me unclear about how mobility data and survey data were combined to estimate macro-distancing behaviour. This part of the model could do with some clarification. E.g. Were these used simultaneously or sequentially? From Equation 16 and line 630 it appears there is a deterministic relation between mobility data M(t) and number of non-household contacts δ(t). Were the survey data used in the process of estimating the coefficients m? Presumably the mapping between survey data and mobility data is noisy – is there an implicit noise term or residual in equation 16? Line 433 says waning in macro-distancing is driven by mobility data – so how does survey data come into estimating this? In Figure S5, it appears that the posterior estimates for macro-distancing for NSW and QLD are systematically higher than the survey data – is this because the mobility data is pulling these estimates back up, i.e. mobility data in these states tend to be closer to baseline, for the same number of reported mean non-household contacts?

Similarly regarding the micro-distancing model – Line 448 – "infer the date of peak micro-distancing behaviour" and the rate of waning. Does this mean micro-distancing is assumed to follow some parametric functional form with respect to time? Or otherwise constrained to have a single peak followed by a waning phase? How does this relate to Equation 21, where micro-distancing appears to be a function solely of the "intervention state" in that region. So wouldn't the timing of interventions in different regions determine when the peak micro-distancing occurred? And how does/would this assumption work if the survey data showed that in fact actual behaviour was not highly correlated with interventions (which it may have been in March 2020 but could conceivably become less so over time). How were the xi_ij parameters in (21) estimated (there doesn't seem to be a prior specified for them)? The micro-distancing behaviour is described as mainly relating to observation of the "1.5m distancing rule". Another significant behaviour factor affecting probability of transmission during a non-household contact is mask use yet this is not mentioned. Is there a reason this wasn't considered in the model, e.g. the survey did not ask about masks? or is it that the effect of masks could not be separately estimated?

Other specific comments

– Is transmission/ travel between different states accounted for or ignored?

– The references to the panels of Figure 2 seem to have got mixed up as the text consistently refers to panels B and F as TP and C and G as Reff but the Figure has them the other way round.

– Line 174 "Reff dropped below 1… prior to activation of stay-at-home restrictions". The data at which Reff dropped below 1 presumably could be given a confidence interval based on the green bands in Figure 2. Do these CIs overlap the date of introduction of stay-at-home restrictions? I also wonder how sensitive these inferred dates are to the infection to reporting lag and the degree of smoothness that is a priori imposed on Reff(t).

– Figure 3 caption mentions the blue bar but this seems to be missing from the graphs. Also it is a bit confusing that both the macro-distancing graphs (B and F) and micro-distancing (C and G) are described "reduction in…" when distancing behaviour appears to be associated with a decrease in B and F but an increase in C and G.

– There appears to be some notational inconsistency or at least ambiguity in the supplementary section. E.g. is TP synonymous with R*(t) in Equation 10? Is Ri^L(t) (or some combination of R^L and R^O) in Equation 6 the same as Reff(t)? Clarifying this would help understand how the method actually estimated these quantities from the data.

– In Equation 10 sigma2 appears to have the effect of always reducing RL (effective reproduction number?) relative to R* (TP). Or do the epsilons have strictly positive mean? In the absence of random effects (epsilon=0) wouldn't you expect R* and RL to have the same mean?

– In Equation (12) is surveillance assumed to have the same effect on household and non-household transmission? If so is that realistic given it's hard to isolate from people at home?

– In Equation (14) f is described as a probability density but I think it must actually be a survival function (or 1- CDF) i.e. f(t') = P(case not yet isolated at time t' after infection). Otherwise Equation (14) can't be correct, e.g. if all cases were isolated on day t'=5 that would say g(t')=0 for t'!=5 rather than g(t')=g*(t') for t'<5 and 0 for t'>5.

– Line 636 should the element corresponding to residential have value -1 not 1 so it is opposite sign to the non-residential locations? And are the 5 coefficients in w constrained to be non-negative?

– Paragraph following line 681 – is there a reason only the "always" response was used?

– Line 748 – is estimating p from transmission rates at the beginning if 1st wave representative of subsequent times? Given the concentration in overseas arrivals one might expect this to be different? Or is it because it's per hour of contact so number of contacts are factored out?

– Figure S8 – it appears there is no change in effect at the second intervention why is this? And the black dotted line mentioned in the caption does not seem to be there.

Reviewer #2 (Recommendations for the authors):

This is valuable work that fills an important need – thank you for doing this!

Future work may consider how to make this approach more accessible by outlining minimum data needs, data collection priorities, or describing the implications of proceeding with the transmission potential calculation even if a data source is unavailable (i.e. for estimation of micro-distancing). Your approach is rigorous, but also more similar to a complete model of infection spread, rather than a quick calculation of a summary statistic during a real-time pandemic response in a region with few modellers and limited resources (i.e. the Pacific Islands, or Atlantic Canada and Canada's northern territories, with much fewer resources than Australia, but that still had an important need for this approach during the pandemic).

In Table 1, regarding the heading "Local elimination", perhaps "Local transmission" is more appropriate since fundamentally this column discusses local transmission, and elimination is non-essential.
