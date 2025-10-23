# Peer review - Round 1

Editors:
- Timothy E Behrens, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91627.sa0](https://doi.org/10.7554/eLife.91627.sa0)

This manuscript will be valuable to scientists working on visual neurobiology and cortical processing. It uses a compartmental model to evaluate the relative contribution of basal and apical dendritic trees to the orientation selectivity of layer 2/3 pyramidal cells. There is solid support for the key claims that pertain to the model itself, but there are some questions as to how well the model reflects the biological circuit.


---

# Peer review - Round 1

Editors:
- Timothy E Behrens, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91627.sa1](https://doi.org/10.7554/eLife.91627.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "A Tale of Two Trees: Modeling Apical and Basal Tree Contribution to L2/3 V1 Pyramidal Cell Orientation Selectivity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Reviewer #1 (Recommendations for the authors):

This work aims to determine the contribution of apical and basal dendrites to orientation selectivity in a cortical neuron. This is a relevant question because basal and apical dendrites receive different qualitatively different classes of inputs: feedforward inputs favour basal dendrites whereas feedback inputs preferentially target apical dendrites. Understanding the rules by which these two dendritic fields interact at the level of single neurons is therefore useful for understanding and predicting how different information streams might be integrated by cortical neurons. Here, the authors take a compartmental modelling approach. Using a previously established model of a layer 2/3 pyramidal cell, they systematically vary some of the model parameters to explore and quantify how much apical and basal dendrites contribute to the generation of somatic spikes when synaptic input is tuned to orientation. The main conclusion is that both apical and basal contribute to spiking, with the apical contribution depending more on sodium conductances and the basal contribution depending mostly on AMPA and NMDA receptors. This conclusion is well supported by the data and the parameter exploration presented will be useful to the field. While the data come from a compartmental model, attempts to understand the biophysical basis of the phenomena described are limited and often not grounded in the current knowledge of cortical neuron biophysics. This aspect of the manuscript could be significantly expanded.

Strengths:

The main strength of this paper is the systematic variation of parameters such as synapse distribution and background activity, and the subsequent quantification of the effect of changing these parameters on somatic spiking. The disparity experiments are interesting, especially for seeing when orientation selectivity breaks down, and extend the modelling results presented in Park et al. 2019. The temporally precise manipulations of conductances and direct spike-by-spike comparison between control and manipulation conditions is a new and nice approach that should be useful for future studies. Another potential strength is the attempt to match the background activity observed in vivo, though this effort has significant weaknesses.

Weaknesses:

Most of the results in the paper describe the behavior of the model when a set of parameters are changed. While this is useful information, the major strength of a model is that it should be possible to understand exactly why model behaves the way it does, but the authors do not make a serious attempt at this. Why do apical dendrites rely more on sodium conductances to influence somatic spiking? Why do basals rely more on AMPA and NMDA conductances? What exactly is different in terms of the spatiotemporal patterns of inputs and voltage propagation across the neuron during "apical", "basal" and "cooperative" somatic spikes? The risk here is that the model behavior might only be valid for a restricted set of parameters (eg: density and distribution of conductances, most of which are not known experimentally), and thus the generality of the findings might be limited. Understanding the biophysics should allow for deriving general rules for the problem studied here and more robust conclusions.

Figure 6 is a step in this direction, but it mostly shows that the number of synapses to reach threshold increases with cable diameter and decreases with distance from soma, which is well known (ie: where the passive and active properties of the cable are uniform, as they are here, the result is explained by the differences in input impedance). The lack of granularity is well illustrated in the title of section 3.6.: "Morphological and Electrophysiological Properties Influence Dendritic Behavior" – indeed they do, this is very well known. But how exactly in this model? Overall, I would have expected a more thorough analysis of the relationships between voltage propagation, morphology, and synaptic activation pattern. For example, could the main results here be explained by fast sodium spikes being more heavily filtered by the basal dendrites (which tend to have a shorter spatial constant, eg : Nevian et al. 2007), which would also explain the higher dependency of the basals on NMDA conductances, which are slower and therefore less filtered? Or are there differences in the relationship between synaptic input patterns and the generation of local non-linearities between basals and apicals?

The attempt to use experimental calcium imaging data to estimate background activity is nice, but the data are not very convincing. In Figure 2C, most of the isolated dendritic events look like noise. I realise that the event-triggered average shown in 3D suggests that there is some real signal being analysed, but I suspect that it is heavily contaminated by noise, and that the authors are grossly over-estimating the frequency of decoupled dendritic events. The method details of the analysis procedure are also worrying: "These percentile values were calculated via trial-and-error, attempting to match the expected firing frequency of a neuron (soma) under spontaneous activity conditions". What is the rationale here? The goal should be to detect the real events in the data, not changing the detection parameters until the result matches a previous publication. Also, if in the end the goal was to obtain the same value as other studies, it is unclear why the experiment was needed in the first place.

1. The authors propose that in Figure 1 they are validating their modelling approach, but it is unclear what exactly is being validated here. The figure shows that dendrites with sodium channels and AMPA/NMDA synapses can generate non-linear input-output curves, which is very much a guaranteed finding – in a model with reasonable passive parameters and morphology (which is the case here since model that has been previously validated against experimental data), I don't see how the result could be any different. Please clarify.

2. Line 587: figure call is wrong, should be 4A (same for the subsequent call)

3. In Figure 6 it is not clear why the results in panel C are qualitatively different that in A. Rm and Ra are presumably uniform, so the electrotonic constant is a transform of the dendritic diameter. Please explain.

Reviewer #2 (Recommendations for the authors):

The manuscript by Petousakis et al. describes a modeling study of a pyramidal neuron in the Layer 2/3 (L2/3) of mouse primary visual cortex V1. The authors use a biophysically detailed, spatially extended model of the neuron, with voltage-gated conductances in the soma, basal dendrites, and apical dendrites to investigate how inputs to basal and apical dendrites sculpt the activity of the neuron and the corresponding major computation that L2/3 excitatory cells presumably carry out – that of orientation detection. The authors report a number of computational experiments and conclude that inputs to basal and apical dendrites synergistically sculpt the orientation selectivity of the neuron.

While the premise is interesting, the study, and especially the model architecture, relied on a number of assumptions that limit the interpretability of the outcomes.

1. The whole study is based on a single model of one neuron. This is a model from Park et al., Nature Communications, 2019, which in turn is based upon other previously published models (e.g., the supplementary tables 2-4 in this manuscript are copied from the Park et al. paper). Park et al. already showed how one can get orientation selectivity with this neuron model and how it can be manipulated by ablating apical and basal dendrites.

2. There is a lot of data on function-dependent connectivity for L2/3 excitatory neurons that sculpts orientation selectivity, but the authors do not mention even the most prominent of the papers in this area. First, it has been shown that excitatory connections are like-to-like (with respect to orientation and/or direction preference), in papers such as Ko et al., Nature, 2011; Cossell et al., Nature, 2015; Lee et al., Nature, 2016; Wertz et al., Science, 2015; Rossi et al., Nature, 2020. Second, there are indications that inhibitory connections are also structured non-randomly with respect to neuron tuning properties (Znamensky et al., biorXiv, 2018). And Rossi et al., Nature, 2020, showed that inhibitory inputs to L2/3 E neurons form a pool that's shifted retinotopically relative to the pool of excitatory inputs. None of these features of connectivity are taken into account by the presented model. It is possible that a model with these known biological features would lead to different conclusions.

In fact, the results presented here contradict the results from the same group of authors published in Park et al., 2019, as they point out in Discussion:

"in vivo micro-ablation via laser of the apical tree in L2/3 mouse V1 pyramidal neurons did not abolish orientation selectivity, which remained essentially unchanged following a recovery period of ~ 1 day."

The authors explain this contradiction by potential homeostatic mechanisms "that might alter the dependence of somatic spiking on basal inputs". But given the points above, it seems equally likely that a more realistic model would have produced these effects. Since this observation is available from in vivo data, why not use it to constrain the model? That seems like the most natural thing to do, and I suspect modeling results with respect to the factors contributing to orientation selectivity would be then quite different.

3. Modeling inhibitory synapses as just noise, without any orientation tuning, is a limitation. Inhibitory neurons certainly show orientation tuning.

4. Overall, using constant-rate Poisson process for all synapses is suboptimal. Cortical neurons generally exhibit log-normal distributions of firing rates, meaning that a single rate for all inputs of a given type is far from realistic. Also, feedback inputs are typically delayed relative to feedforward inputs by about 10 ms; that would be important to take into account.

5. Orientation-tuned synapses should certainly exhibit different amounts of activity for different orientations. Here, synapses are always activated at 0.3 Hz, and their orientation preference is modeled by changing their weight depending on orientation. That is unrealistic. It is the presynaptic activity that changes depending on the orientation, and not the synaptic weight. (Weights can change due to plasticity, but the authors ignore plasticity here, and plasticity can work in either direction – depressing or facilitating – depending on the cell types.)

Some of the points above may seem like minor details, but they are not – consequences of such choices can be substantial. Such assumptions establish the correlation structure of synaptic inputs that is very different from what we know to happen in reality. Since the authors are investigating fine details of neuronal operation, including coincidence of basal and apical inputs, such effects are likely important for their study.

1. Both this manuscript and Park et al. compare the model voltage response to a somatic current injection with that from experiment (for a single cell), but no evidence is provided that electrophysiological properties of dendrites are captured well. In other words, we have no idea if currents and voltages in dendrites in response to synaptic inputs, local current injections, or somatic spikes or current injections, are captured well by the model. Capturing such properties well seems very important for the subject of the study, so, in the absence of a proof that it's working well, it is hard to trust any results from the model.

2. It's not clear why background-driven synapses all have the same activation frequency. Inhibitory synapses should be activated with higher rates, since many inhibitory neurons, especially PV fast-spiking neurons, fire at substantially higher rates than excitatory cells. The rates, 0.11 Hz for spontaneous and 0.3 Hz for orientation tuned inputs, seem too low. It is also not clear whether all synapses receive inputs from just two Poisson processes, or each synapse receives input from its own Poisson process. The former obviously creates unphysiological correlations between synapses, whereas the latter provides no correlations, which is also incorrect (it is well known that activity of neurons in the cortex is correlated – not perfectly, but substantially). Some middle ground informed by the data would be better than either of these extremes. While it may seem like an unimportant detail, in fact it is hugely important for the topic of the study, since correlations between incoming spikes will strongly influence the dendritic processing and coincidence detection.

3. Another big problem with using Poisson spike trains to simulate orientation selectivity is that it completely ignores the spatial structure of the stimulus. The model used only has stronger or weaker input depending on the orientation, but it's always Poisson random input. In reality, a neuron exposed, say, to a drifting grating, will be subject to alternating black and white stripes, which strongly modulate firing. The resulting firing pattern typically has periods when spikes follow each other in close succession and periods when there are barely any spikes at all. This temporal structure of synaptic activation, reflecting the spatial structure of the stimulus and retinotopic distribution of presynaptic neurons, is very likely to have strong effects on the postsynaptic neuron output and phenomena like dendritic integration.

I understand that my comments will be disappointing to the authors, and I am sorry for that. But I hope the comments might be helpful for their future work, and I am sure their approach will continue providing new interesting insights.
