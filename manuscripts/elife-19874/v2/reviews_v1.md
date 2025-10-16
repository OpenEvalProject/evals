# Peer review - Round 1

Editors:
- Mark Jit, London School of Hygiene & Tropical Medicine, and Public Health England , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19874.036](https://doi.org/10.7554/eLife.19874.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Structure in the variability of the basic reproductive number (R0) for Zika epidemics in the Pacific islands" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Prabhat Jha as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

On the whole, the reviewers and the Reviewing Editor appreciated the work. Although there have been a number of previous attempts to estimate R0 for Zika using Pacific Island data, they see the importance in the use of a stochastic model in order to obtain more precise values for both point estimates and uncertainty bounds, as well as the efforts to capture some degree of the structural uncertainty in model design. Making the source data available was particularly appreciated as this enhances the transparency and reproducibility of the analysis.

The reviewers and Reviewing Editor had only two requirements, although both of them are important:

1) Despite a better effort than many to explain the methods used, the details were still unclear to the reviewers. Hence we would like to see the full model code used for the analysis made available alongside the source data.

2) There was some concern over the estimation and interpretation of the parameter ρ, which appears to be a key parameter in the model but is poorly defined. This reduces the population actually involved in the epidemic dynamics as a result of "spatial heterogeneity, immuno-resistance or cross-immunity". It ranges between 34% to 74% across models and islands, and is especially variable in New Caledonia between the two models (34% – 70%). It seems particularly strange that ρ is actually smaller than final seroprevalence rate in the outbreak (73% in Yap and 94% in French Polynesia), when most of the population was naïve prior to the outbreak. How do people seroconvert if they are not involved in the epidemic? And if part of the population was actually protected from infection, is there any evidence to support the mechanism (eg. genetic links to Zika susceptibility, or spatial data showing that part of the islands were unaffected)?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Structure in the variability of the basic reproductive number (R0) for Zika epidemics in the Pacific islands" for further consideration at eLife. Your revised article has been favorably evaluated by Prabhat Jha as the Senior editor and the previous reviewers.

Firstly, we would like to apologise for the time it has taken to respond to your resubmission. We wanted to consult further about the issue of model code availability stated below, but unfortunately this process took far longer than anticipated.

Overall we are happy with the revised article and are almost ready to proceed to acceptance. The one outstanding issue is the availability of the model code. We do understand that you have provided a link to the code to the algorithm used for parameter inference. However, the editors and reviewer were unable to understand how to reproduce your numerical findings using the code in the repository plus the data included in the Appendix. As far as we can tell, all you have provided is a link to code written by other developers that was used in your model, not the actual compartmental model itself.

We would like you to provide either (i) an explanation that we are wrong and that your results (including all the figures behind all the tables and graphs) can be fully regenerated using this code, or (ii) the actual code itself. Once you are able to provide this, we should be able to proceed very rapidly to a final decision
