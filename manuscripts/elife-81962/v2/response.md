# Author response - Round 1

Authors:
- Madeleine Seale
- Oleksandr Zhdanov ([ORCID: 0000-0002-1742-9765](https://orcid.org/0000-0002-1742-9765))
- Merel B Soons
- Cathal Cummins
- Erika Kroll ([ORCID: 0000-0001-8832-7208](https://orcid.org/0000-0001-8832-7208))
- Michael R Blatt
- Hossein Zare-Behtash
- Angela Busse
- Enrico Mastropaolo
- James M Bullock
- Ignazio M Viola ([ORCID: 0000-0002-3831-8423](https://orcid.org/0000-0002-3831-8423))
- Naomi Nakayama ([ORCID: 0000-0002-9390-3545](https://orcid.org/0000-0002-9390-3545))

## Response text

DOI: [10.7554/eLife.81962.sa2](https://doi.org/10.7554/eLife.81962.sa2)

Reviewer #1 (Recommendations for the authors):

Figure S5 of the modelled kernel of density of the predicted flight distance seems underwhelming. The two curves are highly similar and it's difficult to assess if the difference is significant on the logarithmic scale. Could a statistical test be performed to provide a quantification of how different they are? Similarly, since weather statistics is playing a dominant role, could the influence of pappus morphing be assessed with a principal component analysis or some other tool? Basically, how impactful is the dry/windy probability versus morphing/non-morphing effect in the final kernel?

Thank you for your comments. As the kernels in Figure S5 (now labelled Figure 4—figure supplement 2) arise from our modelling rather than empirical data, we could not meaningfully carry out inferential statistical tests. Instead, to address this issue, we have computed the Jensen-Shannon divergence metric (0.034), which gives a quantitative indication of the difference between the models. The result indicated that the two models have similar shapes but that there are some quantitative differences between them. We have highlighted this in lines 345-349.

In terms of breaking down the model into its component parts, we have partially done this in Figure 4 with the different models (varying weather, pappus flight, pappus detachment) indicating the effects of each of these elements. Three of these models (1-3) were directly used to construct Figure 4—figure supplement 2 with different weightings according to the frequency of weather types and dispersal probability. The frequency of detachment beyond the threshold for wet conditions was very low; therefore, one of them (1) dominantly affected the graphs shown in Figure 4—figure supplement 2. To make it clearer what the contributions of each of these component models was, we have added quantitative values in the text (lines 334-339) indicating the probabilities of the weather and detachment to explain how the final distribution was reached. We have also added in some additional panels to Figure 4—figure supplement 2 to visually show the numbers more clearly. We hope that this will aid understanding of this part of the work.

Reviewer #2 (Recommendations for the authors):

The paragraph that starts on line 315 is really key to the ecological understanding of the work, yet is a bit confusing for me. For example, the authors say "When pappi were closed and weather was wet (Model 5)" that this increases dispersal ability. However, model 5 from the figure indicates that the weather is dry.

Thank you for spotting this. This was, in fact, an error made when the manuscript was being edited. We meant to refer to Model 3 here, not Model 5 and this is now corrected.

I think this paragraph could be reworked to be more clear as to why the authors think that wet weather promotes longer dispersal, as from what I see, the models 2 and 3 appear to be the ones with wet weather, and also seem to have PDF's that don't indicate as far of travel (Figure 4b-f). The authors state that the increased wind is the cause, but I do not see the evidence for this in this paragraph or in Figure 4.

Yes, we agree that this could be made clearer. We have improved the wording to make it more specific what we are referring to and have added an additional figure 4g to show the wind speed during successful detachment. We hope this helps with understanding.

Another weakness to me, however an easy to fix weakness, is that in Figures 1g,h and 2c the red to blue gradient of points is unclear to me. I don't think it's necessary. I prefer to leave the points black, and keep the blue/red difference for the dry and wet seeds. In addition I'd encourage the authors to select two colors that are more visually different for those who are colorblind. Also, whatever colors the authors choose for dry/wet conditions, I'd keep those the same throughout the main figures, and the supplemental figures (the authors switch to yellow/blue in the supplement).

Thanks for pointing this out. We have modified the colours in the figures as suggested and stuck with the orange/blue scheme, which should be suitable for colourblind readers.

Something about the wording on lines 316-317 is confusing to me. It seems like it should read that humidity doesn't matter at all for dispersal. Anyway, if you could reword this sentence that would help!

We have modified this sentence to make it clearer.
