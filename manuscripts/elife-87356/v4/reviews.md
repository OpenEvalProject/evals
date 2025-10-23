# Peer review - Round 1

Editors:
- Katalin Toth, University of Ottawa Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87356.3.sa0](https://doi.org/10.7554/eLife.87356.3.sa0)

This study presents a computational model to explore how neurostimulation could impact hippocampal theta oscillations. The computational model combines a detailed physiologically realistic hippocampus model and an abstract theta oscillator. The study could provide valuable predictions on pathological changes in this network. The modelling is based on convincing approaches that could be improved with experimental validation in future experiments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87356.3.sa1](https://doi.org/10.7554/eLife.87356.3.sa1)

In this article, Vardakalis et al. propose a novel model of hippocampal oscillations whereby an external input (emulating the medial septum) can drive theta rhythms. This model displays phase-amplitude coupling of gamma oscillations, as well as theta resetting, which are known features of physiological theta that have been missing in previous models. The end goal proposed by the authors is to have a framework to explore the mechanisms of neurostimulation, which have shown promising applications in pathological conditions, but for which the underlying dynamics remain largely unknown. To reach this objective, the authors implement an existing biophysical model of the hippocampus that is able to generate gamma oscillations, and receives inputs from a set of Kuramoto oscillators to emulate theta drive originating from the medial septum.

Overall, the hypotheses and results are clearly presented and supported by high quality figures. The study is presented in a didactic way, making it easy for a broad audience to understand the significance of the results. The study does present some weaknesses that could easily be addressed by the authors. First, there are some anatomical inaccuracies: line 129 and fig1C, the authors omit medial septum projections to area CA1 (in addition to the entorhinal cortex). Moreover, in addition to CA1, CA3 also provides monosynaptic feedback projections to the medial septum CA3. Finally, an indirect projection from CA1/3 excitatory neurons to the lateral septum, which in turn sends inhibitory projections to the medial septum could be included or mentioned by the authors. This could be of particular relevance to support claims related to effects of neurostimulations, whereby minutious implementation of anatomical data could be key. If not updating their model, the authors could add this point to their limitation section, where they already do a good job of mentioning some limitations of using the EC as a sole oscillatory input to CA1. The authors test conditions of low theta inputs, which they liken to pathological states (line 112). It is not clear what pathology the authors are referring to, especially since a large amount of 'oscillopathies' in the septohippocampal system are associated with decreased gamma/PAC, but not theta oscillations (e.g. Alzheimer's disease conditions). While relevant for the clinical field, there is overall a missed opportunity to explain many experimental accounts with this novel model. Although to this day, clinical use of DBS is mostly restricted to electrical (and thus cell-type agnostic) stimulation, recent studies focusing on mechanisms of neurostimulations have manipulated specific subtypes in the medial septum and observed effects on hippocampal oscillations (e.g. see Muller & Remy, 2017 for review). Focusing stimulations in CA1 is of course relevant for clinical studies but testing mechanistic hypotheses by focusing stimulation on specific cell types could be highly informative. For instance, could the author reproduce recent optogenetic studies (e.g. Bender et al. 2015 for stimulation of fornix fibers; Etter et al., 2019 & Zutshi et al. 2018 for stimulation of septal inhibitory neurons)? Cell specific manipulations should at least be discussed by the authors.

Beyond these weaknesses, this study has a strong utility for researchers wanting to explore hypotheses in the field of neurostimulations. In particular, I see value in such models for exploring more intricate, phase specific effects of continuous, as well as close loop stimulations which are on the rise in systems neuroscience.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87356.3.sa2](https://doi.org/10.7554/eLife.87356.3.sa2)

Theta-nested gamma oscillations (TNGO) play an important role in hippocampal memory and cognitive processes and are disrupted in pathology. Deep brain stimulation has been shown to affect memory encoding. To investigate the effect of pulsed CA1 neurostimulation on hippocampal TNGO the authors coupled a physiologically realistic model of the hippocampus comprising EC, DG, CA1, and CA3 subfields with an abstract theta oscillator model of the medial septum (MS). Pathology was modeled as weakened theta input from the MS to EC simulating MS neurodegeneration known to occur in Alzheimer's disease. The authors show that if the input from the MS to EC is strong (the healthy state) the model autonomously generates TNGO in all hippocampal subfields while a single neurostimulation pulse has the effect of resetting the TNGO phase. When the MS input strength is weaker the network is quiescent but the authors find that a single CA1 neurostimulation pulse can switch it into the persistent TNGO state, provided the neurostimulation pulse is applied at the peak of the EC theta. If the MS theta oscillator model is supplemented by an additional phase-reset mechanism a single CA1 neurostimulation pulse applied at the trough of EC theta also produces the same effect. If the MS input to EC is weaker still, only a short burst of TNGO is generated by a single neurostimulation pulse. The authors investigate the physiological origin of this burst and find it results from an interplay of CAN and M currents in the CA1 excitatory cells. In this case, the authors find that TNGO can only be rescued by a theta frequency train of CA1 pulses applied at the peak of the EC theta or again at either the peak or trough if the MS oscillator model is supplemented by the phase-reset mechanism.

The main strength of this model is its use of a fairly physiologically detailed model of the hippocampus. The cells are single-compartment models but do include multiple ion channels and are spatially arranged in accordance with the hippocampal structure. This allows the understanding of how ion channels (possibly modifiable by pharmacological agents) interact with system-level oscillations and neurostimulation. The model also includes all the main hippocampal subfields. The other strength is its attention to an important topic, which may be relevant for dementia treatment or prevention, which few modeling studies have addressed.

The work has several weaknesses. First, while investigations of hippocampal neurostimulation are important there are few experimental studies from which one could judge the validity of the model findings. All its findings are therefore predictions. It would be much more convincing to first show the model is able to reproduce some measured empirical neurostimulation effect before proceeding to make predictions. Second, the model is very specific. Or if its behavior is to be considered general it has not been explained why. For example, the model shows bistability between quiescence and TNGO, however what aspect of the model underlies this, be it some particular network structure or particular ion channel, for example, is not addressed. Similarly for the various phase reset behaviors that are found. We may wonder whether a different hippocampal model of TNGO, of which there are many published (for example [1-6]) would show the same effect under neurostimulation. This seems very unlikely and indeed the quiescent state itself shown by this model seems quite artificial. Some indication that particular ion channels, CAN and M are relevant is briefly provided and the work would be much improved by examining this aspect in more detail. In summary, the work would benefit from an intuitive analysis of the basic model ingredients underlying its neurostimulation response properties. Third, while the model is fairly realistic, considerable important factors are not included and in fact, there are much more detailed hippocampal models out there (for example [5,6]). In particular, it includes only excitatory cells and a single type of inhibitory cell. This is particularly important since there are many models and experimental studies where specific cell types, for example, OLM and VIP cells, are strongly implicated in TNGO. Other missing ingredients one may think might have a strong impact on model response to neurostimulation (in particular stimulation trains) include the well-known short-term plasticity between different hippocampal cell types and active dendritic properties. Fourth the MS model seems somewhat unsupported. It is modeled as a set of coupled oscillators that synchronize. However, there is also a phase reset mechanism included. This mechanism is important because it underlies several of the phase reset behaviors shown by the full model. However, it is not derived from experimental phase response curves of septal neurons of which there is no direct measurement. The work would benefit from the use of a more biologically validated MS model.

[1] Hyafil A, Giraud AL, Fontolan L, Gutkin B. Neural cross-frequency coupling: connecting architectures, mechanisms, and functions. Trends in neurosciences. 2015 Nov 1;38(11):725-40.

[2] Tort AB, Rotstein HG, Dugladze T, Gloveli T, Kopell NJ. On the formation of gamma-coherent cell assemblies by oriens lacunosum-moleculare interneurons in the hippocampus. Proceedings of the National Academy of Sciences. 2007 Aug 14;104(33):13490-5.

[3] Neymotin SA, Lazarewicz MT, Sherif M, Contreras D, Finkel LH, Lytton WW. Ketamine disrupts theta modulation of gamma in a computer model of hippocampus. Journal of Neuroscience. 2011 Aug 10;31(32):11733-43.

[4] Ponzi A, Dura-Bernal S, Migliore M. Theta-gamma phase-amplitude coupling in a hippocampal CA1 microcircuit. PLOS Computational Biology. 2023 Mar 23;19(3):e1010942.

[5] Bezaire MJ, Raikov I, Burk K, Vyas D, Soltesz I. Interneuronal mechanisms of hippocampal theta oscillations in a full-scale model of the rodent CA1 circuit. Elife. 2016 Dec 23;5:e18566.

[6] Chatzikalymniou AP, Gumus M, Skinner FK. Linking minimal and detailed models of CA1 microcircuits reveals how theta rhythms emerge and their frequencies controlled. Hippocampus. 2021 Sep;31(9):982-1002.
