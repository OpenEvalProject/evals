# Author response - Round 1

Authors:
- Emilia Johnson ([ORCID: 0000-0001-5460-1715](https://orcid.org/0000-0001-5460-1715))
- Reuben Sunil Kumar Sharma
- Pablo Ruiz Cuenca ([ORCID: 0000-0002-2180-9509](https://orcid.org/0000-0002-2180-9509))
- Isabel Byrne ([ORCID: 0000-0002-7800-3733](https://orcid.org/0000-0002-7800-3733))
- Milena Salgado-Lynn ([ORCID: 0000-0003-1769-6465](https://orcid.org/0000-0003-1769-6465))
- Zarith Suraya Shahar
- Lee Col Lin
- Norhadila Zulkifli
- Nor Dilaila Mohd Saidi
- Chris Drakeley ([ORCID: 0000-0003-4863-075X](https://orcid.org/0000-0003-4863-075X))
- Jason Matthiopoulos ([ORCID: 0000-0003-3639-8172](https://orcid.org/0000-0003-3639-8172))
- Luca Nelli ([ORCID: 0000-0001-6091-4072](https://orcid.org/0000-0001-6091-4072))
- Kimberly Fornace ([ORCID: 0000-0002-5484-241X](https://orcid.org/0000-0002-5484-241X))

## Response text

DOI: [10.7554/eLife.88616.4.sa3](https://doi.org/10.7554/eLife.88616.4.sa3)

The following is the authors’ response to the previous reviews.

eLife assessment

This study presents useful findings regarding the impact of forest cover and fragmentation on the prevalence of malaria in non-human primates. The evidence supporting the claims of the authors is, however, incomplete, as the sampling design cannot adequately address the geospatial issues that this study focuses on.

Public Reviews:

Reviewer #1 (Public Review):

The study as a concept is well designed, although there is still one issue I see in the methodology.

I still have concerns with their attempts to combine the different scales of data. While the use of point data is great, it limits the sample size, and they have included the district to country level data to try and increase the sample size. The problem is that although they try to get an overall estimate at the district/state/country by taking 10 random sample points, which could be a method to get an estimate for the district/state/country. It would be a suitable method if the primates were evenly distributed across the district/state/country. The reality is that the primates are not evenly distributed across the district/state/country therefore the random point sampling is not a reasonable method to get an estimate of the environmental variables in relation to the macaques. For example if you had a mountainous country and you took 10 random points to estimate altitude, you would end up with a large number, but if all the animals of interest lived on the coast, your average altitude is meaningless in relation to the animals of interest as they are all living at low altitude. The fact that the model relies less on highly variable components and places more reliance on less variable components, is really not relevant as the district/state/country measurements have no real meaning in relation to the distribution of masques.

A simple possible way forward could be to run the model without the district/state/country samples and see what the outcome is. If the outcome is similar then the random point method may be viable (but if it gives the same outcome as ignoring those samples then you don't need the district/state/country samples). If you get a totally different outcome then it should raise concerns about using the district/state/country samples.

This paper is a really nice piece of work and is a valuable contribution but the district/state/country sample issue really needs to be addressed.

Recommendations for the authors:

Reviewer #1 (Recommendations For The Authors):

A simple possible way forward could be to run the model without the district/state/country samples and see what the outcome is. If the outcome is similar then the random point method may be viable (but if it gives the same outcome as ignoring those samples then you don't need thedistrict/state/country samples). If you get a totally different outcome then it should raise concerns about using the district/state/country samples.

Thank you for your comments, and for the suggestions to address the issues identified in your main commentary by running an analysis on exclusively GPS geolocated data points. This was the original plan for analysis, but the available data identified in the literature review includes only 14 data points (macaque P. knowlesi prevalence surveys) with associated GPS coordinates. This was found to be too limited to obtain meaningful results from a regression analysis, and hence we then explored methods for utilising all available data to identify trends whilst accounting for spatial uncertainty in the analysis. As the point location only represents the location of capture and not the extent of the home range of the NHPs, we additionally feel there is value in exploring methods to encompass the wider surrounding habitat.

We do appreciate the concerns you raise with the random point method being used to represent macaque survey sites when species of interest are not necessarily evenly distributed across an area. To investigate this, we ran sensitivity analysis on a subset of the dataset according to whether the points fall in areas of >50%, >75% or >90% predicted probability of macaque occurrence, with maps derived from published models of macaque suitability in Southeast Asia. For each of these thresholds, points that fall outside these areas were removed – such that, if a random point is located on a mountain range where there is 0 likelihood of macaque occurrence, it is excluded from the analysis. We found that restricting analysis to areas with highly probably macaque habitat still shows a robust effect of forest cover on NHP prevalence, and additionally that for the most conservative (>90%) habitat threshold there remains an effect of forest fragmentation on prevalence (Appendix 6—table 9, Appendix 6—figure 5). Given that using the full data set increases the uncertainty, as there is more variation in covariates between the replicates, this can be considered a more conservative approach to detecting an effect of environment as reported in the main findings.
