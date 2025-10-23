# Peer review - Round 1

Editors:
- Ben S Cooper, https://ror.org/01znkr924 Mahidol University Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72123.sa0](https://doi.org/10.7554/eLife.72123.sa0)

This study will be of interest to readers in the field of virus discovery. This study attempts to identify predictors of human-infective RNA virus discovery and predict high risk areas in a recent period in the United States, China, and Africa using an ecological modeling framework. The study has potential to inform future discovery efforts for human-infective viruses.


---

# Peer review - Round 1

Editors:
- Ben S Cooper, https://ror.org/01znkr924 Mahidol University Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72123.sa1](https://doi.org/10.7554/eLife.72123.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Predictors of human-infective RNA virus discovery in the United States, China and Africa, an ecological study" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Benn Sartorius (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) It seems unlikely that virus discovery effort is homogenous over the large geographic areas considered in this analysis and we would like to see additional work to address remaining discovery bias by extending the analysis to include adjustment for more granular measures of discovery effort. While we don't want to be too prescriptive about how this should be done, we would suggest that bibliographic data potentially provides a valuable and readily-available source of information about how research effort related to virus discovery varies with space and time. It should be possible to use such data to derive sub-national indicators that are both more granular than national economic indicators, and that might be expected to be more directly related to virus discovery effort. We suggest that governance indicators (transparency) and laboratory infrastructure/technology indicators are also considered as predictors.

2) Clarification is needed about how space and time is currently dealt with in the boosted regression tree model.

3) Currently it seems that virus discovery data were matched to covariate data using the nearest decade. Since there might be important changes in virus discovery effort and other covariates at finer timescales, we feel it is important to at least perform a sensitivity analysis to check for this variation and consider how it might impact on the results.

4) We would like to see a consideration of lag periods between the covariates/predictors and virus discovery. i.e. changes in predictor in t-1 year may be more predictive of virus discovery at year t.

5) Clarification is needed regarding handling of how potential collinearity between the predictors.

6) We would like the authors address the likely differences in underlying drivers/predictors for vector-borne (V) vs non-vector-borne (N) viruses and strictly zoonotic (Z) vs human transmissible (T) viruses. This could be done, for example, by using separate models.

7) It would be useful to provide an appraisal of the impact related past studies have had on improving surveillance and control.

Reviewer #1 (Recommendations for the authors):

This study attempts to identify predictors of human-infective RNA virus discovery and predict high risk areas in a recent period in the United States, China and Africa using a ecological modelling framework. The study is relevant in the current context and identification of areas at threat of emerging viral pathogens.

According to findings from their previous study published in 2020, the main predictors for virus discovery at the global scale were GDP-related i.e. and they concluded that this may largely have driven by research effort rather than the underlying biology. In the current study, they have attempted to focus on more restricted and homogenous regions where they suspect research effort is less heterogeneous to an attempt to identify predictors more associated with virus biology. I have some comments and concerns below that would need to be addressed in my opinion prior to a final decision being taken.

While I do understand the rationale for the restricted analysis, I am still concerned that inherent "discovery" bias in the data and how these vary by region and within country/region and across time may still drive the observed associations rather than real distal predictors of virus discovery.

Furthermore the relative lack of accurate geolocating of data in China relative to the other two regions may also misalign the covariate values attached to these data points and potential skew association particular of the more influential covariates vary substantial across space.

Was the model applied at location-year level i.e. spatial and temporal? This was not entirely clear to me under Boosted regression tree model description.

If I understood correctly virus discovery data were matched to covariate data using the nearest decade? While some covariates are likely to change more slowly, some may be far more dynamic (especially at the edge of human-animal-environmental interaction) and vary within a decade. Where any sensitivity analyses conducted to check for this variation within decade and how it might impact on the associative coefficients/influence?

Did the authors consider or test for various lag periods between the covariates/predictors and virus discovery? i.e. changes in predictor in t-1 year may be more predictive of virus discovery at year t.

Did you consider collinearity between the 33 predictors as many of these would likely be highly correlated?

What other predictors were considered in the ecological framework i.e. governance indicators (transparency) and laboratory infrastructure/technology indicators? These would seem to be important re: potential bias in reporting of newly discovered viruses for the former ("effective surveillance is challenging in less developed regions such as large parts of Africa given resource constraints" as alluded to in the introduction) and likelihood of detection for the latter ("better resources to discover new viruses" and "effective surveillance is challenging in less developed regions such as large parts of Africa given resource constraints" as alluded to in the introduction).

Did you consider separate models (#4) for vector-borne (V) vs non-vector-borne (N) viruses and strictly zoonotic (Z) vs human transmissible (T) given the likely difference (and ecological association) in underlying drivers/predictors across these envelopes?

Reviewer #2 (Recommendations for the authors):

As this type of work has been ongoing for some time, It would be useful to provide an appraisal of the impact these past studies have had on improving surveillance and control.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Predictors of human-infective RNA virus discovery in the United States, China and Africa, an ecological study" for further consideration by eLife. Your revised article has been evaluated by George Perry (Senior Editor) and a Reviewing Editor.

The authors have gone some way to addressing the essential revisions from the first round of reviewers and have conducted some of the additional analyses requested. However, this additional analysis does not appear to have been included in the revised manuscript files. While additional analysis is reported in the document with the responses to reviewer comments, it is important that the changes are also included in the manuscript.

Considering the requested essential revisions in turn:

Essential revision 1 asked for additional work to address discovery bias by extending the analysis to include adjustments for more granular measures of discovery effort. The response to this was to clarify aspects of the analysis (e.g. the granularity of GDP indicators) and to add some text to the discussion (lines 408-412) referring to approaches to this problem taken in other papers. There was also a short exploration (figure R1 in the response document, but not appearing in the manuscript) showing the relationship between "published human-infective RNA virus count and the total number of papers from the journals which published all human-infective RNA viruses in Web of Science", and accompanying text that argued that attempts to adjust for discovery effort used by other authors would not be applicable here. I was unable to follow this argument, and given that no additional analysis addressing discovery bias appears in the main manuscript it seems that the essential revision was not undertaken. While the changes the authors have made to the manuscript are welcome, given that (following consultation) round 1 reviewers highlighted this as the key point to address it is important that the authors reconsider how they can change the manuscript to address this point. This may just amount to additional analysis in the supplementary material demonstrating that approaches used by other authors have little applicability here as claimed in the rebuttal letter, but if so the reasoning needs to be expressed more clearly and the evidence for any such assertions clearly laid out.

Essential revision 2 appears to have been addressed adequately.

Essential revision 3 asked for sensitivity analysis to consider matching covariates at finer timescales. This additional analysis appears to have been done but has not yet (as far as I could tell) been included in the revised manuscript.

Essential revision 4 asked for additional analysis that included consideration of lag periods between the covariates/predictors and virus discovery. Again, this appears to have been done and is shown in the rebuttal letter, but I could not locate the new analysis in the revised manuscript files.

Essential revision 5 appears to have been addressed adequately.

Essential revision 6 again appears to have been addressed with additional work but this does not appear to have been included in the revised manuscript.

Essential revision 7 appears to have been addressed adequately (though note that the line numbers for the changes given in the rebuttal letter (311-330) do not correspond to areas of highlighted changes in the manuscript with changes marked).
