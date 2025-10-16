# Peer review - Round 1

Editors:
- Frances K Skinner, Krembil Research Institute, University Health Network Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68803.sa1](https://doi.org/10.7554/eLife.68803.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper will be of interest to theoretical and experimental neuroscientists. It proposes a novel approach based on state space modeling to estimate the phase of neural signals like EEG and LFP in real-time. It is expected to help drive the improvement and proliferation of phase-related concepts in neurobiology.

Decision letter after peer review:

Thank you for submitting your article "A State Space Modeling Approach to Real-Time Phase Estimation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Milad Lankarany (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Consider the impact of noise in the phase estimation, include specifications of the Kalman filter and its robustness, and consider the performance of the estimated phase relative to other methods.

2) Demonstrate the advantage of using this method for exploring the link between rhythms and behaviour and for phase-locked stimulation, and separate applications that require real time phase estimation from those that can be performed offline using acausal methods.

3) Provide some help to readers from non-technical background by linking the method back to applications and in-vivo data more.

4) Expand details regarding computing credible intervals, slow drift considerations, and physiological motivation of the simulations.

Further details are provided below in the 'Recommendations for the authors'.

Reviewer #1 (Recommendations for the authors):

I believe the proposed method in this paper is very novel and timely for the neuroscience community. The paper is well organized and written very clearly. I have some comments that might improve the quality of this paper.

1. Impact of Noise in the phase estimation. Although there is a section in the Discussion related to Noise in Signal, the authors did not address the impact of Signal to Noise Ratio (SNR) on the performance of their algorithms. I think this will add value to your algorithm, specifically because the Kalman Filter can be much more reliable than other methods in this context.

2. Specifications of the Kalman Filter and its robustness. specifications of the Kalman filter (KF) should be described in the Method Section. For example, the choice of state and observation covariance matrices (Q and R) should be clarified. In this regard, the authors can discuss the robustness of the KF in phase estimation.

3. For in-vivo data, how the performance of the estimated phase might be compared to other methods (used in the simulation study)? It can be helpful to visually compare the estimated phase calculated by SSPE and other methods which were used in the simulation study.

Reviewer #2 (Recommendations for the authors):

I think the manuscript can be improved by

1) clearly demonstrating the advantage of using this method for exploring the link between rhythms and behaviour and for phase-locked stimulation. The authors should separate applications that require real time phase estimation from those that can be performed offline using acausal methods.

2) Building on my previous point:

– In figure 2, proposed method clearly outperforms others for signals generated using the "state space model". How representative is this for in-vivo recordings?

– In figure 4, it is demonstrated that other methods cannot track phase-reset, however, is this offset sustained or is it a transient slip in phase estimation for one cycle. In other words, if we zoom out in time, do the other methods converge back to true phase? And if so, when would it be critical to track phase-reset for one cycle?

– The performance of SSPE should be demonstrated with respect to other methods for in-vivo data (figures 5 and 7) so that the reader can evaluate the utility of this method.

3) The paper is well written but comes across as very technical. Readers from non-technical backgrounds may struggle with following some of the concepts. This could be improved by linking the method back to applications and in-vivo data more, and also by reviewing the language used in the methods segment.

Reviewer #3 (Recommendations for the authors):

1) Credible intervals

An interesting aspect of the manuscript is the possibility of computing credible intervals, making it possible to establish bounds on time points when the phase can be estimated with sufficient accuracy. In previous approaches, this is usually done via an amplitude threshold, with the assumption that a high amplitude will also result in high phase estimation accuracy. In Figure 6 the authors therefore study the relationship between amplitude and credible intervals. It is tough to interpret this evidence; the argument is that for an amplitude threshold using the 65th percentile the range of credible intervals is from the minimum to maximum possible. But looking at the major bulk of probability mass, it's centered around intervals with an acceptable looking range? Could more details regarding computation of confidence intervals be provided, e.g. are they symmetric? Figure 6C is a scatter plot with lots of points that are correlated, maybe it would be good to visualize this in a different way reducing the number of points per cycle? Can the credible intervals be related to error in degrees? They look pretty negligible in the left part of the figure (given that the real-time procedure also introduces a lag, Figure 8B),is the plotted x-range the relevant one? How does SNR/amplitude relate to phase accuracy to credible intervals? If the spread of credible intervals can be largely explained by amplitude (aka high correlation between credible interval width and amplitude), then maybe this is not such a big factor?

2) Slow drifts

A practical reason why existent algorithms rely on buffering is the frequent existence of slow drifts in the data, for which detrending needs to be applied. For the EEG data, the following methodological detail of the current approach is given "Before real-time phase estimation, we high-pass filter the data at 0.5 Hz to remove slow drifts." This procedure is not possible when estimating the phase in real-time. The authors claim the benefit of their approach is the absence of needing buffers, but in the light of this I am not sure about whether this is the case. In the discussion, the authors discuss the possibility of modeling the slow drifts via an additional rhythm in the state space, but state that long segments of data are needed for this. In my view, this is a crucial aspect of any algorithm targeting real-time phase and more information and analysis resolving slow drifts would greatly improve the actual applicability of the present approach.

3) Data generation process and simulations

I find some of the simulations not sufficiently motivated from a physiological perspective.

– Two simultaneous rhythms with nearby frequencies: In this scenario the authors simulate the signal as a summation of two sinusoids with a frequency offset with a fixed phase shift. This will result in a signal with amplitude modulation with the envelope given by the difference of the frequencies, resulting in the appearance of oscillatory bursts. I would argue that for physiological signals that present like this, it is not of interest to track a single frequency in this signal, as e.g. the trough phase of this compound signal corresponds to a specific physiological state. I would also suggest showing the amplitude for this case in Figure 3. Possibly the simulation could be modified to be better physiologically motivated, as they are certainly cases where there are neighboring rhythms which present on the same electrode through volume conduction, but it is unclear (but would be of interest) to me if the proposed method could be helpful in this case.

– From my perspective phase is only well-defined if there are clear-cut oscillatory bursts. In that sense, the signal given as an example in Figure 2A iv does not have clear-cut oscillatory states, with no clear spectral peak and the true phase (blue curve) changing rapidly. The authors show that the algorithm performs well here as this is exactly according to their data-generating process assumptions (e.g. Figure 2C right-most), whereas for the other algorithms errors accumulate especially in fast phase changing periods. In my view, this simulated situation conceptually does not capture processes that are relevant to investigating neural oscillations in the brain, which would follow a conceptual model more similar to: multiplicative 1/f contribution * oscillator + additive 1/f contribution, so that presumably corresponds to the presented filtered pink noise case here. Can the authors clarify the motivation for this simulated case?

– The authors speak of broadband oscillations, for instance relating to the mu-rhythm (l. 554). In my view this is a narrowband oscillation with a clear peak judging from the power spectrum, with the broadness of the peak influenced by the presence of strong amplitude envelope modulations. Can authors clarify their criteria for defining an oscillation as broadband, in my view this is non-standard terminology.

– One limitation of band-pass filtered approaches that the authors mention is non-sinusoidality (l. 48). In my view, this is manifested in differences in waveform shape, e.g. the arc-shape of the mu-rhythm in Figure 7D. It does not seem that problems in phase estimation for this type of signals (e.g. non-uniform phase-velocity) is addressed by the method as the estimated state does not capture the arc-shape of the rhythm. Can the authors clarify in what way they contribute to resolve this limitation?

4) I would welcome additional details in the text regarding following methodological procedures, which should yield a more self-contained manuscript:

– While bandpass filtering and Hilbert-transform are quite common operations for electrophysiologists, a state space approach may be unfamiliar to the typical reader. Possibly it would be helpful to have clearer paragraphs describing the framework (aka rework l. 98ff), I think the attempt here was to first explain the procedure without formulas, which appear further down, I am not quite sure that this succeeded in providing clarity. Maybe it would be helpful to first make an example with only 1 rhythm, so that dimensionality of the involved entities is not as complex as for tracking N rhythms. Maybe it would also be helpful to extend Figure 1 with a conceptual diagram. How is the number and frequency of oscillators chosen for empirical data?

– E.g. regarding the parameter estimation the reader is referred to the supplementary material of Soulat et al. 2019. Can an intuition about this procedure be given? I find this interesting in the context that a quite large range for expected computation time is given (2-100 s, l. 573). Can the authors comment on factors influencing this? Maybe a more detailed description of the procedure will be helpful for understanding this.

– Currently descriptions of the comparison algorithms are lacking, e.g. what is the general procedure and difference between Zrenner and Blackwood algorithm, what are the crucial parameters here? The authors give code-accessibility as the main reason for selecting those two specific instances. Because recently a lot of different methods (mostly variants involving band-pass filtering) were proposed for estimating the phase in real-time, maybe those 2 selected ones could be better discussed in the context of others in the literature.

– typo, l.55 extant -> existant

– the dotted lines for phase estimates may be not optimal visually (e.g. Figure 6B), maybe shading of credible intervals would look nicer?

– Can the authors provide more details on how the power spectra were estimated? The simulation ones look like Welch's method and the data ones like multitaper were used.

– If I understood correctly, the employed two-sided t-test is calculated using lots of correlated data points (using all time points in an interval), resulting in reduced degree of freedom. I think the evidence that the SSPE approach works better here is actually strong, but the t-test looks slightly weird because of wrong degrees of freedom, distracting from the result. Maybe the information from table 1 can just be plotted in a distributional way, more like Figure 2C?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A State Space Modeling Approach to Real-Time Phase Estimation" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been considerably improved and this interesting paper provides inspiration for the field, bringing state space models and phase estimation for neural recordings together. However, there are a few remaining points that are mainly related to presentation results that could be improved. It will not be sent back to the reviewers for final evaluation.

Reviewer #3 (Recommendations for the authors):

I thank the authors for extensive replies to my comments, which have clarified many aspects and made the method description more accessible. I like the new waveform shape figure showing the simultaneous tracking of the base + harmonic frequency. I find the SSPE method interesting from a principal perspective, but am not yet sure in what way the performance of the algorithm is superior to other algorithms in physiologically relevant cases. My remaining comments:

1) Plausibility of simulations R3.Q4

– The state space model simulations (Figure 2A.iv) generating model are not a common data generation model for the rhythms the authors actually investigate (theta and mu). The newly added citations are for the γ-rhythm (and a quite obscure EEG paper). -> I would say this is not a generally accepted data generation model for mu and theta. The fact that the SSPE performs well on data generated from the exact state space model does not seem to entirely relevant for the chosen application, with the simulation lacking stability in cycle periods that is present for mu and theta. Possibly, a note can be added in the Discussion section in the narrow-band vs broad-band signal section, reflecting on broad-band phase would be beneficial.

– The filtered pink noise seems to result in a broader spectral peak (green line in Figure 2B.ii) than is present in the empirical data. As the band-pass filter parameters of the alternative algorithms are possibly adjusted for more narrowband signals, not adjusting the bandwidth before e.g., doing a Hilbert transform may yield an unfair comparison. Can you comment on that?

– My suggested approach using multiplicative 1/f corresponds to the second of the simulations provided by the authors in R3.A4. To clarify this, I attach some python lines at the end to show a simulated signal, if there is interest (parameters to be adjusted). The phase estimation errors in the provided plot in the response seem really low, so maybe the oscillatory SNR is too high for this simulated case (also the amplitude modulation is not really prominent?) I find it confusing that the SSPE method does not yield any benefit here. I am not requesting specifically for this type simulation to be included, but I would like to understand generally the conditions under which SSPE yields better results than the alternative algorithms.

From my understanding, SSPE should yield benefits for phase estimation in intermediate SNR ranges, but at the moment the authors have added more evidence that all algorithms show very similar behavior at high SNR (Figure Supplement I for Figure 7 and 8) and the simulation type provided in Figure 5 has some issues with phase stability as it is filtered pink noise (see comments above) and the modelled SNR range (there is not much change in phase estimation errors which I would have expected to vary with increasing SNR).

R3.Q3:

I can acknowledge the scenario of the two simultaneous rhythms with nearby frequencies which the authors attribute to two different rhythms instead of seeing as amplitude modulated bursts. For this case, maybe the modeling scenario would be more general, if the rhythms had varying phase lag (random for each trial) instead of a fixed phase lag (pi/4), which seems like the case in which the rhythms are most easily distinguishable.

2) The relationship between credible intervals and amplitude measures. R3.Q1.

– The authors argue for a dissociation between credible intervals and amplitude values, with evidence provided by e.g., Figure 7. Given the nature of the data, with oscillations occurring in bursts and not as a continuous oscillation, I am wary of phase estimates for time points where there is no oscillation (e.g., for the theta data, oscillation probability is heavily dependent on animal speed and there will be periods in the data without an oscillation). My main point here is that credible intervals seem to have a correspondence to amplitudes in a range where an oscillation is clearly present (high amplitude) and phase is not defined when an oscillation is absent. Sure, the acausal FIR will return a value for every time point, but it's not necessarily meaningful in a physiological sense. Taking this as the ground truth is problematic for the credible interval and amplitude measures dissociation. For instance, is there a discernible oscillation for the data in Figure 7 for an amplitude criterion > 65th percentile? Is a wide or narrow credible interval around a value that is not defined meaningful?

Figure 7C is a scatter plot with lots of points that are correlated, maybe it would be good to visualize this in a different way reducing the number of points per cycle

possibly by subsampling or a 2D histogram. In the current presentation, the plot basically just shows the range of the data, amplifying low-occurrence data points.

This suggests that, at low SNR, an arbitrary amplitude threshold (e.g., amplitude > 1) would eliminate all data at SNR=1, and preserve all data at SNR=2.5.

Typically (e.g., in the Zrenner studies), amplitude is defined as a relative criterion, e.g., with percentile threshold or mean amplitude +- 2.5 SD using some training interval, so I am not sure about this argument.

– We find that fixed amplitude thresholds produce wide ranges of credible intervals (Figure 7C.ii). This is especially apparent at lower amplitude thresholds; choosing a threshold of 65% results in credible intervals that range from 0.042.29 (minimum) to 174.75 (maximum) degrees.

Can authors list the 95% range here, rather than min/max?

– Figure 5: Can a spectrogram can also be plotted in this figure?

I would expect the height of the spectral peak over the 1/f-contribution to vary here.

3) Code availability

I wanted to check the used bandpass filter parameters (since it's not described for the Blackwood algorithm) and noticed that the linked repository does not feature the code to recreate the plots in the manuscript, possibly it would be helpful for other researchers to provide that, also for comparing to other algorithms in the future.
