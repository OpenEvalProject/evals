# A dynamical computational model of theta generation in hippocampal circuits to study theta-gamma oscillations during neurostimulation

## Authors

- Nikolaos Vardalakis<sup>1</sup> ([ORCID: 0000-0002-5436-4091](https://orcid.org/0000-0002-5436-4091))
- Amélie Aussel<sup>1</sup> ([ORCID: 0000-0003-0498-2905](https://orcid.org/0000-0003-0498-2905))
- Nicolas P Rougier<sup>1</sup> ([ORCID: 0000-0002-6972-589X](https://orcid.org/0000-0002-6972-589X))
- Fabien B Wagner<sup>1</sup> ([ORCID: 0000-0002-9582-6109](https://orcid.org/0000-0002-9582-6109)) †

### Affiliations

1. University of Bordeaux, CNRS, IMN Bordeaux France ([ROR:057qpr032](https://ror.org/057qpr032))
2. University of Bordeaux, INRIA, IMN Bordeaux France ([ROR:02kvxyf05](https://ror.org/02kvxyf05))
3. University of Bordeaux, CNRS, Bordeaux INP Talence France ([ROR:054qv7y42](https://ror.org/054qv7y42))

† Corresponding author

## Abstract

Neurostimulation of the hippocampal formation has shown promising results for modulating memory but the underlying mechanisms remain unclear. In particular, the effects on hippocampal theta-nested gamma oscillations and theta phase reset, which are both crucial for memory processes, are unknown. Moreover, these effects cannot be investigated using current computational models, which consider theta oscillations with a fixed amplitude and phase velocity. Here, we developed a novel computational model that includes the medial septum, represented as a set of abstract Kuramoto oscillators producing a dynamical theta rhythm with phase reset, and the hippocampal formation, composed of biophysically realistic neurons and able to generate theta-nested gamma oscillations under theta drive. We showed that, for theta inputs just below the threshold to induce self-sustained theta-nested gamma oscillations, a single stimulation pulse could switch the network behavior from non-oscillatory to a state producing sustained oscillations. Next, we demonstrated that, for a weaker theta input, pulse train stimulation at the theta frequency could transiently restore seemingly physiological oscillations. Importantly, the presence of phase reset influenced whether these two effects depended on the phase at which stimulation onset was delivered, which has practical implications for designing neurostimulation protocols that are triggered by the phase of ongoing theta oscillations. This novel model opens new avenues for studying the effects of neurostimulation on the hippocampal formation. Furthermore, our hybrid approach that combines different levels of abstraction could be extended in future work to other neural circuits that produce dynamical brain rhythms.

## Introduction

Neurostimulation methods have emerged as promising therapeutic modalities to restore neurological functions in a broad range of motor and cognitive disorders (Gupta et al., 2023). In the context of learning and memory, deep brain stimulation (DBS) of the entorhinal area or hippocampus has been shown to either enhance (Suthana et al., 2012; Suthana and Fried, 2014; Titiz et al., 2017; Jun et al., 2019) or disrupt (Jacobs et al., 2016; Goyal et al., 2018; Lozano et al., 2016) memory encoding. These conflicting results may originate from differences in experimental protocols and from a poor understanding of their biophysical underpinnings. Among such mechanisms, the involvement of hippocampal theta oscillations (4–12 Hz) and their interactions with higher-frequency gamma oscillations (30–120 Hz) in memory-related processes has been reported in multiple studies (Lisman et al., 2005; de Almeida et al., 2007; Lega et al., 2012; Lin et al., 2017; Malkov et al., 2022; Abbaspoor et al., 2023). Moreover, the modulation of gamma oscillations by the phase of theta oscillations in hippocampal circuits, a phenomenon termed theta-gamma phase-amplitude coupling (PAC), correlates with the efficacy of memory encoding and retrieval (Jensen and Colgin, 2007; Tort et al., 2009; Canolty and Knight, 2010; Axmacher et al., 2010; Fell and Axmacher, 2011; Lisman and Jensen, 2013; Lega et al., 2016). Experimental and computational work on the coupling between oscillatory rhythms has indicated that it originates from different neural architectures and correlates with a range of behavioral and cognitive functions, enabling the long-range synchronization of cortical areas and facilitating multi-item encoding in the context of memory (Hyafil et al., 2015).

Neurostimulation protocols that affect these rhythms, such as theta burst stimulation (Titiz et al., 2017), have also been shown to optimally induce long-term potentiation (LTP) (Larson and Munkácsy, 2015). Another potential mechanism underlying the effect of hippocampal neurostimulation might be the reset of the phase of theta oscillations in response to exogenous inputs, such as a novel sensory input or a pulse of electrical stimulation applied to the fornix or perforant path (Buño et al., 1978; Williams and Givens, 2003). Theta phase reset is known to facilitate LTP (McCartney et al., 2004) and naturally occurs during both encoding and retrieval of associative memories (Kota et al., 2020). In this context, the design of a computational model that replicates memory-related theta-gamma oscillations and theta phase reset is of uttermost importance to investigate the effects of electrical stimulation on the hippocampal formation and possibly optimize neurostimulation protocols for memory improvement.

Models of memory-related theta-gamma oscillations in the hippocampal formation have been developed across different resolution levels, ranging from abstract mean-field approaches (Traub et al., 1997; Onslow et al., 2014; Segneri et al., 2020) to biophysically realistic conductance-based models (Lundqvist et al., 2006; Herman et al., 2013; Aussel et al., 2018). Neural masses, which represent the mean activity of a neuronal population, can generate gamma oscillations through reciprocal interactions between an excitatory and inhibitory population (Traub et al., 1997; Onslow et al., 2014), or even using a self-projecting inhibitory population (Segneri et al., 2020). Under excitatory oscillatory input at theta frequencies, these models are capable of generating theta-nested gamma oscillations. Similarly, these oscillations can be observed in more complex models of the hippocampal formation composed of single-compartment excitatory and inhibitory neurons connected through conductance-based synapses following the Hodgkin-Huxley formalism (Hodgkin and Huxley, 1952), and driven by a fixed oscillatory theta input (Aussel et al., 2018). Theta-nested gamma oscillations also appear in multi-compartment models of prefrontal cortex activity during memory retrieval (Lundqvist et al., 2006; Herman et al., 2013). Finally, several models have investigated the functional link between the hippocampal theta rhythm and memory processes, showing that encoding and retrieval occur at different phases within each theta cycle through phasic changes in neuronal activity and LTP (e.g. Hasselmo et al., 2002; Cutsuridis et al., 2010).

In terms of neurostimulation, most computational work has focused on the mechanisms underlying DBS of the basal ganglia for motor disorders such as Parkinson’s disease (Rubin and Terman, 2004; Pirini et al., 2009; Mina et al., 2013; Ebert et al., 2014), peripheral nerve stimulation (Rattay et al., 2003; Kipping and Nogueira, 2022), spinal cord stimulation (Rattay et al., 2000; Capogrosso et al., 2013), or has remained generic (Basu et al., 2018). However, models investigating neurostimulation of hippocampal circuits are scarce (Hendrickson et al., 2016; Bingham et al., 2018) and do not take into account the effects on theta-gamma oscillations. For example, a detailed multicompartment model of the rat dentate gyrus was able to replicate experimentally recorded local field potentials induced by different electrode placements and pulse amplitudes during stimulation of the perforant path (Bingham et al., 2018). To model the impact of neurostimulation on neuronal oscillations, a more abstract formalism based on Kuramoto phase oscillators (Kuramoto, 1984) has been introduced in the context of Parkinson’s disease and essential tremor, which enabled the design of novel neurostimulation paradigms that enhance or disrupt neuronal synchrony in basal ganglia circuits (Tass, 2003; Ebert et al., 2014; Asllani et al., 2018; Weerasinghe et al., 2019).

To our knowledge, there is currently no model of the hippocampal formation that is able to replicate both theta-gamma PAC and theta phase reset during neurostimulation. To investigate the effects of neurostimulation on hippocampal circuits while taking into account these two mechanisms, we modified an existing biophysical model of the hippocampal formation (Aussel et al., 2018). In this original model, however, the theta rhythm was considered as an oscillatory input of fixed amplitude and phase velocity, which is inconsistent with theta phase reset. To circumvent this limitation, we combined this biophysical model with abstract Kuramoto oscillators that acted as a dynamical source of theta rhythm, thereby modeling medial septum inputs to the hippocampal formation. This new hybrid dynamical model could generate both theta-nested gamma oscillations and theta phase reset, following a particular phase response curve (PRC) inspired by experimental literature (Lengyel et al., 2005; Akam et al., 2012; Torben-Nielsen et al., 2010).

We then leveraged this model to explore the effect of single-pulse and pulse-train stimulation on theta-gamma oscillations. In the absence of theta input from the medial septum, single-pulse stimulation produced a transient effect consisting of one or several bursts of activity, depending on stimulation amplitude. The presence of multiple bursts depended on the single-cell calcium dynamics and M-type potassium adaptation current. In the presence of weak theta input, designed to mimic a pathological state that impairs theta-gamma oscillations, single-pulse stimulation could produce long-lasting or even persistent activity by switching the network to a highly synchronized state characterized by theta-nested gamma oscillations. When phase reset was not included in the model, this effect was more pronounced when the stimulation pulse was delivered at the peak of the theta rhythm. However, when strong theta reset was considered, the phase at which stimulation was delivered did not influence the outcome. In the presence of an even weaker theta input, mimicking a pathological state that completely abolishes theta-gamma oscillations, only pulse train stimulation could restore physiological theta-gamma oscillations during the stimulation period. As for the previous results, this effect was phase-dependent only when theta reset was not included.

These results provide a new framework to interpret neurostimulation interventions that interfere with hippocampal oscillations and aim at improving memory function. It can be further extended to investigate the effects of more complex neurostimulation protocols, and the impact of stimulation location and amplitude on the observed network dynamics.

## Results

### A computational model of the hippocampal formation with dynamical theta input

We first developed a computational model of hippocampal circuits, able to generate both theta-nested gamma oscillations and theta phase reset. To achieve this, we combined an existing conductance-based model of the hippocampal formation (Aussel et al., 2018) with a set of Kuramoto phase oscillators (Kuramoto, 1984) that were used to model the dynamical theta input originating from pacemaker neurons in the medial septum (Wang, 2002, Figure 1A). Such ensembles of oscillators are designed to exhibit a strong phase reset of their collective rhythm in response to a perturbation (Levnajić and Pikovsky, 2010). The hippocampal model contained excitatory and inhibitory neuronal populations in the entorhinal cortex (EC), dentate gyrus (DG), CA3 and CA1 fields within a coronal slice of the human hippocampus (Figure 1B–C). The output of the hippocampal formation (i.e. the activity of CA1 pyramidal neurons) was provided as an input to the Kuramoto oscillators, simulating the hippocampal-septal projections through the fornix (Williams and Givens, 2003; Nuñez and Buño, 2021; Takeuchi et al., 2021). The oscillations produced by the collective behavior of Kuramoto oscillators represented a population average of their activity: highly synchronized and desynchronized states generated respectively high and low amplitude theta oscillations (Figure 1D). The number of oscillators was chosen so that their synchronization level (i.e. their order parameter) and their frequency distribution were sufficiently close to their asymptotic behavior for a large number of oscillators (Figure 1—figure supplement 1).

![Figure 1.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig1-v3.jpg)

**Figure 1.:** (A) Anatomical representation of the neuronal types and interconnections within and between the medial septum and the hippocampal formation (EC: entorhinal cortex, DG: dentate gyrus, CA3 and CA1 fields of the hippocampus). (B) Simplified anatomy of the hippocampal formation, modeled as a 15-mm-thick cylindrical slice, with spatially segregated excitatory and inhibitory neurons (blue: excitatory neurons, consisting of granule cells in DG and pyramidal cells in other areas; red: inhibitory basket cells). (C) Model architecture and connectivity. Each area is comprised of one excitatory and one inhibitory neuronal population. Theta drive is provided through input from the medial septum, which is modeled as a set of 250 Kuramoto oscillators and receives feedback connections from CA1. Electrical stimulation Is modeled as an intracellular current affecting both excitatory and inhibitory populations in the targeted area (shown here for CA1). (D) Illustration of Kuramoto oscillators with two different levels of synchronization. Each dot represents one oscillator, its position on the circle indicates its phase and its color its angular velocity. Higher synchronization corresponds to a clustering of the dots around a similar phase. ‘$r$’ indicates the order parameter, which is a measure of synchronization.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** Left: influence of the number of Kuramoto oscillators ($N$) on the convergence over time of the order parameter ($r$), which is a measure of synchronization of the set of oscillators. The above results were obtained using a synchronization ratio $k/N$ of 25. Upon initialization, the oscillators’ natural frequencies ($\omega_{i}$) were normally distributed with a center frequency ($f_{0}$) of 6 Hz. Initial phases were uniformly distributed around the unit circle ($U∼[0,2\pi]$). Right: histograms of the natural frequencies ($\omega_{i}$), together with the distribution mean ($\mu$) and standard error of the mean ($\sigma/\sqrt{N}$). As the number of oscillators increases, the mean frequency appears closer to the desired center frequency of 6 Hz, and the standard error of the mean is reduced. Overall, increasing the number of oscillators past 250 did not yield any substantial change in the convergence of the order parameter or the distribution of natural frequencies. This number of oscillators was therefore chosen for all subsequent analyses.

Biologically, GABAergic neurons from the medial septum project to the EC, CA3, and CA1 fields of the hippocampus (Tóth et al., 1993; Hajós et al., 2004; Manseau et al., 2008; Hangya et al., 2009; Unal et al., 2015; Müller and Remy, 2018). Although the respective roles of these different projections are not fully understood, previous computational studies have suggested that the direct projection from the medial septum to CA1 is not essential for the production of theta in CA1 microcircuits (Mysin et al., 2019). Since our modeling of the medial septum is only used to generate a dynamic theta rhythm, we opted for a simplified representation where the medial septum projects only to the EC, which in turn drives the different subfields of the hippocampus. In our model, Kuramoto oscillators are therefore connected to the EC neurons and they receive projections from CA1 neurons (see Materials and methods for more details).

From a conceptual point of view, our model is thus composed of excitatory-inhibitory (E-I) circuits connected in series, with a feedback loop going through a population of coupled phase oscillators. In the next sections, we first describe the generation of gamma oscillations by individual E-I circuits (Figure 2), and illustrate their behavior when driven by an oscillatory input such as theta oscillations (Figure 3). We then present a thorough characterization of the effects of theta input and stimulation amplitude on theta-nested gamma oscillations (Figure 4 and Figure 5). Finally, we present some results on the effects of neurostimulation protocols for restoring theta-nested gamma oscillations in pathological states (Figure 6 and Figure 7).

![Figure 2.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig2-v3.jpg)

**Figure 2.:** (A) Two coupled populations of excitatory pyramidal neurons ($N_{E}$ = 1000) and inhibitory interneurons ($N_{I}$ = 100) are driven by a ramping current input (0 nA to 1 nA) for 5 s. As the input becomes stronger, oscillations start to emerge (shaded green area), driven by the interactions between excitatory and inhibitory populations. The green inset shows the raster plot (neuronal spikes across time) of the two populations during the green shaded period (red for inhibitory; blue for excitatory). When the input becomes sufficiently strong (shaded magenta area), the populations become highly synchronized and produce oscillations in the gamma range (at approximately 50 Hz). The spectrogram (bottom panel) shows the power of the instantaneous firing rate of the pyramidal population as a function of time and frequency. It reveals the presence of gamma oscillations that emerge around 2 s and increase in frequency until 4 s, when they settle at approximately 60 Hz. (B) Similar depiction as in panel A. with the pyramidal-interneuronal populations decoupled. The absence of coupling leads to the abolition of gamma oscillations, each cell spiking activity being driven by its own inputs and intrinsic properties.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** Similar representation as in Figure 2, but with the input provided only to the excitatory population. All conclusions remain the same. In addition, the inhibitory population does not show any spiking activity in the decoupled case.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** (A) Input-Frequency (I–F) curves for excitatory cells (left panel; pyramidal neurons with $I_{CAN}$) and inhibitory cells (right panel; interneurons, fast-spiking) used in the model. Above a certain tonic input (around 0.35 nA for excitatory and 0.1 nA for inhibitory neurons), neurons can spike in the gamma range. (B) Raster plot showing the spiking activity of excitatory (blue,$N_{E}$ = 1000) and inhibitory (red,$N_{I}$ = 100) neurons in decoupled populations under ramping input (top trace) and in the absence of noise in the membrane potential. Despite random initial conditions across neurons, oscillations emerge in both populations due to the intrinsic properties of the cells, with a frequency that is predicted by the respective I-F curves (panel A.). (C) Similar representation as panel B. but with the addition of stochastic noise in the membrane potential of each neuron. The presence of noise disrupts the emergence of oscillations in these decoupled populations.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig2-figsupp3-v3.jpg)

**Figure 2—figure supplement 3.:** All panels show the effects of pulsed optogenetic stimulation of specific cell types (A. excitatory only, B. inhibitory only, C. both excitatory and inhibitory cells) at different frequencies, similar to the experiments reported by Cardin and colleagues (Cardin et al., 2009). Pulsed stimulation was delivered continuously with a frequency ranging from 10 to 200 Hz. The relative power was calculated similarly to Cardin et al., 2009. Specifically, for each stimulation frequency, we computed first the power spectral density of the population firing rates using Welch’s method, and then the ratio between the power within a 10-Hz band centered around the stimulation frequency and the total power across all frequencies. (A) Pulsed stimulation of excitatory cells shows a higher relative power in the stimulated neurons at low frequencies (20 and 40 Hz). (B) Pulsed stimulation of inhibitory cells reveals neuronal entrainment, that is, a peak in their relative power, in the high gamma range (80-100 Hz). (C) Simultaneous pulsed stimulation of both populations reveals a strong entrainment of inhibitory cells in the high gamma range, and a more modest entrainment of excitatory cells at low frequencies.

![Figure 3.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig3-v3.jpg)

**Figure 3.:** (A) Representative example of the network behavior, spontaneously producing theta-nested gamma oscillations and characterized by a reset of the theta phase following a single stimulation pulse (vertical grey line, applied here in CA1 at a theta phase of $\pi/2$, that is in the middle of the descending slope). Top to bottom: theta rhythm originating from the medial septum and provided as an input to the EC ($f_{\theta}$: mean oscillation frequency), instantaneous phase of the theta rhythm, raster plots indicating the spiking activity of CA1 excitatory (blue) and inhibitory (red) neurons ($\mu_{E}$ and $\mu_{I}$: mean firing rates within the shaded area), average population firing rates in CA1 (computed as a windowed moving average with a sliding window of 100ms with 99% overlap), spectrograms for each CA1 population (windowed short-time fast Fourier transform using a Hann sliding window: 100ms with 99% overlap). Spectrograms show gamma oscillations (around 60 Hz) modulated by the underlying theta rhythm (∼4 Hz), indicating theta-gamma PAC. Theta phase reset after stimulation is associated with a rebound of spiking activity and theta-nested gamma oscillations. (B) Power spectral densities of the CA1 firing rates. Theta peaks are found at 4 Hz for excitatory and inhibitory cells. Gamma activity is located between 40 and 80 Hz. (C) PAC as a function of theta phase and gamma frequency. The polar plot represents the amplitude of gamma oscillations (averaged across all theta cycles, see Materials and methods) at each phase of theta (theta range: 3–9 Hz, phase indicated as angular coordinate) and for different gamma frequencies (radial coordinate, binned in 10 Hz ranges), indicating that gamma oscillations between 40 and 80 Hz occur preferentially around the peak of theta. The MI gives an overall quantification of how the phase of low-frequency oscillations (3–9 Hz) modulates the amplitude of higher-frequency oscillations (40–80 Hz) (see Materials and methods and Figure 3—figure supplement 2). (D) PRC in response to a single stimulation pulse applied in CA1 at various phases of the ongoing theta rhythm and for various stimulation amplitudes (color-coded). The phase difference (left y-axis) shows the theta phase induced by the stimulation pulse (computed 2.5ms after the pulse), compared to the phase computed at the same time in a scenario without stimulation. Positive and negative phase differences indicate phase advances and delays, respectively. The grey trace shows the normalized amplitude of theta (right $y$ axis) for different phases, used to indicate the peak and trough of the rhythm. Stimulation applied in the ascending slope of theta ($[−\pi,0]$) produced a phase advance and accelerated the rhythm towards its peak (0 radians). Conversely, stimulation during the descending slope ($[0,\pi]$) produced a phase delay that slowed down the rhythm. Higher stimulation amplitudes yielded a stronger effect.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** This figure shows the behavior of all areas of the hippocampal formation during the simulation illustrated in Figure 3A. All areas display bursts of gamma activity that occur almost synchronously at the peak of each theta cycle in both excitatory and inhibitory neuronal populations ($\mu_{E}$ and:$\mu_{I}$ mean firing rates within the shaded area). The CA1 excitatory population firing rate is supplied back to the medial septum. A single stimulation pulse (vertical line and grey triangle) delivered to both CA1 populations at a phase of $\pi/2$ (i.e. halfway through the descending slope) resets the phase of the theta rhythm according to the PRC shown in Figure 3D.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** (A) Quantifying PAC in the absence of noise produced inaccurate identification of the coupled frequency bands, due to the complete absence of oscillations at some frequencies. All analyses are based on the CA1 firing rates (top traces) during a representative simulation. Power spectral densities of these firing rates (left) indicate that some frequencies have a power of 0. PAC of the excitatory population was assessed using two graphical representations, the polar plot (middle) and comodulogram (right), and quantified using the MI. The comodulogram was calculated by computing the MI across 80% overlapping 1-Hz frequency bands in the theta range and across 90% overlapping 10 Hz frequency bands in the gamma range and subsequently plotted as a heat map. In the absence of noise, a slow theta frequency centered around 5 Hz is found to modulate a broad range of gamma frequencies between 40 and 100 Hz. The value indicated on the comodulogram indicates the average MI in the 3-9 Hz theta range and 40-80 Hz gamma range. As in Figure 3, the polar plot represents the amplitude of gamma oscillations (averaged across all theta cycles) at each phase of theta (theta range: 3–9 Hz, phase indicated as angular coordinate) and for different gamma frequencies (radial coordinate, binned in 1 Hz ranges). (B) Adding uniform noise to the firing rate (with an amplitude ranging between 15 and 25% of the maximum firing rate) improved the identification of the coupled frequency bands. In this case, the slower theta frequency centered around 5 Hz modulates a gamma band located between 45 and 75 Hz.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** Each panel is similar to Figure 3A, but with a different offset added to the phase response function of the Kuramoto oscillators (see methods, Equation 4). The center frequency was set to 6 Hz in all of these simulations. Overall, theta oscillations in these cases are less sinusoidal and show more abrupt phase changes than in the physiological case. (A) A phase offset of $−\pi/2$ leads to an overall theta oscillation of 4 Hz, with a second peak following the main theta peak. (B). A phase offset of $+\pi/2$ reduces the peak of theta, resetting the rhythm to the middle of the ascending phase. (C) A phase offset of $\pi$ or $−\pi$ leads to the CA1 output resetting the theta rhythm to the trough of theta.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig3-figsupp4-v3.jpg)

**Figure 3—figure supplement 4.:** (A) Two coupled neural masses (one excitatory and one inhibitory) driven by Kuramoto oscillators, which represent a dynamical oscillatory drive in the theta range, were used to implement a neural mass equivalent to our conductance-based model represented in Figure 1. Neural masses were modeled using the Wilson-Cowan formalism, with parameters adapted from Onslow et al., 2014 ($W_{EE}$ = 4.8, $W_{EI}$ = $W_{IE}$ = 4, $W_{II}$ = 0). (B) The normalized population firing rates exhibit theta-nested gamma oscillations (middle and bottom panels) in response to the dynamic theta rhythm (top panel). A stimulation pulse delivered at the descending phase of the rhythm to both populations (marked by the inverted red triangle) produces a robust theta phase reset, similarly to Figure 3A.

![Figure 4.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig4-v3.jpg)

**Figure 4.:** (A) Network response to single-pulse stimulation in the absence of medial septum input. Stimulation (grey vertical line, 10 nA, applied in CA1) induced an instantaneous burst of activity lasting about 20ms in both excitatory and inhibitory CA1 neurons, followed by a secondary burst approximately 200 ms later (raster plot and firing rate traces), associated with specific CAN- and M- currents dynamics (bottom traces, illustrated for a representative CA1 excitatory neuron). Positive ($I_{M}$) and negative ($I_{CAN}$) currents indicate respectively a hyperpolarizing and depolarizing effect on the cell membrane potential. (B) Similar representation as in A., but in the absence of CAN channel. Stimulation induced only a single burst of activity, indicating that CAN channels are necessary to observe a rebound of activity. (C) Number of bursts in CA1 spiking activity following a single stimulation pulse at various amplitudes (x-axis), shown both in the presence and absence of CAN channels in excitatory neurons. The absence of the CAN current leads to the abolition of the second burst, irrespective of stimulation amplitude.

![Figure 5.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig5-v3.jpg)

**Figure 5.:** (A-C) Network responses to single-pulse stimulation (vertical line) under medial septum input (with phase reset), shown for different amplitudes of the medial septum oscillatory drive (A-C: increasing oscillator amplitudes). (A) Low oscillatory input: stimulation induces only two bursts of spiking activity as in Figure 4. (B) Medium oscillatory input: a single stimulation pulse switches network behavior from no activity to sustained oscillations driven by the medial septum. (C) Higher oscillatory input: theta drive is capable of inducing self-sustained theta-nested gamma oscillations. In this case, stimulation is delivered at the peak of theta oscillations and does not show a pronounced effect on theta-gamma oscillations. (D) Steady-state response to single-pulse stimulation as a function of medial septum oscillatory input (x-axis) and stimulation amplitude (y-axis), characterized by three metrics: theta power (3–9 Hz), gamma power (40–80 Hz), and PAC (quantified using the MI). White dots: parameter combinations corresponding to panels A-C.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** This figure shows the behavior of all areas of the hippocampal formation during the simulation illustrated in Figure 5A. A single stimulation pulse delivered to both CA1 populations induces two bursts of spiking activity that propagate only from CA1 to EC.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** This figure shows the behavior of all areas of the hippocampal formation during the simulation illustrated in Figure 5B. A single stimulation pulse switches network behavior from no activity to sustained oscillations driven by the medial septum.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig5-figsupp3-v3.jpg)

**Figure 5—figure supplement 3.:** This figure shows the behavior of all areas of the hippocampal formation during the simulation illustrated in Figure 5C. Theta oscillatory drive is enough to induce self-sustained theta-nested gamma oscillations. In this case, stimulation is delivered at the peak of theta and does not induce a pronounced effect on theta-gamma oscillations.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig5-figsupp4-v3.jpg)

**Figure 5—figure supplement 4.:** (A) Same as Figure 5B. (B) Similar simulation as panel A., but without the presence of CAN currents in the EC, CA3, and CA1 fields of the hippocampus. Removing CAN currents from the model abolishes self-sustained theta-nested gamma oscillations in response to a single stimulation pulse (for the parameters represented in Figure 5, point B).

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig5-figsupp5-v3.jpg)

**Figure 5—figure supplement 5.:** (A, B) Network responses to single-pulse stimulation (vertical line) under medial septum input (with phase reset), shown for different synchronization parameter ratios of the Kuramoto oscillators (A,B: $k/N$ of 5 and 35 respectively; stimulation amplitude: 7.0 nA). Panel B. indicates that the model can produce oscillations without external stimulation when the synchronization level is higher. (C) Steady-state response to single-pulse stimulation as a function of medial septum oscillatory input (x-axis) and synchronization parameter ratio ($k/N$, y-axis), characterized by three metrics: theta power (3–9 Hz), gamma power (40–80 Hz), and PAC (quantified using the MI). White dots: parameter combinations corresponding to panels A and B.

![Figure 6.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig6-v3.jpg)

**Figure 6.:** All results shown here were obtained for parameters from Figure 5B (theta oscillation amplitude: 0.13 nA, stimulation amplitude: 7.0 nA). A single stimulation pulse was delivered at the peak (A, B) or trough (C, D) of the underlying theta rhythm, either in the presence (A, C) or absence (B, D) of theta phase reset. With phase reset, both peak and trough stimulation switch network behavior from no activity to sustained oscillations. Without phase reset, only peak stimulation can induce sustained oscillations. (E). Quantification of theta power, gamma power, and PAC (measured using the MI) in CA1 excitatory (blue) and inhibitory (red) populations in all four cases (metrics are computed in the shaded areas of panels A-D).

![Figure 7.](https://cdn.elifesciences.org/articles/87356/elife-87356-fig7-v3.jpg)

**Figure 7.:** All results shown here were obtained for parameters from Figure 5A (theta oscillation amplitude: 0.05 nA; stimulation amplitude: 7.0 nA). Representations are similar to Figure 6, with the difference that stimulation consisted of a pulse train delivered at 6 Hz for a duration of 2 s (individual pulses indicated by grey dots, first pulse by a triangle). The pulse train was delivered at the peak (A, B) or trough (C, D) of the underlying theta rhythm, either in the presence (A, C) or absence (B, D) of theta phase reset. With phase reset, both peak and trough stimulation switch network behavior from no activity to sustained oscillations. Without phase reset, only peak stimulation can induce sustained oscillations. E. Quantification of theta power, gamma power, and PAC (measured using the MI) in CA1 excitatory (blue) and inhibitory (red) populations in all four cases (metrics are computed during the pulse train, within the shaded areas of panels A-D).

### Generation of gamma oscillations by E-I circuits

It is well established that a network of interconnected pyramidal neurons and interneurons can give rise to oscillations in the gamma range, a mechanism termed pyramidal-interneuronal network gamma (PING) (Traub et al., 2004; Onslow et al., 2014; Segneri et al., 2020). This mechanism has been observed in several optogenetic studies with gradually increasing light intensity (i.e. under a ramp input) affecting multiple different circuits, such as layer 2–3 pyramidal neurons of the mouse somatosensory cortex (Adesnik and Scanziani, 2010), the CA3 field of the hippocampus in rat in vitro slices (Akam et al., 2012), and in the non-human primate motor cortex (Lu et al., 2015). In all cases, gamma oscillations emerged above a certain threshold in terms of photostimulation intensity, and the frequency of these oscillations was either stable or slightly increased when increasing the intensity further. We sought to replicate these findings with our elementary E-I circuits composed of single-compartment conductance-based neurons driven by a ramping input current (Figure 2 and Figure 2—figure supplement 1). As an example, all the results in this section will be shown for an E-I circuit that has similar connectivity parameters as the CA1 field of the hippocampus in our complete model (see section ‘Hippocampal formation: inputs and connectivity’ in the Materials and methods).

For low input currents provided to both neuronal populations, only the highly excitable interneurons were activated (Figure 2A). For a sufficiently high input current (i.e. a strong input that could overcome the inhibition from the fast-spiking interneurons), the pyramidal neurons started spiking as well. As the amplitude of the input increased, the activity of both neuronal populations became synchronized in the gamma range, asymptotically reaching a frequency of about 60 Hz (Figure 2A bottom panel). Decoupling the populations led to the abolition of gamma oscillations (Figure 2B), as neuronal activity was determined solely by the intrinsic properties of each cell. Interestingly, when the ramp input was provided solely to the excitatory population, we observed that the activity of the pyramidal neurons preceded the activity of the inhibitory neurons, while still preserving the emergence of gamma oscillations (Figure 2—figure supplement 1A). As expected, decoupling the populations also abolished gamma oscillations, with the excitatory neurons spiking a frequency determined by their intrinsic properties and the inhibitory population remaining silent (Figure 2—figure supplement 1B).

To further characterize the intrinsic properties of individual inhibitory and excitatory neurons, we derived their input-frequency (I-F) curves, which represent the firing rate of individual neurons in response to a tonic input (Figure 2—figure supplement 2A). We observed that for certain input amplitudes, the firing rates of both types of neurons was within the gamma range. Interestingly, in the absence of noise, each population could generate by itself gamma oscillations that were purely driven by the input and determined by the intrinsic properties of the neurons (Figure 2—figure supplement 2B). Adding stochastic Gaussian noise in the membrane potential disrupted these artificial oscillations in decoupled populations (Figure 2—figure supplement 2C). All subsequent simulations were run with similar noise levels to prevent the emergence of artificial gamma oscillations.

Another potent way to induce gamma oscillations is to drive fast-spiking inhibitory neurons using pulsed optogenetic stimulation at gamma frequencies, a strategy that has been used both in the neocortex (Cardin et al., 2009) and hippocampal CA1 (Iaccarino et al., 2016). In particular, Cardin and colleagues systematically investigated the effect of driving either excitatory or fast-spiking inhibitory neocortical neurons at frequencies between 10 and 200 Hz (Cardin et al., 2009). They showed that fast-spiking interneurons are preferentially entrained around 40–50 Hz, while excitatory neurons respond better to lower frequencies. To verify the behavior of our model against these experimental data, we simulated pulsed optogenetic stimulation as an intracellular current provided to our reduced model of a single E-I circuit. Stimulation was applied at frequencies between 10 and 200 Hz to excitatory cells only, to inhibitory cells only, or to both at the same time (Figure 2—figure supplement 3). The population firing rates were used as a proxy for the local field potentials (LFP), and we computed the relative power in a 10 Hz band centered around the stimulation frequency, similarly to the method proposed in Cardin et al., 2009. When presented with continuous stimulation across a range of frequencies in the gamma range, interneurons showed the greatest degree of gamma power modulation (Figure 2—figure supplement 3). Furthermore, when the stimulation was delivered to the excitatory population, the relative power around the stimulation frequency dropped significantly in frequencies above 10 Hz, similar to the reported experimental data (Cardin et al., 2009). The main difference between our simulation results and these experimental data is the specific frequencies at which fast-spiking interneurons showed resonance, which was around 40 Hz in the mouse barrel cortex and around 90 Hz in our model, a fast gamma rhythm. This could be attributed to several factors, such as differences in the cellular properties between cortical and hippocampal fast-spiking interneurons, or the differences between the size of the populations and their relevant connectivity in the cortex and the hippocampus.

### Theta-gamma oscillations and theta phase reset under dynamical theta input

Once we validated that our elementary E-I circuits were able to generate gamma oscillations under an input of sufficiently high amplitude, we studied the behavior of the whole model when the theta input was dynamically provided by the Kuramoto oscillators as described above (Figure 1). As in the original model (Aussel et al., 2018), the input theta rhythm drove the network to produce spiking activity in the gamma range preferentially around the peak of theta in all excitatory and inhibitory populations (Figure 3A and Figure 3—figure supplement 1). Spectrograms of the CA1 population firing rates revealed that these bursts of activity around each theta peak were characterized by oscillations around 60 Hz (Figure 3A). This was confirmed by power spectral densities, which showed a clear peak at 4 Hz (corresponding to the theta drive) and increases in gamma band activity between 40 and 80 Hz (Figure 3B). To quantify PAC between theta and gamma oscillations, we used the modulation index (MI) (Tort et al., 2008; Tort et al., 2010), which has been shown to outperform other similar measures (Hülsemann et al., 2019). However, we discovered that this metric would give erroneous results in our simulated datasets due to the absence of certain frequency components. To overcome this limitation and avoid artifacts, uniform noise was added to the firing rates prior to computing the MI (Figure 3—figure supplement 2). We first visualized the quantification of PAC using the comodulogram, which indicates the MI as a function of two frequencies corresponding to the modulating phase signal and the modulated amplitude signal. This analysis confirmed that gamma-band signals between 45 and 75 Hz were modulated by lower theta frequencies between 3 and 6 Hz, which we quantified by computing a global MI in frequency ranges encompassing theta (3–9 Hz) and gamma (40–80 Hz) (Figure 3—figure supplement 2B). To refine this analysis, we also computed a similar MI between the amplitude of various gamma frequencies and the phase of theta, which indicated that oscillations between 40 and 80 Hz occur preferentially around the peak of theta (Figure 3C and Figure 3—figure supplement 2B).

Next, we verified that our model was able to display theta phase reset during single-pulse stimulation (depolarizing pulse, 1 ms duration). This mechanism is tightly linked with the concept of PRC, which characterizes the phase delay or advancement that follows a single pulse delivered to an oscillatory system, as a function of the phase at which this input is delivered. Although there is no direct measurement of the PRC of septal neurons, such characterizations have been performed for individual pyramidal cells in the CA3 and CA1 fields of the hippocampus (Lengyel et al., 2005; Kwag and Paulsen, 2009; Akam et al., 2012). These PRCs appear biphasic and show a phase advancement (respectively delay) for stimuli delivered in the ascending (respectively descending) slope of theta. We modeled this behavior by a specific term (which we called the phase response function) in the general equation of the Kuramoto oscillators (see methods, Equation 1). Importantly, introducing a phase offset in the phase response function disrupted theta-nested gamma oscillations (Figure 3—figure supplement 3), which suggests that the septohippocampal circuitry must be critically tuned to be able to generate such oscillations. The strength of phase reset could also be adjusted by a gain that was manually tuned. In the presence of the physiological phase response function and of a sufficiently high reset gain, a single stimulation pulse delivered to all excitatory and inhibitory CA1 neurons could reset the phase of theta to a value close to its peaks (Figure 3A). We computed the PRC of our simulated data for different stimulation amplitudes and validated that our neuronal network behaved according to the phase response function set in our Kuramoto oscillators (Figure 3D). It should be noted that including this phase reset mechanism affected the generated theta rhythm even in the absence of stimulation, extending the duration of the theta peak and thereby slowing down the frequency of the generated theta rhythm.

Importantly, our approach is generalizable and can be applied to other models producing theta-nested gamma oscillations. For instance, we adapted the neural mass model by Onslow and colleagues (Onslow et al., 2014), replaced the fixed theta input by a set of Kuramoto oscillators, and demonstrated that it could also generate theta phase reset in response to single-pulse stimulation (Figure 3—figure supplement 4). These results illustrate that the general behavior of our model is not specific to the tuning of individual parameters in the conductance-based neurons, but follows general rules that are captured by the level of abstraction of the Kuramoto formalism.

Overall, we successfully developed a new model of the hippocampal formation able to exhibit both theta-nested gamma oscillations and theta phase reset in response to stimulation. We then decided to explore further the effects of various stimulation protocols on its dynamics.

### Effects of theta input and stimulation amplitudes on theta-gamma oscillations

We investigated the behavior of the model across multiple states of varying septal theta input amplitude in response to single-pulse stimulation delivered to CA1. In the absence of theta drive, a single stimulation pulse elicited either zero or two bursts of spiking activity (depending on stimulation amplitude) separated by about 200 ms (Figure 4A and C). We first sought to understand the origin of this second burst, as it showed that even a single pulse could induce transient periodic activity around 5 Hz in our model, a frequency within the theta range. A previous model has shown that the presence of Calcium-Activated Non-specific cationic (CAN) currents can lead to self-sustained theta oscillations in the hippocampus (Giovannini et al., 2017). Moreover, this study showed a direct link between the increased excitation provided by the CAN current and the spike-frequency adaptation properties of the M current, directly affecting transitions from an asynchronous low-firing regime to synchronous bursting. We tested the role of the CAN current in the response to single-pulse stimulation by completely removing it from our simulations, which abolished the second burst of activity (Figure 4B). Moreover, the time interval separating the two bursts likely resulted from the interplay between the depolarizing CAN current and hyperpolarizing M current (Figure 4A).

In the presence of dynamic theta input, the effects of single-pulse stimulation depended both on theta input amplitude and stimulation amplitude, highlighting different regimes of network activity (Figure 5 and Figure 5—figure supplement 1, Figure 5—figure supplement 2, Figure 5—figure supplement 3). For low theta input, theta-nested gamma oscillations were initially absent and could not be induced by stimulation (Figure 5A). At most, the stimulation could only elicit a few bursts of spiking activity that faded away after approximately 250ms, similar to the rebound of activity seen in the absence of theta drive. For increasing theta input, the network switched to an intermediate regime: upon initialization at a state with no spiking activity, it could be kicked to a state with self-sustained theta-nested gamma oscillations by a single stimulation pulse of sufficiently high amplitude (Figure 5B). This regime existed for a range of septal theta inputs located just below the threshold to induce self-sustained theta-gamma oscillations without additional stimulation, as characterized by the post-stimulation theta power, gamma power, and theta-gamma PAC (Figure 5D). Removing CAN currents from all areas of the model abolished this behavior (Figure 5 - figure supplement 4), which is interesting given the role of this current in the multistability of EC neurons (Egorov et al., 2002; Fransén et al., 2006) and in the intrinsic ability of the hippocampus to generate theta-nested gamma oscillations (Giovannini et al., 2017). For the highest theta input, the network became able to spontaneously generate theta-nested gamma oscillations, even when initialized at a state with no spiking activity and without additional neurostimulation Figure 5C.

### Neurostimulation for restoring theta-gamma oscillations in pathological states

Based on the above analyses, we considered two pathological states: one with a moderate theta input (i.e. moderately weak projections from the medial septum to the EC) that allowed the initiation of self-sustained oscillations by single stimulation pulses (Figure 5, point B), and one with a weaker theta input characterized by the complete absence of self-sustained oscillations even following transient stimulation (Figure 5, point A). In each case, we sought to assess whether single-pulse or pulse train stimulation could induce or restore theta-nested gamma oscillations and whether this effect depended on the phase at which stimulation was delivered (i.e. at the peak or trough of the theta cycle). We hypothesized that any possible phase relationship would also depend on the phase reset mechanism. To test this hypothesis, we ran a series of simulations using two different models: one without phase reset and one with strong phase reset (i.e. the reset gain was set at the value used in Figure 3).

In the case of a moderate theta input and in the presence of phase reset, delivering a pulse at either the peak or trough of theta could induce theta-nested gamma oscillations (Figure 6A and C). By contrast, in the absence of phase reset, only stimulation delivered at the peak of theta was able to induce such oscillations, after some time delay (Figure 6B and D). Quantification of these results in terms of theta power, gamma power, and theta-gamma PAC showed strongly similar responses between stimulation delivered at the peak or trough of theta with phase reset enabled, similar but weaker responses with stimulation delivered at the peak of theta with phase reset disabled, and no response in the case of trough stimulation with phase reset disabled (Figure 6E).

In the case of a weak theta input that completely abolished neuronal oscillations, we delivered stimulation pulses continuously at a frequency matching that of the underlying theta rhythm for a duration of 2 s, in order to restore physiological oscillations (Figure 7). The stimulation onset was timed to either the peak or trough of the ongoing theta cycle. The continuous delivery of pulses produced similar results as single-pulse stimulation. With phase reset, pulse train stimulation restored theta-nested gamma oscillations within the whole network, irrespective of the phase of stimulation onset (Figure 7A and C). Notably, stimulation delivered at the trough forced a reset of the phase of theta rhythm and led to the subsequent delivery of pulses at the peak of theta. Interestingly, in the absence of phase reset, peak-targeted stimulation induced theta-gamma oscillations in all network areas easily, while trough-targeted stimulation created artificial bursts that propagated in other areas with difficulty, requiring multiple pulses to achieve a fraction of the results of peak-targeted stimulation (Figure 7B and D). Comparing these simulations based on theta power, gamma power, and theta-gamma PAC within CA1 (Figure 7E) showed similar albeit less striking differences as single-pulse stimulation, possibly because CA1 was driven directly by the stimulation. Notably, gamma power in the absence of theta phase reset, was higher when utilizing pulse trains. These differences were even more pronounced in areas other than CA1, as can be seen by the gradual emergence of oscillations for trough stimulation without phase reset (Figure 7D).

## Discussion

### Highlights

In summary, we have developed a novel computational model to investigate the effects of electrical stimulation on a slice of the hippocampal formation, incorporating two important features related to memory: theta-nested gamma oscillations and theta phase reset. The key innovation compared to previous models (e.g. Aussel et al., 2018) is the introduction of a set of abstract Kuramoto oscillators, which represent pacemaker neurons in the medial septum and are interfaced with biophysically realistic neuronal models in the hippocampus. From a methodological point of view, this hybrid interfacing between two levels of abstraction represents an innovation in itself and could be applied to other systems or brain structures that are driven by dynamical rhythms. The main outcomes reported here relate to the importance of the theta reset mechanism when examining the effects of neurostimulation on hippocampal oscillations.

A very interesting finding concerns the behavior of the model in response to single-pulse stimulation for certain values of the theta amplitude (Figure 5). For low theta amplitudes, a single stimulation pulse was capable of switching the network behavior from a state with no spiking activity to one with prominent theta-nested gamma oscillations. Whether such an effect can be induced in vivo in the context of memory processes remains an open question. Nevertheless, delivering a single stimulation pulse bilaterally to the human hippocampus during a memory task is sufficient to impair memory encoding (Lacruz et al., 2010), suggesting that even single-pulse stimulation can indeed have wide network effects that are behaviorally relevant.

The second main finding is that the timing of individual stimulation pulses with respect to the phase of the ongoing theta rhythm matters differently depending on the presence or absence of phase reset (Figure 6 and Figure 7). Human intracranial stimulation data indicate that the receptivity of hippocampal circuits to single-pulse stimulation is modulated by the phase of theta (Lurie et al., 2022). A number of studies have also reported conflicting results in terms of memory outcomes, which could potentially be attributed to the induction of phase reset through stimulation (Suthana et al., 2012; Jacobs et al., 2016). To our knowledge, however, the degree of phase reset that follows each stimulation pulse remains unknown and should be investigated in future experimental studies. From a technological point of view, the two regimes with and without phase reset have opposite predictions concerning the need for closed-loop stimulation protocols that would trigger stimulation in real-time based on the phase of ongoing theta oscillations. Such phase-triggered stimulation would be most useful if the phase reset mechanism remains relatively limited. When this mechanism becomes too strong, regular continuous stimulation appears sufficient to restore physiological theta-gamma oscillations (Figure 7).

It should also be noted that the reset gain in our simulations (Equation 1, gain $G_{reset}$) was either completely turned off or set at a high value, producing a strong effect that always reset the phase of theta to its peak. In reality, the degree of theta phase reset is dynamic, depending on the environment and associated task requirements (Rizzuto et al., 2003; Mormann et al., 2005; Jackson et al., 2008), and may be affected by neurodegenerative disorders that affect the connections between the hippocampal formation and the medial septum. Importantly, our proposed framework can simulate intermediate values of the reset gain, which should ideally be fitted to experimental data in future applications.

Finally, we modeled pathological states by reducing the maximum amplitude of the theta input (Equation 2, gain $G_{\theta}$) until theta-nested gamma oscillations were impaired or even abolished (Figure 5). This choice was meant to simulate neurodegeneration in the medial septum, which is known to be affected in Alzheimer’s disease, leading to oscillatory disruptions (Nelson et al., 2014; Hampel et al., 2018; Takeuchi et al., 2021). Another possibility would be that neurodegeneration limits the ability of the septal pacemaker neurons to synchronize, thus producing a weaker collective theta rhythm without affecting the maximum amplitude of individual oscillators. Although we simulated this change in our model by reducing the synchronization parameter, the effects on hippocampal oscillations were less pronounced (Figure 5 - figure supplement 5). Linking these different modeling parameters to experimental biomarkers will be important in future work.

### Limitations

Even though we took great care in developing a precise representation of the hippocampal formation, the resulting model remains a simplification that could be further enriched. In particular, we deliberately modeled only a single theta generator, while multiple intra- and extra-hippocampal generators are known to co-exist (Kocsis et al., 1999; Hummos and Nair, 2017). We decided to model septal pacemaker neurons projecting to the EC as the main source of hippocampal theta as reported in multiple experimental studies (Buzsáki, 2002; Buzsáki et al., 2003; Hangya et al., 2009; Colgin, 2013). However, experimental findings and previous models have also proposed that direct septal inputs are not essential for theta generation (Wang, 2002; Colgin, 2013; Mysin et al., 2019), but play an important role in phase synchronization of hippocampal neurons. Furthermore, the model does not account for the connections between the lateral and medial septum and the hippocampus (Takeuchi et al., 2021). These connections include the inhibitory projections from the lateral to the medial septum and the monosynaptic projections from the hippocampal CA3 field to the lateral septum. An experimental study has highlighted the importance of the lateral septum in regulating the hippocampal theta rhythm Bender et al., 2015, an area that has not been included in the model. Specifically, theta-rhythmic optogenetic stimulation of the axonal projections from the lateral septum to the hippocampus was shown to entrain theta oscillations and lead to behavioral changes during exploration in transgenic mice. To account for these discrepancies, our model could be extended by considering more realistic connectivity patterns between the medial/lateral septum and the hippocampal formation, including glutamatergic, cholinergic, and GABAergic reciprocal connections (Müller and Remy, 2018), or by considering multiple sets of oscillators each representing one theta generator.

In terms of neuronal cell types, we also made an important simplification by considering only basket cells as the main class of inhibitory interneuron in the whole hippocampal formation. However, it should be noted that many other types of interneurons exist in the hippocampus and have been modeled in various works with higher computational complexity (e.g. Bezaire et al., 2016; Chatzikalymniou et al., 2021). Among these various interneurons, oriens-lacunosum moleculare (OLM) neurons in the CA1 field have been shown to play a crucial role in synchronizing the activity of pyramidal neurons at gamma frequencies (Tort et al., 2007), and in generating theta-gamma PAC (e.g. Neymotin et al., 2011; Ponzi et al., 2023). Additionally, these cells may contribute to the formation of specific phase relationships within CA1 neuronal populations, through the integration between inputs from the medial septum, the EC, and CA3 (Mysin et al., 2019). Future work is needed to include more diverse cell types and detailed morphologies modeled through multiple compartments.

Another limitation of our model concerns synaptic transmission delays, which have been largely neglected and could affect the phase relationships between the medial septum and different hippocampal subfields. Experimental studies have indeed reported time delays in the population activities of connected anatomical structures (i.e. from EC to DG; Mizuseki et al., 2009), with pyramidal cells in downstream areas like CA3 and CA1 preferentially firing at different phases of theta (Dragoi and Buzsáki, 2006). Propagation effects could also depend on the spatial scale of the model. We also decided to represent only a thin coronal slice of the hippocampal formation, and it remains unclear how an anatomically accurate model of the whole structure would behave in terms of propagation of spontaneous and electrically-induced neuronal activity.

Importantly, we did not consider learning through synaptic plasticity, even though such mechanisms could drastically modify synaptic conduction for the whole network (Borges et al., 2017). Even more interestingly, the inclusion of spike-timing-dependent plasticity would enable the investigation of stimulation protocols aimed at promoting LTP, such as theta-burst stimulation (Larson and Munkácsy, 2015). This aspect would be of uttermost importance to make a link with memory encoding and retrieval processes (Axmacher et al., 2006; Tsanov and Manahan-Vaughan, 2009; Jutras et al., 2013) and with neurostimulation studies for memory improvement (Titiz et al., 2017; Solomon et al., 2021).

From the point of view of neurostimulation, future work is needed to extend the current model to a multi-compartment representation of neurites, since axons are known to be preferentially activated by extracellular electrical stimulation (Rattay et al., 2003). Specifically, multi-compartment cable models have been developed to investigate spike initiation and propagation by modeling the axon as a series of resistance-capacitance circuits following its trajectory (Rattay et al., 2003; Joucla and Yvert, 2012; Ashida and Nogueira, 2018). These models are particularly suited to study the effects of extracellular stimulation, which are non-intuitive and depend as a first approximation on the second spatial derivative of the electrical potential along the cell membrane (Rattay, 1986; Rattay et al., 2003; McIntyre et al., 2004; Rattay et al., 2018). Here, we have modeled electrical stimulation as an intracellular current applied equally across all neurons in the targeted area, which is extremely simplified but enables computational tractability. Future developments will focus on developing an equivalent multicompartment model with realistic axonal trajectories while making sufficient simplifications to allow for realistic computation times.

Finally, we likened conditions of low theta input to pathological states characteristic of oscillopathies such as Alzheimer’s disease, as these conditions disrupted all aspects of theta-gamma oscillations in our model: theta power, gamma power, and theta-gamma PAC (Figure 5). However, it should be noted that changes in theta or gamma power in these pathologies are often unclear, and that the most consistent alteration that has been reported in Alzheimer’s disease is a reduction of theta-gamma PAC (for review, see Kitchigina, 2018). Future work should explore the effects of cellular alterations intrinsic to the hippocampal formation and their impact on theta-gamma oscillations.

### Outlook

Overall, this new model of the hippocampal formation represents a methodologically innovative basis to further explore multiple neurostimulation strategies that target hippocampal oscillations. Moreover, the limitations discussed above represent important avenues for future refinements, which will require significant work to overcome the costs in terms of computational tractability (e.g. modeling the whole hippocampus, or using multicompartment models of axonal trajectories and dendritic trees). Ultimately, such model refinements should allow the investigation of the effects of extracellular stimulation using charge-balanced biphasic pulses and multipolar electrode configurations with realistic electrode geometries. Most importantly, we believe that our current work may also serve as an inspiration for future computational models of oscillopathies (not necessarily limited to the hippocampus), which could benefit from interfacing abstract sets of synchronizing oscillators and investigating their interactions with biophysically-realistic neurons.

## Materials and methods

### Computational model

#### Overall architecture

We aimed to develop a computational model of the hippocampal formation that is able to generate theta-nested gamma oscillations and takes into account the dynamic nature of the theta input from the medial septum, that is the reset of the theta phase following strong activity in the perforant path or fornix (Buño et al., 1978; Williams and Givens, 2003). To this end, we adapted a previous biophysical model of the human hippocampal formation under fixed sinusoidal input (Aussel et al., 2018) and interconnected it with an abstract representation of the medial septum, modeled as an assembly of Kuramoto oscillators (Kuramoto, 1984; Figure 1).

More precisely, we modeled a 15-mm-thick coronal slice of the hippocampal formation which comprises the DG, the CA3 and CA1 subfields of the hippocampus, and the EC, all populated with excitatory and inhibitory Hodgkin-Huxley neurons. For the medial septum, we opted for a simplified representation where the medial septum projects only to the EC, which in turn drives the different subfields of the hippocampus (see also ‘A computational model of the hippocampal formation with dynamical theta input’, second paragraph). In our model, Kuramoto oscillators are therefore connected to the EC neurons and they receive projections from CA1 neurons (see sections below for more details).

#### Medial septum: Kuramoto oscillators

The medial septum contains pacemaker neurons (Varga et al., 2008; Hangya et al., 2009) that synchronize with one another and generate a global theta rhythm. In turn, these pacemaker neurons drive downstream areas that receive projections from the medial septum. Here, we modeled the entire medial septum neuronal assembly as a set of coupled phase oscillators following the Kuramoto model (Kuramoto, 1984), which generated the driving theta rhythm that was provided to the hippocampal formation through the EC (Breakspear et al., 2010).

Kuramoto oscillators have also been used to investigate the effects of neurostimulation on synchronized brain rhythms in the context of Parkinson’s disease or essential tremor (Tass, 2003; Weerasinghe et al., 2019). Here, each Kuramoto oscillator was described by its phase $\theta_{i}$, which evolves over time according to the following equation:

$$
\frac{d\theta_{i}}{dt}=\omega_{i}+\frac{k}{N}\sumj=1Nsin⁡(\theta_{j}−\theta_{i})+G_{reset}X(t)Z(\theta_{i})
$$

The term $\omega_{i}$ denotes the natural frequency of oscillator $i$, and is normally distributed around the center frequency $f_{0}$ and with standard deviation $\sigma$. The synchronization parameter $k$ represents the coupling strength of the group of oscillators, and $N$ is the number of oscillators. Higher values for the synchronization parameter indicate stronger coupling between pairs of oscillators, thus affecting how fast or slow their phases tend to synchronize. The final product $G_{reset}X(t)Z(\theta_{i})$ is used to describe the effects of external inputs on the phase of the oscillators. Here, the only external input originates in the projections from CA1 to the medial septum. It is described by the instantaneous firing rate $X(t)$ of the CA1 excitatory population. $G_{reset}$ is an arbitrary gain that determines the strength of the CA1 input to the oscillators. Finally, the function $Z(\theta_{i})$ describes how the effects of CA1 inputs on the oscillators depend on the phase of the ongoing theta rhythm.

The coherence and phase of the driving theta rhythm $I_{\theta}$ were computed using the order parameter $r$ to extract the mean amplitude $A$ and the mean phase $ϕ$ of the ensemble of Kuramoto oscillators as follows:

$$
{r(t)=\frac{1}{N}\sumi=1Ne^{j\theta_{i}(t)}A(t)=Re⁡(r)ϕ(t)=Im⁡(r)I_{\theta}(t)=G_{\theta}A(t)\frac{cos⁡(ϕ(t))+1}{2}
$$

where the mean amplitude $A(t)$ and the mean phase $ϕ(t)$ are derived by taking the real and imaginary part of the order parameter respectively, and the output theta rhythm $I_{\theta}(t)$ is a rectified cosine, multiplied by a gain $G_{\theta}$ that controls the maximum output amplitude (in nA).

To simulate the effect of the projections from CA1 to the medial septum on the phase of the oscillators, an approximation of the instantaneous firing rate of the CA1 excitatory population was used as the term $X(t)$. To obtain the instantaneous firing rate, we convolved the CA1 population spike train with an exponential kernel using the following equations:

$$
{\frac{dX}{dt}=−\frac{X}{\tau_{FR}}X_{t+1}=X_{t}+\frac{1}{N\tau_{FR}},∀t\int^{S}
$$

where $t^{S}$ denotes the ordered set of the spike timings, and $\tau_{FR}$ determines the exponential decay of the kernel, which was set to 10ms to compute population activity (for single neurons, a typical value is 100ms) (Gerstner et al., 2014).

Hereafter, we call the term $Z(\theta)$ the phase response function, to distinguish it from the PRC obtained from experimental data or simulations (see section below ‘Data Analysis’, ‘Phase Response Curve’). Briefly, the PRC of an oscillatory system indicates the phase delay or advancement that follows a single pulse, as a function of the phase at which this input is delivered. The phase response function $Z(\theta)$ was chosen to mimic as well as possible experimental PRCs reported in the literature (Lengyel et al., 2005; Kwag and Paulsen, 2009; Akam et al., 2012). These PRCs appear biphasic and show a phase advancement (respectively delay) for stimuli delivered in the ascending (respectively descending) slope of theta. To accurately model this behavior, we used the following equation for the phase response function, where $\theta_{peak}$ represents the phase at which the theta rhythm reaches its maximum and the parameter $ϕ_{offset}$ controls the desired phase offset from the peak:

$$
Z(\theta_{i})=−sin⁡(\theta_{i}−(\theta_{peak}+ϕ_{offset}))
$$

An overview of the default parameters for the Kuramoto oscillators and the bidirectional connections between medial septum-hippocampal formation can be found in Table 1.

**Table 1.**
 Full list of the default parameter values for the Kuramoto oscillators.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th colspan="2">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Number of oscillators (N)</td>
      <td colspan="2">250</td>
    </tr>
    <tr>
      <td>Center frequency (f0)</td>
      <td colspan="2">6 Hz</td>
    </tr>
    <tr>
      <td>Standard deviation (σ)</td>
      <td colspan="2">0.5 HZ</td>
    </tr>
    <tr>
      <td>Synchronization ratio (k/N)</td>
      <td colspan="2">15</td>
    </tr>
    <tr>
      <td>Phase reset gain (Greset)</td>
      <td colspan="2">4</td>
    </tr>
    <tr>
      <td>Peak phase (θpeak)</td>
      <td colspan="2">0 rad</td>
    </tr>
    <tr>
      <td>Firing rate time constant (τFR)</td>
      <td colspan="2">10 ms</td>
    </tr>
  </tbody>
</table>

#### Hippocampal formation: Hodgkin-Huxley Neurons

The following sections describe in detail how individual neurons and synapses were modeled, and are adapted from the original work by Aussel and colleagues (Aussel et al., 2018). Neurons were modeled as conductance-based single compartments, following the Hodgkin-Huxley formalism (Hodgkin and Huxley, 1952), in line with previous work (Aussel et al., 2022; Aussel et al., 2018). The temporal evolution of the membrane potential of each neuron is described by a differential equation whose general form reads:

$$
C_{m}\frac{dV_{m}}{dt}=−I_{L}−\sumchannelI_{channel}−\sumj\in[E,I]I_{syn_{j}}+I_{\theta}+I_{stim}+η
$$

$I_{L}$ denotes the leakage current. $I_{channel}$ are currents associated with specific ion channels, namely potassium ($I_{K}$), fast sodium ($I_{Na}$), and low-threshold calcium ($I_{Ca}$) currents, the CAN current ($I_{CAN}$) (Giovannini et al., 2017), and the M-type potassium channel current ($I_{M}$) responsible for spike adaptation (Kosenko et al., 2012; Sun and Kapur, 2012; Kwag et al., 2014). $I_{syn}$ represents the currents originating from synaptic inputs to the cell and can be either depolarizing (negative sign) or hyperpolarizing (positive sign). $η$ is a Gaussian random noise term accounting for other external inputs and synaptic fluctuations. Theta input from the medial septum is modeled as a depolarizing current and is denoted by $I_{\theta}$, while electrical stimulation is denoted by $I_{stim}$. Excitatory neurons represent pyramidal cells in EC, CA3, and CA1, and granule cells in DG. They were modeled with $I_{Na}$, $I_{K}$, and $I_{Ca}$, and $I_{M}$ currents, with the addition of $I_{CAN}$ for pyramidal cells. Fast-spiking interneurons in all areas were modeled with $I_{Na}$ and $I_{K}$ currents. The complete description for all of the above ionic channels and their corresponding currents can be found in (Giovannini et al., 2017). Leakage currents followed the following equation:

$$
I_{L}=(g_{L}\timesA)\times(V_{m}−E_{L})
$$

where $g_{L}$ is the maximum leakage conductance, $A$ is the area of the single compartment corresponding to the membrane of a neuron, and $E_{L}$ is the reversal potential of the leakage channel.

Channel currents $I_{K}$, $I_{M}$, $I_{CAN}$ obey the following set of equations:

$$
I_{K}=g_{K}\timesA\timesn^{4}\times(V_{m}−E_{K})I_{M}=g_{M}\timesA\timesp\times(V_{m}−E_{M})I_{CAN}=g_{CAN}\timesA\timesm_{CAN}^{2}\times(V_{m}−E_{CAN})
$$

where $g_{K}$, $g_{M}$, $g_{CAN}$ are the maximum conductances for the respective channel, and $n$, $p$, $m_{CAN}$ are the respective gating variables defined by the following differential equations:

$$
\frac{dn}{dt}=\frac{n_{∞}−n}{\tau_{n}}\frac{dp}{dt}=\frac{p_{∞}−p}{\tau_{p}}\frac{dm_{CAN}}{dt}=\frac{m_{CAN,∞}−m_{CAN}}{\tau_{m_{CAN}}}
$$

For the potassium and CAN currents, the steady-state values for their corresponding gating variables $n_{∞}$ and $m_{CAN,∞}$ and their corresponding time constants $\tau_{K}$ and $\tau_{CAN}$ depend on the following functions of the transition rate constants:

$$
n_{∞}=\frac{\alpha_{n}}{\alpha_{n}+\beta_{n}}m_{CAN,∞}=\frac{\alpha_{m_{CAN}}}{\alpha_{m_{CAN}}+\beta_{m_{CAN}}}\tau_{n}=\frac{0.2}{\alpha_{n}+\beta_{n}}\tau_{m_{CAN}}=\frac{0.2}{\alpha_{m_{CAN}}+\beta_{m_{CAN}}}
$$

The sodium current ($I_{Na}$) and calcium current ($I_{Ca}$) follow a similar set of equations:

$$
I_{Na}=g_{Na}\timesA\timesm^{3}\timesh\times(V_{m}−E_{Na})I_{Ca}=g_{Ca}\timesA\timesm^{2}\timesh\times(V_{m}−E_{Ca})
$$

with two gating variables $m$ and $h$ defined by the following differential equations:

$$
\frac{dm}{dt}=\frac{n_{\alpha}−n}{\tau_{n}}\frac{dn}{dt}=\frac{n_{\alpha}−n}{\tau_{n}}m_{∞}=\frac{\alpha_{m}}{\alpha_{m}+\beta_{m}}h_{∞}=\frac{\alpha_{h}}{\alpha_{h}+\beta_{h}}\tau_{m}=\frac{0.2}{\alpha_{m}+\beta_{m}}\tau_{h}=\frac{0.2}{\alpha_{h}+\beta_{h}}
$$

The gating variable of $I_{CAN}$ depends on the calcium concentration within the neuron ($[Ca]_{i}^{2+}$), given by:

$$
\frac{d[Ca]_{i}^{2+}}{dt}=\gamma(I_{Ca})+\frac{([Ca]_{∞}^{2+}−[Ca]_{i}^{2+})}{\tau_{[Ca]^{2+}}}\gamma(I_{Ca})=\frac{−k_{u}\timesI_{Ca}}{2\timesF\timesd\timesA}
$$

where $\tau_{[Ca]^{2+}}$ = 1s represents the rate of calcium removal from the cell, $[Ca]_{∞}^{2+}$ = 0.24 mol/L is the calcium concentration if the calcium channel remains open for a duration of $ΔT→∞$, $k_{u}=10^{4}$ is a unit conversion constant, $F$ is the Faraday constant, and $d$ = 1 μm is the depth at which the calcium is stored inside the cell.

Noise ($η$), accounting for random inputs to the network, was simulated as intracellular current acting on the membrane voltage and following the properties of a Gaussian random variable with a mean of 0 μV and a standard deviation of 1000 μV ($η_{E}∼N(0,1000)$ μV) for excitatory neurons and a mean of 0 μV and standard deviation of 100 μV ($η_{I}∼N(0,100)$ μV) for inhibitory neurons. The ratio of 1:10 between the noise terms was adapted from the original work and it accounts for the higher excitability of the inhibitory neurons as well as the E-I population size ratios.

The original model introduced some parameters representing the vigilance state (i.e. active wakefulness vs slow-wave sleep). However, the present model only focused on the state of active wakefulness, since this is when memory-related theta-nested gamma oscillations occur. For all simulations, the parameters were set so that the network operated in the wakefulness regime in a healthy hippocampus (Aussel et al., 2018). The full expressions for all the parameters defined above can be found in Table 2 for pyramidal cells and in Table 3 for interneurons.

**Table 2.**
 Full list of parameter values and expressions for pyramidal neurons.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Expression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A</td>
      <td>29.103μm2</td>
    </tr>
    <tr>
      <td>Cm</td>
      <td>1μF/cm2</td>
    </tr>
    <tr>
      <td>gL</td>
      <td>0.01mS/cm2</td>
    </tr>
    <tr>
      <td>EL</td>
      <td>−70mV</td>
    </tr>
    <tr>
      <td>gK</td>
      <td>5mS/cm2</td>
    </tr>
    <tr>
      <td>EK</td>
      <td>−100mV</td>
    </tr>
    <tr>
      <td>αn,K</td>
      <td>−0.032Vm+40mV−1+e−0.02(Vm+40mV)</td>
    </tr>
    <tr>
      <td>βn,K</td>
      <td>0.5e−(Vm+45mV)40mV</td>
    </tr>
    <tr>
      <td>gNa</td>
      <td>50mS/cm2</td>
    </tr>
    <tr>
      <td>ENa</td>
      <td>50mV</td>
    </tr>
    <tr>
      <td>αm,Na</td>
      <td>−0.32Vm+42mVe−Vm+42mV4mV−1</td>
    </tr>
    <tr>
      <td>βm,Na</td>
      <td>0.28Vm+15mVe−Vm+15mV5mV−1</td>
    </tr>
    <tr>
      <td>αh,Na</td>
      <td>0.128e−Vm+38mV18mV</td>
    </tr>
    <tr>
      <td>βh,Na</td>
      <td>41+e−Vm+15mV5mV</td>
    </tr>
    <tr>
      <td>gM</td>
      <td>90μS/cm2</td>
    </tr>
    <tr>
      <td>EM</td>
      <td>−100mV</td>
    </tr>
    <tr>
      <td>p∞</td>
      <td>11+e−0.01(Vm+35mV)</td>
    </tr>
    <tr>
      <td>τp</td>
      <td>13.3e(Vm+35mV)20mV+e−(Vm+35mV)20mV</td>
    </tr>
    <tr>
      <td>gCa</td>
      <td>0.1mS/cm2</td>
    </tr>
    <tr>
      <td>ECa</td>
      <td>120mV</td>
    </tr>
    <tr>
      <td>αm,Ca</td>
      <td>−0.055Vm+27mVe−Vm+27mV17mV−1</td>
    </tr>
    <tr>
      <td>βm,Ca</td>
      <td>−0.94eVm+75mV17mV</td>
    </tr>
    <tr>
      <td>αh,Ca</td>
      <td>−0.000457eVm+13mV50mV</td>
    </tr>
    <tr>
      <td>βh,Ca</td>
      <td>0.0065e−Vm+15mV28mV</td>
    </tr>
    <tr>
      <td>gCAN</td>
      <td>25μS/cm2</td>
    </tr>
    <tr>
      <td>ECAN</td>
      <td>−20mV</td>
    </tr>
    <tr>
      <td>αm,CAN</td>
      <td>0.0002e1.4[Ca]i2+0.5mol/L</td>
    </tr>
    <tr>
      <td>βm,CAN</td>
      <td>0.0002e1.4</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Full list of parameter values and expressions for interneurons.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Expression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A</td>
      <td>14.103μm2</td>
    </tr>
    <tr>
      <td>Cm</td>
      <td>1μF/cm2</td>
    </tr>
    <tr>
      <td>gL</td>
      <td>0.1mS/cm2</td>
    </tr>
    <tr>
      <td>EL</td>
      <td>−65mV</td>
    </tr>
    <tr>
      <td>gK</td>
      <td>9mS/cm2</td>
    </tr>
    <tr>
      <td>EK</td>
      <td>−90mV</td>
    </tr>
    <tr>
      <td>αn,K</td>
      <td>0.01Vm+34mV1−e−0.1(Vm+34mV)</td>
    </tr>
    <tr>
      <td>βn,K</td>
      <td>0.125e−Vm+44mV80mV</td>
    </tr>
    <tr>
      <td>gNa</td>
      <td>35mS/cm2</td>
    </tr>
    <tr>
      <td>ENa</td>
      <td>55mV</td>
    </tr>
    <tr>
      <td>αm,Na</td>
      <td>0.1Vm+35mV1−e−0.1(Vm+35mV)</td>
    </tr>
    <tr>
      <td>βm,Na</td>
      <td>4e−Vm+60mV18mV</td>
    </tr>
    <tr>
      <td>αh,Na</td>
      <td>0.07e−Vm+58mV20mV</td>
    </tr>
    <tr>
      <td>βh,Na</td>
      <td>11+e−0.1(Vm+28mV)</td>
    </tr>
  </tbody>
</table>

#### Synaptic models

Inter-neuronal interactions were modeled as instantaneous AMPA and GABA-A synapses using the synaptic currents $I_{syn_{E}}$ and $I_{syn_{I}}$, respectively. Synaptic currents were described by the following bi-exponential differential equations:

$$
I_{syn_{I,E}}=g_{I,E}(V_{m}−E_{I,E})\frac{dg_{I,E}}{dt}=\frac{1}{\tau_{g_{I,E}}}(−g_{I,E}+h_{I,E})\frac{dh_{I,E}}{dt}=−h_{I,E}\frac{1}{\tau_{h_{I,E}}}
$$

where $E_{I,E}$ are the synaptic resting potentials, and $\tau_{g_{I,E}}$ and $\tau_{h_{I,E}}$ are the synaptic time constants of rise and decay for inhibitory and excitatory neurons respectively. The occurrence of a pre-synaptic spike leads to an increase of the values $h_{I}$ or $h_{E}$ in the post-synaptic neuron by a fixed amount, which depends on the type of synapse and the region (due to the presence of cholinergic effects described in the initial model). Specific values for the intra-area and inter-area synaptic connections are given in Table 4 and Table 5, respectively.

**Table 4.**
 A pre-synaptic spike causes an increase in the conductances $h_{e}$ and $h_{i}$ in the post-synaptic neuron.The values for the intra-area connections are given here. Empty cells indicate no connection between the populations.


<table>
  <thead>
    <tr>
      <th></th>
      <th>E→E</th>
      <th>E→I</th>
      <th>I→E</th>
      <th>I→I</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EC</td>
      <td></td>
      <td>20 pS</td>
      <td>600 pS</td>
      <td></td>
    </tr>
    <tr>
      <td>DG</td>
      <td></td>
      <td>180 pS</td>
      <td>1800 pS</td>
      <td></td>
    </tr>
    <tr>
      <td>CA3</td>
      <td>20 pS</td>
      <td>20 pS</td>
      <td>600 pS</td>
      <td></td>
    </tr>
    <tr>
      <td>CA1</td>
      <td></td>
      <td>60 pS</td>
      <td>1800 pS</td>
      <td>1800 pS</td>
    </tr>
  </tbody>
</table>

**Table 5.**
 A pre-synaptic spike causes an increase in the conductances $h_{e}$ and $h_{i}$ in the post-synaptic neuron.The values for the inter-area connections are given here. Empty cells indicate no connection between the areas. Recurrent projections are not allowed and are marked with dashes.


<table>
  <thead>
    <tr>
      <th rowspan="2">Source</th>
      <th colspan="4">Target</th>
    </tr>
    <tr>
      <th>EC</th>
      <th>DG</th>
      <th>CA3</th>
      <th>CA1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EC</td>
      <td>-</td>
      <td>20 pS</td>
      <td>20 pS</td>
      <td>20 pS</td>
    </tr>
    <tr>
      <td>DG</td>
      <td></td>
      <td>-</td>
      <td>180 pS</td>
      <td></td>
    </tr>
    <tr>
      <td>CA3</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>20 pS</td>
    </tr>
    <tr>
      <td>CA1</td>
      <td>60 pS</td>
      <td></td>
      <td></td>
      <td>-</td>
    </tr>
  </tbody>
</table>

#### Hippocampal formation: neuron types and numbers

Each area of the network is comprised of two populations, one excitatory and one inhibitory. Excitatory cells in the DG represent granule cells and pyramidal neurons in all other areas. Interneurons represent basket cells across all areas. The ratio between pyramidal neurons and interneurons was directly adapted from Aussel et al., 2018. The ratio between pyramidal neurons and interneurons was kept as a ratio of 10:1 for all areas except the dentate gyrus, where the ratio was 100:1. The number of neurons per subfield of the hippocampal formation is summarized in Table 6.

**Table 6.**
 Number of neurons per subfield of the hippocampal formation, divided by neuron type.


<table>
  <thead>
    <tr>
      <th>Area</th>
      <th>NExc</th>
      <th>NInh</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EC</td>
      <td>10,000</td>
      <td>1,000</td>
    </tr>
    <tr>
      <td>DG</td>
      <td>10,000</td>
      <td>100</td>
    </tr>
    <tr>
      <td>CA3</td>
      <td>1,000</td>
      <td>100</td>
    </tr>
    <tr>
      <td>CA1</td>
      <td>10,000</td>
      <td>1,000</td>
    </tr>
  </tbody>
</table>

A two-dimensional simplified image depicting a coronal slice of the hippocampal formation (Aussel et al., 2018) was used as a basis for a two-dimensional manifold that was uniformly populated by neurons following a density-driven approach (Rougier, 2018). Pyramidal neurons were uniformly distributed within the stratum pyramidale (or within the stratum granulosum for the dentate gyrus) and interneurons were uniformly distributed within the stratum oriens. Initial neuron positions were drawn from a blue noise distribution and a Voronoi diagram was computed. To adjust the positions of the neurons over a centroidal Voronoi diagram, the Lloyd relaxation algorithm was applied for 1000 iterations. Transitioning from a two-dimensional manifold to a 3D reconstruction of the hippocampal formation was achieved through the addition of the third coordinate with values uniformly distributed between 0 and 15 mm.

#### Hippocampal formation: inputs and connectivity

The hippocampal formation receives most of its external inputs from the EC. Activity from the EC is projected to all hippocampal subfields, starting with the DG. DG granule cells project onto the CA3 pyramidal cells via mossy cell fibers. CA3 projects in turn to CA1 via Schaffer collaterals. These connections form the tri-synaptic pathway. Direct connections from the EC towards the CA3 and CA1 subfields through the monosynaptic pathway are also considered. Pyramidal neurons from CA1 project to pyramidal neurons and interneurons in the EC, closing the hippocampal-entorhinal loop. CA1 pyramidal neurons also project to the medial septum through the fornix. An overview of the connections between areas is presented in panel B of Figure 1.

In the current model, EC pyramidal neurons and interneurons receive oscillatory theta input from the medial septum in the form of an excitatory intracellular current as described in Equation 2 and Equation 5. Projections from CA1 towards the medial septum were modeled as a signal representing the collective firing rate of the CA1 pyramidal neurons. All connections towards and from the medial septum are summarized in panels A and B of Figure 1.

Synaptic connectivity between neurons within a region is characterized using a probability $p$ and is distance-based, following a Gaussian-like distribution (Equation 14) with a width $\sigma$ of 2500 μm (excitatory synapses) and 350 μm (inhibitory synapses). The value of $A_{intra}$ defines the maximum probability of connection between two neurons separated by an infinitesimal distance (i.e. for $D→0$). The maximum values for $A_{intra}$ are given in Table 7.

$$
p=A_{intra}exp⁡(−\frac{D^{2}}{2\sigma^{2}})
$$

**Table 7.**
 Maximum probability of connection ($A_{intra}$, Equation 14) between neurons within each region.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Py-Py</th>
      <th>Py-Inh</th>
      <th>Inh-Py</th>
      <th>Inh-Inh</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EC</td>
      <td>0</td>
      <td>0.37</td>
      <td>0.54</td>
      <td>0</td>
    </tr>
    <tr>
      <td>DG</td>
      <td>0</td>
      <td>0.06</td>
      <td>0.14</td>
      <td>0</td>
    </tr>
    <tr>
      <td>CA3</td>
      <td>0.56</td>
      <td>0.75</td>
      <td>0.75</td>
      <td>0</td>
    </tr>
    <tr>
      <td>CA1</td>
      <td>0</td>
      <td>0.28</td>
      <td>0.3</td>
      <td>0.7</td>
    </tr>
  </tbody>
</table>

Inter-area connectivity followed a similar Gaussian-like distribution (Equation 15), however, only excitatory projections were considered and the distance $D_{z}$ was computed only across the z-coordinate. Pyramidal neurons from the source area projected to pyramidal neurons and interneurons in the target area, with connectivity probabilities drawn from the said distribution with a width $\sigma$ of 1000 μm.

$$
p=min(1,A_{inter}exp⁡(−\frac{D_{z}^{2}}{2\sigma^{2}}))
$$

#### Tuning input gain and connection strengths: targeted firing rates

We adjusted the input gain ($G_{\theta}$) and inter-area connection strengths ($A_{inter}$) to target an overall oscillatory rhythm $f_{osc,targ}$ at the driving frequency of the input, that is, 6 Hz, and a mean firing rate of each excitatory population $f_{exc,targ}$ also at 6 Hz (meaning that each excitatory cell should spike on average once per theta cycle). Because of the ratio between excitatory and inhibitory neurons in the model, this resulted in firing rates of about 60 Hz in inhibitory neurons. These targeted values were inspired by literature in behaving rodents showing that hippocampal pyramidal neurons typically fire at rates below 10 Hz, usually between 1 and 2 Hz, and that interneurons fire at rates between 20 and 80 Hz (Hirase et al., 2001). In practice, the obtained firing rates were constrained by the simplifications made in the model.

The mean population firing rate $f_{exc}$ was computed by counting the number of spikes in the last second of a 3 s simulation run, to avoid edge effects due to the non-physiological initial conditions, and by averaging this number over time and across neurons. The oscillatory frequency $f_{osc}$ was computed as the mean of the inverse of the timing between all pairs of consecutive peaks in the theta rhythm. Finally, the metric used to adjust parameters (input strength and connection strengths) was calculated as the Euclidean distance between the targeted and obtained firing rate and oscillatory rate:

$$
J=\sqrt{(f_{exc}−f_{exc,targ})^{2}+(f_{osc}−f_{osc,targ})^{2}}
$$

#### Tuning input and connection strengths: detailed procedure

The input gain ($G_{\theta}$, Equation 2) and inter-area connection strengths ($A_{inter}$, Equation 15) were sequentially adjusted using the following heuristics. All simulations were performed for a duration of 3 s, and the first 2 s were excluded from the analysis to avoid edge effects. The network was initialized with membrane voltages uniformly distributed in the range [-70, -60] mV. Our initial point was a fully uncoupled model in which all the connection strengths were set to 0. The tuning procedure was performed in the absence of noise.

Following the above procedure, the inter-area synaptic connectivity parameters were set for all subsequent simulations. The values are summarized in Table 8. Empty cells denote no effective connectivity.

**Table 8.**
 Inter-area connection strengths ($A_{inter}$).The source is always the excitatory population of the subfield. The same values are used when targeting excitatory and inhibitory populations. Empty cells indicate no connections. EC: Entorhinal Cortex, DG: Dentate Gyrus.


<table>
  <thead>
    <tr>
      <th rowspan="2">Source</th>
      <th colspan="4">Target</th>
    </tr>
    <tr>
      <th>EC</th>
      <th>DG</th>
      <th>CA3</th>
      <th>CA1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EC</td>
      <td>-</td>
      <td>13.0</td>
      <td>0.14</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>DG</td>
      <td></td>
      <td>-</td>
      <td>0.14</td>
      <td></td>
    </tr>
    <tr>
      <td>CA3</td>
      <td></td>
      <td></td>
      <td>-</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>CA1</td>
      <td>0.2</td>
      <td></td>
      <td></td>
      <td>-</td>
    </tr>
  </tbody>
</table>

#### Numerical implementation

The model was implemented with the Brian2 libraries for Python (Stimberg et al., 2019; see Data availability section for access to the code). Simulations were performed using a timestep of 0.1ms and a total simulation duration ranging between 3 and 10 s (depending on the experiment, see results section). The average time for simulating 1 s for the complete model locally was 10 min.

#### Neural mass model interfaced with Kuramoto oscillators

The neural masses represented in Figure 3—figure supplement 4, were modeled using the Wilson-Cowan formalism, with parameters adapted from Onslow et al., 2014. Specifically, the firing rates of the excitatory and inhibitory populations were determined by the following equations:

$$
{\tau_{E}\frac{dE}{dt}=−E+f(g_{E}\theta_{E}+W_{EE}E−W_{IE}I+stim_{E}(t))\tau_{I}\frac{dI}{dt}=−I+f(g_{I}\theta_{I}+W_{EI}E)
$$

with the following parameters: $\tau_{E}=\tau_{I}=3.2ms$, $g_{E}=0.7$, $g_{I}=0$, $W_{EE}=4.8$, $W_{EI}=W_{IE}=4$, and $W_{II}=0$. The sigmoid response function was not modified from the original work, and was defined as:

$$
f(x)=\frac{1}{1+e^{−\beta(x−x_{m})}}
$$

with parameters $\beta$ and $x_{m}$ set to 4 and 1 respectively, according to the original model. The Kuramoto oscillators were modeled according to Equation 1. For these simulations we used a set of $N=100$ oscillators with a center frequency $f_{0}$ of 4 Hz, a synchronization ratio $\frac{k}{N}$ of 25, and a strong phase reset gain $G_{reset}$ of 90. Other parameters were kept as previously shown in Table 1. The neural masses were coupled to the Kuramoto oscillators by linking the variable $X(t)$ in Equation 1 with the variable $E(t)$ in Equation 17.

We increased the phase reset gain significantly compared to the Hodgkin-Huxley model, as the Onslow model utilized a sigmoid function with values between 0 and 1, whereas the instantaneous firing rate of the populations of single-compartment neurons was much higher and therefore had a stronger phase resetting effect.

### Data analysis

During each simulation, we monitored and exported the following data for subsequent analysis: (i) spike timings per neuron, (ii) time series of ionic currents, (iii) septal input theta rhythm and phase, and (iv) time series of electrical stimulation. Theta phase was wrapped between $[−\pi,\pi]$ with a phase of 0 radians corresponding to the peak of theta rhythm. All PAC analyses were performed using the TensorPAC toolbox for Python (Combrisson et al., 2020).

#### Firing rates

To obtain instantaneous firing rates, the corresponding spike trains were binned in 5 ms rectangular windows with a 90% overlap (i.e. consecutive windows were spaced by 0.5ms). The number of spikes within each bin was normalized by the bin size and the number of neurons in the group, yielding instantaneous population firing rates. Where reported (i.e. values $\mu_{I}$ and $\mu_{E}$ in Figure 3A), the mean population firing rates within a given time window (typically lasting several seconds) were computed by binning all spikes in that time window and normalizing by the window width and the number of neurons in the population.

#### Spectral analyses

Power spectral density (PSD) estimates were calculated based on Welch’s method. The periodogram was computed using 1 s windows with a 90% overlap, yielding a frequency resolution of 1 Hz. The average spectral power within a specific frequency band was calculated using Simpson’s rule within the desired frequency band $\mu_{I}$. Spectrograms were computed using the short-time Fourier transform with a sliding Hann window of 100 ms width and 99% overlap, yielding a frequency resolution of 10 Hz.

#### Modulation index

The MI (Tort et al., 2008) was used to estimate the degree of PAC between theta and gamma oscillations in the model. To compute the MI, the normalized firing rate traces were band-pass filtered in the frequency ranges of interest: 3–9 Hz for theta (referred to as the ‘phase signal’) and 40–80 Hz for gamma (referred to as the ‘amplitude signal’). Then, the phase and amplitude time series were extracted from the filtered signals using the Hilbert transform. A histogram of the mean amplitude of gamma over the phase of theta was then extracted, using phase bins of 5 degrees. The MI was finally calculated as the Kullback-Leibler divergence between the mean amplitude distribution and the uniform distribution. A higher MI indicates stronger PAC. For a schematic representation regarding the computation of the MI, refer to Figure 1 in Tort et al., 2010. These computations were performed using the provided PreferredPhase and Pac methods from the TensorPAC library for Python (Combrisson et al., 2020).

#### Comodulograms

Comodulograms represent the amount of PAC between two ranges of frequencies, used to extract respectively a phase and an amplitude signal. Specifically, we computed the MI between 80% overlapping 1 Hz frequency bands used to compute the phase of the signal (in the theta range), and 90% overlapping 10 Hz frequency bands used to compute the amplitude of the signal (in the gamma range). The resulting distribution of MI values was subsequently plotted as heat maps. An inherent problem with the computation of the MI using simulated data was the lack of frequency components in some frequency bands. Filtering the data within 1 Hz frequency bands thus created a flat signal, resulting in high values of the MI despite the absence of modulation. To overcome this limitation, we added uniform noise to the firing rate signals prior to computing the MI, with an amplitude of approximately 20% of the maximum instantaneous firing rates. The results with and without added noise are presented in Figure 3—figure supplement 2.

#### Phase dependency of PAC

For a given theta frequency, PAC depends on the phase of the underlying theta oscillation. To identify this relationship and the theta phase that maximizes coupling, we used the PreferredPhase function of the TensorPAC toolbox. More precisely, we applied a Hilbert transform to extract the phase of the theta signal (firing rate band-pass filtered between 3 and 9 Hz) and the amplitude of the gamma signal band-pass filtered within narrow (10 Hz wide) frequency ranges between 20 and 100 Hz with a 90% overlap. For each narrow gamma range, we binned the amplitude with respect to the phase in a similar way as in the calculation of the MI. We obtained a vector of the binned high-frequency amplitudes with respect to the phase of the low-frequency phase, represented as a polar plot as in Figure 3C.

#### Phase response curves

The PRC of an oscillatory system indicates the phase delay or advancement that follows a single pulse, as a function of the phase at which this input is delivered. To characterize the PRC of our computational model, we applied a single stimulation pulse to CA1 across different phases of the theta rhythm and calculated the resulting change in the theta phase. We split a single theta cycle into intervals of width $\pi/8$ radians and applied a single stimulation pulse of a given amplitude. For each case, we ran two simulations: one with a stimulation pulse and one without. Finally, we compared the theta phase 2.5ms post-stimulation and at the same time but in the absence of stimulation. The resulting values for the phase difference $Δϕ$ were plotted against the stimulation phase and are presented in Figure 3D for varying stimulation amplitudes.
