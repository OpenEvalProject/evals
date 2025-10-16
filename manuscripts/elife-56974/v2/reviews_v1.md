# Peer review - Round 1

Editors:
- Ben S Cooper, Mahidol University Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56974.sa1](https://doi.org/10.7554/eLife.56974.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Spatio-temporal associations between deforestation and malaria incidence in Lao PDR" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: James A Watson (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Please submit a revised version that addresses these concerns directly.

Summary:

Deforestation is widely thought to have played an important role in the declining incidence of malaria in the Greater Mekong Sub-region but detailed analyses have been lacking. In this paper the authors assemble a large dataset of geolocated malaria cases from Lao PDR together with forest cover data. Using a spatio-temporal modelling framework, they find no evidence of an association of deforestation within 1 or 10km of a village and malaria incidence. However, deforestation within 30km of a village was associated with malaria incidence, though with the direction of the association depended on the timescale considered. In the short term (1-2 years) deforestation was associated with increases in malaria incidence in the south, though no association was found in the north. In the long-term (3-5 years) deforestation was associated with a lower malaria incidence rate, with decreases of about 5% in both the south and the north.

Essential revisions:

1) All reviewers had concerns about variable selection and a number of suggestions were made, including regularisation, the need to adjust for climate anomalies and malaria control programme activities. The differences between the north and south were also highlighted and, following the consultation process, there was a consensus that lumping both parasites together and using one region did not seem appropriate. There were also questions about the choice of initial climate covariates. These issues need to be addressed either by conducting the analysis in a different way (we leave it to the authors to decide on the best way) or by convincing the reviewers that such changes are not needed. A better explanation and consideration of the climate covariates that were considered is also needed.

2) There needs to be a more thorough exploration of the effect of inclusion of malaria cases in the previous month. As reviewer 3 points out, it is surprising that the effect of malaria cases in the previous month is left as a sensitivity analysis as the autocorrelation effect should be important in a transmission system.

3) The concerns about the way forest data are used (as raised by reviewer 2) need to be addressed. The authors should justify how they have derived canopy cover from a dataset not designed to quantify annual forest canopy cover. This is quite a widely used dataset and the interpretation is unconventional. The authors could either re-analyse these data or provide further explanation of how they have modelled canopy cover levels.

4) The authors should include the nonlinear trend f(t) in the results as well as the overall temporal pattern in the regions' deforestation.

5) There needs to be greater clarity about what was done in the results – e.g. regarding the treatment seeking model and adjustment for confounders.

6) There is a need for clarification of differences in malaria regimes in north and south in the Introduction.

Reviewer #1:

This is a carefully written paper on the complex associations between deforestation and malaria incidence. For someone with no background in the relevant literature it provides an easy to read introduction to previous work and shows how these new results fit with previous reports. On the whole I enjoyed reading it. My main suggestions are cosmetic.

I feel that the authors have done themselves a disservice in the Results section when reporting the observed associations between deforestation and malaria incidence. When I first read it, I had the impression that no adjustment for confounders was made! This does not seem to be mentioned at all in the Results. But in fact the underlying model is quite complex (Figure 8) and the authors use elevation, precipitation and temperature as the possible confounders (if I understood correctly). I would suggest adding a few sentences in the Results to clarify this. Maybe the Discussion could have a sentence or two on any unmeasured/residual confounding? Another really important adjustment is done for treatment seeking behaviour. This is rarely done in similar stats analyses and the authors have put quite a lot of work put into constructing a sophisticated model of treatment seeking (Figure 7B is really informative! Relegating this figure to the supplementary materials is a shame.)

I don't think the Results section even mentions the treatment seeking model. It is an important output and when mentioned in the Results, it should be made clear that the treatment seeking model is built using a different dataset, so there is no doubling dipping when constructing the geospatial model.

I'm not very familiar with GAMs so feel free to ignore this comment: instead of doing forward/backward AIC-based variable selection, could you instead fit the full model with appropriate regularisation (ridge regression type but in a GAM framework)?

Final comment concerns P. vivax. It is to be expected that the short term associations are dampened as probably the majority of infections are relapses (as mentioned in the Discussion). So you could argue that seeing a dampened association provides some kind of reassurance that there isn't massive unmeasured confounding going on (I would worry if larger associations were seen for vivax). This argument doesn't really work for the long term associations though. Any reasons for why no long term associations are observed?

Reviewer #2:

This study addresses an important research gap in understanding the ecology of malaria within Lao PDR and assembles an impressive dataset of geolocated malaria cases. However, there are major limitations in this study which question the validity of results and the interpretation of data sources.

First, without adjusting for precipitation or temperature differences annually, it is impossible to interpret whether the time lags between deforestation and malaria incidence reflect ecological changes and forest loss or whether this is due to interannual variation in other environmental factors. This time period includes a major El Nino event with extensive forest fires reported across Southeast Asia, including in Lao PDR (e.g. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6520341/). Without adjusting for the climate anomalies during this time period, it is difficult to attribute changes in risk to deforestation. Additionally, this analysis would ideally include some estimates of malaria control program activities during these time periods and whether this also varied either temporally or spatially. The authors address bias in health system reporting but no other control activities.

Additionally, assuming that the authors are simply using the forest data obtained from Hansen et al., this is not analyzed in a method consistent with how it was produced. This dataset includes tree crown coverage for 2000 (as a percentage) and a forest loss layer which reflects the change in state of a pixel from forest (defined as 50% canopy cover) to non-forest (less than 50%). As the forest loss layer only reflects a change in state (this could be 100% canopy cover to 0% or 52% to 49%), this is can only be interpreted by classifying the initial forest layer using a 50% threshold and cannot be used to estimate canopy cover percentages. There is also a forest gain layer (reflecting the change of state from non-forest to forest) which is not discussed at all within this paper. Following discussions about the accuracy of these datasets, there have also been updates to this data and additional layers available on World Resources Institute which could significantly improve this classification. As well, as forest configuration and fragmentation has widely been associated with malaria incidence in forest settings, this work would be improved by including additional metrics reflecting patterns of deforestation rather than just total area within a circular buffer.

Reviewer #3:

This manuscript addresses an important question in the ecology of malaria, namely what is the impact of deforestation on malaria incidence. Although there have been multiple studies and reviews on the subject for other regions especially the Amazon, an overall picture remains elusive because of the complexity of an environmental impact that is non-stationary in time as proposed in the hypothesis of "frontier malaria". Statistical analyses most often lack the longitudinal data needed to disentangle effects of deforestation as a function of time, and to also consider the spatial scales at which such effects are manifested. The work of Castro and colleagues for the Amazon did consider the temporal axis and provided evidence for a transient increase followed by a decrease to low endemic malaria.

Here, the authors take advantage of a longitudinal and spatially-resolved malaria data set in Lao People's Democratic Republic, together with a forest data set from remote sensing, to investigate how deforestation influences malaria incidence by both P. falciparum and P. vivax at different spatial and temporal scales. They contrast results for two regions within Lao PDR, North and South, with distinct transmission regimes and populations. They provide evidence consistent with the "frontier malaria" hypothesis, albeit with shorter times for the turn-around, from an increasing to a decreasing trend, than reported for the Amazon. The positive and short-term positive effect on malaria incidence is stronger in the South than in the North, and for P. falciparum. These results are important in demonstrating the need to consider statistical analyses that carefully introduce time since deforestation, and in supporting a positive transient effect of deforestation on malaria that should inform both public health strategies and forest management.

I have some comments that should be addressed to make the analyses and their interpretation clearer:

1) The way climate covariates are incorporated may ultimately "work" to capture a complex set of effects in a statistical model, but it is not very convincing. In particular, model selection is conducted on the basis of non-specific cases and the South only. The South and North show very different transmission regimes not just because of different population sizes but because of different environments, especially altitude (and therefore temperatures). In the more endemic regime of the South, malaria cases are likely to reflect much less clear effects of climate covariates than in the low transmission, epidemic, North. In addition, aggregating cases for the different parasites is problematic as their transmission is affected by climate covariates in different ways, given the relapses of P. vivax which typically lead to a different seasonality and less sensitivity to climate drivers. P. falciparum shows a more epidemic behavior in the North as expected for higher altitudes/cooler temperatures. These differences make one wonder whether it is valid to conduct model selection first in terms of the South and for both parasites together, and then fix these variables in the rest of the analysis.

2) The choice of initial climate covariates is also somewhat confusing. Why use WorldClim at all? One can obtain the means, or totals, and the CVs, from the time series used for the monthly data. WordClim uses a particular window of time (decades) to obtain these "typical" variables. It is my understanding that this time period is earlier than that considered here. Why use altitude and temperature? Aren't these strongly correlated within a region? An alternative consideration is to separate interannual and seasonal effects, by considering monthly values (as done here) and also the mean temperatures (of that same data set) over a window of time that precedes the transmission season (for P. falciparum) and corresponds to the rainy season.

3) The effect of malaria cases in the previous month is left for the sensitivity analysis as one variation of the main results. This is surprising as this autocorrelation effect should be important in a transmission system. That is, it would be natural to start with that model and see what is the significance of that variable. Its inclusion seems to do more than just weaken slightly the results. The effect in the North for P. falciparum becomes non-significant and that in the South weakens considerably. I wonder what would have been the result of model selection to start with, if this variable had been included. (I understood that the "adjusted" model does not repeat model selection).

4) The distinction of the malaria regimes in the North and South should be described more clearly in the Introduction for a general reader not familiar with malaria dynamics. The North appears seasonal low transmission or epidemic (given the altitudes and the time series), and the South, seasonal endemic. The differences in transmission characteristics between parasites should also be included early in the text; relapses are mentioned late in the Discussion. These considerations are important to how one looks at the time series and results.

5) The nonlinear trend f(t) is mentioned in the model description but not in the results. I could not tell whether deforestation itself exhibits a trend and how consideration or not of f(t) influences the results. Including the resulting f(t) as well as the overall temporal pattern in the regions' deforestation would be informative.

6) Similarly, I would have liked to see in the supplement the main results underlying variable selection and model selection.
