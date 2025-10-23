# Peer review - Round 1

Editors:
- Timothy Verstynen, Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59430.sa1](https://doi.org/10.7554/eLife.59430.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

There was unanimous agreement that this method has strong potential to be a new "workhorse" tool in human neuroimaging that could substantially advance our ability to measure brain structures that are largely overlooked due to problems with segmentation.

Decision letter after peer review:

Thank you for submitting your article "Multi-contrast Anatomical Subcortical Structures Parcellation" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Timothy Verstynen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Wolf-Julian Neumann (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

In this study, Bazin and colleagues propose a novel segmentation algorithm for parcelling subcortical regions of the human brain that was developed from multiple MRI measures derived from the M2RAGEME sequence acquired on a 7T MRI system. The key advancement of this approach is a reliable segmentation of more subcortical areas (17 regions) in native space than what is possible with currently available methods. The authors validate their algorithm by comparing against age-related measures.

This manuscript was reviewed by three experts in the field, who found that this method has strong potential to be a new "workhorse" tool in human neuroimaging that could substantially advance our ability to measure brain structures that are largely overlooked due to problems with segmentation. The main criticisms of the work are largely centered on how the method is evaluated and implemented, rather than fundamental concerns with the validity of the method itself.

Essential revisions:

1) Benchmarks.

All three reviewers had concerns about the nature of the tests for the new method.

Reviewer 1 was particularly concerned that, while a critical advancement of this method is the ability to segment many more regions than previous subcortical atlases, there are still many regions that overlap with existing segmentation tools. Knowing how the reliability of this new approach compares to previous automatic segmentation methods is crucial in being able to know how to trust the overall reliability of the method. The authors should make a direct benchmark against previous methods where they have overlap.

Reviewer 2 thought that the work would certainly benefit from an additional step of out-of-center / out-of-cohort validation analysis. Though they had no serious concern that performance would be unsatisfactory, it would still highlight the extensibility of the method.

Reviewer 3 shared a similar concern, pointing out that automatized methods are usually sensitive to the number of subjects used to build the parcellation, with results from a bigger training cohort being potentially more robust and generalizable. One of the strongest points of the automated method presented in this paper is the adoption of a Bayesian approach, which usually works efficiently for small sample sizes and allows to update previous results when new data comes. Still, it could be highly illustrative to show the performance of the current method depending on the initial training size. From the same set of delineations of the 105 subjects used to test the age bias, what if the authors show the predicted performance from generating the priors on a training set varying its size?

2) Aging analysis.

All three reviewers were confused as to the purpose for and implementation of the aging analysis included in the paper.

Reviewer 1 said that the analysis of the aging effects on the segmentations seemed oddly out of place. It wasn't clear if this is being used to vet the effectiveness of the algorithm (i.e., its ability to pick up on patterns of age-related changes) or the limitations of the algorithm (i.e., the segmentation effectiveness decreases in populations with lower across-voxel contrast). What exactly is the goal with this analysis? Also, why is it limited to only a subset of the regions output from the algorithm?

Reviewer 2 thought that the most important limitation, as acknowledged by the authors, is the bias from anatomical variation through age or disease. The algorithm is shown to be affected by age and most certainly will be affected by contrast and size changes in neurodegenerative disorders. Broader benchmark tests, as proposed above, would likely address this concern.

Reviewer 3 pointed out that, from Figure 4, it is clear how estimated Dice coefficients decrease with age. As it is well noted by the authors, this is likely caused due to the fact that the priors were built from 10 subjects that had an average age of 24.4 years and thus, the highest predicted performance rates are reflected for subjects whose age range (18-40) lies around this average prior age. The authors mentioned in the paper that they plan on modelling the effects of age in the priors in future work. However, they could already address this question in the current work. Since the data used to test this age bias has already been manually delineated, what if the authors generate new priors for this set of delineations, including subjects from all ages, and test whether the predicted Dice coefficients still depend on age, in the same way as was done in Figure 4?

3) Clarity of the algorithm.

Reviewers 1 and 3 had concerns about details of the algorithm itself.

Reviewer 1 thought that, because of the difficulty of the parcellation problem, the algorithm being used is quite complex. The authors do a good job showing the output of each stage of the process (Figure 7 and Figure 8), but it would substantially help general readers to have a schematic of the logic of the algorithm itself.

Reviewer 3 pointed out that it is unclear what is the value for the scale parameter δ that appears in the priors? Is that a free parameter? If so, do results change when this parameter varies? This seems to be a critical aspect of the process (at least insofar as the precision of the results).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Multi-contrast Anatomical Subcortical Structures Parcellation" for consideration by eLife. Your revised article has been reviewed by three peer reviewers, including Timothy Verstynen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Wolf-Julian Neumann (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The reviewers felt that the revised manuscript is much stronger and focused. There remains only a minor point raised by reviewer #2 that we ask you address.

Essential revisions:

Reviewer #2 (see below) would like to see a more elaborate comparison of the STN segmentation to previous recent methods, given that these sorts of subcortical parcellation methods are likely to be of interest to DBS researchers. While a comparison to the Ewert method (or similar) would be nice, a brief discussion of a subjective comparison of these results would be sufficient to address this concern.

Reviewer #1:

The authors have adequately addressed all of my concerns. Well done.

Reviewer #2:

This is a revised manuscript on a 7T based segmentation approach. My main concern in the primary submission was that at this point the complexity of the data acquisition in combination with the computational approach makes it relatively niche. Other concerns regarded additional validation runs and aging, which the authors have now provided. My feeling is that the authors have made an effort to address the major points raised in the first revision.

There is one minor point that still remains puzzling for me. The fact that the STN is delineated so poorly, when compared to other structures. Given its use as a target in hundreds of thousands of patients for deep brain stimulation, automatized STN segmentation has been validated. The authors cited Ewert et al., which combines a simple normalization with an atlas in MNI space and reached similar and better performance when compared to the presented results here. I would have liked to see the results from this paper reproduced as a comparison here, but if the authors decide not to, I would at least like to invite the authors to discuss why the STN is troublesome for the algorithm and how this could affect use for surgical planning in the future, when 7T becomes available in clinics.

Additionally, I found this a little strange: Figure 3 caption: compared to the most expert of the two human raters.

Reviewer #3:

The authors have addressed all the concerns that I had in the previous version of the manuscript. Important changes in this revision included a benchmark against existing automated parcellation tools, a validation analysis using a test-retest sample from the Human Connectome Project and a thorough examination of training sample size and age biases. All of these changes have significantly increased the quality of the paper and more importantly, provided more clarity and evidence for the benefits of the proposed algorithm for subcortical parcellation. As a consequence, I am more than pleased to recommend the current version of the manuscript for publication.
