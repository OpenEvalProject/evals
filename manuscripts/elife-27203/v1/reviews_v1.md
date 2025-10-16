# Peer review - Round 1

Editors:
- Barbara G Shinn-Cunningham, Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27203.008](https://doi.org/10.7554/eLife.27203.008)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The human auditory brainstem response to running speech reveals a subcortical mechanism for selective attention" for consideration by eLife. Your article has been favorably evaluated by Andrew King (Senior Editor) and three reviewers, one of whom, Barbara G Shinn-Cunningham (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Steve Aiken (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The results of this study are very intriguing, showing differences in auditory steady-state responses (ASSRs) that are specific to which of two speech streams a listener is attending. Although the correlations between the stimulus and response are small, the peak of the cross-correlation function was significant in most of the subjects, as was the effect of attention. The writing is generally clear and concise.

All three reviewers thought that the conclusion that brainstem-generated responses are modulated by attentional focus, if properly justified, is novel and noteworthy. While many aspects of this paper are intriguing, there are questions that affect the interpretation. These technical issues and concerns must be addressed adequately for the study to be acceptable for publication in eLife.

Essential revisions:

1) For any response like this, including the more-common FFR (with a steady-state constant-frequency acoustic signal), observations are a mixture of IC responses and other responses (perhaps in thalamus – but also lower responses such as the cochlear microphonic). For the same relative delays and magnitudes of the responses, these different responses will add in different phases, depending on their frequency. Unlike with the FFR, here, the frequency is changing from moment to moment. This will lead to different cancellation / summation at different frequencies that likely result in different peak delays. Only if there is a single truly dominant source in the mixture will the peak delay be at a fixed delay independent of frequency.

Attention effects in FFRs have been suggested to be due to the involvement of the cortex (the work of Emma Holmes presented at ARO 2017). While the delay of 10 ms relative to the stimulus calls into question a dominant role for the cortex in the present study (see above), it is also possible that the attention effect is mediated through olivocochlear inhibition.

The stats show that attention is changing the observed responses. The question is just where these responses are coming from. Given that the observed response is a mixture, further analysis is warranted to tease apart whether the effects are due to a single dominant source with a fixed delay that is modulated by attention, or whether higher-level sources, which are modulated by attention, cause different summation / cancellation effects depending on attentional focus.

2) The latency reported, 10.3ms, is greater than is usually attributed to a brainstem response. The latency of the largest peak of the click-evoked ABR (usually attributed to inferior colliculus) is usually assumed to be ~5ms or somewhat greater for lower-frequency stimuli (Don and Eggermont, 1978).

Often, the delay in an ASSR is longer (presumably in part because it is a mixture of neural sources as noted above). The authors say that their estimate agrees with that reported by Skoe and Kraus (2010) for speech, but the value reported in that paper is actually 7-8ms. Figure 1 of that paper, where that value is mentioned, illustrates it as the amount by which the response precedes the stimulus (!), so that source itself may have some methodological problems.

Because the latency is the primary fact used to conclude that the induced attentional changes are from brainstem, this issue is very important to consider and discuss.

3) The latency is calculated as a cross-correlation between electrode signals and a "fundamental waveform" defined as a "nonlinear oscillation" derived from the speech by empirical mode decomposition (EMD). EMD is attractive but not very well defined or theoretically grounded; as far as we can tell, it just extracts an approximation of the fundamental Fourier component. The Hilbert transform is calculated, and both the waveform and its Hilbert transform are cross-correlated with the EEG to obtain a "complex correlation function", the amplitude of which peaks at a latency of 10.3ms. The rationale for introducing this Hilbert component is not clear, as it would seem more straightforward to correlate simply with the speech waveform (or its "fundamental waveform). The "amplitude of the complex CC" has a wider peak than the raw CC.

Please explain and justify the analysis more clearly.

4) An accurate estimate of latency is crucial for saying that the response reflects the brainstem. Temporal alignment between audio and EEG may be affected by acoustic delay in the earphones (not specified, possibly ~1ms for ER 3), as well as the signal processing of the inputs and of the brain measures.

Audio is down-sampled (interpolation filter unspecified), filtered by a FIR of order 296 (IR temporal extent 33.4 ms), time-shifted to "compensate for delay" of the FIR, processed by the EMD algorithm, and finally by the Hilbert transform. The Hilbert transform is presumably performed by applying an STFT to a window of unspecified duration. It involves a 90-degree phase shift that translates (for the quasi-sinusoidal fundamental wave) to a frequency-dependent time shift of up to 2.5ms at 100Hz.

On the EEG side, the signal is processed by a frequency-domain method (ClearLine) to attenuate 50Hz and (presumably) harmonics. The possibility that this might affect the fundamental waveform (its time-varying frequency falls in this range) is not discussed. The EEG is filtered by a cascade of FIR filters of order 6862 and 1054 (IR lengths 274ms and 42ms) before correlation with the audio-based signal. There are clearly many stages at which a latency mismatch could arise, and the fact that this is not acknowledged or addressed (for example by calibration) is troubling.

The peak value of the cross-correlation function shown in Figure 1C, 0.05, seems rather high given that the ABR is supposed to have very low SNR. Similar values (0.05 – 0.1) have been reported for cross-correlation with filtered cortical responses that are supposed to have a much better SNR. The shape of the function is also somewhat intriguing because it is approximately symmetrical and extends to negative lag (i.e., there is a noncausal relationship between the input and the neural response). This suggests that it is largely determined by temporal smearing in the processing, for example due to convolution with the various unspecified filter kernels.

Please carefully outline how the acoustical and neural signal processing affects the estimated latency of the neural responses.

5) From the description of methods, it would seem that the stimulus is always presented with the same polarity. Electrode signals measured in that case are likely to be dominated by cochlear microphonic or possibly even cross-talk from the earphone drivers or cables. There is no reason to believe that they are from brainstem, except possibly latency (and as discussed above, it is unclear how good an indicator that is of brainstem activity).

Please include some calibration or analysis to verify that electrical artifact is not a significant factor in your findings.

6) While the speech presentation levels were relatively high, individual high-frequency harmonics would be relatively low in level given the low-pass characteristic of speech signals. Attentional modulation of cochlear gain has been shown to be frequency-specific (e.g., Maison et al., Psychophysiol 2001) and certainly could be specific to a harmonic complex.

It would be useful to include this point in the Discussion.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "The human auditory brainstem response to running speech reveals a subcortical mechanism for selective attention" for consideration by eLife. Your article has been favorably evaluated by Andrew King (Senior Editor) and three reviewers, one of whom, Barbara G Shinn-Cunningham (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Steve Aiken (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. It is not normally eLife policy to allow a paper to go through multiple rounds of reviews, so this will be the last opportunity to revise the manuscript before a final decision is made.

Summary:

This paper provides evidence for attentional modulation in neural responses measured in response to running speech. The approach is relatively novel and the findings interesting.

The revision has gone some way to addressing the concerns raised by the reviewers. However, several questions still need to be answered. The reviewers also provide suggestions for how to strengthen the argument. The controls added here would definitely strengthen the paper.

Essential revisions:

1) The paper continues to over-emphasize that the measured responses are from the brainstem. The evidence shows a clear attentional effect; however, the claim that the observed effects are absolutely from the brainstem is still problematic. If cortical contributions cannot be ruled out, it would be presumptuous to conclude that this is an attentional effect in the brainstem.

The authors should make their case more persuasively. One approach to enhance this argument is to conduct further analysis of their present data. If cortical contributions are indeed responsible for the attentional effects, one would expect to find a positive correlation between peak latency and amplitude in the attended conditions. One might also expect such effects to be stronger for segments with lower fundamental frequencies (e.g., < 200 Hz) given cortical phase-locking limits.

The authors should test for these possibilities. Of interest would be any relationship between peak cross-correlation latency and peak cross-correlation amplitude for attended streams, and between peak cross-correlation amplitude and segment fundamental frequency (also for attended vs. unattended streams). Such an analysis might lead to a more nuanced understanding of the data or conversely add weight to the conclusions.

2) The cross-correlation functions between speech and "fundamental wave" and between raw and processed EEG) address earlier concerns about the effect of processing on latency estimates. Still, an end-to-end calibration would be even more convincing. This does not require recording new data, but rather running simulated data through the processing pipeline: (a) formulate a simple speech-to-neural response model based on the conclusions the authors believe follow from their results, (b) add background EEG signal (e.g., from recorded data shifted in time), (c) run the analysis, (d) check whether latencies conform to what is expected based on the model. Given the importance of the timing of the responses to the argument that the effects are subcortical, the extra effort is worthwhile: the EEG processing pipeline involves many convolutional stages that the authors still do not fully characterize (are all filters zero-phase?).
