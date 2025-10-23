# Peer review - Round 1

Editors:
- Joel K Elmquist, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53560.sa1](https://doi.org/10.7554/eLife.53560.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "A big-data approach to understanding metabolic rate and response to obesity in laboratory mice" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Mark McCarthy as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: John R Speakman (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Corrigan and colleagues offer a large-scale, multi-site analysis of indirect calorimetry as a tool for determining metabolic rate. The authors should be applauded for trying to provide systematic and rational guidance for interpreting this type of specific data sets. However, several issues need to be addressed. Despite the impressive attention to detail in the experimental approach (age-matched mice from the same room at Jackson, diets from the same lot and shipment, analysis of both MMPC and IMPC datasets), the final conclusion appears to be more of a cautionary tale against the over-reliance and over-interpretation of indirect calorimetry, rather than a useful set of guidelines that can be used by all investigators. The authors need to deal with a potential artifact of the way the analysis regarding fundamental rules for multiple regression analysis.

Essential revisions:

A big picture question not really addressed are these institutional variations addressable or does this study call into question the usefulness of indirect calorimetry to provide meaningful insights into metabolic rate?

The model represented in Figure 1F depends on a multiple regression analysis but a fundamental assumption of such an analysis is that the independent variables are independent – by definition. In this case they are not because there are institutional differences in lean and fat mass as shown in Figure 1E. This would tend then to diminish the variance attributable to the traits that differ within site. Indeed lean mass and mass here account for only about 30% of the variation in the EE while other studies indicate much larger explained variation by these two factors (see eg Kaiyala's work). I think it would therefore be better to first omit institution from the analysis – find the effects of lean mass, fat mass, locomotor activity etc and then ask if institution explains any of the residual variation once these biological factors are accounted for.

The most striking finding is how much inter-institutional variation exists between identical experiments. However, there are no suggestions as to how this can be overcome. Is there some standard that all systems can be calibrated to?

It is nonetheless of considerable value as it nicely compares the impact of covariates such as sex, locomotion, body weight, temperature or body weight and body composition on EE variance for a large body of data. Of particularly interest are further the EE data of KO mice that had been linked to obesity in GWAS analyses. First, rather preliminary, assessments indeed suggest that these genes are involved in the regulation of energy homeostasis. This finding would warrant a more comprehensive display of available IMPC data. Furthermore, did the authors try to compute individual factors for the different institutions that would allow to normalize the data between sites? Would such an adjustment normalize the residuals for some of the KOs in Figure 6D,F?

The dominant institutional effect is actually not proven because of the confounding collinearity in the predictors. Institution clearly is not independent of the other factors so the way it is treated in the analysis is key. I strongly advise fitting the biology to the data and then afterwards asking if institution explains any residual variance. That will give a much more representative picture of the institutional effect.

Were environmental measures such as humidity, luminance measured in each room? Were the time of the day when experiments were conducted similar?

The fact that mice at UMass consistently show an RER significantly above 1 during the dark cycle (Figure 1—figure supplement 1E), suggests that this is needed. Is there a way to present raw data, independent of the analysis algorithms of each system? Are they suggestive of an unappreciated biological complexity in that mouse model, or a systemic flaw in that institution's set up?

The resource fails to report how large difference in body weight/composition may affect the data (e.g. comparing a very obese KO model to a lean WT). Will the same ANCOVA analysis be sufficiently robust if animals differ in X % of body weight or lean mass? What should be the limit?

The authors suggest changes in gut microbiota and/or epigenetic changes induced by different environmental triggers. Providing such data would likely be a decisive advance for our field. However, as it now stands it may be better not to specify the factors but just say “site specific factors”.

The analysis here is interesting and sobering for those of us trying to discern effects of genotype on metabolism but there is still the collinearity issue in the predictors of the linear multiple regression (subsection “Variability in KO phenotypes”).
