# Peer review - Round 1

Editors:
- Andre F Marquand, https://ror.org/016xsfp80 Radboud University Nijmegen Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87992.sa0](https://doi.org/10.7554/eLife.87992.sa0)

This important study provides evidence for associations between transdiagnostic psychiatric symptom domains and brain structure and function in a large cohort. The evidence supporting the findings is solid in that brain-behaviour associations are validated in separate subsamples of the data, although out-of-sample accuracies are modest. This study will be of broad interest to researchers interested in the neurobiological basis of mental disorders.


---

# Peer review - Round 1

Editors:
- Andre F Marquand, https://ror.org/016xsfp80 Radboud University Nijmegen Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87992.sa1](https://doi.org/10.7554/eLife.87992.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Multimodal neural correlates of childhood psychopathology" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Roiser as the Senior Editor. Two of the three reviewers have agreed to be named: Eugene Duff (Reviewer 1) and Ted Satterthwaite (Reviewer 2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

This manuscript represents a multifaceted and comprehensive contribution toward the understanding of the link between functional connectivity and latent dimensions of psychopathology. The paper presents an extensive series of analyses integrating multimodal data derived from the ABCD study and results in the estimation and characterisation of multivariate mappings between psychopathology and neurobiology using partial least squares.

There is a consensus amongst the reviewers that this is a relatively well-executed study that provides a contribution suitable for a broad readership. However, the reviewers also highlight several shortcomings that should be addressed before this manuscript can be considered suitable for publication in eLife. The most important of these are:

1) A lack of out-of-sample assessment metrics makes the generalisability and effect sizes of the PLS findings uncertain. We recognise that the authors have used a discovery-replication approach and have re-estimated their multivariate regression model in disjoint subsets of the ABCD sample. However, this is not the same as out-of-sample prediction, which the reviewers feel would yield less biased estimates of generalisability.

2) The reviewers also felt that the authors ought to give attention to the possibility that their findings might be influenced by intrinsic correlations between the neuroimaging data modalities rather than anything specific to the latent component they belong to.

3) Please also provide a more nuanced discussion surrounding the use of the p-factor both from a wider theoretical perspective, accommodating discussion in the field and with particular reference to the presented results. The editors agree with the sentiment expressed by the reviewers that the leading PLS component is not convincingly demonstrated to relate to the p-factor.

4) Finally, the reviewers request that the authors give careful attention to the clarity of exposition of the many analyses conducted, including describing how potential confounding factors such as site, family structure, and ethnicity were accommodated during the modelling procedure. This may include adapting the approaches employed to match best practices as appropriate.

Reviewer #2 (Recommendations for the authors):

Out-of-sample testing: I was surprised that the authors didn't use their split sample to conduct out-of-sample testing or use cross-validation; this would provide a more robust measure of effect size.

Site/family structure: in ABCD these variables are often accounted for via multilevel models / random effects in a mixed effects model to account for the nested structure of the data.

Anatomical features: providing context (and potentially moving volume to the supplement) may facilitate the interpretation of this result for readers.

Ethnicity: the rationale for regressing ethnicity from the data was unclear and may conflict with current best practices. See https://www.nature.com/articles/s41593-022-01218-y

Data quality: for a relevant paper for ABCD, See: https://www.biorxiv.org/content/10.1101/2023.02.28.530498v1

Including the Euler number (https://www.sciencedirect.com/science/article/pii/S1053811917310832) or the manual ratings from the ABCD preprint would mitigate these concerns. For dMRI data I would suggest including a summary measure of in-scanner motion as a covariate.

Reviewer #3 (Recommendations for the authors):

While reading the paper, I noticed that the authors have included a substantial amount of analyses. However, it was not entirely clear to me why certain data were utilized in each analysis. In order to enhance the clarity and comprehension of their work, I recommend the following improvements:

- Provide a concise and explicit description of the data used for each analysis. This will help readers understand the specific datasets employed in each analysis and their relevance to each analytical approach.

- Given that the structural and rsfMRI data were used for the main PLS analysis and the rest for validation, consider providing a more detailed explanation of the rationale behind this choice. Additionally, elucidate how these datasets contribute to the overall findings and conclusions of your study.

- Enhance validation procedures: if I'm correct, all the PLS inferences were done in sample, so I wonder about the transferability of their found results.

Furthermore, to strengthen their argument regarding the relationship between changes in the sensory-to-transmodal axis and behavioral factors, it would be advisable for the authors to directly correlate composite scores reflecting behavior with the gradients. Additionally, if these correlations turn out to be non-significant, it would be interesting for the authors to discuss the possible reasons behind these findings.

Lastly, to address the interpretation concerns for the first latent component, I suggest the following:

- Delve deeper into the observed loadings: Provide a detailed analysis of the specific loadings associated with LC1 and how they relate to impulse control problems over different train-test sets. By exploring the nuances of these loadings, the authors can offer a more precise understanding of the factor's nature and its connection to the broader p-factor construct.

- Acknowledge the ongoing discussion: Recognize the existing discourse within the field regarding the interpretation and utilization of the p-factor. Discuss the differing perspectives and highlight the points of contention, emphasizing the need for further investigation and clarification.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Multimodal neural correlates of childhood psychopathology" for further consideration by eLife. Your revised article has been evaluated by Jonathan Roiser (Senior Editor) and a Reviewing Editor, Andre Marquand.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

We thank the authors for their revised manuscript and their responses to the points raised by the reviewers. Before moving forward with further consideration of this revised submission, we would like to ask the authors to extend the out-of-sample analysis that has been provided and to report this more transparently because this was identified as a critical point by the reviewers in the last submission.

More specifically, it seems that only the replicability of the in-sample and out-of-sample estimates is currently provided (and not the actual out-of-sample predictions) although this is not very clear from the description given (e.g. lines 388-390). Please report the out-of-sample prediction statistics (i.e. corresponding to the in-sample estimates currently shown in Figure 2A). Please also test the significance of these for example using permutation testing and adjust the Discussion section accordingly.

Additionally, please clarify the exact steps taken during the out-of-sample estimation procedure. As noted above, this is currently quite unclear. The standard approach within machine learning would be to keep the training and test sets completely independent, where any normalisation of the features prior to prediction is performed using statistics derived from the training set.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Multimodal neural correlates of childhood psychopathology" for further consideration by eLife. Your revised article has been evaluated by Jonathan Roiser (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The authors have responded satisfactorily to most of the concerns raised by the reviewers. However there is one significant concern that must be addressed before we can consider this suitable for publication in eLife. The focus and narrative of the paper is still nearly entirely based around in-sample statistics, especially the canonical correlations reported in figures 2, 3 and 4 (r ~ 0.35). We feel that this is too optimistic and does not accurately reflect the true magnitude of the effects reported, even in view of the discovery-replication conducted. This is because the out-of-sample canonical correlations now (briefly) included in the manuscript are of a much smaller magnitude (r=0.03 – 0.07), indicating a very small amount of explained variance.

We do not consider the low explained variance to be problematic per se, and indeed it is in line with current standards in the literature (e.g. https://www.nature.com/articles/s41586-022-04492-9), but it should be transparently and accurately reported. In general, given the well-established high propensity of CCA/PLS to overfit thus, resulting in quite brittle models especially where large number of predictor variables are included, we consider that in-sample canonical correlations are not appropriate indicators of model performance in neuroimaging and we should rely on out-of-sample statistics instead (see e.g. https://pubmed.ncbi.nlm.nih.gov/32224000/ for a discussion on this). It is perhaps also useful to note that this view is shared by the reviewers and the reviewing editor who assessed this manuscript.

To address this, please: (i) replace the in-sample statistics reported in all the relevant figures with out-of-sample statistics (or simply add the out of sample statistics to the figures), (ii) report the out-of-sample canonical correlations in the abstract, and (iii) adjust narrative of the paper (and where appropriate downstream analyses) accordingly to focus principally on the out-of-sample statistics.
