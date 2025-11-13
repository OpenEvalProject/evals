# Simultaneous recording of multiple cellular signaling events by frequency- and spectrally-tuned multiplexing of fluorescent probes

## Authors

- Michelina Kierzek<sup>1</sup>
- Parker E Deal<sup>3</sup>
- Evan W Miller<sup>3</sup> ([ORCID: 0000-0002-6556-7679](https://orcid.org/0000-0002-6556-7679))
- Shatanik Mukherjee<sup>6</sup> ([ORCID: 0000-0002-7359-9339](https://orcid.org/0000-0002-7359-9339))
- Dagmar Wachten<sup>7</sup> ([ORCID: 0000-0003-4800-6332](https://orcid.org/0000-0003-4800-6332))
- Arnd Baumann<sup>8</sup>
- U Benjamin Kaupp<sup>9</sup>
- Timo Strünker<sup>1</sup> ([ORCID: 0000-0003-0812-1547](https://orcid.org/0000-0003-0812-1547)) †
- Christoph Brenker<sup>1</sup> ([ORCID: 0000-0002-4230-2571](https://orcid.org/0000-0002-4230-2571)) †

### Affiliations

1. Centre of Reproductive Medicine and Andrology, University of Münster Münster Germany
2. CiM-IMPRS Graduate School, University of Münster Münster Germany
3. Department of Chemistry, University of California, Berkeley Berkeley United States
4. Department of Molecular & Cell Biology, University of California, Berkeley Berkeley United States
5. Helen Wills Neuroscience Institute, University of California, Berkeley Berkeley United States
6. Molecular Sensory Systems, Center of Advanced European Studies and Research Bonn Germany
7. Institute of Innate Immunity, Department of Biophysical Imaging, Medical Faculty, University of Bonn Bonn Germany
8. Institute of Biological Information Processing (IBI-1), Research Center Jülich Jülich Germany
9. Life & Medical Sciences Institute (LIMES), University of Bonn Bonn Germany
10. Cells in Motion Interfaculty Centre, University of Münster Münster Germany

† Corresponding author

## Abstract

Fluorescent probes that change their spectral properties upon binding to small biomolecules, ions, or changes in the membrane potential (Vm) are invaluable tools to study cellular signaling pathways. Here, we introduce a novel technique for simultaneous recording of multiple probes at millisecond time resolution: frequency- and spectrally-tuned multiplexing (FASTM). Different from present multiplexing approaches, FASTM uses phase-sensitive signal detection, which renders various combinations of common probes for Vm and ions accessible for multiplexing. Using kinetic stopped-flow fluorimetry, we show that FASTM allows simultaneous recording of rapid changes in Ca2+, pH, Na+, and Vm with high sensitivity and minimal crosstalk. FASTM is also suited for multiplexing using single-cell microscopy and genetically encoded FRET biosensors. Moreover, FASTM is compatible with optochemical tools to study signaling using light. Finally, we show that the exceptional time resolution of FASTM also allows resolving rapid chemical reactions. Altogether, FASTM opens new opportunities for interrogating cellular signaling.

## Introduction

Cells respond to external stimuli by changes in membrane potential (Vm), ions, messenger molecules, or protein modification (e.g., phosphorylation or dephosphorylation). These signaling events can be monitored in real time using fluorescent probes (Tsien, 1989; Rothman et al., 2005; Mehta and Zhang, 2011; Depry et al., 2013; Ni et al., 2018). To delineate the network of cellular responses, it would be ideal to use different probes under identical conditions in the same sample (dubbed multiplexing) (Keyes et al., 2021). Such measurements can not only reveal the precise sequence of signaling events, for example, whether they are upstream or downstream of each other, but also whether events are mechanistically coupled like ion transport across membranes via exchangers or symporters (Welch et al., 2011; Depry et al., 2013). When recorded in separate experiments on different samples, inter-experimental and cell-to-cell variations may obscure temporal and mechanistic relationships of events. Moreover, by design, probes bind their target molecules, which might perturb the dynamics and sequence of cellular responses (Lew et al., 1985; Haugh, 2012; Delvendahl et al., 2015). Such probe-related perturbations can be inferred from multiplexing experiments.

Signaling events, such as ligand-receptor binding and changes in Vm and ions, often occur on millisecond or even sub-millisecond timescales. Multiplexing of such rapid events requires kinetic techniques that allow both precisely timed stimulation of cells and simultaneous recording from different probes on a millisecond timescale. Discrimination of simultaneously excited probes relies on the spectral separation of their emissions using optical filtering (Figure 1A). However, the spectral space for simultaneous recording of probes is limited (Neher and Neher, 2004) because crosstalk arising from overlapping emission spectra compromises their discrimination. Therefore, although many spectrally distinct probes for Vm and various ions and biomolecules have been developed (Depry et al., 2013; Yuan et al., 2013; Yin et al., 2015; Kulkarni and Miller, 2017; Mehta et al., 2018), simultaneous recording with millisecond time resolution has been restricted to two probes, for example, for two ion species or one ion species and Vm (e.g., Vogt et al., 2011; Jaafari et al., 2015; Deal et al., 2016). For multiplexing of more than two probes, quasi-simultaneous recording has been used: probes are excited and detected sequentially by switching between different excitation wavelengths (Figure 1B; Canepari et al., 2007; Canepari et al., 2008; Lee et al., 2012; Sulis Sato et al., 2017; Miyazaki et al., 2018; Ait Ouares et al., 2019; Nguyen et al., 2019). Although quasi-simultaneous multiplexing overcomes fluorescence crosstalk, it limits the temporal resolution and, thereby, the application range for studying rapid signaling events occurring on a millisecond timescale (van Meer et al., 2019). Hitherto, a multiplexing strategy combining millisecond temporal resolution with high flexibility regarding the number and combinations of probes has been lacking.

![Figure 1.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig1-v2.jpg)

**Figure 1.:** (A) Spectrally separable emission spectra (dashed) of probes allow their simultaneous recording using optical filtering. (B) Spectrally separable excitation spectra (outlined) allow quasi-simultaneous recording of probes using excitation-switching. (C) Frequency-tagging and phase-sensitive detection of fluorescence combined with optical filtering using frequency- and spectrally-tuned multiplexing (FASTM) allow simultaneous recording of probes based on separable excitation and/or emission spectra. (D) Schematic of the chemosensory signaling pathway and (E) illustration of the time course of the signaling events in sea urchin sperm (reviewed in Strünker et al., 2015). Resact, the chemoattractant peptide released by the egg, triggers the synthesis of cGMP by activating a receptor guanylyl cyclase (GC). The rise in cGMP elicits a pulse-like Vm hyperpolarization mediated by a cyclic nucleotide-gated K+ channel (CNGK). The hyperpolarization activates a voltage-gated Na+/H+ exchanger (sNHE) and a hyperpolarization‐activated and cyclic nucleotide‐gated (HCN) channel. The Na+/H+ exchange increases [Na+]i and pHi. In turn, the increase in pHi primes pHi-controlled CatSper Ca2+ channels to open during the recovery from hyperpolarization driven by HCN channels. The resulting Ca2+ influx drives chemotactic steering towards the egg. (F) Schematic of the stopped-flow setup: one syringe is filled with a suspension of probe-loaded sperm, and a second syringe is filled with a solution of resact. The syringe pistons move synchronously to rapidly mix sperm with resact in a micromixer and subsequently push this mixture into an observation cuvette, where spectroscopic measurements are performed (see Hamzeh et al., 2019).

Here, we introduce an approach that leverages phase-sensitive signal detection, which is commonly used to recover small signals buried in large noise (Meade, 1983), but also facilitates signal multiplexing (Aslund and Carlsson, 1993; Carlsson et al., 1994; Lewis et al., 2005; Hwang et al., 2015; Garbacik et al., 2018; Gómez-García et al., 2018; Tovar et al., 2019). We dubbed this method frequency- and spectrally-tuned multiplexing (FASTM). In brief, like conventional multiplexing, FASTM also involves the simultaneous excitation of different probes; however, the excitation light is modulated at distinct frequencies. The frequency-tagging of fluorescence combined with optical filtering allows discriminating probes based on their excitation and/or emission spectra (Figure 1C). We tested the time resolution and applicability of FASTM on signaling pathways of sperm and in single cultured cells. FASTM enabled multiplexing of at least three rapid signaling events at millisecond time resolution using various combinations of common non-ratiometric and ratiometric probes for ions and Vm as well as FRET-based biosensors. Moreover, FASTM can be combined with kinetic rapid-mixing techniques and flash-induced release of caged messengers, for example, cGMP, to instantaneously activate signaling pathways. Finally, FASTM is also suited to resolve rapid chemical reactions. These unique features of FASTM expand the scope of time-resolved multiplexing of cellular signaling.

## Results

### Multiplexing of rapid ionic and electrical signaling events using FASTM

Chemosensory signaling in the flagellum of sea urchin sperm involves rapid changes in cellular messengers, ions, and Vm (Figure 1D and E) (reviewed in: Darszon et al., 2008; Strünker et al., 2015; Wachten et al., 2017; Darszon et al., 2020); therefore, sperm are an ideal model to develop and test novel strategies for multiplexing. In brief, a chemoattractant peptide, resact, activates a receptor guanylyl cyclase. The ensuing rise of cGMP elicits a brief transient hyperpolarization, followed by an increase of the intracellular pH (pHi) and Na+ concentration ([Na+]i) that, ultimately, trigger a Ca2+ influx and rise of the intracellular Ca2+ concentration ([Ca2+]i) (Figure 1E). The sequence of signaling events has been delineated by sequentially recording changes in either [Ca2+]i, pHi, [Na+]i, or Vm on different sperm samples using stopped-flow fluorimetry (Figure 1F; Hamzeh et al., 2019).

We set out to record the resact-induced [Ca2+]i, pHi, and Vm signals in the same sperm sample by multiplexing of the respective fluorescent probes Fura-2, BCECF, and RhoVR (Deal et al., 2016). The well-separated excitation spectra (Figure 2A) render these three probes accessible for quasi-simultaneous recording. The [Ca2+]i, pHi, and Vm signals occur, however, on a millisecond timescale, which requires their simultaneous recording; yet, due to the overlapping emission spectra (Figure 2A), simultaneous recording of these three probes using optical filtering alone seems intractable. Therefore, we chose to multiplex Fura-2, BCECF, and RhoVR based on simultaneous excitation by three LEDs each modulated at a distinct frequency in the kHz range (Figure 2B, Table 1); thereby, the emission of each probe is tagged with a unique frequency signature for discrimination. The fluorescence was collected on opposite sides of the cuvette by two photomultipliers (PMTs) equipped with appropriate optical filters: one PMT detected the emission of Fura-2 and BCECF and the other that of RhoVR (Figure 2B, Table 2). Lock-in amplifiers demodulated and amplified the PMT signals in a phase-sensitive fashion to discriminate, in real time, the probes based on their modulation frequencies. We refer to this approach as FASTM.

![Figure 2.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig2-v2.jpg)

**Figure 2.:** (A) Superposition of excitation (outlined) and emission (filled) spectra of fluorescent probes for Ca2+ (Fura-2), pH (BCECF), and Vm (RhoVR). Bandpass filters used for excitation (filled) and emission (outlined) are shown above the spectra. Inset: excitation and emission spectra depicted individually with respective filters (black bars). (B) Schematic of FASTM: each probe is excited by an LED modulated at a different frequency. The modulated emission is optically filtered and collected by two photomultipliers (PMTs). The PMT signals are demodulated by lock-in amplifiers in a phase-sensitive fashion to recover in real time [Ca2+]i, pHi, and Vm signals.

We tested whether FASTM permits simultaneous recording of the three probes. First, using sperm that had been loaded with one probe only, we compared crosstalk between all three recording ‘channels,’ with (Figure 3, colored traces, FASTM) and without (Figure 3, gray traces, optical filtering) modulating the LEDs at different frequencies. In BCECF-loaded sperm, relying on optical filtering alone, the basal fluorescence intensity (Fo) recorded in the BCECF channel and the Fura-2 channel (Figure 3A, gray) and the relative increase (∆F/Fo), reflecting the pHi response (Figure 3B, gray), were similar. Of note, in Figure 3A, the gray (optical filtering) and blue traces (FASTM) in the BCECF channel are superimposed. Unsurprisingly, the BCECF fluorescence detected in the BCECF and the Fura-2 channel was similar, considering that both were collected by the same detector and optical filter (Figure 2B, Table 2). Basal BCECF fluorescence and the resact-induced relative increase were also detected in the RhoVR channel (Figure 3A and B), demonstrating that optical filtering is not sufficient to isolate the RhoVR channel from BCECF’s broad emission spectrum. To quantify the crosstalk between channels, we plotted the first two seconds of the fluorescence signal recorded in the BCECF channel against that recorded in the Fura-2 or the RhoVR channel (Figure 3C, optical filtering). The slope of a linear fit to these plots is a measure of the crosstalk: if the time course of the fluorescence perfectly correlates between channels, the slope and crosstalk is 1 and 100%, respectively. Vice versa, if the time course of the fluorescence is independent among channels, the slope/crosstalk is zero. For optical filtering alone, we determined a crosstalk between the BCECF and the Fura-2 and RhoVR channels of 100 and 31%, respectively (Figure 3J). Modulating the LEDs at different frequencies using FASTM did not affect the fluorescence signal in the BCECF channel (Figure 3A and B, blue trace). However, FASTM lowered the basal fluorescence and almost abolished its relative increase in both the Fura-2 (Figure 3A and B; cyan) and the RhoVR channel (Figure 3A and B, orange); with FASTM, the crosstalk between the BCECF and the Fura-2 or the RhoVR channel was only 9 and 1%, respectively (Figure 3C and J).

![Figure 3.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig3-v2.jpg)

**Figure 3.:** Time course of the fluorescence signals recorded from BCECF- (A–C), Fura-2- (D–F), or RhoVR-loaded sperm (G–I) after mixing with resact (50 pM). Fluorescence was recorded in the BCECF, Fura-2, and RhoVR channels using optical filtering alone (gray traces) or FASTM (colored traces). (A, D, G) Fluorescence signals in arbitrary fluorescence units (AFU); to ease the comparison, signals in (A), (D), and (G) were normalized (set to 1) to the baseline fluorescence (F0) in the BCECF, the Fura-2, and the RhoVR channel, respectively, recorded immediately after mixing with resact. (B, E, H) Resact-evoked change in fluorescence (ΔF) with respect to the baseline fluorescence (F0), that is, ΔF/F0 (%); #signals smoothed with a sliding average of 80 ms. (C, F, I) First 2 s of the fluorescence signal recorded in the BCECF channel plotted against that recorded in the Fura-2 or the RhoVR channel using either optical filtering (top panel) or FASTM (bottom panel). Gray line: linear fit of the plots to quantify the crosstalk between the channels (see explanation in the text). (J) Percent crosstalk between the channels according to the analysis shown in (C), (F), and (I).

Next, we loaded sperm with Fura-2 alone and monitored the resact-induced [Ca2+]i response. With optical filtering alone, the basal fluorescence and its relative decrease, reflecting the [Ca2+]i response, were similar in all channels (Figure 3D and E; gray traces); the crosstalk between the Fura-2 and the BCECF or RhoVR channels was 98 and 79%, respectively (Figure 3F and J). Of note, Fura-2 fluorescence decreased with increasing [Ca2+]i because the probe was excited at 380 nm. FASTM did not affect the Fura-2 channel (Figure 3D and E; cyan), but lowered the basal fluorescence intensity and abolished its relative decrease in the BCECF channel (Figure 3D and E; blue) and the RhoVR channel (Figure 3D and E; orange); the crosstalk between the channels was ≤1% (Figure 3F and J). Finally, we monitored the resact-induced Vm response in RhoVR-loaded sperm. Due to the probe’s red-shifted spectrum, crosstalk between channels was negligible; basal RhoVR fluorescence and its resact-induced decrease, reflecting the Vm response, were only detected in the RhoVR channel, both with and without FASTM (Figure 3G–J).

We next loaded sperm with all three probes and simultaneously recorded resact-induced [Ca2+]i, pHi, and Vm signals (Figure 4A and B). Using optical filtering alone, the simultaneously recorded signals markedly differed from the respective signals recorded in sperm loaded with one probe only (compare Figure 4A and Figure 3B, E,H ); the pHi and [Ca2+]i signals represent a composite of the Fura-2-reported Ca2+ response (transient fluorescence decrease) and the BCECF-reported pHi response (sustained fluorescence increase), whereas the Vm signal featured a lower amplitude and slower kinetics (Figure 4A). Thus, the crosstalk among channels greatly misrepresented the true time course and size of signaling events.

![Figure 4.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig4-v2.jpg)

**Figure 4.:** Relative changes in fluorescence ∆F/F0 evoked by 50 pM resact. The respective control signal evoked by mixing with artificial sea water (ASW) was subtracted, setting the control-signal level to ΔF/F0 (%) = 0 (dotted line). Signals were recorded using optical filtering alone (A) or frequency- and spectrally-tuned multiplexing (FASTM) (B). (C) Simultaneous FASTM recording of resact-evoked signals from pooled sperm loaded separately with either BCECF, Fura-2, or RhoVR.

By contrast, using FASTM, we simultaneously recorded genuine resact-induced [Ca2+]i, pHi, and Vm signals in the respective channels (Figure 4B). The kinetics, waveforms, and amplitudes of the multiplexed signals were similar to those recorded with FASTM (compare Figure 4B with Figure 3B, E and H) or without FASTM (see previous studies, e.g., Hamzeh et al., 2019) in sperm loaded with one probe only. We further explored whether triple-loading per se affects the response waveforms. To this end, we pooled sperm suspensions that were separately loaded with either Fura-2, BCECF, or RhoVR. The overall time course of the [Ca2+]i, pHi, and Vm signals recorded simultaneously via FASTM from these pooled single-loaded sperm was similar to those recorded from triple-loaded sperm (Figure 4C). Competition of probes with downstream targets for signaling molecules might perturb response dynamics (Lew et al., 1985; Haugh, 2012; Delvendahl et al., 2015); in triple-loaded cells, this potential caveat might be enhanced. Therefore, using FASTM, we further examined in greater detail whether specific features of the signals were altered in single- vs. triple-loaded sperm. We compared resact-induced [Ca2+]i, pHi, and Vm signals in sperm loaded with one probe (single-loaded) to those in sperm loaded with three probes (triple-loaded); of note, for the ease of illustration, Fura-2 fluorescence was multiplied by –1 to depict an increase of [Ca2+]i as an increasing signal. Under both conditions, the respective signals were similar (Figure 5A and B). We took this comparison one step further and compared the resting membrane potential (Vrest) and threshold voltage (Vthr) at which [Ca2+]i and pHi commence to rise after stimulation with different resact concentrations; Vrest and Vthr are characteristic features of the signaling pathway (Figure 5C–E; Seifert et al., 2015). In single- and triple-loaded sperm, both Vrest (Figure 5C) and Vthr (Figure 5D and E) were similar. Thus, signaling is neither perturbed by Ca2+- and H+-binding to Fura-2 and BCECF, respectively, nor by partition of RhoVR into the membrane, at least under the experimental regimes used here.

![Figure 5.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig5-v2.jpg)

**Figure 5.:** Resact-evoked Vm, pHi, and [Ca2+]i signals recorded individually from different sperm samples loaded with one probe only (A) or recorded simultaneously from triple-loaded sperm (B); to facilitate direct comparison, Fura-2 fluorescence was multiplied by –1 to depict an increase of [Ca2+]i as an increasing signal. (C) Comparison of Vrest of sperm loaded with RhoVR (single-loaded) or RhoVR, BCECF, and Fura-2 (triple-loaded). (D) Calibrated resact-induced (50 pM) Vm response and accompanying pHi and [Ca2+]i signals. The artificial sea water (ASW) control was subtracted, and the dotted black line indicates ΔF/F0 = 0 and Vrest. The Vm at the onset of the pHi and [Ca2+]i signals was deduced from the signal latencies. (E) Vm at the onset of pHi and [Ca2+]i signals in single- versus triple-loaded sperm. With increasing resact concentrations, the rise in pHi and [Ca2+]i commenced at increasingly negative Vm (Seifert et al., 2015).

We conclude that Fura-2, BCECF, and RhoVR are not suitable for simultaneous recording based on optical filtering alone, whereas FASTM permits this probe combination for multiplexing of rapid [Ca2+]i, pHi, and Vm responses with millisecond time resolution.

To illustrate the versatility of FASTM, we tested different triple combinations of Vm, Ca2+, pH, and Na+ probes, whose overlapping emission spectra prevent simultaneous recording using optical filtering alone (Figure 6A–C, Figure 6—figure supplement 1). By contrast, FASTM allowed for crosstalk-free multiplexing of resact-induced Vm-[Ca2+]i-pHi (Figure 6D), Vm-[Ca2+]i-[Na+]i (Figure 6E), or Vm-pHi-[Na+]i (Figure 6F) responses.

![Figure 6.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig6-v2.jpg)

**Figure 6.:** Superposition of excitation (outlined) and emission (filled) spectra of (A) Fura-2, VF2.1.Cl, and pHrodo; (B) Fura-2, RhoVR, and ANG-2; (C) BeRST, pHrodo, and ANG-2. Bandpass filters used for excitation (filled) and emission (outlined) are depicted above the spectra. Inset: individual excitation and emission spectra with respective filters (black bars). (D–F) Signals (∆F/F0) evoked by 500 pM resact corrected for the artificial sea water (ASW) control and normalized to their respective peak values (set to 1) for easier illustration.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Calibrated resact-evoked (500 pM) Vm response in sea urchin sperm reported by VF2.1.Cl (A), RhoVR (B), and BeRST (C) upon excitation at the principal peak (gray) versus excitation at the secondary peak (blue). Inset: excitation and emission spectra of probes in sea urchin sperm. Bandpass filters used for excitation (filled) and emission (outlined) are depicted above.

Finally, the shift of the excitation spectra of Fura probes and BCECF upon Ca2+ and H+ binding, respectively, can be harnessed to quantify [Ca2+]i or pHi in absolute terms using ratiometric recording (O’Connor and Silver, 2013). This relies on obtaining the ratio of the probe’s emission recorded at two different excitation wavelengths, which, in previous studies, required switching between excitation wavelengths. We investigated whether FASTM allows for simultaneous ratiometric recording of Fura-FF and BCECF. Moreover, we used human instead of sea urchin sperm, thus, testing FASTM in different cells. In human sperm, the CatSper Ca2+ channel is activated at alkaline pHi and also by the female steroid hormone progesterone (Lishko et al., 2011; Strünker et al., 2011). We mixed Fura-FF- and BCECF-loaded human sperm in the stopped-flow device with NH4Cl or progesterone. Fura-FF and BCECF were simultaneously excited each at two different wavelengths (340/370 nm and 445/485 nm, respectively) with frequency-modulated light; the emission was collected at 530 nm by one detector (Figure 7A and B, Table 3). NH4Cl evoked an instantaneous, rapid and more gradual increase in the emission ratios of BCECF and Fura-2, respectively, reflecting the NH4Cl-induced pHi increase and concomitant pHi-induced Ca2+ influx via CatSper, respectively (Figure 7D). By contrast, progesterone evoked an instantaneous increase of the Fura-FF ratio, reflecting progesterone-induced Ca2+ influx, whereas the BCECF ratio was largely unaffected (Figure 7D). These results demonstrate that FASTM ensures minimal crosstalk between the Fura-FF and the BCECF channels (Figure 7C, Figure 7—figure supplement 1). Taken together, FASTM allows for simultaneous recording of rapid signaling events with millisecond temporal resolution using various combinations of non-ratiometric and ratiometric probes.

![Figure 7.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig7-v2.jpg)

**Figure 7.:** (A) Superimposed excitation (outlined) and emission (filled) spectra of Fura-FF and BCECF. Inset: individual spectra with respective filters (black bars). (B) Schematic of frequency- and spectrally-tuned multiplexing (FASTM) configuration for simultaneous ratiometric dual-excitation recording of Fura-FF and BCECF in human sperm. (C) Crosstalk among channels based on the analysis shown in Figure 7—figure supplement 1. #Under these particular conditions, the approach to quantify crosstalk yielded an erroneously inflated value (for details, see Figure 7—figure supplement 1). (D) Left panels: ratiometric [Ca2+]i and pHi signals (ΔR/R0) in human sperm evoked by NH4Cl (10 mM) or progesterone (100 nM) corrected for the buffer control. Right panel: fluorescence signals in the individual Fura-FF and BCECF channels underlying the ratio.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Human sperm loaded with BCECF or Fura-FF were mixed with either NH4Cl or progesterone, respectively. The first 5 s (BCECF-loaded sperm) and 20 s (Fura-FF-loaded sperm) of the fluorescence signals recorded in the different channels were plotted against each other and crosstalk was evaluated by linear fitting of the data. The steepness of the linear fit (gray line) is a measure of the crosstalk between channels. Of note, Fura-FF fluorescence upon excitation at the isosbestic point at 340 nm does not change with [Ca2+]i. Fura-FF is also excited by 445 nm, and the emission changes with [Ca2+]i. Consequently, the linear fit of the plot of fluorescence signals at 445 vs. 340 nm excitation indicates severe crosstalk among channels. The absolute fluorescence values are, however, an order of magnitude lower compared to that recorded in BCECF-loaded sperm and do, thus, not affect simultaneous recording of Fura-FF and BCECF.

### Combination of FASTM with flash photolysis of caged compounds

Optogenetics and optochemistry employ light-triggered tools (e.g., enzymes, ion channels, caged compounds, photoswitches) to investigate cellular signaling pathways (Ellis-Davies, 2007; Szymański et al., 2013, Ankenbruck et al., 2018). In general, combining such tools with fluorescent probes requires shielding the detectors from the trigger such as the strong UV flash used for uncaging. Optical filtering alone is usually not sufficient to prevent recording artifacts created by the UV flash (e.g., see Strünker et al., 2006; Kilic et al., 2009; Servin-Vences et al., 2012). We used sea urchin sperm to explore whether FASTM can ameliorate flash artifacts. Sperm were loaded with Fluo-4, pHrodo, BeRST, and BECMCM-caged cGMP to simultaneously record [Ca2+]i, pHi, and Vm responses evoked by the intracellular photorelease of cGMP that bypasses receptor GC activation (Hamzeh et al., 2019; Figure 8A and B). Indeed, due to the phase-sensitive signal detection, the flash artifact was suppressed by the lock-in amplifiers (Hamzeh et al., 2019) and FASTM allowed for undisturbed simultaneous recording of cGMP-evoked [Ca2+]i, pHi, and Vm signals (Figure 8C).

![Figure 8.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig8-v2.jpg)

**Figure 8.:** (A) Superimposed absorbance spectrum of BECMCM-cGMP and excitation (outlined) and emission (filled) spectra of Fluo-4, pHrodo, and BeRST. Bandpass filters used for excitation (filled) and emission (outlined) are depicted above the spectra. Inset: individual spectra and respective filters (black bars). (B) Schematic of frequency- and spectrally-tuned multiplexing (FASTM) configuration for uncaging experiments. (C) Vm, pHi, and [Ca2+]i signals evoked by uncaging intracellular cGMP with a 50 ms UV-flash (gray bar).

### Multiplexing of fast chemical reactions using FASTM

We next explored whether FASTM also allows multiplexing of fast chemical reactions in solution. Using the stopped-flow device, we simultaneously monitored the kinetics of Ca2+ dissociation from Fura-2 (dual-excitation recording), Fluo-4, and Calbryte 630 (Figure 9A–C, Figure 9—figure supplement 1). A solution containing Ca2+-bound Fura-2, Fluo-4, and Calbryte 630 was mixed with an excess of the Ca2+ chelator BAPTA that competes with the probes for binding of Ca2+. Dissociation of Ca2+ was reflected by a decrease of Fluo-4 and Calbryte 630 fluorescence; Fura-2 fluorescence decreased and increased at 370 nm and 340 nm excitation, respectively (Figure 9D). Exponential fitting of the traces yielded the dissociation rate constants (koff) (Figure 9E). The koff of Fura-2 (340ex: 115 ± 2; 370ex: 122 ± 3; ratio: 84 ± 2 s–1) was similar to that reported before (Jackson et al., 1987; Kao and Tsien, 1988), whereas that of Fluo-4 (354 ± 3 s–1) and Calbryte 630 (178 ± 2 s–1) (n = 4) had not yet been determined to the best of our knowledge. These experiments demonstrate the utility of FASTM for multiplexing of rapid chemical reactions.

![Figure 9.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig9-v2.jpg)

**Figure 9.:** (A) Superimposed excitation (outlined) and emission (filled) spectra of Fura-2, Fluo-4, and Calbryte 630. Inset: individual spectra depicted with respective filters (black bars). (B) Schematic of the frequency- and spectrally-tuned multiplexing (FASTM) configuration for simultaneous recording of Ca2+ dissociation from Fura-2, Fluo-4, and Calbryte 630. (C) Crosstalk between channels according to Figure 9—figure supplement 1. (D) Changes in Fura-2, Fluo-4, and Calbryte 630 fluorescence and 370 nm/340 nm emission ratio of Fura-2 upon mixing of the Ca2+-bound probes with the Ca2+ chelator BAPTA. (E) Koff values determined by exponential fitting of the individual fluorescence traces and the ratio of Fura-2 (370/340 nm): Fura-2, 340ex: 115 ± 2 s–1; Fura-2, 370ex: 122 ± 3 s–1; Fura-2 ratio: 84 ± 2 s–1; Fluo-4: 354 ± 3 s–1; Calbryte 630: 178 ± 2 s–1 (n = 4).

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig9-figsupp1-v2.jpg)

**Figure 9—figure supplement 1.:** The first 18 ms of the fluorescence signals recorded in the different channels were plotted against each other, and crosstalk was evaluated by a linear fit to the data. The steepness of the linear fit (gray line) is a measure of the crosstalk between channels.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig9-figsupp2-v2.jpg)

**Figure 9—figure supplement 2.:** (A) Kinetics of Ca2+ dissociation from Fura-2 recorded upon excitation at 340 nm. The kinetics were recorded with frequency- and spectrally-tuned multiplexing (FASTM) using either different lock-in amplifier time constants (100 µs and 1 ms) or without modulation of the excitation light and using a conventional amplifier (no lock-in). (B) S/N ratio determined by dividing the mean signal amplitude by the standard deviation of 200 data points. The gray line indicates the S/N ratio in recordings performed without modulation of the excitation light.

### Single-cell FASTM fluorescence microscopy

Finally, we tested FASTM for single-cell fluorescence microscopy (Figure 10). A Gs-coupled octopamine receptor (DmOCTβ1R) (Balfanz et al., 2005), a FRET-based cAMP biosensor (Mukherjee et al., 2016), and a Ca2+-permeable cyclic nucleotide-gated channel (CNGA2-TM) (Wachten et al., 2006; Schröder-Lang et al., 2007) were expressed in HEK293 cells (Figure 10A). Changes in octopamine-induced cAMP synthesis and cAMP-induced Ca2+ influx were simultaneously recorded using the cAMP biosensor and the Ca2+ probe Calbryte 630, respectively (Figure 10B). The FRET donor (cerulean) and Calbryte 630 were excited by light modulated at different frequencies (Figure 10C). Because the emission from the FRET donor and acceptor (citrine) was encoded with the same frequency, signal discrimination was achieved by optically filtering the cerulean and citrine fluorescence and collecting with separate detectors. Calbryte 630 and citrine fluorescence was collected by the same detector and discriminated by the modulation frequencies. Octopamine increased and decreased the donor and acceptor fluorescence of the FRET sensor, respectively, indicating a rise of intracellular cAMP (Figure 10D). Subsequently, Calbryte 630 fluorescence increased, indicating cAMP-induced Ca2+ influx (Figure 10D). These results demonstrate that FASTM can also be employed for multiplexing in single cells using fluorescence microscopy and protein-based FRET sensors.

![Figure 10.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig10-v2.jpg)

**Figure 10.:** (A) Octopamine-signaling pathway in HEK cells coexpressing the DmOCTβ1 receptor, CNGA2-TM channel, and a FRET-based cAMP biosensor. (B) Superimposed excitation (outlined) and emission (filled) spectra of the FRET donor-acceptor pair cerulean-citrine, and the Ca2+-probe Calbryte 630. Bandpass filters used for excitation (filled) and emission (outlined) are depicted above the spectra. Inset: individual spectra and filters (black bars). (C) Schematic of the FASTM configuration for single-cell microscopy. (D) Changes in fluorescence (ΔF/F0 (%)) of the FRET donor and acceptor as well as Calbryte 630 evoked by octopamine (20 µM). Inset: image of the field of view with a single cell enclosed by an aperture.

Curiously, [Ca2+]i did not rise until the FRET signal reached saturation (Figure 10D), indicating that the cAMP sensor competes with the channel for cAMP. The vastly different K1/2 values – about 70 nM (FRET sensor) vs. 10 µM (CNGA2-TM channel) – argue that the FRET sensors get served first, which might affect cAMP dynamics and thus CNGA2-TM activation. We tested this presumption and measured the latency of the [Ca2+]i signal in cells lacking or expressing different variants of the cAMP sensor. The latency was similar in cells lacking the cAMP sensor (14 ± 5 s; n = 24) or expressing a sensor mutant (Mukherjee et al., 2016) that does not bind cAMP (mlCNBD-FRET-R307Q, 16 ± 5 s; n = 14) (Figure 11A and B). By contrast, the latency increased considerably and coincided with the saturation of the cAMP signal in cells expressing either the high-affinity cAMP sensor (44 ± 28 s, n = 22; mlCNBD-FRET) or a variant with lower cAMP affinity (~1 µM) (29 ± 7 s, n = 15; mlCNBD-FRET-M329C) (Figure 11A-C; Figure 11—figure supplement 1). These findings support the notion that cAMP ‘buffering’ by the cAMP sensor delayed activation of the downstream effector CNGA2-TM. This application of FASTM in single cells illustrates how probe-related perturbations of signaling pathways can be unveiled by multiplexing experiments.

![Figure 11.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig11-v2.jpg)

**Figure 11.:** (A) Octopamine-induced (20 µM) [Ca2+]i signals and changes in the FRET ratio (donor/acceptor), that is, cAMP signals, in the absence or presence of a non-binding (R307Q), lower (M329C), or higher-affinity (wildtype) FRET-based cAMP biosensor. Data points corresponding to the representative traces are labeled with a red asterisk in (B) and (C). (B) Onset of the octopamine-induced cAMP and [Ca2+]i signals. (C) Comparison of the time to saturation of the cAMP signal and the onset of the [Ca2+]i signal. The gray line depicts the theoretical perfect correlation.

![Figure 11—figure supplement 1.](https://cdn.elifesciences.org/articles/63129/elife-63129-fig11-figsupp1-v2.jpg)

**Figure 11—figure supplement 1.:** Increase of 8‐NBD‐cAMP fluorescence (emission at 550 nm) upon binding to mlCNBD-M329C (1 μM). 8‐NBD‐cAMP fluorescence in the absence of mlCNBD-M329C was subtracted. The solid line represents a nonlinear least‐squares fit to ΔF = RL · x, with the receptor-ligand complex RL and the normalization factor x, that relates the concentration of bound 8-NBD-cNMP to the change in fluorescence (ΔF) (Cukkemane et al., 2007). The KD value was 0.12 µM.

## Discussion

We show that phase-sensitive signal detection using FASTM readily overcomes the fluorescence crosstalk that has limited true simultaneous recording of probes. The technical implementation of FASTM is straightforward: most LED-based light sources can be modulated in the kHz range, and conventional PMT-based fluorescence-detection setups can readily be upgraded with a lock-in amplifier featuring several demodulation channels. FASTM could be further advanced using additional LEDs, modulation frequencies, and detectors as well as optimized optical filtering. This will allow simultaneous recording of even more than three probes and four fluorescence ‘channels’ (e.g., for dual-excitation recording of Fura-FF and BCECF) as used here. Importantly, the temporal resolution of FASTM is largely independent of the number of probes and only limited by the time constant of the lock-in amplifier(s) and/or detector(s), allowing multiplexing with a time resolution of a few microseconds. For comparison, using state-of-the-art filter wheels and galvanometer-based devices, quasi-simultaneous recording of four ‘channels’ can be performed with a time resolution of only >150 ms and >20 ms, respectively, which would be insufficient to fully resolve such rapid signaling events and chemical reactions that we studied here. Furthermore, phase-sensitive signal detection increases the signal-to-noise (S/N) ratio (e.g., Meade, 1983; Figure 9—figure supplement 2); thus, using FASTM, reasonable S/N ratios can be reached with lower light intensity and density of fluorophores, which minimizes bleaching and sample consumption. Therefore, we envisage that FASTM will be widely adopted for simultaneous recording of rapid signals in aqueous solutions, single cells, and cell populations.

In combination with stopped-flow techniques and optochemical tools, the exceptional time resolution of FASTM might not only allow simultaneous recording of rapid chemical reactions, but also ligand-binding kinetics and the ensuing conformational changes of a protein (e.g., Cukkemane et al., 2007; Peuker et al., 2013). Cognate ligands labeled with solvatochromic fluorophores that change their fluorescence upon binding could be rapidly mixed with proteins. Ligand binding and the protein’s conformational change could be simultaneously recorded by means of fluorescence or absorbance from endogenous tryptophan residues, incorporated non-natural amino acids, extrinsic fluorescent labels, or combinations thereof (Cheng et al., 2020).

Protein conformations and protein-protein interactions in macromolecular complexes are often investigated by time-resolved FRET (trFRET) (Miyawaki and Niino, 2015). Time-resolved readout of several FRET pairs is challenging as it requires two spectrally separated fluorophores for each FRET pair (Depry et al., 2013). Crosstalk arising from overlapping emission spectra compromises discrimination of FRET pairs; therefore, multiplexed trFRET measurements are susceptible to artifacts. The simultaneous recording of ratiometric probes using FASTM provides ample opportunities for future trFRET measurements with millisecond temporal resolution.

Finally, we show the applicability of FASTM for simultaneous recording of probes in single cells. However, the FASTM approach lacked spatial information. Subcellular imaging with FASTM could be achieved using PMT arrays. Alternatively, fluorescence could be recorded from several regions of interest (ROIs), whereby each ROI is illuminated with light modulated at a distinct frequency using acousto-optic-modulated laser excitation (Wu et al., 2006) or rapid switching of a digital micromirror device (DMD) (Chang et al., 2016; Wang et al., 2016). This approach would allow recording fluorescence signals from different ROIs with one PMT. Fast modulation of the excitation laser combined with a fast lock-in amplifier renders even confocal microscopes compatible with FASTM (Carlsson et al., 1994; Wu et al., 2006).

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
      <td>Cell line (HEK293)</td>
      <td>flp-In-293</td>
      <td>Invitrogen</td>
      <td>#R750-07</td>
      <td>RRID:CVCL_U421</td>
    </tr>
    <tr>
      <td>Transfected construct (Drosophila melanogaster)</td>
      <td>DmOCTβ1R</td>
      <td>Balfanz et al., 2005</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Bos taurus)</td>
      <td>CNGA2-TM</td>
      <td>Schröder-Lang et al., 2007</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pc3.1-ml CNBD-FRET</td>
      <td>Mukherjee et al., 2016</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pc3.1-mlCNBD-FRET-R307Q</td>
      <td>Mukherjee et al., 2016</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pc3.1-mlCNBD-FRET-M329C</td>
      <td>This paper</td>
      <td></td>
      <td>Figure 11—figure supplement 1 and materials and methods part of this MS.</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Pluronic F-127</td>
      <td>Sigma-Aldrich</td>
      <td>P2443</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fluo-4 AM</td>
      <td>Thermo Fisher</td>
      <td>F14202</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>BCECF AM</td>
      <td>Thermo Fisher</td>
      <td>B1150</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fura-2 AM</td>
      <td>Thermo Fisher</td>
      <td>F1201</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>pHrodo Red AM</td>
      <td>Thermo Fisher</td>
      <td>P35372</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>ANG-2 AM</td>
      <td>MobiTec</td>
      <td>3502</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Calbryte 630 AM</td>
      <td>AAT Bioquest</td>
      <td>20720</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fura-FF, AM</td>
      <td>AAT Bioquest</td>
      <td>21027</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>VF2.1.Cl</td>
      <td>Miller et al., 2012</td>
      <td>Sold by Thermo Fisher as FluoVolt</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>BeRST</td>
      <td>Huang et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>RhoVR</td>
      <td>Deal et al., 2016</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Calbryte 630, potassium salt</td>
      <td>AAT Bioquest</td>
      <td>20727</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fluo-4, pentapotassium salt</td>
      <td>Thermo Fisher</td>
      <td>F14200</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fura-2, pentapotassium salt</td>
      <td>Thermo Fisher</td>
      <td>F1200</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Handling of sperm from Arbacia punctulata

The protocol for sperm collection and the composition of artificial sea water (ASW) was described previously (Hamzeh et al., 2019). In short, spawning was induced by injection of 500 µl of 0.5 M KCl into the body cavity, and the spawn (dry sperm) was collected with a Pasteur pipette and stored on ice.

### Measurement of changes in [Ca2+]i, pHi, [Na+]i, and Vm

Changes in [Ca2+]i, pHi, [Na+]i, and Vm in sea urchin sperm were measured in a rapid-mixing device (SFM-4000, FC-15 cuvette, BioLogic) in the stopped-flow mode. Dry sperm were loaded with fluorescent probe(s) according to Table 1. Probes were added individually or sequentially to dry sperm diluted 1:6 (v/v) in ASW supplemented with 0.05% Pluronic F-127 (Sigma-Aldrich). After incubation at 18°C in the dark, the probe-loaded sperm suspension was diluted 1:20 (v/v) with ASW and allowed to equilibrate for 5 min prior to measurement. In the stopped-flow, the probe-loaded sperm suspension was mixed 1:1 (v/v) with ASW or ASW supplemented with resact at a flow rate of 1, 2, or 4 ml/s, resulting in a dead time of 36.6, 18.3, or 9.1 ms, respectively. The lead time on the hard-stop valve was 2 ms. The concentration of resact is given as the final concentration after mixing. BECMCM-cGMP was synthesized by Andreas Rennhack (Research Centre casear); the VoltageFluor (VF) probes, VF2.1.Cl, BeRST, and RhoVR, were synthesized in the lab of Evan Miller at UC Berkeley, according to published protocols (Miller et al., 2012; Huang et al., 2015; Deal et al., 2016). VF probes are based on photo-induced electron transfer and exhibit a principal absorbance peak and a secondary peak at ~400 nm. In multiplexed configurations, either peak was effectively employed to excite the VF probe and monitor Vm (Figure 6—figure supplement 1).

**Table 1.**
 Loading protocols for fluorescent probes in A. punctulata sperm and FASTM modulation frequencies.


<table>
  <tbody>
    <tr>
      <td></td>
      <td colspan="3">Fura-2, BCECF, RhoVR</td>
      <td colspan="3">ANG-2, pHrodo, BeRST</td>
    </tr>
    <tr>
      <td>Loading order</td>
      <td>First</td>
      <td>Second</td>
      <td>Third</td>
      <td>First</td>
      <td>Second</td>
      <td>Third</td>
    </tr>
    <tr>
      <td>Name</td>
      <td>Fura-2 AM</td>
      <td>RhoVR</td>
      <td>BCECF AM</td>
      <td>ANG-2 AM</td>
      <td>pHrodo Red AM</td>
      <td>BeRST</td>
    </tr>
    <tr>
      <td>Probe type</td>
      <td>Ca2+</td>
      <td>Vm</td>
      <td>pH</td>
      <td>Na+</td>
      <td>pH</td>
      <td>Vm</td>
    </tr>
    <tr>
      <td>Concentration (µM)</td>
      <td>10</td>
      <td>5</td>
      <td>5</td>
      <td>10</td>
      <td>10</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Incubation (min)</td>
      <td>90</td>
      <td>10</td>
      <td>5</td>
      <td>90</td>
      <td>25</td>
      <td>10</td>
    </tr>
    <tr>
      <td>FASTM modulation frequency (kHz)</td>
      <td>30.4</td>
      <td>37.3</td>
      <td>50</td>
      <td>37</td>
      <td>50</td>
      <td>23</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="3">Fura-2, ANG-2, RhoVR</td>
      <td colspan="3">Fura-2, pHrodo, VF2.1.Cl</td>
    </tr>
    <tr>
      <td>Loading order</td>
      <td>First</td>
      <td>Second</td>
      <td>Third</td>
      <td>First</td>
      <td>Second</td>
      <td>Third</td>
    </tr>
    <tr>
      <td>Name</td>
      <td>Fura-2 AM</td>
      <td>ANG-2 AM</td>
      <td>RhoVR</td>
      <td>Fura-2 AM</td>
      <td>pHrodo Red AM</td>
      <td>VF2.1.Cl</td>
    </tr>
    <tr>
      <td>Probe type</td>
      <td>Ca2+</td>
      <td>Na+</td>
      <td>Vm</td>
      <td>Ca2+</td>
      <td>pH</td>
      <td>Vm</td>
    </tr>
    <tr>
      <td>Concentration (µM)</td>
      <td>10</td>
      <td>10</td>
      <td>5</td>
      <td>10</td>
      <td>10</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Incubation (min)</td>
      <td colspan="2">90 (added together)</td>
      <td>5</td>
      <td>50</td>
      <td>35</td>
      <td>5</td>
    </tr>
    <tr>
      <td>FASTM modulation frequency (kHz)</td>
      <td>50</td>
      <td>23</td>
      <td>37</td>
      <td>50.3</td>
      <td>25.3</td>
      <td>17.1</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="6">Fluo-4, phrodo, BeRST, BECMCM-cGMP</td>
    </tr>
    <tr>
      <td>Loading order</td>
      <td colspan="2">First</td>
      <td colspan="2">Second</td>
      <td>Third</td>
      <td>Fourth</td>
    </tr>
    <tr>
      <td>Name</td>
      <td colspan="2">BECMCM-cGMP</td>
      <td colspan="2">Fluo-4 AM</td>
      <td>pHrodo Red AM</td>
      <td>BeRST</td>
    </tr>
    <tr>
      <td>Probe type</td>
      <td colspan="2">Caged cGMP</td>
      <td colspan="2">Ca2</td>
      <td>pH</td>
      <td>Vm</td>
    </tr>
    <tr>
      <td>Concentration (µM)</td>
      <td colspan="2">10</td>
      <td colspan="2">10</td>
      <td>10</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Incubation (min)</td>
      <td colspan="2">15</td>
      <td colspan="2">10</td>
      <td>35</td>
      <td>10</td>
    </tr>
    <tr>
      <td>FASTM modulation frequency (kHz)</td>
      <td colspan="2">None</td>
      <td colspan="2">37.3</td>
      <td>30.1</td>
      <td>50.3</td>
    </tr>
  </tbody>
</table>

Fluorescence was excited by an array of LEDs (Thorlabs) fitted with dichroics (Table 2). Lock-in amplifiers (MFLI, Zurich Instruments, and SR844 RF, Stanford Research Systems) supplied signals to modulate the LEDs, which were operated by a custom-made LED driver. Modulation frequencies were between 10 and 50 kHz (Table 1). The modulated output of the LEDs was combined with appropriate dichroics (Table 2) into a liquid light guide (series 380, Ø 3 mm × 1000 mm, Lumatec) and delivered to the cuvette (FC-15, BioLogic).

**Table 2.**
 Optical configurations for recording signals from A. punctulata sperm.


<table>
  <thead>
    <tr>
      <th>Probe combination</th>
      <th>Fluorescent probe</th>
      <th>LED (Thorlabs)</th>
      <th>Excitation filter (Semrock)</th>
      <th>Dichroics</th>
      <th>Emission filter(Semrock)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Fura-2, BCECF, RhoVR</td>
      <td>Fura-2</td>
      <td>M375L4</td>
      <td>379/34</td>
      <td rowspan="3">470 LPXR (Chroma)HC BS 409 (Semrock)</td>
      <td rowspan="2">524/24</td>
    </tr>
    <tr>
      <td>BCECF</td>
      <td>M490L4</td>
      <td>485/20</td>
    </tr>
    <tr>
      <td>RhoVR</td>
      <td>M455L4</td>
      <td>438/24</td>
      <td>607/36</td>
    </tr>
    <tr>
      <td rowspan="3">ANG-2, pHrodo, BeRST</td>
      <td>ANG-2</td>
      <td>M490L4</td>
      <td>485/20</td>
      <td rowspan="3">525 LPXR (Chroma)470 LPXR (Chroma)</td>
      <td>542/20</td>
    </tr>
    <tr>
      <td>pHrodo</td>
      <td>M565L3</td>
      <td>575/19</td>
      <td rowspan="2">593LP</td>
    </tr>
    <tr>
      <td>BeRST</td>
      <td>M455L4</td>
      <td>438/24</td>
    </tr>
    <tr>
      <td rowspan="3">Fura-2, ANG-2, RhoVR</td>
      <td>Fura-2</td>
      <td>M340L4</td>
      <td>340/22</td>
      <td rowspan="3">470 LPXR (Chroma)HC BS 409 (Semrock)</td>
      <td rowspan="2">542/20</td>
    </tr>
    <tr>
      <td>ANG-2</td>
      <td>M505L3</td>
      <td>513/17</td>
    </tr>
    <tr>
      <td>RhoVR</td>
      <td>M455L4</td>
      <td>438/24</td>
      <td>607/36</td>
    </tr>
    <tr>
      <td rowspan="3">Fura-2, pHrodo, VF2.1.Cl</td>
      <td>Fura-2</td>
      <td>M340L4</td>
      <td>340/22</td>
      <td rowspan="3">470 LPXR (Chroma)HC BS 409 (Semrock)</td>
      <td rowspan="2">542/20</td>
    </tr>
    <tr>
      <td>VF2.1.Cl</td>
      <td>M455L4</td>
      <td>438/24</td>
    </tr>
    <tr>
      <td>pHrodo</td>
      <td>M565L3</td>
      <td>575/19</td>
      <td>593LP</td>
    </tr>
    <tr>
      <td rowspan="4">BECMCM-cGMP, Fluo-4, pHrodo, BeRST</td>
      <td>BECMCM-cGMP</td>
      <td>M340L4</td>
      <td>340/22</td>
      <td rowspan="4">525 LPXR (Chroma)470 LPXR (Chroma)HC BS 409 (Semrock)</td>
      <td></td>
    </tr>
    <tr>
      <td>Fluo-4</td>
      <td>M490L4</td>
      <td>494/20</td>
      <td>542/20</td>
    </tr>
    <tr>
      <td>pHrodo</td>
      <td>M565L3</td>
      <td>575/19</td>
      <td rowspan="2">593LP</td>
    </tr>
    <tr>
      <td>BeRST</td>
      <td>M455L4</td>
      <td>438/24</td>
    </tr>
  </tbody>
</table>

The emission was collected at right angles to the cuvette and spectrally filtered with bandpass filters (Table 2) onto two PMT modules (H10723-20; Hamamatsu Photonics). Signals from the PMTs were directed to lock-in amplifiers, where they were amplified and frequency filtered with a third-order (18 dB/octave) lowpass filter and a time constant of 1 ms. Data acquisition was performed with a data acquisition pad (PCI-6221; National Instruments) and Bio-Kine software (BioLogic) with a sampling rate of 1 or 2 ms. Of note, to investigate signals recorded upon optical filtering alone (Figure 3), all LEDs were modulated with the same frequency.

### Analysis of stopped-flow recordings from A. punctulata sperm

Data were analyzed using GraphPad Prism 9 (Prism, La Jolla, USA). Each signal represents the average of at least three recordings. Signals are depicted as the percent change in fluorescence with respect to the mean of the first 5–10 data points prior to signal onset (ΔF/F0 (%)); mixing artifacts occurring at the stop of the flow were cropped, prolonging the actual dead time of recordings. The baseline ΔF/F0 obtained upon mixing with ASW alone was subtracted wherever indicated. In some figures, signals were normalized to their maximal values. The calibration procedure to convert the fluorescence changes of a Vm probe into Vm values (mV) has been previously described (Strünker et al., 2006; Seifert et al., 2015; Hamzeh et al., 2019). In brief, sperm were mixed with 2 nM resact at varying extracellular K+ concentrations ([K+]o). With increasing [K+]o, the peak amplitude of the resact-evoked hyperpolarization decreased and, eventually, Vm depolarized. A plot of the peak amplitude (ΔF/F0) versus the K+-Nernst potential for a given [K+]o was fitted with a linear fit. The slope of the fitted line yielded the Vm sensitivity (%ΔF/F0 per mV) of the Vm probe and the x-intercept yielded Vrest, that is, the K+ Nernst potential at which resact did not change Vm. Nernst potentials were calculated assuming an intracellular K+ concentration of 423 mM (Strünker et al., 2006). In simultaneous recordings of [Ca2+]i, pHi, and Vm, the Vm onset of the [Ca2+]i and pHi signals was deduced from their respective latencies.

To determine a probe’s crosstalk into orthogonal channels, the fluorescence values recorded in the different channels were plotted against each other for the particular time window indicated in the figure legend and fitted with a linear equation. The slope of the fit was multiplied by 100 to quantify, as a percentage, the extent of crosstalk.

### Caged compounds and flash photolysis

The protocol for loading sperm with BECMCM-cGMP is provided in Table 1. For uncaging, sperm were mixed with ASW and allowed to equilibrate in the cuvette for 5–10 s, after which a 50 ms pulse of UV light from a LED (M340L4; Thorlabs) was delivered using a custom-made triggering device.

### Simultaneous ratiometric recording of [Ca2+]i and pHi signals in human sperm

Samples of human semen were obtained from volunteers with their prior written consent, under approval of the institutional ethical committees of the medical association Westfalen-Lippe and the medical faculty of the Universtity of Münster (4INie). Human sperm were purified by ‘swim-up’ into human tubular fluid (HTF) as described previously (Strünker et al., 2011). Fura-FF AM (10 µM) was added to a sperm suspension (107 sperm/ml) supplemented with 0.05% Pluronic F-127 and incubated for 90 min at 37°C. The probe-loaded sperm were pelleted by centrifugation (700 × g, 5 min at 37°C), resuspended in HTF, and incubated for 60 min at 37°C to allow de-esterification of intracellular probe. BCECF AM (2 µM) was added to the Fura-FF-loaded sperm and incubated for 5 min; after which, sperm were pelleted (700 × g, 5 min at 37°C) and resuspended in HTF. The sperm density was adjusted to 6 × 107 sperm/ml.

The sperm suspension was rapidly mixed (1:1) with HTF, HTF containing 200 nM progesterone, or HTF containing 60 mM NH4Cl in a microvolume stopped-flow (µSFM, BioLogic) at a flow rate of 1 ml/s, resulting in a dead time of 1.9 ms. The optical configuration is summarized in Table 3. Signals to modulate the LEDs were provided by a lock-in amplifier (MFLI, Zurich Instruments) and a waveform generator (Agilent, 33220A), which was synchronized to the 10 MHz clock of the lock-in amplifier. Signals were amplified and frequency filtered by the lock-in amplifier using a third-order (18 dB/octave) lowpass filter and a time constant of 1 ms. Data acquisition was performed as described for sea urchin sperm, but with a sampling rate of 5 ms.

**Table 3.**
 Optical configuration for simultaneous ratiometric recording of [Ca2+]i and pHi signals in human sperm.


<table>
  <thead>
    <tr>
      <th>Fluorescent probe</th>
      <th>LED (Thorlabs)</th>
      <th>FASTM modulation frequency (kHz)</th>
      <th>Excitation filter (Semrock)</th>
      <th>Dichroics</th>
      <th>Emission filter(Semrock)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Fura-FF</td>
      <td>M340L4</td>
      <td>87.3</td>
      <td>340/22</td>
      <td rowspan="4">HC BS 365 (Semrock)HC BS 409 (Semrock)470 LPXR (Chroma)</td>
      <td rowspan="4">524/24</td>
    </tr>
    <tr>
      <td>M375L4</td>
      <td>73.51</td>
      <td>370/10</td>
    </tr>
    <tr>
      <td rowspan="2">BCECF</td>
      <td>M455L4</td>
      <td>61.7</td>
      <td>445/20</td>
    </tr>
    <tr>
      <td>M490L4</td>
      <td>103.7</td>
      <td>485/20</td>
    </tr>
  </tbody>
</table>

_FASTM, frequency- and spectrally-tuned multiplexing._

Each signal represents the average of at least three recordings. Dual-excitation ratiometric [Ca2+]i signals reported by Fura-FF were determined by dividing the fluorescence signal recorded upon excitation at 340 nm over that at 370 nm (340/370). Ratiometric pHi signals reported by BCECF were determined by dividing the signal recorded upon excitation at 485 nm over that at 445 nm (485/445). Signals are depicted as the percentage change in the ratio with respect to the mean of the first 3–10 data points after mixing (ΔR/R0 (%)). The baseline ΔR/R0 obtained upon mixing with HTF alone was subtracted. Signals were also depicted individually for each signal channel as fluorescence changes (ΔF/F0 (%)) and were calculated as described above for sea urchin sperm.

### Determination of Koff for fluorescent Ca2+ probes and of signal-to-noise ratios

Calbryte 630 (1 µM), Fluo-4 (1 µM), and Fura-2 (20 µM) dissolved in buffer containing 100 mM KCl, 20 mM HEPES, and 400 µM CaCl2 (pH 7.5) were rapidly mixed (1:1) with buffer containing 10 mM BAPTA (Sigma-Aldrich), 100 mM KCl, and 20 mM HEPES, (pH 7.5) in the µSFM at a flow rate of 1.3 ml/s, resulting in a dead time of 1.5 ms. The ensuing changes in probe fluorescence, reflecting the unbinding of Ca2+, were monitored with the optical configuration summarized in Table 4.

**Table 4.**
 Optical configuration for koff determination.


<table>
  <thead>
    <tr>
      <th>Fluorescent probe</th>
      <th>LED (Thorlabs)</th>
      <th>FASTM modulation frequency (kHz)</th>
      <th>Excitation filter (Semrock)</th>
      <th>Dichroics</th>
      <th>Emission filter(Semrock)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Fura-2</td>
      <td>M340L4</td>
      <td>87.31</td>
      <td>340/22</td>
      <td rowspan="4">HC BS 365 (Semrock)HC BS 409 (Semrock)525 LPXR (Chroma)</td>
      <td rowspan="3">524/24</td>
    </tr>
    <tr>
      <td>M375L4</td>
      <td>103.7</td>
      <td>370/10</td>
    </tr>
    <tr>
      <td>Fluo-4</td>
      <td>M490L4</td>
      <td>59.51</td>
      <td>485/20</td>
    </tr>
    <tr>
      <td>Calbryte 630</td>
      <td>M565L3</td>
      <td>47.1</td>
      <td>586/20</td>
      <td>647/57</td>
    </tr>
  </tbody>
</table>

_FASTM, frequency- and spectrally-tuned multiplexing._

Signals were amplified and frequency filtered with a third-order (18 dB/octave) lowpass filter and a time constant of 100 µs and were recorded as described for sea urchin sperm, but with a sampling rate of 100 µs. Each signal represents the average of at least five recordings. Signals are depicted as the relative change in fluorescence (ΔF/F0) with respect to the baseline signal (F0) recorded in 400 µM CaCl2, that is, in the absence of BAPTA (F0). To determine the koff, signal curves were fitted with a monoexponential decay with no fit constraints in GraphPad Prism 9 (Prism). The fluorescence crosstalk between channels was determined as described for recordings from sea urchin sperm.

For evaluation of the S/N ratio, Fura-2 (20 µM) in 100 mM KCl, 20 mM HEPES, and 400 µM CaCl2 (pH 7.5) was mixed with buffer containing 10 mM BAPTA, 100 mM KCl, and 20 mM HEPES (pH 7.5). Fluorescence was excited by light from a single LED (M375L4, fitted with a 370/10 filter) that delivered either continuous or modulated (103.7 kHz) light to the observation cuvette. To detect Fura-2 fluorescence excited by modulated illumination, the recording configuration was the same as described above, except that the time constant of the lock-in amplifier was varied between 100 µs and 2 ms with a matching sample rate. To detect fluorescence excited by continuous illumination, the signal was amplified and filtered through a conventional voltage amplifier (DLPVA-100-B-S: Femto Messtechnik) and subsequently routed to the data acquisition pad (PCI-6221; National Instruments) and Bio-Kine software (BioLogic). The S/N ratio was calculated by dividing the mean signal intensity by the standard deviation over 200 data points.

### Recording of fluorescence spectra

Fluorescence spectra were recorded from 50 µl of either a probe-containing solution or a probe-loaded sperm suspension in 384-well plates (Greiner) with a fluorescent plate reader (CLARIOStar, BMG) in spectral scanning mode using bottom optics.

For sea urchin sperm, dry sperm was diluted 1:6 (v/v) in ASW and loaded with a fluorescent probe according to Table 1. The probe-loaded sperm suspension was further diluted 1:10 (v/v) with ASW for spectral acquisition.

For human sperm, loading with either Fura-FF AM or BCECF AM was performed as described above. The probe-loaded sperm suspension (107 sperm/ml) was centrifuged (700 × g for 5 min at 37°C) and resuspended in different buffers to a concentration of 2 × 107 sperm/ml. Fura-FF-loaded sperm were resuspended in HTF supplemented with 10 µM ionomycin (Biomol) or Ca2+-free HTF supplemented with 5 mM EGTA (Sigma-Aldrich). BCECF-loaded sperm were resuspended in HTF adjusted to either pH 6.5 or pH 8.5.

For spectral acquisition of probes in solution, either Fura-2, Fluo-4, or Calbryte 630 was diluted to 1 µM in a buffer containing 100 mM KCl, 20 mM HEPES (pH 7.5), and either 400 µM CaCl2 or 5 mM EGTA.

### Single-cell recordings of intracellular cAMP and [Ca2+]i

HEK293 cells (flp-In-293) stably transfected with expression constructs encoding the biogenic amine receptor DmOCTβ1R from Drosophila melanogaster (Balfanz et al., 2005) and the bovine CNGA2-TM channel (Wachten et al., 2006; Schröder-Lang et al., 2007) were cultured in DMEM plus GlutaMAX (Thermo Fisher Scientific) supplemented with 10% fetal bovine serum (Biochrom) and 1× penicillin/streptomycin (Thermo Fisher Scientific) with selective pressure provided by G418 (800 µg/ml) (Thermo Scientific) and hygromycin (100 µg/ml) (Thermo Fisher Scientific) for constitutive expression of DmOCTB1R, respectively. Authentication was performed by functional tests as shown in Figure 10. Cell lines were negatively tested for mycoplasma contamination. The cells were seeded onto 5 mm glass coverslips (#1; Thermo Fisher Scientific) that were coated with poly-L-lysine (Sigma-Aldrich). To yield cells expressing a FRET-based cAMP biosensor, DmOCTβ1 receptors, and CNGA2 channels, cells at 50–60% confluency were transfected using Lipofectamine 2000 (Invitrogen) according to the manufacturer’s protocol with either pc3.1-mlCNBD-FRET (high cAMP affinity), pc3.1-mlCNBD-FRET-R307Q (non-binding) (Mukherjee et al., 2016), or pc3.1-mlCNBD-FRET-M329C (low cAMP affinity). Using pc3.1-mlCNBD-FRET as a template, we performed QuikExchange (Agilent) to introduce the M329C mutation. All vectors are based on the pcDNA3.1(+) vector and contain a neomycin-resistant cassette for selection in mammalian cells. To load the cells with Calbryte 630 AM, cells adhered to cover slips were washed once with ES (in mM): 120 NaCl, 5 KCl, 2 CaCl2, 10 HEPES, and 10 glucose, adjusted to pH 7.5 with NaOH and then incubated in ES supplemented with 10 µM Calbryte 630 AM, 0.05% Pluronic, and 3 mM Probenecid (Sigma-Aldrich) for 10 min at 37°C. Cells were washed once with ES to remove unloaded probe. Coverslips were transferred to a custom-built headstage chamber that was fit with a custom-built gravity flow-perfusion system and imaged with an inverted microscope (IX73; Olympus). The excitation module consisted of a blue LED (M455L4; Thorlabs) fitted with a 438/24 nm filter (Semrock) and a green LED (M565L3; Thorlabs) fitted with a 565/24 nm filter (Semrock). The blue and green LEDs were modulated at 36.1 and 49.5 kHz, respectively, by lock-in amplifiers (MFLI, Zurich Instruments, or SR844 RF, Stanford Research Systems). The modulated output of these LEDs was combined on a dichroic (470 LPXR; Chroma), passed through a neutral density filter (NDUV20A; Thorlabs) and a CFP-YFP-mCherry filter cube (AHF Analysetechnik), and focused onto the sample with a ×60 water immersion objective (UPlanSApo, numerical aperture [NA] 1.2; Olympus). The modulated fluorescence signals were directed through the CFP-YFP-mCherry filter cube and split by a dichroic (525 LPXR; Chroma) onto two PMTs. One PMT was fitted with a 475/28 nm bandpass filter (Semrock) to collect fluorescence from the FRET donor (cerulean). The other PMT was fitted with a 578/105 nm bandpass filter (Semrock) to collect fluorescence from the FRET acceptor (citrine) and the Ca2+ probe (Calbryte 630). Signals were routed to lock-in amplifiers, where they were amplified and frequency filtered with a third--order (18 dB/octave) lowpass filter and a time constant of 10 ms. Data were acquired at 200 Hz with an analog-to-digital converter (Axon Digidata 1550A; Molecular Devices) and pCLAMP software (Molecular Devices). Selection of single cells was performed with brightfield illumination using a halogen light source (TH4-200; Olympus) and a condenser (IX2-MLWPO, NA 0.5; Olympus). An aluminum mirror (Chroma) was temporarily installed in the optical path to divert transmitted light to a camera (IDS Imaging). Cells expressing the FRET-based cAMP sensor were selected based on fluorescence. If necessary, an aperture was adjusted to encircle the cell of interest to isolate its fluorescence from surrounding cells. After selection, the mirror was removed, directing the fluorescence to the PMTs. To measure cAMP and [Ca2+]i signals, cells were perfused with ES for 20 s, then perfusion was switched to ES containing 20 µM octopamine. The FRET ratio, that is, cAMP signal, was calculated by dividing the signal recorded in the donor (cerulean) channel by the signal recorded in the acceptor (citrine) channel. The FRET ratio is shown as the percent change in the FRET ratio with respect to the mean value of the first 1 s of recording (ΔR/R0 (%)). The [Ca2+]i signals are shown as the percent change in fluorescence with respect to the mean of the first 1 s of recording (ΔF/F0). The latencies of the FRET and [Ca2+]i signals were deduced from the signal time course.
