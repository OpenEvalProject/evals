# Peer review - Round 1

Editors:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35832.044](https://doi.org/10.7554/eLife.35832.044)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Quantification of anti-parasite and anti-disease immunity to malaria as a function of age and exposure" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ben Cooper as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

All reviewers thought the work presented some very detailed and interesting data. However, following consultation, the consensus was that by failing to account for individual exposure history in the data the work fell short of what was possible with these data, and also made implicit independence assumptions that seem hard to justify. If these limitations could be addressed in future work, the journal would be interested in considering a new manuscript looking at the same data.

Reviewer #1:

This manuscript presents an elegant application of generalised additive models to a rich longitudinal malaria data-set from 773 children across three study sites in Uganda. The authors use this statistical modelling approach to investigate how both anti-parasite immunity to P. falciparum and anti-disease immunity change with age and transmission intensity.

As the authors argue, this works represents a substantial advance over previous attempt to model processes driving malaria immunity which have been informed by aggregated data. The individual level data makes it possible to disentangle the effects of age and exposure history, and demonstrate an independent effect of age (i.e. beyond that which would be expected if exposure alone were driving acquisition of immunity).

Generally the manuscript is very well written, easy to read, clearly presented, and the findings accompanied with appropriate caveats. This work seems to make an important and worthwhile contribution to the literature. The sensitivity analysis in the supplementary material also considerably strengthens the work.

Reviewer #2:

This study analyses data from three longitudinal cohort studies from regions of Uganda with varying transmission intensity. The analysis is based on very detailed epidemiological data sets with data collected on P. falciparum parasite density, temperature, clinical episodes of malaria and EIR. In order to assess the statistical methods it is worthwhile to consider this analysis in the context of a previous analysis of Ugandan data by the same authors in an excellent paper published last year in The Journal of Infectious Diseases. The data utilised in this analysis is superior to that utilised in the previous paper in a number of ways: more participants; household measurements of EIR; individual level measurements of temperature and parasite density, etc. The absence of data on low density PCR-detectable infections however is a limitation. Although the statistical models utilised in this analysis are justifiable and robust, I feel that the methods have taken a step back compared to their previous methods.

In their previous analysis the authors captured how previous exposure to malaria affects the probability that an infection will lead to a clinical episode (e.g. individuals with a greater number of episodes in the past have greater levels of clinical immunity and thus a lower probability that a new infection progresses to an episode of clinical malaria). It appears to me that in this analysis that the rich data on an individuals' exposure history is not accounted for – and with a mean of 2 years' follow-up (over 3 years in some case) this is quite substantial data. Instead, the authors' models for temperature, parasite density and symptomatic malaria for visit k, depend only on measurements at visit k, and not on the individuals' malaria history at previous visits. I would like to see the authors utilise a method that accounts for malaria history at visits before k (e.g. such as the method used in their previous analysis).

Reviewer #3:

This article using 3 very interesting longitudinal data sets from Uganda to investigate how the acquisition of immunity is influenced by exposure and age. These are very pertinent questions. Unfortunately, the authors do not make good use of the excellent longitudinal data they have nor is the way they combine active and passive case detection samples in the definitions of anti-parasite and anti-disease very clear.

The authors treat all infections within a child as statistically independent. This is not strictly speaking correct.

Firstly, infections within the same child are controlled by the same immune system and thus reflective of the same immune status. Appropriate analyses of these data would thus need to take into account the non-independence of samples within the same individual.

Secondly, asymptomatic P. falciparum may last for up to 1 year or more. Therefore, it is likely that in particular in at low transmission household 2 or more consecutive infection may represent a single P. falciparum infection. In low transmission settings where few infections are acquired asymptomatic infections are likely to be longer lasting both the more limited number of treatments and the lack of superinfections that will result in higher parasitaemias and clinical symptoms in their early (exponential) growth phase. This factor could explain the overall higher proportion of asymptomatic infections and the lower parasitaemia at a given in age at low transmission.

The authors have defined anti-disease immunity as difference in the mean objective temperature at a given parasitaemia. This may again be potentially impacted by the quite different numbers of observed symptomatic vs. asymptomatic detection samples. From the Materials and methods section it is not clear how author dealt with children that reports having been febrile in the last 24hrs but did not have an objective fever. Were there many such children (and how to the relate to listed asymtomatic infections) and how were they treated in the analysis. Also did the proportion of such children differ with age and exposure in similar ways that the proportion of asymptomatic infections differs (i.e. highest a low transmission, lowest at moderate transmission).

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Quantification of anti-parasite and anti-disease immunity to malaria as a function of age and exposure" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ben Cooper as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Prabhat Jha as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: James Watson (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors sought to describe how both age and transmission intensity affect the dynamics of the development of immunity against symptomatic Plasmodium falciparum infection. They used data from 773 children in three cohort studies in Uganda (2011-2014), in settings with a wide range of transmission intensity (measured by the annual entomological inoculation rate (aEIR) is estimated from monthly mosquito household catch surveys). They used age and number of infectious bites per year to characterise how immunity develops over time. Immunity was assessed in two ways: anti-parasite immunity (measured by parasite density) and anti-disease immunity (measured by the parasite density which causes fever). The data were analysed using generalised additive models, which allow for complex relationships between aEIR, age and immunity. The results quantified how both age and exposure had important influences on immunity and suggested a surprising (and hard-to-explain) non-linear relationship where children living in the lowest transmission settings appeared to develop immunity faster than those in higher transmission settings.

Essential revisions:

This is a uniquely rich data set, that has the potential to yield important insights.

However, all reviewers were highly skeptical about some of the findings (as outlined in the reviews) which challenge most current thinking about malaria and immunity. Some of these findings are so surprising that we think more effort to check their robustness is needed.

One of the biggest concerns was the grouping of active and passive case detection data without regard to the different data generating mechanisms. In particular there may be important biases operating (particularly in the passive data, which accounts for the majority of the data).

For these reasons we would like to see the following revisions:

1a) Repeat the analysis just with the active case detection data (this should provide the basis for the most reliable inference).

1b) Compare 1a with the same analysis on passive case detection data.

If 1a and 1b give essentially the same results this provides a useful confirmation – if the same results can been shown with data collected in two different ways that should lead to more confidence in the results. If results are different, then some thought about the reasons why are needed (though this in itself could be an interesting finding).

2) The current models use a mean aEIR, but EIR can vary substantially over time (and there is clear evidence that it does vary greatly in this data set]. This means that the model is implicitly assuming that a person's immunity at one time point depends on what happens (to the EIR) in the future. This doesn't make a lot of sense. It should not be difficult to account for this temporal variation in the EIR in the analysis (i.e. considering cumulative EIR), and we consider this an essential revision.

3) All non-linear models should be compared to their linear counterpart. In the current submission AP1 is the linear version of AP2, but there is no linear version of AP3 with the age/EIR interaction (similarly for the ADx models that consider temperature).

4) Additional checking of model adequacy is needed e.g. plots of scaled residuals and predictive checks (see, for example, https://people.maths.bris.ac.uk/~sw15190/mgcv/check-select.pdf).

5) The evidence for the surprising non-monotonic relationships for acquired immunity predicted by the model would be greatly strengthened if the authors could present a plot clearly showing this signal in the data (i.e. without a statistical model).

Reviewer #1:

I reviewed an earlier submission of this manuscript which was rejected largely because of the consensus (following consultation between reviewers) that the analysis was not making the best of use of the data. In particular, not accounting for individual-level malaria history from previous visits was felt to be a big limitation.

There have been a number of changes in the current submission which have undoubtedly improved the manuscript and addressed many substantive concerns. First, the provision of the code and data needed for the analysis is very welcome and helps clarify exactly what was done and makes it possible for others to verify the findings.

Second, the revision has clarified that dependencies were accounted for (with a random effects term), and explained why more explicitly accounting for individual histories was not done (because the data did not come from a birth cohort and only limited windows of time were observed for each individual). It has also clarified that individual exposure histories are being implicitly accounted for through adjustment for age, aEIR and through the random effects terms. In light of these clarifications, the modelling decisions seem more understandable.

In addition to these clarifications there is some new material including individual immunity trajectories (output from original model), additional models which did use data on recent exposure (models adjusted for number of P. falciparum positive visits in the previous 3 and 6 months periods), but found no evidence that this recent exposure was associated with either anti-parasite or anti-disease immunity (when already adjusting for age, aEIR and random effects).

There is also some additional sensitivity analysis e.g. adjusting for cumulative aEIR (rather than just aEIR) which suggests an effect of age independent of exposure.

Finally, the authors have added figures showing confidence bounds for age and EIR-specific anti-parasite and anti-disease immunity. This were omitted from the original submission and are also a welcome addition.

As the rebuttal letter makes clear, the authors do not have a clear explanation for the "provocative finding" that children exposed to the lowest transmission are developing immunity more effectively than those in more moderate transmission settings (although the parasite diversity hypothesis at least sounds plausible). Clearly, this finding goes against most preconceptions about how immunity in malaria works and I think the authors are therefore right to spend a lot of effort in sensitivity analyses to show that this is a robust finding and not an artefact. While the fact that same effect is seen for two different measures of immunity strengthens the case for this being a real effect, I am concerned that there are other possible reasons why this could still be an artefact which have not yet been ruled out. Two possibilities I can think of are:

i) Is there a possibility that differences in measuring aEIR at different sites could account for this? The sensitivity analysis excluding Walukuba helps here (Figure 5—figure supplement 5). What about looking at Kihihi/Kanungu alone? This seems to have a big enough range of aEIRs that the effect should be seen if present. [note: following consultation this was not considered to be an essential revision].

ii) Is there a possibility that there are edge effects in fitting that GAMs that introduce these effects? This could be checked, for example, by fitting the same models to simulated data under different assumptions. Is it possible get similar results (showing immunity developing faster at high and low aEIRs than at intermediate values) even when data are simulated under the assumption of a monotonic relationship between aEIR and the rate at which immunity develops? [note: following consultation this was not considered an essential revision].

When comparing the model fits (Supplementary file 1), the flexible GAM models (which allow for non-monotonic relationships between aEIR & immunity) are compared with a single mixed model expressing a monotonic relationship (with temperature and log parasite density varying linearly with age and with log(aEIR)). Why not also consider other functional monotonic relationships between these measures of immunity and age and aEIR? [note: following consultation this was not considered an essential revision]

Finally, the mgcv packages allows a lot of flexibility when fitting GAMS/GAMMs including allowing for autocorrelated errors. Without diving into the code (which I haven't done) it is not clear what choices were made and why form the supplementary material alone. Are key results robust to modelling decisions made, and what diagnostics checks have been done?

Reviewer #2:

This is a data analysis exercise using cohort studies taken across the spectrum of Pf transmission in Africa. They use age and number of infectious bites per year to characterise how immunity develops over time. This is a very nice dataset and overall the paper is well written, and the plots are informative and clear. Code and data were provided online in order to reproduce the results.

I have a few concerns in the following paragraphs.

“aEIR as a metric of individual exposure”:

The annual entomological inoculation rate (aEIR) is estimated from monthly mosquito household catch surveys. This estimated quantity is then plugged into the models (on the log scale) as the proxy for the total number of infectious bites per year. Given that in the lowest transmission setting, the median number of infectious bites is 2 per year, this implies that a median of 2 infectious mosquitoes were captured over the course of one year. What is the median denominator here, e.g. how many mosquitoes were captured? The uncertainty on these aEIR estimates must be much larger for the low transmission settings vs high transmission settings. This may explain why the R2 is also much lower when correlating log(aEIR) and hazard of infection (as calculated from a time-to-event model). This may also explain the trends observed in Figure 3 (top right panel), where the individuals with lowest aEIR have lower parasite densities that those with medium aEIR.

This potentially indicates that the aEIR is not a good estimate of the true number of infectious bites at very low transmission? If so, this means the conclusions drawn from the models cannot be taken at face value. [note: following consultation the consensus was that EIR is not thought to be problematic, though models in which future values of EIR influence the present are considered to be unjustifiable (since events in the future shouldn't influence the present)]

Model comparison:

The online code was broken in parts and I had to spend an hour debugging it. This is quite annoying!

My main question was to understand whether the more complex non-linear models (GAMs) were truly better than their linear counterparts. In particular whether the pattern shown in Figure 5B was not the result of over-fitting. If I understand Figure 5B correctly (probably the most important plot in the paper), a 2 year old with an aEIR of 2 infectious bites per year has on average the same anti-disease immunity as a 5 year old with an aEIR of ~200 infectious bites per year. This is very hard to believe and my prior on this being true would be very low. I believe this may be an artefact due to the problem highlighted above for the extremely low aEIRs.

I ran a series of 50 random 10-fold cross-validation experiments in order to characterize the out-of-sample mean squared error of each of the models 1-3 and a fourth model: the linear equivalent of model 3 (interaction between age and log(aEIR) with random effects at the individual and household level). The author's model 2 (GAM, no interaction term) performs best on average but the effect is very small. The fact that the non-linear model fits best the data is driving the surprising conclusions and I remain skeptical regarding the following line of the Abstract:

"Our findings suggest a strong effect of age on both types of immunity, that is not explained by cumulative exposure. They also show a non-linear effect of transmission intensity, where children living in the lowest transmission intensity setting appear to develop immunity faster than those experiencing higher transmission."

Even if the underlying relationship is truly non-linear, it would be useful to report the conclusions of a linear model which are likely to be generalisable. This would be similar to what the authors have done (subsection “Anti-parasite immunity”, fourth paragraph), but for instance reported as: for a twofold increase in yearly inoculation, the pyrogenic densities decrease by X amount.

Reviewer #3:

It's tough to come out against this one as the authors have used some great data sets and innovative statistical modelling approaches to tackle a very hard question, namely how is immunity to malaria acquired in moderate to high transmission settings. My concern is that the design of the data, and the design of the model don't fit well together leading to some hard to explain results.

Hard to explain results:

There are at least two results which I would put in the 'hard to explain' category.

Firstly, the authors have proposed biologically and epidemiologically well-informed hypotheses to explain the non-monotonic relationship with aEIR in Figure 7. However a simpler hypothesis is that this is an artefact of combining this particular model and this particular data set.

The second result is from Figure 6 where the fever threshold for 39C comes in and out of view as we increase from (a) aEIR = 2; (b) aEIR = 10; (c) aEIR = 50; to (d) aEIR = 200. This result would imply that a 2 year old with parasite density of 1e6 parasites/uL has fever > 39C when aEIR = 2; tolerates parasites better by having fever < 39C at aEIR = 10; then tolerates parasites worse by having fever > 39C when aEIR = 50; before finally switching back to better toleration of parasites with fever < 39C when aEIR = 200.

"They also show a non-linear effect of transmission intensity, where children living in the lowest transmission intensity setting appear to develop immunity faster than those experiencing higher transmission."

In an Abstract, one has little choice but to read a statement literally. This implies that children living in the lowest transmission setting appear to develop immunity faster than those experiencing higher transmission. This flies in the face of conventional malaria epidemiology. Perhaps the authors are trying to say something more subtle like there is a diminishing contribution to the acquisition of immunity with subsequent infections.

Model:

The authors have provided a change in notation to emphasise the utilisation of random effects, but otherwise left the model and results unchanged. The random effects at the individual and household level will account for a substantial degree of the variation between children. However, within an individual the only piece of longitudinal information included is age, incremented by the index k for visit. Otherwise, incidence of symptomatic episodes are independent (and there can be up to 30 of them). For example, the probability of symptomatic malaria is the same for a child on their 1st and 10th episodes.

It is notable that although age is updated at each visit, aEIR is not – instead being averaged over the duration of follow-up. Looking at Figure 5 of the original publication by Kamya et al., we see that there is a lot of time-dependent variation. For example, in Kihihi there is a huge spike in aEIR in 2013 towards the end of the study.

Some of the 'hard to explain' results could be arising from non-linearities and tensor interactions in the generalised additive models. Looking at models AP1-3, I note very little change in% deviance explained despite changes in the AIC. Looking at models SM1-3, I note that as model complexity increases, the% deviance explained actually decreases, despite the AIC appearing to favouring the more complex models.

Data:

I am concerned that the passively detected cases and routinely (every 3 months) detected cases are fundamentally incompatible.

If I interpret things correctly, a passively detected case will by definition contribute 1 count of a symptomatic episode and 1 light-microscopy measurement of parasite density. These data provide no discriminatory power on whether an infection (upon becoming microscopically detectable) becomes symptomatic, and no information on temperatures < 38°C.

By not having the precondition of treatment-seeking behaviour and fever >38°C, routinely detected cases arguably provide richer information. Although the majority of these measurements are parasite negative (by microscopy) and presumably excluded.

In Table 1 there are reported to be 2447 + 1555 + 207 = 4209 symptomatic episodes versus 955 + 331 + 145 = 1431 asymptomatic parasitaemia episodes. This suggests that the passively detected cases are provided far more data points.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Quantification of anti-parasite and anti-disease immunity to malaria as a function of age and exposure" for further consideration at eLife. Your revised article has been favorably evaluated by Prabhat Jha (Senior Editor), and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers noted that the authors have worked hard to address the raised concerns, generating new sensitivity analyses that lend supporting evidence to their conclusions and providing new presentations of the data to better visualise the non-monotonic relationships.

The authors have now adequately addressed all but one of the reviewers' main concerns.

The one last point, which reviewer 3 noted the authors did not address in their previous response, was related to the unexpected result of% Deviance Explained as the complexity increases for the nested models for anti-parasite immunity and overall immunity against symptomatic malaria. From the previous review:

"Looking at models AP1-3, I note very little change in% deviance explained despite changes in the AIC. Looking at models SM1-3, I note that as model complexity increases, the% deviance explained actually decreases, despite the AIC appearing to favouring the more complex models."

This is an important point that requires a response.

Reviewer 2 also made the comment that It would be useful if the authors provided an extra variable in their data on github: passive versus active detection.
