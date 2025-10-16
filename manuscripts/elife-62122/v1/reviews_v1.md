# Peer review - Round 1

Editors:
- Isabel Rodriguez-Barraquer, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62122.sa1](https://doi.org/10.7554/eLife.62122.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript presents detailed findings from a multi-stage Bayesian approach to estimate spatial and spatio-temporal trends in malaria incidence in Haiti. The proposed methodology represents an advance over their well-established methodology, by explicitly modeling catchment areas, that can be adapted for different diseases to inform decision making.

Decision letter after peer review:

Thank you for submitting your article "Mapping the endemicity and seasonality of clinical malaria for intervention targeting in Haiti using routine case data" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nicole White (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript presents detailed findings from a multi-stage Bayesian approach to estimate spatial and spatio-temporal trends in malaria incidence in Haiti. The proposed methodology represents an advance over their well-established methodology, by explicitly modeling catchment areas, that can be adapted for different diseases to inform decision making. The authors should be commended for the breadth of work undertaken, and methods are justified well overall. However, we have several concerns about how the methods and results are presented and it is not entirely clear how the maps produced by this new model are an improvement over previous simpler models, and of the value this model adds beyond can be inferred directly from case data.

Essential revisions:

1. Even though the manuscript presents methodological advances in risk mapping, it lacks demonstration of the value added by the new models over simpler risk maps or over incidence patterns alone. The maps in Figure 1 seem to recapitulate the patterns in the case data. This suggests a good fit of the model, but it does not address the question of what value this model adds beyond what could be gleaned from examining the case data alone. Similarly, it is not clear whether Figure 3 tells us anything different than we might already know by mapping incidence at those administrative levels. It would be useful to provide concrete examples of the value added (beyond the discussion in lines 262-272) by these models. How simpler methodologies may be misleading with respect to transmission risk, or how these new maps lead to different decisions as compared to simpler approaches.

2. Related to the above – In terms of the methodological advance about incorporating catchment areas, it would be more convincing performance was compared to an alternative model without that feature. Likewise for the part about seasonality or any other advances presented. Demonstrating improved performance (in some way or another) is a routine expectation when introducing a newly "improved" predictive model.

3. Related to the above, it could be argued that the value added by these maps relies on their granularity. However, the validity of estimates is not validated at this fine scale. This should be explicitly discussed.

4. The paper is well written, but the significance of the advances made here is not made as clear as I think it should be for a general audience. Someone not familiar with malaria in Haiti or geospatial statistics should have an easier time understanding why this work is significant.

5. Given the complexity of the proposed methodology the presentation of the various modelling stages is difficult to follow in the Materials and methods section. This can be improved (e.g. no explanation of different subscripts; common parameters shared by the different models).

6. Please make code (and data) available. Per eLifes policy, all data needed to reproduce the study findings should be made available upon publication

7. The presentation of findings from the spatially-varying regression focus on the covariate(s) with the dominant positive and negative effect (Figure 4 and Figure 7). How was dominance defined, given that different covariates appear to be a mix of continuous and binary variable defined on different scales (or were variables standardised as part of processing)? Similarly, was posterior uncertainty in parameter slopes accounted for when determining dominance? I understand that these results are not intended to have a causal interpretation, however further details about chosen metrics here would help with interpretation.

8. The discussion of results around health facility catchments (p9, start line 168) bears resemblance to gravity modelling, yet the manuscript does not appear to reference related research. Given the proposed catchment model is a core element of the proposed methodology, further explanation of how this applies and/or builds upon existing gravity-based approaches would help place the manuscript in the context of related research.

9. The Materials and methods present four stages of modelling that are inter-related (e.g. imputed values of p_{mic,jt} from Model 1 are treated as a covariate in the geostatistical model defined in Model 2). The presentation of the full approach is quite dense and I found myself constantly switching between Models to identify connections/shared parameters. For example, I was unsure how are Models 2 and 3 are connected, or are they separate models? To improve the clarity of presentation, an overarching figure denoting links between modelling stages would be useful.

10. The introduction cites a lack of information to estimated treatment seeking propensity as a challenge for fine-scale disease mapping. This is again discussed in the Materials and methods section (lines 493 to 505), however I did not understand how this was accounted for in Model 3; were these probabilities/propensities treated as known quantities in Model 3 or were they estimated (with uncertainty)? Some further details are provided in the Discussion about this quantity (lines 281 to 284), however specific details were lacking in the presentation of Model 3 on p 25 (line 511).

11. 122: The first two paragraphs of the results were purely descriptive and read like figure captions.

12. 80-81: How accurate and durable are these serological assays following infection?

13. 421: It is not clear how necessary the seasonal trend in microscopy vs RDT is to model and how reliable it is. There appears to be one year (2019) in which there is a comparison to an RDT "gold standard" (not sure how this comparison works), but the premise of why that should be representative of other years and why there should be seasonality in this in the first place is unclear.

14. 480-484: I can understand how human movement and vector species variations could result in problems with the model, but I am less convinced that allowing slopes on linear relationships of environmental variables is an adequate way to address this problem.

15. 102: "clean the data of epidemic fluctuations" is an odd way to put it. If a temporally aggregated or de-trended description of incidence is desired, that's fine. But epidemic fluctuations are in fact real and therefore not something to be cleaned.

16. Paragraph beginning on 122: While it is good that the predicted case patterns at fine-scale resembled the patterns of cases across the country, it is not clear what new information is gained by the very sophisticated mapping exercise in this manuscript. It would seem that this paragraph could be written based on case data alone.

17. 149: While I agree with everything written in this paragraph, the results it presents are underwhelming. Given that the relative importance of different variables is only interpretable within the context of this model, what value is there in these results beyond the limited context of this model?

18. Figure 6: In addition to this figure, it might be helpful to have one that shows these patterns over time somehow (i.e., time on the x-axis).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mapping the endemicity and seasonality of clinical malaria for intervention targeting in Haiti using routine case data" for further consideration by eLife. Your revised article has been evaluated by a Reviewing Editor and a Senior Editor.

We think the additional analyses presented (Figure 9 and associated text) are a good addition to the manuscript. However, before accepting the manuscript, we ask you to please incorporate them into the appropriate sections in the manuscript (these are mostly results not methods).
