# Putting the theory into ‘burstlet theory’ with a biophysical model of burstlets and bursts in the respiratory preBötzinger complex

## Authors

- Ryan S Phillips<sup>1</sup> ([ORCID: 0000-0002-8570-2348](https://orcid.org/0000-0002-8570-2348)) †
- Jonathan E Rubin<sup>1</sup> ([ORCID: 0000-0002-1513-1551](https://orcid.org/0000-0002-1513-1551)) †

### Affiliations

1. Department of Mathematics and Center for the Neural Basis of Cognition, University of Pittsburgh Pittsburgh United States ([ROR:01an3r305](https://ror.org/01an3r305))

† Corresponding author

## Abstract

Inspiratory breathing rhythms arise from synchronized neuronal activity in a bilaterally distributed brainstem structure known as the preBötzinger complex (preBötC). In in vitro slice preparations containing the preBötC, extracellular potassium must be elevated above physiological levels (to 7–9 mM) to observe regular rhythmic respiratory motor output in the hypoglossal nerve to which the preBötC projects. Reexamination of how extracellular K+ affects preBötC neuronal activity has revealed that low-amplitude oscillations persist at physiological levels. These oscillatory events are subthreshold from the standpoint of transmission to motor output and are dubbed burstlets. Burstlets arise from synchronized neural activity in a rhythmogenic neuronal subpopulation within the preBötC that in some instances may fail to recruit the larger network events, or bursts, required to generate motor output. The fraction of subthreshold preBötC oscillatory events (burstlet fraction) decreases sigmoidally with increasing extracellular potassium. These observations underlie the burstlet theory of respiratory rhythm generation. Experimental and computational studies have suggested that recruitment of the non-rhythmogenic component of the preBötC population requires intracellular Ca2+ dynamics and activation of a calcium-activated nonselective cationic current. In this computational study, we show how intracellular calcium dynamics driven by synaptically triggered Ca2+ influx as well as Ca2+ release/uptake by the endoplasmic reticulum in conjunction with a calcium-activated nonselective cationic current can reproduce and offer an explanation for many of the key properties associated with the burstlet theory of respiratory rhythm generation. Altogether, our modeling work provides a mechanistic basis that can unify a wide range of experimental findings on rhythm generation and motor output recruitment in the preBötC.

## Introduction

The complex neurological rhythms produced by central pattern generators (CPGs) underlie numerous behaviors in healthy and pathological states. These activity patterns also serve as relatively experimentally accessible instances of the broader class of rhythmic processes associated with brain function. As such, CPGs have been extensively studied using a combination of experimental and computational approaches. The inspiratory CPG located in the preBötzinger complex (preBötC) in the mammalian respiratory brainstem is perhaps one of the most intensively investigated CPGs. Despite decades of research, the mechanisms of rhythm and pattern generation within this circuit remain unresolved and highly controversial; however, it appears that the pieces may now be in place to resolve this controversy.

Much of the debate in contemporary research into the mechanisms of preBötC rhythm and pattern generation revolves around the roles of specific ion currents, such as $I_{N⁢a⁢P}$ and $I_{C⁢A⁢N}$ (Thoby-Brisson and Ramirez, 2001; Del Negro et al., 2002a; Koizumi and Smith, 2008; Koizumi et al., 2018; Picardo et al., 2019), and whether the observed rhythm is driven by an emergent network process (Rekling and Feldman, 1998; Del Negro et al., 2005; Del Negro et al., 2002b; Del Negro et al., 2002b; Rubin et al., 2009; Sun et al., 2019; Ashhad and Feldman, 2020) and/or by intrinsically rhythmic or pacemaker neurons (Johnson et al., 1994; Koshiya and Smith, 1999; Peña et al., 2004). This debate is fueled by seemingly contradictory pharmacological blocking studies (Del Negro et al., 2002a; Peña et al., 2004; Del Negro et al., 2005; Pace et al., 2007b; Koizumi and Smith, 2008) and by new experimental studies (Kam et al., 2013a; Feldman and Kam, 2015; Kallurkar et al., 2020; Sun et al., 2019; Ashhad and Feldman, 2020) that challenge existing conceptual and computational models about the generation of activity patterns in the preBötC and underlie the so-called burstlet theory of respiratory rhythm generation.

A simple but reasonable hypothesis would be that a group of dedicated preBötC neurons produces a rhythmic output that induces inspiratory movement of the diaphragm, with the strength of that output tuned by some combination of the intensity of firing of these neurons and the number of neurons that become active. The conceptual framework of burstlet theory posits a more complicated two-stage view: first, inspiratory oscillations arise from an emergent, repetitive network process in a specific preBötC subpopulation dedicated to rhythm generation. These oscillations can continue independent of their downstream impact. Second, for inspiration to occur on a particular oscillation cycle, this initial activity must recruit a secondary pattern-generating subpopulation to magnify the oscillation into a full network burst capable of eliciting motor output. This hypothesis is supported by experimental preparations that compared local preBötC neuronal activity and motor output at the hypoglossal (XII) nerve in medullary slices. These studies found that in a low excitability state (controlled by the bath K+ concentration, $K_{bath}$), the preBötC generates a regular rhythm featuring a mixture of large and small amplitude network oscillations, dubbed bursts and burstlets, respectively, with only the bursts eliciting XII motor output (Kam et al., 2013a). Moreover, the fraction of low-amplitude preBötC events (burstlet fraction) sigmoidally decreases with increasing $K_{b⁢a⁢t⁢h}$ and only a subset of preBötC neurons are active during burstlets (Kallurkar et al., 2020). Importantly, preBötC bursts can be blocked by application of cadmium (Cd2+), a calcium channel blocker, without affecting the ongoing burstlet rhythm (Kam et al., 2013a; Sun et al., 2019), supporting the idea that rhythm generation occurs in a distinct preBötC subpopulation from pattern generation and demonstrating that conversion of a burstlet into a burst is a Ca2+-dependent process. Finally, rhythm generation in the burstlet population is hypothesized to result from an emergent network percolation process. This last idea was developed to explain holographic photostimulation experiments, which found that optically stimulating small subsets (4–9) of preBötC inspiratory neurons were sufficient to reliably evoke endogenous-like XII inspiratory bursts with delays averaging $255\pm45ms$ (Kam et al., 2013b). The small number of neurons required to evoke a network burst superficially seems to be at odds with reported sparse connectivities among preBötC neurons (Rekling et al., 2000), while models that can capture this effect via fast threshold modulation (Rubin and Terman, 2002) or the presentation of multiple stimulus pulses in a model of network bursting driven by synaptic dynamics (Guerrier et al., 2015) do not produce such extended delay durations. Additionally, these delays are on a similar timescale to the ramping pre-inspiratory neuronal activity that precedes network-wide inspiratory bursts, leading to the hypothesis that stimulation of this small set of preBötC neurons kicks off an endogenous neuronal percolation process underlying rhythm generation, which could be initiated by the near-coincident spontaneous spiking of a small number of preBötC neurons.

The experimental underpinning of burstlet theory challenges current ideas about inspiratory rhythm and pattern generation. However, the proposed mechanisms of burst and burstlet generation remain hypothetical and, to date, there has not been a quantitative model that provides a unified, mechanistic explanation for the key experimental observations or that validates the conceptual basis for this theory. Interestingly, key components of burstlet theory, namely, that inspiratory rhythm and pattern are separable processes and that large amplitude network-wide bursts depend on calcium-dependent mechanisms, are supported by recent experimental and computational studies. Specifically, Koizumi et al., 2018 and Picardo et al., 2019 showed that the amplitude (i.e., pattern) of preBötC and XII bursts is controlled, independently from the ongoing rhythm, by the transient receptor potential channel (TRPM4), a calcium-activated nonselective cation current ($I_{C⁢A⁢N}$). These findings are consistent with burstlet theory as they demonstrate that rhythm and pattern are separable processes at the level of the preBötC. Moreover, these experimental observations are robustly reproduced by a recent computational modeling study (Phillips et al., 2019a), which shows that pattern generation can occur independently of rhythm generation. Consistent with burstlet theory, this model predicts that rhythm generation arises from a small subset of preBötC neurons, which in this model form a persistent sodium ($I_{N⁢a⁢P}$)-dependent rhythmogenic kernel, and that rhythmic synaptic drive from these neurons triggers postsynaptic calcium transients, $I_{C⁢A⁢N}$ activation, and amplification of the inspiratory drive potential, which drives bursting in the rest of the network.

These recent results suggest that conversion of burstlets into bursts may be Ca2+ and $I_{C⁢A⁢N}$ dependent, occurring when synaptically triggered calcium transients in non-rhythmogenic preBötC neurons are intermittently large enough for $I_{C⁢A⁢N}$ activation to occur and to yield recruitment of these neurons into the network oscillation. The biophysical mechanism responsible for periodic amplification of Ca2+ transients is not known, however. In this computational study, we put together and build upon these previous findings to show that periodic amplification of synaptically triggered $I_{C⁢A⁢N}$ transients by calcium-induced calcium release (CICR) from intracellular stores provides a plausible mechanism that can produce the observed conversion of burstlets into bursts and can explain diverse experimental findings associated with this process. Altogether, our modeling work suggests a plausible mechanistic basis for the conceptual framework of burstlet theory and the experimental observations that this theory seeks to address.

## Results

### CICR periodically amplifies intracellular calcium transients

Our first aim in this work was to test whether CICR from endoplasmic reticulum (ER) stores could repetitively amplify synaptically triggered Ca2+ transients. To address this aim, we constructed a cellular model that includes the ER. The model features a Ca2+ pump, which extrudes Ca2+ from the intracellular space, a sarcoendoplasmic reticulum calcium transport ATPase (SERCA) pump, which pumps Ca2+ from the intracellular space into the ER, and the Ca2+-activated inositol trisphosphate (IP3) receptor (Figure 1A). To simulate calcium transients synaptically generated from a rhythmogenic source (i.e., burstlets), we imposed a square wave Ca2+ current into the intracellular space with varied frequency and amplitude but fixed duration (250 ms) and monitored the resulting intracellular Ca2+ transients. Depending on parameter values used, we observed various combinations of low- and high-amplitude Ca2+ responses and characterized how the fraction of Ca2+ transients that have low amplitude depends on values selected within the 2D parameter space parameterized by Ca2+ pulse frequency and amplitude. We found that the fraction of low-amplitude Ca2+ transients decreases as either or both of the Ca2+ pulse frequency and amplitude are increased (Figure 1B and example traces C1–C4).

![Figure 1.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig1-v2.jpg)

**Figure 1.:** (A) Schematic diagram of the model setup showing square wave profile of Ca2+ current input into the intracellular space, uptake of Ca2+ into the ER by the sarcoendoplasmic reticulum calcium transport ATPase (SERCA) pump, Ca2+ release through the IP3 receptor, and extrusion of Ca2+ through a pump in the cell membrane. (B) Fraction of low-amplitude intracellular Ca2+ transients as a function of the Ca2+ pulse frequency and amplitude. Pulse duration was fixed at 250 ms. (C1–C4) Example traces showing several ratios of low- and high-amplitude Ca2+ transients and the dynamics of the ER stores Ca2+ concentration. Inset in C2 highlights the delay between pulse onset and CICR. The pulse amplitude and frequency for each trace are indicated in panel (B).

### Bursts and burstlets in a two-neuron preBötC network

Next, we tested whether the CICR mechanism (Figure 1) could drive intermittent recruitment in a reciprocally connected two-neuron network that includes one intrinsically rhythmic and one nonrhythmic neuron as a preliminary step towards considering the rhythm and pattern-generating subpopulations of the preBötC suggested by burstlet theory (Kam et al., 2013a; Cui et al., 2016; Kallurkar et al., 2020; Ashhad and Feldman, 2020) and recent computational investigation (Phillips et al., 2019a). In this network, neuron 1 is an $I_{N⁢a⁢P}$-dependent intrinsically bursting neuron, with a burst frequency that is varied by injecting an applied current, $I_{A⁢P⁢P}$ (Figure 2A2–A3). The rhythmic bursting from neuron 1 generates periodic postsynaptic currents ($I_{S⁢y⁢n}$) in neuron 2, carried in part by Ca2+ ions, which are analogous to the square wave Ca2+ current in Figure 1. The amplitude of the postsynaptic Ca2+ transient is determined by the number of spikes per burst (Figure 2A4) and by the parameter $P_{S⁢y⁢n⁢C⁢a}$, which determines the percentage of $I_{S⁢y⁢n}$ carried by Ca2+ ions (see ‘Materials and methods’ for a full description of these model components). Conversion of a burstlet (isolated neuron 1 burst) into a network burst (recruitment of neuron 2) is dependent on CICR (see Figure 2—figure supplement 1), which increases intracellular calcium above the threshold for $I_{C⁢A⁢N}$ activation.

![Figure 2.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig2-v2.jpg)

**Figure 2.:** (A1) Schematic diagram of the synaptically uncoupled network. The rhythm- and pattern-generating components of the network are represented by neurons 1 and 2, respectively. (A2) Example trace showing intrinsic bursting in neuron 1 and quiescence in neuron 2. (A3) Burst frequency and (A4) the number of spikes per burst in neuron 1 as a function of an applied current ($I_{A⁢P⁢P}$). Neuron 2 remained quiescent within this range of $I_{A⁢P⁢P}$. (B1) Schematic diagram of the synaptically coupled network. (B2–B4) 2D plots characterizing the (B2) burstlet fraction, (B3) neuron 2 (burst) frequency, and (B4) neuron 2 spikes per burst (burst amplitude) as a function of $I_{A⁢P⁢P}$ and $P_{S⁢y⁢n⁢C⁢a}$. (C1–C4) Example traces for neurons 1 and 2 for various $I_{A⁢P⁢P}$ and $P_{S⁢y⁢n⁢C⁢a}$ values indicated in (B2–B4). Notice the scale bar is 100s in C1 and 10s in (C2–C4). Inset in (C1) shows the burst shape not visible on the 100 s timescale. The model parameters used in these simulations are: (neurons 1 and 2) $K_{Bath}=8mM$, $g_{Leak}=3.35nS$, $W_{12}=W_{21}=0.006nS$; (neuron 1) $g_{NaP}=3.33nS$, $g_{CAN}=0.0nS$, (neuron 2) $g_{NaP}=1.5nS$, $g_{CAN}=1.5nS$.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** These simulations are identical to those in Figure 2 except the conductance of the IP3 receptor is set to zero ($G_{IP3}=0/ms$). (A1) Schematic diagram of the synaptically uncoupled network. The rhythm- and pattern-generating components of the network are represented by neurons 1 and 2, respectively. (A2) Example trace showing intrinsic bursting in neuron 1 and quiescence in neuron 2. (A3) Burst frequency and (A4) the number of spikes per burst in neuron 1 as a function of an applied current ($I_{A⁢P⁢P}$). Neuron 2 remained quiescent within this range of $I_{A⁢P⁢P}$. (B1) Schematic diagram of the synaptically coupled network. (B2–B4) 2D plots characterizing the (B2) burstlet fraction, (B3) neuron 2 (burst) frequency, and (B4) neuron 2 spikes per burst (burst amplitude) as a function of $I_{A⁢P⁢P}$ and $P_{S⁢y⁢n⁢C⁢a}$. (C1–C4) Example traces for neurons 1 and 2 for various $I_{A⁢P⁢P}$ and $P_{S⁢y⁢n⁢C⁢a}$ values indicated in (B2–B4). Notice that neuron 2 is never recruited by the bursting in neuron 1 for any of the conditions tested. The model parameters used in these simulations are: (neurons 1 and 2) $K_{Bath}=8mM$, $g_{Leak}=3.35nS$, $W_{12}=W_{21}=0.006nS$; (neuron 1) $g_{NaP}=3.33nS$, $g_{CAN}=0.0nS$, (neuron 2) $g_{NaP}=1.5nS$, $g_{CAN}=1.5nS$.

In the reciprocally connected network, we first quantified the dependence of the burstlet fraction, which was defined as the number of burstlets (neuron 1 bursts without recruitment of neuron 2) divided by the total number of burstlets and network bursts (bursts in neuron 1 with recruitment of neuron 2), on $I_{A⁢P⁢P}$ and $P_{S⁢y⁢n⁢C⁢a}$. Increasing $I_{A⁢P⁢P}$ increases the burst frequency in neuron 1 and decreases the number of spikes per neuron 1 burst (Figure 2A3 and A4), consistent with past literature (Butera et al., 1999; Del Negro et al., 2001). These changes do not strongly impact the burstlet fraction until $I_{A⁢P⁢P}$ grows enough, at which point the shorter, more rapid bursts of neuron 1 become less effective at recruiting neuron 2 and thus the burstlet fraction increases (Figure 2B2; note that increasing $I_{A⁢P⁢P}$ corresponds to a horizontal cut through the panel). In general, increasing $P_{S⁢y⁢n⁢C⁢a}$ decreased the burstlet fraction (i.e., increased the frequency of neuron 2 recruitment) by causing a larger calcium influx with each neuron 1 burst (see Figure 2B2 and C1–C4).

The burst frequency in neuron 2 is determined by the burst frequency of neuron 1 and the burstlet fraction. These effects determine the impact of changes in $P_{S⁢y⁢n⁢C⁢a}$ and $I_{A⁢P⁢P}$ on neuron 2 burst frequency (Figure 2B3). As $I_{A⁢P⁢P}$ increases, the rise in burstlet frequency implies that neuron 2 bursts in response to a smaller fraction of neuron 1 bursts, yet the rise in neuron 1 burst frequency means that these bursts occur faster. These two effects can balance to yield a relatively constant neuron 2 frequency, although the balance is imperfect and frequency does eventually increase. Increases in $P_{S⁢y⁢n⁢C⁢a}$ more straightforwardly lead to increases in neuron 2 burst frequency as the burstlet fraction drops.

Finally, the number of spikes per burst in neuron 2 is not strongly affected by changes in $I_{A⁢P⁢P}$ and $P_{S⁢y⁢n⁢C⁢a}$ (Figure 2B4), suggesting an all-or-none nature of recruitment of bursting in neuron 2. Interestingly, the period between network bursts (i.e., time between neuron 2 recruitment events) can be on the order of hundreds of seconds (e.g., Figure 2C1). This delay is consistent with some of the longer timescales shown in experiments characterizing bursts and burstlets (Kallurkar et al., 2020).

### CICR supports bustlets and bursts in a data-constrained preBötC network model

Next, we tested whether the CICR mechanism presented in Figures 1 and 2 could underlie the conversion of burstlets into bursts in a larger preBötC model network including rhythm- and pattern-generating subpopulations (see ‘Data analysis and definitions’ section for details on how these are distinguished in the network setting) and whether this network could capture the $K_{b⁢a⁢t⁢h}$-dependent changes in the burstlet fraction characterized in Kallurkar et al., 2020. $K_{b⁢a⁢t⁢h}$ sets the extracellular K+ concentration, which in turn determines the driving force for any ionic currents that flux K+. In preBötC neurons, these currents include the fast K+ current, which is involved in action potential generation, and the K+-dominated leak conductance, which primarily affects excitability (Figure 3A). In our simulations, we modeled the potassium ($E_{K}$) and leak ($E_{L⁢e⁢a⁢k}$) reversal potentials as functions of $K_{b⁢a⁢t⁢h}$ using the Nernst and Goldman–Hodgkin–Katz equations. The resulting curves were tuned to match existing data from Koizumi and Smith, 2008, as shown in Figure 3B. In our simulations, we found that intrinsic bursting is extremely sensitive to changes in $K_{b⁢a⁢t⁢h}$. However, with increasing $K_{b⁢a⁢t⁢h}$, intrinsic bursting could be maintained over a wide range of K+ concentrations when accompanied by increases in $g_{L⁢e⁢a⁢k}$ (Figure 3C). Additionally, the number of spikes per burst in the bursting regime increases with $K_{b⁢a⁢t⁢h}$ (Figure 3—figure supplement 1). This $K_{b⁢a⁢t⁢h}$-dependence of $g_{L⁢e⁢a⁢k}$ is consistent with experimental data showing that neuronal input resistance decreases with increasing $K_{b⁢a⁢t⁢h}$ (Okada et al., 2005).

![Figure 3.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig3-v2.jpg)

**Figure 3.:** (A) Schematic diagram of an isolated model preBötzinger complex (preBötC) neuron showing the simulated ion channels involved in AP generation, excitability, and burst generation, as well as indication of currents directly affected by changing the bath potassium concentration ($K_{b⁢a⁢t⁢h}$). (B) Dependence of potassium ($E_{K}$) and leak ($E_{L⁢e⁢a⁢k}$) reversal potentials on $K_{b⁢a⁢t⁢h}$. Black dots indicate experimentally measured values for $E_{K}$ and $E_{L⁢e⁢a⁢k}$ from Koizumi and Smith, 2008. (C) Dependence of intrinsic cellular dynamics on $K_{b⁢a⁢t⁢h}$, $g_{L⁢e⁢a⁢k}$, and $g_{N⁢a⁢P}$. Black curve represents the relationship between $K_{B⁢a⁢t⁢h}$ and $g_{L⁢e⁢a⁢k}$ used in the full preBötC network. (D) Schematic diagram of size and connectivity probabilities of the rhythm- and pattern-generating populations within the preBötC model. (E) 2D plot between $g_{N⁢a⁢P}$ and $g_{L⁢e⁢a⁢k}$ showing the location of the intrinsic bursting regime for varied concentrations of $K_{B⁢a⁢t⁢h}$. The distributions of neuronal conductances in the rhythm- and the pattern-generating populations are indicated by the blue dots and red squares, respectively.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Dependence of intrinsic cellular dynamics and the number of spikes per burst on $K_{b⁢a⁢t⁢h}$ and $g_{L⁢e⁢a⁢k}$.For these simulations, $g_{NaP}=5.0nS$.

To construct a model preBötC network, we linked rhythm- and pattern-generating subpopulations via excitatory synaptic connections within and between the two populations (Figure 3D). We distinguished the two populations by endowing them with distinct distributions of persistent sodium current conductance ($g_{N⁢a⁢P}$), as documented experimentally (Del Negro et al., 2002a; Koizumi and Smith, 2008). In both populations, we maintained the dependence of $g_{L⁢e⁢a⁢k}$ on $K_{b⁢a⁢t⁢h}$ (see Figure 3C and E).

For the full preBötC network model, we first characterized the impact of changes in $K_{b⁢a⁢t⁢h}$ on network behavior without calcium dynamics by setting $P_{S⁢y⁢n⁢C⁢a}=0$. This network condition is analogous to in vitro preparations where all Ca2+ currents are blocked by Cd2+ and the preBötC can only generate burstlets (Kam et al., 2013a; Sun et al., 2019). Not surprisingly, with calcium dynamics blocked, we found that the network can only generate small amplitude network oscillations (burstlets) that first emerge at approximately $K_{bath}=5mM$ (Figure 4A). Moreover, under these conditions, increasing $K_{b⁢a⁢t⁢h}$ results in an increase in the burstlet frequency and amplitude (Figure 4B and C), which is consistent with experimental observations (Kallurkar et al., 2020).

![Figure 4.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig4-v2.jpg)

**Figure 4.:** (A) Rhythmogenic output of the simulated network without calcium dynamics ($P_{S⁢y⁢n⁢C⁢a}=0$) as a function of $K_{B⁢a⁢t⁢h}$. These oscillations are considered burstlets as they are incapable of recruiting the pattern-generating population without calcium dynamics. (B) Frequency and (C) amplitude of the burstlet oscillations as a function of $K_{b⁢a⁢t⁢h}$. (D–F) 2D plots characterizing the (D) burstlet fraction, (E) the burst frequency, and (F) the burst amplitude as a function of $K_{b⁢a⁢t⁢h}$ and $P_{S⁢y⁢n⁢C⁢a}$ (note that the $P_{S⁢y⁢n⁢C⁢a}$ range shown does not start at 0). (G1–G4) Example traces illustrating a range of possible burstlet fractions generated by the network. Burstlets are indicated by asterisks. (H) Overlay of the average population voltage during bursts and burstlets. The hypoglossal output is calculated by passing the mean population amplitude through a sigmoid function $f=-60.5+60/[1+e^{-(x+45)/2.5}]$. (I) Burstlet fraction as a function of $K_{b⁢a⁢t⁢h}$ for the four example traces indicated in panels (G1–G4). Figure 4I has been adapted from Figure 1B from Kallurkar et al., 2020.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Example traces of the imposed burstlet rhythm where $P_{S⁢y⁢n⁢C⁢a}=0$ so that the pattern-generating population is not recruited. (B) Dependence of the burstlet amplitude on frequency. The burstlet frequency range and doubling of the burstlet amplitude were chosen to qualitatively match the effects of changing $K_{b⁢a⁢t⁢h}$ on burstlet properties characterized in Kallurkar et al., 2020. (C, D) 2D plots characterizing the (C) burstlet fraction and (D) the burst frequency as a function of the burstlet frequency and $P_{S⁢y⁢n⁢C⁢a}$ (note that the $P_{S⁢y⁢n⁢C⁢a}$ range shown does not start at 0). (E1–E4) Example traces illustrating a range of possible burstlet fractions generated by the network. Burstlets are indicated by asterisks. The imposed burstlet rhythm was generated by imposing a Poisson spike train in each neuron within the rhythmogenic population where the frequency was zero during the interburst interval. At the start of the burstlet, the frequency linearly ramps up over 250 ms to an imposed maximum firing rate and then linearly ramps back down to zero over an additional 250 mS. The burstlet frequency and amplitude were controlled by changing the interburst interval and the maximum firing rate, respectively.

In the full network with calcium dynamics ($P_{SynCa}>0$), burstlets generated by the rhythmogenic subpopulation will trigger postsynaptic calcium transients in the pattern-generating subpopulation. Therefore, in this set of simulations the burstlet activity of the rhythm generating population plays an analogous role to the square wave Ca2+ current in Figure 1 and to bursts of the intrinsically rhythmic neuron in Figure 2. Hence, we characterized the burstlet fraction, burst frequency, and burst amplitude – with a burst defined as an event in which a burstlet from the rhythm generating population recruits a burst in the pattern-generating population – in the full preBötC model network as a function of $K_{b⁢a⁢t⁢h}$ and $P_{S⁢y⁢n⁢C⁢a}$ (Figure 4D–F). In this case, the frequency of the postsynaptic Ca2+ oscillation is controlled by $K_{b⁢a⁢t⁢h}$ (Figure 4B). However, because $K_{b⁢a⁢t⁢h}$ also affects burstlet amplitude (Figure 4C), the postsynaptic Ca2+ amplitude is determined by both $K_{b⁢a⁢t⁢h}$ and $P_{S⁢y⁢n⁢C⁢a}$. If $K_{b⁢a⁢t⁢h}$ is held fixed, then modulating $P_{S⁢y⁢n⁢C⁢a}$ will only affect the amplitude of the postsynaptic Ca2+ transient since burstlet amplitude will not be impacted. The effects of selectively changing the postsynaptic Ca2+ amplitude on the full network can thus be extracted by considering a vertical slice through Figure 4E–F. Note that in the simulations that we show here burstlet generation arises from a mechanism based on $I_{N⁢a⁢P}$; however, we obtain similar network results if we impose burstlet activity on the burstlet subpopulation and maintain the coupling between populations and Ca2+ dynamics for burst recruitment (Figure 4—figure supplement 1).

We found that increasing $P_{S⁢y⁢n⁢C⁢a}$ or $K_{b⁢a⁢t⁢h}$ generally decreases the burstlet fraction, increases burst frequency, and slightly increases the burst amplitude (Figure 4D–F and G1–G). The decrease in the burstlet fraction with increasing $K_{b⁢a⁢t⁢h}$ or $P_{S⁢y⁢n⁢C⁢a}$ is caused by the increase in the burstlet amplitude (Figure 4C) or in Ca2+ influx with each burstlet, respectively, both of which increase the Ca2+ transient in the pattern-generating subpopulation. The increase in burst frequency with increases in $K_{b⁢a⁢t⁢h}$ or $P_{S⁢y⁢n⁢C⁢a}$ is due to the decreased burstlet fraction (i.e., the burstlet to burst transitions occur on a greater proportion of cycles) and, in the case of $K_{b⁢a⁢t⁢h}$, by an increase in the burstlet frequency (Figure 4B). The slight increase in burst amplitude with increasing $K_{b⁢a⁢t⁢h}$ is largely due to the increase in the burstlet amplitude (Figure 4C). Figure 4H highlights the relative shape of burstlets and bursts as well as the delay between burstlet generation and recruitment of the pattern-generating population and simulated hypoglossal output, which agrees qualitatively with experimental observations (Kallurkar et al., 2020). Experimentally, it is likely that postsynaptic Ca2+ transients will increase with increasing $K_{b⁢a⁢t⁢h}$ due to the change in the resting $V_{m}$ in nonrhythmic preBötC neurons (Tryba et al., 2003) relative to the voltage-gated activation dynamics of postsynaptic calcium channels (Elsen and Ramirez, 1998); see ‘Discussion’ for a full analysis of this point. Interestingly, in our simulations, increasing $P_{S⁢y⁢n⁢C⁢a}$ (i.e., the amplitude of the postsynaptic calcium transients) with $K_{b⁢a⁢t⁢h}$ (Figure 4 traces G1–G4) generated $K_{b⁢a⁢t⁢h}$-dependent changes in the burstlet fraction that are consistent with experimental observations (Kallurkar et al., 2020; see Figure 4I).

Note that our model includes synaptic connections from pattern-generating neurons back to rhythm-generating neurons. These connections prolong activity of rhythmic neurons in bursts, relative to burstlets, which in turn yields a longer pause before the next event (e.g., Figure 4G1). This effect can constrain event frequencies somewhat in the fully coupled network relative to the feedforward case (e.g., frequencies in Figure 4B exceed those in Figure 4E for comparable $K_{b⁢a⁢t⁢h}$ levels).

### Calcium and IC⁢A⁢N block have distinct effects on the burstlet fraction

Next, we further characterized the calcium dependence of the burstlet to burst transition in our model by simulating calcium blockade or $I_{C⁢A⁢N}$ blockade by a progressive reduction of $P_{S⁢y⁢n⁢C⁢a}$ or $g_{C⁢A⁢N}$, respectively. We found that complete block of synaptically triggered Ca2+ transients or $I_{C⁢A⁢N}$ block eliminates bursting without affecting the underlying burstlet rhythm (Figure 5A and B). Interestingly, progressive blockades of each of these two mechanisms have distinct effects on the burstlet fraction: blocking postsynaptic Ca2+ transients increases the burstlet fraction by increasing the number of burstlets required to trigger a network burst, whereas $I_{C⁢A⁢N}$ block only slightly increases the burstlet fraction (Figure 5C). In both cases, however, progressive blockade smoothly decreases the amplitude of network bursts (Figure 5D). The decrease in amplitude in the case of $I_{C⁢A⁢N}$ block is due to derecruitment of neurons from the pattern-forming subpopulation and a decrease in the firing rate of the neurons that remain active, whereas in the case of Ca2+ block the decrease in amplitude results primarily from derecruitment (Figure 5E and F). These simulations provide mechanism-specific predictions that can be experimentally tested.

![Figure 5.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig5-v2.jpg)

**Figure 5.:** Network traces showing the effect of (A) calcium current blockade ($P_{S⁢y⁢n⁢C⁢a}$ reduction) and (B) CAN current blockade ($g_{C⁢A⁢N}$ reduction) on the period and amplitude of bursts. Effects of calcium or $I_{C⁢A⁢N}$ blockade on (C) the burstlet fraction, (D) the amplitude of bursts and (E) the number of recruited and (F) peak firing rate of recruited neurons in pattern-generating subpopulation during network bursts as a function of the blockade percentage.

### Dose-dependent effects of opioids on the burstlet fraction

Recent experimental results by Baertsch et al., 2021 showed that opioid application locally within the preBötC decreases burst frequency but also increases the burstlet fraction. In the preBötC, opioids affect neuronal dynamics by binding to the μ-opioid receptor (μOR). The exact number of preBötC neurons expressing μOR is unclear; however, the number appears to be small, with estimates ranging from 8% to 50% (Bachmutsky et al., 2020; Baertsch et al., 2021; Kallurkar et al., 2021). Additionally, μOR is likely to be selectively expressed on neurons involved in rhythm generation, given that opioid application in the preBötC primarily impacts burst frequency rather than amplitude (Sun et al., 2019; Baertsch et al., 2021). Importantly, within the preBötC, opioids ultimately impact network dynamics through two distinct mechanisms: (1) hyperpolarization, presumably via activation of a G protein-gated inwardly rectifying potassium leak (GIRK) current (Kubo et al., 1993; Gray et al., 1999; Montandon et al., 2016), and (2) decreased excitatory synaptic transmission, presumably via decreased presynaptic release (Ballanyi et al., 2009; Wei and Ramirez, 2019; Baertsch et al., 2021).

Taking these considerations into account, we tested if our model could explain the experimental observations. Specifically, we simulated opioids as having a direct impact only on the neurons within the rhythmogenic population and their synaptic outputs (Figure 6A). To understand how preBötC network dynamics are impacted by the two mechanisms through which opioids have been shown to act, we ran separate simulations featuring either activation of GIRK channels or block of the synaptic output from the rhythmogenic subpopulation (Figure 6B–F). We found that both GIRK activation and synaptic block reduced the burst frequency (Figure 6D) and slightly increased burst amplitude (Figure 6E). The decreased frequency with synaptic block comes from an increase in the burstlet fraction, whereas GIRK activation kept the burstlet fraction constant while reducing the burstlet frequency (Figure 6F). Finally, combining these effects, we observed that simultaneously increasing the GIRK channel conductance and blocking the synaptic output of μOR-expressing neurons in our simulations generates slowing of the burst frequency and an increase in the burstlet fraction consistent with in vitro experimental data (Figure 6D–G).

![Figure 6.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig6-v2.jpg)

**Figure 6.:** (A) Schematic preBötC network diagram showing the location of μOR. Example traces showing the effect of progressive (from top to bottom) (B) $g_{GIRK}$ channel activation and (C) synaptic block on the network output. Quantification of $g_{GIRK}$ activation or synaptic block by μOR on the (D) burst frequency, (E) burst amplitude, and (F) burstlet fraction. Error bars indicate SD. (G) Example traces showing the effects of progressive increases in $g_{GIRK}$ and synaptic block on network output. Burstlets are indicated by blue asterisks. The parameters for each case are as follows: (BL) $g_{GIRK}=0.0nS$, $\gamma_{\muOR}=0.0$; (1) $g_{GIRK}=0.031034nS$, $\gamma_{\muOR}=0.81034$; (2) $g_{GIRK}=0.093103nS$, $\gamma_{\muOR}=0.7069$; (3) $g_{GIRK}=0.14483nS$, $\gamma_{\muOR}=0.68966$; (4) $g_{GIRK}=0.19655nS$, $\gamma_{\muOR}=0.58621$. Comparison of experimental data and the effects of progressive increases in $g_{G⁢I⁢R⁢K}$ and synaptic block on the (H) frequency and (I) amplitude of bursts as well as (J) the burstlet fractions for the traces shown in (G). Figure 6H and J have been adapted from Figure 3C and E from Baertsch et al., 2021. The effects of DAMGO on burst amplitude were not quantified in Baertsch et al., 2021.

### Simultaneous stimulation of subsets of preBötC neurons elicits network bursts with long delays

Simultaneous stimulation of 4–9 preBötC neurons in in vitro slice preparations has been shown to be sufficient to elicit network bursts with similar patterns to those generated endogenously (Kam et al., 2013b). These elicited bursts occur with delays of several hundred milliseconds relative to the stimulation time, which is longer than would be expected from existing models. Interestingly, in the current model, due to the dynamics of CICR, there is a natural delay between the onset of burstlets and the recruitment of the follower population that underlies the transition to a burst. Therefore, we investigated whether our model could match and explain the observations seen in Kam et al., 2013b.

In our model, we first calibrated our stimulation to induce a pattern of spiking that is comparable to the patterns generated in Kam et al., 2013b (10–15 spikes with decrementing frequency, Figure 7A). We found that stimulation of 3–9 randomly selected neurons could elicit network bursts with delays on the order of hundreds of milliseconds (Figure 7B and C). Next, we characterized (1) the probability of eliciting a burst, (2) the delay in the onset of elicited bursts, and (3) the variability in delay, each as a function of the time of stimulation relative to the end of an endogenous burst (i.e., a burst that occurs without stimulation) and of the number of neurons stimulated (Figure 7D–F). In general, we found that increasing the number of stimulated neurons increases the probability of eliciting a burst and decreases the delay between stimulation and burst onset. Moreover, the probability of eliciting a burst increases and the delay decreases as the time after an endogenous burst increases (Figure 7G and H). Additionally, with its baseline parameter tuning, our model had a refractory period of approximately 1 s following an endogenous burst during which stimulation could not evoke a burst (Figure 7). The refractory period in our model is longer than measured experimentally (500 ms) (Kam et al., 2013b).

![Figure 7.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig7-v2.jpg)

**Figure 7.:** (A) Raster plot of neuronal spiking triggered by simulated holographic stimulation of six preBötC neurons shortly after an endogenous burst and resulting failure to evoke a network burst. Black line represents the integrated population activity. Scale bar indicates 20 spikes/s/N. Bottom panel shows the spiking activity triggered in individual neurons by the simulated holographic stimulation. Panel duration is 1 s. (B) Example simulation where stimulation of nine preBötC neurons evokes a network burst. Gray curve indicates timing of the next network burst if the network was not stimulated. (Bottom panel) Expanded view of the percolation process that is triggered by holographic stimulation on a successful trial. Panel duration is 1.75 s. (C) Example traces showing the delay between the stimulation time and the evoked bursts as a function of the number of neurons stimulated for the (top) integrated preBötC spiking and (bottom) simulated hypoglossal activity. (D–F) Characterization of (D) the probability of evoking a burst, (E) the mean delay of evoked bursts, and (F) the standard deviation of the delay as a function of the time after an endogenous burst and the number of neurons stimulated. (G) Probability and (H) delay as a function of the stimulation time for stimulation of three, six, or nine neurons. Error bars in (H) indicate SD. (I) Histogram of evoked and endogenous bursts relative to the time of stimulation ($t=0s)$ for all successful trials in all simulations; notice a 1 s refractory period.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Dynamics of $I_{N⁢a⁢P}$ inactivation ($h_{N⁢a⁢P}$), endoplasmic reticulum (ER) calcium concentration ($[C⁢a]_{E⁢R}$), and synaptic depression and recovery ($D$) as a function of time relative to the inspiratory cycle.The values of $h_{N⁢a⁢P}$, $[C⁢a]_{E⁢R}$ and $D$ are normalized to their values at the start of the burst.

To determine the mechanisms involved in the refractoriness, we plotted the time courses of key slow variables in the model, namely, persistent sodium inactivation $h_{N⁢a⁢P}$, ER calcium ($[C⁢a]_{E⁢R}$), and synaptic depression $D$, over one burst cycle in the absence of stimulation (see Figure 7—figure supplement 1). We found that the recovery from synaptic depression and the deinactivation of $h_{N⁢a⁢P}$ were the two slow processes with time courses that aligned with the loss of refractoriness. Thus, in our model, it appears that these two factors are crucial to the probability that a stimulus will elicit a sustained response, while calcium-related effects predominantly relate to the recruitment process by which such a response develops into a burst.

To conclude our investigation, we examined how changes in the connection probability within the pattern-forming population ($P_{P⁢P}$) affect the refractory period, probability, and delay of evoked bursts following simultaneous stimulation of 3–9 randomly selected neurons in the preBötC population. We focused on the pattern-forming population because it comprises 75% of the preBötC population, and, therefore, neurons from this population are most likely to be stimulated and the synaptic projections from these neurons are most likely to impact the properties of evoked bursts. To avoid a confound that would arise if increased connection probability led to overall stronger synaptic input, we adjusted $W_{P⁢P}$ to compensate for changes in $P_{P⁢P}$ and keep the network synaptic strength, defined as $S=N_{P}⋅P_{P⁢P}⋅W_{P⁢P}$, at a constant value.

With this scaling, we found that decreasing/increasing $P_{P⁢P}$ decreased/increased the refractory period (Figure 8A–C) by impacting the probability of eliciting a burst in the period immediately after an endogenous burst (Figure 8D and E). More specifically, the change in the probability of evoking a burst, with decreased/increased $P_{P⁢P}$, is indicated by a leftward/rightward shift in the probability vs. stimulation time curves relative to a control level of $P_{P⁢P}$ ($P_{P⁢P}=2%$) (see Figure 8D and E). That is, relatively small connection probabilities with large connection strengths lead to network dynamics with a shorter refractory period when stimulation cannot elicit a burst and a higher probability that a stimulation at a fixed time since the last burst will evoke a new burst.

![Figure 8.](https://cdn.elifesciences.org/articles/75713/elife-75713-fig8-v2.jpg)

**Figure 8.:** (A–C) Histogram of evoked and endogenous bursts relative to the time of stimulation ($t=0s)$ for all successful trials where three, six, and nine neurons were stimulated and for different connection probabilities (but fixed total network synaptic strength; i.e., $N_{P}⋅P_{P⁢P}⋅W_{P⁢P}=c⁢o⁢n⁢s⁢t⁢a⁢n⁢t$) in the follower population: (A) $P_{P⁢P}=1%$; (B) $P_{P⁢P}=2%$; and (C) $P_{P⁢P}=4%$. (D, E) Effect of (D) decreasing ($2%→1%$) and (E) increasing ($2%→4%$) the connection probability in the follower population, $P_{P⁢P}$. (F) Refractory period and delay from stimulation to burst as functions of the connection probability for the simulations shown in (A–E), still with $N_{P}⋅P_{P⁢P}⋅W_{P⁢P}=c⁢o⁢n⁢s⁢t⁢a⁢n⁢t$. Error bars indicate SD. Notice that the refractory period increases with increasing connection probability. (G) Effect of $P_{P⁢P}$ on the delay to evoked bursts. (H) Probability of evoking a burst as a function of time of stimulation delivery (colorbar) and the number out of nine stimulated neurons that are follower neurons for the baseline case of 2% connection probability.

It may seem surprising that networks with smaller connection probabilities exhibit a faster emergence of bursting despite their larger connection weights since intuitively, with lower connection probabilities, fewer neurons could be recruited by each action potential, resulting in longer, more time-consuming activation pathways. A key point, however, is that when connection weights are larger, fewer temporally overlapping inputs are needed to recruit each inactive neuron. For example, suppose that we fix $N_{P}$ and $W_{P⁢P}$, and we take $P_{P⁢P}$ to scale as $1/N_{P}$. The minimal number of inputs from active neurons needed to activate an inactive neuron depends on the synaptic weight, $W_{P⁢P}$. Let $r$ denote this number for the specific value of $W_{P⁢P}$ that we have selected. We can approximate the expected number of neurons receiving $r$ or more inputs from $A$ active neurons by computing the expected number receiving exactly $r$ inputs, which we denote as $[I_{r}]$, where the brackets indicate an expectation or average. For a network with a random connectivity profile, this expected value is computed from the binomial formula as

$$
[I_{r}]=(Ar)(\frac{1}{N_{P}})^{r}(1−\frac{1}{N_{P}})^{A−r}.
$$

Suppose that next we consider another network in which we double $P_{P⁢P}$ and halve $W_{P⁢P}$, thus keeping their product constant. For this smaller $W_{P⁢P}$, more inputs will be needed to activate an inactive neuron. Specifically, assume that now at least $2⁢r$ inputs are needed for activation. The expected number of neurons receiving $2⁢r$ inputs, $[I_{2⁢r}]$, is given by

$$
[I_{2r}]=(A2r)(\frac{2}{N_{P}})^{2r}(1−\frac{2}{N_{P}})^{A−2r}.
$$

An elementary calculation shows that $[I_{2r}]<[I_{r}]$ for relevant parameter values (such as $N_{P}=300$ and small $r$ as indicated by the stimulation experiments). Thus, increasing $P_{P⁢P}$ and proportionally scaling down $W_{P⁢P}$ reduces the chance of successful recruitment of inactive neurons by active neurons.

Interestingly, our simulations suggest that the connection probability in the pattern-generating population must be between 1% and 2% to match the approximately 500 ms refractory period measured experimentally (Kam et al., 2013b; Figure 8F). Surprisingly, the mean and distribution of delays from stimulation to burst for all successfully elicited bursts are not strongly affected by changes in $P_{P⁢P}$ (Figure 8F). For a given stimulation time and number of neurons stimulated, however, decreasing $P_{P⁢P}$ decreases the delay of elicited bursts (Figure 8G). Finally, because the neurons in the pattern-generating population appear to play a dominant role in determining if stimulation will elicit a network burst, we characterized how the number of pattern-generating neurons stimulated, out of a total set of nine stimulated neurons, affects the probability of eliciting a network burst as a function of stimulation time (Figure 8H). These simulations were carried out under a baseline condition of $P_{P⁢P}=2%$. In general, we found that stimulating a relatively larger proportion of pattern-generating neurons increased the probability of eliciting a network burst for all times after the approximately 1 s refractory period, as indicated by the positive slope in Figure 8H. Additionally, eliciting a network burst does not require stimulation of rhythmogenic neurons.

## Discussion

Recent experiments have revealed a decoupling of respiratory rhythm generation and output patterning in the preBötC, which has given rise to the conceptual framework of burstlet theory. To date, however, this theory lacks the quantitative basis, grounded in underlying biophysical mechanisms, needed for its objective evaluation. To address this critical gap, in this computational study we developed a data-constrained biophysical model of the preBötC that generates burstlets and bursts as proposed by burstlet theory, with a range of features that match experimental observations. To summarize, we first show that CICR from intracellular stores is a natural mechanism to periodically amplify postsynaptic calcium transients needed for $I_{C⁢A⁢N}$ activation and recruitment of pattern-forming neurons into network bursts (Figure 1). Next, we demonstrate that in a two-neuron network CICR can convert baseline rhythmic activity into a mixture of bursts and burstlets, where the burstlet fraction depends largely on the magnitude of postsynaptic calcium transients (Figure 2). In a larger preBötC network containing rhythm- and pattern-forming subpopulations with experimentally constrained intrinsic properties, population sizes, and synaptic connectivity probabilities (Figure 3), similar but more realistic activity patterns arise (Figure 4). Moreover, we show that this model can match a wide range of the key experimental underpinnings of burstlet theory: dependence of the burstlet fraction on extracellular potassium concentration (Figure 4I), the Ca2+ dependence of the burstlet-to-burst transition (Figure 5), the effects of opioids on burst frequency and burstlet fraction (Figure 6), and the long delay and refractory period of bursts evoked by holographic photostimulation of small subsets of preBötC neurons (Figures 7 and 8).

### Insights into the mechanisms of burst (pattern) and burstlet (rhythm) generation within the inspiratory preBötC

Burstlet theory to date has largely been an empirical description of the observed features of bursts and burstlets. One idea that has been suggested is that rhythm generation is driven by a stochastic percolation process in which tonic spiking across the rhythm-generating population gradually synchronizes during the inter-burst-interval to generate the burstlet rhythm. Subsequently, a burst (i.e., motor output) only occurs if the burstlet is of sufficient magnitude, resulting from sufficient synchrony, to trigger all-or-none recruitment of the pattern-forming subpopulation (Kam et al., 2013a; Kam et al., 2013b; Feldman and Kam, 2015; Cui et al., 2016; Kallurkar et al., 2020; Ashhad and Feldman, 2020). This theory, however, does not identify or propose specific biophysical mechanisms capable of generating a quantitative explanation of the underlying cellular and network-level dynamics, fails to capture the Ca2+ dependence of the burst-to-burstlet transition, and cannot explain how extracellular potassium concentration impacts the burstlet fraction. Our simulations support an alternative view of the recruitment process associated with this transition that builds directly from previous computational studies (Jasinski et al., 2013; Phillips et al., 2019a; Phillips and Rubin, 2019b; Phillips et al., 2021), which robustly reproduce a wide array of experimental observations. Specifically, in this study we show that amplification of postsynaptic calcium transients in the pattern-generating subpopulation (triggered by burstlets) provides a natural mechanism capable of explaining the Ca2+ dependence of the burstlet-to-burst transition.

Importantly, our model yields the result, and hence the prediction, that the burstlet fraction is determined by the probability that a burstlet will trigger CICR in the pattern-forming subpopulation. In the model, this probability is determined by the magnitude of postsynaptic calcium transients as well as the activation dynamics of the IP3 receptor and the SERCA pump. Therefore, to explain the decrease in the burstlet fraction with increasing extracellular $K_{b⁢a⁢t⁢h}$, the magnitude of the burstlet-triggered postsynaptic calcium transients must increase with $K_{b⁢a⁢t⁢h}$. Some of this rise can result directly from the increase in burstlet amplitude with increasing $K_{b⁢a⁢t⁢h}$ (see Kallurkar et al., 2020 and Figure 4C). To fully match the experimentally observed relationship between $K_{b⁢a⁢t⁢h}$ and the burstlet fraction (Figure 4J), we also explicitly increased the parameter $P_{S⁢y⁢n⁢C⁢a}$, which sets the proportion of the postsynaptic calcium current carried by Ca2+. Thus, our model predicts that the magnitude of postsynaptic Ca2+ transients triggered by EPSPs should increase as $K_{b⁢a⁢t⁢h}$ is elevated.

This same prediction arises from considering the voltage-dependent properties of Ca2+ channels characterized in preBötC neurons and the changes in the membrane potential of non-rhythmogenic (i.e., pattern-forming) neurons as a function of $K_{b⁢a⁢t⁢h}$. Specifically, it is likely that voltage-gated calcium channels are involved in generating the postsynaptic Ca2+ transients as dendritic Ca2+ transients have been shown to precede inspiratory bursts and to be sensitive to Cd2+, a calcium channel blocker (Del Negro et al., 2011). Consistent with this idea, Cd2+-sensitive Ca2+ channels in preBötC neurons appear to be primarily localized in distal dendritic compartments (Phillips et al., 2018). Voltage-gated calcium channels in the preBötC start to activate at approximately $−65mV$(Elsen and Ramirez, 1998), and importantly, the mean somatic resting membrane potential of non-rhythmogenic preBötC neurons increases from $−67.034mV$ to $−61.78mV$ when extracellular potassium concentration is elevated from $3mM$ to $8mM$ (Tryba et al., 2003). Moreover, at $K_{bath}=9mM$, EPSPs in the preBötC are on the order of 2–5 mV (Kottick and Del Negro, 2015; Morgado-Valle et al., 2015; Baertsch et al., 2021) and the amplitude of EPSCs has been shown to decrease as $K_{b⁢a⁢t⁢h}$ is lowered (Okada et al., 2005). Putting together these data on resting membrane potential, EPSP sizes, and voltage-dependent activation of Ca2+ channels, we deduce that when $K_{bath}=3mM$, the magnitude of EPSPs may not reach voltages sufficient for significant activation of voltage-gated Ca2+ channels. As $K_{b⁢a⁢t⁢h}$ is increased, however, both EPSC magnitudes and the membrane potential of pattern-forming neurons increase. Therefore, with increased $K_{b⁢a⁢t⁢h}$, the prediction is that EPSCs will result in greater activation of voltage-gated Ca2+ channels and increased postsynaptic calcium transients. This effect is captured in the model by an increase in the parameter $P_{S⁢y⁢n⁢C⁢a}$, which determines the percentage of the postsynaptic current carried by Ca2+ ions, with $K_{b⁢a⁢t⁢h}$.

The idea that dendritic postsynaptic Ca2+ transients and $I_{C⁢A⁢N}$ activation play a critical role in regulating the pattern of preBötC dynamics is well supported by experimental and computational studies. Specifically, the dendritic Ca2+ transients that precede inspiratory bursts (Del Negro et al., 2011) have been shown to travel in a wave to the soma, where they activate TRPM4 currents ($I_{C⁢A⁢N}$) (Mironov, 2008). Moreover, the rhythmic depolarization of otherwise non-rhythmogenic neurons (inspiratory drive potential) depends on $I_{C⁢A⁢N}$ (Pace et al., 2007a), while the inspiratory drive potential is not dependent on Ca2+ transients driven by voltage-gated calcium channels expressed in the soma (Morgado-Valle et al., 2008). Finally, pharmacological blockade of TRPM4 channels, thought to represent the molecular correlates of $I_{C⁢A⁢N}$, reduces the amplitude of preBötC motor output without impacting the rhythm (Koizumi et al., 2018; Picardo et al., 2019). These experimental findings were incorporated into and robustly reproduced in a recent computational model (Phillips et al., 2019a) and are reproduced here (see Figure 5B and D). Consistent with these findings, this previous model suggests that rhythm generation arises from a small subset of preBötC neurons, which form an $I_{N⁢a⁢P}$-dependent rhythmogenic kernel (i.e., burstlet rhythm generator), and that rhythmic synaptic drive from these neurons triggers postsynaptic calcium transients, $I_{C⁢A⁢N}$ activation, and amplification of the inspiratory drive potential, which spurs bursting in the rest of the network. This study builds on this previous model by explicitly defining rhythm- and pattern-generating neuronal subpopulations (see Figure 3) and incorporating the mechanisms required for CICR and intermittent amplification of postsynaptic calcium transients.

CICR mediated by the SERCA pump and the IP3 receptor has long been suspected to be involved in the dynamics of preBötC rhythm and/or pattern generation (Pace et al., 2007a; Crowder et al., 2007; Mironov, 2008; Toporikova et al., 2015) and has been explored in individual neurons and network models of the preBötC (Toporikova and Butera, 2011; Jasinski et al., 2013; Rubin et al., 2009; Wang and Rubin, 2020). Experimental studies have not clearly established the role of CICR from ER stores in respiratory circuits, however. For example, Mironov, 2008 showed that application of 1 µM thapsigargin, a SERCA pump inhibitor, abolished rhythmic activity and blocked calcium transients that travel in a wave from the dendrites to the soma. In a separate study, however, block of the SERCA pump by bath application of thapsigargin (2–20 µM) or cyclopiazonic acid (CPA) (30–50 µM) did not significantly affect the amplitude or frequency of hypoglossal motor output in in vitro slice preparations containing the preBötC (Beltran-Parrazal et al., 2012). The explanation for these seemingly contradictory experimental results is unclear, especially since effects of SERCA pump block could be complicated, and will need to be investigated by future studies. It is possible that the role of CICR may be dynamically regulated depending on the state of the preBötC network. For example, the calcium concentration at which the IP3 receptor is activated is dynamically regulated by IP3 (Kaftan et al., 1997), and therefore, activity- or neuromodulatory-dependent changes in the cytoplasmic Ca2+ and/or IP3 concentration may impact ER Ca2+ uptake and release dynamics. Store-operated Ca2+ dynamics are also affected by the transient receptor potential canonical 3 (TRPC3) channels (Salido et al., 2009), which are expressed in the preBötC, and manipulation of TRPC3 has been shown to impact burst amplitude and regularity (Tryba et al., 2003; Koizumi et al., 2018) as would be predicted by this model. It is also possible that calcium release is mediated by the ryanodine receptor, an additional calcium-activated channel located in the ER membrane (Lanner et al., 2010), since bath application of CPA (100 µM) and ryanodine (10 µM) removed large-amplitude oscillations in recordings of preBötC population activity (Toporikova et al., 2015).

Finally, we note that while various markers can be used to define distinct subpopulations of neurons within the preBötC, our model cannot determine which of these ensembles are responsible for rhythm and pattern generation. Past experiments have examined the impact of optogenetic inhibition, applied at various intensities to subpopulations associated with specific markers, on the frequency of inspiratory neural activity, but this activity was measured by motor output, not within the preBötC itself (Tan et al., 2008; Cui et al., 2016; Koizumi et al., 2016). According to burstlet theory and our model, slowed output rhythmicity could derive from inhibition of rhythm-generating neurons, due to a reduced frequency of burstlets, and from inhibition of pattern-generating neurons, due to a reduced success rate of burst recruitment. Thus, measurements within the preBötC will be needed in order to assess the mapping between subpopulations of preBötC neurons and roles in burstlet and burst production.

### Additional comparisons to experimental results

In our model (Figure 4), a burstlet rhythm first emerges at a $K_{b⁢a⁢t⁢h}$ of approximately 5 mM, whereas in the experiments of Kallurkar et al., 2020, the burstlet rhythm continues even down to 3 mM. To explain this discrepancy, we note that our model assumes that the extracellular potassium concentration throughout the network is equal to $K_{b⁢a⁢t⁢h}$. Respiratory circuits appear to have some buffering capacity, however, such that for $K_{b⁢a⁢t⁢h}$ concentrations below approximately 5 mM the extracellular K+ concentration remains elevated above $K_{b⁢a⁢t⁢h}$ (Okada et al., 2005). The $K_{b⁢a⁢t⁢h}$ range over which our model generates a rhythm would extend to that seen experimentally if extracellular K+ buffering were accounted for. This buffering effect can also explain why the burstlet fraction remains constant in experimental studies when $K_{b⁢a⁢t⁢h}$ is lowered from 5 mM to 3 mM (Kallurkar et al., 2020). Our model also does not incorporate short-term extracellular potassium dynamics that depend on $K_{b⁢a⁢t⁢h}$ and may impact the ramping shape of burstlet onset (Abdulla et al., 2021). Importantly, over the range of $K_{b⁢a⁢t⁢h}$ values relevant both to experiments and our model, we find clear agreement on the dependence of burstlet fraction on $K_{b⁢a⁢t⁢h}$ (Figure 4I).

Although our model incorporates various key biological features, it does not include some of the biophysical mechanisms that are known to shape preBötC patterned output or that are hypothesized to contribute to the properties described by burstlet theory. For example, the M-current associated with KCNQ potassium channels has been shown to impact burst duration by contributing to burst termination (Revill et al., 2021). Additionally, intrinsic conductances associated with a hyperpolarization-activated mixed cation current ($I_{h}$) and a transient potassium current ($I_{A}$) are hypothesized to be selectively expressed in the pattern- and rhythm-generating preBötC subpopulations (Picardo et al., 2013; Phillips et al., 2018). Thus, our model predicts that while these currents may impact quantitative properties of burstlets and bursts, they are not critical for the presence of burstlets and their transformation into bursts. The current model also does not include a population of inhibitory preBötC neurons. Inhibition is involved in regulating burst amplitude (Baertsch et al., 2018), but it does not have a clear role in burst or burstlet generation, and therefore inhibition was omitted from this work. More globally, it is crucial to recognize that areas outside of the preBötC impact dynamics within the preBötC. These effects, which remain to be fully elucidated, may range from ongoing modulation of the level of excitability of preBötC neurons to timed signaling that contributes to preBötC rhythmicity and patterning (e.g., Mulkey et al., 2004; Dutschmann and Dick, 2012; Phillips et al., 2012; Smith et al., 2013; Dhingra et al., 2019; Richter et al., 2019; Liu et al., 2022). For example, transection studies suggest that pontine regions may make crucial contributions to respiratory circuit excitability and respiratory pattern formation (Jones and Dutschmann, 2016; Smith et al., 2007). Finally, the data on which this study was based comes from a variety of settings, including in vitro and other reduced preparations, and additional factors no doubt complicate the generation and control of respiratory outputs in vivo. Indeed, although experimental results suggest that manipulations to enhance preBötC excitability in slice preparations do not appear to significantly impact the mechanisms of preBötC rhythmicity or the generation of bursts and burstlets, additional investigation of how higher brainstem centers impact preBötC inspiratory rhythm and pattern generation is an important direction for future studies.

Importantly, our model does robustly reproduce all of the range of key experimental observations underlying burstlet theory. Not surprisingly, block of calcium transients or $I_{C⁢A⁢N}$ in our model eliminates bursts without affecting the underlying rhythm (Figure 5), which is consistent with experimental observations (Kam et al., 2013b; Sun et al., 2019). Interestingly, our model also provides the experimentally testable predictions that blocking calcium transients will increase the burstlet fraction while $I_{C⁢A⁢N}$ block will have no effect on this fraction, whereas both perturbations will smoothly reduce burst amplitude. The calcium-dependent mechanisms that we include in our model pattern-generating population have some common features with a previous model that suggested the possible existence of two distinct preBötC neuronal populations responsible for eupneic burst and sigh generation, respectively, which also included excitatory synaptic transmission from the former to the latter (Toporikova et al., 2015). In the eupnea-sigh model, however, the population responsible for low-frequency, high-amplitude sighs was capable of rhythmic burst generation even without synaptic drive, in contrast to the pattern-generation population as tuned in our model. Also, in contrast to the results on bursts considered in our study, sigh frequency in the earlier model did not vary with extracellular potassium concentration and sigh generation required a hyperpolarization-activated inward current, $I_{h}$.

We also considered the effects of opioids in the context of burstlets and bursts, a topic that has not been extensively studied. It is well established that opioids slow the preBötC rhythm in in vitro slice preparations; however, the limited results presented to date on effects of opioids on the burstlet fraction are inconsistent. Specifically, Sun et al., 2019 found that application of the μOR agonist DAMGO at 10 nM and 30 nM progressively decreased the preBötC network frequency but had no impact on the burstlet fraction before the network rhythm was eventually abolished at approximately 100 nM. Similarly, Baertsch et al., 2021 found that DAMGO decreased the preBötC network frequency in a dose-dependent fashion; however, in these experiments the network was less sensitive to DAMGO, maintaining rhythmicity up to approximately 300 nM, and the burstlet fraction increased with increasing DAMGO concentration. The inconsistent effects of DAMGO on the burstlet fraction across these two studies can be explained by our simulations based on the different sensitivities of these two preparations to DAMGO and the two distinct mechanisms of action of DAMGO on neurons that express μOR – decreases in excitability and decreases in synaptic output of neurons – identified by Baertsch et al., 2021. In our simulations, we show that the decreased excitability resulting from activation of a GIRK channel only impacts frequency, whereas decreasing the synaptic output of μOR-expressing neurons results in an increase in the burstlet fraction and a decrease in burst frequency (Figure 6). In experiments, suppression of synaptic output does not appear to occur until DAMGO concentrations are above approximately 50 nM(Baertsch et al., 2021). Therefore, it is not surprising that DAMGO application did not strongly impact the burstlet fraction before the rhythm was ultimately abolished in Sun et al., 2019 due to the higher DAMGO sensitivity of that particular experimental preparation, as indicated by the lower dose needed for rhythm cessation.

### Mixed-mode oscillations

Mixed-mode oscillations, in which intrinsic dynamics of a nonlinear system naturally lead to alternations between small- and large-amplitude oscillations (Del Negro et al., 2002c; Bertram and Rubin, 2017), are a mechanism that has been previously proposed to underlie bursts and burstlets under the assumption of differences in intrinsic oscillation frequencies across preBötC neurons (Bacak et al., 2016). This mechanism was not needed to explain the generation of bursts and burstlets in the current model, however. Moreover, systems with mixed-mode oscillations can show a wide range of oscillation amplitudes under small changes in conditions and mixed-mode oscillations only emerge in the preBötC when $K_{b⁢a⁢t⁢h}$ is elevated above 9 mM (Del Negro et al., 2002c). These properties are not consistent with the burst and burstlet amplitudes or $K_{b⁢a⁢t⁢h}$-dependent changes in the burstlet fraction seen experimentally (Kallurkar et al., 2020) and in our model.

### Holographic photostimulation, percolation, and rhythm generation

Experimental data supporting burstlet theory has shown that burstlets are the rhythmogenic event in the preBötC. However, although burstlet theory is sometimes referenced as a theory of respiratory rhythm generation, the actual mechanisms of burstlet rhythm generation remain unclear. One idea that has been suggested is that rhythm generation is driven by a stochastic percolation process in which tonic spiking across the rhythm-generating population gradually synchronizes during the inter-burst-interval to generate the burstlet rhythm (Ashhad and Feldman, 2020; Slepukhin et al., 2020). In this framework, a burst (i.e., motor output) only occurs if the burstlet is of sufficient magnitude, resulting from sufficient synchrony, to trigger all-or-none recruitment of the pattern-forming subpopulation (Kam et al., 2013a; Kam et al., 2013b; Feldman and Kam, 2015; Kallurkar et al., 2020; Ashhad and Feldman, 2020; Slepukhin et al., 2020).

The idea that burstlets are the rhythmogenic event within the preBötC is supported by the observation that block of voltage-gated Ca2+ channels by Cd2+ eliminates bursts without affecting the underlying burstlet rhythm (Kam et al., 2013a; Sun et al., 2019). However, the rhythmogenic mechanism based on percolation is speculative and comes from two experimental observations. The first is that the duration and slope (i.e., shape) of the burstlet onset are statistically indistinguishable from the ramping pre-inspiratory activity that immediately precedes inspiratory bursts (Kallurkar et al., 2020). We note, however, that this shape of pre-inspiratory activity can arise through intrinsic mechanisms at the individual neuron level (Abdulla et al., 2021). The second observation evoked in support of the percolation idea is that holographic photostimulation of small subsets (4–9) of preBötC neurons can elicit bursts with delays lasting hundreds of milliseconds (Kam et al., 2013b). These delays are longer than could be explained with existing preBötC models and have approximately the same duration as the pre-inspiratory activity and burstlet onset hypothesized to underlie the rhythm. According to the percolation hypothesis of burstlet rhythm generation, these long delays result from the specific topological architecture of the preBötC, recently proposed to be a heavy-tailed synaptic weight distribution in the rhythmogenic preBötC subpopulation (Slepukhin et al., 2020).

Interestingly, the model presented here naturally captures the long delays characterized by Kam et al., 2013b, and stimulation of small subsets of neurons triggers a growth in population activity in the lead up to a burst that could be described as percolation (Figure 7B). Our model does not require a special synaptic weight distribution to generate the long delays, however. Indeed, our model suggests that the long delays between simulation and burst generation are due in large part to the dynamics of the pattern-forming population, as probabilistically these neurons are the most likely to be stimulated and they appear to play a dominant role in setting the timing of the elicited burst response (Figure 8H). Moreover, the dynamics of this population is strongly impacted by the CICR mechanism proposed here, which is required for burst generation. Interestingly, to match the 500 ms refractory period following an endogenous burst during which holographic stimulation cannot elicit a burst, our model predicts that the connection probability in the pattern-generating preBötC subpopulation must be between 1% and 2% (Figure 8A and B), which is consistent with available experimental data (Ashhad and Feldman, 2020). Experiments applying global, presumably weaker stimulation to the preBötC yield longer (~2 s) refractory periods after endogenous bursts (Baertsch et al., 2018; Kottick and Del Negro, 2015), and our model can also produce similar refractory periods in analogous conditions.

Thus, taken together, previous modeling and our work offer two alternative, seemingly viable hypotheses about the source of the delay between holographic stimulation and burst onset, each related to a proposed mechanism for burstlet and burst generation. Yet additional arguments call into question aspects of the percolation idea. If the burstlet rhythm is driven by a stochastic percolation process, then the period and amplitude of burstlets should be stochastic, irregular, and broadly distributed. Moreover, in the proposed framework of burstlet theory, the pattern of bursts and burstlets for a given burstlet fraction would also be stochastic since the burstlet-to-burst transition is thought to be an all-or-none process that depends on the generation of a burstlet of sufficient magnitude. Example traces illustrating a mixture of bursts and burstlets typically show a pattern of multiple burstlets followed by a burst that appears to regularly repeat (Kam et al., 2013b; Sun et al., 2019; Kallurkar et al., 2020) and hypoglossal output timing has also been found to exhibit high regularity Kam et al., 2013b, however, suggesting that the burstlet-to-burst transition is not dependent on the synchrony and hence magnitudes of individual burstlets but rather on a slow process that gradually evolves over multiple burstlets. The regularity and patterns of burstlets and bursts that arise from such a process in our model match well with those observed experimentally.

We note that the burstlet-to-burst transition mechanism proposed here, based on CICR from ER stores, depends on rhythmic inputs from the rhythm-generating to the pattern-generation population; however, it is independent of the mechanism of rhythm generation. In our simulations, rhythm generation depends on the slowly inactivating persistent sodium current ($I_{N⁢a⁢P}$). The role of $I_{N⁢a⁢P}$ in preBötC inspiratory rhythm generation is a contentious topic within the field, largely due to the inconsistent effects of $I_{N⁢a⁢P}$ block. We chose to use $I_{N⁢a⁢P}$ as the rhythmogenic mechanism in the burstlet population for a number of reasons: (1) consideration of the pharmacological mechanism of action and nonuniform effects of drug penetration can explain the seemingly contradictory experimental findings relating to $I_{N⁢a⁢P}$ (Phillips and Rubin, 2019b), (2) $I_{N⁢a⁢P}$-dependent rhythm generation is a well-established and understood idea (Butera et al., 1999), (3) recent computational work on which the current model is based suggests that rhythm generation occurs in a small, $I_{N⁢a⁢P}$-dependent rhythmogenic kernel that is analogous to the burstlet population (Phillips et al., 2019a), and predictions from this model that depend on the specific proposed roles of $I_{N⁢a⁢P}$ and $I_{C⁢A⁢N}$ in rhythm and pattern formation have been experimentally confirmed in a recent study (Phillips et al., 2021). It is important to note, however, that the findings about burstlets and bursts presented in this work would have been obtained if the burstlet rhythm was imposed (Figure 4—figure supplement 1) or if burstlets were generated by some other means, such as by the percolation mechanism proposed by burstlet theory.

### Summary of model predictions

The model presented here is itself a prediction; that is, this work predicts that a CICR-mediated mechanism is critical to the transition of burstlets into bursts. At a more specific level, our model makes the following predictions: (1) the magnitude of postsynaptic calcium transients triggered by EPSCs in preBötC neurons will increase with K+ (see Figure 4 and related text); (2) network-level burstlets and bursts will persist if currents involved in regulating burst shape, such as $I_{h}$ and $I_{A}$, are blocked (see earlier discussion); (3) blocking postsynaptic Ca2+ transients will increase the burstlet fraction and decrease the burst amplitude before network bursts are eventually abolished (see Figure 5); (4) $I_{C⁢A⁢N}$ block will not change the burstlet fraction and will decrease burstlet amplitudes (see Figure 5); (5) the synaptic connection probability within the pattern-generating population in the preBötC is low (1–2%, see Figure 8); and (6) selective holographic stimulation of pattern-generating neurons should be more effective than stimulation of rhythm-generating neurons at triggering network bursts (see Figure 8). This could be tested by selectively stimulating Dbx1 preBötC neurons that express Sst (pattern forming) or that do not express Sst (rhythmogenic).

### Conclusions

This study has developed the first model-based description of the biophysical mechanism underlying the generation of bursts and burstlets in the inspiratory preBötC. As suggested by burstlet theory and other previous studies, rhythm and pattern generation in this work are represented by two distinct preBötC subpopulations. A key feature of our model is that generation of network bursts (i.e., motor output) requires amplification of postsynaptic Ca2+ transients by CICR in order to activate $I_{C⁢A⁢N}$ and drive bursting in the rest of the network. Moreover, the burstlet fraction depends on rate of Ca2+ buildup in intracellular stores, which is impacted by $K_{b⁢a⁢t⁢h}$-dependent modulation of preBötC excitability. These ideas complement other recent findings on preBötC rhythm generation (Phillips et al., 2019a; Phillips and Rubin, 2019b; Phillips et al., 2021), together offering a unified explanation for a large body of experimental findings on preBötC inspiratory activity that form a theoretical foundation on which future developments can build.

## Materials and methods

### Neuron model

Model preBötC neurons include a single compartment and incorporate Hodgkin–Huxley-style conductances adapted from previously described models (Jasinski et al., 2013; Phillips et al., 2019a; Phillips and Rubin, 2019b) and/or experimental data as detailed below. The membrane potential of each neuron is governed by the following differential equation:

$$
C\frac{dV}{dt}=−I_{Na}−I_{K}−I_{NaP}−I_{Ca}−I_{CAN}−I_{Leak}−I_{Syn}−I_{GIRK}−I_{Holo}+I_{APP},
$$

where $C=36pF$ is the membrane capacitance and each $I_{i}$ represents a current, with i denoting the current’s type. The currents include the action potential generating Na+ and delayed rectifying K+ currents ($I_{N⁢a}$ and $I_{K}$), persistent Na+ current ($I_{N⁢a⁢P}$), voltage-gated Ca2+ current ($I_{C⁢a}$), Ca2+-activated nonselective cation (CAN) current ($I_{C⁢A⁢N}$), K+-dominated leak current ($I_{L⁢e⁢a⁢k}$), synaptic current ($I_{S⁢y⁢n}$), μ-opioid receptor-activated G protein-coupled inwardly rectifying K+ leak current ($I_{G⁢I⁢R⁢K}$) (Kubo et al., 1993), and a holographic photostimulation current ($I_{H⁢o⁢l⁢o}$). $I_{A⁢P⁢P}$ denotes an applied current injected from an electrode. The currents are defined as follows:

$$
I_{N⁢a}=g_{N⁢a}⋅m_{N⁢a}^{3}⋅h_{N⁢a}⋅(V-E_{N⁢a})
$$



$$
I_{K}=g_{K}⋅m_{K}^{4}⋅(V-E_{K})
$$



$$
I_{N⁢a⁢P}=g_{N⁢a⁢P}⋅m_{N⁢a⁢P}⋅h_{N⁢a⁢P}⋅(V-E_{N⁢a})
$$



$$
I_{C⁢a}=g_{C⁢a}⋅m_{C⁢a}⋅h_{C⁢a}⋅(V-E_{C⁢a})
$$



$$
I_{C⁢A⁢N}=g_{C⁢A⁢N}⋅m_{C⁢A⁢N}⋅(V-E_{C⁢A⁢N})
$$



$$
I_{L⁢e⁢a⁢k}=g_{L⁢e⁢a⁢k}⋅(V-E_{L⁢e⁢a⁢k})
$$



$$
I_{S⁢y⁢n}=g_{S⁢y⁢n}⋅(V-E_{S⁢y⁢n})
$$



$$
I_{GIRK}=g_{GIRK}⋅(V−E_{K})
$$



$$
I_{Holo}=g_{Holo}⋅(V−E_{Holo})
$$

where gi is the maximum conductance, $E_{i}$ is the reversal potential, and mi and hi are gating variables for channel activation and inactivation for each current $I_{i}$. The glutamatergic synaptic conductance $g_{S⁢y⁢n}$ is dynamic and is defined below. The values used for the gi and $E_{i}$ are mostly shown in Table 1 , with a few conductances selected from distributions as indicated in Table 2.

**Table 1.**
 Ionic channel parameters.


<table>
  <thead>
    <tr>
      <th>Channel</th>
      <th>Parameters</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IN⁢a</td>
      <td>gNa=150nS</td>
      <td>EN⁢a=26.54⋅l⁢n⁢(N⁢ao⁢u⁢t/N⁢ai⁢n)</td>
      <td>Nain=15mM</td>
      <td>Naout=120mM</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>m1/2=−43.8mV</td>
      <td>km=6.0mV</td>
      <td>τmaxm=0.25ms</td>
      <td>τ1/2m=−43.8mV</td>
      <td>kτm=14.0mV</td>
    </tr>
    <tr>
      <td></td>
      <td>h1/2=−67.5mV</td>
      <td>kh=−11.8mV</td>
      <td>τmaxh=8.46ms</td>
      <td>τ1/2h=−67.5mV</td>
      <td>kτh=12.8mV</td>
    </tr>
    <tr>
      <td>IK</td>
      <td>gK=220nS</td>
      <td>EK=26.54⋅l⁢n⁢(Kb⁢a⁢t⁢h/Ki⁢n)</td>
      <td>Ki⁢n=125</td>
      <td>KB⁢a⁢t⁢h=V⁢A⁢R</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Aα=0.011</td>
      <td>Bα=44.0mV</td>
      <td>kα=5.0mV</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Aβ=0.17</td>
      <td>Bβ=49.0mV</td>
      <td>kβ=40.0mV</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IN⁢a⁢P</td>
      <td>gN⁢a⁢P=N⁢(μ,σ), see Table 2</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>m1/2=−47.1mV</td>
      <td>km=3.1mV</td>
      <td>τmaxm=1.0ms</td>
      <td>τ1/2m=−47.1mV</td>
      <td>kτm=6.2mV</td>
    </tr>
    <tr>
      <td></td>
      <td>h1/2=−60.0mV</td>
      <td>kh=−9.0mV</td>
      <td>τmaxh=5000ms</td>
      <td>τ1/2h=−60.0mV</td>
      <td>kτh=9.0mV</td>
    </tr>
    <tr>
      <td>IC⁢a</td>
      <td>gCa=0.0065pS</td>
      <td>EC⁢a=13.27⋅l⁢n⁢(C⁢ao⁢u⁢t/C⁢ai⁢n)</td>
      <td></td>
      <td>Caout=4.0mM</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>m1/2=−27.5mV</td>
      <td>km=5.7mV</td>
      <td>τm=0.5ms</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>h1/2=−52.4mV</td>
      <td>kh=−5.2mV</td>
      <td>τh=18.0ms</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IC⁢A⁢N</td>
      <td>gC⁢A⁢N=N⁢(μ,σ), see Table 2</td>
      <td>ECAN=0.0mV</td>
      <td>Ca1/2=0.00074mM</td>
      <td>n=0.97</td>
      <td></td>
    </tr>
    <tr>
      <td>IL⁢e⁢a⁢k</td>
      <td>gL⁢e⁢a⁢k=N⁢(μ,σ), see Table 2</td>
      <td>ELeak=−26.54∗ln[(PNa∗Nain+PK∗Kin) /(PNa∗Naout+PK∗Kbath)]</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>PN⁢a=1</td>
      <td>PK=42</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IS⁢y⁢n</td>
      <td>gS⁢y⁢n=V⁢A⁢R, see Equation 25</td>
      <td>ESyn=0.0mV</td>
      <td>τSyn=5.0ms</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IG⁢I⁢R⁢K</td>
      <td>gGIRK=0−0.3nS</td>
      <td>EG⁢I⁢R⁢K=EK</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IH⁢o⁢l⁢o</td>
      <td>gHolo=50nS</td>
      <td>τHolo=100ms</td>
      <td>EH⁢o⁢l⁢o=ES⁢y⁢n</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Distributed channel conductances.


<table>
  <thead>
    <tr>
      <th rowspan="2">Type</th>
      <th colspan="2">gNaP(nS)</th>
      <th colspan="2">gLeak(nS)</th>
      <th colspan="2">gCAN(nS)</th>
    </tr>
    <tr>
      <th>μ</th>
      <th>σ</th>
      <th>μ</th>
      <th>σ</th>
      <th>μ</th>
      <th>σ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Rhythm</td>
      <td>3.33</td>
      <td>0.75</td>
      <td>exp((KBath−3.425)/4.05)</td>
      <td>0.05⋅μleak</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>Pattern</td>
      <td>1.5</td>
      <td>0.25</td>
      <td>exp((KBath−3.425)/4.05)</td>
      <td>0.025⋅μleak</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>

Activation (mi) and inactivation (hi) of voltage-dependent channels are described by the following differential equation:

$$
\tau_{X}⁢(V)⋅\frac{d⁢X}{d⁢t}=X_{∞}⁢(V)-X;X\in{m,h}
$$

where $X_{∞}$ represents steady-state activation/inactivation and $\tau_{X}$ is a time constant. For $I_{N⁢a}$, $I_{N⁢a⁢P}$, and $I_{C⁢a}$, the functions $X_{∞}$ and $\tau_{X}$ take the forms

$$
X_{∞}⁢(V)=1/(1+exp⁡(-(V-X_{1/2})/k_{X})),
$$



$$
\tau_{X}⁢(V)=\tau_{m⁢a⁢x}^{X}/cosh⁡((V-\tau_{1/2}^{X})/k_{\tau}^{X}).
$$

The values of the parameters ($X_{1/2}$, $k_{X}$, $\tau_{m⁢a⁢x}^{X}$, $\tau_{1/2}^{X}$, and $k_{\tau}^{X}$) corresponding to $I_{N⁢a}I_{N⁢a⁢P}$, $I_{NaP}$ and $I_{C⁢a}$ are given in Table 1.

For the voltage-gated potassium channel, the steady-state activation $m_{∞}^{K}⁢(V)$ and time constant $\tau_{m}^{K}⁢(V)$ are given by the expressions

$$
m_{∞}^{K}⁢(V)=\alpha_{∞}⁢(V)/(\alpha_{∞}⁢(V)+\beta_{∞}⁢(V)),
$$



$$
\tau_{m}^{K}⁢(V)=1/(\alpha_{∞}⁢(V)+\beta_{∞}⁢(V))
$$

where

$$
\alpha_{∞}⁢(V)=A_{\alpha}⋅(V+B_{\alpha})/(1-exp⁡(-(V+B_{\alpha})/k_{\alpha})),
$$



$$
\beta_{∞}⁢(V)=A_{\beta}⋅exp⁡(-(V+B_{\beta})/k_{\beta}).
$$

The values for the constants $A_{\alpha}$, $A_{\beta}$, $B_{\alpha}$, $B_{\beta}$, $k_{\alpha}$, and $k_{\beta}$ are also given in Table 1.

$I_{C⁢A⁢N}$ activation depends on the $C⁢a^{2+}$ concentration in the cytoplasm ($[C⁢a]_{C⁢y⁢t⁢o}$) and is given by

$$
m_{C⁢A⁢N}=1/(1+(C⁢a_{1/2}/[C⁢a]_{C⁢y⁢t⁢o})^{n}).
$$

The parameters $C⁢a_{1/2}$ and $n$ represent the half-activation Ca2+ concentration and the Hill coefficient, respectively, and are included in Table 1.

The dynamics of $[C⁢a]_{C⁢y⁢t⁢o}$ is determined in part by the balance of Ca2+ efflux toward a baseline concentration via the Ca2+ pump and Ca2+ influx through voltage-dependent activation of $I_{C⁢a}$ and synaptically triggered Ca2+ transients, with a percentage ($P_{S⁢y⁢n⁢C⁢a}$) of the synaptic current ($I_{S⁢y⁢n}$) carried by Ca2+ ions. Additionally, the model includes an intracellular compartment that represents the ER, which impacts $[C⁢a]_{C⁢y⁢t⁢o}$. The ER removes Ca2+ from the cytoplasm via a sarcoplasmic/endoplasmic reticulum Ca2+- ATPase (SERCA) pump, which transports Ca2+ from the cytoplasm into the ER ($J_{S⁢E⁢R⁢C⁢A}$) and releases Ca2+ into the cytoplasm via calcium-dependent activation of the inositol triphosphate (IP3) receptor ($J_{I⁢P⁢3}$). Therefore, the dynamics of $[C⁢a]_{C⁢y⁢t⁢o}$ is described by the following differential equation:

$$
\frac{d⁢[C⁢a]_{C⁢y⁢t⁢o}}{d⁢t}=\alpha_{C⁢a}⋅(I_{C⁢a}+P_{S⁢y⁢n⁢C⁢a}⋅I_{S⁢y⁢n})+\alpha_{E⁢R}⋅(J_{I⁢P⁢3}-J_{S⁢E⁢R⁢C⁢A})-\frac{([C⁢a]_{C⁢y⁢t⁢o}-C⁢a_{m⁢i⁢n})}{\tau_{p⁢u⁢m⁢p}},
$$

where $\alpha_{Ca}=2.5⋅10^{−5}mM/fC$ is a conversion factor relating current to rate of change of $[C⁢a]_{C⁢y⁢t⁢o}$, $\tau_{pump}=500ms$ is the time constant for the Ca2+ pump, $Ca_{min}=5.0⋅10^{−6}mM$ is a minimal baseline calcium concentration, and $\alpha_{E⁢R}=2.5⋅10^{-5}$ is the ratio of free to bound Ca2+ in the ER.

The flux of Ca2+ from the ER to the cytoplasm through the IP3 receptor is modeled as

$$
J_{I⁢P⁢3}=(E⁢R_{l⁢e⁢a⁢k}+G_{I⁢P⁢3}⋅(\frac{[C⁢a]_{C⁢y⁢t⁢o}}{[C⁢a]_{C⁢y⁢t⁢o}+K_{a}}⋅\frac{[I⁢P⁢3]_{i}⋅l}{[I⁢P⁢3]_{i}+K_{l}})^{3})⋅([C⁢a]_{E⁢R}-[C⁢a]_{C⁢y⁢t⁢o}),
$$

where $ER_{leak}=0.1/ms$ represents the leak constant from the ER stores, $G_{IP3}=77,500/ms$ represents the permeability of the IP3 channel, $K_{a}=1.0⋅10^{−4}mM$ and $K_{l}=1.0⋅10^{−3}mM$ are dissociation constants, and $[IP3]_{i}=1.5⋅10^{−3}mM$ is the cytoplasm IP3 concentration. Finally, the Ca2+-dependent IP3 gating variable, $l$, and the Ca2+ concentration in the ER, $[C⁢a]_{E⁢R}$, are determined by the following equations:

$$
\frac{d⁢l}{d⁢t}=A⋅(K_{d}-l⋅([C⁢a]_{C⁢y⁢t⁢o}+K_{d}));
$$



$$
[C⁢a]_{E⁢R}=([C⁢a]_{t⁢o⁢t⁢a⁢l}-[C⁢a]_{C⁢y⁢t⁢o})/\sigma_{C⁢a},
$$

where $A=0.1mM/ms$ is a conversion factor, $K_{d}=0.2⋅10^{−3}mM$ is the dissociation constant for IP3 inactivation, $[C⁢a]_{t⁢o⁢t⁢a⁢l}$ is the total intracellular calcium concentration, and $\sigma_{C⁢a}=0.185$ is the ratio of cytosolic to ER volume. The total intracellular calcium concentration is described as

$$
\frac{d⁢[C⁢a]_{T⁢o⁢t⁢a⁢l}}{d⁢t}=\alpha_{C⁢a}⋅(I_{C⁢a}+P_{S⁢y⁢n⁢C⁢a}⋅I_{S⁢y⁢n})-\frac{(C⁢a_{C⁢y⁢t⁢o}-C⁢a_{m⁢i⁢n})}{\tau_{p⁢u⁢m⁢p}}.
$$

Finally, removal of Ca2+ from the cytoplasm by the SERCA pump is modeled as

$$
J_{S⁢E⁢R⁢C⁢A}=G_{S⁢E⁢R⁢C⁢A}⋅\frac{[C⁢a]_{C⁢y⁢t⁢o}^{2}}{K_{S⁢E⁢R⁢C⁢A}^{2}+[C⁢a]_{C⁢y⁢t⁢o}^{2}},
$$

where $G_{SERCA}=0.45mM/ms$ is the maximal flux through the SERCA pump, and $K_{SERCA}=7.5⋅10^{−5}mM$ is a dissociation constant.

Nondimensionalization of similar models in past work (Wang and Rubin, 2017; Wang and Rubin, 2020) has shown that $h_{N⁢a⁢P},l$, and $[C⁢a]_{E⁢R}$ are the slowest variables in the model and evolve on similar timescales, while $[C⁢a]_{C⁢y⁢t⁢o}$ evolves on a faster timescale that is still significantly slower than that of the voltage dynamics and other current gating variables. Some subtleties arise in that different components of the calcium dynamics evolve on different timescales and their influences depend on the levels of calcium present in various domains within the cell, but these subtleties are not considered in this article.

When we include multiple neurons in the network, we can index them with subscripts. The total synaptic conductance $(g_{S⁢y⁢n})_{i}$ of the ith target neuron is described by the following equation:

$$
(g_{Syn})_{i}=g_{Tonic}+\sumj\neqi;nW_{j,i}⋅D_{j}⋅C_{j,i}⋅H(t−t_{j,n})⋅e^{−(t−t_{j,n})/\tau_{syn}},
$$

where $g_{T⁢o⁢n⁢i⁢c}$ is a fixed or tonic excitatory synaptic conductance (e.g., from respiratory control areas outside of the preBötC) that we assume impinges on all neurons, $W_{j,i}$ represents the weight of the synaptic connection from neuron $j$ to neuron i, $D_{j}$ is a scaling factor for short-term synaptic depression in the presynaptic neuron $j$ (described in more detail below), $C_{j,i}$ is an element of the connectivity matrix ($C_{j,i}=1$ if neuron $j$ makes a synapse with neuron i and $C_{j,i}=0$ otherwise), $H(.)$ is the Heaviside step function, and $t$ denotes time. $\tau_{S⁢y⁢n}$ is an exponential synaptic decay constant, while $t_{j,n}$ is the time at which the nth action potential generated by neuron $j$ reaches neuron i.

We included synaptic depression in our model because experiments have revealed that it contributes to termination of inspiratory activity in the preBötC (Kottick and Del Negro, 2015) and past computational models have suggested that it might play an important role in preBötC network oscillations (Rubin et al., 2009; Guerrier et al., 2015). Synaptic depression in the jth neuron ($D_{j}$) was simulated using an established mean-field model of short-term synaptic dynamics (Abbott et al., 1997; Dayan and Abbott, 2001; Morrison et al., 2008) as follows:

$$
\frac{dD_{j}}{dt}=\frac{D_{0}−D_{j}}{\tau_{D}}−\alpha_{D}⋅D_{j}⋅\delta(t−t_{j})
$$

where the parameter $D_{0}=1$ sets the maximum value of $D_{j}$, $\tau_{D}=1000ms$ sets the rate of recovery from synaptic depression, $\alpha_{D}=0.2$ sets the fractional depression of the synapse each time neuron $j$ spikes, and $\delta(.)$ is the Kronecker delta function that equals 1 at the time of each spike in neuron $j$ and 0 otherwise. Parameters were chosen to qualitatively match data from Kottick and Del Negro, 2015. Note that with this choice of $\tau_{D}$ synaptic depression recovers on a timescale comparable to that of the other slowest variables in the model.

When we consider a two-neuron network (Figure 2), we take $W_{1,2}=W_{2,1}=0.006$ and $C_{1,2}=C_{2,1}=1$. For the full preBötC population model comprising rhythm- and pattern-generating subpopulations, the weights of excitatory conductances were uniformly distributed such that $W_{j,i}=U⁢(0,W_{M⁢a⁢x})$ where $W_{M⁢a⁢x}$ is a constant associated with the source and target neurons’ populations; with each such pair, we also associated a connection probability and used this to randomly set the $C_{j,i}$ values (see Table 3). Effects of opioids on synaptic transmission for source neurons in the rhythmogenic subpopulation (Figure 6) were simulated by scaling $W_{j,i}$ with the parameter $\gamma_{\mu⁢O⁢R}$, which ranged between 0 and 0.5 and sets the percent synaptic block.

**Table 3.**
 Maximal synaptic weights and connection probabilities between and within rhythm- and pattern-generating preBötC subpopulations ($W_{M⁢a⁢x},P$).


<table>
  <thead>
    <tr>
      <th rowspan="2" colspan="2"></th>
      <th colspan="2">Target</th>
    </tr>
    <tr>
      <th>Rhythm</th>
      <th>Pattern</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Source</td>
      <td>Rhythm</td>
      <td>(0.15 nS, 0.13)</td>
      <td>(0.000175 nS, 0.3)</td>
    </tr>
    <tr>
      <td>Pattern</td>
      <td>(0.25 nS, 0.3)</td>
      <td>(0.0063 nS, 0.02)</td>
    </tr>
  </tbody>
</table>

### Network construction

The relative proportions of neurons assigned to the rhythm- and pattern-generating preBötC subpopulations were chosen based on experimental data. For example, Kallurkar et al., 2020 found that $20\pm9%$ of preBötC inspiratory neurons are active during burstlets at $K_{Bath}=9mM$. Moreover, the rhythm- and pattern-generating neurons are hypothesized to be represented by the subsets of Dbx1-positive preBötC neurons that are somatostatin-negative ($S⁢S⁢T^{-}$) and -positive ($S⁢S⁢T^{+}$), respectively (Cui et al., 2016; Ashhad and Feldman, 2020). Somatostatin-positive neurons are estimated to comprise 72.6% of the $D⁢b⁢x⁢1^{+}$ preBötC population (Koizumi et al., 2016). Therefore, our preBötC network was constructed such that the rhythm and pattern-forming subpopulations represent 25% and 75% of the $N=400$ neuron preBötC population (i.e., $N_{R}=100$ and $N_{P}=300$). The rhythm- and pattern-generating neurons are distinguished by their $I_{N⁢a⁢P}$, $I_{L⁢e⁢a⁢k}$, and $I_{C⁢A⁢N}$ conductances. Also, we included the K+ leak current $I_{G⁢I⁢R⁢K}$ exclusively to the rhythm generating subpopulation, the activation of which we used as one representation of the effects of opioid application (Figure 6).

The synaptic connection probabilities within the rhythm- and pattern-generating neurons, $P_{RR}=13%$ and $P_{PP}=2%$, were taken from previous experimental findings (Rekling et al., 2000 and Ashhad and Feldman, 2020, respectively). The connection probabilities between the rhythm- and pattern-generating populations are not known and in the model were set at $P_{R⁢P}=P_{P⁢R}=30%$ such that the total connection probability in the network is approximately 13% (Rekling et al., 2000).

Heterogeneity was introduced by normally distributing the parameters $g_{l⁢e⁢a⁢k}$, $g_{N⁢a⁢P}$, and $g_{C⁢A⁢N}$ as well as uniformly distributing the weights ($W_{j,i}$) of excitatory synaptic connections (see Table 2 and Table 3). Additionally, $g_{l⁢e⁢a⁢k}$ was conditionally distributed with $g_{N⁢a⁢P}$ in order to achieve a bivariate normal distribution between these two conductances, as suggested by Del Negro et al., 2002a and Koizumi and Smith, 2008. In our simulations, this was achieved by first normally distributing $g_{N⁢a⁢P}$ in each neuron according to the values presented in Table 2. Then we used a property of bivariate normal distribution, which says that the conditional distribution of $g_{l⁢e⁢a⁢k}$ given $g_{N⁢a⁢P}$ is itself a normal distribution with mean ($\mu_{L⁢e⁢a⁢k}^{*}$) and standard deviation ($\sigma_{L⁢e⁢a⁢k}^{*}$) described as follows:

$$
\mu_{L⁢e⁢a⁢k}^{*}=\mu_{L⁢e⁢a⁢k}+ρ⋅(\sigma_{L⁢e⁢a⁢k}/\sigma_{N⁢a⁢P})⋅(g_{N⁢a⁢P}^{i}-\mu_{N⁢a⁢P}),
$$



$$
\sigma_{L⁢e⁢a⁢k}^{*}=\sqrt{(1-ρ^{2})⋅\sigma_{L⁢e⁢a⁢k}^{2}}
$$

In these equations, $\mu_{L⁢e⁢a⁢k}$ and $\mu_{N⁢a⁢P}$ are the mean and $\sigma_{L⁢e⁢a⁢k}$ and $\sigma_{N⁢a⁢P}$ are the standard deviation of the $g_{L⁢e⁢a⁢k}$ and $g_{N⁢a⁢P}$ distributions, while $ρ=0.8$ represents the correlation coefficient and $g_{N⁢a⁢P}^{i}$ represents the persistent sodium current conductance for the ith neuron. All parameters are given in Table 2.

### Activation dynamics of IH⁢o⁢l⁢o

Holographic stimulation was simulated by activating $I_{H⁢o⁢l⁢o}$ in small sets of randomly selected neurons across the preBötC population. Activation of this current was simulated by the following equation:

$$
\frac{dm_{Holo}}{dt}=−\frac{m_{Holo}}{\tau_{Holo}}+\delta(t−t_{stim})
$$

where $m_{H⁢o⁢l⁢o}$ represents the channel activation and ranges between 0 and 1, $\tau_{H⁢o⁢l⁢o}$ represents the decay time constant, and $\delta(.)$ is the Kronecker delta function, which represents the instantaneous jump in $m_{H⁢o⁢l⁢o}$ from 0 to 1 at the time of stimulation ($t_{s⁢t⁢i⁢m}$). Parameters were chosen such that the response in stimulated neurons matched those seen in Kam et al., 2013b. All parameters are given in Table 1.

### Data analysis and definitions

Data generated from simulations was postprocessed in MATLAB (MathWorks, Inc). An action potential was defined to have occurred in a neuron when its membrane potential $V_{m}$ increased through $−35mV$. Histograms of population activity were calculated as the number of action potentials per $20ms$ bin per neuron, with units of $A⁢P⁢s/(s⋅n⁢e⁢u⁢r⁢o⁢n)$. Network burst and burstlet amplitudes and frequencies were calculated by identifying the peaks and the inverse of the interpeak interval from the population histograms. The thresholds used for burst and burstlet detection were $30spk/s/N$ and $2.5spk/s/N$, respectively. For the simulated holographic stimulation simulations, the start of a network burst was defined as the time at which the integrated preBötC population activity increased through the threshold for burst detection, while the end of a network burst was defined as the time at which the integrated preBötC activity returned to exactly zero.

### Integration methods

All simulations were performed locally on an 8-core Linux-based operating system or on compute nodes at the University of Pittsburgh’s Center for Research Computing. Simulation software was custom written in C++. Numerical integration was performed using the first-order Euler method with a fixed step-size ($Δ⁢t$) of $0.025ms$.
