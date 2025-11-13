# A molecular filter for the cnidarian stinging response

## Authors

- Keiko Weir<sup>1</sup> ([ORCID: 0000-0002-2501-9352](https://orcid.org/0000-0002-2501-9352))
- Christophe Dupre<sup>1</sup> ([ORCID: 0000-0002-5929-8492](https://orcid.org/0000-0002-5929-8492))
- Lena van Giesen<sup>1</sup>
- Amy S-Y Lee<sup>2</sup> ([ORCID: 0000-0002-4121-0720](https://orcid.org/0000-0002-4121-0720))
- Nicholas W Bellono<sup>1</sup> ([ORCID: 0000-0002-0829-9436](https://orcid.org/0000-0002-0829-9436)) †

### Affiliations

1. Department of Molecular and Cellular Biology, Harvard University Cambridge United States
2. Department of Biology, Brandeis University Waltham United States

† Corresponding author

## Abstract

All animals detect and integrate diverse environmental signals to mediate behavior. Cnidarians, including jellyfish and sea anemones, both detect and capture prey using stinging cells called nematocytes which fire a venom-covered barb via an unknown triggering mechanism. Here, we show that nematocytes from Nematostella vectensis use a specialized voltage-gated calcium channel (nCaV) to distinguish salient sensory cues and control the explosive discharge response. Adaptations in nCaV confer unusually sensitive, voltage-dependent inactivation to inhibit responses to non-prey signals, such as mechanical water turbulence. Prey-derived chemosensory signals are synaptically transmitted to acutely relieve nCaV inactivation, enabling mechanosensitive-triggered predatory attack. These findings reveal a molecular basis for the cnidarian stinging response and highlight general principles by which single proteins integrate diverse signals to elicit discrete animal behaviors.

## Introduction

Jellyfish, sea anemones, and hydrozoans of the Cnidarian phylum use specialized cells called cnidocytes to facilitate both sensation and secretion required for prey capture and defense (Watson and Mire-Thibodeaux, 1994b). Two major types of cnidocytes contribute to prey capture by the tentacles of the starlet sea anemone (Nematostella vectensis, Figure 1A): (1) spirocytes, anthozoan-specific cells that extrude a thread-like organelle to ensnare prey, and (2) nematocytes, pan-cnidarian cells which eject a single-use venom-covered barb to mediate stinging (Babonis and Martindale, 2017). Sensory cues from prey act on nematocytes to trigger the explosive discharge of a specialized organelle (nematocyst) at an acceleration of up to 5.41 × 106 g, among the fastest of any biological process (Holstein and Tardent, 1984; Nüchter et al., 2006; Figure 1B). The nematocyst can only be discharged once and therefore stinging represents an energetically expensive process that is likely tightly regulated (Watson and Mire-Thibodeaux, 1994b, Babonis and Martindale, 2014). Indeed, simultaneously presented chemical and mechanical (chemo-tactile) cues are required to elicit nematocyte discharge (Pantin, 1942a; Watson and Hessinger, 1989; Watson and Hessinger, 1992; Anderson and Bouchard, 2009). Electrical stimulation of nematocytes increases the probability of discharge in a calcium (Ca2+)-dependent manner (Anderson and Mckay, 1987; McKay and Anderson, 1988; Santoro and Salleo, 1991; Gitter et al., 1994; Watson and Hessinger, 1994a; Anderson and Bouchard, 2009), but direct recordings from nematocytes are limited and thus mechanisms by which environmental signals control discharge are not well studied.

![Figure 1.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig1-v1.jpg)

**Figure 1.:** (A) Starlet sea anemone (Nematostella vectensis). Scale bar = 3 mm. (B) Intact (yellow) and discharged nematocyte (blue). Scale bar = 20 μm. (C) Left: Representative patch clamp experiments from a nematocyte and tentacle neuron. Scale bar = 10 μm. Right: Nematocyte or neuron voltage-gated currents elicited by a maximally activating voltage pulse following 1 s pre-pulses to −110 mV (max current), −90 mV (colored), or 0 mV (inactivated, no current). (D) Nematocyte voltage-gated currents inactivated at very negative voltages compared with neurons. Nematocyte inactivation occurred at voltages more negative than could be measured compared with a sigmoidal inactivation relationship in neurons: nematocyte estimated Vi1/2 = -100.2 ± 0.4mV, n = 13 and neuron Vi1/2 = -70.8 ± 1.0mV, n = 9. Apparent activation thresholds were similar (Figure 1—figure supplement 1A). (E) Nematocyte voltage-gated currents elicited by −40 mV and 0 mV pulses were abolished in absence of external Ca2+ and blocked by cadmium (Cd2+). Representative of n = 4 for 0 Ca2+ and three for Cd2+, p<0.001 paired two-tailed student’s t-test. (F) Nematocyte voltage-gated currents were Ca2+-sensitive. Substitution of extracellular Ca2+, but not Na+ for NMDG+, affected the reversal potential. n = 3–4, p<0.001 for 5 mM Ca2+ versus other conditions, one-way ANOVA with post-hoc Tukey test. (G) Nematocyte discharge was minimal or absent in response to mechanical stimulation alone (n = 11, 3.3 mM Ca2+). In the presence of prey extract, mechanically evoked discharge was similar in standard and higher concentration of extracellular Ca2+ (n = 8 for 3.3 mM Ca2+, n = 5 for 10 mM) and blocked by Cd2+ (n = 8) or the removal of extracellular Ca2+ (n = 15). Discharged nematocysts embedded in presented gelatin-coated coverslips were quantified. p<0.001 for + prey with 3.3 or 10 mM Ca2+ versus other conditions, one-way ANOVA with post-hoc Bonferroni test. Data represented as mean ± sem.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Voltage-gated currents from a nematocyte and tentacle neuron elicited by −40 mV or 0 mV pulses. Conductance-voltage curves: nematocyte Va1/2 = -24.0 ± 0.5mV, n = 10 and neuron Va1/2 = -38.6 ± 0.6mV, n = 7. (B) Peak current density elicited by 0 mV pulse in nematocytes (n = 5), neurons (n = 6), and non-neuronal cells (n = 3). (C) Inward currents activated and inactivated more slowly in nematocytes compared with neurons. n = 10 nematocytes, 11 neurons. p<0.0001 two-tailed student’s t-test. (D) Nematocyte inward currents inactivated more quickly with repetitive stimulation compared with neurons. Protocol: 3.33 Hz stimulation with 20 ms pulses to −10 mV from −90 mV. n = 4 of each cell type, multiple row two-tailed student’s t-test with significance of p<0.05 by sweep five and p<0.0001 by 120. (E) Inactivation of inward currents does not vary with external Ca2+. 0.5 mM Ca2+ estimated Vi1/2 = -100.2 ± 0.4mV, n = 13, from Figure 1. 5 mM Ca2+ estimated Vi1/2 = -99.8 ± 0.9mV, n = 3. Data represented as mean ±sem.

Here, we demonstrate that nematocytes from Nematostella vectensis use a specialized Cav2.1 voltage-gated calcium channel orthologue (nCaV) to integrate dynamic voltage signals produced by distinct sensory stimuli. We show nematocytes are intrinsically mechanosensitive but nCaV exhibits unique voltage-dependent inactivation that basally inhibits cellular activity, thereby preventing responses to extraneous mechanical stimuli, such as background water turbulence. We further show that sensory neurons make synaptic contact with nematocytes, and the neurotransmitter acetylcholine (ACh) elicits a hyperpolarizing response that relieves nCaV inactivation to allow for subsequent cellular stimulation and chemo-tactile-elicited discharge. Thus, we propose that the specialized voltage dependence of nCaV acts as a molecular filter for sensory discrimination.

## Results

### Nematocyte CaV channels

We first obtained whole-cell patch clamp recordings from acutely dissociated nematocytes to investigate nematocyte signal transduction. Using intracellular cesium (Cs+) to block potassium (K+) currents revealed a voltage-gated inward current that was activated by positive or depolarized membrane voltages (ICaV, Figure 1C). In response to sustained positive voltage, voltage-activated ion channels enter a non-conducting, inactivated state and cannot be activated until returned to a resting state by negative membrane voltage. This property generally serves to limit responses to repetitive or prolonged stimulation, similar to receptor desensitization. Remarkably, ICaV began to inactivate at voltages more negative than we could technically measure, thus demonstrating an unusual voltage sensitivity of this conductance (Figure 1C,D). To determine whether these properties were specific to nematocytes, we used a transgenic sea anemone with fluorescently labeled neurons to facilitate direct comparison between these excitable cell types (Nakanishi et al., 2012; Figure 1C). Neuronal voltage-gated currents had a lower threshold for activation and exhibited much weaker voltage-dependent inactivation (Figure 1C,D, Figure 1—figure supplement 1A–D), similar to currents found in neurons of other animals (Hille, 2001), indicating that nematocytes exhibit unusual voltage-dependent properties. Ion substitution and pore blocker experiments confirmed ICaV is a Ca2+-sensitive current (Figure 1E,F), consistent with the contribution of extracellular Ca2+ to chemo-tactile-induced discharge (Watson and Hessinger, 1994a; Gitter et al., 1994; Figure 1G). Increased concentrations of extracellular Ca2+ did not affect inactivation of ICaV (Figure 1—figure supplement 1E), suggesting the enhanced voltage-dependent inactivation is intrinsic to the channel complex. This observation is important because it suggests ICaV renders nematocytes completely inactivated at typical resting membrane voltages and thus cells could not be stimulated from resting state.

To identify the ion channel mediating ICaV, we generated a tentacle-specific transcriptome and aligned reads from nematocyte-enriched cells (Sunagar et al., 2018). This strategy allowed us to search for differentially expressed transcripts that might encode CaV channel subunits (pore-forming α and auxiliary β and α2δ subunits). The orthologue of cacnb2, a β subunit of CaV channels, was the highest expressed CaV transcript in nematocyte-enriched cells, with levels 14-fold higher than other cells in the sea anemone (Figure 2A). β subunits can modulate voltage-dependence and trafficking in diverse ways depending on their splice isoform, interacting subunits, and cellular context (Buraei and Yang, 2010). Importantly, β subunits only interact with α subunits of high voltage-activated (HVA) calcium channels (Perez-Reyes, 2003). In agreement with robust β subunit expression, we found significant enrichment for cacna1a, the pore-forming subunit of HVA CaV2.1, and high expression of cacna2d1 (Figure 2—figure supplement 1A,B). These observations are consistent with a previous report demonstrating specific expression of cacna1a in nematocytes of sea anemone tentacles and expression of β subunits in nematocytes from jellyfish (Bouchard et al., 2006; Moran and Zakon, 2014; Bouchard and Anderson, 2014). Expression of cacna1h, which does not interact with auxiliary subunits (Buraei and Yang, 2010), was also observed, albeit at lower levels and across all cells (Figure 2—figure supplement 1A). Thus, it remains possible that voltage-gated currents in nematocytes are not carried exclusively by one CaV subtype.

![Figure 2.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig2-v1.jpg)

**Figure 2.:** (A) CaV channel complex with α, β, and α2δ subunits. mRNA expression (transcripts per million, TPM) of voltage-gated calcium (CaV) channel β subunits in nematocyte-enriched cells (blue) and non-enriched cells (grey). n = 6, p<0.0001 for cacnb2.1 in nematocytes versus other cells, two-way ANOVA with post-hoc Bonferroni test. (B) Heterologously-expressed nCav channels (Nematostella cacna1a, cacnb2, cacna2d1) inactivated at very negative voltages (estimated Vi1/2 = -101.5 ± 1.6mV, n = 5) versus mammalian orthologues (mCaV, Vi1/2 = -20.9 ± 3.4mV, n = 10). Apparent activation thresholds were the same: nCaV Va1/2 = -9.8 ± 0.3mV, n = 5, mCaV Va1/2 = -10.4 ± 0.5mV, n = 9. Inactivation was measured in response to 1 s pre-pulses from −110 mV to 10 mV with an inter-sweep holding potential of −90 mV. (C) nCaV exhibited slow inactivation with −70 mV holding potential (0.2 Hz stimulation, 5 s inter-pulse interval) that was best fit by two exponential functions with time constants of 10.0 and 369.5 s. n = 6, multiple row two-tailed student’s t-test with significance of p<0.05 by 15 s and p<0.0001 by 500 s. (D) nCav inactivated at −40 mV and quickly recovered at negative holding potentials. n = 7 for nCaV, n = 6 for mCaV. (E) Voltage-gated currents recorded from nCaV or mCaV following a −110 mV pre-pulse, −50 mV pre-pulse (colored), and 20 mV pre-pulse. CaV β subunits were substituted as indicated (mammalian β in red and Nematostella β in blue). Scale bars = 100 pA, 25 ms. (F) Mammalian β shifts nCaV voltage-dependent inactivation to positive voltages. nCaV Vi1/2 = -73.2 ± 1.2mV, n = 6. nCaV + mβ=−16.9 ± 1.9 mV, n = 6. (G) Half maximal inactivation voltage (Vi1/2) for CaV chimeras. p<0.0001 for nCaV versus nCaV + mβ, mCaV versus mCaV + nβ, one-way ANOVA with post-hoc Tukey test. Inactivation was measured in response to pre-pulses from −100 mV to 10 mV with an inter-sweep holding potential of −110 mV to reduce slow inactivation. Data represented as mean ±sem.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) mRNA expression (transcripts per million, TPM) of voltage-gated calcium (CaV) channel α and α2δ subunits in nematocyte-enriched cells (blue) versus non-enriched cells (grey). n = 6, p<0.01 for cacna1a in nematocytes versus other cells, two-way ANOVA with post-hoc Bonferroni test. Expression of other subunits was not significantly different. (B) Sequence alignment of Nematostella and Mus musculus α subunits at the α interaction domain (AID). Red letters indicate important regions for beta subunit interaction, underlined letters are critical for interaction. (C) Representative voltage-activated currents from HEK-293 cells expressing wild-type or chimeric CaV channels with specific combinations of mammalian and Nematostella subunits. Currents were elicited by 0 mV pulses from −110 mV. (D) Half maximal activation voltage (Va1/2) was similar for CaV chimeras. n = 6 nCaV, 6 nCaV + mβ, 10 mCaV, 10 mCaV + nβ, 6 mCaV + nα, 6 mCaV + nα2δ. (E) Left: Rise time of voltage-activated inward current. Right: Relative fraction of inward current remaining after a 200 ms step to 0 mV (R200). n = 6 nCaV, 6 nCaV + mβ, 10 mCaV, 14 mCaV + nβ, 6 mCaV + nα, 7 mCaV + nα2δ. (F) nCaV inactivated more quickly than mCaV. Protocol: 3.33 Hz stimulation with 20 ms pulses to −10 mV from −90 mV. n = 5 nCaV, 6 mCaV, multiple row two-tailed student’s t-test with significance of p<0.05 by sweep two and p<0.0001 by 120. (G) Inactivation curves of mCaV + nβ were similar when external Ca2+ (Vi1/2 = -54.4 ± 1.8mV, n = 10) was replaced with Ba2+ (Vi1/2 = -57.0 ± 0.9mV, n = 6). (H) nCaV exhibited relatively little slow inactivation from −110 mV compared with −70 mV holding potential (Figure 2, 0.2 Hz stimulation, 5 s inter-pulse interval). Data represented as mean ±sem.

Heterologous expression of Nematostella CaV (nCaV: cacna1a, cacnb2, and cacna2d1) produced voltage-gated currents with an apparent activation threshold nearly identical to the CaV complex made from respective mammalian orthologues (mCaV, Figure 2B, Figure 2—figure supplement 1C,D). Both channels had similar activation kinetics, but fast inactivation was significantly pronounced in nCaV, resembling native ICaV (Figure 2E, Figure 2—figure supplement 1E). Importantly, nCaV voltage-dependent inactivation was greatly enhanced compared with mCaV, regardless of the charge carrier (Figure 2B, Figure 2—figure supplement 1F,G). Similar to ICaV, nCaV exhibited unusually-sensitive voltage-dependence and began to inactivate at voltages more negative than we could measure with an estimated midpoint inactivation voltage (Vi1/2)~80 mV more negative than mCaV (Figure 2B). Even with a holding potential of −70 mV, nCaV exhibited slow inactivation resulting in a drastic decrease in responses to depolarizing stimuli over time (Figure 2C). This slow inactivation was largely prevented by adjusting the holding potential to −110 mV, suggesting inactivation occurs when channels are in a closed-state at potentials near or more negative than typical resting membrane potential (Figure 2—figure supplement 1H). Importantly, nCaV rapidly recovered from inactivation, demonstrating that channels could be reset for subsequent activation following brief exposure to negative voltage (Figure 2D). These distinctive features closely match the unique properties of native ICaV, suggesting nCaV forms the predominant CaV channel in nematocytes.

To determine the molecular basis for nCaV inactivation, we analyzed chimeric CaV complexes containing specific α, β, and α2δ1 subunits from nCaV or mCaV orthologues. Using a holding potential of −110 mV to compare voltage-dependent inactivation, we found that only transfer of the β subunit significantly affected voltage-dependent inactivation, while α or α2δ1 subunits produced minimal effects on voltage-dependent activation, inactivation, or kinetics (Figure 2E, Figure 2—figure supplement 1C–E). Indeed, other β subunits can induce significant hyperpolarized shifts in inactivation of HVA CaV channels (Yasuda et al., 2004). In this case, the mCaV β subunit drastically shifted nCaV inactivation by ~56 mV in the positive direction, prevented complete inactivation, and produced slower fast inactivation (Figure 2E–G, Figure 2—figure supplement 1E). Furthermore, nCaV β was sufficient to confer greatly enhanced voltage-dependent inactivation to mCaV (Figure 2E,G). From these results, we conclude that nCaV β, the most enriched CaV subunit in nematocytes, confers nCaV’s uniquely-sensitive voltage-dependent inactivation.

### Nematocyte excitability

Because electrical stimulation has been implicated in nematocyte discharge and some nematocytes can produce action potentials (Anderson and Mckay, 1987; McKay and Anderson, 1988; Anderson and Bouchard, 2009), we used current-clamp to record the electrical responses of nematocytes to depolarizing stimuli. Under our conditions, nematocytes had a resting potential of −64.8 ± 8.9 mV and did not produce a voltage spike when injected with current from rest (Figure 3A). We further considered that the strong voltage-dependent inactivation of ICaV could prevent excitability. Consistent with this idea, when nematocytes were first hyperpolarized to −90 mV and subsequently stimulated by current injection, we observed a singular long voltage spike (Figure 3B,C). In contrast, tentacle neurons produced multiple narrow spikes when injected with equivalent current amplitudes from a similar resting voltage, consistent with other neural systems (Figure 3A–C). Differences in spike width and frequency appear suited to mediate distinctive cellular functions: dynamic information processing in neurons and a single robust discharge event in nematocytes. Furthermore, these results indicate strong voltage-dependent inactivation prevents nematocyte activation from rest.

![Figure 3.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig3-v1.jpg)

**Figure 3.:** (A) Depolarizing current injection only elicited spikes from nematocytes first hyperpolarized to relieve inactivation. Nematocyte spike amplitude: 0 mV at rest, 41.5 ± 2.2 mV from ~−90 mV. n = 8, p<0.0001 two-tailed paired student’s t-test. In contrast, tentacle neurons spiked from rest (31.5 ± 1.7 mV, n = 4). (B) Current injection elicited long singular spikes from nematocytes and numerous narrow spikes from neurons. (C) Nematocytes and neurons had similar resting membrane potentials but distinct spike width. n = 8 nematocytes, n=4 neurons, p<0.01, two-tailed student’s t-test. Nematocytes produced only one spike, regardless of injection amplitude (n = 8), whereas neurons produced varying spike frequency depending on injection amplitude (n = 4). p<0.0001 two-way ANOVA with post-hoc Bonferroni test. Data represented as mean ±sem.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) In the presence of intracellular K+, voltage-activated outward currents were elicited from nematocytes and tentacle neurons. (B) Current-voltage relationships of peak transient and sustained (end of 200 ms voltage pulse) currents in nematocytes and neurons. n = 7. (C) Nematocytes exhibited a lower ratio of sustained/transient outward current, indicating faster inactivation of outward current. n = 7, p<0.01 two-tailed student’s t-test. (D) Nematocyte transient outward currents exhibited strong voltage-dependent inactivation compared with weak voltage-dependent inactivation of outward currents in neurons. n = 5, p<0.0001 for voltages at −100 mV or above, two-way ANOVA with post-hoc Bonferroni test. (E) Transient K+ currents in nematocytes were assessed using voltage protocols to enhance the outward current sensitive to voltage-dependent inactivation. These currents were abolished by the K+ channel blocker TEA+ (n = 4), the intracellular Ca2+ chelator BAPTA (n = 4), or in the absence of external Ca2+ (replaced with NMDG+ + EGTA, n = 3). p<0.0001 for currents measured following pre-pulses to −110 or −100 mV, two-way ANOVA with post-hoc Bonferroni test. Smaller sustained outward currents measured following more positive pre-pulses were significantly affected by TEA+ but not other treatments. (F) mRNA expression (transcripts per million, TPM) of Ca2+-activated K+ channels in nematocyte-enriched cells. n = 6. (G) Nematocyte spike width and resting membrane potential were affected by the presence of intracellular Cs+. Cells were first hyperpolarized to elicit spikes with subsequent current injection. Spike width: n = 8 K+ (from Figure 3) and 3 Cs+, p<0.05 two-tailed student’s t-test. Resting membrane voltage: n = 12 K+ (from Figure 3) and 3 Cs+, p<0.01 two-tailed student’s t-test. Data represented as mean ±sem.

K+ channels contribute to resting membrane voltage (estimated reversal potential for nematocyte K+ is ~−100 mV) and often modulate repolarization following voltage spikes. Thus, we compared K+ currents in nematocytes and tentacle neurons to understand how spike width might be differentially regulated. Nematocytes exhibited transient outward K+ currents that quickly inactivated, while neurons had large sustained K+ currents, perhaps important for repolarization and repetitive spiking (Figure 3—figure supplement 1A–C). The transient component of the nematocyte K+ current was highly sensitive to voltage-dependent inactivation, similar to ICaV (Figure 3—figure supplement 1D). This K+ current was abolished by the rapid intracellular Ca2+ chelator BAPTA or by removing external Ca2+, similar to the effect of the K+ channel blocker TEA+ (Figure 3—figure supplement 1E). Consistent with this observation, nematocyte-enriched cells expressed numerous Ca2+-activated K+ channels (Figure 3—figure supplement 1F). Furthermore, using intracellular Cs+ to block K+ currents resulted in prolonged voltage spikes and greatly increased resting membrane voltage, substantiating a role for K+ channels in modulating membrane voltage (Figure 3—figure supplement 1G). We propose that these distinct K+ channel properties could contribute to the singular wide spikes of nematocytes versus the numerous narrow spikes of neurons.

### Nematocyte sensory transduction

If nematocytes are basally inhibited due to the unique voltage-dependent inactivation of ICaV, how do they respond to sensory signals to elicit discharge? Nematocyte discharge requires simultaneous detection of chemo- and mechanosensory cues (Pantin, 1942b; Watson and Hessinger, 1992), even though mechanical stimulation of the nematocyte’s cilium (cnidocil) within intact tentacles can by itself induce cellular depolarization (Brinkmann et al., 1996; Anderson and Bouchard, 2009). Indeed, we found the deflection of isolated nematocyte cnidocils elicited a mechanically gated inward current with rapid activation and inactivation kinetics. This current was abolished by gadolinium (Gd3+), which blocks mechanoreceptor and other cation channels, and was not observed in neurons (Figure 4A–C). Furthermore, nematocyte-enriched cells differentially expressed transcripts encoding NompC (no mechanoreceptor potential C, Figure 4—figure supplement 1A), a widely conserved mechanoreceptor previously found to localize to the cnidocil of nematocytes from Hydra (Schüler et al., 2015). Heterologous expression of Nematostella NompC (nNompC) resulted in a mechanically-gated current with similar properties to native nematocytes, including rapid kinetics and Gd3+ sensitivity (Figure 4A–C). Comparison with the Drosophila orthologue (dNompC) demonstrated nNompC had similar rapid kinetics, Gd3+ sensitivity, pressure-response relationships, and nonselective cation conductance, all consistent with the conservation of protein regions important for mechanosensitivity and ion selectivity (Jin et al., 2017; Figure 4A–C, Figure 4—figure supplement 1B–D). Thus, we conclude nematocytes are intrinsically mechanosensitive and suggest nNompC contributes to nematocyte mechanosensitivity. Importantly, this mechanically-evoked current is of sufficient amplitude to evoke a spike from very negative membrane voltages, but not from resting voltage at which ICaV is inactivated.

![Figure 4.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig4-v1.jpg)

**Figure 4.:** (A) Mechanical stimulation of nematocytes evoked Gd3+-sensitive, transient inward currents with similar properties to heterologously expressed Nematostella (n) and Drosophila (d) NompC channels. Stimulation thresholds (pipette displacement): nematocyte = 1.7 ± 0.3 μm (n = 6), nNompC = 4.2 ± 0.6 μm (n = 4), dNompC = 4.2 ± 0.5 μm (n = 4). Untransfected cells did not respond to similar stimuli (n = 6). (B) Mechanically evoked currents from nematocytes (n = 6), nNompC (n = 4), and dNompC (n = 4) were blocked by Gd3+, while tentacle neurons lacked mechanically evoked currents (n = 8). p<0.01 two-tailed student’s t-test. (C) Mechanically evoked current activation and desensitization kinetics were similar in nematocytes (n = 6), nNompC (n = 4), and dNompC (n = 4). (D) Chemosensory stimuli did not directly affect nematocytes but the neurotransmitter acetylcholine (ACh, n = 5) elicited a large outward current. n = 4 for prey extract, NANA, Glutamate, GABA, Glycine, p<0.001 for ACh versus other conditions, one-way ANOVA with post-hoc Tukey test. (E) Representative current-voltage relationship of ACh-elicited response in nematocytes. (F) ACh-evoked currents (n = 9) were blocked by nicotinic ACh receptor antagonists (tubocurarine = 4, mecamylamine = 4) and a similar current was elicited by nicotine (n = 4). ACh-evoked outward currents were inhibited by a K+ channel blocker (TEA+, n = 4) and an intracellular Ca2+ chelator (BAPTA, n = 4), but not the G-protein signaling blocker GDPβS (n = 4). p<0.001 for vehicle versus antagonists, one-way ANOVA with post-hoc Tukey test. (G) Acetylcholinesterase staining in tentacles with and without substrate solution (representative of n = 3 animals). Scale bar = 200 μm. Data represented as mean ±sem.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Left: mRNA expression (transcripts per million, TPM) of NompC (no mechanoreceptor potential) ion channels in nematocyte-enriched cells (blue) vs. non-enriched cells (grey). n = 6, p<0.05, two-tailed student’s t-test. Right: Numerous reads mapped across the entire NompC sequence. The transcript architecture is shown below the mapping. CDS, coding sequence; UTR, untranslated regions. The maximum read counts was set as the same value between samples. (B) A representative single Nematostella NompC (nNompC) channel expressed in an excised membrane patch was sensitive to increasing pressure applied via the patch pipette. Vm = −80 mV. (C) nNompC and Drosophila NompC (dNompC) exhibited similar pressure-open probability (NPO) relationships and slope conductance. nNompC was blocked by Gd3+. 95% confidence interval for pressure required to induce half maximal PO: nNompC = 51.9–59.4 mmHg, dNompC = 47.4–59.7 mmHg. n = 5. Slope conductance: nNompC = 168 ± 4 pS, dNompC = 175 ± 4 pS. n = 4. Patches from untransfected cells did not respond to similar stimuli (n = 6). (D) Alignment of Drosophila (dNompC) and Nematostella (nNompC) protein sequences revealed high conservation with overall sequence identity of 44.3% (62.7% similarity). Yellow indicates residues important for mechanosensitivity. (E) Application of filtered prey extract, but not vehicle, elicited a feeding response (contraction of tentacles) in a representative Nematostella. (F) Representative nematocyte response to acetylcholine (ACh) shows an outwardly-rectifying current, which was blocked by mecamylamine (Mec). K+ was the major intracellular cation. (G) Representative current-voltage relationship shows that the ACh-evoked current was inhibited by the K+ channel blocker TEA+. (H) In the presence of intracellular Cs+ to block K+ currents, ACh mediated a mecamylamine-sensitive, inward current that was enhanced by extracellular Ca2+. (I) mRNA expression (transcripts per million, TPM) of nicotinic acetylcholine-like receptors (nAChRs) in nematocyte-enriched cells (blue) vs. non-enriched cells (grey). n = 6, p<0.05 for nACHRa7.1, two-way ANOVA with post-hoc Bonferroni test. (J) Alignment of Nematostella nAChRs and mouse nAChRa7 protein sequences revealed conserved residues that facilitate Ca2+ permeability. Data represented as mean ±sem.

Because nematocyte discharge is mediated by combined chemical and mechanical cues (Pantin, 1942b; Watson and Hessinger, 1992), we wondered if chemosensory signals could modulate nematocyte membrane voltage to allow for ICaV activation and cellular responses. While prey-derived chemicals (<3 kDa extract from brine shrimp) evoked robust behavioral responses, similar treatments did not elicit electrical responses from isolated nematocytes (Figure 4D, Figure 4—figure supplement 1E). Considering in vivo cellular and discharge activity requires the presence of prey-derived chemicals with simultaneous mechanical stimulation, chemoreception may occur indirectly through functionally coupled cells (Price and Anderson, 2006). Previous studies suggest the presence of synaptic connections between nematocytes and other unknown cell types (Westfall et al., 1998; Oliver et al., 2008). To test this possibility, we screened isolated nematocytes for responses to well-conserved neurotransmitters and found only acetylcholine (ACh) elicited a significant response (Figure 4D,E). ACh-evoked outward currents were abolished by nicotinic acetylcholine receptor (nAChR) antagonists and recapitulated by nicotine (Figure 4F, Figure 4—figure supplement 1F). The K+ channel blocker TEA+ and the intracellular Ca2+ chelator BAPTA inhibited responses, suggesting ACh elicits K+ channel activity downstream of increased intracellular Ca2+. While the G-protein signaling inhibitor GDPβS did not affect outward currents, blockade of K+ currents with intracellular Cs+ revealed an ACh-elicited inward current that was enhanced by increased extracellular Ca2+ and blocked by the nAChR antagonist mecamylamine (Figure 4F, Figure 4—figure supplement 1G,H). These results suggest ACh evokes a Ca2+-permeable nAChR-like signaling pathway to engage Ca2+-activated K+ channels, consistent with the absence of muscarinic ACh receptors in Nematostella (Faltine-Gonzalez and Layden, 2019). In agreement with this observation, nematocyte-enriched cells expressed numerous nAChR-like transcripts which had well-conserved domains involved in Ca2+ permeability (Fucile, 2004; Figure 4—figure supplement 1I,J). Finally, we found robust acetylcholinesterase activity in tentacles, further suggesting a role for ACh signaling in nematocyte function (Figure 4G). These results demonstrate that nematocytes use cholinergic signaling to regulate K+ currents, similar to how efferent cholinergic innervation of vertebrate hair cells modulates nAChR-K+ channel signaling to inhibit auditory responses (Elgoyhen and Katz, 2012).

To identify the origin of cellular connections to nematocytes, we used serial electron microscopy reconstruction to visualize nematocytes and neighboring cells. We analyzed similar tentacle tissues from which we carried out physiological experiments and readily observed neurons and nematocytes in close proximity (Figure 5—figure supplement 1A,B). In resulting micrographs, nematocytes were clearly identified by their distinct nematocyst and cnidocil (Figure 5—figure supplement 1C). Interestingly, each nematocyte exhibited a long process, of presently unknown function, that extended into the ectoderm (Figure 5—figure supplement 1D). We also observed numerous spirocytes, indicated by the presence of a large intracellular thread-like structure (Figure 5A, Figure 5—figure supplement 1C). Putative sensory neurons were identified based on their synaptic contacts and extracellular projections (Figure 5A, Figure 5—figure supplement 1E,F). Importantly, dense core vesicles were localized to electron-dense regions at the junction between each nematocyte and one other cell type, either sensory neurons or spirocytes (Figure 5A, Figure 5—figure supplement 2A–E). Thus, nematocytes receive synaptic input from both neurons and spirocytes and likely serve as a site for integrating multiple signals (Figure 5—figure supplement 2F,G). This observation is consistent with the ability of cnidarians to simultaneously discharge multiple cnidocyte types to most efficiently capture prey (Pantin, 1942a).

![Figure 5.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig5-v1.jpg)

**Figure 5.:** (A) Left: Electron micrograph demonstrating dense-core vesicles in the vicinity of an electron-dense zone localized at the junction between a spirocyte and nematocyte. Middle: 3D reconstruction of the nematocyte and spirocyte shown in the left panel. The box indicates the position of the synapse. Right: 3D reconstruction of a different nematocyte making a synapse with a putative sensory neuron. The box indicates the position of the synapse shown in Figure 5—figure supplement 2C and E. (B) ACh induced hyperpolarization of nematocytes. n = 6, p<0.01 paired two-tailed student’s t-test. (C) Depolarizing current injection did not induce active properties from rest, but did elicit a voltage spike from most nematocytes hyperpolarized by ACh. n = 6, p<0.01 paired two-tailed student’s t-test. (D) Chemo-tactile-induced nematocyte discharge (touch + prey extract, n = 8) was inhibited by the mechanoreceptor current blocker Gd3+ (n = 7) and nAChR antagonist mecamylamine (n = 14). In the absence of chemical stimulation (touch - prey extract, n = 5), touch + ACh (n = 14) was sufficient to induce discharge, which was inhibited by mecamylamine (n = 12). p<0.0001 for controls versus respective treatments, one-way ANOVA with post-hoc Bonferroni test. Data represented as mean ±sem.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) Tentacle from elav::mOrange Nematostella stained with dsRed (red) indicated neural processes beneath ectodermal nematocytes and putative sensory neurons located within the ectoderm. DAPI (blue) stains nuclei and nematocysts. White arrow indicates putative sensory projection. Scale bar = 10 μm. (B) Electron micrograph of Nematostella tentacle section (50 nm thickness). Arrow indicates regions containing nematocytes, spirocytes and sensory neurons which were imaged at higher magnification as illustrated in Figure 5 and Figure 5—figure supplement 2. (C) Cnidocil of a nematocyte (blue) and ciliae of a spirocyte (orange). Left: 3D reconstruction. Right: Electron micrograph of one section of the nematocyte (top) and one section of the spirocyte (bottom). (D) Nematocyte process. Left: 3D reconstruction of the nematocyte. Right: Electron micrograph of one section across the nematocyte process, indicated by the region boxed on the left panel. (E) Synapses made between the neuron and other cells than a nematocyte. Two examples are shown (middle and right panels). (F) Sensory terminal of the neuron shown in Figure 5A with multiple filopodia extending in the outside environment. Left: Electron micrograph of one section of the sensory neuron. Right: 3D reconstruction of the sensory neuron.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Putative synapse between a nematocyte (N, blue) and a spirocyte (yellow). Higher magnification is shown in Figure 5A. (B) Putative synapse between a nematocyte (N, blue) and a spirocyte (orange). (C) Putative synapse between a nematocyte (N, blue) and a sensory neuron (red). (D) Higher magnification of the regions boxed in B. (E) Higher magnification of the regions boxed in C. (F) Reconstruction of the synapse between a nematocyte (N, blue) and a spirocyte (S, yellow). Box indicates site of synaptic contact shown in panel A and Figure 5A. (G) 3D reconstruction of the sensory neuron and the two nematocytes shown in Figure 5A (blue).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** (A) For nematocytes with a resting membrane voltage (VRest) more positive than −60 mV, ACh was insufficient to hyperpolarize cells enough to mediate a spike following depolarizing current injection. Representative of n = 2. (B) For nematocytes with VRest more negative than −60 mV, all ACh-hyperpolarized cells produced voltage spikes following depolarizing current injection. n = 4, p<0.001 two-tailed student’s t-test. (C) Controls (related to Figures 1G and 5D) for nematocyte discharge. Control = 8, Gd3+wash = 7, Mec wash = 14, Cd2+wash = 8. (D–F). mRNA expression (transcripts per million, TPM) of calcium-binding proteins (D), calcium exchangers (E), and calcium ATPases (F) in nematocyte-enriched cells.

### Voltage-dependence mediates signal integration

How do distinct mechanosensory and chemosensory signals converge to elicit discharge? In agreement with our observation that nAChR activation increases K+ channel activity, ACh hyperpolarized nematocytes to negative voltages from which they were capable of producing robust voltage spikes (Figure 5B,C). A select number of cells with a more positive resting voltage still failed to produce spikes, and therefore additional regulation could exist through the modulation of resting membrane voltage (Figure 5—figure supplement 3A,B). These results suggest that the voltage-dependence for ICaV prevents basal activation to depolarizing signals, such as mechanical stimulation, but activation of nAChR hyperpolarizes the cell to relieve ICaV inactivation, thereby amplifying depolarizing signals to mediate cellular responses.

Consistent with a requirement for both mechano- and chemosensory input, we found the mechanoreceptor current blocker Gd3+ inhibited chemo-tactile stimulation of discharge. Additionally, the nAChR antagonist mecamylamine greatly reduced chemo-tactile-induced discharge (Figure 5D). Washout of both treatments recovered the ability of nematocytes to discharge (Figure 5—figure supplement 3C). Moreover, the requirement for prey-derived chemicals was completely recapitulated by ACh (Figure 5D). These results are consistent with a role for ACh signaling downstream of chemosensory stimulation. Thus, we propose that the unique ICaV voltage-dependent inactivation provides a mechanism by which nematocytes filter extraneous depolarizing mechanical signals, but can integrate chemosensory-induced hyperpolarization together with a depolarizing stimulus to elicit robust signal amplification and discharge responses (Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/57578/elife-57578-fig6-v1.jpg)

**Figure 6.:** (A) Model for nematocyte signal integration. (B) Nematocyte CaV is inactivated at rest and thus does not amplify extraneous NompC-mediated mechanical signals. Chemosensory stimuli hyperpolarize nematocytes through ACh signaling to relieve inactivation of CaV channels, which can then amplify mechanical stimuli to engage discharge.

## Discussion

Here, we demonstrate that nematocytes use the specialized properties of nCaV to filter salient chemo-tactile signals from environmental noise. The involvement of Ca2+ signaling in this process is consistent with a well-established role for Ca2+ influx in mediating discharge across multiple cnidarian species (McKay and Anderson, 1988; Santoro and Salleo, 1991; Watson and Hessinger, 1994a). However, the exact mechanism by which Ca2+ influx mediates discharge is unclear. It has been proposed that Ca2+ influx alters the permeability of the nematocyst capsule and/or initiates the rapid dissociation of ions within the cyst to induce osmotic changes within the organelle (Lubbock and Amos, 1981; Lubbock et al., 1981; Weber, 1990; Tardent, 1995). Our transcriptomic analyses demonstrate that nematocytes express multiple Ca2+ handling proteins (Figure 5—figure supplement 3D–F), which could control Ca2+ signaling domains in response to spatially restricted sensory transduction cascades. This organization would be consistent with the necessity for ICaV-mediated amplification of receptor-mediated nonselective cation conductances. Indeed, CaV currents could mediate an increase of >500 µM Ca2+ considering a uniform distribution across the small cytoplasmic volume (5%) not occupied by the nematocyst. Future studies will provide insight into the coupling between sensory transduction and organellar physiology.

Our results suggest one mechanism by which nematocytes integrate combined mechanical and chemical cues to filter salient environmental information and appropriately engage nematocyte discharge. However, cnidarians occupy distinct ecological niches and may have evolved different biophysical features to account for increased turbulence, specific behaviors, or particular prey and predatory targets. Numerous sea anemones occupy turbulent tidal pools, whereas others, like Nematostella vectensis, live in calmer regions. Similarly, cnidarians can undergo developmental transitions between immobile and free-floating medusa phases while maintaining the use of nematocytes for prey capture (Martin and Archer, 1997). Although forces generated from swimming prey are likely negligible in comparison with physical contact of the cnidocil, strong tidal waves may be sufficient to elicit mechanoreceptive responses which could interfere with pertinent chemo-tactile sensation and subsequent stinging responses. These ecological differences might require distinct filtering mechanisms for distinguishing salient prey or predator signals. For example, anatomical organization and pharmacological dependence for cellular and discharge activity in anthozoan nematocytes differs from hydrozoans (Anderson and Mckay, 1987; Kass-Simon and Scappaticci, Jr., 2002; Oliver et al., 2008). Indeed, nematocysts vary extensively in morphology, differing in the length of the extruded thread, the presence of spines, and the composition of toxins (Kass-Simon and Scappaticci, Jr., 2002), likely reflecting the diversity of organismal needs.

The modularity provided by synaptic connections could increase the diversity of signals which regulate nematocyte discharge. For instance, distinct chemoreceptor cells could form synaptic connections with specific nematocyte populations to mediate discrete behavioral responses. In addition to chemical mixtures, such as prey extract, numerous amino acids, lipids, and N-acetylated sugars can individually modulate nematocyte discharge (Watson and Hessinger, 1992). While these are broadly-distributed molecules, it is possible distinct prey- or predator-derived compounds regulate specific chemosensory cells to engage predatory or defensive nematocytes, respectively (Brace, 1990). Indeed, we observed that both spirocytes and neurons make synaptic contacts with nematocytes, thus either could release ACh in response to specific stimuli. Future identification and characterization of chemosensory cells and the ecologically relevant compounds which activate them will provide insight regarding chemical coding and mechanisms of synaptic signaling. Discharge can also be regulated by organismal nutritional state (Sandberg et al., 1971), suggesting nematocytes could receive input from digestive cells or hormones. Additionally, various cnidocyte types are found across the cnidarian phylum and regulated by stimuli relevant to their behavioral purpose. For example, the freshwater cnidarian, Hydra vulgaris, uses a specific cnidocyte to grasp surfaces for phototaxis, suggesting that these cells could be regulated downstream of a photoreceptor (Plachetzki et al., 2012). Within anthozoans, nematocytes and spirocytes may use similar or distinct mechanisms to control discharge. Functional comparisons will reveal whether specific proteins, domains, or signaling mechanisms are conserved or give rise to the evolutionary novelties across these incredibly specialized cell types (Babonis and Martindale, 2014).

The ability to distinguish behaviorally-relevant stimuli, such as prey, from background noise is especially critical because nematocytes are single-use cells that must be replaced following discharge. Multiple species have taken advantage of these specialized conditions by adapting to evade and exploit nematocyte discharge for their own defensive purposes. For example, clownfish can live among the tentacles of sea anemones without harmful effects, although the exact mechanism by which this occurs is unclear (Lubbock, 1980). Certain species of nudibranchs and ctenophores acquire undischarged nematocysts from prey and store them for later defense, indicating that these organisms are able to initially prevent discharge responses (Greenwood, 2009). Understanding such regulation could reveal additional mechanisms by which cells process diverse stimuli and provide insight into the evolution of these interspecies relationships.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Strain, strain background (Nematostella vectensis, adult, male and female)</td>
      <td>Nematostella vectensis</td>
      <td>Woods Hole MarineBiological Laboratory</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Nematostella vectensis, stable transgenic line, adult, male and female)</td>
      <td>NvElav1::mOrange</td>
      <td>(Nakanishi et al., 2012)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>HEK293T</td>
      <td>ATCC</td>
      <td></td>
      <td>CRL-3216</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti- DsRed (Rabbit Polyclonal)</td>
      <td>TaKaRa</td>
      <td>Cat#632496</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>nCaV: cacna1a (plasmid)</td>
      <td>Plasmid fromour lab (see Materials and methods)</td>
      <td></td>
      <td>Nematostella nCaV α</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>nCaV: cacna2d1(plasmid)</td>
      <td>Plasmid from our lab (see Materials and methods)</td>
      <td></td>
      <td>Nematostella nCaV α2δ</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>nCaV: cacnb2 (plasmid)</td>
      <td>Plasmid from our lab (see Materials and methods)</td>
      <td></td>
      <td>Nematostella nCaV β</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>nNompC (plasmid)</td>
      <td>Plasmid from our lab (see Materials and methods)</td>
      <td></td>
      <td>Nematostella nNompC</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Rat cacna2d1</td>
      <td>(Lin et al., 2004)</td>
      <td>Addgene Plasmid #26575</td>
      <td>Rat mCaV α2δ</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Mouse cacna1a</td>
      <td>(Richards et al., 2007)</td>
      <td>Addgene Plasmid #26578</td>
      <td>Mouse mCaV α</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Rat cacnb2a</td>
      <td>(Wyatt et al., 1998)</td>
      <td>Addgene Plasmid #107424</td>
      <td>Rat mCaV β</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>dNompC-GFP</td>
      <td>YN Jan (UCSF)</td>
      <td>N/A</td>
      <td>Drosophila nNompC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RACE Primer</td>
      <td>Primer generated in our lab (see Materials and methods)</td>
      <td>PCR primer</td>
      <td>GATTACGCCAAGCTTTATGCGTCCAATCGTACTTGTCGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RACE Primer</td>
      <td>Primer generated in our lab (see Materials and methods)</td>
      <td>PCR primer</td>
      <td>GATTACGCCAAGCTTGCCGACAAGTACGATTGGACGCATA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Cacnb primer F</td>
      <td>Primer generated in our lab (see Materials and methods)</td>
      <td>PCR primer</td>
      <td>CAGAGCCAGGCCTGAGCGAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Cacnb primer R</td>
      <td>Primer generated in our lab (see Materials and methods)</td>
      <td>PCR primer</td>
      <td>GCCCCGTTAAAAGTCGAGAG</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SMARTer RACE 5’/3’ Kit</td>
      <td>TaKaRa</td>
      <td>Cat# 634858</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>N-Acetylneuraminic acid (NANA)</td>
      <td>Sigma</td>
      <td>Cat#857459</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glycine</td>
      <td>Sigma</td>
      <td>Cat#410225</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Acetylcholine chloride</td>
      <td>Sigma</td>
      <td>Cat#A6625</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>GdCl3</td>
      <td>Sigma</td>
      <td>Cat#7532</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TEA</td>
      <td>Sigma</td>
      <td>Cat#86614</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>GDPβS</td>
      <td>Sigma</td>
      <td>Cat#G7637</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CdCl2</td>
      <td>Sigma</td>
      <td>Cat#202908</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Mecamylamine</td>
      <td>Tocris</td>
      <td>Cat#2843</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glutamate</td>
      <td>Tocris</td>
      <td>Cat#0218</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>γ-Aminobutyric acid (GABA)</td>
      <td>Tocris</td>
      <td>Cat#0344</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Nicotine ditartrate</td>
      <td>Tocris</td>
      <td>Cat#3546</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tubocurarine</td>
      <td>Tocris</td>
      <td>Cat#2820</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BAPTA</td>
      <td>Molecular Probes</td>
      <td>Cat#B-1204</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cutadapt</td>
      <td>(Martin, 2011)</td>
      <td></td>
      <td>https://github.com/marcelm/cutadapt/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Trinity</td>
      <td>(Grabherr et al., 2011)</td>
      <td></td>
      <td>https://github.com/trinityrnaseq</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>InterProScan</td>
      <td>(Jones et al., 2014)</td>
      <td></td>
      <td>https://github.com/ebi-pf-team/interproscan/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HMMER</td>
      <td>(Eddy, 2009)</td>
      <td></td>
      <td>http://hmmer.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Pfam</td>
      <td>(El-Gebali et al., 2019)</td>
      <td></td>
      <td>https://pfam.xfam.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DIAMOND</td>
      <td>(Buchfink et al., 2015)</td>
      <td></td>
      <td>https://github.com/bbuchfink/diamond</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Clustal Omega</td>
      <td>(Sievers et al., 2011)</td>
      <td></td>
      <td>https://www.ebi.ac.uk/Tools/msa/clustalo/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji: Linear Stack Alignment with SIFT</td>
      <td>(Schindelin et al., 2012)</td>
      <td></td>
      <td>https://fiji.sc/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab custom script</td>
      <td>Matlab code provided in source data for Figure 1</td>
      <td></td>
      <td>See supplemental table for script</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>VAST</td>
      <td>(Berger et al., 2018)</td>
      <td></td>
      <td>https://software.rc.fas.harvard.edu/lichtman/vast/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>3D Studio Max 2019</td>
      <td>(Autodesk, 2019)</td>
      <td></td>
      <td>https://www.autodesk.com</td>
    </tr>
  </tbody>
</table>

### Animals and cells

Starlet sea anemones (Nematostella vectensis) were provided by the Marine Biological Laboratory (Woods Hole, Massachusetts), Nv-Elav1::mOrange transgenic animals were a gift from F. Rentzsch. We used adult animals of both sexes, which were fed freshly-hatched brine shrimp (Artemia) twice a week and kept on a 12 hr light/dark cycle in 1/3 natural sea water (NSW). Nematocytes and neurons were isolated from tentacle tissue, which was harvested by anesthetizing animals in high-magnesium solution containing (mM): 140 NaCl, 3.3 Glucose, 3.3 KCl, 3.3 HEPES, 40 MgCl2. Cells were isolated from tentacles immediately prior to electrophysiology experiments by treatment with 0.05% Trypsin at 32°C for 30 min and mechanical dissociation in divalent free recording solution (mM): 140 NaCl, 3.3 Glucose, 3.3 KCl, 3.3 HEPES, pH 7.6. Basitrichous isorhiza nematocytes were isolated from tentacles and identified by a thick-walled capsule containing a barbed thread, with a characteristic high refractive index, oblong shape and presence of a cnidocil. Spirocytes were identified by a thin-walled capsule containing a thin, unarmed thread, used for ensnaring prey. Neurons were identified by mOrange expression.

HEK293T cells (ATCC, Cat# CRL-3216, RRID:CVCL_0063, authenticated and validated as negative for mycoplasma by vendor) were grown in DMEM, 10% fetal calf serum, and 1% penicillin/streptomycin at 37°C, 5% CO2. Cells were transfected using lipofectamine 2000 (Invitrogen/Life Technologies) according to the manufacturer’s protocol. 1 µg of Nematostella cacna1a, cacnb2.1, cacna2d1. M. musculus (mouse) cacna1a, R. norvegicus (rat) cacnb2a, or rat cacna2d1 was coexpressed with 0.5 µg GFP. Mechanosensitive proteins were assayed using HEK293T cells transfected with 1 µg of either Drosophila NompC or Nematostella NompC. To enhance channel expression, cells were transfected for 6–8 hr, plated on coverslips, and then incubated at 28°C for 2–6 days before experiments. Drosophila NompC-GFP was a gift from YN Jan. Rat cacna2d1 (RRID:Addgene_26575) and cacna1a (RRID:Addgene_26578) were gifts from D. Lipscombe and cacnb2a (RRID:Addgene_107424) was a gift from A. Dolphin.

### Molecular biology

RNA was prepared from tentacles of adult Nematostella using published methods (Stefanik et al., 2013). Briefly, 50 mg of tentacle tissue were homogenized and RNA was extracted using TRIzol. RNA was isolated and DNase treated (Zymo Research), then used for cDNA library synthesis (NEB E6560). Full-length sequence for a Nematostella calcium channel beta subunit was obtained with a RACE strategy using specific primers (GATTACGCCAAGCTTTATGCGTCCAATCGTACTTGTCGGC and GATTACGCCAAGCTTGCCGACAAGTACGATTGGACGCATA) on the amplified tentacle-tissue library. The final sequence was confirmed using primers corresponding to the end of the derived sequence (CAGAGCCAGGCCTGAGCGAG and GCCCCGTTAAAAGTCGAGAG) to amplify a full-length cDNA from tentacle mRNA, which was sequenced to confirm identity. nCav subunits: cacna1a, cacna2d1, cacnb2, and nNompC-GFP were synthesized by Genscript (Piscataway, NJ). Sequence alignments were carried out using Clustal Omega.

### Transcriptomics

Tentacle tissue was ground to a fine powder in the presence of liquid nitrogen in lysis buffer (50 mM Tris-HCl pH 7.5, 250 mM KCl, 35 mM MgCl2, 25 mM EGTA-KOH pH 8, 5 mM DTT, murine RNase inhibitor (NEB), 1% (w/v) NP-40, 5% (w/v) sucrose, 100 μg ml−1 cycloheximide (Sigma), 500 μg ml−1 heparin (Sigma)). Lysate was incubated on ice for 5 min, triturated five times with an 18 g needle, and insoluble material was removed by centrifugation at 16,000 g for 5 min at 4°C. Polyadenylated RNA was used to make sequencing libraries and sequenced on an Illumina HiSeq 4000 (Novogene). Quality filtering and adapter trimming was performed using Cutadapt (Martin, 2011), and a de novo transcriptome was assembled using Trinity (Grabherr et al., 2011). Annotation was performed using InterProScan (Jones et al., 2014) with Panther member database analysis, HMMER (Eddy, 2009) with the Pfam (El-Gebali et al., 2019) database, and DIAMOND (Buchfink et al., 2015) with the UniProt/TrEMBL database.

Reads from sorted cnidocytes (Bioproject PRJNA391807 Sunagar et al., 2018), enriched for nematocytes, were quality and adapter trimmed as described above, and transcript abundance (TPM) was quantified using Kallisto (Bray et al., 2016) and the tentacle transcriptome. For read mapping visualization, mapping was performed with Bowtie2 (Langmead and Salzberg, 2012), output files were converted to indexed bam files using Samtools (Li et al., 2009), and visualization was performed with the Integrated Genomics Viewer (Robinson et al., 2011).

### Electrophysiology

Recordings were carried out at room temperature using a MultiClamp 700B amplifier (Axon Instruments) and digitized using a Digidata 1550B (Axon Instruments) interface and pClamp software (Axon Instruments). Whole-cell recording data were filtered at 1 kHz and sampled at 10 kHz. For single-channel recordings, data were filtered at 2 kHz and sampled at 20 kHz. Data were leak-subtracted online using a p/4 protocol, and membrane potentials were corrected for liquid junction potentials. For whole-cell nematocyte and neuron recordings, borosilicate glass pipettes were polished to 8–10 MΩ. The standard Nematostella medium was used as the extracellular solution and contained (in mM): 140 NaCl, 3.3 glucose, 3.3 KCl, 3.3 HEPES, 0.5 CaCl2, 0.5 MgCl2, pH 7.6. Two intracellular solutions were used for recording. For isolating inward currents (mM): 133.3 cesium methanesulfonate, 1.33 MgCl2, 3.33 EGTA, 3.33 HEPES, 10 sucrose, 10 CsEGTA, pH 7.6. For outward currents (mM) 166.67 potassium gluconate, 3.33 HEPES, 10 sucrose, 1.33 MgCl2, 10 KEGTA, pH 7.6. In some experiments, BAPTA was substituted for EGTA. For whole-cell recordings in HEK293 cells, pipettes were 3–4 MΩ. The standard extracellular solution contained (in mM): 140 NaCl, 5 KCl, 10 HEPES, 2 CaCl2, 1 MgCl2, pH 7.4. The intracellular solution contained (mM): 140 cesium methanesulfonate, 1 MgCl2, 3.33 EGTA, 3.33 HEPES, 10 sucrose, pH 7.2. In ion substitution experiments, equimolar Ba2+ was substituted for Ca2+. Single-channel recording extracellular solution contained (mM): 140 NaCl, 10 HEPES, 1 NaEGTA, pH 7.4. The intracellular solution used (mM): 140 CsCl, 10 HEPES, 1 CsEGTA, pH 7.4.

The following pharmacological agents were used: N-Acetylneuraminic acid (NANA, 100 µM, Sigma), glycine (100 µM, Sigma), acetylcholine (1 mM), mecamylamine (100 µM, 500 µM for behavioral experiments, Tocris), GdCl3 (100 µM, Sigma), glutamate (1 mM), GABA (1 mM), nicotine (100 µM, Tocris), tubocurarine (10 µM, Tocris), TEA+ (10 mM, Sigma), BAPTA (10 mM, Tocris), GDPβS (1 mM, Sigma), and Cd2+ (500 µM, 250 µM for behavioral experiments). All were dissolved in water. Prey extract was isolated from freshly-hatched Artemia. Artemia were flash-frozen, ground with mortar and pestle, filtered with 0.22 µM pores or 3 kDa ultracentrifugal filters (Amicon UFC500324). Pharmacological effects were quantified as differences in normalized peak current from the same cell following bath application of the drug (Itreatment/Icontrol). Whole-cell recordings were used to assess mechanical sensation together with a piezoelectric-driven (Physik Instrumente) fire-polished glass pipette (tip diameter 1 μm). Mechanical steps in 0.5 μm increment were applied every 5 s while cells were voltage-clamped at −90 mV. Single mechanosensitive channels were studied using excised outside-out patches exposed to pressure applied via a High-Speed Pressure Clamp system (HSPC, ALA-scientific). Pressure-response relationships were established using pressure steps in 10 mmHg increments. Voltage-dependence of currents was measured from −100 mV to 100 mV in 20 mV increments while applying repetitive 60 mmHg pressure pulses.

Unless stated otherwise, voltage-gated currents were measured in response to a 200 ms voltage pulse in 10 mV increments from a −110 mV holding potential. G-V relationships were derived from I-V curves by calculating G: G = ICaV/(Vm-Erev) and fit with a Boltzman equation. Voltage-dependent inactivation was measured during −10 mV (Ca2+ currents in native cells), 0 mV (Ca2+ currents in heterologously expressed channels), 60 mV (K+ currents in native cells) voltage pulses following a series of 1 s pre-pulses ranging from −110 mV to 60 mV. Voltage-dependent inactivation was quantified as I/Imax, with Imax occurring at the voltage pulse following a −110 mV prepulse. In some instances, inactivation curves could not be fit with a Boltzman equation and were instead fitted with an exponential. The time course of voltage-dependent inactivation was measured by using a holding voltage of −110 mV or −70 mV and applying a 0 mV test pulse every 5 s. Recovery from inactivation was quantified by normalizing inactivated and recovered currents to those elicited from the same cell in which a 0 mV voltage pulse was applied from −110 mV. Test pulses from a holding voltage of −40 mV were used to assess inactivation, followed by pulses from −110 mV where currents quickly recovered to maximal amplitude. Repetitive stimulation using 20 ms pulses to −10 mV or 0 mV from a holding voltage of −90 mV was also used to measure inactivation in response to repetitive stimulation. Current inactivation kinetics were quantified by the portion of current remaining at the end of a 200 ms pulse (R200) or fit with a single exponential. Activation was quantified as the time from current activation until peak amplitude. 200 ms voltage ramps from −120 to 100 mV were used to measure ACh-elicited currents. Stimulus-evoked currents were normalized to basal currents measured at the same voltage of 80 mV.

Single channel currents were measured from the middle of the noise band between closed and open states or derived from all-points amplitude histograms fit with Gaussian relationships at closed and open peaks for each excised patch record. Conductance was calculated from the linear slope of I–V relationships. N(PO) was calculated during pressure steps while voltage was held at −80 mV. In current clamp recordings, effects of ACh or intracellular ions on resting membrane potential was measured without current injection (I = 0). 1 s depolarizing current steps of various amplitudes were injected to measure spikes which were quantified by frequency (spikes/second) or width (duration of spike). To test whether resting membrane potential affects the ability to generate spikes, hyperpolarizing current was injected to bring cells to negative voltages (<-90mV) or ACh was locally perfused before depolarizing current injection.

The change in Ca2+ concentration from a nematocyte voltage spike was estimated based on the integral of Ca2+-selective nematocyte currents elicited by a 0 mV step, the same amplitude and slightly shorter duration than a voltage spike. Nematocyte volume was estimated from serial electron microscopy reconstruction with a non-nematocyst volume of approximately 5% of the total volume of the cell. We did not consider the volume occupied by other organelles, making for a conservative estimate. Furthermore, calculations were made with extracellular recording solution containing 0.5 mM Ca2+, which is approximately six-fold less than physiological concentrations. Thus, the large increase we calculated likely underestimates the total Ca2+ influx.

### Immunohistochemistry

#### Neural staining

Adult Nv-Elav1::mOrange Nematostella were paralyzed in anesthetic solution, then placed in a 4% solution of PFA overnight. Animals were cryoprotected using a gradient of increasing sucrose concentrations (10% to 50%) in PBS over two days. Cryostat sections (20 µm thick) were permeabilized with 0.2% Triton-X and 4% normal goat serum (NGS) at room temperature for 1 hr, followed by incubation with DsRed Polyclonal Antibody (Takara Bio Cat# 632496, RRID:AB_10013483) overnight in PBST (0.2%) and NGS (4%) at 4°C. Tissue was rinsed three times with PBST before secondary was applied (Goat anti-rabbit 647, Abcam in PBST + NGS) for 2 hr at room temperature. Tissue was rinsed with PBS and mounted with Vectashield containing DAPI (Novus Biologicals).

#### Acetylcholinesterase staining

Tentacles were stained for the presence of acetylcholinesterase as described (Paul et al., 2010) using 40 µm thick cryosections mounted on glass slides. Slides were incubated in acetylthiocholine and copper-buffered solution at 40°C until tentacles appeared white. The stain was developed with a silver solution so that stained areas appear brown. Slides were incubated in the presence of the silver staining solution (+substrate) or saline (-substrate), rinsed according to protocol, and mounted in Fluoromount-G (SouthernBiotech) and imaged using a scanning, transmitted light microscope.

### Behavior

Discharge of nematocysts was assessed based on well-established assays (Watson and Hessinger, 1994a; Gitter et al., 1994). Adult Nematostella were placed in petri dishes containing a modified Nematostella medium, containing 16.6 mM MgCl2. Animals were given appropriate time to acclimate before presented with stimuli. For assaying discharge, 5 mm round coverslips were coated with a solution of 25% gelatin (w/v) dissolved in medium, and allowed to cure overnight prior to use. Coverslips were presented to the animal’s tentacles for 5 s and then immediately imaged at 20X magnification using a transmitted light source. To assay behavioral response to prey-derived chemicals, freshly hatched brine shrimp were flash frozen and pulverized, then filtered through a 0.22 µm filter. Coverslips were dipped in the prey extract and immediately presented to the animal. All pharmacological agents were bath applied, except for acetylcholine (1 mM), which was delivered as a bolus immediately prior to coverslip presentation. Acetylcholine exposure did not produce movement or contraction of tentacles. Experiments carried out in the absence of extracellular Ca2+ were nominally Ca2+ free and did not use extracellular chelators. The highest density of discharged nematocytes on the coverslip was imaged at 20X. Nematocyte discharge involves everting the barbed thread, causing them to embed in the gelatin-coated coverslips. Therefore, if nematocytes do not discharge, they are not captured by the gelatin-coated coverslip or visualized for quantification. Images were blindly analyzed using a custom Matlab routine (available in supplemental material) in which images were thresholded and the fraction of pixels corresponding to nematocytes was compared across experiments.

### Electron microscopy

Tentacles from an individual Nematostella vectensis were placed between two sapphire coverslips separated by a 100 μm spacer ring (Leica) and frozen in a high-pressure freezer (EM ICE, Leica). This was followed by freeze-substitution (EM AFS2, Leica) in dry acetone containing 1% ddH2O, 1% OsO4 and 1% glutaraldehyde at −90°C for 48 hr. The temperature was then increased at 5°C/h up to 20°C and samples were washed at room temperature in pure acetone 3 × 10 min RT and propylene oxide 1 × 10 min. Samples were infiltrated with 1:1 Epon:propylene oxide overnight at 4°C. The samples were subsequently embedded in TAAB Epon (Marivac Canada Inc) and polymerized at 60°C for 48 hr. Ultrathin sections (about 50 nm) were cut on an ultramicrotome (Leica EM UC6) and collected with an automated tape collector (ATUM Kasthuri et al., 2015). The sections were then post-stained with uranyl acetate and lead citrate prior to imaging with a scanning electron microscope (Zeiss SIGMA) using a back-scattered electron detector and a pixel size of 4 nm.

Once all the sections were scanned, images were aligned into a stack using the algorithm ‘Linear Stack Alignment with SIFT’ available in Fiji (Schindelin et al., 2012). After alignment, images were imported into VAST (Berger et al., 2018) so that every cell could be manually traced. By examining sections and following cellular processes contacts between cells of interest (e.g. neurons and nematocytes) were identified and assessed for the presence of dense-core vesicles in the vicinity (~500 nm). Such instances were labeled as putative synapses. Cells were then rendered in three dimensions using 3D Studio Max 2019 (Autodesk, San Rafael, CA).

Nematocytes were readily identified because resin does not infiltrate the nematocyst capsule, making for an ‘empty’ appearance (large white area). Spirocytes were also readily identified based on their capsule containing a long, coiled filament. Sensory neurons were identified according to the higher number of dense core vesicles, higher number of synapses and the presence of sensory processes extending into the external environment.

### Statistical analysis

Data were analyzed with Clampfit (Axon Instruments) or Prism (Graphpad) and are represented as mean ± s.e.m. n represents independent experiments for the number of cells/patches or behavioral trials. Data were considered significant if p<0.05 using paired or unpaired two-tailed Student’s t-tests or one- or two-way ANOVAs. All significance tests were justified considering the experimental design and we assumed normal distribution and variance, as is common for similar experiments. Sample sizes were chosen based on the number of independent experiments required for statistical significance and technical feasibility.
