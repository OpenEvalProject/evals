# Short-term synaptic dynamics control the activity phase of neurons in an oscillatory network

## Authors

- Diana Martinez<sup>1</sup> ([ORCID: 0000-0003-0982-4092](https://orcid.org/0000-0003-0982-4092))
- Haroon Anwar<sup>1</sup> ([ORCID: 0000-0002-3079-4812](https://orcid.org/0000-0002-3079-4812))
- Amitabha Bose<sup>2</sup>
- Dirk M Bucher<sup>1</sup>
- Farzan Nadim<sup>1</sup> ([ORCID: 0000-0003-4144-9042](https://orcid.org/0000-0003-4144-9042)) †

### Affiliations

1. Federated Department of Biological Sciences New Jersey Institute of Technology and Rutgers University Newark United States
2. Department of Mathematical Sciences New Jersey Institute of Technology Newark United States

† Corresponding author

## Abstract

In oscillatory systems, neuronal activity phase is often independent of network frequency. Such phase maintenance requires adjustment of synaptic input with network frequency, a relationship that we explored using the crab, Cancer borealis, pyloric network. The burst phase of pyloric neurons is relatively constant despite a > two fold variation in network frequency. We used noise input to characterize how input shape influences burst delay of a pyloric neuron, and then used dynamic clamp to examine how burst phase depends on the period, amplitude, duration, and shape of rhythmic synaptic input. Phase constancy across a range of periods required a proportional increase of synaptic duration with period. However, phase maintenance was also promoted by an increase of amplitude and peak phase of synaptic input with period. Mathematical analysis shows how short-term synaptic plasticity can coordinately change amplitude and peak phase to maximize the range of periods over which phase constancy is achieved.

## Introduction

Oscillatory neural activity is often organized into different phases across groups of neurons, both in brain rhythms associated with cognitive tasks or behavioral states (Hasselmo et al., 2002; Buzsáki and Wang, 2012; Buzsáki and Tingley, 2018), and in central pattern generating (CPG) circuits that drive rhythmic motor behaviors (Marder and Bucher, 2001; Marder et al., 2005; Grillner, 2006; Bucher et al., 2015; Katz, 2016; Stein, 2018). The functional significance of different phases in the latter is readily apparent, as they for example provide alternating flexion and extension of limb joints, and coordination of movements between joints, limbs, and segments (Krantz and Parks, 2012; Grillner and El Manira, 2015; Kiehn, 2016; Le Gal et al., 2017; Bidaye et al., 2018). A hallmark of many such patterns is that the relative timing of firing between neurons is well maintained over a range of rhythm frequencies (Dicaprio et al., 1997; Hooper, 1997b; Hooper, 1997a; Wenning et al., 2004; Marder et al., 2005; Grillner, 2006; Mullins et al., 2011; Le Gal et al., 2017). If the latency of firing across different groups of neurons changes proportionally to the rhythm period, phase (latency over period) is invariant, in some cases providing optimal limb coordination at all speeds (Zhang et al., 2014).

The ability of the system to coordinate phases with changes in period arises from central coordinating mechanisms between circuit elements, as it is present in isolated nervous system preparations, but the underlying cellular and circuit mechanisms are not well understood. For instance, constant phase lags between neighboring segments in the control of swimming in lamprey fish and crayfish can be explained mathematically on the basis of asymmetrically weakly coupled oscillators, but the role of intrinsic and synaptic dynamics within each segment is unknown (Cohen et al., 1992; Skinner and Mulloney, 1998; Grillner, 2006; Mullins et al., 2011; Zhang et al., 2014; Le Gal et al., 2017).

The pyloric circuit of the crustacean stomatogastric ganglion (STG) has inspired a series of experimental and theoretical studies of cellular and synaptic mechanisms underlying phase maintenance. The pyloric circuit generates a triphasic motor pattern with stable phase relationships over a wide range of periods (Eisen and Marder, 1984; Hooper, 1997b; Hooper, 1997a; Bucher et al., 2005; Goaillard et al., 2009; Tang et al., 2012; Soofi et al., 2014). Synapses in the pyloric circuit use graded as well as spike-mediated transmission (Graubard et al., 1980; Harris-Warrick and Johnson, 2010; Zhao et al., 2011; Rosenbaum and Marder, 2018). Follower neurons burst in rebound from inhibition from pacemaker neurons (Marder and Bucher, 2007; Daur et al., 2016), and post-inhibitory rebound delay scales with the period of hyperpolarizing currents (Hooper, 1998). Voltage-gated conductances slow enough for cumulative activation across cycles could promote such phase maintenance (Hooper et al., 2009). Similarly, short-term depression of graded inhibitory synapses is slow enough to accumulate over several pyloric cycles, meaning that effective synaptic strength increases with increasing cycle period (Manor et al., 1997; Nadim and Manor, 2000).

Theoretical studies have shown that short-term synaptic depression, by increasing inhibition strength with cycle period, should promote phase maintenance (Manor et al., 2003; Mouser et al., 2008), particularly in conjunction with inactivating (A-type) potassium currents (Bose et al., 2004; Greenberg and Manor, 2005), which control the rebound delay (Harris-Warrick et al., 1995b; Harris-Warrick et al., 1995a; Kloppenburg et al., 1999). These predictions remain experimentally untested.

Additionally, postsynaptic responses also depend on the actual trajectory of synaptic conductances, which are shaped by presynaptic voltage trajectories and short-term synaptic plasticity (Manor et al., 1997; Mamiya et al., 2003; Zhao et al., 2011; Tseng et al., 2014). If amplitude, duration, and trajectory of synaptic conductance determine rebound delay, phase maintenance necessitates all three of these parameters to change with cycle period in coordination. We used the dynamic clamp technique to exhaustively explore the range of these parameters and understand how the coordinated changes in synaptic dynamics determines the phase of follower neurons in an oscillatory circuit. Our findings are consistent with a mathematical framework that accounts for the dependence of amplitude and peak phase of the synaptic conductance on cycle period.

## Results

### Phase maintenance and latency maintenance

The firing of neurons in oscillatory networks is shaped by a periodic synaptic input. The relative firing latency of such neurons is often measured relative to a defined reference time in each cycle of oscillation, and is used to determine the activity phase of the neuron (see, for example Belluscio et al., 2012). For example, in a simple network consisting of a bursting oscillatory neuron driving a follower neuron (Figure 1A1), at a descriptive level, the latency (Δt) of the follower neuron activity relative to the onset of the oscillator’s burst onset may depend on the oscillation cycle period (P). In response to a change in period (say, to P2), the follower neuron may keep constant latency (Δt 2 = Δt), or constant phase, that is modify its latency proportionally to the change in period (Δt2 / P2 = Δt/P; Figure 1A2). However, in many oscillatory systems, for example the pyloric circuit (Hooper, 1997b; Hooper, 1997a), the relationship between L and P falls between these two extremes.

![Figure 1.](https://cdn.elifesciences.org/articles/46911/elife-46911-fig1-v2.jpg)

**Figure 1.:** (A1) Schematic diagram showing that a follower neuron (F) strongly inhibited by a bursting oscillatory neuron (O) with period P can produce rebound bursts with the same period at a latency Δt. (A2) If the period of O changes to a new value (P2), the new F burst latency (Δt2) typically falls between two extremes: it could stay constant (top trace) or change proportionally to P2, so that the burst phase (Δt/P) remains constant (middle trace). (B) Example traces of the pyloric pacemaker PD neuron and the follower LP neuron represent the O and F relationship in panel A. Here, the PD neuron is voltage clamped and a pre-recorded waveform of the same neuron is used to drive this neuron to follow different cycle periods. The LP neuron follows the same period because of the synaptic input it receives. (C) A measurement of the LP neuron burst onset time (Δt) with respect to the onset of the PD neuron burst shows that Δt falls between the two limits of constant latency and constant phase. Dotted curves represent constant latency matched to the latencies at the two extreme P values.

We demonstrated this point in the pyloric follower LP neuron using the following protocol. We voltage clamped one of the pacemaker PD neurons and drove this neuron with its own pre-recorded waveform, but applied at five different cycle periods (also denoted P). This protocol entrained the pacemaker group at this period, which forced the follower LP neuron to obey the same period (Figure 1B). We then measured the latency (Δt) of the LP burst onset with respect to onset of the PD neuron burst. A plot of the LP latency Δt or phase (Δt/P) for different cycle periods demonstrates the above-mentioned finding that the LP neuron activity falls between the two limits of constant phase and constant latency (Figure 1C).

### The burst onset time of the LP neuron depends on the temporal dynamics of its input

The LP neuron does not have intrinsic oscillatory properties, but oscillates due to the synaptic input it receives from the pacemaker anterior burster (AB) and pyloric dilator (PD) neurons, and the follower pyloric constrictor (PY) neurons (Figure 2A). The burst onset phase of the LP neuron (φLP = Δt/P; Figure 2A) is shaped by the interaction between synaptic inputs and the neuron’s intrinsic dynamics that influence post-inhibitory rebound. We measured an overall burst onset phase of the LP neuron to be φLP=0.34 ± 0.03 (N = 9).

![Figure 2.](https://cdn.elifesciences.org/articles/46911/elife-46911-fig2-v2.jpg)

**Figure 2.:** (A) Simultaneous intracellular recording of the LP neuron and extracellular recording of the lateral ventricular nerve (lvn), containing the axons of the LP, PD and PY neurons (arrows). Period (P) and the burst onset time (Δt) of the LP neuron are defined in reference to the pacemaker group (PD) burst. (B) Blocking the AB and PY synaptic inputs (10 µM picrotoxin) to the LP neuron disrupts its bursting oscillations. (C) The LP neuron, in picrotoxin, was driven with a noise current input (Inoise) for 60 min. In response, the LP neuron produced an irregular pattern of bursting. Specific inter-burst intervals (IBIs) were tagged and used for burst-triggered averaging. (D) Example of burst-trigger-averaged input current (IBTA, green). Individual traces are shown in gray. (E) For each IBI (300, 500, 700, 900 ms), IBTA was calculated and normalized to the (negative) peak value of IBTA for IBI = 300 ms. Different traces in each panel show the IBTA of different preparations. (F) The mean (across preparations) of the normalized IBTAs shown in panel E. (G) Traces in panel F normalized by IBI. (H–K) Four parameters define the shape of the IBTA: peak amplitude Iamp (H), peak phase Δpeak (I), slopeup (J) and slopedown (K) across preparations. IBI had a significant effect on amplitude Iamp (p<0.001), peak phase Δpeak (p<0.001), slopeup (p<0.001) and slopedown (p=0.002).

As a first-order quantification, we measured how inputs to the LP neuron interact with its intrinsic properties to determine the timing between its bursts, in the absence of network oscillations. To this end, we blocked the synaptic input from the pacemaker AB and follower PY neurons to the LP neuron (Figure 2B) and drove the LP neuron with a noise current input (see Materials and methods). In response to the noise input, the LP neuron produced an irregular pattern of spike times, which included a variety of bursting patterns with different spike numbers (Figure 2C). We were interested in the characteristics of inputs producing different burst onset latencies. However, unlike a periodic input, noise input does not provide a well-defined reference point to measure the burst onset latency. We categorized bursts with respect to the preceding inter-burst intervals (IBIs; see Materials and methods), during which no other action potentials occurred. We classified these IBIs in bins (300, 500, 700 and 900 ms) and tagged bursts based on the IBI values (Figure 2C). We characterized the driving input leading to bursts with specific IBIs by burst-triggered averaging the input current (IBTA; an example shown in Figure 2D). Our analysis produced a single IBTA for each of the four IBIs in each preparation (N = 23). IBTA’s of each preparation were first normalized in amplitude by the (negative) peak value of the IBTA at IBI = 300 ms (Figure 2E; average shown in Figure 2F) to examine how peak amplitude (Ipeak) varied with IBI. These data were then normalized in time (Figure 2G) to examine the effect of IBI on peak phase (Δpeak) and the rise (slopeup) and fall (slopedown) slopes of the input current across preparations. We found that IBI had a significant effect on Ipeak, Δpeak, slopeup and slopedown (all one-way RM-ANOVA on ranks; data included in Figure 2—source data 1). In particular, larger IBIs corresponded to larger Ipeak values (Figure 2F–2H; p<0.001, χ2 = 65.87) with smaller (more advanced) Δpeak (Figure 2I; p<0.001, χ2 = 41.35). The change in Δpeak was due to a decrease in slopeup (p<0.001, χ2 = 65.25), whereas slopedown did not vary as much (Figure 2J–2K; p=0.002, χ2 = 14.77).

### The burst onset phase of the LP neuron oscillation depends on its synaptic input

Injection of noise current revealed that the timing of the LP response is exquisitely sensitive to the duration and amplitude of inputs. In the intact system, the primary determinant of input duration and amplitude is the network period, as increasing period increases both presynaptic pacemaker burst duration (Hooper, 1997b; Hooper, 1997a) and synaptic strength (Manor et al., 1997; Nadim and Manor, 2000). To explore the effect of the duration and strength of the synaptic input, we used dynamic clamp to drive the LP neuron with a realistic synaptic conductance waveform.

We constructed this realistic waveform by measuring the synaptic current input to the LP neuron during ongoing pyloric oscillations (Figure 3A). These measurements showed the two components of inhibitory synaptic input: those from the pacemaker AB and PD neurons (left arrow) and those from the follower PY neurons (right arrow). In each cycle, the synaptic current always had a single peak, but the amplitude and phase of this peak showed variability across preparations (Figure 3B, average in blue).

![Figure 3.](https://cdn.elifesciences.org/articles/46911/elife-46911-fig3-v2.jpg)

**Figure 3.:** (A) The synaptic input to the LP neuron was measured by voltage clamping it at a holding potential of −50 mV during ongoing oscillations. The onset of the pacemaker (AB/PD) activity is seen as a kink in the synaptic current (ILP, blue). Dashed line: 0 nA. (B) Synaptic input averaged across (last 5 of 30) cycles from nine different LP neurons. Traces are aligned to the onset of the PD neuron burst (dotted vertical red line; see panel A), normalized by the cycle period and terminated at the end of the downslope (coincident with the first LP action potential when present). The blue trace shows the average. (C) An example of the LP neuron driven by the realistic synaptic waveform in dynamic clamp. The burst onset time (Δt) was measured relative to the AB/PD onset and used to measure the LP phase (φLP). gmax denotes the conductance amplitude. (D) Mean φLP (N = 9 preparations) shown as a function of P and fit with the function given by Equation (8) (fit values τs=26.0 ms, g*=0.021 µS and Δpeak·DC = 0.43). (E) Mean φLP plotted against gmax also shown with the fit to Equation (8) . (F) Heat map, obtained from fitting Equation (8) to the data in panels D and E, shows φLP as a function of both gmax and P. Black curves show the level sets of phase constancy for three values of φLP (0.47, 0.49, and 0.52).

The realistic conductance input was injected periodically with strength gmax (Figure 3C). For any fixed gmax, φLP decreased as a function of P (Figure 3D), that is the relative onset of the LP burst was advanced in slower rhythms. In contrast to the effect of P, for any given P, φLP increased sublinearly as a function of gmax (Figure 3E). Figure 3F combines the simultaneous influence of both parameters on φLP. The results shown in Figure 3D indicate that the LP neuron intrinsic properties alone do not produce phase constancy. However, level sets of φLP (highlighted for three values in Figure 3F), indicate that phase could be maintained over a range of P values, if gmax increases as a function of P. This finding was predicted by our previous modeling work, in which we suggested that short-term synaptic depression promotes phase constancy by increasing synaptic strength as a function of P (Manor et al., 2003; Bose et al., 2004). We will further discuss the role of synaptic depression below.

To clarify the results of Figure 3, it is worth examining the extent of phase maintenance for fixed gmax. An example of this is shown in Figure 4A (turquoise plots). A comparison of these data with the theoretical cases in which either delay or phase is constant suggests that the LP neuron produces relatively good phase maintenance, at least much better in comparison with constant delay. However, this conclusion is misleading because, in these experiments, the duty cycle of the synaptic input was kept constant. Therefore, most of the phase maintenance is due the fact that the synaptic input keeps perfect phase. In fact, if the reference point measures phase relative to the end –rather than onset– of the PD burst (Figure 4B), phase maintenance of the LP neuron is barely better than in the constant delay case (Figure 4A, purple plots). It is therefore clear that phase maintenance by the LP neuron would require the properties of the synaptic input to change as a function of P, a hallmark of short-term synaptic plasticity (Fortune and Rose, 2001; Grande and Spain, 2005). As mentioned above, short-term plasticity such as depression could produce changes in gmax as a function of P. Independently of gmax, the peak time of the synaptic current is another parameter that could change with P and influence the timing of the postsynaptic burst. We therefore proceeded to systematically explore the influence of P, gmax and the synaptic peak time on φLP.

![Figure 4.](https://cdn.elifesciences.org/articles/46911/elife-46911-fig4-v2.jpg)

**Figure 4.:** (A) The change in φLP values with P are compared with the constant phase (solid curve) and constant latency (dashed curve) extremes. Lime traces show the usual values of φLP, calculated from the LP burst onset latency with respect to the onset of the PD burst. Lavender traces show φLP calculated from the LP burst onset latency with respect to the end of the PD burst. Data shown are the same as in Figure 3D for gmax = 0.4 µS. (B) Schematic diagram shows the latency of LP burst onset measured with respect to the (estimated) onset and end of the PD burst in the dynamic clamp experiments (see Materials and methods). Bottom panel shows the synaptic current waveform measured in the voltage-clamped LP neuron during ongoing pyloric activity. Top panel shows the dynamic clamp injection of the synaptic conductance waveform into the LP neuron. The current waveform of the bottom panel is aligned to the conductance waveform of the top panel for the comparison used in determining the PD burst onset and end in the top panel.

### A systematic exploration of synaptic input parameters on the phase of the LP neuron

For a detailed exploration of the influence of the synaptic input on φLP, we approximated the trajectory of the (unitary) synaptic conductance in one cycle by a simple triangle (Figure 5A), which could be defined by three parameters: duration (Tact), peak time (tpeak) and amplitude (gmax) (Figure 5B). This simplified triangular synaptic conductance waveform could then be repeated with any period (P) to mimic the realistic synaptic input to the LP neuron. For a given synaptic duration Tact, the peak phase of the synapse can be defined as Δpeak=tpeak/ Tact). The parameter Δpeak is known to vary as a function of P (Tseng et al., 2014) and, in a previous study, we found that Δpeak may influence the activity of the postsynaptic neuron, independent of P and gmax (Mamiya and Nadim, 2004). We therefore systematically explored the influence of three parameters of the synaptic input (P, gmax and Δpeak) on φLP.

![Figure 5.](https://cdn.elifesciences.org/articles/46911/elife-46911-fig5-v2.jpg)

**Figure 5.:** (A) A triangle-shaped conductance was used to mimic the synaptic input to the LP neuron. (B) The triangular waveform can be described by period (P), duration (Tact), peak time (tpeak) and amplitude (gmax). (C) In dynamic clamp runs, the synapse duration Tact was kept constant at 300 ms (C-Dur) or maintained at a constant duty cycle (Tact/P) of 0.3 (C–DC) across all values of P. (D) Intracellular voltage recording of the LP neuron during a dynamic clamp stimulation run using the triangle conductance (in picrotoxin). The burst onset time (Δt, calculated in reference to the synaptic conductance onset) was used to calculate the activity phase (φLP = Δt/P).

As with the realistic synaptic waveforms (Figure 3), we used the dynamic clamp technique to apply the triangular conductance waveform periodically to the LP neuron in the presence of the synaptic blocker picrotoxin. Across different runs within the same experiment, the parameters P, gmax and Δpeak were changed on a grid (see Materials and methods). In addition, all combinations of these three parameter values were run in two conditions in the same experiment, 1: with constant duration, that is constant Tact across different P values (C-Dur of 300 ms), and 2: with constant duty cycle, that is Tact changing proportionally to P (C-DC of 0.3; Figure 5C). Using these protocols, we measured the effects of synaptic parameters on φLP (Figure 5D).

The LP neuron produced burst responses that followed the synaptic input in a 1:1 manner across all values of P that were used (Figure 6A1). When gmax and Δpeak were kept constant, φLP decreased as a function of P (Figure 6A2). This decrease was always larger for the C-Dur case than the C-DC case. For both C-DC and C-Dur, this trend was seen across all values of Δpeak and gmax (Figure 6A3). The effect of P on φLP was highly significant for both C-DC (three-way ANOVA, p<0.001, F = 100.677) and C-Dur (three-way ANOVA, p<0.001, F = 466.424), indicating that the period and duration of the inhibitory input to the LP neuron had a significant effect on its phase.

![Figure 6.](https://cdn.elifesciences.org/articles/46911/elife-46911-fig6-v2.jpg)

**Figure 6.:** Periodic injection of an inhibitory triangular waveform conductance into the LP neuron (in picrotoxin) produced bursting activity from which φLP was calculated. The parameters gmax, Δpeak and P were varied across runs for both C-Dur and C-DC cases. (A) φLP decreases as a function of P. (A1) Intracellular recording of an LP neuron showing a C-DC conductance input across five periods. (A2) φLP for the example shown in A1 plotted as a function of P (for gmax = 0.4 μS, Δpeak=0.5) for both C-Dur and C-DC cases. φLP decreases rapidly with P and the drop is larger for the C-Dur case. (A3) φLP decreased with P in both the C-DC case (three-way RM ANOVA, p<0.001, F = 100.7) and the C-Dur case (three-way RM ANOVA, p<0.001, F = 466.4) for all values of Δpeak. The range of φLP drop was greater for the C-Dur case compared to the C-DC case. (B) φLP increases as a function of gmax. (B1) Intracellular recording of an LP neuron showing the conductance input across three values of gmax. (B2) φLP for the example shown in B1 plotted as a function of P (for p=500 ms, Δpeak=0.25) shows a small increase for both C-Dur and C-DC cases. (B3) φLP increased with gmax in almost all trials for both C-DC and C-Dur cases and all values of Δpeak. (C) φLP increases as a function of Δpeak. (C1) Intracellular recording of the LP neuron showing the conductance input for five values of Δpeak. (C2) φLP for the example neuron in C1 plotted as a function of Δpeak (for p=500 ms, gmax = 0.4 μS) for both C-DC and C-Dur cases. (C3) φLP increased with Δpeak for both C-DC and C-Dur cases and for all values of gmax. In all panels, error bars show standard deviation.

Changing gmax produced a large effect on the level of hyperpolarization in the LP neuron, but this usually translated to only a small or modest effect on the time to the first spike following inhibition (Figure 6B1). Overall, increasing gmax at constant values of P and Δpeak produced a significant but only small to moderate increase in φLP (three-way ANOVA, p<0.001, F = 10.798). Although increasing gmax produced the same qualitative effect for both the C-DC and C-Dur (e.g., Figure 6B2), φLP in the C-DC case was restricted to a smaller range (Figure 6B3 top vs. bottom panels). Overall, this increase was robust for most values of P and Δpeak (Figure 6B3).

Increasing Δpeak for a constant value of P and gmax (Figure 6C1), produced a small but significant increase in φLP (three-way ANOVA, p<0.001, F = 17.172). This effect was robust for most values of P and gmax, for both C-DC and C-Dur (Figure 6C2 and C3).

These results showed that all three parameters that define the shape of the IPSC influence φLP. Clearly, the strongest effect is the decrease in φLP as a function of P. However, φLP modestly increases as a function of the other two parameters, gmax and Δpeak. This raised the question how gmax and Δpeak would have to change in coordination as a function of P to counteract the effect of P on φLP and achieve phase constancy.

### Coordinated changes of gmax and Δpeak produce the largest effect on phase

To explore how gmax and Δpeak might interact to influence φLP, we examined the sensitivity of φLP to these two parameters, individually and in combination, for all values of P in our data (see Materials and methods). Sensitivity of φLP to these two parameters varied across P values, with larger sensitivity at lower values of P (two-way RM-ANOVA, p<0.001, F = 16.054; data included in Figure 7—source data 1). For simplicity, we averaged the sensitivity values across different P values to obtain an overall measure of the influence of gmax and Δpeak. These results showed that, for the C-DC case, φLP had a positive sensitivity to gmax and a smaller positive sensitivity to Δpeak (Figure 7A). The sensitivity was largest if the two parameters were varied together (gmax + Δpeak) and smallest if they were varied in opposite directions (gmax - Δpeak; two-way RM-ANOVA, p<0.001, F = 3.330). Similarly, these sensitivity values were also significantly different for the C-Dur case (Figure 7B; two-way RM-ANOVA, p<0.001, F = 2.892), with largest sensitivity for gmax + Δpeak and smallest for gmax - Δpeak.

![Figure 7.](https://cdn.elifesciences.org/articles/46911/elife-46911-fig7-v2.jpg)

**Figure 7.:** (A) The sensitivity of φLP to local changes in gmax and Δpeak was averaged across all values of P for the C-DC case. Sensitivity was largest if both parameters were increased together (gmax + Δpeak) and smallest if they were varied in opposite directions (gmax - Δpeak; one-way RM-ANOVA, p<0.001, F = 3.330). (B) The same sensitivity analysis in the C-Dur case shows similar results (one-way RM-ANOVA, p<0.001, F = 2.892). In both panels, error bars show standard deviation.

### Level sets of φLP in the P-gmax-Δpeak space for C-DC and C-Dur cases

To search for phase constancy across different P values in our dataset, we expressed φLP as a function of the three IPSC parameters, P, gmax and Δpeak: $\phi_{LP}=Φ(P,g_{max},Δ_{peak})$. Figure 8 shows heat map plots of the function Φ, plotted for the range of values of P and Δpeak and four values of gmax. In these plots, phase constancy can be seen as the set of values in each graph that are isochromatic, indicating the level sets of the function Φ. These level sets are mathematically defined as hypersurfaces on which the function has a constant value: $Φ(P,g_{max},Δ_{peak})=\phi_{c}$. For the C-DC case, in each gmax section of the plot, the level sets (e.g. φc=0.34 denoted in white) spanned a moderate range of P values as Δpeak increased (Figure 8A1). The span of P values across all four panels indicates the range of cycle periods for which phase constancy could be achieved by varying gmax and Δpeak. This range of P values (spanned by the white curves) was considerably smaller for the C-Dur case (Figure 8A2).

![Figure 8.](https://cdn.elifesciences.org/articles/46911/elife-46911-fig8-v2.jpg)

**Figure 8.:** (A) Heat map plots of the function Φ (see Materials and methods), plotted for the range of values of P and Δpeak and 4 values of gmax for the C-DC (A1) and C-Dur (A2) cases. The white curves show the level set of φLP=0.34, shown as an example of phase constancy. The color maps are interpolated from sampled data (see Materials and methods; N = 9 experiments). The locations of the sampled data are marked by black dots. (B) Heat map for the level sets φLP=0.34 for the C-DC (B1) and C-Dur (B2) cases. Range of colors in each panel indicate the range of P values for which φLP could remain constant at 0.34 for each case, as indicated by the gray arrows on the side of the heatmap color legend. (C) The range (ΔP) of P values for which φLP could remain constant at any value between 0.2 and 0.8 for the C-DC (C1) and C-Dur cases (C2). Filled circles show the values shown in panel B. The LP neuron cannot achieve φLP values below 0.3 in the C-DC case. For φLP values between 0.3 and ~0.65, the range was larger in C-DC case.

For any constant phase value φc, these level sets can be expressed as

$$
P=P_{\phi_{c}}(g_{max},Δ_{peak}),
$$

which describes a surface in the 3D space, yielding the P value for which phase can be maintained at φc, for the given values of gmax and Δpeak. The level set indicated by the white curves in panel A for the C-DC case is plotted as a heat map in Figure 8B1 and can be compared with the same plot for the C-Dur case in Figure 8B2. The range of colors in each plot (marked next to each panel) indicates the range of P values for which phase can be kept at φc=0.34. To reveal how this range depends on the desired phase, we measured this range for all values of φc between 0.2 and 0.8 (Figure 8C1 and C2). We found that the LP neuron could not achieve phases below 0.3 in the C-DC case (Figure 8C1), which is simply because the neuron never fired during the inhibitory synaptic current (which had a duty cycle of 0.3). Furthermore, the range of P values for which the LP phase could be maintained by varying gmax and Δpeak was much larger for C-DC inputs compared to C-Dur Inputs, for all φc values between 0.31 and 0.54.

### A model of synaptic dynamics could predict activity onset phase of the LP neuron

To gain a better understanding of our experimental results, we derived a mathematical description of the phase of a follower neuron such as LP, based on the following assumptions: 1, that the firing time of this neuron was completely determined by its synaptic input, 2, that in each cycle the synaptic conductance gsyn increased to a maximum value gmax for a time interval Tact (the active duration of the synapse) and decayed to 0 otherwise, and 3, that the follower neuron remained inactive when gsyn was above some threshold g*. The derivation of this model is described in the Materials and methods.

This simple model provided a mathematical description of φLP as a function of P, gmax and ∆peak, for the C-Dur and C-DC cases. In the C-Dur case (Equation (7)), as P increased, φLP decayed and approached 0 like 1/P. In contrast, in the C-DC case (Equation (8)), φLP approached its lower limit Δpeak·DC, as P increased, and thus behaved very differently than in the C-Dur case.

We used these equations to describe gmax as a function of P (for any given Δpeak) so that LP maintained a constant phase φc, (Equation (10) for the C-DC case). Alternatively, Δpeak could be given as a function of P (for any given gmax, Equation (11) for the C-DC case). We used these derivations to compare how phase constancy depends on gmax or Δpeak in the C-DC case. A comparison of these two cases can be seen in Figure 9A, where either gmax (green) or Δpeak (blue) is varied to keep φLP constant at φc=0.34 across different P values. (The red curve is the depressing case, described below.) As the figure shows, phase constancy can be achieved by varying either parameter, but each parameter produces a different range of P across which phase is maintained.

![Figure 9.](https://cdn.elifesciences.org/articles/46911/elife-46911-fig9-v2.jpg)

**Figure 9.:** (A) For the C-DC case, a constant phase of φLP=0.34 can be maintained across a range of cycle periods P when gmax is constant (at 335 nS; blue plane) and Δpeak varies from 0 to 1 according to Equation (11) (blue), or when Δpeak is fixed (at 0.5; green plane) and gmax varies from 200 to 800 nS according to Equation (10). Alternatively, gmax and Δpeak can covary to maintain phase, as in a depressing synapse, where gmax varies with P according to Equation (16) , and Δpeak is calculated for each P and gmax value according to Equation (11). As seen in the 2D coordinate-plane projections of the 3D graph (right three graphs), the range of P values for which phase constancy is achieved is largest when gmax and Δpeak covary (dotted lines show limits of P for phase constancy). The depressing synapse conductance value is chosen to be 335 nS at P = 1 s. (B, C) A comparison between the C-DC and C-Dur cases shows that in the latter case a constant phase of φLP can be maintained across a larger range of P values when Δpeak increases with P (and gmax is fixed at 400 nS) according to Equation (11). The relationship of Δpeak and P is shown in B for φLP=0.34. (C) shows the range of P values (ΔP) of cycle periods for which phase remains constant at any value of φLP. If gmax also varies with P, as in a depressing synapse (red; Equation (16)), the range of P values for which phase is constant is further increased. (Dotted line: φLP=0.34.).

These equations and their corresponding counterparts for the C-Dur case can be used to calculate the range of P values over which changing Δpeak (from 0 to 1) can maintain a constant phase φc. If ΔP denotes the range of P values for which phase can be constant, it is straightforward to show that ΔPDC > ΔPDur (compare blue and black curves in Figure 9B and C; see Materials and methods for derivation).

Two additional points are notable in Figure 9C. First, the lower bound on φLP for which phase constancy can occur is smaller in the C-Dur (black) than the C-DC (blue) case. This is because we have assumed that in the C-DC case the LP neuron cannot fire during inhibition and therefore the constant value of DC produces a lower limit for φLP. Second, for φc larger than ~0.5, ΔP is larger for the C-Dur case. This occurs because Equation (12) can no longer be satisfied when φc is large. That is, with constant duty cycle, it is not possible to produce an arbitrarily large follower neuron phase, but with constant duration, any large phase is attainable if the cycle period is not much larger than the synaptic duration. These findings are consistent with our experimental results described above (see Figure 8).

The pacemaker synaptic input to the LP neuron shows short-term synaptic depression (Rabbah and Nadim, 2007). In a previous modeling study, we explored how the phase of a follower neuron was affected when the inhibitory synapse from an oscillatory neuron to this follower had short-term synaptic depression (Manor et al., 2003). In that study the role of the parameter Δpeak was not considered. We now consider how the presence of short-term synaptic depression influences phase constancy by changing both gmax and Δpeak. As stated in the Materials and methods (Equation (16)), the effect of synaptic depression on synaptic strength can be obtained as $g_{max}=g¯_{max}⋅s_{max}(P)$), where smax is an increasing function whose value approaches one as P increases. This indicates that the synapse becomes stronger due to more recovery from depression at longer cycle periods. When synaptic depression dictates how gmax varies with P and Δpeak also varies with P and gmax (Equation (11)), the simultaneous changes in gmax and Δpeak (red) greatly increase the range of P values over which φLP is constant (Figure 9A).

Note that the C-DC case with short-term depression spans a larger range of P values than the non-depressing case (Figure 9B). Similarly, the range of P values for which phase can be maintained is larger than the non-depressing case across φLP values, except where φLP is so large that the depressing synapse operates outside its dynamic range (Figure 9C). These results are consistent with our experimental results, indicating that although phase constancy can be achieved when either gmax or Δpeak increases with P, a concomitant increase of both - which could occur for example with a depressing synapse - greatly expands the range of P values for which a constant phase is maintained.

## Discussion

### The importance of phase in oscillatory networks

A common feature of oscillatory networks is that the activities of different neuron types are restricted to specific phases of the oscillation cycle. For example, different hippocampal and cortical neurons are active in at least three distinct phases of the gamma rhythm (Hájos et al., 2004; Hasenstaub et al., 2005), and distinct hippocampal neuron types fire at different phases of the theta rhythm and sharp wave-associated ripple episodes (Somogyi and Klausberger, 2005).

Experimental studies quantify the latency of neural activity with respect to a reference time in the cycle, but in most cases, these latencies are normalized and reported as phase. Distinct neuron types can maintain a coherent activity phase, despite wide variations in the network frequency (30–100 Hz for gamma rhythms, 4–7 Hz for theta rhythms, and 120–200 Hz for sharp wave-associated ripple episodes). Phase-specific activity of different neuron types is proposed to be important in rhythm generation (Wang, 2010), and indicates the necessity of precise timing for producing proper circuit output and behavior (Kopell et al., 2011). For example, phase locking of spike patterns to oscillations is important for auditory processing, single cell and network computations and Hebbian learning rules (Kayser et al., 2009; McLelland and Paulsen, 2009; Panzeri et al., 2010). For brain oscillations, phase relationships may provide clues about the underlying circuit connectivity and dynamics, but a behavioral correlate of varying frequencies is not obvious. In contrast, the activity phase of distinct neuron types in rhythmic motor circuits is a tangible readout of the timing of motor neurons and muscle contractions, thus defining phases of movement (Grillner and El Manira, 2015; Kiehn, 2016; Le Gal et al., 2017; Bidaye et al., 2018). Because meaningful behavior depends crucially on proper activity phases, whether neurons maintain their activity phase in face of changes in frequency simply translates to whether the movement pattern changes as it speeds up or slows down.

### Determinants of phase

In oscillatory networks, the activity phases of different neuron types depend to different degrees on the precise timing and strength of their synaptic inputs (Oren et al., 2006). Our results from noise current injections showed that the timing of the LP neuron is strongly dependent on the timing of inputs it receives. Dynamic clamp injection of realistic or triangular conductance waveforms with different periods (P) indicated that φLP was largely determined by the duration of the synaptic input. φLP changed substantially with P when inputs had constant duration, but much less when inputs had a constant duty cycle, that is when duration scaled with P. However, our experiments also showed that inputs of constant duty cycles alone are insufficient for phase constancy. φLP decreased with P even with a constant duty cycle of inputs, but increased with either synaptic strength (gmax) or peak phase of the synaptic input (Δpeak). The increase in φLP had similar sensitivity to gmax and Δpeak, and therefore a larger sensitivity to a simultaneous increase in both. Consequently, it was possible to keep φLP constant over a wide range of cycle periods by increasing both parameters with P.

The fact that an increase in gmax with P promotes phase constancy is biologically relevant, as short-term depression in pyloric synapses means that synaptic strength indeed increases with P (Manor et al., 1997). Previous modeling studies show that short-term synaptic depression of inhibitory synapses promotes phase constancy (Nadim et al., 2003; Bose et al., 2004), largely because of longer recovery times from depression at larger values of P.

The finding that an increase of Δpeak with P promotes phase maintenance is somewhat surprising, as we have previously shown that Δpeak in LP actually decreases with P (Manor et al., 1997; Tseng et al., 2014). On the face of it, this suggests that an increase in Δpeak is not a strategy employed in the intact circuit. However, the caveat is that such results may critically depend on the cause of the change in P, either experimentally or biologically. While in our current study we varied Δpeak with direct conductance injection into LP, previous results were obtained by changing the waveform and period of the presynaptic pacemaker neurons. When P is changed in an individual preparation by injecting current into or voltage-clamping the pacemakers, phase of follower neurons is not particularly well maintained. An example of this is shown in Figure 1, where φLP values fall between constant phase and constant duration and, additionally, all pyloric neurons show behavior that falls between constant phase and constant latencies (Hooper, 1997b; Hooper, 1997a). This may reflect that neurons are not keeping phase particularly well when the only cause of changing P is the presynaptic input. This is supported by the observation that even during normal ongoing pyloric activity, phases change with cycle-to-cycle variability of P in individual preparations (Bucher et al., 2005). However, it does not preclude the possibility that Δpeak plays an important role in stable phase relationships when P differs because of temperature, neuromodulatory conditions, or inter-individual variability (discussed below).

It is noteworthy that a change in the synaptic strength or peak phase with P is not peculiar to graded synapses. The fact that short-term synaptic plasticity can act as a frequency-dependent gain control mechanism is well known for many spike-mediated synaptic connections. In bursting neurons, the presence of a combination of short-term depression and facilitation in the same spike-mediated synaptic interaction could also result in changes in the peak phase of the summated synaptic current as a function of burst frequency and duration, and the intra-burst spike rate (Markram et al., 1998).

The mathematical model in the current study provides mechanistic explanations for several of our experimental findings. First, it can be used to produce a quantitative measure of phase, given the values of gmax, Δpeak and P. Thus, these equations can be used to compare the C-DC and C-Dur cases, which match our experimental results. They show that, for most phase values, the C-DC case provides a larger range of cycle periods at which phase constancy can occur. Second, these equations provide the activity phase no matter how the pacemaker synaptic input duration changes with cycle period. For instance, our experiments were conducted by changing synaptic input through sampling individual values of the parameter pairs gmax and Δpeak, and then calculating the resulting phase. We then used fitting to find level sets of constant phase (Figure 8). In contrast, when we combined our mathematical derivation here with previous results on the role of short-term synaptic depression (Bose et al., 2004), we could demonstrate how a neuronal circuit can naturally follow a level set of phase (Equation (7), (8), (15), (16)). Moreover, we showed that the combined increase in gmax and Δpeak with P produces a larger range of periods for phase constancy than increasing either parameter alone. In short, this mathematical formulation produces a simple quantitative distillation of our experimental results.

In this study, we did not explore the role of the intrinsic properties of the LP neuron on its phase. In separate experiments, we simultaneously measured post-inhibitory rebound properties in LP neurons and the levels of voltage-gated ionic currents (the transient potassium current IA and the hyperpolarization-activated inward current Ih) that influence rebound spiking. These data were not included in this study for brevity and because they showed that the timing of post-inhibitory spiking was relatively stable across preparations. Therefore, we would expect the contribution of intrinsic properties in controlling the timing of the LP neuron burst onset to be relatively small. However, this result does not generalize to all follower neurons. For example, the follower ventral dilator (VD) and PY neurons have a much higher levels of IA, which in turn has a larger effect on the timing of post-inhibitory spiking. In a set of computational studies, we addressed the role of IA in determining the burst phase in response to periodic inputs (Zhang et al., 2008; Zhang et al., 2009) and in conjunction with short-term depression in the synaptic input (Bose et al., 2004). An experimental clarification of the relative contribution of intrinsic properties vs. synaptic input could be done with controlled dynamic clamp synaptic input, such as those used in the current study, injected in PY or VD neurons. Such a data set would fittingly complement the results of the current study to elucidate more general rules in determining the activity phase of neurons in an oscillatory network.

### Phase relationships in changing temperatures

An interesting case is provided by the observation that phases are remarkably constant when pyloric rhythm frequency is changed with temperature. Tang et al. (2012) report a fourfold decrease in P of the pyloric rhythm between 7 and 23° C. In this study, none of the pyloric phases changed significantly, and it is worth noting that under conditions of changing temperatures, the relationships between P, gmax, and Δpeak appeared to be fundamentally different from when P is changed at a constant temperature. Presynaptic voltage trajectories scaled with changing P, and Δpeak of postsynaptic currents was independent of P, in contrast to the decrease described at constant temperature (Manor et al., 1997; Tseng et al., 2014). Amplitudes of synaptic potentials did not change with temperature, despite an increase in synaptic current amplitudes with increasing temperature (and associated decrease in P). This is in contrast to the positive relationship between gmax and P that results from synaptic depression at a constant temperature (Manor et al., 1997). Therefore, it appears that the likely substantial effects of temperature on synaptic dynamics and ion channel gating are subject to a set of compensatory adaptations different from when P is changed at constant temperature.

### Variability and slow compensatory regulation of phase

Phase maintenance in the face of changing P in an individual animal requires the appropriate short-term dynamics of synaptic and intrinsic neuronal properties. The fact that characteristic (and therefore similar) phase relationships can also be observed under the same experimental conditions across individual preparations is a different conundrum, particularly when P can vary substantially, as is true for brain oscillations (Hájos et al., 2004; Hasenstaub et al., 2005; Somogyi and Klausberger, 2005). Phases show different degrees of variability across individuals in a variety of systems, for example leech heartbeat (Wenning et al., 2018), larval crawling in Drosophila (Pulver et al., 2015), and fictive swimming in zebrafish (Masino and Fetcho, 2005), but in all these cases phases are not correlated with P. In the pyloric rhythm, phases are also variable to a degree across individuals, but not correlated with the mean P, which varies >2 fold (Bucher et al., 2005; Goaillard et al., 2009). This phase constancy occurs despite considerable inter-individual variability in ionic currents, and is considered the ultimate target of slow compensatory regulation, that is homeostatic plasticity (Marder and Goaillard, 2006; Ma and LaMotte, 2007; Marder et al., 2014). Slow compensation can also be observed directly when rhythmic activity is disrupted by decentralization, and subsequently recovers to similar phase relationships over the course of many hours (Luther et al., 2003). It is interesting to speculate if our findings about how synaptic parameters must change to keep phase constant would hold across individuals with different mean P. The prediction would be coordinated positive correlations of both gmax and Δpeak with P.

Synaptic inputs to the LP neuron show considerable variability across preparations (e.g. Figure 3B), which mirrors the variability seen in the levels of voltage-gated ionic currents in pyloric neurons (Schulz et al., 2006). We did not address the role and extent of variability in this study, because a proper analysis of variability required us to first establish the mechanisms that give rise to a consistent output, in this case phase constancy. Based on our findings regarding the influence of synaptic parameters on phase, a natural next step is to explore whether the variability of different parameters defining the synaptic input influences variability of phase or, alternatively, whether variability in some synaptic parameters may be irrelevant to phase or restrained by the postsynaptic neuron.

### Phase relationships under different neuromodulatory conditions

The flipside of the question how neurons maintain phase is the question how their phase can be changed. In motor systems, in particular, changes in phase relationships are functionally important to produce qualitatively different versions of circuit output, for example to produce different gaits in locomotion (Vidal-Gadea et al., 2011; Grillner and El Manira, 2015; Kiehn, 2016). The activity of neural circuits is flexible, and much of this flexibility is provided by modulatory transmitters and hormones which alter synaptic and intrinsic neuronal properties (Brezina, 2010; Harris-Warrick, 2011; Jordan and Sławińska, 2011; Bargmann, 2012; Marder, 2012; Bucher and Marder, 2013; Nadim and Bucher, 2014). The pyloric circuit is sensitive to a plethora of small molecule transmitters and neuropeptides which affect cycle frequency and phase relationships (Marder and Bucher, 2007; Stein, 2009; Daur et al., 2016). Indeed, extensive research has indicated the role of amine modulation of synaptic strength and neuronal firing phase in the pyloric circuit, and how amine modulation of synaptic and intrinsic firing properties changes firing phases (Johnson et al., 2003; Gruhn et al., 2005; Johnson et al., 2005; Peck et al., 2006; Harris-Warrick and Johnson, 2010; Harris-Warrick, 2011; Kvarta et al., 2012). With respect to our findings, any given neuromodulator could act presynaptically to alter P, duration, or duty cycle on the one hand, and gmax and Δpeak on the other. In addition, the neuromodulator could affect the postsynaptic neuron’s properties and alter its sensitivity to any of these parameters. Therefore, our findings could not just further our understanding of how phase can be maintained across different rhythm frequencies, but also provide a framework for testing if and how changes in synaptic dynamics may contribute to altering phase relationships under different neuromodulatory conditions.

## Materials and methods

Adult male crabs (Cancer borealis) were acquired from local distributors and maintained in aquaria filled with chilled (10–13°C) artificial sea water until use. Crabs were prepared for dissection by placing them on ice for 30 min. The dissection was performed using standard protocols as previously described (Tohidi and Nadim, 2009; Tseng and Nadim, 2010). The STNS, including the four ganglia (esophageal ganglion, two commissural ganglia, and the STG) and their connecting nerves, and the motor nerves arising from the STG, were dissected from the stomach and pinned into a Sylgard (Dow-Corning) lined Petri dish filled with chilled saline. The STG was desheathed, exposing the somata of the neurons for intracellular impalement. Preparations were superfused with chilled (10-13°C) physiological Cancer saline containing: 11 mM KCl, 440 mM NaCl, 13 mM CaCl2 · 2H2O, 26 mM MgCl2 · 6H2O, 11.2 mM Trizma base, 5.1 mM maleic acid with a pH of 7.4.

Extracellular recordings were obtained from identified motor nerves using stainless steel electrodes, amplified using a differential AC amplifier (A-M Systems, model 1700). One lead was placed inside a petroleum jelly well created to electrically isolate a small section of the nerve, the other right outside of it. For intracellular recordings, glass microelectrodes were prepared using the Flaming-Brown micropipette puller (P97; Sutter Instruments) and filled with 0.6 M K2SO4 and 20 mM KCl. Microelectrodes used for membrane potential recordings had resistances of 25–30 MΩ; those used for current injections had resistances of 15–22 MΩ. Intracellular recordings were performed using Axoclamp 2B and 900A amplifiers (Molecular Devices). Data were acquired using pClamp 10 software (Molecular Devices) and the Netsuite software (Gotham Scientific), sampled at 4–5 kHz and saved on a PC using a Digidata 1332A (Molecular Devices) or a PCI-6070-E data acquisition board (National Instruments).

Individual pyloric neurons were impaled and identified via their membrane potential waveforms, correspondence of spike patterns with extracellular nerve recordings, and interactions with other neurons within the network (Weimann et al., 1991).

### Constructing realistic graded IPSC waveforms

Inhibitory postsynaptic currents (IPSCs) were recorded from LP neurons during the ongoing rhythm using two-electrode voltage clamp and holding the LP neuron at −50 mV, far from the IPSC reversal potential of ~ −80 mV (Figure 3A). We refer to the total current measured in the voltage-clamped LP neuron during the activity of the PD and PY neurons as a synaptic current for the following reasons: 1, the after blocking the PTX-sensitive component of the pacemaker synapses, the LP neuron produces tonic spiking activity (see, for example Figure 2B), and 2, holding the LP neuron at different voltages (e.g. −60 or −110 mV) produces a similarly shaped current, but with a different amplitude or reversed sign (at −110 mV).

When the LP soma is voltage clamped at −50 mV, the axon (which is electrotonically distant from the soma) produced action potentials following the synaptic inhibition from the PY neuron and the pacemaker neurons. The onset of the LP neuron action potentials (recorded in the current trace) was used to calculate the mean IPSC for each experiment averaging the IPSCs over 10–20 cycles. The IPSC waveforms were then extracted by normalizing both the amplitude and the duration of the mean IPSC.

### Driving the LP neuron with noise current

In these experiments, the preparation was superfused in Cancer saline plus 10-5 M picrotoxin (PTX; Sigma Aldrich) for 30 min to block the synaptic currents to the LP neuron. The removal of synaptic inhibition onto LP neurons changed the activity of these neurons from bursting to tonic firing. Then, noise current, generated by the Ornstein-Uhlenbeck (O-U) process (Lindner, 2019), 60 min using the Scope software (available at http://stg.rutgers.edu/Resources.html, developed in the Nadim laboratory). The baseline of the noise current was adjusted by adding DC current so that it can provide enough inhibition to produce silent periods alternating with bursts of action potentials. The O-U process was defined as

$$
dX_{t}=−\frac{1}{\tau}X_{t}dt+\sigmadW_{t}.
$$

The parameters used for noise injection were τ = 10 to 20 ms, σ = 200 pA and a DC current of −200 to −100 pA. In these experiments, we defined bursts as groups of at least two action potentials with inter-spike intervals < 300 ms, following a gap of at least 300 ms.

### Driving the LP neuron with realistic or triangular IPSC waveforms in dynamic clamp

The dynamic clamp current was injected using the Netclamp software (Netsuite, Gotham Scientific). We pharmacologically blocked synaptic inputs from the pacemaker AB and follower PY neurons to the LP neuron by superfusing the perparation in Cancer saline plus 10-5 M picrotoxin (PTX; Sigma Aldrich) for 30 min. This treatment does not block the cholinergic synaptic input from the PD neurons for which no clean pharmacological blocker is known. Although the PD neuron input has some influence on the LP neuron activity, this input only constitutes <20% of the total pacemaker synapse and cannot drive oscillations in the follower LP neuron.

The LP neuron was driven in PTX with an artificial synaptic current in dynamic clamp. The synaptic current was given as

$$
I_{syn}=g_{syn}(V_{LP}−E_{syn})
$$

where the synaptic conductance gsyn was a pre-determined waveform, repeated periodically with period P, and Esyn was the synaptic reversal potential set to −80 mV (Zhao et al., 2011).

Two sets of dynamic clamp experiments were performed on different animals. In one set of experiments, gsyn was set to be a triangular waveform. We measured the effects of four different parameters in these triangle conductance injections (Figure 1): peak phase (Δpeak), duration (Tact), period (P = time between onsets of dynamic clamp synaptic injections), and maximal conductance (gmax, the peak value of gsyn). This allowed us to explore which combinations of the different parameters influences the LP phase. Five values for P were used: 500, 750, 1000, 1500, and 2000 ms, which cover the typical range of pyloric cycle periods. Three values of gmax were used: 0.1, 0.2 and 0.4 µS, consistent with previous measurements of synaptic conductance (Zhao et al., 2011; Tseng et al., 2014). The value of Δpeak was varied to be 0, 0.25, 0.5, 0.75 or 1. In the same experiment, all runs were done in two conditions: with Tact constant across different P values (C-Dur case with Tact = 300 ms) or with Tact changing proportionally to P (C-DC case with duty cycle DC =Tact/P=0.3).

In the other set of experiments, gsyn was a realistic IPSC waveform, based on a pre-recorded IPSC in the LP neuron. In these experiments, P was varied to be 500, 750, 1000, 1250, 1500, or 2000 ms by scaling the realistic waveform in the time direction. In these experiments, gmax was set to be 0.1, 0.2, 0.4, 0.6, or 0.8 μS. The LP neuron burst onset delay (Δt) was measured relative to the onset of the pacemaker component of the synaptic input (identified by the kink in the synaptic conductance waveform) in each cycle. The burst phase was calculated as φLP = Δt/P. Phase constancy means that Δt changed proportionally to P. To measure the LP neuron phase with respect to a new reference point, the end of the pacemaker input. This reference point was defined by drawing a horizontal line from the kink on the synaptic waveform that identified the onset of the pacemaker input, and chosing the first intersection point.

### Determining relationship between cycle period (P), synaptic strength (gmax) and LP phase (φLP) using the realistic IPSC waveform

We determined how well the mathematical model derived for constant input duty cycles (see Equation (8) below), matched the experimental data obtained with realistic IPSC waveforms. To this end, we fit the model to φLP values measured for all values of gmax and P, using the standard fitting routine 'fit' in MATLAB (Mathworks).

### Sensitivity of φLP to gmax and Δpeak across all P values

To explore how gmax and Δpeak may interact to influence φLP, we examined the sensitivity of φLP to these two parameters, individually and in combination, for all values of P in our data. For each P, we computed the mean value of φLP across all experiments, and all values of gmax (0.1, 0.2, 0.3 and 0.4 µS) and Δpeak (0, 0.25, 0.5, 0.75 or 1). (The φLP value for gmax = 0.3 µS was obtained in this case by linearly interpolating the values for 0.2 and 0.4 µS.) This produced a 4 by 5 matrix of all values. For each data point in the matrix, we moved along eight directions (+gmax, +Δpeak, –gmax, –Δpeak,+gmax and +Δpeak, –gmax and –Δpeak,+gmax and –Δpeak,+gmax and –Δpeak). Here "+” denotes increasing and “- “denotes decreasing. We then calculated the change in φLP per unit gmax (normalized by 0.4 µS), Δpeak, or both. For example, the sensitivity of φLP when Δpeak was changed from 0.25 to 0.5 was measured as

$$
\frac{\phi_{LP}(atΔ_{peak}=0.5)−\phi_{LP}(atΔ_{peak}=0.25)}{0.5−0.25}
$$

Similarly, the sensitivity of φLP when gmax was changed from 0.2 to 0.4 was measured as

$$
\frac{\phi_{LP}(atg_{max}=0.4)−\phi_{LP}(atg_{max}=0.2)}{(0.4−0.2)/0.4}
$$

These data are provided in Figure 7—source data 1. As the next step, we averaged the sensitivity along each aligned direction: [+gmax and –gmax]; [+Δpeak and –Δpeak]; [+gmax & +Δpeak and –gmax & –Δpeak]; [+gmax & –Δpeak and +gmax & –Δpeak]. This produced the four cardinal directions, shown in Figure 7. Finally, we averaged the sensitivity across all P values.

### A model of synaptic dynamics

In the derivation of the model, the firing time of the LP neuron was assumed to be completely determined by its synaptic input. This synaptic conductance (gsyn) was assumed to rise and fall with distinct time constants. The following holds over one cycle period and therefore time is reset with period P (t (mod P)):

$$
\frac{dg_{syn}}{dt}={(g_{max}−g_{syn})\tau_{r}t (modP)−g_{syn}/\tau_{s}t (modP)<t_{peak}\geqt_{peak}
$$

where the time tpeak, corresponding to ∆peak, is tpeak = Δpeak Tact. We assumed that LP neuron remained inactive when gsyn was above a fixed threshold (g∗) less than gmax. Because the synaptic input is periodic with period P, we solved for the minimum and maximum values of gsyn in each cycle. The minimum (glo) occurred just before the onset (t = 0) of AB/PD activity, whereas the maximum occurred at the peak synaptic phase ∆peak for the C-Dur case. In the C-DC case, Tact = DC ·P, where DC is the duty cycle (fixed at 0.3 in our experiments).

To calculate g*, we set the value t = 0 so that gsyn(0) = glo (and, by periodicity, gsyn(P)=glo), and solved the first part of Equation (1) where gsyn increases until t = tpeak. This yielded

$$
g_{peak}= g_{syn}(t_{peak}) = g_{max}+ (g_{lo}− g_{max})e^{−t_{peak}/\tau_{r}}
$$

We then used the second part of Equation (1) to track the decay of gsyn for tpeak <t < P:

$$
 g_{syn}(t) = g_{peak}e^{−(t−t_{peak})/\tau_{s}}
$$

Using Equation (3) , we calculated the time ∆t at which the synaptic conductance gsyn(∆t)=g∗ as follows:

$$
 g*=g_{peak}e^{−(Δt−t_{peak})/\tau_{s}}
$$

Solving Equation (4) for ∆t yielded

$$
Δt=\tau_{s}ln\frac{g(t_{peak})}{g*}+t_{peak}.
$$

Dividing this equation by P yielded φLP:

$$
\phi_{LP}=F(P,g_{max},Δ_{peak})=\frac{\tau_{s}}{P}ln\frac{g_{peak}}{g*}+\frac{t_{peak}}{P},
$$

where gpeak is given by Equation (2) . This expression provides a description of the dependence of φLP as a function of P, gmax and Δpeak. To explore the role of the parameters in this relationship, we made a simplifying assumption that the synaptic conductance gsyn(t) rapidly reached its peak (i.e., τr was small), stayed at this value and started to decay at t = tpeak. In this case g(t)=gmax on the interval (0,tpeak) and the value of glo is irrelevant. With this assumption, Equation (5) reduced to

$$
\phi_{LP}=\frac{\tau_{s}}{P}ln\frac{g_{max}}{g^{*}}+\frac{t_{peak}}{P}.
$$

Substituting tpeak = Δpeak·Tact in Equation (6) , gave

$$
\phi_{LP}=F(P,g_{max},Δ_{peak})=\frac{1}{P}(\tau_{s}ln\frac{g_{max}}{g*}+Δ_{peak}T_{act}),
$$

which we used to describe the LP phase in the C-Dur case. To describe the C-DC case, after substituting tpeak = Δpeak·DC·P, we obtained

$$
\phi_{LP}=F(P,g_{max},Δ_{peak})=\frac{1}{P}(\tau_{s}ln\frac{g_{max}}{g*})+Δ_{peak}DC.
$$

Note that these equations also describe the relationship between φLP with Tact in the C-Dur case, and DC in the C-DC case).

Equations (7), (8) and can be used to approximate a range of parameters over which φLP is maintained at a constant value φc. To do so, we assumed a specific parameter set, say $(P^,g^_{max},Δ^_{peak})$, satisfies

$$
F(P^,g^_{max},Δ^_{peak})=\phi_{c},
$$

for some fixed phase value, φc. We could now ask whether there are nearby parameters for which phase remains constant, that is F remains equal to φc. The Implicit Function Theorem (Krantz and Parks, 2012) guarantees that this is the case, provided certain derivatives evaluated at $(P^,g^_{max},Δ^_{peak})$ are non-zero, which turns out to be true over a large range of parameters. Since the partial derivative with respect to ∆peak of F(P,gmax,∆peak) at this point is a non-zero constant equal to Tact/P (or DC) in the C-Dur (or C-DC) case, there is a function ∆peak = h(P,gmax) such that

$$
F(P,g_{max},h(P,g_{max}))=\phi_{c}
$$

for values of P and gmax near $(P^,g^_{max})$. In other words, the Implicit Function Theorem guarantees that small changes in P and gmax can be compensated for by an appropriate choice of Δpeak in order to maintain a constant LP phase. A similar analysis can be done by solving for gmax in terms of P and Δpeak or by solving for P in terms of gmax and ∆peak.

Keeping gmax (respectively, Δpeak) constant in these equations allows us to obtain a relationship between P and Δpeak (respectively, gmax), for which φLP is kept constant at φc. Consider Equations (7), (8) and for fixed values of both φLP (= φc) and gmax. Then these equations reduce to simple functional relationships where Δpeak can be expressed as a function of P. In the C-DC case, for example, evaluating Δpeak from Equation (8) produces

$$
g_{max}=g*⋅exp(\frac{P}{\tau_{s}}(\phi_{c}−Δ_{peak}DC))
$$

Equation (10) describes how gmax must vary with P for the system to maintain a constant phase φc for any given Δpeak.

Alternatively, Δpeak can be expressed as a function of P. In the C-DC case, evaluating Δpeak from Equation (8) produces

$$
Δ_{peak}=\frac{\phi_{c}}{DC}−\frac{\tau_{s}}{DC⋅P}ln\frac{g_{max}}{g*},
$$

Equation (11) can be used to calculate the range of P values over which changing Δpeak (from 0 to 1) can maintain a constant phase φc. Solving 0 < Δpeak <  1 using Equation (11) yields

$$
\frac{\tau_{s}}{\phi_{c}}ln\frac{g_{max}}{g*}<P_{DC}<\frac{\tau_{s}}{\phi_{c}−DC}ln\frac{g_{max}}{g*}
$$

Performing the same procedure in the C-Dur case, we find

$$
\frac{\tau_{s}}{\phi_{c}}ln\frac{g_{max}}{g*}<P_{Dur}<\frac{T_{act}}{\phi_{c}}+\frac{\tau_{s}}{\phi_{c}}ln\frac{g_{max}}{g*}.
$$

The lower limits of the two cases (PDC and PDur) are the same. The upper limit for PDC is larger than that of PDur if

$$
\phi_{c}<DC(1+\frac{\tau_{s}}{T_{act}}ln\frac{g_{max}}{g*}).
$$

If ΔP denotes the range of P values that respectively satisfy Equation (12) or (13), then ΔPDC > ΔPDur if the inequality given by holds, which it does for true for τs and gmax large enough.

### Adding synaptic depression to the model of synaptic dynamics

In a previous modeling study, we explored how the phase of a follower neuron was affected when the inhibitory synapse from an oscillatory neuron to this follower had short-term synaptic depression (Manor et al., 2003). In that study the role of the parameter Δpeak was not considered. It is straightforward to add synaptic depression to Equations (7), (8) and therefore examine how phase is affected if Δpeak increases with P and synaptic strength also changes with P according to the rules of synaptic depression. We will restrict this section to the C-DC case. A similar derivation can be made for the C-Dur case.

An ad hoc model of synaptic depression can be made using a single variable sd which will be a periodic function that denotes the extent of depression and takes on values between 0 and 1 (Bose et al., 2004). sd decays during the AB/PD burst (from time 0 to Tact, indicating depression) and then recovers during the inter-burst interval (from Tact to P, indicating recovery). Thus, sd can be described by an equation of the form:

$$
\frac{ds_{d}}{dt}={−s_{d}/\tau_{\beta}t (mod​ P)\leqT_{act} (1−s_{d})/\tau_{\alpha}T_{act}<t (mod​ P)<P 
$$

Using periodicity, it is straightforward to show that the maximum value of sd, which occurs at the start of the AB/PD burst, is given by:

$$
s_{max}(P)=\frac{1−e^{−P(1−DC)/\tau_{\alpha}}}{1−e^{−P(1−DC)/\tau_{\alpha}}e^{−DC⋅P/\tau_{\beta}}}.
$$

Note that smax is a monotonically increasing function with values between 0 and 1. Its value approaches one as P increases, indicating that the synapse becomes stronger. For a complete derivation and description, see Bose et al. (2004). The effect of synaptic depression on synaptic strength can be obtained by setting

$$
g_{max}=g¯_{max}⋅s_{max}(P)
$$

where smax is given by Equation (15).

### Software, analysis and statistics

Data were analyzed using MATLAB scripts to calculate the time of burst onset and the phase. Statistical analysis was performed using Sigmaplot 12.0 (Systat). Significance was evaluated with an α value of 0.05, error bars and error values reported denote standard error of the mean (SEM) unless otherwise noted.
