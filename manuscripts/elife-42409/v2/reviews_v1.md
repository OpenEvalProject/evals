# Peer review - Round 1

Editors:
- Stephanie Palmer, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.42409.028](https://doi.org/10.7554/eLife.42409.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Nominally non-responsive frontal and sensory cortical cells encode task-relevant variables via ensemble consensus" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers found the work interesting, making a substantive and impactful contribution to the field. They have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Insanally et al. ask how information about auditory stimuli and behavioral choices, are reflected within the spiking patterns of neurons in the auditory cortex (AC), and frontal cortical area 2 (FR2) of rat. The subjects were presented with octave spaced tones, and required to select go/no-go to the presence of a target tone. The work focuses on neurons whose firing rates (PSTH) show no change in response to the auditory stimulus, and/or no ramping activity preceding the decision. The main finding is that timing information in the ISIs of these neurons can be decoded to determine the stimulus and/or choice. The work demonstrates this using a nonparametric decoding method. Specifically, the authors develop a novel method for quantifying the difference in ISI distributions corresponding to different task-conditions. They use this method to provide a posterior probability of task-condition given the ISIs in a single trial. The median decoding performance is moderate but statistically significant, and superior to rate/PSTH-based metrics.

Essential revisions:

1) The paper refers to neurons with no stimulus-dependent firing rate modulation as "nominally non-responsive", however, these neurons clearly do respond to the stimulus (by changing their ISI distributions). Indeed, this is the basis for the decoding analysis. Consequently, it seems like the main result is that the spike timing contains information that is missed if one only looks for stimulus dependence in the firing rates. This is an important point and worth making, but is lost by labeling these neurons as non-responsive. The paper would be much clearer if the authors would be more upfront in the title, Abstract, Results, etc., about what their data show: timing information is there even when the PSTH looks uninformative.

2) The neural network model in Figure 7 lacks some relevance to the data. A rate-based model is used, in which some neurons have stimulus-locked rate modulations, and some don't, and show that inactivating these "non-responsive" neurons changes task performance (presumably due to the effects of those inactivations on the rest of the network through the recurrent connectivity). In the experimental data, however, the authors show that, even when the neurons' rates don't have obvious stimulus dependence, the timing information still does, and any effects of inactivating subsets of neurons are left untested. To make the model relevant, it would need to use spiking neuron models, and recapitulate the basic phenomenon from the experiments: spike timing information is present even when there's no rate information. Alternatively, the authors could do inactivation experiments (e.g., with archaerhodopsin) to test the main prediction of the current model, which would make it relevant. This experiment would probably be hard to do, it is suggested instead that the authors revise or remove the computational model.

3) Relatedly, the conjecture in the last paragraph of the subsection “Ensemble consensus-building dynamics underlie hidden task information”, and again somewhat in the last paragraph of the Discussion, that the NR cells are a separate functional network from the responsive ones contradicts the modeling result. If they are separate networks, silencing the NR cells wouldn't affect the responsive ones. To retain the claim about separate functional networks, it seems necessary to do optogenetics, or some other manipulation of activity, and show that changing NR cells' activity doesn't affect responsive ones. Otherwise, the authors should remove this unsupported claim.

4) The decoder is quite nice, but it makes several independence assumptions that are not borne out in real neural populations. This point should be made much more upfront in the Materials and methods and the Results: stating that this decoder approximates Bayesian inference, by ignoring all forms of correlation. Doing this will ensure that readers don't mistakenly think these simple expressions are exact. Alternatively, the decoder could be updated to include the correlations discussed below.

Correlations: in the subsection “Decoding” the first, third and sixth equations, and the equation in the subsection “Ensemble decoding”, assume that each ISI is independent for a given neuron, which is not generally true, due to AHP currents among other things. The paper also assumes that ISIs are independent between neurons, which is generally not true in simultaneous neural recordings, due to noise correlations, etc.

5) Two other recent works, listed below, showed a stronger form of the claim advanced in the title and Abstract: that neurons with no stimulus dependence can still contribute to the neural code. There, the non-responsive neurons individually contain no stimulus information, although through correlations with other cells, they still contribute to population-wide neural coding.

The current paper's results are distinct from those, since they consider timing information, whereas the other papers consider rates. However, it would be worth making that distinction somewhere in the paper.

a) Leavitt et al., 2017.

b) Zylberberg, 2017.

6) From the Materials and methods (subsection “Training probabilistic model”), it looks like the ISI distributions used for the decoder are recalculated for different time points during the integration period. This is not clear at all from the text in the Results section, but is a crucial point, as it puts severe limits on how a downstream neural circuit could read out this information: the downstream circuit would need to continually change its readout "decoder" somehow. The decoder and analysis still have a lot of merit. They show that the stimulus information is present in the timing, and show how it could be extracted (e.g., for BMI applications). But the time dependence needs to be made clear in the Results section, and the biological plausibility or implausibility should be discussed.

7) Please expand the Materials and methods and Results sections to clarify the following points:

a) Temporal resolution. It seems like the ISI distributions are estimated in a 1s window (subsection “Training probabilistic model”). Sliding by what amount? How is it decided which 1s windows each ISI contributes? Only those that contain the 2 spikes enclosing the ISI? Are predictions are evaluated at the end of each of these 1s windows (so the first prediction is made at second 1 after trial onset)?

b) Clarify where the formula for the likelihood of the full spike train (subsection “Decoding”, last paragraph) is used. From reading the manuscript, it seems that the formulas for updating the posterior only consider likelihoods for a given ISI.

c) Ensemble decoding. Please be more explicit and include a mathematical formula for how the updating of the posterior is done in this case.

d) Subsection “Ensemble consensus-building dynamics underlie hidden task information”, second paragraph. Sliding window for consensus. Is this the same 1s sliding window above? Probably not, given the time-varying nature of the curves and the fact that they start at zero. Please add explanatory text about the time windows used in the consensus section in the methods. Please also describe in more detail how the curves in Figure 8E-H were calculated?

e) Furthermore, is it correct that the Poisson process estimator takes into account the full duration of the stimulus-response interval? There is some asymmetry in the information available with the ISI approach (which takes into account the 1+ seconds following stimulus onset) and the PSTH (which is short, given the 100ms tone). Were there any firing rate differences over the longer interval that would predict responses?

8) Please add a careful discussion of whether the animal's choice can be cleanly dissected from stimulus encoding, particularly given the very high performance of these animals on the task, the long duration between stimulus and response, and the late build-up of stimulus prediction/consensus. There is plenty of literature on the effects of attention, behavior, and working memory on cortical synchronization and timing, albeit mostly in hippocampus. It is possible that the AC responses simply reflect the choice/memory already decided. The manuscript attempts to disambiguate the choice from the stimulus with a log linear regression, but this is dependent upon prediction information from the decoder analysis that itself may already contain mixed information.

9) Title: Please consider revising your title to either omit or make more intuitive what "ensemble consensus" means and to clarify "nominally non-responsive", given the concerns of some of the reviewers about this terminology. One suggested revision "Response timing in frontal and sensory cortical neurons encodes task-relevant variables even when average responses are uninformative".
