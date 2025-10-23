# Peer review - Round 1

Editors:
- Deborah Cromer, University of New South Wales Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63704.sa1](https://doi.org/10.7554/eLife.63704.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work provides a detailed look into the potential benefits of a test and release quarantine strategy. By using quantitative models of the timing of quarantine, testing, release and transmission, the authors are able to show that testing people during quarantine, and releasing them after a negative test, could provide similar efficacy in terms of reducing transmission, while shortening the burden on quarantines individuals. This is relevant to policy decisions as balances are sought between efficacy and societal cost of quarantine.

Decision letter after peer review:

Thank you for submitting your article "Quantifying the impact of quarantine duration on COVID-19 transmission" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a guest Reviewing Editor and the evaluation has been overseen by Miles Davenport as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mirjam Kretzschmar (Reviewer #2).

The Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this paper the authors compare a standard quarantine scenario with a test and release quarantine scenario, and look at the efficacy and utility of each. This is a timely and important analysis, however as it is presented it is very technical, and not well explained for a general audience. It should therefore be revised, and technical details placed in an appendix.

The authors have successfully summarised both the advantages and disadvantages of a test and release quarantine strategy, as well as quarantine for different durations, and have shown that in some circumstances this may be preferable to a standard strategy.

At the moment, the paper does not clearly explain some of the more technical aspects, despite having many equations. It would be better served by explaining well, in plain language the approaches taken, and leaving the mathematics for a technical appendix.

Essential Revisions:

1) Equations must be tidied and there must be a consistency of notation. Many of them should be removed to a technical appendix, and explained in a more intuitive way in the text so the manuscript can be read by a more general audience.

2) Figures should be combined and edited to make paper accessible to a more general audience.

3) Assumptions made must be contextualised and explained. Specifically (but not exclusively):

a) Why do the authors repeatedly state that someone with a positive test is released on day tR+ when in actual fact they would be in isolation – please amend text and clarify.

b) Discuss how the local community transmission level impacts on the conclusions that can be drawn about returned travellers.

c) Consider how the likelihood that symptomatic individuals (not in already in quarantine) will isolate impacts the conclusions.

Reviewer #1:

This paper is well thought through and presents a very nice analysis of the benefits (and disadvantages) of a test and release quarantine strategy, as well as considering different durations of quarantine. I have some concerns however, with the presentation and the assumptions made, as well as the context in which these strategies are undertaken.

In regards to presentation, there are many mathematical equations presented throughout the manuscript, however in many cases these are confusing. As an example, Equations 2, 3 and 4 have no parameters for the function F, and do not contain an n in them, but F is repeatedly used with the parameter n. The relationship between n, tR, tQ, tE etc should be explained and the functions parameterised more clearly.

Additionally, there are 5 result figures presented, which are difficult to interpret. The authors should consider alternative ways of representing their results to make them easier to understand for a non-technical reader.

Regarding assumptions made, the comments in section “Persistently asymptomatic infections” that state that symptomatic individuals would be removed from the population (N.B. this should read infectious pool rather than population) regardless of their quarantine status are only true if ALL people self-isolate on the day of symptom onset. Since this is unlikely to be the case, there will only be a probability of isolation occurring x days after symptom onset, p(x). Presumably p(x) will increase after (a) testing and (b) a positive result, but we cannot assume it will be 1 on the day of symptom onset. This needs to be addressed.

In section “Adherence to quarantine” a function α(n) is introduced, but α(n) is not shown in the paper, and it is not clear whether subsequent calculations include this α(n) or not. This must be clarified. Also, the authors do not consider the possibility that α may wane over time (i.e. for a fixed duration of quarantine, people may quarantine effectively for the first half and but less effectively for the second half). This should be either commented on, or addressed.

It is not clear from the text what is meant by "the test-and-release strategy always performs better than not testing if the release time is the same as the quarantine duration". This must be clarified, and can be done by stating "It will always be better to test a person prior to release from quarantine, as that way asymptomatic and pre-symptomatic infections are more likely to be detected and prevented from being released".

Finally, the context of this manuscript is not made clear. Early on, the authors state that quarantine of returning travellers occurs when "they have returned from recent travel to a high-risk area with levels of community transmission that are higher than in the home country" however in many countries that is not the strategy that is being implemented. Many countries are requiring quarantine after travel to countries with similar or slightly less community transmission. Therefore, the assumption that returning travellers must have contracted their infection overseas is incorrect. This only works in regions where there is little community transmission in the home country. Therefore, if this is to be presented as an argument, these results need to be stratified by cases where the visited country has either much more, similar or much less community transmission than the home country.

Reviewer #2:

In this manuscript the authors develop a computational approach to determine the impact of test sensitivity and duration of quarantine on onward transmission of COVID-19. Based on the generation time distribution, the authors estimate what part of onward transmission can be prevented, given test sensitivity per day since exposure, and delays in testing. They also introduce a utility measure for quarantine, that takes into account the average time spent in quarantine. Overall this is a well written paper with a clear approach and useful results on various quarantining strategies.

There are a few ways in which this paper could be made more accessible for the reader. The notation is mathematical, and notation of variables not always very intuitive. As many quantities have similar names, it would help the reader to have a table with explanation of the variable names, so that one can look back quickly while reading to check how a variable was defined. Alternatively (of in addition), the graphs in Figure 1 could be extended to include more variables, for example a similar graph could be made for the traced contacts, and for returning travellers.

Reviewer #3:

Quantifying the impact of quarantine is an important topic, where the literature is currently lacking. This piece is very timely and tackles some very important questions in the space. At the moment, I feel this paper is somewhat lacking and requires some revision. I think the biggest issue is that it seems to be tailored for the situation in Switzerland. In itself, that's fine, but if the paper stays that way, the title should be altered to specify "in Switzerland", and the Introduction should give some more detail about the local situation. If the authors made that change, I have only a few technical queries that need to be addressed. I will also give some comments and suggestions about the differences between quarantine for close contacts compared to returned travellers, and what should be done to make the analysis more useful globally.

1) I'm concerned that the calculations in this paper are incorrect. Specifically, I'm looking the second paragraph in subsection “Quantifying the benefit of quarantine” and Equation 1. If q(t) is the probability density of the generation time (and generation time is the time from exposure until the person becomes infectious), then the integral in Equation 1 is the probability that the person becomes infectious while in quarantine. I don't see how this is equal to the fraction of transmission prevented. I thought you would need the function to be the probability that someone is infectious at time t? Which I think is the convolution of Figure 2A and 2B. I am not too concerned about this, as if it is an error it shouldn't be hard to fix.

2) The other technical issue is about returned travellers, and how the trip duration affects the transmission reduction through quarantine. I'm not convinced by the argument that short trips need longer quarantine. I think the calculations are ok, and the result comes from the assumptions themselves. The authors are assuming that a traveller contracts covid while away, so on a 1 day trip, they must have caught it recently, and therefore need more time for symptoms to develop and to test positive. However, I don't think the authors should rule out a traveller catching covid before leaving, and becoming infectious after returning. I understand that the authors want to split the paper up into locally acquired cases, and international, but I don't think it works. If the situation was one where the country had no covid, then this claim about short trips needing longer quarantine makes sense. But in general it's a more nuanced question and certainly doesn't seem to fit Switzerland. I guess it could also work if you assume all local transmissions can be contact-traced, but I don't think the authors claimed this either.

3) On to the more general point about applicability globally, which is specific to returning travellers (apart from the notes above, I think the close contact part of this work look good). I think the authors have missed explaining the decision context clearly (where the decision is about length of quarantine), and how differing values, objectives and system states affect things (see Baker et al., 2020 for a general discussion on decision making). The point I want to get to is, what is the objective of quarantine for returned travellers? The paper focusses on reduction of spread, which seems reasonable for countries with ongoing community transmission. However, it would be important to be clear about how much transmission in the country is coming through airports, relative to the community spread.

There are many countries and jurisdictions that have either no ongoing transmission, or very well contained clusters. Quarantine in these areas is completely different, as the aim isn't about getting some percentage reduction is transmission. Instead, the aim is to have 100% reduction, and the metric of interest is the probability that an infection escapes quarantine and seeds a cluster of cases in the community. I think many people would be very interested in an analysis that looked at quarantine length and testing strategy in this context, to get towards a trade-off between length of stay, costs and importation risk.

Overall, I think this paper has made some good steps. However, the message needs to be refined, and the context of the paper needs to be clarified. I think quarantine is a very important topic, and in its current state, the manuscript is only applicable to regions with active transmission. I think the current scope is acceptable at this journal, but it needs to be clear that it is aiming for that. Even without analysis suited to low/no prevalence scenarios, at a minimum there should be some discussion about how the local epidemiological situation is driving the results and the analysis, and how quarantine may need to be approached differently elsewhere.

I wish the authors all the best in their revisions. As I said, it's an important topic and there needs to be more literature about it. I would happily review this paper again. I also commend the authors for making everything available on Github. This was useful during my review.

References:

Baker, C.M., Campbell, P.T., Chades, I., Dean, A.J., Hester, S.M., Holden, M.H., McCaw, J.M., McVernon, J., Moss, R., Shearer, F.M. & Possingham, H.P. (2020). From climate change to pandemics: decision science can help scientists have impact. ArXiv200713261 Phys.

Reviewer #4:

Ashcroft et al. discussed the appropriate duration of quarantine for travellers and close-contacts by estimating the fraction of transmission that can be avoided under a range of scenario and their relative utility. The study also explored the impact of testing, reinforced hygiene, adherence, and symptom presentation on transmission. This is an important and policy relevant topic. The article is nicely written, and I only have a few comments.

Cases included in Kucirka et al. are all symptomatic, and they back calculated time from exposure assuming incubation period of 5 days. The authors here seem to assume that the sensitivity of the RT-PCR test found in symptomatic individuals can be applied to asymptomatic individuals. Please state this assumption (if that's correct) and discuss how this assumption impacts the outcome.

Figure 4 and other figures, can the authors state how the upper and lower bounds are estimated?
