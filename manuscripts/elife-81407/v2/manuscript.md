# CaV1 and CaV2 calcium channels mediate the release of distinct pools of synaptic vesicles

## Authors

- Brian D Mueller<sup>1</sup> ([ORCID: 0000-0002-6525-7101](https://orcid.org/0000-0002-6525-7101))
- Sean A Merrill<sup>1</sup>
- Shigeki Watanabe<sup>1</sup> ([ORCID: 0000-0001-7580-8141](https://orcid.org/0000-0001-7580-8141))
- Ping Liu<sup>2</sup>
- Longgang Niu<sup>2</sup> ([ORCID: 0000-0001-7209-7436](https://orcid.org/0000-0001-7209-7436))
- Anish Singh<sup>1</sup>
- Pablo Maldonado-Catala<sup>3</sup>
- Alex Cherry<sup>1</sup>
- Matthew S Rich<sup>1</sup>
- Malan Silva<sup>1</sup>
- Andres Villu Maricq<sup>3</sup>
- Zhao-Wen Wang<sup>2</sup> ([ORCID: 0000-0003-3574-8556](https://orcid.org/0000-0003-3574-8556))
- Erik M Jorgensen<sup>1</sup> ([ORCID: 0000-0002-2978-8028](https://orcid.org/0000-0002-2978-8028)) †

### Affiliations

1. Howard Hughes Medical Institute, School of Biological Sciences, University of Utah Salt Lake City United States ([ROR:03r0ha626](https://ror.org/03r0ha626))
2. Department of Neuroscience, University of Connecticut Medical School Farmington United States ([ROR:02der9h97](https://ror.org/02der9h97))
3. Department of Neurobiology, University of Utah Salt Lake City United States ([ROR:03r0ha626](https://ror.org/03r0ha626))

† Corresponding author

## Abstract

Activation of voltage-gated calcium channels at presynaptic terminals leads to local increases in calcium and the fusion of synaptic vesicles containing neurotransmitter. Presynaptic output is a function of the density of calcium channels, the dynamic properties of the channel, the distance to docked vesicles, and the release probability at the docking site. We demonstrate that at Caenorhabditis elegans neuromuscular junctions two different classes of voltage-gated calcium channels, CaV2 and CaV1, mediate the release of distinct pools of synaptic vesicles. CaV2 channels are concentrated in densely packed clusters ~250 nm in diameter with the active zone proteins Neurexin, α-Liprin, SYDE, ELKS/CAST, RIM-BP, α-Catulin, and MAGI1. CaV2 channels are colocalized with the priming protein UNC-13L and mediate the fusion of vesicles docked within 33 nm of the dense projection. CaV2 activity is amplified by ryanodine receptor release of calcium from internal stores, triggering fusion up to 165 nm from the dense projection. By contrast, CaV1 channels are dispersed in the synaptic varicosity, and are colocalized with UNC-13S. CaV1 and ryanodine receptors are separated by just 40 nm, and vesicle fusion mediated by CaV1 is completely dependent on the ryanodine receptor. Distinct synaptic vesicle pools, released by different calcium channels, could be used to tune the speed, voltage-dependence, and quantal content of neurotransmitter release.

## Introduction

Synaptic vesicles fuse to the plasma membrane within the presynaptic bouton in a domain called the active zone, and the intricate molecular architecture within the active zone determines the dynamics of the neurotransmitter release (Guzikowski and Kavalali, 2021). Vesicle fusion is driven by calcium influx and binding to the calcium sensor synaptotagmin on the synaptic vesicle (Geppert et al., 1994; Littleton et al., 1993; Ward et al., 2004). The coupling of calcium channels to fusion sites determines the transfer function of synapses to depolarizing inputs (Eggermann et al., 2011; Eguchi et al., 2022; Özçete and Moser, 2021; Rebola et al., 2019), and thus synaptic activity depends on three features of calcium-mediated vesicular fusion: the dynamic properties of the calcium channel, the concentration of calcium at the fusion site, and the release probability of the vesicle. These features are dictated by calcium channel type and location, by the distance to docked vesicles, and by the activity of the priming protein Unc13. Here, we characterize these features at the Caenorhabditis elegans neuromuscular junction.

Voltage-gated calcium channels are divided into three molecular families: CaV1, CaV2, and CaV3, each with fundamentally different dynamic properties, including voltage-sensitive activation and inactivation (Catterall et al., 2005; Nowycky et al., 1985). Each of these channel classes is primarily associated with tissue-specific functions: In muscle, CaV1 (L-type) channels mediate contraction and are coupled to the ryanodine receptor to release internal calcium stores (RyR). In neurons, CaV2 (P/Q, N, and R-type) channels drive synaptic transmission. In neurons and excitable cells, CaV3 (T-type) regulate action potential oscillations and pacemaker frequencies (Dolphin, 2021) These tissue-specific roles are not exclusive, for example, the CaV1 variants CaV1.3 and CaV1.4 are associated with neurotransmitter release in hair cells and photoreceptors, respectively (Dolphin and Lee, 2020).

In the nematode C. elegans, each class is represented by a single gene: CaV1 (egl-19), CaV2 (unc-2), CaV3 (cca-1), and RyR (unc-68). In all animals, CaV2 is the main calcium channel for synaptic transmission (Richmond et al., 2001; Smith et al., 1996; Tsien et al., 1988; Tsien and Tsien, 1990; Zheng et al., 1995). Unlike other animals, nematodes lack voltage-gated sodium channels and neurotransmission is typically mediated via graded release, however some interneurons use action potentials (Liu et al., 2013; Liu et al., 2009; Mellem et al., 2008). In unc-2 mutants, which lack the CaV2 channel, the frequency of tonic miniature currents (’minis’) is severely reduced; however, some release remains (Richmond et al., 2001; Tong et al., 2017). Physiological studies suggest CaV1 can also contribute to neurotransmission; CaV1 channel blockers reduce tonic minis by half (Tong et al., 2017). However, the role of CaV1 channels at synapses in C. elegans is complicated because CaV1 also contributes to calcium-mediated action potentials in neurons and is required in the body muscle for viability (Lee et al., 1997; Liu et al., 2018a). Finally, the ryanodine receptor also contributes to neurotransmission, and is specifically required for multivesicular release (Chen et al., 2017; Liu et al., 2005).

The distance between the calcium channel and docked and primed vesicle must be very short. After the channels close, diffusion causes a rapid drop in the concentration of calcium at sites of vesicle fusion (Dittman and Ryan, 2019). Free calcium is further reduced by calcium buffers and calcium pumps (Blaustein, 1988; Eggermann et al., 2011). Because intracellular calcium is extremely low (0.05 μM), and levels required for fusion are relatively high (half-maximal 10 μM) (Courtney et al., 2018; Schneggenburger and Neher, 2000), the effective range of calcium around a single voltage-gated calcium channel is predicted to be only 20 nm for evoked fusion, a ‘nanodomain’ not much larger than the diameter of the calcium channel itself (Fedchyshyn and Wang, 2005; Weber et al., 2010). The synaptic vesicle in vertebrates is 45 nm in diameter; in C. elegans vesicles are somewhat smaller, 32 nm in diameter; nevertheless, these data suggest that the vesicle must be nearly on top of the calcium channel.

The presence of vesicles docked at release sites and the probability of vesicle fusion depends on the active zone protein Unc13 (Dittman, 2019; Neher and Brose, 2018). Unc13 tethers vesicles to the active zone membrane through C2B and C2C domains which flank the MUN domain (Imig et al., 2014; Quade et al., 2019). The central MUN domain interacts with the SNARE protein syntaxin (Augustin et al., 1999; Lai et al., 2017; Yang et al., 2015) and promotes the open state of syntaxin to initiate SNARE pairing (Richmond et al., 2001). Moreover, binding of DAG and calcium to Unc13 regulates the differential release probabilities of primed vesicles (Basu et al., 2007; Michelassi et al., 2017; Neher and Brose, 2018). In the absence of Unc13, synaptic vesicles fail to dock at release sites (Hammarlund et al., 2007; Imig et al., 2014; Richmond et al., 1999; Siksou et al., 2009).

Here, we demonstrate in C. elegans that two different classes of voltage-gated calcium channels, CaV2 (UNC-2) and CaV1 (EGL-19) mediate the release of two physiologically distinct pools of synaptic vesicles as described in a previous study (Tong et al., 2017). We also show that a third calcium channel, the ryanodine receptor (RyR / UNC-68), is essential for CaV1-mediated vesicle release. Time-resolved electron microscopy in calcium channel mutants demonstrates that these channels mediate fusion of spatially distinct pools of synaptic vesicles in the same synaptic varicosity. Finally, we use super-resolution fluorescence microscopy to demonstrate that CaV2 is localized with UNC-13L at the dense projection, and that CaV1 and RyR colocalize with UNC-13S at distal sites. Altogether, we describe two pools of synaptic vesicles: (1) The central pool is localized adjacent to the dense projection, vesicles are docked by UNC-13L, and released by a dense cluster of CaV2 channels. (2) The lateral pool of vesicles is broadly distributed, docked by UNC-13S, and released by dispersed CaV1 and RyR channels.

## Results

### CaV1 and CaV2 calcium channels have partially overlapping functions

The genome of C. elegans contains only a single gene for each major voltage-gated calcium channel class: CaV1 (egl-19), CaV2 (unc-2), CaV3 (cca-1), and a single calcium-gated RyR (unc-68) (hereafter, referred to by their common names). Loss of the CaV3 T-type channel does not affect neurotransmitter release in acetylcholine neurons (Liu et al., 2018b). However, loss of any other calcium channel results in impaired neurotransmission (Liu et al., 2005; Richmond et al., 2001; Tong et al., 2017). Null mutants lacking either CaV2 (unc-2(lj1)) or RyR (unc-68(e540)) are viable. unc-2(lj1) is a large deletion and frame shift, and unc-68(e540) is a G>A splice acceptor mutation near the middle of the protein, likely causing a null phenotype (Sakube et al., 1997; this paper). CaV1 null mutants (egl-19(st556)) die as embryos due to a loss of muscle function during morphogenesis (Lee et al., 1997). We rescued the CaV1 null mutant using a muscle promoter expressed early in development; since this strain lacks CaV1 in the nervous system, we refer to it as ‘CaV1(Δns)’.

To determine whether these channels function cooperatively or in parallel, we tested for synthetic interactions between mutations of these channel types. The double mutant CaV1(Δns) RyR(-) is viable, and is no worse than the RyR null, consistent with their coupled function (Figure 1A). However, CaV1(Δns) CaV2(-) double mutants and RyR(-) CaV2(-) double mutants exhibit a synthetic lethal interaction. These data suggest that calcium influx from CaV1-RyR acts redundantly, and in parallel, with CaV2 to sustain neuronal function essential for viability.

![Figure 1.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig1-v2.jpg)

**Figure 1.:** (A) Viability of calcium channel double mutants. (B) Worm Tracks. Healthy animals were tracked for 5 minutes with a frame rate of 8 frames per second. The path the animal created was plotted, starting point is indicated, asterisks represent reversal events. (C) Total average distance animals travelled per animal during the 5 minute interval by genotype. Wild-type 71.2±9.5 mm. CaV1(Δns) 39.0±1.8 mm. CaV1(Δns)+rescue 74.4±10.5 mm. (D) Average speed, including both forward and backward bouts but excluding pauses, for the duration of the assay. Wild-type 294.9 µm/s±19.4 µm/s. CaV1(Δns) 133.8 µm/s±6.3 µm/s. CaV1(Δns)+rescue 331.7 µm/s±13.3 µm/s. (E) Average distance of forward locomotion between reversal events that animals travelled by genotype. Wild-type 12.2 mm ±2.0 mm. CaV1(Δns) 17.7 mm ±1.7 mm. CaV1(Δns)+rescue 15.3 mm ±4.0 mm. (F) Average duration of forward run between reversal events. Wild-type 41.9±8 s. CaV1(Δns) 14.1±1.3 s. CaV1(Δns)+rescue 46.2±10.5 s. (G) Average number of reversal events per minute exhibited by animals by genotype. Wild-type 1.9±0.3 events. CaV1(Δns) 3.8±0.5 events. CaV1(Δns)+rescue 1.3±0.3 events. (H) Average distance travelled in reverse per animal by genotype. Wild-type 601.9±65.1 µm. CaV1(Δns) 413.2±56.8 µm. CaV1(Δns)+rescue 1026±111.1 µm. (I) Average duration of reversal run. Wild-type 2.2 +- 0.1 s. CaV1(Δns) 2.4+/-0.2 s. CaV1(Δns)+rescue 2.5 +- 0.2 s. Wild-type n=11, CaV1(Δns) n=16, CaV1(Δns)+rescue n=13. Error bars reported in SEM. Genotypes were blinded. One-way ANOVA with Tukey’s multiple comparisons was used to calculate p-value. *p<0.05, **p<0.005, ***p<0.001, ****p<0.0005. Data available as Figure 1—source data 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Example track from WT. The path the animal created was plotted, starting point is indicated, asterisks represent reversal events. (B) Example track from RyR(Δns). The path the animal created was plotted, starting point is indicated, asterisks represent reversal events. (C) Total distance. Wild-type 78.2±8.9 mm RyR(Δns) 10.2±13.6 mm. (D) Average speed. Wild-type 329.3 µm/s±18.7 µm/s RyR(Δns) 285.1±8.8 µm/s. (E) Forward distance. Wild-type 10.0 mm ±1.6 mm RyR(Δns) 14.5±5.8 mm. (F) Forward run duration. Wild-type 32.8±6.3 s. RyR(Δns) 27.5±3.6 s. (RyR(Δns) n=11). (G) Reversals per minute. Wild-type 2.2±0.3 events. RyR(Δns) 2.6±0.5 events. (H) Distance travelled in reverse. Wild-type 789.0±90 µm. RyR(Δns) 838.8±136.7 µm. (RyR(Δns) n=11). (I) Duration of reversal run. Wild-type 2.4 +- 0.1 s. RyR(Δns) 2.6±0.4 s. Wild-type n=15 RyR(Δns) n=17. Error bars reported in SEM. Genotypes were blinded. Brown-Forsyth ad Welch ANOVA with Dunnett’s T3 multiple comparisons was used to calculate p-value. *p<0.05, **p<0.005, ***p<0.001, ****p<0.0005.

CaV1(Δns) animals are uncoordinated, and the phenotypes are fully rescued by the expression of CaV1 in the nervous system (Figure 1B). To determine the role of CaV1 on locomotion, we characterized animal movement on agar plates using worm tracker software. CaV1(Δns) worms moved slower than wild-type worms, and consequently travelled shorter distances during the observation period. Additionally, CaV1(Δns) worms reversed more frequently, had shorter durations of forward movement, and moved forward shorter distances than wild type (Figure 1C–G). The distance travelled while backing tended to be shorter in the CaV1(Δns) animals; whereas the rescued animals travelled longer distances in reverse, about a full body length (Figure 1H). Reversals in all genotypes were similar in duration (Figure 1I). These results indicate that the speed of locomotion is dependent on CaV1 function in the nervous system, and that CaV1 also biases the bistable locomotory circuit toward forward locomotion (Zheng et al., 1999).

If CaV1 and RyR are functioning in the same pathway then worms lacking expression of RyR in the nervous system should phenotypically mimic CaV1(Δns). unc-68(syb216) animals lack the neuronal-specific isoform of RyR, but express ~10% levels of RyR in neurons from the muscle promoter (Ma et al., 2016; Marques et al., 2020). We will refer to this strain as RyR(Δns) for simplicity. Like CaV1(Δns) animals, RyR(Δns) animals are significantly slower than the wild type; however, they do not exhibit the same increase in reversal frequency (Figure 1—figure supplement 1A–I).

### CaV2 and CaV1 regulate distinct pools of synaptic vesicles

To determine if CaV1 is playing a direct role in synaptic transmission, we recorded spontaneous synaptic currents at neuromuscular junctions. Body muscles were voltage-clamped at a holding potential of –60 mV, and miniature postsynaptic currents recorded under high chloride internal pipette conditions, in which GABA and ACh release generates inward currents. Miniature postsynaptic currents (‘minis’) are caused by the release of neurotransmitter from one or a few synaptic vesicles. In the nematode, vesicle fusion is graded, that is, it is proportional to membrane depolarization (Liu et al., 2014; Liu et al., 2009); high frequency of these 'tonic' minis drives calcium action potentials in the muscles (Liu et al., 2011).

The rate of miniature postsynaptic currents (minis/s) compared to the wild type (32.2+/-2.1 minis/s) was significantly reduced in each of the single mutants, CaV2 (18.7+/-3.5 minis/s), CaV1(Δns) (18.7+/-3.6 minis/s), and RyR (20.9+/-1.5 minis/s) (Figure 2A and B). Because CaV2 CaV1(Δns) double mutants are synthetic lethal, we acutely blocked CaV1 using 10 µM nemadipine (Kwok et al., 2006). Nemadipine reduced minis in the wild type (+nema 18.4+/-2 minis/s) to a similar level as the CaV1(Δns) mutant alone, and did not further reduce mini frequency when paired with the CaV1(Δns) mutant (+nema 19.1+/-2.7 mini/s). These data demonstrate that nemadipine is an effective blocker of CaV1 and does not block CaV2.

![Figure 2.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig2-v2.jpg)

**Figure 2.:** (A) Spontaneous miniature currents mediated by CaV1 and RyR are inhibited by nemadipine. Wild-type: 32.2±2.1 minis/s n=8, wild type with nemadipine (10 µM): 18.4±2.1 mini/s n=8. CaV1(Δns): 18.7±3.1 minis/s n=9, with nemadipine 19.1±2.7 mini/s n=6. RyR(-): 20.9±1.5 minis/s n=7, with nemadipine 20.7±1.3 mini/s n=7. CaV2(-): 18.7±3.5 minis/s n=7, with nemadipine 1.7±0.6 mini/s n=9. One-way ANOVA with Dunnett’s multiple comparisons test and one-way ANOVA with Tukey’s multiple comparisons tests were used to calculate significance. GABA and ACh release generated inward currents in this preparation. (B) Sample traces of spontaneous release in 0.5 mM extracellular calcium. GABA and ACh release generated inward currents in this preparation. (C) Spontaneous miniature currents from acetylcholine release are reduced with pharmacological block of CaV1 and RyR. Wild-type: 21.7+/-1 mini/s n=13. Wild-type +nemadipine (10 µm): 15.8+/-0.7 mini/s n=11. Wild-type +dantrolene: 12.36+/-0.6 mini/s n=12. Wild-type +nemadipine and dantrolene: 12.2+/-0.9 mini/s n=11. RyR(ns-): 15.9+/-0.6 mini/s n=13. Brown-Forsythe and Welch ANOVA with T3 Dunnett’s multiple comparisons test were used to calculate significance. (D) Dantrolene reduces miniature current amplitude from acetylcholine release. Wild-type: 12.4+/-0.6 pA n=13. Wild-type +nemadipine (10 µm): 10.1+/-0.6 pA n=11. Wild-type +dantrolene: 8.0+/-0.3 pA n=12. Wild-type +nemadipine and dantrolene: 8.2+/-0.24 pA n=11. RyR(ns-): 9.5+/-0.4 pA n=13. Brown-Forsythe and Welch ANOVA with T3 Dunnett’s multiple comparisons test were used to calculate significance. (E) Frequency distribution of mini amplitudes from acetylcholine release in wild-type and with pharmacological block of CaV1 or RyR, normalized to mode. (F) Quantal analysis of post-synaptic amplitudes from wild-type animals treated with nemadipine. Mini amplitudes were transformed into 1 pA bins. The wild-type +nema distribution of amplitudes was fit with a three-term Gaussian convolution to isolate 1, 2 and 3 quantal events, each centered around the mode: 7±1 pa, 14±2 pa and 21±3 pa (khaki). 1-quanta (rust) accounted for 67% of fusions. 2-quanta (butterscotch) 18%. 3-quanta (violet) 15%. (G) Quantal analysis of post-synaptic amplitudes from wild-type animals treated with dantrolene and nemadipine. Mini amplitudes were transformed into 1 pA bins. The wild-type +nema distribution of amplitudes was fit with a three-term Gaussian convolution to isolate 1, 2, and 3 quantal events, each centered around the mode: 6±1 pa, 12±2 pa and 18±3 pa (blue). (blue). 1-quanta (rust) accounted for 75% of fusions. 2-quanta (butterscotch) 15%. 3-quanta (violet) 10%. For all recordings, Vm = –60 mV, 0.5 mM calcium. Error bars reported in SEM. *p<0.05, **p<0.005, ***p<0.001, ****p<0.0005. Data available as Figure 2—source data 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) CaV2 and CaV1-RyR contribute additively to tonic release. GABA and ACh release generated inward currents in these preparations. Muscles were voltage-clamped, and tonic miniature synaptic currents recorded in 0.5 mM extracellular calcium: wild type: 33±4 minis/s, n=8; CaV2(-): 19±4 minis/s n=7, CaV1(Δns): 21±3 minis/s n=7, RyR(-): 20±4 minis/s n=9. CaV2(Δnmj) RyR(-): 11±2 minis/s n=7, CaV2(Δnmj) CaV1(Δns): 13±2 minis/s n=7, CaV1(Δns) RyR(-): 20±2 minis/s n=7. Welch’s t-test was used to calculate significance (B) RyR is required for large-amplitude spontaneous events. At 0.5 mM calcium, wild-type 23±2 pA n=8, and CaV2(-): 23±2 pA n=7, CaV1(Δns): 21±1 pA n=7, RyR(-): 16±2 pA n=9. CaV2(Δnmj) RyR(-): 38±3 pA n=7, CaV2(Δnmj) CaV1(Δns): 26±3 pA n=7, and CaV1(Δns) RyR(-): 17±2 pA n=7. Welch’s t-test was used to calculate significance. (C) Cumulative distribution plot of mutant amplitudes. (D) Frequency distribution plot of CaV mutant miniature current amplitudes normalized to the mode. (E) Frequency distribution plot of ryanodine mutants with reduced amplitudes, normalized to mode. (F) The ryanodine receptor mediates large amplitude tonic miniature currents. Wild type 22.3±1.9 pA n=8, wild type with nemadipine 22.6±2.1 pA n=8. CaV2(-): 22.1±3.5 pA n=7, CaV2(-) with nemadipine 24.1±3.4 pA n=9. CaV1(Δns): 23.4±3.1 pA n=9, CaV1(Δns) with nemadipine 29.4±.9 pA n=6. RyR(-): 15.5±0.6 pA n=7, RyR(-) with nemadipine 14.0±0.9 pA n=7. One-way ANOVA with Dunnett’s multiple comparisons test and Welch’s t-test were used to calculate significance. GABA and ACh release generated inward currents in this preparation. (G) Cumulative distribution plot of miniature current amplitudes. GABA and ACh release generated inward currents in this preparation. Error bars reported in SEM. *p<0.05, **p<0.005, ***p<0.001, ****p<0.0005 Data available as Figure 2—figure supplement 1—source data 1.

Nemadipine application in the RyR mutant did not exacerbate the phenotype (‘RyR(-)+nema’, 20.7+/-1.3 mini/s), indicating that CaV1 and RyR function is coupled at neuromuscular junctions. To determine if the plasma membrane channels CaV1 and CaV2 are required together for all neurotransmitter release, we blocked CaV1 in the CaV2 null mutant. Application of nemadipine almost completely abolished mini frequency in the CaV2 mutant (+nema 1.7+/-0.6 mini/s). We conclude that all vesicle fusion at neuromuscular junctions relies on CaV1 and CaV2, each contributing about half of the minis, in agreement with an earlier study (Tong et al., 2017). In addition, calcium influx through CaV1 is not sufficient for vesicle fusion; CaV1 relies on internal calcium stores released by RyR to fuse synaptic vesicles.

We further tested the roles of calcium channels using double mutants. We found that the rate of minis in the CaV1(Δns) RyR double mutant (19.6+/-2 mini/s) was similar to the single CaV1(Δns) and RyR mutants, supporting the hypothesis that CaV1 relies on coupling to RyR to activate neurotransmitter release. Because CaV1 CaV2 double mutants exhibit synthetic lethality (Figure 1A), we generated a mosaic CaV2 strain in which the channel was expressed in acetylcholine head neurons using a tissue-specific promoter (‘Punc-17h’) in the CaV2 null mutant, referred to as ‘CaV2(Δnmj)’ (Hammarlund et al., 2007; Topalidou et al., 2016). Expression of CaV2 in head neurons bypassed the synthetic lethality of both the CaV1(Δns) CaV2(-) double mutant, and the RyR(-) CaV2(-) double mutant, but the rescued animals exhibit a synthetic paralyzed phenotype. The mini rates of CaV2(Δnmj) CaV1(Δns) double mutants (12.8+/-2.4 mini/s) and CaV2(Δnmj) RyR double mutants (11.3+/-2.1 mini/s) were significantly reduced, but not completely abolished (Figure 2—figure supplement 1A). The remaining neuronal activity in these strains is likely due to CaV2 expression in the sublateral cord motor neurons located in the head and extend long processes that synapse onto body muscles. In summary, these results demonstrate that CaV1 and RyR are interdependent, and act in parallel to CaV2.

To confirm that the reduction of minis observed in the unc-68 null mutant was due to an acute loss of RyR function rather than a developmental defect, we blocked RyR by applying dantrolene (10 µM), a specific RyR inhibitor (Song et al., 1993; Xu et al., 2001), either alone or in combination with the CaV1 blocker nemadipine. The recordings were performed using a low-chloride pipette solution at a holding voltage equal to the chloride equilibrium potential so that only minis mediated by acetylcholine were detected. The frequency of minis was reduced in all treatments compared to the wild type (Figure 2C; wild type 21.7±1.0 mini/s; dantrolene alone 12.36+/-0.6 mini/s; nemadipine alone 15.8+/-0.7 mini/s; dantrolene plus nemadipine 12.2+/-0.9 mini/s). Furthermore, nemadipine did not exacerbate the inhibitory effect of dantrolene on minis. Again, CaV1 is reliant on RyR for neurotransmission.

To confirm that RyR is acting presynaptically we analyzed strains rescued in neurons or in muscle. Previously, we rescued minis in a null mutant by expressing wild-type unc-68 in neurons but not muscle cells, suggesting that RyRs regulate minis by acting presynaptically (Liu et al., 2005). Expression from unc-68 is driven by an upstream muscle promoter and a downstream neuronal promoter (Chen et al., 2017; Marques et al., 2020). To confirm the presynaptic function of RyRs, we recorded minis from the RyR(Δns) mutant unc-68(syb216) (Figure 2C). The frequency of minis was significantly reduced compared to the wild type (wild type 21.7±1.0 mini/s; RyR(Δns) 15.9±0.6 mini/s; p=0.001). The reduction in minis in RyR(Δns) supports the conclusion that RyR is required presynaptically for normal levels of synaptic vesicle fusion. Mini frequency in RyR(Δns) was slightly higher than pharmacological block by dantrolene (12.36+/-0.6 mini/s; p=0.002). This result is consistent with the observation ~10% of RyR transcripts in neurons are expressed from the ‘muscle’ promoter in this strain (Marques et al., 2020).

### RyR is required for multiquantal release

The amplitude of a miniature currents recorded from the muscle reflects the amount of neurotransmitter released by the synaptic bouton. The mode of mini amplitudes represents miniature currents from single vesicle fusions – single fusions are the most probable event. Using recording conditions in which only acetylcholine currents are detected, the modal value of miniature currents was similar in all strains (wild type 8 pA, CaV1 block nemadipine 7 pA, RyR block dantrolene 5 pA, CaV1 +RyR block nemadipine +dantrolene 6 pA, RyR(Δns) 6 pA), suggesting that the receptor field is similar for most single vesicle fusions. Simultaneous fusion of multiple vesicles – multiquantal release – will increase the mean current amplitude. The mean current amplitude from acetylcholine release was significantly reduced by pharmacological or genetic block of RyR in neurons (wild type:12.4±0.6 pA; dantrolene: 8.0±0.3 pA; RyR(Δns): 9.5±0.4 pA) (Figure 2D and E). The presence of large current events was not reduced by mutation of CaV2 (Figure 2—figure supplement 1D, G). Block of CaV1 by nemadipine caused a decrease in the mean current amplitude (wild type:12.4±0.6 pA; nemadipine: 10.1±0.6 pA; nemadipine +dantrolene: 8.2±0.24 pA), suggesting that CaV1 contributes to multiquantal release.

Similar results were observed in mutants lacking these channels, using recording conditions in which both acetylcholine and GABA release were detected. The modal value was similar in all genotypes (WT 10 pA, CaV1Δns 10 pA, RyR 11 pA, CaV2 8 pA, WT +nema 10 pA, CaV1Δns +nema 8 pA, RyR +nema 10 pA, CaV2 +nema 11 pA). However, the mean amplitude of miniature currents was reduced in the RyR(-) mutant (15.5±0.6 pA) compared to the wild type (22.3±1.9 pA; Figure 2—figure supplement 1B–G). Together, these data indicate that CaV1 is coupled to the ryanodine receptor at synapses to drive multiquantal release.

CaV2 is also functionally coupled to RyR to drive multiquantal release in acetylcholine motor neurons. When CaV1 channels are blocked by nemadipine, the remaining miniature currents rely on CaV2 and RyR (Figure 2D), and mini amplitudes arising solely from CaV2 were reduced by further blocking RyR (nemadipine: 10.1+/-0.6 pA; dantrolene +nemadipine: 8.2+/-0.24 pA), suggesting that RyR also responds to calcium from CaV2. To estimate individual contributions to multiquantal release, we fit the distribution of current amplitudes assuming simultaneous fusions from multiple single vesicles (Figure 2E). In the presence of CaV2 and RyR 34% of currents are multiquantal; blocking RyR reduces multiquantal release to 25% (Figure 2F and G). These fits indicate that RyR contributes to CaV2-mediated vesicle fusion by enhancing multiquantal events, though multiquantal events can also be attributed to CaV2.

Together, these data demonstrate that CaV2 and CaV1 channels regulate the release of separate synaptic vesicle pools at neuromuscular junctions. CaV1 requires the ryanodine receptor for any vesicle fusion, consistent with the known relationship of these channels in calcium-activated calcium release. Calcium influx through CaV2 is sufficient to fuse vesicles on its own, although neurotransmitter release is amplified by calcium release from internal stores via the ryanodine receptor.

### CaV2 and CaV1 mediate fusion of separate vesicle pools at single synapses

The physiology data suggest that CaV2 and CaV1 mediate the release of distinct synaptic vesicle pools at neuromuscular junctions. To determine whether these calcium channels regulate spatially distinct pools at the same synaptic varicosity, time-resolved ‘flash-and-freeze’ electron microscopy was used to characterize fusing vesicle pools (Watanabe et al., 2013). Transgenic animals expressing channelrhodopsin (ChIEF) in acetylcholine neurons were loaded into a high-pressure freezing chamber and stimulated with a 20 ms light pulse to depolarize neurons and activate synaptic calcium channels. Animals were frozen 50ms after stimulation; control animals were treated identically but not stimulated. Frozen samples were fixed by freeze substitution, embedded in plastic, and sectioned for electron microscopy (Watanabe et al., 2013). Docked vesicles were defined as those in contact with the plasma membrane; docking was scored blind to treatment and genotype (Figure 3A and B). The distance from the dense projection to the docked vesicle was plotted on the X-axis (Figure 3C). Decreases in docked vesicles after stimulation were assumed to be the result of synaptic vesicle fusion, although calcium influx could cause some vesicles to undock and return to the cytoplasm (Kusick et al., 2020).

![Figure 3.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig3-v2.jpg)

**Figure 3.:** (A) Docked vesicles (black arrows) are present at synapses in electron micrographs of unstimulated animals. (B) Docked vesicles are reduced 50ms after channelrhodopsin stimulation. (C) Vesicle fusion. The number of synaptic vesicles that fuse can be calculated as the number of docked vesicles lost by stimulation. Dense projection indicated in gray in the 0 nm bin. (D–H) Average number of docked vesicles per synapse at a given distance from the dense projection with, or without, light stimulation of channelrhodopsin. (D) Wild-type animals exhibit fewer docked vesicles at all locations after stimulation. Wild type (no stimulation), n=26 synapses. Wild type (stimulated) n=24 synapses. (E) In the CaV2 null mutant unc-2(lj1), vesicles fuse greater than 33 nm from the dense projection; vesicle fusion is reduced directly adjacent to the dense projection. No stimulation n=14, stimulated n=27 synapses. (F) The CaV1 hypomorphic mutant egl-19(n582) exhibits reduced fusions at all distances. No stimulation n=29 synapses, stimulated n=16 synapses. (G) The RyR mutant unc-68(e540) exhibits fusions adjacent to the dense projection, but lacks fusions of lateral vesicles. No stimulation n=11 synapses, stimulated n=17 synapses. (H) The CaV1 CaV2 double mutant, egl-19(n582) unc-2(lj1), lacks fusion of all docked vesicles after stimulation. No stimulation n=24 synapses, stimulated n=17 synapses. Micrographs were segmented blind to treatment and genotype. Bin size was fixed at 33 nm to be consistent with our section thickness in case 3D reconstruction of synapses is required. Error bars SEM, N=2 animals for each condition. Data available as Figure 3—source data 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Docked vesicles adjacent to the dense projection in calcium channel mutants. Unstimulated: wild type: 3.7+/-0.5 vesicles. CaV2(-): 5.6+/-0.6 vesicles. CaV1(-): 4.5+/-0.4. vesicles. RyR(-): 5.0+/-0.4. CaV2(-) CaV1(-): 5.6+/-0.7. Stimulated: wild type: 1.3+/-0.2. CaV2(-): 4.8+/-0.4. CaV1(-): 3.1+/-0.7. RyR(-): 2.3+/-0.4. CaV2(-) CaV1(-): 5.0+/-0.6. (B) Docked vesicles in the intermediate active zone in calcium channel mutants. Unstimulated: wild type: 3.1+/-0.6 vesicles. CaV2(-): 9.2+/-1.0 vesicles. CaV1(-): 6.4+/-0.7 vesicles. RyR(-): 7.0+/-0.7. CaV2(-) CaV1(-): 5.2+/-0.7 vesicles. Stimulated: wild type: 1.5+/-0.3 vesicles. CaV2(-): 2.8+/-0.5 vesicles. CaV1(-): 3.2+/-0.4. RyR(-): 4.9+/-0.6. CaV2(-) CaV1(-): 8.0+/-1.2 vesicles. (C) Docked vesicles in the lateral active zone in calcium channel mutants. Unstimulated: wild-type: 16.7+/-1.9 vesicles. CaV2(-): 12.2+/-1.2 vesicles. CaV1(-): 7.6+/-0.9 vesicles. RyR(-): 3.8+/-1.0 vesicles. CaV2(-) CaV1(-): 9.4+/-1.0 vesicles. Stimulated: wild-type: 3.1+/-0.6 vesicles. CaV2(-):3.4+/-0.4 vesicles. CaV1(-): 3.9+/-0.8 vesicles. RyR(-): 4.1+/-0.6 vesicles. CaV2(-) CaV1(-): 8.2+/-1.5 vesicles. (D) Fusion probability of vesicles docked across the active zone in calcium channel mutants. To calculate the fusion probability at a zone, the mean number of docked vesicles after fusion was divided by the mean number of docked vesicles before fusion, and that result was subtracted from 1. Comparisons made with Chi-squared test. Wild type (no stimulation), n=26 synapses. Wild type (stimulated) n=24 synapses. CaV1(-) (no stimulation) n=29 synapses. CaV1(-) (stimulated) n=16 synapses. CaV2(-) (no stimulation) n=14, CaV2(-) (stimulated) n=27 synapses. RyR(-) (no stimulation) n=11 synapses. RyR(-) (stimulated) n=17 synapses. CaV2(-) CaV1(-) (control) n=24 synapses. CaV2(-) CaV1(-) (stimulated) n=17 synapses All multiple comparisons made with Brown Forsythe and Welch ANOVA with Dunnett’s T3. All single comparisons made with Welch’s T-test. Comparisons of fusion rates were performed using Chi-squared test. Error bars reported in SEM. *p<0.05, **p<0.005, ***p<0.001, ****p<0.0005.

To identify vesicle fusions associated with particular calcium channels, we analyzed the distribution of docked vesicles in mutant animals. In unstimulated animals, docked vesicles were clustered around dense projections, although many were observed at lateral regions extending hundreds of nanometers from dense projections. Docked vesicles were uniformly depleted after stimulation in wild-type animals (Figure 3D). In mutants lacking CaV2 channels, docked vesicles were selectively retained adjacent to the dense projection, but fused normally in regions distal from the dense projection. These results indicate that CaV2 is essential for vesicle fusion at sites adjacent to the dense projection (Figure 3E). Complete loss of both CaV2 and CaV1 function in the nervous system is lethal (Figure 1A). Therefore, to assay mutation of both channels in the nervous system we used a weak allele of CaV1; the hypomorph egl-19(n582) is viable in double mutants with unc-2(lj1). Mutation of the CaV1 channel reduced fusion broadly, although significant vesicle fusions were observed within 100 nm of the dense projection (Figure 3F). In the absence of RyR only CaV2 is functional, and vesicle fusions were only observed in the 33 nm pool — directly adjacent to the dense projection (Figure 3G). The CaV1 CaV2 double mutant exhibited no change in the number and distribution of docked synaptic vesicles after stimulation (Figure 3H). These data indicate that CaV2 and CaV1 act on two spatially distinct pools of synaptic vesicles at the same synapses in C. elegans: a central pool dependent on CaV2 calcium channels and a lateral pool dependent on CaV1 and RyR.

To more finely partition the fusion domains for which each channel, we binned micrographs into three zones: adjacent to the dense projection (0–33 nm), intermediate active zone (33–165 nm), and lateral active zone (165–594 nm). Baseline docking was increased in the 0–33 nm bin in the CaV2(-) mutants, this trend is consistent with decreased tonic fusion adjacent to the dense projection (Figure 3—figure supplement 1A), and release probability of vesicles is reduced adjacent to the dense projection in CaV2(-) mutants (Figure 3—figure supplement 1D).

In the intermediate active zone (33–165 nm), there was no change in the baseline docking of any mutant (Figure 3—figure supplement 1B). However, we observed identical fusion defects in the intermediate zone in the CaV2(-) mutant and RyR(-) mutant, which suggests CaV2 activates RyR to release calcium from internal stores. Activation of RyR by CaV2 is consistent with the multiquantal release mediated by these channels (Figure 2E–G).

In the distal active zone (165–594 nm), the probability of vesicle fusion was reduced in CaV1(-) mutants, RyR(-) mutants, and CaV2(-) CaV1(-) double mutants, but slightly increased in CaV2(-) mutants (Figure 3—figure supplement 1D). An increase in fusion at distal sites in CaV2 mutants might be due to compensatory effects in the expression or organization of CaV1 and RyR.

Together, electron microscopy indicates that CaV2 mediates fusion of vesicles adjacent to the dense projection, and that CaV1 mediates fusion of vesicles at lateral sites. The ryanodine receptor is essential for vesicle fusion mediated by CaV1 at lateral sites and contributes to vesicle fusion by CaV2 near the dense projection.

### CaV2 and CaV1 differentially localized at synapses

The ultrastructural data suggests that distinct calcium channels act at spatially separate areas of the active zone. To determine if these calcium channels are physically located at these sites, we used fluorescence microscopy. We modified the endogenous genes to encode tags for synthetic fluorescent ligands and performed three-color imaging using the dense projection as an anatomical fiducial at the center of the synapse. Because C. elegans synaptic varicosities are less than 1 μm in diameter, superresolution microscopy was required to resolve channel clusters. A segment of the dorsal nerve cord was imaged, and the region of imaging was restricted to a narrow band to avoid potential complications by CaV1 expression in muscle. All imaging was conducted on living, acutely anesthetized nematodes.

Multiple tagging sites were tested for all genes, but in some cases the tags disrupted function. Therefore, we tagged internal sites within regions of poor conservation (Figure 4—figure supplement 1A and B). For example, CaV2 was tagged with HALO (Los et al., 2008) in the second extracellular loop near the N-terminus (Kurshan et al., 2018; Schwartz and Jorgensen, 2016). The strains used for three-color imaging exhibited normal morphology and appear to move like wild-type animals, suggesting the tagged proteins are functional. Analysis of specific movements indicated that most locomotory responses are normal; however, the frequency of reversals was increased in all multiply tagged strains (Figure 4—figure supplement 1E–I).

To confirm that the pattern of calcium channels in our fluorescence images matched the arrangement of dense projections, we reconstructed 20 µm of the dorsal nerve cord from serial sections with electron microscopy (Figure 4A). Dense projections at neuromuscular junctions were spaced roughly 1 µm apart in the reconstruction (1.02 / µm). This matches well to the distribution of CaV2 clusters (1.10+/-0.16 µm) along the dorsal cord by super-resolution microscopy, and is consistent with previous studies demonstrating that CaV2 /UNC-2 channels are localized to dense projections by immuno-electron microscopy (Gracheva et al., 2008). To further demonstrate that CaV2 is localized to the dense projection, we compared CaV2 localization with CRISPR-tagged presynaptic active zone proteins, including Neurexin (nrx-1), Magi (magi-1), SYDE (syd-1), Liprin-α (syd-2), RIMBP (rimb-1), and α-Catulin (ctn-1). The endogenous genes were tagged with the fluorescent protein Skylan-S and colocalization assessed with HALO-tagged CaV2 in the dorsal nerve cord of transgenic worms. CaV2 colocalized with all these proteins (Figure 4B), indicating that it is indeed localized at the dense projection.

![Figure 4.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig4-v2.jpg)

**Figure 4.:** (A) 20 micron reconstruction of the wild-type C. elegans dorsal nerve cord. Dense projections are highlighted to compare to superresolution images below. Scale bar 1 µm, section thickness 100 nm. (B) CaV2 colocalizes with cytomatrix active zone proteins. Super-resolution images of Skylan-S-tagged cytomatrix protein homologs in C. elegans NRX-1, RIMB-1, SYD-2, SYD-1, MAGI-1, CTN-1, ELKS-1 compared to CaV2-HALO in the same animal. (C) ELKS and CaV2 clusters form approximately 1 / µm along the dorsal nerve cord from super-resolution image analysis. Clusters were quantified for over dorsal nerve cords with an average length of 17.8 µm, N=8 animals (D) Localization plot tool (Proberuler) example diagram of a single ELKS (green) and CaV2 (purple) synapse. Cluster centers are marked by solid lines. (E) Histogram of CaV2 localization distance to ELKS center of mass axis from example ELKS and CaV2 synapse.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A–C), Tagging strategies and sites used for CRISPR/Cas9 tagging of the endogenous loci for CaV2, CaV1, and RyR. Regions with low conservation were targeted for insertion of tags into the genomic locus of each gene, unc-2, egl-19, and unc-68, respectively. (D) Tagging strategy at the endogenous locus of unc-13 CRISPR / Cas9. The C-terminal tag labels all isoforms of UNC-13. The N-terminal tag labels the UNC-13S isoform. In addition, it will label a rare transcript UNC-13-LMR (~2% of transcripts), that includes the C2A domain, sequences upstream of UNC-13S, and all sequences included in UNC-13S (https://wormbase.org/ version ws284). Behavioral analysis of imaging strains. (E) Total distance travelled: wild-type 82.7±6.1 mm. EG9617 110.0±16.1 mm. EG9667 143.1±10.1 mm. EG9723 127.7±8.3 mm. EG10117 112.7±15.3 mm. (F) Speed: wild-type 301.6±22.1 µm/s. EG9617 263.5±8.8 µm/s. EG9667 288.0±5.4 µm/s. EG9723 249.0±8.3 µm/s. EG10117 292.4±9.2 µm/s. (G) Reversals per minute: wild-type 1.9±0.5 reversals/min. EG9617 5.0±0.8 reversals/min. EG9667 4.9±0.6 reversals/min. EG9723 7.1±0.7 reversals/min. EG10117 4.9±0.8 reversals/min. (H) Average length of forward run: wild-type 11.9±2.8 mm. EG9617 4.5±0.6 mm. EG9667 7.5±2.4 mm. EG9723 3.6±0.4 mm. EG10117 6.3±1.1 mm.(I) Average length of backward run: wild-type 0.64±0.09 mm. EG9617 0.49±0.05 mm. EG9667 0.78±0.1. EG9723 0.6±0.03 mm. EG10117 0.54±0.09 mm. wild-type n=7. EG9617 n=15. EG9667 n=13. EG9723 n=15. EG10117 n=14. Error bars reported in SEM. Genotypes were blinded. Brown-Forsyth ad Welch ANOVA with Dunnett’s T3 multiple comparisons was used to calculate p-value. *p<0.05, **p<0.005, ***p<0.001, ****p<0.0005.

ELKS clusters in particular are tightly associated with CaV2 clusters and exhibit the same 1 µm spacing (Figure 4C), and serves as a synaptic fiducial. To quantify the distribution of CaV2 relative to ELKS, the center of mass of the cluster centers was determined, an X-axis was plotted between the two cluster centers, and localizations were placed onto a 2D plot (Figure 4D). The ELKS center of mass was defined as the origin, and the distance of each CaV2 localization to the Y-axis of the ELKS cluster was assigned as an axial coordinate. These distances were collapsed onto a 1D plot, distances were binned and frequency plotted (Figure 4E). These plots were then used to calculate mean distributions of proteins from multiple synapses. CaV2 clusters and ELKS clusters were similar in diameter (297 nm vs 294 nm, respectively, n=26 synapses). The cluster centers are slightly offset (Ᾱ=124 nm), so that 62% of ELKS localizations were within a CaV2 cluster (Figure 5A–C). The offset could indicate that the clusters overlap but are not coincident. Alternatively, these proteins may be perfectly colocalized but differ in our plots due to the positions of the tags on the proteins; specifically, CaV2 was tagged on the extracellular side in the synaptic cleft, whereas ELKS was tagged at the C-terminus on the intracellular side. In summary, CaV2 is tightly clustered and associated with an ELKS cluster; the offset may simply be due to tagging sites and the length of the proteins.

![Figure 5.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig5-v2.jpg)

**Figure 5.:** (A, B) Localization microscopy plots of the dorsal nerve cord. ELKS is tagged with Skylan-S. The CaV2-HALO ligand is HTL-JF646, and the CaV1-SNAP tag ligand is STL-JF549pa. (A) CaV2 (magenta) colocalizes with dense projections labeled with ELKS (cyan). CaV1-SNAP (yellow) is largely excluded from the dense projection; and scattered in the synaptic varicosity. Scale bar = 1 µm. (B) Distributions of CaV2 and CaV1 in a synapse. Dense projections labeled with ELKS (cyan) colocalize with CaV2 (magenta), but not CaV1 (yellow). Scale bar = 250 nm. (C) Quantitation of protein localizations from multiple synapses. The center of mass of localizations was calculated from 2D plots. An axis between the centers was fixed and all localizations collapsed onto the axis. Localizations were combined into 33 nm bins, to match the electron microscopy analysis, and plotted as the fraction of total localizations. Data were collected and combined from n=26 synapses, N=5 animals. Data available as Figure 5—source data 1.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Comparison of endogenously-tagged CaV1 and neuronally expressed rescue of CaV1. (A) Endogenous CaV1 tag: Localization microscopy images of dorsal nerve cord with CaV1-SNAP stained with STL-JF549cp (yellow), CaV2-HALO stained with HTL-JF646 (purple), and Giant Ankyrin-Skylan-S (red). scale bar = 1 µm. (B) Exogenous CaV1 in the CaV1(Δns) strain. In the CaV1(Δns) background, CaV1 was rescued in neurons using a single copy transgene insertion of Psnt-1 promoter driving CaV1-HALO in neurons. Localization microscopy images of dorsal nerve cord. Dorsal cord of animals labelled with neuronal CaV1-HALO stained with HTL-JF646 (purple), Giant Ankyrin-SNAP stained with TMR-Star (red) and RIMBP-Skylan-S (cyan). scale bar = 1 µm. (C) Neuronal CaV1 colocalizes with LIN7 expressed in acetylcholine neurons. In the CaV1(Δns) background, CaV1 was rescued in neurons using a single copy transgene insertion of Psnt-1 promoter driving CaV1-HALO in neurons and stained with HTL-JF646. LIN7 was tagged with SNAP and stained with STL-JF549cp, and was expressed in acetylcholine neurons using the unc-129 promotor as an extrachromosomal array. scale bar = 1 µm. Localization microscopy images of dorsal nerve cord. Dense projections are marked by RIMBP-Skylan-S. (D) Single synapse analysis of LIN7, CaV1, RIMBP. Dense projections are marked by RIMBP-Skylan-S. In the CaV1(Δns) background, CaV1 was rescued in neurons using a single copy transgene insertion of the Psnt-1 promoter driving CaV1-HALO, and stained with HTL-JF646. LIN7 was expressed in acetylcholine neurons using the Punc-129 promotor as an extrachromosomal array, and tagged with SNAP and stained with STL-JF549cp and. Scale bar = 250 nm. (E) Cumulative distribution plot of Psnt-1:CaV1-HALO to RIMBP-Skylan-S center, and LIN7 tagged with SNAP to RIMBP-Skylan-S center measured from synaptic regions. n=24 synapses, N=5 animals. Data available as Figure 5—figure supplement 1—source data 1.

In contrast to CaV2, CaV1 was broadly distributed as dispersed puncta in the synaptic bouton ('cluster' diameter 869 nm), and is largely excluded from ELKS and CaV2 clusters (Figure 5A). Although dispersed, CaV1 usually exhibits a site of high density that is about 250 nm from the ELKS and CaV2 clusters (262 nm and 274 nm, respectively; Figure 5C). Although CaV1 is largely excluded from CaV2 clusters, the clusters often abut one another (Figure 5B, see Figure 10 for more examples).

To confirm that the CaV1 localizations are presynaptic and not in the muscle or epidermis, we generated a HALO-tagged CaV1 under the pan-neuronal synaptotagmin promoter (Psnt-1). This construct was inserted in the CaV1(Δns) strain, and the transgene fully rescues locomotion and behavior (Figure 1B–I). For convenience of genetic crosses, we used RIM binding-protein (RIMBP/RIMB-1) as the dense projection marker. The overexpressed CaV1::HALO tended to be more punctate than the endogenously tagged protein (Figure 5—figure supplement 1A and B). CaV1 did not colocalize with RIMBP and the mean distance to the dense projection was similar to the endogenously tagged gene (endogenous CaV1 to ELKS, 262 nm; transgene CaV1 to RIMBP, 378 nm; Figure 5—figure supplement 1E). To demonstrate that CaV1 clusters are presynaptic as opposed to postsynaptic, we searched for potential binding partners that might colocalize with the CaV1 puncta. SHN-1(Shank) binds the C-terminus of CaV1 via its PDZ domain but is primarily postsynaptic (Pym et al., 2017). LIN-7 also contains a PDZ domain but is presynaptic and could serve as a scaffold for CaV1 (Butz et al., 1998; Hallam et al., 2002). We expressed LIN-7 in acetylcholine motor neurons using the unc-129 promoter (Figure 5—figure supplement 1D). CaV1 and LIN-7 localizations were overlapping, but distal to the dense projection marker RIMBP (Figure 5—figure supplement 1E). These data suggest that CaV1 is localized at presynaptic boutons in a separate domain from CaV2 channels.

If CaV1 and RyR function in the same vesicle fusion pathway as the physiology data suggests, they should be colocalized in motor neurons (Piggott and Jin, 2021). RyR was tagged with HALO at the N-terminus of the neuronal isoform (Figure 4—figure supplement 1C; Marques et al., 2020). RyR localizations were compared to CaV1 localizations and the dense projection marker ELKS (Figure 6A and B). RyR localizations were diffusely distributed, and lateral to the dense projection (ELKS to RyR center of mass distance: 393 nm; 25 synapses) (Figure 6C). RyR localizations were correlated with CaV1 (RyR to CaV1 center of mass: 166 nm). Visual inspection of the images suggested that RyR and CaV1 are often interdigitated in adjacent zones (Figure 6A). To characterize this relationship a nearest neighbor analysis was performed and revealed that 94% of RyR localizations were within 100 nm of a CaV1 localization (Figure 6D). CaV1 exhibits a slightly broader distribution; nevertheless, 82% of CaV1 localizations were within 100 nm of a RyR channel. The spatial correlation between CaV1 and RyR is consistent with the functional coupling observed by physiology and electron microscopy.

![Figure 6.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig6-v2.jpg)

**Figure 6.:** (A) CaV1 and RyR are adjacent along the dorsal nerve cord, lateral to the dense projection. Animals and HTL-JF646. Scale bar = 1 µm. CaV1-SNAP is labelled with STL-JF549pa, RyR-HALO is labelled with HTL-JF646, and dense projections are labeled by ELKS-Skylan-S. (B) RyR and CaV1 colocalize within synapses. Labelling as in ‘A’. Scale bar = 250 nm. (C) Distances from CaV1-SNAP localizations to center of ELKS-Skylan-S cluster versus ELKS localizations to ELKS center. Distances from RyR-HALO localizations to center of ELKS-Skylan-S cluster versus ELKS localizations to ELKS center. Distances from CaV1-SNAP localizations to the center of the RyR-HALO cluster versus RyR-HALO localizations to the RyR center. N=5 animals, n=25 synapses. (D) RyR and CaV1 are adjacent. Left, nearest neighbor analysis was performed on CaV1-SNAP localizations to find the nearest RyR-HALO localization. Right, nearest neighbor distances from RyR-HALO to CaV1-SNAP were calculated. n=5 animals, 25 synapses. Data available as Figure 6—source data 1.

### Different UNC-13 isoforms are associated with CaV1 and CaV2

Vesicle docking and SNARE priming require UNC-13 proteins. Null mutations in unc-13 nearly eliminate neurotransmission and vesicle docking in C. elegans (Hammarlund et al., 2007; Richmond et al., 1999). In most organisms, there are two types of Unc13 proteins, those with an N-terminal C2A domain, and those lacking the C2A domain (Dittman, 2019). Binding of the C2A domain to the scaffolding protein RIM activates Unc13 (Betz et al., 2001; Hu et al., 2013; Liu et al., 2019; Lu et al., 2006; Zhou et al., 2013). Unc13 isoforms which lack a C2A domain bind ELKS / CAST in flies and mice (Böhme et al., 2018; Kawabe et al., 2017). In C. elegans, the unc-13 gene encodes two major splice isoforms: a long isoform UNC-13L with a C2A domain, and a short isoform UNC-13S lacking a C2A domain. To determine whether UNC-13 colocalizes with CaV1 and CaV2, we edited the unc-13 locus to append Skylan-S to the C-termini of both major isoforms (‘UNC-13all’) (Figure 4—figure supplement 1D). Both CaV2 and CaV1 calcium channels were tightly associated with UNC-13 isoforms (Figure 7A–C). Nearest-neighbor analysis indicates that 99.7% of CaV2 channels were within 100 nm of an UNC-13 localization, and 89% of CaV1 channels were within 100 nm of an UNC-13 protein (Figure 7D).

![Figure 7.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig7-v2.jpg)

**Figure 7.:** Localization microscopy identifies CaV1 and CaV2 associated with ‘UNC13all’, which labels a C-terminal site common to all UNC-13 isoforms. (A) UNC-13all colocalizes with CaV1 and CaV2 along the dorsal nerve cord. Proteins are labelled with CaV2-HALO stained with HTL-JF646, CaV1-SNAP stained with STL-JF549, and UNC13all-Skylan-S. (B) UNC-13all colocalizes with CaV1 and CaV2 within synapses. Staining as in ‘A’. (C) Left, distances from CaV1-SNAP localizations to the center of the CaV2-HALO cluster, and CaV2-HALO localizations to the center of the CaV2-HALO cluster. Middle, distances from UNC13all-Skylan-S localizations to the center of the CaV2-HALO cluster. Right, distances from UNC13all-Skylan-S localizations to the center of the CaV1-SNAP cluster, n=5 animals, 25 synapses. (D) Left, nearest-neighbor distances between UNC13all and CaV1 and CaV2 localizations. Right, nearest neighbor analysis between UNC13all-Skylan-S and CaV2-HALO or CaV1-SNAP measured from synaptic regions, n=5 animals, 25 synapses. Data available as Figure 7—source data 1.

To determine if UNC-13 isoforms are differentially associated with calcium channels, we tagged the N-terminus of UNC-13S with Skylan-S. UNC-13S did not colocalize with CaV2 (peak-to-peak 319 nm) but was associated with CaV1 (Figure 8A–C). Nearest neighbor analysis indicates that 99% of UNC-13S localizations are within 100 nm of a CaV1 channel (Figure 8D). These data demonstrate that CaV1 channels are associated with UNC-13S at lateral sites. Although it is possible that UNC-13L is also at these lateral sites, UNC-13S can dock vesicles independent of UNC-13L. Rescue of unc-13 null animals with UNC-13S restores locomotion and mini frequency to about half of wild-type (Hu et al., 2013). In contrast to the null, mutants lacking UNC-13L have normal or elevated numbers of docked vesicles in lateral regions of the synapse (Hammarlund et al., 2007; Zhou et al., 2013), indicating that the UNC-13S isoform is capable of docking synaptic vesicles in the absence of UNC-13L (Hu et al., 2013). Together, the localization data, electron microscopy, and physiology indicate that UNC-13L is coupled to CaV2 at the dense projection, and UNC-13S is coupled to CaV1 and the ryanodine receptor at lateral sites.

![Figure 8.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig8-v2.jpg)

**Figure 8.:** Localization microscopy identifies CaV1 associated with UNC-13S which labels a n-terminal site common to a short isoform. (A) UNC-13S localizes with CaV1 along the dorsal cord, but not with CaV2. The endogenous protein tags CaV2-HALO was stained with HTL-JF646, CaV1-SNAP with STL-JF549, and imaged with Skylan-S-UNC-13S using single-molecule localization microscopy. (B) UNC-13S localizes with CaV1 within synapses. Strain was labelled as in ‘A’. (C) Left, distances from CaV1-SNAP localizations to the center of the CaV2-HALO cluster compared to CaV2-HALO localizations to their own center. Middle, distances from Skylan-S-UNC-13S localizations to the center of the CaV2-HALO cluster. Right, distances from Skylan-S-UNC-13S localizations to the center of the CaV1-SNAP cluster. N=5 animals, 25 synapses (D) Nearest-neighbor distances of CaV1-SNAP to Skylan-S-UNC-13S localizations. Nearest neighbor analysis of Skylan-S-UNC-13S to CaV1-SNAP measured from synaptic regions. N=5 animals, 25 synapses. Data available as Figure 8—source data 1.

## Discussion

Calcium channel classes tend to be associated with specific tissue functions: CaV2 (N, P/Q, R-type) with synaptic transmission, and CaV1 (L-type) channels with muscle contraction. Here, we demonstrate that both CaV2 and CaV1 channels drive vesicle fusion at C. elegans neuromuscular junctions and mediate the release of different synaptic vesicle pools. In electrophysiological assays, these pools are genetically separable and complementary. Flash-and-freeze electron microscopy revealed that CaV2 channels fuse vesicles near the dense projection at the center of the synapse; whereas CaV1 channels fuse vesicles at lateral sites in the same synapses. Super-resolution imaging indicates that CaV2 channels are compacted at the dense projection into 250 nm clusters, along with the active zone proteins ELKS, neurexin, α-Liprin, and RIMBP. CaV2 is associated with the long isoform of the docking and priming protein UNC-13L. By contrast, CaV1 is dispersed in the synaptic varicosity and is associated with the short isoform UNC-13S. Finally, vesicle fusion mediated by CaV1 is dependent on the ryanodine receptor, presumably to activate calcium release from internal stores (Figure 9).

![Figure 9.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig9-v2.jpg)

**Figure 9.:** Voltage-gated calcium channels localize to two distinct zones at the neuromuscular synapse of C. elegans. The CaV2 channel localizes to the dense projection along with ELKS, RIMBP, Neurexin, Liprin-alpha, SYDE, MAGI1, alpha-Catulin and the SNARE priming protein UNC-13L. CaV2 is required to fuse synaptic vesicles are docked directly adjacent to the dense projection. The second channel CaV1 is at a lateral site centered ~300 nm from the dense projection but can span hundreds of nanometers. CaV1 requires coupling to RyR to synaptic vesicles at the lateral site. These near and far pools utilize specific release machinery. Most UNC-13all localizes to the dense projection. However, some UNC-13 localizes with CaV1 at the lateral site. Isoform specific tagging shows UNC-13S localized with lateral site.

Participation of multiple classes of calcium channels at the same synapse may serve to tune the dynamics of neurotransmission (Dolphin, 2021). Different calcium sources could regulate the strength of output, dynamics of release, or even termination of synaptic activity. Below we discuss the potential contributions of channel numbers, clustering, distance to docked vesicles, and voltage-dependence to differential synaptic behavior.

### Counting calcium channels

The number of calcium channels per synapse can be estimated from the single molecule localization data (see Methods for details). CaV1 channels are dispersed in the synapse but often also form small clusters (Figure 10A, F and G). The number of CaV1 channels was calculated from the mean number of blinks per channel, as well as from the total photon flux, converging on 77±15 CaV1 channels per synapse (Figure 10B–E).

![Figure 10.](https://cdn.elifesciences.org/articles/81407/elife-81407-fig10-v2.jpg)

**Figure 10.:** (A) Superresolution images of C. elegans expressing CaV1::SNAP, CaV2::HALO. Animals were stained with HTL-JF646, STL-JF549cp. Clusters of calcium channels are indicated with colored wireframes. Scale bar = 250 nm. (B) Poisson distribution fitted to frequency distribution plot of number of blinks per channel. (C) CaV1 channel count based on number of total number of blink over blinks per channel. (D) Frequency distribution of number of photons per channel cluster. Inlay: Frequency distribution of number of photons per blink. (E) CaV1 channel count based on number of total photons over the mode of photons per channel. (F) Four example superresolution images of C. elegans expressing CaV1::SNAP, CaV2::HALO. Animals were stained with HTL-JF646, STL-JF549cp. A sample cluster of CaV1 was 142 nm in diameter, contained 113 blinks that on average emitted 806 photons. These blinks were localized with 15 nm precision at a 30ms frame rate. A sample CaV2 cluster was 274 nm in diameter, contained 281 blinks with an average emissions of 505 photons per blink. Blinks were localized with 29 nm precision at a 30ms frame rate. (G) Four example superresolution images of C. elegans expressing CaV1::SNAP, RyR::HALO. Animals were stained with HTL-JF646, STL-JF549pa. n=6 synapses N=3 animals. Error bars reported in SEM. CaV1 data available as Figure 10—source data 1. CaV2 data available as Figure 10—source data 2.

The ryanodine receptor images were suffused with high background fluorescence, and photon flux was not a reliable measure. Using the mean blinks per channel produces an estimate of 29±4 RYR channels per synapse (Figure 10G).

CaV2 channels are tightly localized to the dense projection (Figure 10F). In our images, the cluster appears as a solid mass; the overlap in localization precision made it impossible to assign blinks or photon flux to individual channels in the cluster. However, assuming the blinking rate of rhodamine dyes is similar to cyanine dyes (Helmerich et al., 2022), the frequency of blinking indicates that the cluster contains 101±16 CaV2 channels.

The ~100 CaV2 channels per synapse derived from our single molecule localization data is much higher than the ~35 CaV2.1 channels determined by immunogold labelling synapses in the mouse central nervous system (Holderith et al., 2012; Kusch et al., 2018). Nevertheless, the density of calcium channels at C. elegans neuromuscular junctions (91 CaV2 per µm2) is similar to mammalian synapses (100–400 CaV2.1 channels per µm2).

### High-density CaV2 clusters mediate rapid fusion

The dense cluster of CaV2 channels likely insures reliable synchronous fusion, due to the large number of channels and because of the tight coupling distance to docked vesicles. A large number of channels is required because single calcium channels open stochastically, and can introduce jitter to the precise timing of a signal (Borst and Sakmann, 1996). For synapses to reliably track high frequency action potentials, there must be a sufficient number of channels to insure that some open immediately in response to depolarization. Nematode motor neurons rely on graded potentials rather than conventional action potentials; nevertheless, a dense cluster of CaV2 channels will promote a rapid synaptic response to rapid depolarizations.

The calcium channels must be physically coupled to the neurotransmitter release site, that is, the docked synaptic vesicle must be just 20–30 nm from the calcium channel, for the calcium concentration in the nanodomain to be high enough to drive vesicle fusion (Fedchyshyn and Wang, 2005; Weber et al., 2010). Synaptic vesicle pools can be designated as 'tightly coupled' or 'loosely coupled' to calcium channels based on their sensitivity to EGTA (Dittman and Ryan, 2019; Eggermann et al., 2011). At C. elegans neuromuscular junctions, UNC-13L mediates tight coupling (EGTA-insensitive), whereas UNC-13S mediates loose coupling (EGTA-sensitive) (Hu et al., 2013). Here, we found that UNC-13L is colocalized with CaV2 at dense projections. Consistent with EGTA-insensitive priming by UNC-13L, CaV2 mediates the release of vesicles within 33 nm of the dense projection (Hammarlund et al., 2007).

Finally, the dense cluster of CaV2 channels transfers enough calcium from the synaptic cleft to fuse multiple vesicles upon depolarization – termed multiquantal release. The calcium influx from CaV2 also activates the ryanodine receptor, which in turn drives fusion of vesicles docked beyond 33 nm in the intermediate active zone (33–165 nm). The frequency of CaV2-mediated fusion is not affected by presence or loss of RyR, indicating that CaV2 reliably drives vesicle fusion in response to depolarizations on its own. Only the amplitude of these currents is reduced in the absence of RyR, indicating that the ryanodine receptor only potentiates CaV2 responses by releasing calcium from internal stores.

### CaV1 requires coupling to the ryanodine receptor

In contrast to CaV2, CaV1 localizations are dispersed broadly in the synapse and localizations are frequently solitary. Calcium influx mediated by CaV1 is not sufficient to drive vesicle fusion directly, but the ryanodine receptor is activated by low levels of cytosolic calcium and releases calcium from internal stores. CaV1 and RyR colocalize with the UNC-13S synaptic vesicle docking protein. Two-step calcium signaling is consistent with the EGTA-sensitivity of UNC-13S vesicle fusion (Hu et al., 2013); EGTA can buffer the small amount of calcium from CaV1 before it detonates the ryanodine receptor, or buffer calcium diffusing from the endoplasmic reticulum to the UNC-13S docking site.

CaV1 channels inactivate slowly (the moniker 'L-type' refers to 'long-lasting') and are therefore more responsive to long duration synaptic depolarizations (Naranjo et al., 2015; Yu et al., 2018). For example, slow inactivation of CaV1.3 and CaV1.4 channels allows synapses in sensory neurons to accurately report the depolarization status of the synaptic bouton (McRory et al., 2004; Platzer et al., 2000). Similarly, EGL-19 exhibits slow inactivation (Lainé et al., 2014), which likely contributes to graded miniature currents at C. elegans synapses (Liu et al., 2018b).

### The ryanodine receptor mediates multiquantal release

CaV2 and CaV1 both contribute to activation of RyR, but all transmission at lateral sites by CaV1 relies on activation of RyR. The miniature currents mediated by RyR are large amplitude currents, and are likely to be multiquantal vesicle fusions. However, we cannot exclude the possibility that the receptor field under the lateral site is larger than the field at the dense projection, or that lateral synaptic vesicles contain more neurotransmitter.

Despite the potentiation of neurotransmitter release by the ryanodine receptor, the ultimate output of calcium release from internal stores might be a rapid shutdown of synaptic transmission. In CA1 hippocampal neurons CaV1 channels and RyR2 activate calcium gated-potassium channels in the cell body of mouse CA1 hippocampal neurons and hyperpolarize the neuron (Sahu et al., 2019). In C. elegans, CaV1 activity is specifically coupled to SLO-2 BK potassium channels (Liu et al., 2014), activation of SLO-2 by a calcium burst would hyperpolarize the membrane and terminate synaptic transmission. Furthermore, RyR is inhibited by high concentrations of calcium. Hyperpolarization mediated by calcium sparks could act as a safety mechanism to break the positive feedback loop of calcium at synapses, or could regulate switching between neuronal circuits.

The ryanodine receptor is directly stimulated by calcium binding to the receptor (des Georges et al., 2016). Activation of the ryanodine receptor will then depend on the diffusion rate of calcium, buffering capacity, and the distance between the voltage-gated calcium channel and the ryanodine receptor. Modeling studies suggest that the endoplasmic reticulum must be within ~100 nm of vesicle, and that high-frequency stimulation may be required to overcome these barriers (Bouchard et al., 2003).

Alternatively, the voltage sensor in CaV1 could be physically coupled to RyR and bypass the requirement for calcium diffusion. In skeletal muscle, CaV1.1 is physically coupled to RYR1 and voltage-sensing by the calcium channel can gate the ryanodine receptor in the absence of extracellular calcium (Schneider, 1994; Shoshan-Barmatz and Ashley, 1998). In hippocampal cells, CaV1.3 is physically coupled to RyR2 and depolarization alone is sufficient to release calcium stores (Kim et al., 2007). Similarly, in C. elegans, large amplitude currents were not eliminated in 0 mM extracellular calcium (Liu et al., 2005). But in unc-68(-) mutants, which lack the ryanodine receptor, miniature currents were completely eliminated in 0 mM external calcium (Liu et al., 2005). These data suggest that in worms, release of calcium from internal stores may also be coupled by a physical link to a voltage sensor.

### Active zones at invertebrate and vertebrate synapses

Invertebrate synapses are marked by a prominent dense projection ('T-bar' in flies) that is not observed at vertebrate synapses, with the exception of inner ear hair cell. Our data indicate that this structure comprises many of the proteins associated with the full breadth of the vertebrate synapse, including the adhesion molecules Neurexin and SYDE, and the active zone proteins RIMB and ELKS / CAST. Although lacking a focused density, the vertebrate synapse is not homogenous in organization; CaV2, RIM, Munc13, and Bassoon form irregular clusters in the active zone (Holderith et al., 2012; Kawabe et al., 2017; Kusch et al., 2018; Tang et al., 2016). The invertebrate dense projection may serve to create a single density of CaV2 channels for synaptic reliability and speed at the sacrifice of synaptic plasticity.

Participation of the CaV1-RyR axis at synapses may be widespread. In addition to CaV2 channels, CaV1 channels are also present at neuromuscular junctions in the fly and mouse (Katz et al., 1996; Krick et al., 2021; Urbano and Uchitel, 1999). CaV1.2 and CaV1.3 are also expressed broadly in the brain (Hell et al., 1996; Hell et al., 1993; Nanou and Catterall, 2018). Pharmacological experiments suggest that CaV2 and CaV1 channels function together in GABA neurons in the central nervous system. Moreover, these synapses depend on both 'tight' and 'loose' coupling to calcium channels as assayed by EGTA (Eggermann et al., 2011; Goswami et al., 2012; Rey et al., 2020; Vyleta and Jonas, 2014). CaV1 could also be linked to the release of internal stores in the central nervous system, since ryanodine receptors are found at vertebrate presynapses (Bouchard et al., 2003). These ryanodine receptors play a role in multiquantal release at inhibitory inputs to Purkinje cells, and in hippocampal slice culture (Llano et al., 2000; Sharma and Vijayaraghavan, 2003). Recruitment of the CaV1-RyR axis would increase neurotransmitter release from these synapses, but ultimately might shut down neurotransmission by activating potassium channels. The tuning of the output of the presynapse then ultimately depends on the timing and spatial organization of calcium at release sites (Eggermann et al., 2011; Nakamura et al., 2015).

In C. elegans, these calcium channels regulate two separate synaptic vesicle pools. It is not known whether the composition of the vesicles in these pools differ, as has been observed in vertebrates (Kavalali, 2015). In C. elegans, these pools are distinguished by the docking and priming machinery: Vesicle docking at CaV2 sites is mediated by UNC-13L; docking to CaV1 sites is mediated by UNC-13S. This organization could be conserved at vertebrate synapses; a subset of hippocampal synapses express orthologs of both UNC-13L (Munc13-1) and UNC-13S (bMunc13-2) (Kawabe et al., 2017). Further studies are required to test whether CaV2 is coupled to Munc13-1, and the CaV1-RyR axis is coupled to bMunc13-2 in vertebrates, and eventually to determine how these different release sites regulate synapse kinetics and circuit behavior.

## Methods

### Rescue of lethal calcium channel mutants

Lethal CaV1 /egl-19(st556) animals were rescued by Mos-mediated transgenes (oxTi1047[Pset-18::egl-19b::let-858 3’utr] II. EG9034 ‘CaV1 (Δns)’) or by extrachromosomal array (oxEx2017[Pset-18::eGFP_egl-19b::let858utr; Punc-122::GFP]. EG8827 ‘CaV1(Δns) RyR(-)’) (Frøkjær-Jensen et al., 2014). An egl-19 minigene was constructed from cDNA and portions of gDNA containing small introns to aid expression. The first exons 1–4 are cDNA, followed by gDNA of exon 5–9, and cDNA of exon 10–17. The minigene was placed downstream from a muscle Pset-18 promoter and inserted directly into the genome by MosSCI (Frøkjaer-Jensen et al., 2008).

For the array rescue of CaV1 in muscle, Pset-18::eGFP_egl-19b::let858utr; Punc-122::GFP was microinjected into the gonad of adult hermaphrodite egl-19(n582) C. elegans. Array positive animals were selected and crossed with egl-19(st556) (RW3563), which rescued lethality but lacked expression in the nervous system (EG8409). The resulting construct oxTi1047 was crossed into CaV1(-) / egl-19(st556) animals (RW3563), which rescued lethality but lacked expression in the nervous system.

To demonstrate that phenotypes in this EG9034/EG8409 were due to loss of nervous system function, we expressed the egl-19 minigene under the neuron-specific Psnt-1 promoter and inserted the construct into the genome by miniMos (Frøkjær-Jensen et al., 2014). The resulting oxTi1049 construct was crossed into the muscle-rescued CaV1(Δns) animals (EG9034) to generate EG9145.

Lethal double mutants of CaV2-RyR (genotype: unc-2 (lj1); unc-68 (e540)) and CaV2-CaV1 (genotype: unc-2 (lj1); egl-19 (st556)) were rescued by an extrachromosomal array expressing SNAP::CaV2/unc-2 cDNA in a minimum set of acetylcholine head neurons, using a previously described truncated unc-17 promoter, referred to as ‘Punc-17h’ (Hammarlund et al., 2007; Topalidou et al., 2016). The extrachromosomal array oxEx2096 was generated in the unc-2(lj1) strain AQ130 and crossed to RyR / unc-68(e540) or CaV1 /egl-19(st556) oxTi1047[Pset-18::egl-19b] animals to generate double mutants. The resulting strains are lethal without the presence of oxEx2096[Punc-17h::SNAP::unc-2] and were used in electrophysiology experiments. Table 1 contains a genotype summary of calcium channel mutants with allele designations of mutant alleles and rescues.

**Table 1.**
 Summary of strain nomenclature and alleles.


<table>
  <thead>
    <tr>
      <th>Common name</th>
      <th>Usage</th>
      <th>CaV2</th>
      <th>CaV1</th>
      <th>RyR</th>
      <th>CaV2 rescue</th>
      <th>CaV1 rescue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WildtypeN2 Bristol</td>
      <td>ePhysEM behavior</td>
      <td>wt</td>
      <td>wt</td>
      <td>wt</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>CaV1(rescue)</td>
      <td>behaviorSMLM</td>
      <td>wt</td>
      <td>st556</td>
      <td>wt</td>
      <td>n/a</td>
      <td>oxTi1047[Pset-18::egl-19b] oxTi1049[Psnt-1::HALO::egl-19b]</td>
    </tr>
    <tr>
      <td>CaV1(Δns)</td>
      <td>behavior ePhys</td>
      <td>wt</td>
      <td>st556</td>
      <td>wt</td>
      <td>n/a</td>
      <td>oxTi1047[Pset-18::egl-19b]</td>
    </tr>
    <tr>
      <td>CaV1(Δns)RyR(-)</td>
      <td>ePhys</td>
      <td>wt</td>
      <td>st556</td>
      <td>e540</td>
      <td>n/a</td>
      <td>oxEx2017[Pset-18::eGFP::egl-19b]</td>
    </tr>
    <tr>
      <td>CaV2(Δnmj) CaV1(Δns)</td>
      <td>ePhys</td>
      <td>lj1</td>
      <td>st556</td>
      <td>wt</td>
      <td>oxEx2096[Punc-17h::SNAP::unc-2]</td>
      <td>oxTi1047[Pset-18::egl-19b]</td>
    </tr>
    <tr>
      <td>CaV2(Δnmj)RyR(-)</td>
      <td>ePhys</td>
      <td>lj1</td>
      <td>wt</td>
      <td>e540</td>
      <td>oxEx2096[Punc-17h::SNAP::unc-2]</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>CaV2(-)</td>
      <td>ePhysEM</td>
      <td>lj1</td>
      <td>wt</td>
      <td>wt</td>
      <td>no</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>RyR(-)</td>
      <td>ePhysEM</td>
      <td>wt</td>
      <td>wt</td>
      <td>e540</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>CaV1(-)CaV2(-)</td>
      <td>EM</td>
      <td>lj1</td>
      <td>n582</td>
      <td>wt</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <td>CaV1(-)</td>
      <td>EM</td>
      <td>wt</td>
      <td>n582</td>
      <td>wt</td>
      <td>n/a</td>
      <td>no</td>
    </tr>
  </tbody>
</table>

### Behavioral experiments

Animals were maintained under standard laboratory conditions. For behavioral experiments, 3–6 well-fed, young adult worms were transferred to a 10 cm containing standard NGM. Each assay was recorded for 5 min at 8 frames per second using the worm tracking software WormLab (2019.1.1, MBF Bioscience). The trajectory of each worm was collected using WormLab and imported into custom written R scripts for analysis. Worms that crawled out of the field of view during the first 3 min were discarded from analysis. Worms whose speed was lower than 100 µm/s were excluded as they may have been damaged during transfer, the number of worms that fell in this category were few and not different between groups. A reversal was defined as backwards locomotion that lasted more than 4 frames or 500ms.

### Generation of CaV2::HALO by CRISPR/cas9

CaV2 was tagged by CRISPR-mediated insertion of HALO coding DNA into the unc-2 endogenous genomic locus. A DNA mix containing (1) PCR-generated DNA repair template that includes the HALO tag with an embedded Cbr-unc-119(+) cassette flanked by loxP sites and 33 bp homology arms to the cut site, (2) plasmid DNA that directs expression of Cas9 and an sgRNA (Schwartz and Jorgensen, 2016), and (3) an inducible negative selection plasmid directing expression of a histamine-gated chloride channel in neurons, pNP403 (Pokala et al., 2014) was injected into the gonads of young adult EG6207 unc-119(ed3) animals (Maduro and Pilgrim, 1995; Schwartz and Jorgensen, 2016; Zhang et al., 2015). Transgenic animals were selected for expression of unc-119(+), and extrachromosomal-array bearing animals were selected against by addition of histamine to the media. The loxP::Cbr-unc-119(+)::loxP region of the insertion was excised by injecting pDD104[Peft-3::Cre] and identifying unc-119(-) animals (Dickinson et al., 2013). The modified locus introduces HALO-tag within an unconserved region in the second extracellular loop of CaV2 encoding UNC-2a. The resulting strain EG9823 (genotype: unc-119(ed3); unc-2(ox672[HALO])) was subsequently used to generate CRISPR-mediated insertions of Skylan-S tags.

### Generation of super-resolution Tags by CRISPR/cas9

Tags for other genes, including egl-19, unc-68, elks-1, nrx-1, rimb-1, elks-1, syd-2, syd-1, magi-1, ctn-1, unc-13, and unc-13b were constructed as previously described (Schwartz and Jorgensen, 2016). A single plasmid containing sgRNA and the repair template, composed of 57 bp homology arms and Skylan-S (Zhang et al., 2015) containing a loxP::Cbr-unc-119(+)::loxP, was appended by SapTrap plasmid assembly. Each assembled plasmid was mixed with plasmids to express Cas9 in the germline, and HisCl- in neurons, and injected into the gonads of young adult EG9823 animals. After selecting for unc-119(+) and selecting against extrachromosomal arrays by histamine application, animals were injected with pDD104[Peft-3::Cre], selected for excision of loxP::Cbr-unc-119(+)::loxP, and outcrossed once before analysis by super-resolution microscopy. Table 2 contains a full list of superresolution alleles used in this study. Table 3 contains a look up table for common nomenclatures for nematode, fly and mammalian homologs of protiens localized in this study.

**Table 2.**
 Super-resolution alleles generated for this study.


<table>
  <thead>
    <tr>
      <th>Allele</th>
      <th>Gene</th>
      <th>Common name</th>
      <th>sgRNA</th>
      <th>Repair template</th>
      <th>Tag</th>
      <th>Chr</th>
      <th>Terminus</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ox672</td>
      <td>unc-2</td>
      <td>CaV2</td>
      <td>pSAM429 (ACAGACCGCCAACCAACCGG)</td>
      <td>pSAM593</td>
      <td>HALO</td>
      <td>X</td>
      <td>internal</td>
    </tr>
    <tr>
      <td>ox704</td>
      <td>rimb-1</td>
      <td>RIMBP</td>
      <td>TGGGTAAATCGATAAATCG</td>
      <td>pSAM514</td>
      <td>SKY-S</td>
      <td>III</td>
      <td>c</td>
    </tr>
    <tr>
      <td>ox719</td>
      <td>nrx-1</td>
      <td>Neurexin</td>
      <td>TTTTCTTTGCCACCCCATTC</td>
      <td>pSAM534</td>
      <td>SKY-S</td>
      <td>V</td>
      <td>c</td>
    </tr>
    <tr>
      <td>ox721</td>
      <td>unc-68</td>
      <td>RyR</td>
      <td>pSAM488 (gattagttagttccaagaaA)</td>
      <td>pSAM593h</td>
      <td>HALO</td>
      <td>V</td>
      <td>n</td>
    </tr>
    <tr>
      <td>ox727</td>
      <td>ctn-1d</td>
      <td>α-Catulin</td>
      <td>CATCCAATGTAATCGGC</td>
      <td>pSAM598</td>
      <td>SKY-S</td>
      <td>III</td>
      <td>c</td>
    </tr>
    <tr>
      <td>ox728</td>
      <td>egl-19</td>
      <td>CaV1</td>
      <td>CTTCTCATCCATTGCTC</td>
      <td>pSAM604</td>
      <td>SNAP</td>
      <td>IV</td>
      <td>internal</td>
    </tr>
    <tr>
      <td>ox729</td>
      <td>syd-1</td>
      <td>SYDE</td>
      <td>GCACTGCGATTCCGAGACAT</td>
      <td>pSAM545</td>
      <td>SKY-S</td>
      <td>II</td>
      <td>c</td>
    </tr>
    <tr>
      <td>ox730</td>
      <td>syd-2</td>
      <td>α-Liprin</td>
      <td>TTGCTGTAGCTCATatttct</td>
      <td>pSAM549</td>
      <td>SKY-S</td>
      <td>X</td>
      <td>n</td>
    </tr>
    <tr>
      <td>ox747</td>
      <td>elks-1</td>
      <td>ELKS/CAST</td>
      <td>gagcagtacaatATGGCACC</td>
      <td>pSAM550</td>
      <td>SKY-S</td>
      <td>IV</td>
      <td>n</td>
    </tr>
    <tr>
      <td>ox748</td>
      <td>unc-13all</td>
      <td>UNC13all</td>
      <td>gctttgaatccaacaaaaaa</td>
      <td>pSAM613</td>
      <td>SKY-S</td>
      <td>I</td>
      <td>c</td>
    </tr>
    <tr>
      <td>ox803</td>
      <td>magi-1</td>
      <td>MAGI</td>
      <td>aagATGACCGACAAAACAGC</td>
      <td>pSAM552</td>
      <td>SKY-S</td>
      <td>IV</td>
      <td>n</td>
    </tr>
    <tr>
      <td>ox814</td>
      <td>unc-13b</td>
      <td>UNC13s</td>
      <td>GGAACTGCAAGACTTGGCAC</td>
      <td>pSAM684</td>
      <td>SKY-S</td>
      <td>I</td>
      <td>n</td>
    </tr>
    <tr>
      <td>ox802</td>
      <td>unc-44</td>
      <td>Giant Ankyrin</td>
      <td>GCTGTTGGTCGTGCTCCCGA</td>
      <td>pSAM546</td>
      <td>SKY-S</td>
      <td>IV</td>
      <td>c</td>
    </tr>
    <tr>
      <td>ox708</td>
      <td>unc-44</td>
      <td>Giant Ankyrin</td>
      <td>GCTGTTGGTCGTGCTCCCGA</td>
      <td>pSAM557</td>
      <td>SNAP</td>
      <td>IV</td>
      <td>c</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Common names and nomenclature used in this study.


<table>
  <thead>
    <tr>
      <th>Common name</th>
      <th>Mammalian ortholog</th>
      <th>C. elegans ortholog</th>
      <th>Drosophila ortholog</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CaV2</td>
      <td>CaV2.1CaV2.2CaV2.3</td>
      <td>UNC-2</td>
      <td>Cacophony</td>
    </tr>
    <tr>
      <td>CaV1/L-type</td>
      <td>CaV1.1CaV1.2CaV1.3CaV1.4</td>
      <td>EGL-19</td>
      <td>DmCa1D</td>
    </tr>
    <tr>
      <td>ELKS</td>
      <td>ELKS/CAST</td>
      <td>ELKS-1</td>
      <td>Bruchpilot</td>
    </tr>
    <tr>
      <td>RyR</td>
      <td>RYR1RYR2RYR3</td>
      <td>UNC-68</td>
      <td>dRyr</td>
    </tr>
    <tr>
      <td>UNC13all</td>
      <td>Munc13-1ubMunc13-2 bMunc13-2Munc13-3</td>
      <td>UNC-13L,UNC-13S</td>
      <td>Unc13AUnc13B</td>
    </tr>
    <tr>
      <td>UNC-13S</td>
      <td>bMunc13-2Munc13-3</td>
      <td>UNC-13S</td>
      <td>UNC13B</td>
    </tr>
    <tr>
      <td>RIMBP</td>
      <td>RIMBP</td>
      <td>RIMB-1</td>
      <td>Rbp</td>
    </tr>
    <tr>
      <td>Veli/LIN7</td>
      <td>LIN7A</td>
      <td>LIN-7</td>
      <td>Lin-7</td>
    </tr>
    <tr>
      <td>Giant Ankyrin</td>
      <td>gAnkB</td>
      <td>UNC-44L</td>
      <td>AnkG</td>
    </tr>
    <tr>
      <td>Neurexin/NRX</td>
      <td>Neurexin 1</td>
      <td>NRX-1</td>
      <td>DNrx</td>
    </tr>
    <tr>
      <td>α-Liprin</td>
      <td>α-Liprin</td>
      <td>SYD-2</td>
      <td>Liprin-α</td>
    </tr>
    <tr>
      <td>SYDE</td>
      <td>SYDE</td>
      <td>SYD-1</td>
      <td>Syd-1</td>
    </tr>
    <tr>
      <td>α-Catulin</td>
      <td>α-Catulin</td>
      <td>CTN-1</td>
      <td>α-Cat</td>
    </tr>
    <tr>
      <td>MAGI1</td>
      <td>MAGI1</td>
      <td>MAGI-1</td>
      <td>Magi</td>
    </tr>
  </tbody>
</table>

### Strains

All strains were maintained at 22 °C on standard NGM media seeded with OP50.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Strain</th>
      <th>Genotype</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wild-type</td>
      <td>N2</td>
      <td>wild-type</td>
    </tr>
    <tr>
      <td>CaV2(-)</td>
      <td>AQ130</td>
      <td>unc-2(lj1) X</td>
    </tr>
    <tr>
      <td>RyR(-)</td>
      <td>CB540</td>
      <td>unc-68(e540) V</td>
    </tr>
    <tr>
      <td>CaV1(-) balanced</td>
      <td>RW3563</td>
      <td>egl-19(st556) / unc-82(e1323) unc-24(e138am) IV</td>
    </tr>
    <tr>
      <td>EM Wildtype</td>
      <td>EG5793</td>
      <td>oxSi91[Punc-17::ChIEF::mCherry::unc-54UTR unc-119(+)] II; unc-119(ed9) III</td>
    </tr>
    <tr>
      <td>EM CaV2(-)</td>
      <td>EG6584</td>
      <td>oxSi91[Punc-17::ChIEF::mCherry::unc-54UTR unc-119(+)] II; unc-2(lj1) X</td>
    </tr>
    <tr>
      <td>EM CaV1(-)</td>
      <td>EG6585</td>
      <td>oxSi91[Punc-17::ChIEF::mCherry::unc-54UTR unc-119(+)] II; egl-19(n582) IV</td>
    </tr>
    <tr>
      <td>EM CaV2(-) CaV1(-)</td>
      <td>EG6586</td>
      <td>oxSi91[Punc-17::ChIEF::mCherry::unc-54UTR unc-119(+)] II; egl-19(n582) IV; unc-2(lj1) X.</td>
    </tr>
    <tr>
      <td>EM RyR(-)</td>
      <td>EG6587</td>
      <td>oxSi91[Punc-17::ChIEF::mCherry::unc-54UTR unc-119(+)] II; unc-68(e540) V</td>
    </tr>
    <tr>
      <td>CaV1 muscle rescue array</td>
      <td>EG8409</td>
      <td>egl-19(st556) IV; egl-19(oxEx2017[Pset-18::eGFP_egl-19b::let-858-utr; ccGFP])</td>
    </tr>
    <tr>
      <td>CaV1(Δns) RyR(-)</td>
      <td>EG8827</td>
      <td>egl-19(st556) IV; unc-68(e540) V; oxEx2017[Pset-18::eGFP::egl-19b::let-858-utr; Punc-122::GFP]</td>
    </tr>
    <tr>
      <td>CaV1(Δns)</td>
      <td>EG9034</td>
      <td>oxTi1047[Pset-18::egl-19b::let-858–3’utr] II; egl-19(st556)</td>
    </tr>
    <tr>
      <td>CaV2(Δnmj) RyR(-)</td>
      <td>EG9405</td>
      <td>unc-68(e540) V; unc-2(lj1) X; oxEx2097[Punc-17h::SNAP::unc-2]</td>
    </tr>
    <tr>
      <td>CaV2(Δnmj) CaV1(Δns)</td>
      <td>EG9406</td>
      <td>unc-2(lj1) oxTi1047[Pset-18::egl-19b::let-858 3’utr] II; egl-19(st556)IV; unc-2(lj1) X; oxEx2097[Punc-17h::SNAP::unc-2]</td>
    </tr>
    <tr>
      <td>RIMBP-SKYSCaV1-HALO (+ns rescue)Giant Ankryin-SNAP</td>
      <td>EG9418</td>
      <td>egl-19(st556) IV; ox704[Skylan-S::rimb-1] III; oxTi1047[Pset-18::egl-19b::let-858utr; HygroR(+)], oxTi1055[Psnt-1::HALO::egl-19b; NeoR(+)] II; unc-44(ox708[unc-44::snap]) IV</td>
    </tr>
    <tr>
      <td>CaV2-HALOLiprinα-SKYS</td>
      <td>EG9425</td>
      <td>unc-119(ed3) III; unc-2(ox672[HALO]), syd-2(ox715[Skylan-S(loxP::Cbr-unc-119(+)::loxP)]) X</td>
    </tr>
    <tr>
      <td>RIMBP-SKYSCaV2-HALOCaV1-SNAP</td>
      <td>EG9475</td>
      <td>oxIs322[Cbr-unc-119(+) Pmyo-2::mCherry::histone Pmyo-3::mCherry::histone] II; unc-119(ed3) III; rimb-1(ox704[Skylan-S]) III; egl-19(ox728[snap]) IV; unc-2(ox672[HALO::]) X</td>
    </tr>
    <tr>
      <td>αCatulin-SKYSCaV1-SNAPCaV2-HALO</td>
      <td>EG9476</td>
      <td>ctn-1d(ox727[Skylan-S]) I; oxIs322[Cbr-unc-119(+) Pmyo-2::mCherry::histone Pmyo-3::mCherry::histone] II; unc-119(ed3) III; egl-19(ox728[SNAP]) IV; unc-2(ox672[HALO]) X</td>
    </tr>
    <tr>
      <td>NRX-SKYSCaV1-SNAPCaV2-HALO</td>
      <td>EG9588</td>
      <td>egl-19(ox728[SNAP]) IV; nrx-1(ox719[Skylan-S]) V; unc-2(ox672[HALO]) X</td>
    </tr>
    <tr>
      <td>ELKS-SKYSCaV1-SNAPCaV2-HALO</td>
      <td>EG9617</td>
      <td>elks-1(ox747[Skylan-S]), egl-19(ox728[SNAP]) IV; unc-2(ox672[HALO]) X</td>
    </tr>
    <tr>
      <td>ELKS-SKYSCaV1-SNAPRyR-HALO</td>
      <td>EG9667</td>
      <td>egl-19(ox728[SNAP]), elks-1(ox747[Skylan-S]) IV; unc-68(ox721[HALO]) V</td>
    </tr>
    <tr>
      <td>Giant Ankryin -SKYSCaV1-SNAPCaV2-HALO</td>
      <td>EG9722</td>
      <td>unc-2(ox672[HALO]) X; egl-19(ox728[SNAP]) IV; unc-44(ox802[Skylan-S]) IV</td>
    </tr>
    <tr>
      <td>UNC13all-SKYSCaV1-SNAPCaV2-HALO</td>
      <td>EG9723</td>
      <td>unc-2(ox672[HALO]) X; egl-19(ox728[SNAP]) IV; unc-13(ox748[Skylan-S]) I</td>
    </tr>
    <tr>
      <td>UNC13short-SKYSCaV1-SNAPCaV2-HALO</td>
      <td>EG9782</td>
      <td>unc-13(ox814[SKYLAN-S(loxP)]) I; unc-2(ox672[HALO]) X; egl-19(ox728[SNAP]) IV</td>
    </tr>
    <tr>
      <td>CaV2-HALO</td>
      <td>EG9823</td>
      <td>unc-2(ox672[HALO::unc-2]) X; unc –119(ed3) III</td>
    </tr>
    <tr>
      <td>RIMBP-SKYSCaV1-HALO(+ns rescue)Lin7-SNAP</td>
      <td>EG10094</td>
      <td>oxTi1055[Psnt-1::HALO::egl-19b; NeoR(+)] oxTi1047[Pset-18::egl-19b::let858utr; HygroR(+)] II; unc-119(ed3) rimb-1(ox704[Skylan-S]) III; egl-19(st556) IV; oxEx2223[Punc-129::lin-7::SNAPf-tag]</td>
    </tr>
    <tr>
      <td>SYDE-SKYSCaV2-HALO</td>
      <td>EG10095</td>
      <td>syd-1(ox723[Skylan-S(loxP::Runc-119::loxP)]) II; unc-119(ed3) III; unc-2(ox672[HALO]) X</td>
    </tr>
    <tr>
      <td>MAGI-SKYSCaV1-SNAPCaV2-HALO</td>
      <td>EG10096</td>
      <td>unc-119(ed3) III; egl-1-19(ox728[snap]), magi-1(ox755[Skylan-S(loxP::Cbr-unc-119::loxP)]) IV; unc-2(ox672[HALO]) X</td>
    </tr>
  </tbody>
</table>

### Single molecule localization microscopy

Super-resolution images were recorded with a Vutara SR 352 (Bruker Nanosurfaces, Inc, Madison, WI) commercial microscope based on single molecule localization biplane technology (Juette et al., 2008; Mlodzianoski et al., 2009). First, 20–30 adult hermaphrodite C. elegans expressing HALO- tagged proteins Encell et al., 2012; Mollwitz et al., 2012 were allowed to lay eggs for 6–8 hr. Adults were moved to a new plate or destroyed. ~2 days later, when L4s were abundant on the plate, but before young adults emerged, animals were washed off using M9 an briefly centrifuged and resuspended in M9 several times to remove bacteria. Dye solution was prepared by suspending 5 nmol of JF dye in 5 µl of fresh DMSO to make 1 mM solution of dye. Five µL of 1 mM solution was added to 95 µl of worms in M9. Animals were stained for 2 hr on an orbital shaker at room temperature in the dark in 50 μM of HTL-JF646, and 50 μM of STL-JF549cp, STL-JF549, or STL-JF549pa (Gift from Luke Lavis, Janelia Farms; Grimm et al., 2017; Grimm et al., 2015). Early super-resolution experiments were conducted with JF549-STL or PA-JF549-STL, we later found that a new cell permeable variant cp-JF549-STL improved labeling of channels. After 2 hr, 1 mL of M9 was added to the staining tubes, spun gently on a benchtop centrifuge and aspirated several times to remove dye. Animals were allowed to recover 12 hr at 15degC on agar seeded with OP50 bacteria. Molting is essential to remove non-specific staining of the cuticle. After they had molt, live intact animals were anesthetized in 25 mM NaN3 and regions of their dorsal cords that were positioned directly against the cover glass and away from the intestine. These were imaged with 640 nm excitation power of 10kW/cm2, or 549 nm excitation power of 5kW/cm2 Skylan-S was imaged by 488 nm excitation at 2kW/cm2, while photoactivated by 0.37 mW/cm2 405 nm light. Images were recorded using a 60 x/1.2 NA Olympus water immersion objective and Hamamatsu Flash4 V1 sCMOS, or 60 x/1.3 NA Silicon immersion objective and Orca Fusion BT SCMOS camera with gain set at 50 and frame rate at 50 Hz. Individual laser settings varied per animal to optimize blinking, but typically lasers were set below 12%. Example settings: 9% 646, 7% 549, 4% 488 with 2% 405 activation laser. A minimum of 1000 frames per fluorophore were recorded. Data was analyzed by the Vutara SRX software (version 7.0.0rc39). Single molecules were identified by their brightness frame by frame after removing the background. Identified molecules were localized in three dimensions by fitting the raw data in a 12x12-pixel region of interest centered around each particle in each plane with a 3D model function that was obtained from recorded bead data sets. Fit results were filtered by a density-based denoising algorithm to remove isolated particles. The experimentally achieved image resolution of 40 nm laterally (x,y) and 70 nm axially (in z) was determined by Fourier ring correlation. Localizations were rendered as 80 nm.

### SML analysis

Localization data was exclusively collected from the dorsal nerve cord, which contains axons and synapses but no neuronal soma. We performed a 3D reconstruction of C. elegans dorsal nerve cord to inform region of interest selection from fluorescent images. The orientation of dorsal cord synapses is predictable. Excitatory acetylcholine neurons and inhibitory GABA neurons synapse onto muscle arms (Figure 3A). These connections are near the edges of the cord bundle. Thus, the roll of the animal affects the orientation of the synapse; en face or axial.

For single molecule localization experiments, animals were rolled to ensure en face orientation of synapses. Synapses that were in focus and en face were analyzed. The average size of a synapse from the dorsal nerve cord is 579.7 nm (SEM +/-16 nm). Thus, super-resolution analysis regions of interest were narrowed to localizations within 700 nm of the dense projection marker. Localization position data was flattened in the z-dimension due to chromatic aberrations. A script was used to calculate the center of each probe. To compare the distribution of probe A to probe B, an angle between the two clusters centers was calculated. The distribution distances were calculated by measuring the distance along the center-to-center axis from a probe B to the center of cluster A, and cluster B. Nearest neighbor analysis was done with knnsearch. The 95% confidence interval of these distance measurements is considered the diameter of the cluster. Distribution center and range or ‘diameter’ were reported as (mean, 95% CI). Proberuler available at https://github.com/bdmscience/proberuler (copy archived at Mueller, 2022).

### Counting calcium channels

CaV1 calculations. CaV1-SNAP was coupled to JF549cp. CaV1 channels are dispersed in the synapse but also often form small clusters, spatially distinct from CaV2 clusters (Figure 10A). To estimate the number of CaV1 channels, imaging conditions were optimized to maximize localizations from only CaV1 by imaging them first, and estimated their number using three approaches.

Total blinks. Each blink was assumed to be a channel (total CaV1 blinks Ᾱ=196 ± 37 channels). Since total blinks assumes every channel blinks only once, this method will represent an overcount of the true number of channels. Single channels emit multiple blinks (see next method), thus 200 channels likely represents the maximum number of channels.

Mean blinks per channel (~60 nm). Spatial information was used to determine how many blinks belong to the same channel – singlet blinks were assigned as a channel, and two or more blinks within 60 nm of each other were assumed to arise from a single channel via DBSCAN, based on a typical confidence interval (We observe 40 nm resolution by Fourier ring analysis, to be conservative a 60 nm arbitrary criterion was used, given that we only include blinks with better than 80 nm localization precision by Cramér-Rao lower bound; for context, a calcium channel with subunits is ~20 nm in diameter). A Poisson distribution was fit to the number of blinks per channel (m=2.7 blinks per channel). Dividing the total number of blinks in synapses by the mean number of blinks per channel produces an estimate of 79±10 CaV1 channels per synapse (Figure 10B, C).

Photon flux. Every blink has a photon count. The mode number of photons emitted in a blink was determined from all blinks at analyzed synapses (Mo = 575 photons / blink; Ᾱ=765 ± 11 photons/ blink; Figure 10D). Blinks were also clustered into single channels (as described above) and the number of photons per ‘channel’ was measured. Channels emitted a mean of 1996±489 photons because some channels blinked multiple times. The mode was 550 photons per channel (Figure 10D). The mode photon count for channels is similar to the mode photon count of single blinks indicating that most channels blink once. The total number of photons emitted by a synapse for the whole imaging session was divided by the mean number of photons per channel to estimate CaV1 channel count: (75±19 CaV1 channels; Figure 10E).

CaV2 calculations. CaV2-HALO was labelled with JF646. CaV2 channels are tightly localized into ~250 nm diameter clusters coincident with the dense projection. Each synapse contains just one density, but each density has several hundred CaV2 blinks. The number of CaV2 channels in individual boutons was estimated with the following approaches. Total blinks. CaV2 exhibited a mean 569±54 blinks / synapse. Again, as described above total blinks is an overestimate of the number of channels at a synapse.

Mean blinks or photon flux per channel. CaV2 blinks exhibited a mode of 900 photons. However, CaV2 localizations saturate the dense projection so single channels cannot be isolated. The cluster appears as a uniform mass, because the resolution and precision of our experiments are not adequate to spatially resolve single channels in densely labeled domains. To circumvent this limitation, the maximum number of channels in the density was calculated.

Cluster diameter – upper bound. An upper bound was estimated for the number of channels by mathematically fitting circles within a larger circle (20 nm channels in a 250 nm cluster) yields a maximum capacity of 120 channels at the dense projection.

Minimal overlap -- lower bound. The CaV2 clusters appears continuous without cavities, meaning all localizations overlap with neighboring channels. A mathematical fit of 60 nm circles within a 250 nm cluster results in at least 12 channels. Each channel would need to blink 50 times in 1 min. Organic dye blinking photophysics are not well characterized. However, this rate is approximately 10-fold higher than rates experimentally determined, as described below, suggesting there are many more channels.

Blinking rate. The blinking rate of dyes was used to estimate channel count. Although blinking rates of rhodamine dyes have not been determined, cyanine dyes in oxygen scavenging buffer can blink about six times in one minute depending on the imaging conditions (Helmerich et al., 2022). 569 blinks on average were observed from the CaV2 cluster in a one minute imaging interval. If rhodamine dyes are similar to cyanine dyes, then 101±16 CaV2s are present at a single synaptic bouton. Thus, 101 CaV2 channels is the best estimate given our limited knowledge of dye photophysics.

### Electrophysiology

All electrophysiological experiments were performed with young adult hermaphrodites. The animals were immobilized and dissected as previously described (Liu et al., 2013). In experiments to record minis mediated by both GABA and ACh receptors, the extracellular solution contained (in mM) NaCl 140, KCl 5, CaCl2 0.5, MgCl2 5, dextrose 11 and HEPES 5 (pH 7.2), and the pipette solution containing (in mM) KCl 120, KOH 20, Tris 5, CaCl2 0.25, MgCl2 4, sucrose 36, EGTA 5, and Na2ATP 4 (pH 7.2). In experiments to record minis mediated by only ACh receptors, the pipette solution was modified by reducing KCl to 6.8 mM and adding Kgluconate 112.2 mM. The holding voltage used in all the experiments was –60 mV. Dantrolene (D3996, TCI America) and nemadipine-A (SC-202727, Santa Cruz Biotechnology, Inc) stock solutions (10 mM) were made in DMSO. In each experiment, 1 µl of the stock solution was first thoroughly mixed with 50 µl of the bath solution in a small centrifuge tube, and then the entire volume of the mixed solution was added to the bath (total volume 1 ml) to reach the final concentration of 10 µM. After adding the dantrolene or nemadipine-A solution, the bath solution was pipetted up and down 5 times using the same pipette (set at 50 µl), and an incubation period of 5 min was allowed prior to starting the electrophysiological recording. The classic whole-cell configuration was used for voltage-clamp recordings with a Multiclamp 700B amplifier (Molecular Devices, Sunnyvale, CA, USA) and the Clampex software (version 10 or 11, Molecular Devices). Data were filtered at 2 kHz and sampled at 10 kHz. The frequency and amplitude of minis were quantified with ClampFit (version 11, Molecular Devices).

### Quantal modelling

A 3-term gaussian distribution was fit to the frequency distribution of amplitudes in 1 pA bins using MATLAB Curve Fitter (Mathworks, Natick, MA, USA). The terms were centered on 7+/-1 pA (nema alone) or 5+/-1 pA (dantrolene +nema) intervals which are the modes of the mini amplitudes, that is, a single quantum (Del castillo and Katz, 1954). The coefficient for the mean of the first gaussian curve was set to the mode amplitude (7 pA ±1). Every coefficient for subsequent gaussian terms were set to 7 pA ±1 intervals, but the other coefficients were not constrained and allowed to find a best fit. Area under each curve was calculated using MATLAB trapz.

### Flash and freeze electron microscopy

Electron microscopy was performed as previously described (Watanabe et al., 2013). Freezing was performed on a Leica EMpact2 (Leica, Wetzlar, Germany). To stimulate neurotransmission animals were exposed to blue (488 nm) LED light for 20ms and frozen 50ms later. Thirty-three nm serial sections were taken and imaged using a Hitachi H-7100 transmission electron microscope equipped with a Gatan Orius digital camera (Gatan, Pleasanton, CA). Micrographs were analyzed in ImageJ using a program for morphological analysis of synapses (Watanabe et al., 2020). Scripts available at: https://github.com/shigekiwatanabe/SynapsEM (copy archived at Watanabe, 2022).

### Dorsal nerve cord reconstruction

Serial sections were cut at 100 nm and imaged using JEOL JEM-1400 (JEOL, Peabody, MA) then annotated and assembled using TrackEM2 in FIJI (Cardona et al., 2012). Specifically, a wireframe was fit through each process that was suspected to be in the previous micrograph. Then an outline of the plasma membrane of each process was drawn. We analyzed several criteria to more specifically determine the specific process name and type: the morphology of each process and compared to previously published data (White et al., 1986), and the number of synapses. These data allow us to determine the identity of a process with some certainty.

### Whole genome sequencing of unc-68(e504)

CB504 animals were grown on HB101 and pelleted. DNA was extracted with a Qiagen DNeasy Blood and Tissue kit (Qiagen #69504) and eluted in EB buffer. Sequencing libraries were prepared using a Nextera XT DNA Library preparation kit (Illumina) and sequenced on an Illumina NovaSeq using paired 150-base reads. Reads were aligned to the C. elegans genome (WS276) with bwa (Li and Durbin, 2009) and processed with Samtools (Li et al., 2009). Aligned reads were base-called with GATK (McKenna et al., 2010) and mutations were annotated with SnpEff (Cingolani et al., 2012). Nextera library preparation and sequencing was performed by the Huntsman Cancer Institute High Throughput Genomics core facility. The VCF file describing unc-68(e540) can be found in Source data 1. Research reported in this publication utilized the High-Throughput Genomics and Bioinformatic Analysis Shared Resource at Huntsman Cancer Institute at the University of Utah and was supported by the National Cancer Institute of the National Institutes of Health under Award Number P30CA042014. The content is solely the responsibility of the authors and does not necessarily represent the official views of the NIH.
