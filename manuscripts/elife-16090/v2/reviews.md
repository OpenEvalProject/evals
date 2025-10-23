# Peer review - Round 1

Editors:
- Simon I Hay, Institute for Health Metrics and Evaluation , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16090.031](https://doi.org/10.7554/eLife.16090.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for resubmitting your work entitled "The impact of pyrethroid resistance on the efficacy and effectiveness of bednets for malaria control" for further consideration at eLife. Your revised article has been favorably evaluated by Prabhat Jha (Senior editor), a Reviewing editor, and three reviewers.

There are some issues that need to be addressed before acceptance, as outlined below:

Reviewer 1 raises many important points for further clarification of the model and reviewer 2 some clear guides for improvement in terms of the justification/motivation of the models, its extrapolation to Africa and the overall messaging of the paper. The specific concerns are as follows:

Reviewer #1:

This paper combines three meta-analyses of bioassays and hut trials with analysis based on a transmission dynamic model to explore how different levels of pyrethroid resistance might be expected to affect malaria incidence and the potential benefits of switching to nets containing PBO.

Clearly this work addresses a very important public health problem. I believe the broad class of methods used are appropriate, though further justification for some specific assumptions is needed (see below). The work claims to offer substantial new insights, in particular highlighting the importance of even low levels of resistance which has the potential to change the way pyrethroid resistance is thought about. I don't know the LLIN literature well enough to assess the accuracy of this claim, but it sounds plausible.

The paper is clearly written, the results are explained very well, and the figures clearly convey the key findings. The methods are also well-described (though will be even clearer once code has been made available as is planned). There is one area that I think needs to be improved: while the methods describe clearly what was done, it is not always clear why. In particular, I found the reasons behind a number of modelling choices described in the subsections “Quantifying the impact of standard and PBO LLINs in the presence of insecticide resistance” and “Parameterising transmission dynamics model” opaque. For example, why use a 3rd order polynomial when looking at LLIN deterrence? Are there reasons for thinking there should be two change-points? To what extent are the assumptions of normally distributed errors (Equation 9) justified? Can the data motivating the choice of Equations 10–11 be shown in a technical appendix? Motivation of Equations 12–14 is also lacking: taking the simplest (Equation 13) it is unclear why s_p0 (the proportion of mosquitoes feeding successfully) should depend on both m_p (the ratio of the number of mosquitoes entering a hut with a LLIN to the number entering a hut without a bednet), and on k_p (the proportion which enter and successfully feed a p-treated hut), given that the latter already includes entering. Moreover, it is claimed that s_p0 is a proportion, so should be constrained between 0 and 1, but if m_p = 1 (so bednets have no effect on entering) then s_p0=k_p/k_0, which is a ratio of two proportions rather than a proportion itself (for plausible parameters values it presumably will be below 1, but it is not necessarily so). I therefore think further motivation is required, which should ideally include some graphical assessments of model assumptions (3rd order polynomial, normally distributed errors, relationship between k_p and mortality) which could go in the appendix.

It is also good practice in any Bayesian analysis to explicitly show posterior distributions of model parameters or at the very least to summarise CrIs for these.

Reviewer #1 (Additional data files and statistical comments):

It would be useful to provide code and data used in meta analyses – and the statistical submission form states that these will be made available.

Reviewer #2:

The authors have used three small datasets (all that is available) and many assumptions to model the impact of insecticide resistance, defined using insecticide bioassay results, on malaria incidence in Africa in a defined range of scenarios. Their scope is ambitious and this work brings together several separate studies to incorporate resistance into an existing malaria model. The work builds on earlier studies and is novel and interesting, however, the results need to be caveated carefully to recognise the limitations of the datasets used and the assumptions made. It also needs to be clear that this work makes predictions for a limited range of scenarios.

The work uses a series of meta-analyses to show that insecticide bioassay results can be used to predict the impact of resistance on malaria incidence, however, the final model has not been validated using African locations that were not included in the meta-analyses datasets where values are known for both malaria incidence and resistance as measured by an insecticide bioassay.

The data used, the mosquito species included and the range of slide prevalence values considered are all specific to scenarios found in Africa but nowhere in the paper is this limitation mentioned. The implication from the title and throughout the manuscript is that this is a generalizable analysis of pyrethroid resistance but it is in fact only applicable in Africa, and only in certain scenarios within subsaharan Africa.

Throughout the Results and Discussion there are sentences that look like statements of fact but they are in fact predictions within the limits of certain scenarios defined by the authors and predicated on analysis of a limited dataset and many assumptions, for example, "For the An. gambiae complex PBO had the greatest benefit in mosquito populations with intermediate levels of pyrethroid resistance", "The probability that a mosquito will feed on someone beneath a LLIN only increases at high levels of pyrethroid resistance", and so on. These statements need to be presented as predictions, and it would also be useful if the Results could start with a summary of the scenarios covered and assumptions made (see below). In Results, the authors state "The numbers of mosquitoes deterred from entering the experimental hut substantially decreases in areas of higher pyrethroid resistance" – this is a strong statement but when you look at Figure 3A you can see that the credible intervals are large ("substantial" even) and this statement needs to caveated appropriately.

Where values are given, these are not bounded by any intervals, for example in Results "causing up to 200 additional cases per 1000" or "where over 500 cases per 100 people can be prevented each year". A range or intervals are needed to give an idea of uncertainty.

Meta-analyses 1 and 2 were compared to the observed results collected for the third meta-analysis but this comparison was visual only with no formal analysis or validation (end of subsections “Added benefit of PBO” and” Predicting the added benefit of PBO LLINs in experimental hut trials”).

The paper as a whole, and the Methods in particular, is a long and dense read and would benefit from summaries for biomedical/entomological readers who are not mathematical modellers, whilst still retaining important details about the scenarios modelled and the assumptions made. In particular, summaries aimed at these readers at the beginning of both the Methods and Results would be hugely helpful for eLife's broader readership.

Figure 1 is cited in the Introduction and seems to be a key result but is not explained in the Results at all or discussed. No credible intervals are included. It shows model predictions for the scenario where bioassay results give 20% mortality but it would be interesting to see the results for other mortality/survival rates that are often found in the region. The green dashed line in 1A shows 10% parasite prevalence but it is unclear why. The starting prevalence is >20% and then it drops after control but come up to 10% every three years so presumably this is the setting the green line refers to? The legend says the black line shows the situation with no resistance and the red line shows the situation if resistance arrives at Y6, but the red lines starts before Y0 and the black line doesn't start until Y6.

There are a lot of assumptions made by this work but it is unclear how they have been justified and which ones have been subject to sensitivity analyses in the context of the results presented here, i.e. the impact of the prevalence of resistance on malaria incidence. The assumptions made include: Assumed mosquito deterrence and exiting can be described by the degree of mosquito mortality seen in the same hut trial; Assumed the relationship between deterrence/exiting, feeding successfully and dying is consistent across all species; Assumed washing nets gives the same results as a durability study; Assumed the activity of the insecticide decays according to a given formula that includes half-life in washes; Assumed resistance arises spontaneously, and after six years of LLINs use; Assumed LLINs are re-distributed every three years; Assumed transmission is perennial; Assumed there is no other vector control (and presumably no other non-vector related pyrethroid use); Assumed resistance remains constant after arising; Assumed 35% clinical cases are treated of which 36% receive ACT); Incorporated assumptions/estimates used previously by the same group that are not all given here; Assumed physiological resistance has no effect on the vectorial capacity of individual mosquitoes.

Reviewer #2 (Additional data files and statistical comments):

I am not a mathematical modeller and assume that this manuscript has also gone to reviewers who can comment on the modelling work in more depth.

The authors propose to make the data used in the meta-analysis available via Dryad if they have previously been published. This is reasonable but some of the unpublished datasets were provided by the authors of this paper and so should also be included in data deposit.

I am not qualified to comment on whether the source code provided would allow a reader to repeat this work but this is important.

Reviewer #3:

This is a well written, well-designed and important manuscript.

The observation that bioassay survival can be used as a quantitative test to assess the level of pyrethroid resistance is an important one. As the authors note bioassays are a crude tool but they can be potential important on a programmatic level.

The observation that LLINs provide protection until high levels of resistance is important from a policy perspective and contributes to understanding a poorly studied topic.

The model is statistically sound and the authors must be commended on sharing their code for full transparency.

The final recommendation of the benefits of PBO nets has important policy implications for areas high in resistance.
