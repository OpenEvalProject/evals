# Peer review - Round 1

Editors:
- Moritz Helmstaedter, Max Planck Institute for Brain Research Germany

Reviewers:
- Franco Pestilli, Indiana University United States
- Jason P Lerch, The Hospital for Sick Children Canada

## Review text

DOI: [10.7554/eLife.44443.024](https://doi.org/10.7554/eLife.44443.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Inter-individual differences in human brain structure and morphometry link to variation in demographics and behavior" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen Moritz Helmstaedter as the Reviewing Editor and Richard Ivry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Franco Pestilli (Reviewer #1) and Jason P Lerch (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers value the importance of the work and see significance in the finding that structural features, not just functional ones, can show high correlation to behavioral phenotypes in humans.

Essential revisions:

1) Additional analyses to solidify the (possibly causal) relation between structural and functional determinants are required as suggested by the reviewers:

a) Including all functional and structural modalities to begin with would at least provide a way of testing their relative contribution to behavioral prediction within the same analytic framework, and/or as suggested (reviewer 2)

b) To strengthen the findings some level of replication from an additional dataset would be helpful (e.g. UK BioBank for older subjects, etc.). (reviewer 3)

c) It would be valuable to try and validate the multivariate imaging components that are seen to predict behavior. For example, are the components of each signature more spatially nested within the canonical brain networks than one would expect by chance? (reviewer 2)

2) Careful revision of the manuscript to enhance clarity and methodological detail (see associated comments by all reviewers below). This especially applies to the figures, which were considered improvable. Please make use of the generous space offering at eLife, include more detailed methodological figures where possible (also the supplementary figure can be integrated into the main paper). An illustration of all relevant structural components could help, as well (beyond component number 6).

3) The requests for methodological explanations/clarifications are considered essential for a successful revision. In particular with respect to:

a) Different pre-processing compared to Smith et al., and linked-ICA, reviewer 1);

b) Publication of code on github/gitlab and usability of code (reviewer 1): code and methods need to be available for evaluation, replicability, and reuse;

c) Scale, image QA, motion effects, choice of anatomical features (reviewer 2);

d) Issues of causality and colinearity (reviewer 3, but also raised by the other reviewers).

We are providing the reviewers' full set of comments below for your consideration. However, in line with eLife’s consolidated approach, we emphasize that the above requests are the ones we deem essential and ask that you provide a letter detailing your response when you submit the revision. The comments below can be treated as recommendations and a point-by-point response is not required.

Reviewer #1:

This is a nice paper following up on previous work by Smith et al., 2015. The results replicate and extend the previously published ones. The manuscript is well written and succinct.

Care should be taken when revising the text as several sections seem unpolished. Yet, I think that several sections of the Materials and methods can improve with added details of the methods. Figure 1 especially should be improved (visually it does not seem to be ready for publication) but also it should be clarified how the dimensionality of the data for each step in the algorithm. It would have to accompany the figure with equations in the Materials and methods describing the mathematical operations and code implementing the model. See below.

A more thorough description of the Linked-ICA is necessary to let this article stand on its own feet. The Materials and methods should provide additional details on the ICA approach, brain and behavioral preprocessing. The detailed description of the preprocessing steps for extractive the behavioral variable should clearly state whether and how the data preprocessing different from Smith et al. If differences existed the authors should clarify why they were necessary and how their choice affected the final result.

In addition, I believe Smith preprocessed/standardized the behavioral and phenotypical data in a way that is not described in the current manuscript. is this correct? Why was the preprocessing performed differently?

Code implementing the analysis should be made readily available. The code should be well documented and allow the readers to reproduce that analyses. The code should help a reader perform the following:

Extract the features as used in the current article starting from each data modality in the HCP release.

Extract and preprocess the behavioral and phenotypical variables given the files that can be obtained by the HCP consortium.

Built the matrices of features as needed for the Linked-ICA modeling.

Perform the additional analysis given the model results.

Reproduce the major plots in the article.

This is especially important in this case as this dataset is public and readers are likely to attempt going beyond the current work. Ideally, the code should be deposited on a platform to allow version tracking and accompanied by a comprehensive readme file describing license and step by step how-to. Github.com seems to be a proper platform for this.

What were the criteria for exclusion for subjects? This is not clearly reported in the Materials and methods.

A few sentences link the following were vague and should be clarified:

"The straight-forward individual linear correlation analysis against the behavioral/demographic measures separately instead affords simple interpretation, albeit possibly being over-conservative given the chosen significance level."

The claim that the current structural mode and Smith functional mode are “strongly correlated” seems an overstatement (r value is only 0.46) I would say that is moderate. Still interesting.

The introductory sentences about phrenology seem out of context unless it is clarified how phrenology fits with the current work.

Reviewer #2:

There are several strengths to the work presented. The unbiased modeling of multiple anatomical variables as predictors of multidimensional measures of behavior is valuable, and represents an important complement to the traditional (but likely less biological valid) approach of mass univariate tests of one structural feature against one behavioral measure. A downside of the many-many multivariate analyses is that they can be hard to map back into a lower dimensional space that is easier for us to interpret – but the authors do an excellent job of "translating" the brain-behavior relationships that they find into text and figures that can be more concretely interpreted. The authors also conduct several useful sensitivity analyses which help readers better understand the conditions under which their core findings hold. The authors also quantitatively assess the interrelationship between structural component #6 in their work, and the previously reported multivariate functional imaging component reported in the HCP by Smith et al.

The main potential for novelty and impact of this manuscript (above and beyond the earlier functional imaging study by Smith et al.) rested very heavily on the questions of relative predictive capacity and directional interdependent between multivariate structural (this paper) and functional (Smith et al) predictors of behavior. However, these questions are fundamentally hard to address meaningfully in the absence of longitudinal multimodal data – which would be the ideal observational study design in humans. Appreciate that the authors used components from the Smith paper in causal analyses to conclude in favor of a structure-to-function model (vs. function-to-structure), but I am not confident that this analytic approach can carry the weight being placed upon it. A caveat here however is that I am not qualified to provide an expert statistical review of the Hyvarinen and Smith paper presenting the method used for directional inference. My point is rather a simpler one about limits around the certainty with which one can infer causal processes from cross-sectional data. I wondered if including all functional and structural modalities to begin with would at least provide a way of testing their relative contribution to behavioral prediction within the same analytic framework – even though this would only go some way to getting at the relative predictive utility of structural vs. functional metrics, while still leaving directionality untouched.

I also through the following issues would benefit from further consideration:

The behavioral variables include both raw and age adjusted version for many scales, but age is already a predictor itself. I think it would be good to provide further details around the rationale for selecting which types of scale go in to the multivariate behavior/demographic matrices to be predicted.

It would be good to include more details around image QA and exploration of motion as potential confound.

I appreciate that ratio of variables to observations is an issue, but these analyses would really benefit from a discovery-replication design.

The authors did drop JD to test if structural prediction still there when excluding information about "morphological variation" – but (i) I see this as a specific instance of the more general need to assess relative contribution of different anatomical metrics to different behavioral dimensions., and (ii) opening up the important question of which anatomical features one considers in the first place (for example, no folding or sulfa depth information despite this being provided by FreeSurfer).

It would be valuable to try and validate the multivariate imaging components that are seen to predict behavior. For example, are the components of each signature more spatially nested within the canonical brain networks than one would expect by chance?

Reviewer #3:

This is a very interesting article recovering brain-behaviour relations from brain structure in ways that map onto previous findings in brain function. These results are exciting, providing evidence of brain structure influencing (or being influenced by) function. My core reading of the paper leads me to two conclusions:

- I buy that brain structure can predict function – the authors provide solid evidence. To strengthen the findings I would like to see some level of replication from an additional dataset (e.g. UK BioBank for older subjects, etc.).

- I am less convinced of the mediation between structure and function, and especially the claimed link that methodological/misalignment issues might be the cause. That argument could be dropped without weakening the paper; if the authors feel strongly about this point then they need to make a better case.

More detailed comments:

- I don't understand footnotes 1 and 2. The authors chose an FDR threshold of q < 2.2x10e-4? That seems arbitrary? Or does a q < 0.05 correspond to an uncorrected p<2.2x10e4?

- It is curious that VBM would explain much more variation in component 6 than thickness or surface area. It is not easy to determine why from the figure, though part of the explanation could be that subcortical regions play a strong role.

- It is even more curious that JD explains so much less in comp 6 than VBM. What type of VBM was conducted – were the tissue densities modulated by the Jacobians?

- Components 1 and 2 have a strong gender contribution and show significant VBM contributions. How were variations in overall brain volume accounted for, if at all?

- The discussion in the fourth paragraph of the Results confuses me. The authors appear to imply that only the Jacobian determinant measures uniquely morphometric differences; how is it that thickness, surface area, and VBM do not reflect morphometric differences? And aren't these results more of an argument that non-linear registrations in this study were either not tuned very well or that alignment of ideosyncratic cortical features is a hard problem?

- The section on linking the structural and functional analyses is problematic. Given that they correlate using the linear model will obviously run into issues of colinearity. This can be seen by the bivariate nature of the results – covaring structure on function or function on structure gives a similar change in r and removes multiple findings. The secondary argument that the reason why covarying structure removes so many of the function findings – due to misalignment or similar methodological issues – is thus suspect and needs to be expanded on.

- I would like the authors to expand on the advantages of linear models over CCA or other multivariate analyses. In that vein, the Smith et al. paper often referred to in this manuscript also tested structural associations and found them much less relevant than rsfMRI – why the results are different should be discussed.
