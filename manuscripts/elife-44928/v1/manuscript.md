# GABA neurons in the ventral tegmental area regulate non-rapid eye movement sleep in mice

## Authors

- Srikanta Chowdhury<sup>1</sup> ([ORCID: 0000-0002-2216-5960](https://orcid.org/0000-0002-2216-5960))
- Takanori Matsubara<sup>1</sup>
- Toh Miyazaki<sup>1</sup>
- Daisuke Ono<sup>1</sup>
- Noriaki Fukatsu<sup>1</sup>
- Manabu Abe<sup>5</sup>
- Kenji Sakimura<sup>5</sup>
- Yuki Sudo<sup>6</sup>
- Akihiro Yamanaka<sup>1</sup> ([ORCID: 0000-0001-6099-7306](https://orcid.org/0000-0001-6099-7306)) †

### Affiliations

1. Department of Neuroscience II, Research Institute of Environmental Medicine Nagoya University Nagoya Japan
2. Department of Neural Regulation,Graduate School of Medicine Nagoya University Nagoya Japan
3. CREST, JST, Honcho Kawaguchi Saitama Japan
4. Research Fellowship for Young Scientist Japan Society for the Promotion of Science Tokyo Japan
5. Department of Animal Model development, Brain Research Institute Niigata University Niigata Japan
6. Division of Pharmaceutical Sciences, Graduate School of Medicine, Dentistry, and Pharmaceutical Sciences Okayama University Okayama Japan

† Corresponding author

## Abstract

Sleep/wakefulness cycle is regulated by coordinated interactions between sleep- and wakefulness-regulating neural circuitry. However, the detailed mechanism is far from understood. Here, we found that glutamic acid decarboxylase 67-positive GABAergic neurons in the ventral tegmental area (VTAGad67+) are a key regulator of non-rapid eye movement (NREM) sleep in mice. VTAGad67+ project to multiple brain areas implicated in sleep/wakefulness regulation such as the lateral hypothalamus (LH). Chemogenetic activation of VTAGad67+ promoted NREM sleep with higher delta power whereas optogenetic inhibition of these induced prompt arousal from NREM sleep, even under highly somnolescent conditions, but not from REM sleep. VTAGad67+ showed the highest activity in NREM sleep and the lowest activity in REM sleep. Moreover, VTAGad67+ directly innervated and inhibited wake-promoting orexin/hypocretin neurons by releasing GABA. As such, optogenetic activation of VTAGad67+ terminals in the LH promoted NREM sleep. Taken together, we revealed that VTAGad67+ play an important role in the regulation of NREM sleep.

## Introduction

Sleep or sleep-like behavioral quiescence is known to be one of the most ubiquitously observed phenomena across the animal kingdom, from nematodes to primates (Joiner, 2016; Siegel, 2008). Broadly, sleep consists of non-rapid eye movement (NREM) sleep and REM sleep in mammals (Siegel, 2008). While the physiological functions of either NREM sleep or REM sleep, or sleep as a whole, are intriguing and shrouded in mystery, sleep deprivation in humans and experimental animals causes severe cognitive impairment (Siegel, 2008). Pioneering studies discovered certain physiological functions of sleep that include clearing metabolic waste products and toxins from the brain (Xie et al., 2013), memory encoding, consolidation and erasure (Rasch and Born, 2013), synaptic homeostasis (Bushey et al., 2011), and energy conservation (Schmidt, 2014). However, a universal function of sleep that is relevant to all animals is yet to be revealed (Joiner, 2016). As animals remain largely isolated from sensory processing and goal-oriented activity during sleep, it is expected that the regulation of sleep, both NREM and REM, as well as arousal should be controlled by the central nervous system. Many brain areas and residing cellular subtypes have been shown to be critical in regulating sleep-wakefulness. For instance, orexin/hypocretin-producing neurons (orexin neurons) in the lateral hypothalamus (LH) project to and activate monoaminergic, cholinergic, and other peptidergic neurons as well as other orexin neurons to induce and maintain wakefulness (Brown et al., 2012; Inutsuka and Yamanaka, 2013; Sakurai, 2007; Scammell et al., 2017). Subsequently, these monoamine neurons inhibit sleep-active γ-aminobutyric acid (GABA)-ergic neurons in the ventrolateral preoptic area (VLPO) in the hypothalamus to induce wakefulness (Saito et al., 2018; Saper et al., 2010). It is reported that some wake-active neurons also display activity during REM sleep (Brown et al., 2012; Scammell et al., 2017). Comparatively, NREM sleep is regulated by neurons that release classical fast neurotransmitters, including GABA. For example, circadian rhythms and/or homeostatic sleep pressures activate GABAergic neurons in the VLPO and median preoptic nucleus (MnPO), which in turn inhibit wake-promoting orexin/hypocretin, monoaminergic, and cholinergic systems (Scammell et al., 2017). While this flip-flop switch model of sleep-wake regulation is well established, recent studies have demonstrated a critical involvement of other brain areas and neuronal subtypes in regulating the transformations and subsequent maintenance of specific vigilances states (Liu et al., 2017; Oishi et al., 2017b).

Reinforcement learning, motivation, and locomotion, as well as the adaptation of responses to salient stimuli, all of which demand behavioral arousal, are critically regulated by a midbrain structure called the ventral tegmental area (VTA) in both rodents and primates (Arsenault et al., 2014; Fields et al., 2007). While one could also expect a critical role for VTA in the regulation of sleep/wakefulness, it is only recently that VTA dopamine (DA) neurons have been reported to have a fundamental role in the maintenance of the awake state as well as in the consolidation of arousal in mice (Eban-Rothschild et al., 2016; Oishi et al., 2017a). However, the VTA contains considerable heterogeneity among the neuronal subtypes, which include GABAergic and glutamatergic neurons alongside DA neurons. Studies have reported that about 60–65% of VTA neurons are dopaminergic, whereas 30–35% are GABAergic, and 2–3% are glutamatergic neurons (Nair-Roberts et al., 2008; Pignatelli and Bonci, 2015).

As GABAergic neurons provide strong inhibition to the wake- and REM-active DA neurons in the VTA (Eban-Rothschild et al., 2016; Tan et al., 2012; van Zessen et al., 2012), it is probable that these GABAergic neurons in the VTA may also participate in sleep/wakefulness regulation. Moreover, GABA-mediated responses have been implicated in the modulation of the sleep/wakefulness cycle (Brown et al., 2012; Scammell et al., 2017). Here, we examined the role of glutamic acid decarboxylase 67 (Gad67)-positive neurons in the VTA on sleep/wakefulness by using AAV-aided whole-brain anterograde tracing, neural manipulations by chemo- and optogenetics, fiber photometry, as well as slice electrophysiology. Gad67 (encoded by Gad1 gene) is an isomer of an enzyme that synthesizes GABA from glutamic acid, suggesting that Gad67+ neurons are GABAergic neurons (Erlander et al., 1991). We revealed that Gad67+ neurons in the VTA (VTAGad67+ neurons) are highly active during NREM sleep and send their axons to multiple brain areas that were previously reported to regulate sleep/wakefulness. Bidirectional manipulations of neuronal activity and fiber photometry recordings revealed that VTAGad67+ neurons are active in and promote NREM sleep. Part of the NREM sleep-promoting effect of VTAGad67+ is mediated through inhibition of wake-promoting orexin/hypocretin neurons in the LH.

## Results

### GABAergic neurons in the VTA project to brain areas involved in the regulation of sleep/wakefulness

Glutamatergic, GABAergic, and dopaminergic (DA) neurons are intermingled in the VTA (Nair-Roberts et al., 2008; Pignatelli and Bonci, 2015). Here, we focused on the GABAergic neurons and tried to identify relevant projection areas. To specifically target GABAergic neurons in the VTA (VTAGABA neurons), Gad67-Cre mice (Higo et al., 2009) were unilaterally injected with a Cre-inducible AAV virus carrying humanized renilla green fluorescent protein (hrGFP) (Figure 1a). Many hrGFP-positive neurons were observed in the VTA (Figure 1b–d). These hrGFP-positive neurons were Gad67-positive but tyrosine hydroxylase-negative (TH, an enzyme and marker of DA neurons in the VTA) (Figure 1b, n = 4 mice) confirming that these hrGFP-positive neurons were GABAergic. At least 3 weeks after unilateral injection of AAV aimed at the VTA to express hrGFP, we prepared coronal brain sections at 40 µm thickness and counted all labeled cells on every fourth section. Within the VTA, we counted a total of 636 ± 122 neurons per animal (n = 4 mice). Among them, 63.5 ± 1.8% were TH-positive neurons (DA neurons) and 36.1 ± 1.8% were hrGFP-positive neurons. Only 0.4 ± 0.1% were co-labeled with hrGFP and TH (Figure 1c). hrGFP was distributed not only in the soma, but also in the axons. We could even anterogradely trace axons to reveal projection sites since hrGFP emits a strong fluorescence (Figure 1d–f). Along with local innervations, we found long-range projections of Gad67+ neurons in the VTA (VTAGad67+ neurons) throughout the brain. Among these sites, the lateral hypothalamus (LH) and the central nucleus of the amygdala (CeA) were densely innervated (Figure 1e–f). Moderate projections were found in the nucleus accumbens (NAc), ventral pallidum (VP), parafascicular thalamic nucleus (PF), periaqueductal gray (PAG), ventral nucleus of the lateral lemniscus (VLL), dorsal raphe nucleus (DR), and pontine reticular nucleus (PnO). These brain areas are also reported to be involved in the modulation of sleep/wakefulness, suggesting that VTAGad67+ neurons might play a role in this regulation (Brown et al., 2012).

![Figure 1.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig1-v1.jpg)

**Figure 1.:** (a) Schematic of AAV injection to express Cre-inducible hrGFP in Gad67-Cre mice. The dotted brain map area is shown to the right. White rectangular area is shown below. (b) Immunohistochemical studies showing expression of hrGFP in Gad67+ neurons (arrowhead), but not in the nearby DA (arrow) neurons. (c) Pie chart showing the percent of hrGFP expression in DA and non-DA neurons in the VTA (n = 4 mice). (d and e) Expression of hrGFP in VTAGad67+ neurons and some of their projected brain areas are shown. (f) Table showing the comparative scoring of hrGFP signals across different brain areas. Abbreviations- AcbC: Nucleus accumbens core, AcbSh: Nucleus accumbens shell, BLA: Basolateral amygdala, CeA: Central nucleus of the amygdala, CM: Central medial thalamic nucleus, CnF: Cuneiform nucleus, CPu: Caudate putamen (striatum), DEn: Dorsal endopiriform nucleus, DR: Dorsal raphe nucleus, IMD: Intermediodorsal thalamic nucleus, InG: Intermediate gray layer of the superior colliculus, LH: Lateral hypothalamus, LPO: Lateral preoptic area, MM: Medial mammillary nucleus, Pa4: Paratrochlear nucleus, PAG: Periaqueductal gray, PF: Parafascicular thalamic nucleus, PnO: Pontine reticular nucleus, SubB: Subbrachial nucleus, VLL: Ventral nucleus of the lateral lemniscus, VP: Ventral pallidum, Xi: Xiphoid thalamic nucleus and xscp: Decussation of the superior cerebellar peduncles. DAPI (4′,6-diamidino-2-phenylindole) staining was used to label nuclear DNA and also to assist understanding of the anatomical position of VTAGad67+ neuronal projections.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (a) Schematic of AAV micro-injection to express mCherry in VTAGad67+ neurons in Gad67-Cre mice. (b) Confocal images showing multiplex fluorescence detection by using probes against Gad67, mCherry, and Vgat mRNA. Dotted rectangular area in the upper panels are enlarged in the lower panels. (c) Bar and venn diagram showing the percent of Gad67+ neurons co-expressing Vgat. (d) Bar and venn diagram showing the percent of Gad67+ and Vgat+ neurons co-expressing mCherry (n = 4 mice). Numbers in the parenthesis indicate total number of neurons counted in all animals. Data are represented as mean ± SEM.

### VTAGad67+ neurons represent a small subset of Vgat-expressing neurons in the VTA

To reveal what percent of total GABAergic neurons in the VTA are Gad67-positive, we performed in situ hybridization using RNAscope technology. We injected Cre-inducible AAV (AAV(9)-CAG-FLEX-mCherry) into the VTA of Gad67-Cre mice (n = 4 mice) to label Gad67-expressing neurons (Figure 1—figure supplement 1a). We selected probes to visualize Gad67, Vgat (SLC32A1), and mCherry (Table 1). Gad67, Vgat (vesicular GABA transporter), and mCherry mRNA were visualized by multicolor in situ hybridization (Figure 1—figure supplement 1b). Regarding Gad67 and Vgat expression, we found three different types of neurons: Vgat-only (66.8 ± 2.0%), Gad67-only (1.1 ± 0.1%), and Vgat and Gad67 double-positive neurons (32.1 ± 2.1%) (Figure 1—figure supplement 1c). Whereas 96.5 ± 0.5% of Gad67-positive neurons co-expressed Vgat mRNA, only 32.4 ± 2.1% of Vgat-positive neurons co-expressed Gad67 mRNA in the VTA (Figure 1—figure supplement 1c). Consistent with these findings, 94.8 ± 1.5% of mCherry-positive neurons in the VTA of Gad67-Cre mice co-expressed Gad67 and Vgat mRNA (Figure 1—figure supplement 1d). These results indicate that Gad67-positive neurons represent a small subset of Vgat-positive neurons in the VTA.

**Table 1.**
 Details of probes designed for in situ hybridization.


<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>Channel</th>
      <th>Color</th>
      <th>Position</th>
      <th>Accession</th>
      <th>Catalog number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gad67</td>
      <td>1</td>
      <td>Opal 520</td>
      <td>62-3113</td>
      <td>NM_008077.4</td>
      <td>400951</td>
    </tr>
    <tr>
      <td>Vgat (SLC32A1)</td>
      <td>4</td>
      <td>Opal 690</td>
      <td>894-2037</td>
      <td>NM_009508.2</td>
      <td>319191-C4</td>
    </tr>
    <tr>
      <td>mCherry</td>
      <td>3</td>
      <td>Opal 620</td>
      <td>23-681</td>
      <td>n/a</td>
      <td>431201-C3</td>
    </tr>
  </tbody>
</table>

### Chemogenetic activation of VTAGad67+ neurons induced NREM sleep with high delta power

Next, to reveal whether VTAGad67+ neurons contribute to the regulation of sleep/wakefulness, we activated these neurons by means of pharmacogenetics (chemicogenetics), using designer receptors exclusively activated by designer drugs (DREADD). We bilaterally injected a Cre-inducible AAV virus to express either hM3Dq-mCherry or mCherry into the VTA of Gad67-Cre mice (Figure 2a–b, Figure 2—figure supplement 1a–b). We then confirmed the function of hM3Dq by applying its ligand clozapine-N-oxide (CNO) to acute brain slices while recording neuronal activity (Figure 2—figure supplement 1c). As expected, CNO application significantly increased the firing frequency of hM3Dq-expressing, but not mCherry-expressing, VTAGad67+ neurons (Figure 2—figure supplement 1d–e, hM3Dq: 286 ± 61%, n = 8 cells; mCherry: 110 ± 8%, n = 6 cells, p=0.02, unpaired t-test). Next, to analyze the effect of CNO-induced activation of VTAGad67+ neurons in sleep/wakefulness states, electroencephalogram (EEG) and electromyogram (EMG) electrodes were implanted in Gad67-Cre mice (Figure 2a). After recovery from the surgery and behavioral habituation (see Materials and methods), either saline or CNO (1 mg/kg) were administered intraperitoneally (i.p.) just before the onset of the dark period (at 8:00 pm). CNO administration resulted in a significantly reduced time spent in wakefulness and increased time spent in NREM sleep (also known as slow-wave sleep) in the hM3Dq-mCherry expressing mice, but not in mCherry-expressing mice (Figure 2c–d, hM3Dq: n = 6 mice, mCherry: n = 4 mice). The CNO-induced increase in NREM sleep lasted for at least 4 hr after CNO administration (Figure 2d, % change from saline in hM3Dq-mCherry-expressing mice: wakefulness 22 ± 2, NREM 259 ± 18, REM 30 ± 8, vs saline NREM, p=3.0e-4, paired t-test). Interestingly, the delta power (1–5 Hz) during NREM sleep was significantly increased in the CNO-injected group compared to the NREM sleep in the saline-injected control group (mean relative delta power for 4 hr post-injection: hM3Dq-saine: 83 ± 3%, hM3Dq-saine: 138 ± 8%, p=0.001, paired t-test), suggesting that VTAGad67+ neurons might be a critical regulator of slow-wave in NREM sleep (Figure 2e–g). However, time spent in REM sleep remained unaffected during activation of VTAGad67+ neurons, suggesting that VTAGad67+ neurons are involved in the regulation of NREM sleep, but not REM sleep (Figure 2c–d).

![Figure 2.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig2-v1.jpg)

**Figure 2.:** (a) Schematic of Cre-inducible expression of either hM3Dq-mCherry or mCherry in VTAGad67+ neurons. (b) Immunohistochemical confirmation of hM3Dq-mCherry expression in VTA non-DA neurons. (c) Time spent in each vigilance state before and after i.p. administration of either saline or CNO. Arrowhead indicates timing of injection (just before the dark period; hM3Dq: n = 6 mice; mCherry: n = 4 mice). White and gray bars above the x-axis indicate light and dark periods, respectively. (d) 4 hr average time spent in each vigilance state after i.p. administration. (e) Relative power of fast Fourier transformation (FFT) analysis of NREM sleep for hM3Dq-expressing saline and CNO groups before (pre: left) and after (1 hr post: middle, 4 hr post: right) i.p. administration. (f) Heatmap showing a trace indicating that delta wave power activity increases after CNO administration compared to the saline control. (g) Summary of the delta wave power change during NREM sleep after saline or CNO injection. Traces in dark color indicate mean value, while lighter color indicates EEG spectrum of each mice injected with saline (black) and CNO (red). Inset shows the mean relative delta power for 4 hr after either saline or CNO administration. Data are shown as the mean ± SEM (hM3Dq: n = 6 mice; mCherry: n = 4 mice). *p<0.05, ***p<0.001, (d) two-way ANOVA followed by Tukey post hoc, (e) two-tailed paired Student’s t-test (n = 8 mice).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (a) Schematic of Cre-mediated expression of either hM3Dq-mCherry or mCherry alone in Gad67-Cre mice. (b) Histological verification and reconstruction of hM3Dq-mCherry expressing areas in mice used in Figure 2. (c) Schematic of patch clamp recording from hM3Dq-mCherry- or mCherry-expressing neurons in the VTA while applying CNO through the bath solution. (d) Traces showing CNO-induced increases in firing of VTAGad67+ neurons expressing hM3Dq-mCherry, but not of neurons expressing mCherry alone. (e) Summary of experiment in (d) showing firing rate as a percent of baseline (average for 5 s before CNO application). CNO was applied at a concentration of 30 µM (hM3Dq: n = 8 cells and mCherry: n = 6 cells, p=0.02, two-tailed unpaired Student’s t-test). Data are represented as mean ± SEM.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (a and b) Power spectra before (pre: left) and after 4 hr (post (4 hr): right) i.p. administration is shown. Note that during the wake period at 4 hr post-CNO injection mice display an EEG power spectrum with lower theta power, presumably because pharmacological activation lasts up to 4 hr after i.p. administration.

### Optogenetic inhibition of VTAGad67+ neurons induced wakefulness

Since activation of VTAGad67+ neurons resulted in increases in NREM sleep with increases in delta wave power, we next examined the selective inhibition of VTAGad67+ neurons, which might be expected to increase wakefulness. To test this, we used an acute inhibition strategy with optogenetics. An inhibitory anion channel, anion channelrhodopsin-2 (ACR2, Genbank accession no. KP171709) (Mohammad et al., 2017), was expressed in VTAGad67+ neurons (Figure 3a and Figure 3—figure supplement 1a–b). We first confirmed the function of ACR2 employing in vitro electrophysiology. Three weeks after injection of AAV (expressing either ACR2-2A-mCherry or mCherry) into the VTA of Gad67-Cre mice, we prepared acute brain slices including the VTA and performed cell-attached recordings from mCherry-expressing neurons. Blue light (6.8 mW/mm2) was able to completely silence the spontaneous activity of ACR2-2A-mCherry-expressing VTAGad67+ neurons (n = 10 cells), whereas light irradiation on mCherry alone-expressing neurons had no such effect (n = 7 cells) (Figure 3—figure supplement 1d–f). Next, using these two groups of mice, we implanted fiber optics at a diameter of 400 µm into the VTA along with EEG and EMG electrodes (Figure 3a and b). After recovery and habituation, continuous blue light for 5 s was illuminated every 15 min for 24 hr (Figure 3c). Interestingly, blue light illumination immediately induced wakefulness from NREM sleep, but not from REM sleep, in mice expressing ACR2-2A-mCherry (n = 6 mice, Figure 3d–f, Video 1). No such effect was observed in mice expressing mCherry alone (n = 5 mice, Video 2). However, as the light-induced influences on NREM sleep and wakefulness showed an extended effect after the cessation of light (Figure 3d–e), with behaviors taking around 60 s to return to the basal state, we sought to identify whether optogenetic inhibition of VTAGad67+ neurons also causes prolonged wakefulness. We, therefore, isolated the trials depending on sleep-wakefulness states just before light illumination in the cases of wakefulness, NREM, or REM sleep (with the same state lasting ≥30 s before light illumination). Surprisingly, we found that optogenetic inhibition of VTAGad67+ neurons in the state of wakefulness prolonged the time spent in wakefulness in all sorted trials compared to behavior of the control group (Figure 3f, ACR2: 35 ± 5 s, mCherry: 8 ± 8 s; p=0.02, unpaired t-test). Again, REM sleep was not affected. Therefore, these data showed that in vivo optogenetic inhibition of VTAGad67+ neurons promoted and sustained wakefulness in mice. This result clearly suggested that VTAGad67+ neurons have a role in the regulation of not only NREM sleep but also wakefulness.

![Video 1.](https://cdn.elifesciences.org/articles/44928/elife-44928-video1.mp4.jpg)

**Video 1.:** Blue light (475 ± 18 nm, 10 mW, 5 s) was illuminated in the VTA area in each vigilance state to inhibit ACR2-expressing VTAGad67+ neurons. EEG, EMG, and light stimulation signals appear at the top of the window.

![Video 2.](https://cdn.elifesciences.org/articles/44928/elife-44928-video2.mp4.jpg)

**Video 2.:** Blue light (475 ± 18 nm, 10 mW, 5 s) was illuminated in the VTA area in each vigilance state in mCherry-expressing Gad67-Cre mice. EEG, EMG, and light stimulation signals appear at the top of the window.

![Figure 3.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig3-v1.jpg)

**Figure 3.:** (a) Schematic of surgery showing Gad67-Cre mice expressing either ACR2-2A-mCherry or mCherry alone that were subjected to implantation of fiber optics and EEG-EMG electrodes. (b) Schematic of fiber optic implantation (left). Pictures indicate position of tip of fiber optics and ACR2-2A-mCherry expression and DAT-positive neurons in the VTA. (c) Schematic of protocol for light stimulation in optogenetic inhibition experiments. (d) Representative traces showing EEG, EEG power spectra, and EMG during optogenetic inhibition in different vigilance states (wake, NREM, and REM sleep). Vigilance states are indicated by colored bars above the EEG traces. (e) Probability of vigilance state before and after light illumination in all recorded trials of ACR2-2A-mCherry or mCherry-alone expressing mice. Blue and red lines indicate mean probability of each vigilance state, ACR2-2A-mCherry (n = 6 mice) and mCherry (n = 5 mice). (f) Light illumination during wakefulness, NREM, or REM sleep was isolated from subfigure e (ACR2-2A-mCherry = 6 mice; and mCherry = 5 mice). Each vigilance state lasted for at least 30 s before light illumination was isolated. SEM is indicated as the lighter color band.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (a) Schematic of Cre-inducible expression of either ACR2 (AAV(9)-CMV-FLEX-ACR2-2A-mCherry, 300 nl each side, 6.2 × 1012 copies/ml) or mCherry (AAV(9)-CAG-FLEX-mCherry, 300 nl each side, 1.9 × 1012 copies/ml) in VTAGad67+ neurons. (b) Immunohistochemical confirmation that ACR2-2A-mCherry-positive Gad67+ neurons are not co-expressing the dopamine transporter (DAT, expressed by DA neurons in the VTA). (c) Schematic of recordings from ACR2-2A-mCherry or mCherry-expressing VTAGad67+ neurons. (d and e) Traces showing firing in a loose cell-attached mode from VTAGad67+ neurons expressing either ACR2-2A-mCherry (d) or mCherry alone (e). (f) Summary of experiment in (d) and (e), showing the firing rate as a percent of baseline (average for 5 s before illumination). Blue light of 6.8 mW/mm2 was illuminated for 5 s (ACR2: n = 10 and mCherry: n = 7). Data are represented as mean ± SEM.

Next, we tested whether brief (5 s) optogenetic inhibition of VTAGad67+ neurons can induce arousal even under conditions of high homeostatic sleep pressure. To test this, mice were sleep-deprived for 4 hr, starting at light onset, and were then allowed to experience recovery sleep for 30 min (Figure 4a). Sleep-deprived animals usually display extended NREM sleep because of high homeostatic sleep pressure. Moreover, the slow-wave activity in NREM sleep increases during recovery sleep (Lancel et al., 1992). However, to our surprise, even under such a higher sleep pressure condition, optogenetic inhibition of VTAGad67+ neurons could successfully and immediately induce wakefulness in all trials (Figure 4b and c). Once again, induced-wakefulness displayed an extended effect after cessation of light, whereby it took 54 ± 14 s to return to NREM sleep. Taken together, these results suggest that VTAGad67+ neurons might be involved in the initiation and maintenance of physiological NREM sleep.

![Figure 4.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig4-v1.jpg)

**Figure 4.:** (a) Schematic of the protocol of the experiment. (b) EEG, EEG power spectra, and EMG before and after optogenetic inhibition during recovery sleep after 4 hr sleep deprivation. (c) Summary of the experiment in (a) showing the probability of each vigilance state before and after blue light illumination. Colored circles and lines indicate mean probability of each vigilance state and shaded area indicates SEM (ACR2-2A-mCherry: n = 6 mice and mCherry alone: n = 5 mice).

### VTAGad67+ neurons showed the highest population activity during NREM sleep

Our chemogenetic activation and optogenetic inhibition studies suggest that the in vivo activity of VTAGad67+ neurons might change across brain states with putatively higher activity during NREM sleep. To test this hypothesis, we recorded the population activity of VTAGad67+ neurons using fiber photometry (Inutsuka et al., 2016). A Cre-inducible AAV expressing the fluorescent calcium indicator GCaMP6f (Chen et al., 2013) was unilaterally injected into the VTA of Gad67-Cre mice (n = 8 mice; Figure 5a and Figure 5—figure supplement 1a). First, we tested whether GCaMP6f signal from VTAGad67+ neurons correspond to firing frequency in vitro (Figure 5—figure supplement 1b). The fluorescence intensity from GCaMP6f was increased in an evoked firing frequency-dependent manner (n = 13 cells; Figure 5—figure supplement 1c–e, ΔF/F (%, normalized to 100 Hz), 10 Hz: 9.2 ± 3.0, 20 Hz: 23.0 ± 5.4, 50 Hz: 52.1 ± 6.2). Next, activity recordings were performed in vivo by a fiber optic inserted into the VTA area (Figure 5—figure supplement 2b). Offline determination of vigilance states was aided by signals from EEG-EMG electrodes (Figure 5a–b). Both fluorescence and EEG-EMG were recorded during the light period in the home cage after habituation. We observed robust changes in the fluorescence signal across brain states (Figure 5c, Figure 5—figure supplement 1f). To facilitate the statistical analyses of mean ΔF/F among vigilance states, we compared the fluorescence signal at the transition of vigilance states. We found that VTAGad67+ neurons show the highest population activity during NREM and the lowest during REM sleep (Figure 5d, Figure 5—figure supplement 1f). Notably, VTAGad67+ neurons began to increase their activity before wake-to-NREM transitions (mean ΔF/F: Wake: 2.9 ± 0.4%, NREM: 3.8 ± 0.4%, p=2.5e-6) and decrease their activity before NREM-to-REM (mean ΔF/F: NREM: 5.0 ± 0.5%, REM: 2.7 ± 0.3%, p=2.4e-5) and NREM-to-wake (mean ΔF/F: NREM: 3.8 ± 0.5%, wake: 3.0 ± 0.4%, p=2.4e-4) transitions. However, the changes in signal from REM-to-wake (mean ΔF/F: REM: 2.9 ± 0.4%, wake: 3.7 ± 0.5%, p=0.02) was comparatively less significant and occurred only after the onset of state transition. Most interestingly, the population activity of VTAGad67+ neurons was found to be completely contrary to DA neuronal activity in the VTA (Dahan et al., 2007; Eban-Rothschild et al., 2016), further suggesting that Gad67+ neurons and DA neurons differentially modulate sleep-wakefulness in mice (Eban-Rothschild et al., 2016).

![Figure 5.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig5-v1.jpg)

**Figure 5.:** (a) Schematic of GCaMP6f expression in VTAGad67+ neurons and position of fiber optics. Gad67-Cre mice expressing GCaMP6f were subjected to implantation of guide cannula, EEG, and EMG electrodes. PMT indicates photomultiplier tube. (b) Immunohistochemical studies confirmed that GCaMP6f expression was in the TH-negative cells in the VTA. (c) Representative traces of EEG, EEG spectra, EMG, and fluorescent intensity from GCaMP6f (represented as ΔF/F) in a trial having all different states. Vigilance states were determined by EEG and EMG signals and indicated by colored bars. (d) Fluorescent intensity alterations in each trial 60 s before and after vigilance state changes. Upper panel shows the heat map of all separated transitions. Middle panel represents the changes in the intensity of calcium signals represented as ΔF/F. Gray lines indicate average intensities in individual mice and the green line indicates the mean of all mice. Lower panel indicates the average intensity separated for specific vigilance states. Data are represented as mean ± SEM. ***, p<0.001; *, p<0.05. Two-tailed paired Student’s t-test (n = 8 mice).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (a and b) Schematic of Cre-inducible expression of GCaMP6f in VTAGad67+ neurons (a), and simultaneous recording of membrane potential by electrophysiology and changes in intracellular calcium concentration by calcium imaging from GCaMP6f-expressing VTAGad67+ neurons (b) in brain slice using Gad67-Cre mice. (c) Representative traces showing the correlation between the action potential frequency (middle trace) and the increase in calcium concentration intensity (ΔF/F, upper trace). Action potentials were generated by injecting depolarizing current (~50 pA, lower trace) through the recording pipette at 10 Hz, 20 Hz, 50 Hz, and 100 Hz, while the ΔF/F was simultaneously measured from the same VTAGad67+ neuron. i and ii show 10 and 100 Hz current-induced action potentials. (d, e) Summarized data showing induced firing probability (d) and normalized ΔF/F (e) of VTAGad67+ neurons from the experiment in (c) (n = 13 cells, p=0.13 (10 vs 20 Hz), p=2.5e-8 (10 vs 50 Hz), p=1.0e-4 (20 vs 50 Hz), p=0 (10 vs 100, 20 vs 100 and 50 vs 100 Hz), one-way ANOVA followed by post hoc Tukey test). Data are represented as mean ± SEM. (f) Traces showing four different types of vigilance state transitions (Wake to NREM, NREM to REM, REM to Wake, and NREM to wake) with corresonding EEG, EEG power spectra, EMG and calcium fluorescence (ΔF/F) recorded by fiber photometry in a Gad67-Cre mice expressing GCaMP6f. Note that the highest fluorescence (ΔF/F) was observed during the NREM sleep and the lowest during REM sleep.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (a) Location of tip of optical fibers in all mice injected with either ACR2-2a-mCherry (n = 6 mice, blue circles) or mCherry alone (n = 5 mice, red circles). (b) Same as in a, but for GCaMP6f-expressing mice (n = 6 mice, green circles).

### VTAGad67+ neurons directly inhibited wake-promoting orexin neurons in the lateral hypothalamus

Dense projections were observed from VTAGad67+ neurons to a well-known sleep-wake regulatory brain region, the lateral hypothalamus (LH), where wake-active and wake-promoting orexin (LHorexin) neurons are exclusively located. Thus, we wondered whether VTAGad67+ neurons mediate their sleep-promoting effect through the inhibition of LHorexin neurons. To test this, we generated a bigenic orexin-Flippase (Flp); Gad67-Cre mouse, in which orexin neurons exclusively express Flp recombinase and Gad67+ neurons express Cre recombinase (Figure 6a–c) (Chowdhury et al., 2019). We injected a Cre-inducible AAV expressing the blue light-gated cation channel channelrhodopsin2 (E123T/T159C; ChR2) (Berndt et al., 2011) in the VTA as well as a Flp-inducible AAV expressing tdTomato in the LH of orexin-Flp; Gad67-Cre mice (Figure 6a–c). In slice recordings from VTAGad67+ neurons expressing ChR2, blue light flashes (6.8 mW/mm2) through an objective lens could depolarize and significantly increase spontaneous firing frequency to approximately 650% compared with before light illumination (Figure 6d–f, n = 5 cells, p=0.004 vs either pre or post, one-way ANOVA followed by post-hoc Tukey). Next, we recorded spontaneous firings from tdTomato-positive neurons (orexin neurons) in the LH by loose cell-attached recordings, and the nerve terminals of VTAGad67+ neurons in the LH were activated by illuminating blue light pulses (Figure 6g and Figure 6—figure supplement 1a). We found that blue light inhibited LHorexin neuron firing in a light-pulse frequency-dependent manner (5, 10 and 20 Hz). However, no such effect was observed when yellow light pulses (20 Hz) were applied (Berndt et al., 2011) (Figure 6h and Figure 6—figure supplement 1b–c).

![Figure 6.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig6-v1.jpg)

**Figure 6.:** (a) AAV-mediated gene expression in orexin-Flp; Gad67-Cre bigenic mice. (b and c) Immunohistochemical studies confirmed expression of tdTomato exclusively in orexin neurons and ChR2 in non-TH-positive neurons in the VTA. (d–f) Schematic and current clamp recordings from ChR2-expressing Gad67+ neurons in the VTA in acute brain slices. Blue light stimulation of 6.8 mW/mm2 increased the firing up to 674 ± 174% (n = 5 cells, p=0.004 vs both pre and post, one-way ANOVA followed by Tukey post hoc tests). (g) Schematic of the experiments in (h). (h) Firing of LHorexin neurons in vitro and effect of activation of VTAGad67+ neuronal terminals using different frequencies of blue lights (5, 10, or 20 Hz). Yellow light of 20 Hz was used as a negative control. Raster plot of each trial (upper panel) and running average of firing frequencies (lower panel) of LHorexin neurons are indicated in each rectangular box following illumination of the brain slice through the objective lens. Two vertical red lines indicate illumination start (left) and stop (right) timing.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (a) Schematic of experiment. (b) Loose cell-attached recording traces from LHorexin neurons while optogenetically activating VTAGad67+ nerve terminals using light pulse of different wavelength and frequency. (c) Summary of experiments in (b). Blue light 5 Hz (n = 7 cells), 10 Hz (n = 8 cells), 20 Hz (n = 9 cells), and yellow light 20 Hz (n = 6 cells). p=0.01 (Blue 5 vs 10 Hz), p=3.6e-6 (Blue 5 vs 20 Hz), p=0.02 (Blue 10 vs 10 Hz), p=0.9 (Blue five vs Yellow 20 Hz), p=0.004 (Blue 10 vs Yellow 20 Hz), and p=1.7e-6 (Blue 20 vs Yellow 20 Hz) one-way ANOVA followed by post hoc Tukey test). Data are represented as mean ± SEM.

To reveal the mechanism of inhibition of orexin neurons, we performed additional electrophysiological experiments. We performed whole-cell voltage clamp recordings from orexin neurons at −60 mV holding potential (mVhold) to record post-synaptic currents. Activation of nerve terminals of VTAGad67+ neurons in the LH (blue light pulse, duration of 5 ms) induced a post-synaptic current (PSC) in 8 out of 11 cells. These light-induced PSCs were blocked by gabazine (10 μM), a GABAA receptor antagonist (Figure 7a–c, aCSF: −253 ± 70 pA, gabazine: −9 ± 3 pA, n = 8 cells, p=1.6e-10, paired t-test). This result suggests that GABA is involved in generating the light-induced PSCs in LHorexin neurons. The average synaptic delay from light onset was recorded as 6.2 ± 1.0 ms (Figure 7d). To rule out the effect of glutamate, we blocked both AMPA (α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid) and NMDA (N-Methyl-D-aspartic acid) type glutamate receptors by applying CNQX (20 μM) and AP5 (50 μM), respectively, in the extracellular bath solution. CNQX and AP5 could not block light-induced PSCs, while the combination of CNQX, AP5, and gabazine could inhibit (Figure 7e–g. AP5 +CNQX: −188 ± 38 pA, with gabazine: −6 ± 2 pA, n = 7 cells, p=3.1e-9, paired t-test). Again, a delay of 6.7 ± 0.3 ms was found (Figure 7h). Finally, to confirm whether light-induced PSCs were indeed driven by monosynaptic release of GABA from VTAGad67+ neurons, we performed an additional set of experiments (Figure 7i–l). We found that tetrodotoxin (TTX, 1 μM), a blocker of voltage-gated sodium channels, inhibited the light-induced PSCs (Figure 7i–k. aCSF: −340 ± 73 pA, TTX: −2 ± 0.6 pA, n = 6 cells). However, combined application of TTX along with 4-aminopyridine (4-AP, 1 mM), a voltage-gated potassium channel blocker that prolongs depolarization of axon terminals and enables ChR2-mediated release of neurotransmitter in the absence of action potentials (Petreanu et al., 2009), could rescue the light-induced PSCs, suggesting a monosynaptic connection between VTAGad67+ neurons and LHorexin neurons (−291 ± 131 pA). Again, the rescued current was blocked by adding gabazine (−6 ± 2 pA), but not by CNQX (−295 ± 121 pA). Finally, to further confirm that Cl- channels are involved in this GABAergic input, we changed mVhold to +90 mV. The calculated reversal potential of Cl- under recording conditions were near 0 mV (2.2 mV). As expected, we found that the current direction of light-induced PSCs was opposite at +90 mVhold (Figure 7j–k, 237 ± 115 pA). All these experiments confirm that LHorexin neurons were directly innervated and inhibited by VTAGad67+ neurons.

![Figure 7.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig7-v1.jpg)

**Figure 7.:** (a) Schematic of experiments in b-d. (b) Blue light pulses (5 ms) induced post-synaptic currents in the LHorexin neurons. The thicker line indicates average traces, and the thinner line indicates responses in individual cells (n = 8 cells). (c) Summary of the experiments in b showing the amplitude of current normalized to the aCSF application. (d) Delay in response from light onset. (e) Schematic of the experiments in f-h. (f–h) Similar data representation as in (b–e) in the presence of glutamatergic and GABAergic antagonists. (i) Schematic of the experiments j-l. (j) The effect of glutamatergic and GABAergic antagonists and channel blockers on blue light pulse-induced currents (n = 7 cells). (k) Summary of the experiments in (j) showing the amplitude of current normalized to aCSF (n = 6 cells). Data are represented as mean ± SEM. ***, p<0.001. p values were calculated by two-tailed paired Student’s t-test.

### VTAGad67+ neurons mediate a sleep-promoting function via the lateral hypothalamus

Finally, to test whether the VTAGad67+ to LH projection participates in the induction of NREM sleep, we performed in vivo optogenetic activation of VTAGad67+ nerve terminals in the LH. We expressed either ChR2-EYFP (n = 7 mice) or hrGFP (n = 5 mice) in the VTAGad67+ neurons in a Cre-dependent manner using Gad67-Cre mice. Two weeks later, we bilaterally implanted fiber optics at a diameter of 400 µm above the LH (Figure 8a and b). After recovery and habituation, blue light (20 Hz, 10 mW) was applied for 60 min in the dark period when mice were awake and active (Figure 8c). Interestingly, blue light illumination into the LH resulted in decreased wakefulness and increased NREM sleep in the ChR2-expressing mice, whereas hrGFP-expressing mice showed no such effects (Figure 8c–e, in ChR2-expressing mice: wakefulness (in min) Pre: 55.0 ± 2.2, Stimulation: 29.2 ± 1.7, Post: 53.3 ± 2.1; p=7.3e-8 vs Pre, p=2.7e-7 vs Post, NREM (in min) Pre: 4.3 ± 1.8, Stimulation: 29.9 ± 1.8, Post: 6.0 ± 1.9, p=0 vs Pre, p=5.5e-8 vs Post, one-way ANOVA followed by post-hoc Tukey). Again, the REM sleep remained unaffected (Figure 8c–e, in ChR2-expressing mice: REM (in min) Pre: 0.7 ± 0.5, Stimulation: 0.9 ± 0.3, Post: 0.7 ± 0.4, p=0.94 vs Pre, p=0.95 vs Post, one-way ANOVA followed by post-hoc Tukey). These results suggest that VTAGad67+ neurons promote NREM sleep, at least in part, through their projection to the LH.

![Figure 8.](https://cdn.elifesciences.org/articles/44928/elife-44928-fig8-v1.jpg)

**Figure 8.:** (a) Schematic of the projection specific optogenetic activation. (b) Schematic and immunohistochemistry of fiber implantation in the LH. Top right panel shows merged fluorescence image depicted in the coronal brain map. Lower panels indicate enlarged images of the boxed area shows VTAGad67+ terminals near orexin neurons in the LH. (c) Representative traces showing EEG, EEG spectra, and EMG while mice experienced 20 Hz blue light stimulation (left: start of light illumination, right: stop of light illumination). Vigilance states determined by EEG and EMG signals are indicated by colored bars. (d and e) Probability of vigilance state (d) and total time spent (e) of either ChR2- or hrGFP-expressing mice. Blue and green lines indicate mean probability of each vigilance state in ChR2 (n = 7 mice) and hrGFP (n = 5 mice) group, respectively. Data are represented as mean ± SEM. ***, p<0.001 (vs Pre); +++, p<0.001 (vs Post). p values were calculated by one-way ANOVA followed by post-hoc Tukey test.

## Discussion

By employing anterograde tracing and localization of brain-wide neural projections, bidirectional neuronal manipulations, fiber photometry, slice electrophysiology, as well as sleep recordings, we provide multiple lines of evidence in favor of our claim that VTAGad67+ neurons regulate NREM sleep in mice. GABAergic neurons constitute a significant part of the VTA (Nair-Roberts et al., 2008; Pignatelli and Bonci, 2015) and help to regulate the function of DA neurons residing nearby (Tan et al., 2012; van Zessen et al., 2012). Dysregulation of signaling pathways in the VTA is associated with drug abuse and several other psychiatric disorders including schizophrenia, bipolar disorder, and major depressive disorder (Winton-Brown et al., 2014; Wulff et al., 2010). Moreover, irregular sleep-wake timing and architectures are recognized as common co-morbidities in many neuropsychiatric and neurodegenerative diseases (Wulff et al., 2010). Therefore, the relationship between neurochemical signaling in the VTA and the regulation of sleep/wakefulness poses an interesting point of study. However, classical lesioning experiments suggest that cats with reduced dopamine levels exhibit decreased behavioral arousal but no significant change in electro-cortical waking (Jones et al., 1973). It is only very recently that investigators have shown an interest in understanding the role of the VTA in the regulation of sleep/wakefulness (Eban-Rothschild et al., 2016; Oishi et al., 2017a; Yang et al., 2018). However, not much scientific literature has been published focusing on the functional importance of GABAergic neurons in the VTA. Therefore, our findings on the role of these neurons in sleep/wakefulness regulation will provide a conceptual and systematic framework for the association between sleep and psychiatric disorders and will generate opportunities to study VTA-related dysregulation in mental disorders.

van Zassen and colleagues reported that in vivo optogenetic activation of GABAergic neurons in the VTA in mice disrupts reward consummatory behavior (van Zessen et al., 2012). In addition, Shank et al. reported that dose- and time-related selective ablation of GABAergic neurons in the VTA in rats increased spontaneous locomotor activity (Shank et al., 2007). These studies are consistent with the hypothesis that GABAergic neurons in the VTA play an important role in the regulation of behavior. We now argue that one reason for such disruption in behavior might be promotion of NREM sleep by selective activation of GABAergic neurons in the VTA.

Using bidirectional chemogenetic manipulations as well as neurotoxic lesions in rats, a recent study found that neurons in the rostromedial tegmental nucleus (RMTg), also known as the GABAergic tail of the VTA, are essential for physiological NREM sleep (Yang et al., 2018). Although Yang et al. did not identify neuronal subtypes involved in the RMTg, their results might be related to our findings. Interestingly, VTAGad67+ neurons in our study are located throughout the VTA, but at a somewhat higher density toward the caudal parts of the VTA. More recently, Takata et al. reported that GABA neurons in the ventral medial midbrain/pons, which includes the VTA region, regulate sleep/wake cycles by modulating DA neurons (Takata et al., 2018). These GABA neurons should include VTAGad67+ neurons. Indeed, GABAergic neurons regulating NREM sleep might be distributed across both VTA and RMTg.

Chemogenetic activation of VTAGad67+ neurons induced NREM sleep accompanied by higher delta power (slow wave) compared with control conditions (Figure 2g), suggesting that VTAGad67+ neurons might play a critical role in the generation of slow wave in NREM sleep. Recently, Oishi et al. reported that activation of either the cell bodies of GABAergic neurons in the core of NAc or their axonal terminals in the VP evoked slow wave sleep (Oishi et al., 2017b). In addition, activation of GABAergic neurons in the basal forebrain, which includes the VP, produced wakefulness, whereas their inhibition induced sleep (Anaclet et al., 2015). These facts suggest that inhibition of GABAergic neurons in the VP is a critical pathway to generate slow waves in NREM sleep. We also found that VTAGad67+ neurons moderately project to the VP. Therefore, we reasoned that VTAGad67+ neurons projecting to the VP might be involved in the generation of slow wave sleep.

Population activity recordings across vigilance states shows that DA neurons in the VTA exhibit higher activity in REM sleep versus either wake or NREM sleep (Eban-Rothschild et al., 2016). On the contrary, VTAGad67+ neurons exhibit a completely opposite activity pattern from that of DA neurons across vigilance states, with highest activity during NREM sleep (Figure 5). This suggests an existing functional interaction between DA and Gad67+ neurons in the VTA. Using in vivo single unit recordings in rats, Lee et al. found wake- and REM-active VTAGABA neurons, suggesting that there might be several types of VTAGABA neurons (Lee et al., 2001). Our fiber photometry data showed that VTAGad67+ neurons exhibit weak activity even during wakefulness. This might suggest that VTAGad67+ neurons are also comprised of several subtypes. However, most VTAGad67+ neurons are predominantly active in NREM sleep. Therefore, additional research is needed to clarify any electrophysiological, anatomical, and/or functional variations of GABAergic neurons in the VTA. Very recently, Yu et al. reported that coordinated interaction between GABA and glutamate neurons in the VTA regulates sleep/wakefulness in mice (Yu et al., 2019). Although this study similarly found a NREM-sleep promoting role of VTAGABA neurons, the in vivo activity of VTAGABA neurons was quite different from our observations with the highest activity observed during wake and REM sleep. One difference between studies was that Yu et al. used Vgat-Cre mice (Cre recombinase is targeted to the slc32a1 gene) and we used Gad67-Cre mice to target GABAergic neurons. Our in situ hybridization results showed that Gad67-positive neurons represent a small subset of Vgat-positive neurons in the VTA. Again, this difference further indicates the existence of different populations of GABAergic neurons in the VTA.

Optogenetic inhibition of VTAGad67+ neurons induced immediate wakefulness from NREM sleep, but not from REM sleep, suggesting the importance of uninterrupted neuronal activity of VTAGad67+ neurons for the maintenance of NREM sleep. Both chemogenetic activation and optogenetic inhibition data suggest that VTAGad67+ neurons might not play a decisive role in the physiological regulation of REM sleep. Interestingly, inhibition of VTAGad67+ neurons prolonged wakefulness (Figure 3f). This result might suggest that VTAGad67+ neurons also regulate levels of wakefulness. This is consistent with data showing that VTAGad67+ neurons displayed weak activity in wakefulness in terms of population activity. This idea is also supported by observed increases in spontaneous locomotor activity following selective ablation of VTAGABA neurons in rats (Shank et al., 2007). These facts might suggest that an improvement in alertness and ability to maintain wakefulness require the suppression of activity of VTAGABA neurons.

One possible cellular mechanism underlying NREM sleep promotion by VTAGABA neurons is via inhibition of DA neurons residing in the VTA. In addition to this, our results showed that direct inhibition of wake-promoting LHorexin neurons might contribute to the induction of NREM sleep. Projection-specific activation of VTAGABA neuron nerve terminals using optogenetics indicated that VTAGABA-to-LH represents a pathway responsible for inducing NREM sleep. It will also be fascinating to study how VTAGABA neurons are regulated. Using an optimized trans-synaptic retrograde tracing approach, Faget and colleagues recently labeled afferent neurons to DA, GABA, or glutamate neurons in the VTA and found that these populations receive qualitatively similar inputs, with dominant and comparable projections from three brain areas known to be critical for sleep/wakefulness regulation: LH, raphe, and ventral pallidum (Faget et al., 2016). Here we report that VTAGad67+ neurons project to those areas, suggesting the existence of a mutual interaction with these brain areas to regulate sleep/wakefulness. Moreover, while many brain areas including the cholinergic basal forebrain and brain stem, histaminergic posterior hypothalamus, serotonergic raphe nucleus, as well as the noradrenergic locus coeruleus are important in sleep/wake regulation (Brown et al., 2012), we speculate a critical role for VTAGad67+ neurons in sleep/wakefulness-regulating circuitry as these neurons modulate diverse targets, including DA neurons in the VTA (Tan et al., 2012).

In conclusion, our study elucidated that VTAGABA neurons regulate NREM sleep in mice. These neurons might be a possible target for therapeutic intervention in treating sleep-related as well as neuropsychiatric disorders.

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
      <td>Strain, strain background</td>
      <td>AAV(9)-CMV-FLEX-hrGFP</td>
      <td>This paper</td>
      <td>NA</td>
      <td>Titer: 6.0 × 1012 copies/ml</td>
    </tr>
    <tr>
      <td>Strain, strain background</td>
      <td>AAV(9)-CAG-FLEX-hM3Dq-mCherry</td>
      <td>This paper</td>
      <td>NA</td>
      <td>Titer: 1.1 × 1012 copies/ml</td>
    </tr>
    <tr>
      <td>Strain, strain background</td>
      <td>AAV(9)-CMV-FLEX-ACR2-2A-mCherry</td>
      <td>Mohammad et al., 2017</td>
      <td>Genbank accession# KP171709</td>
      <td>Titer: 6.2 × 1012 copies/ml</td>
    </tr>
    <tr>
      <td>Strain, strain background</td>
      <td>AAV(9)-CAG-FLEX-mCherry</td>
      <td>This paper</td>
      <td>NA</td>
      <td>Titer: 1.9 × 1012 copies/ml</td>
    </tr>
    <tr>
      <td>Strain, strain background</td>
      <td>AAV(9)-CMV-FLEX-ChR2 (ET/TC)-eYFP</td>
      <td>Berndt et al., 2011</td>
      <td>NA</td>
      <td>Titer: 3.0 × 1013 copies/ml</td>
    </tr>
    <tr>
      <td>Strain, strain background</td>
      <td>AAV(9)-CMV-FLEX-GCaMP6f</td>
      <td>Chen et al., 2013</td>
      <td>NA</td>
      <td>Titer: 1.3 × 1012 copies/ml</td>
    </tr>
    <tr>
      <td>Strain, strain background</td>
      <td>AAV(DJ)-CMV-dFrt-tdTomato-WPRE</td>
      <td>This paper</td>
      <td>NA</td>
      <td>Titer: 8.1 × 1012 copies/ml</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Glutamic acid decarboxylase 67-Cre</td>
      <td>Higo et al., 2009</td>
      <td>Gad67-Cre</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Orexin-Flippase</td>
      <td>Chowdhury et al., 2019</td>
      <td>Orexin-Flp</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Orexin-Flippase; Glutamic acid decarboxylase 67-Cre</td>
      <td>Chowdhury et al., 2019</td>
      <td>Orexin-Flp; Gad67-Cre</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-TH</td>
      <td>Millipore</td>
      <td>AB-152</td>
      <td>(1/1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-GFP</td>
      <td>Fujifilm Wako Pure Chemical Corporation</td>
      <td>mFX75</td>
      <td>(1/1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-orexin</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-8070</td>
      <td>(1/1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Gad67</td>
      <td>Millipore</td>
      <td>MAB5406</td>
      <td>(1/500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-DAT</td>
      <td>Frontier Institute Co. Ltd.</td>
      <td>DAT-Rb-Af1800</td>
      <td>(1/1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-DsRED</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-390909</td>
      <td>(1/1000)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNAscope Fluorescent Multiplex Reagent ver.2</td>
      <td>ACD Bio</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>clozapine-N-oxide (CNO)</td>
      <td>Enzo Life Sciences</td>
      <td>BML-NS105-0025</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>4',6-diamidino-2-phenylindole dihydrochloride (DAPI)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# D1306</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Gabazine</td>
      <td>Abcam</td>
      <td>Cat# Ab-120042</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>tetrodotoxin (TTX)</td>
      <td>Alomone Labs</td>
      <td>Cat# T-550</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>D-2-Amino-5-phosphopentanoic acid (AP5)</td>
      <td>Alomone Labs</td>
      <td>Cat# D-145</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>6-cyano-7-nitroquinoxaline-2,3-dione (CNQX)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# C127</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>4-Aminopyridine (4-AP)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# 8.01111</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Origin 2017</td>
      <td>Lightstone</td>
      <td>Origin 2018</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SleepSign</td>
      <td>Kissei Comtec</td>
      <td>Version 3</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pClamp 10.5Software and Algorithms</td>
      <td>Molecular Devices</td>
      <td>RRID:SCR_011323</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>https://imagej.nih.gov/ij/</td>
      <td>RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>In situ hybridyzation probe</td>
      <td>Gad67 Channel 1</td>
      <td>ACD Bio</td>
      <td>Cat# 400951</td>
      <td></td>
    </tr>
    <tr>
      <td>In situ hybridyzation probe</td>
      <td>Vgat Channel 4</td>
      <td>ACD Bio</td>
      <td>Cat# 319191</td>
      <td></td>
    </tr>
    <tr>
      <td>In situ hybridyzation probe</td>
      <td>mCherry Channel 3</td>
      <td>ACD Bio</td>
      <td>Cat# 431201</td>
      <td></td>
    </tr>
    <tr>
      <td>TSA enhancement (ISH)</td>
      <td>Opal520</td>
      <td>PerkinElmer</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TSA enhancement (ISH)</td>
      <td>Opal620</td>
      <td>PerkinElmer</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TSA enhancement (ISH)</td>
      <td>Opal690</td>
      <td>PerkinElmer</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Animals

All experimental protocols that involved animals were approved by the Institutional Animal Care and Use Committees, Research Institute of Environmental Medicine, Nagoya University, Japan (Approval number #18232, #18239). All efforts were made to reduce the number of animals used and also to minimize the suffering and pain of animals. Animals were maintained on a 12 hr light-dark cycle (lights were turned on at 8:00 am), with free access to food and water.

### Generation and microinjection of adeno-associated virus (AAV) vectors

AAV vectors were produced using the AAV Helper-Free System (Agilent Technologies, Inc, Santa Clara, CA). The virus purification method was adopted from a previously published protocol (Inutsuka et al., 2016). Briefly, HEK293 cells were transfected together with three distinct plasmids carrying a pAAV vector, pHelper and pAAV-RC (serotype 9 or DJ; purchased from Cell Biolabs Inc, San Diego, CA) using a standard calcium phosphate method. HEK293 cells were collected and suspended in artificial CSF (aCSF) solution (in mM: 124 NaCl, 3 KCl, 26 NaHCO3, 2 CaCl2, 1 MgSO4, 1.25 KH2PO4 and 10 glucose) three days post-transfection. Following multiple freeze-thaw cycles, the cell lysates were treated with benzonase nuclease (Merck, Darmstadt, Germany) at 37°C for 30 min, and were centrifuged 2 times at 16,000 g for 10 min at 4°C. The supernatant was used as the virus-containing solution. Quantitative PCR was performed to measure the titer of purified virus. Virus aliquots were then stored at −80°C until use.

Adult Gad67-Cre or orexin-Flp; Gad67-Cre mice of both sexes were subjected to either unilateral or bilateral injection of AAV(9)-CMV-FLEX-hrGFP (100 × 1 nl, 6.0 × 1012 copies/ml), AAV(9)-CAG-FLEX-hM3Dq-mCherry (200 × 2 nl, 1.1 × 1012 copies/ml), AAV(9)-CMV-FLEX-ACR2-2A-mCherry (300 × 2 nl, 6.2 × 1012 copies/ml), AAV(9)-CAG-FLEX-mCherry (300 × 2 nl, 1.9 × 1012 copies/ml), AAV(9)-CMV-FLEX-ChR2 (ET/TC)-eYFP (300 nl, 3.0 × 1013 copies/ml), or AAV(9)-CMV-FLEX-GCaMP6f (300 × 1 nl, 1.3 × 1012 copies/ml) into the VTA (3.0 to 3.7 mm posterior and 0.4 to 0.6 mm lateral from bregma, 4.0 to 4.2 mm deep from brain surface) under ~1.2% isoflurane (Fujifilm Wako Pure Chemical Industries, Osaka, Japan) anesthesia. Orexin-Flp; Gad67-Cre bigenic mice also received bilateral injection of AAV(DJ)-CMV-dFrt-tdTomato-WPRE (300 × 2 nl, 8.1 × 1012 copies/ml) into the lateral hypothalamus (1.5 mm posterior and 0.5 mm lateral from bregma, 5.0 mm deep from brain surface), which were used for slice electrophysiological experiments.

### Immunohistochemistry

Under deep anesthesia with 0.65% pentobarbital sodium solution (Kyoritsu Seiyaku Corporation, Tokyo, Japan) diluted with saline (1.0 ml/kg body weight), mice were subjected to serial transcardial perfusion first using ice-cold saline (20 ml) and then ice-cold 4% formaldehyde solution (20 ml, Fujifilm Wako Pure Chemical Industries, Ltd., Osaka, Japan). The brain was then gently collected and post-fixed with 4% formaldehyde solution at 4°C overnight. Later, the brain was subsequently immersed in phosphate-buffered saline (PBS) containing 30% sucrose at 4°C for at least 2 days. Coronal sections of either 40 or 80 μm thickness were made using a cryostat (Leica CM3050 S; Leica Microsystems, Wetzlar, Germany; or Leica VT1000 S, Wetzlar, Germany), and slices were preserved in PBS containing 0.02% of NaN3 at 4°C until stained. For staining, coronal brain sections were immersed in blocking buffer (1% BSA and 0.25% Triton-X in PBS), and then incubated with primary antibodies (TH: Millipore, Massachusetts, 1/1000 dilution; DAT: Frontier Institute Co. Ltd., Hokkaido, Japan, 1/1000 dilution, Japan; DsRED: Santa Cruz Biotechnology, Heidelberg, Germany, 1/1000 dilution; GFP: Fujifilm Wako Pure Chemical Corporation, Osaka, Japan, 1/1000 dilution; orexin-A: Santa Cruz Biotechnology, 1/1000 dilution) at 4°C overnight. For Gad67 staining, slices were incubated with anti-Gad67 antibody (Millipore, 1/500 dilution in blocking buffer without Triton-X) at 4°C for 4 days. After washing by blocking buffer three times, the brain sections were then incubated with secondary antibodies for 1 hr at room temperature. After washing with the same blocking solution three times, slices were stained by DAPI (Thermo Fisher Scientific, Waltham, MA) across several experiments. Slices were mounted in 50% glycerol solution and examined with an epifluorescence microscope (BZ-9000, Keyence, Osaka, Japan or IX71, Olympus, Tokyo, Japan).

### Anterograde tracing and localization of brain-wide neural projections

A Cre-inducible AAV carrying the hrGFP gene (AAV(9)-CMV-FLEX-hrGFP; 100 × 1 nl, 6.0 × 1012 copies/ml) was unilaterally injected into the VTA of Gad67-Cre mice. Three weeks post-injection, animals were perfused-fixed and brain slices of 80 μm thickness were made serially from the anterior to the posterior part of the brain using a vibratome (Leica VT1000 S, Wetzlar, Germany). After DAPI staining, slices were serially mounted and images were taken using an epifluorescence microscope (BZ-9000, Keyence, Osaka, Japan or IX71, Olympus, Tokyo, Japan). Images were taken using an identical configuration in the microscope and were then analyzed using ImageJ (US National Institute of Health) software. Projection scorings were made in all visible projection sites, except for the VTA, by first selecting the most innervated brain region and comparing other areas to that region.

### In situ RNA hybridization using RNAscope

Under deep anesthesia with 0.65% pentobarbital sodium solution (Kyoritsu Seiyaku Corporation, Tokyo, Japan) diluted with saline (1.0 ml/kg body weight), mice were transcardially perfused using ice-cold saline (20 ml) and then using ice-cold 4% formaldehyde solution (20 ml, Fujifilm Wako Pure Chemical Industries, Ltd., Osaka, Japan). The brain was then gently removed, post-fixed with 4% paraformaldehyde solution overnight at 4°C and was subsequently immersed in phosphate-buffer containing 30% sucrose at 4°C for at least 2 days. Coronal brain sections of 25 μm thickness were made using a cryostat (Leica CM3050 S; Leica Microsystems) and were mounted on glass slides (SMAS-01, Matsunami, Japan), and fixed in 4% paraformaldehyde for 60 min. The slides were then treated by RNAscope multiplex fluorescent v2 (#323100, Advanced Cell Diagnostics, Hayward, CA) according to the RNAscope standard protocol. In short, slides were incubated with hydrogen peroxide at RT for 10 min, followed by boiling with target retrieval reagent at 98 ~ 102°C for 5 min, and protease digestion at 40°C in a HybEZ hybridization oven (Advanced Cell Diagnostics) for 30 min. Subsequently, slides were incubated at 40°C with target probes in hybridization buffer for 2 hr, AMP1 in hybridization buffer for 30 min, AMP2 in hybridization buffer for 30 min, and AMP3 in hybridization buffer for 15 min. After each hybridization step, slides were washed with wash buffer twice at room temperature. For multiplex detection, equimolar amounts of target probes, AMP1, AMP2 and AMP3 of each amplification system were used. Sequences of target probes, AMP1, AMP2, and AMP3 are proprietary (vGAT, GAD1 and mCherry, Advanced Cell Diagnostics, Hayward, CA). For fluorescent detection, the RNA probes were conjugated to Opal 520, 620, or 690 with the HRP and TSA Plus fluorophores system (Perkin Elmer, Waltham, MA). Slices were mounted with ProLong Gold Antifade Mountant (Thermo Fisher Scientific, Waltham, MA) and observed via a confocal microscope (LSM 710 Zeiss, Oberkochen, Germany).

### Surgery for EEG-EMG and/or optogenetics, fiber photometry

Procedures for implanting EEG and EMG electrodes for polysomnographic recording experiments were adapted from the previously published protocol (Tabuchi et al., 2014). Briefly, virus-injected mice were implanted with EEG and EMG electrodes under isoflurane anesthesia. Immediately after surgery, each mouse received an i.p. injection of 10 ml/kg of an analgesic solution containing 0.5 mg/ml of Carprofen (Zoetis Inc, Parsippany-Troy Hills, NJ). Mice were singly housed for 7 days during the recovery period. Mice were then connected to a cable in order to allow them to move freely in the cage as well as to be habituated to the recording cable for another 7 days.

For fiber-guided optogenetic experiments, virus-injected mice received a surgical implantation of single fiber optic cannula (400 µm; Lucir Inc, Japan), along with EEG-EMG electrodes, above the VTA (AP −3.3 to −3.6 mm; ML 0.4 to 0.6 mm; DV −3.75 mm. For fiber photometry experiments, virus-injected mice received surgical implantation of a single guide cannula (400 µm; Thorlabs Inc) just above the VTA (AP −3.3 mm; ML 0.4 to 0.5 mm; DV −4.0 mm) to target VTAGad67+ neurons. These mice were also implanted with the EEG-EMG electrodes following the protocol described above.

For projection-specific optogenetic activation of VTAGad67+ nerve terminals in the LH, virus-injected mice received bilateral implantation of fiber optic cannula (400 µm; Kyocera Corporation, Japan), along with EEG-EMG electrodes, above the LH at a stereotaxic co-ordinate of AP −1.4 mm; ML ± 0.9 mm; DV −5.0 mm.

### Vigilance state determination

EEG and EMG signals were amplified (AB-610J, Nihon Koden, Japan), filtered (EEG at 1.5–30 Hz, and EMG at 15–300 Hz), digitized (at a sampling rate of 128 Hz), and recorded (Vital Recorder, Kissei Comtec Co., Ltd, Japan) from individual habituated mice. Recorded signals were then analyzed to identify vigilance states using SleepSign (Kissei Comtec) software. Vigilance state identification was assisted by an infrared sensor as well as by video monitoring through a CCD video camera (Amaki Electric Co., Ltd., Japan) during both the light and dark periods (Kissei Comtec). Video recording during the dark period was aided by infrared photography (Amaki Electric Co., Ltd., Japan). EEG and EMG data were automatically scored in epochs (every 4 s) and classified as wake, REM sleep, or NREM sleep. All auto-screened data were examined visually and corrected. The EEG analysis yielded power spectra profiles over a 0 ~ 20 Hz window with 1 Hz resolution for delta (1–5 Hz), theta (6–10 Hz), alpha (11–15 Hz), and beta (16–20 Hz) bandwidths. The criteria for determining vigilance states were the same as the protocol described elsewhere (Tabuchi et al., 2014): briefly, (i) wake (low EEG amplitude with high EMG or locomotion score), (ii) NREM sleep (low EMG and high EEG delta amplitude), and (iii) REM sleep (low EMG as well as low EEG amplitude with high theta activity, and should be followed by NREM).

### In vivo recordings and data analysis of neuronal activity using fiber photometry

In vivo population activity of the VTAGad67+ neurons was recorded using a silica fiber of 400 μm by implanting the fiber just above the VTA. Details of the fiber photometric recordings are described elsewhere (Inutsuka et al., 2016). Briefly, the fiber photometry system (COME2-FTR/OPT, Lucir, Tsukuba, Japan) utilizes a custom-made single silica fiber of 400 μm diameter to deliver excitation light and to detect fluorescence from GCaMP6f, simultaneously. Blue excitation light (465 nm, 0.5 mW at the tip of the silica fiber) was produced by a high-power LED system (PlexonBright OPT/LED Blue_TT_FC, Plexon, Dallas, TX). The LED-emitted excitation light was reflected by a dichroic mirror and coupled to the silica fiber (400 μm diameter) through an excitation bandpass filter (path 472 ± 35 nm). GCaMP6f-emitted green fluorescence was collected by the same silica fiber passed through a bandpass emission filter (path 525 ± 25 nm) and guided to a photomultiplier (PMTH-S1M1-CR131, Zolix instruments, Beijing, China). The fiber photometry signal was recorded by Vital Recorder (Kissei Comtec Co., Ltd, Japan) along with the EEG/EMG signals. Fiber photometry signals were collected at a sampling frequency of 128 Hz and the software averaged every 10 samples to minimize fluctuations and noise.

After recording and sleep analysis, the fiber photometry signal was outputted along with the EEG and EMG signals as a text file of raw data. For each experiment, the photometry signals at all data points were motion averaged and were then converted to ΔF/F by ΔF/F(t) = (F(t)- Fmin)/Fmin. We recorded the signals in the light period as nocturnal animal mice usually show multiple transitions among different vigilance states during the light period. All mice were subjected to at least two recording sessions with at least a 2 day interval in between each session to allow photobleaching recovery. We separated all sleep-state transitions that last at least for 1 min before and after the state change. All the sessions were selected after the photometry signal became stable, as we observed a decay of photometry signal at the beginning of the recordings.

### Sleep deprivation

Mice expressing ACR2-2A-mCherry in VTAGad67+ neurons were used for optogenetic inhibition in Figure 3 and were subjected to sleep deprivation. Mice were submitted to complete sleep deprivation, through the gentle handling method, which consists of keeping the animal awake by gently touching them with a soft brush if behavioral signs of sleep were observed. Mice were sleep-deprived for 4 hr, starting at light onset. Mice were then allowed to experience recovery sleep for 30 min. Optogenetic inhibition was performed during the recovery sleep.

### Acute brain slice preparation

Preparation of acute brain slices and subsequent electrophysiological recordings were performed as previously reported with a slight modification (Chowdhury and Yamanaka, 2016). Briefly, mice were decapitated under isoflurane (Fujifilm Wako Pure Chemical Industries) anesthesia and the brain was quickly isolated and chilled in an ice-cold cutting solution (in mM: 110 K-gluconate, 15 KCl, 0.05 EGTA, 5 HEPES, 26.2 NaHCO3, 25 glucose, 3.3 MgCl2 and 0.0015 (±)−3-(2-carboxypiperazin-4-yl)propyl-1-phosphonic acid) gassed with 95% O2 and 5% CO2. Coronal slices of 300 µm thickness containing either VTA or LH were prepared using a vibratome (VT-1200S; Leica, Wetzlar, Germany) and were temporarily placed in an incubation chamber containing a bath solution (in mM: 124 NaCl, 3 KCl, 2 MgCl2, 2 CaCl2, 1.23 NaH2PO4, 26 NaHCO3 and 25 glucose) gassed with 95% O2 and 5% CO2 in a 35°C water bath for 30–60 min. Slices were then incubated at room temperature in the same incubation chamber for another 30–60 min for recovery.

### In vitro electrophysiology

After the recovery period, acute brain slices were transferred to a recording chamber (RC-26G; Warner Instruments, Hamden, CT). The recording chamber was equipped with an upright fluorescence microscope (BX51WI; Olympus, Tokyo, Japan) stage and was superfused with a 95% O2 and 5% CO2-gassed bath solution at a rate of 1.5 ml/min using a peristaltic pump (Dynamax; Rainin, Oakland, CA). An infrared camera (C3077-78; Hamamatsu Photonics, Hamamatsu, Japan) was installed in the fluorescence microscope along with an electron multiplying charge-coupled device camera (Evolve 512 delta; Photometrics, Tucson, AZ) and both images were separately displayed on monitors. Micropipettes of 4–6 MΩ resistance were prepared from borosilicate glass capillaries (GC150-10; Harvard Apparatus, Cambridge, MA) using a horizontal puller (P-1000; Sutter Instrument, Novato, CA). Patch pipettes were filled with KCl-based internal solution (in mM: 145 KCl, 1 MgCl2, 10 HEPES, 1.1 EGTA, 2-Mg-ATP, 0.5 Na2-GTP; pH 7.3 with KOH) with osmolality between 280–290 mOsm. Electrophysiological properties of cells were monitored using an Axopatch 200B amplifier (Axon Instrument, Molecular Devices, Sunnyvale, CA). Output signals were low-pass filtered at 5 kHz and digitized at a sampling rate of 10 kHz. Patch clamp data were recorded through an analog-to-digital (AD) converter (Digidata 1550A; Molecular Devices) using pClamp 10.2 software (Molecular Devices). Voltage clamp recordings were performed at a holding potential of −60 mV, unless otherwise stated. Blue light at a wavelength of 475 ± 18 nm and yellow light at a wavelength of 575 ± 13 nm were generated by a light source that used a light-emitting diode (Spectra Light Engine; Lumencor, Beaverton, OR) and guided to the microscope stage with a 1 cm diameter optical fiber. Brain slices were illuminated through the objective lens of the fluorescence microscope.

### In vitro calcium imaging

Gad67+ neurons were identified via green fluorescence of GCaMP6f. Excitation light of 475 ± 18 nm (6.8 mW/mm2) was emitted into the brain slice containing VTA through the objective lens of a fluorescence microscope. The light source (Spectra light engine) was controlled by Metamorph software (Molecular Devices). GCaMP6f fluorescence intensity was recorded continuously using Metamorph software at a rate of 1 Hz with 100 ms of exposure time. To synchronize calcium imaging and patch clamp recording, pClamp software was triggered by the TTL output from Metamorph software. Metamorph data were analyzed by setting the region of interest (ROI) on GCaMP6f-expressing VTAGad67+ neurons and the ΔF/F was calculated from the average intensity of the ROI. Finally, ΔF/F values for 10, 20, and 50 Hz were normalized to the ΔF/F values for corresponding 100 Hz frequencies.

### Data analysis and presentation

Immunostaining data were analyzed and processed with ImageJ (US National Institute of Health) and BZ-X Analyzer (Keyence BZ-X710 microscope). Electrophysiological analysis was performed with either Clampfit10 (Molecular Devices, Sunnyvale, CA) or Minianalysis software (Synaptosoft Inc, Decatur, GA). Analysis of EEG-EMG data was performed using SleepSign software (Kissei Comtec) and data were outputted as text files. Further analyses were performed using Microsoft Excel. Electrophysiological data were saved as American Standard Code for Information Interchange (ASCII) files and further data calculations were performed in Microsoft Excel. Graphs were generated in Origin 2017 (OriginLab, Northampton, MA) using data from Excel. Statistical analysis was also performed with Origin 2017. Graphs were generated using Canvas 15 (ACD Systems, Seattle, WA).
