# Peer review - Round 1

Editors:
- Ben S Cooper, Mahidol University Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58785.sa1](https://doi.org/10.7554/eLife.58785.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper describe key features of the COVID-19 epidemic and public health response in Australia up until mid-April. It represents a concise and worthwhile contribution to the COVID-19 literature.

Decision letter after peer review:

Thank you for submitting your article "Early analysis of the Australian COVID-19 epidemic" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ben S Cooper as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Andrew James Kerr Conlan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Please aim to submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter we also need to see the corresponding revision in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This paper describe key features of the COVID-19 epidemic and public health response in Australia up until mid-April. It represents a concise and worthwhile contribution to the COVID-19 literature. The paper mostly uses established methodologies (or recently described extensions of established methodology) and the findings are likely to be of broad interest. The main limitation (which is acknowledged by the authors) is that no attempt is made to quantify the likely effect of different interventions. Adding this would strengthen the paper but given that multiple measures were enacted at different times and the limited extent of the outbreak further investigation into the relative impact of different measures would be challenging and is not considered an essential revision.

Required revisions:

1) Subsection “Forecasting case counts”. The observation model is a little hard to understand and needs clarification. It appears to be saying that there are two points in the course of an infection when the infection might be observed (in both cases with probability pobs): either the day when the infected person enters the second infectious compartment (I2) or the day they cease to be infectious and enter the R compartment. With this formulation it looks like it's possible for there to be more observed infections than there are infected hosts. It's also not specified whether S, E1, E2 etc represent absolute numbers or the proportion of hosts in the compartments. The initial conditions suggest that these are proportions, but if they are proportions then the observation model makes no sense (as then the expected number of observed infections per day would be at most 1). It's also surprising that there is not a delay between the state transitions in the model and the observations yt (assuming yt represents the number of infections observed at time t). Maybe it's just that accounting for such a delay would make no practical difference to the conclusions and for that reason the delay can be ignored. If that's the case it's worth saying so. Also worth saying explicitly somewhere that units of time are days – this doesn't seem to be mentioned anywhere.

2) To put the findings into context it would be helpful to describe what was not done as well as what was. In particular, information on recommendations and practice regarding mask wearing and hand hygiene would be of interest as would information on use of/lack of use of contact tracing apps over this period. To put the results into context it might also be helpful to extend the Discussion to consider and contrast the magnitude of the estimated effective reproduction numbers before and after interventions compared to other countries if space permits.

3) "contact quarantine" is reported to have been used. It would be helpful to clarify the dates when this started and any information on the success and speed of tracing contacts of cases would be helpful here.

4) To help put the Australian experience in perspective it would also be helpful to briefly give information on factors that might influence spread (such as temperature, humidity, crowding etc) and perhaps consider these (very briefly) in the Discussion.

5) Subsection “Forecasting the clinical burden”: Please give a brief explanation of the sequential Monte Carlo method used in the Materials and methods section.

6) Subsection “Estimating the effective reproduction number over time”: "optimally selected". Selected to optimise what?

7) Subsection “Accounting for imported cases”: "50%, 50% and 80%"?

8) "narrow uniform priors" – can these be specified in the Materials and methods.

9) Table 2: Can "Time of first exposure" be defined? Unclear what this means.

10) "Australia's symptomatic case ascertainment rate is very high (between 77 and 100%)".

This seems extremely high given that we know that many people experience very mild symptoms. Is this really credible? Unfortunately the link to London School of Hygiene and Tropical Medicine Mathematical Modelling of Infectious Diseases nCoV working group, 2020, which makes this claim does not seem to be working so it's not possible to confidently assess the assumptions behind this. However, if we assume the link should be to https://cmmid.github.io/topics/covid19/global_cfr_estimates.html this this would indicate that the estimate is based on the case fatality ratio, and the assumption that true CFR is 1.4% (based on Chinese data). However, case fatality ratio is highly age dependent and given lack of widespread dissemination in the community it seems at least possible that spread in Australia might have been largely confined to younger age groups leading to lower CFR. Given this estimate seems so surprising (and is not based on peer-reviewed research) it seems appropriate at least to add some caveats to this. Wouldn't this also depend on precisely what case definition is being used?

11) Figure 1—figure supplement 2 reports states "encouraging" parents to keep children from school. Is there any information that can be shared on what actually happened (i.e. what proportion of school aged children went to school)?

12) It would also be helpful to update the numbers reported in the Introduction.

13) Given that the time periods for model prediction are now in the past, it would be instructive to compare the predictions made with the actual numbers (or to provide some other form of model assessment).

14) Values for the serial interval were retrieved from early outbreak data in Wuhan. There are more recent estimations of the serial intervals now. What impact could this have on the results?

15) It is important to account for different infectivities of imported cases through sensitivity analyses. However justifications for the different percentages for the contribution to the transmission (Figure 2—figure supplements 1, 2, 3) is lacking. Are these arbitrary? It would be good to have an explanation.

16) It is not clear on which data or assumptions the parameters for the length-of-stay distribution in a ward or ICU bed are based on since no references are given.

17) It is surprising that there wasn't a change in time from onset to report during the outbreak. Could the authors clarify?

18) Could there be more detail on where the local transmissions occurred? Or is this reported elsewhere?

19) Could there be more clarity about the uncertainty presented in the R estimation figures legends? There seems to be a lot of confusion on Twitter etc in interpreting these graphs in terms of variance around the mean/median or variance in the R (some people transmitting more than others), therefore this is an opportunity to state very clearly what the uncertainty represents.
