# Peer review - Round 1

Editors:
- Larisa V Suturina, https://ror.org/027n02r78 Scientific Center for Family Health and Human Reproduction Russian Federation

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83662.sa0](https://doi.org/10.7554/eLife.83662.sa0)

This article provides important findings that have practical implications for reproductive medicine and would be of interest to IVF specialists. Based on the compelling strength of evidence, the study demonstrates significant results in improving the predictive value of the live birth model based on blastocyst evaluation and clinical features.


---

# Peer review - Round 1

Editors:
- Larisa V Suturina, https://ror.org/027n02r78 Scientific Center for Family Health and Human Reproduction Russian Federation

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83662.sa1](https://doi.org/10.7554/eLife.83662.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Development and evaluation of a live birth prediction model for evaluating human blastocysts: a retrospective study" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ricardo Azziz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please, expand the section "Model architecture" and clarify the details regarding "decision-level features".

2) Provide the details of how parameter optimization was accomplished as well as the architectural details, i.e., the number of layers and nodes. What was the computational overhead for training these models?

3) Consider presenting the data for all significant predictors to justify the choice for inclusion in the model and verify if the important or top features MLP (using explanation methods) uses for prediction are the same as those inferred by the logistic regression.

4) Please, consider presenting in detail a weighted sampling approach used to tackle the imbalance issue.

5) The code is available only for generating figures 2, 4 reported in the paper. For figure 3, only data is available. Consider presenting this code for reproducibility purposes.

6) Please, improve the discussion of the potential applications of the proposed model in clinical settings and mention the method of testosterone assessment as a study limitation.

Reviewer #1 (Recommendations for the authors):

The authors could mention the method of testosterone assessment as a study limitation that may cause a potential bias regarding the estimation of significance of testosterone as a predictor of live birth.

The authors could consider presenting the data for all significant predictors (of example, in the supplemental Figure 3 data) and justify the choice for inclusion in the model. It will better demonstrate the correctness of the selection of predictors

Reviewer #2 (Recommendations for the authors):

I quite enjoyed reading the article. Overall, the motivation and concepts are well defined; however, the manuscript lacks the necessary methodological details, which hindered my ability to fully understand and appreciate the work.

The link between CNN and MLP architecture in the final integrated model is unclear. The section "Model architecture" needs to be expanded. It is not clear what "decision-level features" are from CNN or MLP. Are these features from the CNN's fully connected layer? In MLP, are they before the final layer? And how do authors concatenate these features? These details are important to understand final architecture.

How was parameter optimization accomplished? Architectural details, i.e., the number of layers and nodes, are missing. What was the computational overhead for training these models?

It is difficult to understand the discrepancy of features between CNN with clinical features and CNN without clinical features. Maybe it is because model architecture is not well defined. For the moment, it seems like CNN was trained independently, even in the concatenated version of the model. How can you explain the discrepancy between the activation maps of these two models?

Important features were identified using logistic regression. I do not observe the link presenting these features as important features when the model was built using MLP instead. Could you verify that the important or top features MLP (using explanation methods) uses for prediction are the same as those inferred by the logistic regression?

The imbalance issue was tackled using a weighted sampling approach. This approach needs to be detailed in the main text. And how were train, val, and test partitions built in view of the distribution of minority and majority classes? Did the author verify other approaches that can help resolve this issue?

The code to reproduce the model is missing.

Discussion regarding implementation in a clinical setting would be informative. How feasible is the model's deployment in a clinic? Maybe you can further elaborate on prospective clinical trial which was mentioned in line # 363.

Reviewer #3 (Recommendations for the authors):

The study is well designed as the Materials and methods were convincing. Results are supporting the Aims. Further studies will be important for establishing the Criteria.

The challenging issue is to keep reporting the effectiveness of this predictive procedure and publish it with LBR.
