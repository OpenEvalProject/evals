# Peer review - Round 1

Editors:
- Jennifer Flegg, The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68441.sa1](https://doi.org/10.7554/eLife.68441.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper presents a comparison of several mathematical models of human mobility in low and middle income settings, fitted to mobile phone usage data. This article is of particular interest to researchers within the field of human mobility studies, in addition it is also of potential interest to a broader audience with interests in the application of human movement patterns such as the spread of infectious diseases, health service access and utilization, logistics and more.

Decision letter after peer review:

Thank you for submitting your article "Characterizing human mobility patterns in rural settings of Sub-Saharan Africa" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jennifer Flegg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Francois Rerolle (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Is there data across more countries in Africa? If so, it would be great to see the applicability of the recommendations of models to similar settings.

2) Can the authors be clearer about how they select which model was most appropriate for different contexts eg the interplay between model fit and model complexity?

3) Can the authors comment on the likely suitability of the recommendations outside of Africa?

4) Why were only 1.4% of randomly selected subscribers from the Burkina Faso provider included? Was this the only data provided to authors or was this the percentage of subscribers left once the authors excluded local movement within the district?

5) Line 138 of the manuscript reads "By comparing and evaluating a wide range of models…" This statement is too broad and potentially misleading given that all models (except the radiation model) utilised in this study are variations of the gravity model.

6) Have the authors considered deriving an ensemble model as part of their future work? If they were to pursue this idea, it would be interesting to see the results from other interaction models first such as an intervening opportunities model.

7) It would also be great to see something similar done for LMICs on a different continent, although I note this is beyond the scope of the current manuscript.

8) Given the differences in time frame for call data records (provided in the supporting information) used for each country, this should be discussed in the Materials and methods section of the manuscript.

9) The rationale behind the choice of the target interval of 0.5-2 times the observed trip counts determined to be appropriate for the percentage of estimated trips should be included.

10) From the title, I was expecting a bit more description/characterization of what the human travel looks like on these settings. I believe the article needs to describe the overall patterns of human mobility highlighted in the data collected rather than focus too much on model performance. How many trips are there per inhabitants per year? How much does it depend on distance (simple interpretation of decay function: trips decreased by X% every 100km or something like that), population density (there are Y times as many trips to urban areas compared to rural areas). And how it varied across the 3 countries.

11) The analysis ends up suggesting a variation of basic models with more parameters, adapted to the rural settings of sub-saharan Africa. Shouldn't the introduction provide more background on the performances of the basic models and their more parametrized variations in settings where they have been developed (high-income countries)? One would expect the basic model not to perform as well across all mobility settings of high-income countries. Similar adjustment for regionality and urbanicity may be needed (and previously evaluated) in more studied settings of rural America for instance?

12) Figure 1 J-L: For those type of plots, it would be worth spending a sentence or two to describe interpretations. For the axis, I know there is a reference to supplementary materials but it took me a while to understand that these were just numbered locations? Same comment with respect to the coloring, what proportion is that referencing to? Within a destination? Overall? Why categorize the coloring and not use a continuous nuanced color palette? Breaking by log values seems arbitral and the bluest categories contains a very wide range of proportion (0.1 to 1). Also, have you considered sorting the locations by population density? It might convincingly demonstrate the limitations of the basic model.

13) The introduction mentions other studies in LMIC that have adjusted basic models with individual levels factors such as education, SES, gender,etc and improved the fit. In this study, the authors propose a different and higher-level type of adjustment (regionality and urbanicity of trips' origin/destination). Are the authors also able to adjust for those individual level factors or are they absent from the mobile phone data? The comparison with previous work and improvements suggested in the article would be more convincing if both type of adjustment are done and combined on the same datasets. Otherwise we can't really compare the 2 approaches and advocate in favor of one or the other, can we?

14) Stratifying models by features (urbanicity and regionality) limits generalizability to other settings important features and/or where cut points (e.g, between rural and urban) may need to be different. Thanks to Bayesian analysis, have the authors considered modeling parameters of the gravity models as continuous functions of population density instead? Although it would decrease interpretability of the results, it would improve generalizability of the work and potentially result in significant fit improvements.

15) The authors compare models' performance based on % change in DIC. I am not as familiar with DIC, but I thought absolute changes (for AIC) were more relevant. Can the authors please clarify?

16) Lines 275: The selected interval (1/2; 2) seems both arbitral and pretty wide. Could the authors elaborate a bit more on it?

17) Figure 3B: Out of the gravity models, the bell curve for the basic model seems to be the closest to the 1:1 ratio except for the rural-rural trips. Doesn't this mean it is well performing?

18) At first, it is a bit confusing to use similar notation for functions used in the equations to denote exponential/power decay f() and stratification of parameters f(all trips), f(urbanicity),…. Can the authors please revise the notation?
