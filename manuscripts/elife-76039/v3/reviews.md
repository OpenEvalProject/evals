# Peer review - Round 1

Editors:
- Jun Ding, https://ror.org/00f54p054 Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76039.sa0](https://doi.org/10.7554/eLife.76039.sa0)

This manuscript addresses the cellular and dendritic physiology of cholinergic interneurons in the striatum. The authors use a creative integration of electrophysiology and optical methods to investigate this distinctive cell type, which is critically important at the intersection of motivated behavior and disease. They uncover a mechanism through which two separate active conductances – the hyperpolarization-activated h-current (HCN) and the persistent sodium current (NaP) – act in concert to selectively boost synaptic input from the thalamus onto proximal dendrites of cholinergic interneurons.


---

# Peer review - Round 1

Editors:
- Jun Ding, https://ror.org/00f54p054 Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76039.sa1](https://doi.org/10.7554/eLife.76039.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Non-uniform distribution of dendritic nonlinearities differentially engages thalamostriatal and corticostriatal inputs onto cholinergic interneurons" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Scott Owen (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1, The use of ChR2 to induce the ZAP protocol. This is a central part of the story. The inactivation properties of the opsin should be discussed and it should even be incorporated in the model and tested in a few control experiments.

2. There is a disconnect between the first 4 figures and the last two figures. Regarding the primate data, the link to the slice work should be strengthened.

3. New physiology or modeling should be done to explain why cortical inputs to distal dendrites are not boosted as they pass through the proximal dendrite (Figure 5).

4. Both reviewers made detailed suggestions on additional edits and discussion points. Please take a close look at the reviewers' comments below, and incorporate these suggestions in the revision.

Reviewer #1 (Recommendations for the authors):

The authors should be congratulated on an important and well executed study. This scope of this manuscript seems to be a good fit for the readership at eLife, provided the concerns raised in the public section are adequately addressed.

To address the first major concern raised in public comments, regarding why boosting of proximal dendrites does not affect input from distal dendrites, additional text should be added to the Results and Discussion sections. Specifically, the authors should address whether this is a valid concern or a possible misconception, and how this can be resolved. This is an exceptionally important point, because without an adequate explanation, it is hard to understand how Figures 5 and 6 belong in the same manuscript as Figures 1-4.

To address the second major concern, regarding potential over-fitting of the model, the manuscript would benefit from additional tables and analysis. This description should include tables describing all fixed and free parameters that are fed into the model in Equations 1-4, and how fixed parameters were determined. In addition, a figure illustrating graphically how these parameters contribute to the plot fits would be invaluable. Which parameters contribute to saturation of phase drift at high and low frequencies? What sets the slope of phase drift? How many parameters had to be changed to allow a single model to fit both the simple, monotonically rising curve shape in Figure 3, and the very complex, multi-phasic curve in Figure 2B. In particular, how do these parameters interact with one another and how do those interactions affect the confidence with which results can be interpreted? i.e. how do we know that there are not other very different solutions to this model that provide equivalently good fits but point to very different physiological interpretations? A handful of well-chosen plots, following a format of the curves in Figures 1-3, but demonstrating which features of these curves are altered by specific model parameters, could be far more informative than any extensive discussion in text.

To address the third major concern, additional control experiments are likely required. The degree of inactivation of ChR2 is likely a function of light power and available channel population in the membrane, and therefore has to be measured empirically under specific experimental conditions. In the public comments, two experiments are suggested (directly measuring ChR2 inactivation with equivalent light power, and running the ramp backwards). Although it seems feasible to do both experiments in the same preparation, either one of these would likely be sufficient if both measurements cannot be made.

Reviewer #2 (Recommendations for the authors):

I have just a few comments for improving the paper, listed below in no particular order.

1. The zap protocol presented in the first figures has been used previously for CINs (Beatty 2015) and gave somewhat different resonance peaks. It would be interesting to discuss potential reasons for these differences.

2. Using the ZAP protocol by current/voltage somatic injection is likely to result in very different behavior than optogenetic entrainment due to the biophysical properties of ChR2 itself. ChR2 has its own activation and inactivation time constants which will affect the currents recorded during the ZAP protocol. Indeed, the phase-shift curves in Figure 3 are very different from those in figures 1 and 2.

3. The analysis of the backpropagation of action potentials into the CIN dendrites relies on the calcium responses presented in Figure 4D, however there is no direct measurement of the invasion of the AP and the measurement could also reflect the density of certain calcium channels and not only that of NaP ones. While performing dendritic electrophysiological recordings is labor intensive and may indeed be outside the scope of this study, this issue should be discussed. Also, the variability in the dendritic calcium responses presented in 4D is huge, and it is difficult to assess the statistical validity of the observed decay in response amplitude. Were there no responses beyond ~120 microns?

4. The synaptic input from optogenetic activation of cortical and thalamic input generated synaptic responses in the presence of AMPA, NMDA, GABAA, and GABAB blockers (according to the Methods section). What was the nature of these responses if they were not AMPA/NMDA mediated? If a different set of blockers was used it should be mentioned. Were the responses purely monosynaptic? This should be tested using TTX/4AP combination, as in Petreanu et al., (2009). If no blockers were used in these particular experiments, could there be polysynaptic interactions in addition to the monosynaptic responses?

5. While the thalamic inputs were activated by viral injections in the PfN of Vglut2-Cre mice, the cortical activation relies on the ChR2 reporter in Thy1 mice. Is ChR2 expressed only in cortical cells? Which other inputs may be activated? Is there no thalamic labeling in Thy1-ChR2 mice?

6. Could ranolazine have presynaptic effects on the optogenetic stimulation of axons? This could be checked by assessing changes in synaptic release properties by PPR or train optogenetic protocols.

7. The entrainment of TANs and MSNs to slow wave oscillations is interesting and the difference from SPNs is striking. There is a discrepancy with previous papers showing a very strong modulation of MSNs during cortical slow-wave oscillations (Stern et al., (1997, 1998), Reig and Silberberg (2014)). Intracellular (and whole-cell) recordings of CINs during slow-wave oscillations also showed various degrees of entrainment of the membrane potential to the cortical oscillation but to a lesser degree than MSNs (Schulz et al., (2011), Reig and Silberberg (2014)). This does not necessarily mean that the input is cortical since thalamus also displays slow-wave oscillations under the same conditions. Moreover, natural slow wave sleep is different from slow wave anesthesia-induced sleep. These differences would be interesting to discuss.

8. Is the entrainment of TANs to slow-wave oscillations stronger than to other "sleep frequencies"? How locked are they to the higher frequencies in other sleep stages?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Non-uniform distribution of dendritic nonlinearities differentially engages thalamostriatal and corticostriatal inputs onto cholinergic interneurons" for further consideration by eLife. Your revised article has been evaluated by John Huguenard (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Further experiment or simulation is needed to address the discrepancy between the modeling in Appendix 2 and the physiology results in Figure 5.

Reviewer #1 (Recommendations for the authors):

The authors have done an admirable job of responding to most of the major comments through a combination of new experiments, modeling, and conceptual insight. Their efforts are especially thorough with respect to questions regarding how the kinetics of ChR2 may influence the interpretation of results from the Chirp stimulus protocol. The modified manuscript is substantially clarified and improved.

However, the new manuscript still falls short of convincingly addressing one of the primary conceptual questions raised in the previous review: Why are cortical inputs onto distal dendrites not boosted as they pass through a proximal dendrite? The authors offer an explanation (that the NaP current is voltage-dependent and nonlinear), which appears well suited to explain the new modeling results in Appendix 2. However, there appears to be a fundamental discrepancy between the modeling in Appendix 2 and the physiology results in Figure 5. In the modeling data (Appendix 2), the cortical EPSP is far smaller at the soma than the thalamic EPSP (presumably due to attenuation/leak over the length of the dendrite?). This reduced amplitude of the cortical EPSP as it passes through the proximal dendrite seems well suited to account for the lack of boosting observed in the model. However, in the physiology data (Figure 5), the cortically evoked EPSP is equivalent size or larger at the soma than the thalamically evoked EPSP. Wouldn't this mean that, in this experiment, the cortical EPSP is at least as large as the thalamic EPSP when it passes through the proximal dendrite?

If cortical and thalamic EPSPs are each driving equivalent depolarization of the proximal dendrite in Figure 5, how is it that the cortically evoked EPSP does not experience the same non-linear boosting as the thalamic EPSP?

In order to adequately explain the physiology data in Figure 5, the modeling in Appendix 2 should compare evoked inputs from different sources that elicit equivalent EPSP amplitude at the soma. If this model cannot explain differential boosting of inputs that elicit equivalent EPSP amplitudes at the soma, some alternate interpretation should be provided for the surprising physiological result in Figure 5.

Reviewer #2 (Recommendations for the authors):

My comments have been addressed and I congratulate the authors for a very interesting paper.

Just for curiosity, what is the advantage in using discrete frequency transitions rather than a continuous frequency increase in the ZAP protocol?
