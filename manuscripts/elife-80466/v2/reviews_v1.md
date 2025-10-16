# Peer review - Round 1

Editors:
- Niel Hens, https://ror.org/04nbhqj75 Hasselt University Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80466.sa0](https://doi.org/10.7554/eLife.80466.sa0)

This is a valuable study characterizing seasonal deviations in indoor activity at the county level in the United States with relevance to respiratory disease transmission. The strength of evidence is solid. This study and its results are of potential interest to those people constructing more evidence-based infectious disease transmission models.


---

# Peer review - Round 1

Editors:
- Niel Hens, https://ror.org/04nbhqj75 Hasselt University Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80466.sa1](https://doi.org/10.7554/eLife.80466.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Disentangling the rhythms of human activity in the built environment for airborne transmission risk: a large-scale analysis of mobility data" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Diane Harper as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Guillaume Béraud (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) One of the major issues is related to the definition of "indoor". It should be stated from the beginning what "indoor" locations are about, in particular, that home is not part of it, which is an important point to understand the results (and the discussion). Did the authors conduct any sensitivity analysis related to these choices?

2) Compare trends with other proxies for seasonality.

3) Provide a better justification of the clustering approach used (choice of methodology) and conduct the necessary sensitivity analyses (including choice of threshold).

4) Compare model fits to real COVID-19 data and/or ILI (because of the difficulty in dealing with NPIs for COVID-19), or step back from the claims that the 'σ' metric generates better model fits given that you've shown that it yields different model fits, but not necessarily better ones.

5) Provide formal justifications for several claims throughout the Results section (e.g. a measurement of geographic heterogeneity in trends, and differences in pre-pandemic vs. peri-pandemic patterns).

In summary, this work has potential but requires essential revisions, particularly by clarifying some of the language used and by including more detailed and quantitative analyses.

Reviewer #1 (Recommendations for the authors):

Overall, I found this study to be well-conducted and impactful. There are a number of areas where it could be improved, particularly by clarifying some of the language and by including more detailed and quantitative analyses. In the following comments, I'll try to provide specific suggestions for where the authors might focus their efforts.

Specific comments:

10: Perhaps "impacting" rather than "suppressing"? The rest of the manuscript makes clear that the authors interpret seasonality as a force that can both enhance and suppress transmission, so it would be worth using consistent language here.

54-56 ("While more is known about… rates of indoor activity.") I had trouble parsing this sentence. What do you mean by spatio-temporal variation in the indoor environment? At what scale? Are you talking about the environment itself, or the variation in people's experience of it? What kinds of rates of indoor activity are unknown, and why does this matter? It seems to me that this sentence is identifying the key gap that this study aims to fill, so it would be worth making this more precise.

90: What sort of global change do you mean? As it stands, the term is too vague to be meaningful here.

Figure 1: The authors could consider grouping Figure 1B by latitude rather than alphabetically; this might reveal some interesting patterns that more clearly support their findings of different seasonal patterns in the north vs. the south.

109: systematic how? This paragraph and Figure 1A seem to discuss just two counties, but a "systematic" difference suggests to me that there's some kind of variation that's observed repeatedly across instances (counties). It would be good to discuss here what exactly is systematic about this variation.

Figure 2: Did the data include Alaska and Hawaii and/or the territories? I would imagine these states might also have substantially different seasonal trends relative to the lower 48 and might give some indication of what sorts of seasonal trends we might expect outside the US.

140: Heterogeneous how? Can you provide some measurement of the degree of heterogeneity?

142: ("in most locations indoor activity deviated from pre-pandemic trends") – again, as measured how? In what fraction of locations? To what degree did the trends deviate?

146: ("activity was more likely to be outdoor than in prior years") – how much more likely? How widespread was this change?

158-159: It would be worth reporting the changes in amplitude and phase here, with appropriate units.

161: A poorer fit as measured how?

170: "accuracy of disease models" – I appreciate that the authors have shown that using different seasonal forcing terms as inputs can yield different epidemic curves, but I don't think they've made a formal assessment of accuracy here, which would require comparing model fits to disease transmission data. The evidence presented so far does not make clear to me the degree of detail needed in the seasonal forcing term to accurately characterize disease transmission trends, as this will depend on the disease dynamics themselves and the temporal and geographic scale of the model.

234: Perhaps "southern latitudes should be targeted for such interventions in summer months as well"? It seems that southern latitudes still have a substantial winter peak, it's just that they also have a summer peak.

278: Again, it would be worth specifying what global change events the authors have in mind here.

Another general point for the Discussion: how should we interpret differences in amplitude across locations? Since σ is a measurement of the percent change in baseline activity, the indoor activity in a location with a high baseline but low σ might still be higher than the indoor activity in a location with a low baseline but a large σ. To what extent can we use σ to compare indoor activity across locations in the US? Or can we only use it to compare variations in indoor activity within counties? Would it be worth including some analysis of the baseline indoor activity across the US, since σ is really operating on this baseline?

288: Make explicit that you'll be referring to this as a POI.

294: What kind of spatial imputation did you do? Why?

Figures S7: It feels odd to me to have amplitude, frequency, and phase all plotted on the same vertical axis despite them all having different units. Perhaps a table would be better?

Reviewer #2 (Recommendations for the authors):

I am confident that a revision of the issues in the public review would improve the quality of the paper and allow it to exploit the full potential of this work.

I believe that it is crucial to repeat the analysis taking into account the nature of the correlation matrix, so either adjusting the null hypothesis on modularity optimization or by using a different community detection algorithm.

Reviewer #3 (Recommendations for the authors):

Overall, it is an excellent paper and very well written. However, there are some issues I'd like to be considered:

The major issue is related to the definition of "indoor". It should be stated from the beginning what is "indoor" locations, in particular, that home is not part of it, which is an important point to understand the results (and the discussion). At the moment, it is only defined within the methods (Line 300), at the end of the article.

Line 43-41: Maybe authors could extend a few references on seasonality causes. But it is not mandatory.

Figure 1B: Why counties are ordered in alphabetical order? Which does not bring a lot of information, while it could be ordered by latitude, as an example, which could reveal some patterns.

Lines 103-106: authors should define more precisely what is the average (county-level? season? …).

Cluster: Maybe the clustering methods could be explained more extensively in the appendix.

Figure 3: I found it difficult to observe a shift in indoor activities, according to season.

Line 232-233: Isn't it the contrary? Increase of indoor activities in winter for northern regions?

Finally, a discussion on the difference between relationship and causality could be useful to distinguish human behavior seasonality and infectious diseases seasonality.
