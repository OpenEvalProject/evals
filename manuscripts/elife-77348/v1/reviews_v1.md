# Peer review - Round 1

Editors:
- Ole Jensen, https://ror.org/03angcq70 University of Birmingham United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77348.sa0](https://doi.org/10.7554/eLife.77348.sa0)

The paper addresses the highly timely question of how to quantify aperiodic and periodic neural activity. This was done by extending previous work by embracing time-resolved parametrization of both simulated, noninvasive EEG and intracranial data. The new approach is termed Spectral Parametrization Resolved in Time (SPRiNT) and the paper shows that the slope of aperiodic activity is linked with both behavior and age. The method thus demonstrates the importance of evaluating the state-dependence of aperiodic activity and dynamic properties of oscillatory components in a time-resolved manner, and we believe that this approach would be of great interest to researchers analyzing human electrophysiological data to address clinical and cognitive neuroscience questions.


---

# Peer review - Round 1

Editors:
- Ole Jensen, https://ror.org/03angcq70 University of Birmingham United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77348.sa1](https://doi.org/10.7554/eLife.77348.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Time-resolved parameterization of aperiodic and periodic brain activity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Mats W.J. van Es (Reviewer #2); Jan Kujala (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The three reviewers were in general positive about the manuscript. However, several concerns were raised. Several of those were related to the simulated data used for testing the algorithm. Also, the comparison to other methods could be improved. Please see below for details.

Reviewer #1 (Recommendations for the authors):

One aspect that can improve the impact of the paper is to show how the application of SPRiNT cardinally changes the interpretation of the data in the case when it was analyzed with rather conventional approaches. For instance, one can show that while using conventional methods, there are changes in the power, yet, when SPRiNT is applied these changes disappear or vice versa. It can be either dataset presented in this study or other datasets.

Please explain more carefully how the data was generated with respect to SNR of oscillations, how SNR was explicitly controlled.

The authors write: "Each simulation was analyzed with SPRiNT using 5x1s STFT windows with 50% overlap (frequency range: 1-40 Hz)." What would happen if the fluctuation of periodic and aperiodic components occur in < 1-sec time range? This would correspond to a situation in real brain activity since E and I inputs are often transient in nature and can span just a few hundred milliseconds.

When differentiating eyes-open or eyes-closed condition, was this differentiation based on 5 mins data or on shorter segments, like a few seconds only? The latter case would be most interesting.

What are the smallest segments and number of overlapped segments for the estimation of periodic and aperiodic components? It seems that EEG and LFP data were analyzed with different parameters.

In contrast to EEG data, intracranial animal data was analyzed with different parameters for SPRiNT, i.e. each recording block was analyzed with SPRiNT using 5x2 s sliding time windows with 75% overlap. Why was it the case? For the reader, it is important to know how these decisions are made about the length of the window and overlap.

When tracking movement transitions it is important to take into account movement-related artifacts which can introduce changes in a wide frequency range. How were they handled?

The authors write: "We noted that both methods tended to overestimate peak bandwidths (Figure 2 —figure supplement 1)" It seems that there is a systematic bias in peak bandwidth estimation. Is there a way to compensate for it?

It is possible that the changes between young and old participants (or in eyes-open and eyes-closed conditions) were due to relatively local changes in low-frequency oscillations which would consequently lead to deviation from 1/f decay of spectrum. This in turn would lead to changes in goodness-of-fit (GOF) of 1/f component between conditions. Have authors observed systematic changes in GOFs between different conditions?

Please discuss cases where the aperiodic part can be stable vs when it can be unstable.

Reviewer #2 (Recommendations for the authors):

1. In the first analysis, the authors compare SPRiNT with specparam applied to a wavelet time-frequency spectrum. Given that the original method by Donoghue et al., is based on Welch's method (which uses the Discrete Fourier Transform; DFT), it is unclear why the authors chose wavelets as a benchmark. A more direct comparison with Donoghue et al., would be comparing the time-resolved with the static specparam approach, without the implicit comparison of STFT with wavelets. Could the authors please motivate their choice of benchmark? (potentially the analysis described in lines 36-46 of the supplement could be moved/referred to in the main text).

2. One issue when applying SPRiNT to task data is that it temporally smooths a/periodic parameter estimates (i.e. by averaging Fourier coefficients over neighbouring windows), which can lead to blurring of baseline and task windows (especially in a typical task where baseline and task period are only a few seconds). Could the authors elaborate on how to choose parameter settings (e.g., number of overlapping time windows; whether or not to fit a knee) and what pitfalls to look out for?

3. Line 194 refers to a supplemental figure (the figure 2 equivalent prior to removal of outlier peaks). Line 21 of the supplement also refers to this figure. However, the figure appears to be absent.

4. Figure 3D shows there is a general underestimation of the number of periodic components, especially in the δ band. Perhaps it would be useful to add a figure to the supplement containing a confusion matrix, i.e. showing how likely each simulated peak is to be recognised as a peak in a different frequency band (or not recognised) over all simulations.

5. Figure 3C shows the detection probability of spectral peaks with respect to centre frequency and peak amplitude. Could to authors create a similar figure for bandwidth, or at least comment on this?

6. Alternatives to the Short Time Fourier Transform (STFT) are discussed in both the introduction and discussion but do not mention Empirical Mode Decomposition (EMD; Huang et al., 1998; Quinn et al., 2021).

7. Recently, another adaptation of specparam, called PAPTO, was described by Brady and Bardouille (2022; https://doi.org/10.1016/j.neuroimage.2022.118974), specifically regarding transient oscillations. It would be good if the authors could add this in their discussion, especially in light of pruning the periodic component outliers.

8. A few observations from the Results are missing in the discussion. I would like to ask the authors to add a discussion on (1) the overestimation of peak bandwidth by SPRiNT, (2) the underestimation of the number of detected peaks in figure 3, and (3) the peaks in the aperiodic component and offset at moments of switching eyes open/closed in figure 4 – supplement 1 (also related to point 2).

9. From lines 245-248 it does not become clear from the main text that the authors conducted a logistic regression analysis; this only becomes clear from the subtext of figure 4B. Please add it to the main text.

10. It seems that tables 5 and 6 are mixed up in the main text (line 304, 309), e.g. line 304 is referring to table 5 but should be referring to table 6.

11. There appears to be a grammatical error in lines 416-418 ("…has associated how locomotor behavior is associated…").

12. Figure 3D would be clearer with a legend. Also, the subtext talks about "blue" for 3-8 Hz peaks but is ambiguous because (dark) blue also denotes an undetected peak. Please clarify in the text.

13. The reference to figure 3E in the subtext should be in bold font.
