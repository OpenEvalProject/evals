# Peer review - Round 1

Editors:
- Thomas Yeo, National University of Singapore Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64058.sa1](https://doi.org/10.7554/eLife.64058.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this work, Feilong and colleagues investigated the degree to which the strength of functional connectivity is predictive of general intelligence, and the degree to which that predictive power is improved using hyperalignment procedures. More specifically, the authors showed a two-fold increase in variance explained in general intelligence when using fine-grained hyperaligned connectivity compared with coarse-grained hyperaligned connectivity. This is a very clearly written paper that presents an important result, which has the potential of great impact on the field of behavioral prediction.

Decision letter after peer review:

Thank you for submitting your article "The neural basis of intelligence in fine-grained cortical topographies" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Floris de Lange as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Janine Diane Bijsterbosch (Reviewer #2); Evan Gordon (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this work, Feilong and colleagues use the Human Connectome Project fMRI data to investigate the degree to which the strength of functional connectivity is predictive of general intelligence, and the degree to which that predictive power is improved using the hyperalignment procedures their lab has developed. More specifically, the authors predict general intelligence using either coarse-grained functional connectivity (based on 360 ROIs) or fine-grained functional connectivity (vertex-wise) after hyperalignment. The results show a two-fold increase in variance explained in general intelligence between coarse-grained and fine-grained connectivity. This is a very clearly-written paper that presents an important result, which has the potential of great impact on the field of behavioral prediction. However, the reviewers and editors do have some significant concerns with the predictive modeling presented in this work.

Essential revisions:

1) A major contribution of this study is the massive improvement in prediction performance using connectivity hyperalignment and fine-grained functional connectivity. As such it is important that code for this study be made publicly available, so that other researchers can test and replicate the authors' analyses under new conditions and datasets. Our understanding is that the connectivity hyperalignment code from the previous study (Guntupalli et al., 2018) is available in PyMVPA. However, our experience is that the code is not easy to use. As such, we believe it is important that the code specific to this study be made publicly available. More specifically, code utilized in this study to apply the existing connectivity hyperalignment code to the HCP dataset should be made available. Furthermore, code for computing fine-grained functional connectivity together with PCA+ridge regression and nested cross-validation should also be made available.

2) With regards to the leave-one-family-out nested cross-validation procedure, previous studies (e.g., Varoquaux et al., 2017) have suggested a single round of cross-validation can be sensitive to the particular split of the data. A more robust procedure would be to perform 10-fold nested cross-validation procedure 50 times. The prediction performance is then averaged across the 50 x 10 = 500 folds. In the case of the HCP data, care should be taken to handle family structure, i.e., within a single 10-fold nested cross-validation procedure, a family should not be split across the 10 folds. We believe that such a procedure is especially important for this study because the major result here is the huge improvement in prediction performance.

3) The authors should clarify what hyperparameters were tuned in their nested cross-validation. Our understanding is that the authors tune the number of PCA components and ridge regularization parameter. However, hyperalignment has a few hyperparameters as well. Did the authors use the exact same hyperalignment parameters as their previous studies? If so, this should be clearly stated in this study. If different hyperalignment parameters were used, then these hyperalignment hyperparameters should also be tuned within the nested cross-validation framework.

4) The residuals of fine-grained connectivity profiles were obtained after subtracting coarse-grain connectivity. Why was subtraction used here, rather than regressing out (i.e., orthogonalizing with respect to) the coarse-grained connectivity?

5) The authors have generally done a good job controlling for motion-related confounds, which can be a serious issue in the HCP data. In fact, Siegel et al., 2016, demonstrated that many behavioral measures, including intelligence, appeared to be spuriously related to motion effects. This is a particular concern for predictive modeling of the type done in the current work, as it is never clear when predictions are being made based on real aspects of the data vs. when predictions are being made based on intelligence-correlated motion artifact. However, the authors did not "scrub" their data (completely remove high-motion frames), as Siegel et al. did. This could be an issue, as Siegel et al. appeared to show that scrubbing by itself could remove a good portion of spurious behavioral covariance, and Ciric et al., 2017, showed that scrubbing removes different portions of the motion-related artifact than nuisance regression of the type performed by the authors does. Have the authors tested whether their strong FC-behavior predictive power survives more stringent removal of motion frames?

6) Glasser et al., 2016, showed that machine learning approaches could generate individual-specific versions of their parcellation in HCP data that were substantially variable across subjects (even after MSM alignment). This is, of course, a different approach to hyperalignment, at the parcel level rather than the fine-grained vertex level. Have the authors considered testing whether hyperalignment results in better predictive power than such individualized parcel estimates?

7) How does the bootstrapping handle the family structure in the data? If family structure is not taken into account, the authors should justify why that is the case.

8) The Materials and methods states that a linear regression model was used to control for area size in dissimilarity estimates. It would be useful to provide more details here please? For example, is the model fit across subjects or across regions within subject?

9) Some more details about the implementation of permutation testing of the model would be helpful. For example, was each model fully re-trained in each permutation, including the parameter optimization?

10) The fine-grained functional connectivity has richer features than coarse-grained, leading to higher dimensionality in the PCA step (Figure 3—figure supplement 5). We wonder if this might contribute to improved prediction accuracy. Related to this, it appears that there may also be a relationship between PCA dimensionality and regularization parameter, such that more regularization may be needed when more PCs are used in the model. It would be interesting to test the effect of fixing the PCA dimensionality (and perhaps also the regularization) across all models to control model complexity.
