# Peer review - Round 1

Editors:
- Megan R Carey, Champalimaud Foundation Portugal

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55592.sa1](https://doi.org/10.7554/eLife.55592.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript investigates the effect of GABAergic input on control of SNr activity, with a focus on how the shift in chloride reversal may change an inhibitory response to excitatory. It effectively combines experiments and modeling and spans cellular and network effects.

Decision letter after peer review:

Thank you for sending your article entitled "A computational model explains and predicts substantia nigra pars reticulata responses to pallidal and striatal inputs" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Kate Wassum as the Senior Editor.

Concerns about the extent of direct experimental evidence for the paper's conclusions were raised by both reviewers 1 and 2. Meanwhile, questions about the physiological relevance of the model's assumptions were raised by both reviewers 2 and 3. These criticisms are both central to the manuscript's claims. The possibility was raised that despite the lack of direct experimental evidence, the paper could be considered as primarily a modeling paper with some supporting experiments. However, it was agreed that for the modeling evidence to stand on its own as prediction and verification of likely changes in ECl in biological neurons, a substantially more convincing bridge to biophysically relevant parameters needs to be demonstrated. Therefore, during the consultation process, there was consensus that there were enough uncertainties about both the extent of direct experimental evidence and of the physiological relevance of the model's assumptions that it was premature to move forward with publication at this stage. However, there is also quite a lot of positivity in the reviews, and the suggestions for new experiments and revisions are straightforward. Therefore, there appear to be several possible paths that successful revision might take.

In addition to the full reviews included below, the following points and suggestions were raised during consultation:

Regarding direct experimental evidence:

Gramicidin perforated patch-clamp experiments are hard but doable, and they could be used to show that EGABA is changed following stimulation via both GPe and Str input. One might still see shifts in EGABA in whole-cell mode, especially following dendritic input, as the a whole-cell patch can't effectively clamp Cl– especially peripherally. An easier, more achievable experiment may be for them to repeat the cell attached experiments in the presence of selective KCC2 blockade (VU0463271 is the best), they should see a different distribution with more excitatory / biphasic responses etc. (There is a bit of controversy about pharmacological KCC2 enhancers – it's not clear those work).

Regarding Figure 6:

For the slice data shown in Figure 6 please report the number of mice, slices and neurons.

Were excitatory and/or cholinergic inputs pharmacologically blocked? Even if an inhibitory pathway was directly stimulated, in the time course shown, network effects could lead to excitation. Admittedly, the network effect candidates in slices are more limited than in vivo, but this should be ruled out.

Reviewer #1:

In their study "A computational model explains and predicts substantia nigra pars reticulata responses to pallidal and striatal inputs" Phillips et al. use computational models of substantia nigra pars reticulata (SNr) neurons which account for Cl- dynamics to explain experimentally observed diversity in output responses following different GABAergic input. They then explore how Cl- dynamics may account for how inhibitory input tunes the response properties of theses neurons under various conditions. They present in vivo data which is consistent with predictions from their model. I agree that the demonstration of biphasic responses are a good indication that Cl- accumulation is occurring. In general, I am enthusiastic about this work, which uses computational modelling of Cl- dynamics (which is often forgotten) to good effect to explain the diversity of experimental observations. I have no major comments for the authors to address.

Reviewer #2:

In this manuscript Phillips et al. examine the implications of depolarization in the chloride reversal potential (ECl) in SNr neurons that could be triggered by chloride inflow due to tonic inhibitory input. Certainly SNr neurons are receiving a constant barrage of inhibitory inputs in vivo from GPe as well as striatum as described by the authors, and are a good candidate to ask these questions. The authors pursue a dual modeling and experimental approach to first argue for the likelihood that such depolarizing changes do occur, and second discover implications of such shifts on firing rates, slow oscillations, SNr synchronization, and changes in behaviourally relevant inhibitory responses. These finding are quite intriguing and the reviewer agrees with the authors that the results described are consistent with ECl shifts performing important functional roles. However, throughout the entire set of simulations and experiments no direct evidence is brought forward towards the main hypothesis, and at each step alternative interpretations do exist. It is the opinion of this reviewer that such direct evidence needs to be delivered in order to make the study compelling, and that several types of experiments would be feasible to do so.

Major comments:

I will break these down into comments about experiments (A) and simulations (B).

A1) A direct demonstration of a shift of ECl with GPe and Str input stimulation in slices should be made. A number of experiments could fully or partly deliver such evidence. As the authors indicate in the Discussion, perforated patching of SNr neurons might be ideal – and while not feasible in dendrites, it would be feasible on cell bodies. A bit simpler technically, and a little less powerful, would be to break into whole cell mode from the cell attached recording, and repeat stimulation after the chloride from the pipette controls ECl. Excitatory stimulation effects and biphasic effects should disappear. In addition there are KCC2 blockers and enhancers available (see e.g. Hamidi and Avoli, 2015) and their use could shed light on the observed effects also. For instance, adding a KCC2 enhancer should shift biphasic responses towards pure inhibition.

A2) There are no experimental methods given at all for the in vivo data shown in Figure 10. It is not even clear if the mice were anesthetized or awake. A lot of the details seem to be taken from Whalen et al., 2020, but this paper is not published yet. A copy of the Whalen manuscript should be attached to the eLife submission. Is Figure 10 a part of this study? The disappearance of slow oscillations with GPe stimulation is clear, but quite a number of alternative explanations not related to ECl in SNr exist for such a finding. To match the model more directly, it would be better to express halorhodopsin in the SNr, and directly control local chloride flow into the cell, instead of backfiring a large population of GPe axons that likely leads to network effects in the GPe and potentially STN.

B1) There is no statement in the manuscript that modeling scripts will be made available. For models to be replicable they need to be available and sharing is best done by posting on Yale ModelDB. This should be indicated in the manuscript.

B2) The model is a highly simplified 2-compartment model of SNr neurons. A careful match with the physiological properties of biological SNr neurons is not shown. Such a match is claimed in the text without evidence – this would be great material for a supplemental figure. (For instance, the spike cycle diagram in Figure 1D shows some obvious differences with the experimental diagram shown by Atherton et al., 2005. The AHP in Atherton et al. is -70 mV, and only -60 mV in the model, and the max dv/dt is over 200 in the data, and less than 150 in the model). The reviewer largely agrees that as a demonstration model of how ECl shifts affect the responses to inhibition such detail may not be needed to match the data accurately. However, when it comes to the predictive power of the model with respect to time courses and levels of Cl concentration changes in the intracellular volume, a more detailed justification of how the volumes were chosen, and how the levels of KCC2 and Cl conductance are likely to map onto reality, should be given. The representation of multiple thin dendrites with a single lumped dendrite may impact such dynamics. Please discuss the appropriateness of the lumped dendrite for radial and axial chloride flow. With respect to Figure 11, how was the somato-dendritic coupling in terms of chloride flow chosen, and why would it match biophysical properties of SNr neurons?

B3) The use of 2 connected equal SNr model neurons to predict oscillations or synchrony in vivo seems poorly justified. Given the input from about 4 SNr neurons onto any given SNr neuron, a network of such sparsely connected neurons with varying delays in the axonal connection, as well as different basal firing rates plus some added noise might perform quite differently from the pair of connected neurons. To make more realistic predictions, it would be nice to see a network model of such heterogenous model neurons with realistic noise added as well.

Reviewer #3:

This manuscript investigates the effect of GABAergic input on control of SNr activity, with a focus on how the shift in chloride reversal may change an inhibitory response to excitatory. It is a great example of discoveries through synergistic interactions between modelers and experimentalists. The research spans cellular and network effects. The authors provide a fantastic explanation of the very difficult concept of PRC for single neurons. I especially appreciate Figure 10 – the in vivo test of effect of GPe stimulation, which has no effect on firing rate but suppresses oscillations. Overall it is a very well written manuscript and makes a significant contribution to our understanding of basal ganglia information processing.

Major concerns:

Figure 5: The authors need to comment on the relevance of change in effect, e.g. partial inhibition, over 1 sec given that SPNs do not fire at 20 Hz for 1 sec. Though a group of SPNs may indeed do that, these inputs would be distributed over multiple dendritic branches and therefore may not produce change in ECl.

The PRC for coupled neurons is difficult to understand. In Figure 8, additional figure panels showing the traces and histogram for one or two cases would be helpful. Also, how similar do the two neurons need to be? What if coupled neurons are firing at different rates? This is especially important to show results when these neurons are firing closer to in vivo rates.

Figure 11: A single neuron mean firing rate > 20 Hz is not observed in the striatum. Perhaps the term "mean firing" refers to entire striatum and not to single neurons? If so, the authors need to use a different word. If not, it seems the model will not exhibit suppression for physiological rates. Again, this needs to be mentioned and put in context.

Regarding the coupling between soma and dendrite: given the length of dendrites, is 200ms a reasonable value for diffusion of chloride into the dendrite?

A repeated t-test is not the appropriate test here: "The spiking in each bin was then compared to baseline using t-tests where a p-value less than 0.05 was considered statistically significant." At the very least, correction for multiple t-tests is required. Ideally, a repeated measures ANOVA should be done.
