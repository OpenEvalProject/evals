# Author response - Round 1

Authors:
- Gaetan De Waele ([ORCID: 0000-0003-0367-9699](https://orcid.org/0000-0003-0367-9699))
- Gerben Menschaert
- Willem Waegeman

## Response text

DOI: [10.7554/eLife.93242.4.sa2](https://doi.org/10.7554/eLife.93242.4.sa2)

The following is the authors’ response to the previous reviews.

Reviewer #1:

Section 4.3 ("expert baseline model"): the authors need to explain how the probabilities defined as baselines were exactly used to predict individual patient susceptible profiles.

We have added a more detailed and mathematically formal explanation of the “simulated expert’s best guess” in Section 4.3.

This section now reads:

“More formally, considering all training spectra as Strain, all training labels corresponding to one drug j and species t are gathered: ysubset j,t={yij∣si∈Strain ∧species⁡(si)=t}. The "simulated expert's best guess" predicted probability for any spectrum si and drug dj, then, corresponds to, the fraction of positive labels in their corresponding training label set Ysubset j,t: ysubset j,t={yij∣si∈Strain ∧species⁡(si)=t}”

Authors should explain in more detail how a ROC curve is generated from a single spectrum (i.e., per patient) and then average across spectra. I have an idea of how it's done but I am not completely sure.

We have added a more detailed explanation in Section 3.2. It reads:

To compute the (per-patient average) ROC-AUC, for any spectrum/patient, all observed drug resistance labels and their corresponding predictions are gathered. Then, the patient-specific ROC-AUC is computed on that subset of labels and predictions. Finally, all ROC-AUCs per patient are averaged to a "spectrum-macro" ROC-AUC.

In addition, our description under Supplementary Figure 8 (showing the ROC curve) provides additional clarification:

Note that this ROC curve is not a traditional ROC curve constructed from one single label set and one corresponding prediction set. Rather, it is constructed from spectrum-macro metrics as follows: for any possible threshold value, binarize all predictions. Then, for every spectrum/patient independently, compute the sensitivity and specificity for the subset of labels corresponding to that spectrum/patient. Finally, those sensititivies and specificities are averaged across patients to obtain one point on above ROC curve.

Section 3.2 & reply # 1: can the authors compute and apply the Youden cutoff that gives max precision-sensitivity for each ROC curve? In that way the authors could report those values.

We have computed this cut-off on the curve shown in Supplementary Figure 8. The Figure now shows the sensitivity and specificity at the Youden cutoff in addition to the ROC. We have chosen only to report these values for this model as we did not want to inflate our manuscript with additional metrics (especially since the ROC-AUC already captures sensitivities and specificities). We do, however, see the value of adding this once, so that biologists have an indication of what kind of values to expect for these metrics.

Related to reply #5: assuming that different classifiers are trained in the same data, with the same number of replicates, could authors use the DeLong test compare ROC curves? If not, please explain why.

We thank the reviewer for bringing our attention to the DeLong’s test. It does indeed seem true that this test is appropriate for comparing two ROC-AUCs using the same ground truth values.

We have chosen not to use this test for one conceptual and one practical reason:

(1) Our point still stands that in machine learning one chooses the test set, and hence one can artificially increase statistical power by simply allocating a larger fraction of the data to test.

(2) DeLong’s test is defined for single AUCs (i.e. to compare two lists of predictions against one list of ground truths), but here we report the spectrum/patient-macro ROC-AUC. It is not clear how to adjust the test to macro-evaluated AUCs. One option may be to apply the test per patient ROC curve, and perform multiple testing correction, but then we are not comparing models, but models per patient. In addition, the number of labels/predictions per patient is prohibitively small for statistical power.

Reviewer #2 (Recommendations For The Authors):

After revision, all issues were been resolved.
