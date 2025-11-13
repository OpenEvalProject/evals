# Learning excitatory-inhibitory neuronal assemblies in recurrent networks

## Authors

- Owen Mackwood<sup>1</sup> ([ORCID: 0000-0001-8569-6614](https://orcid.org/0000-0001-8569-6614))
- Laura B Naumann<sup>1</sup> ([ORCID: 0000-0002-7919-7349](https://orcid.org/0000-0002-7919-7349))
- Henning Sprekeler<sup>1</sup> ([ORCID: 0000-0003-0690-3553](https://orcid.org/0000-0003-0690-3553)) †

### Affiliations

1. Bernstein Center for Computational Neuroscience Berlin Berlin Germany
2. Department for Electrical Engineering and Computer Science, Technische Universität Berlin Berlin Germany

† Corresponding author

## Abstract

Understanding the connectivity observed in the brain and how it emerges from local plasticity rules is a grand challenge in modern neuroscience. In the primary visual cortex (V1) of mice, synapses between excitatory pyramidal neurons and inhibitory parvalbumin-expressing (PV) interneurons tend to be stronger for neurons that respond to similar stimulus features, although these neurons are not topographically arranged according to their stimulus preference. The presence of such excitatory-inhibitory (E/I) neuronal assemblies indicates a stimulus-specific form of feedback inhibition. Here, we show that activity-dependent synaptic plasticity on input and output synapses of PV interneurons generates a circuit structure that is consistent with mouse V1. Computational modeling reveals that both forms of plasticity must act in synergy to form the observed E/I assemblies. Once established, these assemblies produce a stimulus-specific competition between pyramidal neurons. Our model suggests that activity-dependent plasticity can refine inhibitory circuits to actively shape cortical computations.

## Introduction

With the advent of modern optogenetics, the functional role of inhibitory interneurons has developed into one of the central topics of systems neuroscience (Fishell and Kepecs, 2020). Aside from the classical perspective that inhibition serves to stabilize recurrent excitatory feedback loops in neuronal circuits (van Vreeswijk and Sompolinsky, 1996; Brunel, 2000; Murphy and Miller, 2009; Sprekeler, 2017), it is increasingly recognised as an active player in cortical computation (Isaacson and Scanziani, 2011; Priebe and Ferster, 2008; Rubin et al., 2015; Pouille and Scanziani, 2001; Letzkus et al., 2011; Adesnik et al., 2012; Hennequin et al., 2014; Phillips et al., 2017; Barron et al., 2016; Barron et al., 2017; Tovote et al., 2015).

Within cortical neurons, excitatory and inhibitory currents are often highly correlated in their response to stimuli (Wehr and Zador, 2003; Froemke et al., 2007; Tan et al., 2011; Bhatia et al., 2019), in time (Okun and Lampl, 2008; Dipoppa et al., 2018) and across neurons (Xue et al., 2014). This co-tuning of excitatory and inhibitory currents has been attributed to different origins. In topographically organised sensory areas such as cat primary visual cortex (V1), the co-tuning with respect to sensory stimuli could be a natural consequence of local feedback inhibition and does not impose strong constraints on inhibitory circuitry (Harris and Mrsic-Flogel, 2013). In the case of feedforward inhibition, co-tuning of excitatory and inhibitory currents was suggested to arise from homeostatic synaptic plasticity in GABAergic synapses (Vogels et al., 2011; Clopath et al., 2016; Weber and Sprekeler, 2018; Hennequin et al., 2017).

In sensory areas with poor feature topography, such as V1 of rodents (Ohki et al., 2005), feedback inhibition has been hypothesised to be largely unspecific for stimulus features, a property inferred from the dense connectivity (Fino and Yuste, 2011; Packer and Yuste, 2011) and reliable presence of synapses connecting pyramidal (Pyr) neurons to inhibitory interneurons with dissimilar stimulus tuning (Harris and Mrsic-Flogel, 2013; Bock et al., 2011; Hofer et al., 2011). However, recent results cast doubt on this idea of a ‘blanket of inhibition’ (Fino and Yuste, 2011; Packer and Yuste, 2011).

In mouse V1, Znamenskiy et al., 2018 report that although the presence of synaptic connections between Pyr cells and parvalbumin-expressing (PV) interneurons is independent of their respective stimulus responses, the efficacy of those synapses is correlated with their response similarity, both in PV → Pyr and in Pyr → PV connections. These mutual preferences in synaptic organisation suggest that feedback inhibition may be more stimulus-specific than previously thought and that Pyr and PV neurons form specialised—albeit potentially overlapping—excitatory-inhibitory (E/I) assemblies (Chenkov et al., 2017; Yoshimura et al., 2005; Litwin-Kumar and Doiron, 2012; Litwin-Kumar and Doiron, 2014). While the presence of such E/I assemblies (Znamenskiy et al., 2018; Rupprecht and Friedrich, 2018) suggests the need for an activity-dependent mechanism for their formation and/or refinement (Khan et al., 2018; Najafi et al., 2020), the requirements such a mechanism must fulfil remain unresolved.

Here, we use a computational model to identify requirements for the development of stimulus-specific feedback inhibition. We find that the formation of E/I assemblies requires a synergistic action of plasticity on two synapse types: the excitatory synapses from Pyr neurons onto PV interneurons and the inhibitory synapses from those interneurons onto the Pyr cells. Using ‘knock-out experiments’, in which we block plasticity in either synapse type, we show that both must be plastic to account for the observed functional microcircuits in mouse V1. In addition, after the formation of E/I assemblies, perturbations of individual Pyr neurons lead to a feature-specific suppression of other Pyr neurons as recently found in mouse V1 (Chettih and Harvey, 2019). Thus, synergistic plasticity of the incoming and outgoing synapses of PV interneurons can drive the development of stimulus-specific feedback inhibition, resulting in a competition between Pyr neurons with similar stimulus preference.

## Results

To understand which activity-dependent mechanisms can generate specific feedback inhibition in circuits without feature topography—such as mouse V1 (Figure 1a), we studied a rate-based network model consisting of $N^{E}=512$ excitatory Pyr neurons and $N^{I}=64$ inhibitory PV neurons. To endow the excitatory neurons with a stimulus tuning similar to Pyr cells in layer 2/3 of mouse V1 (Znamenskiy et al., 2018), each excitatory neuron receives external excitatory input that is tuned to orientation, temporal frequency and spatial frequency (Figure 1b). The preferred stimuli of the Pyr neurons cover the stimulus space evenly. Because we are interested under which conditions feedback inhibition can acquire a stimulus selectivity, inhibitory neurons receive external inputs without stimulus tuning, but are recurrently connected to Pyr neurons. While the network has no stimulus topography, Pyr neurons are preferentially connected to other Pyr neurons with similar stimulus tuning (Hofer et al., 2011; Cossell et al., 2015), and connection strength is proportional to the signal correlation of their external inputs. Note that the Pyr → Pyr connections only play a decisive role for the results in Figure 4 but are present in all simulations for consistency. Connection probability across the network is $p=0.6$, with the remaining network connectivity (Pyr → PV, PV → PV, PV → Pyr) initialised randomly according to a log-normal distribution (Song et al., 2005; Loewenstein et al., 2011), with a variability that is similar to that measured in the respective synapses (Znamenskiy et al., 2018).

![Figure 1.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig1-v1.jpg)

**Figure 1.:** (a) Emergence of E/I assemblies comprised of pyramidal (Pyr) neurons (triangles) and parvalbumin-expressing (PV) interneurons (circles) in circuits without feature topography. (b) Network architecture and stimulus tuning of external inputs to Pyr cells. (c) Stimulus selectivity of Pyr neurons and PV interneurons (before and after learning). Arrows indicate the median. (d) Example responses of reciprocally connected Pyr cells and PV interneurons. Examples chosen for large, intermediate, and low response similarity (RS). Numbers correspond to points marked in (e). (e) Relationship of synaptic efficacies of output (left) and input connections (centre) of PV interneurons with RS. Relationship of input and output efficacies (right). Black lines are obtained via linear regression. Reported r and associated p-value are Pearson’s correlation. (f) Stimulus tuning of excitatory and inhibitory currents onto an example Pyr cell, before and after learning. For simplicity, currents are shown for spatial and temporal frequency only, averaged across all orientations. (g) Angle between the weight update and the gradient rule while following the local approximation for input (top) and output (bottom) connections of PV interneurons. Time course for first 4% of simulation (left) and final distribution (right) shown. Black lines are low-pass filtered time courses.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (a) Schematics of PV → Pyr plasticity (left) and Pyr → PV plasticity (right). PV → Pyr plasticity follows a simple logic: A given inhibitory synapse is potentiated if the postsynaptic Pyr neuron fires above target and is depressed if below. The Pyr → PV plasticity compares the excitatory input current received by the postsynaptic PV neuron to a target value, and adjusts the incoming synapses in proportion to this error and to presynaptic activity. (b) Time plots of the Pyr population firing rate (top), mean of all PV → Pyr synaptic weights (middle) and Pyr → PV weights (bottom). Columns correspond to simulations in which both PV → Pyr and Pyr → PV plasticity are present (left), only Pyr → PV is present (middle), and only PV → Pyr is present (right).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (a) In a network learning with the derived gradient rules of Equation 15, significant correlations are reliably detected between response similarity (RS) and excitatory weights (red bars), RS and inhibitory weights (blue bars), and excitatory and inhibitory weights for reciprocally connected pyramidal (Pyr)-PV cell pairs (black bars) only if both synapse types are plastic. (b) Interneurons fail to develop stimulus selectivity if their input weights do not change according to the gradient rule of Equation 15a. (c) Synaptic currents onto Pyr neurons only develop reliable, strong excitatory-inhibitory (E/I) co-tuning if both input and output synapses are updated using the gradient rules. Currents are averaged across all Pyr neurons after centring according to the neuron’s preferred stimulus. The bottom row is a slice through the difference (third row) of the average excitatory (first row) and inhibitory currents (second row). (d) Violin plot of the distribution of E/I synaptic current similarity values for all Pyr neurons in the network (see Materials and methods).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (a) Excitatory (red) and inhibitory (blue) synaptic currents onto a random selection of Pyr neurons, as a function of temporal and spatial stimulus frequency (averaged over all orientations), when both incoming and outgoing parvalbumin-expressing (PV) synapses are plastic. (b) The network-averaged excitatory (first row) and inhibitory (second row) synaptic currents onto Pyr neurons, both centred according to the peak excitatory current before averaging. After averaging, their difference is taken (third row) and a slice is plotted (bottom row). When both plasticities are present, currents are well balanced across stimuli with a modest excitatory bias for preferred stimuli. (c) Quality of excitatory-inhibitory (E-I) current co-tuning for every Pyr in the network quantified by the distribution of their cosine similarities. Only when both plasticities are present, do most Pyr neurons receive well co-tuned E-I synaptic currents.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** In a network with both local rules (left column), the update to Pyr → PV synapses rapidly aligns to the gradient (i.e. when the angle between the approximate update and the gradient is below $\pi/2$; bottom left). While updates to the Pyr → PV weights occasionally point away from the gradient, 79% of samples are below $\pi/2$. For the knock-out (KO) experiments (right column), output plasticity closely follows the PV → Pyr gradient even if input plasticity is absent (upper right). In contrast, if output (PV → Pyr) plasticity is absent, the approximate Pyr → PV rule does not follow the gradient (lower right).

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** (a) Plots of 2D histograms for PV → Pyr (top) and Pyr → PV (bottom) weight versus response similarity (RS), in different networks trained with the local plasticity rules (columns). White lines indicate the threshold of experimental detectability. Any weight < 10-4 is not included when computing Pearson’s correlation between RS and synaptic weight, or weight-weight correlations. (b) Same plots as (a), but for networks trained with the gradient rules.

### E/I assemblies are formed by homeostatic plasticity rules in input and output connections of PV interneurons

In feedforward networks, a stimulus-specific balance of excitation and inhibition can arise from homeostatic inhibitory synaptic plasticity that aims to minimise the deviation of a neuron’s firing rate from a target for all stimuli of a given set (Vogels et al., 2011; Clopath et al., 2016; Weber and Sprekeler, 2018). We wondered whether a stimulus-specific form of homeostasis can also generate stimulus-specific feedback inhibition by forming E/I assemblies. To that end, we derive synaptic plasticity rules for excitatory input and inhibitory output connections of PV interneurons that are homeostatic for the excitatory population (see 'Materials and methods'). A stimulus-specific homeostatic control can be seen as a ‘trivial’ supervised learning task, in which the objective is that all Pyr neurons should learn to fire at a given target rate $ρ_{0}$ for all stimuli. Hence, a gradient-based optimisation would effectively require a backpropagation of error (Rumelhart et al., 1985) through time (BPTT; Werbos, 1990).

Because backpropagation rules rely on non-local information that might not be available to the respective synapses, their biological plausibility is currently debated (Lillicrap et al., 2020; Sacramento et al., 2018; Guerguiev et al., 2017; Whittington and Bogacz, 2019; Bellec et al., 2020). However, a local approximation of the full BPTT update can be obtained under the following assumptions: First, we assume that the sensory input to the network changes on a time scale that is slower than the intrinsic time scales in the network. This eliminates the necessity of backpropagating information through time, albeit still through the synapses in the network. This assumption results in what we call the ‘gradient-based’ rules (Equation 15 in Appendix 1), which are spatially non-local. Second, we assume that synaptic interactions in the network are sufficiently weak that higher-order synaptic interactions can be neglected. Third and finally, we assume that over the course of learning, the Pyr → PV connections and the PV → Pyr connections become positively correlated (Znamenskiy et al., 2018), such that we can replace PV → Pyr synapses by the reciprocal Pyr → PV synapse in the Pyr → PV learning rule, without rotating the update too far from the true gradient (see Appendix 1).

The resulting learning rule for the output connections of the interneurons is similar to a previously suggested form of homeostatic inhibitory plasticity (Figure 1—figure supplement 1a, left) (Vogels et al., 2011). Specifically, PV output synapses $W^{E←I}$ undergo Hebbian changes in proportion to presynaptic interneuron activity $r_{j}^{I}$ and the signed deviation of total postsynaptic Pyr cell input $h_{i}^{E}$ from the homeostatic target:

$$
ΔW_{ij}^{E←I}∝r_{j}^{I}(h_{i}^{E}−ρ_{0})+weight decay.
$$

In contrast, the PV input synapses $W^{I←E}$ are changed such that the total excitatory drive $I_{i}^{E,rec}$ from the Pyr population to each interneuron is close to some target value I0 (Figure 1—figure supplement 1a, right):

$$
ΔW_{ij}^{I←E}∝r_{j}^{E}(I_{i}^{E,rec}−I_{0})+weight decay.
$$

Both synapse types are subject to a weak weight decay, to avoid the redundancy that a multiplicative rescaling of input synapses can be compensated by a rescaling of the output synapses.

While our main results are obtained using the local approximations, we also simulated the gradient-based rules to verify that the approximation does not qualitatively change the results (Figure 1—figure supplement 2).

When we endow the synapses of an initially randomly connected network of Pyr neurons and PV interneurons with plasticity in both the input and the output synapses of the interneurons, the network develops a synaptic weight structure and stimulus response that closely resemble that of mouse V1 (Znamenskiy et al., 2018). Before learning, interneurons show poor stimulus selectivity (Figure 1c), in line with the notion that in a random network, interneurons pool over many Pyr neurons with different stimulus tuning (Harris and Mrsic-Flogel, 2013). The network is then exposed to randomly interleaved stimuli. By the end of learning, interneurons have developed a pronounced stimulus tuning, albeit weaker than that of Pyr neurons (Figure 1c,d). Interneurons form strong bidirectional connections preferentially with Pyr neurons with a similar stimulus tuning, whereas connections between Pyr-PV pairs with dissimilar stimulus tuning are weaker (Figure 1d,e). To make our results comparable to Znamenskiy et al., 2018, we randomly sample an experimentally feasible number of synaptic connections from the network ($n=100$). Both the efficacy of PV input and output connections are highly correlated with the response similarity (RS) (see 'Materials and methods') of the associated Pyr neurons and interneurons (Figure 1e, left and centre). For bidirectionally connected cell pairs, the efficacies of the respective input and output connections are highly correlated (Figure 1e, right). The stimulus tuning of the inhibitory inputs onto the Pyr cells—initially flat—closely resembles that of the excitatory inputs after learning (Figure 1f, Figure 1—figure supplement 3; Tan et al., 2011), that is, the network develops a precise E/I balance (Hennequin et al., 2017).

Finally, the optimal gradient rules produce very similar results to the local approximations (Figure 1—figure supplement 2). Over the course of learning, the weight updates by the approximate rules align to the updates that would result from the gradient rules (Figure 1g, Figure 1—figure supplement 4), presumably by a mechanism akin to feedback alignment (Lillicrap et al., 2016; Akrout et al., 2019).

In summary, these results show that combined homeostatic plasticity in input and output synapses of interneurons can generate a similar synaptic structure as observed in mouse V1, including the formation of E/I assemblies.

### PV → Pyr plasticity is required for the formation of E/I assemblies

Having shown that homeostatic plasticity acting on both input and output synapses of interneurons are sufficient to learn E/I assemblies, we now turn to the question of whether both are necessary. To this end, we perform ‘knock-out’ experiments, in which we selectively block synaptic plasticity in either of the synapses. The motivation for these experiments is the observation that the incoming PV synapses follow a long-tailed distribution (Znamenskiy et al., 2018). This could provide a sufficient stimulus selectivity in the PV population for PV → Pyr plasticity alone to achieve a satisfactory E/I balance. A similar reasoning holds for static, but long-tailed outgoing PV synapses. This intuition is supported by results from Litwin-Kumar et al., 2017, where for a population of neurons analogous to our interneurons, the dimensionality of responses in that population can be high for static input synapses, when those are log-normally distributed.

When we knock out output plasticity but keep input plasticity intact, the network fails to develop E/I assemblies and a stimulus-specific E/I balance. While there is highly significant change in the distribution of PV interneuron stimulus selectivity (Mann-Whitney U test, $U=1207$, $p<10^{−4}$), the effect is much stronger when output plasticity is also present (Figure 2a,b). Importantly, excitatory and inhibitory currents in Pyr neurons are poorly co-tuned (Figure 2c, Figure 1—figure supplement 3b). In particular, feedback inhibition remains largely untuned because output connections are still random, so that Pyr neurons pool inhibition from many interneurons with different stimulus tuning.

![Figure 2.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig2-v1.jpg)

**Figure 2.:** (a) Example responses of reciprocally connected pyramidal (Pyr) cells and PV interneurons. Numbers correspond to points marked in (d). (b) Stimulus selectivity of Pyr cells and PV interneurons (before and after learning; Mann-Whitney U test, $p<10^{−4}$). Arrows indicate median. (c) Stimulus tuning of excitatory and inhibitory input currents in a Pyr cell before and after learning. For simplicity, currents are shown for spatial and temporal frequency only, averaged across all orientations. (d) Relationship of output (left) and input (centre) synaptic efficacies of PV interneurons with response similarity. Relationship of input and output efficacies (right). Plotted lines are obtained via linear regression. Reported r and associated p-value are the Pearson’s correlation. (e) Distribution of Pearson’s correlation coefficients for multiple samples as shown in (d). Dashed line marks threshold of high significance ($p<0.01$). (f) Fraction of samples with highly significant positive correlation before plasticity, after plasticity in both input and output connections, and for KO of plasticity in PV output connections (based on 10,000 random samples of 100 synaptic connections).

To investigate whether the model without output plasticity is consistent with the synaptic structure of mouse V1, we repeatedly sample an experimentally feasible number of synapses ($n=100$, Figure 2d) and plot the distribution of the three pairwise Pearson’s correlation coefficients between the two classes of synaptic weights and RS (Figure 2e). When both forms of plasticity are present in the network, a highly significant positive correlation ($p<0.01$) is detected in all samples for all three correlation types (Figure 2f). When output plasticity is knocked out, we still find a highly significant positive correlation between input weights and RS in 99% of the samples (Figure 2d–f). In contrast, correlations between input and output synapses are weaker and cannot reliably be detected (2% of samples). Notably, we find a correlation between output weights and RS in <0.01% of samples (Figure 2f). Finally, for an experimentally realistic sample size of $n=100$, the probability of a correlation coefficient equal or higher than that observed by Znamenskiy et al., 2018 is <0.01% for the correlation between output weights and RS ($r=0.55$), and <0.01% for the correlation between input and output synapses ($r=0.52$).

The non-local gradient rule for the PV input synapses alone also does not permit the formation of E/I assemblies (Figure 1—figure supplement 2). While the selectivity of interneurons increases more than for the local approximation (Figure 1—figure supplement 2b), feedback inhibition still remains untuned in the absence of output plasticity (Figure 1—figure supplement 2c,d).

We therefore conclude that input plasticity alone is insufficient to generate the synaptic microstructure observed in mouse V1.

### Pyr → PV plasticity is required for assembly formation

When we knock out input plasticity but keep output plasticity intact, we again observe no formation of E/I assemblies. This remains true even when using the gradient-based rule (Figure 1—figure supplement 2). The underlying reason is that input weights remain random. Interneurons collect excitation from many Pyr neurons with different preferences, and absent plasticity on their input synapses, they maintain their initial poor stimulus selectivity (Figure 3a–c). Because of the poor stimulus tuning of the interneurons, output plasticity cannot generate stimulus-specific inhibitory inputs to the Pyr neurons (Figure 3d). Instead, they essentially receive a tonic, unspecific background inhibition that is weakly modulated by the stimulus (Figure 1—figure supplement 3b). While this weak modulation is correlated with the excitatory inputs, the overall similarity between excitatory and inhibitory input remains low (Figure 1—figure supplement 3c).

![Figure 3.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig3-v1.jpg)

**Figure 3.:** (a) Example responses of reciprocally connected pyramidal (Pyr) cells and PV interneurons. (b) Stimulus selectivity of Pyr cells and PV interneurons (before and after learning). Arrows indicate median. (c) Violin plots of inhibitory stimulus selectivity before plasticity, after learning with plasticity in both input and output connections of PV interneurons and for knock-out (KO) of plasticity in PV input connections. (d) Stimulus tuning of excitatory and inhibitory currents in a Pyr cell before and after learning. Dimensions correspond to spatial and temporal frequency of the stimuli averaged across all orientations. (e) Fraction of samples with highly significant ($p<0.01$) positive correlation before plasticity, after plasticity in both input and output connections, and for KO of plasticity in PV input connections (based on 10,000 random samples of 100 synaptic connections).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Scatter plots containing every synapse in networks without PV → Pyr plasticity (top), or without Pyr → PV plasticity (bottom). Pearson’s correlation is always highly significant, though sometimes weak.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** To ensure that the results of Figure 3 were not simply a consequence of our chosen Pyr → PV weight distribution ($\sigma^{I←E}=0.65$), we repeat those simulations with weights drawn from a log-normal distribution with a longer tail ($\sigma^{I←E}=1.6$). (a) The default and longer-tailed distributions of Pyr → PV weights. (b) PV neurons exhibit greater stimulus selectivity than in Figure 3, when Pyr→ PV plasticity is knocked out. (c) Excitatory currents are more precisely balanced by inhibition (compare with Figure 3). (d) When repeatedly sampling 100 synapses, the strength of inhibitory synapses that connect Pyr and PV cell pairs are always significantly correlated ($p<0.01$) with response similarity (RS). Excitatory synapses between cell pairs are only correlated with RS in about half of the samples. For reciprocally connected cell pairs, the strength of excitatory weights is rarely correlated with the inhibitory weights. (e) Similar to Figure 3—figure supplement 1 (bottom), when all synapses for the Pyr → PV KO network are considered, Exc-RS and Exc-Inh correlations are weak but highly significant. Dashed lines indicate the threshold below which synapses are considered experimentally undetectable and discarded for the analysis in (d).

This modulation is made possible by the fact that interneurons still possess a weak, but consistent stimulus tuning arising from random variations in their input weights. A particularly strong input connection will cause the postsynaptic interneuron to prefer similar stimuli to the presynaptic Pyr. Because of the resulting correlated activity, the Hebbian nature of the output plasticity potentiates inhibitory weights for such cell pairs that are reciprocally connected. The tendency of strong input synapses to generate a strong corresponding output synapse is reflected in a positive correlation between output synapses and RS (Figure 3e, Figure 3—figure supplement 1), despite the fact that input synapses remain random.

This effect further increases when input synapses are drawn from a distribution with an even heavier tail, beyond what is observed in mouse V1 (Znamenskiy et al., 2018; Figure 3—figure supplement 2a). In this case, the stimulus tuning of the interneurons is dominated by a small number of very large synapses. The resulting higher selectivity of the interneurons (Figure 3—figure supplement 2b) allows a better co-tuning of excitation and inhibition in Pyr neurons (Figure 3—figure supplement 2c), in line with theoretical arguments for sparse connectivity (Litwin-Kumar et al., 2017). However, the dominance of a small number of large synapses also makes it unlikely that those synapses are observed in an experiment in which a finite number of synapses are sampled. As a result, a heavier tail does not yield the correlation of reciprocal input and output synapses observed by Znamenskiy et al., 2018 (Figure 3—figure supplement 2d,e), although it increases the probability of observing correlations between input synapses and RS when weak synapses are discarded. See Appendix 1 for a more extensive discussion.

Collectively, these results indicate that plasticity of both the inhibitory output and the excitatory input synapses of PV interneurons is required for the formation of E/I assemblies in cortical areas without feature topography, such as mouse V1.

### Single-neuron perturbations

Our findings demonstrate that in networks without feature topography, only a synergy of excitatory and inhibitory plasticity can account for the emergence of E/I assemblies. But how does stimulus-specific feedback inhibition affect interactions between excitatory neurons? In layer 2/3 of V1, similarly tuned excitatory neurons tend to have stronger and more frequent excitatory connections (Ko et al., 2011). It has been hypothesised that this tuned excitatory connectivity supports reliable stimulus responses by amplifying the activity of similarly tuned neurons (Cossell et al., 2015). However, the presence of co-tuned feedback inhibition could also induce the opposite effect, such that similarly tuned excitatory neurons are in competition with each other (Chettih and Harvey, 2019; Moreno-Bote and Drugowitsch, 2015).

To investigate the effect of stimulus-specific inhibition in our network, we simulate the perturbation experiment of Chettih and Harvey, 2019: First, we again expose the network to the stimulus set, with PV input and output plasticity in place to learn E/I assemblies. Second, both before and after learning, we probe the network with randomly selected stimuli from the same stimulus set, while perturbing a single Pyr cell with additional excitatory input, and measure the resulting change in activity of other Pyr neurons in the network (Figure 4a).

![Figure 4.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig4-v1.jpg)

**Figure 4.:** (a) Perturbation of a single pyramidal (Pyr) neuron. Responses of other Pyr neurons are recorded for different stimuli, both with and without perturbation. (b) Perturbation-induced change in activity ($Δ$ Act.) of a subset of Pyr cells, for a random subset of stimuli (with neuron 1 being perturbed). (c) Influence of perturbing a Pyr neuron on the other Pyr neurons, averaged across all stimuli, for a subset of Pyr neurons. (d) Dependence of influence among Pyr neurons on their receptive field correlation (Pearson’s r), across all neurons in the network (see 'Materials and methods'). Dotted lines indicate plasticity knock-out (KO) experiments; see Figure 4—figure supplement 1b for details. Error bars correspond to the standard error of the sample mean, but are not visible due to their small values. (e) Total strength of output synapses from a Pyr neuron predicts the average effect perturbing it has on other neurons. Dashed line is the result of a linear regression, while r and its associated p-value correspond to the Pearson’s correlation.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/59715/elife-59715-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (a) Receptive field correlations (Pearson’s) between Pyr neurons, before (top) and after (bottom) learning with both PV → Pyr and Pyr → PV synaptic plasticity. (b) The effect of perturbing a Pyr neuron on the response of other Pyr neurons (to random stimuli) as a function of their receptive field correlation (see 'Materials and methods'). On their own, both Pyr → PV and PV → Pyr plasticity have little effect on the feature amplification observed prior to learning. (c) Despite the absence of feature competition on average in the KO networks, the total strength of Pyr → PV synapses from a given Pyr neuron is still predictive of its influence on the rest of the network: The stronger its total weight, the more likely a Pyr is to suppressing the response of other Pyr neurons.

While the activity of the perturbed neuron increases, many of the other Pyr neurons are inhibited in response to the perturbation (Figure 4b). Although comparing the pairwise influence of Pyr neurons on each other does not reveal any apparent trend (Figure 4c), recent experiments report that the influence a single-cell perturbation has on other neurons depends on the similarity of their stimulus feature tuning (Chettih and Harvey, 2019). To test whether we observe the same feature-specific suppression, we compute the influence of perturbing a Pyr on the rest of the network as a function of the receptive field correlation of the perturbed cell and each measured cell. In line with recent perturbation studies (Chettih and Harvey, 2019; Sadeh and Clopath, 2020), we observe that—on average—neurons are more strongly inhibited if they have a similar tuning to the perturbed neuron (Figure 4d). The opposite holds before learning: the effect of single-neuron perturbations on the network is increasingly excitatory as receptive field correlation increases. Notably, the networks in which input or output plasticity was knocked out during learning (and therefore did not develop E/I assemblies) show the same excitatory effect (Figure 4d, Figure 4—figure supplement 1b). This confirms that a ‘blanket of inhibition’ does not account for feature-specific suppression between excitatory neurons (Sadeh and Clopath, 2020).

To better understand this behaviour, we use the Pyr-Pyr receptive field correlations to compute the coefficient of determination for all pairs ($R^{2}$, which quantifies how well the receptive field of one Pyr neuron predicts that of another). Learning changes the correlative structure in the network (Figure 4—figure supplement 1a) and thereby decreases the coefficient of determination on average, indicating a reduction in Pyr-Pyr correlations within the network ($E⁢[R^{2}]=0.06$ before learning, 0.02 after). Thus, plasticity suppresses some of the strongest correlations, resulting in ‘feature competition’ which is believed to aid sensory processing (Lochmann et al., 2012; Moreno-Bote and Drugowitsch, 2015).

While on average the network exhibits feature competition, the influence of individual Pyr neurons on the rest of the network is highly variable. According to recent modelling work (Sadeh and Clopath, 2020), the strength of Pyr → PV synapses strongly influences whether a network will exhibit feature competition. In our network, the total outgoing weight of a Pyr cell onto the PV neurons indeed predicts the average influence that neuron will have on the rest of the network when perturbed (Figure 4e; $r=-0.6$).

In summary, the stimulus-specific feedback inhibition that emerges in the model also captures the paradoxical suppression of similarly tuned excitatory neurons observed in single-cell perturbation experiments.

## Discussion

The idea that feedback inhibition serves as a ‘blanket of inhibition’ (Packer and Yuste, 2011; Fino and Yuste, 2011) that can be selectively broken (Karnani et al., 2016) has been gradually relaxed over recent years and replaced by the notion that feedback inhibition can be rather selective (Rupprecht and Friedrich, 2018) and could thereby support specific neuronal computations (Vogels and Abbott, 2009; Hennequin et al., 2014; Denève and Machens, 2016; Najafi et al., 2020), even in networks without topographic organisation (Znamenskiy et al., 2018; Rupprecht and Friedrich, 2018). Here, we used a computational model to show that the development of E/I assemblies similar to those observed in mouse V1 (Znamenskiy et al., 2018) or zebrafish olfactory areas (Rupprecht and Friedrich, 2018) can be driven by a homeostatic form of plasticity of the incoming and outgoing synapses of inhibitory interneurons. Based on the results of virtual knock-out experiments, we suggest that, on their own, input or output plasticity of interneurons are insufficient to explain the Pyr-PV microcircuitry in mouse V1 and that input and output plasticity in interneurons must act in synergy for stimulus-specific feedback inhibition to develop. To investigate how the presence of E/I assemblies affects interactions between excitatory neurons, we mimicked a perturbation experiment and found that—as in mouse visual cortex—stimulating single excitatory cells paradoxically suppresses similarly tuned neurons (Chettih and Harvey, 2019). Our findings suggest that, by driving the development of tuned feedback inhibition, plasticity of interneurons can fundamentally shape cortical processing.

The learning rules for the input and output synapses of PV interneurons are based on a single homeostatic objective that aims to keep the net synaptic current onto Pyr neurons close to a given target for all stimuli. The two forms of plasticity fulfil different purposes, however. Plasticity of input synapses is required for interneurons to acquire a stimulus selectivity, whereas plasticity of output synapses can exploit interneuron selectivity to shape inhibitory currents onto excitatory cells. The output plasticity we derived for our recurrent network is very similar to a previously suggested form of inhibitory plasticity (Vogels et al., 2011; Sprekeler, 2017). Homeostatic plasticity rules for inhibitory synapses are now used regularly in computational studies to stabilise model circuits (Vogels et al., 2011; Hennequin et al., 2017; Landau et al., 2016). In contrast, a theoretically grounded approach for the plasticity of excitatory input synapses onto inhibitory neurons is missing.

Homeostatic changes in excitatory synapses onto interneurons in response to lesions or sensory deprivation have been reported (Keck et al., 2011; Takesian et al., 2013; Kuhlman et al., 2013), but the specific mechanisms and functions of this form of interneuron plasticity are not resolved. The plasticity rule we derived for the input synapses of interneurons effectively changes the selectivity of those neurons according to the demands of the Pyr cells, that is, such that the interneurons can best counteract deviations of Pyr activity from the target. By which mechanisms such a (nearly teleological) form of plasticity can be achieved is at its core a problem of credit assignment, whose biological implementation remains open (Lillicrap et al., 2016; Guerguiev et al., 2017; Sacramento et al., 2018).

Here, we used a local approximation of the gradient, backpropagation rules, which produces qualitatively similar results, and which we interpret as a recurrent variant of feedback alignment, applied to the specific task of a stimulus-specific E/I balance (Lillicrap et al., 2016; Akrout et al., 2019). The excitatory input connections onto the interneurons serve as a proxy for the transpose of the output connections. The intuition why this replacement is reasonable is the following: The task of balancing excitation by feedback inhibition favours symmetric connections, because excitatory cells that strongly drive a particular PV interneuron should receive a strong feedback connection in return. Therefore, E/I balance favours a positive correlation between the incoming and outgoing synapses of PV neurons and thus the two weight matrices will be aligned in a final balanced state (Lillicrap et al., 2016; Akrout et al., 2019). This weight replacement effectively replaces the ‘true’ feedback errors by a deviation of the total excitatory input to the PV neurons from a target (Hertäg and Sprekeler, 2020). The rule therefore has the structure of a homeostatic rule for the recurrent excitatory drive received by PV neurons.

A cellular implementation of such a plasticity rule would require the following ingredients: (i) a signal that reflects the cell-wide excitatory current and (ii) a mechanism that changes Pyr → PV synapses in response to variations in this signal. For the detection of excitatory inputs, postsynaptic sodium or calcium concentrations are natural candidates. Due to the lack of spines in PV dendrites, both are expected to diffuse more broadly in the dendritic arbor than in spiny neurons (Hu et al., 2014; Kullmann and Lamsa, 2007) and may thus provide a signal for overall dendritic excitatory currents. Depending on how excitatory inputs are distributed on PV interneuron dendrites (Larkum and Nevian, 2008; Jia et al., 2010; Grienberger et al., 2015), the integration of the excitatory currents may not need to be cell-wide—which could limit the temporal resolution of the plasticity—but could be local, for example, to a dendrite, if local excitatory input is a sufficient proxy for the global input. Notably, in PV interneurons, NMDA receptors are enriched in excitatory feedback relative to feedforward connections (Le Roux et al., 2013), suggesting those two sources of excitation are differentially treated on the postsynaptic side. As for many other excitatory synapses (Sjöström et al., 2008), postsynaptic calcium is likely a key factor also for the plasticity of excitatory input synapses onto interneurons. Blocking NMDA receptors interferes with Hebbian long-term plasticity in some of these synapses (Lamsa et al., 2007; Kullmann and Lamsa, 2007), as does a block of excitatory input (Le Roux et al., 2013). Furthermore, NMDAR-dependent plasticity in Pyr → PV synapses is expressed postsynaptically and seems to require presynaptic activation (Kullmann and Lamsa, 2007). In summary, we believe that there are no conceptual issues that would rule out an implementation of the suggested plasticity rule for excitatory inputs onto PV interneurons.

We also expect that the rules we suggest here are only one set of many that can establish E/I assemblies. Given that the role of the input plasticity in the interneurons is the formation of a stimulus specificity, it is tempting to assume that this could equally well be achieved by classical forms of plasticity like the Bienenstock-Cooper-Munro (BCM) rule (Bienenstock et al., 1982), which is commonly used in models of receptive field formation. However, in our hands, the combination of BCM plasticity in Pyr → PV synapses with homeostatic inhibitory plasticity in the PV → Pyr synapses showed complex dynamics, an analysis of which is beyond the scope of this article. In particular, this combination of rules often did not converge to a steady state, probably for the following reason. BCM rules tend to make the postsynaptic neuron as stimulus-selective as possible. Given the limited number of interneurons in our circuit, this can lead to a situation in which parts of stimulus space are not represented by any interneurons. As a result, Pyr neurons that respond to those stimuli cannot recruit inhibition and maintain a high firing rate far above the target. Other Pyr cells, which have access to interneurons with a similar stimulus tuning, can recruit inhibition to gradually reduce their firing rates towards the target rate. Because the BCM rule is Hebbian, it tends to strengthen input synapses from Pyr neurons with high activity. This shifts the stimulus tuning of the interneurons to those stimuli that were previously underrepresented. However, this in turn renders a different set of stimuli uncovered by inhibition and withdraws feedback inhibition from the corresponding set of Pyr cells, which can now fire at high rates.

We suspect that this instability can also arise for other Hebbian forms of plasticity in interneuron input synapses when they are combined with homeostatic inhibitory plasticity (Vogels et al., 2011) in their output synapses. The underlying reason is that for convergence, the two forms of plasticity need to work synergistically towards the same goal, that is, the same steady state. For two arbitrary synaptic plasticity rules acting in different sets of synapses, it is likely that they aim for two different overall network configurations. Such competition can easily result in latching dynamics with a continuing turn-over of transiently stable states, in which the form of plasticity that acts more quickly gets to reach its goal transiently, only to be undermined by the other one later.

Both Pyr → PV and PV→ Pyr plasticity have been studied in slice (for reviews, see, e.g., Kullmann and Lamsa, 2007; Vogels et al., 2013), but mostly in isolation. The idea that the two forms of plasticity should act in synergy suggests that it may be interesting to study both forms in the same system, for example, in reciprocally connected Pyr-PV pairs.

Like all computational models, the present one contains simplifying design choices. First, we did not include stimulus-specific feedforward inhibition, because the focus lay on the formation of stimulus-specific feedback inhibition. The model could be enriched by feedforward inhibition in different ways. In particular, we expect that the two forms of plasticity will establish E/I assemblies even in the presence of stimulus-selective external inputs to the interneurons, because stimulus-specific external excitation should always be more supportive of the homeostatic objective than unspecific inputs. It may be worth exploring whether adding feedforward inhibition leaves more room for replacing the PV input plasticity that we used by classical Hebbian rules, because the activity of the external inputs remains unaltered by the plasticity in the network (such that the complex instability described above may be mitigated). Given that the focus of this work was on feedback inhibition, an extensive evaluation of the different variants of feedforward inhibition is beyond the scope of the present article.

Second, we neglected much of the complexity of cortical interneuron circuits by including only one class of interneurons. We interpret these interneurons as PV interneurons, given that PV interneurons provide local feedback inhibition (Hu et al., 2014) and show a stimulus-selective circuitry akin to E/I assemblies (Znamenskiy et al., 2018). With their peri-somatic targets on Pyr cells, PV-expressing (basket) cells are also a prime candidate for the classical feedback model of E/I balance (van Vreeswijk and Sompolinsky, 1996). Note that our results do not hinge on any assumptions that are specific to PV neurons and may thus also hold for other interneuron classes that provide feedback inhibition (Tremblay et al., 2016). Given that the division of labour of the various cortical interneuron classes is far from understood, an extension to complex interneuron circuits (Litwin-Kumar et al., 2016; Hertäg and Sprekeler, 2019) is clearly beyond the present study.

Similarly tuned Pyr cells tend to be recurrently connected (Cossell et al., 2015; Harris and Mrsic-Flogel, 2013), in line with the notion that excitatory cells with similar tuning mutually excite each other. This notion is questioned by a recent perturbation experiment demonstrating feature-specific suppression between Pyr cells with similar tuning (Chettih and Harvey, 2019). It has been suggested that this apparently paradoxical effect requires strong and tuned connections between excitatory and inhibitory neurons (Sadeh and Clopath, 2020). The E/I assemblies that develop in our model provide sufficiently strong and specific inhibitory feedback to cause a suppression between similarly tuned Pyr neurons in response to perturbations. Hence, despite the presence of stimulus-specific excitatory recurrence, Pyr neurons with similar stimulus preference effectively compete. Computational arguments suggest that this feature competition may be beneficial for stimulus processing, for example, by generating a sparser and more efficient representation of the stimuli (Olshausen and Field, 2004; Denève and Machens, 2016).

In addition to predicting that knocking out plasticity of inhibitory input or output synapses should prevent the development of E/I assemblies, our model also predicts different outcomes for single-neuron perturbation experiments in juvenile and adult mice. Given that in rodents, stimulus tuning of inhibitory currents occurs later in development than that of excitation (Dorrn et al., 2010), we expect that in juvenile mice single-cell perturbations would not cause feature-specific suppression but amplification due to excitatory recurrence and unspecific feedback inhibition.

## Materials and methods

### Network and stimuli

We use custom software to simulate a rate-based recurrent network model containing $N^{E}=512$ excitatory and $N^{I}=64$ inhibitory neurons. The activation of the neurons follows Wilson-Cowan dynamics:

$$
(1a)\tau_{E}\frac{d}{dt}h^{E}=−h^{E}+W^{E←E}r^{E}−W^{E←I}r^{I}+I^{bg}+I(s)(1b)\tau_{I}\frac{d}{dt}h^{I}=−h^{I}+W^{I←E}r^{E}−W^{I←I}r^{I}+I^{bg}.
$$

Here, $r^{E}=[h^{E}]_{+}$, $r^{I}=[h^{I}]_{+}$ denote the firing rates of the excitatory and inhibitory neurons, which are given by their rectified activation. $W^{Y←X}$ denotes the matrix of synaptic efficacies from population $X$ to population $Y$ ($X,Y\in{E,I}$). The external inputs $𝐈⁢(𝐬)$ to the excitatory neurons have a bell-shaped tuning in the three-dimensional stimulus space consisting of spatial frequency, temporal frequency, and orientation (Znamenskiy et al., 2018). To avoid edge effects, the stimulus space is periodic in all three dimensions, with stimuli ranging from -$\pi$ to $\pi$. The stimulus tuning of the external inputs is modelled by a von Mises function with a maximum of 50 Hz and a tuning width $κ=1$. The preferred stimuli of the $N^{E}=512$ excitatory cells cover the stimulus space evenly on a $12\times12\times12$ grid. All neurons receive a constant background input of $I^{bg}=5$ Hz.

Recurrent connections $W^{E←E}$ among excitatory neurons have synaptic weight between neurons i and j that grows linearly with the signal correlation of their external inputs:

$$
W_{i⁢j}^{E←E}=[c⁢o⁢r⁢r⁢(I_{i}⁢(𝐬),I_{j}⁢(𝐬))-C]_{+}.
$$

The cropping threshold C is chosen such that the overall connection among the excitatory neurons probability is 0.6. The remaining synaptic connections (E→I, I→E, I→I) are initially random, with a connection probability $p=0.6$ and log-normal weights. For parameters, please refer to Table 1.

**Table 1.**
 Model parameters.


<table>
  <thead>
    <tr>
      <th>NE</th>
      <th>512</th>
      <th>NI</th>
      <th>64</th>
      <th>Number of exc. and inh. neurons.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>τE</td>
      <td>50 ms</td>
      <td>τI</td>
      <td>25 ms</td>
      <td>Rate dynamics time constants</td>
    </tr>
    <tr>
      <td>d⁢t</td>
      <td>1 ms</td>
      <td></td>
      <td></td>
      <td>Numerical integration time step</td>
    </tr>
    <tr>
      <td>pE←X</td>
      <td>0.6</td>
      <td>pI←X</td>
      <td>0.6</td>
      <td>Connection probability to exc. and inh. neurons</td>
    </tr>
    <tr>
      <td>JiE←E</td>
      <td>2</td>
      <td>JiI←E</td>
      <td>5</td>
      <td>Total of exc. weights onto neuron i: ∑jWi⁢jX←E</td>
    </tr>
    <tr>
      <td>JiE←I</td>
      <td>1</td>
      <td>JiI←I</td>
      <td>1</td>
      <td>Total of inh. weights onto neuron i: ∑jWi⁢jX←I</td>
    </tr>
    <tr>
      <td>σE←X</td>
      <td>0.65</td>
      <td>σI←X</td>
      <td>0.65</td>
      <td>Std. deviation of the logarithm of the weights</td>
    </tr>
    <tr>
      <td>θE←I</td>
      <td>10-4</td>
      <td>θI←E</td>
      <td>10-4</td>
      <td>Experimental detection threshold for synapses</td>
    </tr>
    <tr>
      <td>Ibg</td>
      <td>5 Hz</td>
      <td>max⁡(𝐈⁢(𝐬))</td>
      <td>50 Hz</td>
      <td>Background and maximum stimulus-specific input</td>
    </tr>
    <tr>
      <td>NS</td>
      <td>12×12×12</td>
      <td>Ntrials</td>
      <td>500</td>
      <td>Number of stimuli and trials</td>
    </tr>
    <tr>
      <td>RS</td>
      <td>2⁢π×2⁢π×2⁢π</td>
      <td>κ</td>
      <td>1</td>
      <td>Range of stimuli and Pyr RF von Mises width</td>
    </tr>
    <tr>
      <td>Δ⁢I</td>
      <td>10 Hz</td>
      <td></td>
      <td></td>
      <td>Change of input for perturbation experiments</td>
    </tr>
    <tr>
      <td>ηApprox.</td>
      <td>10-5</td>
      <td>ηGrad.</td>
      <td>10-3</td>
      <td>Learning rates (approximate and gradient rules)</td>
    </tr>
    <tr>
      <td>δE←I</td>
      <td>0.1</td>
      <td>δI←E</td>
      <td>0.1</td>
      <td>Weight decay rates</td>
    </tr>
    <tr>
      <td>ρ0</td>
      <td>1 Hz</td>
      <td></td>
      <td></td>
      <td>Homeostatic plasticity target</td>
    </tr>
    <tr>
      <td>β1</td>
      <td>0.9</td>
      <td>β2</td>
      <td>0.999</td>
      <td>Adam parameters for gradient rules</td>
    </tr>
    <tr>
      <td>ϵ</td>
      <td>10-9</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

During learning, we repeatedly draw all 12 × 12 × 12 preferred stimuli of the Pyr neurons, in random order. This procedure is repeated 500 times to ensure convergence of synaptic weights. To reduce simulation time, we present each stimulus long enough for all firing rates to reach steady state and only then update the synaptic weights.

### Synaptic plasticity

The PV → Pyr and Pyr → PV synapses follow plasticity rules that aim to minimise the deviation of the excitatory activations from a target rate $ρ_{0}$ ($ρ_{0}=1$ Hz):

$$
ℰ(h^{E})=⟨\frac{1}{2}\sumj=1N^{E}(h_{j}^{E}−ρ_{0})^{2}⟩_{s},
$$

where $⟨⋅⟩_{𝐬}$ denotes the average over all stimuli. When plastic, synaptic weights change according to

$$
(4a)ΔW_{ji}^{E←I}∝(h_{j}^{E}−ρ_{0})r_{i}^{I},(4b)ΔW_{ij}^{I←E}∝[\sumk=1N^{E}W_{ik}^{I←E}(h_{k}^{E}−ρ_{0})]r_{j}^{E}≈[\sumk=1N^{E}W_{ik}^{I←E}(r_{k}^{E}−ρ_{0})]r_{j}^{E}(4c)=(I_{i}^{E,rec}−I_{0})r_{j}^{E}.
$$

After every update of the Pyr → PV matrix, the incoming weights for each PV interneuron are multiplicatively scaled such that their sum is $J^{I←E}$ (Akrout et al., 2019). In that case, the rule in Equation 4b is approximately local in that it compares the excitatory input current $I_{i}^{E,rec}$ received by the postsynaptic PV neuron to a target value $I_{0}=J^{I←E}⁢ρ_{0}$, and adjusts the incoming synapses in proportion to this error and to presynaptic activity (see Equation 4c).

Both plasticity rules are approximations of the gradient of the objective function Equation 3. Interested readers are referred to Appendix 1 for their mathematical derivation. For the results in Figure 1—figure supplement 2, we use the Adaptive Moment Estimation (Adam) algorithm (Kingma and Ba, 2014) to improve optimisation performance.

We used a standard reparameterisation method to ensure the sign constraints of an E/I network. Moreover, all weights are subject to a small weight-dependent decay term, which aids to keep the firing rates of the interneurons in a reasonable range. For details, please refer to Appendix 1 . The learning rule Equation 4a for the output synapses of the inhibitory neurons is similar to the rule proposed by Vogels et al., 2011, wherein each inhibitory synapse increases in strength if the deviation of the postsynaptic excitatory cell from the homeostatic target $ρ_{0}$ is positive (and decreases it when negative). In contrast, the learning rule Equation 4b increases activated input synapses for an interneuron if the weighted sum of deviations in its presynaptic excitatory population is positive (and decreases them if it is negative). Though it is local, when operating in conjunction with the plasticity of Equation 4a, this leads to feedback alignment in our simulations and effectively performs backpropagation without the need for weight transport (Akrout et al., 2019).

Note that the objective function Equation 3 can also be interpreted differently. The activation $h^{E}$ of a neuron is essentially the difference between its excitatory and inhibitory inputs. Therefore, the objective function Equation 3 is effectively the mean squared error between excitation and inhibition, aside from a small constant offset $ρ_{0}$. The derived learning rules can therefore be seen as supervised learning of the inhibitory inputs, with excitation as the label. They hence aim to establish the best co-tuning of excitation and inhibition that is possible given the circuitry.

### Perturbation experiments

The perturbation experiments in Figure 4 are performed in a network in which both forms of plasticity have converged. The network is then exposed to different stimuli, while the afferent drive to a single excitatory cell i is transiently increased by $Δ⁢I=10$ Hz. For each stimulus, we compute the steady-state firing rates rj of all excitatory cells both with and without the perturbation. The influence of the perturbation of neuron i on neuron j is defined as the difference between these two firing rates, normalised by the pertubation magnitude (Sadeh and Clopath, 2020). This stimulation protocol is repeated for 90 randomly selected excitatory neurons. The dependence of the influence on the tuning similarity (Figure 4d) is obtained by binning the influence of the perturbed neuron i and the influenced neuron j according to their stimulus response correlation, and then averaging across all influences in the bin. During the perturbation experiments, synaptic plasticity was disabled.

### Quantitative measures

The response similarity (RS) of the stimulus tuning of two neurons i and j is measured by the dot product of their steady-state firing rates in response to all stimuli, normalised by the product of their norms (Znamenskiy et al., 2018):

$$
RS⁢(r_{i},r_{j})=\frac{\sum_{𝐬}r_{i}⁢(𝐬)⁢r_{j}⁢(𝐬)}{(\sum_{𝐬}(r_{i}⁢(𝐬))^{2}⁢\sum_{𝐬}(r_{j}⁢(𝐬))^{2})^{1/2}}.
$$

The same measure is used for the similarity of synaptic currents onto excitatory neurons in Figure 1—figure supplement 3c and Figure 1—figure supplement 2d.

There is no structural plasticity, that is, synapses are never added or pruned. However, when calculating Pearson’s correlation between synaptic weights and RS, we exclude synapses that are too weak to be detected using the experimental protocol employed by Znamenskiy et al., 2018. The threshold values $\theta^{E←I}$ and $\theta^{I←E}$ were chosen to be approximately four orders of magnitude weaker than the strongest synapses in the network. The rules that we investigate here tend to produce bimodal distributions of weights, with the lower mode well below this threshold (Figure 1—figure supplement 5).

The stimulus selectivity of the neurons is measured by the skewness of their response distribution across all stimuli:

$$
\gamma_{i}=\frac{⟨(r_{i}⁢(𝐬)-r¯_{i})^{3}⟩_{𝐬}}{⟨(r_{i}⁢(𝐬)-r¯_{i})^{2}⟩_{𝐬}^{3/2}}
$$

where $r¯_{i}=⟨r_{i}⁢(𝐬)⟩_{𝐬}$. Both the RS Equation 5 and the stimulus selectivity Equation 6 are adapted from Znamenskiy et al., 2018.

Finally, the angle $\theta$ between the gradient G from Equation 15 and its approximation A from Equation 4 is given by

$$
\theta=arccos⁡(\frac{\sum_{i⁢j}G_{i⁢j}⁢A_{i⁢j}}{(\sum_{i⁢j}G_{i⁢j}^{2}⁢\sum_{i⁢j}A_{i⁢j}^{2})^{1/2}})
$$
