# Peer review - Round 1

Editors:
- Daeyeol Lee, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75540.sa0](https://doi.org/10.7554/eLife.75540.sa0)

Neural activity measured in both electrophysiological and functional neuroimaging experiments are often temporally correlated, and the timescales of such correlation in ongoing neural activity, or intrinsic neural timescales, show a hierarchical pattern across the cortical surface. The present study establishes a close link between these timescales and functional connectivity in the brains of non-human primates, suggesting that temporal autocorrelation is an important organizing feature of large-scale neural activity.


---

# Peer review - Round 1

Editors:
- Daeyeol Lee, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75540.sa1](https://doi.org/10.7554/eLife.75540.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Intrinsic timescales as an organizational principle of neural processing across the whole rhesus macaque brain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Daeyeol Lee as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Effects of anesthesia. Compared to previous human neuroimaging studies and NHP electrophysiological experiments, a significant weakness of this study is that the experiments were performed in anesthetized animals. This is even more problematic, since the analyses in this study mostly focus on the fronto-parietal network, which might be more affected by anesthetics. Although it has been shown that the FC can be studied in anesthetized animals, how specific methods of anesthesia might influence by the measures of INT should be discussed more thoroughly.

2. INT measure. They authors put forth the INT measure as related to intrinsic timescale. INT is defined as the integrated area under the autocorrelation function (ACF) up until the first point where the ACF goes below zero. This is different than how intrinsic timescale has been measured in single-neuron spike trains or in prior fMRI studies. While a longer timescale would be expected to increase INT, the problem is that INT (as an integrated area) combines effects of autocorrelation timescale and autocorrelation amplitude.

– It would be insightful to visualize INT properties at the whole-brain or whole-cortex level (instead of only a single lobe), including (i) INT values themselves, (ii) the lag-one autcorrelation value reflecting autocorrelation amplitude, and (iii) the zero-crossing lag time used to compute INT.

– A highly relevant paper (which is not currently cited) is Ito et al., (2020) NeuroImage, "A cortical hierarchy of localized and distributed processes revealed via dissociation of task activations, connectivity changes, and intrinsic timescales". Figure 5 of Ito shows a cortex-wide map of intrinsic timescale as defined in single-neuron studies (i.e. fitting time constant of decay). Figure 6 then shows this is related to cortical hierarchy as reflected in the T1w/T2w map (which in principle could be tested by the authors here too). Ito's analysis was performed on the parcellated timeseries, not the voxel level as in the present study, which is a notable methodological difference.

– That INT combines effects of timescale and amplitude would not be a problem if the autocorrelation amplitude does not vary across brain regions. However, it appears that it does for whatever reasons (neural and/or in fMRI measurement such as SNR). A relevant preprint is by Shinn et al., (2021) bioRxiv, “Spatial and temporal autocorrelation weave human brain networks”. In human cortex, again using parcellated timeseries, Figure 1F there shows systematic variation across cortical parcels of the lag-1 autocorrelation value. In the present study, it is currently unknown whether INT is reflecting regional differences in autocorrelation timescale (as interpreted), amplitude (not considered), or both.

– Contribution of autocorrelation amplitude to INT may potentially explain why a cortex-wide map of INT does not follow an expected hierarchy as much the more restricted views within one lobe as the current manuscript focuses. For instance, Figure 1 shows that INT values for somatosensory cortex (Figure 1A) are larger than association regions (Figure 1B). Is this potentially due to autocorrelation amplitude being larger in somatosensory cortex?

– Perhaps some smoothing or parcellation would be required to better tease apart autocorrelation timescale from autocorrelation amplitude.

– A highly relevant paper (which is not currently cited) is Ito et al., (2020) NeuroImage, "A cortical hierarchy of localized and distributed processes revealed via dissociation of task activations, connectivity changes, and intrinsic timescales". Figure 5 of Ito shows a cortex-wide map of intrinsic timescale as defined in single-neuron studies (i.e. fitting time constant of decay). Figure 6 then shows this is related to cortical hierarchy as reflected in the T1w/T2w map (which in principle could be tested by the authors here too). Ito's analysis was performed on the parcellated timeseries, not the voxel level as in the present study, which is a notable methodological difference.

– That INT combines effects of timescale and amplitude would not be a problem if the autocorrelation amplitude does not vary across brain regions. However, it appears that it does for whatever reasons (neural and/or in fMRI measurement such as SNR). A relevant preprint is by Shinn et al., (2021) bioRxiv, "Spatial and temporal autocorrelation weave human brain networks". In human cortex, again using parcellated timeseries, Figure 1F there shows systematic variation across cortical parcels of the lag-1 autocorrelation value. In the present study, it is currently unknown whether INT is reflecting regional differences in autocorrelation timescale (as interpreted), amplitude (not considered), or both.

– Contribution of autocorrelation amplitude to INT may potentially explain why a cortex-wide map of INT does not follow an expected hierarchy as much the more restricted views within one lobe as the current manuscript focuses. For instance, Figure 1 shows that INT values for somatosensory cortex (Figure 1A) are larger than association regions (Figure 1B). Is this potentially due to autocorrelation amplitude being larger in somatosensory cortex?

– Perhaps some smoothing or parcellation would be required to better tease apart autocorrelation timescale from autocorrelation amplitude.

3. Does the calculation of fMRI-based neuronal time constants obscure the unit of time? True comparison with ephys data is not possible without clarifying the relationship of the two quantities compared. In the ephys measurements time constants are in units of seconds and often below 1s. In contrast, BOLD response has a sluggish time course (tens of seconds) due to the properties of the hemodynamic response function. The smoothing of spiking and field-potential activity with the HRF introduces substantial auto-correlation in BOLD and is expected to reduce our ability to distinguish small differences of time constants discovered with ephys. Because the analyses in this paper do not explore the complications caused by the slow and noisy BOLD measurements, it is impossible to know if the observed temporal hierarchy has the same nature and origin as those reported with ephys. It would be useful to perform additional analyses and modeling that clarifies this missing link. If that is not possible, at the very least I would recommend explicit reporting of the units of time constants based on BOLD in the figures, and discussing if the differences of BOLD time constants across regions match the differences of spiking activity time constants in previous publications. Also, throughout the paper, figures should clearly indicate the unit for INT.

4. Functional connectivity gradients: Figures 3 and 4 rely on functional connectivity gradients calculated within a single lobe, against which INT topography is correlated. On such a restricted geometry as a single lobe, a functional connectivity gradient may be reflecting a simpler property, namely the geometry of the restricted cortical sheet. In other words, given the sheet geometry of the frontal lobe, does an anterior-posterior topography fall out naturally as the first gradient (e.g. with distance-dependent falloff) and medial-lateral as second gradient? If so, it is difficult to strongly interpret these results as linking INT to functional connectivity when the gradient is a generic consequence of the sheet geometry. In human neuroimaging such functional gradients are typically calculated at the whole-cortex level which reveals less trivial topographies (e.g. Margulies et al., 2016, PNAS). These results and interpretations should be considered in light of this concern.

5. There is no strong relationship between within area FC and INT maps in figure 4. Unlike the FC maps that seem to monotonically change along a cortical axis, the INT maps seem to have non-monotonic changes. For example, the INT map for OFC has maximum values both in the anterior-medial and caudal-lateral regions. Similar discrepancies between the INT and FC maps are apparent for PFC. Also, unlike the FC maps, the INT maps seem asymmetrical in the two hemispheres. Unfortunately, the visualization and stats are too dense to probe what is going on. Deeper analyses and explanation are necessary (please see the next comment for a potential solution).

6. Many fine level discrepancies are also observed between striatal INTs and cortico-striatal INTs. In the current figures, it is impossible for readers to know if the variations and discrepancies are within the range expected from noise in the data. The alternative is that some of the variations are meaningful but ignored by the authors to keep the narrative simple. Either way, the authors are encouraged to improve their presentation method and analyses in order to provide adequate information for readers. One possibility is to use old-fashioned scatter plots with error bars, where individual data points are different locations within the striatum and the axes are striatal INTs and cortico-striatal INTs. The authors can choose how they'd like to divide striatum into distinct sub-regions (e.g., a simple 3D grid or functional divisions). Similar plots would be useful for figure 4, and more generally anywhere that the authors report a correlation between INTs and FCs. 7.

7. The authors should provide more detailed information about how the hierarchy shown in the x-axis of Figure 1 was computed, so that this can be replicated by other investigators. Some schematic diagram for cortical hierarchy might be also helpful.

8. The paper would have more value if the same analyses were carried out in other brain areas, such as the temporal cortex, that are not currently covered. If such results are not included, the authors should at least provide a reason why the paper focuses only on the frontal and parietal regions.
