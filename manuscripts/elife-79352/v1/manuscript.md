# A prefrontal network model operating near steady and oscillatory states links spike desynchronization and synaptic deficits in schizophrenia

## Authors

- David A Crowe<sup>1</sup>
- Andrew Willow<sup>1</sup>
- Rachael K Blackman<sup>2</sup>
- Adele L DeNicola<sup>2</sup>
- Matthew V Chafee<sup>2</sup> ([ORCID: 0000-0001-9289-0239](https://orcid.org/0000-0001-9289-0239)) †
- Bagrat Amirikian<sup>2</sup> ([ORCID: 0000-0001-8080-0902](https://orcid.org/0000-0001-8080-0902)) †

### Affiliations

1. Department of Biology, Augsburg University Minneapolis United States ([ROR:057ewhh68](https://ror.org/057ewhh68))
2. Department of Neuroscience, University of Minnesota Minneapolis United States ([ROR:017zqws13](https://ror.org/017zqws13))
3. Medical Scientist Training Program (MD/PhD), University of Minnesota Minneapolis United States ([ROR:017zqws13](https://ror.org/017zqws13))
4. Brain Sciences Center, VA Medical Center Minneapolis United States ([ROR:032b8d361](https://ror.org/032b8d361))
5. Center for Cognitive Sciences, University of Minnesota Minneapolis United States ([ROR:017zqws13](https://ror.org/017zqws13))

† Corresponding author

## Abstract

Schizophrenia results in part from a failure of prefrontal networks but we lack full understanding of how disruptions at a synaptic level cause failures at the network level. This is a crucial gap in our understanding because it prevents us from discovering how genetic mutations and environmental risks that alter synaptic function cause prefrontal network to fail in schizophrenia. To address that question, we developed a recurrent spiking network model of prefrontal local circuits that can explain the link between NMDAR synaptic and 0-lag spike synchrony deficits we recently observed in a pharmacological monkey model of prefrontal network failure in schizophrenia. We analyze how the balance between AMPA and NMDA components of recurrent excitation and GABA inhibition in the network influence oscillatory spike synchrony to inform the biological data. We show that reducing recurrent NMDAR synaptic currents prevents the network from shifting from a steady to oscillatory state in response to extrinsic inputs such as might occur during behavior. These findings strongly parallel dynamic modulation of 0-lag spike synchrony we observed between neurons in monkey prefrontal cortex during behavior, as well as the suppression of this 0-lag spiking by administration of NMDAR antagonists. As such, our cortical network model provides a plausible mechanism explaining the link between NMDAR synaptic and 0-lag spike synchrony deficits observed in a pharmacological monkey model of prefrontal network failure in schizophrenia.

## Introduction

NMDAR synaptic malfunction has been implicated as causal in schizophrenia (Fromer et al., 2014; Schizophrenia Working Group of the Psychiatric Genomics Consortium, 2014; Timms et al., 2013), and loss of NMDAR synaptic function in prefrontal networks is believed to contribute to cognitive deficits as well as clinical symptoms in the disease (Goldman-Rakic, 1999; Javitt et al., 2012; Wang et al., 2013). However, we do not have a complete understanding of how NMDAR synaptic mechanisms influence neural dynamics in prefrontal networks, nor how the disruption of NMDAR synaptic mechanisms might cause prefrontal networks to malfunction. To address these questions, we recently investigated how blocking NMDAR altered neural dynamics and effective communication between neurons in prefrontal cortex of monkeys performing a cognitive control task measuring deficits in schizophrenia (Blackman et al., 2013; Jones et al., 2010; Kummerfeld et al., 2020; Zick et al., 2018). We found that reducing NMDAR synaptic communication reduced the frequency of synchronous (‘0-lag’) spiking between neurons, as well as effective communication between neurons on timescales consistent with monosynaptic interactions between them (Kummerfeld et al., 2020; Zick et al., 2022; Zick et al., 2018). Whereas these studies suggested that NMDAR synaptic function and spike timing in prefrontal networks were linked, they did not elucidate the circuit mechanisms responsible.

In the current study, we developed a spiking neural network model to understand mechanisms that might mediate the link between NMDAR synaptic malfunction and neural dynamics (reduced 0-lag synchronous spiking) we observed in biological data (Kummerfeld et al., 2020; Zick et al., 2022; Zick et al., 2018). The network is comprised of leaky integrate-and-fire neurons embedded in a sparsely connected recurrent network employing realistic NMDAR, GABAR, and AMPAR mediated synaptic currents. We use network stability and mean field analyses to investigate how the balance between NMDA and AMPA components of recurrent excitatory and GABA inhibitory currents influence regimes of network dynamics and spiking synchrony.

For cortical neurons synchrony can occur naturally due to the local recurrent network connectivity, even when external afferent inputs are entirely uncorrelated. Theoretical studies have shown that such synchrony can arise in randomly connected recurrent networks operating in asynchronous irregular (Amit, 1989; Amit and Brunel, 1997; Brunel, 2000; Renart et al., 2010; van Vreeswijk and Sompolinsky, 1996; Vicente et al., 2008) and synchronous irregular regimes (Brunel, 2000; Brunel and Hakim, 1999; Brunel and Wang, 2003; Ledoux and Brunel, 2011). In both regimes, individual neurons fire spikes highly irregularly at low rates, a typical situation in a cortex. The major distinction is that in an asynchronous regime population spike rate is steady in time, whereas in a synchronous regime it becomes oscillatory.

We show that simulated prefrontal networks operating near the boundary between steady (asynchronous irregular) and oscillatory (synchronous irregular) regimes in the synaptic parameter space can explain several key experimental observations. First, such networks achieve biologically realistic stochastic spike trains and firing rates of excitatory and inhibitory neurons in prefrontal cortex. Second, increased extrinsic inputs, such as those that might occur during behavior, shift these networks from a steady to an oscillatory regime that causes the emergence of 0-lag spiking between neurons as they stochastically entrain to oscillatory population activity. Third, and perhaps most importantly, we show that reducing recurrent NMDAR synaptic currents prevents these networks from transitioning into oscillatory activity in response to extrinsic inputs, thereby preventing the emergence of 0-lag spike synchrony. Although prior modeling studies have addressed the relationship between NMDAR function and oscillatory activity in prefrontal networks (Brunel and Wang, 2003; Compte et al., 2000; Kirli et al., 2014; Wang, 1999), none account for this range of experimental observations. The current results allow us to establish strong parallels between simulated and biological data, including the emergence of 0-lag synchronous spiking via recurrent synaptic interactions between neurons during behavior, the association between synchronous spiking and oscillatory population activity, as well as their joint dependence on NMDAR synaptic mechanisms, both in our current simulation and in the neural data (Zick et al., 2018).

## Results

### Summary of experimental results

In this section, we summarize main experimental findings reported previously by our group (Zick et al., 2018). In that study, spike trains of ensembles of single neurons were recorded simultaneously from PFC of monkeys while they performed the dot-pattern expectancy (DPX) task, a task that measures specific deficits in cognitive control in schizophrenia (Jones et al., 2010). In the DPX task, the correct response (left or right joystick movement) to a probe stimulus depends on a preceding cue followed by a delay period (Materials and methods).

In the present study, we focus on PFC population spike dynamics recorded in the DPX task under two conditions: drug-naive and drug. The drug naive data were collected before monkeys were administered drug, phencyclidine, which is an NMDA receptor antagonist. Figure 1 shows the population average pairwise correlation between spike trains of neurons recorded in drug-naive (black) and drug (magenta) conditions. The strength of spike correlation was quantified by the ratio between the observed frequency of synchronous spikes (1ms resolution) and the frequency expected if the spike trains were uncorrelated (we subtracted 1 from this ratio so that correlation value is zero for uncorrelated, positive for correlated, and negative for anticorrelated spike activity, Materials and methods). The frequency of spike synchrony was determined from activity observed during a short (100 ms-long) window that was slid across time of task performance. Figure 1A shows that spike synchrony obtained from trials aligned to the cue onset (time 0) remained relatively weak and unchanged during the cue and delay periods, until the probe onset, in both drug-naive and drug conditions. The corresponding population average spike rates during these periods are shown in Figure 1C. Because the instant of response after probe presentation varied from trial to trial, to appreciate the time course of synchrony and spike rate after the delay period immediately preceding the response, in Figure 1B and D we aligned trials to response time (time 0). It is seen that synchrony started to increase sharply about 200ms before the motor response in the drug-naive condition and reached its peak at the time of the response (Figure 1B, black). The spike rate also started to increase before the response but more gradually and starting earlier before the response (Figure 1D, black). Both spike synchrony (Figure 1B) and spike rate (Figure 1D) exhibited secondary peaks occurring approximately 150–250ms after the response. In the drug condition, however, the increase in spike synchrony at the time of the response was markedly weakened (Figure 1B, magenta). The increase in spike rate was also reduced, although less dramatically (Figure 1D, magenta). We term this effect as NMDAR blockage induced desynchronization of spiking activity.

![Figure 1.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig1-v1.jpg)

**Figure 1.:** Plots show time evolution of spike synchrony (A, B) and spike rate (C, D) estimated with 100 ms temporal resolution for drug-naive (black) and drug (magenta) conditions. Spike synchrony was measured with 1 ms resolution, and only neuron pairs for which a reasonably reliable estimation of synchrony could be achieved contributed to the plots (see Materials and methods). (A, C): Trials are aligned to the cue onset ($t=0$ ms); in all trials, the cue was presented until $t=1,000$ ms (yellow shaded area), followed by a 1,000 ms delay period, after which the probe was presented at $t=2,000$ ms for 500 ms (green shaded area). Color-coded horizontal error-bars indicate the mean and standard deviation of the motor response time for the corresponding drug condition. The numbers of contributing pairs for drug-naive and drug conditions are 524 and 195 (A), and the number of neurons are, correspondingly, 514 and 343 (C). (B, D): Trials are aligned to the time of motor response ($t=0$ ms) to show the temporal modulation of synchrony and spike rate during the last 600 ms immediately preceding the response. Color-coded horizontal error-bars indicate the mean and standard deviation of the probe presentation time for the corresponding drug condition. The numbers of contributing pairs for drug-naive and drug conditions are 661 and 223 (B), and the number of neurons are, correspondingly, 538 and 343 (D). Shaded grey and magenta bands show the standard errors for spike synchrony (A, B) and rate (C, D). Green asterisks show the instances of times when the drug-naive and drug conditions are statistically different (false discovery rate 0.05 [Benjamini and Hochberg, 1995] using two-sample t-test p-values).

### Network model and theoretical framework

To understand the phenomenon of drug-induced desynchronization of spiking activity and the role played by various components of synaptic currents, we considered a spiking network model representing a local circuit of monkey PFC. Details of the model and the theoretical framework are given in Materials and methods. Here, we only highlight their main aspects.

The network comprises excitatory and inhibitory neurons representing populations of pyramidal cells and interneurons, respectively. All neurons are modeled as leaky integrate-and-fire units (see, e.g., Dayan and Abbott, 2001). Synaptic connections are random and sparse, but the number of connections received by individual neurons is large. In addition to the recurrent local connections, each neuron also receives external connections from excitatory neurons outside of the network that fire spikes with rate $ν_{X}$.

Recurrent synaptic currents of excitatory connections are two-component, mediated by AMPA and NMDA receptors, whereas currents of inhibitory connections are mediated by GABAA receptors (GABA thereafter). External currents represent the noisy inputs due to the background synaptic activity and are mediated by AMPA receptors. Thus, the model entails eight maximal synaptic conductance parameters $g_{X,\alpha}$, $g_{AMPA,\alpha}$, $g_{NMDA,\alpha}$, $g_{GABA,\alpha}$ corresponding to the external AMPA, recurrent AMPA, NMDA, and GABA currents ($\alpha=E,I$ for excitatory and inhibitory neurons, respectively).

To produce a desired regime of network dynamics (asynchronous or synchronous) with a given firing rate of excitatory and inhibitory neurons $ν_{E}$ and $ν_{I}$, respectively, the values of the conductance parameters should be properly adjusted. For this purpose, we used mean field analysis. In this framework, population mean firing rates $v_{E}^{0}$ and $v_{I}^{0}$ in the asynchronous stationary state of the network can be effectively parametrized by three parameters expressed as ratios of component synaptic currents: $I_{AMPA}/I_{GABA}$, $I_{NMDA}/I_{GABA}$, and $I_{X,E}/I_{\theta,E}$, where $I_{R}$ is the mean current of the $R$-receptor mediated synapse ($R=X,AMPA,NMDA,GABA$), and $I_{\theta,E}$ is the current that is needed for an excitatory neuron to reach firing threshold $\theta$ in absence of recurrent feedback. These parameters characterize the balance between recurrent excitation and inhibition, and the balance between external input and firing threshold. Once they are specified, for a given external spike rate $ν_{X}$ one can solve the mean field equations to obtain the underlying eight synaptic conductances providing the desired population mean firing rates $v_{E}^{0}$ and $v_{I}^{0}$ in asynchronous state of the network.

While the mean field analysis allows us to determine synaptic conductances that achieve desired firing rates of neurons, whether these rates remain stable over time is another issue. To address it, we conduct a linear stability analysis of the asynchronous state to understand if the network develops oscillatory instability caused by small fluctuations in population firing rates. This analysis entails two parameters, $\lambda$ and $\omega$, describing the rate of instability growth and the oscillation frequency. The asynchronous state is stable when $\lambda<0$; in this case small perturbations of firing rates cause exponentially damped oscillation of network activity. The case $\lambda=0$ corresponds to the onset of instability of the asynchronous state and the emergence of sustained sinusoidal oscillations of population average firing rates with frequency $\omega$; in the oscillatory regime spike trains remain sparse and irregular but at each oscillation cycle a random subset of network neurons fire synchronously giving rise to the synchronous irregular state. Lastly, when $\lambda>0$, small fluctuations in the stationary rates develop oscillatory instability with the amplitude of oscillations growing exponentially in time; however, higher order terms neglected in linear analysis can eventually saturate the instability growth (Brunel and Hakim, 1999), resulting in a stable oscillation with a finite amplitude.

To examine the boundary between the regions of asynchronous and synchronous states, we fix the balance of tonic NMDA current relative to GABA current, $I_{NMDA}/I_{GABA}$, and vary the remaining two parameters: the balance between recurrent excitation and inhibition, $I_{AMPA}/I_{GABA}$, and the balance between external excitation and firing threshold, $I_{X,E}/I_{\theta,E}$. For a given point in this $(I_{AMPA}/I_{GABA},I_{X,E}/I_{\theta,E})$ parameter plane we solve the mean field equations to find the underlying set of eight synaptic conductances that provide the prescribed rates $v_{E}^{0}$ and $v_{I}^{0}$ given external spike rate $ν_{X}$, and then carry out linear stability analysis to find out if these rates are stable. Figure 2A shows a state diagram of the system for which external spike rate is set to $ν_{X}=5$ Hz, the rates of excitatory and inhibitory populations are set to $v_{E}^{0}=5$ Hz, $v_{I}^{0}=20$ Hz, and the NMDA current balance is fixed at $I_{NMDA}/I_{GABA}=0.15$. The diagram shows solutions for $\lambda$ obtained from the linear stability analysis in the $(I_{AMPA}/I_{GABA},I_{X,E}/I_{\theta,E})$ parameter space. The asynchronous stationary state corresponds to the region where $\lambda<0$, whereas the synchronous oscillation state is realized in the region where $\lambda>0$. The asynchronous and synchronous states are separated by a “critical” or instability line on which $\lambda=0$ (shown in white color in Figure 2A). This boundary is the locus where the stationary network dynamics becomes unstable, and the sinusoidal oscillation of network activity develops. The oscillation frequency on the critical line, $f_{ntwrk}=\omega/2\pi$, as a function of the balance between the recurrent AMPA and GABA currents, $I_{AMPA}/I_{GABA}$, is shown in Figure 2B.

![Figure 2.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig2-v1.jpg)

**Figure 2.:** Parameters are as follows: prescribed firing rates of excitatory and inhibitory populations are 5 Hz and 20 Hz, respectively; external input spike rate is 5 Hz; and the balance between NMDA and GABA currents is fixed at 0.15. (A:) State diagram in the $(I_{AMPA}/I_{GABA},I_{X,E}/I_{\theta,E})$ parameter plane showing color coded value of the rate of instability growth $\lambda$: in the region of the parameter space where $\lambda<0$ the asynchronous state is stable, whereas the region where $\lambda>0$ corresponds to the synchronous oscillation state. The two regimes are separated by a critical line on which $\lambda=0$. This boundary, shown by a white line, is the locus where the stationary network dynamic becomes unstable, and oscillatory population activity develops. Each point in this parameter plane corresponds to a network with a specific set of eight synaptic conductances provided by the mean field approximation. Red and blue asterisks are the points in the state diagram corresponding to the steady and critical primary networks, respectively (see Selection of Primary Networks in Results). (B:) Network oscillation frequency that develops on the critical line as a function of the balance between AMPA component of recurrent excitation and inhibition.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A:) Critical line separating the asynchronous and synchronous states in the $(I_{AMPA}/I_{GABA},I_{X,E}/I_{\theta,E})$ parameter plane is shown for several values of the $I_{NMDA}/I_{GABA}$ balance. (B:) Oscillation frequency on the critical line as a function of the balance between AMPA component of recurrent excitation and GABA inhibition. Plots for different values of the $I_{NMDA}/I_{GABA}$ balance nearly completely overlap.

The characteristic features of the state diagram qualitatively remain unchanged when the balance between the NMDA and GABA currents is varied (Figure 2—figure supplement 1A). Furthermore, the network frequency at the onset of oscillation, $f_{ntwrk}$, essentially is independent of the $I_{NMDA}/I_{GABA}$ balance (Figure 2—figure supplement 1B).

### Integration of DPX task context and drug condition into the model

To study spike synchrony in asynchronous and synchronous networks in the context of the DPX task performed in drug-naive and drug conditions (Zick et al., 2018), we make two assumptions regarding neural and synaptic activity: (1) the increase in spike synchronization observed before the monkey’s response in Zick et al., 2018 is due to task-specific external afferent signals received by PFC neurons after probe presentation; (2) administration of NMDAR antagonist results in blocking NMDAR mediated synaptic currents. In the framework of our model, we implemented these assumptions as follows: task specific external signals were accounted for by an increase in the external spike rate from its background level $ν_{X}$, whereas the effect of drug administration was modeled by setting NMDAR conductances $g_{NMDA,E}$ and $g_{NMDA,I}$ to zero.

Next, to investigate how spike synchrony in asynchronous and synchronous networks depends on the modulations of $v_{X}$ and $g_{NMDA,\alpha}$, for each network regime we proceed with the following three steps. First, we choose proper values for conductances, so that the underlying network operates in a desired regime providing the prescribed population firing rates $v_{E}^{*}$ and $v_{I}^{*}$ for a given external spike rate $v_{X}^{*}$. We shall designate this network as the primary network relating to the underlying regime and distinguish the corresponding values of all its parameters by the asterisk (*). Second, we carry out a series of network simulations, in which external spike rate $v_{X}$ and NMDAR conductance $g_{NMDA,\alpha}$ are varied relative to their standard values $v_{X}^{*}$ and $g_{NMDA,\alpha}^{*}$, respectively. Lastly, for each simulated network, we compute population average pairwise correlation between spike trains of neurons and analyze how this correlation depends on the external spike rate and NMDAR conductance.

### Selection of primary networks

To perform a comparison between the primary networks, we need to choose appropriate values for their parameters. We begin with the parameters that are common to both networks. First, we set the excitatory and inhibitory population mean firing rates to $v_{E}^{*}=5$ Hz and $v_{I}^{*}=20$ Hz, respectively, which are on the order of magnitude of spontaneous rates observed for PFC neurons. Second, since external inputs represent activity of excitatory neurons outside the PFC circuit model, we choose the background external rate $v_{X}^{*}$ to be the same as the excitatory population rate $v_{E}^{*}$ inside the model and, thus, set $v_{X}^{*}=5$ Hz. Lastly, for both networks, we fix the balance between NMDA and GABA currents at $I_{NMDA}^{*}/I_{GABA}^{*}=0.15$. Note that the state diagram in the $(I_{AMPA}/I_{GABA},I_{X,E}/I_{\theta,E})$ space shown in Figure 2A was obtained exactly for these values of the above listed parameters. We use this state diagram for selecting the primary networks and determining the remaining parameters that are network specific.

In this regard, we note that each point in the $(I_{AMPA}/I_{GABA},I_{X,E}/I_{\theta,E})$ plane corresponds to a network with a specific set of synaptic conductances. For synchronous regime, we look for a network on the critical line ($\lambda=0$, white line in Figure 2A), at the onset of oscillatory instability with a frequency in the $\gamma$-band (a frequency band associated with the LFPs recorded from prefrontal areas [Bastos et al., 2018; Lundqvist et al., 2016]). For instance, the point marked by a blue asterisk in Figure 2A located at $(I_{AMPA}^{∗}/I_{GABA}^{∗}=0.4,I_{X,E}^{∗}/I_{\theta,E}^{∗}=1.09)$ corresponds to such a network with oscillation frequency $f_{ntwrk}^{*}~58$ Hz (Figure 2B). In the following, we refer to this network as the critical state primary network.

Correspondingly, for the asynchronous regime, we need to select a network that is far from the critical line and deep in the region of stable network dynamics ($\lambda<0$). The point marked by a red asterisk in Figure 2A located at $(I_{AMPA}^{∗}/I_{GABA}^{∗}=0.2,I_{X,E}^{∗}/I_{\theta,E}^{∗}=1.09)$ is an example of such a network. We shall refer to this network as the steady state primary network. For each primary network, we obtain the underlying set of eight synaptic conductance parameters $g_{GABA,\alpha}^{*},g_{NMDA,\alpha}^{*},g_{AMPA,\alpha}^{*},g_{xAMPA,\alpha}^{*}$ ($\alpha=E,I$) by numerically solving the mean field equations.

### Correlation of spiking activity and synchrony in the asynchronous and synchronous states

To investigate characteristic features of spiking dynamics in asynchronous and synchronous regimes, we carried out direct simulations of the primary networks. Both networks comprise $N=5,000$ neurons, of which $N_{E}=4,000$ are excitatory and $N_{I}=1,000$ inhibitory. Neurons are connected randomly with a probability $p=0.2$. Figure 3 illustrate the behavior of simulated networks with synaptic conductance parameters corresponding to the steady and critical primary networks indicated by the red and blue asterisks, respectively, in the state diagram presented in Figure 2A. The dynamic behavior is shown at the level of individual cell activity (spike rasters, top of panels in Figure 3), as well as whole population activity (bottom of panels in Figure 3).

![Figure 3.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig3-v1.jpg)

**Figure 3.:** Conductance parameters are solutions of mean field equations for the steady state primary network (A1, B1) and the critical state primary network (A2, B2) corresponding to the red and blue asterisks, respectively, in the $(I_{AMPA}/I_{GABA},I_{X,E}/I_{\theta,E})$ state plane shown in Figure 2A and inset. (A1, B1), (A2, B2): Top, spike rasters (sorted by rate) of 200 excitatory (black) and 50 inhibitory (green) neurons. Bottom, time-varying activity (1ms resolution) of excitatory (black) and inhibitory (green) populations. (A1, A2): External input spike rate $ν_{X}=5$ Hz. Excitatory and inhibitory neurons display average firing rates of, respectively, 5.3 Hz and 20 Hz (A1), and 6.3 Hz and 22 Hz (A2). (B1, B2): In these simulations $ν_{X}$ was increased by 5%. Excitatory and inhibitory neurons display average firing rates of, respectively, 7.5 Hz and 25 Hz (B1), and 12 Hz and 34 Hz (B2).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A1, B1): Spectra of the steady state network activities shown in Figure 3A1 and Figure 3B1, respectively. (A2, B2): Spectra of the critical state network activities shown in Figure 3A2 and Figure 3B2, respectively.

In simulations shown in Figure 3 panels A1 and A2 external spike rate $ν_{X}$ was fixed at the level of $v_{X}^{*}=5$ Hz chosen for the primary networks. It is seen that excitatory and inhibitory neurons exhibit highly irregular firing with average rates, $ν_{E}$ and $ν_{I}$, about 5.2 Hz and 20 Hz in the steady state primary network (Figure 3A1) and 5.5 Hz and 21 Hz in the critical state primary network (Figure 3A2). These observed in simulations rates $ν_{E}$ and $ν_{I}$ are in good agreement with the prescribed rates $v_{E}^{*}=5$ Hz and $v_{I}^{*}=20$ Hz that were used to derive the synaptic conductance parameters of the simulated networks. Moreover, Figure 3A1 demonstrates that population activity of the steady state primary network is rather stationary in time, whereas activity of the critical primary network shown in Figure 3A2 exhibits signs of developing of oscillatory instability (compare Figure 3—figure supplement 1A1 vs Figure 3—figure supplement 1A2). Thus, spiking dynamics observed in the simulated steady state primary network displays basic characteristics of the asynchronous regime—irregular firing of individual neurons and stationary population activity. Correspondingly, the behavior of the simulated critical state primary network exhibits similarity with the boundary regime on which the asynchronous stationary state destabilizes and oscillatory behavior of the population activity emerges.

Panels B1 and B2 in Figure 3 demonstrate results of simulations in which external spike rate $ν_{X}$ was increased by 5% relative to the rate $v_{X}^{*}$ used in simulations illustrated in Figure 3 panels A1 and A2. For the steady state primary network (Figure 3B1), the firing rates of excitatory and inhibitory neurons increase with the external drive. However, the regime of network dynamics qualitatively does not change and remains asynchronous (compare Figure 3—figure supplement 1A1 vs Figure 3—figure supplement 1B1). In contrast, stronger external inputs received by the critical state primary network synchronize population activity (Figure 3B2). It is seen that while individual neurons continue to fire irregularly, population activity now clearly exhibits oscillatory behavior, indicating that the network is in synchronous irregular regime in which the average firing frequency of neurons is low, about 20 Hz, compared to the frequency of network oscillation, which is about 50 Hz (see Figure 3—figure supplement 1B2). This frequency is close to the theoretically predicted network frequency of 58 Hz near the onset of oscillation.

Thus, direct simulations confirm that analytically derived network parameters for both steady and critical primary networks provide the anticipated regimes of network dynamics.

To facilitate the comparison of characteristic features exhibited by a simulated network with experimentally measurable quantities, we compute temporal correlation of spiking activity that quantifies average pairwise correlation between spike trains of excitatory neurons. In the context of the DPX task performed in drug-naive and drug conditions studied in Zick et al., 2018 and with the purpose of elucidating the mechanism of drug-induced desynchronization of spiking activity, we investigated how temporal correlations depend on the strength of external drive and the NMDAR mediated synaptic current. To this end, we varied external input rate $v_{X}$ and the NMDAR conductance parameters $g_{NMDA,E}$ and $g_{NMDA,I}$ relative to their respective standard values $v_{X}^{*}$, and $g_{NMDA,E}^{*}$ and $g_{NMDA,I}^{*}$ , while keeping all other system parameters fixed, and performed simulations of the ensuing networks. Conductances for excitatory and inhibitory neurons were scaled with the same factor and, therefore, their relative values $g_{NMDA,E}/g_{NMDA,E}^{*}$ and $g_{NMDA,I}/g_{NMDA,I}^{*}$ are the same; in the following we drop the $E,I$ designation.

Figure 4 displays correlation of spiking activity (panels A1, A2, C1, C2) and synchrony (0-lag correlation, panels B1, B2, D1, D2) obtained from spike trains of simulated steady (panels A1, B1, C1, D1) and critical (panels A2, B2, C2, D2) networks for a range of $v_{X}/v_{X}^{*}$ (panels A1, A2, B1, B2) and $g_{NMDA}/g_{NMDA}^{*}$ (panels C1, C2, D1, D2) values. It is seen that in the steady state primary network correlations are weak and insensitive to the modulations of external input rate or NMDAR conductance (Figure 4 panels A1, B1, C1, D1). In contrast, in the critical state primary network temporal correlations show sharp dependence on these parameters (Figure 4 panels A2, C2), and with decreasing external drive or decreasing NMDAR conductance profoundly attenuating spike synchrony (Figure 4 panels B2, D2).

![Figure 4.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig4-v1.jpg)

**Figure 4.:** Conductance parameters are solutions of mean field equations for the steady state primary network (A1, B1, C1, D1) and the critical state primary network (A2, B2, C2, D2) corresponding to the red and blue asterisks, respectively, in the $(I_{AMPA}/I_{GABA},I_{X,E}/I_{\theta,E})$ state plane shown in Figure 2A and inset. For the steady state network, correlation and synchrony are weak and insensitive to the modulation of external input spike rate $ν_{X}$ (A1, B1) and NMDAR conductance $g_{NMDA}$ (C1, D1). In contrast, for the critical state network spike correlation depends strongly on the external spike rate (A2) and NMDAR conductance (C2) and the degree of spike synchrony could be modulated from relatively weak to strong (B2, D2). Results shown in (C1, D1, C2, D2) are obtained from simulations in which $ν_{X}$ is increased by 5%. The magnitudes of modulation of $ν_{X}$ and $g_{NMDA}$ are normalized by their standard values $v_{X}^{*}$ and $g_{NMDA}^{*}$, respectively. The numbers next to color-coded lines for spike correlation plots show the normalized magnitudes of external input spike rates, $v_{X}/v_{X}^{*}$, (A1, A2) and NMDAR conductance, $g_{NMDA}/g_{NMDA}^{*}$, (C1, C2).

### Circuit mechanisms of spike synchronization modulation

What are the network mechanisms of external drive and NMDA conductance dependent spike synchronization? Why in the network close to the boundary between asynchronous and synchronous regimes, are spike correlations strongly affected by the modulations of external inputs and recurrent NMDA currents, but in the network far from this boundary and deep in the region of the asynchronous regime, correlations are essentially independent of these modulations? How does the interplay between synchronous and asynchronous regimes at their boundary lead to spike synchronization when external input rate $ν_{X}$ increases, and to desynchronization when the NMDA conductance $g_{NMDA}$ decreases?

To answer these questions and to illuminate the role of asynchronous and synchronous regimes in the shaping of network-wide synchronization of spiking activity, we carried out linear stability analysis in the $(v_{X}/v_{X}^{∗},g_{NMDA}/g_{NMDA}^{∗})$ parameter plane while keeping the remaining parameters fixed. For both steady and critical state primary networks, stability is investigated in the vicinity of the standard values of the external input spike rate and NMDAR conductances corresponding to the respective networks.

Figure 5 illustrates state diagrams in the $(v_{X}/v_{X}^{∗},g_{NMDA}/g_{NMDA}^{∗})$ plane in the neighborhood of the steady (Figure 5A) and critical (Figure 5B) state primary networks. As in Figure 2A, the critical line ($\lambda=0$) separating the asynchronous stationary ($\lambda<0$) and synchronous oscillatory ($\lambda>0$) states is shown in white color. Asterisks correspond to the loci of the steady (Figure 5A) and critical (Figure 5B) state primary networks in these parameter planes. It is seen that the modulations of $ν_{X}$ and $g_{NMDA}$ in the steady state primary network (Figure 5A) do not change the network state; these modulations have no impact on the spike correlation and the strength of synchrony (Figure 4B1 and D1 and Figure 5A insets).

![Figure 5.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig5-v1.jpg)

**Figure 5.:** Network state diagrams in th e $(v_{X}/v_{X}^{∗},g_{NMDA}/g_{NMDA}^{∗})$ plane.The critical line ($\lambda=0$, white line) separates the parameter plane into regions of asynchronous stationary ($\lambda<0$) and synchronous oscillatory ($\lambda>0$) regimes. In the state diagram for the steady state network (A) the critical line is beyond the area covered by the diagram. Asterisks correspond to the steady (A) and critical (B) state primary networks in these planes. Color-coded arrows show the range of modulation of $ν_{X}$ (yellow) and $g_{NMDA}$ (magenta) corresponding to the range of modulation of these parameters for which temporal correlations of spiking activity and synchrony are shown in Figure 4. The insets show how spike synchrony changes along the corresponding arrows in the state diagrams. These insets display the same plots for spike synchrony that are shown in panels B1 and B2 (bottom insets in A and B, correspondingly) and D1 and D2 (right insets in A and B, correspondingly) in Figure 4.

In contrast, the modulations of $ν_{X}$ and $g_{NMDA}$ in the critical state primary network (Figure 5B) induce transitions between the network states. Specifically, as the external input spike rate $ν_{X}$ increases (horizontal yellow arrow in Figure 5B) the system crosses the boundary between asynchronous and synchronous regimes and the network state changes from stationary to oscillatory; this transition is accompanied by a sharp increase in spike synchrony (Figure 4B2 and Figure 5B bottom inset). The decrease of NMDAR conductance $g_{NMDA}$ (vertical magenta arrow in Figure 5B) causes the system to cross the boundary again, and the network state changes now from oscillatory to stationary; this transition is accompanied by a sharp decrease in spike synchrony (Figure 4D2 and Figure 5B right inset).

Thus, this analysis reveals that networks that are close to the boundary between asynchronous and synchronous regimes, in contrast to asynchronous networks that are far from this boundary, have a rich dynamic behavior. The dynamic states of these networks could be easily switched around by modulations in the external drive and the strength of recurrent excitation by NMDAR mediated currents. Switching between the network states, in turn, results in sharp changes in the degree of network-wide synchronization of spiking activity in response to these modulations.

### Explaining the effects of blocking of NMDAR observed in primate PFC by the prefrontal circuit model

As illustrated in Figure 1B, spiking activity observed in monkey PFC in the DPX task (Zick et al., 2018) remains practically desynchronized after probe presentation for about 200ms but it begins to increase sharply about 200ms before the motor response. To get a deeper insight into the properties of spike timing dynamics, we show in Figure 6 temporal correlations of spiking activity during the 200ms period following probe presentation (Figure 6A1) and during the 200ms period preceding the motor response (Figure 6B1) in drug-naive (black) and drug (magenta) conditions. It can be now appreciated that in drug-naive condition, population activity during the pre-response period develops characteristics of synchronized oscillation behavior, as signaled by the appearance of time lagged peaks of correlation (blue arrows, Figure 6B1, black). However, administration of a drug blocking NMDAR desynchronizes neuronal activity during this period (Figure 6B1, magenta).

![Figure 6.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig6-v1.jpg)

**Figure 6.:** (A1, B1) Plots show population average temporal correlations between spiking activity of neuron pairs recorded from PFC during the 200 ms period immediately following probe presentation (A1) and the 200 ms period immediately preceding the motor response (B1) in the DPX task (Zick et al., 2018). In the drug-naive condition (black line), population activity during the pre-response period develops characteristics of synchronous oscillation with a frequency of ∼55 Hz (peaks at time lags ±18 ms, blue arrows, B1). Administration of a drug blocking NMDAR (magenta line) desynchronizes neuronal activity during the pre-response period (B1). (A2, B2, C) Temporal correlations (A2, B2) computed from spike trains of simulated networks corresponding to four conditions shown in the $(ν_{X}/v_{X}^{∗},g_{NMDA}/g_{NMDA}^{∗})$ state plane (C) by bold dots and arrow heads: initial probe ( $v_{X}/v_{X}^{*}=0.97$, A2) and pre-response ( $v_{X}/v_{X}^{*}=1.03$, B2) periods for drug-naive ( $g_{NMDA}/g_{NMDA}^{∗}=1.25$, black line) and drug ( $g_{NMDA}/g_{NMDA}^{*}=0$, magenta line) conditions. The critical line ($\lambda=0$, white line in panel C) separates the parameter plane into regions of asynchronous stationary ($\lambda<0$) and synchronous oscillation ($\lambda>0$) regimes. The locus of the blue asterisk corresponds to the critical state primary network in this plane.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** In a large (network size $N≫1$) and sparsely connected network (probability of connection $p≪1$), when the population average firing rate is stationary and the network is in the asynchronous state, spike synchrony vanishes in the limit $N→∞,p→0$, while the average number of connections of individual neurons $C=pN$ remains finite. The small 0-lag peak seen for the asynchronous network in panel Figure 6 A2 is due to the effect of the finite size of the network (Brunel and Hakim, 1999) in the simulations. The plot shows spike synchrony obtained from the spike trains of the asynchronous steady (red circles) and synchronous oscillatory networks (blue circles) as a function of the simulated network size (from left to right, $N=$ 20,000, 10,000, 5,000, and 3,333). The red and blue lines represent linear fits to the corresponding simulated data. It can be seen that, as the sizes of the networks increase, the synchrony of the asynchronous network extrapolates to zero in the limit $N→∞$, whereas for the synchronous network it remains finite. Solid red and blue circles correspond to the networks in panels (Figure 6 A2 and B2), respectively.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** In the framework of computational modeling studies of cortical networks, it is commonly assumed that the model network receives specific external inputs during specific events such as cue/probe presentations in the course of a behavioral task. It is assumed that such inputs are received by a small (~10%) specific group of neurons, which are selective to a particular cue/probe. In our model, we assume that during the pre-response period all network neurons receive elevated external input, which is modeled as an increase in the external spike rate from its background level. Due to this input the network switches from the steady asynchronous to synchronous oscillatory dynamics resulting in the increase of spike synchrony, similarly to what is observed in the course of the DPX task around the time of response (Figure 1B). On the other hand, during the cue and initial probe presentation periods no increase in the spike synchrony occurs in the empirical data (Figure 1A, B). To understand whether our model is consistent with this observation as well, we carried out a series of simulations in which the fraction of neurons $f$ that received the increase in external spike rate varied from 0 to 1. The plot shows spike synchrony obtained from the spike trains of simulated networks as a function of the fraction $f$. In this approach, the cue and probe presentations correspond to the case when relatively small fraction of neurons ($f<0.2$) receive the increase in external input, in contrast to the case of the pre-response period, when all neurons receive increased input ($f=1$). It is seen that for small $f$ the spike synchrony remains week, which is in agreement with the experimental observations. The solid red and blue circles correspond to the spike synchrony values of networks in panel Figure 6A2 and Figure 6B2, respectively.

The presence of strong spike synchrony (0ms lag) together with the correlation peaks at ±18 ms lags in the pre-response period (Figure 6B1), and the absence of these characteristics in the initial probe period (Figure 6A1) suggest that after probe presentation but before motor response network dynamics switches from the asynchronous stationary state to the synchronous oscillation state with a $\gamma$-frequency around 55 Hz. Desynchronization of neuronal activity produced by drug administration implies that NMDAR blockage prevents PFC circuits operating in the asynchronous regime from switching to synchronous dynamics.

These experimental findings could be readily explained by a prefrontal network model that operates on the boundary between asynchronous and synchronous regimes. We start by recalling that in the framework of our approach the pre-response afferent signals, which we assume are received by PFC neurons before the monkey’s response, are modeled as an increase in the external spike rate from its background level $ν_{X}$. This assumption is supported by the increase in the population spike rate preceding the monkey’s response observed in neural data shown in Figure 1D. Secondly, the effect of drug administration is modeled by setting NMDAR conductances $g_{NMDA,E}$ and $g_{NMDA,I}$ to zero. The capacity of the prefrontal network model to provide a circuit mechanism for the emergence of synchrony in spiking activity and drug-dependent desynchronization can be illustrated by considering the system’s behavior in the $(v_{X}/v_{X}^{∗},g_{NMDA}/g_{NMDA}^{∗})$ state plane around the point $(v_{X}/v_{X}^{∗}=1,g_{NMDA}/g_{NMDA}^{∗}=1)$ corresponding to the critical state primary network (Figure 6C). In this space, the effects of probe presentation on the spiking dynamics of the prefrontal circuit model under drug-naive ($g_{NMDA}/g_{NMDA}^{∗}=1.25$) and drug ($g_{NMDA}/g_{NMDA}^{*}=0$) conditions are represented, respectively, by black and magenta horizontal arrows (Figure 6C). The arrows are pointing from the state of the network corresponding to the initial probe period ($v_{X}/v_{X}^{∗}=0.97$) to the network state corresponding to the pre-response period ($v_{X}/v_{X}^{∗}=1.03$).

In drug-naive condition, increase in the external spike rate $v_{X}$ switches the circuit model from asynchronous to synchronous regime (Figure 6C, black arrow crosses the boundary between the regimes). The oscillation frequency is about 50 Hz, which is manifested in the temporal correlations of spiking activity as a sharp increase in synchrony and appearance of peaks at ±20 ms lags (Figure 6A2 vs B2, black line). This is very similar to what is observed in monkey PFC during the initial probe and pre-response periods in the DPX task (Fig. 6A1 vs A2 and B1 vs B2, black line). In the drug condition, setting NMDAR conductance to zero prevents the circuit model from switching to the synchronous regime in response to an increase in the external spike rate $v_{X}$ (Figure 6C, magenta arrow does not cross the boundary between the regimes). This, in turn, considerably reduces the degree of spike synchrony compared to drug-naive condition (Figure 6B2, magenta vs black line), similar to the desynchronizing effect of NMDAR antagonist administration on spiking activity in monkey PFC (Figure 6 B1, magenta vs black line).

In the consideration above, we investigated the network spiking dynamics in the asynchronous and synchronous states during stationary external input at a decreased ($v_{X}/v_{X}^{*}=0.97$) and increased ($v_{X}/v_{X}^{*}=1.03$) external rate. To simulate a more biologically realistic scenario, we also examined the network behavior in response to transient external input. In this analysis, external input rate had a trapezoid-like temporal profile (Figure 7A). First, external rate was fixed at a lower level ($v_{X}/v_{X}^{*}=0.97$) setting the network in the asynchronous state. Then, throughout 100ms period the rate was linearly increased to a higher level ($v_{X}/v_{X}^{*}=1.05$) and kept constant for 400ms, pushing the network across the boundary to the synchronous state. Finally, the rate was decreased to the initial level during the next 100ms to switch the network back to the asynchronous state. Figure 7 shows time evolution of population spike rate (Figure 7B) and synchrony (Figure 7C) in response to such transient external input (Figure 7A) for $g_{NMDA}/g_{NMDA}^{*}=1.25$ (black) and $g_{NMDA}/g_{NMDA}^{*}=0$ (magenta) corresponding to drug-naive and drug conditions, respectively. These simulated temporal profiles can be compared with the temporal profiles shown in Figure 1 for population average spike rate (Figure 1D) and synchrony (Figure 1B) obtained from experimental data. Parallels between the simulated and recorded neural data are evident. Spike synchrony and spike rate peak at about the same time both in simulated (Figure 7B and C) and recorded (Figure 1B and D) neural activity. Further, the increase in spike rate is early and gradual in comparison to the increase in spike synchrony which is delayed and abrupt both in simulated (Figure 7B and C) and recorded (Figure 1B and D) neural activity. While our relatively simple model qualitatively is consistent with dynamical features of the firing rate and synchrony observed in primate PFC, there are, however, some quantitative discrepancies in firing rates. In addition, recorded neural activity exhibits complex dynamics following the response (Figure 1B and D), that are not evident in the simulation (Figure 7B and D). This presumably reflects temporal modulation of synaptic inputs to the recorded neurons in the biological data that are more complex than the ramp transient we implemented in the simulation.

![Figure 7.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig7-v1.jpg)

**Figure 7.:** (A) Temporal profile of external rate. Initially, external rate is fixed at a lower level ($v_{X}/v_{X}^{*}=0.97$) and the network is in the asynchronous state. At time $t=0$ the rate begins to increase and in the next 100 ms it crosses the boundary between the asynchronous and synchronous states reaching a higher level ($v_{X}/v_{X}^{*}=1.05$). The rate is kept constant for the next 400 ms and, afterwards, it decreases within 100 ms and returns to its initial level corresponding to the asynchronous state. (B, C) Average population spike rate (B) and synchrony (C) obtained from spike trains of 100 network simulations that received the transient external input shown in A for drug-naive ($g_{NMDA}/g_{NMDA}^{∗}=1.25$, black line) and drug conditions ($g_{NMDA}/g_{NMDA}^{*}=0$, magenta line). Shaded grey and magenta bands show the standard errors for spike rate (B) and synchrony (C). (D) Population average temporal correlations between spiking activity of neuron pairs obtained in simulations during the 200 ms period shown in (C) by yellow shaded area.

In summary, the analyses of simulations with stationary and transient external inputs suggest that when the prefrontal network model operates close to the boundary between asynchronous stationary and synchronous oscillatory regimes it has a considerable capacity to capture experimentally observed aspects of spike synchrony in both drug-naive and drug conditions.

### Role of the balance between NMDAR mediated recurrent excitation and GABA inhibition

So far, in most of our analyses, we did not vary the balance between the tonic component of recurrent excitation mediated by NMDA and GABA inhibition, keeping it fixed at $I_{NMDA}^{*}/I_{GABA}^{*}=0.15$. We have only shown that the network frequency at the onset of oscillation essentially is independent of the $I_{NMDA}/I_{GABA}$ balance (Figure 2—figure supplement 1B), and that the characteristic features of the $(I_{AMPA}/I_{GABA},I_{X,E}/I_{\theta,E})$ state diagram qualitatively remain unchanged when this balance is varied (Figure 2—figure supplement 1A). Could, however, the $I_{NMDA}^{*}/I_{GABA}^{*}$ balance be crucial for the prefrontal circuit model capacity to provide the underlying mechanism for external input and NMDA conductance dependent spike synchronization? To investigate this issue, we analyzed how characteristic features of the $(v_{X}/v_{X}^{∗},g_{NMDA}/g_{NMDA}^{∗})$ state diagram shown in Figure 6C depend on the $I_{NMDA}^{*}/I_{GABA}^{*}$ balance.

Figure 8 shows state diagrams in the $(v_{X}/v_{X}^{∗},g_{NMDA}/g_{NMDA}^{∗})$ plane obtained for several $I_{NMDA}^{*}/I_{GABA}^{*}$ balance values. It is seen that the orientation of the critical line in the state space depends on the $I_{NMDA}^{*}/I_{GABA}^{*}$ balance. When the balance is shifted toward stronger inhibition ($I_{NMDA}^{∗}/I_{GABA}^{∗}<0.15$, Figure 8A), the critical line becomes too steep: in the drug condition, blocking NMDA current may not necessarily lead to spike desynchronization because the external spike modulation could trigger the network to switch to the synchronous regime (magenta arrow in Figure 8A). On the other hand, when the balance is shifted toward stronger tonic excitation ($I_{NMDA}^{∗}/I_{GABA}^{∗}>0.15$, Figure 8C), the critical line becomes too flat: in the drug-naive condition the external spike modulation may not be able to produce strong enough synchrony because the system would be too close to the critical line, and not shift deep enough into the region of the synchronous regime (black arrow in Figure 8C).

![Figure 8.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig8-v1.jpg)

**Figure 8.:** State diagrams in the $(v_{X}/v_{X}^{∗},g_{NMDA}/g_{NMDA}^{∗})$ plane obtained for several values of the balance between the NMDA and GABA currents.Notations are the same as in Figure 6C. (A) $I_{NMDA}^{*}/I_{GABA}^{*}=0.05$; (B) $I_{NMDA}^{*}/I_{GABA}^{*}=0.15$; (C) $I_{NMDA}^{*}/I_{GABA}^{*}=0.25$. Note that the critical line orientation depends on the $I_{NMDA}^{*}/I_{GABA}^{*}$ balance.

### Dependence of oscillatory instability growth rate on synaptic parameters

Further insights into how synaptic conductances and external rate affect synchrony can be achieved by obtaining an analytic expression describing the dependence of the rate of oscillatory instability growth $\lambda$ on these parameters near the boundary between the asynchronous and synchronous states. Such expression can be derived by linearizing the stability analysis equations in the limit of small relative changes $\Deltag_{AMPA}/g_{AMPA}^{*}$, $\Deltag_{NMDA}/g_{NMDA}^{*}$, $\Deltag_{GABA}/g_{GABA}^{*}$, and $\Deltav_{X}/v_{X}^{*}$ of the synaptic parameters around the critical point ${g_{AMPA,{E,I}}^{∗},g_{NMDA,{E,I}}^{∗},g_{GABA,{E,I}}^{∗},v_{X}^{∗}}$ corresponding to the onset of oscillatory instability where $\lambda=0$ (conductances $g_{R,E}$ and $g_{R,I}$ of excitatory and inhibitory neurons ($R=AMPA,NMDA,GABA$) are again scaled with the same factors and, thus, their relative changes are equal: $\Deltag_{R,E}/g_{R,E}^{*}=\Deltag_{R,I}/g_{R,I}^{*}$). The calculation is detailed in the Materials and methods section. The result is that $\lambda$ in the vicinity of the critical point on the boundary between the steady and oscillatory states can be approximated by

$$
\lambda=Λ_{AMPA}(\frac{Δg_{AMPA}}{g_{AMPA}^{∗}}+\frac{Δϕ_{I_{syn,E}}^{′}}{ϕ_{I_{syn,E}}^{′}})+Λ_{NMDA}(\frac{Δg_{NMDA}}{g_{NMDA}^{∗}}+\frac{Δϕ_{I_{syn,E}}^{′}}{ϕ_{I_{syn,E}}^{′}})−Λ_{GABA}(\frac{Δg_{GABA}}{g_{GABA}^{∗}}+\frac{Δϕ_{I_{syn,I}}^{′}}{ϕ_{I_{syn,I}}^{′}}),
$$

where $Λ_{AMPA}$, $Λ_{NMDA}$, and $Λ_{GABA}$ are quantities defined by the parameters of the critical state network around which the equations are linearized, $ϕ_{I_{syn,\alpha}}^{`}$ is the slope of the neuron’s current-frequency response function at the critical state, and $\Deltaϕ_{I_{syn,\alpha}}^{`}$ is the change in the slope of the response function due to the deviations of the synaptic parameters from their critical values ($\alpha=E,I$ for excitatory and inhibitory neurons, respectively). The deviations of the synaptic conductances $\Deltag_{AMPA}$, $\Deltag_{NMDA}$, $\Deltag_{GABA}$, and external rate $\Deltav_{X}$ give rise to the changes in the corresponding average recurrent $I_{AMPA}$, $I_{NMDA}$, $I_{GABA}$ and external $I_{X}$ synaptic currents. This produces the change $\DeltaI_{syn}$ in the average total current $I_{syn}=I_{X}+I_{AMPA}+I_{NMDA}-I_{GABA}$ and shifts the operating point of the current-frequency response function $v=ϕI_{syn}$ that describes the relationship between the average total input current $I_{syn}$ and the output firing frequency of the neuron $v$. For the leaky integrate-and-fire neuron model, $ϕ$ is a monotonically increasing non-linear function (see, e.g., Renart et al., 2003). Thus, the shift of the operating point of the neuron’s response function $ϕ$ due to the change $\DeltaI_{syn}$ in the total average synaptic current results not only in the change of the firing rate (i.e. $\Deltaϕ$), but also in the change of the slope of the response function $\Deltaϕ_{I_{syn}}^{`}$. The latter can be calculated by linearizing the self-consistent mean field equations (see Materials and methods). As a result, $\Deltaϕ_{I_{syn}}^{`}$ is approximated as

$$
\frac{Δϕ_{I_{syn,\alpha}}^{′}}{ϕ_{I_{syn,\alpha}}^{′}}=U_{\alpha}(\frac{I_{X}}{I_{GABA}}\frac{Δv_{X}}{v_{X}^{∗}}+\frac{I_{AMPA}}{I_{GABA}}\frac{Δg_{AMPA}}{g_{AMPA}^{∗}}+\frac{I_{NMDA}}{I_{GABA}}\frac{Δg_{NMDA}}{g_{NMDA}^{∗}}−\frac{Δg_{GABA}}{g_{GABA}^{∗}}),\alpha=E,I,
$$

where $U_{\alpha}$ is a positive constant defined by the parameters of the critical state network around which the mean field equations are linearized. The analytical expression for $\lambda$ given by Equation 1, 2 provides a very good approximation of the exact relationship (see Appendix 1).

Within the linear approximation, the change $\Deltaϕ_{I_{syn}}^{`}$ is proportional to the change $\DeltaI_{syn}$ :

$$
\frac{Δϕ_{I_{syn,\alpha}}^{`}}{ϕ_{I_{syn,\alpha}}^{`}}=U_{\alpha}\frac{\DeltaI_{syn}}{I_{0}},
$$

where $I_{0}$ is a positive constant. Hence, from Equation 2 it follows that $\DeltaI_{syn}$ is proportional to the expression in the brackets:

$$
\DeltaI_{syn}=I_{0}\frac{I_{X}}{I_{GABA}}\frac{\Deltav_{X}}{v_{X}^{*}}+\frac{I_{AMPA}}{I_{GABA}}\frac{\Deltag_{AMPA}}{g_{AMPA}^{*}}+\frac{I_{NMDA}}{I_{GABA}}\frac{\Deltag_{NMDA}}{g_{NMDA}^{*}}-\frac{\Deltag_{GABA}}{g_{GABA}^{*}}.
$$

From Equation 1 it follows that the rate of oscillatory instability growth $\lambda$ directly depends on the changes in the synaptic conductances but does not explicitly depend on the external rate variation $\Deltav_{X}$. However, $\lambda$ depends on $\Deltav_{X}$ indirectly via the terms involving the change in the slope $\Deltaϕ_{I_{syn}}^{`}$ due to the change in the average total synaptic current $\DeltaI_{syn}$ (Equations 3, 4). In fact, $\DeltaI_{syn}$ is affected by the variations of the synaptic conductances as well. Thus, the rate of instability growth $\lambda$ not only directly depends on the synaptic conductances, but also indirectly via the effect of the recurrent excitatory and inhibitory currents mediated by them on the average total synaptic current and, therefore, the operating point of the current-frequency response function.

The factors $Λ_{AMPA}$, $Λ_{NMDA}$, and $Λ_{GABA}$ govern the strength of the direct and indirect contributions of the changes in the synaptic conductances $\Deltag_{AMPA}$, $\Deltag_{NMDA}$, and $\Deltag_{GABA}$ to the oscillatory instability. By inspecting Equation 1, one can see that the strength of the direct contribution of the change $\Deltag_{R}$ ($R=AMAPA,NMDA,GABA$) is determined only by the corresponding factor $Λ_{R}$ via the term $Λ_{R}\Deltag_{R}/g_{R}^{*}$. However, the strength of its indirect contribution is determined by all three factors, $Λ_{AMPA}$, $Λ_{NMDA}$, and $Λ_{GABA}$, through the changes in the slopes $\Deltaϕ_{I_{syn,E}}^{`}$ and $\Deltaϕ_{I_{syn,I}}^{`}$, which depend on $\Deltag_{R}$ (Equation 2). For example, the strength of direct contribution to $\lambda$ due to the change in the GABAR conductance $\Deltag_{GABA}$ is determined only by $Λ_{GABA}$ via the term $Λ_{GABA}\Deltag_{GABA}/g_{GABA}^{*}$ in Equation 1. However, the strength of indirect contribution from $\Deltag_{GABA}$ is determined by all three factors $Λ_{AMPA}$, $Λ_{NMDA}$, and $Λ_{GABA}$ via the terms $Λ_{AMPA}\Deltaϕ_{I_{syn,E}}^{`}/ϕ_{I_{syn,E}}^{`}$, $Λ_{NMDA}\Deltaϕ_{I_{syn,E}}^{`}/ϕ_{I_{syn,E}}^{`}$, and $Λ_{GABA}\Deltaϕ_{I_{syn,I}}^{`}/ϕ_{I_{syn,I}}^{`}$ in Equation 1 because $\Deltaϕ_{I_{syn,E}}^{`}$ and $\Deltaϕ_{I_{syn,I}}^{`}$ themselves depend on $\Deltag_{GABA}$ (Equation 2). As noted above, this indirect contribution is due to the change in the average total synaptic current and, therefore, the change in the operating point of the current-frequency response function.

Figure 9 illustrates the contributions of individual terms involving $Λ_{AMPA}$, $Λ_{NMDA}$, and $Λ_{GABA}$ in Equation 1 to the oscillatory instability growth rate $\lambda$. The panels display separately four cases in which one of the synaptic parameters is varied while the remaining three are kept constant at their critical values. It is seen that in all four cases the dominant contribution to $\lambda$ is coming from the term involving $Λ_{AMPA}$. The contribution related to $Λ_{NMDA}$ is nearly zero, whereas the contribution from $Λ_{GABA}$ term is much smaller than the one from $Λ_{AMPA}$. While both $Λ_{NMDA}$ and $Λ_{GABA}≪Λ_{AMPA}$, the primary reasons are different (see Appendix 2).

![Figure 9.](https://cdn.elifesciences.org/articles/79352/elife-79352-fig9-v1.jpg)

**Figure 9.:** Contributions from various terms in the analytical approximation of the oscillatory instability growth rate $\lambda$.The plots show separately the rate $\lambda$ and its individual terms $Λ_{AMPA}$, $Λ_{NMDA}$, and $Λ_{GABA}$ (Equation 1) as functions of the relative deviations from the critical value of external rate (A), AMPAR conductance (B), NMDAR conductance (C), and GABAR conductance (D). The comparison is performed by varying the underlying parameter while keeping the other parameters at their critical values. Black lines correspond to the rate $\lambda$, whereas red, green, and blue lines correspond to the terms involving $Λ_{AMPA}$, $Λ_{NMDA}$, and $Λ_{GABA}$, respectively. In each plot, the values corresponding to red, blue, and green lines add up to the values of black lines. Note that red lines run very close to black lines, and blue and green lines are nearly horizontal. This indicates that the term $Λ_{AMPA}$ alone approximates the dependence of $\lambda$ on the synaptic parameters rather accurately and that the contributions from the remaining terms $Λ_{NMDA}$ and $Λ_{GABA}$ are rather small.

It should be noted that even though $Λ_{NMDA}$ and $Λ_{GABA}$ are negligibly small, this does not mean that changes in the NMDAR and GABAR conductances do not affect oscillatory instability (black lines, panels C and D, Figure 9). The fact that $Λ_{NMDA}$ and $Λ_{GABA}$ are small only means that $\Deltag_{NMDA}$ and $\Deltag_{GABA}$ do not affect the oscillatory instability directly. However, the changes in the NMDAR and GABAR conductances still affect the instability growth rate $\lambda$ indirectly via the term involving the product of $Λ_{AMPA}$ and $\Deltaϕ_{I_{syn,E}}^{`}/ϕ_{I_{syn,E}}^{`}$ in Equation 1, as mentioned above (and summarized below).

Since $Λ_{NMDA},Λ_{GABA}≪Λ_{AMPA}$, we can neglect the terms involving $Λ_{NMDA}$ and $Λ_{GABA}$ in Equation 1 for the oscillatory instability growth rate $\lambda$. With this approximation, the equation for $\lambda$ simplifies to

$$
\frac{\lambda}{Λ_{AMPA}}=\frac{Δg_{AMPA}}{g_{AMPA}^{*}}+\frac{Δϕ_{I_{syn,E}}^{`}}{ϕ_{I_{syn,E}}^{`}}=\frac{Δg_{AMPA}}{g_{AMPA}^{*}}+U_{E}\frac{\DeltaI_{syn}}{I_{0}}.
$$

Inserting the expression for $\DeltaI_{syn}$ from Equation 4, we obtain

$$
\frac{\lambda}{Λ_{AMPA}}=\frac{Δg_{AMPA}}{g_{AMPA}^{*}}+U_{E}\frac{I_{X}}{I_{GABA}}\frac{\Deltav_{X}}{v_{X}^{*}}+\frac{I_{AMPA}}{I_{GABA}}\frac{\Deltag_{AMPA}}{g_{AMPA}^{*}}+\frac{I_{NMDA}}{I_{GABA}}\frac{\Deltag_{NMDA}}{g_{NMDA}^{*}}-\frac{\Deltag_{GABA}}{g_{GABA}^{*}},
$$

Thus, the instability growth rate $\lambda$, in essence, directly depends only on the AMPAR conductance via the first term in Equation 6. The term in the brackets describes the dependence on the NMDAR mediated excitation, GABAR mediated inhibition, and external rate $v_{X}$ that affect $\lambda$ only indirectly through their effect on the operating point of the response function. In addition, $\lambda$ also depends indirectly on the AMPAR conductance. For the critical state network $U_{E}=2.5$ and $I_{AMPA}/I_{GABA}=0.4$. Therefore, half of the contribution to $\lambda$ is due to the indirect and the second half due to the direct dependence on the AMPAR conductance. A more detailed consideration of the direct and indirect pathways by which modulations of synaptic conductances and external rate affect synchrony is given in Appendix 3.

Since in our network model we vary only the NMDAR conductance and external rate, Equation 6 for $\lambda$ simplifies to

$$
\frac{\lambda}{Λ_{AMPA}}=U_{E}\frac{I_{X}}{I_{GABA}}\frac{\Deltav_{X}}{v_{X}^{*}}+\frac{I_{NMDA}}{I_{GABA}}\frac{\Deltag_{NMDA}}{g_{NMDA}^{*}}.
$$

The expression in the brackets is proportional to the change in the average total synaptic current $I_{syn}$ (Equation 4). The transition to synchrony in the model simulations is achieved by increasing external input (drug-naive condition in Zick et al., 2018), whereas reducing the NMDAR conductance prevents the network from such transition (drug condition in Zick et al., 2018). These simulation results and the mechanism implemented in our model for the transition between the steady and oscillatory states, and the lack thereof when the NMDAR conductance is blocked can be explained in terms of Equation 7 for the instability growth rate $\lambda$. As explained above, changes in external rate $\Deltav_{X}$ and NMDAR conductance $\Deltag_{NMDA}$ both affect synchrony via indirect mechanism by changing the excitatory drive $I_{syn}$ and, therefore, shifting the operating point of the neuron’s response function. In the drug-naive condition, increase in external rate ($Δv_{X}>0$) increases the excitatory drive. As a result, $\lambda$ becomes positive (see Equation 7) and the network switches to the synchronous regime. However, in the drug condition, when NMDAR is blocked ($Δg_{NMDA}<0$), the initial excitatory drive is reduced compared to the drug-naive condition, and now the same increase in external rate $\Deltav_{X}$ becomes insufficient to offset the reduced excitatory drive caused by the NMDAR blockage. As a result, $\lambda$ stays negative and the network remains in asynchronous regime.

A more formal consideration of the mechanism implemented in our model for the transition between the steady and oscillatory states as well as an analytical approximation for the critical line separating these two states are given in Appendix 4. In Appendix 5, we provide theoretical explanations in terms of the equation for the oscillatory instability growth rate $\lambda$ for some other simulation results obtained earlier.

## Discussion

To better understand how synaptic mechanisms influence neural synchrony in recurrent local circuits in monkey prefrontal cortex, we developed a theoretical framework employing a sparsely connected recurrent network model accounting for AMPAR, NMDAR, and GABAR mediated synaptic currents. This allowed us to examine how varying combinations of synaptic transmission in the recurrent network influenced spike timing at the level of pairs of neurons and oscillatory dynamics at the level of neural populations. Our motivation to pursue this question derives from recent neurophysiological experiments investigating the impact of pharmacological NMDAR blockade on spike timing dynamics in monkey prefrontal cortex (Kummerfeld et al., 2020; Zick et al., 2022; Zick et al., 2018). These studies were initiated to investigate how risk factors associated with schizophrenia alter neural dynamics in prefrontal cortex. Those studies found that pharmacological and genetic factors associated with schizophrenia convergently reduce 0-lag synchronous spiking between pairs of prefrontal neurons in monkeys and mice (Zick et al., 2022). The spiking network model we develop in the present study provides a circuit mechanism capable of explaining the biological data. The principal features of this circuit mechanism are as follows: (i) synaptic conductance parameters of the underlying circuit are such that it is in an asynchronous state near a critical boundary in the (NMDAR conductance – external input) parameter plane separating asynchronous and synchronous network states, (ii) small increases in extrinsic inputs push the circuit past this critical boundary into the region of a synchronous state, causing emergence of gamma oscillations in population activity, (iii) 0-lag synchronous spiking between neurons emerges as they stochastically entrain to the gamma population rhythm, (iv) blocking NMDAR currents prevents the circuit from switching to a synchronous regime in response to external inputs, (v) thereby precluding emergence of 0-lag synchronous spiking in neurons.

This circuit mechanism offers a reasonable explanation accounting for the task-locked increase in 0-lag spike synchrony that occurs in monkey prefrontal cortex just before the motor response in the cognitive control task (Zick et al., 2018): the increase in synchrony could reflect increased synaptic input to prefrontal networks at around this time, potentially from mediodorsal nucleus of thalamus (DeNicola et al., 2020). It also explains why pharmacological blockade of NMDAR attenuates 0-lag spike synchrony before the motor response: the deficit in NMDAR mediated synaptic currents prevents prefrontal networks from switching to a synchronous regime in response to external inputs.

In the circuit model, the balance between the AMPA component of recurrent excitation and GABA inhibition controls the network frequency at the onset of oscillation, consistent with results in Brunel and Wang, 2003. This frequency is virtually independent of the balance between the tonic component of recurrent excitation mediated by the NMDAR and GABA inhibition. However, the balance between the NMDA and GABA currents determines the strength of modulation of the external synaptic input needed for switching between the asynchronous stationary and synchronous oscillatory states in the absence and presence of NMDAR antagonist.

### Firing rate and synaptic mechanisms jointly influence synchronous spiking

To gain further insights into how specifically synaptic conductances and external rate affect emergence of synchronous oscillations, we obtained an analytic approximation for the oscillatory instability growth rate $\lambda$ describing the dependence on these parameters near the boundary between the asynchronous and synchronous states where $\lambda=0$. We showed that $\lambda$, in essence, directly depends only on the AMPAR synaptic conductance; it is virtually independent of the NMDAR conductance due to the slow synaptic decay time constant, while the dependence on the GABAR conductance is much weaker compared to AMPAR because of nearly 90° effective phase lag introduced by synaptic filtering. However, $\lambda$ depends on the NMDAR, GABAR as well as AMPAR conductances and external rate indirectly via their effect on the operating point of the neuron’s input current-output frequency response function. The direct dependence manifests the essential influence of the AMPAR synaptic conductance on the strength of an excitatory-inhibitory feedback loop via fast excitatory to excitatory and excitatory to inhibitory recurrent connections. The indirect dependence manifests the influence of the synaptic conductances and external rate on the location of the operating point on the current-frequency response curve and, therefore, the slope of the response function. The steepness of the slope, in turn, determines the amplitude of the neuron’s response to dynamically varying input current and, therefore, affects the strength of excitatory feedback.

The analytic expression for the oscillation growth rate $\lambda$ also reveals the differences and similarities in how AMPAR and NMDAR, both of which mediate recurrent excitation, influence the stability of asynchronous state and transition to synchronous oscillations. Both AMPAR and NMDAR conductances affect $\lambda$ indirectly by influencing the amplitude of the neuron’s response to varying input current. However, because AMPA currents are much faster than NMDA currents, unlike NMDAR, AMPAR conductance also affects $\lambda$ directly by influencing the strength of fast excitatory feedback.

### Relation to prior studies of NMDAR function and oscillatory dynamics

Previous work (Wang, 1999) suggested that NMDAR mediated recurrent currents have a stabilizing effect on the network activity. Compte and colleagues (Compte et al., 2000) carried out spiking network simulations with different relative contributions of the NMDAR and AMPAR mediated currents to the recurrent excitation and showed that with less NMDA but more AMPA currents, the asynchronous steady state becomes unstable and neurons begin to synchronize, leading to network oscillations in the gamma band. At first glance, these simulation results seem to contradict the experimental findings in Zick et al., 2018. Indeed, in the neural recording experiments blocking NMDAR caused desynchronization of neurons, whereas in the simulations (Compte et al., 2000) the reduction of NMDAR currents provoked strong synchronization. Our model and theoretical analysis allows to explain this apparent paradox. In general, the asynchronous state becomes unstable and oscillation emerges when an excitatory feedback from the fast AMPA currents becomes sufficiently strong and is followed by a strong inhibitory feedback from the slower GABA currents (Brunel and Wang, 2003; Compte et al., 2000; Tsodyks et al., 1997; Wang, 1999). As explained above, the excitatory feedback can be enhanced via different mechanisms involving direct and indirect influence of synaptic parameters on the instability growth rate. In Compte et al., 2000, the concurrent increasing AMPAR and decreasing NMDAR conductances nullifies the indirect effect because contributions from the changes in the NMDAR and AMPAR mediated currents to the average total synaptic current, in essence, cancel each other. As a result, the operating point of the response function, defined by the average total current, does not change. However, due to the direct effect of the AMPAR on the instability growth rate $\lambda$, increasing AMPAR conductance enhances the excitatory-inhibitory feedback loop leading to the destabilization of the asynchronous activity and emergence of synchronous oscillations. In our model, by contrast, there is no direct effect on the instability growth rate because the AMPAR conductance is kept fixed, and the enhancement of recurrent excitatory feedback is entirely due to the indirect mechanism. It is achieved through external rate increase at a certain strength of the NMDAR conductance resulting in the neuron’s operating point shift toward a steeper slope above the point of the critical network. This induces network oscillation and synchronization of neurons as observed in monkey PFC when NMDAR is not blocked (Zick et al., 2018). However, when the NMDAR conductance is set to zero, the average total synaptic current is reduced, and the operating point moves down to such locus that it cannot be shifted above the point of the critical network by the same increase in external rate. As a result, external rate increase no longer provides a strong enough excitatory feedback, the network remains in asynchronous state, and no increase in synchrony occurs, consistent with observations in Zick et al., 2018 when NMDAR is blocked.

### Relation to prior studies of NMDAR function and working memory

In monkeys performing a memory-guided saccade task, prefrontal neurons exhibit persistent activity that is associated with the maintenance of information in working memory (Chafee and Goldman-Rakic, 1998; Funahashi et al., 1989; Goldman-Rakic, 1995). Prior theoretical studies have investigated circuit and synaptic mechanisms that can generate persistent activity in recurrent prefrontal networks, specifically addressing how reducing NMDAR function destabilizes attractor states (patterns of stable neural activity) in these networks during a delay period (when the memory of the stimulus must be retained) leading to working memory deficits (Calvin and Redish, 2021; Compte et al., 2000; Funahashi et al., 1989; Goldman‐Rakic, 1987; Loh et al., 2007; Murray et al., 2014). In one seminal study by Compte et al., 2000, the authors investigated the robustness of working memory storage against external synaptic noise and distraction stimuli in attractor networks. They showed that a concomitant increase of NMDAR- and GABAR-mediated currents leads to an increase of persistent activity and to a decrease of spontaneous activity, thereby enhancing the resistance of the network to distractors (Brunel and Wang, 2001; Compte et al., 2000). In another prominent work, Murray et al., 2014, employing an attractor network model, investigated the neural and behavioral effects of synaptic disinhibition induced by the malfunction of NMDAR mediated synapses targeting inhibitory neurons. They demonstrated that disinhibition resulted in a broadening of stimulus selective persistent activity at the neural level, with a concomitant loss of precision, increase in variability over time, and increase in distractibility of stored information at the behavioral level. Although these modeling studies provide important mechanistic insight into prefrontal network dynamics underlying working memory, and potentially, working memory deficits in schizophrenia (Goldman-Rakic, 1999), they do not address the topic of the current study, which is how slow NMDAR recurrent excitation and external input received by the network jointly influence spike timing dynamics at the neuron level and oscillatory dynamics at the population level in the presence of fast AMPA excitation and GABA inhibition. Thus, no prior modeling study captures the relationship between NMDAR synaptic mechanisms, spike timing, and network oscillations that we have observed in neural recordings (Kummerfeld et al., 2020; Zick et al., 2018), and for which we provide a theoretical explanation in the current report.

### Spike timing disruptions and rewiring of prefrontal local circuits via STDP

We previously hypothesized that reduced synchrony at the level of spiking neurons (Zick et al., 2022; Zick et al., 2018) could disconnect prefrontal local circuits via spike-timing dependent synaptic plasticity (STDP; Dan and Poo, 2004; Feldman, 2012), contributing to the reduction in dendritic spine density that has been observed in postmortem analysis of prefrontal cortex in schizophrenia (Glantz and Lewis, 2000; MacDonald et al., 2017). However, the interaction between neural synchrony and synaptic connectivity in networks incorporating STDP is hard to predict, as changes in connectivity patterns and neural dynamics are mutually dependent and interact in complex ways as connectivity and synchrony influence each other over time. Perhaps for this reason, prior theoretical studies incorporating STDP into spiking networks have obtained divergent results with respect to how STDP changes the pattern of synaptic connections between neurons in networks, and whether synchronous inputs to the neurons are required for STDP to influence the pattern of synaptic connections. For example, STDP operating on random spiking in neurons can either lead to the formation of structured stable connections between neurons in the absence of synchronous inputs (forming neural ‘groups’) (Izhikevich et al., 2004), or not (Morrison et al., 2007), depending on the assumptions incorporated into the models. Similarly, correlated external input to recurrent networks incorporating STDP can either fail to produce structured synaptic connections between neurons (Morrison et al., 2007), or it can lead to the formation of such structured connections (Litwin-Kumar and Doiron, 2014) depending on the specifics of the simulations. Key parameters that could influence the diversity of outcomes among studies include whether (Izhikevich et al., 2004) or not (Morrison et al., 2007) axonal conduction delays and the geometry of recurrent connections are incorporated into the models (since circuit architecture and associated signal conduction delays powerfully influences when action potentials arrive at pre- and postsynaptic elements), as well as the specific form of the STDP rule employed (Babadi and Abbott, 2013; Bono and Clopath, 2017; Izhikevich et al., 2004; Morrison et al., 2007). Based on these results, it seems reasonable that distortions of spike timing dynamics in prefrontal networks may alter the pattern of neural connections via STDP in schizophrenia. However, the diversity of results obtained from theoretical studies of STDP outlined above make it difficult to conclude that the reduction in synchronous spiking we observed would lead to synaptic disconnection via STDP, imposing important constraints on our prior hypothesis (Zick et al., 2022; Zick et al., 2018), although this remains a possibility. Network simulations that accurately incorporate as many of these biological variables as possible may be useful in predicting how spike timing changes that may emerge downstream of schizophrenia risk factors would be likely to influence synaptic connectivity in the human cortex. In addition, as noted, genetic linkage studies have implicated altered NMDAR function in schizophrenia (Fromer et al., 2014; Schizophrenia Working Group of the Psychiatric Genomics Consortium, 2014). Since NMDAR play a central role in the molecular mechanisms that implement STDP in the brain, disruption of NMDAR synaptic transmission in schizophrenia may alter STDP directly, independently of the impact of disrupted NMDAR function on neural spiking dynamics in the disease state.

### Potential U-shaped relation between NMDAR function and spike synchrony

We had previously reported that blocking NMDAR in monkeys (Zick et al., 2018) and deleting a schizophrenia risk gene (Dgcr8) in mice (Zick et al., 2022), both reduced the frequency of synchronous, 0-lag spiking between prefrontal neurons. Dgcr8 encodes a protein involved in the synthesis of miRNA, which in turn bind to mRNA and suppress their translation into proteins, including mRNA coding for NMDAR subunits (Corbel et al., 2015). Deleting Dgcr8 would therefore be expected to reduce miRNA synthesis and increase translation of mRNA coding for NMDAR subunits. Given these considerations, the convergent spike desynchronization we observed in monkey drug and mouse genetic models could be explained by an inverted U-shaped relationship wherein either too little NMDAR function (as produced by NMDAR blockade in monkeys) or too much NMDAR function (as predicted to result from deletion of Dgcr8 in mice) decreases the frequency of 0-lag spiking between prefrontal neurons (Zick et al., 2022; Zick et al., 2018). An inverted U-shaped relationship has been reported between the level of D1 dopamine receptor stimulation and the strength of persistent neural activity in prefrontal neurons during working memory tasks wherein small doses of an agonist amplify persistent activity, and larger doses degrade it (Vijayraghavan et al., 2007). However, additional experimental data are needed to establish that spike synchrony exhibits a similar inverted U-shaped relation to NMDAR function, insofar as our prior neural recording studies did not test a U-shaped relationship directly (Zick et al., 2022; Zick et al., 2018). These studies did not for example contrast the effect of low versus high doses of an NMDAR agonist (such as NMDA) on spike synchrony in the monkey model, nor relate reduction in spike synchrony specifically to the upregulation of NMDAR subunit expression in the mouse model (rather than the many other proteins regulated by miRNA that are dependent on Dgcr8).

Results we present in the current study establish a theoretical basis and circuit mechanism explaining how reduction of NMDAR synaptic function implicated in schizophrenia could lead to the desynchronization of neural activity in prefrontal recurrent circuits. We provide evidence that spiking networks situated close to a boundary in the synaptic parameter space separating asynchronous and synchronous activity states can explain a variety of biological observations. These include the emergence of 0-lag synchronous spiking between individual prefrontal neurons when external inputs to the network push it across this state boundary, and failure of synchronous spiking to emerge between prefrontal neurons when NMDAR synaptic currents are reduced, as we have observed in neural recordings in primate prefrontal cortex (Kummerfeld et al., 2020; Zick et al., 2022; Zick et al., 2018).

## Materials and methods

### Experimental data

For the present theoretical study, we used experimental data obtained in our previous work (Zick et al., 2018). Here, we provide brief descriptions of the experimental task, NMDAR antagonist regimen, and neurophysiological recording methodology employed in that work; details have been reported in Blackman et al., 2016; Zick et al., 2018.

#### Experimental task

Male rhesus macaque monkeys (8–10 kg) were trained to perform the dot-pattern expectancy (DPX) task. This task is closely related to the AX-CPT (continuous performance task) except that dot patterns replace letters as stimuli. During each trial of the DPX tasks, monkeys maintained gaze fixated on a central target as a cue stimulus (1,000ms), followed by a delay period (1,000ms), and a probe stimulus (500ms) were presented. Monkeys were rewarded for moving a joystick to the left if the cue-probe sequence had been AX (69% of trials), or to the right if any other cue-probe sequence had been presented (AY, BX, BY, collectively 31% of trials). Since the correct response to the X-probe depended on the preceding cue (A or B), the task required both working memory and cognitive control. Both The DPX and AX-CPT measure specific cognitive control impairments in schizophrenia (Barch et al., 2003; Jones et al., 2010).

#### Neurophysiological recording

In our previous study (Zick et al., 2018), we recorded neural activity from the region of the principal sulcus (centered on Brodmann’s areas 46) in the dorsolateral prefrontal cortex of two macaques performing the DPX task. We found that 0-lag synchrony while present in both monkeys was much stronger in one than the other animal. For comparison to spiking dynamics in the present neural network simulation, we used neurophysiological recording data from the monkey that exhibited the strongest 0-lag spike correlation during task performance (Zick et al., 2018). For neurophysiological recording, we used a computer-controlled electrode drive (System Eckhorn, Thomas Recording, GmbH) advancing 16, closely spaced, independently movable glass coated platinum/tungsten microelectrodes into the prefrontal cortex. Electrodes were spaced 400 µm apart, and interelectrode distances in the array spanned 400–1,400 µm. Moving the electrodes in depth and the position of the array within recording chambers over days made it possible to isolate the spiking activity of different neural ensembles, each containing 15–30 individually isolated, simultaneously recorded neurons. The database included in the present study consisted of 47 neural ensembles containing a total of 893 prefrontal neurons. Spike correlation was evaluated within ensembles of simultaneously recorded ensembles using spike trains recorded during DPX task performance (Zick et al., 2018).

#### NMDAR antagonist regimen

We examined the effect of systemic administration of an NMDAR antagonist (phencyclidine, 0.25–0.30 mg/kg IM) on spike timing dynamics in prefrontal local circuits. Neural activity was recorded in a Naive condition (before first exposure to drug), and a Drug condition (following systemic drug administration) (Zick et al., 2018).

### Spike correlation and synchrony

To estimate correlation between spiking activity of simultaneously recorded neuron pairs as a function of time, we used a similar approach described in Zick et al., 2018. Correlation is evaluated from spiking activity observed during a time window $\DeltaT$ around a given instant of time $t$. The window size $\DeltaT$, thus, defines the temporal resolution of time resolved correlation. The interval $\DeltaT$ is subdivided into small time bins of width $\Deltat$. Activity of neuron $i$ in a given trial at a time bin $t^{′}$ is represented by a binary variable $ξ_{i}(t^{′})$ that can take on two values: 1 if in the time bin $t^{′}$ one or more spikes are present, and 0 if there are no spikes. Correspondingly, time-lagged joint spike activity of neurons $i$ and $j$ is described by the product $ξ_{i}(t^{′})\timesξ_{j}(t^{′}+\tau)$: it is 1 if neuron $i$ fired a spike in the time bin $t^{′}$ and neuron $j$ fired a spike in the time bin $t^{′}+\tau$; otherwise, it is 0. The duration of the bin $\Deltat$, thus, defines the spike coincidence window. We assume that spike firing statistics of neurons do not change during the interval $\DeltaT$, so that low order moments of the binary variables, such as the mean spike frequencies $ν_{i}=ξ_{i}(t^{′})¯$ and $ν_{j}=ξ_{j}(t^{′})¯$ and the mean joint spike frequency $ρ_{ij}(\tau)=ξ_{i}(t^{′})\timesξ_{j}(t^{′}+\tau)¯$, can be reliably estimated by averaging over $\DeltaT/\Deltat$ time bins (bars $.¯$ above the expressions denote time averaging operation). To avoid a contribution to correlation from possible cross-trial non-stationarity (slow covariation) of neural activity, for each neuron pair correlation is estimated from single trials and then averaged over all trials. Spiking correlation between neurons $i$ and $j$ in a single trial is characterized by the observed frequency of joint spikes $ρ_{ij}(\tau)$ normalized by the expected joint spike frequency $ν_{i}\timesν_{j}$ if activity of the neurons were independent: $ρ_{ij}(\tau)/(ν_{i}\timesν_{j})$. We then average this ratio over the trials to obtain time-lagged correlation of spiking activity as $c_{ij}(\tau)=⟨ρ_{ij}(\tau)/(ν_{i}\timesν_{j})⟩$, where angular brackets $∙$ denote trial averaging operation. Finally, $c_{ij}(\tau)$ is averaged over the population of simultaneously recorded pairs resulting in the population average spike correlation $C(\tau)$. Spike synchrony is defined as 0-lag correlation.

To accurately estimate spike synchrony and time-lagged correlation in PFC circuits, it is necessary to keep the value of time bin $\Deltat$, controlling the spike coincidence window, sufficiently small, within 1–2ms (no more than one spike occurred in a bin). On the other hand, the firing rates of PFC neurons are relatively low, on the order of 10 Hz. Therefore, to increase the number of counts of joint spike events and improve the estimate of spike synchrony while keeping $\Deltat$ small (and, thus, spike synchrony resolution sufficiently high), one needs to increase the duration of time window $\DeltaT$ and/or the number of trials $K$ However, $\DeltaT$ should be kept sufficiently short so that during this interval spiking activity remains nearly stationary, whereas $K$ cannot be made arbitrarily large because it is limited by practical considerations.

These experimental restrictions, as a result, impose constraints on the firing rates of the neurons in the pair. To derive a meaningful criterion for selecting ‘good’ neuron pairs, we note that for a reliable estimation of the mean joint spike firing frequency, which is a second order statistic, one needs quadratically more experimental samples than for a reliable estimation of the mean spike frequency, which is a first order statistic. We also note that the expected joint spike frequency if neurons in the pair were independent is simply given as the product of their mean spike frequencies. It is this quantity that is used as a reference (normalization) for the quantification of spike correlation strength. Therefore, to reliably estimate the joint spike firing frequency from available samples of a given pair, one should be confident that at least when assuming that neurons fire independently, a sufficiently accurate estimation of the expected joint spike frequency from these samples is possible. This, in turn, means that, given the neuron firing rates $v_{i}$ and $v_{j}$, the average total number of counts of joint spikes $(v_{i}Δt)(v_{j}Δt)(ΔT/Δt)K$ observed in $\DeltaT/\Deltat$ bins in $K$ trials predicted under the assumption of independence and calculated from experimental samples should be ‘detectable’, that is, it should be at least greater than 1. This condition results in a constraint for the geometric mean, $v¯_{ij}=\sqrt{v_{i}v_{j}}$, of the firing rates of neuron pairs: $v¯_{ij}>1/\sqrt{KΔTΔt}$. The typical values for the time window and spike coincidence window are $\DeltaT~100$ ms and $\Deltat~1$ ms. Given that the number of correct trials in the DPX task were on the order of $K~200$, this means that the geometric mean firing rate of neuron pairs, for which a reliable estimation of synchrony can be achieved, should be at least 7 Hz.

### Network model

The network consists of $N$ leaky integrate and fire neurons (see, e.g., Dayan and Abbott, 2001), of which $N_{E}=0.8N$ are excitatory and $N_{I}=0.2N$ are inhibitory (Abeles, 1991; Braitenberg and Schüz, 1998). Neurons are connected randomly with a probability $p$, so that, on average, each neuron receives $C_{E}=pN_{E}$ connections from excitatory and $C_{I}=pN_{I}$ from inhibitory neurons. In the framework of mean field consideration, the network is large ($N≫1$) and connections are sparse ($p≪1$) but the average number of connections received by individual neurons, $C$, is large ($C=pN≫1$). In most simulations, networks consisted of $N=5∙10^{3}$ neurons that were randomly connected with the probability $p=0.2$ and, therefore each neuron, on average, received $C=10^{3}$ connections. In addition, each neuron also receives $C_{X}$ external connections from excitatory neurons outside of the network that fire spikes independently according to a Poisson process with rate $ν_{X}$.

The dynamics of the membrane potential $V(t)$ of a neuron below the spike firing potential threshold $\theta$ obeys the standard leaky integrate and fire equation:

$$
C_{m}\frac{dV(t)}{dt}=−g_{m}(V(t)−V_{L})−i_{syn}(t),
$$

where $C_{m}$ is the cell membrane capacitance, $g_{m}$ is the membrane leak conductance, $V_{L}$ is the resting potential, and $i_{syn}(t)$ is the total synaptic current. When the membrane potential reaches the threshold $\theta$, the neuron fires a spike, the potential is reset to $V_{rst}$, and the neuron becomes insensitive to its input for the duration of a refractory period $\tau_{rp}$. Both excitatory and inhibitory neurons have $\theta=-50$ mV, $V_{L}=-70$ mV, and $V_{rst}=-55$ mV. For excitatory neurons $C_{m}=0.5$ nF, $g_{m}=25$ nS, $\tau_{rp}=2$ ms, and for inhibitory neurons $C_{m}=0.2$ nF, $g_{m}=20$ nS, $\tau_{rp}=1$ ms (see, e.g., Koch, 2004).

The total synaptic input for each neuron is a linear sum of four components:

$$
i_{syn}(t)=i_{AMPA}(t)+i_{NMDA}(t)+i_{GABA}(t)+i_{X}(t),
$$

where $i_{AMPA}$ and $i_{NMDA}$ correspond to recurrent excitatory currents mediated by AMPA and NMDA receptors, respectively, $i_{GABA}$ corresponds to inhibitory currents mediated by GABA receptors, and $i_{X}$ corresponds to external currents mediated by AMPA receptors. The purpose of external currents is twofold: (i) to represent the noisy inputs due to the background synaptic activity and (ii) to convey neural signals from outside of the network.

The description of component synaptic currents of a postsynaptic neuron follows Wang, 1999:

$$
i_{AMPA}(t)=g_{AMPA}(V(t)−V_{E})\sumjs_{AMPA,j}(t)
$$



$$
i_{NMDA}(t)=\frac{g_{NMDA}(V(t)−V_{E})}{1+[Mg^{2+}]/\gammaexp⁡(−\betaV(t))}\sumjs_{NMDA,j}(t)
$$



$$
i_{GABA}(t)=g_{GABA}(V(t)−V_{I})\sumjs_{GABA,j}(t)
$$



$$
i_{X}(t)=g_{X}(V(t)−V_{E})\sumjs_{X,j}(t),
$$

where synaptic reversal potentials $V_{E}=0$ mV and $V_{I}=-70$ mV. NMDAR mediated currents have voltage dependence controlled by the extracellular magnesium concentration (Jahr and Stevens, 1990): $\beta=0.062mV^{−1}$ , $\gamma=3.57$ mM, $[Mg^{2+}]=1$ mM. The gating variable $s_{R,j}(t)$, describes the temporal course of postsynaptic currents received from the presynaptic neuron $j$ mediated by the receptor $R$, where $R=$ X, AMPA, NMDA, GABA. For a spike train generated by a presynaptic neuron with emission times ${t_{k}}$, the temporal dynamics of the gating variable obeys the equations

$$
{\tau_{r}\frac{dx(t)}{dt}=−x(t)+\tau_{∗}\sumk\delta(t−t_{k}−\tau_{l})\tau_{d}\frac{ds(t)}{dt}=−s(t)+x(t),
$$

where $\tau_{l}$, $\tau_{r}$ and $\tau_{d}$ are, respectively, latency, rising, and decay time constants. Their values are $\tau_{AMPA,l}=1$ mS, $\tau_{AMAP,r}=0.2$ ms, $\tau_{AMPA,d}=2$ ms for AMPAR mediated currents (Zhou and Hablitz, 1998), $\tau_{NMDA,l}=1$ mS, $\tau_{NMDA,r}=2$ ms, $\tau_{NMDA,d}=100$ ms for NMDAR mediated currents (Hestrin et al., 1990), and $\tau_{GABA,l}=1$ mS, $\tau_{GABA,r}=0.5$ ms, $\tau_{GABA,d}=5$ ms for GABAR-mediated currents (Gupta et al., 2000). The time integral of $s(t)$ in response to a presynaptic spike equals $\tau_{*}$ and, thus, is independent of the temporal shape of $s(t)$, which is determined by the rising and decay time constants that are specific to each receptor type. Because the charge flowing to the cell is determined by the product of the time integral of $s(t)$ and the maximal conductance, we set $\tau_{*}$ to be the same for all types of receptors, so that the charge entry mediated by each type of receptor is parametrized, in essence, solely by the corresponding maximal conductance parameter.

### Network simulations

In all direct network simulations, the numerical integration of the coupled differential equations describing the dynamics of membrane potentials and synaptic variables of all cells and synapses were carried out using a custom MATALAB (The MathWorks) code implementing a second order Runge-Kutta method with interpolation of spike firing times between integration time steps $\Deltat$ (Hansel et al., 1998). In most simulations $\Deltat=0.1$ ms.

### Mean field approximation

To derive maximal synaptic conductance parameters $g_{X,\alpha}$, $g_{AMPA,\alpha}$, $g_{NMDA,\alpha}$, $g_{GABA,\alpha}$ ($\alpha=E,I$) providing prescribed neural firing rates $ν_{E}$ and $ν_{I}$, we used mean field analysis (Amit and Brunel, 1997; Brunel, 2000; van Vreeswijk and Sompolinsky, 1996) extended to networks of neurons with realistic, conductance based synapses (Brunel and Wang, 2001; Renart et al., 2003). For simplicity, we disregard the heterogeneity of synaptic connectivity and assume that each neuron receives $C_{E}$ excitatory and $C_{I}$ inhibitory connections. In the mean field approximation synaptic inputs are described in terms of their average and their fluctuations arising from both external and recurrent inputs. To this end, the sums of gating variables in Equations 10–13 are replaced by their respective population averages $\tau_{*}S_{R}^{0}$, where $R$ designates the type of the synapse, and

$$
S_{X}^{0}=C_{X}ν_{X},S_{AMPA}^{0}=C_{E}ν_{E},S_{NMDA}^{0}=C_{E}ν_{E},S_{GABA}^{0}=C_{I}ν_{I}.
$$

The voltage dependence of NMDAR conductance is linearized around the mean value of the potential $V$:

$$
\frac{(V(t)−V_{E})}{1+[Mg^{2+}]/\gammaexp(−\betaV(t))}≈\frac{V(t)−V_{E}}{κ}+\beta\frac{(V(t)−⟨V⟩)(⟨V⟩−V_{E})(κ−1)}{κ^{2}},
$$

where $κ=1+Mg^{2+}/\gammaexp⁡(-\betaV)$. After these simplifications, average components of synaptic currents for excitatory ($\alpha=E$) and inhibitory ($\alpha=I$) populations can be written as

$$
I_{X,\alpha}^{0}=g_{X,\alpha}V_{\alpha}-V_{E}\tau_{*}S_{X}^{0}=J_{X,\alpha}S_{X}^{0}
$$



$$
I_{AMPA,\alpha}^{0}=g_{AMPA,\alpha}V_{\alpha}-V_{E}\tau_{*}S_{AMPA}^{0}=J_{AMPA,\alpha}S_{AMPA}^{0}
$$



$$
I_{NMDA,\alpha}^{0}=g_{NMDA,\alpha}/κV_{\alpha}-V_{E}\tau_{*}S_{NMDA}^{0}=J_{NMDA,\alpha}S_{NMDA}^{0}
$$



$$
I_{GABA,\alpha}^{0}=g_{GABA,\alpha}V_{\alpha}-V_{I}\tau_{*}S_{GABA}^{0}=J_{GABA,\alpha}S_{GABA}^{0},
$$

where $V_{\alpha}$ is the average membrane potential, and $J_{R,\alpha}$ is the effective strength of the $R$-receptor mediated synapse, expressed as the total charge entering the postsynaptic neuron due to a single presynaptic spike. In this framework, the system of equations describing the dynamics of membrane potentials for each of $N_{E}$ excitatory and $N_{I}$ inhibitory neurons is reduced to equations describing the dynamics of membrane potentials $V_{E}(t)$ and $V_{I}(t)$ of just two neurons representing, respectively, excitatory, $E$, and inhibitory, $I$, populations (Brunel and Wang, 2001; Renart et al., 2003):

$$
\tau_{\alpha}\frac{dV_{\alpha}(t)}{dt}=−(V_{\alpha}(t)−V_{L})+\mu_{\alpha}+\sigma_{\alpha}\sqrt{\tau_{\alpha}}η_{\alpha}(t),\alpha=E,I,
$$

where $V_{L}$ is the resting potential, $\tau_{\alpha}$ is the effective membrane time constant, $\mu_{\alpha}$ is the effective mean synaptic input, $\sigma_{\alpha}$ is the magnitude of the fluctuations in the synaptic input, and $η_{\alpha}(t)$ is the time course of these fluctuations:

$$
\tau_{\alpha}=\frac{C_{m,\alpha}}{g_{m,\alpha}S_{\alpha}}
$$



$$
S_{\alpha}=1+T_{X,\alpha}ν_{X}+T_{AMPA,\alpha}ν_{E}+T_{NMDA1,\alpha}+T_{NMDA2,\alpha}ν_{E}+T_{GABA,\alpha}ν_{I}
$$



$$
T_{X,\alpha}=\frac{g_{X,\alpha}C_{X}\tau_{*}}{g_{m,\alpha}}
$$



$$
T_{AMPA,\alpha}=\frac{g_{AMPA,\alpha}C_{E}\tau_{*}}{g_{m,\alpha}}
$$



$$
T_{NMDA1,\alpha}=\frac{g_{NMDA,\alpha}C_{E}\tau_{∗}}{g_{m,\alpha}κ}
$$



$$
T_{NMDA2,\alpha}=\beta\frac{g_{NMDA,\alpha}C_{E}\tau_{∗}(⟨V_{\alpha}⟩−V_{E})(κ−1)}{g_{m,\alpha}κ^{2}}
$$



$$
T_{GABA,\alpha}=\frac{g_{GABA,\alpha}C_{I}\tau_{*}}{g_{m,\alpha}}
$$



$$
\mu_{\alpha}=\frac{(T_{X,\alpha}ν_{X}+T_{AMPA,\alpha}ν_{E}+T_{NMDA1,\alpha}ν_{E})(V_{E}−V_{L})}{S_{\alpha}}+\frac{T_{NMDA2,\alpha}ν_{E}(⟨V_{\alpha}⟩−V_{L})+T_{GABA,\alpha}ν_{I}(V_{I}−V_{L})}{S_{\alpha}}.
$$

In the absence of spiking and fluctuations, the average membrane potential would equal $\mu_{\alpha}+V_{L}$ (Equation 21). The average membrane potential $V_{\alpha}$ of spiking neuron in the presence of synaptic noise can be calculated from the distribution of potentials obtained in Brunel and Hakim, 1999 and is given by (Renart et al., 2003)

$$
V_{\alpha}=\mu_{\alpha}+V_{L}-\theta-V_{rst}v_{\alpha}\tau_{\alpha}-\mu_{\alpha}+V_{L}-V_{rst}v_{\alpha}\tau_{rp,\alpha}.
$$

The total synaptic noise $\sigma_{\alpha}^{2}$ characterizing fluctuations in the input that result from random arrival of spikes is approximated as the sum of the fluctuations in the external and recurrent inputs (Fourcaud and Brunel, 2002):

$$
\sigma_{\alpha}^{2}=\sigma_{X,\alpha}^{2}+\sigma_{AMPA,\alpha}^{2}+\sigma_{NMDA,\alpha}^{2}+\sigma_{GABA,\alpha}^{2},
$$

where

$$
\sigma_{R,\alpha}^{2}=\frac{J_{R,\alpha}^{2}S_{R}^{0}\tau_{\alpha}}{C_{m,\alpha}^{2}},R=X,AMPA,NMDA,GABA.
$$

$η_{\alpha}(t)$ is a Gaussian process with zero mean, $⟨η_{\alpha}(t)⟩=0$, and an exponentially decaying correlation function, $⟨η_{\alpha}(t)η_{\alpha}(t^{′})⟩∝exp(−|t−t^{′}|/\tau_{syn,\alpha})$, which is due to synaptic filtering with effective time constant $\tau_{syn,\alpha}$ (Fourcaud and Brunel, 2002):

$$
\tau_{syn,\alpha}=\frac{\sigma_{\alpha}^{2}}{\frac{\sigma_{X,\alpha}^{2}}{\tau_{AMPA}}+\frac{\sigma_{AMPA,\alpha}^{2}}{\tau_{AMPA}}+\frac{\sigma_{NMDA,\alpha}^{2}}{\tau_{NMDA}}+\frac{\sigma_{GABA,\alpha}^{2}}{\tau_{GABA}}},
$$

where $\tau_{AMPA}=\tau_{AMPA,l}+\tau_{AMPA,r}+\tau_{AMPA,d}$, $\tau_{NMDA}=\tau_{NMDA,l}+\tau_{NMDA,r}+\tau_{NMDA,d}$, $\tau_{GABA}=\tau_{GABA,l}+\tau_{GABA,r}+\tau_{GABA,d}$ are effective synaptic time constants for AMPAR, NMDAR, and GABAR-mediated currents, respectively. In addition, because of sparse connectivity, the correlation of the fluctuations in the synaptic inputs of excitatory and inhibitory populations is neglected: $⟨η_{E}(t)η_{I}(t^{′})⟩=0$. The firing rate $ν_{\alpha}$ of a neuron, whose potential is governed by Equation 21, is given by a current-frequency relationship $ϕ_{\alpha}\mu_{\alpha},\sigma_{\alpha}$ that is a function of the mean and fluctuating part of synaptic input (Brunel and Sergi, 1998; Fourcaud and Brunel, 2002):

$$
ϕ_{\alpha}(\mu_{\alpha},\sigma_{\alpha})=( \tau_{rp,\alpha}+\tau_{\alpha}\int_{a(\mu_{\alpha},\sigma_{\alpha})}^{b(\mu_{\alpha},\sigma_{\alpha})}dx\sqrt{\pi}exp⁡(x^{2})(1+erf(x)))^{−1},
$$

where

$$
a\mu_{\alpha},\sigma_{\alpha}=\frac{V_{rst}-V_{L}-\mu_{\alpha}}{\sigma_{\alpha}}
$$



$$
b(\mu_{\alpha},\sigma_{\alpha})=\frac{\theta−V_{L}−\mu_{\alpha}}{\sigma_{\alpha}}(1+0.5\frac{\tau_{syn,\alpha}}{\tau_{\alpha}})+1.03\sqrt{\frac{\tau_{syn,\alpha}}{\tau_{\alpha}}}−0.5\frac{\tau_{syn,\alpha}}{\tau_{\alpha}}.
$$

Since $\mu_{\alpha}$ and $\sigma_{\alpha}$ themselves depend on the population firing rates $ν_{E}$ and $ν_{I}$, the two coupled frequency-current equations

$$
{ν_{E}=ϕ_{E}(\mu_{E}(ν_{E},ν_{I}),\sigma_{E}(ν_{E},ν_{I}))ν_{I}=ϕ_{I}(\mu_{I}(ν_{E},ν_{I}),\sigma_{I}(ν_{E},ν_{I}))
$$

provide a self-consistent description of the network in stationary states, that is regimes of network dynamics when the population average quantities such as firing rates and synaptic inputs are constant in time. In the framework of our model, synaptic conductances $g_{X,\alpha}$, $g_{AMPA,\alpha}$, $g_{NMDA,\alpha}$, $g_{GABA,\alpha}$ ($\alpha=E,I$) and the external spike rate $ν_{X}$ are system parameters controlling the regime of network dynamics; they enter to the mean field analysis through expressions for $\mu_{\alpha}$, and $\sigma_{\alpha}$,. If these parameters are given, one can solve the self-consistent equations to obtain predicted by the mean field approximation population firing rates $v_{E}^{0}$ and $v_{I}^{0}$ in a stationary state of the network. Conversely, once external $ν_{X}$ and population spike rates $v_{E}^{0}$ and $v_{I}^{0}$ are specified, the self-consistent equations could be solved to find the values of synaptic conductance parameters $g_{X,\alpha}$, $g_{AMPA,\alpha}$, $g_{NMDA,\alpha}$, $g_{GABA,\alpha}$ ($\alpha=E,I$) that correspond to these spike rates. However, because there are eight unknown parameters and only two equations, to find a unique solution one would need six additional equations imposing constraints on conductance parameters.

### Model parametrization

We derive three of these equations by implementing a commonly used constraint (e.g. Brunel and Wang, 2003; Compte et al., 2000) that equalizes the ratio of synaptic conductance parameters for component currents in excitatory and inhibitory neurons. Since each component current is proportional to its respective synaptic conductance, this constraint implies that the balance between different components of average synaptic currents $I_{X,\alpha}^{0}$, $I_{AMPA,\alpha}^{0}$, $I_{NMDA,\alpha}^{0}$, $I_{GABA,\alpha}^{0}$ for excitatory ($\alpha=E$) and inhibitory ($\alpha=I$) populations is the same, thus providing the following three equations:

$$
\frac{I_{NMDA,E}^{0}}{I_{GABA,E}^{0}}=\frac{I_{NMDA,I}^{0}}{I_{GABA,I}^{0}},\frac{I_{AMPA,E}^{0}}{I_{GABA,E}^{0}}=\frac{I_{AMPA,I}^{0}}{I_{GABA,I}^{0}},\frac{I_{X,E}^{0}}{I_{GABA,E}^{0}}=\frac{I_{X,I}^{0}}{I_{GABA,I}^{0}}.
$$

As a result, whenever the ratio of synaptic conductances and/or component currents is involved, the index $\alpha$ designating the type of the neuron can be dropped.

Two additional equations are obtained by fixing the balance between inhibition and two-component recurrent excitation at certain values:

$$
\frac{I_{NMDA}^{0}}{I_{GABA}^{0}}=q_{1},\frac{I_{AMPA}^{0}}{I_{GABA}^{0}}=q_{2}
$$

The last constraint is provided in terms of the relative magnitude of average external current of excitatory neurons, $I_{X,E}^{0}$:

$$
\frac{I_{X,E}^{0}}{I_{\theta,E}^{0}}=q_{3},
$$

where $I_{\theta,E}^{0}$ is the current that is needed for an excitatory neuron to reach firing threshold $\theta$ in absence of recurrent feedback. This approach allowed to parametrize network dynamics in terms of three parameters expressed as ratios of absolute values of average synaptic currents, $I_{AMPA}/I_{GABA}$, $I_{NMDA}/I_{GABA}$, and $I_{X,E}/I_{\theta,E}$, characterizing the balance between components of recurrent excitation and inhibition, and the balance between external input and firing threshold. For a given external spike rate $ν_{X}$ and fixed values of these three parameters, we are now able to solve the self-consistent equations for the eight synaptic conductances that provide the prescribed population firing rates $v_{E}^{0}$ and $v_{I}^{0}$ in a stationary state of the network.

We are interested in the asynchronous stationary state in which neurons fire spikes irregularly and at low rates, like neurons in prefrontal cortex. When mean synaptic inputs $\mu_{\alpha}$ are well below threshold $\theta$, firing is driven by the synaptic fluctuations $\sigma_{\alpha}$ around the mean input, therefore, resulting in irregular spike trains and low rates (Renart et al., 2003). Given that the number of synaptic connections received by individual neurons is large and network connectivity is sparse, solutions of self-consistent equations providing the subthreshold regime for $\mu_{\alpha}$ and, thus, low rate asynchronous network dynamics, arise when inhibition strongly dominates recurrent excitation and the mean external inputs are around or above threshold $\theta$ (Brunel, 2000; Renart et al., 2003; van Vreeswijk and Sompolinsky, 1996). Thus, for the network to be in asynchronous irregular state the three system parameters characterizing the balance between recurrent excitation and inhibition, and the relative strength of external inputs should be within certain bounds: $I_{AMPA}/I_{GABA}+I_{NMDA}/I_{GABA}<1$, and $I_{X,E}/I_{\theta,E}≳1$.

### Linear stability analysis

We perform a linear stability analysis of the asynchronous state (Abbott and van Vreeswijk, 1993; Brunel and Hakim, 1999) on the basis of an analytical consideration in Brunel and Wang, 2003. To understand if the network develops instability caused by fluctuations in population firing rates, we consider small deviations from the stationary population rates $v_{E}^{0}$ and $v_{I}^{0}$. In order to analyze the resulting network behavior, the mean field approach and self-consistent equations providing population mean firing rates $v_{E}^{0}$ and $v_{I}^{0}$ are extended to describe the dynamics of population rates $ν_{E}(t)$ and $ν_{I}(t)$.

In the framework of mean field approximation, each component of synaptic current is determined by the product of effective synaptic strength $J$ and average gating variable $S$ (Equations 17–20 for the steady state consideration). The dynamics of $S$ is governed by the same type of equations as for the gating variable $s$ of an individual synapse in a given postsynaptic neuron (Equation 14), except that the instantaneous rate of spikes $\sumk\deltat-t_{k}-\tau_{l}$ arriving from the presynaptic cell is replaced by the instantaneous average rate of spikes, $C_{\alpha_{R}}ν_{\alpha_{R}}(t-\tau_{l})$, arriving from all presynaptic cells making the same type of synapse in the postsynaptic neuron:

$$
{\tau_{r}\frac{dx(t)}{dt}=−x(t)+C_{\alpha_{R}}ν_{\alpha_{R}}(t−\tau_{l})\tau_{d}\frac{dS_{R}(t)}{dt}=−S_{R}(t)+x(t),
$$

where $R$ designates the type of the synapse ($R=X,AMPA,NMDA,GABA$), and $\alpha_{R}$ designates the presynaptic population establishing these synapses ($\alpha_{R}=X,E$ for glutamatergic and $\alpha_{R}=I$ for GABAergic synapse). Since external firing rate $ν_{X}$ is stationary, the gating variable for external current is constant in time: $S_{X}=C_{X}ν_{X}$ . For recurrent currents, the temporal course of $S_{R}$ is dependent on the instantaneous presynaptic population activity $ν_{\alpha_{R}}(t)$. Consequently, the total synaptic input current $I_{syn}(t)$, given as a sum of contributions from external and recurrent components

$$
I_{syn}(t)=J_{X}S_{X}+J_{AMPA}S_{AMPA}(t)+J_{NMDA}S_{NMDA}(t)+J_{GABA}S_{GABA}(t),
$$

depends on the population firing rates $ν_{E}(t)$ and $ν_{I}(t)$. The output firing rate of population neurons, in turn, is determined by the input current and can be modeled in terms of an input-output response function $F$.

In general, the input-output relationship $v(t)=F(I_{syn}(t))$ depends on the spectral characteristics of the input current, resulting in frequency dependent phase shifts and/or amplitude modulations between the oscillatory components of $I_{syn}$ and $v$. However, it has been shown (Brunel et al., 2001; Fourcaud and Brunel, 2002) that the output rate in the leaky integrate and fire neuron model follows instantaneously the temporal variations in its synaptic input current given that synaptic noise is sufficiently strong and synaptic time constant is comparable with membrane time constant. That is, in these conditions, the response does not exhibit a phase shift, and its amplitude is independent of the frequency of oscillatory components of the input current. As a result, even if the input current is varying in time, the input-output function $F$ can be approximated by the current-frequency response function $ϕ$, given by Equation 34, describing the output due to the steady input current.

In the framework of mean field approximation, the output rates $ϕ_{E}(I_{syn,E}(t))$ and $ϕ_{I}(I_{syn,I}(t))$ for excitatory and inhibitory populations must be the same as the instantaneous presynaptic population rates $ν_{E}(t)$ and $ν_{I}(t)$ because both presynaptic and output rates are of the same populations. This requirement results in two self-consistent equations:

$$
{ν_{E}(t)=ϕ_{E}(I_{syn,E}(ν_{E}(t),ν_{I}(t)))ν_{I}(t)=ϕ_{I}(I_{syn,I}(ν_{E}(t),ν_{I}(t))).
$$

Since the amplitudes of firing rate deviations from the rates in asynchronous steady state are small, $ϕ(I_{syn}(t))$ can be linearized about the input current $I_{syn}^{0}$ in asynchronous state as:

$$
ϕ(I_{syn}(t))≈ϕ(I_{syn}^{0})+\frac{dϕ(I_{syn}^{0})}{dI_{syn}}(I_{syn}(t)−I_{syn}^{0}).
$$

With this approximation, the self-consistent equations for excitatory and inhibitory populations become

$$
{ν_{E}(t)=v_{E}^{0}(1+A_{E}\frac{I_{syn,E}(t)−I_{syn,E}^{0}}{I_{syn,E}^{0}})ν_{I}(t)=v_{I}^{0}(1+A_{I}\frac{I_{syn,I}(t)−I_{syn,I}^{0}}{I_{syn,I}^{0}}),
$$

where $A_{\alpha}=\frac{I_{syn,\alpha}^{0}}{v_{\alpha}^{0}}\frac{dϕ_{\alpha}I_{syn,\alpha}^{0}}{dI_{syn,\alpha}}$ is the dimensionless slope of the current-frequency response function at the current value in asynchronous state, expressed as the ratio between the relative changes in the firing rate and the input current (Brunel and Wang, 2003).

The self-consistent equations Equation 45 together with Equation 41 for the gating variables and Equation 42 for the total synaptic current describe approximate firing rate dynamics of excitatory and inhibitory populations. To determine if the network develops oscillatory instability caused by small fluctuations in population firing rates, we seek solutions for the rates $ν_{E}(t)$ and $ν_{I}(t)$ in which initially small (with relative amplitudes $\epsilon_{E}≪1$ and $\epsilon_{I}≪1$) oscillatory perturbations that can change exponentially with time are added to the stationary rates $v_{E}^{0}$ and $v_{I}^{0}$ such that: $ν_{\alpha}(t)=v_{\alpha}^{0}(1+|\epsilon_{\alpha}|exp⁡(\lambdat)cos(\omegat+\phi_{\alpha}))$ or, equivalently, in complex form

$$
ν_{\alpha}(t)=v_{\alpha}^{0}(1+\epsilon_{\alpha}exp⁡(\lambdat+i\omegat)),\alpha=E,I,
$$

where $\lambda$ is the rate of perturbation growth, $\omega$ is the oscillation frequency, and $\epsilon_{\alpha}$ is complex accounting for a possible shift in oscillation phase $\phi_{\alpha}$ between the two populations. We can now replace the firing rates in Equation 41 with these expressions to solve the two equations and determine the synaptic variables $S_{R}(t)$ for recurrent currents mediated by $R=AMPA, NMDA, GABA$ receptors:

$$
S_{R}(t)=S_{R}^{0}[1+\epsilon_{\alpha_{R}}Q_{R}(\lambda,\omega)exp⁡(\lambdat+i\omegat−iΦ_{R}(\lambda,\omega))],
$$

where

$$
Q_{R}(\lambda,\omega)=\frac{exp(−\lambda\tau_{R,l})}{\sqrt{((1+\lambda\tau_{R,r})^{2}+\omega^{2}\tau_{R,r}^{2})((1+\lambda\tau_{R,d})^{2}+\omega^{2}\tau_{R,d}^{2})}}
$$

and

$$
Φ_{R}(\lambda,\omega)=\omega\tau_{R,l}+atan(\frac{\omega\tau_{R,r}}{1+\lambda\tau_{R,r}})+atan(\frac{\omega\tau_{R,d}}{1+\lambda\tau_{R,d}}).
$$

The components of synaptic currents and the total currents $I_{syn,E}(t)$ and $I_{syn,I}(t)$ can now be calculated and inserted into the linearized self-consistent Equation 45 for population firing rates. Taking into account that the balance between the components of synaptic currents in excitatory and inhibitory populations is equal, we arrive at the following set of two equations

$$
{X_{AMPA}(\lambda,\omega)cos⁡(Φ_{AMPA}(\lambda,\omega))+X_{NMDA}(\lambda,\omega)cos⁡(Φ_{NMDA}(\lambda,\omega))−X_{GABA}(\lambda,\omega)cos⁡(Φ_{GABA}(\lambda,\omega))=1X_{AMPA}(\lambda,\omega)sin⁡(Φ_{AMPA}(\lambda,\omega))+X_{NMDA}(\lambda,\omega)sin⁡(Φ_{NMDA}(\lambda,\omega))−X_{GABA}(\lambda,\omega)sin⁡(Φ_{GABA}(\lambda,\omega))=0
$$

and the relationship between the relative amplitudes:

$$
\epsilon_{E}A_{I}=\epsilon_{I}A_{E},
$$

where

$$
X_{AMPA}(\lambda,\omega)=A_{E}\frac{I_{AMPA}}{I_{syn}}Q_{AMPA}(\lambda,\omega)
$$



$$
X_{NMDA}(\lambda,\omega)=A_{E}\frac{I_{NMDA}}{I_{syn}}Q_{NMDA}(\lambda,\omega)
$$



$$
X_{GABA}(\lambda,\omega)=A_{I}\frac{I_{GABA}}{I_{syn}}Q_{GABA}(\lambda,\omega).
$$

Solving Equation 50, we obtain the rate of perturbation growth $\lambda$ and the oscillation frequency $\omega$. Because both $A_{E}$ and $A_{I}$ are real, the linear relationship between the amplitudes $\epsilon_{E}$ and $\epsilon_{I}$ given by Equation 51 means that there is no phase lag between firing rates of excitatory and inhibitory populations.

### Analytical consideration of the dependence of oscillation growth rate on network parameters

To further elucidate how specifically synaptic conductances $g_{AMPA}$, $g_{NMDA}$, $g_{GABA}$, and external rate $v_{X}$ affect synchrony, we linearize the mean field equations Equation 37 and equations Equation 50 for the stability analysis around the point ${g_{AMPA,{E,I}}^{∗}, g_{NMDA,{E,I}}^{∗}, g_{GABA,{E,I}}^{∗}, v_{X}^{∗} }$ corresponding to the critical state network where $\lambda=0$. We then derive an analytical approximation for the oscillation growth rate $\lambda$ describing its dependence on the synaptic conductances and external rate in the vicinity of this point.

#### Linearization of mean field equations

Approximate analytic description of the changes in the population firing rates $\Deltav_{E}$ and $\Deltav_{I}$ due to small changes in the synaptic conductances and external rate can be obtained by linearizing the current-frequency response function $ϕ$, providing population firing rates $v_{E}$ and $v_{I}$ as a function of synaptic conductances and external rate. We note that the function $ϕ$ (Equations 34–36) explicitly depends on the mean effective synaptic input μ, synaptic noise $\sigma$, membrane time constant $\tau$, and synaptic time constant $\tau_{syn}$, which in turn depend on the synaptic conductances and external rate (Equations 22–33). Thus, changes in the firing rates $\Deltav_{E}$ and $\Deltav_{I}$ in response to small changes in the synaptic conductances $\Deltag_{AMPA}$, $\Deltag_{NMDA}$, $\Deltag_{GABA}$, and external rate $\Deltav_{X}$ can be approximated as:

$$
Δv_{\alpha}=\frac{dϕ_{\alpha}}{d\mu_{\alpha}}Δ\mu_{\alpha}+\frac{dϕ_{\alpha}}{d\sigma_{\alpha}}Δ\sigma_{\alpha}+\frac{dϕ_{\alpha}}{d\tau_{\alpha}}Δ\tau_{\alpha}+\frac{dϕ_{\alpha}}{d\tau_{syn,\alpha}}Δ\tau_{syn,\alpha},\alpha=E,I.
$$

The dominant contribution to $\Deltav_{\alpha}$ is due to the change in synaptic input, $Δ\mu_{\alpha}$. Contributions from the remaining terms are relatively small, with the largest contribution being due to the change in the effective membrane time constant, $Δ\tau_{\alpha}$. Therefore, the expression for $\Deltav_{\alpha}$ can be simplified by retaining only the terms involving $Δ\mu_{\alpha}$ and $Δ\tau_{\alpha}$:

$$
Δv_{\alpha}≈\frac{dϕ_{\alpha}}{d\mu_{\alpha}}Δ\mu_{\alpha}+\frac{dϕ_{\alpha}}{d\tau_{\alpha}}Δ\tau_{\alpha},\alpha=E,I.
$$

$Δ\mu_{\alpha}$ and $Δ\tau_{\alpha}$ are expressed through the relative changes in synaptic conductances $\Deltag_{AMPA}/g_{AMPA}^{*}$, $\Deltag_{NMDA}/g_{NMDA}^{*}$, $\Deltag_{GABA}/g_{GABA}^{*}$, external rate $\Deltav_{X}/v_{X}^{*}$, and the changes in population rates $\Deltav_{E}$ and $\Deltav_{I}$:

$$
Δ\mu_{\alpha}=a_{\alphaE}^{\mu}\Deltaν_{E}+a_{\alphaI}^{\mu}\Deltav_{I}+b_{X,\alpha}^{\mu}\frac{\Deltav_{X}}{v_{X}^{*}}+\sum_{R}b_{R,\alpha}^{\mu}\frac{\Deltag_{R}}{g_{R}^{*}}
$$



$$
Δ\tau_{\alpha}=a_{\alphaE}^{\tau}\Deltaν_{E}+a_{\alphaI}^{\tau}\Deltav_{I}+b_{X,\alpha}^{\tau}\frac{\Deltav_{X}}{v_{X}^{*}}+\sum_{R}b_{R,\alpha}^{\tau}\frac{\Deltag_{R}}{g_{R}^{*}},
$$

where $R={AMPA,NMDA,GABA}$, and

$$
a_{\alphaE}^{\mu}=\frac{(T_{AMPA,\alpha}+T_{NMDA1,\alpha})(V_{E}−V_{L})+T_{NMDA2,\alpha}(V_{0}−V_{L})}{S_{\alpha}}−\frac{\mu_{\alpha}(T_{AMPA,\alpha}+T_{NMDA1,\alpha}+T_{NMDA2,\alpha})}{S_{\alpha}}
$$



$$
a_{\alphaI}^{\mu}=\frac{T_{GABA,\alpha}(V_{I}-\mu_{\alpha}-V_{L})}{S_{\alpha}}
$$



$$
b_{AMPA,\alpha}^{\mu}=\frac{T_{AMPA,\alpha}V_{E}-\mu_{\alpha}-V_{L}}{S_{\alpha}}ν_{E}
$$



$$
b_{NMDA,\alpha}^{\mu}=\frac{T_{NMDA1,\alpha}V_{E}-\mu_{\alpha}-V_{L}+T_{NMDA2,\alpha}(V_{0}-\mu_{\alpha}-V_{L})}{S_{\alpha}}ν_{E}
$$



$$
b_{GABA,\alpha}^{\mu}=\frac{T_{GABA,\alpha}V_{I}-\mu_{\alpha}-V_{L}}{S_{\alpha}}ν_{I}
$$



$$
b_{X,\alpha}^{\mu}=\frac{T_{X,\alpha}V_{E}-\mu_{\alpha}-V_{L}}{S_{\alpha}}ν_{X}
$$



$$
a_{\alphaE}^{\tau}=-\frac{T_{AMPA,\alpha}+T_{NMDA1,\alpha}+T_{NMDA2,\alpha}}{S_{\alpha}}\tau_{\alpha}
$$



$$
a_{\alphaI}^{\tau}=-\frac{T_{GABA,\alpha}}{S_{\alpha}}\tau_{\alpha}
$$



$$
b_{AMPA,\alpha}^{\tau}=-\frac{T_{AMPA,\alpha}}{S_{\alpha}}\tau_{\alpha}ν_{E}
$$



$$
b_{NMDA,\alpha}^{\tau}=-\frac{T_{NMDA1,\alpha}+T_{NMDA2,\alpha}}{S_{\alpha}}\tau_{\alpha}ν_{E}
$$



$$
b_{GABA,\alpha}^{\tau}=-\frac{T_{GABA,\alpha}}{S_{\alpha}}\tau_{\alpha}ν_{I}
$$



$$
b_{X,\alpha}^{\tau}=-\frac{T_{X,\alpha}}{S_{\alpha}}\tau_{\alpha}ν_{X}.
$$

Inserting expressions for $Δ\mu_{\alpha}$ and $Δ\tau_{\alpha}$ into Equation 56, we obtain a closed system of linear equations for the changes in the firing rates of excitatory and inhibitory populations in response to small changes in the synaptic conductances and external rates. In matrix form these equations can be written as

$$
\Deltav=a\Deltav+b\Deltap,
$$

where

$$
a=[ϕ_{\mu,E}^{′}a_{EE}^{\mu}+ϕ_{\tau,E}^{′}a_{EE}^{\tau}ϕ_{\mu,E}^{′}a_{EI}^{\mu}+ϕ_{\tau,E}^{′}a_{EI}^{\tau}ϕ_{\mu,I}^{′}a_{IE}^{\mu}+ϕ_{\tau,I}^{′}a_{IE}^{\tau}ϕ_{\mu,I}^{′}a_{II}^{\mu}+ϕ_{\tau,I}^{′}a_{II}^{\tau}],Δv=[Δν_{E}Δv_{I}]
$$



$$
b^{T}=[ϕ_{\mu,E}^{′}b_{X,E}^{\mu}+ϕ_{\tau,E}^{′}b_{X,E}^{\tau}ϕ_{\mu,I}^{′}b_{X,I}^{\mu}+ϕ_{\tau,I}^{′}b_{X,I}^{\tau}ϕ_{\mu,E}^{′}b_{AMPA,E}^{\mu}+ϕ_{\tau,E}^{′}b_{AMPA,E}^{\tau}ϕ_{\mu,I}^{′}b_{AMPA,I}^{\mu}+ϕ_{\tau,I}^{′}b_{AMPA,I}^{\tau}ϕ_{\mu,E}^{′}b_{NMDA,E}^{\mu}+ϕ_{\tau,E}^{′}b_{NMDA,E}^{\tau}ϕ_{\mu,I}^{′}b_{NMDA,I}^{\mu}+ϕ_{\tau,I}^{′}b_{NMDA,I}^{\tau}ϕ_{\mu,E}^{′}b_{GABA,E}^{\mu}+ϕ_{\tau,E}^{′}b_{GABA,E}^{\tau}ϕ_{\mu,I}^{′}b_{GABA,I}^{\mu}+ϕ_{\tau,I}^{′}b_{GABA,I}^{\tau}],Δp=[Δv_{X}/v_{X}^{∗}Δg_{AMPA}/g_{AMPA}^{∗}Δg_{NMDA}/g_{NMDA}^{∗}Δg_{GABA}/g_{GABA}^{∗}].
$$

Here, the elements of matrices $a$ and $b$ are constants defined by the point in the network parameter space around which the mean field equations are linearized. Components of the vector $\Deltav$ are the changes in the firing rates of excitatory and inhibitory populations due to the changes in the synaptic conductances and external rate given by the components of vector $\Deltap$. Taking into account that $ϕ_{\tau,\alpha}^{`}b_{R,\alpha}^{\tau}≪ϕ_{\mu,\alpha}^{`}b_{R,\alpha}^{\mu}$ and that $\mu_{\alpha}+V_{L}≈V_{\alpha}$, we neglect the $ϕ_{\tau,\alpha}^{`}b_{R,\alpha}^{\tau}$ terms in $b$ and replace $\mu_{\alpha}+V_{L}$ with $V_{\alpha}$. With these approximations $b$ simplifies to:

$$
b≈b_{0}[I_{X}/I_{GABA}I_{AMPA}/I_{GABA}I_{NMDA}/I_{GABA}−1]^{T},b_{0}=[ϕ_{\mu,E}^{′}I_{GABA,E}/g_{m,E}S_{E}ϕ_{\mu,I}^{′}I_{GABA,I}/g_{m,I}S_{I}].
$$

Equation Equation 71 can now be rewritten as

$$
a-I\Deltav+b_{0}I_{X}/I_{GABA}I_{AMPA}/I_{GABA}I_{NMDA}/I_{GABA}-1^{T}\Deltap=0,
$$

where $I$ is the identity matrix. Solving this equation for $\Deltav$ we obtain

$$
\Deltav=WI_{X}/I_{GABA}I_{AMPA}/I_{GABA}I_{NMDA}/I_{GABA}-1^{T}\Deltap,
$$

or in component form

$$
\Deltav_{E}=W_{E}\frac{I_{X}}{I_{GABA}}\frac{\Deltav_{X}}{v_{X}^{*}}+\frac{I_{AMPA}}{I_{GABA}}\frac{\Deltag_{AMPA}}{g_{AMPA}^{*}}+\frac{I_{NMDA}}{I_{GABA}}\frac{\Deltag_{NMDA}}{g_{NMDA}^{*}}-\frac{\Deltag_{GABA}}{g_{GABA}^{*}}
$$



$$
\Deltav_{I}=W_{I}\frac{I_{X}}{I_{GABA}}\frac{\Deltav_{X}}{v_{X}^{*}}+\frac{I_{AMPA}}{I_{GABA}}\frac{\Deltag_{AMPA}}{g_{AMPA}^{*}}+\frac{I_{NMDA}}{I_{GABA}}\frac{\Deltag_{NMDA}}{g_{NMDA}^{*}}-\frac{\Deltag_{GABA}}{g_{GABA}^{*}},
$$

where $W=W_{E}W_{I}^{T}$ is given by

$$
W=-a-I^{-1}b_{0}.
$$

In summary, equations Equations 77, 78 describe changes in the excitatory, $\Deltav_{E}$, and inhibitory, $\Deltav_{I}$, population firing rates due to the small relative changes in the synaptic conductances $\Deltag_{AMPA}/g_{AMPA}^{*}$, $\Deltag_{NMDA}/g_{NMDA}^{*}$, $\Deltag_{GABA}/g_{GABA}^{*}$, and external rate $\Deltav_{X}/v_{X}^{*}$.

#### Linearization of equations for oscillatory instability analysis

Changes in synaptic parameters result not only in the changes of population firing rates, but also affect the stability of population dynamics. To understand the precise role played by the synaptic conductances and external input in the destabilization of the steady dynamics and emergence of network oscillation near the boundary between asynchronous and synchronous states, we derive an approximate analytic description of the change in the rate of oscillatory instability growth $\Delta\lambda$ and the change in the oscillation frequency $\Delta\omega$ caused by small changes in the synaptic conductances and external rate. For this purpose, we linearize equations Equation 50 for $\lambda$ and $\omega$ around the point ${g_{AMPA,{E,I}}^{∗},g_{NMDA,{E,I}}^{∗},g_{GABA,{E,I}}^{∗},v_{X}^{∗}}$ corresponding to the critical state network that is on the boundary between steady and oscillatory states where $\lambda=0$. We do this by taking the differentials with respect to the synaptic variables $Φ_{R}$ and $X_{R}$, ($R=AMPA,NMDA,GABA$) that, in turn, depend on $\lambda$ and $\omega$:

$$
{ΔX_{AMPA}cos⁡(Φ_{AMPA})−X_{AMPA}sin⁡(Φ_{AMPA})ΔΦ_{AMPA}+ΔX_{NMDA}cos⁡(Φ_{NMDA})−X_{NMDA}sin⁡(Φ_{NMDA})ΔΦ_{NMDA}−ΔX_{GABA}cos⁡(Φ_{GABA})+X_{GABA}sin⁡(Φ_{GABA})ΔΦ_{GABA}=0ΔX_{AMPA}sin⁡(Φ_{AMPA})+X_{AMPA}cos⁡(Φ_{AMPA})ΔΦ_{AMPA}+ΔX_{NMDA}sin⁡(Φ_{NMDA})+X_{NMDA}cos⁡(Φ_{NMDA})ΔΦ_{NMDA}−ΔX_{GABA}sin⁡(Φ_{GABA})−X_{GABA}cos⁡(Φ_{GABA})ΔΦ_{GABA}=0,
$$

The parameter $X_{R}$ (see Equations 52–54) characterizes the relative attenuation in the strength of the underlying synapse due to the $R$-current dynamics. In addition to the dependency on $\lambda$ and $\omega$ through $Q_{R}$ (Equation 48), $X_{R}$ depends directly on its corresponding synaptic conductance $g_{R}$ and indirectly on all the synaptic conductances and external rate through its dependency on the slope $ϕ_{I_{syn},\alpha_{R}}^{`}$ of the current-frequency response function. The change $ΔX_{R}$ due to small variations in the synaptic conductances and external rate is given by

$$
ΔX_{R}=X_{R}\frac{Δg_{R}}{g_{R}^{*}}+\frac{Δϕ_{I_{syn,\alpha_{R}}}^{`}}{ϕ_{I_{syn,\alpha_{R}}}^{`}}+\frac{ΔQ_{R}}{Q_{R}},
$$

where $ϕ_{I_{syn},\alpha_{R}}^{`}$, $X_{R}$, $Q_{R}$, and $Φ_{R}$ are constants whose values are defined by the point ${g_{AMPA,{E,I}}^{∗},g_{NMDA,{E,I}}^{∗}, g_{GABA,{E,I}}^{∗},v_{X}^{∗}}$ in the synaptic parameter space around which the stability analysis equations are linearized.

The relative change $ΔQ_{R}/Q_{R}$ can be obtained from Equation 48:

$$
\frac{ΔQ_{R}}{Q_{R}}=-\tau_{R}^{1}Δ\lambda-\tau_{R}^{2}Δ\omega,
$$

and the change in $Φ_{R}$ from Equation 49:

$$
ΔΦ_{R}=\tau_{R}^{1}Δ\omega-\tau_{R}^{2}Δ\lambda,
$$

where

$$
\tau_{R}^{(1)}=\tau_{R,l}+\frac{\tau_{R,r}}{1+(\omega\tau_{R,r})^{2}}+\frac{\tau_{R,d}}{1+(\omega\tau_{R,d})^{2}}
$$



$$
\tau_{R}^{2}=\omega\frac{\tau_{R,r}^{2}}{1+(\omega\tau_{R,r})^{2}}+\frac{\tau_{R,d}^{2}}{1+(\omega\tau_{R,d})^{2}},
$$

and $\omega$ is the oscillation frequency at the critical state. Inserting expressions for $ΔQ_{R}/Q_{R}$ into equations Equation 81 for $ΔX_{R}$ and, subsequently, expressions for $ΔΦ_{R}$ and $ΔX_{R}$ into equations Equation 80, we obtain a system of two linear equations for $Δ\lambda$ and $Δ\omega$:

$$
{T_{+}Δ\omega+T_{−}Δ\lambda=Δξ_{AMPA}+Δξ_{NMDA}−Δξ_{GABA}T_{−}Δ\omega−T_{+}Δ\lambda=Δζ_{AMPA}+Δζ_{NMDA}−Δζ_{GABA},
$$

where

$$
T_{+}=X_{AMPA}\tau_{AMPA}^{+}+X_{NMDA}\tau_{NMDA}^{+}-X_{GABA}\tau_{GABA}^{+}
$$



$$
T_{-}=X_{AMPA}\tau_{AMPA}^{-}+X_{NMDA}\tau_{NMDA}^{-}-X_{GABA}\tau_{GABA}^{-}
$$



$$
\tau_{R}^{+}=\tau_{R}^{(1)}sin⁡(Φ_{R})+\tau_{R}^{(2)}cos⁡(Φ_{R})
$$



$$
\tau_{R}^{−}=\tau_{R}^{(1)}cos⁡(Φ_{R})−\tau_{R}^{(2)}sin⁡(Φ_{R})
$$



$$
Δξ_{R}=X_{R}cos⁡(Φ_{R})\frac{Δg_{R}}{g_{R}^{*}}+\frac{Δϕ_{I_{syn,\alpha_{R}}}^{`}}{ϕ_{I_{syn,\alpha_{R}}}^{`}}
$$



$$
Δζ_{R}=-X_{R}sin⁡(Φ_{R})\frac{Δg_{R}}{g_{R}^{*}}+\frac{Δϕ_{I_{syn,\alpha_{R}}}^{`}}{ϕ_{I_{syn,\alpha_{R}}}^{`}}
$$

and $R=AMPA,NMDA,GABA$. Solving the system of equations Equation 86 for $Δ\lambda$ and $Δ\omega$ we obtain:

$$
Δ\lambda=Λ_{AMPA}(\frac{Δg_{AMPA}}{g_{AMPA}^{∗}}+\frac{Δϕ_{I_{syn,E}}^{′}}{ϕ_{I_{syn,E}}^{′}})+Λ_{NMDA}(\frac{Δg_{NMDA}}{g_{NMDA}^{∗}}+\frac{Δϕ_{I_{syn,E}}^{′}}{ϕ_{I_{syn,E}}^{′}})−Λ_{GABA}(\frac{Δg_{GABA}}{g_{GABA}^{∗}}+\frac{Δϕ_{I_{syn,I}}^{′}}{ϕ_{I_{syn,I}}^{′}})
$$



$$
Δ\omega=Ω_{AMPA}(\frac{Δg_{AMPA}}{g_{AMPA}^{∗}}+\frac{Δϕ_{I_{syn,E}}^{′}}{ϕ_{I_{syn,E}}^{′}})+Ω_{NMDA}(\frac{Δg_{NMDA}}{g_{NMDA}^{∗}}+\frac{Δϕ_{I_{syn,E}}^{′}}{ϕ_{I_{syn,E}}^{′}})−Ω_{GABA}(\frac{Δg_{GABA}}{g_{GABA}^{∗}}+\frac{Δϕ_{I_{syn,I}}^{′}}{ϕ_{I_{syn,I}}^{′}}).
$$

Here, $Λ_{R}$ and $Ω_{R}$ are constants defined by the parameters of the critical state network around which the stability analysis equations are linearized:

$$
Λ_{R}=\frac{X_{R}}{T_{+}^{2}+T_{-}^{2}}T_{+}sin⁡Φ_{R}+T_{-}cos⁡Φ_{R}
$$



$$
Ω_{R}=\frac{X_{R}}{T_{+}^{2}+T_{-}^{2}}T_{+}cos⁡Φ_{R}-T_{-}sin⁡Φ_{R},
$$

or, equivalently,

$$
Λ_{R}=\frac{X_{R}}{T_{0}}cos⁡(Φ_{R}+Φ_{0})
$$



$$
Ω_{R}=−\frac{X_{R}}{T_{0}}sin⁡(Φ_{R}+Φ_{0}),
$$

where $T_{0}=\sqrt{T_{+}^{2}+T_{-}^{2}}$ and $Φ_{0}=-atan⁡(T_{+}/T_{-})$.

Note that while $\Delta\lambda$ and $\Delta\omega$ given by equations Equations 93 and 94 depend directly on the changes in the synaptic conductances, they also depend indirectly on these parameters and the change in external rate through the terms involving $Δϕ_{I_{syn,E}}^{`}$ and $Δϕ_{I_{syn,I}}^{`}$ characterizing changes in the slopes of the current-frequency response functions of excitatory and inhibitory neurons. To calculate these changes due to the changes in the synaptic conductances and external rate, we note that

$$
\frac{Δϕ_{I_{syn}}^{′}}{ϕ_{I_{syn}}^{′}}=\frac{Δ(\frac{dϕ}{d\mu}\frac{d\mu}{dI_{syn}})}{\frac{dϕ}{d\mu}\frac{d\mu}{dI_{syn}}}=\frac{\frac{d\mu}{dI_{syn}}Δ(\frac{dϕ}{d\mu})+\frac{dϕ}{d\mu}Δ(\frac{d\mu}{dI_{syn}})}{\frac{dϕ}{d\mu}\frac{d\mu}{dI_{syn}}}=\frac{Δϕ_{\mu}^{′}}{ϕ_{\mu}^{′}}+\frac{Δ(\frac{d\mu}{dI_{syn}})}{\frac{d\mu}{dI_{syn}}}.
$$

Taking into account the linear relationship $\mu~-I_{syn}/g_{m}S$ between the effective synaptic input μ and total synaptic current $I_{syn}$, we arrive at

$$
\frac{Δϕ_{I_{syn,\alpha}}^{′}}{ϕ_{I_{syn},\alpha}^{′}}=\frac{Δϕ_{\mu,\alpha}^{′}}{ϕ_{\mu,\alpha}^{′}}−\frac{ΔS_{\alpha}}{S_{\alpha}},\alpha=E,I.
$$

As in the case of the change in the current-frequency response function $Δϕ_{\mu,\alpha}$, the dominant contribution to the change in the slope of the response function $Δϕ_{\mu,\alpha}^{`}$ is coming from the change in the synaptic input $\Delta\mu_{\alpha}$, while the change in the effective membrane time constant $\Delta\tau_{\alpha}$, similarly, is the next largest contribution. Therefore, $Δϕ_{\mu,\alpha}^{`}$ can be approximated as

$$
Δϕ_{\mu,\alpha}^{`}≈\frac{d^{2}ϕ_{\alpha}}{d\mu_{\alpha}^{2}}\Delta\mu_{\alpha}+\frac{d^{2}ϕ_{\alpha}}{d\tau_{\alpha}d\mu_{\alpha}}\Delta\tau_{\alpha}.
$$

Note also that using Equation 22 one can express the relative change $ΔS_{\alpha}/S_{\alpha}$ through the change $\Delta\tau_{\alpha}$ as $ΔS_{\alpha}/S_{\alpha}=-Δ\tau_{\alpha}/\tau_{\alpha}$. Inserting expressions for $Δϕ_{\mu,\alpha}^{`}$ and $ΔS_{\alpha}/S_{\alpha}$ into Equation 100 we obtain

$$
\frac{Δϕ_{I_{syn,\alpha}}^{`}}{ϕ_{I_{syn,\alpha}}^{`}}=\frac{ϕ_{\mu\mu,\alpha}^{``}}{ϕ_{\mu,\alpha}^{`}}\Delta\mu_{\alpha}+\frac{ϕ_{\tau\mu,\alpha}^{``}}{ϕ_{\mu,\alpha}^{`}}+\frac{1}{\tau_{\alpha}}\Delta\tau_{\alpha}.
$$

Equations for $\Delta\mu_{\alpha}$ and $\Delta\tau_{\alpha}$ in terms of the changes in the synaptic conductances, external rate, and the resulting changes in the population firing rates $\Deltav_{E}$ and $\Deltav_{I}$ have been already derived and are given by Equations 57 and 58. We replace $\Deltav_{E}$ and $\Deltav_{I}$ in these equations with the solution obtained from the linearization of the mean field equations given, respectively, by Equations 77, 78. Next, by inserting the resulting $\Delta\mu_{\alpha}$ and $\Delta\tau_{\alpha}$ into Equation 102, we obtain expressions describing the relative changes in the slopes of the response functions for excitatory and inhibitory neurons due to the small changes in the synaptic conductances and external rate. In matrix form, these expressions can be written as

$$
[\frac{Δϕ_{I_{syn,E}}^{′}}{ϕ_{I_{syn,E}}^{′}}\frac{Δϕ_{I_{syn,I}}^{′}}{ϕ_{I_{syn,I}}^{′}}]=−a∼W[I_{X}/I_{GABA}I_{AMPA}/I_{GABA}I_{NMDA}/I_{GABA}−1]^{T}Δp+b∼Δp,
$$

where

$$
a~=\frac{ϕ_{\mu\mu,E}^{``}}{ϕ_{\mu,E}^{`}}a_{EE}^{\mu}+\frac{ϕ_{\tau\mu,E}^{``}}{ϕ_{\mu,E}^{`}}+\frac{1}{\tau_{E}}a_{EE}^{\tau}\frac{ϕ_{\mu\mu,E}^{``}}{ϕ_{\mu,E}^{`}}a_{EI}^{\mu}+\frac{ϕ_{\tau\mu,E}^{``}}{ϕ_{\mu,E}^{`}}+\frac{1}{\tau_{E}}a_{EI}^{\tau}\frac{ϕ_{\mu\mu,I}^{``}}{ϕ_{\mu,I}^{`}}a_{IE}^{\mu}+\frac{ϕ_{\tau\mu,I}^{``}}{ϕ_{\mu,I}^{`}}+\frac{1}{\tau_{I}}a_{IE}^{\tau}\frac{ϕ_{\mu\mu,I}^{``}}{ϕ_{\mu,I}^{`}}a_{II}^{\mu}+\frac{ϕ_{\tau\mu,I}^{``}}{ϕ_{\mu,I}^{`}}+\frac{1}{\tau_{I}}a_{II}^{\tau}
$$



$$
b~^{T}=\frac{ϕ_{\mu\mu,E}^{``}}{ϕ_{\mu,E}^{`}}b_{X,E}^{\mu}+\frac{ϕ_{\tau\mu,E}^{``}}{ϕ_{\mu,E}^{`}}+\frac{1}{\tau_{E}}b_{X,E}^{\tau}\frac{ϕ_{\mu\mu,I}^{``}}{ϕ_{\mu,I}^{`}}b_{X,I}^{\mu}+\frac{ϕ_{\tau\mu,I}^{``}}{ϕ_{\mu,I}^{`}}+\frac{1}{\tau_{I}}b_{X,I}^{\tau}\frac{ϕ_{\mu\mu,E}^{``}}{ϕ_{\mu,E}^{`}}b_{AMPA,E}^{\mu}+\frac{ϕ_{\tau\mu,E}^{``}}{ϕ_{\mu,E}^{`}}+\frac{1}{\tau_{E}}b_{AMPA,E}^{\tau}\frac{ϕ_{\mu\mu,I}^{``}}{ϕ_{\mu,I}^{`}}b_{AMPA,I}^{\mu}+\frac{ϕ_{\tau\mu,I}^{``}}{ϕ_{\mu,I}^{`}}+\frac{1}{\tau_{I}}b_{AMPA,I}^{\tau}\frac{ϕ_{\mu\mu,E}^{``}}{ϕ_{\mu,E}^{`}}b_{NMDA,E}^{\mu}+\frac{ϕ_{\tau\mu,E}^{``}}{ϕ_{\mu,E}^{`}}+\frac{1}{\tau_{E}}b_{NMDA,E}^{\tau}\frac{ϕ_{\mu\mu,I}^{``}}{ϕ_{\mu,I}^{`}}b_{NMDA,I}^{\mu}+\frac{ϕ_{\tau\mu,I}^{``}}{ϕ_{\mu,I}^{`}}+\frac{1}{\tau_{I}}b_{NMDA,I}^{\tau}\frac{ϕ_{\mu\mu,E}^{``}}{ϕ_{\mu,E}^{`}}b_{GABA,E}^{\mu}+\frac{ϕ_{\tau\mu,E}^{``}}{ϕ_{\mu,E}^{`}}+\frac{1}{\tau_{E}}b_{GABA,E}^{\tau}\frac{ϕ_{\mu\mu,I}^{``}}{ϕ_{\mu,I}^{`}}b_{GABA,I}^{\mu}+\frac{ϕ_{\tau\mu,I}^{``}}{ϕ_{\mu,I}^{`}}+\frac{1}{\tau_{I}}b_{GABA,I}^{\tau}.
$$

The elements of matrices $a~$ and $b~$ are constants defined by the parameters of the critical state network. Noting that $\frac{ϕ_{\tau\mu,\alpha}^{``}}{ϕ_{\mu,\alpha}^{`}}+\frac{1}{\tau_{\alpha}}b_{R,\alpha}^{\tau}≪\frac{ϕ_{\mu\mu,\alpha}^{``}}{ϕ_{\mu,\alpha}^{`}}b_{R,\alpha}^{\mu}$, we neglect the $\frac{ϕ_{\tau\mu,\alpha}^{``}}{ϕ_{\mu,\alpha}^{`}}+\frac{1}{\tau_{\alpha}}b_{R,\alpha}^{\tau}$ terms in $b~$ and, as in the calculation of the change in the current-frequency response function, replace $\mu_{\alpha}+V_{L}$ with $V_{\alpha}$. With these approximations $b~$ simplifies to:

$$
b∼≈b∼_{0}[I_{X}/I_{GABA}I_{AMPA}/I_{GABA}I_{NMDA}/I_{GABA}−1]^{T},b∼_{0}=[\frac{ϕ_{\mu\mu,E}^{′′}}{ϕ_{\mu,E}^{′}}\frac{I_{GABA,E}}{g_{m,E}S_{E}}\frac{ϕ_{\mu\mu,I}^{′′}}{ϕ_{\mu,I}^{′}}\frac{I_{GABA,I}}{g_{m,I}S_{I}}].
$$

Equation Equation 103 can now be written as

$$
\frac{Δϕ_{I_{syn,E}}^{`}}{ϕ_{I_{syn,E}}^{`}}\frac{Δϕ_{I_{syn,I}}^{`}}{ϕ_{I_{syn,I}}^{`}}=UI_{X}/I_{GABA}I_{AMPA}/I_{GABA}I_{NMDA}/I_{GABA}-1^{T}\Deltap,
$$

or in component form

$$
\frac{Δϕ_{I_{syn,E}}^{`}}{ϕ_{I_{syn,E}}^{`}}=U_{E}\frac{I_{X}}{I_{GABA}}\frac{\Deltav_{X}}{v_{X}^{*}}+\frac{I_{AMPA}}{I_{GABA}}\frac{\Deltag_{AMPA}}{g_{AMPA}^{*}}+\frac{I_{NMDA}}{I_{GABA}}\frac{\Deltag_{NMDA}}{g_{NMDA}^{*}}-\frac{\Deltag_{GABA}}{g_{GABA}^{*}}
$$



$$
\frac{Δϕ_{I_{syn,I}}^{`}}{ϕ_{I_{syn,I}}^{`}}=U_{I}\frac{I_{X}}{I_{GABA}}\frac{\Deltav_{X}}{v_{X}^{*}}+\frac{I_{AMPA}}{I_{GABA}}\frac{\Deltag_{AMPA}}{g_{AMPA}^{*}}+\frac{I_{NMDA}}{I_{GABA}}\frac{\Deltag_{NMDA}}{g_{NMDA}^{*}}-\frac{\Deltag_{GABA}}{g_{GABA}^{*}},
$$

where $U=U_{E}U_{I}^{T}$ is given by

$$
U=−a~W+b_{0}~.
$$

Equations Equations 108 and 109 describing the relative changes in the slopes of the response functions for excitatory and inhibitory neurons can now be combined with Equations 93 and 94 to account for both direct and indirect dependence of the change in the oscillation growth rate $Δ\lambda$ and change in the oscillation frequency $Δ\omega$ on the small relative changes in the synaptic conductances and external rate.

### Numerical solutions

Self-consistent mean field equations for the eight conductance parameters, and linear stability equations for the perturbation growth rate $\lambda$ and the oscillation frequency $\omega$ were both solved numerically using custom codes written in MATLAB (The MathWorks) with the aid of fsolve function.
