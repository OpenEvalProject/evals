# Peer review - Round 1

Editors:
- Michael Häusser, University College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.14193.015](https://doi.org/10.7554/eLife.14193.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for choosing to send your work entitled "Single-cell resolution circuit mapping with temporal-focused excitation of soma-targeted channelrhodopsin" for consideration at eLife. Your full submission has been evaluated by Eve Marder as the Senior editor and three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the decision was reached after discussions between the reviewers. Based on our discussions and the individual reviews below, we regret to inform you that the work does not meet the standard for publication in eLife.

While the reviewers agreed that the strategy you propose is elegant and potentially very powerful, and could have a major impact on the field of neuroscience, unfortunately they also expressed serious concerns regarding the details of the experiments and the presentation of the results, which dampened enthusiasm for the manuscript. In particular, the section of the manuscript on circuit mapping was felt to be especially weak and would require a major series of additional experiments. As you probably know, eLife has a policy of not asking for significant new experiments as part of a revision, thus resulting in the present decision.

Reviewer #1:

In this paper, the authors describe an optogenetics method to reach optogenetics activation with single cell resolution. The approach combines the use of temporal focusing with targeted opsins, which restrict the chanelrhodopsin expression to the soma and the apical dendrites. The development of somatic opsins is one of the most promising ways of reaching a true cellular resolution with optogenetics and will surely strongly impact the neuroscience community.

However, in my opinion, the manuscript cannot be published in the present form and requires significant major modifications.

Introduction:

References reporting optical methods using two-photon excitation, diffractive optics and temporal focusing for optogenetics are not extensively cited. Also a state of the art (including eventual references) on alternative approaches to achieve somatic ChR2 targeting will help in appreciating the novelty of the paper. The decision of using Kv2.1 voltage gated potassium channel to confine ChR2 targeting should be discussed more extensively.

Results and Discussion:

Figure 1 (left): The meaning of this figure is not clear. It seems that the authors want here to characterize the optical resolution of the system. If this is the case, lateral resolution will be better characterized by performing a lateral displacement of the excitation spot along the x and y direction and plotting the corresponding curves (similarly as was done in figure 1, right panel, for axial resolution). The 3D image is very confusing and not necessary.

Figure 2—figure supplement 2: Cross sections through the images are needed in order to appreciate the values for lateral and axial FWHM.

Figure 2A: The image showing the Alexa 594 distribution (central bottom panel) has a very reduced fluorescence spreading with respect to the central top one: this difference is not justified as the spreading should be comparable in the two cells: authors should probably choose a better example.

Figure 2D: The experiment on acute slice has been done only once: this is not enough to support their conclusion more statistics is needed. They should be able to derive for acute slice a figure similar to Figure 2B and C.

They need to discuss the effect of the planarity of the dendrites in the experiments: the excitation spot has been moved laterally along the objective focal plane, if the dendritic process is axially tilted this could also induce a decrease in the current (more statistic will enables removing this ambiguity).

In order to compare data from non targeted and targeted cells, authors should comment on the time they wait after injections in the two cases. Is this comparable? How long the somatic targeting stays somatic? Is there a critical time window after which the somatic ChR2 starts spreading along dendritic processes? Scale bar should be indicated in the bottom image. Why for the targeted ChR2, data have been taken with larger step?

Figure 2F: The authors should better explain how they obtained this figure; how do they define the threshold?

Figure 2G: In the caption they write "each position in a map was stimulated with the minimum power that reliably evoked action potential when stimulation was applied to the soma": they should better quantify the meaning of "reliably evoked action potential". Stimulation protocol (pulse duration, pulse frequency) should be indicated in the caption for all the experiments.

Figure 2—figure supplement 1: Not needed.

Figure 3: The data and procedure reported in this figures needed to be better presented and explained.

A picture showing the GCamp6 fluorescence before photostimulation is needed to visualize the distribution of the cells in rest condition.

It is not clear if the cell dye-filled and imaged in A is a ChR2 positive cell. If this is the case, authors need to show the current when the photostimulation spot is placed on the cell. The experiment should be repeated more than a single time to be convincing.

The construct used in Figure 3 uses ChR2 directly linked to GCamp6: this is a very powerful idea and should be better highlighted.

Results section: "[…] owing to the lower efficiency of spike generation by ChR2 in the absence of TF […]" this sentence is wrong. TF does not increase the efficiency of ChR2 excitation but only reduce the out of focus contribution, thus improving axial resolution.

"[…] and a reproducible current with appropriate synaptic delay and kinetics […]" this sentence is very vague, authors should define and quantify what is an "appropriate synaptic delay and kinetics".

The discussion on the biological results of in Figure 3 should be toned down. The paper is a methodological paper with interesting results and does not need in my opinion a biological conclusion that is not supported by enough data.

Reviewer #2:

The authors created a new construct that localizes ChR2 to the soma and proximal dendrites of neurons. When combined with two-photon beam shaping methods (e.g. temporal focusing), this should improve the ability to target and stimulate individual densely packed neurons without concurrently activating their neighbors.

While the new construct may alleviate some of the concerns typically associated with optical mapping of connectivity (i.e. the inability to precisely stimulate only neurons of choice), the data presented in this manuscript are far too preliminary to make an impact in the field of circuit mapping.

Detailed comments:

Figure 1: Much more quantification is needed. The important variable for circuit mapping (Figure 3) is whether or not a spike is elicited, rather than the inward current. The authors should determine on what fraction of trials a spike is elicited for each power, for each location. Currently only single-trial raw current-clamp data is shown in Figure 1, but some quantification of this is required, for example:

For the final power chosen, for each neuron, what fraction of trials led to a spike when the spot was directly on the soma, and what fraction of trials led to a spike when the spot was directly, vertically, above the neuron (i.e. position iv), which seems to be the most vulnerable position for eliciting unwanted action potentials?

What was the final power used for the example shown? 61mW is on the threshold of activating the neuron soma directly (position iii), and 89mW (the next power tested) is on the threshold of activating the neuron when the beam is not directed to the soma (position iv).

As far as I can make out, the authors go on to change the protocol later in the paper (Figure 3, "circuit mapping"), using 150ms long pulses in order to generate trains of action potentials. However, all of the analysis in Figure 1 needs to be redone with these experimental parameters, since longer stimulation pulses will increase the probability of unwanted spikes away from the location of light stimulation.

What is the latency to action potential for each of the laser powers?

Figure 2: In panel 2D, the authors should show an example of a "targeted" neuron (i.e. ChR2 localized to the soma), whilst stimulating at points along the apical dendrite at the same density as that shown for the "non-targeted" neuron. Also, the current elicited in the targeted neuron is here lower than the current elicited for the non-targeted neuron, which contradicts panel E, and is not "representative" – what was the stimulation power used in the two cases?

In panel 2G, the interesting variable is the average number of spikes elicited in current clamp and these data would have been more valuable.

Figure 3: The image quality needs to be refined, and some of the somata are poorly defined. This applies particularly to the cells that are assumed to be connected.

The voltage-clamp traces in panel 3C are single trial data. The authors should show multiple traces for each connection to convince the reader that a true connection is present, rather than an EPSC which happens to coincide with light stimulation.

The authors should quantify the calcium signals in all the neurons in the imaged population when a single neuron has been targeted for stimulation (beyond what's shown in Video 1 & 2, which are not informative). Crucially, the authors must show unambiguously that there was only one neuron active on each stimulation trial.

Reviewer #3:

The authors present a novel combination of two known methods, light shaping and opsin targeting, for the purpose of mapping synaptic connections in vitro. This is in principle a very elegant approach for improving the spatial precision of optogenetic activation, currently a key limitation in the field. However, the manuscript has a rather preliminary flavor (several of the key observations appear to be n = 1). The authors are in the position to provide a major advance here by performing a detailed quantification of how accurate and reliable their method is, using ground truth calibrations. For example, the authors have not quantified how accurate their method is with any paired recordings to prove the connections they find are real. They only state that the average connectivity is similar to that in other experiments in which pairs were directly recorded. Most importantly, the lack of detailed quantification (with mean, SD, and N) needs to be addressed prior to publication.

Major comments:

1) There are major details missing in Figure 1. What is the mean action potential reliability and resolution, i.e. the grand average result of Figure 1A across all neurons? What powers were typically used for AP generation at the soma in these experimental conditions? What are the max currents observed? Please provide mean, SD, and N. Note that the figure was not created with the construct that was ultimately used, which is a weakness.

2) How many cells were used to generate the data in Figure 2—figure supplement 2? It appears that some of the differences are statistically borderline and without complete data including the sample size it is difficult to determine the reliability of this result. Also, how did the authors determine the number of significant digits to include?

3) In describing Figure 3, the authors mention that 3 photostimulation trials are performed at each location. Could the authors please show raw trials, perhaps in a lighter shade behind the average, to indicate the reliability of observed connections?

4) Figure 3 uses a different stimulation duration that rest of paper – the photostimulation time has been increased to 150 ms for Figure 3. As this value doesn't match the previous calibrations, it is very difficult to use the data in Figure 2 to calibrate Figure 3. How does the longer duration affect spatial resolution, action potential threshold, etc.?

5) Many of the calcium imaging transients in Figure 3 are quite large, and sometimes double-peaked when there is only one EPSC observed (Figure 3C, bottom row, red square). How do the authors explain the discrepancy between the fact that these long photostimulations (150 ms!) may very well induce more than one action potential, but only one post-synaptic response is observed? Many cortical synapses may depress, but not sufficiently to explain these observations.

6) What is the cutoff for a connection and how reliable is this? For example, in the bottom row of Figure 3C, fourth from the right, there is a large calcium transient and some tiny EPSCs – could these be a weak connection?

7) How often do the authors observe failures to confirm pre-synaptic action potential generation with imaging? They only say "occasionally". Excluding these from analysis could heavily bias estimation of connectivity rates!

8) In Figure 3, the authors photostimulate 192 different locations in a grid-like fashion. They don't aim to zap neurons directly, but rather by shooting at many locations, they hope to hit some neurons by chance. A quick segmentation of the image to find neurons and shoot them directly would improve accuracy, reliability, and potentially even be more efficient! Why do the authors not target neurons initially?

9) Have the authors repeated the experiment shown in Figure 3 more than once? If so, please present some grand average data.

10) Losonczy et al. 2010, cited by the authors, shows effective activation of axons. How can the authors be sure that is not occurring here? Can they provide some presynaptic patch confirmations of any of the connections they see?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Single-cell resolution circuit mapping with temporal-focused excitation of soma-targeted channelrhodopsin" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We hope you will be able to submit the revised version within two months, so please let us know if you have any questions first.

Summary:

The development of somatically targeted opsins is one of the most promising ways of achieving true cellular resolution with optogenetics and will surely have a strong impact the neuroscience community. The authors have considerably improved the quality of the manuscript by adding more data and statistical analysis. There is a strong case now for arguing that this new construct is better suited for mapping connectivity in the circuit using targeted optogenetic stimulation. However a few points of the paper still need additional work before the manuscript is ready to proceed towards publication. We encourage the authors to proceed with these final experiments as a matter of urgency, as this is a highly competitive field.

Essential revisions:

1) The power levels used in the different experiments are often missing, and this information is crucial to appreciate the spatial resolution achieved in the experiments (e.g. how far are the powers used from the saturation value?). The powers used to evoke a single AP are rather high and latency and jittering are rather long compared to what has been reported in the literature. This point is particularly weak considering that in several parts of the manuscript the authors insist on the "enhanced sensitivity "of the targeted opsin. Overall this implies that the opsins (somatic or not) used in this experiments are not very efficient and may not be suitable for experiments requiring e.g. multi-spot stimulation. Many datapoints e.g. the ones showing cellular resolution, or the connectivity experiments, are only performed using the targeted opsins and it is difficult to appreciate their importance if one can't compare the same experiments performed with the non-targeted version.

2) In order to showcase the advantage of the 'new targeted' construct, it is crucial to include the axial and lateral profile of spike probability also for the 'non-targeted' construct in Figure 2C, D. Please add this quantification to existing panels in this figure. State the power at which these curves were obtained.

3) Figure 1B: line scans to demonstrate somatic targeting are all done along dendritic processes, while no information or data are provided to show the expression confinement along axons. This would be helpful.

4) Figure 1D: "each pixel in the map show the direct current" are the authors plotting the peak current here? Moreover from this map it is difficult to understand the depolarization achieved. The same experiment performed in current clamp would allow us to learn about the spike probability for spot placed out of the target, which ultimately is the key elements to support the necessity of the somatic opsin for the connectivity experiments in Figure 3 or to appreciate the enhanced spatial resolution (see next comment).

5) Figure 3 is nice. The quantification of these connectivity mapping experiments could be included in this figure rather than only in the Results section of the text. For completion, please add an additional example of another such slice experiment in an extra supplementary figure. Also, the information on the stimulation protocol used here is very vague: "each cell was stimulated in series with 2 seconds between stimuli": how many stimuli? What power did they use? How confined is the response if experiments as the ones showed in Figure 1 C-D are done using this protocol? How do these results compare if similar experiments are done with a non-somatic opsin?

6) In the discussion the authors justify the use of high power and long photostimulation power:

"We did not take full advantage of the temporal precision capability of TF to fire action potentials in our current study, instead focusing on a screening method that would identify connections without optimizing the amount of power that would fire each potential presynaptic neuron with minimal latency. We therefore chose longer pulses at a power sufficient to fire most neurons and generate trains of action potentials, which would elicit stronger signals with calcium indicators. For experiments requiring temporal precision, the minimization of action potential latency requires optimization of excitation area and laser power"

This paper should convince us about the use of a new optogenetic construct, and (as discussed above) a more detailed characterization of the opsin showing the photostimulation area and laser power that enables AP generation with a temporal resolution and precision comparable to what has been achieved in the literature is important and should be carried out.

7) The sentence "Furthermore, these techniques could also be used in vivo, where the enhanced sensitivity of the targeted ChR2 makes it especially attractive" is misleading: in the paper the authors do show that the targeted version is more sensitive than the non-targeted one. But in both cases they use excitation powers much higher than what has been achieved in the literature and demonstrate performances (temporal resolution, latency and jittering) inferior to what has been achieved with ChR2 or C1V1 by other labs. This should be reworded.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Single-cell resolution circuit mapping in mouse brain with temporal-focused excitation of soma-targeted channelrhodopsin" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder as the Senior editor, a Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) There remain concerns about the intensity and duration of the illumination pulses used (150 ms). This suggests that the construct is not very efficient. Why were such long pulses used? Were shorter pulses used in some experiments? The authors should either demonstrate that their construct is also effective in triggering spikes when using shorter pulses, or provide a convincing justification for the use of longer pulses.

2) Please add to the Methods section some of the text that is currently a response to point 1, related to stimulation power needed to excite the cells. ("Our manuscript reports excitation powers of between 15 and 285 mW (for both types of opsins); assuming our spot size to be at least 10 μm wide and 10 μm thick, we are using powers of no greater than 0.2 to 3.8 mW/μm2). Expressing power as mW/μm2 (rather than incident power in hundreds of mW) will be useful for readers.

3) 'Single-cell resolution' is advertised in the title, but is not well supported. We suggest changing the beginning of the title to 'Cellular resolution…'.

4) Please extend the comparison between your results and those of Wu et al. 2013 Plos ONE (since they originated the somatic restriction strategy).
