# Peer review - Round 1

Editors:
- Maria Chait, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70068.sa1](https://doi.org/10.7554/eLife.70068.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This manuscript reports on two separate investigations. In the first, the authors provide novel evidence from two anaesthesia challenges that the slope of the 1/f structure of the power spectrum of the EEG fluctuates in a manner that tracks the presumed excitation: inhibition (E:I) balance of the tissue generating the EEG signal. Next they show that fluctuations in this slope also covary in systematic and modality- and stimulus-specific ways with behavioral performance on a multimodal attention task. These observations have potential foundational implications for how this previously unappreciated component of the EEG can be interpreted in terms of brain physiology and function.

Decision letter after peer review:

Thank you for submitting your article "Modality-specific tracking of attention and sensory statistics in the human electrophysiological spectral exponent" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Maria Chait as Reviewing Editor and Barbara Shinn-Cunningham as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Bradley R Postle (Reviewer #1); Jonathan Z Simon (Reviewer #2).

The Reviewing Editor and reviewers have discussed the reviews with one another. We agree that the balance between excitation and inhibition in the cortex is an important and timely topic. While the approach you use to uncover the role of E/I in attention is interesting, unfortunately, for the reasons outlined below the data as they stand do not support the study's conclusions. We feel that this is potentially addressable with a revision and the RE has drafted this to help you prepare a revised submission.

Essential revisions:

(1) The results of Experiment 1, whilst compelling, require a delicate interpretation. In particular, it is difficult to make a clear distinction between different anaesthetics in terms of their effect on brain activity (see references provided by Rev3). Given this and the low N, results thus do not fully support the strong conclusions offered by the authors. We encourage the authors to revise based on the specific comments from Reviewers 1 and 2 including:

(a) addressing the pattern of spectral effects (propofol mostly enhancing frequencies below ~20-30 Hz and spreading α; ketamine suppressing α while enhancing lower and higher frequencies),

(b) justifying why modelling this as a 1/f change is appropriate, and

(c) quantifying the differences between the different awake spectra (there appears to be a large difference in the awake spectra between the anaesthetics conditions).

Please also acknowledge the limitations associated with small N and existing literature highlighted by Reviewer #3.

(2) The authors interpret the findings of Experiment 2, where changing the value of the spectral exponent in the stimulus resulted in a similar change in the value of the spectral exponent of the response, but only for the selectively attended modality, as originating from an attention-driven change in E/I balance. However, an alternative interpretation of the findings is that these effects reflect attention-driven changes to temporal tracking of the stimulus waveform. These concerns are potentially addressable in a revision but it would require an entirely new data analysis involving a thorough investigation of potential temporal tracking of the stimulus waveform and an unambiguous result. There will need to be a visual temporal analysis (a la VESPA) and auditory temporal analysis (a la AESPA) for both the attended and unattended conditions. The part of the response explained would need to be subtracted out first, and then the "spectral-exponent-tracking" analysis would need to be performed on the residual. There may be additional subtleties that arise in that process. Given the successes of AESPA/VESPA/TRFs in the literature, this should be considered a simpler explanation of the observed response patterns than dependence on E:I balance. It's the residual (true response minus response explained by this mechanism) that would still need an explanation, and that might be argued to be explainable by E:I balance.

Reviewer #1 (Recommendations for the authors):

Figure 1, it's really hard to see how the slopes change in the way that the authors state. For propofol, visual inspection suggests that the biggest change is a broadening of the α oscillation, such that its inflection starts at a lower frequency and then because the peak is also 'less pointy,' the purple line simply has to fall at a higher rate to catch up with the gray line by ~30 Hz. For ketamine, at the lowest frequencies (lower than α bump) the slope of the green line simply is steeper than the gray, and then again the biggest difference seems to be that the α bump is abolished with ketamine, and so the gray line is then steeper than the green line for the same reason that purple appears to be steeper than gray in propofol plot. Additionally, there's a lot of jitter with ketamine in the 20-60 Hz range. I realize that visual inspection isn't a rigorous way to analyze these data, but on the other hand it's generally preferable for a figure to clearly illustrate the point that the authors are trying to convey. Perhaps the authors should consider accompanying the 'raw' spectra shown here with the same data decomposed into oscillatory vs. aperiodic components, the way that it is done in the Donoghue et al., (2020) paper?

The Discussion section is largely a repetition of what was written in the Intro and/or a restatement of the results with little additional interpretation and contextualization. For example, although it's important to show that α and aperiodic components of the EEG are statistically dissociable, this is only a step toward understanding more fundamental questions such as (a) what are the functions that periodic vs. aperiodic components support? and (b) what underlying factors that give rise to them?

Here are some more specific comments about the Discussion.

"Jointly, these results underscore the importance of 1/f brain activity for perception and behaviour." Don't the authors really mean: "underscore the utility of parameters of 1/f brain activity for studying the neural bases of perception and behavior"? At the end of the day, the major take-home of this paper is that the slope of the 1/f spectrum is a valid index of E:I balance, but it's E:I balance, per se, that is 'important for perception and behavior,' not the slope itself.

"… these results cannot be explained by attention-dependent differences in neural α power (8-12 Hz, Figure 3), commonly interpreted as a marker of top-down guided sensory inhibition." Idling is an important alternative to inhibition that should be acknowledged.

"First, it is important to emphasise that the representation of stimulus spectra in the EEG likely does not trace back to an alignment of oscillatory neural activity and oscillatory stimulus features, commonly referred to as "entrainment" in the strict sense; the presented stimuli were stochastic in nature and without clear sinusoidal signals. However, neurally tracking the statistical properties of random noise time-series might emerge via a mechanism similar to the one implied in the generation of steady-state evoked potentials (SSEPs)." Both of these seem like important points that merit more elaboration. That is, the word "entrainment" tends to be used carelessly and so more detailed and explicit argumentation about why this is NOT an instance of entrainment would be valuable. With regard to SSEPs, specifying some details about this 'implied mechanism' would be helpful. More generally, although entrainment and evoked responses are precisely specified processes that can be shown to be true or not, the same is not true for "tracking," which is just a loose concept that can't be tested and falsified. Can the authors either specify what they mean by "tracking" or else replace it with a more rigorously defined process?

Reviewer #2 (Recommendations for the authors):

P. 4, last paragraph: It is somewhat disconcerting to learn in the Results section that the first study uses a publicly available dataset and the second is wholly separate and from data acquired by the authors. This would be be less startling if it were mentioned in the introduction.

Lines 159-160: As written, this sentence seems to implies that the new results of this paper aren't actually new but merely a confirmation of an old result. It would easier on the reader to more clearly distinguish the previous results (with very strong connections to E:I balance?) from the new findings (where the connection to E:I balance is less direct).

Figure 1B: Would the authors consider using the same vertical scale in both graphs? The overall numbers between the two sets are close enough in value that having two different scales can be distracting.

Figure 1B: The inset graphs are missing axis limits (or scale), and there is no definition of their error bars.

L. 196 and elsewhere: incorrect formatting of numbers in scientific notation, e.g. 7e-6 instead of 7 x 10-6.

L. 189 and following: The description of the stimuli, especially the auditory stimuli is confusing. The phase "to detect regular (i.e., sinusoidal) amplitude variations in streams of amplitude modulated white noise", in the auditory literature would be understood as analogous to "to detect tone pips in noise", but that is not what is meant here. Figure 2 indicates rather that the stimulus temporarily changes from non-sinusoidal amplitude modulated white noise to sinusoidal amplitude modulated white noise.

Figure 2C: Please explain what the circles and lines represent (I presume individual subjects with lines representing identities, but I need toask after seeing Figure 3B).

Figure 3B: Please explain what the circles and lines represent. Do the lines connect the different tasks of the same individuals? The systematic progression of the slopes of the lines seems to indicate that they do not.

Lines 234-235: Getting R2 > 0.84 is a real achievement-it speaks very highly of the importance of the spectral exponent.

L. 383: the phrase "and hence" is confusing here. Maybe "even though they"?

L. 419 and Supplemental Figures: There are two supplemental figures labeled as S4 and none as S5. This reference appears to be to the 5th supplemental figure.

Lines 445-475: This section appears to be where the possibility of temporal tracking is meant to be addressed, but it does not accomplish this (instead only justifying that steady-state analysis does not apply here, which is true). Note also to be careful with the word "stationary". A "stationary process" is one with a fixed spectrum and random phases, which seems to be a good description of the stimulus envelopes/contrasts used here.

Lines 576-577. What does "normalized" mean here? Standard usage is a multiplicative rescaling, not mean-centering. [On the other hand, if the mean-centering was performed on the logarithm (or in dB), then that is equivalent to a multiplicative rescaling of the original waveform.]

L. 616 and following: Regarding the visual modulation, why is the acoustic noise, which had been high-passed at 200 Hz before its modulation, downsampled to 85 Hz (which throws away all the carrier information), instead of just applying the 1/fX modulation directly (downsampled to 85 Hz)? Why the extra complication? Or am I just confused by the multiple uses of the word "noise"?

L. 739 and following: I very much appreciate the careful analysis methods employed here.

Figure S1 caption: This caption would be much clearer if it stated that the graphs and data were identical to that shown in Figure 1 except without normalization. (In its current form it seems almost like an example of an item in a change-blindness study.)

Figures 1B and S1B. There seems to be a lot of inter-subject variability in the Awake case between the subjects who used Propofol vs Ketamine (which should have nothing to do with the awake case). Is that an artifact of changes in the axis scaling (or normalization)? It shouldn't matter since the important statistics are changes within subject, but it is a little disconcerting.

Reviewer #3 (Recommendations for the authors):

The authors based their correlation analysis on 24 participants. While the authors do argue that bigger sample size and cross-validation could strengthen the results, the authors could do more with the data they have.

For example, they can employ a leave-one-out linear regression approach, or use k-folds

With regards to the ERP analysis, the authors appear to be using a cluster-permutation approach to assess any differences between the conditions. Here they do have to keep in mind that such a mass-univariate approach is biased towards longer-sustained responses that have a wide scalp distribution, than the rather more focal discrete ERP components. Please see refer to the following discussion on this topic.

https://projects.iq.harvard.edu/files/kuperberglab/files/fieldskuperberg_psychophysiology_2020.pdf

Finally, why I am intrigued by the idea of the slope of 1/f as being something rather important, I am still not convinced that it could be a residual of other factors in the EEG, such as changes in slow frequency power, or evoked responses. I think it would be interesting to see how much unique variance the change 1/f can contribute relative to the other measures of the EEG.
