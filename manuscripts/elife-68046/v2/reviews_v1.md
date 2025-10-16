# Peer review - Round 1

Editors:
- Brice Bathellier, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68046.sa1](https://doi.org/10.7554/eLife.68046.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This study establishes a new method for more precise estimation of pairwise noise and signal correlations in two-photon calcium imaging, by modeling generically the influence of calcium dynamics and subtracting the interaction between response signals and variability when the trial number is low. The accuracy of this new estimator is demonstrated here for the mouse auditory cortex, but this tool will find useful applications on a large diversity of datasets.

Decision letter after peer review:

Thank you for submitting your article "Direct Extraction of Signal and Noise Correlations from Two-Photon Calcium Imaging of Ensemble Neuronal Activity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Brice Bathellier as the Reviewing Editor and Reviewer #1. and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers agree on the quality of the method proposed in this study and it potential for assessing correlations in two-photon calcium imaging data. However, two points should be carefully addressed according to the comments below. First the authors should better explain what aspect of your method is key for your approach to outperform others methods. Second, the authors should better explore the behavior of your method on data that does not fulfil the core assumptions you make (uncorrelated noise, LN response model).

1. Surrogate data use a measurement noise model that has no temporal correlations. This is not the case in real two-photon imaging data, which include both correlation-free noise (photon count statistics) and temporally (and spatially) correlated artefacts. As in Deneux et al. 2016 (cited in the paper), the authors should provide simulations with different types of noise and show how this affects their correlation estimates. Is it still more robust than more classical methods?

2. Another simplifying assumption used by the authors is their model of spiking activity which is composed of a linear receptive field followed by a non-linear mapping function. Several papers have shown that this only imperfectly models neural responses (e.g. to sound in auditory cortex). There are, in fact in real neural data, non-linearities that are more complex than what the mapping function can capture. How does this impact their estimate? The authors should simulate this with e.g. a multilayer network (two-layer linear non-linear cascade, deep net) or simulate neurons that respond to the quadratic sum of the output of several linear filter (see e.g. recent work by the Shamma and colleagues).

3. There is a lack of intuition about the key aspects in their approach that makes it overperform other methods. This should be introduced in the results and/or discussion to better guide and convince the reader.

It is crucial that any end-user be able to get a clear picture of the conditions under which the method can or cannot be applied before diving in. The fact that such an applicability domain is not well defined is a major concern. Notably, each Real Data Study presented in the paper uses a preliminary selection of "highly active cells" (1rst study: N = 16; 2nd study: N = 10; 3rd study: N~20 per field), as the authors succinctly discuss that performance is expected to degrade "in the regime of extremely low spiking rate and high observation noise" (l. 518-519). But no precise criteria are provided to specify what is meant by "highly active cells". On the other hand, the authors also assume that there is at most one spiking event per time frame for each neuron, which seems to exclude bursting neurons. The latter assumption seems to be a challenge with respect to the example traces shown on Figure 4C (∆F/F reaches 400%) and on Figure 6C (∆F/F reaches 100%), considering that the GCaMP6s signal for a single spike is expected to peak below 10-20%. This forces the authors to take a scaling factor of the observations A = 1 x I (Real Data Study 1 and 3) or A = 0.75 x I (Real Data Study 2) compared to the A = 0.1 x I taken in the Simulation Studies. Therefore, it looks like if the Real Data Studies were performed on mainly bursting cells and each burst was counted as one spiking event. A detailed discussion of the usable range of firing rates, whether in spike or burst units, as well as the usable range of SNR should be added to the main text to allow future users to assess the suitability of their data for this analysis.

4. Another parameter seems to be set by the authors on a criterion that is unclear to me: the number of time lags R to be included in the sound stimulus vector st. It seems to act as a memory of the past trajectory of the stimulus and probably serves to enhance the effect of stimulus onset/offset relative to the rest of the sound presentation. It is consistent with the known tendency of neurons in the primary auditory cortex to respond to these abrupt changes in sound power. However, this R is set at 2 in the Simulation Study 1, whereas it is set at 25, in the Real Data Studies 1 and 3, and to 40 in the Real Data Study 2. What leads to these differences escaped to me and should be explained more clearly.

5. This memory of the past stimulus trajectory appears to be specific to the proposed method and is not accounted for in the 2-stage Pearson estimation, for example. Since it probably helps to reflect the common sensitivity of neurons to onset/offset, it alone provides an advantage to the proposed method over the 2-stage Pearson estimation. It would be instructive to also perform this comparison with R set to 1 to get an idea of the magnitude of this advantage.

Reviewer #1 (Recommendations for the authors):

1. Surrogate data use a measurement noise model that has no temporal correlations. This is not the case in real two-photon imaging data, which include both correlation-free noise (photon count statistics) and temporally (and spatially) correlated artefacts. As in Deneux et al. 2016 (cited in the paper), the authors should provide simulations with different types of noise and show how this affects their correlation estimates. Is it still more robust than more classical methods?

2. Another simplifying assumption used by the authors is their model of spiking activity which is composed of a linear receptive field followed by a non-linear mapping function. Several papers have shown that this only imperfectly models neural responses (e.g. to sound in auditory cortex). There are, in fact in real neural data, non-linearities that are more complex than what the mapping function can capture. How does this impact their estimate? The authors should simulate this with e.g. a multilayer network (two-layer linear non-linear cascade, deep net) or simulate neurons that respond to the quadratic sum of the output of several linear filter (see e.g. recent work by the Shamma and colleagues).

3. There is a lack of intuition about the key aspects in their approach that makes it overperform other methods. This should be introduced in the results and/or discussion to better guide and convince the reader.
