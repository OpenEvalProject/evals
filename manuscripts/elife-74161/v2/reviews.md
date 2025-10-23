# Peer review - Round 1

Editors:
- Bernhard Schmid, https://ror.org/02crff812 University of Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74161.sa0](https://doi.org/10.7554/eLife.74161.sa0)

Using 486 long-term population records of 157 mammal species, the authors show that species with a short life span and large litters are more affected, either positively or negatively, by extreme weather events than are species with a long life span and few offspring. This suggests that these "fast" species may require particular conservation attention, to avoid extinction due to the increased frequency and magnitude of extreme events.


---

# Peer review - Round 1

Editors:
- Bernhard Schmid, https://ror.org/02crff812 University of Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74161.sa1](https://doi.org/10.7554/eLife.74161.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Life-history predicts global population responses to the weather in the terrestrial mammals" for consideration by eLife.

Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Bernhard Schmid as the Reviewing Editor and Christian Rutz as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Nigel Yoccoz (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this decision letter to help you prepare a revised submission.

Essential revisions:

1) Please try to improve the narrative by making it less exploratory (Reviewer #4). Clearly state your a priori hypotheses or at least explain why you expected the chosen life-history traits and environmental variables to be the most relevant and how they may interact and influence population dynamics. It may also be useful to explain why you expected robust prediction of absolute changes, but not for the direction of changes, and why this can still be useful for conservation biologists (Reviewer #4).

2) Please explain to which extent the greater absolute response of species to weather anomalies scales to a potentially larger absolute variation in population size of those species (Reviewer #2).

3) Please justify the selection of explanatory weather variables (Reviewers #3 and #4), e.g., by mentioning that fits with alternative variables were worse.

4) Perhaps try to analyze some subsets of the data to verify the robustness of the overall analysis (Reviewer #2).

5) Please discuss the limitations highlighted below by Reviewers #2-4, as well as the following points: traits were assumed constant between populations within species as were other characteristics of populations within species (e.g., marginality with regard to distribution range and thus "weather niche" (Reviewer #2), other traits (Reviewer #3) such as size at birth, sociality). Please provide a reason for why (or add corresponding analyses) biome (Reviewers #2 and #3) or site characteristics were not considered as explanatory variables (but rather subsumed in multilevel factors).

6) Please amend the title to read "Life-history predicts global population responses to weather in terrestrial mammals".

Reviewer #1 (Recommendations for the authors):

I must admit being a bit skeptical when it comes to large comparative analyses, as databases such as the Living Planet includes data of variable quality, and maximum longevity is, as you acknowledge, a far from ideal index for adult survival rate. Moreover, as you rightly point out, the available data are heavily biased towards some groups and biomes. Many analyses have been published using similar databases (e.g., Ono et al., 2019), so clearly some see value in such analyses. My concern is that because one has to "sell" the paper one avoids pointing out the limitations -- but alas this is not specific to your study.

One concern I have is how such analyses can be informed by the more detailed and accurate studies based on long-term monitoring of single populations (e.g., Gaillard et al., 2013). One knows that weather effects will vary among populations -- e.g., depending on where the population is in the climatic niche (see above) -- and such variation is crucial in predicting effects of weather and climate change. Large "meta-regressions" such as yours might be useful in summarizing the data available in one database, and you have done an excellent job analyzing these data, but given the far from random sample you have available, it is hard to assess how to make sense of the patterns observed. Perhaps using subsamples of high quality studies in different groups and biomes (if that is at all possible) to assess the predictive performance of your models may help.

You rightly discuss the limits of using maximum longevity as an index of a better measure such as adult survival rate. Would it be possible for the sample of species you have to at least assess the relationship between maximum longevity and adult survival rate? And for those species to repeat the analyses? The precision would be much lower as the sample size is likely to be small but you can at least assess the consistency of the relationships.

Regarding the effects of biomes, I did not understand how it was parameterized (e.g., l 465). It was included as a categorical predictor, right (figure S16 seems to indicate that)? So you have β_Biome[j] for j=1:number of biomes?

Adler, P. B., et al., 2011. Productivity Is a Poor Predictor of Plant Species Richness. Science 333:1750-1753.

Angert, A. L. 2009. The niche, limits to species' distributions, and spatiotemporal variation in demography across the elevation ranges of two monkeyflowers. Proceedings of the National Academy of Sciences of the United States of America 106 Suppl 2:19693-19698.

Gaillard, J. M., A. J. M. Hewison, F. Klein, F. Plard, M. Douhard, R. Davison, and C. Bonenfant. 2013. How does climate change influence demographic processes of widespread species? Lessons from the comparative analysis of contrasted populations of roe deer. Ecology Letters 16:48-57.

Ono, K., O. Langangen, and N. C. Stenseth. 2019. Improving risk assessments in conservation ecology. Nature Communications 10:7.

Reviewer #2 (Recommendations for the authors):

Jackson et al., present a global analysis of the effects of life history on the response of terrestrial mammal populations to weather, showing that litter size and longevity significantly alter how population's respond to anomalies in temperature and rainfall. The topic is highly interesting, and generally the manuscript is written in clear and concise way with some exceptions (see comments below). My main concern is about the timescales over which the weather events are calculated. As I understand it, these are anomalies away from the yearly expected value. This approach was of course used because the LPD data is recorded on an annual basis. However, there is a huge difference in the effect of slightly elevated temperatures across a whole year vs. one month with very high temperatures. The authors appear to have addressed this by looking at the yearly anomaly and the variance in the weather (annual weather variance) calculated across each year; however they are currently lacking some detail on exactly what this entailed (it is currently only mentioned in passing).

The authors have done a good job pulling all these analyses together into an accessible piece, and have provided all of the code to repeat these analyses.

Reviewer #3 (Recommendations for the authors):

1/ Overall framing and questions/hypotheses:

– Please justify more clearly, somewhere in the introduction, why looking at the weather is interesting for understanding future effects of climate change (see lines 87/88 and 111/112).

– In the introduction, the evidence from past work could be summarised more efficiently and concisely around key points (e.g., see lines 74-82, lines 96-104); thus the overall narrative/structure of the introduction can be improved.

– Beyond the three questions you ask, please explain what the underlying hypotheses are (e.g., for each question, adding a few words to explain what you expect: what are the spatial patterns you predict, what do you hypothesize would be the effect of life history, etc.)? In addition, the phrasing of the first question is a bit ambiguous with the term "consistent" (in my understanding, here you ask, across species and populations, whether the weather effects are significant, as in whether they differ from zero). Adding a specific hypothesis would also help to make this question clearer.

– Finally, please justify more why you look at the magnitude (absolute values) of the weather effects when investigating the influence of life-history on the responses, and why you don't investigate the directionality of the effects.

2/ Results

The results could be presented more efficiently and clearly overall. I would suggest including a few higher-level summaries throughout the manuscript to conclude on specific points.

3/ Discussion:

– Some of the limitations of the study should be developed in the discussion, in particular:

– The potential biases of the study (e.g., length of the time series): you mention that record length was significantly associated with temperature and precipitation effects. I would be good to mention whether your results are likely robust to these biases or otherwise what the expected effects on the results would be.

– The fact that you use absolute values (magnitude of the weather effects) for the life-history models, so that you can't conclude about the directionality of the effects. I suggest highlighting how your work helps predict future responses and inform conservation despite the fact that you didn't investigate the directionality of the effects (see lines 239/240; 243/244) (e.g., do your results imply that populations of species with fast life history should be more closely monitored irrespectively of whether they grow or decline?).

– It would be good for the discussion to make the key points stand out more.

4/ Methods

Life-history traits: It is important to include a statement about the degree of multicollinearity among the traits.
