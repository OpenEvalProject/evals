# Peer review - Round 1

Editors:
- Manuel Zimmer, Research Institute of Molecular Pathology, Vienna Biocenter and University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50566.sa1](https://doi.org/10.7554/eLife.50566.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In order to evaluate their environment, animals can process information via multiple sensory channels. The basic computations that lead to salient and behaviorally relevant neuronal representations, such as valence of an input, are an active area of research. The authors describe a C. elegans interneuron class, termed AIA, that receives information about attractive odors from multiple pre-synaptic primary sensory neurons. The sensory neuron AWA, which is activated by attractive odors, excites AIA via electrical signaling, while a set of sensory neurons that are inhibited by attractive odors, inhibit AIA via glutamatergic chemical synapses. This circuit motif performs an AND-gate computation during which concomitant excitation and disinhibition ensures reliable positive valence responses in AIA in the presence of low odor concentrations. In support of their model, the authors find that AIA exhibits non-linear bimodal voltage responses to input currents, suggesting a cellular mechanism for this computation. The computational motif described here perhaps repeats in the C. elegans nervous system; moreover, it is likely implemented in a similar way in circuits of animals with larger nervous systems.

Decision letter after peer review:

Thank you for submitting your article "Reliability of an interneuron response depends on an integrated sensory state" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Catherine Dulac as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this manuscript, Dobosiewicz and Bargmann use calcium imaging and genetic manipulations to examine the integration of sensory information by AIA interneurons in C. elegans. By comparing odor- and optogenetically- driven responses from upstream neurons, the authors find that input from a single sensory neuron (AWA) produces a slow and unreliable response, while coincident input from multiple sensory neurons produces more robust and reliable responses. The authors find that AWA provides excitatory input to AIA through electrical synapses, while ASK and AWC provide disinhibitory input through glutamatergic synapses. The authors conclude that integration onto AIA functions as an "AND-gate" and is involved in the selective filtering of sensory information for behavior.

A) Major concern:

The AND gate logic and filtering function seem largely speculative at the moment and more experiments are required to support this claim. The reviewers agree that summation at the level of AIA as opposed to a non-linear AND computation could equally well explain your observations. We understand that reviewer #3 suggestion to perform simultaneous imaging in AIA and the sensory neurons is perhaps out of reach within 2 Months of revisions due to the low resolution of your experimental setup. But we find it necessary that you perform additional convincing experiments that could address this issue in an equivalent manner (for example, by co-stimulating AIA with a specific ASK ligand, or voltage imaging).

Reviewer #3 also is concerned by the lack of explanation what causes the variability in AIA and that you cannot exclude effects from network states, like in Gordus et al. See also reviewer #1, comment (6). While we find it not necessary to address this concern with new experiments, the possible sources of variability should be better discussed.

Please pay also particular attention to rule out reviewer #3's concern that some of your results and conclusions are simply due to the thresholding procedures. A better explanation and a quantitative assessment of how certain parameters were chosen and that your choice does not skew the results is important.

B) Other essential revisions:

Reviewer #1:

1) The main experiment has the caveat that Chrimson is not only very sensitive but also has a long excitation tail extending to the wavelength (474nm) used for GCaMP imaging. Other experts in the field struggle with this problem. It is likely that GCaMP excitation light leads to basal tonic activation of AWA and perhaps habituation of signaling pathways parallel or downstream of Ca++. As stated in their Materials and methods, to prevent AWA activation, the authors use low 447nm light levels. In addition, a peculiar 474nm light-pulsing protocol (10 ms, every 100 ms) is used. I assume that these conditions have been somehow optimized to prevent AWA::Chrismon activation but a systematic demonstration of this is missing here as well as in previous literature. The authors should report in detail how they optimized and scrutinized their light stimulation protocol. This would be needed for the community to reproduce these data, and also extremely useful for other combined optogenetics/imaging experiments.

2) A crucial element of their model is that AWA signals unidirectionally via a gap junction to AIA. While inhibitory glutamatergic signaling to AIA via the other sensory neurons has been characterized, the support for AWA-AIA gap junction signaling is rather thin here.

2a) Conclusions made with the AWA::TeTx strain are based on a negative result, therefore some validation should be provided that this strain is effective at all. For example, AWA sends a relative high number of synapses to AIZ. Does optogenetic activation of AWA affect AIZ activity and is this altered in the AWA::TeTx strain?

2b) UNC-7 and UNC-9 are broadly expressed in the nervous system and are implicated in many functions. Therefore, indirect effects cannot be excluded.

- Is there no phenotype in single mutants?

- This concern could be addressed by transgenic rescue experiments in AWA and AIA.

- In addition, or alternatively, the authors have reported previously a tool for cell-class selective removal of unc-9, which could be used for AIA and AWA.

3) Figure 6. A-B: n-numbers are not listed in legend or table

The data would be more informative if the authors also showed the cumulative response probabilities of AWC, AWA and ASK as well as the AIA response delay time for WT.

4) The authors discuss that the function of this AND-gate computation might be "an integrative step that may filter out environmental noise". Is this consistent with the result in Figure 3A?: based on the authors model, we should assume that the AND-gate computation is absent in the synaptic transmission mutants. Here, I would expect unreliable responses of AIA to the weak AWA stimulation via 11.6nM dia (see Figure 1A), as opposed to when AWA gets strongly activated by Chrimson. This seeming contradiction and the functional relevance of the mechanism could be better discussed.

5) The authors discuss that AIA primarily is modulated by stimulus versus motor state. Although their wording is careful ("AIA activity is more closely coupled to sensory state, and less to motor state,"), a reader less acquainted with the literature could be misled. Currently, I don't see evidence for this statement. In contrast, in freely moving imaging studies Laurent et al., 2015, showed that AIA is indeed modulated by motor state; this paper should be cited and the implications to the current study should be discussed.

Reviewer #3:

1) Measures of response reliability and kinetics and interpretation of AIA integration as an AND-gate (But see our comments Major concern (A) above.)

The conclusion that AIA performs an "AND" gate is based in large part on data in Figure 1 showing that AWA:Chrimson produces smaller, more delayed and less likely responses in AIA than 115 nM diacetyl, however that response kinetics, when there is a response, are similar. However these two pieces of data seem to be in conflict. In the heat maps in Figure 1C (last column) there are clearly some responses with very slow kinetics. The fact that the two curves in Figure 1F are similar (though not the same) is likely an artefact of the thresholding used to determine that there was a response. The same is likely true in Figure 3D, which likewise shows an average of thresholded responses, while the heat maps in 3B show responses with variable latencies.

More generally, I think the authors should try to provide more experimental insight into the source of the observed variability. Some measures of variability and regression on expression levels of Chrimson and GCaMP are shown in the supplement to Figure 1, but only a subset of trials are ever shown in any of the figures. Do responses change in any systematic way over the time of the experiment? Are there slow fluctuations in response magnitude? Are responses correlated on some timescale? What do the authors think is the primary source of the variability in responses? Is it arising at the level of synaptic integration, or calcium channel activation? Is there a contribution of motor state variability to responses as in AIB, even if smaller?

Finally, I think conclusions about integration in AIA would be greatly strengthened by showing AIA responses as a function of simultaneously measured responses in AWA or ASK/AWC. Since simultaneous imaging experiments are mentioned in Figure 5, it seems like this data would be possible to obtain. Plotting AIA response magnitude on a trial-by-trial basis as a function of AWA/ASK/AWC activation on that trial would allow the authors to explicitly test and accept or reject the hypothesis that the integration between these sensory inputs is non-linear, versus being linear with some correlated or uncorrelated noise source either up or downstream. I think these analyses and an explicit model are important to draw the conclusions made here.

2) Temporal filtering by AIA

A second, more minor, conclusion drawn in the Discussion is that AIA integration serves to filter out transient or noisy odor stimuli. However, this idea is not explicitly tested in the manuscript. Odor dynamics can be challenging to control but can be done with proportional valves and measured by photo-ionization detector. Chrimson activation can be reliably controlled in time. If the authors wish to draw conclusions about temporal filtering or noise rejection in AIA I think they need to test this idea by explicitly varying the timecourse of odor or the level of background noise and measuring responses.

Reviewer #2:

1) Subsection “Calcium Imaging”, fourth paragraph: Both pulses were pooled for analyses.

For both heatmaps in Figure 1C last panel (AWA:Chr) and Figure 1—figure supplement 1E, it appears that probability of AIA response is <50% (with varying latencies) given each row is a single trial (n= 569). Number of animals tested (Figure 1—figure supplement 1J) are 282 where 35% respond to both AWA:Chr pulses, 28% to 1st only, and 16% to 2nd only. What is getting pooled in Figure 1? Only traces which respond to both pulses?

2) The mean trace for the AWA:Chr stimulus is similar to 115 nM diacetyl, but the trials seem more variable, including a number of non-responders. Are these most likely expression differences, or something about Chrimson dynamics? Can you be sure the low-level of 474 nm blue light used to image GCaMP prior to red light stimuluation does not have an effect on Chrimson? Did you try stimulating only the dendrite / sensory ending of AWA?

3) Did you attempt to image AWA and AIA at the same time, or is this precluded by the need to image the AIA process?

4) unc-13 mutants as well another transgene of unc-18 seem to have no effect on AIA response latency at 1.15uM diacetyl. Though this is mentioned in the second paragraph of the subsection “Chemical synapses inhibit AIA”, the rationale is not clearly explained. Is the reliability of the response also dosage dependent? Only data related to latency are shown in Figure 3A and Figure 3—figure supplement 1A, heatmaps which can indicate reliability are missing.

5) As in comment 2, only response time profiles are shown in Figure 4, indicating differences in latency, but heatmaps should be added as supplementary data to show trial-to-trial variability in responses.

6) At 11.5nM diacetyl, AWA is activated and ASK is inhibited, and this leads to moderate reliability of AIA response. At 1.15uM dia, AWA is activated with high fidelity, ASE is activated; ASK and AWC are inhibited and this leads to disinhibition of AIA and high reliability in its response. Do glutamate levels or different channel expression regulate the magnitude of disinhibition and in turn affect the reliability? ASK seems to be a key candidate tuning this reliability, as inhibition of ASK alone (Figure 4D) has a significant effect on AIA response reliability.

7) Glutamate release from ASE (with AWC::Figure 4I) can inhibit AIA activation. However, 1.15uM dia activates ASE, yet increases AIA reliability. This is not well clarified in the manuscript, and a model figure and extended discussion would help in this regard.

8) Were the unc-9 and unc-7 mutants tested individually to identify which of the innexins are required for AWA-AIA communication?
