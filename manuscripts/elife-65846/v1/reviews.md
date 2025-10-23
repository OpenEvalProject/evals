# Peer review - Round 1

Editors:
- Jennifer Flegg, The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65846.sa1](https://doi.org/10.7554/eLife.65846.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper will be of interest to parasitologists, immunologists and modellers working in the field of malaria. It provides a model-based approach to quantify different host responses to malaria infection and identify the response(s) best explaining the infection outcomes (i.e., survival rate and host resilience to malaria infection). The methods for model construction and fitting and data analysis are appropriate and rigorous, however, extra work is required for validation of model predictions, which are critical for the interpretation of the results.

Decision letter after peer review:

Thank you for submitting your article "Within-host dynamics reveal functional diversity of host resilience to malaria infection" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jennifer Flegg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Miles Davenport as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Parameter correlations. The results of the manuscript are primarily based on the parameter estimates, which are calculated by the samples of the posterior distributions, so the correlations between model parameters (based on the posterior samples) should be examined. One example for the correlated parameter would be the activation rate and decay rate of immune response in equation 1. Since the immune response Ni was not measured and used in model fitting, the two parameters should show a strong positive correlation, which would prevent accurate estimates. A clear view of the parameter correlations is critical for the reliability of the estimates and in turn any conclusion based on the estimates.

2) Prior distributions. These were not shown on top of the posteriors such that it is difficult to judge how much information was from the priors and how much was from the data. Since the priors are relatively informative, e.g. 2.5 and sqrt(2.5) (see Table 1), it is also necessary to examine the impact of the choice of the priors on the posteriors by a sensitivity analysis. The choice of priors is not well-justified. How were the hyperparameters for the host response parameters chosen? Is the model sensitive to these?

3) The authors showed that the too strong and too weak immune activation predicted by the model was associated with high host mortality and concluded that a balanced immune response may be a major determinant of host survival. However, a stronger immune activation in the model refers to a higher activation rate (i.e., a higher value of parameter psi in equation 1). This is not necessarily related to a balance immune response, which is a balanced level of expression of pro-inflammatory and anti- inflammatory cytokines and is mathematically interpreted by that a strong/weak activation should be associated with a strong/weak decay such that the net effect (Ni in equation 1) is maintained at a healthy level. Further clarification on this point is necessary.

4) Cytokine dynamics. In the results, the authors selected and discussed some model predictions that are consistent with what the cytokine data suggest. However, it lacks a comprehensive comparison between the data and the model prediction. I am wondering if it is possible to create a figure similar to Figure 3b (only psi's and phi's) using the cytokine data and compare with the model prediction. It will tell clearly how well the model predictions are consistent with the data. Could you connect the cytokine dynamics with the mechanistic model more directly? This seems like a missed opportunity – you have beautiful timecourses here – could you reframe the model to directly include processes reflected by the cytokines?

5) Figures. It would be useful to have a detailed graphical representation of the model in the main text. The temporal information in Figure 5 is hard to process.

Reviewer #1:

This paper presents a dynamic mathematical model of malaria parasites and red blood cells in a mouse model. A strength of the paper is the collection of experimental data to fit to the mathematical model, however the model is overly simplified and is therefore unlikely to have high impact in the field.

Reviewer #2:

Kamiya, Davis et al., studied the associations between the diversity of host responses to malaria infection and infection outcomes (i.e., survival rate and host resilience to malaria infection). In detail, they collected the longitudinal data from mice that are genetically different and estimated some key biological parameters governing the parasite replication dynamics and immune responses by fitting a mathematical model to the data. By comparing the parameter estimates and a set of cytokine data collected from the same pool of mice, they identified some consistency between model predictions and data and concluded that the longitudinal data contain important information that may facilitate the explanation of the diverse infection outcomes. The methods for model fitting and data analysis are appropriate and rigorous. The conclusion about balanced immune response is partly supported by the data but not clearly associated with model predictions. Some further analyses on fitting results are necessary in order to ensure the reliability of some conclusions.

Reviewer #3:

The first section of the analysis connects parameter estimates with outcome. With such a large model this section needs a thorough analysis of correlations between parameters – the PCA goes a little way towards this, but not enough. Identifying parameter subspaces might also make the interpretation of these fitted values simpler.

The second section – the data are rich, but it feels let down slightly by its qualitative nature. Could the authors connect the cytokine dynamics with the mechanistic model more directly? This seems like a missed opportunity – there are beautiful timecourses here – could the model be reframed to directly include processes reflected by the cytokines?

It would be useful to have a detailed graphical representation of the model

in the main text.

The temporal information in Figure 5 is hard to process. I like the idea of the 'phase-space' view but here I think it would be clearer to have the timecourses of pro and anti-inflammatory cytokines stacked on top of each other.

At what time(s) of day were the cytokine measurements made? Were they consistent? Given there is a daily replication/infection cycle, I would guess timing matters.

p9 "We found that reducing the expression of anti-inflammatory …" This phrase is misleading as there was no intervention that reduced expression.
