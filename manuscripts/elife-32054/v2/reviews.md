# Peer review - Round 1

Editors:
- Saskia Haegens, Columbia University College of Physicians and Surgeons United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32054.011](https://doi.org/10.7554/eLife.32054.011)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Stochastic Resonance Mediates the State-Dependent Effect of Periodic Stimulation on Cortical Alpha Oscillations" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Saskia Haegens, served as Guest Reviewing Editor, and the evaluation has been overseen by Sabine Kastner as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Caroline Di Bernardi Luft and Vincenzo Romei.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript by Lefebvre et al. addresses how intrinsic oscillatory activity affects the brain's susceptibility to rhythmic transcranial stimulation, using a computational model of the thalamocortical system. Systematically manipulating stimulation frequency and amplitude, as well as the state of the network during stimulation, ranging from rest to active task engagement, the authors observed evidence for stochastic resonance. Cortical spiking responses were phase locked to the rhythmic stimulation only for intermediate values of thalamic drive; below this drive, endogenous network activity suppressed cortical entrainment, while above this value noise decreased the saliency of the evoked responses. The reviewers deem this paper interesting and relevant and believe it could be further strengthened by expanding on more realistic scenarios and physiological plausibility and referring directly to existing work empirically providing such links.

Essential revisions:

The reviewers raise a number of concerns that must be adequately addressed before the paper can be accepted. We suggest to expand the discussion of the model further by considering realistic (experimental) scenarios including rhythmic sensory stimulation and different neuromodulation protocols:

1) The authors should clarify the simulated stimulation intensity and how it compares to the stimulation intensities used in experimental studies with humans. It is not clear how strong the simulated stimulation was, which is key if we want to test this model's predictions using weak vs. strong currents (e.g. tACS vs. TMS). The authors must explicitly state whether the intensity was sub or supra-threshold and how it compares to the current reaching the brain in studies with humans.

2) Do the authors think the results presented here are exclusive to cortical stimulation approaches, or would this (potentially) also hold for "entrainment" type sensory stimulation paradigms? In that light, it has been shown recently (Keitel et al., 2017 NeuroImage) that the temporal structure of natural stimuli is hardly ever fully rhythmic but possesses certain rhythmic structures. Examining periodic brain responses elicited by strictly rhythmic stimulation might therefore represent ideal, yet isolated cases (neurostimulation being one of those). Therefore, a first question here is what kind of task state the system has been tested on? Have the authors thought of testing the equivalent of a rhythmic sensory input that could induce a rhythmic thalamic drive? How would this translate in terms of cortical oscillatory activity? The second question is whether a quasi-periodic stimulation (think about speech) would exert the same impact on the endogenous ongoing oscillatory activity in the computational model presented?

3) The discussion could be improved by using the findings to explain results from empirical work. For example:

– A study with intracranial recordings in humans (Ezzyat et al., Current Biology 2017) observed that the stimulation only boosted memory on trials in which the expected oscillatory pattern was not present, a finding which could be nicely explained by the current model. The authors might go a bit too far saying that stimulating at rest has no effect due to the strong endogenous frequency, as this is not entirely supported by their evidence (which seems to suggest that the stimulation frequency has to be much closer to the endogenous frequency than at higher thalamic drive). Possible effects on LTP and the aftereffects are also not taken into account by the model nor were they tested, so it would be good to see some discussion on how their findings connect to those, or to address it as a limitation.

– A recent MEG tACS paper by Minami and Amano, 2017 showed how stimulating at slower or faster alpha frequencies than the individual alpha via tACS directly modulates the individual alpha peak itself, which becomes aligned to the externally imposed rhythm. Interestingly, the authors test their model during a visual task (which is impacted by the tACS manipulation), thus perfectly in line with the model proposed here when looking at modulation of the intrinsic alpha peak during task.

4) The authors might want to incorporate the recently published paper by the senior author (Li, Henriquez, and Frohlich, 2017, Plos Comp. Biol.) into their Discussion (and Introduction). Although the study is different, the thalamic model somehow similar and the findings and ideas related. It would be good if the authors could point out the main differences between them and discuss their findings against those. Li et al. observed entrainment depending on the stimulated frequency (e.g. entrainment was stronger when stimulating at γ). These findings could be discussed in the context of whether stimulating at different frequencies would have a different impact on the observed effects.

Furthermore, there were several questions on what the full spectral output of the model looks like, whether this is physiologically plausible, and to what extent the results would hold for other (oscillatory) states:

5) It would be good if the authors could clarify how much variability is in the model and the outputs of stimulation simulations, including in terms of the model's temporal and inter-trial variability, which is especially important considering the non-stationary nature brain signals even under low thalamic drive. It would be good to see measures of variability in order to understand the stability of the responses and how this might affect the outcomes of the stimulation, e.g., does the model result in a constant endogenous 8Hz oscillatory output? Or is there some variation around this central frequency of 8Hz? And if so, how is the model assuming a transition from 8Hz to 11Hz? Would this be physiologically plausible?

6) Figure 3C shows a nice representation of the spectrum during the stimulation at 11 Hz over different levels of thalamic drive. It would be good to see the same figure without the stimulation in order to have an overview of the changes in the spectrum caused by the thalamic drive alone. Additionally, it would be good to see what the EEG spectrum looks like under these different levels of thalamic drive as in rest and task (in Figure 4, without stimulation).

7) "Overall, our findings suggest that modulating brain oscillations is best achieved in states of low endogenous rhythmic activity," Shouldn't that say, "in states of low endogenous alpha activity"? Or do the authors think this holds for other frequencies as well? And if so, which and why, and where is the evidence for such a general claim?

8) It would be helpful to the reader if the authors could clearly define what they mean by "state", e.g.:

– Results section: "or other sensory inputs meant to fluctuate as a function of state"

– Figure 1 legend: "Sensory inputs, whose intensity scales with state"

Also later when discussing "state-dependent effects", use of the term "state" is ambiguous. Do the authors exclusively mean externally imposed experimental state (rest vs task condition)? Or do they also consider intrinsic (spontaneous?) brain state? Or both? Especially considering these two are not independent (e.g., spontaneous state might affect the response to external input), this should be discussed. In that light: "Visual inputs (or other sensory inputs meant to fluctuate as a function of state) are sent through the LGN to cortical areas for further processing". Do the authors mean to imply that thalamic input is unmodulated? i.e., does LGN, in this model, simply relay visual input? Or is LGN activity also modulated based on intrinsic brain state? All of this should be unambiguously spelled out in the manuscript. It would also be helpful to have the operational definition of task and rest states ("the rest state – which we have defined as a regime of weak inputs to the thalamus, and the task state – where thalamic drive is high") in the Introduction or early in the Results section.

9) In addition to a qualitative representation, a quantitative approach specifying the extent to which the proposed model is statistically robust could make it a much stronger contribution. The authors should substantiate their claims, e.g., focusing on the results presented in Figure 3: for which thalamic drive values is spike rate correlation significantly different for stimulation vs sham? Similarly, when is 8-Hz power sig different from 11-Hz power? Same for the phase-locking analysis. Figure 3D shows an asterisk for the peak of mutual information, is that signifying any statistical test result? All of this should be quantified using appropriate statistics, and documented in the Results section. (Same applies to results presented in the following figures.)
