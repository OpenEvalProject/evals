# Peer review - Round 1

Editors:
- Richard B Ivry, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53246.sa1](https://doi.org/10.7554/eLife.53246.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Skilled movement involves the interplay of feedforward and feedback processes. A large body of evidence has provided compelling evidence of the critical role for the cerebellum in feedforward control. In contrast, cerebellar involvement in feedback control has been more controversial. In this study, Zimmet and colleagues show that individuals with cerebellar ataxia are able to use visual feedback in a similar manner as control participants. However, unlike the controls, they were unable to compensate for delays in feedback processing-thus, their inability for predictive control resulted in delayed feedback. Interestingly, if the feedback was phase advanced in a virtual reality system, the patients' performance improved, providing a nice demonstration of the interplay between feedback and feedforward processes.

Decision letter after peer review:

Thank you for submitting your article "Cerebellar patients have intact feedback control that can be leveraged to improve reaching" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Richard Ivry as Reviewing Editor and Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Max Donelan (Reviewer #2); Frederic Crevecoeur (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript investigates the role of the cerebellum in feedback control, comparing the performance of individuals with cerebellar pathology to a matched control group. The patients failed to exhibit predictive control (feedforward control), instead showing a strong dependency on the visual feedback (feedback control). The authors simplified a complicated control system intro tractable models, evaluated the model across different topologies, and designed experiments to distinguish between feedback control in the absence of prediction, and feedback control that leverages prediction. Their findings support the hypothesis that while, control participants could combine proprioceptive feedback with an internal model to have a prediction of the body's state and/or the target motion to allow for zero-delay tracking, the patients with cerebellar damage could not. The final experiment provides a strong and courageous test of these ideas, using a manipulation that partly corrected for the patients' deficiencies by shifting the visual information in an idiosyncratic manner to optimize predictive control to the visual feedback. The manuscript is clearly of great interest as it provides valuable data and insight with respect to cerebellar-dependent motor impairments.

Essential revisions:

1) Issues with Experiment 3: Is the experimental manipulation about the manipulation of the delay, or does it become one of a manipulation of gain? If you would add acceleration feedback to a response that consists of sines (as in experiments 1 and 2), you add a signal that is 180 degrees out of phase, which simply leads to a reduction of gains (not a correction for delays as claimed, see the Introduction, last paragraph). For single point-to-point movements, adding acceleration could make sense, but does this make a clear prediction relevant to the goals of the current study? It seems as if it also here acts as a change of gain. The authors show that the optimal amount of acceleration (and thus the gain) is idiosyncratic. This corresponds with idiosyncratic biases in visuomotor matching that have been reported in the literature (e.g. in Rincon-Gonzalez et al.,(011, and Kuling et al., 2017). Gain control may be in intact in the patients (or experiment may lack sensitivity to detect gain control given ease in learning these).

2) Complexity of the analyses. These analyses are smart but difficult to follow and there may be alternatives that either simplify the presentation or are better suited to the questions under consideration.

a) The authors argue that the use of visual feedback introduces a delay. Instead of assessing the delay, they present the results in terms of a frequency-dependent phase-lag (illustrated by phasor plots that require some explanation). It may be simpler to regard the observed phase lags as corresponding to a delay of a bit more than 100 ms for al frequencies. The same argument holds for switching between the frequency domain and spatial analyses.

b) The models would benefit from more explanation. In particular, it requires a big leap of faith from the reader to be willing to accept that the controller and plant can be modeled as a simple integrator. It required in part, reading the McRuer and Krendel, 1974 paper. But requiring readers to seek it out, read it, and understand it gets in the way of the digesting the present manuscript.

c) It took a while to understand why the acceleration term is like prediction. Others may benefit from a clear explanation in the Introduction that builds their intuition.

d) The manner in which you chose the appropriate gain on the acceleration term may suffer from post-hoc selection bias. This concern was ameliorated by Figure 7C and Figure 8 which show clear systematic effects of this gain on dysmetria.

e) The developments are based on a simple model which ignores much of recent work on feedback control and delay compensation: state-of-the-art control models consider state-feedback control (Todorov and Jordan, 2002), and a lot of work has been done to characterise feedback functions and their respective latencies (Scott, Trends in neurosciences 39 (8), 512-526). Delay compensation has been studied in this context following visual perturbations (Izawa and Shadmehr, 2008) and mechanical perturbations (Crevecoeur and Scott, 2013). Recently it was proposed that in theory, a faulty delay compensation within the stability margin can produce oscillations in eye and arm movements, but these two operations are needed in both visual and limb motor systems (Crevecoeur and Gevers, Neural computation 31 (4), 738-764). While recognizing all models have limitations, the authors should consider this framework. The reason is that this literature has found consistent delays of ~100-120ms for the visual system, and ~50-60ms for somatosensory feedback. These are physiological measurements so if there is no reason to suspect a change in conduction velocity for cerebellar patients, these numbers could be used in in a state-feedback control model. This concern is based on the fact that the calculated delays by fitting the McRuer integrator with a Smith predictor seem off (170ms). If the model structure does not correspond to the physiology, the fitted parameters can be precise but inaccurate. We realize that considering state-feedback control model and delay compensation in the framework of LQG is more complex. However, this may be justified as this framework has been used extensively to model reach control and feedback responses to mechanical and visual perturbations.

f) The previous study by Kurtzer on long-latency control in cerebellar patients (Kurtzer et al., 2013) was not used in this study since it did highlight a reduction in response gain specific to the long-latency motor system, which is a valuable data for modelling purposes.

3) The results show that the patients lack delay compensation for the predictable visual stimulus. The question arises as whether the problem was delay compensation with respect to their body movements or with respect to the external world. The behavior of Exp 1 is used to conclude that the patients had impairments in their estimate of limb state. This conclusion seems indirect and it is not based on a limb perturbation. The authors imply that delay compensation is associated with proprioceptive estimates only, and that it is not expected to occur in the visual system. The associated rationale is not clear. It would seem that compensation for delays in the visual system is also necessary for controls to track the predictable target. Can we conclude that feedback control is intact, or is this specific form of visuomotor control that is unaffected? Possibly feedback control in the proprioceptive system is also intact, what seems to be missing is delay compensation, but it was not demonstrated whether the faulty delay compensation was in the visual or somatosensory motor system. The lack of predictive control could be in the visual system based on the tracking experiments. The deficit was attributed to predictive control of the limb based on indirect fitting of the model, but the rationale for this is unclear.

Related to this issue, the theoretical background suggests a role of the cerebellum in predicting the behavior of one's body (internal model). It is unclear how the experiments test this idea. Experiments 1 and 2 differ in the predictability of the stimulus, not the predictability of the body. The different behavior of the cerebellar patients in experiment 2 (and not in experiment 1) would indicate a problem with the prediction of the world, rather than of the body.

4) It was suggested that cerebellar patients had intact feedback control based on experiment 1. This is likely an overstatement: qualitative differences were visible in the traces of Figure 4 and the interaction between conditions and groups was associated with p = 0.07. Thus, it could be that the relatively low sample size does not allow to conclude for differences based on the analyses suggested.
