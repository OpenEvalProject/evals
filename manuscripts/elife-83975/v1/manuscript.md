# Optogenetic manipulation of neuronal and cardiomyocyte functions in zebrafish using microbial rhodopsins and adenylyl cyclases

## Authors

- Hanako Hagio<sup>1</sup> ([ORCID: 0000-0003-2197-4595](https://orcid.org/0000-0003-2197-4595))
- Wataru Koyama<sup>1</sup> ([ORCID: 0009-0005-6851-5961](https://orcid.org/0009-0005-6851-5961))
- Shiori Hosaka<sup>1</sup>
- Aysenur Deniz Song<sup>1</sup> ([ORCID: 0000-0003-0998-9225](https://orcid.org/0000-0003-0998-9225))
- Janchiv Narantsatsral<sup>1</sup>
- Koji Matsuda<sup>1</sup>
- Takashi Shimizu<sup>1</sup> ([ORCID: 0000-0002-8750-6797](https://orcid.org/0000-0002-8750-6797))
- Shoko Hososhima<sup>4</sup>
- Satoshi P Tsunoda<sup>4</sup>
- Hideki Kandori<sup>4</sup> ([ORCID: 0000-0002-4922-1344](https://orcid.org/0000-0002-4922-1344))
- Masahiko Hibi<sup>1</sup> ([ORCID: 0000-0002-9142-4444](https://orcid.org/0000-0002-9142-4444)) †

### Affiliations

1. Graduate School of Science, Nagoya University, Japan Nagoya Japan ([ROR:04chrp450](https://ror.org/04chrp450))
2. Graduate School of Bioagricultural Sciences, Nagoya University Nagoya Japan ([ROR:04chrp450](https://ror.org/04chrp450))
3. Institute for Advanced Research, Nagoya University Nagoya Japan ([ROR:04chrp450](https://ror.org/04chrp450))
4. Department of Life Science and Applied Chemistry, Nagoya Institute of Technology Nagoya Japan ([ROR:055yf1005](https://ror.org/055yf1005))

† Corresponding author

## Abstract

Even though microbial photosensitive proteins have been used for optogenetics, their use should be optimized to precisely control cell and tissue functions in vivo. We exploited GtCCR4 and KnChR, cation channelrhodopsins from algae, BeGC1, a guanylyl cyclase rhodopsin from a fungus, and photoactivated adenylyl cyclases (PACs) from cyanobacteria (OaPAC) or bacteria (bPAC), to control cell functions in zebrafish. Optical activation of GtCCR4 and KnChR in the hindbrain reticulospinal V2a neurons, which are involved in locomotion, induced swimming behavior at relatively short latencies, whereas activation of BeGC1 or PACs achieved it at long latencies. Activation of GtCCR4 and KnChR in cardiomyocytes induced cardiac arrest, whereas activation of bPAC gradually induced bradycardia. KnChR activation led to an increase in intracellular Ca2+ in the heart, suggesting that depolarization caused cardiac arrest. These data suggest that these optogenetic tools can be used to reveal the function and regulation of zebrafish neurons and cardiomyocytes.

## Introduction

Cells can respond to various signals by changing their internal states. For example, in the nervous system, neurons respond to neurotransmitters to increase or decrease ions and/or chemical mediators such as cAMP and cGMP in the cytoplasm. Similarly, cardiomyocyte function is regulated by sympathetic and parasympathetic nerves that involve noradrenergic and cholinergic receptors, respectively, and control chemical mediators such as cAMP. To understand the regulation of cell and tissue functions, it is necessary to manipulate intracellular ions and cAMP/cGMP at a precise timing and locations, and examine their effects on cell and tissue functions in vivo.

Optogenetics is a rapidly expanding technology that controls or detects cellular functions by using photoreactive proteins that are genetically expressed in cells. Microbial rhodopsins have been used for optogenetics (Kandori, 2020; Kandori, 2021). Two main types of microbial rhodopsins are used in optogenetics. The first includes microbial rhodopsins with ion-transporting properties such as light-gated ion channels (channelrhodopsins [ChRs]) and light-driven ion pumps, while the other includes microbial rhodopsins with enzymatic activity, that is, enzymorhodopsins (Figure 2B).

Among the ChRs, channelrhodopsin 1 and 2 (CrChR1 and CrChR2), which are light-gated cation channels, were identified from the green alga Chlamydomonas reinhardtii (Nagel et al., 2002; Sineshchekov et al., 2002; Suzuki et al., 2003). When CrChR1 and CrChR2 were expressed in Xenopus oocytes, they functioned as light-gated cation-selective channels (Nagel et al., 2002; Nagel et al., 2003). CrChR2 was used to depolarize mammalian cells in response to light (Boyden et al., 2005; Ishizuka et al., 2006). Thereafter, variants of CrChR2 or chimeric forms of CrChR1 and CrChR2 were developed to improve the efficiency of expression and induce higher activity than the original CrChR1 and CrChR2 (Berndt et al., 2011; Deisseroth, 2011; Ernst et al., 2014; Wang et al., 2009). These efforts have made CrChRs the most commonly used optogenetic tools to induce depolarization in neurons and mimic neuronal activation through ion channel-type neurotransmitter receptors. However, there are some limitations when using CrChRs as optogenetic tools. The ion selectivity of CrChR2 is much higher for H+ than Na+ (Nagel et al., 2003). If pH inside and outside the cell differs, CrChR2 acts as an H+ channel rather than an Na+ channel. As CrChR2 is permeable to Ca2+ to some extent (Nagel et al., 2003), neuronal activation by CrChR2 leads to both depolarization and activation of the Ca2+ pathway, making it difficult to distinguish between the two effects. GtCCR4 is a light-gated cation channel derived from the cryptophyte Guillardia theta (Govorunova et al., 2016; Yamauchi et al., 2017). The light sensitivity of GtCCR4 is higher than that of CrChR2 while the channel open lifetime lies in the same range as that of CrChR2 when expressed in mammalian neuronal cells. Since GtCCR4 conducts almost no H+ and no Ca2+ under physiological conditions, GtCCR4 is a high Na+-selective ChR (Hososhima et al., 2020; Shigemura et al., 2019). KnChR is another cation ChR derived from the filamentous terrestrial alga Klebsormidium nitens (Tashiro et al., 2021). Truncation of the carboxy-terminal of KnChR prolonged the channel open lifetime by more than 10-fold, providing strong light-induced channel activity (Tashiro et al., 2021). These findings imply that GtCCR4 and truncated variants of KnChR are alternative optogenetic tools that can compensate for the shortcomings of CrChRs or display stronger photo-inducing activity than CrChRs (Hososhima et al., 2020; Tashiro et al., 2021). In addition to these, the activity of several ChRs, including CoChR and ChrimsonR, has been studied in zebrafish neurons, but these have not been compared directly with GtCCR4 or KnChR (Antinucci et al., 2020).

Among the microbial enzymorhodopsins (Mukherjee et al., 2019; Tsunoda et al., 2021), BeGC1 is a rhodopsin guanylyl cyclase (Rh-GC) derived from the aquatic fungus Blastocladiella emersonii and is responsible for its zoospore phototaxis (Avelar et al., 2014). BeGC1 functions as a light-activated guanylyl cyclase. BeGC1 shows a rapid light-triggered increase in cGMP when expressed in Xenopus oocytes, mammalian cell lines and neurons, and Caenorhabditis elegans (Gao et al., 2015; Scheib et al., 2015). Furthermore, when BeGC1 was co-expressed with cyclic nucleotide-gated channel (CNG) in neurons, photoactivation of BeGC1 depolarized the neurons and evoked behavioral responses in C. elegans (Gao et al., 2015), suggesting the feasibility of BeGC1-mediated optogenetic control of neural functions.

In addition to enzymerhodopsins, photoactivated adenylyl cyclases (PACs) have also been used to regulate intracellular cyclic nucleotides in cells (Iseki and Park, 2021). PACs are flavoproteins that catalyze the production of cAMP in response to light stimulation. PACs from the sulfur bacterium Beggiatoa sp. (bPAC) (Losi and Gärtner, 2008) and the cynobacterium Oscillatoria acuminata (OaPAC) (Ohki et al., 2016) are well characterized. Both bPAC and OaPAC have a BLUF (sensors of blue-light using the flavin adenine nucleotide) domain and an adenylyl cyclase catalytic domain (Figure 2B). When expressed in Escherichia coli (Ryu et al., 2010), Xenopus oocytes, rat hippocampus neurons, and adult fruit flies (Stierl et al., 2011), bPAC acted as a light-dependent adenylyl cyclase. When bPAC was expressed in zebrafish interrenal cells, which is the teleost homologue of adrenal gland cells, cortisol increased in a light-dependent manner (Gutierrez-Triana et al., 2015). bPAC was also used for light-dependent control of sperm motility in mice (Jansen et al., 2015), the release of neurotransmitter in C. elegans neurons (Steuer Costa et al., 2017), and the control of developmental processes of Dictyostelium discoideum (Tanwar et al., 2017). Compared to bPAC, OaPAC showed lower minimum photoactivity in the dark and lower maximum photoactivity upon light stimulation when expressed in HEK293 cells (Ohki et al., 2016). Nevertheless, OaPAC induced light-dependent axon growth in rat hippocampal neurons (Ohki et al., 2016). These experimental findings indicate that bPAC and OaPAC are useful optogenetic tools, although their activity in other cell types and animals is unknown. Specifically, the effectiveness of bPAC and OaPAC in a variety of zebrafish cells remains unclear.

In this study, we expressed the ChRs GtCCR4 and KnChR, enzymorhodopsin BeGC1, and two PACs, bPAC and OaPAC, in hindbrain reticulospinal V2a neurons (Kimura et al., 2013), which are involved in the induction of swimming behavior, and in cardiomyocytes using the zebrafish Gal4-UAS system (Asakawa et al., 2008), and examined their optogenetic activities. Our findings suggest that the optogenetic control using these tools provides a way to analyze the function and regulation of zebrafish neurons and cardiomyocytes in vivo.

## Results

### Optogenetic activation of cultured neuronal cells by ChRs

To express rhodopsins in vivo, fluorescence markers are useful to confirm expression in target cells. We tested two methods for marking rhodopsin-expressing cells: expression as a fusion protein with a fluorescent protein, and expression of epitope (e.g. Myc and Flag)-tagged rhodopsin and fluorescent protein separately using a viral 2A (P2A) peptide system. We expressed a fusion protein of GtCCR4-3.0-EYFP, which contains the membrane-trafficking signal and the endoplasmic reticulum (ER)-export signal from a Kir2.1 potassium channel (Gradinaru et al., 2010; Hoque et al., 2016), or Myc-tagged GtCCR4 (GtCCR4-MT) and TagCFP separately in neuronal ND7/23 cells, which are a hybrid cell line derived from rat neonatal dorsal root ganglia neurons fused with mouse neuroblastoma (Wood et al., 1990). We also compared the optogenetic activity of KnChR-3.0-EYFP whose biophysical properties were previously analyzed (Tashiro et al., 2021). Since carboxy terminal truncations of KnChR were shown to prolong the channel open lifetime and result in stronger optogenetic activity (Tashiro et al., 2021), a truncated KnChR containing 272 amino acids from the N-terminus was expressed as a fusion protein containing the membrane-trafficking signal, the ER-export signal, and EYFP (KnChR-3.0-EYFP). CrChR2[T159C]-mCherry, CoChR-tdTomato, and ChrimsonR-tdTomato were employed as positive controls to compare the tools investigated in this study (Antinucci et al., 2020; Berndt et al., 2011). We irradiated transfected cells with 511 nm light (GtCCR4-3.0-EYFP, GtCCR4-MT), 469 nm light (KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, CoChR-tdToamto), or 590 nm light (ChrimsonR-tdTomato). As was reported with GtCCR4-EGFP (Hososhima et al., 2020; Shigemura et al., 2019; Yamauchi et al., 2017), when GtCCR4-3.0-EYFP or GtCCR4-MT-P2A-TagCFP were photoactivated in ND7/23 cells, they induced a peak photocurrent that was comparable to that of KnChR-3.0-EYFP and CrChR2[T159C]-mCherry, higher than that of ChrimsonR-tdTomato, and lower than that of CoChR-tdTomato (Figure 1A and B). Peak and steady-state photocurrents were not significantly different in cells expressing GtCCR4-3.0-EYFP and GtCCR4-MT (Figure 1B), suggesting that photoactivation of GtCCR4 from both constructs became immediately saturated. Channel-closing kinetics after shutting-off light (τoff) was equally fast for GtCCR4-3.0-EYFP, GtCCR4-MT, CrChR2[T159C]-mCherry, and CoChR-tdTomato, and was faster than that observed for KnChR-3.0-EYFP, but slower than that of ChrimsonR-tdTomato (Figure 1C). Spectrum analysis revealed that GtCCR4-3.0-EYFP responded to light of slightly longer wavelengths than KnChR-3.0-EYFP and CrChR2[T159C]-mCherry, but to shorter wavelengths for ChrimsonR-tdTomato (Figure 1D). The half-saturation maximum (EC50) of peak and steady-state photocurrents was lower in GtCCR4-3.0-EYFP than in CrChR2[T159C]-mCherry and ChrimsonR-tdTomato, but comparable to that of CoChR-tdTomato (Figure 1E, Figure 1—figure supplement 1), suggesting that GtCCR4-3.0-EYFP responded to weaker light stimulation than CrChR2[T159C]-mCherry and ChrimsonR-tdTomato. These data indicate that GtCCR4-3.0-EYFP, GtCCR4-MT, and KnChR-3.0-EYFP are highly sensitive tools comparable to CoChR-3.0-EYFP, CrChR2[T159C]-mCherry and ChrimsonR-tdTomato. In addition, GtCCR4-3.0-EYFP and GtCCR4-MT in cultured cells can be activated by light of wavelengths between those of CrChR2[T159C]-mCherry and ChrimsonR-tdTomato.

![Figure 1.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig1-v1.jpg)

**Figure 1.:** (A) Representative photocurrent traces of GtCCR4-3.0-EYFP (GtCCR4-3.0), GtCCR4-MT-P2A-TagCFP (GtCCR4-MT), KnChR, CrChR2[T159C], CoChR, and ChrimsonR. Electrophysiological recordings were performed. Membrane voltage was clamped at –60 mV. Illumination sources were 511 nm light (GtCCR4-3.0, GtCCR4-MT), 469 nm light (KnChR, CrChR2[T159C], CoChR), and 590 nm light (ChrimsonR) at 1.4 mW/mm2. (B) Photocurrent amplitude. Gray bar: peak photocurrent (Ip); white bar: steady state photocurrent (Iss) (n = 6–9). Wilcoxon rank-sum test (CrChR2[T159C]-mCherry Ip vs. Iss, p=0.025; CoChR-tdTomato Ip vs. GtCCR4-3.0-EYFP Ip, p=0.025; ChrimsonR Ip vs. GtCCR4-3.0-EYFP Ip, p=0.049). (C) Comparison of the channel closing kinetics after shutting-off light (τoff) (n = 6–9), Wilcoxon rank-sum test (KnChR-EYFP vs. GtCCR4-3.0-EYFP, p=0.0002; ChrimsonR vs. GtCCR4-3.0-EYFP, p=0.0004). (D) The action spectrum of GtCCR4-3.0 (green circle), KnChR (blue circle), CrChR2[T159C] (purple circle), CoChR (light blue circle), and ChrimsonR (red circle). Illumination sources were 385, 423, 469, 511, 555, 590, or 631 nm light at 1.4 mW/mm2 (GtCCR4-3.0, CrChR2[T159C]) or 0.14 mW/mm2 (KnChR, CoChR, ChrimsonR) (n = 5–10). (E) Half saturation maximum (EC50) of the peak photocurrent (gray bar) and the steady-state photocurrent (white bar) are shown (n = 5, 6), Wilcoxon rank-sum test (CrChR2[T159C]-mcherry Ip vs. Iss, p=0.0079; CrChR2[T159C]-mCherry Ip vs. GtCCR4-3.0-EYFP Ip, p=0.0086; ChrimsonR Ip vs. GtCCR4-3.0-EYFP Ip, p=0.0021; ChrimsonR Iss vs. GtCCR4-3.0-EYFP Iss, p=0.0021). *p<0.05, **p<0.01, ***p<0.001, ****p<0.0005, Mean and SEM are indicated.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Photocurrent amplitude at − 60 mV was plotted as a function of light power. 511 nm light (A), 469 nm light (B, C), and 590 nm light (D) were illuminated. Filled circle: peak photocurrent; open circle: steady-state photocurrent (n = 5, 6). Error bars indicate standard errors of the mean (SEMs).

### Optogenetic activation of zebrafish locomotion circuit by GtCCR4 and KnChR

We expressed GtCCR4 and KnChR in the hindbrain reticulospinal V2a neurons of zebrafish, which were reported to drive locomotion (Kimura et al., 2013) by using a Gal4-UAS system (Figure 2A). We compared the activities of these ChRs with those of CrChR2[T159C]-mCherry, CoChR-tdTomato, and ChrimsonR-tdTomato. We crossed a transgenic (Tg) zebrafish Tg(vsx2:GAL4FF), which is also known as Tg(chx10:GAL4) and expresses a modified transcription factor Gal4-VP16 in the hindbrain reticulospinal V2a neurons (Kimura et al., 2013), with Tg lines carrying optogenetic tools that are expressed under the control of 5xUAS (upstream activating sequences of yeast Gal1 gene) and the zebrafish hsp70l promoter (Muto et al., 2017). Since transgene-mediated protein expression depends on the nature of the introduced gene, as well as the transgene-integrated sites and copy number, we established multiple Tg lines and analyzed stable Tg lines (F1 or later generations) with the highest tool expression for each tool. The expression of the fusion proteins, composed of a ChR and a fluorescent protein, in the hindbrain reticulospinal V2a neurons were detected under an epifluorescent stereomicroscope. Despite differences in expression between lines, immunohistochemistry with anti-fluorescent protein (anti-GFP and DsRed antibodies for EYFP and RFP/mCherry, respectively) and anti-MT antibodies revealed that in the reticulospinal V2a neurons, GtCCR4-3.0-EYFP, KnChR-3.0-EYFP, and CrChR2[T159C]-mCherry were similarly expressed, and GtCCR4-MT was expressed more strongly (Figure 2C, Table 1). KnChR-3.0-EYFP demonstrated mosaic expression (Figure 2C). The detection of fluorescence in CoChR-tdTomato and ChrimsonR-tdTomato indicated that these ChRs were also expressed adequately in the reticulospinal V2a neurons (Figure 2C). We irradiated a hindbrain area of 3 days post fertilization (dpf) Tg larvae expressing GtCCR4-3.0-EYFP, GtCCR4-MT, KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, CoChR-tdTomato, and ChrimsonR-tdTomato with light of 520 nm (GtCCR4, ChrimsonR) and 470 nm (KnChR, CrChR2[T159C], and CoChR) for 100 ms (Figures 2A and D and 3A–E, Table 1, Figure 2—videos 1–6). We measured the rate at which light stimulation induced tail movements (locomotion rate, Figure 3A, Figure 3—figure supplement 3), the time from stimulation to the onset of tail movements (latency, Figure 3B, Figure 3—figure supplement 2), the duration of tail movements (Figure 3C), and the amplitude of tail movements (Figure 3D). To examine photosensitivity of these ChRs, we also irradiated them with light of various intensities and examined corresponding tail movements (Figure 3E, Figure 3—figure supplements 1–3).

![Figure 2.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig2-v1.jpg)

**Figure 2.:** (A) Schematic of experimental devices. A larva was embedded in agarose. The hindbrain region or the heart were irradiated with light. Tail (caudal fin) movements and heartbeats were monitored by a high-speed camera with infrared light. (B) Schematic diagram of optogenetic tools used in this study. GC, guanylyl cyclase; AC, adenylyl cyclase; BLUF, sensors of blue-light using FAD. (C) Expression of GtCCR4-3.0-EYFP, GtCCR4-MT, KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, CoChR-tdTomato, and ChrimsonR-tdTomato in the zebrafish hindbrain reticulospinal V2a neurons. 3 dpf (day post fertilization) Tg(vsx2:GAL4FF);Tg(UAS-hsp70l:GtCCR4-3.0-EYFP, GtCCR4-MT-P2A-TagCFP, KnChR-3.0-EYFP, or CrChR2[T159C]-mCherry, myl7:mCherry) larvae were fixed and stained with anti-GFP (EYFP, green), anti-Myc tag (green) or anti-DsRed (RFP, magenta) antibodies. For CoChR and ChrimsonR, fluorescent images of the hindbrain of Tg(vsx2:GAL4FF);Tg(UAS:CoChR-tdTomato, or UAS-hsp70l:ChrimsonR-tdTomato, myl7:mCherry) larvae are shown. Inset: higher magnification images for the boxed areas showing double-labeled neurons. (D) Tail movements of 3-dpf Tg larvae expressing GtCCR4-3.0-EYFP, GtCCR4-MT, KnChR-3.0-EYFP, and CrChR2[T159C]-mCherry, CoChR-tdTomato, and ChrimsonR-tdTomato in the reticulospinal V2a neurons after stimulation of the hindbrain area with LED (0.4 mW/mm2) light with a wavelength of 520 nm (GtCCR4-3.0-EYFP, GtCCR4-MT, ChrimsonR-tdTomato) and 470 nm (KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, CoChR-tdTomato) for 100 ms. Light stimulations started at time 0 s. Typical examples are shown. Scale bars = 150 μm in (C), 5 μm in the insets of (C).

**Table 1.**
 Optogenetic tools.Microbial optogenetic tools were expressed in the hindbrain reticulospinal V2a neurons or cardiomyocytes using the Gal4-UAS system.The expression levels of the tools were determined by immunostaining with anti-tag (MT or Flag) antibodies or anti-fluorescent marker antibodies (anti-GFP and anti-DsRed for EYFP/EGFP and mCherry, respectively) (+, weak; ++, medium; +++, strong expression). The light stimulus-dependent responses (induced swimming or cardiac arrest) are indicated by the percentage of fish that responded to light stimuli. As controls, the responses of sibling larvae that did not express the tools were also examined. ND, not determined.


<table>
  <thead>
    <tr>
      <th rowspan="2">Type</th>
      <th rowspan="2">Tool name</th>
      <th rowspan="2">Origin</th>
      <th rowspan="2">Detection</th>
      <th rowspan="2">Stimulation light (nm)</th>
      <th colspan="2">V2a neurons</th>
      <th colspan="2">Heart</th>
    </tr>
    <tr>
      <th>Expression</th>
      <th>Swimming response (control)</th>
      <th>Expression</th>
      <th>Cardiac response(control)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="9">Channelrhodopsin</td>
    </tr>
    <tr>
      <td>Cation</td>
      <td>GtCCR4-3.0-EYFP</td>
      <td>Guillardia theta</td>
      <td>EYFP fusion</td>
      <td>520</td>
      <td>++</td>
      <td>62.5%, n = 8(14.6%, n = 8)</td>
      <td>+++</td>
      <td>100%, n = 4(0%, n = 4)</td>
    </tr>
    <tr>
      <td>Cation</td>
      <td>GtCCR4-MT</td>
      <td>Guillardia theta</td>
      <td>MT-P2A-TagCFP</td>
      <td>520</td>
      <td>+++</td>
      <td>50.0%, n = 8(8.33%, n=8)</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
    <tr>
      <td>Cation</td>
      <td>KnChR-3.0-EYFP</td>
      <td>Klebsormidium nitens</td>
      <td>EYFP fusion</td>
      <td>470</td>
      <td>++*</td>
      <td>100%, n = 8(8.33%, n = 8)</td>
      <td>+++</td>
      <td>100%, n = 4(0%, n = 4)</td>
    </tr>
    <tr>
      <td>Cation</td>
      <td>CrChR2 [T159C]-mCherry</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>mCherry fusion</td>
      <td>470</td>
      <td>++</td>
      <td>67.4%, n = 12(25.0%, n = 8)</td>
      <td>+ ¶</td>
      <td>100%, n = 4(0%, n = 4)</td>
    </tr>
    <tr>
      <td>Cation</td>
      <td>CoChR-tdTomato</td>
      <td>Chloromonas oogama</td>
      <td>tdTomato fusion</td>
      <td>470</td>
      <td>+++†</td>
      <td>100%, n = 8(2.08%, n = 8)</td>
      <td>ND</td>
      <td>100%, n = 4</td>
    </tr>
    <tr>
      <td>Cation</td>
      <td>ChrimsonR-tdTomato</td>
      <td>Chlamydomonas noctigama</td>
      <td>tdTomato fusion</td>
      <td>520</td>
      <td>++†</td>
      <td>23.8%, n = 8(6.25%, n = 8)</td>
      <td>ND</td>
      <td>100%, n = 4</td>
    </tr>
    <tr>
      <td>Anion</td>
      <td>GtACR1-EYFP</td>
      <td>Guillardia theta</td>
      <td>EYFP fusion</td>
      <td>520</td>
      <td>++ ‡</td>
      <td>80.5%, n = 6 §(13.2%, n = 6)</td>
      <td>+++</td>
      <td>100%, n = 4(0%, n = 4)</td>
    </tr>
    <tr>
      <td colspan="9">Enzymorhodopsin</td>
    </tr>
    <tr>
      <td>Guanyly cyclase</td>
      <td>BeGC1-EGFP</td>
      <td>Blastocladiella emersonii</td>
      <td>EGFP fusion</td>
      <td>520</td>
      <td>+++</td>
      <td>53.5%, n = 8(10.4%, n = 8)</td>
      <td>+++**</td>
      <td>0%, n = 102††(ND)</td>
    </tr>
    <tr>
      <td colspan="9">Photoactivated adenylyl cyclase</td>
    </tr>
    <tr>
      <td>Adenylyl cyclase</td>
      <td>bPAC-MT</td>
      <td>Beggiatoa</td>
      <td>MT-T2A-tDimer</td>
      <td>470</td>
      <td>++</td>
      <td>60.6%, n = 8(26.2%, n = 8)</td>
      <td>+++</td>
      <td>100%, n = 4 ‡ ‡(ND)</td>
    </tr>
    <tr>
      <td>Adenylyl cyclase</td>
      <td>OaPAC-Flag</td>
      <td>Oscillatoria acuminata</td>
      <td>Flag-P2A-TagCFP</td>
      <td>470</td>
      <td>++</td>
      <td>42.5%, n = 8(15.4%, n = 8)</td>
      <td>+++</td>
      <td>0%, n = 104 § §(ND)</td>
    </tr>
  </tbody>
</table>

_*Expression of KnChR-3.0-EYFP was mosaic.†Expression of CoChR-tdTomato and ChrimsonR-tdTomato was detected by observation with an epifluorescent stereomicroscope.‡Expression was confirmed by detecting EYFP.§The percentages of spontaneous tail movements elicited by white light that was inhibited by rhodopsin activation (locomotion-inhibition trials) are indicated (no rhodopsin activation was used as the control).¶Expression of CrChR2 [T159C]-mCherry was detected by qPCR.**The expression of BeGC1-EGFP was determined by observation with an epifluorescent microscope MZ16 FA and a fluorescence detection filter (460–500 nm, Leica).††Cardiac arrest was not induced with 490–510 nm, 530–560 nm (epifluorescent stereomicroscope-equipped light source, n = 100), or 520 nm (LED) light stimuli (n = 2).‡ ‡Light stimulation with 470 nm LED light for 5 s induced bradycardia, which took a few minutes to return to normal heartbeats.§ §Stimulation with 460–500 nm (epifluorescent stereomicroscope-equipped light source, n = 100) or 470 nm LED light (n = 4) induced neither cardiac arrest nor bradycardia, while stimulation with 470 nm LED light occasionally induced transient tachycardia for a few seconds (n = 2)._

![Figure 3.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig3-v1.jpg)

**Figure 3.:** (A) Light stimulation-dependent locomotion rates of 3-dpf Tg larvae expressing GtCCR4-3.0-EYFP, GtCCR4-MT, KnChR-3.0-EYFP, CrChR2[T159C]-mCherry. The hindbrain area was irradiated with light (0.4 mW/mm2) with a wavelength of 520 nm (GtCCR4-3.0-EYFP and GtCCR4-MT) or 470 nm (KnChR-3.0-EYFP and CrChR2[T159C]-mCherry) for 100 ms. Six consecutive stimulation trials were analyzed for eight rhodopsin-expressing and non-expressing (control) larvae of each Tg line. The average locomotion rates for each larva are shown, Wilcoxon rank-sum test (GtCCR4-3.0-EYFP vs. control, p=0.00166; GtCCR4-MT vs. control, p=0.00216; KnChR-EYFP vs. control, p=0.000266; CrChR2[T159C]-mCherry vs. control, p=0.0246). (B–D) Latency (B), duration (C), and strength (D) of tail movements. The time from the start of light stimulation to the first tail movement was defined as latency (s), and the time from the start of the first tail movement to the end of that movement was defined as duration (s). The maximum distance that the caudal fin moved from the midline divided by body length was measured as representative of its strength. One-way ANOVA with Tukey’s post hoc test (latency GtCCR4-3.0-EYFP vs. CrChR2[T159C]-mCherry, p=0.0115; GtCCR4-3.0-EYFP vs. KnChR-EYFP, p=0.0128; strength GtCCR4-3.0-EYFP vs. KnChR-EYFP, p=0.00601; GtCCR4-MT vs. KnChR-EYFP, p=0.00181; KnChR-EYFP vs. CrChR2[T159C]-mCherry, p=4.00e-06). (E) Locomotion evoked by light of various light intensities. The hindbrain area was irradiated with light at 0.4, 0.2, or 0.1 mW/mm2. Six consecutive trials were analyzed for 4–6 rhodopsin-expressing larvae for each Tg (n = 6 for GtCCR4-3.0-EYFP and KnChR-3.0-EFYP; n = 5 for CrChR2[T159C]-mCherry). Light stimulation experiments at 0.2 and 0.1 mW/mm2 were conducted only on larvae that exhibited evoked locomotion three or more times in response to the initial light stimulation at 0.4 mW/mm2. One-way ANOVA with Tukey’s post hoc test (GtCCR4-3.0-EYFP: 0.4 mW/mm2 vs. 0.1 mW/mm2, p=1.03e-05, 0.4 mW/mm2 vs. 0.2 mW/mm2, p=4.39e-05; CrChR2[T159C]-mCherry: 0.4 mW/mm2 vs. 0.1 mW/mm2, p=0.0185). *p<0.05, **p<0.01, ***p<0.001, ns: not significant. Means and SEMs are indicated.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The hindbrain of 3-dpf larvae expressing GtCCR4-3.0-EYFP, GtCCR4-MT, or KnChR-3.0-EYFP, and non-expressing sibling control larvae was irradiated with light (520 nm for GtCCR4-3.0-EYFP, GtCCR4-MT and 470 nm for KnChR-3.0-EYFP) for 100 ms. Six consecutive stimulation trials were analyzed for eight rhodopsin-expressing and non-expressing control larvae of each line (48 trials for each condition). Latency was measured as the tail movements observed within 8 s after the onset of light stimulation and plotted in a graph. The number of tail movements was 28 and 7 for GtCCR4-3.0-EYFP and the control, 24 and 4 for GtCCR4-MT and the control, and 25 and 4 for KnChR-3.0-EYFP and the control, respectively.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Latency (A) and duration (B) of evoked tail movements. The hindbrain area of 3-dpf Tg larvae expressing GtCCR4-3.0, KnChR-3.0, and CrChR2[T159C] and control larvae (non-expressing sibling larvae) were irradiated by light of different light intensities. Six consecutive stimulation trials were analyzed for eight rhodopsin-expressing and non-expressing (control) larvae of each Tg line. One-way ANOVA with Tukey’s post hoc test (latency GtCCR4-3.0-EYFP 0.4 mW/mm2 vs. 0.2 mW/mm2, p=0.00571; KnChR-3.0-EYFP 0.4 mW/mm2 vs. 0.2 mW/mm2, p=0.00553; 0.4 mW/mm2 vs. 0.1 mW/mm2, p=5.26e-06; 0.2 mW/mm2 vs. 0.1 mW/mm2, p=0.00469). **p<0.01, ***p<0.001, ns: not significant. Means and SEMs are indicated.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (A) Light stimulation-dependent locomotion rates of 3-dpf Tg larvae expressing CoChR-tdTomato and ChrimsonR-tdTomato. The hindbrain area was irradiated with light (0.4 mW/mm2) with a wavelength of 470 nm (CoChR-tdTomato) or 520 nm (ChrimsonR-tdTomato) for 100 ms. Six consecutive stimulation trials were analyzed for eight rhodopsin-expressing and eight non-expressing (control) larvae of each Tg line. The average locomotion rates for each larva are shown. Wilcoxon rank-sum test (CoChR-tdTomato vs. control, p=0.000205; ChrimsonR vs. control, p=0.0509). (B–D) Latency (B), duration (C), and strength (D) of tail movements. Welch’s t-test (strength CoChR-tdTomato vs. ChrimsonR; p=0.00463). (E) Rate of locomotion induced with CoChR-tdTomato by light of various light intensities. **p<0.01, ***p<0.001, ns: not significant. Means and SEMs are indicated.

Light stimulation of the reticulospinal V2a neurons with CrChR2[T159C]-mCherry immediately evoked tail movements (locomotion rate 67.4 ± 11.8%, latency 0.109 ± 0.0311 s, Figure 3A and B, Figure 2—video 1). Light stimulation with GtCCR4-3.0-EYFP and GtCCR4-MT evoked tail movements at comparable locomotion rates, although it took more time than CrChR2[T159C]-mCherry (GtCCR4-3.0-EYFP locomotion rate 62.5 ± 8.77%, latency 1.59 ± 0.536 s; GtCCR4-MT locomotion rate 50 ± 8.91%, latency 1.16 ± 0.445 s, Figure 3A and B, Figure 3—figure supplement 1, Figure 2—videos 2 and 3). Light stimulation with these ChRs induced transient tail movements (duration: GtCCR4-3.0-EYFP 0.698 ± 0.263 s, GtCCR4-MT 1.51 ± 0.414 s, CrChR2[T159C]-mCherry 2.17 ± 1.19 s, Figure 3C). The strength of the tail movements was not significantly different between GtCCR4-3.0-EYFP/GtCCR4-MT and CrChR2[T159C]-mCherry (GtCCR4-3.0-EYFP 0.642 ± 0.0555, GtCCR4-MT 0.605 ± 0.0796, CrChR2[T159C]-mCherry 0.404 ± 0.0629, Figure 3D), suggesting comparable photo-inducible activities of GtCCR4 and CrChR2[T159C] in the reticulospinal V2a neurons. As the activity of GtCCR4-3.0-EYFP was slightly higher than that of GtCCR4-MT (Figure 2C), we used GtCCR4-3.0-EYFP for further analysis. We found that KnChR-3.0-EYFP was a more potent tool for activating the zebrafish locomotion system than GtCCR4-3.0-EYFP, CrChR2[T159C]-mCherry, and ChrimsonR-tdTomato (Figure 3 and Figure 3—figure supplements 1–3). In all trials of all larvae, light stimulation of KnChR immediately evoked tail movements (locomotion rate 100 ± 0%, latency 0.0198 ± 0.00357 s, and duration 0.661 ± 0.0733 s, Figures 2D and 3A–C, Figure 2—video 4). The strength of evoked tail movements with KnChR-3.0-EYFP was stronger than that of GtCCR4-3.0-EYFP, GtCCR4-MT, CrChR2[T159C]-mCherry, and ChrimsonR-tdTomato, and comparable to that of CoChR-tdTomato (Figure 3D, Figure 3—figure supplement 3). Stimulation with GtCCR4-3.0-EYFP or CrChR2[T159C]-mCherry by light of lower intensities (0.1 mW/mm2) reduced locomotion rate, while that with KnChR-3.0-EYFP or CoChR-tdTomato still induced tail movements in all trials (Figure 3E, Figure 3—figure supplement 3). These data indicate that the optogenetic activity of KnChR-3.0-EYFP was as strong as that of CoChR-tdTomato in zebrafish reticulospinal V2a neurons.

### Optogenetic control of zebrafish heart by GtCCR4 and KnChR

We next examined the optogenetic activity of GtCCR4 and KnChR in cardiomyocytes, comparing it with that of the cation ChR CrChR2[T159C], CoChR, and ChrimsonR, and the anion ChR GtACR1 (GtACR1-EYFP), which enables the induction of hyperpolarization in cells (Govorunova et al., 2015). We expressed these ChRs in zebrafish cardiomyocytes by using Tg(myl7:GAL4FF), in which GAL4FF was expressed under the promoter of the cardiac myosin light chain gene myl7, and the UAS Tg lines. We established multiple Tg lines for each tool and used Tg lines with the highest tool expression level in cardiomyocytes. The expression of the fusion proteins, composed of ChR and fluorescent protein, in cardiomyocytes was detected under an epifluorescent stereomicroscope. Immunostaining with antifluorescent protein antibody revealed comparable expression of GtCCR4-3.0-EYFP, KnChR-3.0-EYFP, and GtACR1-EYFP in 4-dpf Tg larvae (Figure 4A, Table 1). Stimulation of the entire heart area of 4-dpf Tg larvae expressing ChRs with light (520 nm for GtCCR4, GtACR1, and ChrimsonR; 470 nm for KnChR, CrChR2[T159C], and CoChR) for 100 ms induced cardiac arrest in all six trials, with some differences in latency (Figures 4B and C and 5A and B, Figure 4—videos 1–6). The latency of cardiac arrest induced by stimulation with these ChRs was short, especially that of KnChR-3.0-EYFP, which was shorter than that of GtACR1-EYFP (GtCCR4-3.0-EYFP 163 ± 12 ms, KnChR-3.0-EYFP 55.2 ± 13.4 ms, CrChR2[T159C]-mCherry 112 ± 8.72 ms, GtACR1-EYFP 243 ± 48.8 ms, CoChR-tdTomato 215 ± 31.4 ms, ChrimsonR-tdTomato 212 ± 55.2 ms, Figure 5B, Figure 5—figure supplement 2).

![Figure 4.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig4-v1.jpg)

**Figure 4.:** (A) Expression of GtCCR4-3.0-EYFP, KnChR-3.0-EYFP, and GtACR1-EYFP in cardiomyocytes of Tg(myl7:GAL4FF);Tg(UAS-hsp70l:GtCCR4-3.0-EYFP, KnChR-3.0-EYFP, or GtACR1-EYFP, myl7:mCherry) larvae. 4-dpf Tg larvae were fixed and stained with anti-GFP (for EYFP, green) or anti-DsRed (for mCherry, magenta) antibodies. Z stacks of confocal images. (B) Heartbeat (HB) monitoring by changes in luminosity (AU, arbitrary units). The entire heart area of 4-dpf Tg larvae was irradiated with light (520 nm for GtCCR4 and GtACR1; 470 nm for KnChR and CrChR2) for 100 ms at a strength of 0.5 mW/mm2. (C) Average of relative HB frequency. The heart area was irradiated at the indicated periods. Six consecutive stimulus trials were analyzed for four rhodopsin-expressing larvae of each Tg line. Relative HB frequency was calculated from HB data during 1 s and 500 ms before and after each time point, so the change in the HB frequency was observed before light stimulation, even though cardiac arrest occurred during light stimulation. Gray shading indicates SEMs. Scale bar = 100 µm in (A).

![Figure 5.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig5-v1.jpg)

**Figure 5.:** (A) Cardiac arrest rates of 4-dpf Tg larvae expressing GtCCR4-3.0-EYFP, KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, or GtACR1-EYFP in cardiomyocytes. The heart area was irradiated with appropriate light (520 nm for GtCCR4 and GtACR1; 470 nm for KnChR and CrChR2) for 100 ms at a strength of 0.5 mW/mm2. Sibling larvae that did not express the rhodopsins were used as controls. Six consecutive stimulation trials were analyzed for four rhodopsin-expressing larvae and four control larvae of each Tg line, Wilcoxon rank-sum test (GtCCR4-3.0-EYFP, KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, and GtACR1-EYFP, p=0.0131). (B, C) Latency to cardiac arrest (B) and time to resumption of HBs (C) after light stimulation with GtCCR4-3.0-EYFP, KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, or GtACR1-EYFP. HB data were obtained from the experiments described above (A). One-way ANOVA with Tukey’s post hoc test (latency to cardiac arrest KnChR-3.0-EYFP vs. GtACR1-EYFP, p=0.00144; CrChR2[T159C]-mCherry vs. GtACR1-EYFP, p=0.0190; time to resumption of heartbeat GtCCR4-3.0-EYFP vs. GtACR1-EYFP, p=0.000786; KnChR-3.0-EYFP vs. GtACR1-EYFP, p=0.0189; CrChR2[T159C]-mCherry vs. GtACR1-EYFP, p=0.000236). (D) Light intensity dependence of cardiac arrest rates of 4-dpf Tg larvae expressing GtCCR4-3.0-EYFP, KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, GtACR1-EYFP in cardiomyocytes. The heart area was irradiated with light (520 nm for GtCCR4 and GtACR1; 470 nm for KnChR and CrChR2) for 100 ms at a strength of 0.5, 0.2, or 0.05 mW/mm2. Six consecutive stimulation trials were analyzed for four rhodopsin-expressing larvae of each Tg line. One-way ANOVA with Tukey’s post hoc test (GtCCR4-3.0-EYFP: 0.5 mW/mm2 vs. 0.05 mW/mm2; p=0.0222). (E, F) Changes in fluorescence intensity of GCaMP6s (ΔF/F) in the heart of 4-dpf Tg larvae expressing KnChR-3.0-EYFP and GCaMP6s (E), or GtACR1-EYFP and GCaMP6s (F). Sibling larvae that did not express the rhodopsins were used as the control. The heart area of Tg larvae was stimulated with a fluorescence detection filter (excitation 470–495 nm, emission 510–550 nm). Two rhodopsin-expressing larvae (green) and two control larvae (black) were analyzed for each rhodopsin. Three trials were analyzed for each larva. The linear mixed-effects model was used for statistical analysis. *p<0.05, **p<0.01, ***p<0.001, ns: not significant. Means and SEMs are indicated.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Latency to cardiac arrest (A) and time to resumption of heartbeats (B) after light stimulation with ChRs. The heart area of 4-dpf Tg larvae expressing GtCCR4-3.0-EYFP, KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, or GtACR1-EYFP was irradiated with light (520 nm for GtCCR4, GtACR1; 470 nm for KnChR, CrChR2) for 100 ms at a strength of 0.5, 0.2, or 0.05 mW/mm2. Six consecutive stimulation trials were analyzed for four rhodopsin-expressing larvae of each Tg line. One-way ANOVA with Tukey’s post hoc test (time to resumption of heartbeat GtACR1-EYFP 0.5 mW/mm2 vs. 0.05 mW/mm2, p=0.0240). *p<0.05, ns: not significant. Means and SEMs are indicated.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Cardiac arrest rate. The heart area of 4-dpf Tg larvae expressing CoChR-tdTomato or ChrimsonR-tdTomato was irradiated with light (470 nm for CoChR; 520 nm for ChrimsonR) for 100 ms at a strength of 0.5, 0.2, or 0.05 mW/mm2. Six consecutive stimulation trials were analyzed for four rhodopsin-expressing larvae of each Tg line. (B, C) Latency to cardiac arrest (B) and time to resumption of heartbeats (C) after light stimulation with optogenetic tools. One-way ANOVA with Tukey’s post hoc test was used for statistical analysis. ns: not significant. Means and SEMs are indicated.

Heartbeats (HBs) resumed within 2 s after light stimulation but took longer when stimulated with GtACR1-EYFP than with GtCCR4-3.0-EFYP or KnChR-3.0-EYFP (GtCCR4-3.0-EYFP 418 ± 91.4 ms, KnChR-3.0-EYFP 742 ± 62.3 ms, CrChR2[T159C]-mCherry 284 ± 29.7 ms, GtACR1-EYFP 1350 ± 215 ms, CoChR-tdTomato 379 ± 45.6 ms, ChrimsonR-tdTomato 319 ± 41.7 ms, Figure 5C, Figure 5—figure supplement 2). Stimulation with GtCCR4-3.0-EYFP by light of lower light intensity (0.05 mW/mm2) reduced cardiac arrest rate, while stimulation with KnChR-3.0-EYFP or CoChR-tdTomato still induced cardiac arrest in all trials (Figure 5D, Figure 5—figure supplements 1 and 2). These data again indicate that optogenetic activity of KnChR-3.0-EYFP is as strong as that of CoChR-tdTomato in zebrafish cardiomyocytes. Considering that GtACR1 is an anion ChR and GtCCR4/KnChR are cation ChRs, the mechanism of cardiac arrest is expected to be different. To address this issue, we monitored intracellular Ca2+ concentration in cardiomyocytes using GCaMP6s. Light stimulation with KnChR-3.0-EYFP increased fluorescence intensity (ΔF/F) of GCaMP6s in the heart and induced cardiac muscle contraction (Figure 5E, Figure 5—video 1), whereas that with GtACR1-EYFP reduced the fluorescence intensity of GCaMP6s and induced relaxation of the myocardium (Figure 5F, Figure 5—video 2), suggesting distinct mechanisms for cardiac arrest induced by the cation ChRs (GtCCR4 and KnChR) and anion ChR (GtACR1).

### Optogenetic control of cAMP/cGMP by BeGC1 and PACs

We examined the optogenetic activity of the fungal guanylyl cyclase rhodopsin BeGC1 and compared it to that of the flavoprotein-type bacterial PACs bPAC and OaPAC. By using Tg(vsx2:GAL4FF) and UAS Tg lines, we established Tg lines that expressed BeGC1-EGFP, bPAC-MT, and OaPAC-Flag in the reticulospinal V2a neurons (Figures 6A and 7A). Although the levels of expression of bPAC-MT and OaPAC-Flag were slightly lower than that of BeGC1, light stimulation of the reticulospinal V2a neurons with BeGC1-EGFP (520 nm), bPAC-MT (470 nm), and OaPAC-Flag (470 nm) at 0.4 mW/mm2 for 500 ms evoked relatively high-frequency tail movements (BeGC1-EGFP 53.5 ± 7.25%, bPAC-MT 60.6 ± 9.8%, OaPAC-Flag 42.5 ± 13.7%, Figures 6B and C and 7B and C, Figure 6—video 1, Figure 7—videos 1 and 2). The tail movements induced by activation with BeGC1, bPAC, or OaPAC had a long latency (BeGC1-EGFP 0.674 ± 0.118 s, bPAC-MT 2.6 ± 0.396 s, OaPAC-Flag 4.0 ± 0.582 s, Figures 6D and 7D), but similar duration and strength compared to activation with the ChRs (duration BeGC1-EGFP 2.05 ± 0.33 s, bPAC-MT 2.02 ± 0.531 s, OaPAC-Flag 2.83 ± 1 s; strength BeGC1-EGFP 0.815 ± 0.0926, bPAC-MT 0.66 ± 0.116, OaPAC-Flag 0.705 ± 0.102, Figures 6E and F and 7E and F). The latency of light responses in Tg fish expressing bPAC or OaPAC was long, whereas in control larvae that did not express these tools, spontaneous responses within 8 s were significantly lower (Figure 7C). Even when observing within 30 s after the light stimulus, the frequency of spontaneous tail movements was low (Figure 7—figure supplement 1), indicating that most of the tail movements induced with bPAC and OaPAC were robust responses to light. When a cAMP fluorescent indicator Flamindo2 (Odaka et al., 2014) was co-expressed with bPAC-MT or OaPAC-Flag in postmitotic neurons by the elavl3 promoter and the elavl3 promoter-driven GAL4-VP16 Tg line, continuous light stimulation reduced the ΔF/F of Flamindo2, which is indicative of an intracellular increase in cAMP (Odaka et al., 2014), in the optic tectum (Figure 7G and H). We also used Tg lines expressing BeGC1, bPAC or OaPAC in cardiomyocytes. Although light stimulation of cardiomyocytes with BeGC1 or OaPAC (Table 1) induced neither cardiac arrest nor bradycardia, activation with bPAC for 5 s gradually reduced HBs and it took a few minutes to return to normal HBs (Figure 7—figure supplement 2, Figure 7—video 3). These data indicate that BeGC1 and OaPAC can be used for optogenetic activation of neurons but not cardiomyocytes, while bPAC can be used for optogenetic control of neurons as well as cardiomyocytes in zebrafish.

![Figure 6.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig6-v1.jpg)

**Figure 6.:** (A) Expression of BeGC1-EGFP in the hindbrain reticulospinal V2a neurons. 3-dpf Tg(vsx2:GAL4FF);Tg(UAS:BeGC1-EGFP, myl7:mCherry);Tg(UAS:RFP) larvae were fixed and stained with anti-GFP (EGFP, green) or anti-DsRed (RFP, magenta) antibodies. Inset: higher magnification images for the boxed area showing double-labeled neurons. In the inset, fluorescence signal intensities were modified to compare the subcellular localization of the tools. (B) Tail movements of 3-dpf Tg larvae expressing BeGC1 in the reticulospinal V2a neurons after stimulation with light (0.4 mW/mm2) at 520 nm for 500 ms. The stimulation started at time 0 s. A typical induced tail movement is shown. (C) Light stimulation-dependent locomotion rates of 3-dpf BeGC1-expressing larvae or non-expressing sibling control larvae. Six consecutive stimulation trials were analyzed for eight BeGC1-expressing and eight non-expressing larvae. The average locomotion rates for each larva are shown. Wilcoxon rank-sum test (BeGC1-EGFP vs. control, p=0.00608). (D–F) Latency (D), duration (E), and strength (F) of induced tail movements in the BeGC1-expressing larvae. The time from the start of light stimulation to the first tail movement was defined as latency (s), and the time from the start of the first tail movement to the end of that movement was defined as duration (s). The maximum distance that the caudal fin moved from the midline divided by body length reflected its strength. Scale bars = 150 μm in (A), 10 μm in the insets of (A). **p<0.01. Means and SEMs are indicated.

![Figure 7.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig7-v1.jpg)

**Figure 7.:** (A) Expression of bPAC and OaPAC in reticulospinal V2a neurons. 3-dpf Tg(vsx2:GAL4FF);Tg(UAS-hsp70l:bPAC-MT-T2A-tDimer, myl7:mCherry);Tg(UAS;RFP) and Tg(vsx2:GAL4FF);Tg(UAS-hsp70l:OaPAC-Flag-P2A-TagCFP, myl7:mCherry);Tg(UAS:RFP) larvae were fixed and stained with anti-Myc or anti-Flag (green), and anti-DsRed (RFP, magenta) antibodies. To detect relatively weak fluorescent signals of bPAC-MT and OaPAC-Flag, images were taken with increased laser power (2× for bPAC-MT and 4× for OaPAC-Flag compared to BeGC1-EGFP in Figure 6A). Inset: higher magnification images for the boxed areas showing double-labeled neurons. (B) Tail movements of 3-dpf Tg larvae expressing bPAC-MT or OaPAC-Flag in the reticulospinal V2a neurons after stimulation with light (0.4 mW/mm2) at 470 nm for 500 ms. The stimulation started at time 0 s. Typical examples are shown. (C) Light-induced locomotion rates. Larvae that did not express PACs were used as controls. Six consecutive stimulation trials for eight PAC-expressing and eight control larvae were analyzed. The average locomotion rates for each larva are shown. Wilcoxon rank-sum test (bPAC-MT vs. control, p=0.0376; OaPAC-Flag vs. control, p=0.145). (D–F) Latency (D), duration (E), and strength (F) for light stimulus-induced tail movements in larvae expressing bPAC-MT or OaPAC-Flag. The data for each larva are plotted in graphs. (G, H) Changes in fluorescence intensity (ΔF/F) of cAMP indicator Flamido2 in neurons of Tg larvae expressing bPAC-MT (G) or OaPAC-Flag (H) after light stimulation. The entire optic tectum area of 3-dpf Tg(elavl3:GAL4-VP16); Tg(elavl3:Flamindo2); Tg(UAS-hsp70l:bPAC-MT-T2A-tDimer) and Tg(elavl3:GAL4-VP16); Tg(elavl3:Flamindo2); Tg(UAS-hsp70l:OaPAC-Flag-P2A-TagCFP) larvae was stimulated with a fluorescence detection filter (excitation 470–495 nm, emission 510–550 nm). The fluorescence intensity of the optic tectum was measured, and ΔF/F was calculated. Sibling larvae that did not express PACs were used as controls. Three trials for two PAC-expressing (green) and two control (black) larvae were analyzed, and the data from a total of six trials are plotted on graphs. The linear mixed-effects model was used. Scale bars = 150 μm in (A), 10 μm in insets of (A). *p<0.05, ***p<0.001, ns: not significant. Means and SEMs are indicated.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** The hindbrain of 3-dpf larvae expressing bPAC or OaPAC, and non-expressing sibling control larvae was irradiated with 470 nm light for 500 ms. Six consecutive stimulation trials were analyzed for eight PAC-expressing and eight non-expressing control larvae of each line (48 trials for each condition). Latency was measured as the tail movements observed within 30 s after the onset of light stimulation and plotted in a graph. The number of the tail movements were 32 and 13 for bPAC and the control, and 26 and 13 for OaPAC and the control.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/83975/elife-83975-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** (A) Expression of bPAC-MT or OaPAC-Flag in cardiomyocytes. 4-dpf larvae expressing bPAC-MT or OaPAC-Flag were fixed and stained with anti-Myc or Flag (green), and anti-DsRed (mCherry, magenta) antibodies. (B, C) Heartbeats (HBs) monitored by luminosity (AU), changes (B), and relative HB frequency (C) of bPAC-expressing larvae. The heart area of Tg larvae expressing bPAC was irradiated with light (0.5 mW/mm2) of 470 nm for 5 s at the indicated periods. Similar results were obtained from four Tg larvae. A typical example from one larva is shown in (B), and average HB frequency of the first or second trial showing a typical pattern for the four larvae is shown in (C). The larvae showed induced bradycardia in the third through sixth trials. Scale bar = 100 μm in (A).

## Discussion

### Utility of ChRs GtCCR4 and KnChR

As was reported for GtCCR4-EGFP (Hososhima et al., 2020; Shigemura et al., 2019; Yamauchi et al., 2017), GtCCR4-3.0-EYFP and GtCCR4-MT were more sensitive to light stimuli than CrChR2[T159C]-mCherry in cultured mammalian neuronal cells (Figure 1). However, the optogenetic ability of GtCCR4-3.0-EYFP and CrChR2[T159C]-mCherry to induce tail movements in the reticulospinal V2a neurons was comparable (Figure 3A and D), and GtCCR4-3.0-EYFP took longer to initiate tail movements (Figure 3B). There are a couple of explanations for this difference. First, the expression of GtCCR4-3.0-EYFP and CrChR2[T159C]-mCherry proteins might be different. Differences in levels of mRNA expression between Tg lines cannot be ruled out. In addition, there might be differences in translation, cell surface trafficking, and protein stability between these two rhodopsins in zebrafish neurons. GtCCR4-3.0-EYFP contains a membrane-trafficking signal and an ER-export signal that allows expression on the cell surface, but GtCCR4-3.0-EYFP proteins might aggregate slightly within the cytoplasm and might not express efficiently on the cell surface of reticulospinal V2a neurons (Figure 2C). Differences in ion channel properties might also affect their activity in vivo. CrChR2 is permeable to not only Na+ but also H+ and Ca2+, whereas GtCCR4 is relatively specific to Na+ (Nagel et al., 2003; Shigemura et al., 2019). Activation of reticulospinal V2a neurons with CrChR2 induces an influx of Na+, H+, and Ca2+, while activation with GtCCR4 induces only an influx of Na+. This may account for the difference in light-evoked tail movements between GtCCR4 and CrChR2. On the other hand, the Na+-specific channel property of GtCCR4 may favor distinguishing depolarization effects from intracellular Ca2+ signaling. Furthermore, the activation wavelength of GtCCR4 is slightly more red-shifted than that of CrChR2 (Figure 1D; Hososhima et al., 2020; Nagel et al., 2003; Shigemura et al., 2019), which might be useful when used in conjunction with short-wavelength optogenetic tools or neural activation sensors.

We found that KnChR was a more potent optogenetic tool than GtCCR4, CrChR2, and ChrimsonR in zebrafish reticulospinal V2a neurons. Optogenetic activity of KnChR was comparable to that of CoChR in both reticulospinal V2a neurons and cardiomyocytes (Figures 1, 3 and 5). Truncation of KnChR prolonged the channel open lifetime by more than 10-fold (Tashiro et al., 2021; Figure 1). KnChR conducts various monovalent and bivalent cations, including H+, Na+, and Ca2+, while KnChR has a higher permeability to Na+ and Ca2+ and a higher permeability ratio of Ca2+ to Na+ than CrChR2 (Tashiro et al., 2021). These properties may contribute to the high photo-inducible activity of KnChR. Activation of KnChR may induce the influx of more cations with a longer channel open time than CrChR2 and ChrimsonR, leading to stronger cell depolarization. The optogenetic activity of KnChR was comparable to that of GtCCR4 in cultured cells, but higher than that of GtCCR4 in zebrafish reticulospinal V2a neurons and cardiomyocytes. While the exact reason is unclear, it is possible that the expression of functional KnChR protein may be high in zebrafish cells. Furthermore, since KnChR can be activated by light with a short wavelength (maximal sensitivity between 430 and 460 nm), KnChR can be used in conjunction with other red-shifted optogenetic tools and cell activity sensors.

The photoactivation of both cation (GtCCR4, KnChR) and anion (GtACR1) ChRs induced cardiac arrest (Figures 4 and 5). However, activation of KnChR and GtACR1 increased and decreased intracellular Ca2+ in cardiomyocytes, respectively (Figure 5). Since Ca2+ is a readout of depolarization in cardiomyocytes, these data suggest that activation of the cation ChRs depolarized cardiomyocytes, increased intracellular Ca2+ concentration, and inhibited cardiac resumption. Alternatively, cardiac arrest can potentially be explained by a phenomenon known as depolarization block, in which action potentials cannot be generated because the cells remain in a depolarized state. In contrast, activation with the anion ChR hyperpolarized cardiomyocytes, decreased intracellular Ca2+ concentration, and inhibited cardiac contraction. Tg larvae with a high expression of KnChR-3.0-EYFP in the heart always showed cardiac arrest after light stimulation (Figures 4 and 5). This finding indicates that KnChR is a strong tool. By altering the degree of depolarization by KnChR by changing the expression level or the intensity of light stimulation, the function of cardiomyocytes and other cells may be precisely controlled. Highly sensitive KnChR has the potential to identify neural circuits that have not been previously identifiable with other optogenetic tools.

In this study, we demonstrated that GtCCR4, KnChR, and CrChR2 function in both reticulospinal V2a neurons and cardiomyocytes in zebrafish. Given the different ion-channel properties of GtCCR4, KnChR, and CrChR2, they can be used for optogenetic manipulation of cell activities in a variety of applications in zebrafish.

### Utility of enzyme rhodopsin BeGC1 and bacterial flavoprotein PACs

cAMP and cGMP are major second messengers that regulate multiple biological functions in a variety of tissues. We expressed BeGC1 and bPAC/OaPAC to manipulate intracellular cGMP and cAMP signaling in reticulospinal V2a neurons and cardiomyocytes (Figures 6 and 7, Figure 7—figure supplements 1 and 2). Light stimulation of the V2a neuron with BeGC1 as well as bPAC/OaPAC induced tail movements with a longer delay than when stimulated with ChRs. There are two possible mechanisms by which cyclic nucleotides control cell excitability. One mechanism is through cyclic nucleotide-gated ion (CNG) channels, in which binding of cGMP or cAMP to CNG channels opens the cation channels and depolarizes the cell (Bradley et al., 2005; Matulef and Zagotta, 2003). The other is through cAMP-dependent protein kinase (PKA), in which binding of cAMP to the regulatory unit of PKA releases the catalytic unit of PKA, resulting in phosphorylation of cation channels such as the voltage-dependent Ca2+ channel CaV1.2 (Fu et al., 2014; McDonald et al., 1994; Reuter, 1983). The former mechanism is often used for various sensory systems in the nervous system and the latter for the sympathetic noradrenergic regulation of HBs. Which mechanism is used may depend on the availability of necessary components to activate these mechanisms. It is likely that the CNG-mediated mechanism is involved in the activation of reticulospinal V2a neurons. In this mechanism, neurons are not activated until the intracellular cGMP/cAMP concentration reaches the threshold for CNG activation. Consistent with this, activation with BeGC1 and PACs induced neural activation with a relatively long delay (Figures 6 and 7). On the other hand, the PKA-mediated pathway may be involved in the heart. Activation of bPAC – but not BeGC1 or OaPAC – in the heart induced bradycardia (Figure 7—figure supplement 2). A prolonged increase in intracellular Ca2+ induced by PKA-mediated phosphorylation of the Ca2+ channel might contribute to the long-lasting bradycardia. Different effects of bPAC and OaPAC activation on neurons and the heart are due to differences in basal and photo-inducible activity of these two PACs (Ohki et al., 2016). Further analysis is required to reveal the precise mechanism for optogenetic control of cell functions with BeGC1 and bPAC/OaPAC. A two-component system comprising bPAC and the prokaryotic CNG potassium channel (PAC-K) silenced the activity of zebrafish neurons (Bernal Sierra et al., 2018). In combination with endogenous CNG or exogenous CNG K+ channel, PAC can be used to both activate and inhibit zebrafish neurons.

Optogenetic control of intracellular cAMP and cGMP concentrations has been achieved in cells and tissues in which the role of cAMP and cGMP is well understood, as described previously (Gutierrez-Triana et al., 2015). In this study, we focused our analysis on hindbrain reticulospinal V2a neurons and cardiomyocytes, partly as a comparison with ChRs. In the future, expression of these tools in various types of cells and examination of their activity will reveal their usefulness in regulating intracellular cAMP and cGMP levels.

Cell and tissue functions are regulated by various intercellular signaling molecules, such as neurotransmitters, hormones, and cytokines. We demonstrated the usefulness of multiple types of ChRs, cGMP/cAMP-producing tools (in this study), and of G-protein-coupled rhodopsins (in the accompanying paper, Hagio et al., 2023) in manipulating zebrafish neuronal and cardiomyocyte function. Optogenetic studies with these tools alone or in combination will elucidate detailed mechanisms of cellular and tissue regulation.

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
      <td>Gene(Guillardia theta)</td>
      <td>GtCCR4</td>
      <td>Yamauchi et al., 2017</td>
      <td>GenBank: MF039475.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene(Klebsormidium nitens)</td>
      <td>KnChR</td>
      <td>Tashiro et al., 2021</td>
      <td>GenBank: DF236986.1, GAQ79757.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene(Chlamydomonas reinhardtii)</td>
      <td>CrChR2[T159C]</td>
      <td>Berndt et al., 2011</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene(Chloromonas oogama)</td>
      <td>CoChR</td>
      <td>Klapoetke et al., 2014</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene(Chlamydomonas noctigama)</td>
      <td>ChrimsonR</td>
      <td>Klapoetke et al., 2014</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene(Blastocladiella emersonii)</td>
      <td>BeGC1</td>
      <td>Scheib et al., 2015</td>
      <td>GenBank: KP731361.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene(G. theta)</td>
      <td>GtACR1</td>
      <td>Govorunova et al., 2015</td>
      <td>GenBank: KP171708.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene(Beggiatoa sp.)</td>
      <td>bPAC</td>
      <td>Stierl et al., 2011</td>
      <td>GenBank: GU461306.2</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene(Oscillatoria acuminata)</td>
      <td>OaPAC</td>
      <td>Ohki et al., 2016</td>
      <td>GenPept: WP_015149803.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Danio rerio)</td>
      <td>mitfaw2/w2</td>
      <td>Lister et al., 1999</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>TgBAC(vsx2:GAL4FF)</td>
      <td>Kimura et al., 2013</td>
      <td>TgBAC(vsx2:GAL4FF) nns18Tg</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(myl7:GAL4FF)</td>
      <td>Accompanying paper</td>
      <td>Tg(myl7:GAL4FF)nub38Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:GtCCR4-3.0-EYFP)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:GtCCR4-3.0-EYFP, myl7:mCherry)nub49Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS:CoChR-tdTomato)</td>
      <td>This paper</td>
      <td>Tg(14xUAS-E1b:CoChR-tdTomato)nub120Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:ChrimsonR-tdTomato)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:ChrimsonR, myl7:mCherry)nub119Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:GtCCR4-MT-P2A-TagCFP)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:GtCCR4-MT-P2A-TagCFP, myl7:mCherry)nub50Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:KnChR-3.0-EYFP)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:KnChR-3.0-EYFP, myl7:mCherry)nub51Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:CrChR2[T159C]-mCherry)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:CrChR2[T159C]-mCherry, myl7:mCherry)nub52Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:GtACR1-EYFP)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:GtACR1-EYFP, myl7:mCherry)nub53Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS:CoChR-tdTomato)</td>
      <td>This paper</td>
      <td>Tg(14xUAS-E1b:CoChR-tdTomato)nub120Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:ChrimsonR-tdTomato)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:ChrimsonR-tdTomato)nub119Tg</td>
      <td>Available from M. Hibi Lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:BeGC1-EGFP)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:BeGC1-EGFP, myl7:mCherry)nub54Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:bPAC-MT-T2A-tDimer)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:bPAC-MT-T2A-tDimer, myl7:mCherry)nub55Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:OaPAC-Flag-P2A-TagCFP)</td>
      <td>This paper</td>
      <td>Tg(5xUAS-hsp70l:OaPAC-Flag-P2A-TagCFP, myl7:mCherry)nub56Tg</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(UAS-hsp70l:GCaMP6s)</td>
      <td>Muto et al., 2017</td>
      <td>Tg(5xUAS-hsp70l:GCaMP6s) nkUAShspzGCaMP6s13aTg</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(elavl3:Flamindo2)</td>
      <td>This paper</td>
      <td>Tg(elavl3:Flamindo2)nub57TG</td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Cell line(hybrid of Rattus norvegicus and Mus musculus)</td>
      <td>ND7/23</td>
      <td>Wood et al., 1990</td>
      <td>ECACC 92090903</td>
      <td>https://www.saibou.jp/en/reagents/</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCS2+GtCCR4-3.0-EYFP</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCS2+GtCCR4-MT-P2A-TagCFP</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCS2+CrChR2[T159C]-mCherry</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pBH-R1-R2</td>
      <td>Accompanying paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pENTR L1-5xUAS-hsp70l-R5</td>
      <td>Accompanying paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pENTR L5-GtCCR4-MT-P2A-TagCFP-SV40pAS-L2</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pENTR L5-KnChR-3.0-EYFP-SV40pAS -L2</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pENTR L5-GtACR1-EYFP-SV40pAS-L2</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pENTR L5-CrChR2[T159C]-mCherry-SV40pAS-L2</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pENTR L5-BeGC1-EGFP-SV40pAS-L2</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pENTR L5-BeGC1-EGFP-SV40pAS-L2</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pENTR L5-bPAC-MT-T2A-tDimer-SV40pAS-L2</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pENTR L5-OaPAC-Flag-P2A-TagCFP-SV40pAS-L2</td>
      <td>This paper</td>
      <td></td>
      <td>Available from M. Hibi lab</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Flag antibody</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# F3165; RRID:AB_259529</td>
      <td>Dilution 1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Myc tag antibody</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat# sc-40; RRID:AB_627268</td>
      <td>Dilution 1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal anti-GFP antibody</td>
      <td>Nacalai Tesque, Inc.</td>
      <td>Cat# 04404-84; RRID:AB_10013361</td>
      <td>Dilution 1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-DsRed antibody</td>
      <td>Takara Bio</td>
      <td>Cat# 632496; RRID:AB_10013483</td>
      <td>Dilution 1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat CF488A anti-mouse IgG antibody</td>
      <td>Biotium, Inc</td>
      <td>Cat# 20018; RRID:AB_10557263</td>
      <td>Dilution 1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat CF488A anti-rat IgG antibody</td>
      <td>Biotium, Inc</td>
      <td>Cat# 20023; RRID: AB_10557403</td>
      <td>Dilution 1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat CF568 anti-rabbit IgG antibody</td>
      <td>Biotium, Inc</td>
      <td>Cat# 20103; RRID:AB_10558012</td>
      <td>Dilution 1:500</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>tricaine methanesulfonate</td>
      <td>Nacalai Tesque, Inc</td>
      <td>Cat# 01916-32</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>low gelling temperature Type VII-A</td>
      <td>Sigma-Aldrich</td>
      <td>A0701</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>pentylenetetrazol</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# P6500</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SutterPatch 1.1.1</td>
      <td>Sutter Instrument Co.</td>
      <td></td>
      <td>https://www.sutter.com/AMPLIFIERS/SutterPatch.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pCLAMP10.6</td>
      <td>Molecular Devices</td>
      <td></td>
      <td>https://support.moleculardevices.com/s/article/Axon-pCLAMP-10-Electrophysiology-Data-Acquisition-Analysis-Software-Download-Page</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PolyScan2</td>
      <td>Mightex</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>StreamPix7</td>
      <td>NorPix Inc</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LabVIEW</td>
      <td>National Instruments</td>
      <td>2015</td>
      <td>https://www.ni.com/ja-jp.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism5</td>
      <td>GraphPad Software</td>
      <td></td>
      <td>https://www.mdf-soft.com/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>VSDC Free Video Editor 6.4.7.155</td>
      <td>FLASH-INTEGRO LLC</td>
      <td></td>
      <td>https://www.videosoftdev.com/jp</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Microsoft Movies &amp; TV</td>
      <td>Microsoft Corp.</td>
      <td></td>
      <td>https://apps.microsoft.com/store/detail/movies-tv/9WZDNCRFJ3P2</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>QuickTime player 10.5</td>
      <td>Apple Inc.</td>
      <td></td>
      <td>https://quicktime.softonic.jp/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji/ImageJ</td>
      <td>National Institutes of Health (NIH)</td>
      <td></td>
      <td>http://fiji.sc/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R 3.6.1 and 4.2.1</td>
      <td></td>
      <td></td>
      <td>https://www.r-project.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ggplot2 3.2.0 of R</td>
      <td></td>
      <td></td>
      <td>https://ggplot2.tidyverse.org</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>nlme 3.1–162 of R</td>
      <td></td>
      <td></td>
      <td>https://cran.r-project.org/web/packages/nlme/index.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Bonsai</td>
      <td>Lopes et al., 2015</td>
      <td></td>
      <td>https://open-ephys.org/bonsai</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Python 3.5.6</td>
      <td>Python Software Foundation</td>
      <td></td>
      <td>https://www.python.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Tracker Video Analysis and Modeling Tool for Physics Education 5.1.5</td>
      <td></td>
      <td></td>
      <td>https://physlets.org/tracker/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Microsoft Excel for Mac, ver. 16.74</td>
      <td>Microsoft</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HB_frequency.py</td>
      <td>This paper</td>
      <td></td>
      <td>Source code file</td>
    </tr>
  </tbody>
</table>

### Cell culture

The electrophysiological assays of ChRs were performed on ND7/23cells, which are a hybrid cell line derived from neonatal rat dorsal root ganglia neurons fused with mouse neuroblastoma (Wood et al., 1990). ND7/23 cells were obtained from DS Pharma Biomedica, Osaka, Japan, and KAC Co. Ltd., Kyoto Japan. ND7/23 cells were grown on a collagen-coated coverslip in Dulbecco’s modified Eagle’s medium (Fujifilm Wako Pure Chemical Corp., Osaka, Japan) supplemented with 2.5 μM all-trans retinal, 5% fetal bovine serum under a 5% CO2 atmosphere at 37°C. ND7/23 cells have been confirmed to be free from mycoplasma contamination, and their identity has been verified through careful morphological observation. The expression plasmids were constructed based on pCS2+ (see the ‘Zebrafish’ section) and were transiently transfected by using FuGENE HD (Promega, Madison, WI) according to the manufacturer’s instructions. Electrophysiological recordings were then conducted 16–36 hr after transfection. Successfully transfected cells were identified by EYFP, CFP, mCherry, or tdTomato fluorescence under a microscope prior to measurements.

### Electrophysiology

All experiments were carried out at room temperature (25 ± 2°C). Photocurrents were recorded using an amplifier IPA (Sutter Instrument, Novato, CA) or Axopatch 200B amplifier (Molecular Devices, Sunnyvale, CA) under a whole-cell patch-clamp configuration. Data were filtered at 5 kHz and sampled at 10 kHz, then stored in a computer (IPA and SutterPatch, Sutter Instrument or Digdata1550 and pCLAMP10.6, Molecular Devices). The standard internal pipette solution for whole-cell voltage-clamp contained (in mM) 125 K-gluconate, 10 NaCl, 0.2 EGTA, 10 HEPES, 1 MgCl2, 3 MgATP, 0.3 Na2GTP, 10 Na2-phosphocreatine, and 0.1 leupeptin, adjusted to pH 7.4 with KOH. The standard extracellular solution contained (in mM) 138 NaCl, 3 KCl, 10 HEPES, 4 NaOH, 2 CaCl2, 1 MgCl2, and 11 glucose, adjusted to pH 7.4 with KOH. Time constants were determined by a single exponential fit unless noted otherwise.

### Optics for cultured cells

For the whole-cell patch clamp, irradiation at 385, 423, 469, 511, 555, 590, or 631 nm was carried out using Colibri7 (Carl Zeiss, Oberkochen, Germany) controlled by computer software (SutterPatch Software version 1.1.1, Sutter Instrument or pCLAMP10.6, Molecular Devices). Light power was directly measured under an objective lens of the microscope by a visible light-sensing thermopile (MIR-100Q, SSC Inc, Mie, Japan).

### Zebrafish

All Tg zebrafish lines in this study were generated using the mitfaw2/w2 mutant (also known as nacre) line, which lacks melanophores (Lister et al., 1999). To construct expression plasmids for GtCCR4, the cDNA of a fusion protein GtCCR4-3.0-EYFP or the open-reading frame (ORF) of GtCCR4 with a MycTag (MT) tag sequence, the 2A peptide sequence (P2A) from porcine teschovirus (PTV-1) (Provost et al., 2007; Tanabe et al., 2010), and TagCFP (Evrogen, Moscow, Russia) (GtCCR4-MT-P2A-TagCFP) were subcloned to pCS2+. GtCCR4-3.0-EYFP, which contains a membrane-trafficking signal and the ER-export signal (3.0) from the Kir2.1 potassium channel (Gradinaru et al., 2010; Hoque et al., 2016), was constructed according to a previously described procedure (Hoque et al., 2016). To construct KnChR expression plasmids, a carboxy terminal-truncated version (amino acids 1–272 were used), fused with the membrane- and ER-export signals and EYFP, was used (Tashiro et al., 2021). The KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, ChrimsonR-tdTomato, GtACR1-EYFP, BeGC1-EGFP, OaPAC, and bPAC-MT-T2A (2A sequence from Thosea asigna virus) DNA fragments were isolated by PCR from phKnChhR-272–3.0-eYFP (Tashiro et al., 2021), pmCherry ChR2 T159C (Berndt et al., 2011), pTol1-UAS:ChrimsonR-tdTomato (Antinucci et al., 2020), pFUGW-hGtACR1-EYFP (Govorunova et al., 2015) (a gift from John Spudich [RRID:ADDgene_67795]), peGFP-N1-BeGC1 (Matsubara et al., 2021), pCold His OaPAC (Ohki et al., 2016) (a gift from Sam-Yong Park), and pAAV hSyn1 bPAC cMyc T2A tDimer (a gift from Thomas Oertner [RRID:Addgene_85397]), respectively, and were subcloned to pCS2+ (for OaPAC, Flag-P2A-TagCFP was attached at the carboxy-terminal). pENTR L1-R5 entry vectors containing five repeats of the upstream activation sequence (UAS) and the hsp70l promoter (Muto et al., 2017), and pENTR L5-L2 vectors containing the ORF of the optogenetic tools and the polyadenylation site of SV40 (SV40pAS) from the pCS2+ plasmids were generated by the BP reaction of the Gateway system. The UAS-hsp70l promoter and optogenetic tool expression cassettes were subcloned to the Tol2 donor vector pBleeding Heart (pBH)-R1-R2 (Dohaku et al., 2019), which was modified from pBH-R4-R2 and contains the mCherry cDNA and SV40 pAS under the myosin, light chain 7, regulatory (myl7) promoter (van Ham et al., 2010) by the LR reaction of the Gateway system. For expression of CoChR-tdTomato, pTol1-UAS:CoChR-tdTomato (Antinucci et al., 2020) was used. To make a Tol2 plasmid expressing the cAMP fluorescent indicator Flamindo2 in all postmitotic neurons, the elavl3 promoter (Park et al., 2000), Flamindo2 cDNA (Odaka et al., 2014), and SV40pAS were subcloned to pT2ALR-Dest (pT2ALR-elavl3-Flamindo2). To make Tg fish, 25 pg of the Tol1 or Tol2 plasmids and 25 pg of Tol1 or Tol2 transposase capped and polyadenylated RNA were injected into one-cell-stage embryos. The Tg fish that expressed optogenetic tools in a Gal4-dependent manner are referred as to Tg(UAS:opto-tool). Tg(UAS:opto-tool) fish were crossed with TgBAC(vsx2:GAL4FF) (Kimura et al., 2013), Tg(myl7:GAL4FF), or Tg(elavl3:GAL4-VP16) (Kimura et al., 2013) to express tools in the hindbrain reticulospinal V2a neurons, heart, and all postmitotic neurons, respectively. For Ca2+ imaging and cAMP monitoring, Tg(5xUAS-hsp70l:GCaMP6s) (Muto et al., 2017) and Tg(elavl3:Flamindo2) were used. Adult zebrafish were raised at 28.5°C with a 14 hr light and 10 hr dark cycle. Individual larvae used for behavioral experiments were kept in the dark except for the fluorescence observation and light exposure experiments.

### Immunostaining

For immunostaining, anti-Flag antibody (1:500, mouse, Sigma-Aldrich, St. Louis, MO, Cat# F3165, RRID:AB_259529), anti-Myc Tag (MT) antibody (1:500, mouse, Santa Cruz Biotechnology, Dallas, TX, Cat# sc-40, RRID:AB_627268), anti-GFP (1:500, rat, Nacalai Tesque, Inc, Kyoto, Japan, Code: 04404-84, RRID:AB_10013361), and anti-DsRed (1:500, rabbit, Takara Bio, Shiga, Japan, Cat# 632496; RRID:AB_10013483) were used as primary antibodies. CF488A anti-mouse IgG (1:500, H+L, Biotium Inc, Fremont, CA, Cat# 20018; RRID:AB_10557263), CF488A anti-rat IgG (1:500, H+L, Biotium, Inc, Cat# 20023; RRID:AB_10557403), and CF568 anti-rabbit IgG (1:500, H+L, Biotium Inc, Cat# 20103; RRID:AB_10558012) were used as secondary antibodies. The detailed method for immunostaining is described in the accompanying paper. Images were acquired using a confocal laser inverted microscope LSM700 (Carl Zeiss). To detect weak fluorescent signals, laser power was increased, but when the power was increased by a factor of 2 or more, it was noted in the figure legend (Figure 7A).

### Locomotion assay

The expression of optogenetic tools in 3-dpf larvae was determined by the expression of fluorescent marker in reticulospinal V2a neurons. Sibling fish that did not express the fluorescent marker were used as control fish. The detailed method is described in the accompanying paper. Briefly, after larvae were anesthetized with tricaine methansulfonate (Nacalai Tesque, Inc, Cat# 01916-32) and embedded in 2.5% agarose (low gelling temperature Type VII-A A0701, Sigma-Aldrich), the tail was set free by cutting the agarose around it. This agarose was placed in a 90 mm Petri dish filled with rearing water and kept for 20 min to recover from anesthesia. Light stimulation was performed using a patterned LED illuminator system LEOPARD (OPTO-LINE, Inc, Saitama, Japan) and the control software PolyScan2 (Mightex, Toronto, Canada) was used. The irradiation intensity and area were 0.4 mW/mm2 and 0.30 mm × 0.34 mm. Tail movements were captured by an infrared CMOS camera (67 fps, GZL-CL-41C6M-C, Teledyne FLIR LLC, Wilsonville) mounted under the stage and StreamPix7 software (NorPix Inc, Montreal, Canada) and analyzed by Tracker Video Analysis and Modeling Tool for Physics Education version 5.1.5. The timing of tail motion capture and light irradiation to the reticulospinal V2a neurons was controlled by a USB DAQ device (USB-6008, National Instruments, Austin, TX) and the programming software LabVIEW (2015, National Instruments). The stimulation was repeated six times every 10 or 20 min, 100 ms (ChRs) or 500 ms (BeGC1 and adenylyl cyclases) each time, with a minimum of eight individuals for each strain. Trials in which swimming behavior was induced within 8 s after light stimulation were defined as induced trials. The percentage of induced trials was defined as locomotion rate, excluding trials in which swimming behavior was elicited before light stimulation. The time from the start of light irradiation to the first tail movement was defined as latency, and the time from the start of the first tail movement to the end of that movement was defined as duration. The maximum distance the tail moved from the midline divided by body length was defined as strength. To examine the tools’ ability to inhibit locomotion, 4-dpf Tg larvae were pretreated with 15 mM pentylenetetrazol (Sigma-Aldrich, Cat# P6500) and spontaneous tail movements were induced by white LED light (peak 640  nm; Kingbright Electronic Co., Ltd., New Taipei City, Taiwan) powered by a DC power supply (E3631A; Agilent Technologies, Santa Clara, CA) for 5 s. After 500 ms from the onset of the white LED light, the hindbrain reticulospinal V2a neurons were stimulated with the patterned LED illuminator. Trials in which swimming behavior stopped within 1 s after white light stimulation were defined as locomotion-inhibition trials. The percentage of locomotion-inhibition trials was calculated; these values are indicated in Table 1. Graphs were created with GraphPad Prism5 software (GraphPad Software, San Diego, CA). We used VSDC Free Video Editor version 6.4.7.155 (FLASH-INTEGRO LLC, Moscow, Russia) and Microsoft Movies & TV (Microsoft Corp., Redmond, WA) to make all movies.

### Heartbeat experiments

4-dpf larvae carrying an expressed fluorescent marker in the heart were used for the experiments. Sibling fish that did not express the marker were used as control fish. Four larvae were used for each line. The detailed method is described in the accompanying paper. Briefly, after larvae were quickly anesthetized with about 0.2% tricaine methanesulfonate and embedded in agarose, they were placed in a 90 mm Petri dish filled with water and kept for 20 min to recover from anesthesia. Irradiation intensity was adjusted to 0.5 mW/mm2. The area of irradiation was 0.17 mm × 0.25 mm, including the entire heart. The heart area in Tg fish was irradiated for 100 ms (ChRs) or 5 s (bPAC-MT) with light wavelengths that had the closest values to the maximum absorption wavelength of each optogenetic tool, as shown in Table 1. The HBs of larvae were captured by an infrared CMOS camera (67 fps) and recorded with StreamPix7 software, as described above. The irradiation trial was repeated six times every 3 min (for GtCCR4-3.0-EYFP and GtACR1-EYFP) or 10 min (for KnChR-3.0-EYFP, CrChR2[T159C]-mCherry, CoChR-tdTomato, ChrimsonR-tdTomato, and bPAC-MT) for one fish and a total of four larvae were analyzed for each strain. The video recordings of the HBs were observed using QuickTime player 10.5 (Apple Inc, Cupertino, CA). After opening videos with Fiji/ImageJ (National Institutes of Health, Bethesda, MD), the entire heart was set as the region of interest (ROI), and the luminosity (AU: arbitrary units) data in the ROI was used to create graphs of HBs using ggplot2 version 3.2.0 in R. To calculate relative HB frequency, temporal changes in luminosity were obtained from the video using Bosai (Lopes et al., 2015) and the frames where HBs occurred were identified by the code (HB_frequency.py) created in Python version 3.5.6 (Python Software Foundation, Wilmington, DE). Relative HB frequency was calculated from the HB frame data, 500 ms before and after each time point using Excel (Microsoft). Graphs of the average relative HB frequency were created by ggplot2 of R. The latency to cardiac arrest and the time to first resumption of HBs were also measured. Graphs were created with GraphPad Prism5 software. All movies were created with VSDC Free Video Editor. Simple HB experiments were also performed using a light source equipped with an MZ16 FA microscope and GFP (460–500 nm), YFP (490–510 nm), and DSR filters (530–560 nm, Leica, Wetzlar, Germany), as indicated in Table 1.

### Ca2+ imaging

4-dpf Tg fish expressing KnChR or GtACR1, and GCaMP6s in cardiomyocytes were used. Tg fish expressing only GCaMP6s were used as controls. The larvae anesthetized with tricaine methanesulfonate were embedded in 3% agarose (low-gelling temperature Type VII-A, Sigma-Aldrich) in 1/10 Evans solution, placed in a 90 mm Petri dish filled with water, and left on the microscope stage for 10 min. A 130 W light source (U-HGLGPS, Olympus, Tokyo, Japan) with a fluorescence detection filter (excitation 470–495 nm, emission 510–550 nm, U-MNIBA3, Olympus) was used to observe the fluorescence of GCaMP6s. A CCD camera (ORCA-R2, Hamamatsu Photonics, Shizuoka, Japan) located on the microscope was used to capture the GCaMP6s fluorescence images at 9 fps. After image acquisition, the entire heart area was manually set as the ROI using Fiji/ImageJ, and fluorescence intensity was measured. Trials were repeated three times every 10 min. The relative change in ΔF/F was calculated by dividing the fluorescence intensity in each frame by the fluorescence intensity at the start of light exposure.

### cAMP live imaging

3-dpf larvae expressing an optogenetic tool and the cAMP indicator Flamindo2 in postmitotic neurons were used. Sibling larvae that did not express the optogenetic tool were used as controls. The larvae that were quickly anesthetized with 0.04% tricaine methanesulfonate were embedded in 3% agarose, placed in a 90 mm Petri dish filled with rearing water, and left on the microscope stage for 20 min. A 130 W light source (U-HGLGPS, Olympus) with a fluorescence detection filter (excitation 470–495 nm, emission 510–550 nm) was used for observation. The fluorescence images were captured by a CCD camera (ORCA-R2, Hamamatsu Photonics) at 9 fps. After image acquisition, the entire optic tectum area was set as a ROI using Fiji/ImageJ and fluorescence intensity was measured. ΔF/F was calculated.

### Statistical analysis

Data were analyzed using R software package (versions 3.6.1 and 4.2.1). Statistical tests were applied as indicated in figure legends. All data in the text and figures are expressed as the mean ± standard error of the mean (SEM). A linear mixed-effects model was applied using R package ‘nlme’ version 1.3–162.
