# NaV1.1 is essential for proprioceptive signaling and motor behaviors

## Authors

- Cyrrus M Espino<sup>1</sup> ([ORCID: 0000-0003-2708-4577](https://orcid.org/0000-0003-2708-4577))
- Cheyanne M Lewis<sup>1</sup> ([ORCID: 0000-0002-0057-2047](https://orcid.org/0000-0002-0057-2047))
- Serena Ortiz<sup>2</sup>
- Miloni S Dalal<sup>3</sup>
- Snigdha Garlapalli<sup>4</sup>
- Kaylee M Wells<sup>5</sup>
- Darik A O'Neil<sup>5</sup>
- Katherine A Wilkinson<sup>2</sup> ([ORCID: 0000-0002-2692-5533](https://orcid.org/0000-0002-2692-5533))
- Theanne N Griffith<sup>1</sup> ([ORCID: 0000-0003-0090-6286](https://orcid.org/0000-0003-0090-6286)) †

### Affiliations

1. Department of Physiology and Membrane Biology, University of California, Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))
2. Department of Biological Science, San Jose State University San Jose United States ([ROR:04qyvz380](https://ror.org/04qyvz380))
3. Department of Pharmacology, Physiology, and Neuroscience, New Jersey Medical School, Rutgers University Newark United States ([ROR:05vt9qd57](https://ror.org/05vt9qd57))
4. Undergraduate Program in Psychology, University of California, Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))
5. Neurobiology Course, Marine Biological Laboratory Woods Hole United States ([ROR:046dg4z72](https://ror.org/046dg4z72))

† Corresponding author

## Abstract

The voltage-gated sodium channel (NaV), NaV1.1, is well-studied in the central nervous system; conversely, its contribution to peripheral sensory neuron function is more enigmatic. Here, we identify a new role for NaV1.1 in mammalian proprioception. RNAscope analysis and in vitro patch-clamp recordings in genetically identified mouse proprioceptors show ubiquitous channel expression and significant contributions to intrinsic excitability. Notably, genetic deletion of NaV1.1 in sensory neurons caused profound and visible motor coordination deficits in conditional knockout mice of both sexes, similar to conditional Piezo2-knockout animals, suggesting that this channel is a major contributor to sensory proprioceptive transmission. Ex vivo muscle afferent recordings from conditional knockout mice found that loss of NaV1.1 leads to inconsistent and unreliable proprioceptor firing characterized by action potential failures during static muscle stretch; conversely, afferent responses to dynamic vibrations were unaffected. This suggests that while a combination of Piezo2 and other NaV isoforms is sufficient to elicit activity in response to transient stimuli, NaV1.1 is required for transmission of receptor potentials generated during sustained muscle stretch. Impressively, recordings from afferents of heterozygous conditional knockout animals were similarly impaired, and heterozygous conditional knockout mice also exhibited motor behavioral deficits. Thus, NaV1.1 haploinsufficiency in sensory neurons impairs both proprioceptor function and motor behaviors. Importantly, human patients harboring NaV1.1 loss-of-function mutations often present with motor delays and ataxia; therefore, our data suggest that sensory neuron dysfunction contributes to the clinical manifestations of neurological disorders in which NaV1.1 function is compromised. Collectively, we present the first evidence that NaV1.1 is essential for mammalian proprioceptive signaling and behaviors.

## Introduction

Voltage-gated sodium channels (NaVs) are critical mediators of neuronal excitability and are responsible for action potential generation and propagation (Ahern et al., 2016; Bean, 2007). In the mammalian nervous system, there are nine isoforms (NaV1.1–1.9), each with unique biophysical properties, as well as distinguishing cellular expression and subcellular localization patterns (Bennett et al., 2019; Catterall, 2017). Of these different subtypes, NaV1.1 is notable for its role in brain disease (Escayg and Goldin, 2010; Mulley et al., 2005; Ogiwara et al., 2007). Indeed, Scn1a, the gene that encodes NaV1.1, is referred to as a ‘super culprit’ gene, with over 1000 associated mutations that lead to abnormal brain function, resulting in brain disorders such as epilepsy and migraine, as well as neurodivergent phenotypes, such as autism spectrum disorder (Ding et al., 2021; Lossin, 2009). Homozygous Scn1a-/- global knockout mice are ataxic and die by postnatal day (P) 15, while heterozygous Scn1a+/- animals develop seizures and begin to die sporadically starting at P21 (Yu et al., 2006). In addition to the central nervous system (CNS), NaV1.1 is also expressed in the peripheral nervous system (PNS) (Sharma et al., 2020; Usoskin et al., 2015); yet, the prominent role this channel plays in brain function has left its physiological roles in sensory neuron populations understudied.

Peripheral sensory neurons of the dorsal root ganglia (DRG) and trigeminal ganglia (TG) are tasked with encoding somatic sensations, such as touch, temperature, pain, and proprioception, and are anatomically and functionally heterogenous (Kupari et al., 2021; Nguyen et al., 2021; Oliver et al., 2021; Wu et al., 2021). Scn1a transcript and protein have been observed primarily in myelinated mechanosensory DRG and TG neurons (Fukuoka et al., 2008; Ho and O’Leary, 2011; Osteen et al., 2016). Indeed, subcutaneous injection of the NaV1.1 activator, Hm1a, into mouse hind paw causes noninflammatory mechanical pain and spontaneous pain behaviors (Osteen et al., 2016). Interestingly, pharmacological inhibition of NaV1.1 does not affect mechanical thresholds in uninjured mice but does reduce mechanical pain in a spared-nerve injury model (Salvatierra et al., 2018), suggesting that NaV1.1 may have a more prominent role in mechanical pain as opposed to normal touch sensing. NaV1.1 in TG neurons has also been reported to mediate mechanical pain in an orbitofacial chronic constriction injury model (Pineda-Farias et al., 2021). In addition to somatosensory neurons, NaV1.1 is found in colon-innervating vagal neurons, where it contributes to firing of colonic mechano-nociceptors and is upregulated in a mouse model of chronic visceral hypersensitivity (Osteen et al., 2016; Salvatierra et al., 2018). Lastly, NaV1.1 contributes to action potential firing in a subset of DRG neurons that express the cold-sensitive ion channel, transient receptor potential melastatin 8 (TRPM8), suggesting that the channel may also contribute to thermosensory transmission (Griffith et al., 2019). While most data support a role for NaV1.1 in pain, the limited number of studies that have investigated NaV1.1 function in sensory neurons has left gaps in our knowledge regarding other potential roles this channel may play in somatosensation.

Given the relatively underexplored role of NaV1.1 in the PNS, we set out to determine what other somatosensory modalities rely on NaV1.1 expression in sensory neurons. Here, we show that 100% of proprioceptors express Scn1a mRNA, where it makes notable contributions to the somal whole-cell sodium current and intrinsic excitability. A functional role for NaV1.1 in proprioceptive signaling was also supported by ex vivo electrophysiological recordings from functionally identified muscle spindle afferents. Importantly, mice lacking NaV1.1 in all sensory neurons display visible and profound motor deficits and ataxic-like behavior, which were quantified in rotarod and open-field assays. Surprisingly, we found that NaV1.1 is haploinsufficient for normal proprioceptor function and behavior, in ex vivo recordings and the open-field assay, respectively. Collectively, our data provide the first evidence that peripherally expressed NaV1.1 is critical for sensory proprioceptive signaling and motor coordination.

## Results

Most studies have localized NaV1.1 expression primarily to myelinated sensory neurons that transmit mechanical signals (Fukuoka et al., 2008; Ho and O’Leary, 2011; Osteen et al., 2016; Wang et al., 2011). In line with prior work, RNAscope analysis of DRG sections from adult mice showed that 93% of myelinated neurons, as determined by neurofilament heavy chain (NFH) labeling, express Scn1a transcripts (Figure 1A). RNA-sequencing datasets have consistently identified NaV1.1 expression in proprioceptors; thus, we next analyzed NaV1.1 expression in these cells using a ParvalbuminCre;Rosa26Ai14 reporter line (PvalbAi14) and found that 100% of genetically identified proprioceptors were positive for Scn1a message (Figure 1B). This contrasted with low expression of Scn1a mRNA in both calcitonin gene-related peptide (CGRP)-expressing neurons, which represent peptidergic nociceptors, and non-peptidergic polymodal Mrgprd-expressing nociceptors (24 and 3%, respectively, Figure 1C and D). Frequency and cumulative distribution plots show the spread of integrated fluorescence density measurements obtained for Scn1a transcripts in proprioceptors (Figure 1E and F).

![Figure 1.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig1-v2.jpg)

**Figure 1.:** (A–D) Representative confocal images of cryoprotected adult dorsal root ganglia (DRG) sections (25 μm) with pie chart quantifications indicating the percentage of Scn1a+ and Scn1a- neurons in each subpopulation (magenta and yellow, respectively). Images were acquired with a ×40, 0.9 NA water-immersion objective. Sections were hybridized using RNAscope with probes targeting Scn1a (Scn1a, magenta) and stained with the following antibodies (yellow): (A) anti-neurofilament heavy (NFH, n = 787), (B) anti-DsRed to label TdTomato+ proprioceptors (n = 153), (C) anti-calcitonin gene-related peptide (CGRP, n = 877), and (D) anti-GFP to label Mrgprd+ neurons (n = 744). DRG from C57BL/6, PvalbCre;Rosa26Ai14, and MrgprdGFP mice of both sexes were used. Scale bar 50 μm. White arrowheads indicate Scn1a+ neurons while white arrows indicate Scn1a- neurons. Frequency (E) and cumulative (F) distribution plots of integrated fluorescence density of the Scn1a signal in TdTomato+ proprioceptors (n = 153). n = cells.

In addition to NaV1.1, NaV1.6 and NaV1.7 expression has also been reported in proprioceptors (Carrasco et al., 2017). As with Scn1a, mRNA for Scn8a and Scn9a is also found in 100% of genetically identified proprioceptors (Figure 2A and B). Cumulative distribution plots of Scn8a and Scn9a integrated fluorescence density measurements showed higher variability as compared to NaV1.1 (Figures 1E and 2C and D). This was quantified using the coefficient of variation (CV), a relative measure of the extent of variations within data. The CV for Scn1a transcript expression was calculated to be 75.6, whereas this value increased to 97.3 and 88.1 for Scn8a and Scn9a, respectively. This indicates that while all three isoforms are ubiquitously expressed in proprioceptors, the relative levels differ, with NaV1.1 having the most consistent level of expression across neurons analyzed. Furthermore, the average integrated density of the NaV1.1 signal for a given proprioceptive DRG neuron was significantly higher than the average integrated densities calculated for both NaV1.6 and NaV1.7 (Figure 2E, p<0.0001).

![Figure 2.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig2-v2.jpg)

**Figure 2.:** (A, B) Representative confocal images of cryoprotected adult dorsal root ganglia (DRG) sections (25 μm) with quantifications indicating the percentage of NaV+ and NaV- neurons in TdTomato+ proprioceptors. Sections were hybridized using RNAscope with probes targeting NaV1.6 or NaV1.7 (Scn8a and Scn9a, respectively, magenta) and stained with anti-DsRed (yellow). (A) Snc8a, n = 298, (B) Scn9a, n = 166. Scale bar set to 50 μm. White arrowheads indicate NaV+ neurons. (C–, D) Frequency distribution plots of integrated fluorescence density of NaV1.6 and NaV1.7 mRNA in TdTomato+ proprioceptors, respectively. (E) The average integrated density of Scn1a, Scn8a, and Scn9a RNAscope probe signal. Dots represent individual cells. Statistical significance was determined using a Kruskal–Wallis test with Dunn’s post-hoc comparisons. (F) Top: experimental workflow of serial pharmacological blockade of NaV channels expressed in proprioceptors. We first elicited a whole-cell sodium current in the absence of drug. We next bath applied 500 nM of ICA 121431 to block current carried by NaV1.1. Subsequently, we bath applied 9-anhydroustetrodoxin (AH-TTX) (300 nM) to block NaV1.6-mediated current, and PF-05089771 (25 nM) to block the NaV1.7-mediated current. Finally, tetrodotoxin (TTX) (300 nM) was used to block residual current and to confirm there was no contribution of TTX-resistant NaVs in proprioceptors. Bottom: representative current traces following application of NaV-selective inhibitors. All drugs were applied for 1 min. (G) Quantification of the average percentage of the whole-cell sodium current that was sensitive to the individual drugs used (n = 8). n = cells. ****p<0.0001.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Representative current trace before (black trace) and after (red trace) application of 0.1% DMSO to TdTomato+ proprioceptors during in vitro electrophysiological experiments. Quantification of current density (B) and current decay kinetics (C) before (normal external solution, black circles) and after DMSO application (red circles). A paired t-test was used to determine statistical significance (B), p=0.0855 and (C), p=0.3125, n = 5 cells.

Due to the ubiquitous expression of NaV1.1, NaV1.6, and NaV1.7 in proprioceptors, we sought to determine the relative contributions of these isoforms to the proprioceptor whole-cell sodium current (INa). We performed in vitro voltage-clamp experiments on TdTomato+ neurons harvested from thoracic spinal levels of adult PvalbAi14 mice (de Nooij et al., 2013) and used serial application of selective NaV channel antagonists to determine the specific contributions of NaV1.1, NaV1.6, and NaV1.7 (Figure 2F). We first applied the selective NaV1.1 antagonist ICA 1214314 (ICA, 500 nM), followed by 9-anhydroustetrodoxin (AH-TTX, 300 nM), which is a selective NaV1.6 blocker but also partially blocks NaV1.1 (Denomme et al., 2020; Griffith et al., 2019). We reasoned that by first blocking the NaV1.1-mediated current, the effect of AH-TTX should largely be due to inhibition of NaV1.6. Finally, we blocked NaV1.7 channels using the antagonist PF-05089771 (25 nM), followed by tetrodotoxin (TTX, 300 nM) to block any residual current, as proprioceptors do not express TTX-resistant NaVs. On average, 7.8% of the current remained unblocked following serial application of these antagonists due to incomplete block by the drugs used. We found that the ICA-sensitive component was 44.8% of INa. Conversely, 14.5 and 32.9% of INa was sensitive to AH-TTX and PF-05089771, respectively (Figure 2G). No significant effect of the 0.1% DMSO vehicle solution on INa amplitude was observed (Figure 2—figure supplement 1). Collectively, these data suggest that in proprioceptors NaV1.1 is a dominant functional NaV subtype.

We next determined the biophysical features of the whole-cell sodium current (INa) in proprioceptors, which has not been previously reported (Figure 3A–D). The current–voltage relationship shows the first detectable current appeared at voltages near –50 mV and was maximal at voltages near –30 mV when evoked from a holding potential of –90 mV (Figure 3B). Voltage dependence of peak conductance was best fit to a single Boltzmann function and the voltage for half-maximal activation was –38.7 mV (Figure 3C). The voltage dependence of inactivation was determined with 40 ms prepulse steps ranging from –120 mV to +10 mV. The midpoint of the inactivation curve was –64.5 mV and was best fit to a single Boltzmann function (Figure 3D). To analyze recovery from fast inactivation, TdTomato+ neurons were depolarized to –20 mV, followed by a series of recovery periods ranging from 0.5 ms to 10 ms before a second test step to –20 mV was given to assess sodium channel availability. INa recovery was rapid (τ = 0.54ms), with greater than 50% of INa recovered after 0.5 ms (Figure 3E). Finally, entry into slow inactivation was determined. Cells were held at 0 mV during conditioning voltage steps ranging from 10 ms to 2000 ms, separated by two 2 ms pulses to –20 mV to compare channel availability before and after the conditioning pulse (Figure 3F). The tau for entry into slow inactivation was 928.6 ms, with more than 50% of channels available after a 2000 ms conditioning pulse.

![Figure 3.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig3-v2.jpg)

**Figure 3.:** (A) Top: representative image of a TdTomato+ proprioceptor in culture during electrophysiological recordings (scale bar set to 50 μm). Bottom: representative current traces from current–voltage relationship of INa from TdTomato+ proprioceptors shown in (B). Currents were elicited by 40 ms voltage steps from –90 mV to +40 mV in 5 mV increments (n = 7–9). (C) Top: the voltage protocol used to measure the voltage dependence of whole-cell sodium current activation in proprioceptors. Currents were elicited using a series of 40 ms voltage steps from –90 mV to 40 mV at 5 mV increments from a holding potential of –90 mV. Bottom: data are expressed as conductance over maximum conductance (n = 6–9). (D) Top: the voltage protocol used to measure the voltage dependence of inactivation. A 40 ms prepulse ranging from –120 mV to +10 mV was given followed by a test pulse to 0 mV. Bottom: data are expressed as current over maximum current (n = 8–12). (E) Left: quantification of recovery from fast inactivation (n = 8). Line shows a monoexponential fit of the data (τ = 0.54 ms). Top right: voltage protocol to measure recovery from fast inactivation. A 20 ms step to –20 mV from –100 mV is followed by varying durations of recovery at –100 mV before a second test step to –20 mV. Bottom right: representative traces of currents elicited before (black trace) and after (gray trace) a 0.5 ms recovery period. (F) Left: quantification of entry into slow inactivation (n = 6). Line shows a monoexponential fit of the data (τ = 928.6 ms). Top right: voltage protocol to measure entry into slow inactivation. A 3 ms test pulse to –20 mV from –100 mV was followed by conditioning pulses at 0 mV for varying durations before a third test step to –20 mV. 12 ms recovery periods after the first test pulse and before the second were included to remove fast inactivation. Bottom right: representative current trace elicited before and after a 2000 ms conditioning pulse. All error bars represent standarad error of the mean (SEM) n = cells.

We next asked how blocking NaV1.1 channels affects proprioceptor function in vitro. Similar to serial pharmacological experiments, INa density in proprioceptors was significantly reduced from ~–140 pA/pF to ~–75 pA/pF following ICA application (Figure 4B, p=0.0003). The proprioceptor INa had an average tau of 0.6 ms, which was significantly slowed to 1.0 ms following application of ICA (Figure 4C, p=0.0007), in line with loss of a fast gating channel. Blocking NaV1.1 did not change INa rise time (Figure 4D, p=0.1611). Quantification of the ICA-sensitive component found an average tau of 0.4 ms and an average current density of –96 pA/pF (Figure 4E). Of note, there was a wide distribution of current densities for the ICA-sensitive component, ranging from ~–28 pA/pF to ~–263 pA/pF, suggesting some variability in the contribution of NaV1.1 to proprioceptor excitability that may be proprioceptor subtype dependent. We next used current-clamp experiments to determine the effect of ICA on proprioceptor intrinsic excitability (Figure 4F). Pharmacological inhibition of NaV1.1 significantly reduced the number of evoked action potentials in most genetically identified proprioceptors (Figure 4G); however, five of the cells recorded had low firing rates that were not inhibited by ICA. This further suggests that NaV1.1 is important for repetitive firing in most proprioceptors, but some subtypes with lower intrinsic excitability instead rely on a combination of NaV1.6 and NaV1.7. Action potential amplitude (Figure 4H, p=0.0420) and action potential threshold (Figure 4I, p=0.0186) were also significantly reduced following ICA application, and action potential full-width half-max was significantly increased following ICA application (Figure 4K, p=0.0068), in line with loss of the fast NaV1.1-mediated current.

![Figure 4.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig4-v2.jpg)

**Figure 4.:** (A) Left: representative whole-cell voltage-clamp traces elicited before (black) and after (magenta) application of ICA 121431 (500 nM). Right: the subtracted ICA-sensitive current shown in black. (B) Quantification of the reduction in whole-cell current density before (white) and after (magenta) ICA, p=0.0003, n = 11 cells. (C) Quantification of rate of current decay before and after ICA, p=0.0007, n = 11 cells. (D) Quantification of whole-cell current rise time before and after ICA, p=0.1611, n = 10 cells. (E) Left: current densities of ICA-sensitive sodium currents (n = 11); right: current decay taus of ICA-sensitive sodium currents (n = 9 cells). (F) Representative whole-cell current-clamp traces before (left) and after (right) application of ICA. (G–J) Quantification of number of action potentials in response to current injection (G; p=0.0002, n = 20 cells), action potential amplitude (H; p=0.0420, n = 20 cells), action potential threshold (I; p=0.0186, n = 20 cells), and full-width half max (J; p=0.0068, n = 20 cells). Gray lines represent paired observations, circles and lines represent means and standard deviations. White circles, before ICA application. Magenta circles, after ICA application. The Wilcoxon matched-pairs signed-rank test was used to determine statistical significance.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Representative whole-cell current trace from a large-diameter DRG neurons (>60 pF) from a Scn1a-cKO mouse. The black trace represents the INa recorded in external solution, and the red trace represents the current following application of 500 nM of ICA 121431 for 1 min. (B) Quantification of the current density before (black circles) and after ICA (red circles, n = 9). A significant effect of ICA was found (paired Student’s t-test, p=0.0041). n = cells.

It is important to note that ICA 121431 also blocks NaV1.3 channels, which could be upregulated in our cultured DRG neuron preparations (Wangzhou et al., 2020). Indeed, a small but significant decrease in INa was observed in recordings from large-diameter DRG neurons harvested from PirtCre;Scn1a-floxed mice (Scn1a-cKO), which lack NaV1.1 in all sensory neurons. Thus, inhibition of upregulated NaV1.3 channels could contribute to the effect of on ICA on the proprioceptor INa(Figure 4—figure supplement 1).

To clarify the importance of NaV1.1 to proprioceptor function and avoid the caveats associated with in vitro pharmacological studies, we took an in vivo approach and analyzed motor behaviors in Scn1a-cKO mice of both sexes. We were precluded from using a Pvalbcre driver line to directly interrogate a role for NaV1.1 in proprioceptors as loss of NaV1.1 in Pvalb-expressing brain interneurons produces an epilepsy phenotype that prevents behavioral analyses in adult animals (Ogiwara et al., 2007). Consistent with in vitro data, Scn1a-cKO animals of both sexes displayed profound and visible motor abnormalities. These abnormalities include ataxic-like tremors when suspended in the air (Video 1), abnormal limb positioning (Videos 2 and 3), and paw clasping, which are absent in Scn1a-floxed littermate controls and heterozygous animals (PirtCre;Scn1afl/+, Scn1a-Het, respectively, Figure 5A). We first ran animals in the open-field test for 10 min each to quantify spontaneous locomotor behaviors (Figure 5B). We found that Scn1a-cKO animals traveled significantly less (Figure 5C) and slower (Figure 5D) than Scn1a-floxed littermate controls (p=0.0077 and p=0.0057, respectively). Surprisingly, Scn1a-Het mice also displayed motor abnormalities in the open-field test, performing similarly to Scn1a-cKO animals (Figure 5B–D), demonstrating NaV1.1 haploinsufficiency in sensory neurons for motor behaviors. No genotype-dependent differences were observed in the amount of time spent moving, suggesting gross motor function was intact (Figure 5E). Additionally, the amount of time spent in the center of the open-field chamber was also independent of genotype (Figure 5F). We next used the rotarod assay to investigate differences in motor coordination. Mice were assayed on three consecutive days and latency to fall and revolutions per minute (RPM) were quantified. Unlike in the open-field assay, both Scn1a-floxed and Scn1a-Het mice performed at similar levels during the 3-day period (Figure 5G and H). Conversely, Scn1a-cKO animals performed significantly worse. By day 3, on average they were only able to maintain their position on the rotarod for 41 s, falling over 50% faster Scn1a-floxed and Scn1a-Het mice. We did not observe any sex-dependent differences in performance in the open-field or rotarod tests (Figure 5—figure supplement 1). We confirmed that our mouse model selectively targeted sensory neurons by crossing a PirtCre driver with a fluorescent reporter line (PirtCre;Rosa26Ai14). We observed little-to-no neuronal expression of TdTomato in both dorsal and ventral spinal cord (Figure 5—figure supplement 2). In contrast, DRG somata and axons showed strong labeling. Collectively, our behavioral data provide evidence for a new in vivo role of NaV1.1 in sensory neurons in mammalian proprioception.

![Video 1.](https://cdn.elifesciences.org/articles/79917/elife-79917-video1.mp4.jpg)

**Video 1.:** A Scn1a-cKO mouse (left) shows abnormal and spastic movements when suspended in the air. These movements are absent in Scn1a-floxed mice (right).

![Video 2.](https://cdn.elifesciences.org/articles/79917/elife-79917-video2.mp4.jpg)

**Video 2.:** A Scn1a-cKO mouse has uncoordinated leg movements and makes an abnormal rotation of its hind paw to grasp its tail while suspended in the air.

![Video 3.](https://cdn.elifesciences.org/articles/79917/elife-79917-video3.mp4.jpg)

**Video 3.:** A Scn1a-cKO mouse is scruffed and places hind paws with foot pads facing down. This contrasts with the normal paw positioning seen in the forepaws, in which foot pads are in the outward-facing position.

![Figure 5.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig5-v2.jpg)

**Figure 5.:** (A) Representative images showing limb positions of adult Scn1a-floxed (left), Scn1a-Het (middle), and Scn1a-cKO (right) mice. White arrows represent the direction of limbs. (B) Representative heat maps from open-field experiments between Scn1a-floxed (left), Scn1a-Het (middle), and Scn1a-cKO (right). Open field (C–F). Quantification of total distance traveled during a 10-min open-field test between Scn1a-floxed (cyan), Scn1a-Het (gray), and Scn1a-cKO (magenta) mice. (C) Scn1a-Het p=0.0255, Scn1a-cKO, p=0.0077, compared to Scn1a-floxed, average animal velocity. (D) Scn1a-Het p=0.00311, Scn1a cKO, p=0.0057, compared to Scn1a-floxed, percent time moving. (E) Scn1a-Het p=0.1362, p=0.0730, compared to Scn1a-floxed, and percent time spent in center. (F) Scn1a-Het p=0.2297, Scn1a-cKO, p=0.2494, compared to Scn1a-floxed, during the test. Rotarod (G–I). Quantification of the latency to fall across three consecutive training days (G) and day 3 (H). Quantification of revolutions per minute (RPM) at the moment of animal fall (I) and the day 3 average (J). Each dot represents one animal. Box and whisker plots represent maximum, minimum, median, upper and lower quartiles of data sets.****p<0.0001. A one-way ANOVA (Dunnett’s post-hoc comparison) was used to determine statistical significance in (C–F) and (I) and (J). A two-way mixed-design ANOVA (Dunnett’s post-hoc comparison) was used to determine statistical significance in (G) and (H) Open field: Scn1a-floxed N = 15, Scn1a-Het N = 6, Scn1a-cKO N = 12. Rotarod: Scn1a-floxed N = 11, Scn1a-Het N = 11, Scn1a-cKO N = 20.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A–D) Quantification of sex-dependent parameters during a 10-min open-field trial. Total distance moved (A). Velocity (B). Percent time spent in center of box (C). Total percent time moving (D) Males n = 10, females n = 17. Quantification of the sex-dependent differences in rotarod day 3 trial latency to fall (E) and revolutions per minute (RPM) (F). Males n = 18, females n = 24.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A–D) Images stained using immunohistochemistry with anti-DsRed (TdTomato). (A–C) Representative confocal images of spinal cord sections at ×10, 0.45 NA dry objective. Scale bar 200 μm. (D) Image was taken at ×20, 0.8 NA air objective of the ventral horn. (E) Image was taken at ×40, 1.3 NA oil-immersion objective of the ventral horn. (F) Image was taken at ×40, 1.3 NA oil-immersion objective of the ventral horn. Arrowheads indicate TdTomato+ puncta. (D–F) Scale bar 50 μm (N = 3 mice, n = 30 sections).

Could the motor deficits observed in Scn1a-cKO mice be due to abnormal proprioceptor development? To address this question, we performed RNAscope analysis of DRG sections from Scn1a-floxed, Scn1a-Het, and Scn1a-cKO mice. We quantified the number of neurons per DRG section that were positive for both Runx3 and Pvalb transcript, the molecular signature of mature proprioceptors (Figure 6, Oliver et al., 2021). We found no significant genotype-dependent differences in the number of proprioceptors in Scn1a-Het and Scn1a-cKO mice compared to Scn1a-floxed controls (p=0.3824 and p=0.1665, respectively), indicating that the behavioral deficits observed in Scn1a-cKO mice are not the result of a developmental loss of proprioceptors. We also analyzed muscle spindle morphology to determine whether aberrant sensory end organ development may contribute to the observed motor abnormalities. Similar to conditional Piezo2-knockout animals (Woo et al., 2015), no qualitative differences were observed between genotypes (Figure 6—figure supplement 1). Thus, abnormal proprioceptor development does not contribute to the overall phenotype of Scn1a-cKO mice.

![Figure 6.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig6-v2.jpg)

**Figure 6.:** Representative images of Scn1a-floxed (A), Scn1a-Het (B), and Scn1a-cKO (C) adult dorsal root ganglia (DRG) neuron sections (25 μm). Images were acquired with a ×40, 0.9 NA water-immersion objective. Sections were hybridized with probes targeting parvalbumin (Pvalb, yellow) and Runx3 (magenta). (D) Quantification of the percentage of Pvalb+/Runx3+ neurons in each genotype. Each dot represents one DRG section. Box and whisker plots represent maximum, minimum, median, upper and lower quartiles of data sets. A Kruskal–Wallis test with Dunn’s post-hoc comparison was used to determine statistical significance (p=0.1971, Scn1a-floxed n = 17, Scn1a-Het n = 17, Scn1a-cKO n = 18). n = sections. Scale bar 50 μm.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A–C) Representative confocal images of muscle spindle whole mounts. Images were acquired with a ×40, 1.3 NA oil-immersion objective. Sections were stained using immunohistochemistry with VGLUT1 (cyan) and neurofilament heavy (NFH, magenta). (A) Representative images from Scn1a-floxed (B), Scn1a-Het, and (C) Scn1a-cKO mice. Scn1a-floxed, n = 7; Scn1a-Het, n = 8; Scn1a-cKO, n = 9. Scale bar 50 μm. n = muscle spindles.

We next asked whether the motor deficits of Scn1a-cKO mice are due to altered synaptic connectivity between proprioceptive axons and motor neurons in the ventral spinal cord. Spinal cord sections were harvested from Scn1a-floxed, Scn1a-Het, and Scn1a-cKO mice and stained with antibodies against vesicular glutamate transporter 1 (VGLUT1) to label proprioceptor axons, and choline acetyltransferase (ChAT). ChAT primarily labels α- and γ-motor neurons in the ventral horn, which can be distinguished based on size. We analyzed the number of VGLUT1 puncta on the somata and proximal dendrites of individual cholinergic neurons greater than 400 μm2 to bias our quantification towards α-motorneurons. We found no significant decrease in VGLUT puncta density per ChAT+ neuron between Scn1a-Het or Scn1a-cKO when compared to Scn1a-floxed littermate controls (Figure 7, Scn1a-Het, p>0.9999, Scn1a-cKO, p=0.4573). This suggests that general deficits in proprioceptor innervation of motor neurons do not contribute to the phenotype of Scn1a-cKO mice.

![Figure 7.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig7-v2.jpg)

**Figure 7.:** (A–C) Representative images of Scn1a-floxed (A), Scn1a-Het (B), and Scn1a-cKO (C) adult spinal cord sections (30 μm). Images were acquired with a ×63, 1.4 NA oil-immersion objective. Sections were stained using immunochemistry with VGLUT1 (yellow) and ChAT (magenta). Nuclei (cyan) were labeled with DAPI. (D) Schematic of spinal cord regions of interest. (E) Quantification of the average density of VGLUT1+ puncta per 100 μm2 onto ChAT+ neurons that were larger than 400 μm2. A Kruskal–Wallis test with Dunn’s post-hoc comparison was used to determine statistical significance. Each dot represents a motor neuron. Box and whisker plots represent maximum, minimum, median, upper and lower quartiles of data sets. Scn1a-floxed, n = 101; Scn1a-Het, n = 102; Scn1a-cKO, n = 92. Scale bar 20 μm. n = cells.

We next asked whether proprioceptor electrical signaling is altered in Scn1a-cKO mice. While in vitro patch-clamp electrophysiology can assess NaV function at DRG somata and provide insight as to how they contribute to intrinsic excitability, the physiological contributions of ion channels in DRG soma to somatosensory transmission in vivo are not well understood. Thus, to directly investigate how NaV1.1 shapes action potential propagation down proprioceptor axons, we used an ex vivo preparation to record muscle afferent activity during ramp-and-hold stretch and sinusoidal vibration. Afferents from both Scn1a-Het and Scn1a-cKO mice exhibited impaired static stretch sensitivity as evidenced by a decreased likelihood of firing during rest as compared to Scn1a-floxed mice, as well as an inability to maintain firing throughout the entire 4 s stretch. Almost all afferents from Scn1a-floxed mice could fire consistently throughout the entire 4 s hold phase (Figure 8A), but loss of one or both copies of NaV1.1 led to either firing only near the beginning of stretch or inconsistent firing in a high percentage of afferents lacking NaV1.1 (Figure 8B and C). We quantified this inconsistent firing by determining the CV of the interspike interval (ISI) during the plateau phase of stretch (1.5–3.5 s into the hold phase) across different stretch lengths and found a significant effect of genotype, with the knockout afferents both having higher ISI CV than the Scn1a-floxed afferents (Figure 8D; 0.074 ± 0.06, 0.313 ± 0.456, 0.497 ± 0.831, at 7.5% Lo, Scn1a-floxed, Scn1a-Het, and Scn1a-cKO afferents, respectively, two-way ANOVA, main effect of genotype, p=0.015). In contrast to the clear deficits in static sensitivity in afferents lacking NaV1.1, dynamic sensitivity was not significantly impaired. The maximum firing frequency during the rampup phase (Dynamic Peak) was independent of genotype, and even trended slightly higher in afferents lacking NaV1.1 (Figure 8E; two-way ANOVA, effect of genotype p=0.0633).

![Figure 8.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig8-v2.jpg)

**Figure 8.:** (A–C) Representative responses to ramp-and-hold muscle stretch at 7.5% of optimal length (Lo) from Scn1a-floxed (A), Scn1a-Het (B), and Scn1a-cKO (C) afferents. Afferents from Scn1a-Het and Scn1a-cKO mice were more likely to show inconsistent firing during the hold phase of stretch. The percentage of afferents from each genotype that were able to fire consistently for the entire duration of stretch at 2.5, 5.0, and 7.5% of Lo is shown in the pie charts next to the representative trace from their genotype (black indicates percentage with inconsistent firing). The final pie charts represent the proportion of afferents that exhibited resting discharge at Lo for every stretch for each genotype (black indicates absence of resting discharge). (D) Inconsistency in firing was quantified as the interspike interval coefficient of variation (ISI CV) during the plateau stage of the hold phase of stretch (1.5–3.5 s into stretch) for the three different genotypes. A significant effect of genotype was observed (two-way mixed-design ANOVA, p=0.015). (E) The highest firing rate during the rampup phase of stretch (dynamic peak) is a measure of dynamic sensitivity. No significant effect of genotype on dynamic peak was observed (two-way mixed-design ANOVA, p=0.0633). Box and whisker plots represent maximum, minimum, median, upper and lower quartiles of data sets Each dot represents one afferent in (D) and (E) (Scn1a-floxed, n = 10; Scn1a-Het, n = 12; Scn1a-cKO, n = 11).

We next examined the requirement of NaV1.1 for proprioceptor afferent responses to sinusoidal vibration, which is a measure of dynamic sensitivity, and found no differences with loss of NaV1.1 (Figure 9A–C, Tables 1–3). We characterized a unit as having entrained to vibration if it fired at approximately the same time every cycle of the 9 s vibration. In most cases, afferents lacking NaV1.1 were equally likely to entrain to vibration than Scn1a-floxed afferents (Figure 9D–F). Indeed, Scn1a-cKO afferents were able to maintain firing during the entire 9 s sinusoidal vibration, in contrast to their inability to maintain consistent firing during 4 s of static stretch. There were no significant differences in firing rate during vibration between Scn1a-floxed, Scn1a-Het, and Scn1a-cKO afferents (Figure 9D–F). Taken together, our ex vivo recordings suggest that behavioral deficits in Scn1a-cKO result from abnormal proprioceptor responses to static muscle movement, whereas afferent responsiveness to dynamic stimuli is NaV1.1-independent. Furthermore, recordings from Scn1a-Het animals support the notion that NaV1.1 is haploinsufficient for proprioceptor function at the cellular level.

![Figure 9.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig9-v2.jpg)

**Figure 9.:** (A–F) Representative traces from afferents that were able to entrain to a 50 Hz, 100 µm vibration as well as graphs with the percentage of all Scn1a-floxed (cyan; A), Scn1a-Het (gray; B), and Scn1a-cKO (magenta; C) afferents that could entrain to the vibration shown in (A–C). Average firing frequency during a 9 s 50 Hz vibration shown for a 25 µm (D), 50 µm (E), and 100 µm (F) amplitude vibration. There was no significant effect of genotype on the firing frequency during vibration (25 µm, p=0.2398, 50 µm, p=0.2413, 100 μm, p=0.1276). A one-way ANOVA was used to determine statistical significance in (D) and (E). A Kruskal–Wallis test was used to determine statistical significance in (F). Box and whisker plots represent maximum, minimum, median, upper and lower quartiles of data sets. Each dot represents one afferent (Scn1a-floxed, n = 9; Scn1a-Het, n = 10; Scn1a-cKO, n = 11).

**Table 1.**
 Afferent entrainment to 25 μm amplitude vibration.The percentage of muscle spindle afferents that entrained to a 25 μm amplitude sinusoidal vibration.


<table>
  <thead>
    <tr>
      <th>Genotype</th>
      <th>10 Hz (%)</th>
      <th>25 Hz (%)</th>
      <th>50 Hz (%)</th>
      <th>100 Hz (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Scn1a-floxed</td>
      <td>33.33</td>
      <td>11.11</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Scn1a-Het</td>
      <td>50.00</td>
      <td>40.00</td>
      <td>10.00</td>
      <td>10.00</td>
    </tr>
    <tr>
      <td>Scn1a-cKO</td>
      <td>27.27</td>
      <td>9.09</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Afferent entrainment to 50 μm amplitude vibration.The percentage of muscle spindle afferents that entrained to a 50 μm amplitude sinusoidal vibration.


<table>
  <thead>
    <tr>
      <th>Genotype</th>
      <th>10 Hz (%)</th>
      <th>25 Hz (%)</th>
      <th>50 Hz (%)</th>
      <th>100 Hz (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Scn1a-floxed</td>
      <td>88.89</td>
      <td>22.22</td>
      <td>11.11</td>
      <td>11.11</td>
    </tr>
    <tr>
      <td>Scn1a-Het</td>
      <td>80.00</td>
      <td>70.00</td>
      <td>30.00</td>
      <td>10.00</td>
    </tr>
    <tr>
      <td>Scn1a-cKO</td>
      <td>45.45</td>
      <td>54.55</td>
      <td>18.18</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Afferent entrainment to 100 μm amplitude vibration.The percentage of muscle spindle afferents that entrained to a 100 μm amplitude sinusoidal vibration.


<table>
  <thead>
    <tr>
      <th>Genotype</th>
      <th>10 Hz (%)</th>
      <th>25 Hz (%)</th>
      <th>50 Hz (%)</th>
      <th>100 Hz (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Scn1a-floxed</td>
      <td>100.00</td>
      <td>44.44</td>
      <td>33.33</td>
      <td>22.22</td>
    </tr>
    <tr>
      <td>Scn1a-Het</td>
      <td>90.00</td>
      <td>90.00</td>
      <td>70.00</td>
      <td>40.00</td>
    </tr>
    <tr>
      <td>Scn1a-cKO</td>
      <td>63.64</td>
      <td>72.73</td>
      <td>63.64</td>
      <td>18.18</td>
    </tr>
  </tbody>
</table>

## Discussion

The critical role for NaV1.1 in various brain disorders has overshadowed the potential contributions of this channel in peripheral signaling. The results presented in this study are the first to provide functional evidence that NaV1.1 in peripheral sensory neurons is required for normal proprioception. We found that mice lacking NaV1.1 in sensory neurons exhibit visible motor deficits and ataxic-like behaviors, which we propose is largely attributed to loss of NaV1.1 in proprioceptors. Indeed, RNAscope analysis showed expression of NaV1.1 mRNA in 100% of genetically identified proprioceptors. While NaV1.6 and NaV1.7 were also ubiquitously expressed in proprioceptors, NaV1.1 displayed higher expression levels, consistent with a previous RNA-sequencing study (Zheng et al., 2019). There are anywhere from 5 to 8 different proprioceptor molecular subclasses (Oliver et al., 2021; Wu et al., 2021), however, and it is possible that these distinct classes rely on different combinations of these channels for function. Nevertheless, our functional in vitro patch-clamp experiments found NaV1.1 to be the dominant subtype across recorded neurons, comprising nearly half of the proprioceptor INa. In line with this, pharmacological inhibition of NaV1.1 is sufficient to significantly attenuate action potential firing in most proprioceptors; yet, it should be noted that 25% of the neurons we recorded fired action potentials that were insensitive to ICA application. This suggests that some proprioceptor subtypes rely more heavily on NaV1.6 and NaV1.7 for electrical activity. Interestingly, the proprioceptors that were insensitive to ICA application also were less intrinsic excitable, firing only 1–2 action potentials in response to current injection, as opposed to the other 75% on neurons recorded, which fired repetitively during the 100 ms injection protocol. This further supports a role for NaV1.1 in maintaining action potential firing in response to sustained stimulation. These results, however, should be interpreted with the caveat that in these experiments ICA may also be acting on NaV1.3 channels that are upregulated during DRG neuron culturing (Wangzhou et al., 2020). Nevertheless, at the afferent level Scn1a-cKO and Scn1a-Het animals show clear deficits in static stretch sensitivity, but not dynamic sensitivity, and could even entrain to vibrations as fast as 100 Hz, suggesting a specific role for NaV1.1 in proprioceptors responses to static muscle movement. Finally, we found that loss of NaV1.1 in sensory neurons had no effect on proprioceptor development, muscle spindle morphology, or proprioceptive afferent innervation of ChAT+ motor neurons in the spinal cord. Thus, the observed motor behavioral deficits are likely due to reduced static sensitivity of proprioceptor afferents.

Our model proposes that NaV1.1 is tasked with maintaining consistent firing in spindle afferents during static muscle stretch for normal motor behaviors, whereby activation of the mechanotransduction channel Piezo2 initiates electrical signaling, which in turn activates a complement of TTX-sensitive NaV channels (Carrasco et al., 2017; Florez-Paz et al., 2016; Woo et al., 2015; Figure 10). During dynamic or vibratory stimuli, Piezo2, and likely a combination of other molecular mediators, including NaV1.6 and NaV1.7, are sufficient to elicit normal electrical activity. Conversely, during prolonged muscle stretch when Piezo2 channels presumably inactivate, NaV1.1 is required for regular and reliable firing. While other signaling molecules and channels, such as vesicle-released glutamate (Bewick et al., 2005; Than et al., 2021), and mechanosensitive ASIC channels (Lin et al., 2016) and ENaC channels (Bewick and Banks, 2015), also contribute to mammalian proprioception, our data suggests that NaV1.1 is a critical for muscle spindle afferent mechanotransduction, given the overt behavioral deficits observed in Scn1a-cKO mice. Due to the ubiquitous expression of NaV1.1 in all proprioceptors and the importance of Golgi tendon organ (GTO) feedback to motor control, alterations in function in those proprioceptors likely contribute to the behavioral deficits we observed; however, we did not directly measure their function.

![Figure 10.](https://cdn.elifesciences.org/articles/79917/elife-79917-fig10-v2.jpg)

**Figure 10.:** Upon muscle static stretch, various channels activate, including Piezo2 (red), which results in an influx of calcium and sodium ions, causing a depolarization that activates NaV1.1 (dark blue). NaV1.1 activation drives reliable repetitive firing of proprioceptors during static stretch for normal motor behavior. Loss of NaV1.1 in sensory neurons results in inconsistent static firing at the afferent level while maintaining dynamic firing, resulting in uncoordinated movements and abnormal limb positioning. It is possible that a combination of Piezo2, NaV1.6 (yellow), NaV1.7 (pink), and/or other channels, such as glutamate receptors (dark blue), ASIC, and ENaC channels (green), mediates dynamic firing.

To date, our knowledge of the functional contributions of NaV1.1 in the PNS is limited. Most studies have identified roles for this channel in mechanical pain signaling in DRG, TG, and vagal sensory neurons. Intraplantar pharmacological activation of NaV1.1 induces spontaneous pain behaviors and mechanical pain, which are absent in mice lacking NaV1.1 in small- and medium-diameter sensory neurons (Osteen et al., 2016). Inhibition of NaV1.1 prevented the development of mechanical pain in several preclinical models, including spared nerve injury (Salvatierra et al., 2018), an irritable bowel syndrome mouse model (Salvatierra et al., 2018), and infraorbital nerve chronic constriction injury (Pineda-Farias et al., 2021). Additionally, blocking NaV1.1 channels inhibited firing in TRPM8-expressing neurons in vitro, suggesting a potential role for this channel in thermosensation (Griffith et al., 2019). No prior studies, however, have reported a functional role for NaV1.1, or NaVs in general, in proprioception.

The loss of consistent firing we observed during static stretch in Scn1a-cKO and Scn1a-Het animals is functionally similar to deletion of NaV1.1 in other brain cell types. Indeed, loss of a single copy of NaV1.1 is sufficient to attenuate sustained action potential firing in parvalbumin-positive hippocampal interneurons (Ogiwara et al., 2007; Yu et al., 2006) and cerebellar Purkinje neurons (Yu et al., 2006). NaV1.1 has been associated with persistent sodium current (INaP) and resurgent sodium current (INaR), both of which promote repetitive firing in a wide variety of cell types in the CNS and PNS (Barbosa et al., 2015; Kalume et al., 2007; Khaliq et al., 2003). NaV1.1 also recovers rapidly from fast inactivation compared to other channel subtypes (Herzog et al., 2003; Patel et al., 2015) and has been shown to be refractory to entry into slow inactivation in TRPM8-expressing DRG neurons (Griffith et al., 2019). We observed similar characteristics when analyzing the proprioceptor INa. Future studies will determine whether proprioceptors rely on these features of NaV1.1 for reliable and consistent encoding of static muscle stretch.

Loss of NaV1.1 notably impacted proprioceptor afferent static sensitivity during ramp-and-hold stretch, but not dynamic sensitivity as measured by entrainment to sinusoidal vibrations using ex vivo muscle-nerve recordings. Afferents from Scn1a-cKO animals were more likely to have action potential failures and thus were largely unable to fire consistently throughout the 4 s of stretch, which was accompanied by a higher coefficient of variability in the ISI. This indicates that NaV1.1 has a critical role in transmitting static stretch information to the CNS. Interestingly, however, dynamic sensitivity in these afferents was unimpaired. Both Scn1a-cKO and Scn1a-Het afferents were able to entrain throughout the entire 9 s vibration; therefore, NaV1.1 does not appear to have a generalized role in maintaining high-frequency firing, but a more specific contribution to muscle-afferent static sensitivity. NaV1.1 has been localized to muscle spindle afferent endings and has been hypothesized to help amplify receptor current (Carrasco et al., 2017). Our results support a model whereby current from Piezo2 and potentially other mechanically sensitive ion channels at the start of stretch produces a sufficient receptor potential to generate firing at the heminode, but that amplification of the receptor potential by NaV1.1 is necessary to maintain firing during held stretch.

A similar deficit in static but not dynamic sensitivity was seen following loss of synaptic-like vesicle released glutamate from afferent endings (Than et al., 2021); however, in those afferents, firing only occurred at the beginning of stretch and patchy firing was never observed. This may indicate that glutamate plays a more general role maintaining excitability, whereas NaV1.1 is required for reliable action potential generation at heminodes during static stimuli. Alternatively, or in addition, NaV1.1 expressed along the axon could be essential for sustained static firing. A detailed examination of NaV1.1 subcellular localization along proprioceptor afferents could shed light on how this channel contributes to signal propagation. The lack of an effect on dynamic sensitivity could suggest the upregulation of other NaV subtypes or other molecules as a compensatory mechanism to counteract the loss of NaV1.1. Indeed, our in vitro electrophysiological experiments found a more pronounced effect of acute NaV1.1 inhibition on proprioceptor excitability. This could be due, however, to artificially upregulated NaV1.3 channel activity in culturing conditions, or conversely, a higher density of NaV1.1 expression in proprioceptor somata. Future studies using temporally controlled deletion of NaV1.1 in sensory neurons could tease this apart. Nevertheless, as static sensitivity is still very much impaired in both Scn1a-cKO and Scn1a-Het afferents, NaV1.1 may play a potentially unique role in maintaining afferent firing during the sustained stretch.

Loss of NaV1.1 in sensory neurons did not impact proprioceptor development as the number of proprioceptors in DRG sections was unchanged between genotypes, and muscle spindles developed normally in our model. While we did not directly examine GTOs, we do not anticipate that abnormal end organ development would be restricted to that proprioceptor subtype. Additionally, we did not observe a general decrease in α-motor neuron innervation, which is consistent with the findings of Mendelsohn et al., 2015, who reported loss of proprioceptor activity does not generally reduce proprioceptive input into the spinal cord. Interestingly, however, the authors did observe changes in heteronymous sensory-motor connectivity when proprioceptor transmission was blocked, whereby proprioceptor innervation of motor neurons that project to antagonistic muscles was increased. Whether loss of NaV1.1 in proprioceptive afferents causes them to ‘mis-wire’ in our model to make connections with inappropriate motor neuron pools is unclear. Future studies will determine whether this contributes to the observed behavioral deficits.

We found effects of both pharmacological inhibition and genetic deletion of NaV1.1 in in vitro and ex vivo electrophysiological experiments, respectively (Figures 2, 4, 8 and 9); however, in our mouse model NaV1.1 is deleted in all sensory neurons. Thus, we cannot rule out that loss of NaV1.1 in other mechanosenory neuron populations, such as touch receptors, contributes to the motor deficits observed. Deletion of NaV1.1 in small- and medium-diameter DRG neurons using a peripherin-Cre driver did not produce visible motor deficits (Osteen et al., 2016), indicating that sensory neuron populations in those categories are not involved. We did observe NaV1.1 transcripts in the vast majority of myelinated DRG neurons (a combination of large- and medium-diameter DRG neurons), consistent with its presence in different subclasses of tactile sensory neurons (Zheng et al., 2019). However, the severe motor phenotype of Scn1a-cKO mice precludes mechanical threshold analysis using von Frey or tactile sensitivity using tape test. Notably, baseline mechanical thresholds were unchanged following intraplantar injection of a selective NaV1.1 inhibitor (Salvatierra et al., 2018). This suggests that while NaV1.1 mRNA is expressed in most tactile sensory neurons, functional protein may only be upregulated in these populations during pathological states.

Despite this limitation, one noteworthy and intriguing finding from our study was the haploinsufficiency of NaV1.1 in sensory neurons for proprioceptor function and normal motor behavior in the open-field test. At the afferent level, heterozygous and homozygous loss of NaV1.1 produced similar deficits in static firing, suggesting that loss of less than a quarter of the proprioceptor INa is sufficient to impair proprioceptor responsiveness to muscle stretch. NaV1.1 is haploinsufficient in several brain neuron cell types for normal excitability and function (Ogiwara et al., 2007; Yu et al., 2006), suggesting the contributions of NaV1.1 to neuronal function are highly sensitive to genetic perturbations. At the behavioral level, Scn1a-Het mice had an identical phenotype to Scn1a-cKO mice, moving more slowly and less than controls, despite not having the more severe and visible motor coordination deficits. Indeed, their performance on the rotarod was identical to that of Scn1a-floxed controls (Figure 5). How these behavioral differences arise given the similar transmission deficits in Scn1a-cKO and Scn1a-Het afferents is unclear. One possibility is a presynaptic role for NaV1.1 in proprioceptive terminals that is unveiled when both copies of NaV1.1 are lost. For example, loss of presynaptic NaV1.7 channels in the spinal cord reduced glutamate release from nociceptive afferents onto dorsal horn neurons (MacDonald et al., 2021). If a similar mechanism is at play for NaV1.1 in proprioceptors, reduced neurotransmitter release from Scn1a-Het afferent terminals could be sufficient to produce quantifiable, albeit more subtle, motor deficits. Future studies are required to test this possibility.

Notably, Scn1a is a super culprit gene with over 1000 associated disease-causing mutations, most of which are linked to different forms of epilepsy. Many epilepsy patients with hemizygous NaV1.1 loss of function display ataxia and motor delays and deficiencies (Claes et al., 2001; Fujiwara et al., 2003), which has traditionally been attributed to loss of NaV1.1 function in the brain, namely, the cerebellum (Kalume et al., 2007). Our findings suggest that some of the clinical manifestations associated with epilepsy are not solely due to NaV1.1 loss of function in the brain, but also may manifest in part as a result of unreliable coding by peripheral proprioceptors.

Data presented in this study provide new evidence of a role for peripherally expressed NaV1.1 in motor coordination. We show that NaV1.1 is ubiquitously and strongly expressed in proprioceptors, contributes to proprioceptor excitability in vitro and ex vivo, and is haploinsufficient in sensory neurons for normal motor behaviors. Collectively, this work identifies a new role for NaV1.1 in mammalian proprioception.

## Materials and methods

Key Resources Table contains a list of key resources and supplies used for this study.

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
      <td>Antibody</td>
      <td>Anti-DsRed (rabbit polyclonal)</td>
      <td>Takara Bio</td>
      <td>Cat #632496</td>
      <td>1:3000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>GFP (chicken polyclonal)</td>
      <td>Abcam</td>
      <td>Cat #ab13970</td>
      <td>1:3000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>NFH (chicken polyclonal)</td>
      <td>Abcam</td>
      <td>Cat #ab4680</td>
      <td>In muscle spindles: (1:300)In DRG:(1:3000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CGRP (rabbit polyclonal)</td>
      <td>ImmunoStar</td>
      <td>Cat #24112</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>VGLUT1 (guinea pig polyclonal)</td>
      <td>Zuckerman institute (Columbia University)</td>
      <td>Cat #CU1706; RRID:AB_2665455</td>
      <td>In spinal cord: (1:8000)In muscle spindles:(1:800)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>β3-tubulin (chicken polyclonal)</td>
      <td>Abcam</td>
      <td>Cat #ab41489</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>β3-tubulin (rabbit polyclonal)</td>
      <td>Abcam</td>
      <td>Cat #ab18207</td>
      <td>1:3000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>ChAT (rabbit polyclonal)</td>
      <td>Zuckerman Institute (Columbia University)</td>
      <td>Cat #CU1574</td>
      <td>1:10,000</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>VECTASHIELD Antifade Mounting Media with DAPI</td>
      <td>Vector Laboratories</td>
      <td>Cat #H-2000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tissue-Tek OCT compound</td>
      <td>Sakura</td>
      <td>Cat #4583</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Laminin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat #L2020-1MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Collagenase type P</td>
      <td>Sigma-Aldrich</td>
      <td>Cat #11213865001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TrypLE Express</td>
      <td>Thermo Fisher</td>
      <td>Cat #12605-010</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MEM</td>
      <td>Thermo Fisher</td>
      <td>Cat #11095-080</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Penicillin-streptomycin</td>
      <td>Thermo Fisher</td>
      <td>Cat #15140-122</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MEM vitamin solution</td>
      <td>Thermo Fisher</td>
      <td>Cat #11120-052</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>B-27 supplement</td>
      <td>Thermo Fisher</td>
      <td>Cat #17504-044</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Horse serum, heat inactivated</td>
      <td>Thermo Fisher</td>
      <td>Cat #26050-070</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ICA 121431</td>
      <td>Tocris Bioscience</td>
      <td>Cat #5066/10</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>4,9-anhydrous tetrodotoxin</td>
      <td>Tocris Bioscience</td>
      <td>Cat #6159</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PF-05089771</td>
      <td>Tocris Bioscience</td>
      <td>Cat #5931</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tetrodotoxin</td>
      <td>Abcam</td>
      <td>Cat ab120054</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNAscope Fluorescence Multiplex Kit</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat #320851</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Pvalb probe channel 1</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat #421931</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Scn1a probe channel 2</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat #556181-C2</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Scn8a probe channel 2</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat #313341-C2</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Scn9a probe channel 2</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat #434191-C2</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Runx3 probe channel 3</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat #451271-C3</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>Pirtcre</td>
      <td>Dr. Xinzhong Dong</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>Rosa26Ai14</td>
      <td>Jackson Laboratories</td>
      <td>Stock #007914</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>Pvalbcre</td>
      <td>Jackson Laboratories</td>
      <td>Stock #008069</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>Scn1a-floxed</td>
      <td>UC Davis MMRRC</td>
      <td>Stock # 041829-UCD</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>MrgprdGFP</td>
      <td>Zheng et al., 2019</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pClamp 11.2 Software Suite</td>
      <td>Molecular Devices</td>
      <td>https://www.moleculardevices.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>Schneider et al., 2012</td>
      <td>https://imagej.nih.gov</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism 9</td>
      <td>GraphPad</td>
      <td>https://www.graphpad.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LabChart</td>
      <td>ADInstruments</td>
      <td>https://www.adinstruments.com/products/labchart</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>https://www.mathworks.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>This study</td>
      <td>https://github.com/doctheagrif/Current-Clamp-Matlab-Code_O-Neil-DA; O’Neil, 2022b</td>
      <td>Current-clamp experiments were analyzed with a custom-written MATLAB Script that is available on GitHub</td>
    </tr>
  </tbody>
</table>

### Animals

Pirtcre mice were a kind gift from Dr. Xinzhong Dong (Johns Hopkins University). Rosa26Ai14 (stock #007914; Madisen et al., 2010) and Pvalbcre (stock # 008069) were obtained from Jackson Laboratories. Scn1a-floxed (stock #041829-UCD) mice were purchased from the UC Davis MMRRC. Mrgprd mice were originally published in Zheng et al., 2019. All mice used were on a mixed C57BL/6 background (non-congenic). Genotyping was outsourced to Transnetyx. Animal use was conducted according to guidelines from the National Institutes of Health’s Guide for the Care and Use of Laboratory Animals and was approved by the Institutional Animal Care and Use Committee of Rutgers University-Newark (PROTO201900161), UC Davis (#21947 and #22438), and San José State University (#990, ex vivo muscle recordings). Mice were maintained on a 12 hr light/dark cycle, and food and water was provided ad libitum.

### Rotarod

To assess motor coordination, a rotarod machine (IITC Life Sciences, Woodland Hills, CA) that has an accelerating rotating cylinder was used. 8–10-week-old mice of both sexes were acclimated to the behavior room for 2 hr prior to testing. Mice were assayed on the rotarod for three consecutive days, with three trials per day and an intertrial interval of at least 15 min. The average of the three trials per day was used. The experimenter was blind to genotype.

### Open-field test

8–10-week-old mice of both sexes were acclimated to the behavior room for 2 hr prior to testing. The open-field apparatus consisted of a black square sound attenuating box of dimensions 40.6 cm × 40.6 cm. A camera suspended above the arena was connected to a computer running Ethovision XT software, which tracked animal movement and velocity. An animal was placed in the center of the arena and allowed to freely explore for a 10-min trial. The experimenter was blind to genotype.

### Tissue processing

For spinal cord immunolabeling experiments, whole spinal columns from adult (8–15 weeks) PirtCre;Rosa26Ai14 and PirtCre;Scn1a-floxed animals of both sexes were harvested on ice. For Tdtomato immunohistochemistry, spinal columns were fixed overnight at 4°C in 4% paraformaldehyde. For vesicular glutamate transporter 1 (VGLUT1) and choline acetyltransferase (ChAT) co-labeling experiments, spinal columns were fixed in 4% paraformaldehyde for 1 hr on ice. Tissue was then placed in 30% sucrose solution overnight at 4°C. Following cryoprotection, tissue was embedded in optimal cutting temperature compound (OCT, Tissue-Tek Sakura) and stored at –80°C until sectioning. DRG from adult (8–15 weeks) animals of both sexes were harvested from thoracic spinal levels and fixed in 4% formaldehyde for 15 min at 4°C and were then incubated in 30% sucrose for 2–4 hr at 4°C. DRG were embedded in OCT and stored at –80°C until sectioning.

### Immunohistochemistry

Immunohistochemistry of spinal cord cryostat sections (30 μm) was performed using the following primary antibodies: rabbit anti-DsRed (1:3000, Takara Bio, 632496), guinea pig anti-VGLUT1 (1:8000, Zuckerman Institute, 1705), and rabbit anti-ChAT (1:10,000, Zuckerman Institute, 1574). Secondary antibodies used were as follows: anti-rabbit 594 (1:1000, Thermo Fisher, A32740), anti-guinea pig 488 (1:1000, Thermo Fisher, A11073), and anti-chicken 647 (Thermo Fisher, A32733). Specimens were mounted with Fluoromount-G with DAPI (SouthernBiotech, 0100-20). EDL muscles used in ex vivo muscle afferent recordings were placed in ice-cold 4% paraformaldehyde for 1 hr followed by ice-cold methanol for 15 min. Muscles were incubated in blocking solution (0.3% PBS-T and 1% BSA) followed by incubation in primary antibodies (guinea pig anti-VGLUT1 1:800 and chicken anti-NFH 1:300, Thermo Fisher ab4680) for 3–6 days at 4°C. After primary antibody treatment, tissue was washed in blocking solution and treated with secondary antibody (anti-guinea pig 488 1:50 and anti-chicken 594 1:300, Invitrogen, WA316328) for 2–3 days. Specimens were mounted with VECTASHIELD with DAPI (H-2000, Vector Laboratories). All specimens were imaged in three dimensions on a Zeiss LSM880 Airyscan confocal microscope. Images were analyzed using ImageJ software.

### Multiplex in situ hybridization

Fixed-frozen DRG tissue from 8- to 15-week-old mice of both sexes was cut into 25 μm sections and placed on electrostatically coated slides. Sections were processed for RNA in situ detection using a modified version of the manufacturer’s protocol (Griffith et al., 2019, Advanced Cell Diagnostics) and the following probes: Pvalb (421931C1, mouse), Runx3 (451271-C3, mouse), Scn1a (556181-C2, mouse), Scn8a (313341-C2, mouse), and Scn9a (434191-C2, mouse). Following in situ hybridization, sections were incubated in blocking solution (5% normal goat serum, 0.1% PBS-T) for 1 hr at room temperature (RT). Tissue was then incubated in primary antibodies overnight at 4°C. The following antibodies were used: rabbit DsRed (1:3000, Takara Bio, 632496), rabbit β3-tubulin (1:3000, Abcam, ab18207), chicken β3-tubulin (1:500, Abcam, ab41489), rabbit CGRP (1:1000, ImmunoStar, 24112), chicken GFP (1:3000, Abcam, ab13970), and chicken NFH (1:3000, Abcam, ab4680). Tissue was treated with the following secondary antibodies for 45 min at RT: anti-rabbit 448 (1:1000, Invitrogen, A32731), 594 (1:1000, Invitrogen, A11037) and 647 (1:1000, Invitrogen, A32733), anti-chicken 488 (1:1000, Invitrogen, A32931) and 594 (1:1000, Invitrogen, A32740). Sections were washed and mounted with Fluoromount-G with DAPI and imaged in three dimensions (2 μm axial steps) on an Olympus confocal (LV3000) using a ×40 0.90 NA water objective lens. Images were autothresholded and the probe signal integrated density for individual neurons was analyzed using ImageJ software. The coefficients of variation for Scn1a, Scn8a, and Scn9a integrated densities were calculated in Prism 9.0 (GraphPad Software) using the following formula: CV = μ/σ * 100.

### DRG culture preparation

DRGs were harvested from thoracic spinal levels of adult Pvalbcre;Rosa26Ai14 and Pirtcre;Scn1a-floxed (6–16 weeks) mice of both sexes and transferred to Ca2+-free and Mg2+-free HBSS solution (Invitrogen, 14170-112). Upon isolation, processes were trimmed, and ganglia were transferred into collagenase (1.5 mg/mL; Type P, Sigma-Aldrich, 11213865001) in HBSS for 20 min at 37°C followed by TrypLE Express (Thermo Fisher, 12605-010) for 3 min with gentle rotation. TrypLE was neutralized with 10% horse serum (heat-inactivated; Invitrogen, 26050-070) and supplemented with culture media (MEM with l-glutamine, Phenol Red, without sodium pyruvate, Thermo Fisher, 11095-080), containing 10,000 U/mL penicillin-streptomycin (Thermo Fisher, 15140-122), MEM Vitamin Solution (Invitrogen, 11120-052), and B-27 supplement (Thermo Fisher, 17504-044). Serum-containing media was decanted and cells were triturated using a fire-polished Pasteur pipette in the MEM culture media described above. Cells were resuspended and triturated using a plastic pipette tip. Cells were plated on glass coverslips that had been washed in 2 M NaOH for at least 4 hr, rinsed with 70% ethanol, UV-sterilized, and treated with laminin (0.05 mg/mL, Sigma-Aldrich, L2020-1MG) for 1 hr prior to plating. Cells were then incubated at 37°C in 5% CO2. Cells were used for electrophysiology experiments 14–36 hr post-plating.

### In vitro electrophysiology

Whole-cell voltage-clamp recordings were made from dissociated DRG neurons using patch pipettes pulled from Model P-1000 (Sutter Instruments). Patch pipettes had a resistance of 3–5 MΩ when filled with an internal solution containing the following (in mM): 140 CsF, 10 NaCl, 1.1 EGTA,.1 CaCl2, 10 HEPES, and 2.5 MgATP, pH with CsOH to 7.2. Seals and whole-cell configuration were obtained in an external solution containing the following (in mM): 145 NaCl, 5 KCl, 10 HEPES, 10 glucose, 2 CaCl2, 2 MgCl2, pH 7.3 with NaOH, osmolarity ~320 mOsm. Series resistance ranged from 6 to 11 MΩ and was compensated by 70–80%. Voltage errors were not directly assessed in current-clamp recordings. To isolate whole-cell sodium currents during voltage-clamp experiments, a modified external solution was applied containing the following (in mM): 15 NaCl, 130 TEA-Cl, 10 HEPES, 2 BaCl2, 13 glucose, 0.03 CdCl2, pH 7.3 with NaOH, osmolarity ~320 mOsm. Voltage-clamp recordings were performed at RT and current-clamp recordings were conducted at 37°C. Bath temperature was controlled and monitored using CL-100 (Warner Instruments).

### Ex vivo electrophysiology

The effect of the loss of NaV1.1 on muscle spindle afferent firing rates during muscle stretch and sinusoidal vibration was determined using an isolated muscle nerve preparation. The extensor digitorum longus muscle and innervating peroneal branch of the sciatic nerve were dissected from adult (2–4-month-old) mice of both sexes. Muscles were held at optimal length (Lo), or the length of the muscle that maximal force of twitch contraction occurred. A series of nine 4 s ramp-and-hold stretches were given to three different stretch lengths repeated three times each (2.5, 5, and 7.5% Lo; ramp speed 40% Lo/s). A series of twelve 9 s sinusoidal vibrations were given (25, 50, and 100 µm amplitude; 10, 25, 50, and 100 Hz frequency). A 1-min rest was given between each length change. Firing rates during a 10 s baseline before stretch (resting discharge or RD) and the maximal firing rate during the rampup phase of stretch (dynamic peak or DP) were calculated for all animals. We determined whether the response to static stretch was maintained consistently throughout the 4 s stretch, as well as the coefficient of variability of the ISI during the plateau phase of stretch (CV = Std Dev/Mean of ISI over the time period of 1.5–3.5 s after end of rampup). Average firing rate during the 9 s of vibration and whether the unit could entrain in a 1:1 fashion to vibration was also determined. Detailed methods can be found in Wilkinson et al., 2012.

### Pharmacology

ICA 121431 (#5066), 4,9-anhydrotetrodotoxin (AH-TTX, #6159), and PF-05089771 (#5931) were purchased from Tocris Bioscience. Tetrodotoxin (TTX, ab120054) was purchased from Abcam. All other chemicals were from Sigma-Aldrich and Fisher Chemical.

### Data acquisition and analysis

Currents and voltages were acquired using pClamp software v11.2 (Molecular Devices). Recordings were obtained using an AxoPatch 200b patch-clamp amplifier and a Digidata 1550B and filtered at 5 kHz and digitized at 10 kHz. For biophysical analysis of whole-cell sodium currents, conductance (G) was calculated as G = I/(V – ENa), in which I is the peak current, V is the voltage step, and ENa is the reversal potential for sodium calculated from Nernst equation based on the intracellular and extracellular sodium concentrations in our recording solutions (10.38 mV). Conductance data were normalized by the maximum conductance value, Gmax, and data was fit with the Boltzmann equation: Fraction available = Minimum + ([Maximum-Minimum]/[1 + exp(V50 Vm)/k]), where V50 denotes the membrane potential at which half the channels are inactivated and k denotes the Boltzmann constant/slope factor. For voltage dependence of steady-state inactivation, peak current data were normalized based on the maximum current, Imax. Analysis of action potential amplitude, full-width half max, and threshold was performed on the first action potential elicited in response to a 100 pA current injection (100 ms). Action potential threshold was calculated as the membrane potential at which the first derivative of the somatic membrane potential (dV/dT) reached 10 mV ms–1 (Griffith et al., 2019; Kress et al., 2008). Tau values were calculated from 20 ms voltage steps from –90 mV to –30 mV and analyzed with single-exponential curve fits. Voltage-clamp and current-clamp experiments were analyzed with Clampfit software v11.2 (Molecular Devices) and custom MATLAB Scripts. Ex vivo recordings were obtained using an A-M Systems Model 1800 extracellular amplifier with headstage and digitized using an ADInstruments PowerLab. Data was analyzed using ADInstruments LabChart software using the Spike Histogram function.

### Experimental design and statistical analysis

Summary data are presented as mean ± SEM, from n cells, afferents, or sections, or N animals. For quantitative analysis of in situ hybridization data, at least three biological replicates per condition were used and the investigator was blinded to genotype for analysis. Behavioral experiments and analysis were also performed genotype-blind. Statistical differences were determined using parametric tests for normally distributed data and nonparametric tests for data that did not conform to Gaussian distributions or had different variances. Statistical tests are listed in ‘Results’ and/or figure legends. Statistical significance in each case is denoted as follows: *p<0.05, **p<0.01, ***p<0.001, and ****p<0.0001. Statistical tests and curve fits were performed using Prism 9.0 (GraphPad Software). All data generated or analyzed during this study are included in the article. Source data files have been uploaded to Mendeley for all figures (https://data.mendeley.com/datasets/kt23th75v9). Code has been uploaded to GitHub (https://github.com/darikoneil/PropAnalysisScripts; O’Neil, 2022a). A Key Resources Table with specific organism and reagent information has been included in the ‘Materials and methods’ section.
