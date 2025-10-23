# Peer review - Round 1

Editors:
- John Huguenard, Stanford University School of Medicine United States

Reviewers:
- Carl CH Petersen, École Polytechnique Fédérale de Lausanne (EPFL) Switzerland

## Review text

DOI: [10.7554/eLife.48622.sa1](https://doi.org/10.7554/eLife.48622.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Li et al. examine various methods for optogenetic inhibition of specific brain regions. Optogenetic methods for precisely inactivating cortical areas are of central importance to mouse systems neuroscience. The authors utilize novel quantitative methods to study of the spatiotemporal effects of optogenetic cortical inactivation, and find, somewhat surprisingly that a wide variety of optical and optogenetic approaches all produce near complete silencing of all cortical layers with a lateral resolution of approximately one mm. This paper will be a valuable resource for design and interpretation of studies performing cortical silencing.

Decision letter after peer review:

Thank you for submitting your article "Spatiotemporal limits of optogenetic manipulations in cortical circuits" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen Eve Marder as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Carl CH Petersen (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Perturbations are an essential tool for understanding causal mechanisms in the brain, and focal inactivation of cortex with optogenetics is a useful paradigm for assessing localization of cortical function. However, due to recurrent circuitry, perturbations produce downstream effects that need to be quantified and understood. In this study, Li et al. systematically benchmark the spatial and temporal limits of optogenetic silencing of the cortex using a broad range of current tools. They test tools using two strategies: 1) ChR2 assisted-photoinhibition, which leverages inhibitory interneurons to suppress cortical pyramidal cells, and 2) direct photo-inhibition of pyramidal cells.

The authors find, perhaps surprisingly, that all methods produce a similar spatial extent of cortical suppression, on the order of ~1mm. Of considerable note, this photo-inhibition profile extends beyond the spatial profile of light delivery, suggesting resolution is limited by the structure of the cortical circuitry.

The authors also generate and characterize a new transgenic line that expresses a light-gated silencing (anion) channel (GtACR). This channel is tagged with a somatic localization sequence to minimize axonal expression. Cortical silencing with GtACR was the most potent with effects at very low light levels.

The results provide practical guidance for the design and interpretation of optogenetic silencing in the mouse neocortex.

Essential revisions:

1) The paper is not written very clearly. Please improve the presentation including experimental approach, interpretation and logic. Please correct language, grammar, and syntax.

2) There are frustrating aspects of the study, especially in terms of what was not studied. For example, the assays of inactivation do not adequately explore a complete dynamic range of light intensities. In fact, for many of the manipulations, the minimal power used was apparently nearly maximally effective (e.g. Figure 1E, most opsins), and so the reader is left with incomplete knowledge of the power levels actually needed to silence neural networks. This is critical to know given Kreitzer lab's recent report on non-specific light induced artefacts in the brain.

3) One of the main findings, that the primary effects of photon delivery mainly extend to superficial cortex, and yet this leads to global inactivation across all cortical layers is extremely important (see point 5a, below), and may explain why it doesn't matter which optogenetic approach is used – the results are generally the same. It is important to get this message out. However, the speculation in the Discussion on the role for thalamocortical interactions in propagating the silencing between layers is just that -- speculation. This is one area where addition experiments to test this hypothesis would be extremely useful, although not required.

4) In many places the approach and rationale for the data analysis was opaque. a) It is not clear how the authors have quantified their "relative spike rates" in most figures. In the Materials and methods it states: "The spike rates with photostimulation were averaged across the population and normalized by dividing the averaged baseline spike rate." Does this mean the baseline spike rates are from the averaged population but not for individual neurons? What was the rationale for this, rather than just normalizing each neuron to its own spike rate? Is this also true for figures where individual neurons are plotted (e.g. Figure 1D)?

b) In many figures, the legend states that the error bars are SEM from bootstrap, but there is limited information on the bootstrapping in the Materials and methods. What was being bootstrapped (different subsamples of neurons for the population average and baseline response?), and how many bootstraps were performed? Also what is the rational for using SEM (which presumably depends on the number of bootstraps) instead of the confidence interval?

c) More information is needed to understand the photobleaching experiment. It wasn't clear how the "empirical relationship" between laser power and photobleaching was computed. Is this the exponential fit in Figure 1C? Is the data in Figure 3D and G from a specific light power- or is the distribution for all light powers, just varying in magnitude? Does this process account for potential differences in light absorption (and photobleaching sensitivity) of GFP and mCherry? That is, how do we know that the difference in effect between the different wavelengths of light is due to the wavelength or the fluorophore? It is also unfortunate that the light powers used for this experiment do not match the ones used for the physiology- in fact, 5 mW (the lowest light power used) is two orders of magnitude higher than the light power that is sufficient to locally suppress the cortex to ~25% of initial rates with Emx1-Cre x GtACR (Figure 6). As such, it is hard to understand how the measurements made reflect the conditions that are actually used- or if this method is sensitive enough to accurately measure the true distribution of light intensity. Clarifying these relationships is important since the authors use these measurements later to make arguments about the mechanism through which suppression propagates in the cortex (see Major Concern 2a).

d) How were layers defined in laminar recordings?

5) In many cases, the authors make definitive statements where it is not entirely clear where the supporting data is or whether that is the only possible interpretation. A number of examples are below, but there are likely others.

a) The authors make a strong argument that the direct effects of photoinhibition are restricted to the superficial layers and drive the photoinhibition in deep layers through indirect effects. They seem to base this conclusion on two observations: 1) the lack of penetration of blue light from their photobleaching experiments and 2) the restriction of excitation of FS cells to superficial layers. Concerns about the interpretation of the photobleaching experiment are in point 1c. In addition, the authors' conclusions about the effects on FS cells are limited by cell numbers, their ability to accurately identify ChR2 expressing neurons, and the contribution of paradoxical effects. Most importantly, their own data is not entirely consistent with this conclusion: if the deep layer suppression is mainly caused by the loss of activity in superficial layers, one would not observe the striking difference in the suppression in layer 5/6 given the similar degree of suppression in superficial layers with different light powers in Figure 4.

b) The authors indicated that the paradoxical effects they observed were mainly due to reduced excitation from nearby excitatory neurons to GABAergic neurons (subsection “Strong coupling between cortical neurons and the paradoxical effect”). However, the paradoxical effects could also be induced by increased inhibition from activation of nearby GABAergic neurons. The authors also state that the increase in FS neuron activity at higher light intensities is "partly driven by increased photocurrent". This seems likely to be true, but what evidence to the authors have for this statement? And why only "partly"- what else contributes?

c) The statement regarding the observation of "axonal excitation" was unexpected and it wasn't clear why the authors concluded that the increase in firing rates were due to activation of the axonal compartment. Also- are Figures 2C and D the same data, just at different time scales?

d) In describing Figure 11C, the authors state that "… the photoinhibition lagged FS neuron excitation by 3 ms…". However, there is no clear quantification of the onset of FS neuron activation.

e) The authors should be clear that given their cell-type identification is only dependent on the spike width, that the classifications are "putative". There is plenty of evidence for narrow spiking excitatory cells and broad spiking interneurons.

6) The authors need to provide some explanation for why the laminar profile of suppression is so similar with blue and red light using EMX1-cre GtACR, given their expected differences in the tissue penetration properties. Similarly, the authors should provide some explanation for why the spatial spread of photoinhibition is smaller with viral injections than transgenic expression if blue light spread is not a limitation.

7) The authors need to provide some discussion of the fact that all of their measurements were made under conditions of spontaneous activity. Should we expect all of these methods to be similarly effective at silencing areas the animal is receiving sensory input or actively engaged in behavior tasks?

8) The title of the paper "Spatiotemporal limits of optogenetic manipulations in cortical circuits" is somewhat misleading in that it is clearly possible to carry out optogenetic manipulations on a finer scale than carried out here, indeed even in some cases with single-cell resolution.

9) Figure legends need to be greatly improved. It should be possible to understand what is going on in all parts of the figure. Each panel/subgraph should at least be explained.

10) How worried should users of the GtACR reporter line be about axonal activation? Cortex can be silenced with light intensities of 0.1-0.2 mW, but axons begin spiking around 0.8 mW. Are users safe if they restrict intensities < 0.3 mW? Are there tell-tale signs of axon activation that users should lookout for, or are there specific controls that would always be recommended?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Spatiotemporal constraints on optogenetic inactivation in cortical circuits" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder as the Senior Editor, a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

While the revised manuscript is substantially improved in its clarity of presentation, there still remain a number of issues that have not been satisfactorily addressed.

1) One major strengths of the paper is that it quantitively assesses both light delivery into the brain and downstream effects of light. The innovative approach of using photobleaching to assess light penetration is a reasonable one, but far from perfect, in that it requires much greater levels of light, and/or over extended periods of time compared to optogenetic activation/inhibition. Accordingly, there is a level of imprecision to the method that should be much more explicitly addressed in the paper, either in explaining the limitations are in providing additional data.

Critically, the spread of light does indeed appear to depend on the light power used. Indeed, the authors seem to suggest this themselves when responding to point 6 ("At high laser power the light illuminates a larger volume"). This is also very evident in Figure 3B. However, the photobleaching data suggest that the penetration of the light is independent of light power (or light dose, as the authors now call it), and thus argue that the higher powers they use only confer better signal to noise. It seems like some independent validation/calibration of this approach is needed.

2) The authors state in their rebuttal that the calculation of light intensity does not depend on differences across fluorophores. However, the k in their equation seems to be fluorophore dependent. More information is needed on whether the same k was used across fluorophores, or whether this was part of their fitting process, and if so whether these values are in line with expectations about the fluorophores. In addition, some citations that support which factors do and don't contribute to the photobleaching process would be helpful.

3) If the radius of laser light scatter is ~200 microns, then it is still confusing why the viral injection, which has a radius of ~250 microns (i.e. greater than the light) should restrict the spread of inhibition compared to in the transgenic condition. This result suggests that the authors are underestimating the spread of their light.

4) The terminology regarding light levels in the revised manuscript and rebuttal letter is quite inconsistent, with moderate meaning different things (1 mW or 20 mW) in different contexts. This terminology should be standardized throughout the paper, especially in relation to light levels required for biological effects.

5) It would be valuable to add some discussion regarding how these optogenetic silencing approaches seem to be extremely sensitive such that there is not much dynamic range for the manipulation, regarding e.g. the possibility to explore the behavioral consequences of different degrees of cortical suppression. On a related note, the new limited data provided in the rebuttal on silencing with low level light delivery should be included in the revised paper.
