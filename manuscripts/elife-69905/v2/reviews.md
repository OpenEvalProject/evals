# Peer review - Round 1

Editors:
- Manuel Zimmer, University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69905.sa1](https://doi.org/10.7554/eLife.69905.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper combines behaviour quantification, optogenetic perturbation, and modelling to study C. elegans locomotion. It will be of interest to neuroscientists studying lcomotion and gait adaptation. The quantitative agreement between the model and experiments-importantly including the perturbation experiments-suggests forward locomotion in worms can be understood as being driven by a relaxation oscillator. This conclusion provides intuition for how worms move and should provide useful constraints on more detailed models that include neural anatomy and physiology.

Decision letter after peer review:

Thank you for submitting your article "Phase response analyses support a relaxation oscillator model of locomotor rhythm generation in Caenorhabditis elegans" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Manuel Zimmer as a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Carter Johnson (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. As you can see below, the reviewers provide an extensive list of detailed comments, however the overall result of the reviews and subsequent discussions is that we are very excited about your work, and we would like to support publication in eLife of a revised manuscripts that addresses all comments. The comments below are partially concerned with similar issues but to retain each reviewers' details, we provide you here with the full list. Please submit with your revision a point-by-point response to the comments.

Essential revisions:Reviewer #1:

(R1.1) The authors set out to better understand the dynamics of C. elegans locomotion characterizing the rhythmic pattern of the worm's head during locomotion and by generating the phase response curve in that region. The authors then illustrate how well the relaxation-oscillator phenomenological model, with only a handful of free parameters optimized to match the data, is consistent with the observations, including observations under different mechanical loads.

(R1.2) The authors provide a characterization of the curvature dynamics in the worm's head region (0.1-0.3 body coordinate). The reasoning for focusing on this area in particular is not discussed or justified in the manuscript. Also, no comment is made whether the characteristics observed for the limit cycle in that region is consistent across the rest of the regions. From the experimental description and data shown (i.e., Figure 2B), it would appear that the authors had access to a characterization of the limit cycle across any region of the body of the worm, from head to tail. To avoid the appearance of cherry-picking a region, authors are encouraged to include the full characterization of the limit cycle for all the data available to them. In addition to that, authors are encouraged to clarify explicitly whether the characteristics observed in one region (e.g., nonsinusoidal limit cycle) hold true across the rest of the worm's body. How sinusoidal or nonsinusoidal, non-ellipsoidal, asymmetric is the limit cycle as a function of the body region of the worm, from head to tail? Crucially, if the characterization observed in the selected region is not equally pronounced across the rest of body, it seems crucial to discuss it in the interpretation of the results. This is particularly important given that throughout the manuscript, the authors interpret the results as applicable to the rhythmic generation across the whole body, not just that limited region (see first sentence of the Discussion, for example; and it is also relevant given that they discuss equally proprioceptive feedback in the head as well as in the rest of the body). These points apply to the characterization of the limit cycle given that the data is there but not shown; this is not the case for the phase response analysis, because understanding it for the full body would require further experimentation. However, this should be a point of discussion: is the expectation that the phase response curve through transient ontogenetic inhibition will look similar throughout the body? Is the same sawtooth-shape with the sharp transitions in the same part of the phase expected? What is the implication of the expected results if they are consistent or not consistent with the ones shown for the region focused on here?

(R1.2) The model assumes proprioceptive feedback from the curvature of the same region that is bending. However, the undifferentiated processes that are used as inspiration for this assumption extend posteriorly in the case of SMD and anteriorly in the case of B-class motor neurons. So the assumption that the curvature in one region can affect the bending in that same region should be discussed.

(R1.3) The model also assumes that the stretch receptors sense both the curvature and the rate of curvature. However, the authors provide no evidence of other C. elegans neurons where both of those can be sensed simultaneously. It seems feasible that a neuron might be sensitive to either the curvature or the rate of curvature, but it seems less feasible that the neuron would be sensitive to a linear combination of both. This seems to be a central assumption of the model, with little or no justification.

(R1.4) I commend the authors for comparing their selected model with other similar ones. I would highly encourage that the authors include a comparison of the models into the main manuscript. In particular, given the similarities between the results, I would highly encourage the authors to place the results of their chosen model next to the alternatives (it can be a figure like S10 but including the preferred model). As it is, with the alternatives in S10 and the rest of the figures from the best model in the main text, the comparison is significantly harder.

(R1.5) Finally, the discussion of previous relevant computational models of C. elegans locomotion is rather limited. There are at least four particularly relevant contributions that the authors do not discuss in relation to their own contribution:

(a) Johnson, Lewis, and Guy (2020) Neuromechanical Mechanisms of Gait Adaptation in C. elegans: Relative Roles of Neural and Mechanical Coupling.

(b) Izquierdo and Beer (2018) From head to tail: a neuromechanical model of forward locomotion in Caenorhabditis elegans.

(c) Kunert, Proctor, Brunton, Kutz (2017) Spatiotemporal feedback and network structure drive and encode Caenorhabditis elegans locomotion

(d) Denham, Ranner, Cohen (2018) Signatures of proprioceptive control in Caenorhabditis elegans locomotion.

Reviewer #2:

(R2.1) The paper's conclusions are supported by the data and the experiments and model results are clearly presented. In some cases there could be more analysis of uncertainty. For example, how consistent is the phase portrait? This could be illustrated by including some individual traces and/or by estimating a confidence interval (using resampling if necessary). A different kind of uncertainty that should be explained is that arising from fitting the model. Was the optimisation sensitive to the choice of starting parameters? Are there several local minima that explain the data reasonably well or did the optimisation always converge to the same parameter values?

(R2.2) The authors have focused on forward locomotion bouts and have also eliminated cycles with a period that deviated more than 20% from the average across worms within a session. How many of the bouts were eliminated with this threshold? Are any of the conclusions of the paper sensitive to this threshold?

(R2.3) The authors have convincingly ruled out the van der Pol and Stuart-Landau oscillators but the Rayleigh oscillator fits the data quite well with three parameters. Some quantification of the relative fit quality of the threshold-switch model and the Rayleigh might help guide future work.

(R2.4) Finally, the discussion does a good job of putting the results of the phenomenological threshold-switch model in the context of previously published detailed models but it might be strengthened with more quantitative comparisons. For example, do the observed muscle switching time scales or the nature of the proprioceptive threshold rule out or usefully constrain any of the detailed models?

(R2.5) The schematic figures (1 and 4) would be improved by leaving out the abbreviations. At a minimum, include (BWM) after 'body wall muscles' in the caption of figure 1.

(R2.6) Would a different colour map make Figure S2 clearer? Jet makes some regions stand out more than is warranted. For example, the purple patch in the lower right corner and red patch in the upper left corder are visually very salient but are probably just normal fluctuations within the noise.

(R2.7) In Figure 3, grey is used to indicate the control data in B but is used for individual trials in subsequent panels. Use a different colour for controls in B? Also add the grey curves to the legend next to D rather than only describing them in the caption.

(R2.8) Line 299, state the gene name of the GABA receptor.

(R2.9) In the Appendix there are a few cases of missing articles (for example line 812, "worm's head" should be "the worm's head" and on line 886 "animal's" should be "the animal's").

(R2.10) Starting on line 817, D^C is used to denote the distance from the origin over the normal cycle. To avoid confusion with the scaling constant c, perhaps choose a different symbol for the scaling constant or to indicate the normal cycle?Reviewer #3:

(R3.1) The main suggestion I have is to change the framing of the section "The Analysis of Alternative Models Supports a Relaxation Oscillation Mechanism'. In the first paragraph, the authors state that the purpose of this section is to "[ask] whether other models could also explain our findings." However, the section title and final paragraph suggest that the purpose of the section is to support the idea that the underlying oscillatory mechanism is a relaxation-oscillation. If my understanding of the authors' purpose here is correct, then I don't think the analysis of these three specific phenomenological models provides evidence of this. Specifically, the last paragraph of this section (Lines 586-590), suggests that because the non-relaxation oscillator (Stuart-Landau) was not able to capture your results (non-sinusoidal limit cycle and sawtooth PRCs), the underlying mechanism is a relaxation-oscillation. I don't think these models support that claim, because a different non-relaxation oscillator tuned precisely may be able to capture these results. I think a much more thorough analysis of general oscillator dynamics would be needed to make such a claim. To be clear, I think the paper is strong enough without this analysis, I would just be more cautious about the claims here.

(R3.2) The strength of the author's original computational model is that it is based on specific mechanisms thought to underlie C. elegans neurolocomotion (specifically motor neurons, muscles, and proprioception). The authors discuss how this model functions as a relaxation-oscillator in the discussion, but I think it would be stronger in this section.

(R3.3) Intro or discussion – In addition to Cohen's group's models, two recent modeling papers from other modeling groups have investigated the C. elegans neurolocomotion system explicitly as a chain of coupled neuromechanical oscillators (Olivares et al., 2021 doi:10.3389/fncom.2021.572339 and Johnson et al., 2021 doi:10.1137/20M1346122). In particular, Johnson et al., 2021 show how phase-response properties influence coordination of the neuromechanical oscillators. Describing how your computational model compares with or supports these other recent models would help give context to the modeling contribution of this work.

(R3.14) Lines 311-313: The authors mention that sawtooth PRCS "may reflect a phase-resetting property of an oscillator with respect to a perturbation". I think more detail would be helpful here. To my knowledge, this is referring to the idea that if an oscillator gets a really strong perturbation, the phase-response curve turns into a "phase-resetting curve", where the large perturbation essentially resets the phase of the oscillator, and then it just marches forward linearly through time. Are you suggesting that this sawtooth shape is indicative of your perturbation being large? This would be an important detail to include.

(R3.5) Section "Analysis of Alternative Models Supports a Relaxation Oscillation Mechanism":

The strength of the author's original computational model is that it is based on specific mechanisms thought to underlie C. elegans neurolocomotion (specifically motor neurons, muscles, and proprioception). To support the idea that the underlying mechanism is a relaxation-oscillation, I would suggest that the authors instead analyze their own computational model and show or point out how it functions structurally as a relaxation-oscillation. This is mentioned briefly in the discussion, but I think it would be stronger in this section. Furthermore, I think the authors could give the reader a clearer reason why exactly showing that the mechanism is a relaxation-oscillation is important. To my understanding, the open question in the C. elegans locomotion-modeling literature is whether the oscillations are fundamentally neurally-driven (like a CPG or HCO) or reflex-driven (like the proprioceptive mechanism here). Perhaps evidence for the relaxation-oscillation mechanism could be made by considering an alternative mechanistic model with neurally-driven oscillations and whether it can capture the new phase response data.

(R3.6) The authors have not given adequate description of the model fitting process in the main text. In line 548, you only mention that appropriate parameters were chosen, and reference the supplement. I don't think too much detail is needed here, but explaining that the models were fit to match both the limit cycles and PRCs would be helpful here. My first impression of this section was that the limit cycles were matched and the PRCs were emergent. After looking at the supplementary details I saw that you explicitly attempted to match both results. This would be helpful to put up front.

(R3.7) Lines 61-64: Sentence grammar/structure. The "but also …" is missing a "not only" earlier in the sentence (e.g. "A comprehensive understanding of animal locomotion should therefore encompass not only neural activity, muscle activity, and sensory feedback, but also biomechanical forces within the animal's body and between the animal and its environment (Figure 1A; 1-3).").

(R3.8) Lines 152-153 and Figure 2D caption: I think it would help to clarify in either or both of these places that the boxed portion of the nematode bodies corresponds to the curvature region (0.1-0.3 body coordinates).

(R3.9) Lines 940-951: The mechanics here depend on the assumption of a traveling wave of fixed wavelength λ down the body. I would mention explicitly that both the wavelength λ and normal drag coefficient CN will be varied with fluid viscosity.
