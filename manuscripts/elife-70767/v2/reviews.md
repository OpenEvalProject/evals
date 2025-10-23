# Peer review - Round 1

Editors:
- Jennifer Flegg, https://ror.org/01ej9dk98 The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70767.sa0](https://doi.org/10.7554/eLife.70767.sa0)

This paper is a timely update to the authors previous work and will be of interest to those working on public health responses and the mathematical modelling of infectious diseases. In this work the authors infer the generation interval of SARS–CoV–2 which can allow for the assessment of public health measures. The derivation of the likelihood function is also of interest to mathematical modellers as it allows for the inference of the generation interval from data sets where susceptible depletion may dominate infection dynamics.


---

# Peer review - Round 1

Editors:
- Jennifer Flegg, https://ror.org/01ej9dk98 The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70767.sa1](https://doi.org/10.7554/eLife.70767.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Inference of SARS–CoV–2 generation times using UK household data" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Rowland Raymond Kao (Reviewer #1); Eamon Conway (Reviewer #2).

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Specifically, all of the reviewers agreed that there wasn't enough novelty in the manuscript, given that the main methodology has been previously published, to be considered in eLife. There were also concerns over the generalisability of the work. The work is very well written and important but would be better suited in a more specialised journal. The authors should consider emphasising the changes to the likelihood function to deal with household data, since this is a novel contribution of the work.

Reviewer #1:

This paper extends a previous analytical method that the authors developed to evaluate the time to infectiousness of COVID–19, in order to evaluate differences in the generation interval across different time periods during the course of the pandemic in England in 2020. The time to infectiousness (i.e. how long is it until infected individuals start producing virus in a way that is a risk of infecting others) is a generalisable concept. That is unless we expect there to be inherent differences in the way infected individuals progress to becoming infectious (when looking at distributions of outcomes, comparing between populations of interest) we can take a result from one population of individuals, and assume that it gives us a reasonable idea of how long it takes to become infectious, in another population. Differences in the way people come into contact with each other will have some influence on this, but generally speaking if a person is infectious after 4 days in China, you should be considering a person to be a risk of infecting others after 4 days in other countries as well.

In contrast, generation time (how long does it take an infected person, on average, to infect the persons they are going to infect?) depends strongly not just on the inherent characteristics of the virus, and progression of disease in individuals, but also (more strongly that time to infectiousness) the circumstances of contact between individuals. Because generation time is tied to so many other factors, one of the most reliable ways to estimate generation times is to analyse data where there are groups of in–contact individuals where there is likely to be highly likely that there is only one generation of transmission involved (where contacts between individuals are clustered, possibly two but with three generations highly unlikely). In this case, the most important unknowns are the time from when individuals are infected to when become infectious and the time to when they test positive – the requirement for time to infectiousness is why the methods used in the initial paper are appropriate for generating better generation time estimates.

As most published results relate to the very early stages of the pandemic in China where extensive contact tracing was done, there is some interest in understanding whether the generation times differ substantially in other locations and if they change over time (and therefore, why). In this analysis, Hart et al. estimate generation times across three, three month time periods using household contact data in England in 2020, and show differences in generation time estimates depending on the method used (in particular, when considering an approach which ties infectiousness to symptomatic development which they showed provided better results compared to other methods in their previous paper) and the period of 2020 over which the estimates are taken. While the result appears technically robust for the data analysed, its usefulness is limited by difficulty in extending the results – while a different dataset from ones used for the analyses in China they refer to, and from the result of Challen et al. that looked at contacts of international travellers in the UK, it is also in its own way quite specific and further breakdown of possible factors would be worthwhile. First, the limitations to household contacts means that it is not representative of general transmission in the population – household contacts are high risk, with many opportunities for transmission and may therefore be relatively short. Generalised contacts outside of households are likely to be less frequent and often of shorter duration and more strongly affected by diurnal and weekly rhythms. Second, it is also known that demographic factors such as ethnicity and income are strongly linked to infection and severe infection risk. While this does not tell us directly about any links to infectiousness and infectious contact, it is reasonable to consider a connection – and therefore a link to generation times. As such, in this relatively small sample (172 households, with much higher numbers in the first 3 months, compared to the middle or last three) differences in demographics may influence generation times as well. Finally, the α variant, first identified in Kent, was probably circulating for much of the final three months of this analysis – dominant by early 2021 in the UK, it would have had a variable proportion across much of those final three months, and also varied geographically in terms of proportion as well, with a much earlier rise in the SE and in London. Unless those proportions are known, it would be difficult to know how much differences in generation times are due to the variant, to demographics, or other, possibly behavioural factors. Thus, some caution should be applied before taking general lessons from it, at least in the absence of those additional considerations.

In my view, the bulk of the methodological innovation was in the original paper and therefore as it stands, the principle interest is in the estimates of the generation times themselves. However, while I do think there is some interest in these results really in my view, they are specific and situational. The data are limited as they are to a relatively small number of households, involving only household contacts, where the uncertainties of variants of concern, and demographics including ethnicity, income, nature of housing, etc. make it difficult to interpret the results with real generality. I would also recommend that the authors include a discussion of the biases that may limit the generality of their work.

Reviewer #2:

In this work, Hart et al. infer the generation interval for SARS–CoV–2 using infector–infectee pairs from household data. The generation interval is obtained across three different time intervals (March–April, May–August and September–November) and using both an "independent transmission" model and the "mechanistic" model that was originally proposed in Hart et al. 2021. The main result is that the inferred generation interval in September–November has decreased compared to the earlier months of the pandemic, irrespective of the model considered. Overall, the conclusions drawn in the paper are well supported and have been shown to be robust through a thorough sensitivity analysis.

Strengths

– They use a mechanistic model to account for the change in infectivity at symptom onset.

– A major strength of this investigation is that they can observe the dynamics of the generation time over three different time periods of the pandemic. To my knowledge, this is a novel result that allows for a more up to date understanding of SARS–CoV–2 transmission.

– Whilst not highlighted in the text, it appears that there has been significant effort to extend the likelihood function to appropriately model household dynamics. This is non–trivial work in my opinion, and I believe the details of the derivation will be of use to mathematical modellers that deal with susceptible depletion in their data.

Weaknesses

– The main weakness of the paper in its current form is that the analysis appears superficial, with a large amount of curve fitting and very little explanation. It would be beneficial if the authors delved more deeply into their results, especially with the mechanistic model. It would be very interesting to relate the changes in generation time to mechanisms of transmission.

– The authors calculate the mean and standard deviation of the generation interval across three different time points; however, they only present one figure with the distribution of the generation time (Figure 2). It would be interesting to know how the generation time distribution changes in time, as opposed to just the mean and standard deviation. I believe that such an analysis would link nicely to their previous work, where they highlight the importance of ongoing public health measures such as contact tracing.

I would like to congratulate the authors on a timely update to their work. I thoroughly enjoyed seeing their updated results, especially as some of the questions addressed have been of interest to myself. I do however have some recommendations.

I understand that writing a rather mathematical paper for a general audience can be quite complicated, but I feel in this case that the authors have done themselves a disservice by not emphasising the technical concepts in the paper. At first read it appears that the authors have taken their model and fitted values, which is not particularly interesting. It was only once I made it to the Materials and methods section where I found the significant extension on previous work. I believe highlighting the adaptation of the likelihood function to account for the household level data was non–trivial and should be mentioned earlier (I believe this could be placed in the Results section), adding to the appeal of the paper. I note that susceptible depletion is mentioned in the main text, but I believe you should elaborate on how the likelihood function has been constructed to account for this.

Throughout the work the posterior mean has been used as a point estimate for parameter values. I believe a more natural point estimate would be to choose the maximum of the posterior distribution. I notice that when looking at the posterior distributions of the mechanistic model (Figure S2), the maximum value of the posterior and the posterior mean differ by a wide mark for α_p and k_E/k_inc. The impact of this choice might be minimal, but I believe it should be investigated.

It would be interesting to know how the generation time distribution changes in time, as opposed to just the mean and standard deviation. This would be a simple extension where they take the point estimates for multiple time points to show the temporal variation. I believe that such an analysis would link nicely to your previous work.

I am uncertain why the arguments of the paragraph at line 227 are required. It appears that the point is to justify the inclusion of a 1/n factor in the force of infection, however, I believe this is an obvious factor to include (I would use 1/(n–1) rather than 1/n though) that does not require parameter fitting to understand. If you were to consider a multigroup SIR model with varying population numbers the 1/(n–1), where n is the number of individuals in the group, is included so as the force of infection acts on the proportion of individuals that are susceptible. If this was not the case, then a different β would be required in each group. As you argue that the β value is a constant and does not vary between households it makes sense that the β value must be scaled by the number of individuals in the household, otherwise you would need a different β value for each house (which would be impossible to infer given the small household sizes).

For reproducibility and transparency, I would like the authors to provide all code used to generate results, in line with eLife's policies on availability of data, software and research materials. This will allow other researchers to implement the methods they have developed on other data sets, but also enable confirmation that there is no coding mistakes.

Reviewer #3:

The authors have previously published a mechanistic model for inferring infectiousness profile that explicitly models dependence of the risk of onward transmission on the onset of symptoms on an individual. In the present study, they apply this model as well as another more commonly used model which assumes these two things (transmission risk and onset of symptoms) to be independent, to data from a household study conducted from March–Nov 2020 in the UK. Both the models find that the mean generation time in Sept–Nov 2020 is shorter than in the earlier periods of the study.

This is well–presented study with careful analysis and extensive sensitive analysis which shows that the modelled estimates are robust to a range of assumptions.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Inference of the SARS–CoV–2 generation time using UK household data" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Rowland Raymond Kao (Reviewer #1); Eamon Conway (Reviewer #2).

This paper is a timely update to the authors previous work and will be of interest to those working on public health responses and the mathematical modelling of infectious diseases. In this work the authors infer the generation interval of SARS–CoV–2 which can allow for the assessment of public health measures. The derivation of the likelihood function is also of interest to mathematical modellers as it allows for the inference of the generation interval from data sets where susceptible depletion may dominate infection dynamics.

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post–review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

1) While the observation of reduced generation times is both useful if true, and potentially plausible, it may not be robust. The overlap between the posterior estimates of generation times etc. are quite broad – and looking across three periods it doesn't seem like it would take much to change the trends in even the mean values.

2) In particular, the size of the study is not that large, and in each household, it seems from the Miller paper, that only two PCR tests were taken – as the approach does not consider the impact of latent processes (i.e. missed infections) it would be important to know whether a slight bias in missed infections across periods would impact on the conclusions.

3) The authors also state (line 573) that "Potential bias towards more recent infection of the primary host if community prevalence is increasing, or less recent if prevalence is decreasing (Britton and Scalia 900 Tomba, 2019; Ferretti et al., 2020b; Lehtinen et al., 2021), was neglected." Could this also provide some possible explanation for the shift in generation times? Especially given that the justify their assumption in part on the analysis across individual months, and there are relatively few recruited households (on the order of 10 I think, based on Figure 3 in the supplement).

4) The authors also say that (line 150) " we corrected for the regularity of household contacts to derive more widely applicable estimates of the generation time. We did this by including a factor in the likelihood to account for each infected individual avoiding infection from household contacts that occurred prior to their actual time of infection (see Materials and Methods for full details of our approach)." This sounds really interesting and would greatly increase the generality of the outcome. But unfortunately, from the description in the material and methods I was not able to figure out exactly why this was – which doesn't mean it’s wrong of course, but it would be helpful to me to have a more detailed description.

5) The authors state that on line 163 that "point estimates for each model using the posterior means of fitted model parameters because the mode of the joint posterior distribution could not easily be calculated from the output of the MCMC

procedure." It would be important to know whether there are any correlations in the parameter posteriors that might make inappropriate.

6) I spent some time trying to understand if there could be any issue causing the higher fraction of pre symptomatic transmission, which is the most unexpected result, and I could not find any obvious one. Same for the high variance of the generation time distribution (though this and the high pre–symptomatic transmission could be related). Hence, I think that these results can be published in the current form.

On the other way, the temporal changes in generation time do not seem to account for the epidemic dynamics and therefore would be biased upward in Spring 2020 and downward in Autumn 2020 as observed. The authors are aware of that as they explain in the Discussion, but I think that the author should either correct for this effect in their approach or clarify better how this effect is accounted for and what may its contribution be.

Reviewer #1:

The additional work done by the authors has been considerable and substantially increased the potential value of the work. In particular, the addition of data augmentation MCMC helps to provide greater depth to the outcomes, and the identification of declining generation times useful (especially if it could be established in 'real time' – i.e. rather than retrospectively, but to aid in understanding ongoing epidemics) and interesting.

I do have a few concerns which in my view need to be addressed before it would be suitable for publication in eLife.

First, while the observation of reduced generation times is both useful if true, and potentially plausible, it may not be robust. The overlap between the posterior estimates of generation times etc. are quite broad – and looking across three periods it doesn't seem like it would take much to change the trends in even the mean values.

In particular, the size of the study is not that large, and in each household, it seems from the Miller paper, that only two PCR tests were taken – as the approach does not consider the impact of latent processes (i.e. missed infections) it would be important to know whether a slight bias in missed infections across periods would impact on the conclusions.

The authors also state (line 573) that "Potential bias towards more recent infection of the primary host if community prevalence is increasing, or less recent if prevalence is decreasing (Britton and Scalia 900 Tomba, 2019; Ferretti et al., 2020b; Lehtinen et al., 2021), was neglected." Could this also provide some possible explanation for the shift in generation times? Especially given that the justify their assumption in part on the analysis across individual months, and there are relatively few recruited households (on the order of 10 I think, based on Figure 3 in the supplement).

The authors also say that (line 150) " we corrected for the regularity of household contacts to derive more widely applicable estimates of the generation time. We did this by including a factor in the likelihood to account for each infected individual avoiding infection from household contacts that occurred prior to their actual time of infection (see Materials and Methods for full details of our approach)." This sounds really interesting and would greatly increase the generality of the outcome. But unfortunately, from the description in the material and methods I was not able to figure out exactly why this was – which doesn't mean it’s wrong of course, but it would be helpful to me to have a more detailed description.

The authors state that on line 163 that "point estimates for each model using the posterior means of fitted model parameters because the mode of the joint posterior distribution could not easily be calculated from the output of the MCMC

procedure." It would be important to know whether there are any correlations in the parameter posteriors that might make inappropriate.

Reviewer #2:

I'd like to thank the authors for updating the manuscript in a very thorough manner, I really enjoyed reading through the revisions. I believe that the authors have addressed all of my concerns.

Reviewer #4:

This excellent paper suggests that despite extensive studies, we have not yet reached a full understanding of the generation time of SARS–CoV–2. The study is a robust examination of the subject of generation time within households in UK, which may not be representative of transmission in other contexts. It is unclear to the reviewers if temporal changes in generation time are real and attributable to e.g. the appearance of B.1.177.

This work is sound. While surprising, the results are supported by multiple statistical/modelling approaches and robustness analyses, and believable.

The three most striking results are:

1) The width of the generation time distribution is much wider than in previous works. While this is undoubtedly surprising, the explanation by the authors is believable: home quarantine in the UK is probably less effective in stopping late transmissions within households and may even amplify them.

2) The fraction of pre-symptomatic transmissions is >70%, quite high compared to most previous estimates. Combined with the high number of fully asymptomatic individuals, it would imply that <20% of transmissions come from individuals showing symptoms. This result seems also hard to square with the previous one, which would suggest a wide distribution of TOST. Of course, this estimate may be affected by the setting, since the analysis is restricted to households and therefore a higher force of infection.

3) According to this work, the generation time changed between spring 2020 and autumn 2020 in the UK. This corresponds to the arrival of the B.1.177 lineage, probably more infectious than previous variants, but also to a different epidemiological phase of the epidemic: lockdown followed by gradual reopening in spring/summer, with a corresponding decrease in incidence, then a new wave in autumn with an increase in the number of cases until November. The authors do not correct for this epidemiological dynamic, therefore leaving open the possibility that it would cause an apparent change in generation time similar to the observed one. Other explanations (e.g. behavioural or reporting ones) may be possible.

It is important to remark that many of the results of the mechanistic model may be affected by the assumption that longer incubation intervals correspond to higher infectiousness. The agreement with the results of the simpler model with independent incubation period and generation time implies that this assumption is not relevant for the main results (with the possible exception of the longer mean generation time).

Recommendations:

The results of the paper look really robust.

I spent some time trying to understand if there could be any issue causing the higher fraction of pre symptomatic transmission, which is the most unexpected result, and I could not find any obvious one. Same for the high variance of the generation time distribution (though this and the high pre–symptomatic transmission could be related). Hence, I think that these results can be published in the current form.

On the other way, the temporal changes in generation time do not seem to account for the epidemic dynamics and therefore would be biased upward in Spring 2020 and downward in Autumn 2020 as observed. The authors are aware of that as they explain in the Discussion, but I think that the author should either correct for this effect in their approach or clarify better how this effect is accounted for and what may its contribution be.
