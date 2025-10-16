# Peer review - Round 1

Editors:
- Sanmi Koyejo, University of Illinois at Urbana-Champaign United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62376.sa1](https://doi.org/10.7554/eLife.62376.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript evaluates and extends a method for estimating levels of alertness in fMRI. The primary contributions include alertness prediction using a subset of voxels and the alertness measure's usage as a regressor in task fMRI. Reducing the required spatial map from the whole brain to a thresholded set of voxels is an interesting methodological contribution. Further, results suggest that this approach can help address alertness as a possible confound in task fMRI analyses.

Decision letter after peer review:

Thank you for submitting your article "fMRI-based detection of alertness predicts behavioral response variability" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Christian Büchel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript evaluates multimodal fMRI-EEG data to estimate and assess attention in the fMRI signal based on its correlation with the EEG signal. The study of attention using fMRI is a well-studied topic, including somatosensory, visual, and auditory paradigms. Still, this study adds to the literature by using multimodal data to create the fMRI model. The discussed method follows prior work on the same approach and explores using a subset of voxels and applications as an fMRI signal regressor.

Essential revisions:

1. Conceptually, improved methods for addressing alertness confounds are a valuable contribution. The evaluation of the alertness index via the auditory task is a useful contribution. In terms of specific contributions, the reduction in the required spatial map, from the whole brain to a thresholded set of voxels, is an interesting methodological contribution. However, perhaps the main methodological contribution can be achieved more effectively using a direct approach, e.g., using a lasso model to predict the EEG alertness score using the fMRI time series. The lasso is considered a relatively standard statistical model, so it is not clear that the slight reduction in complexity is worth the loss in performance. At the very least, the authors should compare this approach to the presented thresholded correlation.

2. Reproducibility should be described more clearly. Reviewers recommend using cross-validation, dividing the data into 2 sets. The models can be built separately on each set, then compared. Also, one set's model can be used to evaluate prediction in the other set, and thus calculate sensitivity and specificity for this model. This would be complementary to the permutation testing already performed, as permutation testing is somewhat limited because these signals appear highly periodic (e.g., Figure 2) and thus can likely mismatch easily.

3. For the rsfMRI, participants were instructed to stay awake. Was this evaluated? There is a concern that participants might fall asleep during the 24.5m duration of the scan.

4. The auditory fMRI task made use of different tones. How were these tones delivered? Where earbuds used?

5. In the processing, it is stated that motion coregistration has been performed. Was there a quality check for excessive movement? When a participant moves more than the voxel size, the data are often discarded.

6. While testing hit/miss is clear, testing reaction times are limited to faster or slower than a single time (565 ms). As the study describes this method's use on an individual basis, consider intraindividual methods previously published, e.g., those from Thompson et al. 2013 (Citation 19), which includes separation by individual means, and also a separation of individuals into fast and slow groups.

7. A reaction time threshold of 565ms was used, but it remains unclear what the reason is for splitting the trails in an equal number of fast and slow trails. A reaction time of 565ms is still fast, and there can be a lot of variation between the fast and slow trails. A non-response was recorded if there was no button press within 5s. Therefore, perhaps fast can also be stated as below 2.5s and slow above 2.5s. The reference to Lim and Dinges (2008) indeed used a threshold at 0.5s but in a different setting.

8. A sample of 14 participants was investigated in this study. Would this sample be sufficient to prove the point of predicting fMRI results? There is no apriori sample size calculation, and therefore, it remains unknown if the data are sufficient to prove the point. In fMRI, usually larger samples up to 80 and more used to reduce variability/noise in the measurement.

9. The authors seem to indicate that the alertness metric could be used in resting-state fMRI data. Can't this be tested on either the authors' data or a publically available database? All that is needed is data with an index of alertness (such as eye-tracking) or even self-report of alertness/sleepiness.

10. Figure 5B shows positive (red) correspondence in a ventricle. This makes one wonder if this method is picking up on the EEG-linked CSF fluctuations reported elsewhere, e.g., Kiviniemi, V. et al. (2016). J Cereb Blood Flow Metab 36(6): 1033-1045. Can the authors discuss this?

11. What software was used for the processing of the data? Is the code available online? Please share via GitHub. Also, it remains unclear which statistical software was used for the statistical analyses.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "fMRI-based detection of alertness predicts behavioral response variability" for consideration by eLife. Your article has been overseen by a Reviewing Editor and Christian Büchel as the Senior Editor.

The Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewing editor believes that this manuscript is much improved and has addressed the conceptual and scientific concerns raised in the first round of reviews. While concerns about the sample size remain, the reviewing editor believes that this manuscript can be accepted as the contributions are primarily methodological.

The reviewing editor requests that the authors address the sample size limitations more directly in the main manuscript. In addition to the justification given in the response, consider adding language to the manuscript that clarifies that the findings may not generalize to the population from which they have sampled. Authors should also consider mentioning that their small sample likely overestimates the effect size of their results.
