# Theta-modulation drives the emergence of connectivity patterns underlying replay in a network model of place cells

## Authors

- Panagiota Theodoni<sup>1</sup>
- Bernat Rovira<sup>1</sup>
- Yingxue Wang<sup>5</sup>
- Alex Roxin<sup>1</sup> ([ORCID: 0000-0003-1015-8138](https://orcid.org/0000-0003-1015-8138)) †

### Affiliations

1. Centre de Recerca Matemàtica Bellaterra Spain
2. New York University Shanghai Shanghai China
3. NYU-ECNU Institute of Brain and Cognitive Science at NYU Shanghai Shanghai China
4. Department of Information and Communication Technologies Universitat Pompeu Fabra Barcelona Spain
5. Max Planck Florida Institute for Neuroscience Jupiter United States
6. Barcelona Graduate School of Mathematics Barcelona Spain

† Corresponding author

## Abstract

Place cells of the rodent hippocampus fire action potentials when the animal traverses a particular spatial location in any environment. Therefore for any given trajectory one observes a repeatable sequence of place cell activations. When the animal is quiescent or sleeping, one can observe similar sequences of activation known as replay, which underlie the process of memory consolidation. However, it remains unclear how replay is generated. Here we show how a temporally asymmetric plasticity rule during spatial exploration gives rise to spontaneous replay in a model network by shaping the recurrent connectivity to reflect the topology of the learned environment. Crucially, the rate of this encoding is strongly modulated by ongoing rhythms. Oscillations in the theta range optimize learning by generating repeated pre-post pairings on a time-scale commensurate with the window for plasticity, while lower and higher frequencies generate learning rates which are lower by orders of magnitude.

## Introduction

As an animal explores in any given environment, place cells in the hippocampus fire selectively at particular locations (O'Keefe and Dostrovsky, 1971; O'Keefe and O’Keefe, 1976; Harvey et al., 2009), known as the ‘place-fields’ of the cells. Furthermore, the place fields of an ensemble of place cells remap to completely new positions with respect to one another if the animal enters a distinct environment (Muller and Kubie, 1987; Kubie and Muller, 1991; Bostock et al., 1991). Sequential place cell activation during exploration therefore acts as a unique fingerprint for each environment, providing information needed for navigation and spatial learning. The spontaneous replay of such sequential activation, which occurs within sharp-wave/ripples (SWRs) during quiet wakefulness (Foster and Wilson, 2006; Karlsson and Frank, 2009; Carr et al., 2011) and sleep (Wilson and McNaughton, 1994; Lee and Wilson, 2002) suggests that the animal has formed an internal representation of the corresponding environment, presumably during exploration (Wu and Foster, 2014). Synaptic plasticity is the clear candidate mechanism for this formation. Nonetheless it remains unclear how changes in the synaptic connectivity are coordinated at the network level in order to generate well-ordered sequences spontaneously. An additional prominent physiological signature of exploratory behavior in the hippocampus is the theta rhythm (4–12 Hz). Decreases in theta power due to lesions of the medial septum strongly reduce performance in spatial-memory based tasks (Winson, 1978; Mitchell et al., 1982; Dwyer et al., 2007) and other hippocampal dependent tasks (Berry and Thompson, 1979; Allen et al., 2002) although they do not eliminate place fields on linear tracks (Brandon et al., 2014; Wang et al., 2015). Despite this, lesioned animals can still reach fixed performance criteria given enough time (Winson, 1978; Berry and Thompson, 1979). This shows not only that theta is important for learning, but also suggests a potential mechanism. Namely, it may act as a dial for the learning rate, presumably by modulating the network-wide coordination of synaptic plasticity. How this occurs is unknown. Here, we develop a model that explains how synaptic plasticity shapes the patterns of synaptic connectivity in a strongly recurrent hippocampal circuit, such as CA3, as an animal explores a novel environment. We show that a temporally asymmetric spike-timing dependent plasticity (STDP) rule (Markram et al., 1997; Bi and Poo, 1998) during motion-driven sequential place-cell activity leads to the formation of network structure capable of supporting spontaneous bursts. These bursts occur in the absence of place-field input, that is during awake-quiescence or sleep. Importantly, the spatio-temporal structure of the bursts undergoes a sharp transition during exploration, exhibiting well-ordered replay only after a critical time of exploration in the novel environment. The underlying rate of this plasticity process, and hence the critical time, is strongly modulated through external oscillatory drive: for very low and high frequency the rate is near zero, while for an intermediate range, set by the time-scale of the plasticity rule, it is higher by several orders of magnitude, allowing for learning on realistic time-scales. Our theoretical findings lend support to the hypothesis that the theta rhythm accelerates learning by modulating place-cell activity on a time-scale commensurate with the window for plasticity. This maximizes the growth rate of network-wide patterns of synaptic connectivity which drive spontaneous replay. Finally, we confirm a main prediction from the model using simultaneous recordings of hippocampal place cells from a rat exploring a novel track. Namely, pairwise correlations between cells with neighboring place fields show a pronounced increase over the span of several minutes at the outset of exploration. Furthermore, in a rat in which the medial septum is partially inactivated via muscimol injection, which strongly reduces theta modulation, this increase is not seen.

## Results

### Plasticity during exploration of a novel environment leads to a transition in the structure of sharp-wave events

We modeled the dynamics of hippocampal place cells in a strongly recurrent circuit, such as area CA3, as an animal sequentially explored a series of distinct novel ring-like tracks, Figure 1a. The model consisted of recurrently coupled, excitatory stochastic firing rate neurons, each of which received a place-specific external input on any given track, and inhibition was modeled as a global inhibitory feedback, see Materials and methods for model details. To model the global remapping of place fields from one track to another, we randomized the position of the peak input, and as a consequence the place field, of each neuron. In this way, the ordering of cells according to their place field location on one track was random and uncorrelated with their ordering on any other track, see Figure 1b.

![Figure 1.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig1-v2.jpg)

**Figure 1.:** (a) We model the sequential exploration of a number of distinct linear tracks. (b) The network consists of N place cells. The ordering of the place fields is randomly remapped on each track. Therefore, if the cells are properly ordered in any given environment the place field input is represented by a spatially localized bump of activity (upper left and lower right). Sequential activity on a familiar track would look random given an ordering on a novel track, and vice versa (upper right and lower left respectively).

We were interested in knowing how the exploration of a novel environment affected the pattern of synaptic connectivity between place cells via a temporally asymmetric plasticity rule, and how this in turn shaped the activity. While the plasticity rule we use is formally referred to as 'Spike-timing dependent’ (Kempter et al., 1999; Song et al., 2000; Pfister and Gerstner, 2006), our model neurons generate spikes stochastically as Poisson processes. Therefore the exact spike timing itself does not play any role but rather only the time variations in the underlying firing rate. Recent theoretical work has shown that the plasticity induced by a number of plasticity rules, including heuristic STDP rules, is in fact dominated by such firing rate variations when irregular, in-vivo like activity is considered (Graupner et al., 2016). We also considered a ‘balanced’ plasticity rule, for which the degree of potentiation and depression were the same, on average, given constant firing rates. Such a rule is a means of avoiding fully potentiating or fully depressing all synapses on long time-scales, that is it allows for the generation and maintenance of structured synaptic connectivity. Alternatively, we could have considered an unbalanced plasticity rule with additional stabilizing mechanisms (Zenke et al., 2015).

In order to study ‘typical’ place-cell dynamics during exploration we first exposed the network to a series of distinct tracks until the matrix of recurrent synaptic weights no longer depended on its initial state. When the trajectory and velocity of the virtual animal was stochastic and distinct on different tracks, the resulting evolution of the synaptic weights also exhibited some variability from track to track, see Figure 2—figure supplement 1. In simulations with constant velocity this variability largely vanished, see Figure 2—figure supplement 2a. After exploring 10 tracks, we exposed the network to another novel track and studied the dynamics in detail; because the exploration process had already become largely stereotyped (despite some variability), the dynamics on the novel track reflected what would be seen qualitatively during the exploration of any other novel track in the future, that is it was dependent only on the learning process itself and not the initial state of the synaptic weight matrix.

In our simulations, we modeled the movement of a virtual animal around the track by varying the external inputs to place cells. Specifically, the external input was maximal for cells with place fields at the animal’s current position and minimal for cells with place fields at the opposite side of the track, with the input decaying smoothly for intermediate locations like a cosine curve, see Materials and methods for details. We modeled the motion of the animal by taking the velocity to be an Ornstein-Uhlenbeck process with a time constant of 10 s; this lead to realistic trajectories with changes of direction, see Figure 2—figure supplement 3. (We will use the metaphor of a virtual animal for conceptual ease, although we really mean that we moved the bump-like external input to our model neurons). Every three minutes of simulation time we stopped the animal at its current location for three seconds and removed the place field input. This led to spontaneous bursting via a synaptic depression-dependent mechanism (Romani and Tsodyks, 2015), reminiscent of sharp-waves seen during awake quiescence and sleep, see Figure 2. Neither the bursting, nor the learning process itself depended qualitatively on the exact amount of time the virtual animal spent moving versus staying still. Synaptic plasticity was allowed to occur during both theta activity and sharp-waves, that is it was never ‘turned-off’.

![Figure 2.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig2-v2.jpg)

**Figure 2.:** (a) Snapshots of the connectivity during the exploration of a novel environment. During early exploration, the connectivity is not correlated with the place-field ordering, while during late exploration cells with neighboring place-fields are more strongly connected. (b) i. The mean cross-correlation of the activity of place cells with adjacent place fields on a novel track during exploration (sequential correlation SC). Black: SC during active exploration (theta-activity), Orange: SC during spontaneous bursts. Note the sharp transition in the SC of burst activity. ii. The SC of the total activity binned into 3 min intervals shows a steady increase preceding the transition. (c) Burst activity exhibits replay after a critical period. i. Early exploration. Top: average input to place cells before (blue star), during (black star) and after period of ‘quiet wakefulness’. Bottom: space-time plots of the place cell input and firing rate. Note the disordered spatio-temporal structure of the burst activity. ii. Later exploration. After a critical transition time bursts exhibit sequential replay of activity from the novel track. Note the sequential structure of the burst activity.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a) The mean synaptic weight of recurrent excitatory connections as a function of time for 10 consecutive simulations of 1 hr each. The initial condition was all the weights identical and set to a value of 40. (b) the distribution of synaptic weights at the end of the 10 hr of simulation. About 10% of synaptic weights are maximally depressed to zero, 40% are maximally potentiated (threshold set to 80) and 50% take on intermediate values. As new environments are explored the distribution remains largely fixed but individual synapses change in time.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (a) The evolution of the mean synaptic weight over the course of exploration of 10 distinct tracks and the resulting distribution of synaptic weights (right). (b) Snapshots of the profile of the recurrent connectivity and firing rate during exploration of a novel track, up to 15 hr. The place cell activity is calculated with respect to the maximum of the subthreshold input. Note that at later times the maximum of the place cell activity is shifted to the right (clockwise, in the direction of motion) compared to the input. In experiment this would be seen as a backward shift in the place field of cells. Note also the negative skewness in the activity. (c) Transition in the SC of burst activity (black circles) reflecting the change in the spatio-temporal structure of the bursts. The SC of the sensory-driven theta-activity shows an increase leading up to the transition. Inset: The same over 16 hr of simulation time. (d) ‘LFP’ and space-time plots of the network firing rate and external input before and after the transition. (e) The amplitudes of the even and odd Fourier modes of the recurrent connectivity after 1 hr of exploration. (f) A transition in the SC occurs only for a range of frequencies. (g) An anti-symmetric plasticity rule (left) or a rule with dominant depression at short latencies (right) does not lead to an emergence of spontaneous bursts. All parameters are the same as in Figures 2 and 3 with the exception of the following. The modulation frequency during training on the 10 tracks for one hour each is f = 5 Hz, $I_{1}$ = 22 Hz, and the velocity of the animal is constant with a value $v$ = 1 rad/sec. Finally, during the training period of 1 hr on each of ten distinct tracks, theta activity was always present, that is there were no bursts. Allowing for bursts during training did not alter the results qualitatively.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (a) A sample trajectory of the virtual animal. The velocity is modeled as an Ornstein-Uhlenbeck process. Left: Position of virtual animal, i.e. the position of the maximum in the place-field input. Right: Place-cell activity. (b) The bias in the motion of the virtual animal during the first 15 min of a simulation, averaged in one-minute bins. Specifically the bias is the difference in the time spent moving clockwise versus moving counter-clockwise. The velocity of the virtual rat is an Ornstein-Uhlenbeck process with a non-zero mean as described in Materials and methods; the non-zero mean results in an overall clockwise bias. (c) The growth of the odd Fourier mode (sine mode) over time (solid line) compared to the cumulative motion bias. The cumulative motion bias is the time integral of the motion bias, scaled to match amplitudes with the normalized odd mode of the connectivity.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) The SC for three identical simulations with the only difference being the degree of heterogeneity in the place-field input to place-cells. The curve with the black circles is identical to the simulation in Figure 2 of the main text, for which $I_{PF}$ = 25 Hz. The red squares are a simulation for which $I_{PF}$ is uniformly distributed between 20 and 30 Hz (and hence the mean is the same as before). The orange diamonds show an extreme case where $I_{PF}$ is uniformly distributed between 0 and 50 Hz. B. Examples of place-cell activity for the strongly heterogeneous case. Note that in this case some cells are only very weakly selective to place, for example cell 3, while others have no place field whatsoever, for example cell 4.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** (a) A space-time plot of the firing rate (Hz) during early exploration. (b) The position of the most active place cell over time (solid line). The position of the animal is given by the dashed line. (c) The firing rate of a single place cell. Peaks in the theta rhythm are given by dotted vertical lines, and most likely spike times by solid lines. (d)-(f) The same as (a)-(c) for late exploration. Parameters are the same as those used for Figure 2—figure supplement 2, with the exception of $f$ = 8 Hz.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** (a) The firing rate r (top), short-term synaptic depression variable x (middle) and external input to place cells (bottom) during a period of ßleep’ or ‘quiet wakefulness’, that is in the absence of theta-modulated place field input. Spontaneously occurring bursts always travel forward when the input is globally homogeneous, reflecting the asymmetry in the underlying recurrent connectivity. However, a strong location-specific input (just after 1 s and 8 s) can transiently depress the synapses in downstream neurons, facilitating the propagation of activity backwards. Right: blow-up of activity showing forward and backward replay. (b) Raster plot generated from the same simulation as in (a). The external input is $I_{i}=−0.8$ Hz except for the two spatially-modulated inputs which are presented for 50 ms each and have the form $I_{i}=40(1+cos\theta_{i})$ Hz.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig2-figsupp7-v2.jpg)

**Figure 2—figure supplement 7.:** (a) The temporal maximum of the mean firing rate (averaged over the network) as a function of the external input. The input is a constant, that is there is no place-specific input. Simulations are run for 100 s and the first 10 s are discarded to avoid transients. (b) 'LFP's of the spontaneous activity, actually the total input to the network for I = −0.8 (left), −0.35 and 1 respectively. (c) Space-time plots of the spontaneous activity shown with neurons ordered according to their place fields in the last, next-to-last and first environments explored. Parameter values are identical to those in Figure 2.

![Figure 2—figure supplement 8.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig2-figsupp8-v2.jpg)

**Figure 2—figure supplement 8.:** (a) The amplitude of the even mode of the recurrent connectivity over time. (b) Top: The SC of the SWR activity. Bottom: The mean firing rate in the network over time. The initial condition for the recurrent connectivity is the same as for the simulation shown in Figure 2, in other words that resulting from the exploration of 10 distinct tracks.

As the virtual animal explored the track, the sequential activation of the place cells led to changes in the recurrent connectivity via the plasticity rule, Figure 2a. Whereas the connectivity between cells was initially unstructured on the novel track, it evolved over the span of minutes to tens of minutes such that cells with nearby place fields were more strongly connected than ones with disparate place fields. Furthermore the resulting connectivity was slightly asymmetric, reflecting the bias of the animal’s motion, see Figure 2—figure supplement 3. Although the changes we observed in the recurrent connectivity, see Figure 2a, and concomitant changes in place cell activity were continuous and smooth during the duration of the simulation, there was a dramatic and sharp transition in the structure of the burst activity during awake quiescence. We quantified this transition by measuring the mean pairwise cross-correlation of cells with neighboring place fields on the novel track. Such cells are ‘neighbors’ only on the novel track and not on any other track by virtue of the global remapping or randomization of place-fields. We call this measure the sequential correlation (SC) because it is high when there is a properly ordered sequence of place-cell activations on any given track. The SC during theta-activity (exploration) was already non-zero at the outset of the simulation by virtue of the external place-field input which generates sequential activity, black squares Figure 2b. On the other hand, the SC was initially near zero during spontaneous bursts, red circles Figure 2b. Interestingly the SC abruptly increased during burst activity at a critical time and remained elevated for the duration of the simulation. This transition occurred even in simulations where we included strong heterogeneity in place field tuning, see Figure 2—figure supplement 4. Note that the SC for theta-activity also showed a steady increase leading up to this transition, as did the SC when the total activity was taken into account, without discerning between epochs of movement or awake quiescence, see Figure 2b inset. This steady increase is due to the emergence of so-called theta sequences (Foster and Wilson, 2007). These are bursts of place-cell activity which sweep ahead of the animal’s position on every theta cycle during awake exploration, see Figure 2—figure supplement 5. The emergence of theta sequences here also coincides with a precession of the phase of the underlying firing rate with the ongoing theta rhythm, see Figure 2—figure supplement 5f and discussion for more detail.

Space-time plots of place-cell activity show that the abrupt increase in SC coincides with a transition in the spatio-temporal structure of the bursts: it is initially uncorrelated with the ordering of cells on the novel track, Figure 2c (i), and after the transition there is a clear sequential activation reminiscent of so-called ‘replay’ activity, Figure 2c (ii). In fact, before the transition the bursts are highly structured, but this structure is correlated with a previously explored track and not the novel one. If the learning process was carried on for much longer times all relevant network properties, such as connectivity and mean firing rates, saturated, see Figure 2—figure supplement 8.

### The transition in the structure of bursts is strongly dependent on the shape of the plasticity rule and the frequency of ‘theta’ modulation

We hypothesized that changes in the recurrent connections between place cells in our model during exploration were shaping the spontaneous activity and driving the transition to replay-like activity. The connectivity profile at any point in time could be decomposed into a series of spatial Fourier modes, Figure 3a. We tracked these modes in time and discovered that the transition in burst activity always occurred when the coefficient of the first even mode reached a critical value. Specifically, we conducted additional simulations in which we increased the firing rate of the feedforward inputs which drove place cell activity which in turn led the transition in burst activity to occur at earlier times, see shaded regions in Figure 3b. In fact, a theoretical analysis of our model shows that there is an instability of the spontaneous activity to bursts when the even mode of the connectivity times the gain in the neuronal transfer function is greater than a critical value, see Materials and methods. In our simulations the gain in the transfer function was nearly always the same during bursts because it depended on the mean input to the network during quiescence, which was constant. Therefore it was principally the even mode of the recurrent connectivity which determined the time of the transition. For this reason, the transition to replay occurred when the coefficient of the even mode reached a critical value as seen in Figure 3c. Note that there was no such dependence on the odd mode (dotted lines in Figure 3c).

![Figure 3.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig3-v2.jpg)

**Figure 3.:** This mode grows only for STDP rules with dominant potentiation, and grows fastest when periodic modulation is in the theta range. (a) The profile of the recurrent connectivity at any point in time can be decomposed into a series of even (cosine) and odd (sine) modes. Only the first two modes are shown. (b) As the amplitude of the place-field input is increased from 25 Hz (black), 30 Hz (orange) and 35 Hz (green) the transition shifts to earlier times. The SC of the SWR activity shows a sharp transition (shaded grey bars), while the total activity displays a smooth increase leading up to the transition. (c) In all cases the value of the even mode reaches approximately the same critical value at the time of the transition (shaded grey bars). The growth of the odd mode (dotted lines) is much more irregular, and its value does not correlate with the transition time.

We then asked how the growth of the even mode depended on the details of the plasticity rule and the frequency of periodic modulation of the place cell activity. We found that the growth of the even mode depended strongly on the frequency, peaking at an intermediate range and decreasing by orders of magnitude at low and high frequencies, Figure 4ai. This occurred independent of the details of the animal’s motion, for example compare Figure 4ai and Figure 2—figure supplement 2e for irregular versus purely clockwise motion respectively. On the other hand the odd mode, which represents a directional bias in the recurrent connectivity, closely tracks the cumulative bias in the animal’s motion, see Figure 2—figure supplement 3, and is independent of the forcing frequency to leading order, see Materials and methods for details. The strong dependence of the growth of the even mode on frequency, meant that, for simulations of up to 1 hr, transitions in the burst activity were observed only when the frequency was in the range of 2–10 Hz, Figure 4aii. Furthermore, the even mode only grew, and transitions only occurred, when the plasticity rule had dominant potentiation at short latencies. For a perfectly anti-symmetric plasticity rule, and for a rule with dominant inhibition at short latencies, the even mode did not change and even decreased, respectively, Figure 4b and c. In the latter case bursts were suppressed entirely (not shown).

![Figure 4.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig4-v2.jpg)

**Figure 4.:** (a) A temporal asymmetric plasticity rule with dominant potentiation at short latencies. i. The amplitude of the even mode of the connectivity after 1 hr of exploration, as a function of the modulation frequency. The even mode grows maximally over a range of approximately 1–10 Hz and it is strongly attenuated at lower and higher frequencies. Note the logarithmic scale. On the other hand, the growth of the odd mode is largely independent of the modulation frequency, see text for details. ii. The degree of SC of spontaneous bursting after 1 hr of exploration. Replay occurs only when the frequency lies between 2–10 Hz. Inset: The time at which a transition in the SC takes place as a function of frequency, for times up to 1 hr. (b) A purely anti-symmetric plasticity rule leads to recurrent connectivity which has only odd Fourier modes. There is no increase or transition in the SC of bursts in these simulations even after 1 hr. (c) An asymmetric plasticity rule with depression dominating at short latencies leads to connectivity with a negative amplitude of the even mode, that is recurrent excitation is weaker between pairs of place cells with overlapping place fields than those with widely separated place fields. In this case bursts are actually completely suppressed (not shown).

### A self-consistent theory to explain how the interplay between theta-modulation and the plasticity rule govern changes in recurrent connectivity

We sought to understand the mechanism underlying the evolution of the recurrent connectivity seen in simulations by studying a continuum version of a network of place cells, which can be written

$$
\taur˙=−r+ϕ(\frac{1}{2\pi}\int_{−\pi}^{\pi} d\theta^{′^{}}w(\theta,\theta^{′^{}})r(\theta^{′^{}},t)+I(\theta,t)),
$$

where $r(\theta,t)$ is the firing rate of a place cell with place field centered at a location $\theta$, $w(\theta,\theta^{ ′})$ is the synaptic weight from a cell at a position $\theta^{ ′}$ to a cell at a position $\theta$, and $I(\theta,t)$ is the external input which has the form

$$
I(\theta,t)=I_{0}+I_{PF}cos⁡(\theta−x(t))(1+I_{theta}cos⁡(2\pift)).
$$

The position of the virtual animal is given by $x(t)$, and the corresponding place-field input is modulated with a frequency $f$. This type of multiplicative theta modulation is seen in intracellular recordings in-vivo, for example see Figures 1 and 5 in (Harvey et al., 2009) and Figure 4 in (Lee et al., 2012).

![Figure 5.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig5-v2.jpg)

**Figure 5.:** (a) The growth rate of the symmetric mode is proportional to the integral of the product of the autocorrelation (AC) of place cell activity with the plasticity window (PW). Left: The AC of place cell activity overlaid on the PW with dominant potentiation at short latencies. Middle: Product of the PW and the AC. Right: The growth rate of the symmetric (cosine) mode of the connectivity as a function of frequency. i. When the activity is modulated at 1 Hz (top), the product returns nearly the original plasticity window, which being balanced yields near-zero growth rate. ii. For 5 Hz the potentiating lobe is maintained and some of the depression lobe changes sign and becomes potentiating leading to higher growth rate. iii. For 20 Hz the plasticity window undergoes sign reversals at a rate faster than the width of the lobes, meaning the integral is again near zero. (b) The growth rate of the even (cosine) and odd (sine) spatial Fourier coefficients as a function of the modulation frequency (black curve is the same as in (a) except on a log-log scale). Inset: The growth rate of the even mode normalized by its value for no periodic modulation. Rule parameters are $A_{+}$ = 0.1, $\tau_{+}$ = 20 ms, $A_{−}$ = 0.1/3, $\tau_{−}$= 60 ms (c) Increased growth rate in the theta range does not require fine tuning. (d) The frequency at which growth is maximal depends on the overall width of the plasticity window. Broader windows favor slower frequencies. (e) A triplet rule increases the growth rate at all frequencies compared to the pairwise rule, but does not significantly shift the optimal frequency range. The parameters for pairwise interactions are as before. The time constants for triplet interactions are indicated on the figure, while the remaining parameters are chosen to make the rule balanced.

To model the evolution of the recurrent connectivity we made use of the fact that the step-wise increases in synaptic strength due to the plasticity rule can be approximated as a smooth process as long as plasticity occurs much more slowly than the firing rate dynamics. When this is the case, the rate of change of the synaptic weight from place cell with place field centered at $\theta^{ ′}$ to one with place field at $\theta$ can be written as

$$
w˙(\theta,\theta^{′^{}})=\int−∞∞ dTK(T)r(\theta,t)r(\theta^{′^{}},t+T),
$$

where $K(T)$ is the change in the synaptic weight according to the plasticity rule given a spike pair with latency $T$ (Kempter et al., 1999) and see Materials and methods. This equation reflects the fact that the total change in the synaptic weight is the sum of all the pairwise contributions from the pre- and post-synaptic cells, with each pair of spikes weighted by the plasticity rule with the appropriate latency. (Equations 1–3) represent a self-consistent model for the co-evolution of the firing rates and synaptic weights in the network.

In order to derive an analytical solution we first assume that the neuronal transfer function $ϕ$ is linear. We then make the assumption of slowly evolving synaptic weights explicit by scaling the amplitudes of the potentiations and depressions from the plasticity rule by a small parameter. The upshot is that the connectivity evolves to leading order only on a slow time scale, much slower than the fast neuronal dynamics. Furthermore, we know from numerical simulations that after sufficient exploration the probability of connection between any two cells depends on average only on the difference in place field locations. Therefore, by averaging the connectivity over the fast time $t$ we can write

$$
⟨w˙(\theta,\theta^{′})⟩_{t}=⟨w˙(\theta−\theta^{′})⟩_{t}=⟨w˙_{even}⟩_{t}cos(\theta−\theta^{′})+⟨w˙_{odd}⟩_{t}sin(\theta−\theta^{′})
$$

where the growth rates of the even and odd modes $⟨w˙_{even}⟩_{t}$ and $⟨w˙_{odd}⟩_{t}$ are functions of the plasticity rule parameters, the velocity of the animal and the frequency of periodic modulation, see Materials and methods for details. It turns out it is possible to understand these dependencies intuitively and comprehensively without having to study the analytical formulas. Specifically, if we wish to isolate the growth rate of the even mode, which is responsible for driving the emergence of replay in the burst, we can consider place cell pairs where $\theta=\theta^{ ′}$, that is pairs with overlapping place fields. When this is the case we can combine (Equations 3 and 4) to yield

$$
⟨w˙_{even}⟩_{t}=\int−∞∞ dTK(T)AC(T),
$$

where $AC(T)=⟨r(\theta,t)r(\theta,t+T)⟩_{t}$ is the autocorrelation (AC) of the place-cell activity. Note that despite the similarity in form between (Equation 5) and (Equation 3), the biological interpretation of the two is quite distinct. (Equation 3) describes the changes in the strength of a specific synapse, that from a cell with place-field centered at a position $\theta^{ ′}$ onto a cell with place-field centered at a position $\theta$. The evolution of this single synapse depends only on the sum of the changes from all spike pairs from these two cells. If we averaged this equation over fast fluctuations in time we would find that the slow evolution of the synapse depends on the cross-correlation of the activity of the two neurons times the STDP window. There is an equation like this for every cell pair in the network; clearly for a large network it is not feasible to solve these equations self-consistently. On the other hand, (Equation 5) does not describe the changes in strength of a single synapse. Rather, it describes changes in the strength of a particular pattern of synaptic connectivity in the network. This pattern is one in which cells with highly overlapping place fields have strong and symmetric recurrent connectivity. Furthermore the strength of the synaptic connections decays smoothly with the difference between place field locations. In our theoretical model, in the limit of a large network, the cross-correlation of very nearby cells is simply given by the auto-correlation, which is why it appears in (Equation 5). It is perhaps remarkable that using purely local information, namely the AC of place cell activity, one can infer the growth rate of a network-wide mode of synaptic connectivity. The key assumption that makes this possible is that the synaptic weight between any two cells should depend only on the difference in place-field location and not on the absolute position, (Equation 4). Therefore the growth rate of the even mode is found by multiplying the AC of place-cell activity by the window for plasticity, and integrating. Because the effect of periodic modulation on the AC is straightforward, we can determine graphically how the frequency of modulation interacts with the plasticity rule to drive changes in the burst structure.

We first note that if there is no periodic modulation of place-cell activity then the AC will simply reflect the movement of the animal. This will lead to a very broad AC compared to the time-scale of plasticity. For example, if we assume that the width of the place field is a fraction of the track length (as in our model), then a rat running between 5 and 50 cm/sec on a multi-meter track would have an AC which decays on the order of between seconds and tens of seconds. Therefore, the AC is essentially constant compared to a typical plasticity window of between tens and hundreds of milliseconds, and the integral in (Equation 5) will give nearly zero. Periodically modulating place-cell activity will increase the growth rate as long as potentiation is dominant at short latencies, Figure 5a. Slow modulation will bias the integral in (Equation 5) toward the potentiation lobe of the STDP (Figure 5a left and middle, top), while in an optimal range of frequencies the peaks and troughs of the AC will maximally capture potentiation and flip the sign of the depression lobe (Figure 5a left and middle, middle). Finally, at higher frequencies the plasticity rule undergoes multiple sign flips on a fast time scale, which again gives a near zero value for (Equation 5) (Figure 5a, left and middle, bottom). This means that the maximal growth rate of the even mode occurs for an intermediate range of frequencies: those which modulate place-cell activity on a time scale commensurate with the window for plasticity, Figure 5a right. Note that this has nothing to do with the overall rate of plasticity, which is the same independent of the modulation frequency. That is, even if the AC is flat, recurrent synapses undergo large numbers of potentiations and depressions. Rather, periodic modulation serves to organize the structure of synaptic plasticity at the network level by preferentially strengthening connections between place-cells with overlapping or nearby place field and weakening others. The optimal range of frequencies for growth of the even mode depends only weakly on the ratio of the width of the potentiation to that of the depression lobe, Figure 5c, but significantly on the total width, Figure 5d. Allowing for triplet interactions (as opposed to just pairwise) in the plasticity rule increases the overall growth rate but does not alter the range of optimal frequencies, Figure 5e. On the other hand, the theory predicts that the growth rate of the odd mode is only weakly dependent on the modulation frequency (Figure 5b) as is seen in simulations (Figure 2—figure supplement 2e), and can be understood by considering (Equation 3) with $\theta−\theta^{ ′}=\pi/2$. In this case the growth rate depends on the product of the plasticity rule with the cross-correlation (CC) of cells with disparate place fields. When there is an overall direction bias in motion then the CC will have peak shifted from zero-lag and the product with the STDP rule reliably gives a positive (or negative) growth rate. When there is very little motion bias the CC will be nearly flat, yielding little growth in the odd mode and the resulting connectivity will be highly symmetric.

It is also clear from (Equation 5) that a perfectly anti-symmetric plasticity rule will lead to no growth in the even mode as the product of the rule and the AC will itself be an odd function, see Figure 4b. A rule with dominant depression at short latencies will similarly yield a growth rate which is precisely the inverse of that shown in Figure 5a. This causes a decay in the even mode resulting in a connectivity pattern with locally dominant inhibition, see Figure 4c.

Finally, to go beyond this qualitative treatment and find the exact dependence of the evolution of the synaptic weights on model parameters requires solving (Equations 1–3) self-consistently, see (Equations 43–45) in Materials and methods for the case when $v$ is constant. These are the equations we use to generate the curves in Figure 5. When the AC of the place cell activity is predominantly shaped by the modulation frequency $f$, compared to the motion of the animal (strictly speaking when $v/(2\pif)≪1$, which is the case already for $f>1$ Hz and for reasonable values of $v$) then the connectivity evolves to leading order as

$$
⟨w˙_{even}⟩_{t}∝I_{PF}^{2}I_{theta}^{2}[\frac{1}{1+4\pi^{2}\tau_{+}^{2}f^{2}}−\frac{1}{1+4\pi^{2}\tau_{−}^{2}f^{2}}],
$$



$$
⟨w˙_{odd}⟩_{t}∝I_{PF}^{2}v[\frac{\tau_{+}}{1+\tau_{+}^{2}v^{2}}+\frac{\tau_{−}}{1+\tau_{−}^{2}v^{2}}].
$$

Equation 6 shows clearly that the growth of the even mode, which drives the emergence of replay, is proportional to strength of oscillatory modulation $I_{theta}$. Additionally it can be seen on inspection that the modulation frequency itself plays a crucial role in setting the growth rate, and peaks at intermediate values. On the other hand, the growth of the odd mode, which represents the degree of asymmetry in the recurrent connectivity, is driven entirely by the motion of the animal to leading order. In the case of constant motion, studied here, it depends only on the velocity of the animal.

### Sparse coding allows for the replay of activity from multiple explored tracks during bursts

The spatio-temporal structure of sharp-wave-like bursts in our model reflected the sequential ordering of place fields on the most recently explored track; correlation with earlier tracks was erased or greatly reduced. In reality, only a fraction of place cells have well-defined place fields in any given environment, that is coding is sparse (Bostock et al., 1991; Fyhn et al., 2007). We incorporated this sparse-coding strategy to our model by providing place-field input to only one half of the total neurons in the network; the other half received constant input. These place cells were chosen randomly from one track to the next and place field locations were assigned randomly as before. Therefore the overlap in the population of place-cells between any two tracks was also fifty percent. We then allowed the network to evolve by having the virtual animal explore thirty distinct tracks, each for 1 hr of simulation time, as before. The resulting matrix of synaptic connections was correlated with the ordering of place-cells in several past explored environments, Figure 6a. The amplitude of the even mode, which is responsible for generating spontaneous replay, decayed roughly exponentially as a function of the recency of the explored track, Figure 6a inset. This suggested that the replay dynamics in the network with sparse coding might be correlated with several previously explored tracks simultaneously (Romani and Tsodyks, 2015). Indeed, when the network was driven with a global, non-selective input, the replay was strongly correlated with the past two explored environments, Figure 6b, whereas the correlation with earlier environments was negligible. On the other hand, when the constant external drive was selective to the subset of place-cells on any given track, replay activity was robustly correlated with activity on that track only, Figure 6c. Such selective input may originate in cortical circuits which store environment-specific sensory information as stable patterns of activity; these patterns correspond to attracting fixed points in network models of long-term memory storage and memory recall (Hopfield, 1982; Tsodyks and Feigel'man, 1988; Recanatesi et al., 2015). Spontaneous switching between cortical representations during slow-wave activity would therefore engage distinct hippocampal replay patterns, which in turn could strengthen and consolidate the corresponding cortical memory trace.

![Figure 6.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig6-v2.jpg)

**Figure 6.:** (a) The connectivity profile after exploration of 30 environments in a network in which one half of the neurons are place cells on any given track. The same connectivity can be visualized using the ordering of the place cells on the most recently explored track (track n, black curve) or using the ordering of past explored tracks (green and red curves). The spatial structure which emerges during exploration on any given track eventually gets overwritten as new tracks are explored. Nonetheless the connectivity stores structure from several past explored tracks simultaneously. Inset: The amplitude of the even Fourier mode as a function of the recency of the corresponding track. (b) A global stimulus applied to all the neurons in the network generates replay which is highly correlated with the past two tracks. (c) Selective stimulation of only those neurons which were place cells in the most recently explored track (top) or next-to-last track (bottom) generates replay which is highly correlated only with the corresponding environment. N = 200 neurons in all simulations.

Therefore, sparse coding causes the synaptic connectivity matrix to be simultaneously correlated with place field orderings from multiple tracks and allows for robust replay of activity from those tracks given appropriate inputs. The number of different environments which could be simultaneously encoded in replay depended on model details, particularly the coding level, that is the fraction of active place cells in any given environment (not shown) (Battaglia and Treves, 1998).

### Experimental evidence for a transition to replay

Pairwise reactivations of CA1 place-cells with overlapping place fields during awake SWRs improve during exploration; they are stronger during late exploration than early exploration (O'Neill et al., 2006). This holds true not only for pairwise correlations, but also reactivations of entire neuronal ensembles, at least on linear tracks (Jackson et al., 2006). More recent work has shown that significant replay events during awake SWRs in rats running along a three-arm maze emerge abruptly only after a certain number of runs (Wu and Foster, 2014). These results are consistent with our model predictions. We additionally sought to directly test for a time-resolved increase in SC in neuronal data. We looked for this increase in multi-unit recordings of place-cell activity from the hippocampus of rats exploring novel, periodic tracks (Wang et al., 2015).

We first identified cells with well-defined place fields by extracting the coefficients and phase of the first two spatial Fourier modes of their time-averaged activity as a function of the normalized distance along the track (in radians), see Figure 7—figure supplements 1–3. We kept only those cells for which the ratio of the coefficients, the Tuning Index (TI), exceeded the threshold of one, indicating strong spatially selective activity, see methods for details. We then ordered the cells according to their phase (approximately the position of peak firing). The SC of activity over the total duration of the experiment using this ordering was significantly higher than 5000 randomly reshuffled orderings which on average gave SC = 0, see Figure 7a and b.

![Figure 7.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig7-v2.jpg)

**Figure 7.:** (a) Sample firing rate profiles from place cells recorded from CA1 of rat hippocampus during exploration of a novel periodic track with an illustration of how cells can be ordered according to their phases. (b) The SC calculated over the entirety of the experiment (35 min) given the correct ordering (red dot) and for 5000 reshuffled orderings. (c) The time course of SC given the proper ordering (solid symbols) does not show any dynamics when the medial septum is reversibly inactivated with muscimol. Note, however, the clear separation with the shuffled data (open symbols), indicating that place fields are intact even though theta is disrupted. (d) After a rest period the animal is placed back onto the same track; the SC now exhibits a significant increase given the proper ordering (solid symbols) over the first 10 min of exploration and then plateaus. Note that the bottom plots in (c) and (d) show the power spectrum of hippocampal LFP (CA1), indicating a large reduction of theta power in the muscimol condition. (e) When the animal is allowed to explore a novel track and then placed back on the track for a second and third session, there is a significant increase in the SC only during the first session. Error bars are S.E.M.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (a) Three sample cells. Spike maps (top), rate maps (middle) and linearized rate along the track with muscimol and post-muscimol (bottom). Each linearized rate profile is fit by a curve $r=r_{0}+r_{1}cos⁡(\theta−ϕ_{1})+r_{2}cos⁡2(\theta−ϕ_{2})$ and the coefficients extracted. (b) Left: The values of the coefficients of the first cosine mode vs. the spatially homogeneous mode for all cells. Middle: The histogram of the tuning index ratio for all cells. Right: Histogram of firing rates. (c) There is only weak rate-remapping for clockwise versus counter-clockwise motion. (Left to right) The first two Fourier coefficients and phase of the fit to the linearized rate profiles in the clockwise versus the counter-clockwise direction, and a sample cell.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig7-figsupp2-v2.jpg)

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** (a) Time-resolved SC for each session. Asterix and shaded regions as above, in Figure 7—figure supplement 4. (b) First Fourier coefficient plotted versus the zeroth order coefficient of average place field activity for all cells. (c) Histogram of the TI for all cells (dashed line) and for those cells with mean firing rate $>$0.4 Hz (solid lines). (d) Histogram of firing rates. e. Norrmalized TI histograms.

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/37388/elife-37388-fig7-figsupp4-v2.jpg)

**Figure 7—figure supplement 4.:** Asterix indicates a significant difference with the first data point (t-test p$<$0.006 corrected for multiple comparisons) except for the second asterix in the plot of SC for $TI\geq1$ which indicates a significant difference between the second and third data points. Shaded regions indicate a significant difference between SC and that of 5000 shuffles with randomized ordering (t-test p$<$0.005, corrected for multiple comparisons). Bottom: Power spectra of LFP recorded during each session.

When the medial septum (MS) was inactivated via muscimol the SC did not exhibit any dynamics as a function of time, Figure 7c. However, once the animal recovered from the muscimol the SC using the proper phase ordering exhibited an initial ramp over the first ten minutes of exploration and then remained high (significant difference between first point and all others, t-test with multiple-comparison Bonferroni correction, p-values<0.004 and between second and third points), see Figure 7d, solid circles. This is consistent with the model result which showed a similar ramping increase when the total activity (and not just bursts) was considered, see for example Figure 2bii. On the other hand, the SC computed for shuffled phases showed no dynamics and remained close to zero, see Figure 7c,d, open squares. This indicates that there are no global changes in neuronal correlations during exploration, which could occur, for example, due to slow changes in theta modulation or neuronal excitability. Rather, there is a sustained increase in pairwise correlations only between those neurons which encode nearby places, and only when strong theta modulation is present. This finding also held when we considered the more lax criterion $TI\geq1/2$, see Figure 7—figure supplement 4 (rat A991). In a second animal there was an insufficient number of well-tuned units to repeat the analysis, see Figure 7—figure supplement 4 (rat A992). One possible confound in attributing this increase in correlation to theta modulation alone, is the fact that the firing rates of place-cells during MS inactivation were lower on average than during the post-muscimol experiment. Lower firing rates in the computational model lead to lower rates of plasticity. However, this difference in firing rates was not significant for the well-tuned neurons shown in Figure 7 ($TI\geq1$), (t-test, p=0.30). An initial, sustained increase in SC was also observed in data from a separate experiment in which an animal was first exposed to a novel hexagonal track, Figure 7e (difference between first point and all others, t-test with correction for multiple comparison, p-values<10–6). Furthermore, no such increase was found on subsequent sessions on the same track, indicating that the change in correlation only occurred when the environment was novel. This result held when we considered the more lax criterion $TI\geq1/2$ and also when all units were used, regardless of tuning, see Figure 7—figure supplement 3a (rat A992). In a second rat there were too few well-tuned cells to use the criterion $TI\geq1$, but an initial and sustained increase in SC was also seen using all units, although this correlation was not always significantly different from that calculated from shuffled orderings of the cells (unshaded points in Figure 7—figure supplement 3a, rat A991).

## Discussion

### Summary

We have presented a computational model of a hippocampal place-cell network in order to investigate how the exploration of novel environments shapes the patterns of recurrent synaptic connectivity. Because place-fields remap randomly from one environment to the next, the recurrent connectivity, shaped by previous learning, is initially uncorrelated with place-cell activity in a novel environment. Our major finding is that the learning rate during the exploration of a novel environment depends almost entirely on the product of the autocorrelation of place-cell activity and the window for plasticity. The integral of this product determines the growth rate of a global, network-wide pattern of synaptic connectivity, which results in strong local recurrence and long-range competition. It is this mode which drives spontaneous replay activity in our model network. The growth rate of this mode is maximum when place-cell activity is periodically modulated on a time-scale commensurate with the plasticity rule, which for realistic time constants yields frequencies in the theta range. Furthermore, lower and higher frequencies than theta lead to learning rates which are orders of magnitude slower. This suggests that the role of theta is to accelerate learning. Note that the overall rate of plasticity is not affected by the presence of oscillations. The number of spike pairs, and hence the number of potentiations and depressions, depends only on the firing rates. Rather, theta oscillations generate repeated pre-post pairings in both directions, which coupled with a plasticity rule with dominant potentiation at short latencies bias plasticity toward potentiating events for neurons with neighboring place fields. One signature of this mechanism is a continuous increase in the pairwise cross-correlation in the activity of neighboring place-cells leading up to a critical time. We have found evidence consistent with this by analyzing the activity of simultaneously recorded hippocampal place cells in a rat during the exploration of a novel track.

### The assumption of plasticity at recurrent synapses

In our model we have assumed that plasticity occurs only in the recurrent excitatory synaptic connections, and not in the feed-forward inputs. Therefore we also assume that the place-field input, which peaks at the spatial position of the virtual animal at given moment in time, is itself stable. In fact, consistent with this assumption, it seems most place cells are active from the outset of exploration of a new environment, although see (Hill, 1978; Frank et al., 2004; Monaco et al., 2014). Furthermore cells tend to exhibit only subtle changes in the size and shape of their place fields over time (Mehta et al., 1997; Mehta et al., 2000), also consistent with our model, see Figure 2—figure supplement 2b. On the other hand, it has been shown in area CA1 that some place-cells exhibit place-fields only after several minutes of exploration (Frank et al., 2004; Frank et al., 2006). Recent intracellular recordings indicate that appearance of these ‘hidden’ place-fields requires the coincidence of active dendritic events and synaptic input via the Schaeffer collaterals (Lee et al., 2012; Bittner et al., 2015; Bittner et al., 2017). It may be that this mechanism for place-cell ‘generation’ is particularly salient in cells of area CA1 by virtue of being uniquely positioned to compare and integrate both entorhinal and hippocampal inputs. In any case the strongly recurrent nature of the network we study may make it a more relevant model for circuits in area CA3.

Nonetheless we would expect that changes in spiking activity arising in CA3 due to plasticity in the recurrent connectivity, as in our model, would be reflected in similar changes in the spiking activity of CA1 cells due to the direct inputs via the Schaeffer collaterals. More specifically, in contrast to plasticity mechanisms leading to the formation of place cells themselves, here we have modeled on how plasticity shapes the recurrent connections between already-formed place cells. We find that pairwise correlations between place cells with nearby preferred locations increases during exploration of a novel environment. Assuming such an increase occurs in a strongly recurrent circuit in CA3, we would also expect to observe an increase in correlation in target CA1 pyramidal cells, as long as there exists some mapping from CA3 place cells to CA1 place cells. Such a mapping could be a simple random projection or a more ordered relationship. Recent work suggests that place fields of CA1 pyramidal cells on linear tracks are built up of a weighted sum of CA3 inputs from positions surrounding the relevant place field (Bittner et al., 2017); in such a case the increased correlation in CA3 activity would be shared by CA1 output. Indeed, the data we have analyzed from place cells of area CA1 show increase sequential correlation as predicted by our recurrent model. A recent computational model of STDP-induced formation of place fields in CA1 cells via the feed-forward excitatory connections from CA3 (Schaeffer Collaterals) suggests a role for theta in speeding up place cell formation (D'Albis et al., 2015). This raises the intriguing suggestion that theta may play a key role both in place-cell formation through plasticity of feed-forward inputs, and also in the emergence of replay through plasticity of recurrent synaptic connections as indicated by our work here.

### Remapping of place fields for different directions of motion on the same track

Hippocampal place cells actually exhibit global remapping of their place fields depending on the direction of motion of the animal on linear tracks (McNaughton et al., 1983; Muller et al., 1994). This is perhaps not surprising given that the behaviorally relevant information for the animal is not just the position along the track but also the way in which it is facing; for example this determines how far away a potential reward is, if located at one or both ends of the track. Studies using periodic tracks have shown no such global remapping, but rather some degree of rate remapping (Schwindel et al., 2016), that is the direction of motion affects the shape and amplitude of place fields, but not their position. In the data we have analyzed there is very weak remapping, see Figure 7—figure supplements 1c and 2b, and so the assumption of invariance of place field to direction of motion is a good one. In our model we have made this assumption. The consequence of this is that while exclusively clockwise (CW) or counter-clockwise (CCW) motion will lead to highly asymmetric recurrent connectivity, exploration of both directions will give rise to much more symmetric connectivity, see Figure 2a. In practice any trajectory over a finite amount of time will have a directional bias; in the data we have analyzed the rat spends a slightly larger fraction of the time moving CW compared to CCW, and this will necessarily lead to asymmetries in the connectivity. In linear tracks, due to the global remapping such asymmetries should be even more pronounced.

### Forward versus backward replay

The inevitable asymmetry in the recurrent connectivity of our model place-cell network due to plasticity during exploration strongly biases spontaneous activity. On a periodic track this replay would be exclusively CW or CCW depending on the corresponding bias in motion during exploration, while learning on a linear track would always produce forward replay. Previous work has shown that perfectly symmetric connectivity can give rise to both forward and backward replay in equal measures, due to spontaneous symmetry breaking of activity (Romani and Tsodyks, 2015). We would argue that such symmetric connectivity is not robust for the reasons given above, although we cannot rule out the existence of homeostatic mechanisms which would conspire to make it so. Rather, we propose here an alternative mechanism for generating backward replay given asymmetric connectivity, based on local sensory input.

Specifically, if global input to our model network is homogeneous then replay occurs only in one direction. This is due to the asymmetry in the connectivity which comes about through a bias in the direction of motion of the animal during exploration. On the other hand, if the input is not homogeneous, but rather spatially localized, then the replay dynamics can be qualitatively distinct. This difference is mediated by the short-term synaptic depression mechanism present in the model. With a strong, spatially localized input, synapses to downstream neurons (in the sense of the asymmetric bias of the connectivity) become rapidly depressed, see Figure 2—figure supplement 6. This forces the activity to travel backward with respect to the bias in the connectivity. In fact, in experiment, when local spatial input is absent, for example when the animal is sleeping in a rest box, forward replay is predominant (Roumis and Frank, 2015). On the other hand, both backward and forward replay are observed when the animal is awake but quiescent on a given track. This is precisely when locally sensory cues are available to the animal, and could potentially shape spontaneous replay events. Recent work shows that some neurons in area CA2 fire more strongly during awake quiescence than during exploration (Kay et al., 2016); they may be providing information regarding local sensory cues. In our scenario the mechanisms leading to forward versus backward replay are distinct and therefore in principle relevant replay statistics such as replay velocity and spiking intensity should also be different.

### Robustness to changes in the plasticity model and to the presence of spike correlations

Here we have considered a simple phenomenological model of plasticity which depends on the timing of spike pairs. Taking into account spike triplets as opposed to only pairs does not alter our findings qualitatively, see Figure 5e, although we are necessarily ensuring a balanced rule through our choice of parameters. Fits of heuristic spike timing-dependent models to data from slice experiments yield parameter values which do not lead to balanced rules such as the ones we have used here (Pfister and Gerstner, 2006). Specifically, when the repetition-rate of spike pairs is high, in-vitro STDP is dominantly potentiating; for such a rule there would be no non-monotonic dependence of the learning rate on modulation frequency at high rates. The mechanism we propose for theta would not be operative in that case. However, in a recurrent network model, unbalanced plasticity rules would quickly lead to synapses either saturating to maximum efficacy or vanishing completely; non-trivial network structure is therefore not possible with such rules. One solution to this problem is to complement the heuristic, unbalanced Hebbian rule, extracted from slice experiments, with a non-Hebbian heterosynaptic rule, as well as additional, slower homeostatic mechanisms (Zenke et al., 2015). It is unclear if the learning rate of this rule would also exhibit a non-monotonic dependence of the modulation frequency, as in our rule. However, heuristic rules describing synaptic plasticity in-vivo are still largely unknown. Therefore one reasonable approach to studying plasticity in recurrent networks in-vivo is to choose the simplest possible rule which allows for the emergence of non-trivial structure; this has been our approach here. It remains to be studied how more realistic voltage- or calcium-based plasticity rules interact with the theta-modulation to affect learning in recurrent networks (Clopath et al., 2010; Graupner and Brunel, 2012), although at a single-synapse one can find qualitatively similar regimes for an array of plasticity rules in the presence of pre- and post-synaptic oscillations (Albers et al., 2013).

Our results clearly do not depend on the actual spike timing since our model neurons generate spikes as Poisson processes; rather, all lasting changes in the connectivity are due to time-varying modulations of the firing rates. In fact, recent work with a spiking neuron model suggests that such modulations in the firing rate, as opposed to exact spike timing, are sufficient to explain the effect of plasticity from STDP and more realistic calcium-based plasticity rules in general (Graupner et al., 2016). In any case the contribution of pairwise spike correlations to the evolution of the recurrent connectivity can be formally taken into account in (Equation 4), that is via its affect on the auto-correlation of place-cell activity.

### Theta sequences and phase precession

The increase in SC during theta activity in our model is due to the emergence of theta sequences, Figure 2—figure supplement 5, a consequence of the strengthening of the recurrent excitatory connectivity during exploration. The emergence of theta sequences also gives rise to phase precession of the place cell activity. Specifically, the peak of the place cell firing rate shifts to earlier phases of the theta rhythm as the animal enters the place field. This mechanism was first studied in (Tsodyks et al., 1996), in which theta sequences arose through asymmetry in the recurrent connectivity. A very similar effect can be achieved through short-term synaptic depression even without the need for asymmetric connectivity (Romani and Tsodyks, 2015). The reason is that the motion of the animal, and hence the sequential activation of place cells, generates an asymmetric pattern of synaptic depression (upstream synapses are more depressed than downstream ones). This is the mechanism responsible for theta sequences and phase precession in our model. Phase precession therefore emerges over time in our model, and is not present during early exploration. We have also studied the effect of phase precession on learning numerically by generating theta sequences directly via the place-field input itself (not shown). Preliminary simulations suggest that phase precession can actually speed up learning, although the mechanism is non-trivial and requires additional study.

### Other network models of place-cell activity

Recurrent network models for place-cell activity provide a parsimonious explanation for electro-physiological phenomena associated with exploratory behavior as well as the generation of sharp-wave bursts during awake quiescence and sleep (Romani and Tsodyks, 2015; Tsodyks et al., 1996; Shen and McNaughton, 1996; Cutsuridis and Hasselmo, 2011; Jahnke et al., 2015). In recent theoretical work (Romani and Tsodyks, 2015) sharp-wave-like bursts were generated spontaneously by virtue of the spatial modulation of the recurrent connectivity, which drives an instability to traveling waves in the absence of place-field input. The presence of short-term depression modulates the amplitude of the waves, leading to narrow bursts. This is the same mechanism we have used here. Alternatively, recent work with a biophysically detailed spiking network model focused on the role of nonlinear dendritic integration on the generation of replay during SWRs (Jahnke et al., 2015). In that work the authors found that the exploration of a virtual linear track in the presence of pairwise STDP led to highly asymmetric connectivity; this could generate replay activity given a sufficiently synchronous external input which recruited nonlinear dendritic events. In our work, we have sought to explain the replay as an emergent phenomenon which depends only on the network-wide organization of synaptic structure. In doing so we have considered a simple stochastic firing rate model which allowed us to fully characterize how interplay between the plasticity rule and the place-cell activity affects learning. Nonetheless, a detailed reproduction of the phenomenology of SWRs certainly requires mechanisms we have not included here. In particular, while our model generates sharp-wave-like bursts, it does not generate high-frequency ripples, which are likely generated by networks of inhibitory interneurons in CA1 (Buzsáki, 2006).

### Spatial learning

It seems reasonable that the learning of tasks which depend on spatial information require the formation of an internal representation of the relevant environment. This is the process we have studied here. While we have not modeled any particular cognitive task, we propose that the network-wide organization of synaptic structure, in order that it be in concordance with the place-field distribution of place cells, should be a necessary step in spatial learning tasks. Our results suggest that this process is dramatically sped up by modulating place-cell activity in the theta range, which is one possible role of this prominent rhythm. Interestingly, while theta modulation is prominent in land-going rodents, it is absent in the bat (Yartsev and Ulanovsky, 2013). Although we cannot purport to know why this is, we find that it actually may be consistent with the theoretical mechanism for learning rates we put forth here. Namely, to attain a high learning rate the AC of place-cell activity should be modulated on a time-scale commensurate with the window for plasticity. In the case of land mammals like rats and mice, the behavioral time-scale related to spatial navigation may be too slow, therefore necessitating oscillatory modulation in the form of theta. In the case of flying animals, like the bat, changes in sensory input alone are already likely to occur on the order of tens to hundreds of ms due to the high velocity of flight, thereby obviating the need for theta. This speculation is based on the modulatory effect of ongoing oscillations on learning in our computational model, and is therefore not yet supported by experimental evidence. Indeed, our theoretical prediction is that more generally, for learning to occur on behaviorally relevant time scales, neuronal activity should vary somehow on a time-scale commensurate with synaptic plasticity mechanisms. One means of achieving this is to have a broad window for synaptic plasticity, on the order of seconds, so-called behavioral time-scale plasticity (Bittner et al., 2017). Alternatively, internally generated rhythms may serve to modulate neuronal activity on non-behavioral time-scales, with a similar effect.

## Materials and methods

### Network Model

We simulate a network of $N$ place-cells. The firing rate of neuron $i$ is given by

$$
\taur˙_{i}=−r_{i}+ϕ(\frac{1}{N}\sumj=1N w~_{ij}x_{j}r_{j}+I_{i}(t)),
$$

where the time constant $\tau=10$ ms and $N=100$ for all simulations except for those in Figure 6 in which $N=200$. We take $ϕ(I)=\alphaln(1+e^{I/\alpha})$ with $\alpha=1$ Hz for all simulations. The input

$$
I_{i}=I_{0}+I_{PF}cos⁡(\theta_{i}^{\mu}−x(t))(1+I_{theta}cos⁡(2\pift)),
$$

where $\theta_{i}^{\mu}$ is the center of the place field for cell $i$ on track $\mu$. These place field positions are random and uncorrelated for each cell $i$ on different tracks. The position of the animal is given by $X(t)$. For the simulations in all figures except Figure 2—figure supplement 2 the position was calculated by assuming that the velocity of the animal was random with a characteristic time constant of 10 sec. Specifically the velocity is given by $v=v_{0}+v_{1}(t)$ where the mean velocity $v_{0}=0.5$ rad/sec and

$$
\tau_{v}v˙_{1}=−v_{1}+\sigma_{v}ξ_{v}(t),
$$

where $ξ_{ν}$ is a Gaussian white-noise process with mean zero and unit variance, with $\tau_{ν}=10$ sec and $\sigma_{ν}=2$ rad/sec. The position of the animal is then given by solving $X˙=v$. For Figure 2—figure supplement 2 the velocity is taken to be a constant $v=1$ rad/sec and the position $X=vt$.

The short-term synaptic depression variable $x_{i}$ obeys

$$
x˙_{i}=\frac{(1−x_{i})}{\tau_{x}}−U_{0}x_{i}r_{i},
$$

with $\tau_{x}=800$ ms and $U_{0}=0.0008$.

#### Synaptic weights

The synaptic weight from cell $j$ to cell $i$ is $w~_{ij}=w_{ij}−w_{I}$, where $w_{I}$ represents a global inhibitory feedback. The weights $w_{ij}$ are plastic and evolve according to a spike-timing dependent plasticity rule. In order to generate spike trains we take the firing rates of the cells as the underlying rates for a Poisson process. Specifically, the probability that a cell $i$ produces a spike in a given time step $Δt≪1$ is defined as $Pr(spike)=r_{i}(t)Δt$.

We consider a simple pairwise STDP rule (Kempter et al., 1999). To implement this numerically, if we take the point of view of a neuron $i$, which receives synaptic input from a neuron $j$, then the weight $w_{ij}$ will change value for each pre-post spike pair. Specifically, the weight is strengthened every time there is a post-synaptic spike. The amount it is strengthened by depends on the how long ago the pre-synaptic spike occurred. If it is discounted exponentially then we need only take into account a presynaptic variable $r_{j}$, where

$$
r˙_{j}=−\frac{r_{j}}{\tau_{+}}+S_{j}(t),
$$

and $S_{j}(t)=\sumk \delta(t−t_{j}^{k})$ is the train of spikes emitted by neuron $j$. Then, when the postsynaptic spike occurs at time $t$ we increase $w_{ij}→w_{ij}+A_{+}r_{j}(t)$. Similarly, $w_{ij}$ is weakened whenever there is a presynaptic spike by an amount which depends on the spike times of the postsynaptic neuron $i$. Therefore, we can keep track of a postsynaptic variable $o_{i}$, where

$$
o˙_{i}=−\frac{o_{i}}{\tau_{−}}+S_{i}(t),
$$

and everytime there is a presynaptic spike at time t we update $w_{ij}→w_{ij}−A_{−}o_{i}(t)$. Weights are bounded below by zero and above by $w_{max}$. This fully characterizes the plasticity rule. The parameters $A_{+}=0.1$, $\tau_{+}=20$ ms, $A_{−}=0.1/3$, $\tau_{−}=60$ ms unless otherwise stated.

##### Initial Condition

The weight matrix $w_{ij}$ was trained by simulating exploration on 10 distinct linear tracks for one hour each. The value of $w_{ij}$ was taken as a constant 40 for all synapses at the beginning of exploration of the first environment and the maximum possible weight was set at $w_{max}=80$. See Figure 2—figure supplement 1 for statistics of the synaptic weights during the training process. For the connectivity profiles, we calculate the mean synaptic weight between pairs of neurons with a difference in place field location $Δ\theta$ at the given time of the snapshot. There are no autapses, but the curve is made continuous at $Δ\theta$ by interpolating between adjacent points. The connectivity is normalized by subtracting the mean and dividing by 40.

##### Details for Figure 2

To generate the figure in Figure 2b we calculate the SC in 1 s bins during the entire simulation. Every 180 s there is a 3 s period during which the external theta-modulated place field input is removed, in order to model awake quiescence. Activity during this period is spontaneous and is considered to be bursts (black circles). During burst activity we only calculate the SC for the second and third seconds because it takes some time for the place field activity to die away and the burst activity to emerge, for example SC for bursts is calculated for seconds 181–182 and 182–183 but not for 180–181. For the simulation in Figure 2b the place field input is simply removed when the animal stops, that is the external input is set to a constant value of $I_{0}=3$ Hz while for Figure 2c it is set to $I_{0}=−0.75$ Hz. Changing $I_{0}$ does not significantly affect the value of SC, only the degree of burstiness of the spontaneous activity, see Figure 2—figure supplement 7. The inset in Figure 2b was generated by binning the SC of the total network activity into 3 min bins. The ‘LFP’ in Figure 2c is the network-averaged input current to the neurons, that is the network-average of the argument in the firing rate equations. Additional parameters are: $I_{0}=3$ Hz, $I_{PF}=25$ Hz, $I_{theta}=1$, $f=8$ Hz, $w_{I}=65$.

##### Details for Figure 3

The curves shown in Figure 3a are a cartoon meant to illustrate how the recurrent connectivity can be decomposed into a spatial Fourier series which include even (cosine) and odd (sine) terms. The amplitude of an even term (its coefficient) can lead to a transition in the network dynamics when it reaches a critical value. In Figure 3c the coefficients $w_{even}$ and $w_{odd}$ are the first cosine and sine Fourier coefficients of the mean recurrent connectivity are calculated as in Figure 2 at a given time during the simulation. Parameters in (c) are the same as in Figure 2.

##### Details for Figure 4

The parameters in (a) and (b) are the same as in Figure 2. Parameters in (c) and (d) are the same as in Figure 2 with the sole exception of the STDP rule. For the anti-symmetric case (c) the parameters are $A_{+}=0.1$, $\tau_{+}=40$ ms, $A_{−}=0.1$, $\tau_{−}=40$ ms while for (d) they are $A_{−}=0.1$, $\tau_{+}=20$ ms, $A_{+}=0.1/3$, $\tau_{−}=60$ ms.

##### Details for Figure 6

The virtual animal has explored thirty distinct environments for one hour each. In each environment the coding level is one half, that is one half of the neurons are modeled as place cells (randomly assigned place field location from uniform distribution around the track) and the other half receive only constant background input with $I_{0}=0$ Hz. Plasticity occurs via STDP as before between all cell pairs. Place cells in any given environment are chosen randomly with equal probability; hence the overlap in place-cell representation between any two environments is on average one half. The number of neurons is N = 200, so that in any environment there are still 100 place cells, as in previous simulations.

### Derivation of continuous learning rule from pairwise and triplet STDP rule

#### Pairwise rule

We can write down an approximate description for the evolution of $w_{ij}$ which is accurate if the STDP occurs much more slowly than changes in the firing rates (see Kempter et al. PRE 1999 for details). For the case of inhomogeneous Poisson processes the equation is

$$
w˙_{ij}=−A_{−}\int_{−∞}^{0} dT⋅e^{T/\tau_{−}}r_{j}(t)r_{i}(t+T)+A_{+}\int_{0}^{∞} dT⋅e^{−T/\tau_{+}}r_{j}(t−T)r_{i}(t).
$$

As we are only interested in the evolution of the weights on a long time-scale (longer than the time-scale of fluctuations in the rates) we will consider the time averaged equation

$$
⟨w˙_{ij}⟩_{t}=−A_{−}\int_{−∞}^{0} dT⋅e^{T/\tau_{−}}⟨r_{j}(t)r_{i}(t+T)⟩_{t}+A_{+}\int_{0}^{∞} dT⋅e^{−T/\tau_{+}}⟨r_{j}(t−T)r_{i}(t)_{t}⟩.
$$

For a stationary process we have $⟨r_{j}(t−T)r_{i}(t)⟩_{t}=⟨r_{j}(t)r_{i}(t+T)⟩_{t}$. Therefore, as long as we restrict our analysis to stationary processes (which is the case here), we can write (Equation 15) in the compact form

$$
w˙_{ij}=\int_{−∞}^{∞} dT⋅K(T)r_{j}(t)r_{i}(t+T),
$$



$$
K(T)={A_{+}e^{−T/\tau_{+}}if T\geq0−A_{−}e^{T/\tau_{−}}if T<0.
$$

If neurons are arranged along a periodic track and can be parameterized according to their position (phase) $\theta$, then (Equation 16) becomes (Equation 3). Note that (Equation 3) is only used for analysis. Plasticity in the numerical simulations is modeled as described in the preceding section.

#### Triplet rule

The STDP rule which depends only on spike pairs cannot account for some general experimental findings, including the dependence of LTP on presentation frequency. A triplet rule can describe these effects (Pfister and Gerstner, 2006). The triplet rule is implemented as above, but by adding one additional variable to keep track of per neuron. Specifically, we rename the previous pre-synaptic and post-synaptic variables $o_{1}$ and $r_{1}$ and add two more $o_{2}$ and $r_{2}$. Now if there is a spike in neuron $i$ at time $t$, then the weight $w_{ij}$ is potentiated by an amount $r_{1,j}(A_{2}^{+}+A_{3}^{+}o_{2,i}(t−ϵ))$, where the $ϵ$ means that you take the value of the post-synaptic variable $o_{2}$ before it is incremented due to the spike. Similarly, the weight $w_{ji}$ is depressed by an amount $o_{1,j}(t)(A_{2}^{−}+A_{3}^{−}r_{2,i}(t−ϵ))$.

One can write an equation similar to (Equation 3) for the triplet rule, which is exact if the learning is slow compared to the rate dynamics. The full equation, with pairwise and triplet interactions is

$$
w˙_{ij}=\int_{−∞}^{∞} d\tauK_{11}(\tau)r_{i}(t)r_{j}(t+\tau)−A_{3}^{−}\int_{0}^{∞} d\tau_{1}\int_{0}^{∞} d\tau_{2}e^{−\tau_{1}/\tau_{−}}e^{−\tau_{2}/\tau_{x}}r_{i}(t)r_{j}(t−\tau_{1})r_{i}(t−\tau_{2})+A_{3}^{+}\int_{0}^{∞} d\tau_{1}\int_{0}^{∞} d\tau_{2}e^{−\tau_{1}/\tau_{+}}e^{−\tau_{2}/\tau_{y}}r_{j}(t)r_{i}(t−\tau_{1})r_{j}(t−\tau_{2}).
$$

The kernel $K_{11}$ is just the standard pairwise one from before, where we write 11 to mean ‘one presynpatic spike and one postsynaptic spike’. The kernel $K_{12}$ is the one for ‘two presynaptic spikes and one postsynaptic spike’. The STDP rule is multiplicative, that is the potentiation due to the triplet is the product of $r_{1}$ and $o_{2}$ which implies that $K_{21}(\tau_{1},\tau_{2})=K_{11}(\tau_{1})K~_{21}(\tau_{2})$, where $\tau_{1}=t_{pre}−t_{post,2}$ and $\tau_{2}=t_{post,1}−t_{post,2}$, so $\tau_{1}\leq0$ and $\tau_{2}\leq0$, and we are only integrating over the potentiating part of $W_{11}$ which is also clear from the STDP rule.

### Plasticity in network of place cells on periodic track

We first consider a simple case where the place cell activity is given by $r(\theta,t)=r_{0}+r_{PF}cos⁡(\theta−vt)$, that is the rate dynamics trivially follow the motion of the virtual animal and are not ‘theta’-modulated. Also, we are taking a continuum limit in which the index of a neuron $i$ is replaced with the position of its place field along the track $\theta$. In (Equation 3) we have the product

$$
r(\theta,t)r(\theta^{′^{}},t+T)=r_{0}^{2}+r_{PF}^{2}cos⁡(\theta−vt)cos⁡(\theta^{′^{}}−vt−vT)+f(t),=r_{0}^{2}+r_{PF}^{2}cos⁡(\theta−\theta^{′^{}}+vT)+f(t),=r_{0}^{2}+\frac{r_{PF}^{2}}{2}(cos⁡(\theta−\theta^{′^{}})cos⁡(vT)+sin⁡(\theta−\theta^{′^{}})sin⁡(vT))+f(t),
$$

where $f(t)$ is a time-periodic function. The first two terms in (Equation 18) will therefore determine the mean growth of the even and odd modes of the connectivity on a slow time-scale, while the remainder will lead to fluctuations about this mean on a faster time scale. (This time-scale separation will be conducted more formally in a later section) Averaging over the fast time eliminates these fluctuations. Therefore the rate of change of the connectivity can be expressed as

$$
⟨w˙⟩_{t}(\theta−\theta^{′^{}})=w˙_{0}+w˙_{even}cos⁡(\theta−\theta^{′^{}})+w˙_{odd}sin⁡(\theta−\theta^{′^{}}),
$$

where the brackets on the l.h.s. indicate that we have taken a time-average to eliminate time-oscillating terms. Therefore, (Equation 3) reduces to

$$
w˙_{0}=r_{0}^{2}\int_{−∞}^{∞} dT⋅K(T),
$$



$$
w˙_{even}=\frac{r_{PF}^{2}}{2}\int_{−∞}^{∞} dT⋅K(T)cos⁡(vT),
$$



$$
w˙_{odd}=\frac{r_{PF}^{2}}{2}\int_{−∞}^{∞} dT⋅K(T)sin⁡(vT).
$$

Performing these integrals gives

$$
w˙_{0}=(A_{+}\tau_{+}−A_{−}\tau_{−})r_{0}^{2},
$$



$$
w˙_{even}=\frac{r_{PF}^{2}}{2}[\frac{A_{+}\tau_{+}}{1+\tau_{+}^{2}v^{2}}−\frac{A_{−}\tau_{−}}{1+\tau_{−}^{2}v^{2}}],
$$



$$
w˙_{odd}=\frac{r_{PF}^{2}}{2}[\frac{A_{+}\tau_{+}^{2}v}{1+\tau_{+}^{2}v^{2}}+\frac{A_{−}\tau_{−}^{2}v}{1+\tau_{−}^{2}v^{2}}].
$$

We see from (Equation 22) that the balance condition $A_{+}\tau_{+}=A_{−}\tau_{−}$ must hold to avoid the synapses from all reaching their maximum or minimum value. At this point we would also note that for any reasonable velocity the growth rate of the even mode is extremely small and far from the maximal possible growth rate. Specifically, the velocity has unit of radians. For a three meter track, a rat running at 50 cm/s would have a velocity of about 1 rad/sec. Typical time scale for STDP are 50 ms or 0.05 s. Therefore the non-dimensional quantity $\tau^{2}v^{2}=0.0025≪1$ and, given the balance condition, $w˙_{even}∼0$.

Including the triplet interactions by using (Equation 17) gives

$$
w˙_{0}=(A_{+}\tau_{+}−A_{−}\tau_{−})r_{0}^{2}+A_{3}^{+}[\tau_{+}\tau_{y}r_{0}^{3}+\frac{\tau_{+}\tau_{y}r_{0}r_{PF}^{2}}{2(1+\tau_{y}^{2}v^{2})}]−A_{3}^{−}[\tau_{−}\tau_{x}r_{0}^{3}+\frac{\tau_{−}\tau_{x}r_{0}r_{PF}^{2}}{2(1+\tau_{x}^{2}v^{2})}],
$$



$$
w˙_{even}=\frac{r_{PF}^{2}}{2}[\frac{A_{+}\tau_{+}}{1+\tau_{+}^{2}v^{2}}−\frac{A_{−}\tau_{−}}{1+\tau_{−}^{2}v^{2}}]+A_{3}^{+}\frac{\tau_{+}\tau_{y}r_{0}r_{PF}^{2}}{2(1+\tau_{+}^{2}v^{2})}[1+\frac{(1+\tau_{+}\tau_{y}v^{2})}{(1+\tau_{y}^{2}v^{2})}]−A_{3}^{−}\frac{\tau_{−}\tau_{x}r_{0}r_{PF}^{2}}{2(1+\tau_{−}^{2}v^{2})}[1+\frac{(1+\tau_{−}\tau_{x}v^{2})}{(1+\tau_{x}^{2}v^{2})}],
$$



$$
w˙_{odd}=\frac{r_{PF}^{2}}{2}[\frac{A_{+}\tau_{+}^{2}v}{1+\tau_{+}^{2}v^{2}}+\frac{A_{−}\tau_{−}^{2}v}{1+\tau_{−}^{2}v^{2}}]+A_{3}^{+}\frac{\tau_{+}\tau_{y}vr_{0}r_{PF}^{2}}{2(1+\tau_{+}^{2}v^{2})}[\tau_{+}+\frac{(\tau_{+}−\tau_{y})}{1+\tau_{y}^{2}v^{2}}]+A_{3}^{−}\frac{\tau_{−}\tau_{x}vr_{0}r_{PF}^{2}}{2(1+\tau_{−}^{2}v^{2})}[\tau_{−}+\frac{(\tau_{−}−\tau_{x})}{1+\tau_{x}^{2}v^{2}}]
$$

From (Equation 25) we see there are two additional balance conditions to avoid saturation or decay to zero of synaptic weights: $\tau_{x}=\tau_{y}$ and $A_{3}^{+}\tau_{+}\tau_{y}=A_{3}^{−}\tau_{−}\tau_{x}$. Once we apply the balance conditions the growth rate of the mean connectivity $w_{0}$ is identically zero.

### Including periodic modulation

Here we consider the case where the place cell activity is modulated periodically with a frequency $f$, that is $r(t)=r_{0}+r_{PF}cos⁡(\theta−vt)(1+r_{theta}cos⁡(2\pift))$. This can be rewritten as

$$
r(t)=r_{0}+r_{PF}cos⁡(\theta−vt)+\frac{r_{PF}r_{theta}}{2}(cos⁡(\theta−v_{+}t)+cos⁡(\theta−v_{−}t)),
$$

where $v_{+}=v+2\pif$ and $v_{−}=v−2\pif$. Now when we plug (Equation 28) into (Equation 3) or (Equation 17) we find that each of the three cosine terms makes an independent contribution. The reason is that the cross terms (which arise due to the product of rates) lead to time periodic terms which vanish once we average the equation. Therefore we end up with equations of the form (Equation 22–24) or (Equations 25–27) but with three times the number of terms, that is for $v$, $v_{+}$ and $v_{−}$. These equations can, however, be simplified by considering the limit where the ratio $ϵ=\frac{v}{2\pif}≪1$. For example, when $f=8$ Hz and $v=1$ rad/sec (50 cm/sec on a three meter track) then $\frac{v}{2\pif}∼0.02$. Slower running speeds or faster oscillations will make the following approximation even more accurate. In this limit we have (for the pairwise rule)

$$
w˙_{even}=\frac{r_{PF}^{2}A_{+}\tau_{+}}{2}[\frac{1}{1+\tau_{+}^{2}v^{2}}−\frac{1}{1+\tau_{−}^{2}v^{2}}]+r_{PF}^{2}r_{theta}^{2}A_{+}\tau_{+}[\frac{1}{1+4\pi^{2}\tau_{+}^{2}f^{2}}−\frac{1}{1+4\pi^{2}\tau_{−}^{2}f^{2}}]+𝒪(ϵ^{2}),
$$



$$
w˙_{odd}=\frac{r_{PF}^{2}A_{+}\tau_{+}}{2}[\frac{\tau_{+}v}{1+\tau_{+}^{2}v^{2}}+\frac{\tau_{−}v}{1+\tau_{−}^{2}v^{2}}]+𝒪(ϵ).
$$

Furthermore, given that $\tauv$ is also a small parameter, we can neglect the first term in (Equation 29), which means that the growth rate of the even mode is entirely dominated by the modulation frequency to leading order. Because $f$ could take on any value the $w˙_{even}$ need not be close to zero. In fact, there is a critical value of f which maximizes the growth rate $f=\frac{1}{2\pi\sqrt{\tau_{+}\tau_{−}}}$. On the other hand the growth of the odd mode is not dependent on the modulation frequency to leading order, but only on the motion of the animal.

### Coupled rate dynamics and synaptic plasticity

Now we return to the full problem, namely, (Equations 1–3) and we take $ϕ$ to be linear for simplicity. In principle (Equations 1–3) are extremely challenging to analyze by virtue of the nonlinear combinations of the rates and the connectivity, both of which evolve in time. However, if we assume that the connectivity evolves much more slowly than the rates, the problem simplifies considerably. Specifically, we assume that the changes to the synaptic weights due to each spike pair are small. Formally, we can introduce a small parameter $ϵ$ and write $A_{+}=ϵA~_{+}$ and $A_{−}=ϵA~_{−}$, and so $K(T)=ϵK~(T)$, where all of the ‘tilded’ quantities are order one. In the limit $ϵ→0$ we would then find that (Equation 1) is unchanged while (Equation 3) becomes $w˙(\theta−\theta^{′^{}})=0$, that is the connectivity is a constant. This clearly is an approximation since the connectivity will change over time, just slowly. In fact it is precisely this slow evolution that we would like to describe. In order to do this we can define a new, slow time $\tau_{s}=ϵt$ and allow both the firing rate and the connectivity to evolve on both the fast and the slow time scales, which are now taken to be independent. This is known as a multi-scale approach.

Formally we make the following ansatz

$$
w=w_{0}(\theta−\theta^{ ′},t_{s},t)+ϵw_{1}(\theta−\theta^{ ′},t_{s},t)+ϑ(ϵ^{2}),
$$



$$
r=r_{0}(\theta,t_{s},t)+ϵr_{1}(\theta,t_{s},t)+ϑ(ϵ^{2}),
$$

where $t_{s}=ϵt$. Therefore, the temporal derivatives in (Equations 1–3) can be written $r˙=∂_{t}r+ϵ∂_{t_{s}}r$ by using the chain rule. This leads to the system of equations

$$
\tau(∂_{t}+ϵ∂_{t_{s}})(r_{0}+ϵr_{1}+…)=−r_{0}−ϵr_{1}−…+\frac{1}{2\pi}\int−\pi\pi d\theta^{′^{}}(w_{0}+ϵw_{1}+…)(r_{0}+ϵr_{1}+…)+I(\theta,t),
$$



$$
(∂_{t}+ϵ∂_{t_{s}})(w_{0}+ϵw_{1})=ϵ\int−∞∞ dTK~(T)(r_{0}(\theta,t)+ϵr_{1}(\theta,t)+…),(r_{0}(\theta^{′^{}},t+T)+ϵr_{1}(\theta^{′^{}},t+T)+…)
$$

To leading order we have the equations

$$
\tau\partial_{t}r_{0}=−r_{0}+\frac{1}{2\pi}\int−\pi\pi d\theta^{ ′}w_{0}(\theta−\theta^{ ′})r_{0}(\theta^{ ′})+I(\theta,t),
$$



$$
\partial_{t}w_{0}(\theta−\theta^{ ′})=0.
$$

(Equation 36) shows that, to leading order, the connectivity is independent of the fast time $t$, that is $w_{0}=w_{0}(\theta−\theta^{ ′},t_{s})$. Given this, the term $w_{0}$ can be treated as a constant in (Equation 35), and the rate is given by $r_{0}=r_{0}(\theta,t_{s},t)$. At order $ϑ(ϵ)$ the equations are

$$
\tau\partial_{t_{s}}r_{0}+\tau\partial_{t}r_{1}=−r_{1}+\frac{1}{2\pi}\int−\pi\pi d\theta^{ ′}(w_{1}r_{0}+w_{0}r_{1}),
$$



$$
∂_{t_{s}}w_{0}+∂_{t}w_{1}=\int−∞∞ dTK~(T)r_{0}(\theta,t_{s},t)r_{0}(\theta^{′^{}},t_{s},t+T).
$$

The solution to (Equation 37), $r_{1}$ gives the next order correction to the firing rates. On the other hand, (Equation 38) would seem to require solving for both $w_{0}$ and $w_{1}$ simultaneously. However, we note that the product of rates $r_{0}(\theta,t_{s},t)r_{0}(\theta^{ ′},t_{s},t+T)$ can actually be written as $g(\theta−\theta^{ ′},t_{s};T)+f(\theta−\theta^{ ′},t_{s},t;T)$. That is, there is a part which is independent of time, except for the dependence of the slow time through the connectivity, and a part which varies on a regular, non-slow time scale. This fast, time-varying part, has zero mean (it is periodic here) and hence can be eliminated by averaging on an appropriate intermediate time scale, which is still much faster than the slow time scale, that is $⟨f⟩_{t}=0$. Therefore, we can define $w_{1}$ as that component of the connectivity which is driven by $f$, and hence also will have zero mean and will vanish upon averaging. Finally, combining the order one equation for the rate and the averaged order epsilon equation for the connectivity yields

$$
\tau\partial_{t}r_{0}=−r_{0}+\frac{1}{2\pi}\int−\pi\pi d\theta^{ ′}w_{0}(\theta−\theta^{ ′})r_{0}(\theta^{ ′})+I(\theta,t),
$$



$$
∂_{t_{s}}w_{0}(\theta−\theta^{′^{}})=\int−∞∞ dTK~(T)f(\theta−\theta^{′^{}},t_{s};T)..
$$

(Equations 39 and 40) are the system we wish to solve here. We first note that the connectivity can always be decomposed into a Fourier series. Anticipating the fact that the only terms which will not have zero mean in time will be the first cosine and sine terms, we write

$$
w_{0}(\theta−\theta^{′^{}},t_{s})=w_{0}(t_{s})+w_{even}(t_{s})cos⁡(\theta−\theta^{′^{}})+w_{odd}(t_{s})sin⁡(\theta−\theta^{′^{}}),
$$

Given that the forcing term can be written

$$
I(\theta,t)=I_{0}+I_{PF}cos⁡(\theta−vt)+I_{PF}I_{theta}(cos⁡(\theta−v_{+}t)+cos⁡(\theta−v_{−}t)).
$$

then the firing rates $r_{0}$ will be

$$
r_{0}(\theta,t)=r~_{0}+r_{even}cos⁡(\theta−vt)+r_{odd}sin⁡(\theta−vt)+r_{even}^{+}cos⁡(\theta−v_{+}t)+r_{odd}^{+}sin⁡(\theta−v_{+}t)+r_{even}^{−}cos⁡(\theta−v_{−}t)+r_{odd}^{−}sin⁡(\theta−v_{−}t),
$$

where, after some linear algebra one finds

$$
r~_{0}=\frac{I_{0}}{1−w_{0}},
$$



$$
r_{even}=\frac{I_{PF}(1−w_{even}/2)}{(1−w_{even}/2)^{2}+(w_{odd}/2−\tauv)^{2}},
$$



$$
r_{odd}=\frac{I_{PF}(w_{odd}/2−\tauv)}{(1−w_{even}/2)^{2}+(w_{odd}/2−\tauv)^{2}},
$$



$$
r_{even}^{+}=\frac{I_{PF}I_{theta}(1−w_{even}/2)/2}{(1−w_{even}/2)^{2}+(w_{odd}/2−\tauv_{+})^{2}},
$$



$$
r_{odd}^{+}=\frac{I_{PF}I_{theta}(w_{odd}/2−\tauv_{+})/2}{(1−w_{even}/2)^{2}+(w_{odd}/2−\tauv_{+})^{2}},
$$



$$
r_{even}^{−}=\frac{I_{PF}I_{theta}(1−w_{even}/2)/2}{(1−w_{even}/2)^{2}+(w_{odd}/2−\tauv_{−})^{2}},
$$



$$
r_{odd}^{−}=\frac{I_{PF}I_{theta}(w_{odd}/2−\tauv_{−})/2}{(1−w_{even}/2)^{2}+(w_{odd}/2−\tauv_{−})^{2}}.
$$

Taking the product of the rates and keeping only those terms with non-zero mean yields the function $f$, which when plugged into (Equation 40) gives

$$
w˙_{0}=(A_{+}\tau_{+}−A_{−}\tau_{−})r_{0}^{2},
$$



$$
w˙_{even}=\frac{r_{even}^{2}+r_{odd}^{2}}{2}[\frac{A_{+}\tau_{+}}{1+\tau_{+}^{2}v^{2}}−\frac{A_{−}\tau_{−}}{1+\tau_{−}^{2}v^{2}}]+\frac{(r_{even}^{+})^{2}+(r_{odd}^{+})^{2}}{2}[\frac{A_{+}\tau_{+}}{1+\tau_{+}^{2}v_{+}^{2}}−\frac{A_{−}\tau_{−}}{1+\tau_{−}^{2}v_{+}^{2}}]+\frac{(r_{even}^{−})^{2}+(r_{odd}^{−})^{2}}{2}[\frac{A_{+}\tau_{+}}{1+\tau_{+}^{2}v_{−}^{2}}−\frac{A_{−}\tau_{−}}{1+\tau_{−}^{2}v_{−}^{2}}],
$$



$$
w˙_{odd}=\frac{r_{even}^{2}+r_{odd}^{2}}{2}[\frac{A_{+}\tau_{+}^{2}v}{1+\tau_{+}^{2}v^{2}}+\frac{A_{−}\tau_{−}^{2}v}{1+\tau_{−}^{2}v^{2}}]+\frac{(r_{even}^{+})^{2}+(r_{odd}^{+})^{2}}{2}[\frac{A_{+}\tau_{+}^{2}v_{+}}{1+\tau_{+}^{2}v_{+}^{2}}+\frac{A_{−}\tau_{−}^{2}v_{+}}{1+\tau_{−}^{2}v_{+}^{2}}]+\frac{(r_{even}^{−})^{2}+(r_{odd}^{−})^{2}}{2}[\frac{A_{+}\tau_{+}^{2}v_{−}}{1+\tau_{+}^{2}v_{−}^{2}}+\frac{A_{−}\tau_{−}^{2}v_{−}}{1+\tau_{−}^{2}v_{−}^{2}}].
$$

In the limit $v/(2\pif)≪1$ the leading order terms of (Equations 44 and 45) are given by (Equations 6 and 7).

The solution for the triplet rule can be similarly found by replacing $r_{PF}$ in (Equations 25–27) by $(r_{even}^{2}+r_{odd}^{2})/2$ as well as the analogous terms corresponding to $v_{+}$ and $v_{−}$.

### Motion with non-uniform velocity

Up until now we have considered a constant velocity $v$ for ease in calculation. In reality, the motion of the animal will be much more erratic, with both positive and negative speeds during the exploration of the track. In the extreme case of a random walk, in which both clockwise (CW) and counterclockwise (CCW) motion is equally likely, the resulting connectivity is much more symmetric. This occurs because contributions from CW and CCW motion to the even mode simply add, while the same contributions to the odd mode cancel out. We can illustrate this more clearly by considering the continuum learning rule, (Equation 3), with a given distribution of velocities. Specifically, we take the simple case where the firing rates can be written $r_{0}+r_{PF}cos⁡(\theta−vt)$ (we have seen that the solution to the full model can be written in an analogous way to the solution of this simpler problem) and assume a distribution of firing rates $ρ(v)$. From (Equations 20 and 21) we have

$$
w˙_{even}=\int_{−∞}^{∞} dvρ(v)\int_{−∞}^{∞} dT⋅K(T)cos⁡(vT)=\int_{−∞}^{∞} dT⋅K(T)\int_{−∞}^{∞} dvρ(v)cos⁡(vT),
$$



$$
w˙_{odd}=\int_{−∞}^{∞} dT⋅K(T)\int_{−∞}^{∞} dvρ(v)sin⁡(vT).
$$

If we choose $ρ(v)=\delta(v−v^{∗})$, that is, a fixed velocity $v^{∗}$, then we recover our results from previous sections. We can allow for a range of velocities by considering a uniform distribution of velocities, that is

$$
ρ(v)={\frac{1}{2v^{∗}},|v|\leqv^{∗}0,|v|>v^{∗}.
$$

For this choice of distribution we find $w˙_{even}=\int_{−∞}^{∞} dT⋅K(T)\frac{sin⁡(v^{∗}T)}{v^{∗}T}$, while $w˙_{odd}=0$. The function $sin⁡(x)/x$ is even and decays more slowly than $cos⁡(x)$ around zero lag, meaning that the AC of the firing rate is qualitatively similar whether $v$ is a constant or distributed. On the other hand, the CC of neurons with disparate place field location will be zero on average if the animal samples both directions equally. Nonetheless, any asymmetry in the velocity distribution (which is expected for any finite length of exploration) will lead to a non-zero odd mode in the connectivity.

### A traveling wave instability of the rate equation for modulated connectivity

In the previous sections we have seen how the connectivity grows in time due to the non-stationarity of the firing rates. In particular, the AC of the place-cell activity drives growth of the even mode, and this growth depends on the STDP rule parameters and the modulation (theta) frequency. Here we show that once the amplitude of the even mode reaches a critical value there is an instability of the network activity in the absence of place field input, which gives rise to spontaneous traveling waves. This is the origin of replay activity in the model.

We consider the firing rate equation in the absence of place field input, that is spontaneous dynamics.

$$
\taur˙(\theta,t)=−r(\theta,t)+ϕ(\frac{1}{2\pi}\int_{−\pi}^{\pi} d\theta^{′^{}}w(\theta−\theta^{′^{}})r(\theta^{′^{}},t)+I_{0}),
$$

and a small perturbation about a steady state solution of the form $r(\theta,t)=r_{0}+(\deltar_{0}+\deltar_{even}cos⁡(\theta)+\deltar_{odd}sin⁡(\theta))e^{\lambdat}$. Plugging this into (Equation 49) leads to a characteristic equation for $\lambda$ the solutions of which are

$$
\tau\lambda=−(1−\frac{w_{even}}{2}ϕ^{ ′})\pmi\frac{w_{odd}}{2}ϕ^{ ′}.
$$

Therefore when $w_{even}>2/ϕ^{ ′}$ there is an oscillatory instability with frequency $\omega=\frac{w_{odd}}{2\tau}ϕ^{ ′}$.

### Including the effects of synaptic depression

A general study of the dynamics in recurrent networks with a ring topology and synaptic depression can be found in (York and van Rossum, 2009). Here we outline several calculations which are relevant for our model in the context of plasticity and replay.

#### Evolution of recurrent connectivity

Synaptic depression is included in the model in order to generate burst-like activity during awake quiescent periods. The equations are

$$
\taur˙=−r+ϕ(\frac{1}{2\pi}\int_{−\pi}^{\pi} d\theta^{′^{}}w(\theta−\theta^{′^{}})x(\theta^{′^{}},t)r(\theta^{′^{}},t)+I(\theta,t)),
$$



$$
x˙=\frac{1−x}{\tau_{x}}−U_{0}xr,
$$



$$
w˙(\theta−\theta^{′^{}})=\int_{−∞}^{∞} dTK(T)r(\theta,t)r(\theta^{′^{}},t+T)
$$

Here we note that the quadratic nonlinearities $xr$ in (Equations 51 and 52) make it impossible to find a closed form solution. However, we also note that the growth rate of the first even mode of the connectivity will still depend only on the product of the STDP window with the autocorrelation (AC) of the firing rate, as before. Therefore, the modulation of the firing rate due to the theta rhythm, the resulting shape of the AC, and its consequence for the growth rate: maximal growth for intermediate frequencies commensurate with the STDP window, is qualitatively the same.

If we assume the place field input is weak, that is $I(\theta,t)=I_{0}+I_{PF}cos⁡(\theta−vt)$, where $I_{PF}≪1$, then we can linearize the solution. In this case we can write $r(t)=r_{0}+r_{even}cos⁡(\theta−vt)+r_{odd}sin⁡(\theta−vt)$ and $x(t)=x_{0}+x_{even}cos⁡(\theta−vt)+x_{odd}sin⁡(\theta−vt)$, and the product

$$
xr=x_{0}r_{0}+(x_{0}r_{even}+r_{0}x_{even})cos⁡(\theta−vt)+(x_{0}r_{odd}+r_{0}x_{odd})sin⁡(\theta−vt),=r~_{0}+r~_{even}cos⁡(\theta−vt)+r~_{odd}sin⁡(\theta−vt)+h.o.t.
$$

where ‘h.o.t.’ means higher order terms. Plugging this into (Equation 52) gives the solution to x in terms of r

$$
x_{0}=\frac{1}{1+\tau_{x}U_{0}r_{0}},
$$



$$
x_{even}=−U_{0}\frac{(v\tau_{x}r_{odd}+(1+\tau_{x}U_{0}r_{0})r_{even})}{(1+\tau_{x}U_{0}r_{0})(v^{2}\tau_{x}^{2}+(1+\tau_{x}U_{0}r_{0})^{2})},
$$



$$
x_{odd}=−U_{0}\frac{(−v\tau_{x}r_{even}+(1+\tau_{x}U_{0}r_{0})r_{odd})}{(1+\tau_{x}U_{0}r_{0})(v^{2}\tau_{x}^{2}+(1+\tau_{x}U_{0}r_{0})^{2})}.
$$

Now we plug the expansion (Equation 54) into (Equation 51). Doing so yields the following nonlinear algebraic equations

$$
r_{0}=\frac{w_{0}r_{0}}{1+\tau_{x}U_{0}r_{0}}+I_{0},
$$



$$
vr_{even}=−r_{odd}+\frac{1}{2}(w_{even}r~_{odd}+w_{odd}r~_{even}),
$$



$$
−vr_{odd}=−r_{even}+\frac{1}{2}(w_{even}r~_{even}−w_{odd}r~_{odd}),
$$

which can be solved to find $r_{0}$, $r_{even}$ and $r_{odd}$. This analysis has been carried out without periodic modulation of the input. Including periodic modulation with frequency $f$ once again just leads to two equivalent sets of algebraic equations for $v_{+}=v+2\pif$ and $v_{−}=v−2\pif$. Then, the self-consistent equations for the growth rates of the connectivity are just (Equations 43–45), where the $r$s are replaced by the $r~$s calculated above.

#### Linear stability of spontaneous activity

To study the stability of the spontaneous state we consider (Equations 51 and 52) with constant input $I=I_{0}$. We consider perturbations of the steady state solution of the form $r(t)=r_{0}+(\deltar_{0}+\deltar_{even}cos⁡(\theta)+\deltar_{odd}sin⁡(\theta))e^{\lambdat}$, and $x(t)=x_{0}+(\deltax_{0}+\deltax_{even}cos⁡(\theta)+\deltax_{odd}sin⁡(\theta))e^{\lambdat}$. Plugging these formulas into (Equations 51 and 52) yields a fourth-order characteristic equation for the eigenvalues associated with the spatially modulated modes. In the limit $U_{0}≪1$ and $1/\tau_{x}≪1$, which is always the case in our simulations, this equation reduces to a quadratic equation, the solution of which is

$$
\tau\lambda=−(1−\frac{w_{even}x_{0}}{2}ϕ^{ ′})\pmi\frac{w_{odd}x_{0}}{2}ϕ^{ ′},
$$

which is similar to the case without synaptic depression, (Equation 50), with the sole difference that the connectivity is multiplied by the the depression variable in the steady state $x_{0}$. Therefore there again is an instability to traveling waves, but the effective recurrent connectivity is weakened by the synaptic depression, thereby shifting the instability. When there is no depression $x_{0}=1$ and we recover the previous result.

### Analysis of data from hippocampal recordings

We analyzed data collected from hippocampal recordings using bilateral silicon probes from two distinct sets of experiments. In the first set two rats had their medial septa reversibly inactivated through injection of muscimol and were then exposed to a novel square, periodic track for 35 min (Wang et al., 2015). After a recovery period they were re-introduced onto the same track for an additional 35 min. In the second set of experiments two rats were exposed to a novel hexagonal track for 35 min in a first session. Thereafter they were placed back onto the same track for two additional 35 min sessions with a rest period in between each session.

#### Medial septum inactivation experiments

There were a total of n = 124 and n = 128 cells from rats A991 and A992 respectively. In order to identify place cells we first calculated a rate map on the track for each neuron, and then linearized the rate to obtain a one-dimensional place field. We then fit the place field with the function $r=r_{0}+r_{1}cos⁡(\theta−ϕ_{1})+r_{2}cos⁡2(\theta−ϕ_{2})$ thereby extracting the coefficients of the Fourier modes and their phases, see Figure 7—figure supplement 1a and b and Figure 7—figure supplement 2. We also extracted the coefficients via Fast-Fourier Transform and found identical results. We did not find any cells for which $r_{2}$ was significant compared to the first two coefficients and hence limited our analysis to the first two coefficients and the phase, that is the place field was centered at $ϕ_{1}$. We excluded all cells for which the tuning index (TI) $r_{1}/r_{0}$ was below one. We additionally required that the mean firing rate of selected cells over the entire experiment was greater than 0.4 Hz. With these criteria we had a total of n = 13 and n = 19 cells for the muscimol and post-muscimol sessions in rat A991 and n = 4 and n = 0 cells for rat A992, see Figure 7—figure supplement 4. To ensure we had a sufficient number of neurons we additionally compared the time-resolved SC to the SC from 5000 shuffled orderings of the cells (t-test, p<0.005, corrected for multiple comparison). Significant differences indicate that the SC carries spatial specificity as opposed to simply reflecting the degree of global correlation in the network (shaded regions in Figure 7—figure supplement 4). The SC for rat A991 was always significantly different from shuffled for all TI, while for rat A992 it was often not so. For this reason we only used the data from rat A991 for these experiments, see Figure 7. We furthermore computed the power spectrum of a simultaneously recorded local field potential (LFP) signal, see Figure 7c and d and Figure 7—figure supplement 4.

#### Hexagonal track experiments

There were a total of n = 158 and n = 134 cells from rats A991 and A992 respectively. We selected cells as described above. This left a total of n = 6, 9 and 4 cells and n = 17, 20 and 13 cells for rat A991 and A992 respectively for the three sessions. The SC calculated for rat A991 was not significantly different from that from 5000 shuffled data sets with random re-orderings of the cells, see non-shaded regions in Figure 7—figure supplement 3. Therefore we only considered data from rat A992 for these experiments, see Figure 7e.

#### Calculating the SC

We consider the firing rate of a $N$ neurons in a time interval of length $T$, divided into $k$ equal time bins of length $T/k$. Once we have ordered the cells according to their place field positions, the cross-correlation of two neighboring cells over the interval is given by

$$
CC_{i,i+1}^{\mu}=\frac{1}{T}\sumt=1k \frac{(r_{i}^{t}−⟨r_{i}⟩)(r_{i+1}^{t}−⟨r_{i+1}⟩)}{\sqrt{Var(r_{i})Var(r_{i+1})}},
$$

where $r_{i}^{t}$ is the firing rate of cell $i$ in time bin $t$, and $�r_{i}�$ and $Var(r_{i})$ are the mean and the variance of the firing rate over the interval. The superscript $\mu$ indicates the particular ordering. The sequential correlation is the average cross-correlation of neighbors in the network

$$
SC^{\mu}=\frac{1}{N−1}\sumi=1N CC_{i,i+1}^{\mu}.
$$

Therefore we can also write

$$
SC^{\mu}=\frac{1}{T}\sumt=1k SC_{t}^{\mu},
$$

where

$$
SC_{t}^{\mu}=\frac{1}{N−1}\sumiN \frac{(r_{i}^{t}−⟨r_{i}⟩)(r_{i+1}^{t}−⟨r_{i+1}⟩)}{\sqrt{Var(r_{i})Var(r_{i+1})}}.
$$

We can use (Equation 65) to calculate the variance of the SC over the time interval in question. The SC in Figure 7c,d,e as well as in Figure 7—figure supplements 3,4, is calculated by first dividing the total experiment into intervals of 3 min. For each of these 3 min intervals a bin of 1 s was used to calculate the SC. In Figure 7b the firing rates over the whole experiment are used, in time bins of 500 ms. The shuffled SC shown in Figure 7a (histogram), and c-e (open symbols) is found in the same way by randomly re-ordering the cells.
