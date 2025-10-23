# Peer review - Round 1

Editors:
- Prabhat Jha, University of Toronto , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00626.010](https://doi.org/10.7554/eLife.00626.010)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Targeting Malaria Transmission Control: Predicting Mosquito Infectivity from Plasmodium falciparum Gametocyte Density” for consideration at eLife. Your article has been favorably evaluated by Prabhat Jha as Senior editor and 3 reviewers, one of whom was Vasee Moorthy.

The reviewers discussed their comments before we reached this decision and the Senior editor has assembled the following major substantive comments to help you prepare a revised submission.

1) Estimating Gametocyte Density From QT-NASBA Assays

I do not know the inverse regression problem well and can appreciate that there are alternative approaches. The supplementary file indicates some uncertainty in the choice of this method “for discussion see Osbourne, 1991” but this is not explained. It would be useful to give brief reasons why the particular method was chosen.

The authors say that QT-NASBA may detect only female gametocytes and elsewhere that the sex ratio of P falciparum can change to optimise transmission. This may alter the shape of the relationship between QT-NASBA results and the estimated gametocyte densities.

It would be useful to validate the model for estimating gametocyte densities from QT-NASBA assays for data other than that to what was fitted.

Figure 1A shows a double hump in the relationship between gametocytes in the blood sample and mosquito infectivity. This seems unintuitive for a biological process. I wondered to what extent this might be forced by the functions chosen. Does adding extra flexibility result in the same double hump?

Figure 1: An elegant presentation of this data. In the inset to part A there is a large clump of points on the x axis and it is not clear that the fit is good enough to be useful. For me this graph highlights the importance of understanding how different the line is in this model to other lines, and how much better this model fits, than the models that are the next best fit.

Please provide some discussion of this in the text (in addition to supplementary information). A listing of alternative models with their goodness of fit on a quantitative basis should be included in the manuscript itself.

The uncertainty range is huge, and ranges from very little increase in infectivity with increasing gametocyte density, to very steep increases in infectivity with increasing gametocyte density. What steps do the authors propose are taken to reduce the uncertainty range?

2) Mosquito Infectivity

Equation A4 includes a parameter called kappa. This is confusing since kappa is conventionally used to represent the infectious reservoir.

Results: The results for age are presented as if there was evidence of an effect, but the confidence intervals suggest otherwise.

The rationale for adjusting for asexual parasite density was not clear. It “improved model fit” but the aim here is not the best fitting model so much as to describe the relationship between estimated gametocyte density and infectivity. Including asexual parasite density as a main effect modifies the interpretation of the parameters.

3) The Paper Estimates the Relationship Between Gametocyte Densities and Age

The data comes from a cross-sectional survey of 412 people in a village in Burkina Faso. There is likely to be seasonal variation in parasite densities and the relative densities in adults and children may vary seasonally due to different levels of acquired immunity. It should be stated when the survey was carried out and also that a single survey is a potential limitation.

4) Efficacy Definition

A major issue is to be quite clear what is meant by efficacy throughout the paper. This lack of clarity permeates this entire technical area (i.e., not only this manuscript) and causes a lot of confusion. I believe most or all instances of use of the word efficacy in this manuscript refers to a % reduction in the gametocyte density. How does this relate to % reduction in proportion of infected mosquitoes and how will this translate to reduced incidence of human infection? This is a critical discussion that is omitted. Discussion of efficacy without some idea what this translates to in terms of reduction in human infection is rather misleading.

If the authors mean reduced transmission from humans to mosquito, I suggest they use a narrative phrase, such as this and do not use the word efficacy at all.

5) Data/Model Description

The data the model was fitted to was not well described (“repeatedly testing samples with known gametocyte density”). I also had trouble working out whether the fitting was simultaneous with the model for mosquito infectivity or not. The text mentions that the “estimates were used in the functions below” but the table presents all parameters together. My concern is that that the error in the estimated gametocyte densities, from the QT-NASBA results and also the chance of gametocytes being contained in the blood sample, is incorporated.

The model and parameters are not explained. The methods section merely mentions “a mathematical model” and the supplementary file gives an equation involving three parameters, but it is not clear how the equation was derived or what the parameters represent. A smooth curve is produced, but the relationship does not necessarily have to be smooth: for example, pregnant women may have higher parasitaemia and affect the age-curves.

Figure 2A suggests that the relationship does not fit well for two of the age groups. This should be acknowledged and possible reasons mentioned.

A negative binomial error structure was used. The Figure 2—source data 1 table suggests that there were some zeros in the data and that the densities are skewed. Did the residuals suggest a good fit? If there are many zeros, then a zero-inflated negative binomial model may be more appropriate.

6) Acknowledge Limitations

On a couple of occasions, the authors make statements that are not backed up by evidence from this paper.

Discussion. It is implied that this work gives direct evidence of the effectiveness of parasite strategies at low gametocyte densities such altering the sex ratio, but no direct information on strategies is obtained.

Although the paper does include an elegant sampling approach to quantify uncertainties, Although the paper does include an elegant sampling approach to quantify uncertainties, there should be a beefed up discussion of the uncertainties underlying this work. The authors should provide more discussion on what is known about which parameters in the input data are driving uncertainty, how much confidence they have that the model they chose is superior to alternative models, and on what basis they made this decision. There should also be a discussion on the limitations related to the differences between mosquitoes used in feeding assays, and wild-type mosquitoes.

Although uncertainty is presented in one of the figure panels, and this is very helpful, uncertainty ranges/confidence intervals should be quoted in the text where figures are provided.

We suggest that the authors consider how the paper can act as an aid to conceptualising the components underlying person-to-person transmission in field settings, and to gaining a better understanding of the uncertainties related to the component of transmission that their results speak to, and also to gain a better understanding of what the existing data gaps are that must be filled in order that the research community can determine how to test new transmission-reducing interventions, and quantify their effect on person-to-person transmission.
