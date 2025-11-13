# Learning accurate path integration in ring attractor models of the head direction system

## Authors

- Pantelis Vafidis<sup>1</sup> ([ORCID: 0000-0002-9768-0609](https://orcid.org/0000-0002-9768-0609)) †
- David Owald<sup>4</sup> ([ORCID: 0000-0001-7747-7884](https://orcid.org/0000-0001-7747-7884))
- Tiziano D'Albis<sup>2</sup> ([ORCID: 0000-0003-1585-1433](https://orcid.org/0000-0003-1585-1433))
- Richard Kempter<sup>2</sup> ([ORCID: 0000-0002-5344-2983](https://orcid.org/0000-0002-5344-2983)) †

### Affiliations

1. Computation and Neural Systems, California Institute of Technology Pasadena United States ([ROR:05dxps055](https://ror.org/05dxps055))
2. Bernstein Center for Computational Neuroscience Berlin Germany ([ROR:05ewdps05](https://ror.org/05ewdps05))
3. Institute for Theoretical Biology, Department of Biology, Humboldt-Universität zu Berlin Berlin Germany ([ROR:01hcx6992](https://ror.org/01hcx6992))
4. Institute of Neurophysiology, Charité – Universitätsmedizin Berlin, corporate member of Freie Universität Berlin and Humboldt-Universität zu Berlin, and Berlin Institute of Health Berlin Germany ([ROR:001w7jn25](https://ror.org/001w7jn25))
5. NeuroCure, Charité - Universitätsmedizin Berlin Berlin Germany ([ROR:001w7jn25](https://ror.org/001w7jn25))
6. Einstein Center for Neurosciences Berlin Germany ([ROR:05s5xvk70](https://ror.org/05s5xvk70))

† Corresponding author

## Abstract

Ring attractor models for angular path integration have received strong experimental support. To function as integrators, head direction circuits require precisely tuned connectivity, but it is currently unknown how such tuning could be achieved. Here, we propose a network model in which a local, biologically plausible learning rule adjusts synaptic efficacies during development, guided by supervisory allothetic cues. Applied to the Drosophila head direction system, the model learns to path-integrate accurately and develops a connectivity strikingly similar to the one reported in experiments. The mature network is a quasi-continuous attractor and reproduces key experiments in which optogenetic stimulation controls the internal representation of heading in flies, and where the network remaps to integrate with different gains in rodents. Our model predicts that path integration requires self-supervised learning during a developmental phase, and proposes a general framework to learn to path-integrate with gain-1 even in architectures that lack the physical topography of a ring.

## Introduction

Spatial navigation is crucial for the survival of animals in the wild and has been studied in many model organisms (Tolman, 1948; O’Keefe and Nadel, 1978; Gallistel, 1993; Eichenbaum, 2017). To orient themselves in an environment, animals rely on external sensory cues (e.g. visual, tactile, or auditory), but such allothetic cues are often ambiguous or absent. In these cases, animals have been found to update internal representations of their current location based on idiothetic cues, a process that is termed path integration (PI, Darwin, 1873; Mittelstaedt and Mittelstaedt, 1980; McNaughton et al., 1996; Etienne et al., 1996; Neuser et al., 2008; Burak and Fiete, 2009). The head direction (HD) system partakes in PI by performing one of the computations required: estimating the current HD by integrating angular velocities; namely angular integration. Furthermore, head direction cells in rodents and flies provide an internal representation of orientation that can persist in darkness (Ranck, 1984; Mizumori and Williams, 1993; Seelig and Jayaraman, 2015).

In rodents, the internal representation of heading takes the form of a localized "bump" of activity in the high-dimensional neural manifold of HD cells (Chaudhuri et al., 2019). It has been proposed that such a localized activity bump could be sustained by a ring attractor network with local excitatory connections (Skaggs et al., 1995; Redish et al., 1996; Hahnloser, 2003; Samsonovich and McNaughton, 1997; Song and Wang, 2005; Stringer et al., 2002; Xie et al., 2002), resembling reverberation mechanisms proposed for working memory (Wang, 2001). Ring attractor networks used to model HD cells fall in the theoretical framework of continuous attractor networks (Amari, 1977; Ben-Yishai et al., 1995; Seung, 1996). In this setting, HD cells can update the heading representation in darkness by smoothly moving the bump around the ring obeying idiothetic angular-velocity cues.

Interestingly, a physical ring-like attractor network of HD cells was observed in the Drosophila central complex (CX, Seelig and Jayaraman, 2015; Green et al., 2017; Green et al., 2019; Franconville et al., 2018; Kim et al., 2019; Fisher et al., 2019; Turner-Evans et al., 2020). Notably, in Drosophila (from here on simply referred to as ‘fly’), HD cells (named E-PG neurons, also referred to as ‘compass’ neurons) are physically arranged in a ring, and an activity bump is readily observable from a small number of cells (Seelig and Jayaraman, 2015). Moreover, as predicted by some computational models (Skaggs et al., 1995; Samsonovich and McNaughton, 1997; Stringer et al., 2002; Song and Wang, 2005), the fly HD system also includes cells (named P-EN1 neurons) that are conjunctively tuned to head direction and head angular velocity. We refer to these neurons as head rotation (HR) cells because of their putative role in shifting the HD bump across the network according to the head’s angular velocity (Turner-Evans et al., 2017; Turner-Evans et al., 2020).

A model for PI needs to both sustain a bump of activity and move it with the right speed and direction around the ring. The latter presents a great challenge, since the bump has to be ‘pushed’ for the right amount starting from any location and for all angular velocities. Therefore, ring attractor models that act as path integrators require that synaptic connections are precisely tuned (Hahnloser, 2003). If the circuit was completely hardwired, the amount of information that an organism would need to genetically encode connection strenghts would be exceedingly high. Additionally, it would be unclear how these networks could cope with variable sensory experiences. In fact, remarkable experimental studies in rodents have shown that when animals are placed in an augmented reality environment where visual and self-motion information can be manipulated independently, PI capabilities adapt accordingly (Jayakumar et al., 2019). These findings suggest that PI networks are able to self-organize and to constantly recalibrate. Notably, in mature flies there is no evidence for such plasticity (Seelig and Jayaraman, 2015) — however, the presence of plasticity has not been tested in young animals.

Here, we propose that a simple local learning rule could support the emergence of a PI circuit during development and its re-calibration once the circuit has formed. Specifically, we suggest that accurate PI is achieved by associating allothetic and idiothetic inputs at the cellular level. When available, the allothetic sensory input (here chosen to be visual) acts as a ‘teacher’ to guide learning. The learning rule is an example of self-supervised multimodal learning, where one sense acts as a teaching signal for the other and the need for an external teacher is obviated. It exploits the relation between the allothetic heading of the animal (given by the visual input) and the idiothetic self-motion cues (which are always available), to learn how to integrate the latter.

The learning rule is inspired by previous experimental and computational work on mammalian cortical pyramidal neurons, which are believed to associate inputs to different compartments through an in-built cellular mechanism (Larkum, 2013; Urbanczik and Senn, 2014; Brea et al., 2016). In fact, it was shown that in layer 5 pyramidal cells internal and external information about the world arrive at distinct anatomical locations, and active dendritic gating controls learning between the two (Doron et al., 2020). In a similar fashion, we propose that learning PI in the HD system occurs by associating inputs at opposite poles of compartmentalized HD neurons, which we call ‘associative neurons’ (Urbanczik and Senn, 2014; Brea et al., 2016). Therefore, to accomplish PI the learning rule relies on structural inductive biases in terms of the morphology and arborization of HD cells.

In summary, here we show for the first time how a biologically plausible synaptic plasticity rule enables to learn and maintain the complex circuitry required for PI. We apply our framework to the fly HD system because it is well characterized; yet our model setting is general and can be used to learn PI in other animal models once more details about the HD circuit there are known (Abbott et al., 2020). We find that the learned network is a ring attractor with a connectivity that is strikingly similar to the one found in the fly CX (Turner-Evans et al., 2020) and that it can accurately path-integrate in darkness for the entire range of angular velocities that the fly displays. Crucially, the learned network accounts for several key findings in the experimental literature, and it generates predictions, including the presence of plasticity in young animals, that could be tested experimentally.

## Results

To illustrate basic principles of how PI could be achieved, we study a computational model of the HD system and show that synaptic plasticity could shape its circuitry through visual experience. In particular, we simulate the development of a network that, after learning, provides a stable internal representation of head direction and uses only angular-velocity inputs to update the representation in darkness. The internal representation of heading (after learning) takes the form of a localized bump of activity in the ring of HD cells. All neurons in our model are rate-based, i.e., spiking activity is not modeled explicitly.

### Model setup

The gross model architecture closely resembles the one found in the fly CX (Figure 1A). It comprises HD cells organized in a ring, and HR cells organized in two wings. One wing is responsible for leftward and the other for rightward movement of the internal heading representation. HD cells receive visual input from the so-called ‘ring’ neurons; this input takes the form of a disinhibitory bump centered at the current HD (Figure 1B, Omoto et al., 2017; Fisher et al., 2019). The location of this visual bump in the network is controlled by the current head direction. We simulate head movements by sampling head-turning velocities from an Ornstein-Uhlenbeck process (Materials and methods), and we provide the corresponding velocity input to the HR cells (Figure 1C). HR cells provide direct input to HD cells, and HR cells also receive input from HD cells (Figure 1A). Both HR and HD cells receive global inhibition, which is in line with a putative ‘local’ model of HD network organization (Kim et al., 2017). The connections from HR to HD cells ($W^{HR}$) and the recurrent connections among HD cells ($W^{rec}$) are assumed to be plastic. The goal of learning is to tune these plastic connections so that the network can achieve PI in the absence of visual input.

![Figure 1.](https://cdn.elifesciences.org/articles/69841/elife-69841-fig1-v2.jpg)

**Figure 1.:** (A) The ring of HD cells projects to two wings of HR cells, a leftward (Left HR cells, abbreviated as L-HR) and a rightward (Right HR cells, or R-HR), so that each wing receives selective connections only from a specific HD cell (L: left, R: right) for every head direction. For illustration purposes, the network is scaled-down by a factor of 5 compared to the cell numbers $N^{HR}=N^{HD}=60$ in the model. The schema shows the outgoing connections ($W^{HD}$ and $W^{rec}$) only from the green HD neurons and the incoming connections ($W^{HR}$ and $W^{rec}$) only to the light blue and yellow HD neurons. Furthermore, the visual input to HD cells and the velocity inputs to HR cells are indicated. (B) Visual input to the ring of HD cells as a function of radial distance from the current head direction (see Equation 5). (C) Angular-velocity input to the wings of HR cells for three angular velocities: 720 (green), 0 (blue), and -360 (orange) deg/s (see Equation 10). (D) The associative neuron: $V^{a}$ and $V^{d}$ denote the voltage in the axon-proximal (i.e. closer to the axon initial segment) and axon-distal (i.e. further away from the axon initial segment) compartment, respectively. Arrows indicate the inputs to the compartments, as in (A), and $I^{vis}$ is the visual input current. (E) Left: skeleton plot of an example HD (E-PG) neuron (Neuron ID =416642425) created using neuPrint (Clements et al., 2020) the ellipsoid body (EB) and protocerebral bridge (PB) are overlayed. Right: zoomed in area in the EB indicated by the box, showing postsynaptic locations in the EB for this E-PG neuron; for details, see Methods. The neuron receives recurrent and HR input (green and orange dots, corresponding to inputs from P-EN1 and P-EN2 cells, respectively) and visual input (purple and blue dots, corresponding to inputs from visually responsive R2 and R4d cells, respectively) in distinct spatial locations.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/69841/elife-69841-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Synaptic locations in the EB where visual (R2 and R4d) and recurrent and HR-to-HD (P-EN1 and P-EN2) inputs arrive, for a total of 16 HD neurons tested (Neuron ID above each panel). Similarly to the example in Figure 1E (repeated here in the top left panel, Neuron ID 416642425), these two sets of inputs appear to arrive in separate locations. (B) Binary classification between the two classes (R2 and R4d vs. P-EN1 and P-EN2) using SVMs with Gaussian kernel. Nested 5-fold crossvalidation was performed 30 times for every neuron tested, and the test accuracy histograms per neuron are plotted. The two classes can be separated with a test accuracy greater than 0.95 for every neuron.

The unit that controls plasticity in our network is an ‘associative neuron’. It is inspired by pyramidal neurons of the mammalian cortex whose dendrites act, via backpropagating action potentials, as coincidence detectors for signals arriving from different layers of the cortex and targeting different compartments of the neuron (Larkum et al., 1999). Paired with synaptic plasticity, coincidence detection can lead to long-lasting associations between these signals (Larkum, 2013). To map the morphology of a cortical pyramidal cell to the one of a HD cell in the fly, we first point out that all relevant inputs arrive at the dendrites of HD cells within the ellipsoid body (EB) of the fly (Xu, 2020) moreover, the soma itself is externalized in the fly brain, and it is unlikely to contribute considerably to computations (Gouwens and Wilson, 2009; Tuthill, 2009). We thus link the dendrites of the pyramidal associative neuron to the axon-distal dendritic compartment of the associative HD neuron in the fly, and we link the soma of the pyramidal associative neuron to the axon-proximal dendritic compartment of the associative HD neuron in the fly. Furthermore, we assume that the axon-proximal compartment is electrotonically closer to the axon initial segment, and therefore, similarly to the somatic compartment in pyramidal neurons, inputs there can more readily initiate action potentials. Note that our model does not require active backpropagation of action potentials — passive spread of voltage to the axon-distal compartment would be sufficient (for details, see Materials and methods and Discussion). We also assume that associative HD cells receive visual input ($I^{vis}$) in the axon-proximal compartment, and both recurrent input ($W^{rec}$) and HR input ($W^{HR}$) in the axon-distal compartment; accordingly, we model HD neurons as two-compartment units (Figure 1D). The associative neuron can learn the synaptic weights of the incoming connections in the axon-distal compartment, therefore, as mentioned, we let $W^{rec}$ and $W^{HR}$ be plastic.

We find that the assumption of spatial segregation of postsynapses of HD cells is consistent with our analysis of EM data from the fly (Xu, 2020). For an example HD (E-PG) neuron, Figure 1E depicts that head rotation and recurrent inputs (mediated by P-EN1 and P-EN2 cells, respectively [Turner-Evans et al., 2020]) contact the E-PG cell in locations within the EB that are distinct compared to those of visually responsive neurons R2 and R4d (Omoto et al., 2017; Fisher et al., 2019), as hypothesized. The same pattern was observed for a total of 16 E-PG neurons (one for each ‘wedge’ of the EB) that we analyzed (Figure 1—figure supplement 1A). To further support the assumption that visual inputs are separated from recurrent and HR-to-HD inputs, we perform binary classification between the two classes, using SVMs (for details, see Materials and methods). Figure 1—figure supplement 1B shows that predicting class identity from spatial location alone in held-out test data is excellent (test accuracy >0.95 across neurons and model runs).

The connections from HD to HR cells ($W^{HD}$) are assumed to be fixed, and HR cells are modeled as single-compartment units. Projections are organized such that each wing neuron receives input from only one specific HD neuron for every HD (Figure 1A). This simple initial wiring makes HR cells conjunctively tuned to HR and HD, and we assume that it has already been formed, for example, during circuit assembly. We note that the conditions for 1-to-1 wiring and constant amplitude of the HD-to-HR connections can be relaxed, because the learning rule can balance asymmetries in the initial architecture (see Appendix 3). In addition, the connections carrying the visual and angular velocity inputs are also assumed to be fixed. Although plasticity in the visual inputs has been shown to exist (Fisher et al., 2019; Kim et al., 2019), here we focus on how the path-integrating circuit itself originally self-organizes. Therefore, to simplify the setting and without loss of generality, we assume a fixed anchoring to environmental cues as the animal moves in the same environment (for details, see Discussion).

In our model, the visual input acts as a supervisory signal during learning (as in D’Albis and Kempter, 2020), which is used to change weights of synapses onto the axon-distal compartment of HD cells. We utilize the learning rule proposed by Urbanczik and Senn, 2014 (for details, see Materials and methods), which tunes the incoming synaptic connections in the axon-distal compartment in order to minimize the discrepancy between the firing rate of the neuron $f⁢(V^{a})$ (where $V^{a}$ is the axon-proximal voltage, primarily controlled by the visual input) and the prediction of the firing rate by the axon-distal compartment from axon-distal inputs alone, $f⁢(p⁢V^{d})$ (where $p$ is a constant and $V^{d}$ is the axon-distal voltage, which depends on head rotation velocity). From now on, we refer to this discrepancy as ‘learning error’, or simply ‘error’ (Equation 18; in units of firing rate). The synaptic weight change $Δ⁢W_{pre,post}$ from a presynaptic (HD or HR) neuron to a postsynaptic HD neuron is then given by:

$$
Δ⁢W_{pre,post}=η⁢[f⁢(V_{post}^{a})-f⁢(p⁢V_{post}^{d})]⁢P_{pre}
$$

where $η$ is the constant learning rate and $P_{pre}$ is the postsynaptic potential from the presynaptic neuron. When implementing this learning rule, we low-pass filter the prospective weight change $Δ⁢W_{pre,post}$ to ensure smoothness of learning.

Importantly, this learning rule is biologically plausible because the firing rate of an associative neuron $f⁢(V^{a})$ is locally available at every synapse in the axon-distal compartment due to the (passive or active) backpropagation of axonal activity to the axon-distal dendrites. The other two signals that enter the learning rule are the voltage of the axon-distal compartment $V^{d}$ and the postsynaptic potential P, which are also available locally at the synapse; for details, see Materials and methods. Furthermore, recent behavioral experiments show that conditioning in Drosophila (Zhao et al., 2021) is not well explained by classical correlation-based plasticity, but it can be well accounted for by predictive synaptic plasticity. The latter is in line with the learning rule utilized here.

### Mature network can path-integrate in darkness

Figure 2A shows an example of the performance of a trained network, for the light condition (i.e. when visual input is available; yellow overbars) and for PI in darkness (purple overbars); the performance is quantified by the PI error (in units of degrees) over time. PI error refers to the accumulated difference between the internal representation of heading and the true heading, and it is different from the learning error introduced previously.

![Figure 2.](https://cdn.elifesciences.org/articles/69841/elife-69841-fig2-v2.jpg)

**Figure 2.:** (A) Example activity profiles of HD, L-HR, and R-HR neurons (firing rates gray-scale coded). Activities are visually guided (yellow overbars) or are the result of PI in the absence of visual input (purple overbar). The ability of the circuit to follow the true heading is slightly degraded during PI in darkness. The PI error, that is, the difference between the PVA and the true heading of the animal as well as the instantaneous head angular velocity are plotted separately. (B) Temporal evolution of the distribution of PI errors in darkness, for 1000 simulations. The distribution gets wider with time, akin to a diffusion process. We estimate the diffusion coefficient to be $D=24.5⁢deg^{2}/s$ (see ‘Diffusion Coefficient’ in Materials and methods). Note that, unless otherwise stated, for this type of plot we limit the range of angular velocities to those normally exhibited by the fly, i.e. $|v|<500$ deg/s. (C) Relation between head angular velocity and neural angular velocity, i.e., the speed with which the bump moves in the network. There is almost perfect (gain 1) PI in darkness for head angular velocities within the range of maximum angular velocities that are displayed by the fly (dashed green horizontal lines; see Methods). (D) Example of consecutive stimulations in randomly permeated HD locations, simulating optogenetic stimulation experiments in Kim et al., 2017. Red overbars indicate when the network is stimulated with stronger than normal visual-like input, at the location indicated by the animal’s true heading (light green line), while red dashed vertical lines indicate the onset of the stimulation. The network is then left in the dark. Our simulations show that the bump remains at the stimulated positions.

A unique bump of activity is clearly present at all times in the HD network (Figure 2A, top), in both light and darkness conditions, and this bump moves smoothly across the network for a variable angular velocity (Figure 2A, bottom). The position of the bump is defined as the population vector average (PVA) of the neural activity in the HD network. The HD bump also leads to the emergence of bumps in the HR network, separately for L-HR and R-HR cells (Figure 2A, second and third panel from top). In light conditions (0–20 s in Figure 2A), the PVA closely tracks the head direction of the animal in HD, L-HR, and R-HR cells alike, which is expected because the visual input guides the network activity. Importantly, however, in darkness (20–50 s in Figure 2A), the self-motion input alone is enough to track the animal’s heading, leading to a small PI error between the internal representation of heading and the ground truth. This error is corrected after the visual input reappears (at 50 s in Figure 2A). Such PI errors in darkness are qualitatively consistent with data reported in the experimental literature (Seelig and Jayaraman, 2015). The correction of the PI error also reproduces in silico the experimental finding that the visual input (whenever available) exerts stronger control on the bump location than the self-motion input (Seelig and Jayaraman, 2015), which suggests that even the mature network does not rely on PI when visual cues are available.

To quantify the accuracy of PI in our model, we draw 1,000 trials, each 60 s long, for constant synaptic weights and in the absence of visual input. We also limit the angular velocities in these trials to retain only velocities that flies realistically display (see dashed green lines in Figure 2C and Methods). We then plot the distribution of PI errors every 10 s (Figure 2B). We find that average absolute PI errors (widths of distributions) increase with time in darkness, but most of the PI errors at 60 s are within 60 deg of the true heading. This vastly exceeds the PI performance of flies (Seelig and Jayaraman, 2015). In flies, the correlation between the PVA estimate and the true heading in darkness varied widely across animals in the range [0.3, 0.95] (Seelig and Jayaraman, 2015), whereas for the model it is close to 1. However, it should be noted that the model here corresponds to an ideal scenario that serves as a proof of principle. We will later incorporate irregularities owing to biological factors (asymmetry in the weights, biological noise) that bring the network’s performance closer to the fly’s behavior.

To further assess the network’s ability to integrate different angular velocities, we simulate the system both with and without visual input in 5 s intervals during which the angular velocity is constant. We then compute the average movement velocity of the bump across the network, that is the neural velocity, and compare it to the real velocity provided as input. Figure 2C shows that the network achieves a PI gain (defined as the ratio between neural and real velocity) close to 1 both with and without supervisory visual input, meaning that the neural velocity matches very well the angular velocity of the animal, for all angular velocities that are observed in experiments ($|v|<500$ deg/s for walking and flying) (Geurten et al., 2014; Stowers et al., 2017). Although expected in light conditions, the fact that gain 1 is achieved in darkness shows that the network predicts the missing visual input from the velocity input, that is, the network path integrates accurately. Note that PI is impaired in our model for very small angular velocities (Figure 2C, flat purple line for $|v|<30$ deg/s), similarly to previous hand-tuned theoretical models (Turner-Evans et al., 2017). This is a direct consequence of the fact that maintaining a stable activity bump and moving it across the network at very small angular velocities are competing goals. Crucially, it has been reported that such an impairment of PI for small angular velocities exists in flies (Seelig and Jayaraman, 2015). Note that if we increase the number of HD neurons from 60 (∼50 were reported in the fly by Turner-Evans et al., 2020; Xu, 2020) to 120 or 240, this flat region is no longer observed (data not shown).

### The network is a quasi-continuous attractor

A continuous attractor network (CAN) should be able to maintain a localised bump of activity in virtually a continuum of locations around the ring of HD cells. To prove that the learned network approximates this property, we seek to reproduce in silico experimental findings in Kim et al., 2017. There it was shown that local optogenetic stimulation of HD cells in the ring can cause the activity bump to jump to a new position and persist in that location — supported by internal dynamics alone.

To reproduce the experiments by Kim et al., 2017, we simulate optogenetic stimulation of HD cells in our network as visual input of increased strength and extent (for details, see Materials and methods). We find that the strength and extent of the stimulation needs to be increased relative to that of the visual input; only in this case, a bump at some other location in the network can be suppressed, and a new bump emerges at the stimulated location. The stimuli are assumed to appear instantaneously at random locations, but we restrict our set of stimulation locations to the discrete angles represented by the finite number of HD neurons. Furthermore, the velocity input is set to zero for the entire simulation, signaling lack of head movement.

Figure 2D shows network activity in response to several stimuli, when the stimulation location changes abruptly every 5 s. During stimulation (2 s long, red overbars), the bump is larger than normal due to the use of a stronger than usual visual-like input to mimic optogenetic stimulation. The way in which the network responds to a stimulation depends on how far away from the ‘current’ location it is stimulated: for shorter distances, the bump activity shifts to the new location, as evidenced by the transient dynamics at the edges of the bump resembling a decay from an initial to a new location (see Figure 2D at {5,15,20} s). However, for larger phase shifts $Δ⁢\theta$ the bump first emerges in the new location and subsequently disappears at the initial location, a mechanism akin to a ‘jump’ (Figure 2D, all other transitions). Similar effects have been observed in the experimental literature (Seelig and Jayaraman, 2015; Kim et al., 2017). The way the network responds to stimulation indicates that it operates in a CAN manner, and not as a winner-takes-all network where changes in bump location would always be instantaneous (Carpenter and Grossberg, 1987; Itti et al., 1998; Wang, 2002). That is to say, the network operates as expected from a quasi-continuous attractor. Furthermore, we find that the transition strategy in our model changes from predominantly smooth transitions to jumps at $Δ⁢\theta≈90⁢deg$, which matches experiments well (Kim et al., 2017).

Following a 2 s stimulation, the network activity has converged to the new cued location. After the stimulation has been turned off, the bump remains at the new location (within the angular resolution $Δ⁢ϕ$ of the network), supported by internal network dynamics alone (Figure 2D). We confirmed in additional simulations that the bump does not drift away from the stimulated location for extended periods of time (3 min duration tested, only 3 s shown), and for all discrete locations in the HD network (only six locations shown). Therefore, we conclude that the HD network is a quasi-continuous attractor that can reliably sustain a heading representation over time in all HD locations. Note that for the network size used ($N^{HD}=60$) we still obtain discrete attractors with separated basins of attraction; however it is expected that with increasing $N^{HD}$ adjacent attractors will merge when the intrinsic noise overcomes the barrier separating them. Indeed, we find that for $N^{HD}=N^{HR}=120$ it is easier to diffuse to adjacent attractors in the presence of synaptic input noise; for the impact of noise, see Appendix 1—figure 1C. In reality, the bump may drift away due to asymmetries in the connectivity of the biological circuit as well as intrinsic noise (Burak and Fiete, 2012) see also Appendix 1. In flies, for instance, the bump can stay put only for several seconds (Kim et al., 2017).

### Learning results in synaptic connectivity that matches the one in the fly

To gain more insight into how the network achieves PI and attains CAN properties, we show how the synaptic weights of the network are tuned during a developmental period (Figure 3). Figure 3A and B shows the learned recurrent synaptic weights among the HD cells, $W^{rec}$, and the learned synaptic weights from HR to HD cells, $W^{HR}$, respectively. Circular symmetry is apparent in both matrices, a crucial property for a symmetric ring attractor. Therefore, we also plot the profiles of the learned weights as a function of receptive field difference in Figure 3C. Note that pixelized appearance in these plots is due to the fact that two adjacent HD neurons are tuned for the same HD, and develop identical synaptic strengths.

![Figure 3.](https://cdn.elifesciences.org/articles/69841/elife-69841-fig3-v2.jpg)

**Figure 3.:** (A), (B) The learned weight matrices (color coded) of recurrent connections in the HD ring, $W^{rec}$, and of HR-to-HD connections, $W^{HR}$, respectively. Note the circular symmetry in both matrices. (C) Profiles of (A) and (B), averaged across presynaptic neurons. (D) Absolute learning error in the network (Equation 19) for 12 simulations (transparent lines) and average across simulations (opaque line). At time $t=0$, we initialize all the plastic weights at random and train the network for $8\times10^{4}$ s (∼22 hr). The mean learning error increases in the beginning while a bump in $W^{rec}$ is emerging, which is necessary to generate a pronounced bump in the network activity. For weak activity bumps, absolute errors are small because the overall network activity is low. After ∼1 hr of training, the mean learning error decreases with increasing training time and converges to a small value. (E), (F) Time courses of development of the profiles of $W^{rec}$ and $W^{HR}$, respectively. Note the logarithmic time scale.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/69841/elife-69841-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Profiles of the HR-to-HD weight matrix $W^{HR}$ from Figure 3C (dashed lines), and the same profiles after the long-range excitatory projections have been removed (solid lines). (B) PI in the resulting network is impaired for high angular velocities, compared to Figure 2C.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/69841/elife-69841-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Learning errors (Equation 18) in the converged network in light conditions (yellow overbar) or during PI in darkness (purple overbar). Note the difference in scale. In light conditions, the error is zero in all positions apart from the edges of the bump, where the error is substantial. Such errors occur because the velocity pathway, which implements PI, cannot move the bump for very small angular velocities, and tends to move it slightly faster for intermediate velocities, and slower for large ones (see Figure 2C). The velocity pathway is active and affects network activity even in the presence of visual input; hence, in light conditions, it creates errors at the edges of the bump, and the sign of the errors is consistent with the aforementioned PI velocity biases. Other than that, the angular velocity input predicts the visual input near-perfectly, as evidenced by the near-zero error everywhere else in the network. During PI in darkness, the network operates in a self-consistent manner, merely integrating the angular velocity input, and the learning error is much smaller. (B) Snapshot of the bump and the errors at $t=11.5$ s in light conditions from (A). Also overlaid is the hypothetical form of the bump if only the visual input was present in the axon-proximal compartment of the HD neurons, termed ‘Visual bump’. Notice that the errors are due to the fact that the visual bump is trailing in relation to the bump in the network. As a result, at the front of the bump the subthreshold visual input is actually inhibiting the bump. Also note that the bump in the network has a square form, in contrast to the smoother form that would be expected from visual input alone. This is because the learning rule in Equation 12 only converges when HD neurons reach saturation (see also panel A2). (C) Histogram of entrained velocities.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/69841/elife-69841-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** After learning, the synaptic connections in Figure 3A and B have been perturbed with Gaussian noise with standard deviation ∼1.5. (A), (B) Synaptic weight matrices after noise addition. (C) Example of PI. The activity of HD, L-HR, and R-HR neurons along with the PI error and instantaneous angular velocity are displayed, as in Figure 2A. (D) Temporal evolution of distribution of PI errors during PI in darkness. Compared to Figure 2B the distribution widens faster, and also exhibits side bias. (E) PI is impaired compared to Figure 2C, particularly for small angular velocities. Note that the exact form of the PI gain curve at very small angular velocities may vary slightly depending on the noise realization, but the findings mentioned in the Results (middle part of last paragraph of section ‘Learning results in synaptic connectivity that matches the one in the fly’) remain consistent.

First, we discuss the properties of the learned weights. Local excitatory connections have developed along the main diagonal of $W^{rec}$, similar to what is observed in the CX (Turner-Evans et al., 2020). This local excitation can be readily seen in the weight profile of $W^{rec}$ in Figure 3C, and it is the substrate that allows the network to support stable activity bumps in virtually any location. In addition, we observe inhibition surrounding the local excitatory profile in both directions. This inhibition emerges despite the fact that we provide global inhibition to all HD cells ($I_{i⁢n⁢h}^{HD}$ parameter, Materials and methods), in line with suggestions from previous work (Kim et al., 2017). Surrounding inhibition was a feature we observed consistently in learned networks of different sizes and for different global inhibition levels. Finally, the angular offset of the two negative sidelobes in the connectivity depends on the size and shape of the entrained HD bump (for details, see Appendix 5).

Furthermore, we find a consistent pattern of both L-HR and R-HR populations to excite the direction for which they are selective (Figure 3C), which is also similar to what is observed in the CX (Turner-Evans et al., 2020). Excitation in one direction is accompanied by inhibition in the reverse direction in the learned network. As a result of the symmetry in our learning paradigm, the connectivity profiles of L-HR and R-HR cells are mirrored versions of each other, which is also clearly visible in Figure 3C. The inhibition of the reverse direction has a width comparable to the bump size and acts as a ‘break’ to prevent the bump from moving in this direction. The excitation in the selective direction, on the other hand, has a wider profile, which allows the network to path integrate for a wide range of angular velocities, that is for high angular velocities neurons further downstream can be ‘primed’ and activated in rapid succession. Indeed, when we remove the wide projections from the excitatory connectivity, PI performance is impaired for the higher angular velocities exclusively (Figure 3—figure supplement 1). The even weight profile in $W^{rec}$ and the mirror symmetry for L-HR vs. R-HR profiles in $W^{HR}$, together with the circular symmetry of the weights throughout the ring, guarantee that there is no side bias (i.e. tendency of the bump to favor one direction of movement versus the other) during PI. Indeed, the PI error distribution in Figure 2B remains symmetric throughout the 60 s simulations.

Next, we focus our attention on the dynamics of learning. For training times larger than a few hours, the absolute learning error drops and settles to a low value, indicating that learning has converged after ∼20 hr (or 4000 cycles, each cycle lasting $1/η$) of training time (Figure 3D). The non-zero value of the final error is only due to errors occurring at the edges of the bump (Figure 3—figure supplement 2A, top panel). An intuitive explanation of why these errors persist is that the velocity pathway is learning to predict the visual input; as a result, when the visual input is present, the velocity pathway creates errors that are consistent with PI velocity biases in darkness.

Figure 3E and F shows the weight development history for the entire simulation. The first structure that emerges during learning is the local excitatory recurrent connections in $W^{rec}$. For these early stages of learning, the initial connectivity is controlled by the autocorrelation of the visual input, which gets imprinted in the recurrent connections by means of Hebbian co-activation of adjacent HD neurons. As a result, the width of the local excitatory profile mirrors the width of the visual input. Once a clear bump is established in the HD ring, the HR connections are learned to support bump movement, and negative sidelobes in $W^{rec}$ emerge. To understand the shape of the learned connectivity profiles and the dynamics of their development, we study a reduced version of the full model, which follows learning in bump-centric coordinates (see Appendix 5). The reduced model produces a connectivity strikingly similar to the full model, and highlights the important role of non-linearities in the system.

So far, we have shown results in which our model far outperforms flies in terms of PI accuracy. To bridge this gap, we add noise to the weight connectivity in Figure 3A and B and obtain the connectivity matrices in Figure 3—figure supplement 3A,B, respectively. This perturbation of the weights could account for irregularities in the fly HD system owning to biological factors such as uneven synaptic densities. The resulting neural velocity gain curve in Figure 3—figure supplement 3E is impaired mainly for small angular velocities (Figure 2C). Interestingly, it now bears greater similarity to the one observed in flies, because the previously flat area for small angular velocities is wider (flat for $|v|<60$ deg/s, cf. extended data fig. 7G,J in Seelig and Jayaraman, 2015). This happens because the noisy connectivity is less effective in initiating bump movement. Finally, the PI errors in the network with noisy connectivity grow much faster and display a strong side bias (Figure 3—figure supplement 3D, Figure 2B). The latter can be attributed to the fact that the noise in the connectivity generates local minima that are easier to transverse from one direction vs. the other. Side bias can also emerge if the learning rate $η$ in Equation 16 is increased, effectively forcing learning to converge faster to a local minimum, which results in slight deviations from circularly symmetric connectivity (data not shown). It is therefore expected that different animals will display different degrees and directions of side bias during PI, owning either to fast learning or asymmetries in the underlying neurobiology. Since the exact behavior of the network with noise in the connectivity depends on the specific realization, we also generate multiple such networks and estimate the diffusion coefficient during path integration, which quantifies how fast the width of the PI error distribution in Figure 3—figure supplement 3D increases. We find the grand average to be $82.3\pm15.7⁢deg^{2}/s$, which is considerably larger (Student’s t-test, 95% conf. intervals for a total of 12 networks) than the diffusion coefficient for networks without a perturbation in the weights ($24.5⁢deg^{2}/s$ in Figure 2B). Finally, in Appendix 1 we also incorporate random Gaussian noise to all inputs, which can account for noisy percepts or stochasticity of spiking, and show that learning is not disrupted even for high noise levels.

### Fast adaptation of neural velocity gain

Having shown how PI and CAN properties are learned in our model, we now turn our attention to the flexibility that our learning setup affords. Motivated by augmented-reality experiments in rodents where the relative gain of visual and self-motion inputs is manipulated (Jayakumar et al., 2019), we test whether our network can rewire to learn an arbitrary gain between the two. In other words, we attempt to learn an arbitrary gain $g$ between the idiothetic angular velocity $v$ sensed by the HR cells and the neural velocity $g⋅v$ dictated by the allothetic visual input. This simulates the conditions in an augmented reality environment, where the speed at which the world around the animal rotates is determined by the experimenter, but the proprioceptive sense of head angular velocity remains the same.

Starting with the learned network shown in Figure 3, which displayed gain $g=1$, we suddenly switch to a different gain, that is we learn weights for $g\in{0.25,0.5,1.5,2}$. In all cases, we observe that the network readily rewires to achieve the new gain. The mean learning error after the gain switch is initially high, but reaches a lower, constant level after at most 3 hr of training (Figure 4A). We note that convergence is much faster compared to the time it takes for the gain-1 network to emerge from scratch (compare to Figure 3D), especially for the smaller gain changes. Importantly, Figure 4B shows that PI performance in the resulting networks is excellent for the new gains, with some degradation only for very low and very high angular velocities. There are two reasons why high angular velocities are not learned that well: limited training of these velocities, and saturation of HR cell activity. Both reasons are by design and do not reflect a fundamental limit of the network.

![Figure 4.](https://cdn.elifesciences.org/articles/69841/elife-69841-fig4-v2.jpg)

**Figure 4.:** Starting from the converged network in Figure 3, we change the gain $g$ between visual and self-motion inputs, akin to experiments conducted in VR in flies and rodents (Seelig and Jayaraman, 2015; Jayakumar et al., 2019). (A) The mean learning error averaged across 12 simulations for each gain. After an initial increase due to the change of gain, the errors decrease rapidly and settle to a lower value. The steady-state values depend on the gain due to the by-design impairment of high angular velocities, which affects high gains preferentially. Crucially, adaptation to a new gain is much faster than learning the HD system from scratch (Figure 3D). (B) Velocity gain curves for different gains. The network has remapped to learn accurate PI with different gains for the entire dynamic range of head angular velocity inputs (approx. [-500, 500] deg/s). (C), (D) Final profiles of $W^{rec}$ and $W^{HR}$, respectively, for different gains.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/69841/elife-69841-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Normalized root mean square error (NRMSE) between neural and head angular velocity, for gain-1 networks that subsequently have been rewired to learn different gains. To compute the NRMSE, we first estimate from PI performance plots (examples in (B), (C), and (D)) the root mean square error (RMSE) between the neural and head angular velocity, but only within the range of head angular velocities that each network can handle. This range is restricted because there is a maximum neural angular velocity $v_{m⁢a⁢x}$ (e.g. blue dot-dashed line in C; see also Appendix 1—figure 1A); thus the range of head angular velocity is given by this maximum neural angular velocity divided by the gain $g$. Then, to obtain the NRMSE we divide the RMSE by that range. For instance, in (C), $g=10$ and $v_{m⁢a⁢x}=1150$ deg/s. Then the head angular velocity range we test is determined by the x-coordinate for which the Gain-10 line (gray, dashed) meets the neural velocity limit line (blue, dot-dash); hence in this extreme example we only test for the range [-115, 115] deg/s. We find that rewiring performance is excellent for gains $g$ between 0.25 and 4.5, for which NRMSE is less than 0.15. Note that the more a new gain differs from original gain 1, the longer it takes for the network to rewire. (B), (C) PI performance plots for a small ($g=0.125$) and a large ($g=10$) gain. The NRMSE is 0.31 and 0.46, respectively. Performance is impaired because the flat area for small angular velocities gets enlarged in (B), whereas the network struggles to keep up with the desired gain in (C). (D) PI performance plot for a network that has been instructed to reverse its gain (from +1 to -1), i.e. when the visual and self-motion inputs are signaling movement in opposite directions. Performance is excellent, indicating that there is nothing special about negative gains; albeit learning takes considerably more time. (E), (F) Weight history for HR-to-HD and for recurrent connections, respectively, for the network trained to reverse its gain. The directionality of the asymmetric HR-to-HD connections in (E) reverses only after ∼20 hours, while the recurrent weights in (F) remain largely unaltered.

In Appendix 2, we show that without the aforementioned limitations the network learns to path-integrate up to an angular velocity limit set by synaptic delays and that the bump width sets a trade-off between location and velocity-integration accuracy in the HD system.

Figure 4C and D compare the weight profiles of the circularly symmetric matrices $W^{rec}$ and $W^{HR}$ resulting from the initial gain $g=1$, with the weight profiles resulting from adaptation to the most extreme gains shown in Figure 4, that is $g\in{0.25,2}$. An increase in gain slightly suppresses the recurrent connections and slightly amplifies the HR-to-HD connections, while a decrease in gain substantially amplifies the recurrent connections and slightly suppresses the HR-to-HD connections. The latter explains why the flat region for small angular velocities in Figure 4B has been extended for $g\in{0.25,0.5}$: it is now harder for small angular velocities to overcome the attractor formed by stronger recurrent weights and move the bump.

Finally, we address the limits of the ability of the network to rewire to new gains (Figure 4—figure supplement 1). We find that after rewiring the performance is excellent for gains between 0.25 and 4.5. The network can even reverse its gain to $g=-1$, that is, when allothetic and idiothetic inputs are signaling movement in opposite directions. However, for larger gain changes, learning takes longer.

## Discussion

The ability of animals to navigate in the absence of external cues is crucial for their survival. Head direction, place, and grid cells provide internal representations of space (Ranck, 1984; Moser et al., 2008) that can persist in darkness and possibly support path integration (PI) (Mizumori and Williams, 1993; Quirk et al., 1990; Hafting et al., 2005). Extensive theoretical work has focused on how the spatial navigation system might rely on continuous attractor networks (CANs) to maintain and update a neural representation of the animal’s current location. Special attention was devoted to models representing orientation, with the ring attractor network being one of the most famous of these models (Amari, 1977; Ben-Yishai et al., 1995; Skaggs et al., 1995; Seung, 1996). So far, modelling of the HD system has been relying on hand-tuned synaptic connectivity (Zhang, 1996; Xie et al., 2002; Turner-Evans et al., 2017; Page et al., 2019) without reference to its origin; or has been relying on synaptic plasticity rules that either did not achieve gain-1 PI (Stringer et al., 2002) or were not biologically plausible (Hahnloser, 2003).

### Summary of findings

Inspired by the recent discovery of a ring attractor network for HD in Drosophila (Seelig and Jayaraman, 2015), we show how a biologically plausible learning rule leads to the emergence of a circuit that achieves gain-1 PI in darkness. The learned network features striking similarities in terms of connectivity to the one experimentally observed in the fly (Turner-Evans et al., 2020), and reproduces experiments on CAN dynamics (Kim et al., 2017) and gain changes between external and self-motion cues in rodents (Jayakumar et al., 2019). Furthermore, an impairment of PI for small angular velocities is observed in the mature network, which is a feature that has been reported in experiments (Seelig and Jayaraman, 2015). Finally, the proposed learning rule can serve to compensate deviations from circular symmetry in the synaptic weight profiles; such deviations are expected in biological systems and — if not compensated — could lead to large PI errors.

The mature circuit displays two properties characteristic of CANs: (1) it can support and actively maintain a local bump of activity at a virtual continuum of locations, and (2) it can move the bump across the network by integrating self-motion cues. Note that we did not explicitly train the network to achieve these CAN properties, but they rather emerged in a self-organized manner.

To achieve gain-1 PI performance, our network must attribute learning errors to the appropriate weights. The learning rule we adopt in Equation 1 is a ‘delta-like’ rule, with a learning error that gates learning in the network, and a Hebbian component that comes in the form of the postsynaptic potential and assigns credit to synapses that are active when errors are large. The learning rule leads to the emergence of both symmetric local connectivity between HD cells (which is required for bump maintenance and stability), and asymmetric connectivity from HR to HD cells (which is required for bump movement in darkness). The first happens because adjacent neurons are co-active due to correlated visual input; the second because only one HR population is predominantly active during rotation: the population that corresponds to the current rotation direction. Crucial to the understanding of the learning dynamics of the model was the development of a reduced model, which follows learning in bump-centric coordinates and is analytically tractable (see Appendix 5). The reduced model can be extended to higher dimensional manifolds (Gardner et al., 2022), and therefore it offers a general framework to study how activity-dependent synaptic plasticity shapes CANs.

### Relation to experimental literature

Our work comes at a time at which the fly HD system receives a lot of attention (Seelig and Jayaraman, 2015; Turner-Evans et al., 2020; Kim et al., 2017; Kim et al., 2019; Fisher et al., 2019), and suggests a mechanism of how this circuit could self-organize during development. Synaptic plasticity has been shown to be important in this circuit for anchoring the visual input to the HD neurons when the animal is exposed to a new environment (Kim et al., 2019; Fisher et al., 2019). This has also been demonstrated in models of the mammalian HD system (Skaggs et al., 1995; Zhang, 1996; Song and Wang, 2005). Here, we assume that an initial anchoring of the topographic visual input to the HD neurons with arbitrary offset with respect to external landmarks already exists prior to the development of the PI circuit; such an anchoring could even be prewired. In our model, it is sufficient that the visual input tuning is local and topographically arranged. Once the PI circuit has developed, visual connections could be anchored to different environments, as shown by Kim et al., 2019 and Fisher et al., 2019. Alternatively, the HD system itself could come prewired with an initial gross connectivity, sufficient to anchor the visual input; in this case, our learning rule would enable fine tuning of this connectivity for gain-1 PI. In either case, for the sake of simplicity and without loss of generality, we study the development of the path-integrating circuit while the animal moves in the same environment, and keep the visual input tuning fixed. Therefore, the present work addresses the important question of how the PI circuit itself could be formed, and it is complementary to the problem of how allothetic inputs to the PI circuit are wired (Fisher et al., 2019; Kim et al., 2019). The interplay of the two forms of plasticity during development would be of particular future interest.

A requirement for the learning rule we use is that information about the firing rate of HD neurons is available at the axon-distal compartment. There is no evidence for active backpropagation of APs in E-PG neurons in the fly, but passive backpropagation would suffice in this setting. In fact, passive spread of activity has been shown to attenuate weakly in central fly neurons (Gouwens and Wilson, 2009). In HD neurons, the axon-proximal and axon-distal compartments belong to the same dendritic tuft (Figure 1E), and since we assume that the axon initial segment is close to the axon-proximal compartment, the generated AP would need to propagate only a short distance compared to the effective electrotonic length. This means that APs would not be attenuated much on their way from the axon initial segment to the axon-distal compartment, and thus would maintain some of their high-frequency component, which could be used at synapses to differentiate them from slower postsynaptic potentials.

In Figure 4, we show that our network can adapt to altered gains much faster than the time required to learn the network from scratch. Our simulations are akin to experiments where rodents are placed in a VR environment and the relative gain between visual and proprioceptive signals is altered by the experimenter (Jayakumar et al., 2019). In this scenario, Jayakumar et al., 2019 found that the PI gain of place cells can be recalibrated rapidly. In contrast, Seelig and Jayaraman, 2015 found that PI gain in darkness is not significantly affected when flies are exposed to different gains in light conditions. We note, however, that Seelig and Jayaraman, 2015 tested mature animals (8–11 days old), whereas plasticity in the main HD network is presumably stronger in younger animals. Also note that the manipulation we use to address adaptation of PI to different gains differs from the one in Kim et al., 2019 who used optogenetic stimulation of the HD network combined with rotation of the visual scene to trigger a remapping of the visual input to the HD cells in a Hebbian manner. The findings in Jayakumar et al., 2019 can only be reconciled by plasticity in the PI circuit, and not in the sensory inputs to the circuit.

In order to address the core mechanisms that underlie the emergence of a path integrating network, we use a model that is a simplified version of the biological circuit. For example, we did not model inhibitory neurons explicitly and omitted some of the recurrent connectivity in the circuit, whose functional role is uncertain (Turner-Evans et al., 2020). We also choose to separate PI from other complex processes that occur in the CX (Raccuglia et al., 2019). Finally, we do not force the network to obey Dale’s law and do not model spiking explicitly.

Nevertheless, after learning, we obtain a network connectivity that is strikingly similar to the one of the fly HD system. Indeed, the mature model exhibits local excitatory connectivity in the HD neurons (Figure 3A and C), which in the fly is mediated by the excitatory loop from E-PG to P-EG to P-EN2 and back to E-PG (Turner-Evans et al., 2020), a feature that hand-tuned models of the fly HD system did not include (Turner-Evans et al., 2017). Furthermore, the HR neurons have excitatory projections towards the directions they are selective for (Figure 3B and C), similar to P-EN1 neurons in the fly. Interestingly, these key features that we uncover from learning have been utilized in other hand-tuned models of the system (Turner-Evans et al., 2017; Kim et al., 2017; Kim et al., 2019). Future work could endeavor to come closer to the architecture of the fly HD system and benefit from the incorporation of more neuron types and the richness of recurrent connectivity that has been discovered in the fly (Turner-Evans et al., 2020).

Compared to the fly, our network achieved better PI performance. As a simple way to match the performances, we added noise to the learned connectivity in the model; however, this is not an explanation why the fly performs worse. Indeed, there could be multiple reasons why PI performance is worse in the biological circuit. For instance, a confounder that would affect performance but not necessarily learning could be the presence of inputs that are unrelated to path integration, for example, inputs related to circadian cycles and sleep (Raccuglia et al., 2019). In the presence of such confounders, a precise tuning of the weights might be crucial in order to reach the performance of the fly. In other words, only if the model outperforms the biological circuit in a simplified setting, it has a chance to perform as well in a realistic setting, with all the additional complexities the latter comes with.

### Relation to theoretical literature

A common problem with CANs is that they require fine tuning: even a slight deviation from the optimal synaptic weight tuning leads to catastrophic drifting (Goldman et al., 2009). A way around this problem is to sacrifice the continuity of the attractor states in favor of a discrete number of stable states that are much more robust to noise or weight perturbations (Kilpatrick et al., 2013). In our network, the small number of HD neurons enables a coarse-grained representation of heading; the network is a CAN only in a quasi-continuous manner, and the number of discrete attractors corresponds to the number of HD neurons. This makes it harder to transition to adjacent attractors, since a ‘barrier’ has to be overcome in the quasi-continuous case (Kilpatrick et al., 2013). The somewhat counter-intuitive conclusion follows that a CAN with more neurons and, as a result, finer angular resolution, will not be as potent in maintaining activity, and diffusion to nearby attractors will be easier since the barrier will be lower. Indeed, we found that doubling the number of neurons produces a CAN that is less robust to noise. Overall, the quasi-continuous and coarse nature of the attractor shields the internal representation of heading against the ever-present biological noise, which would otherwise lead to diffusion of the bump with time. The fact that the network can still path-integrate accurately with this coarse-grained representation of heading is remarkable.

Seminal theoretical work on ring attractors has proven that in order to achieve gain-1 PI, the asymmetric component of the network connectivity (corresponding here to $W^{HR}$) needs to be proportional to the derivative of the symmetric component (corresponding to $W^{rec}$) (Zhang, 1996). However, this result rests on the assumption that asymmetric and symmetric weight profiles are mediated by the same neuronal population, as in the double-ring architecture proposed by Xie et al., 2002 and Hahnloser, 2003, but does not readily apply to the architecture of the fly HD system where HD and HR cells are separate. In our learned network, we find that the HR weight profile is not proportional to the derivative of the recurrent weight profile, therefore this requirement is not necessary for gain-1 PI in our setting. Note that our learning setup can also learn gain-1 PI for a double-ring architecture, which additionally obeys Dale’s law (Vafidis, 2019). Finally, we emphasize that circular symmetry is not a necessary condition for a ring attractor (Darshan and Rivkind, 2021). Rather, symmetry in our model results from the symmetry in the architecture, the symmetrically prewired weights, and the symmetric stimulus space. If any of those were to be relaxed, the resulting network would not be circular symmetric; then, the reduced model analysis that we perform in Appendix 5 would also not be feasible, because local asymmetries in the setup would result in non-local deviations from circular symmetry of the learned weights, which was our main assumption there. Nevertheless, we demonstrated that the full model can handle such asymmetries in the setup and learn accurate PI (see Appendix 3).

Our learning setup, inspired by Urbanczik and Senn, 2014, is similar to the one in Guerguiev et al., 2017 in the sense that both involve compartmentalized neurons that receive ‘target’ signals in a distinct compartment. It differs, however, in the algorithm and learning rule used. Guerguiev et al., 2017 use local gradient descent during a ‘target’ phase, which is separate from a forward propagation phase, akin to forward/backward propagation stages in conventional deep learning. In contrast, we use a modified Hebbian rule, and in our model ‘forward’ computation and learning happen at the same time; time multiplexing, whose origin in the brain is unclear, is not required. Our setting would be more akin to the one in Guerguiev et al., 2017 if an episode of PI in darkness would be required before an episode of learning in light conditions, which does not seem in line with the way animals naturally learn.

Previous theoretical work showed that head direction cells, head rotation cells, and grid cells emerge in neural networks trained for PI (Banino et al., 2018; Cueva and Wei, 2018). These networks were trained with backpropagation, therefore achieving gain-1 PI was not their primary focus; rather, this work elegantly demonstrated that the aforementioned cell types are efficient representations for spatial navigation that could be learned from experience.

### Testable predictions

We devote this section to discussing predictions of our model, and we suggest future experiments in flies and, potentially, other animal models. An obvious prediction of our model is that synaptic plasticity is critical for the development of the PI network for heading, and the lack of a supervisory allothetic sensory input (e.g. visual) during development should disrupt the formation of the PI system. Previous experimental work showed that head direction cells in rat pups displayed mature properties already in their first exploration of the environment outside their nest (Langston et al., 2010), which may seem to contradict our assumption that the PI circuit wires during development; however, directional selectivity of HD cells in the absence of allothetic inputs and PI performance were not tested in this study. In addition, it has been shown that visually impaired flies were not able to learn to accurately estimate the size of their body. This type of learning also requires visual inputs and, upon consolidation, remains stable (Krause et al., 2019).

We also predict that HD neurons have a compartmental structure where idiothetic inputs are separated from allothetic sensory inputs, which initiate action potentials more readily due to being electrotonically closer to the axon initial segment. While we already demonstrate the separation of allothetic and idiothetic inputs to E-PG neurons in the fly EB (Figure 1E, Figure 1—figure supplement 1), our prediction can only be tested with electrophysiological experiments. Another model prediction that can be tested only with electrophysiology is that APs backpropagate from the axon-proximal compartment (at least passively but with little attenuation) to the axon-distal compartment. Then spikes could be separated from postsynaptic potentials locally at the synapse by cellular mechanisms sensitive to the spectral density of the voltage.

Finally, similarly to place cell studies in rodents (Jayakumar et al., 2019), we predict that during development the PI system can adapt to experimenter-defined gain manipulations, and that it can do so faster than the time required for the system to develop from scratch. Therefore, a suggestion from this study would be to repeat in young flies the adaptation experiments by Seelig and Jayaraman, 2015.

### Outlook

The present study adds to the growing literature of potential computational abilities of compartmentalized neurons (Poirazi et al., 2003; Gidon et al., 2020; Payeur et al., 2021). The associative HD neuron used in this study is a coincidence detector, which serves to associate external and internal inputs arriving at different compartments of the cell. Coupled with memory-specific gating of internally generated inputs, coincidence detection has been suggested to be the fundamental mechanism that allows the mammalian cortex to form and update internal knowledge about external contingencies (Doron et al., 2020; Shin et al., 2021). This structured form of learning does not require engineered ‘hints’ during training, and it might be the reason why neural circuits evolved to be so efficient at reasoning about the world, with the mammalian cortex being the pinnacle of this achievement. Here, we demonstrate that learning at the cellular level can predict external inputs (visual information) by associating firing activity with internally generated signals (velocity inputs) during training. This effect is due to the anti-Hebbian component of the learning rule in Equation 12, where the product of postsynaptic axon-distal and presynaptic activity comes with a negative sign. Specifically, it has previously been demonstrated that anti-Hebbian synaptic plasticity can stabilize persistent activity (Xie and Seung, 2000) and perform predictive coding (Bell et al., 1997; Hahnloser, 2003). At the population level, this provides a powerful mechanism to internally produce activity patterns that are identical to the ones induced from an external stimulus. This mechanism can serve as a way to anticipate external events or, as in our case, as a way of ‘filling in’ missing information in the absence of external inputs.

Local, Hebb-like learning rules are considered a weak form of learning, due to their inability to utilize error information in a sophisticated manner. Despite that, we show that local associative learning can be particularly successful in learning appropriate fine-tuned synaptic connectivity, when operating within a cell structured for coincidence detection. Therefore, in learning and reasoning about the environment, our study highlights the importance of inductive biases with developmental origin (e.g. allothetic and idiothetic inputs arrive in different compartments of associative neurons) (Lake et al., 2017).

In conclusion, the present work addresses the age-old question of how to develop a CAN that performs accurate, gain-1 PI in the absence of external sensory cues. We show that this feat can be achieved in a network model of the HD system by means of a biologically plausible learning rule at the cellular level. Even though our network architecture is tailored to the one of the fly CX, the learning setup where idiothetic and allothetic cues are associated at the cellular level is general and can be applied to other PI circuits. Of particular interest is the rodent HD system: despite the lack of evidence for a topographically organized recurrent HD network in rodents, a one-dimensional HD manifold has been extracted in an unsupervised way (Chaudhuri et al., 2019). Therefore, our work lays the path to study the development of ring-like neural manifolds in mammals. Finally, it has recently been shown that grid cells in mammals form a continuous attractor manifold with toroidal topology (Gardner et al., 2022). It would be interesting to see if a similar mechanism underlies the emergence of PI in place and grid cells. Our model can be extended to higher dimensional CAN manifolds and provides a framework to interrogate this assumption.

## Materials and methods

In what follows, we describe our computational model for learning a ring attractor network that accomplishes accurate angular PI. The model described here focuses on the HD system of the fly; however, the proposed computational setup is general and could be applied to other systems. Unless otherwise stated, the simulation parameter values are the ones summarized in Table 1. Simulation results for a given choice of parameters are very consistent across runs, hence most figures are generated from a single simulation run, unless otherwise stated.

**Table 1.**
 Parameter values.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value</th>
      <th>Unit</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NHD</td>
      <td>60</td>
      <td></td>
      <td>Number of head direction (HD) neurons</td>
    </tr>
    <tr>
      <td>NHR</td>
      <td>60</td>
      <td></td>
      <td>Number of head rotation (HR) neurons</td>
    </tr>
    <tr>
      <td>Δ⁢ϕ</td>
      <td>12</td>
      <td>deg</td>
      <td>Angular resolution of network</td>
    </tr>
    <tr>
      <td>τs</td>
      <td>65</td>
      <td>ms</td>
      <td>Synaptic time constant</td>
    </tr>
    <tr>
      <td>Ii⁢n⁢hHD</td>
      <td>-1</td>
      <td></td>
      <td>Global inhibition to HD neurons</td>
    </tr>
    <tr>
      <td>τl</td>
      <td>10</td>
      <td>ms</td>
      <td>Leak time constant of axon-distal compartment of HD neurons</td>
    </tr>
    <tr>
      <td>C</td>
      <td>1</td>
      <td>ms</td>
      <td>Capacitance of axon-proximal compartment of HD neurons</td>
    </tr>
    <tr>
      <td>gL</td>
      <td>1</td>
      <td></td>
      <td>Leak conductance of axon-proximal compartment of HD neurons</td>
    </tr>
    <tr>
      <td>gD</td>
      <td>2</td>
      <td></td>
      <td>Conductance from axon-distal to axon-proximal compartment</td>
    </tr>
    <tr>
      <td>Ie⁢x⁢cHD</td>
      <td>4</td>
      <td></td>
      <td>Excitatory input to axon-proximal compartment in light conditions</td>
    </tr>
    <tr>
      <td>σn</td>
      <td>0</td>
      <td></td>
      <td>Synaptic input noise level</td>
    </tr>
    <tr>
      <td>M</td>
      <td>4</td>
      <td></td>
      <td>Visual input amplitude</td>
    </tr>
    <tr>
      <td>Mstim</td>
      <td>16</td>
      <td></td>
      <td>Optogenetic stimulation amplitude</td>
    </tr>
    <tr>
      <td>σ</td>
      <td>0.15</td>
      <td></td>
      <td>Visual receptive field width</td>
    </tr>
    <tr>
      <td>σstim</td>
      <td>0.25</td>
      <td></td>
      <td>Optogenetic stimulation width</td>
    </tr>
    <tr>
      <td>Iov⁢i⁢s</td>
      <td>-5</td>
      <td></td>
      <td>Visual input baseline</td>
    </tr>
    <tr>
      <td>fm⁢a⁢x</td>
      <td>150</td>
      <td>spikes/s</td>
      <td>Maximum firing rate</td>
    </tr>
    <tr>
      <td>β</td>
      <td>2.5</td>
      <td></td>
      <td>Steepness of activation function</td>
    </tr>
    <tr>
      <td>x1/2</td>
      <td>1</td>
      <td></td>
      <td>Input level for 50% of the maximum firing rate</td>
    </tr>
    <tr>
      <td>Ii⁢n⁢hHR</td>
      <td>-1.5</td>
      <td></td>
      <td>Global inhibition to HR neurons</td>
    </tr>
    <tr>
      <td>k</td>
      <td>1/360</td>
      <td>s/deg</td>
      <td>Constant ratio of velocity input and head angular velocity</td>
    </tr>
    <tr>
      <td>Aa⁢c⁢t⁢i⁢v⁢e</td>
      <td>2</td>
      <td></td>
      <td>Input range for which f has not saturated</td>
    </tr>
    <tr>
      <td>wHD</td>
      <td>13.3¯</td>
      <td>ms</td>
      <td>Constant weight from HD to HR neurons</td>
    </tr>
    <tr>
      <td>τδ</td>
      <td>100</td>
      <td>ms</td>
      <td>Plasticity time constant</td>
    </tr>
    <tr>
      <td>Δ⁢t</td>
      <td>0.5</td>
      <td>ms</td>
      <td>Euler integration step size</td>
    </tr>
    <tr>
      <td>τv</td>
      <td>0.5</td>
      <td>s</td>
      <td>Time constant of velocity decay</td>
    </tr>
    <tr>
      <td>σv</td>
      <td>450</td>
      <td>deg/s</td>
      <td>Standard deviation of angular velocity noise</td>
    </tr>
    <tr>
      <td>η</td>
      <td>0.05</td>
      <td>1 /s</td>
      <td>Learning rate</td>
    </tr>
  </tbody>
</table>

_Parameter values, in the order they appear in the Methods section. These values apply to all simulations, unless otherwise stated. Note that voltages, currents, and conductances are assumed unitless in the text; therefore capacitances have the same units as time constants._

.

### Network architecture

We model a recurrent neural network comprising $N^{HD}=60$ head-direction (HD) and $N^{HR}=60$ head-rotation (HR) cells, which are close to the number of E-PG and P-EN1 cells in the fly central complex (CX), respectively (Turner-Evans et al., 2020; Xu, 2020). A scaled-down version of the network for $N^{HR}=N^{HD}=12$ is shown in Figure 1A. The average spiking activity of HD and HR cells is modelled by firing-rate neurons. HD cells are organized in a ring and receive visual input, which encodes the angular position of the animal’s head with respect to external landmarks. We use a discrete representation of angles and we model two HD cells for each head direction, as observed in the biological system (Turner-Evans et al., 2017). Therefore the network can represent head direction with an angular resolution $Δ⁢ϕ=12⁢deg$.

Motivated by the anatomy of the fly CX (Green et al., 2017; Turner-Evans et al., 2020), HR cells are divided in two populations (Figure 1A): a ‘leftward’ (L-HR) population (with increased velocity input when the head turns leftwards) and a ’rightward’ (R-HR) population (with increased velocity input when the head turns rightwards). After learning, these two HR populations are responsible to move the HD bump in the anticlockwise and clockwise directions, respectively.

The recurrent connections among HD cells and the connections from HR to HD cells are assumed to be plastic. On the contrary, connections from HD to HR cells are assumed fixed and determined as follows: for every head direction, one HD neuron projects to a cell in the L-HR population, and the other to a cell in the R-HR population. Because HD cells project to HR cells in a 1-to-1 manner, each HR neuron is simultaneously tuned to a particular head direction and a particular head rotation direction. The synaptic strength of the HD-to-HR projections is the same for all projections (these restrictions on the HD-to-HR connections are relaxed in Appendix 3). Finally, HR cells do not form recurrent connections.

### Neuronal model

We assume that each HD neuron is a rate-based associative neuron (Figure 1D), that is, a two-compartmental neuron comprising an axon-proximal and an axon-distal dendritic compartment (Urbanczik and Senn, 2014; Brea et al., 2016). The two compartments model the dendrites of that neuron that are closer to or further away from the axon initial segment. Note that here the axon-proximal compartment replaces the somatic compartment in the original model by Urbanczik and Senn, 2014. This is because the somata of fly neurons are typically electrotonically segregated from the rest of the cell and they are assumed to contribute little to computation (Gouwens and Wilson, 2009; Tuthill, 2009). We also note that to fully capture the input/output transformations that HD neurons in the fly perform, more compartments than two might be needed (Xu, 2020). Finally, only HD cells are associative neurons, whereas HR cells are simple rate-based point neurons.

HD cells receive an input current $I^{d}$ to the axon-distal dendrites, which obeys

$$
\tau_{s}⁢\frac{d⁢I^{d}}{d⁢t}=-I^{d}+W^{r⁢e⁢c}⁢r^{HD}+W^{HR}⁢r^{HR}+I_{i⁢n⁢h}^{HD}+\sigma_{n}⁢n^{d}
$$

where $I^{d}$ is a vector of length $N^{HD}$ with each entry corresponding to one HD cell. In Equation 2, $\tau_{s}$ is the synaptic time constant, $W^{rec}$ is a $N^{HD}\timesN^{HD}$ matrix of the recurrent synaptic weights among HD cells, $W^{HR}$ is a $N^{HD}\timesN^{HR}$ matrix of the synaptic weights from HR to HD cells, $r^{HR}$ and $r^{HD}$ are vectors of the firing rates of HR and HD cells respectively, $I_{i⁢n⁢h}^{HD}$ is a constant inhibitory input common to all HD cells, and $n^{d}$ is a random noise input to the axon-distal compartment. $n^{d}$ is drawn IID from $N⁢(0,1)$, and its variance is scaled by $\sigma_{n}^{2}$. Note that in the main text we set $\sigma_{n}$ to zero, but we explore different values for this parameter in Appendix 1. The constant current $I_{i⁢n⁢h}^{HD}$ is in line with a global-inhibition model with local recurrent connectivity, as opposed to having long-range inhibitory recurrent connectivity (Kim et al., 2017). The inhibitory current $I_{i⁢n⁢h}^{HD}$ suppresses HD bumps in general; however the exact strength of this inhibition is not important in our model.

Since several electrophysiological parameters of the fly neurons modeled here are unknown, we use dimensionless conductance values. Therefore, in Equation 2, which describes the dynamics of the axon-distal input of HD cells, currents (e.g. $I^{d}$, $I_{i⁢n⁢h}^{HD}$, and $n^{d}$) are dimensionless. Membrane voltages are also chosen to be dimensionless, and because we measure firing rates in units of 1 /s, all synaptic weights (e.g. $W^{rec}$ and $W^{HR}$) then have, strictly speaking, the unit ‘seconds’ (s), even though we mostly suppress this unit in the text. Importantly, all time constants (e.g. $\tau_{s}$), which define the time scale of dynamics, are measured in units of time (in seconds).

Our model incorporates several time scales, whose interplay is not obvious. To facilitate understanding, we summarize the parameters that define the time scales in Appendix 4—table 1, and discuss their relation in Appendix 4.

The axon-distal voltage $V^{d}$ of HD cells is a low-pass filtered version of the input current $I^{d}$, that is,

$$
\tau_{l}⁢\frac{d⁢V^{d}}{d⁢t}=-V^{d}+I^{d}
$$

where $\tau_{l}$ is the leak time constant of the axon-distal compartment. The voltage $V^{d}$ and the current $I^{d}$ have the same unit (both dimensionless), which means that the leak resistance of the axon-distal compartment is also dimensionless, and we assume that it is unity for simplicity. We choose values of $\tau_{l}$ and $\tau_{s}$ (for specific values, see Table 1) so that their sum matches the phenomenological time constant of HD neurons (E-PG in the fly), while $\tau_{s}$ equals to the phenomenological time constant of HR neurons (P-EN1 in the fly, Turner-Evans et al., 2017). Note that $V^{d}$ is the low-frequency component of the axon-distal voltage originating from postsynaptic potentials, that is excluding occasional high-frequency contributions from backpropagating action potentials.

The axon-proximal voltage $V^{a}$ of HD cells is then given by

$$
C⁢\frac{d⁢V^{a}}{d⁢t}=-g_{L}⁢V^{a}-g_{D}⁢(V^{a}-V^{d})+I^{v⁢i⁢s}+I_{e⁢x⁢c}^{HD}+\sigma_{n}⁢n^{a}
$$

where $C$ is the capacitance of the membrane of the axon-proximal compartment, $g_{L}$ is the leak conductance, $g_{D}$ is the conductance of the coupling from axon-distal to axon-proximal dendrites, $I^{v⁢i⁢s}$ is a vector of visual input currents to the axon-proximal compartment of HD cells, $I_{e⁢x⁢c}^{HD}$ is an excitatory input to the axon-proximal compartment, and $n^{a}$ is a random noise vector injected to the axon-proximal compartment, drawn IID from $N⁢(0,1)$. The excitatory current $I_{e⁢x⁢c}^{HD}$ is assumed to be present only in light conditions. The values of $C$, $g_{L}$, and $g_{D}$ in the fly HD (E-PG) neurons are unknown, thus we keep these parameters unitless, and set their values to the ones in Urbanczik and Senn, 2014. Note that since conductances are dimensionless here, $C$ is effectively a time constant.

Following Hahnloser, 2003, the visual input to the i-th HD cell is a localized bump of activity at angular location $\theta_{i}$:

$$
I_{i}^{v⁢i⁢s}⁢(t)=M⁢exp⁡(-\frac{1}{2⁢\sigma^{2}}⁢sin^{2}⁡(\frac{\theta_{i}+\theta_{0}⁢(t)}{2}))+I_{o}^{v⁢i⁢s}
$$

where $M$ scales the bump’s amplitude, $\sigma$ controls the width of the bump, $\theta_{i}$ is the preferred orientation of the i-th HD neuron , $\theta_{0}⁢(t)$ is the position of a visual landmark at time $t$ in head-centered coordinates, and $I_{o}^{vis}<0$ is a constant inhibitory current that acts as the baseline for the visual input. We choose $M$ so that the visual input can induce a weak bump in the network at the beginning of learning, and we choose $\sigma$ so that the resulting bump after learning is ∼60 deg wide. Note that the bump in the mature network has a square shape (Figure 3—figure supplement 2B); therefore we elect to make it slightly narrower than the average full width at half maximum of the experimentally observed bump (∼80 deg; Seelig and Jayaraman, 2015; Kim et al., 2017; Turner-Evans et al., 2017). In addition, the current $I_{o}^{v⁢i⁢s}$ is negative enough to make the visual input purely inhibitory, as reported (Fisher et al., 2019). The visual input is more inhibitory in the surround to suppress activity outside of the HD receptive field. Therefore, the mechanism in which the visual input acts on the HD neurons is disinhibition.

The firing rate of HD cells, which is set by the voltage in the axon-proximal compartment, is given by

$$
r^{HD}=f⁢(V^{a})
$$

where

$$
f⁢(x)=\frac{f_{m⁢a⁢x}}{1+exp⁡(-\beta⁢(x-x_{1/2}))}
$$

is a sigmoidal activation function applied element-wise to the vector $V^{a}$. The variable $f_{m⁢a⁢x}$ sets the maximum firing rate of the neuron, $\beta$ is the slope of the activation function, and $x_{1/2}$ is the input level at which half of the maximum firing rate is attained. The value of $f_{m⁢a⁢x}$ is arbitrary, while $\beta$ is chosen such that the activation function has sufficient dynamic range, and $x_{1/2}$ is chosen such that for small negative inputs the activation function is non-zero.

We note that the saturation of the activation function $f$ in Equation 7 is an essential feature of our model, especially for the convergence of the plasticity rule in Equation 12; see also the section ‘Synaptic Plasticity Rule’. Even though, to the best of our knowledge, it is currently not known whether E-PG neurons actually reach saturation, other Drosophila neurons are known to reach saturation with increasing inputs, instead of some sort of depolarization block (Wilson, 2013; Brandão et al., 2021). Saturation with increasing inputs may be due to, for instance, short-term synaptic depression: beyond a certain frequency of incoming action potentials, the synaptic input current is almost independent of that frequency (Tsodyks and Markram, 1997; Tsodyks et al., 1998).

The firing rates of the HR cells are given by

$$
r^{HR}=f⁢(W^{HD}⁢r_{LP}^{HD}+I^{v⁢e⁢l}+I_{i⁢n⁢h}^{HR}+\sigma_{n}⁢n^{HR})
$$

where $r^{HR}$ is the vector of length $N^{HR}$ of firing rates of HR cells, the $N^{HR}\timesN^{HD}$ matrix $W^{HD}$ encodes the fixed connections from the HD to the HR cells, $r_{LP}^{HD}$ is a low-pass filtered version of the firing rate of the HD cells where the filter accounts for delays due to synaptic transmission in the incoming synapses from HD cells, $I^{v⁢e⁢l}$ is the angular velocity input, $I_{i⁢n⁢h}^{HR}$ is a constant inhibitory input common to all HR cells, and $n^{HR}$ is a random noise input to the HR cells drawn IID from $N⁢(0,1)$. We set $I_{i⁢n⁢h}^{HR}$ to a value that still allows sufficient activity in the HR cell bump, even when the animal does not move. The low-pass filtered firing-rate vector $r_{LP}^{HD}$ is given by

$$
\tau_{s}⁢\frac{d⁢r_{LP}^{HD}}{d⁢t}=-r_{LP}^{HD}+r^{HD},
$$

and the angular-velocity input to the i-th HR neuron is given by

$$
I_{i}^{vel}(t)=qkv(t)withq={−1for i\leqN^{HR}/21for i>N^{HR}/2
$$

where $k$ is the proportionality constant between head angular velocity and velocity input to the network, $v⁢(t)$ is the head angular velocity at time $t$ in units of deg/s, and the factor $q$ is chosen such that the left (right) half of the HR cells are primarily active during leftward (rightward) head rotation. Note that the same $\tau_{s}$ is in both Equation 2 and Equation 9. Finally, as mentioned earlier, the matrix $W^{HD}$ encodes the hardwired 1-to-1 HD-to-HR connections, i.e., $W_{i⁢j}^{HD}=w^{HD}$ if the j-th HD neuron projects to the i-th HR neuron, and $W_{i⁢j}^{HD}=0$ otherwise. Specifically, for $j$ odd, HD neuron $j$ projects to L-HR neuron $i=\frac{j+1}{2}$, whereas for $j$ even, HD neuron $j$ projects to R-HR neuron $i=30+\frac{j}{2}$. The synaptic strength $w^{HD}$ is chosen such that the range of the firing rates of the HD cells is mapped to the entire range of firing rates of the HR cells. Specifically, we set $w^{HD}=\frac{A_{a⁢c⁢t⁢i⁢v⁢e}}{f_{m⁢a⁢x}}$, where $A_{a⁢c⁢t⁢i⁢v⁢e}$ is the range of inputs for which $f$ has not saturated, i.e., the input values for which $f$ remains between about 7% and 93% of its maximum firing rate $f_{m⁢a⁢x}$ (see Equation 7). Finally, the proportionality constant $k$ is set so that the firing rate of HR neurons does not reach saturation for the range of velocities relevant for the fly (approx. [-500, 500] deg/s), given all other inputs they receive.

### Synaptic plasticity rule

In our network, the associative HD neurons receive direct visual input in the axon-proximal compartment and indirect angular velocity input in the axon-distal compartment through the HR-to-HD connections (Figure 1D). We hypothesize that the visual input acts as a supervisory signal that controls the axon-proximal voltage $V^{a}$ directly, and the latter initiates spikes. Therefore, the goal of learning is for the axon-distal voltage $V^{d}$ to predict the axon-proximal voltage by changing the synaptic weights $W^{rec}$ and $W^{HR}$. This change is achieved by minimizing the difference between the firing rate $f⁢(V^{a})$ in the presence of visual input and the axon-distal prediction $f⁢(V^{s⁢s})$ of the firing rate in the absence of visual input. In the latter case and at steady-state, the voltage $V_{i}^{s⁢s}$ for the i-th HD neuron is an attenuated version of the axon-distal voltage,

$$
V_{i}^{s⁢s}=\frac{g_{D}}{g_{D}+g_{L}}⁢V_{i}^{d},
$$

with conductance $g_{D}$ of the coupling from the axon-distal to axon-proximal dendrites and leak conductance $g_{L}$ of the axon-proximal compartment, as explained in Equation 4, and $p=\frac{g_{D}}{g_{D}+g_{L}}$ in Equation 1. Therefore, following Urbanczik and Senn, 2014, we define the plasticity-induction variable $PI_{i⁢j}$ for the connection between the j-th presynaptic neuron and i-th postsynaptic neuron as

$$
PI_{i⁢j}=[f⁢(V_{i}^{a})-f⁢(V_{i}^{s⁢s})]⁢P_{j}
$$

where $P_{j}$ is the postsynaptic potential of neuron $j$, which is a low-pass filtered version of the presynaptic firing rate rj. That is,

$$
P_{j}⁢(t)=H⁢(t)∗r_{j}⁢(t)
$$

where * denotes convolution. The transfer function

$$
H⁢(t)=\frac{1}{\tau_{l}-\tau_{s}}⁢[exp⁡(-\frac{t}{\tau_{l}})-exp⁡(-\frac{t}{\tau_{s}})]⁢u⁢(t)
$$

is derived from the filtering dynamics in Equation 2 and Equation 3 and accounts for the delays introduced by the synaptic time constant $\tau_{s}$ and the leak time constant $\tau_{l}$. In Equation 14, $u⁢(t)$ denotes the Heaviside step function, that is, $u⁢(t)=1$ for $t>0$ and $u⁢(t)=0$ otherwise. The plasticity-induction variable is then low-pass filtered to account for slow learning dynamics,

$$
\tau_{\delta}⁢\frac{d⁢\delta_{i⁢j}}{d⁢t}=-\delta_{i⁢j}+PI_{i⁢j},
$$

and the final weight change is given by

$$
\frac{d⁢W_{i⁢j}}{d⁢t}=η⁢\delta_{i⁢j}
$$

where $η$ is the learning rate and $W_{i⁢j}$ is the connection weight from the j-th presynaptic neuron to the i-th postsynaptic neuron. Note that the synaptic weight $W_{i⁢j}$ is an element of either the matrix $W^{rec}$ or the matrix $W^{HR}$ depending on whether the presynaptic neuron $j$ is an HD or an HR neuron, respectively. The value of the plasticity time constant $\tau_{\delta}$ is not known, therefore we adopt the value suggested by Urbanczik and Senn, 2014.

Equation 12 is a ‘delta-like’ rule that can be interpreted as an extension of the Hebbian rule; compared to a generic Hebbian rule, we have replaced the postsynaptic firing rate $f⁢(V_{i}^{a})$ by the difference between $f⁢(V_{i}^{a})$ and the predicted firing rate $f⁢(V_{i}^{s⁢s})$ of the axon-distal compartment of the postsynaptic neuron. This difference drives plasticity in the model. We note that $f⁢(V_{i}^{a})$ is a continuous approximation of the spike train of the postsynaptic neuron, which could be available at the axon-distal compartment via back-propagating action potentials (Larkum, 2013). Furthermore, the axon-distal voltage $V_{i}^{d}$ and postsynaptic potentials are by definition available at the synapses arriving at the axon-distal compartment. Note that even though $f⁢(V_{i}^{s⁢s})$ is the firing rate in the absence of visual input, it can still be computed at the axon-distal compartment when the visual input is available; $V_{i}^{d}$ is the local voltage and therefore only a constant multiplicative factor (Equation 11) and the static nonlinearity $f$ need to be computed to obtain $f⁢(V_{i}^{s⁢s})$. Therefore, the learning rule is biologically plausible because all information is locally available at the synapse.

The learning rule used here differs from the one in the original work of Urbanczik and Senn, 2014 because we utilize a rate-based version instead of the original spike-based version. Even though spike trains can introduce Poisson noise to $f⁢(V_{i}^{a})$, Urbanczik and Senn, 2014 show that once learning has converged, asymmetries in the weights due the spiking noise are on average canceled out.

Another difference in our learning setup is that, unlike in Urbanczik and Senn, 2014, the input to the axon-proximal compartment does not reach zero in equilibrium (see, e.g. Figure 3D, and Appendix 5). Therefore, an activation function with a saturating non-linearity, as in Equation 7, is crucial for convergence, which could not be achieved with a less biologically plausible threshold-linear activation function. This lack of strict convergence in our setup is responsible for the square form of the bump (Figure 3—figure supplement 2B and Appendix 5).

### Training protocol

We train the network with synthetically generated angular velocities, simulating head turns of the animal. $W^{rec}$ and $W^{HR}$ are both initialized with random connectivity drawn from a normal distribution with mean 0 and standard deviation $1/\sqrt{N^{HD}}$, as common practise in the modeling literature. In further simulations with various other initial conditions (e.g. in the simulations with gain changes in Figure 4 or in simulations in which we randomly shuffled weights after learning, not shown), we confirmed that the final PI performance is virtually independent of the initial distribution of weights $W^{rec}$ and $W^{HR}$.

The network dynamics are updated in discrete time steps $Δ⁢t$ using forward Euler integration. The entrained angular velocities cover the range of angular velocities exhibited by the fly, which are at maximum ∼500 deg/s during walking or flying (Geurten et al., 2014; Stowers et al., 2017). The angular velocity $v⁢(t)$ is modeled as an Ornstein-Uhlenbeck process given by

$$
v(t+Δt)=(1−\alpha)v(t)+\sigma_{v}\sqrt{Δt}n(t)
$$

where $\alpha=Δ⁢t/\tau_{v}$ and $\tau_{v}$ is the time constant with which $v⁢(t)$ decays to zero, $n⁢(t)$ is noise drawn from a normal distribution with mean 0 and standard deviation 1 at each time step, and $\sigma_{v}$ scales the noise strength.

We pick $\sigma_{v}$ and $\tau_{v}$ so that the resulting angular velocity distribution in Figure 3—figure supplement 2C and its time course, for example in Figure 2A, are similar to what has been reported in flies during walking or flying (Geurten et al., 2014; Stowers et al., 2017). Finally, note that we train the network for angular velocities a little larger than what flies typically display (up to ±720 deg/s).

### Quantification of the mean learning error

In Equation 12 we have used the learning error

$$
E_{i}=f⁢(V_{i}^{a})-f⁢(V_{i}^{s⁢s})
$$

which controls learning in the i-th associative HD neuron. To quantify the mean learning error $err⁢(t)$ in the whole network at time $t$, we average $E_{i}$ across all HD neurons and across a small time interval $[t,t+t_{w}]$, that is,

$$
err⁢(t)=\frac{1}{t_{w}⁢N^{HD}}⁢\sumi=1N^{HD}\int_{t}^{t+t_{w}}|E_{i}⁢(\tau)|⁢d\tau
$$

with $t_{w}=10$ s. In Figure 3D, we plot this mean error at every 1% of the simulation, for 12 simulations, and averaged across the ensemble of the simulations. Note that individual simulations occasionally display ‘spikes’ in the error. Large errors occur if the network happens to be driven by very high velocities that the network does not learn very well because they are rare; larger errors also occur for very small velocities, that is, when the velocity input is not strong enough to overcome the local attractor dynamics, as seen, for example, in Figure 2C. On average, though, we can clearly see that the mean learning error decreases with increasing time and settles to a small value (e.g. Figure 3D and Figure 4A).

### Population vector average

To decode from the activity of HD neurons an average HD encoded by the network, we use the population vector average (PVA). We thus first convert the tuning direction $\theta_{i}$ of the i-th HD neuron to the corresponding complex number $e^{j⁢\theta_{i}}$ on the unitary circle, where $j$ is the imaginary unit. This complex number is multiplied by the firing rate $r_{i}^{HD}$ of the i-th HD neuron, and then averaged across neurons to yield the PVA

$$
r_{a⁢v}=\frac{1}{N^{HD}}⁢\sumi=1N^{HD}r_{i}^{HD}⁢e^{j⁢\theta_{i}}.
$$

The PVA is a vector in the 2-D complex plane and points to the center of mass of activity in the HD network. Finally, we take the angle $\theta$ of the PVA as a measure for the current heading direction represented by the network.

### Diffusion coefficient

To quantify the variability of heading direction in the trained networks, we define the diffusion coefficient $D$ as:

$$
D=\frac{⟨Δ⁢\theta^{2}⟩-⟨Δ⁢\theta⟩^{2}}{t_{sim}}
$$

where $Δ⁢\theta$ is the change in heading direction in a time interval $t_{sim}$. Therefore, $D$ is given by the variance of the distribution of displacements in a given time interval, divided by the time interval.

In the main text, we estimate $D$ during PI, i.e. with velocity inputs only. In this setting, $D$ is the rate at which the variance of the PI errors increases (see e.g. Figure 2B). Deviations from gain-1 PI contribute to this estimate; hence, to single out the effects of noise during training on the stability of the learned attractor in Appendix 1, we also estimate $D$ in the presence of test noise when no inputs are received at all.

### Fly connectome analysis

Our model assumes the segregation of visual inputs to HD (E-PG) cells from head rotation and recurrent inputs to the same cells. To test this hypothesis, we leverage on the fly hemibrain connectome (Xu, 2020; Clements et al., 2020). First, we randomly choose one E-PG neuron per wedge of the EB, for a total of 16 E-PG neurons. We reasoned this sample would be sufficient because the way E-PG neurons in the same wedge are innervated is expected to be similar. We then find all incoming connections to these neurons from visually responsive ring neurons R2 and R4d (Omoto et al., 2017; Fisher et al., 2019). These are the connections that arrive at the axon-proximal compartment in our model. We then find all incoming connections from P-EN1 cells, which correspond to the HR neurons, and from P-EN2 cells, which are involved in a recurrent excitatory loop from E-PG to P-EG to P-EN2 and back to E-PG (Turner-Evans et al., 2020). These are the connections that arrive at the axon-distal compartment in our model.

To further support the assumption that visual inputs are separated from recurrent and HR-to-HD inputs in the Drosophila EB, we perform binary classification between the two classes (R2 and R4d vs. P-EN1 and P-EN2). We use SVMs with Gaussian kernel, and perform nested 5-fold cross validation, for a total of 30 model runs for every neuron tested (Figure 1—figure supplement 1).

### Quantification of PI performance

To quantify PI performance of the network and compare to fly performance, we use the measure defined by Seelig and Jayaraman, 2015 and estimate the correlation coefficient between the unwrapped PVA and true heading in darkness. We estimate the correlation in 140 s long trials and report the point estimate and 95% confidence intervals (Student’s t-test, $N=100$).

### Resource availability

All code used in this work is available at https://github.com/panvaf/LearnPI (copy archived at swh:1:rev:c6e354f80bf435114e577af70892db41c3ce5315, Vafidis, 2022). The files required to reproduce the figures can be found at https://gin.g-node.org/pavaf/LearnPI.
