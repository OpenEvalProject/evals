# Modeling apical and basal tree contribution to orientation selectivity in a mouse primary visual cortex layer 2/3 pyramidal cell

## Authors

- Konstantinos-Evangelos Petousakis<sup>1</sup> ([ORCID: 0000-0003-2022-1671](https://orcid.org/0000-0003-2022-1671))
- Jiyoung Park<sup>3</sup>
- Athanasia Papoutsi<sup>2</sup> ([ORCID: 0000-0003-2466-7259](https://orcid.org/0000-0003-2466-7259))
- Stelios Smirnakis<sup>3</sup> ([ORCID: 0000-0002-1929-2811](https://orcid.org/0000-0002-1929-2811)) †
- Panayiota Poirazi<sup>2</sup> ([ORCID: 0000-0001-6152-595X](https://orcid.org/0000-0001-6152-595X)) †

### Affiliations

1. Department of Biology, University of Crete Heraklion Greece ([ROR:00dr28g20](https://ror.org/00dr28g20))
2. IMBB, FORTH Heraklion Greece ([ROR:052rphn09](https://ror.org/052rphn09))
3. Department of Neurology, Brigham and Women’s Hospital and Jamaica Plain Veterans Administration Hospital, Harvard Medical School Boston United States ([ROR:04b6nzv94](https://ror.org/04b6nzv94))

† Corresponding author

## Abstract

Pyramidal neurons, a mainstay of cortical regions, receive a plethora of inputs from various areas onto their morphologically distinct apical and basal trees. Both trees differentially contribute to the somatic response, defining distinct anatomical and possibly functional sub-units. To elucidate the contribution of each tree to the encoding of visual stimuli at the somatic level, we modeled the response pattern of a mouse L2/3 V1 pyramidal neuron to orientation tuned synaptic input. Towards this goal, we used a morphologically detailed computational model of a single cell that replicates electrophysiological and two-photon imaging data. Our simulations predict a synergistic effect of apical and basal trees on somatic action potential generation: basal tree activity, in the form of either depolarization or dendritic spiking, is necessary for producing somatic activity, despite the fact that most somatic spikes are heavily driven by apical dendritic spikes. This model provides evidence for synergistic computations taking place in the basal and apical trees of the L2/3 V1 neuron along with mechanistic explanations for tree-specific contributions and emphasizes the potential role of predictive and attentional feedback input in these cells.

## Introduction

In the primary visual cortex (V1), layer 2 and 3 (L2/3) pyramidal neurons conform to a stereotypical morphology characterized by separate apical and basal dendritic arbors. The apical tree consists of a thick apical trunk that extends into L1 and splits into an apical tuft. The basal tree consists of numerous dendritic segments, the majority of which sprout directly from the base of the soma, indicating that they can directly influence somatic output (Spruston, 2008). This compartmentalization of V1 neurons is also evident in the wiring diagram describing each tree: layer 4 (L4) and L2/3 pyramidal neurons synapse with basal dendrites of L2/3 pyramidal neurons, providing them with feedforward input (Coogan and Burkhalter, 1990; Larkum, 2013). The apical dendrites of the L2/3 pyramidal neurons instead receive feedback input from higher order areas of the cortex such as the secondary and tertiary visual cortices, lateromedial area and prefrontal cortex (Coogan and Burkhalter, 1990; Larkum, 2013), as well as orientation-tuned thalamocortical input (Chen et al., 2013; Cruz-Martín et al., 2014; Jia et al., 2010; Roth et al., 2016). These anatomical and connectivity features of the apical and basal trees, complemented by their distinct biophysical properties (Cho et al., 2008), shape both the local dendritic processing and the integration of the two input streams at the soma.

Few studies have undertaken the technically difficult task of measuring single spine tuning properties in the mouse visual cortex (Chen et al., 2013; Iacaruso et al., 2017; Jia et al., 2010). These studies have shown that single spines of L2/3 pyramidal neurons exhibit orientation selectivity, with synaptic orientation preferences varying even on the same branch (Iacaruso et al., 2017; Jia et al., 2010). These findings raise the question of how dendritic integration of sparse synaptic inputs along the apical and basal trees shape orientation tuning in L2/3 V1 pyramidal neurons.

The effect of synaptic input on neuronal output depends on the biophysical properties of dendritic branches. Older modeling work has established that blockage of dendritic sodium and NMDA activity leads to impaired or abolished orientation selectivity at the level of the soma (Archie and Mel, 2000; Mel et al., 1998). It is also known that individual dendritic segments of L2/3 neurons generate nonlinear regenerative responses, termed dendritic spikes, independently of the soma, making their exact contribution to somatic output unclear (Palmer et al., 2014; Smith et al., 2013). This could indicate that multiple dendritic segments need to be activated in order to generate a spike at the soma. On the other hand, it was recently proposed that strong, sparse inputs to the dendrites are sufficient to drive somatic output (Goetz et al., 2021). Interestingly, although dendritic spikes in the apical tuft of L2/3 V1 pyramidal neurons influence orientation selectivity (Goetz et al., 2021; Smith et al., 2013), this orientation selectivity is robust to ablation of the apical tree (Park et al., 2019). Altogether, the above studies highlight the need to scrutinize the functional effect that synaptic inputs along the basal and apical dendritic arbors have on the soma, building towards a realistic theory of visual processing.

In this work, we used a detailed biophysical model of a L2/3 V1 pyramidal cell (Park et al., 2019), to tease apart the relative contributions of apical vs. basal dendritic trees in somatic orientation tuning. We start by examining the threshold and strength of dendritic non-linearities, which are found to vary along the apical and basal dendrites. By comparing model output to in vivo two-photon calcium fluorescence imaging data, we find that dendritic and somatic spontaneous activity patterns in the model adequately reproduce experimental data. We then simulate orientation tuning in our model and evaluate its responses to specific combinations of dendritic disparity and synaptic distributions. We find that the tuned output of the model does not always match the linear summation of tuned input, instead deviating towards orientation preferences more closely matching either the apical or basal mean orientation preference.

We continue by evaluating the dependence of somatic spikes on dendritic voltage-gated sodium channel conductances by performing just-in-time interventions that nullify sodium conductance on either the apical or basal tree prior to a somatic spike. We find that the majority of stimulus-driven somatic spiking activity is dependent on sodium spikes generated in the apical tree, suggesting that apical and basal trees contribute via different mechanisms to tuned somatic output. We investigate this further by examining the role of both specific ionic (sodium channels) and synaptic (AMPA/NMDA) mechanisms in shaping orientation tuning. Results indicate that apical sodium channels are critical for proper neuronal tuning, while basal sodium channels do not play as significant a role. Conversely, AMPA and NMDA activity of both the apical and basal trees is required for orientation tuning at the level of the soma. A potential reason for this is that basal dendritic branches feature higher sodium spiking thresholds for similar electrotonic constant-normalized length values (i.e. ‘electrotonic length’) compared to apical branches, reducing their propensity to generate sodium spikes compared to apical dendrites.

Overall, our simulations suggest a synergistic effect between apical and basal trees, as somatic spikes are only reliably produced when apical dendritic sodium spikes coincide with basal synaptically driven depolarizations and/or spikes. In this manner, apical and basal dendrites contribute to neuronal function using different mechanisms, ionic or synaptic, which together drive action potential generation in this neuronal type.

## Methods

### Model description

The single neuron model is based on the L2/3 V1 pyramidal cell model of Park et al., 2019 created in the NEURON simulation environment (Hines and Carnevale, 2001). As the model makes use of a variety of passive and active mechanisms ( Tables 1–4), its electrophysiological properties were validated against experimental data (Park et al., 2019). Neither the morphology nor the biophysical properties of the source model were altered, barring specific ion channel or synaptic mechanism conductance changes wherever specified (see Extended methods for details). Apical stimulus-driven synaptic inputs have had a 10ms delay added, to better reflect experimental data on feedback synaptic inputs (Ju et al., 2020). Simulations with synchronous activation of the apical and basal synaptic inputs resulted in qualitatively similar results (data not shown). For a more detailed description of the model, see Park et al., 2019 and Extended methods, Model description.

**Table 1.**
 Outline of passive, active, and synaptic mechanisms present in the model neuron.


<table>
  <thead>
    <tr>
      <th>Compartment type</th>
      <th>Passive/active mechanisms</th>
      <th>Synaptic mechanisms</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Soma</td>
      <td rowspan="3">Hodgkin/Huxley voltage-gated Na+ channelsHodgkin/Huxley voltage-gated K+ channelsMuscarinic voltage-gated K+ channelsA-Type voltage-gated K+ channelsT-Type Ca++ channelsHigh voltage activated (HVA) Ca++ channelsCalcium-dependent K+ channelsActive ATP Ca++ pumps</td>
      <td>GABAA (background-driven)</td>
    </tr>
    <tr>
      <td>Basal dendrites</td>
      <td rowspan="2">AMPA (background-driven)NMDA (background-driven)GABAA (background-driven)AMPA (stimulus-driven)NMDA (stimulus-driven)GABAA (stimulus-driven)</td>
    </tr>
    <tr>
      <td>Apical dendrites</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Outline of membrane mechanism conductances (not synaptic).Reproduced from Park et al., 2019.


<table>
  <thead>
    <tr>
      <th>Conductance (mS/cm2)</th>
      <th>Soma</th>
      <th>Apical</th>
      <th>Basal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>gNa</td>
      <td>0.505</td>
      <td>0.303</td>
      <td>0.303</td>
    </tr>
    <tr>
      <td>gKdr</td>
      <td>0.05</td>
      <td>1.5*10–3</td>
      <td>1.5*10–3</td>
    </tr>
    <tr>
      <td>gKm</td>
      <td>2.8*10–3</td>
      <td>1.27*10–3</td>
      <td>1.27*10–3</td>
    </tr>
    <tr>
      <td>gA</td>
      <td>5.4</td>
      <td>Diameter ≤0.8 μm: 108Diameter &gt;0.8 μm: 10.8</td>
      <td>Diameter ≤0.8 μm: 108Diameter &gt;0.8 μm: 10.8</td>
    </tr>
    <tr>
      <td>gT</td>
      <td>0.03</td>
      <td>x≤260 μm: 0.029*sin(0.009*x+0.88)x&gt;260 μm: 0.012</td>
      <td>0.03+6*10–5*x</td>
    </tr>
    <tr>
      <td>gHVA</td>
      <td>0.05*10–3</td>
      <td>x≤260 μm:0.049*10–3*sin(0.009*x+0.88)x&gt;260 μm: 0.02*10–3</td>
      <td>0.05*10–3+10–7*x</td>
    </tr>
    <tr>
      <td>gKCa</td>
      <td>2.1*10–3</td>
      <td>2.1*10–3</td>
      <td>2.1*10–3</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Outline of model electrophysiological properties.RMP: resting membrane potential, IR: Input Resistance measured at hyperpolarizing current (–0.04 nA), AP: action potential, AHP: after hyperpolarization measured at depolarizing current (0.16 nA), P-T peak-trough. Reproduced from Park et al., 2019.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Model</th>
      <th>Cho et al., 2010</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RMP, mV</td>
      <td>–79</td>
      <td>–78.56 ± 1.34</td>
    </tr>
    <tr>
      <td>IR, MΩ</td>
      <td>123.6</td>
      <td>125.2 ± 8.2</td>
    </tr>
    <tr>
      <td>τ, ms</td>
      <td>17.3</td>
      <td>16 ± 0.7</td>
    </tr>
    <tr>
      <td>AP amplitude, mV</td>
      <td>66.1</td>
      <td>67.8 ± 1.8</td>
    </tr>
    <tr>
      <td>AP threshold, mV</td>
      <td>–41.8</td>
      <td>–37.7 ± 1.3</td>
    </tr>
    <tr>
      <td>AHP, mV</td>
      <td>17.9</td>
      <td>13.3 ± 0.5</td>
    </tr>
    <tr>
      <td>P-T time, ms</td>
      <td>38.6</td>
      <td>55.3 ± 2.7</td>
    </tr>
    <tr>
      <td>AP adaptation</td>
      <td>1.16</td>
      <td>1.18 ± 0.02</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Outline of synaptic mechanism conductances and time constants.Reproduced from Park et al., 2019.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Conductance (nS)</th>
      <th>τ1, ms</th>
      <th>τ2, ms</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NMDA</td>
      <td>1.15</td>
      <td>2</td>
      <td>30</td>
    </tr>
    <tr>
      <td>AMPA</td>
      <td>0.84</td>
      <td>0.1</td>
      <td>2.5</td>
    </tr>
    <tr>
      <td>GABAA</td>
      <td>1.25</td>
      <td>0.2</td>
      <td>1.4</td>
    </tr>
  </tbody>
</table>

### Simulation information

All simulations were performed on our High-Performance Computing Cluster (Rocks 7.0) with 624 cores and 3.328 TB of shared RAM under CentOS 7.4 OS (Papadopoulos et al., 2003), through the NEURON simulation environment (Hines and Carnevale, 2001). Model neuron output measurements were obtained at a sampling rate of 10 KHz (dt = 0.1ms). Unless specified otherwise, voltage recordings from any section of the model (soma / dendrites) were performed at the midpoint of the respective section. Simulation duration was 2500 ms, with stimulus onset (where present) at t = 500 ms. For information on manipulations of biophysical properties for specific experiments, see Extended methods, Biophysical manipulations. For details on specific simulation protocols, see Extended methods, Simulation protocols.

### Two-photon imaging

All experimental protocols were approved by Brigham and Women’s Hospital (BWH) Institution Animal Care and Use Committee. Male and female wild-type (C57BL/6) mice were purchased from The Jackson Laboratory and bred for experiments. A total of 2 mice were used in these experiments, with recordings from 11 neurons used for data analysis. For details on chronic window implantation, sparse labeling and in vivo imaging methodology, see Extended methods, Two-photon microscopy.

### Data analysis

Data analysis of both modeling and two-photon imaging experiments was performed through Python 3.8+, using publicly available libraries as well as custom code. Analysis procedures include methods for dendritic spike detection, quantification of dendritic non-linearities, calculation of dendritic electrotonic length, analysis of two-photon imaging recordings, processing of calcium fluorescence traces, detection of calcium events, conversion of voltage traces into approximate calcium fluorescence traces, and comparison of in vivo fluorescence data with converted model voltage traces. For specifics, see Extended methods, Data analysis.

## Results

### The degree of non-linearity varies across basal and apical model dendrites

To ensure the validity of our modeling approach, we first examined dendritic integration by characterizing the sodium spike properties of all dendritic segments (Figure 1A), wherein a specific number of synapses is synchronously activated by two pulses at 50 Hz while all other compartments are modeled as passive (‘I3P’; see Extended methods, Iterative paired-pulse protocol (I3P)), and the response of each dendritic segment is assessed. Results show that the model can produce realistic dendritic spikes (Figure 1—figure supplement 1C, D), while the properties of the spiking events vary between dendritic segments (Figure 1B–D, Figure 1—figure supplement 1A, B). Both apical and basal dendritic segments exhibit a large degree of variation in their spiking thresholds (Figure 1E, F; threshold synapse count mean and standard deviations: basal 12.286±6.649 sodium, 51.429 ± 13.179 NMDA; apical 14.442 ± 13.825 sodium, 40.721 ± 23.675 NMDA). Dendritic segments with high sodium spiking thresholds also tended to exhibit higher NMDA spiking thresholds. To quantitatively characterize the nonlinear behavior of each dendritic segment we used the Nonlinearity Relative to Linear Extrapolation (NRLE) metric (Behabadi et al., 2012), which is an estimate of the degree of non-linear dendritic integration within a specific branch (see Extended methods, Quantification of dendritic nonlinearities). Results indicate that all dendritic segments of the model neuron exhibit non-linear input-output functions (Figure 1D, NRLE = 1 denotes linear, NRLE <1 sublinear, and NRLE >1 supralinear), in line with experimental observations (Smith et al., 2013; Wilson et al., 2016). In addition, the NRLE values are relatively widely dispersed (values ranging from >1 to~3.5), providing a large dynamic range of possible dendrite-level computations. The above results show that there is diversity in apical and basal dendritic integration that can be exploited to modulate orientation tuning. The above differences are, at least in part, due to the morphological and electrophysiological features of dendritic segments, as we found that the sodium spiking propensity varies as a function of dendritic segment volume and electrotonic length (see Figure 5).

![Figure 1.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig1-v2.jpg)

**Figure 1.:** (A) Graphical representation of the iterative paired-pulse protocol. Green dots represent allocated synapses. Synapses were activated only within the designated (red) dendritic segment, with all other segments being passive. We record the voltage response of the dendritic segment with NMDA channels disabled or enabled, acquiring information on dendritic sodium and NMDA spikes, respectively. (B) Example of an ‘expected vs. actual plot’, showing the response produced by a single basal dendritic segment (solid black line) as a result of voltage-gated sodium channel activity elicited through simultaneous activation of 1–200 AMPA synapses. The dashed black line indicates the expected dendritic response assuming a linear dendrite. (C) Same as B, but for an apical dendritic segment. (D) NRLE value histogram for all apical (red) and basal (black) dendritic segments. (E) Bar plot of per-dendrite nonlinearity thresholds for all basal dendritic segments, sorted by the sodium spike thresholds. Note that NMDA spike thresholds largely follow the sodium spike threshold increase. (F) As E, for all apical dendritic segments.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Expected vs Actual plot for all basal dendrites undergoing the I3P protocol for 1–200 synapses. Blue line represents the dendrite in Figure 1B (basal dendrite #0). (B) Same as A, but for all apical dendrites. Blue line represents dendrite in Figure 1C (apical dendrite #0). (C) Example traces from the I3P protocol for NMDA spike generation from basal dendrite #0. Traces are 10 synapses apart from each other. (D) Same as C, but for apical dendrite #42 (oblique branch). Dendrites in C and D chosen to show examples of NMDA spiking.

### Model neuron features robust orientation tuning

Given the diverse integration properties of basal and apical dendrites in our model cell, we sought to assess their functional cooperation when receiving a more realistic set of background- and stimulus-driven inputs. Stimulus driven synapses were modeled with individual orientation preferences (Jia et al., 2010; Park et al., 2019), leading them to exhibit different firing rates depending on the orientation of the presented stimulus (for details, see Extended methods, Model description). As dictated by experimental data (Chen et al., 2013), background-driven synapses comprise the majority of inputs to the model, although they are activated at lower rates than stimulus-driven synapses (see Extended methods, Model description). To validate their impact on somatic output, we compared the simulated spontaneous activity with in vivo calcium two-photon fluorescence imaging data (see Extended methods, Analysis and comparison of true vs “generated” fluorescence data and Figure 2—figure supplements 1–4). Although this approach has its limits, it allows us to use two-photon imaging data to increase model reliability. We found that spontaneous activity patterns in the model are very similar to those seen in two-photon calcium imaging data (Figure 2—figure supplement 1E, F).

Next, we combined stimulus-driven and background-driven activity to derive the orientation tuning curve of the model neuron (see Extended methods, Orientation tuning validation protocol). We focused on the biologically plausible model (see Extended methods, Model description), whereby the distribution of tuned synaptic inputs onto the basal and apical trees is in line with experimentally reported values (60% vs 40%, respectively; Defelipe and Fariñas, 1992). The resulting orientation tuning curve (preferred orientation firing rate: 1.55 ± 0.3 Hz, orthogonal orientation firing rate: 0.21 ± 0.12 Hz, OSI 0.77 ± 0.11, tuning width 44 ± 9.17°; Figure 2A) indicates that the model neuron is well-tuned (OSI >0.2, tuning width <80°; see Extended methods, Orientation tuning validation protocol), in agreement with our prior work using the original version of this model (Park et al., 2019). We also reproduced the apical tree ablation experiment from that publication, finding that orientation tuning does indeed persist post-ablation (Figure 2—figure supplement 5; see Extended methods, Ablation protocol).

![Figure 2.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig2-v2.jpg)

**Figure 2.:** (A) Orientation tuning curve for the ‘biologically plausible’ model. (B) Example from a configuration of a model neuron set to a disparity of 40°. Right-side polar plots display the distribution of synaptic orientation preferences for the indicated dendritic segments. Left-side polar plots display the distribution of synaptic orientation preferences for the apical (top) and basal (bottom) dendritic trees. (C) Example voltage traces recorded at the soma of a model neuron from (A) Note the clearly different responses between the preferred orientation (0°) and all others. (D) Orientation preference plot for the ‘biologically plausible’ model featuring various degrees of disparity. Grey dashed line denotes the expected orientation preference per degree of disparity. Black and red arrows point in the direction of basal and apical dominance, respectively. (E) As D, but for the ‘even’ model. Note that dominance has shifted from the basal domain towards the apical domain. (F) As D, but for the ‘inverted biologically plausible’ model. This configuration clearly features apical dominance. Error bars: Standard error of the mean, for all panels.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Simultaneous recordings from basal dendritic segments and somata of L2/3 V1 pyramidal neurons were performed in anesthetized mice (spontaneous activity of 11 neurons from 2 mice, see Extended methods, Data analysis; panel A). These imaging data were compared to modeling data generated using the spontaneous activity protocol, whereby simulations feature only background activity, that is noise, in the absence of a visual stimulus (see Extended methods, Spontaneous activity protocol). (A) Image from one of the neurons in the dataset. Note the separate, multiple ROIs per dendritic segment, as well as the four circular ROIs used for background fluorescence calculation. (B) Example traces from the model data conversion pipeline. Voltage spiking data is binarized and convolved with a GcaMP6s kernel function (Figure 2—figure supplement 2). Resulting data is downsampled to two-photon sampling rates (~7.25 Hz) from the original sampling rate (10 KHz), and processed exactly like in vivo two-photon fluorescence data. Red vertical lines show the timing of the original spikes. (C) Example somatic (top) and distal dendritic (bottom) ΔF/F0 traces from the neuron in (A) Black dots at the origin of colored dashed lines denote detected events. Note that somatic events (green dashed lines/arrows) are not necessarily coincident with dendritic events (red dashed lines/arrows). (D) Event-triggered averages for all somatic (blue) and basal dendritic segment ROIs (1 dt ≃ 0.138 s; error bars: Standard error of the mean). (E) Event pair timing difference histogram for the two-photon data. A total of 48.12% of event pairs feature basal dendritic events that are decoupled from the soma (red; dendritic events occur at least 1 dt before the onset of a somatic spike), with 27.8% being decoupled if the four bins (~552ms) closest to zero are excluded (excluded data marked as lightly shaded bars). (F) Event pair timing difference histogram for the converted model data; 48.79% of event pairs feature basal dendritic events that are decoupled from the soma (red; dendritic events occur at least 1 dt before the onset of a somatic spike), with 24.3% being decoupled if the 4 bins (~552ms) closest to zero are excluded (excluded data marked as lightly shaded bars). Note that in both D and E, the zero-difference bin was removed, as it is assumed to contain the majority of backpropagating events. The middle two bars in F have been truncated for visualization purposes; the corresponding values are (left to right) 0.15958 and 0.16533, respectively. Some of the detected somatic events are not closely preceded by any detected basal dendritic events (panel F, green bars), suggesting that other events, perhaps arising in the apical tree or basal dendritic segments not in the recording field of view, contribute to somatic activity in such cases.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Illustration of the output of the kernel function for a single event (AP) occurring at t0 = 500ms. (marked as a red line). (B) Response intensity as a function of the number of events (APs) within a 250ms window. Compare with (Chen et al., 2013).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Somatic waveforms in blue, basal dendritic waveforms in red. Spike onset detected at t=5 dt. (A) Waveforms from all detected events from both mice. (B) Waveforms from all detected events in mouse 1. (C) Waveforms from all detected events from mouse 2. Note: 1 dt is equal to approximately 0.138 s, and exactly equal to the microscope recording frame time.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) Event-triggered averages for somatic (blue) and basal dendrite (red) events in mouse 1. (B) Event-triggered averages for somatic (blue) and basal dendrite (red) events in mouse 2. Note the difference in fluorescence intensity compared to mouse 1. Error bars: Standard error of the mean. (C) Comparison of the true (two-photon) data distribution (blue) with the null distribution (light red). Distributions are different (K.S. two-sample test; test value ~0.105, p<<0.05). Note that the middle bar for the true data has been truncated (actual value 0.12267).

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** Note that the y-axis shows the normalized response (firing rate values divided by their corresponding maximum). Error bars: standard error of the mean.

Having established the orientation tuning of our model cell, we tried to disentangle the effects of the apical and basal trees by introducing dendritic disparity (Figure 2B; see Extended methods, Orientation disparity protocol). We used the disparity protocol, in which the apical and basal trees are tuned to different orientations: the apical tree features synaptic orientation preferences sampled from a Gaussian distribution with a mean of 0°, whereas the basal tree uses the same method, but with a different mean (0° - 90°, in steps of 10°). The expected orientation preference of the model neuron is calculated using Euler’s Formula, which assumes that synapses contribute to overall orientation preference in a linear fashion (for details, see Extended methods, Orientation disparity protocol). We found that the model neuron diverges from the expected orientation preference (linear summation of synaptic inputs) and exhibits a bias towards the preferred orientation of the basal tree. This is an example of basal dominance (Figure 2D) and was previously observed using the original version of the model used here (Park et al., 2019). Of note, the model neuron did not exhibit adequate tuning (i.e. 20% or more of neurons featured OSI <0.2 or tuning width >80°; see Extended methods, Orientation tuning validation protocol) beyond a dendritic disparity of 50°.

To assess whether this result depends on the particular synaptic distribution used, we repeated the experiment using two different synaptic distribution profiles – the ‘inverse biologically plausible’ (40% on the basal tree, 60% on the apical tree) and ‘even’ (50% on both trees) models (see Extended methods, Model description). We found that, indeed, the deviation from expectation displayed by the neuron appears to be decreased in the ‘even’ model, and is clearly reversed in the ‘inverse biologically plausible’ model. Similar to the ‘biologically plausible’ model, these two models did not feature adequate tuning past 50° of dendritic disparity. Overall, the observed deviation from expectation indicates that apical and basal synaptic inputs are not linearly combined, but rather interact in a non-linear manner to produce somatic output. This interaction is influenced by the synaptic distribution along the two dendritic trees, as well as their mean synaptic orientation preferences.

### Apical sodium spikes are the primary driver of neuronal output

The previous results show that orientation tuning emerges from non-linear interactions between apical and basal trees. To elucidate the contribution of each tree in orientation tuning, we selectively interrupt specific aspects of their operation and assess the effect of the intervention on somatic tuning. We start by selectively and precisely modifying the sodium spiking activity of each dendritic tree, while controlling for the type of input received (stimulus-driven vs background-driven). Specifically, we use the ionic intervention protocol (see Extended methods, Ionic intervention protocol) to remove the sodium-induced depolarization that is provided by either the apical or the basal tree, just before the generation of a somatic spike.

We start by using a control version of the ‘biologically plausible’ model (‘Control background’) and a preferred (0°) stimulus (case #1). In this condition, both stimulus-driven and background-driven synapses are active, and most synapses (60%; both stimulus-driven and background-driven) are allocated on the basal tree. For every somatic spike, we perform the intervention protocol and categorize the spike as either: ‘apically driven’ (dependent on the presence of apical sodium conductances), ‘basally driven’ (dependent on the presence of basal sodium conductances), or ‘cooperative’ (dependent on the presence of both apical and basal sodium conductances; Figure 3A). We find that the majority of somatic spikes are dependent on apical sodium conductance (N=131 spikes; apically driven 76.51 ± 10.21%, basally driven 9.61 ± 5.03%, cooperative 13.89 ± 11.22%; Figure 3B), which is surprising, considering the proximity of the basal dendrites to the soma, as well as the salient nature of the feedforward, visually evoked inputs received by the basal tree. These somatic events are a mix of stimulus-driven and background-driven input. In order to separate the two, we changed the orientation of the stimulus being presented to 90° (i.e. orthogonal to the orientation preference of the neuron), rendering the vast majority of stimulus-driven synapses inactive, while keeping background-driven synapses active as normal (case #2). We found that the resulting percentages are similar to the previous condition (N=25 spikes; apically driven 71.07 ± 31.56%, basally driven 17.5 ± 22.5%, cooperative 1.43 ± 4.29%; Figure 3D), indicating that the dependence of somatic spiking activity on dendritic sodium conductance does not significantly differ between instances of stimulus-driven and background-driven activity.

![Figure 3.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig3-v2.jpg)

**Figure 3.:** (A) Diagram describing the ionic intervention protocol, with example traces on the right. Shaded areas on the traces denote the pre-spike (grey) and post-spike (red) intervention time windows. (B) Somatic spike dependence on dendritic sodium conductance for the ‘biologically plausible’ model with a stimulus of 0° (preferred orientation). (C) Same as B, but background synapses are evenly distributed across the apical and basal dendritic trees, while stimulus-driven synapses follow the ‘biologically plausible’ (60% basal, 40% apical) model. (D) Somatic spike dependence on dendritic sodium conductance for the ‘biologically plausible’ model with a stimulus of 90° (orthogonal/non-preferred orientation). (E) Same as D, but background synapses follow the ‘even’ model (evenly distributed), while stimulus-driven synapses follow the ‘biologically plausible’ (60% basal, 40% apical) model. ‘N’ is the total number of spikes for each condition. Error bars: Standard error of the mean, for all panels.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Visualization of basal dendrites. Colors correspond to traces in panels B and C. (B) Voltage traces from the basal dendrites and soma (blue) around the occurrence of an apically driven somatic spike. (C) Voltage traces from the basal dendrites and soma (blue) around the occurrence of a basally driven somatic spike. (D) Visualization of a specific apical path. Colors correspond, in the same sequence (proximal to distal), to the traces in panels E and F. (E) Voltage traces from the soma (blue) and the apical dendritic segments shown in D around the occurrence of an apically driven somatic spike. (F) Voltage traces from the soma (blue) and the apical dendritic segments shown in D around the occurrence of a basally driven somatic spike. (G) As in D, but for a different apical path. (H) As in E, but for a different apical path. (I) As in F, but for a different apical path. In all panels, traces are ordered by distance of the recording point from the soma (closest to farthest). Red dots denote the maximum voltage attained by the corresponding dendritic segment. Magenta dashed line indicates the timing of the somatic spike. The soma (and corresponding somatic trace) is always marked in blue. Dendritic segments colored grey are not inactive during these events, but their activity is not shown directly in these traces. Dashed arrows indicate propagation of potential towards (dark green) or away from (dark red) the soma.

However, it is possible that background-driven synapses are actually the ones that determine somatic spiking. While firing at low rates (0.11 Hz vs 0.3 Hz for stimulus-driven; see Extended methods, Model description), these synapses are vastly more numerous compared to stimulus-driven synapses (75% vs 25% of total synapses). To test this possibility, we equalized the contribution of background-driven synapses to apical and basal tree outputs, by introducing a new condition (‘Evenly distributed background’) whereby the model is configured as in case #1 (i.e. ‘biologically plausible’ model), but the distribution of background-driven synapses is the same on both trees (i.e. excitatory: 50% apical, 50% basal; inhibitory: 46.5% apical, 46.5% basal, 7% soma). In this way, we ensure that the greater proportion of background-driven synapses on the basal tree is no longer a confounding factor. Presenting a stimulus of the preferred orientation (0°) under these conditions (case #3), we find that the resulting percentages (N=156 spikes; apically driven 85.08 ± 7.34%, basally driven 5.15 ± 6.72%, cooperative 9.78 ± 8.17%; Figure 3C) are similar to those seen in case #1, indicating that the distribution of background-driven synapses does not significantly affect somatic spike generation.

By changing the orientation of the presented stimulus to 90° for this altered model configuration, we can also evaluate whether the same conclusion holds for background-driven spikes (case #4). Indeed, the results (N=42 spikes; apically driven 85.83 ± 29.83%, basally driven 2.5 ± 7.5%, cooperative 1.67 ± 5.0%; Figure 3E) are not significantly different from those seen in case #2. These simulations predict that somatic spike generation reliably depends on apical sodium conductance, a seemingly counterintuitive finding, as feedforward stimulus-driven input reaches mostly the basal tree and not the apical tree.

To gain more insight into these findings, we looked at the spatiotemporal evolution of voltage through different apical and basal paths during the occurrence of an apically or basally driven spike (Figure 3—figure supplement 1). For heavily branching apical dendrites, input summation and/or voltage propagation in one segment along the path exceeds the sodium spiking threshold, leading to a cascade of dendritic sodium spikes both in the direction of the soma as well as towards any terminal dendrites that did not yet generate sodium spikes of their own (e.g. Figure 3—figure supplement 1H; dendritic sodium spiking does not originate from the terminal segment, but propagates to it). The lack of extensive branching on the basal dendrites, on the other hand, renders them less predictable in terms of sodium spiking activity (e.g. Figure 3—figure supplement 1C). Although the intervention experiments are required in order to decisively determine the origin of each somatic spike, the temporal precedence of dendritic sodium spiking reliably indicates which tree drives somatic spiking activity (e.g. compare Figure 3—figure supplement 1B, C, E, F).

### Apical and basal dendrites influence somatic tuning via different mechanisms

The previous results are counter-intuitive: although we would expect both apical and basal dendritic segments to contribute to somatic spiking, the contribution of the apical tree overshadows that of the basal tree, at least with respect to the role of sodium conductances. However, as indicated by our results in Figure 2D, the basal tree, being the bearer of the majority of feedforward inputs, has a dominant role in orientation tuning. Thus, we assume that the basal tree exerts its influence via a different mechanism. To assess the veracity of this assumption, we performed a series of experiments aimed at evaluating the impact of ionic (see Extended methods, Sodium (channel) blockage and Ionic intervention protocol) and synaptic (see Extended methods, Synaptic modulation, Input manipulation and Synaptic intervention protocol) mechanisms on neuronal orientation tuning, using the biologically plausible model (see Extended methods, Stimulation protocol).

First, we assess the tuning characteristics of the neuron when stimulus-driven input is removed from either the apical or the basal tree (see Extended methods, sectionInput manipulation), and compare it with the control case. We find that the neuron remains tuned in all cases, albeit with significantly decreased OSI values (dependent two-sample t-test, control vs basal: p ≈ 0.000037; control vs apical: p ≈ 0.000007) (Figure 4A). Removal of apical stimulus-driven input has a much smaller effect on tuning than removal of basal input (dependent two-sample t-test, apical vs basal: p ≈ 0.0095), which is in line with our previous findings (Park et al., 2019).

![Figure 4.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig4-v2.jpg)

**Figure 4.:** (A) Orientation tuning curves (left) and mean OSI values (right) for the experiment where stimulus-driven synapses are completely absent on either the apical (‘apical target’; red) or basal (‘basal target’; green) tree. (B) Selective reduction of stim-driven synaptic (AMPA/NMDA) weights by 50% 30ms prior to somatic spike occurrence (lasting up to 10ms after the pre-recorded somatic spike timing), on either the apical (apical target; red) or basal (basal target; green) tree. (C) Nullification of sodium conductances 3ms prior to somatic spike occurrence (lasting up to 1ms after the pre-recorded somatic spike timing), on either the apical (apical target; red) or basal (basal target; green) tree. Error bars: Standard error of the mean, for all panels. If present, ‘n/a’ denotes a lack of orientation tuning for that specific experimental setup. Stars denote statistical significance at a significance level (α) of 0.05 (*), 0.01 (**) or 0.001 (***), whereas ‘n.s.’ stands for ‘no statistically significant difference’, that is p-value ≥ α. Dependent two-sample t-tests were used in all cases.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Apical gNa decreased by 5%. Elimination of the apical sodium component results in total loss of tuning. (B) Apical gNa decreased by 10%. Unlike A, elimination of the apical or basal sodium component results in total loss of tuning. (C) Apical gNa is unchanged (control condition, identical to Figure 4C). Similar to A, elimination of the apical sodium component results in total loss of tuning. If present, ‘n/a’ denotes a lack of orientation tuning for that specific experimental setup. Stars denote statistical significance at a significance level (α) of 0.05 (*), 0.01 (**) or 0.001 (***), whereas ‘n.s.’ stands for ‘no statistically significant difference’, that is p-value ≥ α. Dependent two-sample t-tests were used in all cases.

Next, we use the synaptic intervention protocol to selectively reduce synaptic (AMPA and NMDA) weights by 50% on either the apical or basal tree for a brief time only, and only when a somatic spike is about to occur (see Extended methods, seSynaptic intervention protocol). We find that somatic tuning is completely abolished when manipulating the basal but not the apical synaptic weights, although tuning is significantly affected by loss of apical inputs as well (Figure 4B; dependent two-sample t-test, control vs apical: p ≈ 0.00065). These results indicate that synaptic input from the basal tree is critical for orientation tuning, while apical tree synaptic inputs play a less important role.

Finally, we assess the impact of sodium conductance nullification (as in Figure 3), this time on orientation tuning rather than somatic spiking. In line with our previous results (Figure 3), we find that sodium conductance nullification in the apical tree completely abolishes orientation tuning (Figure 4C) while the same manipulation in the basal tree has no impact on tuning (dependent two-sample t-test, control vs basal: p ≈ 0.24125).

### Sensitivity analysis

To assess whether the above findings are robust to biologically relevant variability in the conductance values of sodium channels, we performed a sensitivity analysis whereby we reduced the sodium conductance only in the apical tree by either 5% or 10% (Figure 4—figure supplement 1). For a decrease of 5%, we found that elimination of the apical but not the basal sodium component results in total loss of tuning (dependent two-sample t-test, control vs basal p-value: 0.32549). Importantly, in this scenario the apical tree remains the primary driver of somatic activity as the majority of somatic spikes are apically driven (Figure 4—figure supplement 1A N=345 spikes; 60 ± 15% of spikes are apically driven, 30 ± 18% are basally driven, and 10 ± 8% of spikes are cooperatively driven, for details on the characterization of spiking activity, see Results, Apical sodium spikes are the primary driver of neuronal output). However, a 10% decrease in the apical sodium conductance results in total loss of tuning when either the apical or the basal sodium component is eliminated (Figure 4—figure supplement 1B). In this case, a large number of spikes are completely lost (N=190 spikes vs 345), and out of the remainder, 41 ± 25% are apically driven, 48 ± 28% are basally driven, and 11 ± 12% are cooperatively driven. We further compare these two conditions (5% and 10% reduction) with one where the apical sodium conductance is unchanged (Figure 4—figure supplement 1C identical to Figure 4C). Similarly to the results seen in the 5% reduction, elimination of the apical – but not the basal – sodium component results in total loss of tuning (dependent two-sample t-test, control vs basal p-value: 0.24125). In this case, 80 ± 9% of spikes are apically driven, 13 ± 8% are basally driven, and 7 ± 4% of spikes are cooperatively driven. Notably, the number of spikes is drastically higher in this condition (N=885 spikes in the unchanged condition vs. N=345 for the 5% reduction and N=190 for the 10% reduction).

The above simulations show that, as expected, the reduction in apical sodium conductance results in a decrease of the overall spiking rate of the neuron (number of spikes: 885 in the unchanged condition, 345 for the 5% reduction, and 190 for the 10% reduction). Even so, decreasing apical sodium conductance by 5% failed to negate its role in somatic spike generation, with the apical tree remaining the primary contributor (60 ± 15% of spikes were apically driven vs 30 ± 18% basally driven; Figure 4—figure supplement 1A). A decrease of 10%, however, exerts greater influence as an ever-larger number of apically driven spikes are lost, shifting the percentages to a more even distribution between apically driven and basally driven (41 ± 25% vs 48 ± 28%, respectively; Figure 4—figure supplement 1B). Of note, in this particular case the neuronal firing rate is well below the experimentally relevant range, suggesting that such a reduction is not physiological (see Figure 4—figure supplement 1A, B). Overall, our sensitivity analysis suggests a greater-than-expected contribution of apical sodium non-linearities in somatic spike generation. This finding is in line with experimental work showing that L2/3 V1 neurons can produce spikes even in the absence of feedforward (i.e. basal stimulus-driven) activity (Keller et al., 2020).

Overall, our simulations predict that apical sodium channels are necessary for both spike generation in general (Figure 3) as well as for orientation tuning in particular (Figure 4C). Additionally, AMPA and NMDA activity is necessary for both apical and basal trees (Figure 4A and B). This means that the apical tree most likely exerts its influence on somatic spiking via sodium-mediated spiking, whereas the basal tree mostly utilizes AMPA- and NMDA-driven depolarizations, rather than sodium spikes.

### Tree-specific morphological and electrophysiological properties influence dendritic and somatic behavior

Our simulations predict that apical and basal dendritic segments exert causal influence on somatic spike generation via separate mechanisms. In an attempt to explain these differences in contribution, we looked at the anatomical and electrophysiological properties of the two types of dendrites (apical/basal). Specifically, we searched for links between anatomical/electrophysiological properties of dendrites and (a) signal attenuation or (b) dendritic excitability (number of synapses required to drive a local sodium spike, or ‘threshold’; see also Extended methods, Quantification of dendritic impact on somatic output for details).

To ensure a fair comparison among different dendritic branches, we induced a 20 mV local EPSP (actual amplitudes: 19.78±0.98 mV) and assessed its attenuation at the soma (see Extended methods, Quantification of dendritic impact on somatic output). We found that EPSP attenuation is greater in apical versus basal dendritic segments of similar length (Figure 5A; p-value 0.000002), diameter (Figure 5B; p-value 0.005864), or volume (data not shown; p-value 0.000001). When normalized by distance from the soma (data not shown; p-value 0.42941), dendritic path volume (data not shown; p-value 0.027934), or electrotonic length (data not shown; p-value 0.666959), EPSP attenuation did not significantly differ between apical and basal dendritic segments. We also examined the relationship between apical vs. basal EPSP attenuation with respect to high apical dendrite branching order (>3), as well as high apical dendrite distance from the soma (>182.7 μm). We found no significant difference between apical and basal dendrite EPSP attenuation with respect to high apical dendrite branching order (Figure 5—figure supplement 1D; apical attenuation: 16.59±3.18 mV, basal attenuation: 12.69±4.04 mV, p-value 0.0580). A statistically significant difference did emerge in the case of EPSP attenuation in basal dendrites versus distant (d≥182.7 μm) apical dendrites (Figure 5—figure supplement 1C; apical attenuation: 17.64±1.84 mV, basal attenuation: 12.69±4.04 mV, p-value 0.0236). We observed, however, that a particular basal dendritic segment – segment #3, the only one featuring branching in the basal tree – yielded unusually low attenuation values (all basal dendritic segments: 12.69±4.04 mV, outlier: 5.11 mV, basal dendritic segments excluding outlier: 13.96±2.8 mV), and repeated the analysis without this atypical data point, still yielding statistically significant differences between distant apical and basal dendrites (apical attenuation: 17.64±1.84 mV, basal attenuation: 13.96±2.8 mV, p-value 0.0312; see Extended Methods, Relationship of branch order and distance with signal attenuation for details). We also repeated the analysis for apical dendrites of high branching order without this outlier, finding no significant changes in the results (apical attenuation: 16.59±3.18 mV, basal attenuation: 13.96±2.8 mV, p-value 0.0956).

![Figure 5.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig5-v2.jpg)

**Figure 5.:** (A) Left: Attenuation of a 20 mV dendritic EPSP (measured at the soma) as a function of dendritic segment length. Right: Comparison of length-normalized EPSP attenuation at the soma between apical and basal dendritic segments. Apical dendritic segments feature greater attenuation. (B) Left: Attenuation of a 20 mV dendritic EPSP (measured at the soma) as a function of dendritic segment diameter. Right: Comparison of diameter-normalized EPSP attenuation at the soma between apical and basal dendritic segments. Apical dendritic segments feature greater attenuation. (C) Left: Dendritic sodium spiking thresholds as a function of dendritic electrotonic length. Right: Comparison of electrotonic length-normalized sodium spiking thresholds between apical and basal dendritic segments. Apical dendritic segments feature lower thresholds. (D) Left: Dendritic sodium spiking thresholds as a function of dendritic volume. Right: Comparison of volume-normalized sodium spiking thresholds between apical and basal dendritic segments. Apical dendritic segments feature greater thresholds, but also much greater variability of thresholds. Stars denote statistical significance at a significance level (α) of 0.05 (*), 0.01 (**) or 0.001 (***), whereas ‘n.s.’ stands for ‘no statistically significant difference’, i.e. p-value ≥ α.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Dendritic segments were stimulated with a number of synapses sufficient to elicit dendritic sodium spiking, and the attenuation at the soma was measured. (A) Somatic sodium spike attenuation as a function of dendritic segment diameter (left panel). Differences between apical and basal dendrites can be evaluated by normalizing spike attenuation by the diameter of the dendritic segment (right panel), showing significantly greater attenuation per μm for apical over basal dendrites (p-value 0.006459). (B) Somatic sodium spike attenuation as a function of dendritic segment length (left panel). Differences between apical and basal dendrites can be evaluated by normalizing spike attenuation by the length of the dendritic segment (right panel), showing significantly greater attenuation per μm for apical over basal dendrites (p-value 0.000097). (C) 20 mV EPSP attenuation as a function of distance of the dendritic segment from the soma. (D) 20 mV EPSP attenuation as a function of the branch order of the dendritic segment. (E) As C, but for sodium spikes rather than 20 mV EPSPs. (F) As D, but for sodium spikes rather than 20 mV EPSPs. Stars denote statistical significance at a significance level (α) of 0.05 (*), 0.01 (**) or 0.001 (***), whereas ‘n.s.’ stands for ‘no statistically significant difference’, that is p-value ≥ α.

We also performed analyses for dendritic sodium spikes (Figure 5—figure supplement 1) and found similar results: spike attenuation is greater in apical versus basal dendritic segments, when comparing apical and basal dendritic segments of approximately equivalent length (Figure 5—figure supplement 1B; p-value 0.000097), diameter (Figure 5—figure supplement 1A; p-value 0.00646), or volume (data not shown; p-value 0.000002). There was no significant difference in spike attenuation between apical and basal dendritic segments when controlling for distance from the soma (data not shown; p-value 0.768547), dendritic path volume (data not shown; p-value 0.061389), or electrotonic length (data not shown; p-value 0.396982). As above, we also examined dendritic spike attenuation at the soma with respect to high apical dendrite branching order and high apical dendrite distance from the soma. There was no significant difference between attenuation for apical vs basal sodium spikes with respect to branching order (Figure 5—figure supplement 1F; apical attenuation: 64.93±26.28 mV, basal attenuation: 49.72±24.3 mV, p-value 0.1997) or distance from the soma (Figure 5—figure supplement 1E; apical attenuation: 70.94±22.85 mV, basal attenuation: 49.72±24.3 mV, p-value 0.0844). Once again, however, we observe unusual attenuation values for basal dendritic segment #3 (all basal dendritic segments: 49.72±24.3 mV, outlier: –8.308 mV, basal dendritic segments excluding outlier: 59.4±5.8 mV), caused by additional current provided by its child branches that feature much lower sodium spiking thresholds (6 synapses for child branches vs 19 synapses for parent branch; see Extended methods, Relationship of branch order and distance with signal attenuation for details). As such, we repeated these two analyses excluding this data point. Results did not change for high apical dendrite branch order (apical attenuation: 64.93±26.28 mV, basal attenuation: 59.4±5.8 mV, p-value 0.2894), but a statistically significant difference did emerge in the comparison of distant apical dendrites against basal dendrites (apical attenuation: 70.94±22.85 mV, basal attenuation: 59.4±5.8 mV, p-value 0.0336).

The above suggest that signals originating in apical vs. basal dendritic segments with similar morphological characteristics (length, diameter, volume), attenuate more than those originating in basal dendritic segments. This is partly because most apical dendrites are located further away from the soma compared to basal dendrites: comparison of EPSP and sodium spike attenuation with respect to distance from the soma yields statistically significant differences between basal and distant apical dendrites for EPSPs, although the difference is not significant for spikes (Figure 5—figure supplement 1C, E).

Finally, we also examined the relationship between dendritic sodium spiking thresholds and the morphological and electrophysiological parameters stated previously. We found that dendritic sodium spiking thresholds are significantly lower for apical versus basal dendritic segments with approximately equivalent values of electrotonic length (Figure 5C; p-value 0.001585), but this relationship is reversed for dendritic segments with similar volume (Figure 5D; p-value 0.000002). On the contrary, apical and basal dendritic segments featuring similar distances from the soma (data not shown; p-value 0.320436), dendritic path volume (data not shown; p-value 0.418108), length (data not shown; p-value 0.407686), or diameter (data not shown; p-value 0.592490) did not exhibit significant differences in their sodium spiking thresholds.

Taken together, this analysis shows that – as expected – the attenuation of signals originating in morphologically and electrophysiologically equivalent dendritic segments is significantly larger for apical vs. basal dendrites, likely because most apical dendrites are located further away from the soma. However, the threshold for inducing sodium spikes in apical dendritic segments is significantly smaller compared to basal dendritic segments of similar electrotonic length (most likely due to the proximity of the soma, causing a ‘current sink’ effect for basal dendrites), making it easier to drive such spikes in the apical compared to the basal tree. These findings provide a more intuitive explanation of the greater role of sodium conductances in the apical vs. basal trees of our model neuron.

## Discussion

In this work, we used a detailed computational model to delineate the dendritic constituents of neuronal computation in L2/3 V1 pyramidal cells. We found that the model exhibits a wide range of non-linear behavior at the dendritic segment level (Figure 1) and can mimic the activity patterns of neurons under spontaneous conditions in vivo (Figure 2—figure supplement 1). The model neuron exhibits robust orientation tuning in response to tuned input (Figure 2A), and under conditions of dendritic disparity, the model still remains robustly tuned (OSI <0.2 and tuning width >80°) for non-extreme dendritic disparity conditions (disparity ≤50°). Importantly, the neuronal orientation preference deviates from the expected one (Figure 2D–F), indicating that apical and basal inputs interact in non-linear ways. This bias is dependent on the distribution of synaptic inputs along the two trees (Figure 2D–F), it follows the preference of basal tree inputs under physiological conditions (Figure 2D) and is in line with prior work, whereby apical tree ablation had no impact on somatic orientation preference (Figure 2—figure supplement 5; Park et al., 2019). Remarkably, while the above would seem to suggest a minor role for apical inputs in the orientation preference of our model cell (Figure 2D), we found that the orientation tuning of the neuron is greatly affected by sodium conductances in the apical – but not the basal – tree (Figure 4). Interestingly, while basal sodium channel conductances are not critically important (Figure 4C), AMPA and NMDA conductances are necessary in both dendritic trees for orientation tuning (Figure 4A, B). This indicates that depolarizations from the basal tree play a key role in shaping neuronal output, even when basal sodium spikes do not. As such, neuronal output is a synergistic phenomenon mostly between apical sodium spikes and basal depolarizations or sodium spikes. Our simulations suggest that a form of intra-tree dendritic cooperativity – a synergistic effect between apical and basal dendritic segments that exhibit activity in relative synchrony – might be present in these neurons. This is supported by the existence of extinction-prone ‘cooperative’ somatic spikes that are lost when either of their dendritic components (apical or basal, be that depolarization or spiking) is lost (Figure 3). Additional evidence is provided by the experiments in which removal or suppression (decrease in conductance) of basal stimulus-driven synapses (i.e. only background-driven synapses are fully active) significantly decreases the quality of orientation tuning (i.e. OSI values) in the model neuron, or abolishes tuning altogether (Figure 4A, B).

A potential explanation for the differential contributions of apical and basal dendrites lies with their morphological and electrophysiological properties. Despite featuring a uniform sodium conductance throughout both dendritic trees, basal dendrites have higher sodium spiking thresholds than apical dendrites with similar electrotonic length values. Moreover, apical dendrites have highly variable spiking thresholds (Figure 5D). This is likely because the soma acts as a current sink, effectively increasing the sodium spiking threshold of all soma-proximal branches (mostly basal dendrites). Meanwhile, the majority of apical dendrites feature much better electrical isolation from the soma due to distance and branching, and are as such exempt from such current sink effects, instead only suffering a loss of current from other connected apical dendritic branches. As such, they exhibit a much greater range of possible thresholds compared to basal dendrites of similar volume (Figure 5D), while simultaneously featuring greater signal attenuation (Figure 5—figure supplement 1C, E). Put together, these results indicate that apical dendrites overcome their signal attenuation deficit (compared to basal dendrites) by having a greater propensity for dendritic sodium spike generation for different amounts of input. This suggests that sodium spikes are more difficult to induce in basal compared to apical dendrites, offering a potential explanation as to why apical sodium conductances contribute more to somatic output.

Taken together, our model predicts that somatic output in L2/3 V1 pyramidal neurons is likely to be determined through Bimodal Input Coincidence, a subcategory of coincidence detection (Figure 6). Specifically, we propose that the basal tree receives visual feedforward input, representing the information therein as a series of hyperpolarizations, depolarizations, and occasional dendritic spikes. Thus, visual input creates a basal ‘backdrop’ of depolarizations that represents visual information. At the same time, predictive and attentional signals from higher-order cortical areas reach the apical tree of the neuron, causing the generation of dendritic spikes that propagate to the soma and are temporally summed with any concurrent basal depolarization. In the event that visual input is non-existent, or of a non-preferred orientation, the depolarization is minimal to none. Thus, the apical dendritic spike will not be significantly augmented through summation and will fail to produce a somatic response in the majority of cases. If there is visual input, however, especially of an orientation matching the preferred orientation of the basal tree, the aforementioned ‘backdrop’ will include multiple subthreshold depolarizations, perhaps even dendritic spikes. The apical dendritic spikes are thus likely to be temporally summed with these depolarizations and generate a somatic spike. As such, even though most somatic spikes will be generated through an apical tree dendritic spike, the cases in which this is possible in the first place will be dictated by the backdrop of depolarizations (and/or spikes) provided by the basal tree.

![Figure 6.](https://cdn.elifesciences.org/articles/91627/elife-91627-fig6-v2.jpg)

**Figure 6.:** Action potential generation requires the spatiotemporal coincidence of apical sodium spikes with either basal sodium spikes or significant basal depolarizations, allowing the neuron to respond to salient stimuli that may or may not be affected by attentional and/or predictive signals from higher-order areas.

The findings presented here propose a more central role for the apical tree than previously suggested. Specifically, in Park et al., 2019, we found that orientation selectivity was not abolished by in vivo laser ablation of the apical tree in L2/3 mouse V1 pyramidal neurons, remaining essentially unchanged following a recovery period of ~1 day. Importantly, the model pr‘sented here reproduces the in vivo ablation findings of the aforementioned study (see Extended methods, Ablation protocol; Figure 2—figure supplement 5). What is seen as a contradiction is resolved by considering that in both Park et al., 2019 and the simulations presented here, apical dendrite ablation is assumed to be accompanied by homeostatic alterations that counteract the increase in input resistance from the loss of the apical tree. These homeostatic mechanisms keep the firing rate of the neuron the same pre- and post-ablation, as seen experimentally (Park et al., 2019). Similarly, the neuron can potentially compensate for the loss of input from one of its dendritic trees via homeostatic mechanisms that amplify the effect of synaptic inputs on the other tree, an approach followed by Mel et al., 1998 in their efforts to demonstrate that V1 L5 pyramidal neurons were capable of exhibiting orientation tuned responses through either apical or basal inputs. Thus, the contribution of the apical tree to somatic spiking in the intact neuron can be obviated by homeostatic mechanisms following apical tree ablation.

Our findings suggest that L2/3 V1 pyramidal cells may perform salient feature extraction from visual input compatible with predictive coding (Rao and Ballard, 1999). When top-down signals reflecting attentional or predictive processes reach the apical tree, they ‘highlight’ appropriate parts of the signal ‘landscape’ generated by the visual input reaching the basal trees through the generation of apical dendritic sodium spikes. This could result in a neuron that is activated only when specific features are present in its receptive field, facilitating the processing of salient stimuli. Such phenomena have been observed experimentally as a result of attention (Simons and Chabris, 1999).

However, this work also suffers from a number of limitations. Our findings are inherently bound to the particular characteristics of the simulated morphology. To ensure their generality, further exploration of different neuronal morphologies of L2/3 V1 neurons is required. However, given that our findings correlate with specific anatomical and electrophysiological features of the model neuron (Figure 5, Figure 5—figure supplement 1), it would be possible to infer whether the behavior we observe in our model could be present in other neuronal morphologies as well. In addition, while repeating our analysis using other morphologies is beyond the scope of this study (validating model function and performing the extensive parameter exploration reported here is highly resource-intensive), our code and all analysis scripts are made publicly available, allowing interested scientists to apply our approach to other morphologies. The sensitivity analysis that we added in Sensitivity analysis (Figure 4—figure supplement 1) also further establishes the robustness of our findings within biologically relevant ranges of ionic conductances. We have taken all these steps in order to more conclusively demonstrate that our findings are likely to generalize to other L2/3 V1 pyramidal neurons. Furthermore, our model is limited by the lack of data on dendritic features such as signal attenuation and distribution of ion channel conductances. However, this has been counteracted at least to some extent by the use of experimental data (e.g. see Figure 2—figure supplements 1–4) and the sensitivity analysis, which demonstrates that our conclusions are robust to biologically relevant variations of the key conductances (Figure 4—figure supplement 1). It should be noted, however, that there could be multiple ‘solutions’ to the problem of model validation, that is multiple different sets of values for the model parameters that yield the desired output. As such, we cannot be absolutely certain that our particular configuration of parameter values is correct, although this is an issue faced by all models in general, and not exclusive to this work.

Additionally, the single-neuron model sacrifices much of the complexity found in the actual L2/3 network, particularly certain input features. First, we do not simulate in vivo-like input patterns, due to a lack of data. Instead, we use randomly generated Poisson spike trains, which are widely used in the field. Also, in our model, inhibitory inputs are not patterned according to different interneuron subtypes and are background-driven, lacking tuning and featuring firing rates lower than stimulus-driven excitatory synapses. A similar complexity loss is incurred by using a relatively simple stimulation protocol, compared to the alternating stimulation of the ‘drifting gradient’ protocol that is more widely used. Additionally, the model does not account for retinotopically shifted inhibitory inputs (e.g. Rossi et al., 2020). Retinotopic shift in inhibitory inputs would not affect our results, since stimulation is implicitly assumed to only take place at the center of the receptive field of the model neuron, a fact which would render any retinotopically offset neurons quiescent. Finally, although inhibitory inputs could be biased towards one dendritic tree over the other, the overall effect of such an imbalance would be a change in the net amount of excitation received by each tree – a scenario which we already explore in part (Figure 2 and Figure 3), finding tuning and somatic spike generation to be generally unaffected. The omission of these features that were unlikely to influence the presence or absence of orientation tuning was performed in an attempt to reduce the complexity (and thus computational requirements) of the model.

In terms of questions that still need to be answered, the exact nature of the attentional and predictive signals received by the apical tree remains to be deciphered. Secondly, the formation of the visual ‘backdrop’ as a result of basal tree depolarization merits further study. Encoding of visual information using mostly subthreshold depolarizations in the presence of noise is an interesting problem, possibly resolved through the effects of intra-tree dendritic cooperativity, where apical spikes sharpen responses to stimulus-driven input rather than noise, improving the signal-to-noise ratio (Poleg-Polsky, 2019). In addition, a number of differences emerge when comparing the visual system across different model species. In rodents, orientation-selective cells akin to V1 simple cells have been discovered in the thalamus itself (Scholl et al., 2013), and direct thalamocortical projections to L1 of V1 have also been observed (Roth et al., 2016). Furthermore, rodent V1 organization follows a dispersed salt-and-pepper motif, unlike the highly structured organization typical of higher mammals like primates and cats (Ohki and Reid, 2007). These differences are important to take into account when trying to infer general rules of function from information derived from rules of information processing in different animal models. Finally, perhaps the most interesting unanswered question is whether these computations take place elsewhere in the cortex in addition to the visual system. Predictive coding as a means of stimulus compression has already been proposed as a way to simplify visual perception (Rao and Ballard, 1999), and this might also be the case for other sensory or cognitive tasks. Larger-scale models of the visual system, featuring realistic input structure and properties, will most likely be required to explore these phenomena in depth. Regardless, further investigation is required in order to unravel the Gordian knot that is visual perception.
