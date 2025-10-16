# Peer review - Round 1

Editors:
- Talía Malagón, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77434.sa0](https://doi.org/10.7554/eLife.77434.sa0)

This paper will be of interest to public health specialists and cancer scientists working in cancer prevention. The work presents valuable data on how the COVID-19 pandemic has impacted breast cancer screening indicators compared with previous years. Overall, the results support the assertion that while many key indicators have not been substantially impacted, the screening participation rate declined compared to the pre-pandemic era.


---

# Peer review - Round 1

Editors:
- Talía Malagón, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77434.sa1](https://doi.org/10.7554/eLife.77434.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Impact of the COVID-19 pandemic on breast cancer screening indicators in a Spanish population-based program: a cohort study" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Paolo Giorgi Rossi (Reviewer #2).

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

– Please provide an analysis of participation rates (participated/invited) additional to the distribution of participant distribution in Table 2 to adjust for changes in invitation distributions over time.

– Remove the description of the study as a "quasi-experimental" study.

– Please comment on the fact that recall rates and false positive rates are not independent outcomes.

– Consider performing a detailed monthly analysis of the selected indicators.

– Specify whether the analysis method accounted for the non-independence of the observations (multiple observations per woman). If not, please employ an analysis method that accounts for the correlation between observations, such as a multilevel model or a robust estimate of the variance.

– Specify the time frame considered for relevant outcomes such as participation in an invitation or detection.

– Please be careful not to interpret ORs as RRs. If the authors would like to use the results of the regression model as percentage reduction in the probability of an outcome, then they should use log-binomial models rather than logistic regression models.

– Please comment on whether changes in private care use may have had an impact on the results.

– Please comment on whether different screening invitation strategies were used during the pandemic compared with prior to the pandemic.

– If available, it would be interesting to also include participant compliance with recall for further assessment as an indicator to the analysis.

Reviewer #1 (Recommendations for the authors):

– Table 1 shows clearly that there were differences in the types of women who were invited in the pre- and post-COVID eras. This means that the differences in the types of participants in Table 2 reflect in part differences in invitations rather than differences in participation in the pre- and post-COVID era. Presumably, differences in invitation are due to changes in population composition/eligibility over time rather than changes attributable to the pandemic, and we would want to adjust for this when looking at whether participation has changed in the COVID era. Rather than examine participant distribution in Table 2, which is highly influenced by participant invitation, it would be more interesting to change Table 2 to look at participation rates instead (#participated/#invited) to see if the rates changed over time by participant characteristics.

– Discussion: "Although the aim of our study was not to evaluate the factors associated with participation, we found a lower representation of high-income women in the post-COVID-19 period." The lower proportion of high-income participants in the post-COVID-19 era is due to the lower proportion of high-income women which were invited in the post-COVID-19 era, and so may reflect changes in invitation rather than in participation. Please consider comparing the participation rates instead, as this will show whether high income women were less likely to participate in screening in the post-COVID-19 era than in the pre-COVID era.

– For Tables 1-3, the tests for significance appear to have been done by row rather for the whole RXC cross-tabulation distribution of a variable (for example, compare the % invitations in the 50-54 age group in pre-Covid to post-Covid in 2X2 tables, rather than compare the whole age distribution in pre-COVID vs post-COVID in the a RXC table). While this likely does not matter too much for Tables 1 & 2 due to the large number of participants, I think it could influence results in Table 3 due to the low number of cancer cases, which leads to lower statistical power when looking at individual rows. The authors should consider using the Freeman-Halton extension of the Fisher Test for contingency tables larger than 2X2 to compare the stage distributions across eras rather than comparing the 2X2 tables for individual cancer stages.

– Figure 2: I would suggest including the overall estimates as well as the stratified (prevalent/incident) estimates. It is possible the results for the recall would be significant if all events were combined together. The similarity of the ORs suggests that there is no interaction and that is justifiable to provide an overall estimate for all these outcomes.

– While the authors have posted their data and code in line with eLife's data availability policy, the files are currently in restricted access. It would have been nice to be able to review these elements of the research as well.

– The analysis showed the cancer detection rate per number of participants was stable over time. However, I would have been interested also to see if the cancer detection rate per number of invitations has changed over time. Presumably, if participation is lower, then the overall yield of the program in terms of detection rate among all eligible (invited) women should be lower in the COVID-19 era.

Reviewer #2 (Recommendations for the authors):

I do not agree about the definition of a quasi-experimental study. I think this is a before/after study studying the impact of an external accident that cannot be considered as a natural experiment. The changes in screening activities that occurred as a consequence of the pandemic cannot be considered as a simulation of the consequences of a possible intervention (maybe suspending the invitations? shifting to opportunistic screening?). Thus, there is no possible intervention that we would like to evaluate in an experimental study design that could be assimilated to the pandemic. Furthermore, the pandemic had so many other impacts on society that, even if we could identify a theoretical similar intervention to our changes in the screening, the effects would be extremely confounded.

The interpretation of statistical significance in the case of recall and false-positive is tricky. The latter parameter should be fully determined given the recall rate and the detection rate. Therefore, if you are affirming that the recall rate increased in a way that is unlikely to be by chance, and detection is similar if not lower, the false positive cannot increase by chance but increased because the recall rate increased, even if the difference is not statistically significant.

Finally, a detailed analysis of the number of invitations per month or week and the mammographies performed could explain who actually delayed or decided not to attend at all. For example, did the women scheduled for the months of March and April attend less than those scheduled in September? In the previous attenders, can you compute the average delay since the previous examination month by month? This indicator would be very efficient in terms of statistical power and strictly related to the potential impact on health since it represents the actual delay in mammograms and potentially in diagnoses that occurred in women who attended… Given that the woman's id is the same through different rounds, you should be able to compute the distance between the previous mammogram ad present mammogram for three rounds before covid (n-1) and for covid round. the same could be done also for invitations; then delay in invitation could be used as a determinant of the participation. I think this would be a much more interesting analysis with more universal validity and relevance for the international audience.

Abstract

Methods: see general comments about "quasi-experimental".

please specify what do you mean with "observations"; invitations? screening episodes?

Results: I suggest not using the percentage difference in odds to describe the ORs (i.e. 11% lower) because this way of presenting results suggests that there was an 11% decrease in participation was, but actually the decrease is about 8% in relative terms and 3.7% as difference. I suggest using relative risks or prevalence ratios building log-binomial models, otherwise do not use 1-OR to report changes. Outcomes are very common and the OR is not a good estimator of the RR or the PR.

Introduction

It is well written, clear and focussed.

Methods

Page 4, line 10. Does the number refer to inhabitants or to the female target population? The second would be better.

Page 4 line 20: please explain better what you mean with "observations" invitation and I suppose all the consequent actions if the woman participated…

the sub-heading "outcomes" actually describes outcomes and co-variate or variables of interest.

Page 6 lines 6-9. this seems to be more relevant for analyses. did you really consider the observations regarding the same woman as independent? I suggest taking into account the possible non-independence of the observations using a multilevel model or a robust estimate of the variance. The effect should not be too important for stratified models or models with the interaction between screening round and Covid, but the estimate of the variance would be more adequate to the structure of the sample.

Page 6, line 20: participation in the round what does it mean? Which is the time since the invitation to be considered a participant? This is a critical point, in fact, if you included women who had the mammogram up to 20 months after the invitation, the follow-up time is shorter for the covid round than for the previous round. This could be a strong bias. Please explain what is the time considered for participating and demonstrate that there could not be a follow-up bias when comparing the last with previous rounds. This issue is also relevant for the detection rate.

Statistical analyses: see the previous comment about the structure of variance for non-independent observations.

Results

Page 8, line 12: please do not interpret 1-OR as 1-RR and thus a percentage of reduction. same in page 12 line 1.

In all the results I suggest reporting only one digit for decimals in raw percentages.

Table 3, probably even 1 digit for decimals for percentages is too much.

Discussion

The first sentence states "in this longitudinal study". I am not sure this study design is really a longitudinal study, i.e. a cohort. Actually, the study seems to be analysed as repeated cross-sectional surveys or as several short follow up cohorts (one for each round). I do not think it is really important to give a name or classify the study design, but in the methods, you did not present it as a cohort, so you should not introduce this concept in the discussion.

Page 17, lines 19-25: I suggest also another possible explanation, not mutually exclusive to the one proposed by the authors. Among women not attending screening, there are probably many women who perform mammography more or less regularly in opportunistic screening with private providers. During the lockdown, all the providers experienced difficulties in organizing planned activity as mammography in asymptomatic women. Therefore, it is possible that women who usually perform mammography in private had difficulties in getting their mammogram timely and when received the invitation by the program decided to participate. This could be a specular effect of that observed in women regularly attending the screening program that this time decided not to attend, probably because the invitation was late and they seek for mammography elsewhere. The disruption of planned activities during the lockdown, in all providers, may explain both decrease in participation in regular attendees and the increase in never attenders. This is also consistent with a decrease in high socioeconomic status in participants post covid, in fact, these women are those who may have a higher propensity to seek a mammogram in the private sector.

The authors correctly recognize the limit of assuming independence of the observation, but, if the id is woman-specific and is the same across the rounds, there is no need to make this assumption. I also agree that stratified analyses by type of round reduce the impact of this limit.

Page 19, line 1. "The same target population" this sentence may be confusing, the study does not have a closed cohort design, so each subsequent round targets slightly different populations.

Reviewer #3 (Recommendations for the authors):

I consider the work well done and interesting so for me is publishable with the following small revisions:

1. the authors describe what invitation modes were used up to the pandemic (invitation letter with prefixed appointment) but it is not clear what recruitment strategies were used during the pandemic. Were there any changes in recruitment methods? It would be useful for the readers to get an idea.

2. Page 4, lines 25-32; wouldn't this whole part go into the results?

3. One of the parameters used for the comparison is the recall rate. the authors limit their analysis the recall rate (number of women sent to the second level) and do not mention the compliance of women to in-depth diagnostics. Comparing the recall rates certainly allows to highlight a potential change in radiologists' behaviours, connected to all sanitization and social distancing measures that had to be put in place. It could have been interesting also to evaluate the presence (or not) of a change in women's behaviour and their willingness to compliance further assessments, despite the pandemic.

4. Among the analysed parameters, invitation coverage (the number of women invited out of the target population) was not included: it would have been interesting to know the trend of this parameter as an index of the resilience of the screening program.

5. the authors made a pre and post covid-19 pandemic comparison. It is a very marginal issue but I would not talk about post covid since we are still inside the pandemic (although hopefully in the final stages); what about pre covid and covid?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Impact of the COVID-19 pandemic on breast cancer screening indicators in a Spanish population-based program: a cohort study" for further consideration by eLife. Your revised article has been evaluated by a Senior Editor and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The first paragraph of the Discussion should be modified to reflect the new results, as some of the changes in recall and false positives are now significant.

2. The revision indicates that different invitation approaches were used for different types of participants (first, regular, non-participant) during the post-COVID era. Please discuss this in the Discussion, and how this may have impacted the results in Figure 1; it is likely some of the differences in participation may be due to these different invitation practices.

3. The analysis of compliance with recall (Table 5 in the response to reviewers) would be of interest to some readers and should be included in the manuscript.
