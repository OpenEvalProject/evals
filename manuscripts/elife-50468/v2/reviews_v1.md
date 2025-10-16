# Peer review - Round 1

Editors:
- Miles P Davenport, University of New South Wales Australia

Reviewers:
- Miles P Davenport, University of New South Wales Australia
- Jon Zelner, UMICH
- Edward J Feil, Univesity of Bath United Kingdom

## Review text

DOI: [10.7554/eLife.50468.sa1](https://doi.org/10.7554/eLife.50468.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript addresses the important question of transmission of drug resistance in a hospital setting. It analyses a dataset of children regularly swabbed for Klebsiella pneumoniae after admission to an intensive care unit in Cambodia. Such data is inherently complex and difficult to interpret. The authors use mathematical modelling approach to investigate the role of a number of factors such as colonization pressure, antibiotic treatment, and breastfeeding. The results provide insights into the spread of drug resistant bacteria in an important setting for the development and transmission of drug resistant bacteria.

Decision letter after peer review:

Thank you for submitting your article "Transmission dynamics and control of multidrug-resistant Klebsiella pneumoniae in neonates in a developing country" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Miles P Davenport as the Reviewing Editor, and the evaluation has been overseen by a Neil Ferguson as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jon Zelner; Edward J Feil.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript uses a modelling approach to investigate acquisition of drug resistant bacteria in a hospital setting. The authors study various risk factors for 'acquisition', and find that antibiotic use was the only significant effect. The strength of this study is that it looks at a very clinically important organism in the exact setting in which it is problematic. The value of the study is tempered by the fact that much of the screening data was already published, along with more coarse-grained analysis of the role of antibiotic on acquisition. The modelling and analysis is therefore a central factor in the study, but also falls short in several ways that need to be addressed. The reviewers expressed that there are several possibilities to improve the analysis that need to be explored.

Essential revisions:

1) the Bayesian approach to model fitting of the risk factor and the transmission models, uses arbitrary priors, that do not truly reflect prior probability. Despite the authors claim that they were selected to be weakly informative, most prior distributions cover a range that make it possible that they are significantly influencing the posterior. A straightforward way of conveying this to the reader is to plot the prior and the posteriors together. This is a key shortcoming because if the model estimates are driven by these arbitrary choices, much of the remaining paper comes into question. This is certainly a criticism that can be addressed by changing the fitting approach to remove the influence of the priors, or by switching to another approach, maximum likelihood or proportional hazard models.

2) the results of the model are not presented carefully, many of the risk factors have credibility intervals that would not generally be considered significant, yet are presented as if they are (e.g.: "covariates associated with reduced daily risk of acquisition," but nothing in this paragraph is significant; "suggests that contamination left by previously colonized infants decays rapidly to background levels", when there is no support for the model with this parameter and the λ estimate is heavily influenced by the prior with mean 1 and variance 2). This is also true for the results presented in Figure 4B, C, D and the lengthy discussion in Discussion section, which fails to accurately convey the possibility that these factors play no role in colonization is also consistent with the data. The large uncertainty in most parameter estimates likely reflects the challenge of fitting 109 observations with a 14-parameter model. This needs to be stated and the limitations emphasized.

3) the analysis of the transmission models appears to have a bias toward finding model 4 to be the best because there is a single value of α for all the sequence types, but there are different average colonization probabilities across the sequence types (because some had many more observed colonization events than others). This variability it likely to be picked up, at least to some extent, in the ST specific betas. A fairer test is whether ST specific β fits better than a ST specific alphas. The temporal clustering of ST in Figure 3F suggest this may be true, but the approach seem to have been biased to find an effect of β. Are there explanations for the temporal clustering of the ST other than transmission in the NU, such a transient increased in the community or in the water supply etc.

4) A concern with this analysis relate to the way the different infection models are described. Specifically, the differentiation between a 'risk factor model' and a 'transmission model'. It is not clear from the main text that the transmission models considered are essentially hierarchical regression models in which the impact of an increasing number of colonized patients is considered to have an additive rather than a multiplicative effect on individual risk. This is not a critique of the modeling, which is generally appropriate and well-done. But it is difficult to read the manuscript and understand the distinction between these two sets of analyses. In addition, the authors should clarify earlier that the non-significant, negative OR for colonization pressure may be due to this fact as a way of framing the need for an additive model that more able to directly account for the impact of transmission on daily infection risk.

5) It is not clear to me why the transmission models could not incorporate some of the covariates used in the first set of risk factor models. For example, age at admission or the number of nurses on the unit could be used to modulate infection risk, i.e. be used to calculate an individual risk ratio that is then multiplied by the hazard of infection, e.g. exp(\ζ Xi)*(\α +\β ni), where Xi is a set of individual or day-specific risk factors, and \ζ is a vector of log-risk ratios. This would seem to make the most of the data and incorporate both the additive effect of colonization pressure with the risk-modulation of individual level factors.
