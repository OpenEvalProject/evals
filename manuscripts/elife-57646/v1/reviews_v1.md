# Peer review - Round 1

Editors:
- Miles P Davenport, University of New South Wales Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57646.sa1](https://doi.org/10.7554/eLife.57646.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The search for an HIV 'cure' includes a number of approaches. These include eradication of the latent virus, as well as strategies to prevent viral replication. The known clinical examples of HIV 'cure' have occurred in patients that have received bone marrow transplants where the new donor marrow lacked the CCR5 gene that encodes an HIV co-receptor molecule. Thus, understanding how reduced CCR5 expression affects viral replication is an important question. In this study, the authors investigate viral control in SHIV infected macaques following autologous CCR5 gene-edited transplantation. To this end, they combine experimental data on SHIV-infected macaques with mathematical models describing viral and immune cell dynamics using a stepwise approach. This as a very innovative interdisciplinary study that provides important insights to inform potential future treatment regimens against HIV.

Decision letter after peer review:

Thank you for submitting your article "Thresholds for post-rebound SHIV control after CCR5 gene-edited autologous hematopoietic cell transplantation" for consideration by eLife. Your article has been reviewed by Aleksandra Walczak as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional work is required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this study, the authors investigate the requirements for viral control in SHIV infected macaques under CCR5 gene-edited HSPC transplantation treatment. To this end, they combine experimental data on SHIV-infected macaques with mathematical models describing viral and immune cell dynamics using a stepwise approach. The Materials and methods and Results are presented in a thorough way. The article utilizes a robust data set and also uses detailed mathematical models and extensive analyses to capture the relevant dynamics.

Essential revisions:

1) The authors perform model selection based on the AIC values to determine the appropriate mathematical model describing the observed dynamics. However, the reliability of the obtained AIC values also depends on the identifiability of the estimated model parameters. Can you say anything about the extent to which you are overfitting in these models? The number of parameters is quite large and you see some quite substantial correlations (Supplementary file 3).

2) Conditioning and CCR5-deleted autologous HSCT depletes existing infected cells and pre-existing immunity to SHIV and ultimately increases the proportion of infection-resistant cells after reconstitution. It's therefore not obvious that extensive conditioning is necessarily the best strategy, and you have shown this in Peterson et al., 2017 and Reeves et al., 2017. Could this be worth highlighting early on? It may help to increase the impact of the insights you derive from the modeling.

3) When modeling reconstitution in deltaCCR5 individuals – you assume that the CCR5- cells all behave like CCR5- cells in WT transplants. This doesn't seem like a valid assumption; a proportion of CCR5-/- cells will become activated (as they do in WT transplants) and so the CCR5-/- cell kinetics should be a mixture of the CCR5- and CCR5+ kinetics. The same parameters could be used in the two groups. How sensitive are your conclusions to this issue?

4) Subsection “A reduction in SHIV-specific immunity leads to higher viral rebound set points and CD4+CCR5+ T cell depletion following ATI in transplanted animals” and Figure 5E – this section needs more interpretation/discussion. It's surprising that the only difference in parameters between the control and treatment groups was the time to virus rebound; so presumably differences across groups derive from the steady state sizes of the different populations? Are latently infected cells depleted in the transplant groups? And it's puzzling that delayed rebound in transplant groups is taken to imply more depleted immunity. Shouldn't it imply less depletion? Also – elevated virus load after ATI only occurs in the WT transplant group, not both. Please clarify and expand this section.

5) Subsection “Post-ATI viral control requires a large HSPC dose containing a high fraction of CCR5-edited cells”: Are strategies 1 and 2 not in conflict? Or does more potent conditioning somehow not necessarily imply a greater reduction in anti-SHIV immunity?

In summary, the reviewers acknowledged the analysis of an important topic by a unique dataset. However, they identified some major aspects that addressed the parameter identifiability within the model estimates as well as identifying the role of conditioning and dynamics of CCR5- cells. Therefore, we would like to ask you to analyze/comment on parameter identifiability for individual model estimates and validate the robustness of parameter estimates and, hence, model selection. This will be subject to re-review to determine if these issues have been satisfactorily addressed.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Thresholds for post-rebound SHIV control after CCR5 gene-edited autologous hematopoietic cell transplantation" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but the reviewers have identified some remaining issues that need to be addressed before acceptance, as outlined below:

1) Figure 2—figure supplement 1, Panel B: The statistical comparison total vs. TN+TCM does not make sense. As I assume that Total=TN+TCM+TEM, "Total" does not contain additional information when there is already a comparison TN+TCM vs. TEM.

2) The manuscript contains a lot of typos and needs proofreading.

3) The Berlin and London patients are still not described.

4) The authors should provide all data and code used to perform the analyses.
