# Peer review - Round 1

Editors:
- Niel Hens, https://ror.org/04nbhqj75 Hasselt University Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73120.sa0](https://doi.org/10.7554/eLife.73120.sa0)

In their work, the authors present a novel geostatistical framework allowing for modelling complex animal-environment-human interactions during zoonotic spillover. The presented case relates to zoonotic spillover of Leptospira infections in a marginalised urban setting in Salvador, Brazil. The outcomes of such applications could contribute to inform public health interventions. The methodological approach is to be applauded and can be of benefit beyond the study of zoonotic spillover.


---

# Peer review - Round 1

Editors:
- Niel Hens, https://ror.org/04nbhqj75 Hasselt University Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73120.sa1](https://doi.org/10.7554/eLife.73120.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Linking rattiness, geography and environmental degradation to spillover Leptospira infections in marginalised urban settings: an eco-epidemiological community-based cohort study in Brazil" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by David Serwadda as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Benny Borremans (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers and I have several comments that should be carefully addressed. I tried to merge the essential ones here; though the public reviews and the recommendations for authors should be taken into account to (note that there is some overlap between the essential revisions and the public reviews).

1) On the statistical model and the choices made:

– On p7, section 2.2.2 the authors use mu_2 for defining the intensity of the inhomogeneous Poisson process. Shouldn't this be mu_1 rather mu_2? If not, what makes using the same function for Yi,1 and Yi,2 a reasonable choice? Note that the model used in both components is not the same.

– Did the authors perform a sensitivity analysis related to the assumption of t=0.5 for the disturbed traps (how often did this occur)?

– For the most part, the explanatory variables assessed in the different models were well described and justified, however there were some cases for which further explanation would have been helpful. For example, how did the authors determine which occupations to evaluate? Specifically, why traveling salesperson? What is the difference between open sewer within 10 m and unprotected from sewer?

– Sup file 2 and Figure S1 (and Table 1): This could be a function of me not understanding correctly, not necessarily the authors not conducting the study appropriately, but I couldn't understand why elevation was split into 3 when distance to large refuse piles was only split into 2 categories since the shape of the splines was similar. Based on Figure S1 (B) it seems that the effect decreases until ~ 60m then increases until ~ 145m and then decreases again? Also, it was unclear to me why in Table 1 an effect estimate for distance to large refuse piles of.02 is 'of little effect' when one of -.07 is considered noteworthy. They both seemed quite small.

– Table 2: It was unclear to me why both relative elevation and elevation level were included and how they differed. Further explanation would be helpful.

– Figure 4. It seems to me that the elevation levels were chosen simply by identifying the elevation cut-offs that divided the household sample sizes into three equal groups. It would be helpful if the authors included a viable biological justification for this division.

– The authors provide an extensive model building exercise and investigate, in different ways, whether the model captures the necessary complexity (GAM smoothers – testing linearity, spatial correlation, etc). I believe the work would benefit from (1) a formal diagnostic investigation, if feasible; (2) providing guidelines on how model building should be performed.

More specifically there are some additional concerns about this specific analysis:

(1) The infection risk data: while the actual infection risk data are not shown, the map shown in Figure 5B suggests that there is an infection hotspot that happens to be at high elevation. This raises the question of how strongly this single hotspot is driving the observed correlation between rat abundance and infection risk (which the authors find to be much stronger at high elevation than at lower elevations).

(2) The statistical models: if I understand correctly, all tested models of infection risk include the variable rat abundance, and while the individual effect estimates for rat abundance are statistically significant (Table 3), the more important question of how the fit of a model without the rat abundance variables compares with those of the other tested models (shown in Supplementary Table S2) has not been addressed.

I am wondering about this curious spatial pattern, where there seems to be one main predicted hotspot of infection risk (Figure 5B), which happens to be at a high elevation. There are a few other locations at a similar elevation, but these don't result in high infection risk predictions, which I assume is because of a difference in other important covariates? When comparing this result to the rattiness map (Figure 5A), one would never guess there is a meaningful (biologically significant) correlation between rattiness and infection risk. Model selection however did find a statistically significant effect of rattiness (Table 3), with the largest effect sizes for the high elevation. This makes me wonder whether the statistical pattern is mostly driven by this one hotspot that happens to be at high elevation, and how important rattiness really is overall.

It would be great to see a map based on the raw infection data, so it's possible to get a better sense of this possible biasing effect on the contribution of rattiness. Maybe add it to figure 5?

One way to test this would be to do the same analysis, but without the location(s) driving this high infection risk hotspot, and see if rattiness is still an important contributor to infection risk.

Perhaps more importantly, all human infection models (Supplementary table 2) include rattiness, so there is no way to assess how a model without rattiness compares with those that do. I strongly suggest adding at least one model without rattiness, for example model M1 but excluding rattiness. If the AIC values of all models in Table S2 are much lower than a model without rattiness, it would add a lot of confidence to the assumed significant effect of rattiness. This is related to the model framework relying on conditional independence within its built up (equation (1)). Whereas this is a reasonable assumption, it would be good to discuss situations in which this assumption is questionable and what the implications are for applying the modeling framework to other settings. In addition the authors indicate that the most complex model was chosen when modeling rattiness (p8, section 2.3.1). Doesn't this imply that the model selection reaches its limits given the candidate models at hand, ie is there a need to consider more complex models?

2) Presentation and interpretation of results

– In Tables 2 and 3, the authors present their results in a comprehensive way but it's not easy to connect those tables in terms of results. For example; are the occupational exposures binary variables? If not, what is the reference category and why is only one (work as traveling salesperson) retained in Table 3? Which of the variables reach overall significance?

Reviewer #1 (Recommendations for the authors):

I believe the manuscript is overall clearly written. I do have a few questions for clarification though.

On p2, section 2.1.2 serosurveys, eligibility criteria for inclusion in the cohort study are outlined. It would help explaining why these specific conditions were used for inclusion: ie 'who had slept more than 3 nights in the previous week in a study household'.

On p7, section 2.2.3 the authors define Zi,j using a Bernoulli variable with probability p_j(x_i). Wouldn't it make sense to consider a hazard-based framework or derive the corresponding hazard function in terms of it's interpretation?

Textual comments:

– Please use \mbox for the correlation in section 2.2.1.

Reviewer #2 (Recommendations for the authors):

Line 62 – typo? Analyze vs. analysing?

Figure 2 description – typo? … dh and dr are not mutually exclusive groups of explanatory [variables – missing?] and the same variables…

Line 277 – it would be nice to reference table 2 here so that the readers can see the full list of considered variables by group.

Regarding supplemental information, it would have been easier if the actual table or figure had been referenced vs. the file in which it could be found.

Reviewer #3 (Recommendations for the authors):

It was a pleasure to review your manuscript.

In my opinion the writing is excellent, the study design is clever and powerful (and must have been a lot of work!), and the spatial statistics are performed expertly.

I do have a few suggestions, that I hope can either be easily refuted or can help to improve the analyses.

Congratulations on this fantastic work.

L65: I suggest writing DALYs in full, as not all readers will know what this is.

L94: I don't agree that there is an absence of methods (multilevel Bayesian models for example have been around for a while), but rather that they are rarely applied in this context.

L99: I find this particular unspecific use of abundance quite confusing, as this is already a very specific and well-defined ecological term. For example, what exactly is then meant by reservoir host abundance on L104? Is this the number of reservoir hosts, or the number of infected hosts, or the number of leptospires in the environment?

If it is used as a measure of exposure to a disease of interest (L100), why not use a term like pathogen pressure, or just exposure? I strongly suggest using different words to describe actual abundance and pathogen-related abundance.

L115: The term rattiness is useful (and fun), but does it really represent leptospire pressure by rats if the model does not take into account leptospira prevalence/shedding in the rat populations? I agree that the presence/abundance of rats can be a decent proxy for the potential risk of leptospira spillover in locations with known presence of leptospira in the rat population, but I'm less inclined to accept that it is ok to define rattiness, which implies rat abundance, as a proxy for leptospiral contamination when the study did not measure the presence of leptospira in the rats.

I see that this is mentioned in the discussion (L493). I think it might be more useful to add this information earlier on, at the place where the term rattiness is introduced.

I agree that with such a high prevalence, it is reasonable to use rattiness as a proxy, but would still be wary: these 80% of rats are likely not distributed randomly across the area, as pathogen transmission is typically more spatially clustered. That means that 1 out of 5 local rat populations are not infected, which is definitely not negligible. That is an important caveat to highlight clearly, early on.

L208, 213: On L208, i is defined as a location, and on L213 as household location. I assume these represent the same location? If so, it might be best to be a bit more specific in the definition on L208, and add 'household', just so it's clear there is only one definition of a location.

L284: What is the rationale for choosing those specific knots?

L324: Kudos for citing the individual R packages (as one should, but often not done).
