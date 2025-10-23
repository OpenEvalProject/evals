# Peer review - Round 1

Editors:
- Marisa Carrasco, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40868.035](https://doi.org/10.7554/eLife.40868.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Attention periodically samples competing stimuli during binocular rivalry" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Daniel H Baker (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an innovative, interesting and timely study that reveals periodic switching dynamics during binocular rivalry, following cross-modal cues, and explores the rate of attentional sampling during dominance and suppression. Data from perceptual responses show that with relevant cross-modal cues attentional modulations are periodic. When the cue is congruent with the current visual percept, switches display an 8Hz periodicity; when the cue is incongruent, switches occur in about half of 8Hz, with a 3.5Hz frequency. This pattern of results fits well with the idea of attentional sampling, whereby attention samples a single target at around 8Hz, but for two competing targets the effective sampling rate is divided, i.e. about 4Hz. The presence of EEG correlates of these rhythmic dynamics at the same frequencies tends to support the authors' claims.

Addressing the following points will provide information regarding the validity of the claims and strengthen the manuscript.

Essential revisions:

Theoretical issues

1) You should discuss the Dieter, Melnick and Tadin, 2015 study, which shows that stimulus-driven cues can bias perceptual report. Exogenous feature-based cues were presented close to the rivalry stimuli; the cue congruent with the (currently) dominant percept lengthened its duration whereas the cue congruent with the suppressed percept hastened it to emerge back. The authors should stress the novelty of their study regarding the oscillatory nature of such process.

2) The authors should discuss whether they think that the oscillatory behavioral responses they found reflect an oscillation of perception or decision criteria, even though these two aspects cannot be distinguished in the perceptual report used in this study. Germane to this discussion is a recent study that using signal detection theory found that alpha oscillation modulates criterion, not sensitivity (Lemi et al., 2017).

3) The reported effects only occur for the 4.5-Hz modulated stimulus, and not for the 20Hz modulation. Does this imply an upper temporal limit for crossmodal interactions or for attention?

4) The authors should relate their findings to computational models of binocular rivalry. Many use mutual inhibition, adaptation and noise to describe the neural circuit underlying rivalry (e.g. Wilson, 1997; Laing and Chow, 2002). Some have explicitly implemented an attentional component (e.g. Li et al., 2017). None of the rivalry models have attempted to model oscillatory perceptual rhythms. Could the current results inform which model component(s) (e.g. input drive, mutual inhibition or attention) may be oscillatory?

5) The authors suggest that the 7-8 Hz oscillation reflects a single attentional focus, and the ~4Hz oscillation reflects attention that was split into two foci. Does that imply that without a mismatched cue, observers' attention would be predominantly allocated to the dominant image without oscillating between the two stimuli? Were that the case, how would this relate to the theory on rivalry. Are the authors suggesting that a mismatch cue allowed attention to start jumping across two items? And that such a process would not happen without a mismatched cue?

Methods, Analyses and Results

6) It is not clear that there are 3 types of cross-modal cues (auditory, tactile, and both combined) until the Materials and methods section; i.e., well after reading the Results and considering the figures. The existence of 3 cue types should be mentioned explicitly earlier. In addition, this begs the question of possible differences among the cue types: Do they affect the dynamics of switching and the results described in all figures?

7) It would be good to report the frequency tagged responses to the rivaling stimuli themselves. Are there increases in the response when a frequency-matched cross-modal cue is presented? Do the amplitudes correspond to participant button presses consistent with Brown and Norcia, 1997?

8) For computing Fourier amplitude spectrum, the authors analyzed the time window from 0.5 to 2s from the cue onset. However, Figure 3C and 3D also show oscillatory patterns in the first 0.5s time window. Include this time, narrow the window, or explain why this range was not analyzed. Note that previous studies have removed a shorter time window after the cue (e.g. Landau and Fries, 2012; Fiebelkorn et al., 2013).

9) It is unclear whether the authors performed FFT on the averaged (across subjects) time course, or on individual time courses, and then averaged the spectrum across subjects. If the former, the latter should also be reported. It is important to ensure that the effect does not merely result from the averaging procedure.

10) A technical issue regards the EEG ITPC calculation and the logic of upsampling. We agree that it is necessary to equate the number of mismatched and matched cue types for the analysis. However, the strategy of upsampling the lowest-trial-count condition up to the trial number in the highest-trial-count condition is questionable. We are not convinced that the authors' analysis confirmed that upsampling, compared to downsampling, reduced the bias introduced when equating ITPC values across subjects. Running the Matlab code below, the authors will see that the ITPC bias caused by a difference in trial count (first figure) is not reduced when upsampling the low-trial-count condition (second figure), but disappears when downsampling the high-trial-count condition (third figure). You should repeat the analysis with downsampling, ideally multiple times to avoid spurious results.

1.%% Matlab code

2. phases = 2*pi*rand(30,1000);% low trial count condition

3. otherphases = 2*pi*rand(90,1000);% high trial count condition

4. downsampled_otherphases = otherphases(1:30,:);% downsample high trial count

5. upsampled_phases = repmat(phases,3,1);% upsample low trial count

6. ITPC = abs(mean(exp(1i*phases),1));

7. otherITPC = abs(mean(exp(1i*otherphases),1));

8. downsampledITPC = abs(mean(exp(1i*downsampled_otherphases),1));

9. upsampledITPC = abs(mean(exp(1i*upsampled_phases),1));

10. figure;

11. subplot(2,1,1); hist(ITPC); title('Original phases (low N)'); set(gca,'xlim',[0 0.4],'ylim',[0 250]); xlabel('ITPC');

12. subplot(2,1,2); hist(otherITPC); title('Original phases (high N)'); set(gca,'xlim',[0 0.4],'ylim',[0 250]); xlabel('ITPC');

13. figure;

14. subplot(2,1,1); hist(upsampledITPC); title('Upsampled phases (low N)'); set(gca,'xlim',[0 0.4],'ylim',[0 250]); xlabel('ITPC');

15. subplot(2,1,2); hist(otherITPC); title('Original phases (high N)'); set(gca,'xlim',[0 0.4],'ylim',[0 250]); xlabel('ITPC');

16. figure;

17. subplot(2,1,1); hist(ITPC); title('Original phases (low N)'); set(gca,'xlim',[0 0.4],'ylim',[0 250]); xlabel('ITPC');

18. subplot(2,1,2); hist(downsampledITPC); title('Downsampled phases (high N)'); set(gca,'xlim',[0 0.4],'ylim',[0 250]); xlabel('ITPC');

19.% % End Matlab code

Figures

11) Figures 2A, 3A, 4B and 5B require figure legends so that the meaning of the colors is clear without reading the caption.

12) In Figures 4A and 5A it would be helpful to mark all electrode locations with small dots. We assume these plots are thresholded, such that electrodes with non-significant t-values are set to t=0, but this wasn't stated explicitly. Why not plot all t-values and indicate which are significant in some other way (e.g. with superimposed symbols).

13) The 9Hz difference in Figure 5B is somewhat unexpected. This is described as a 'stimulus harmonic', but if so, we wouldn't expect to see a difference between matched and mismatched trials. Do the authors have an explanation for this? Does the 9Hz response also correlate with the PSI measure?

14) The model diagrams in Figure 6 are somewhat confusing. For model (a), do the authors mean that the suppressed image emerges back because attention shifts to the mismatched cue first, and thus the mismatched cue enhances the suppressed image? For model (b), it seems surprising that the presence of the green-crossmodal cue would let the attention focus move from the dominant red image to the suppressed red image, before it moves to the dominant green image…

15) For correlation scatterplots, it would be helpful to include R and p values in the plot. Are the straight lines in these plots regression lines that predict the y-values using the x-values (i.e. minimizing the error in the y-direction)? Given that both of these are dependent variables with presumably no implied causation, we recommend using Deming regression lines instead, which minimize the absolute error between the line and each data point.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Attention periodically samples competing stimuli during binocular rivalry" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Frank (Senior Editor), a Reviewing Editor, and three reviewers.

The three reviewers and I think that you have addressed all the issues raised satisfactorily, but one. The pending issues regards the ITPC calculations and down-sampling vs. up-sampling.

We note that there is a crucial difference in the definition of ITPC "bias": You are talking about minimizing absolute bias (the fact that ITPC is always overestimated when using a finite number of trials, to an extent inversely related to the trial number, e.g. compare Author response image 4D and 4E). Instead, the reviewers are worried about relative bias (the fact that two experimental conditions with equal "true" ITPC may produce very different ITPC values if the number of trials is not equated, e.g. compare Author response image 4A and 4D).

Your upsampling method keeps the absolute bias as low as possible in each condition (given the trial number), but does not reduce relative bias (e.g. compare Author response image 4C and 4D). Only downsampling can remove this relative bias (e.g. compare Author response image 4A and 4E). This comes with the cost of an increase in absolute bias for the high N condition (compare Author response image 4D and 4E), but given that your analysis relies on a comparison of the two conditions, the relative bias must be eradicated; absolute bias changes are just collateral damage.

To summarize:

1) The reviewer made the null assumption that the 2 experimental conditions (matched/mismatched) have the same true ITPC but different numbers of trials. (Here the true ITPC was assumed to be zero, which is the worst-case scenario: no actual phase-locking).

2) When comparing ITPC across the two conditions, a systematic difference was found (Author response image 4A vs. 4D). This difference is necessarily a statistical artifact.

3) The reviewer applied the authors' upsampling method to equate trials; the systematic difference remained (Author response image 4B/4C vs. 4D).

4) The reviewer applied a downsampling method to equate trials; the (artifactual) difference disappeared (Author response image 4A vs. 4E).

5) Conclusion:

The authors are correct that upsampling can preserve the ITPC to have a similar value as that derived from the original dataset (without resampling). But, this is not the point here. The aim of resampling is to let the ITPCs from the two conditions comparable when performing statistical tests. When comparing ITPC from two conditions with unequal trial numbers, upsampling can produce false positives, downsampling will not. Thus, the authors should use downsampling instead of upsampling.
