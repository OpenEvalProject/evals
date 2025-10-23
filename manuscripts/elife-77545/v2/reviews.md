# Peer review - Round 1

Editors:
- Saad Jbabdi, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77545.sa0](https://doi.org/10.7554/eLife.77545.sa0)

This study uses a large dataset on alcohol misuse in adolescents that have been followed up for several years. MRI data are used to test whether the structure and connectivity of the brains of adolescents can predict their alcohol misuse later in their early twenties. The results show that binge drinking can be predicted out of multiple brain phenotypes with good accuracy, even after controlling for many confounding variables. This study can be impactful as it suggests a re-evaluation of studies of the effect of alcohol on the adolescent brain.


---

# Peer review - Round 1

Editors:
- Saad Jbabdi, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77545.sa1](https://doi.org/10.7554/eLife.77545.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Structural differences in adolescent brains can predict alcohol misuse" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please pay particular attention to the below points raised by one of the reviewers, which I believe to be important.

1) Provide a more convincing explanation for the poor results of the leave-one-site-out predictions.

2) Model longitudinal changes using pre-onset data.

Reviewer #1 (Recommendations for the authors):

This study uses a nice longitudinal dataset and performs relatively thorough methodological comparisons. I also appreciate the systematic literature review presented in the introduction. The discussion of confound control is interesting and it is great that a leave-one-site-out test was included. However, the prediction accuracy drops in these important leave-one-site-out analyses, which should be assessed and discussed further. Furthermore, I think there is a missed opportunity to test longitudinal prediction using only pre-onset individuals to gain clearer causal insights. Please find specific comments below, approximately in order of importance.

1. The leave-one-site-out results fail to achieve significant prediction accuracy for any of the phenotypes. This reveals a lack of cross-site generalizability of all results in this work. The authors discuss that this variance could be caused by distributed sample sizes across sites resulting in uneven folds or site-specific variance. It should be possible to test these hypotheses by looking at the relative performance across CV folds. The site-specific variance hypothesis may be likely because for the other results confounds are addressed using oversampling (i.e., sampling with replacement) which creates a large sample with lower variance than a random sample of the same size. This is an important null finding that may have important implications, so I do not think that it is cause for rejection. However, it is a key element of this paper and I think it should be assessed further and discussed more widely in the abstract and conclusion.

2. The authors state that "83.3% of subjects reported having no or just one binge drinking experience until age 14". To gain clearer insights into the causality, I recommend repeating the MRIage14 → AAMage22 prediction using only these 83% of subjects.

3. The feature importance results for brain regions are quite inconsistent across time points. As such, the study doesn't really address one of the main challenges with previous work discussed in the introduction: "brain regions reported were not consistent between these studies either and do not tell a coherent story". This would be worth looking into further, for example by looking at other indices of feature importance such as permutation-based measures and/or investigating the stability of feature importance across bootstrapped CV folds.

Reviewer #2 (Recommendations for the authors):

I only have a few suggestions.

1) The abstract should be more specific, pointing out the best-predicted measure(binge) and the conclusion of methods, like the conclusion did. Also, the introduction should include more recent prediction studies using IMAGEN.

2) The structure of brain mapping needs clarification. We would like to see the most contributing structural measures（thickness, volume, intensity）separately mapping, how about the accuracy using each type alone? Could you show the brain mapping of each type of 3 sMRI features respectively? Figure 7 is too general.

3) How about the availability of data and code?
