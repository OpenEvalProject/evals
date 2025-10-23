# Peer review - Round 1

Editors:
- John Huguenard, Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41925.024](https://doi.org/10.7554/eLife.41925.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Thalamocortical synapses in the cat visual system in vivo are weak and unreliable" for consideration by eLife. Your article has been reviewed by Ronald Calabrese as the Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

These data are hard-won, from a highly challenging preparation, with important implications for models of thalamocortical function. There have been very few recordings of connected thalamocortical pairs in vivo, and even fewer with intracellular recordings. Using this approach, the authors report that the LGN-V1 synapse is highly unreliable in vivo, in contradiction to previous slice studies. They build a model of a L4 neuron receiving LGN connections, which predicts that unreliability increases cortical firing rates. There are only a handful of similar datasets to this one and absolutely no others in visual cortex; these are truly unique data. The analyses are clever and original. Much of what we base our general ideas of thalamocortical interactions on is thus based on in vitro, rather than in vivo, data. Given the authors' careful quantitative approach, the current findings are thus likely to have a substantial impact in the field.

Essential revisions:

There are a few major elements of the manuscript that could be substantially improved through text clarification and there are several points that could benefit from additional analysis or enhanced discussion (listed as the first major points below). No additional experiments seem necessary.

1) The authors should acknowledge that they cannot measure synaptic reliability in vivo. This does not detract from the impact of the findings, but the use of 'reliability' is misleading in the broader context of the field. Reliability is the term used to describe the variance in synaptic transmission events-release of neurotransmitter that successfully binds to receptors and causes a synaptic current flux. It is not currently possible to measure this in vivo. What the authors are measuring is the functional impact of the synaptic event on the postsynaptic neuron's membrane potential. This is an important measure, as it is directly linked to postsynaptic spike output, but it is distinct from the technical term 'reliability'. The authors cannot distinguish in vivo between (1) synaptic failures-which do impact reliability estimates-and (2) moments where a successful synaptic event is lost to noise, shunting, etc. – which do not impact synaptic reliability but do affect functional postsynaptic impact.

2) The model makes an interesting prediction (unreliable synapses are helpful), but the authors could do a better job of making this theoretical case. First, they compare the predicted enhancement of cortical discharges given unreliability versus thalamic synchrony, which is interesting. However, the synchrony mechanism requires recurrent cortical excitation and feedforward inhibition, which a few papers cited by the authors (Wang et al., 2010; Bruno, 2011) make a strong point of and which are well documented experimentally. The model here, however, lacks both recurrent excitation and feedforward inhibition, so it is hard to know how unreliable synapses and thalamic synchrony compare or interact. Second, these two elements could lessen the effect of unreliable synapses. Since the model is the only evidence that unreliable synapses are feature not flaw, the authors should consider an expanded simulation.

3) The authors must include in the Discussion section a mention of the caveats associated with the use of anesthesia, especially as the data represent a mix of thiopental and propofol preparations. Even light anesthesia alters the statistics of thalamic firing, and almost no cortical recordings have ever been made under propofol anesthesia.

4) The discussion in subsection “Detecting Single-spike EPSPs” is not clear. For a multisite EPSP (i.e. one arising from multiple synaptic contacts from a single thalamic axon onto a single cortical neuron) to fractionate, i.e. be resolved as separate EPSPs they would likely need to be distributed at very distinct electrotonic distances from the presumed somatic recording. In addition, I think this discussion is not particularly relevant to the interpretation of the results. The bottom line is that it would be very difficult to resolve whether an individual paired response results from a single synapse or a group of synapses, whether they are clustered or not. The large amplitude variability of responses (subsection “Validating single-spike EPSP detector”) is in fact consistent with either multivesicular release at individual synapses, or multi-synapse release, with a possible binomial distribution (subsection “Thalamocortical synapses are unreliable and produce highly variable EPSPs”) of amplitudes, as expected from standard synaptic models. This needs to be better explained.

5) While both the White Noise and Grating stimuli produce similar results, there seems to be a significant difference, which the authors gloss over. Figure 4H suggests that synapses are stronger and more unreliable during Grating stimulation than during White Noise stimulation. The authors should report the results of a paired test and discuss appropriately.

6) KS tests, which evaluate the whole distribution, are overly sensitive in that the slightest difference-even of a tail-produces a significant result. Unless the authors wish to focus on potential subpopulations (tail effects) in their analysis, then the results around short vs long ISIs (Figure 5C,D) would be more compelling if the authors could construct a simple analysis testing the median or means of these data, which appears to be their real question.

7) The present results seem somewhat more consonant with previous findings than the authors suggest. For instance, the authors did not find a correlation of depression and pre-synaptic firing rate, which they say is at odds with Boudreau and Ferster 2005's study of thalamocortical depression (subsection “Thalamocortical synapses exhibit short-term synaptic plasticity”). Might it not be that the present study is simply at the high end of pre-synaptic firing rates (B&F's at the lower end) and the depression is largely maxed out? The authors could explain better the extent to which this is or is not a discrepancy. A second instance is where the authors say that their EPSP amplitudes are modest even when compared to the in vivo measurements in the somatosensory system (subsection “Thalamocortical strength, reliability, and variability in vivo”). Bruno and Sakmann, 2006 reported similar average EPSPs as the 'all single-spikes' in Figure 4 here, and Schoonover et al., 2014 claim similar strength of unitary EPSPs (failures removed) as the 'detectable EPSPs' in Figure 4 here. This is a positive not a negative of the manuscript because it suggests that different sensory systems might be exploiting similar mechanisms and principles. A comment about the authors' discovery may be merited.

8) Simply reporting that spikes were manually clustered is not sufficient. The authors should report% spikes occurring with 1 ms of each other along with cluster isolation metrics.

9) Subsection “Effect of thalamocortical variability on L4”: 'Data not shown' is not really acceptable, the authors should include simulations in supplementary data or not mention them at all.

10) Subsection “Thalamocortical synapses are unreliable and produce highly variable EPSPs”. IPSPs do not need to be hyperpolarizing to influence membrane responses and especially EPSPs. The associated in increase in conductance will itself decrease amplitude of EPSPs, all other things being equal. Overall, I would like to see a discussion of the influence of dynamics of membrane conductance in terms of the influence of EPSPs on Vm and on their amplitude and detectability.

11) Previous in vitro and in vivo studies have focused on layer IV itself, while this study more broadly samples deeper cortical layers. This may influence some of the results. In particular, it has been reported that thalamocortical inputs onto FS cells in layer IV tend to be stronger and more reliable than the inputs onto RS cells. The relative similarity in EPSPs reported here may result in part from undersampling layer IV.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Thalamocortical synapses in the cat visual system in vivo are weak and unreliable" for further consideration at eLife. Your revised article has been favorably evaluated by Ronald Calabrese (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below in the next section. The reviewing editor will make the final assessment of the revised manuscript.

Essential revisions:

Overall, the authors have addressed most previous concerns. The text is also generally more readable and clear. The manuscript now focuses on the dynamics of the LGN-V1 synapse in vivo and simply advocates that this synaptic variability enhances post-synaptic fluctuations and therefore firing rates. While a more extensive model that addressed the intriguing issue of synchrony could provide substantial insight, we agree with the authors that a full examination deserves a separate study.

- There does not seem to be a clear set of criteria for unit inclusion based on cluster metrics. The plot in Figure 1—figure supplement 1 does not make it easy to evaluate the isolation distances, but some points appear to be very low.

- The final paragraph of the Introduction is somewhat confusing as written. Perhaps the authors meant "high variability of the thalamocortical synapse, rather than being irrelevant system noise, does play a functional role…"?

- There are a few places where text changes have not been fully incorporated and should be fixed, e.g. subsection “Thalamocortical synapses are unreliable and generate highly variable EPSPs”, Discussion section, figure legend for Figure 1—Figure supplement 1.

- The authors are perhaps overly modest in citing their own previous work. The Contreras group has published several other studies (2007, 2010) on the synaptic and intrinsic properties of RS and FS cells in cat visual cortex that are relevant to the current findings.

- Subsection “Thalamocortical synapses are unreliable and generate highly variable EPSPs”, "…there is a population of very large (>4 mV) EPSPs triggered by LGN input." This unusual population is interesting and warrant comparison with the more typical 0.5-1.0 mV EPSPs. Most of the traces shown are the common small type. Figure 3B green appears to show a larger one that is 2-3 mV at most. These very large EPSPs could result from nonlinear voltage-dependent mechanisms that might have a different shape from normal EPSPs, bursts of LGN spikes, etc. The green traces indeed exhibit a long shoulder suggestive of voltage-dependent mechanisms. Peak normalizing the average small and large EPSPs should allow visual comparison of their shapes.

- On a related note, subsection “Detecting Single-spike EPSPs” states that small "undetectable" EPSPs are unlikely to influence postsynaptic Vm. While I agree with this statement generally, I think the authors have to qualify it with "at least under our conditions". One can easily imagine nonlinear voltage-gated channels that make such small EPSPs potent under different conditions (e.g., state dependent neuromodulation of those channels, disinhibitory circuits, etc.). Also, the interim results summary paragraph, subsection “subsection “Thalamocortical synapses are unreliable and generate highly variable EPSPs”, is confusing. Consider "…including a large percentage of EPSPs that do not visibly affect somatic Vm and are unlikely to contribute to the cortical output." As noted in point 2, this is not guaranteed. More so it doesn't seem to allow for the possibility of synaptic failures. This and the surrounding text could be read to mean they "undetected" EPSPs are always small and never failures.

The authors have improved the short-term depression section, but there is still some difficulty following the logic of the predictions (subsection “Short-term synaptic plasticity in vivo”). Boudreau and Ferster, 2005 electrically stimulated LGN inputs in anesthetized cats and predicted that depression would be near saturated in the awake animal. The present study, also under anesthesia, evoked LGN spikes by visual stimulation and measured the synaptic input. They find that LGN firing rate does not correlate with the amount of depression (short vs long ISI) they observe, which in any case is about a 17% decrease. However, Boudreau and Ferster's depression curve does show a slight similar decrease from the first to later stimuli. Additionally, the present study only has 3 data points above 10 Hz-how can it be used to make claims about what happens for awake firing rates? 1-10 Hz is already in the range of awake spontaneous activity.
