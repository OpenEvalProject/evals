# Peer review - Round 1

Editors:
- Marla B Feller, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90456.3.sa0](https://doi.org/10.7554/eLife.90456.3.sa0)

This important study uses a combination of computational modeling and glutamate imaging to show how a particular synaptic organization referred to as space-time wiring contributes minimally to a dendritic computation that occurs in the retina. The evidence supporting the claims of the authors is compelling, incorporating new findings regarding dynamic receptive field properties, an improvement over previous modeling and experimental results based on static visual stimuli. The work will be of interest to retinal neurobiologists and neurophysiologists interested in dendritic computations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90456.3.sa1](https://doi.org/10.7554/eLife.90456.3.sa1)

Summary:

Direction selectivity (DS) in the visual system is first observed in the radiating dendrites of starburst amacrine cells (SACs). Studies over the last two decades have aimed to understand the mechanisms that underlie these unique properties. Most recently, a 'space-time' model has garnered special attention. This model is based on two fundamental features of the circuit. First, distinct anatomical types of bipolar cells (BCs) are connected to proximal/distal regions of each of the SAC dendritic sectors (Kim et al., 2014). Second, that input across the length of the starburst is kinetically diverse, a hypothesis that has only recently gained some experimental support using iGluSnFR imaging (Srivastava et al., 2022). However, in these prior studies, the sustained/transient distinctions in BC input that are proposed to underlie direction selectivity were shown to be present mainly in responses to stationary stimuli. When BC receptive field properties are probed using white noise stimuli, the kinetic differences between proximal/distal BC input are relatively subtle or nonexistent (Gaynes et al., 2022; Strauss et al., 2022, Srivastava et al., 2022). Thus, if and how BCs contribute to direction selectivity driven by moving spots that are commonly used to probe the circuit remains to be clarified. To address this issue, Gaynes et al., combine evolutionary computational modeling (Ankri et al., 2020) with two-photon iGluSnFR imaging to address to what degree BCs contribute to the generation of direction selectivity in the starburst dendrites.

Strengths:

Combining theoretical models and iGluSnFR imaging is a powerful approach as it first provides a basic intuition on what is required for the generation of robust DS, and then tests the extent to which the experimentally measured BC output meets these requirements.

The conclusion of this study builds on the previous literature and comprehensively considers the diverse BC receptive field properties that may contribute to DS (e.g. size, lag, rise time, decay time).

By 'evolving' bipolar inputs to produce robust DS in a model network, these authors provide a sound framework for understanding which kinetic properties could potentially be important for driving downstream DS. They suggest that response delay/decay kinetics, rather than the center/surround dynamics are likely to be most relevant (albeit the latter could generate asymmetric responses to radiating/looming stimuli).

Weaknesses:

Finally, these authors report that the experimentally measured BC responses are far from optimal for generating DS. Thus, the BC-based DS mechanism does not appear to explain the robust DS observed experimentally (even with mutual inhibition blocked). Nevertheless, I feel the comprehensive description of BC kinetics and the solid assessment of the extent to which they may shape DS in SAC dendrites, is a significant advancement in the field.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90456.3.sa2](https://doi.org/10.7554/eLife.90456.3.sa2)

Summary:

In this study, the authors sought to understand how the receptive fields of bipolar cells contribute to direction selectivity in starburst amacrine cell (SAC) dendrites, their post synaptic partners. In previous literature, this contribution is primarily conceptualized as the 'space-time wiring model', whereby bipolar cells with slow-release kinetics synapse onto proximal dendrites while bipolar cells with faster kinetics synapse more distally, leading to maximal summation of the slow proximal and fast distal depolarizations in response to motion away from the soma. The space-time wiring contribution to SAC direction selectivity has been extensively tested in previous literature using connectomic, functional, and modeling approaches. However, the authors argue that previous functional studies of bipolar cell kinetics have focused on static stimuli, which may not accurately represent the spatiotemporal properties of the bipolar cell receptive field in response to movement. Moreover, this group and others have recently shown that bipolar cell signal processing can change directionally when visual stimuli starts within the receptive field rather than passing through it, complicating the interpretation of moving stimuli that start within a bipolar cell of interest's receptive field (e.g. stimulating only one branch of a SAC or expanding/contracting rings). Thus, the authors choose to focus on modeling and functionally mapping bipolar cell kinetics in response to moving stimuli across the entire SAC dendritic field.

General Comments:

There have been several studies that have addressed the contribution of space-time wiring to SAC process direction selectivity. This study offers a more complete assessment of potential impact space-time wiring can have on this dendrite computation. The experimental results based on glutamate imaging assess the kinetics of glutamate release under conditions of visual stimulation across a large region of retina largely confirm previous observations. By combining their model with this experiment data, they conclude that even the optimal space-time wiring is not sufficient to explain the SAC process DS. Though there is no conclusion which of the many other proposed cellular and circuit mechanisms could potentially contribute to this computation, the limited role for spacetime wiring is firmly established.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90456.3.sa3](https://doi.org/10.7554/eLife.90456.3.sa3)

Summary:

Gaynes et al. investigated the presynaptic and postsynaptic mechanisms of starburst amacrine cell (SAC) direction selectivity in the mouse retina by computational modeling and glutamate sensitivity (iGluSnFR) imaging methods. Using the SAC computational simulation, the authors initially tested bipolar cell contributions (space-time wiring model, presynaptic effect) and SAC axial resistance contributions (postsynaptic effect) to the SAC DS. Then, the authors conducted two-photon iGluSnFR imaging from SACs to examine the presynaptic glutamate release and found seven clusters of ON-responding and six clusters of OFF-responding bipolar cells. They were categorized based on their response kinetics: delay, onset phase, decay time, and others. Finally, the authors used cluster data to reconstruct bipolar cell inputs to SACs that generate direction selectivity. They concluded that presynaptic effects through the space-time wiring model only account for a fraction of SAC DS.

The article has many interesting findings, and the data presentation is superb. Strengths and weaknesses are summarized below.

Major Strengths:

The authors utilized solid technology to conduct computational modeling with Neuron software and a machine-learning approach based on evolutionary algorithms. Results are effectively and thoroughly presented.

The space-time wiring model was evaluated by changing bipolar cell response properties in the proximal and distal SAC dendrites. Many response parameters in bipolar cells are compared, and DSI is compared in Figure 3. These parameter comparisons are valuable to the field.

Two-photon microscopy was used to measure the bipolar cell glutamate outputs onto SACs by conducting iGluSnFR imaging. All the data sets, including images and transients, are elegantly presented. The authors analyzed the response based on various parameters, which generated more than several response clusters. The clustering is convincing.

Major Weaknesses:

The computational modeling demonstrates intriguing results: SAC dendritic morphology produces dendritic isolation, and a massive input overcomes the dendritic isolation (Figure 1). This modeling seems to be generated by basic dendritic cable properties. However, it has been reported that SAC dendrites express Kv3 and voltage-gated Ca channels. Are they incorporated into this model? If not, how about comparing these channel contributions?

In Figure 9 the authors generated the bipolar cell cluster alignment based on the space-time wiring model. The space-time wiring model has been proposed based on the EM study that distinct types of bipolar cells synapse on distinct parts of SAC dendrites (Green et al 2016, Kim et al 2014). While this is one of the representative Reicardt models, it is not fully agreed upon in the field (see Stincic et al 2016). Therefore, the authors' approach might be only hypothetical without concrete evidence for geographical cluster distributions. Is there any data suggesting each cluster's location on the SAC dendrites? I assume that the iGluSnFR imaging was conducted on the SAC dendritic network, which does not provide geographical information. How about injecting the iGluSnFR-AAV at a lower titer, which labels only some SACs in a tissue? This method may reveal each cluster's location on SAC dendrites.

The authors found that there are seven ON clusters and six OFF clusters, which are supposed to be bipolar cell terminals. However, bipolar cells reported to provide synaptic inputs are T-7, T-6, and multiple T-5s for ON SACs and T-1, T-2, and T-3s for OFF SACs. The number of types is less than the number of clusters. Is there a possibility of clusters belonging to glutamatergic amacrine cells? Please provide a discussion regarding the relations between clusters and cell types.

In Figure 5B, representative traces are shown responding to moving bars in horizontal directions. These did not show different responses to two directional stimuli. Is there any directional preference from other ROIs? Yonehara's group recently exhibited the bipolar cells' direction selectivity (Matsumoto et al 2021). Did you see any correlations with their results? Please discuss.
