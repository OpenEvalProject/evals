# Peer review - Round 1

Editors:
- Fred Rieke, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57484.sa1](https://doi.org/10.7554/eLife.57484.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Neural variability determines coding strategies for natural self-motion: implications for perception and behavior" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that substantial additional analyses and clarifications are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

The dichotomy between faithful and efficient coding neurons received a good deal of attention in the consultation among the reviewers. All of the reviewers felt that more needed to be done to clarify and to test this distinction. For example, it is not clear how the decoding errors could be larger for the efficient coding neurons if they really are efficient. Related to this point is whether the efficient coding neurons are simply noisier, and if the whitening comes at the expense of higher noise. Several additional specific points raised in the individual reviews are related to this point. I should emphasize that in consultation the reviewers felt more strongly about this point than is reflected in the individual reviews, and whether you are able to deal with it clearly and effectively will be critical to a re-evaluation of the paper.

Reviewer #1:

This paper follows a previous paper from some of the same authors exploring coding of naturalistic inputs in the vestibular system. The previous paper showed that the combination of stimulus power spectrum, neural filtering and noise led to spectrally-flat ("whitened") responses in one class of vestibular neuron. The present paper extends this analysis to two other types of vestibular neurons, concluding that they show considerable heterogeneity in the degree of whitening. I had several concerns about the analysis/presentation:

Filter calculations and non-Gaussian stimuli:

The paper relies on naturalistic head movement stimuli and uses these for the coding analyses. Some of the calculations presented, however, are valid only for gaussian stimuli. This is particularly true of the linear-nonlinear model and more broadly the construction of the transfer functions. Thus, it seems that the filters extracted could be impacted by the correlation structure of the stimulus. This is a key issue for interpretation of the paper.

Adding noise and optimality:

Neurons that whiten the stimulus are referred to as optimal, while other neurons that encode the stimulus faithfully are referred to as non-optimal. If much of the whitening comes from noise in the resting discharge, however, it does not seem that the "optimal" neurons are really optimal – i.e. they would encode better with non-white responses and less noise. This issue recurs throughout the paper and bears on the tradeoff of optimal vs faithful coding.

How does coding in low and high noise neurons differ:

It would be very useful to see a separation of differences in encoded signal and noise to differences in response power spectra. For example, in Figure 2D, how much of the power spectrum in the high variability neurons is due to noise and how much is due to signal? Related, is the spectrum of the encoded signal similar in high and low variability neurons?

Related to this point, in subsection “Neurons with lower variability faithfully encode the detailed time course of naturalistic self-motion stimuli”: the observation that neurons with low variability encode the stimulus more faithfully than those with high variability is not too surprising. It would help to analyze the nature of the coding – e.g. are there systematic errors or bias in encoding in the case of the high variability neurons? Or are both low and high variability neurons encoding the same temporal frequencies, just with different signal to noise ratios?

Reviewer #2:

This is a very nice extension of previous work, now including more classes of vestibular neurons (PVP/EH/VO), whereas only VO were published on in the earlier work. Some excellent hypotheses are outlined about how different types of signals (faithful stimulus encoders versus efficient whitened outputs) are used in different behaviors. This work nicely connects input statistics to encoding with an eye on behavior.

I have just a few main points that I think would enhance the presentation of these results in the manuscript:

1) A main claim of the paper relies on the dissection of neurons in to high and low CV cells, but it really doesn't seem like the data support a statistical distinction between classes, Figure 1D. Specific questions and comments are:

a) Something else needs to be shown here in Figure 1, like the overall histogram of CV, and the accompanying text should not state that there were significant differences amongst these classes of neurons, then point to a figure in which almost all group comparisons are not significant. This just needs to be made crystal clear throughout: this is a hard-fought-and-won dataset that shows some differences amongst neurons, but there aren't enough data to make claims about broad differences between PVP/EH/VO classes, except for the CF result for PVP vs. EH/VO. The result that the PVP class has a lower CV than EH seems like a very small effect size.

b) This appears to be mostly a paper about high versus low baseline variability (though it would be nice to make rate-matched comparisons, next comment), not about differences in response classes. Put another way, it seems like all classes contain neurons that follow the stimulus and some that perform temporal whitening. The first figure could be reformatted to highlight that more clearly.

c) What is the main claim about subtypes, if the above true? Is it that each type needs a "faithful encoder" channel and a "whitened" channel? It seems that this is exactly what is presented in the Discussion, but then the claims about differences in the EH population and a longer discussion about the VO subtype seems out of place, if that's true. Perhaps PVP can be separated by CF, but the distinction between VO and EH neurons in these data seem more tenuous.

2) Do these results hold if high/low variability neurons are compared in pairs that have similar firing rates?

Reviewer #3:

The authors record from three classes of central vestibular neurons (PVP, EH, VO), which project to different areas. They show that functionally, neurons in each of the classes can be divided into "high variability" (HV) and "low variability" (LV) neurons based on characteristics such as CV of the ISI. HV neurons perform decorrelation (=whitening) consistent with efficient coding, while LV neurons perform "faithful encoding", i.e., permit a precise linear reconstruction of the stimulus. The suggested implication is that this division makes sense in the light of downstream computations: e.g., control of eye velocity in VOR favors LV type encoding, as they show computationally.

I find the paper well-written and well-argued, and would support publication after revisions. I do not see any major technical flaws, but recommend one extra analysis as detailed below.

1) I was confused in how precisely the authors define "High variability" and "Low variability" classes. They look at the FR and CV statistics, and also at the power in the natural frequency band, and all these statistics can be done on natural stim or in the resting state. I presume the classification is based only on the CV in the resting state. If that is true, this should be said explicitly (and if you use any thresholds to decide what is "high" and what "low", please specify). Please clarify.

But if the variability is "continuously distributed", then the HV and LV neurons (used as the examples) are only at the extreme ends of that CV distribution. Can you mark where the example neurons of 1B are in Figure 1C (and perhaps in other relevant figures)? For how many of all your neurons do you then see such clear differences between two encoding schemes, what are the neurons in the middle of the CV distribution doing and what is your functional expectation for them? Figures 2E and 3C show the "interpolation" as a function of CV in terms of whitening and CF, showing this continuum of behaviors, but the story seems to tend to much towards a black and white dichotomy between the two extreme behaviors. I would suggest rewording to make clearer that this is not a dichotomy.

2) Figure 2E and 3C show a pretty strong dependence of WI and CF on CV. If the baseline firing rate (that the authors also quantified in Figure 1) is included as an additional explanatory variable for CF in addition to CV, do you see a much better prediction of CF or WI? For example, are low-CV neurons that have a high CF in Figure 3C the ones that have higher firing rates?

3) When the authors interpret the function of HV / LV neurons in Figure 3 and 4, suggesting that LV neurons are better for VOR, they imply that the system is choosing to use one or the other class. But I imagine the population, which is mixed and has a full CV spectrum, is input to the neural integrator. In fact, it would make lots of sense if I look at Figure 3A, to interpret LV neurons as tracking the slower changes in the stimulus well, whereas HV neurons emphasize faster modulation. A system that reads out both types of neurons (or the full heterogenous population) is thus expected to perform much better in reconstructing the stimulus and controlling the eyes.

I suggest that the authors test this hypothesis by linearly decoding from two or more neurons. In the easiest scenario, they could take one LV and one HV neuron (maybe examples in Figure 3B) and jointly linearly decode the stimulus. This could be compared with the decoding based on two LV and two HV neurons, to see if the major benefit comes from combination of the two classes. One could reconstruct from even more neurons if that is feasible, to see how the reconstruction depends on the number / type of neurons (cf. Marre et al., 2015), but I don't consider necessary for resubmission. If, however, it turns out that the authors discover a large benefit to decoding really from two classes (LV + HV) jointly, I think the interpretation and discussion needs to be modified: heterogeneity is beneficial since it permits precise full stimulus reconstruction, and so VOR control should not only be done with low variability neurons.

An additional discussion point that the authors may want to consider is that LV neurons can be decoded with more instantaneous filters, whereas decoding from neurons (like HV) that decorrelate requires decoding filters that are extended in time; this may cause delays in the reconstruction and is possibly detrimental if the sensory-motor loop in VOR needs to be fast?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Neural variability determines coding strategies for natural self-motion in macaque monkeys" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor) and Fred Rieke (Reviewing Editor).

The manuscript has been improved but there are some remaining issues that need to be addressed before we can make a final decision, as outlined below:

As you will see below, reviewer #3 has some remaining substantial concerns. In consultation, both reviewers and the Reviewing Editor agreed that these points are quite important and dealing with them fully will be essential if we are to proceed with the paper.

Reviewer #2:

I feel that the paper is much improved after revision. Many of my claims were addressed, as were several of the other reviewers. The Gaussian shape of the naturalistic inputs to this system were clearly a point that needed more emphasis and explanation. I'm glad that's been addressed fully.

The distinction amongst classes of neurons is now much clearer, as is, I believe the Abstract and Results section.

Reviewer #3:

The authors have addressed many of my concerns and their additional analyses have clarified the situation. Especially important are the new quantifications that make it clear that low-CV neurons actually transmit more information (thus better stimulus reconstruction) but do not whiten, whereas high-CV neurons transmit less information due to higher noise power, but their output spectra are white.

I have a two outstanding comments:

1) The authors respond that the self-motion marginal PDF is ~Gaussian with low skew. Even small skew can cause distortions in RF estimates (Meyer et al., 2016); more importantly, the necessary condition for the consistency of RF estimates is spherical symmetry, i.e., P(s) = P(-s) where s is the full stimulus waveform, not just a single marginal value (which is what they report). I understand the authors are faced with the empirical issue of a naturalistic stimulus, so I just ask to clarify precisely the conditions for consistent estimation.

2) Perhaps most importantly, although it may appear nitpicking, I would like the authors to go through the text and be very careful about the interchangeable use of "optimal coding" and "whitening", for their high-CV class neurons. I agree that these neurons produce, to a good approximation, a whitened output. I also agree that there is a regime of efficient coding theory, but by no means the only operating regime, where the theory predicts as optimal a match between stim statistics, noise, and the neural filter that generates white outputs (van Hateren, 1992a): specifically, this happens at high SNR, where the "input noise" Np (in van Hateren paper) is vanishing (Equation 25). But this is not the only regime of optimality. When input noise is high, filters are proportional to (sqrt of) signal spectrum (Equation 30), in this case neurons would not whiten but still be optimal.

In your analysis, you have access to channel noise (Nc in van Hateren notation) which you empirically equate by resting discharge spectrum. But I am not sure if you have direct access to the input noise, Np (I am not familiar enough with the system to know what this would constitute). While the traditional regime of application of efficient coding theory is the regime where channel noise dominates over input noise and thus the optimal prediction is whitening, there are cases where the system is not in this regime (retina at low light, or processing of higher order spatial textures beyond V1).

As a consequence, it could be that low-CV neurons are or are not optimal even in the sense of efficient coding, depending on noise constraints we do not know; but they for sure don't whiten.

I would thus recommend being very precise about the claims, e.g., in the Abstract, instead of saying that the neurons did not optimally encode…, I would say they do not whiten. I think it is fair to point out in the paper that the typical regime of efficient coding predicts whitening (van Hateren et al.), but it may be going beyond what you can demonstrate to claim that absence of whitening means non-optimal coding in low-CV neurons. I think that these world-level corrections, to focus on non-whitening vs whitening rather than optimal vs. non-optimal encoding, should not detract from the main message of the paper, and provide an interesting discussion point about optimality.
