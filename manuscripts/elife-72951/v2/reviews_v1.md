# Peer review - Round 1

Editors:
- Naoshige Uchida, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72951.sa0](https://doi.org/10.7554/eLife.72951.sa0)

To characterize physiological properties of dorsal raphe serotonin neurons, the authors applied the approach called an augmented generalized integrate-and-fire [aGIF] model, which incorporates a relatively small number of salient biophysical properties of a specific neuron type, and whose parameters are optimized based on voltage dynamics obtained experimentally. The results showed that after-hyperpolarization and A-type potassium currents, in combination with heterogeneous feedforward inhibition from local GABA neurons, give rise to a derivative-like input-output relationship in serotonin neurons.


---

# Peer review - Round 1

Editors:
- Naoshige Uchida, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72951.sa1](https://doi.org/10.7554/eLife.72951.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Temporal derivative computation in the dorsal raphe network revealed by an experimentally-driven augmented integrate-and-fire modeling framework" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jochen Roeper (Reviewer #1); Hitoshi Morikawa (Reviewer #2); Paul Miller (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

In this study, Harkin and colleagues examined the biophysical properties of dorsal raphe (DR) serotonin neurons using a combination of whole-cell patch clamp recording in brain slices and biophysical computational modeling. The authors adopted the approach called a generalized integrate-and-fire [aGIF] model, which incorporates a relatively small number of salient biophysical properties (ionic currents) of a specific neuron, and whose parameters are optimized based on voltage dynamics obtained experimentally. First, the authors observe two prominent features in serotonin neurons. The first is a prominent spike frequency adaptation, resulting from after-hyperpolarization potentials. The second is a "kink" in the voltage trace leading up to the first spike, which can be attributed to the effect of A-type potassium currents (I-A). Using the data, the authors constructed aGIF model of serotonin neurons which contains I-A, two Hodgkin-Huxley currents and a stochastic spike generation process. Next, the authors constructed a simple network model using aGIF serotonin and GABA neurons, and show that heterogeneous feedforward inhibition due to heterogeneous electrophysiological properties of local GABA neurons lead to divisive inhibition of serotonin neuron firing (i.e., change in the slope of input-output function). Finally, using a ramp depolarization, the authors found that serotonin neurons encode the temporal derivative of depolarization, i.e., the slope of ramp depolarization. This property can be ascribed to the prominent spike-frequency adaptation observed in serotonin neurons.

The reviewers found the conclusions of this study very interesting and functionally relevant. The reviewers also thought that the experiments and modeling are generally sound and rigorous, and the results are presented clearly. However, the reviewers have identified various concerns and points to be clarified.

1. The slice experiments were carried out in room temperature, which distorts the kinetics of ion channels and pumps relevant for in vivo electrical activity. Ideally, some of the main conclusions should be confirmed at room temperature. In case this is difficult, please explicitly discuss this caveat and potential impacts on conclusions.

2. The series resistance up to 30 Mohm remains uncompensated and in combination with potassium currents in the range of 1 nA generates voltage errors up to 30 mV. In addition, gating properties of A-type currents will be distorted under these recording conditions. Do the main experimental results hold with a more stringent cutoff of the series resistance? Conversely, how robust are the modeling results with respect to the specific gating properties of A-type currents including the inactivation kinetics?

3. Some of the model parameters appear to be non-physiological. For example, the reversal potential of potassium is given as at least 20mV lower than that used typically in the literature. Please justify the use of -101mV rather than the range -75mV to -85mV as is more common. Please clarify whether the results depend on this very low reversal potential.

4. It is unlikely that the derivative-like computation holds in all of potential input regimes. It is important to clarify in what conditions derivative-like computation is a good approximation of the input-output relationship of serotonin neurons, and when it breaks down.

5. The derivative-like computation and its role in reinforcement learning are emphasized in the manuscript (e.g. abstract). However, as discussed above, the derivative-like computation likely occurs only in a limited input regimen, and the relevance to reinforcement learning is very speculative. The reviewers thought that these points need to be a little toned down.

Reviewer #1 (Recommendations for the authors):

The electrophysiological characterization of 5-HT neurons has a number of shortcomings that should be addressed by additional experiments:

1. Experiments are carried out in room temperature. This distorts the kinetics of ion channels and pumps relevant for in vivo electrical activity.

2. The series resistance up to 30Mohm remains uncompensated and in combination with potassium currents in the range of 1 nA generates voltage errors up to 30 mV. In addition, gating properties of IA-currents will be distorted under these recording conditions

3. An intracellular solution is used without calcium buffering. Given the key role of adaptation and relevant calcium-dependent conductances in 5-HT neurons this is not state-of-the-art

4. 4-AP is not a selective Kv4 (IA) channel blocker. There are more-selective, commercially available alternatives like Heteropodatoxin-2 or AmmTx3.

5. Author show that augmentation of the GIF-model with IA-currents does not specifically improve the model in comparison to a generic iGIF model (Figure 3F2). Doesn´t this call in into question the whole strategy of using experimentally validated biophysical enhancements of GIFs? Does the experimentally augmented GIF outperform the standard computational model of 5-HT neurons (see Tuckwell & Penington (2014) Computational modeling of spike generation in serotonergic neurons of the dorsal raphe nucleus. Prog Neurobiol 118:59-101).

6. Authors should experimentally study the biophysics of adaptation in 5-HT neurons as this is most related to temporal derivative computation, the key insight of this ms. For experimental conditions see 3.

Reviewer #2 (Recommendations for the authors):

1) Electrophysiological recordings are conducted at room temperature. It is not clear why the authors did not conduct recordings at more physiological temperature, as temperature should affect properties on many ion channels, and thus the excitability of neurons.

2) The authors may want to briefly mention the potential behavioral conditions in which endocannabinoids could be released in the dorsal raphe.

3) Dopamine neurons are also known to display low frequency firing, large afterhyperpolarizations, and A-type K currents. It would be helpful to briefly discuss whether similar computations could be applied to these neurons, especially in light of their role in reinforcement learning,

4) P. 14: Figure 1C3 is not present in Figure 1. There might be other places where figure panels are not correctly referred to.

Reviewer #3 (Recommendations for the authors):

The paper is very well written and clear, with a solid approach.

p.10 the reversal potential of potassium is given as at least 20mV lower than any I have come across. Please justify the use of -101mV rather than the range -75mV to -85mV as is more common.

p.11 "within 8 ms": this seems like an arbitrary time range and a rather large one to predict spike timing given typical membrane time constants and jitter. Also, it is unclear if this is related to the "1.5 ms before to 6.5 ms after" a spike where the dV/dt is constrained – and again, why this 8 ms window? And why the smaller window for SOM neurons for the fitting of dV/dt, though not the validation of spike times?

p.21-p.22 The authors state that the aGIF is more parsimonious than the iGIF but it appears that the aGIF has more parameters so the reverse would be true? Perhaps because the aGIF includes a known, well-characterized current, the number of free parameters is smaller even if the total number is greater? Or am I missing something? For sure if the current is shown to be present in the neuron then it is reasonable to use a model with that current rather than the iGIF, but "more parsimonious" would not be the reason.

The authors then on p.22 state the aGIF "best accounts" for the data, but again the iGIF appears to fit the data just as well, and no other model currents or neural were tested. I think the valid conclusion is that adding the extra current(s) improves the fit, no more. It would be good to see a criterion like AIC used to justify the improvement to fit is greater than that bound to arise with extra free parameters.

Figure 5: Given the 5-HT neuron has a sustained response that depends on step height, its output is not the differential of its input. This is an important proviso in any discussion of the properties of the circuit as a differentiator, since it is not one.

p.32, Figure 6 caption. "includes a strong subtractive component (F2)". I think "E2" may be meant as I see a shift between "Het SOM" and "Hom SOM" curves in E2 but not in F2. Also it is important to be clear when discussing the "input-output function" of a neuron whether the transient peak response is being discussed, or the sustained response, or both. Normally sustained firing rate to sustained input would be meant, so if it is the peak of the transient, that should be added in the description.

p.33 Figure 7 caption. "output is … linearly related": again, only the peak of the transient response appears to have a linear relationship. This is not the same as the neuron's output in general.

It would be nice to see that the output of the neuron responding to some range of fluctuating inputs, I(t), has higher linear correlation with dI/dt than with I or to show the neuron responds more to dI/dt than I(t) via some other statistical test. In particular, if dI/dt is more and more negative, does the rate decrease more and more (or is it only a positive slope detector)?

Figure 7F is too opaque for me to understand. It seems like two different manipulations on one plot, but then it is unclear why the different manipulations and color scales correspond to different regions of the x-y plane. I am confused, so I suggest a bit more explanation, or 2 figures if 2 manipulations are carried out.

p.39 temporal difference learning for example is not the same as producing the time-derivative of an input. It is the difference between two inputs (one being expected reward the other being actual reward) – or one can calculate it as the difference across trials from some average reward to the current reward, but that difference between the current input and trial-averaged input is over a far slower timescale than that of the peak responses to a change in input demonstrated here.
