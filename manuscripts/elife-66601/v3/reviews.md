# Peer review - Round 1

Editors:
- Joshua T Schiffer, Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66601.sa1](https://doi.org/10.7554/eLife.66601.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Thank you for submitting and revising this paper which makes the important point that the herd immunity threshold, as well as the pattern of incidence over time, is likely to be dictated by the degree of assortative mixing between racial and ethnic groups during the SARS-CoV-2 pandemic. The paper's observations can hopefully be used to optimize non-pharmaceutical interventions and vaccine implementation in high-risk ethnic and racial groups.

Decision letter after peer review:

Thank you for submitting your article "Modeling the impact of racial and ethnic disparities on COVID-19 epidemic dynamics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Joshua T Schiffer as the Reviewing Editor and Reviewer #1, by Miles Davenport as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jon Zelner (Reviewer #2); Mia Moore (Reviewer #3).

The reviewers have discussed their reviews with one another in detail, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please consider broadening the range of R0 considered in the analysis, with inclusion of values closer to one. It would also be useful to allow R0 (or rather R_effective) to take on varying levels over time to reflect observed shifts in physical distancing and NPIs during the pandemic. All 3 reviewers agreed that it would be interesting to see whether these changes, which would more closely approximate reality, would alter the paper's conclusions in anyway.

We do not feel that it is required to precisely recapitulate the dynamics of the NYC and/or Long Island epidemics, but rather to attempt scenarios other than the unmitigated simulated epidemic in the original version.

2) Similarly, another way to strengthen the paper would be to show what happens when "herd immunity" is achieved via vaccination rather than infection. The interaction with the mixing models would be a fascinating and useful contribution.

Reviewer #1 (Recommendations for the authors):

Strengths:

1) The model structure is appropriate for the scientific question.

2) The paper addresses a critical feature of SARS-CoV-2 epidemiology which is its much higher prevalence in Hispanic or Latino and Black populations. In this sense, the paper has the potential to serve as a tool to enhance social justice.

3) Generally speaking, the analysis supports the conclusions.

Other considerations:

1) The clean distinction between susceptibility and exposure models described in the paper is conceptually useful but is unlikely to capture reality. Rather, susceptibility to infection is likely to vary more by age whereas exposure is more likely to vary by ethnic group / race. While age cohort are not explicitly distinguished in the model, the authors would do well to at least vary susceptibility across ethnic groups according to different age cohort structure within these groups. This would allow a more precise estimate of the true effect of variability in exposures. Alternatively, this could be mentioned as a limitation of the current model.

2) I appreciated that the authors maintained an agnostic stance on the actual value of HIT (across the population and within ethnic groups) based on the results of their model. If there was available data, then it might be possible to arrive at a slightly more precise estimate by fitting the model to serial incidence data (particularly sorted by ethnic group) over time in NYC and Long Island. First, this would give some sense of R_effective. Second, if successive waves were modeled, then the shift in relative incidence and CI among these groups that is predicted in Figure 3 and Sup Figure 8 may be observed in the actual data (this fits anecdotally with what I have seen in several states). Third, it may (or may not) be possible to estimate values of critical model parameters such as epsilon. It would be helpful to mention this as possible future work with the model.

Caveats about the impossibility of truly measuring HIT would still apply (due to new variants, shifting use and effective of NPIs, etc….). However, as is, the estimates of possible values for HIT are so wide as to make the underlying data used to train the model almost irrelevant. This makes the potential to leverage the model for policy decisions more limited.

3) I think the range of R0 in the figures should be extended to go as low as 1. Much of the pandemic in the US has been defined by local Re that varies between 0.8 and 1.2 (likely based on shifts in the degree of social distancing). I therefore think lower HIT thresholds should be considered and it would be nice to know how the extent of assortative mixing effects estimates at these lower R_e values.

4) line 274: I feel like this point needs to be considered in much more detail, either with a thoughtful discussion or with even with some simple additions to the model. How should these results make policy makers consider race and ethnicity when thinking about the key issues in the field right now such as vaccine allocation, masking, and new variants. I think to achieve the maximal impact, the authors should be very specific about how model results could impact policy making, and how we might lower the tragic discrepancies associated with COVID. If the model / data is insufficient for this purpose at this stage, then what type of data could be gathered that would allow more precise and targeted policy interventions?

Reviewer #2 (Recommendations for the authors):

Overall I think this is a solid and interesting piece that is an important contribution to the literature on COVID-19 disparities, even if it does have some limitations. To this point, most models of SARS-CoV-2 have not included the impact of residential and occupational segregation on differential group-specific covid outcomes. So, the authors are to commended on their rigorous and useful contribution on this valuable topic. I have a few specific questions and concerns, outlined below:

1. Does the reliance on serosurvey data collected in public places imply a potential issue with left-censoring, i.e. by not capturing individuals who had died? Can the authors address how survival bias might impact their results? I imagine this could bring the seroprevalence among older people down in a way that could bias their transmission rate estimates.

2. It might be helpful to think in terms of disparities in HITs as well as disparities in contact rates, since the HIT of whites is necessarily dependent on that of Blacks. I'm not really disagreeing with the thrust of what their analysis suggests or even the factual interpretation of it. But I do think it is important to phrase some of the conclusions of the model in ways that are more directly relevant to health equity, i.e. how much infection/vaccination coverage does each group need for members of that group to benefit from indirect protection?

3. The authors rely on a modified interaction index parameterized directly from their data. It would be helpful if they could explain why they did not rely on any sources of mobility data. Are these just not broken down along the type of race/ethnicity categories that would be necessary to complete this analysis? Integrating some sort of external information on mobility would definitely strengthen the analysis.

Reviewer #3 (Recommendations for the authors):

The authors show that in an uncontrolled epidemic the herd-immunity threshold may differ dramatically between racial groups. Although this question is undeniably important and the authors have shown that their results are robust to differing assumptions about population mixing, it seems to me that the situation considered is not completely relevant to current state of the covid epidemic. The herd-immunity threshold is assumed to be reached via a single, unmitigated wave within a few months. Unfortunately, the details of how this threshold is calculated are missing from the manuscript, but I can't help but imagine that it would be quite different if it was assumed to be possible to reach herd-immunity via vaccination. I think the authors need to address this.

Figure 2 could potentially include the cumulative incidence associated with R0=3 in a homogeneous model.

Multi-panel figures are unlabeled and split over more than one page, separated from their captions.

Issue with assortative mixing assumption: When you assume a = 1, you assume that everyone makes the same number of contacts. How, then, is one group defined to be at higher risk than another. Is a really 1 in this case?

Issue with assortative mixing derivation: I have a minor concern about the derivation, specifically how the contact matrix is fit. When I try to follow your steps and fill-in the gaps I get a slightly different result. So please either clarify your reasoning or fix the result.

Total i seen by a single j in one day = c_ij*Ni

Total i seen by all j in one day = c_ij*Ni*Nj=total j seen by all i in one day

Using the P_ij formulation (and please drop the P_ab notation, it is not consistently used and P_ij makes it easier to follow)

Total j seen by a single i in one day = P_ij % of people seen by group i = P_ij*ai=P_ij (as a=1)

Total j seen by all i in one day = P_ij*Ni

Therefore you want to minimize |c_ij*Ni*Nj-P_ij*Ni|=|(1-e)N_j*Ni/sum(N_k)+e*Ni*d_ij – Ni*Pij|

= |Ni((1-e)Nj/sum(N_k) + e*d_ij – P_ij)|

Which is only different from what you have in that Ni and Nj are switched in one term.

With a not equal to 1 (which you appear to use?) should be something like:

= |Ni((1-e)a_i a_j Nj/sum(N_k) + e*d_ij – a_i a_j sum_k(N_ik N_jk/sum(a_i N_lk)))|

Where the P_ij term is now weighted by a.

Calculation of HIT not described: I also feel like I'm missing something about how HIT is derived from the simulations. It sounds as though you used a computation rather than analytic approach, but I cannot find where it is spelled out. That seems important.

Fit to sero-prevalence data not shown or described: You initially list fitted activity levels, can you provide error bounds for these values? What is the nature of the data that is being fit? Is it only a single proportion collected at a single time? Can you show model fits? Unclear what was done here?

You also say "differences in exposure…are in line with theoretical derivations". I assume that what you meant is that differences in herd immunity levels and final epidemic sizes are in line with theoretical derivations, but the sentence doesn't read that way.

Please put activity levels in a table: These values (and uncertainty ranges) should be in a table where it is easy to compare between the models.

Fit of assortative mixing model not shown or described: In the results you say you first choose epsilon, then you fit a afterwards. However the epsilon fit is performed assuming that a is zero. Can you explain the reasoning here? I'm concerned that this methodology underestimates mixing (because if contact is heterogeneous by group, then you are more likely to contact individuals from the higher risk group than is strictly predicted by geographic distribution).

Incidence rate ratio plot is misleading: The incidence does not follow this pattern in proportionate mixing, and incidence is dropping in all groups. Furthermore this plot shows a time series which is completely unrealistic and wildly different from data. Most importantly, it seems to be wholly irrelevant to the main point of the paper.
