# Impact of energy limitations on function and resilience in long-wavelength Photosystem II

## Authors

- Stefania Viola<sup>1</sup> ([ORCID: 0000-0003-0773-8158](https://orcid.org/0000-0003-0773-8158)) †
- William Roseby<sup>1</sup>
- Stefano Santabarbara<sup>2</sup>
- Dennis Nürnberg<sup>3</sup>
- Ricardo Assunção<sup>3</sup>
- Holger Dau<sup>3</sup>
- Julien Sellés<sup>4</sup>
- Alain Boussac<sup>5</sup>
- Andrea Fantuzzi<sup>1</sup>
- A William Rutherford<sup>1</sup> ([ORCID: 0000-0002-3124-154X](https://orcid.org/0000-0002-3124-154X)) †

### Affiliations

1. Department of Life Sciences, Imperial College London London United Kingdom ([ROR:041kmwe10](https://ror.org/041kmwe10))
2. Photosyntesis Research Unit, Consiglio Nazionale delle Ricerche Milan Italy ([ROR:04zaypm56](https://ror.org/04zaypm56))
3. Physics Department, Freie Universität Berlin Berlin Germany ([ROR:046ak2485](https://ror.org/046ak2485))
4. Institut de Biologie Physico-Chimique, UMR CNRS 7141 and Sorbonne Université Paris France ([ROR:01na0pb61](https://ror.org/01na0pb61))
5. Institut de Biologie Intégrative de la Cellule, UMR9198, CEA Saclay Gif-Sur-Yvette France ([ROR:01fftxe08](https://ror.org/01fftxe08))

† Corresponding author

## Abstract

Photosystem II (PSII) uses the energy from red light to split water and reduce quinone, an energy-demanding process based on chlorophyll a (Chl-a) photochemistry. Two types of cyanobacterial PSII can use chlorophyll d (Chl-d) and chlorophyll f (Chl-f) to perform the same reactions using lower energy, far-red light. PSII from Acaryochloris marina has Chl-d replacing all but one of its 35 Chl-a, while PSII from Chroococcidiopsis thermalis, a facultative far-red species, has just 4 Chl-f and 1 Chl-d and 30 Chl-a. From bioenergetic considerations, the far-red PSII were predicted to lose photochemical efficiency and/or resilience to photodamage. Here, we compare enzyme turnover efficiency, forward electron transfer, back-reactions and photodamage in Chl-f-PSII, Chl-d-PSII, and Chl-a-PSII. We show that: (i) all types of PSII have a comparable efficiency in enzyme turnover; (ii) the modified energy gaps on the acceptor side of Chl-d-PSII favour recombination via PD1+Phe- repopulation, leading to increased singlet oxygen production and greater sensitivity to high-light damage compared to Chl-a-PSII and Chl-f-PSII; (iii) the acceptor-side energy gaps in Chl-f-PSII are tuned to avoid harmful back reactions, favouring resilience to photodamage over efficiency of light usage. The results are explained by the differences in the redox tuning of the electron transfer cofactors Phe and QA and in the number and layout of the chlorophylls that share the excitation energy with the primary electron donor. PSII has adapted to lower energy in two distinct ways, each appropriate for its specific environment but with different functional penalties.

## Introduction

Photosystem II (PSII) is the water/plastoquinone photo-oxidoreductase, the key energy converting enzyme in oxygenic photosynthesis. The near-universal type of PSII, found in all photosynthetic eukaryotes and in most cyanobacteria, contains 35 chlorophylls a (Chl-a) and 2 pheophytins a (Phe). Four of the Chl molecules (PD1, PD2, ChlD1, and ChlD2) and both Phe molecules are located in the reaction centre (Diner and Rappaport, 2002). The remaining 31 Chl-a in the PSII core constitute a peripheral light-collecting antenna. When antenna chlorophylls are excited by absorbing a photon, they transfer the excitation energy to the primary electron donor, ChlD1, the red-most chlorophyll in the reaction centre, although it’s been reported that charge separation from PD1 can occur in a fraction of centres (Diner and Rappaport, 2002; Holzwarth et al., 2006; Romero et al., 2010; Cardona et al., 2012). The initial charge separation, forming the first radical pair ChlD1+Phe- (assuming ChlD1 as primary donor), is quickly stabilized by the formation of the second radical pair, PD1+Phe-, and then by further electron transfer steps (Figure 1A) that lead to the reduction of plastoquinone and the oxidation of water.

![Figure 1.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig1-v3.jpg)

**Figure 1.:** (A) Chl-a-PSII with the key cofactors of the reaction centre, located in the subunits D1 and D2, labelled. Besides the PD1, PD2, ChlD1, and ChlD2 chlorophylls and the two pheophytins, PheD1 and PheD2, these cofactors include the quinones, QA and QB, and the non-heme iron (Fe) on the acceptor side and the two redox-active tyrosines TyrZ and TyrD and the manganese cluster (Mn4O5Ca) on the donor side. The arrows represent the electron transfer steps and the numbers the order of the steps. The yellow arrow is the primary charge separation, with other steps shown as red arrows. The primary donor is shown as ChlD1. (B) and (C) Chl-d-PSII and Chl-f-PSII, with the far-red chlorophylls in the reaction centres highlighted and the wavelength of the primary donor, assumed to be ChlD1, indicated. The hexagons on the sides of each reaction centre represent the chlorophylls of the respective antennas, located in the subunits CP43 and CP47. Chl-a is represented in green, Chl-d in orange and Chl-f in brown. In (C) the single Chl-d is located in the ChlD1 position, reflecting the assignment of the single Chl-d as the primary donor (Gisriel et al., 2022), leaving the remaining 4 Chl-f molecules as peripheral antenna. For all three types of PSII, the model of the reaction centre cofactors was made based on the crystal structure of PSII from the cyanobacterium Thermosynechococcus vulcanus (PDB ID: 3WU2, Umena et al., 2011).

PSII activity is energy demanding. In Chl-a-PSII, the primary donor absorbs red photons at 680 nm, and this defines the energy available for photochemistry (1.82 eV) with a high quantum yield for the forward reactions. The energy stored in the products of the reaction (reduced plastoquinone and molecular oxygen) and in the trans-membrane electrochemical gradient is ~1 eV, while the remaining ~0.82 eV is released as heat helping to ensure a high quantum yield for the forward reaction and minimize damaging and wasteful side- and back-reactions. The 1.82 eV was suggested to be the minimum amount of energy required for an optimum balance of efficiency versus resilience to photodamage, and responsible for explaining the ‘red limit’ (~680 nm) for oxygenic photosynthesis (Nürnberg et al., 2018; Rutherford et al., 2012).

The first reported case in which the red limit is exceeded was the chlorophyll d (Chl-d)-containing cyanobacterium Acaryochloris marina (A. marina) (Miyashita et al., 1996). Chl-d-PSII contains 34 Chl-d and 1 Chl-a (proposed to be in the PD1 position Renger and Schlodder, 2008) and uses less energy, with the proposed Chl-d primary donor in the ChlD1 position absorbing far-red photons at ~720 nm (Schlodder et al., 2007), corresponding to an energy of ~1.72 eV (Figure 1B).

Recently, it was discovered that certain cyanobacteria use an even more red-shifted pigment, chlorophyll f (Chl-f), in combination with Chl-a (Chen et al., 2010; Gan et al., 2014). When grown in far-red light, these cyanobacteria replace their Chl-a-PSII with Chl-f-PSII, that has far-red specific variants of the core protein subunits (D1, D2, CP43, CP47, and PsbH) and contains ~90% of Chl-a and ~10% of Chl-f (Nürnberg et al., 2018; Gan et al., 2014). The Chl-f-PSII from Chroococcidiopsis thermalis PCC7203 (C. thermalis), which contains 30 Chl-a, 4 Chl-f, and 1 Chl-d, was shown to have a long wavelength primary donor (originally proposed to be either Chl-f or d, in the ChlD1 position Nürnberg et al., 2018) absorbing far-red photons at ~720 nm (Figure 1C), the same wavelength as in A. marina (Nürnberg et al., 2018; Judd et al., 2020). A recent cryo-EM structure has also argued for ChlD1 being the single Chl-d in the Chl-f-PSII of Synechococcus sp. PCC7335 (Gisriel et al., 2022). This suggests that this could be the case also in the Chl-f-PSII of C. thermalis, because of the conservation of the amino acids coordinating ChlD1 in the far-red PSII of the two species. The facultative, long-wavelength species that use Chl-f are thus the second case of oxygenic photosynthesis functioning beyond the red-limit (Nürnberg et al., 2018), but the layout of their long wavelength pigments is quite different from that of the Chl-d-PSII.

Assuming that Chl-a-PSII already functions at an energy red limit (Rutherford et al., 2012), the diminished energy in Chl-d-PSII and Chl-f-PSII seems likely to increase the energetic constraints. Thus, if the far-red PSII variants store the same amount of energy in their products and electrochemical gradient, as seems likely, then it was suggested that they should have decreased photochemical efficiency and/or a loss of resilience to photodamage (Nürnberg et al., 2018; Cotton et al., 2015; Davis et al., 2016). These predicted energetic constraints are worth investigating to generate knowledge that could be beneficial for designing strategies aimed at engineering of far-red photosynthesis into other organisms of agricultural or technological interest (Chen and Blankenship, 2011).

Here we report a comparison of the enzyme turnover efficiency, forward reactions, and back-reactions in the three known types of PSII: Chl-a-PSII, and the two far-red types, the Chl-f-PSII from C. thermalis and the Chl-d-PSII from A. marina. To compare the enzymatic properties of the three types of PSII and minimize the effects of physiological differences between strains, isolated membranes rather than intact cells were used. The use of isolated membranes allows the minimization of potential effects due to: (i) the transmembrane electric field, which affects forward electron transfer (Diner and Joliot, 1976) and charge recombination (Joliot and Joliot, 1980), (ii) the uncontrolled redox state of the plastoquinone pool in whole cells, which can affect the QB/QB- ratio present in dark-adapted PSII, (iii) differences in the size and composition of the phycobilisomes and in their association with PSII, and (iv) the presence of photoprotective mechanisms such as excitation energy quenching and scavengers of reactive oxygen species.

## Results

### Fluorescence decay kinetics in the three types of PSII

The electron transfer properties of the three types of PSII were investigated by comparing the decay kinetics of the flash-induced fluorescence in membranes from A. marina, white-light (WL) grown C. thermalis and far-red-light (FR) grown C. thermalis. When forward electron transfer occurs (Figure 2A), the fluorescence decay comprises three phases (Crofts and Wraight, 1983; Vass et al., 1999): the fast phase (~0.5ms) is attributed to electron transfer from QA- to QB or QB- and the middle phase (~3ms) is generally attributed to QA- oxidation limited by plastoquinone (PQ) entry to an initially empty QB site and/or by QBH2 exiting the site prior to PQ entry (de Wijn and van Gorkom, 2001). These two phases had comparable time-constants in all samples (T1=0.5–0.6 and T2=3.5–5ms, Table 1). The fast electron transfer from QA- to the non-heme iron possibly oxidized in a fraction of centres is too fast (t½~50 µs) to be detected here.

![Figure 2.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig2-v3.jpg)

**Figure 2.:** The datapoints represent the averages of three biological replicates,± s.d. (provided in Figure 2—source data 1), the lines represent the fits of the experimental data. All traces are normalized on the initial variable fluorescence (Fm-F0, with Fm measured 190 μs after the saturating flash). The full 100 s traces of the data in (A) are shown in Figure 2—figure supplement 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** These are the same traces as in Figure 2A but here including all points up to 100 s. The datapoints represent the averages of three biological replicates,±s.d., while the lines represent the fits of the experimental data. All traces are normalized on the initial variable fluorescence (Fm-F0, with Fm measured 190 μs after the saturating flash). Note that the fluorescence rise observed at the end of the A. marina decay is present in only one of the three replicates used to do the averages (see Figure 2—source data 1) and is considered to be a measurement artefact.

**Table 1.**
 Time constants and relative amplitudes (%) of the different phases of fluorescence decay obtained by fitting the data in Figure 2 and Figure 2—figure supplement 1.Statistically significant differences according to Student’s t-tests are indicated with asterisks (*p≤0.05, **p≤0.01, ***p≤0.001, ****p≤0.0001).


<table>
  <thead>
    <tr>
      <th colspan="4">No addition (1 s)*</th>
    </tr>
    <tr>
      <th rowspan="2">Strain</th>
      <th>Fast phase</th>
      <th>Middle phase</th>
      <th>Slow phase +y0</th>
    </tr>
    <tr>
      <th>T1/Amp (ms/%)</th>
      <th>T2/Amp (ms/%)</th>
      <th>Amp (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A. marina</td>
      <td>0.58±0.21 / 26±5</td>
      <td>4.9±1.3 / 32±5</td>
      <td>42±3**</td>
    </tr>
    <tr>
      <td>C. thermalis WL</td>
      <td>0.50±0.09 / 32±3</td>
      <td>3.7±0.4 / 37±4</td>
      <td>31±2</td>
    </tr>
    <tr>
      <td>C. thermalis FR</td>
      <td>0.53±0.16 / 26±4</td>
      <td>4.7±0.7 / 45±4</td>
      <td>30±3</td>
    </tr>
    <tr>
      <td>No addition 100 s†</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Not bound</td>
      <td>Middle phase</td>
      <td>Slow phase</td>
    </tr>
    <tr>
      <td>Strain</td>
      <td>T1/Amp (ms/%)</td>
      <td>T2/Amp (s/%)</td>
      <td>T3/Amp (s/%)</td>
    </tr>
    <tr>
      <td>A. marina</td>
      <td>-/-</td>
      <td>0.98±0.58 / 19±8</td>
      <td>6.5±1.0 / 81±8</td>
    </tr>
    <tr>
      <td>C. thermalis WL</td>
      <td>2.0±0.9 / 5±1</td>
      <td>0.25±0.04 / 17±1</td>
      <td>6.9±0.3 / 78±1</td>
    </tr>
    <tr>
      <td>C. thermalis FR</td>
      <td>2.7±0.9 / 6±1</td>
      <td>1.31±0.35** / 14±3</td>
      <td>10.4±0.8** / 80±3</td>
    </tr>
    <tr>
      <td colspan="4">DCMU (100 s)‡</td>
    </tr>
    <tr>
      <td rowspan="2">Strain</td>
      <td>Fast phase</td>
      <td>Middle phase</td>
      <td>Slow phase</td>
    </tr>
    <tr>
      <td>T1/Amp (ms/%)</td>
      <td>T2/Amp (ms/%)</td>
      <td>T3/Amp (s/%)</td>
    </tr>
    <tr>
      <td>A. marina</td>
      <td>1.8±0.3 / 47±3***</td>
      <td>44.7±11.2 / 26±3</td>
      <td>10.8±2.6* / 27±1****</td>
    </tr>
    <tr>
      <td>C. thermalis WL</td>
      <td>1.7±0.2 / 62±2</td>
      <td>99.8±23.5*/ 24±2</td>
      <td>5.6±2.4 / 14±2</td>
    </tr>
    <tr>
      <td>C. thermalis FR</td>
      <td>2.2±0.3 / 58±3</td>
      <td>38.7±10.3 / 26±3</td>
      <td>14.3±4.6* / 16±1</td>
    </tr>
  </tbody>
</table>

_*The decay kinetics measured over 100 s in samples with no additions were truncated at 1 s and fitted with a three exponential equation allowing y0 to account for the part decaying in >1 s. For this reason, the cumulative amplitude of the slowest exponential decay phase and of y0 is provided, but no T3.†The decay kinetics recorded over a period of 100 s were fitted with two exponentials and one hyperbole. In the case of A. marina, fitting of the fluorescence decay kinetics was done by excluding the datapoints between 30 and 100 s after flash, because of the presence of a non-decaying fluorescence that likely arises from a fraction of centres devoid of an intact Mn-cluster in which QA- is stabilised.‡The data recorded in the presence of DCMU over a period of 100 s were fitted with two exponentials (only one in the case of A. marina) and one hyperbole._

The slower decay phase is attributed to the charge recombination between QA- and the Mn-cluster mostly in the S2 state (see section 2.2) in centres where forward electron transfer to QB/QB- did not occur. This phase was significantly slower in FR C. thermalis (T3=14.3 ± 4.6 s) than in WL C. thermalis (T3=5.6 ± 2.4 s) but had a similar amplitude in the two samples (Figure 2—figure supplement 1 and Table 1). In A. marina this phase had a bigger amplitude than in the two C. thermalis samples (Table 1), because it was superimposed to a non-decaying component of the fluorescence, that did not return to the original F0 level even at 100 s after the flash (Figure 2—figure supplement 1). This non-decaying component, absent in the two C. thermalis samples, is attributed to centres without a functional Mn-cluster, in which PD1+ is reduced by an electron donor that does not recombine in the minutes timescale (such as Mn2+, TyrD, or the ChlZ/Car side-path), with the consequence of stabilizing QA- (Nixon et al., 1992; Debus et al., 2000). The fluorescence decay arising from the S2QA- recombination was slower in A. marina (T3=10.8 ± 2.6 s) than in WL C. thermalis, but its overlap with the non-decaying component made the fit of its time-constant potentially less reliable.

Indeed, when the fluorescence decay due to charge recombination was measured in presence of the QB-site inhibitor DCMU (Figure 2B), the decay kinetics were bi-phasic in all samples, and no difference in the major S2QA- recombination phase (slow phase in Table 1, ~80% amplitude, T3 ~6–7 s) was found between A. marina and WL C. thermalis. In contrast, the decay was significantly slower in FR C. thermalis, with the time-constant of the major S2QA- recombination phase (slow phase in Table 1, ~80% amplitude, T3=10.4 ± 0.8 s) similar to that measured in the absence of DCMU. The shorter lifetime (~0.22–1 s) of the middle decay phase (amplitude 15–20%) was compatible with it originating from TyrZ•(H+)QA- recombination occurring either in centres lacking an intact Mn-cluster (Yerkes et al., 1983) or in intact centres before charge separation is fully stabilised, as proposed in Debus et al., 2000. The fluorescence decay in WL and FR C. thermalis also had an additional fast phase of small amplitude (5–6%), attributed to forward electron transfer in centres in which DCMU was not bound (Lavergne, 1983). Again, the A. marina traces included a non-decaying phase of fluorescence, attributed to centres lacking an intact Mn-cluster.

The fluorescence decay kinetics in membranes of Synechocystis sp. PCC6803 (Synechocystis), perhaps the best studied Chl-a containing cyanobacterium, were also measured as an additional control. The kinetics in Synechocystis membranes were comparable to those reported for WL C. thermalis (Appendix 1). The Synechocystis and A. marina fluorescence decay kinetics measured in membranes here are overall slower than those previously measured in cells (Cser et al., 2008). This difference is ascribed to pH and membrane potential effects, as discussed in Appendix 1, and illustrates the difficulty to use whole cells for such measurements.

To conclude, the forward electron transfer rates from QA- to QB/QB- are not significantly different in the three types of PSII. In contrast, the S2QA- recombination is slower in Chl-f-PSII of FR C. thermalis compared to Chl-a-PSII of WL C. thermalis and Chl-d-PSII of A. marina.

### S-state turnover efficiency in the far-red PSII

The efficiency of PSII water oxidation activity can be estimated by the flash-dependent progression through the S-states of the Mn-cluster. This can be measured by thermoluminescence (TL), which arises from radiative recombination of the S2QB- and S3QB- states (Rutherford et al., 1982). The TL measured in A. marina, WL C. thermalis, and FR C. thermalis membranes showed similar flash-dependencies in all three types of PSII (Appendix 2—figure 1), confirming and extending the earlier report (Nürnberg et al., 2018). Because the TL data presented some variability between biological replicates (Appendix 2), additional analyses were performed by polarography and absorption spectroscopy.

Figure 3 shows the flash-dependent oxygen evolution measured in A. marina, FR C. thermalis and Synechocystis membranes. The latter were used as a Chl-a-PSII control because the content of PSII in membranes of WL C. thermalis was too low to allow accurate O2 polarography measurements (Figure 3—figure supplement 1D). As shown by fluorescence, no significant difference in forward electron transfer between the two types of Chl-a-PSII was observed (Appendix 1), and the use of Synechocystis membranes was therefore considered as a valid control.

![Figure 3.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig3-v3.jpg)

**Figure 3.:** (A–C) Patterns of oxygen release in A. marina, FR C. thermalis and Synechocystis membranes. Flashes were given at 900 ms intervals and the O2 produced after each flash was measured. Flashes were provided by a white xenon flash lamp, a red LED centered at 613 nm, and a far-red LED centered at 730 nm. The data represent the averages of 3 biological replicates ±s.d. The lines represent the fits of the experimental data. The data were normalized to the O2 yield of the last of the 40 flashes sequence. The non-normalized data are shown in Figure 3—figure supplement 1. Normalized and non-normalized data are provided in Figure 3—source data 1. (D) Miss factors (in %) calculated from the data shown in (A–C). The miss factor in Synechocystis membranes flashed at 730 nm is significantly higher than in A. marina and FR C. thermalis membranes according to Student’s t-test, as indicated with asterisks (****p≤0.0001).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** (A–D) Patterns of oxygen release in A. marina, FR C. thermalis, Synechocystis, and WL C. thermalis membranes, with 10 µg of chlorophyll used for each sample. Flashes were given at 900 ms intervals and the O2 produced after each flash was measured. Flashes were provided by a white xenon flash lamp (pulse length of 10 µs, 540 µJ), a red LED centered at 613 nm (pulse length of 40 µs, 270 µJ), and a far-red LED centered at 730 nm (pulse length of 40 µs, 270 µJ). The data represent the averages of 3 biological replicates ±s.d. The lines represent the fits of the experimental data. The data in panels A, B, and C are the same as the normalized ones represented in Figure 3.

The measurements were performed using white, red, and far-red flashes. As expected, in dark-adapted samples, with S1 as the majority state (Table 2), the maximal O2 evolution occurred on the 3rd flash with subsequent maxima at 4 flash intervals. These maxima reflect the occurrence of the S3YZ●/S4 to S0 transition in most centres as two water molecules are oxidized, resulting in the release of O2. This oscillation pattern was the same in all samples and under all excitation conditions, except in Synechocystis membranes illuminated with far-red light, where the slow rise in O2 evolution is due to the weak excitation of Chl-a-PSII by the short wavelength tail of the 730 nm flash.

**Table 2.**
 Initial distribution of S-states obtained by fitting the flash-dependent oxygen evolution data in Figure 3.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="3">FR C. thermalis</th>
      <th colspan="3">A. marina</th>
      <th colspan="3">Synechocystis</th>
    </tr>
    <tr>
      <th>613 nm LED</th>
      <th>730 nm LED</th>
      <th>Flashlamp</th>
      <th>613 nm LED</th>
      <th>730 nm LED</th>
      <th>Flashlamp</th>
      <th>613 nm LED</th>
      <th>730 nm LED</th>
      <th>Flashlamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>S0 (%)</td>
      <td>15.7</td>
      <td>15.3</td>
      <td>14.9</td>
      <td>15.6</td>
      <td>15.9</td>
      <td>15.2</td>
      <td>22.3</td>
      <td>18.7</td>
      <td>19.7</td>
    </tr>
    <tr>
      <td>S1 (%)</td>
      <td>84.3</td>
      <td>84.7</td>
      <td>85.1</td>
      <td>75.4</td>
      <td>76.1</td>
      <td>75.8</td>
      <td>66.7</td>
      <td>73.3</td>
      <td>71.3</td>
    </tr>
    <tr>
      <td>S2 (%)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>8</td>
      <td>9</td>
      <td>11</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>

The miss factor, indicating the fraction of PSII centres failing to progress through the S-states after a saturating flash excitation (Lavergne, 1991; Grabolle and Dau, 2007 and see Discussion ), was ≤20% in all the samples except in the Synechocystis sample illuminated with far-red flashes, where it was >80% (Figure 3D). For A. marina, the misses (13–17%) were very similar to those reported earlier (Shevela et al., 2006). The misses in FR C. thermalis and in Synechocystis when illuminated with the 613 nm LED were slightly higher (17%–20%). Nevertheless, these differences, attributed to the combination of the absence of exogenous electron acceptors, and the relatively long and possibly not fully saturating flashes (Figure 3—figure supplement 1), were not significant.

In order to confirm and expand the results obtained with polarography, we measured the S-state turnover as the flash-induced absorption changes at 291 nm (Figure 4), that reflect the redox state of the Mn ions in the oxygen evolving complex (Lavergne, 1991; Boussac et al., 2004). These measurements were done in the presence of the electron acceptor PPBQ and using single-turnover monochromatic saturating laser flashes. In the case of A. marina, the measurements could be done using membranes, but the membranes of WL and FR C. thermalis could not be used because of their high light-scattering properties in the UV part of the spectrum. In the case of the FR C. thermalis partially purified O2 evolving Chl-f-PSII were made and used for the measurements, while difficulties were encountered in isolating O2 evolving PSII from WL C. thermalis. Therefore, PSII cores from T. elongatus with the D1 isoform PsbA3 (Sugiura et al., 2008) were used as a Chl-a-PSII control. Among the three D1 present in T. elongatus, PsbA3 has the highest sequence identity with the D1 of Chl-f-PSII in FR C. thermalis (see Discussion).

![Figure 4.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig4-v3.jpg)

**Figure 4.:** Absorption changes were measured at 291 nm at 100 ms after each of a series of single-turnover saturating flashes fired with a 300 ms time interval. (A) and (B) Measurements in FR C. thermalis PSII cores using flashes at the indicated wavelengths with 100% and 83% laser power (the power of the laser at the different wavelengths is reported in Appendix 7). (C) Comparison between the absorption changes obtained in FR C. thermalis PSII cores and A. marina membranes using flashes at the indicated wavelengths (100% laser power). The traces in (C) were normalized on the maximal oscillation amplitude (3rd minus 5th flash). The breaks in the vertical axes in panels (A–C) allow the oscillation pattern to be re-scaled for clarity, because the absorption change on the first flash contains a large non-oscillating component (Lavergne, 1991) that was not included in the fits. (D) Measurements in isolated T. elongatus PsbA3-PSII cores using flashes at the indicated wavelengths. All data are provided in Figure 4—source data 1.

The Chl-f-PSII was illuminated with flashes at wavelengths preferentially absorbed by Chl-a (680 nm) and by long-wavelength chlorophylls (720–750 nm) (Figure 4A). As expected, maximum absorption decrease (positive ΔI/I, as defined in Materials and methods, section UV transient absorption) occurred on S2 (flash 1,5,9 etc.) and maximum absorption increase (negative ΔI/I) on S0 (flash 3,7,11 etc.) (Lavergne, 1991). No differences could be observed in either the amplitude or the damping of the oscillations between the excitation wavelengths. When using sub-saturating flashes (~83% power), the damping of the oscillations was the same for all excitation wavelengths (Figure 4B), verifying that the illumination with 100% laser power was saturating at all the wavelengths. The equal amplitude of the oscillations obtained at all excitation wavelengths also indicates that the FR C. thermalis sample used does not contain any detectable Chl-a-PSII contamination. No differences in the oscillation patterns measured in FR C. thermalis Chl-f-PSII cores and in A. marina membranes, flashed at either 680 or 725 nm, were observed (Figure 4C). The PSII of T. elongatus showed a normal S-states progression when using 680 nm excitation, but no oscillation pattern when far-red flashes were used (Figure 4D). For all samples the calculated miss factor was ~10% (Appendix 3, discussion based on Styring and Rutherford, 1987; Velthuys and Visser, 1975; Vermaas et al., 1984; Sugiura et al., 2004).

In conclusion, the data reported here show that the overall efficiency of electron transfer from water to the PQ pool is comparable in all three types of PSII (independently of the Chl-a-PSII control used), as shown by the near-identical flash patterns of thermoluminescence (Appendix 2) and O2 release (Figure 3), both measured without external electron acceptors. When the S-state turnover was measured by following the absorption of the Mn-cluster in the UV (Figure 4), the use of artificial electron acceptors and single-turnover saturating flashes allowed us to obtain better resolved flash patterns that were essentially indistinguishable in all three types of PSII and between excitation with visible or far-red light in the case of the Chl-d-PSII and Chl-f-PSII.

### Back-reactions measured by (thermo)luminescence

Charge recombination reactions were investigated by monitoring the thermoluminescence and luminescence emissions. The TL curves in Figure 5A and B show that both Chl-f-PSII and Chl-d-PSII are more luminescent than Chl-a-PSII, with Chl-f-PSII being the most luminescent. These differences, that are much larger than the variability between biological replicates (Figure 5—figure supplement 1C and D and Table 3), fit qualitatively with earlier reports (Nürnberg et al., 2018; Cser et al., 2008) (see Appendix 4 for more details). The high luminescence indicates that in the Chl-d-PSII and Chl-f-PSII there is an increase in radiative recombination, although the causes of this increase are likely to be different between the two photosystems, as detailed in the Discussion.

![Figure 5.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig5-v3.jpg)

**Figure 5.:** (A) and (B) TL measured in the absence of inhibitors (S2QB-) or in the presence of DCMU (S2QA-), respectively. The signal intensities are normalized on the content of O2-evolving PSII of each sample, measured as the maximal oxygen evolution rates under saturating illumination. The dashed vertical lines indicate the two peak positions of the C. thermalis samples. (C) Plots of the total S2QA- luminescence emission (integrated area below the curves), normalized on the maximal oxygen evolution rate of each sample, at 10, 20, and 30°C. (D) Plots of the average S2QA- luminescence decay lifetimes (τav), calculated from the decay phases attributed to S2QA- recombination, as a function of temperature. In (C) and (D) each point represents the average of 3 biological replicates ±s.d. Statistically significant differences according to Student’s t-tests are indicated with asterisks (*p≤0.05, **p≤0.01, ***p≤0.001, ****p≤0.0001).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** Plots of the temperatures (A and B) and of the normalized amplitudes (C and D) of the thermoluminescence peaks deriving from S2QB- and from S2QA- back-reaction, including the examples shown in Figure 5A and B. In C and D, the TL peak amplitudes are normalized on the content of O2-evolving PSII of each sample, measured as the maximal oxygen evolution rates under saturating illumination. Each point represents an independent biological replicate, the horizontal lines represent the mean values ± standard error (for S2QB-: A. marina n=5, WL C. thermalis n=5, FR C. thermalis n=7; for S2QA-: A. marina n=5, WL C. thermalis n=5, FR C. thermalis n=5). All curves are provided in Figure 5—figure supplement 1—source data 1. Statistically significant differences according to Student’s t-tests are indicated with asterisks (*p≤0.05, **p≤0.01, ***p≤0.001, ****p≤0.0001).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** (A) Thermoluminescence measured in the absence of inhibitors (S2QB-) or in the presence of DCMU (S2QA-) in Synechocystis membranes. The dashed vertical lines indicate the two peak positions. (B) Plots of the average S2QA- luminescence decay lifetimes (τav) in A. marina, WL C. thermalis, FR C. thermalis and Synechocystis membranes. Each series of data corresponds to an independent biological replicate. The A. marina, WL C. thermalis and FR C. thermalis datasets are those used to calculate the average decay values plotted in Figure 5D. (C) Representative S2QA- luminescence decay curves measured in Synechocystis membranes at 10, 20, and 30°C, after normalization on the initial intensities. The luminescence decays were measured for 300 s after the flash and plotted on a logarithmic scale. All Synechocystis curves are provided in Figure 5—figure supplement 2—source data 1.

**Table 3.**
 Average values (± s.d.) of the temperatures (T) and of the normalized amplitudes (Amp, in relative units) of the thermoluminescence peaks from S2QB- and from S2QA- back-reactions, plotted in Figure 5—figure supplement 1.The difference in temperature between the S2QB- and the S2QA- (ΔT) is also reported. The ΔT in A. marina is significantly bigger than the one in WL and FR C. thermalis according to Student’s t-test, as indicated with an asterisk (*p≤0.05).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">S2QB-</th>
      <th colspan="2">S2QA-</th>
      <th rowspan="2">ΔT (°C)</th>
    </tr>
    <tr>
      <th>Strain</th>
      <th>T (°C)</th>
      <th>Amp (r.u.)</th>
      <th>T (°C)</th>
      <th>Amp (r.u.)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A. marina</td>
      <td>46.5±1.8</td>
      <td>2.77±1.15</td>
      <td>14.9±3.7</td>
      <td>1.15±0.55</td>
      <td>31.5±2.8*</td>
    </tr>
    <tr>
      <td>WL C. thermalis</td>
      <td>52.9±3</td>
      <td>0.65±0.31</td>
      <td>28.1±1.7</td>
      <td>0.54±0.21</td>
      <td>24.9±3.2</td>
    </tr>
    <tr>
      <td>FR C. thermalis</td>
      <td>50.3±4.7</td>
      <td>4.61±1.29</td>
      <td>26±3.3</td>
      <td>3.27±0.88</td>
      <td>24.3±5.1</td>
    </tr>
  </tbody>
</table>

Despite the large difference in TL intensity between the Chl-a-PSII and Chl-f-PSII, the peak temperatures corresponding to the S2QB- and S2QA- recombination were both similar in Chl-a-PSII and Chl-f-PSII. In Chl-d-PSII, the temperature of the S2QB- peak was only slightly lower, while the S2QA- peak was ~15 °C lower (Figure 5—figure supplement 1A and B and Table 3). Earlier TL reports comparing Chl-d-PSII in A marina cells with Chl-a-PSII in Synechocystis cells also showed that, while the peak position of S2QB- recombination was similar in the two samples, the S2QA- peak position was lower in A. marina (Cser et al., 2008), in agreement with the present results in membranes. The peak temperatures measured in cells were lower than those reported here, which can be explained by (i) the effect of the transmembrane electric field, as discussed for the fluorescence decay results, and (ii) by differences in the heating rates used (1 °C s–1 here, 0.33 °C s–1 in Cser et al., 2008). When performing the same measurements in Synechocystis membranes (Figure 5—figure supplement 2A), the S2QB- and S2QA- peak positions were comparable to those obtained in the two C. thermalis samples, confirming that the lower S2QA- peak temperature is a specific feature of Chl-d-PSII.

The S2QA- recombination in the presence of DCMU was also measured by luminescence decay kinetics at 10, 20, and 30°C, a range of temperatures that covers those of the S2QA- TL peaks of the three samples. Luminescence decay kinetics were recorded from 570ms for 300 seconds after the flash. In this time-range, the luminescence arises mainly from recombination via the back-reaction of S2QA- (Goltsev et al., 2009). The total S2QA- luminescence emission (Figure 5C) reflected the intensities of the TL peaks, as expected (Rutherford and Inoue, 1984), with the order of intensity as follows: Chl-f-PSII>Chl-d-PSII>Chl-a-PSII (although the variability between replicates made the difference between Chl-a-PSII and Chl-d-PSII less significant than that measured by TL). The total emissions did not vary significantly between 10°C and 30°C, although the decay kinetics were temperature-sensitive (Appendix 5—figure 1). The decay components identified by fitting the curves and their significance are discussed further in Appendix 5, based on Yerkes et al., 1983; Lavorel and Dennery, 1984; Tyystjarvi and Vass, 2007; Sugiura et al., 2014. The luminescence decay attributed to S2QA- recombination was bi-phasic (Appendix 5—table 1), with the kinetics of both phases being faster in Chl-d-PSII (~3 and~11 s) than in Chl-a-PSII (~4 and~25 s), but slower in Chl-f-PSII (~9 and~39 s). The average S2QA- luminescence decay lifetimes accelerated with increasing temperature in Chl-a-PSII and Chl-f-PSII but were always the fastest in Chl-d-PSII and the slowest in Chl-f-PSII (Figure 5D). The luminescence decay kinetics of the Chl-a-PSII in Synechocystis membranes were similar to those measured in WL C. thermalis (Figure 5—figure supplement 2B and C), suggesting, as seen with the TL data, that the differences in kinetics observed in the two types of far-red PSII are not due to differences between species.

In conclusion, both Chl-f-PSII and Chl-d-PSII show strongly enhanced luminescence, as previously reported (Nürnberg et al., 2018; Cser and Vass, 2007). However, the Chl-d-PSII differs from the Chl-a-PSII and Chl-f-PSII by having a lower S2QA- TL peak temperature and a faster S2QA- luminescence decay. This indicates that Chl-d-PSII has a smaller energy gap between QA- and Phe compared to Chl-a-PSII and Chl-f-PSII, resulting in: (i) less heat required for the electron to be transferred energetically uphill from QA- to Phe (manifest as lower TL peak temperature), and (ii) a bigger proportion of S2QA- recombination occurring via repopulation of PD1+Phe-, a route faster than direct PD1+QA- recombination (manifest as faster luminescence decay kinetics, see also Appendix 5). The lower TL temperature and faster luminescence decay for S2QA- recombination in Chl-d-PSII, but without a marked increase in its QA- decay rate as monitored by fluorescence (Figure 2), could reflect differences in the competition between radiative and non-radiative recombination pathways in Chl-d-PSII compared to those in Chl-a-PSII and Chl-f-PSII. In contrast, in Chl-f-PSII the energy gap between QA- and Phe does not appear to be greatly affected or could even be larger, as suggested by the slower S2QA- recombination measured by fluorescence (Figure 2) and luminescence (Figure 3) decay. The QB potentials appear to be largely unchanged, as manifested by the similar S2QB- stability in all three types of PSII, with the slightly lower S2QB- TL peak temperature in A. marina probably reflecting the decrease in the energy gap between QA- and Phe.

### Singlet oxygen production and sensitivity to high light in the far-red PSII

The smaller energy gap between QA- and Phe reported here in A marina is expected to result in enhanced singlet O2 production and hence greater sensitivity to photodamage (Nürnberg et al., 2018; Cotton et al., 2015; Johnson et al., 1995; Vass and Cser, 2009). This was investigated by measuring the rates of 1O2 generation induced by saturating illumination in isolated membranes using histidine as a chemical trap (Figure 6A, representative traces in Figure 6—figure supplement 1A-C). 1O2 reacts with histidine to form the final oxygenated product, HisO2, resulting in the consumption of O2, as measured using the O2 electrode. Without the histidine trap, most 1O2 is thought to be quenched by carotenoids (Telfer et al., 1994). When histidine was present in addition to DCMU, the Chl-d-PSII in A. marina membranes showed significant light-induced 1O2 formation. Under the same conditions, little 1O2 formation occurred in Chl-a-PSII or Chl-f-PSII in C. thermalis membranes. Similarly low levels of 1O2 were generated by Chl-a-PSII in Synechocystis membranes (Figure 6—figure supplement 1D). The His-dependent O2 consumption in A. marina membranes showed the same light intensity dependence as O2 evolution (Appendix 6—figure 1B), which suggests that 1O2 formation was related to Chl-d-PSII photochemistry. Sodium azide, a 1O2 quencher, suppressed the His-dependent oxygen consumption measured in A. marina in the presence of DCMU and when using the 1O2-generating dye Rose Bengal, confirming that it was due to the production of 1O2 (Figure 6—figure supplement 1E and F).

![Figure 6.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig6-v3.jpg)

**Figure 6.:** All samples were used at a chlorophyll concentration of 5 µg ml–1. (A) 1O2 production in presence of DCMU measured as the rate of histidine-dependent consumption of O2 induced by saturating illumination (xenon lamp, 7100 µmol photons m–2 s–1, saturation curves in Appendix 6). The data are averages (± s.d.) of six biological replicates for A. marina and FR C. thermalis and three replicates for WL C. thermalis for the DCMU +His samples, and of four biological replicates for FR C. thermalis and three replicates for A. marina and WL C. thermalis for the DCMU samples. For each replicate, the rates of oxygen consumption were normalized to the maximal oxygen evolution rates measured in presence of DCBQ and ferricyanide. The non-normalized rates of each replicate are provided in Appendix 6. All traces are provided in Figure 6—source data 1. (B) Maximal PSII activities, measured as in (A), after 30 min illumination with saturating red light (660 nm LED, 2600 µmol photons m–2 s–1) relative to the maximal activities measured in control samples kept in darkness (provided in Figure 6—source data 2). The light used for the 30 min treatment was as saturating as the xenon lamp used in (A) (see Appendix 6). The data are averages of three biological replicates ±s.d. Statistically significant differences according to Student’s t-tests are indicated with asterisks (*p≤0.05, **p≤0.01, ***p≤0.001).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig6-figsupp1-v3.jpg)

**Figure 6—figure supplement 1.:** All samples were used at a chlorophyll concentration of 5 µg ml–1. (A, B, C and D) Representative O2 electrode traces monitoring O2 evolution and uptake. 1O2 production in presence of DCMU was measured as the rate of histidine-dependent consumption of O2 induced by saturating illumination (xenon lamp, 7100 µmol photons m–2 s–1). Measurements were performed in in presence of DCBQ and ferricyanide (Acceptors), or in presence of DCMU, with or without the addition of histidine (His). Synechocystis traces are provided in Figure 6—figure supplement 1—source data 1. (E and F) 1O2 production in a different A. marina membrane preparation and when using Rose Bengal to generate 1O2, respectively, showing the effect of sodium azide (NaN3) (traces in Figure 6—figure supplement 1—source data 1). Sodium azide is a 1O2 quencher that regenerates O2 in competition with 1O2 scavenging by histidine. All traces are shown after subtraction of the dark baseline.

The strikingly high amount of 1O2 generated by Chl-d-PSII prompted us to perform additional controls. (i) To test if the high 1O2 production was related to the intactness of the PSII donor side, Mn was removed from A. marina membranes by Tris-washing. This had little effect on the 1O2 formation with respect to the Mn-containing membranes (Appendix 6—figure 2), suggesting that the high 1O2 production in untreated A. marina membranes does not arise specifically from the fraction of centres lacking an intact Mn-cluster that are potentially responsible for the non-decaying fluorescence observed in Figure 2. (ii) The possibility that photosystem I (PSI) contributed to the light-induced O2 consumption by reducing oxygen to O2•- in membranes was tested (Appendix 6—figure 3). In the presence of DCMU, PSI-driven O2 reduction mediated by methyl viologen only took place when exogenous electron donors to PSI were provided. This indicates that there is no contribution from PSI-induced O2 reduction in Figure 6A, where exogenous PSI donors are absent. (iii) The higher 1O2 production is also seen in A. marina cells compared to FR C. thermalis cells (Appendix 6—figure 4A), and thus is not an artefact associated with the isolation of membranes (e.g. damaged photosystems or free chlorophyll). WL C. thermalis cells also showed low levels of 1O2 production, similar to those measured in membranes (Appendix 6—figure 4B). The reliability of the His-trapping method to monitor 1O2 production in intact cyanobacterial cells has been previously demonstrated (Rehman et al., 2013).

Figure 6B shows the effect of 30 min of saturating illumination (red light) on the activity of the Chl-d-PSII, Chl-a-PSII and Chl-f-PSII. The results show that Chl-d-PSII is significantly more susceptible to light induced loss of activity compared to Chl-f-PSII, and to a lesser extent to Chl-a-PSII, and this can be correlated to the higher levels of 1O2 production in Chl-d-PSII.

## Discussion

We investigated several functional properties of the two different types of far-red PSII, (i) the constitutive Chl-d-PSII of A. marina, and (ii) the facultative Chl-f-PSII of C. thermalis. We compared these properties with each other and with those of Chl-a-PSII, from either WL C. thermalis, Synechocystis or T. elongatus, looking for differences potentially related to the diminished energy available in the two long-wavelength PSII variants.

### Forward electron transfer and enzymatic activity

The turnover of the water oxidation cycle is comparably efficient in all three types of PSII, as shown by their near-identical flash patterns in thermoluminescence (Appendix 2—figure 1), O2 release (Figure 3), and UV spectroscopy (Figure 4). In PSII, a photochemical ‘miss factor’ can be calculated from the damping of the flash patterns of O2 evolution. These misses, which are typically ~10% in Chl-a-PSII, are mainly ascribed to the µs to ms recombination of S2TyrZ•QA- and S3TyrZ•QA- states (Grabolle and Dau, 2007). Despite the diminished energy available, the miss factors in both types of far-red PSII were virtually unchanged compared to Chl-a-PSII, which also suggests that the misses have the same origin. If so, the energy gaps between TyrZ and PD1, and thus their redox potentials, would be essentially unchanged. These conclusions agree with those in earlier work on Chl-d-PSII (Shevela et al., 2006) and on Chl-f-PSII (Nürnberg et al., 2018).

The similar flash-patterns also indicate that, after the primary charge separation, the electron transfer steps leading to water oxidation must have very similar efficiencies in all three types of PSII, that is, close to 90%, and that there are no major changes affecting the kinetics of forward electron transfer. In the case of Chl-f-PSII, this confirms earlier suggestions based on flash-dependent thermoluminescence measurements (Nürnberg et al., 2018). Indeed, electron transfer from QA- to QB/QB-, monitored by fluorescence, showed no significant differences in kinetics in the three types of PSII (Figure 2A).

### Back reactions and singlet oxygen production

The most striking difference between the three types of PSII is that the Chl-d-PSII of A. marina shows a decreased stability of S2QA-, indicated by the lower temperature of its TL peak and the correspondingly faster luminescent decay kinetics (Figure 5), and consequently a significant increase in 1O2 generation under high light (Figure 6A). This likely corresponds to the decrease in the energy gap between Phe and QA predicted to result from the ~100 meV lower energy available when using light at ~720 nm to do photochemistry (Nürnberg et al., 2018; Cotton et al., 2015). This is also supported by the estimates in the literature of the redox potential (Em) values of Phe/Phe- and QA/QA- in Mn-containing Chl-d-PSII: compared to Chl-a-PSII, the estimated increase of ~125 mV in the Em of Phe/Phe- is accompanied by an estimated increase of only ~60 mV in the Em of QA/QA-, which implies that a normal energy gap between the excited state of the primary donor (ChlD1*) and the first and second radical pairs (ChlD1+Phe- and PD1+Phe-) is maintained, but the energy gap between PD1+Phe- and PD1+QA- is significantly decreased (~325 meV vs ~385 meV) (Allakhverdiev et al., 2011). The changes in the D1 and D2 proteins of A. marina responsible for the changes in the Em of Phe/Phe- and QA/QA- are currently unknown.

Our results indicate that in Chl-d-PSII, the decrease in the energy gap between Phe and QA favours charge recombination by the back-reaction route (via PD1+Phe-), forming the reaction centre chlorophyll triplet state (Rutherford et al., 1981), which acts as an efficient sensitizer for 1O2 formation (Johnson et al., 1995; Vass and Cser, 2009; Keren et al., 1995; Keren et al., 2000). Consequently, the Chl-d-PSII is more sensitive to high light (Figure 6B), reflecting the fact that this long-wavelength form of PSII has evolved in shaded epiphytic environments (Nürnberg et al., 2018; Miyashita et al., 1996; Cotton et al., 2015; Davis et al., 2016; Murakami et al., 2004; Miller et al., 2005; Kühl et al., 2005; Mohr et al., 2010). The increase in the proportion of recombination going via PD1+Phe- in Chl-d-PSII can also result in a higher repopulation of the excited state of the primary donor (ChlD1*), with a consequent increase in radiative decay (high luminescence).

In contrast to the Chl-d-PSII, the Chl-f-PSII shows no increased production of 1O2 and no increased sensitivity to high light compared to Chl-a-PSII, in the conditions tested here (Figure 6). The back-reactions appear to be little different from the Chl-a-PSII except for the more stable (more slowly recombining) S2QA-, as seen by fluorescence (Figure 2) and luminescence (Figure 5) decay. These properties may seem unexpected because this type of PSII has the same energy available for photochemistry as the Chl-d-PSII. In the Chl-d-PSII the lower energy of ChlD1* is matched by an increase in the Em of Phe/Phe-. In the Chl-f-PSII of C. thermalis and of the other Chl-f containing species, the Em of Phe/Phe- is also expected to be increased by the presence, in the far-red D1 isoform, of the strong H-bond from Glu130 (Figure 7), which is characteristic of high-light D1 variants in cyanobacteria (Sugiura et al., 2010). In Chl-a-PSII, this change has been reported to induce an increase in the Em of Phe/Phe- between ~15 and~30 mV (Sugiura et al., 2010; Merry et al., 1998): an increase of this size would only partially compensate for the ~100 meV decrease in the energy of ChlD1* in Chl-f-PSII, and this would result in a smaller energy gap between ChlD1* and the first and second radical pairs ChlD1+Phe- and PD1+Phe-. This would favour the repopulation of ChlD1* by back-reaction from PD1+Phe- (even if the repopulation of PD1+Phe- from the PD1+QA- state did not increase), resulting in the higher luminescence of Chl-f-PSII, as proposed earlier (Nürnberg et al., 2018). Increased decay of the PD1+QA- radical pair via the radiative route could in principle decrease the decay via the triplet route, but the overall small yield of luminescence means that this could be a minor effect.

![Figure 7.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig7-v3.jpg)

**Figure 7.:** (A) Multi-alignment of the D1 proteins of T. elongatus, C. thermalis and A. marina. The Q130E substitution is present also in the far-red light-induced D1 isoform of C. thermalis (C. therm FR) and in two out of three of its non-far-red induced D1 isoforms (C. therm WL2 and 3) but is not present in any of the three D1 isoforms of A. marina. (B) Multi-alignment of the far-red light induced D1 isoforms of C. thermalis and other Chl-f species. The presence of E130 is conserved in the far-red light induced D1 isoforms of most of the cyanobacteria species capable of far-red light photo-acclimation. Both alignments were done using Clustal Omega (Sievers et al., 2011), the sequences were retrieved from the KEGG (https://www.kegg.jp/) and NCBI (https://www.ncbi.nlm.nih.gov/) databases. For each alignment only a 33 amino acid region is shown, the start and end positions with respect to each full sequence are indicated with numbers. The Q130E substitution is highlighted as white font on black background. The far-red D1 sequence from C. thermalis is framed in red. All sequences used for the multi-alignments are provided in Figure 7—source data 1.

Additionally, the longer lifetime of S2QA- recombination in Chl-f-PSII indicates that the Em of QA/QA- has increased to compensate the up-shift in the Em of Phe/Phe- and to maintain an energy gap between Phe and QA large enough to prevent an increase in PD1+Phe- repopulation and thus in reaction centre chlorophyll triplet formation. This situation occurs in the PsbA3-D1 high light variant of T. elongatus, although the protein changes responsible for the increase in the Em of QA/QA- are not known (Sugiura et al., 2010). A slower S2QA- recombination could also arise from an increase in the redox potential of PD1/PD1+ (Diner et al., 2001), but this would likely compromise forward electron transfer in Chl-f-PSII by decreasing the driving force for stabilization of ChlD1+Phe- by the formation of PD1+Phe-, if the redox potential of ChlD1/ChlD1+ was not increased accordingly. If this problem were avoided by an equivalent increase in the redox potential of ChlD1/ChlD1+, this would likely compromise charge separation, as a matching up-shift the ChlD1+/ChlD1* couple would occur, thus decreasing the reductive power of ChlD1*. As a 720 nm pigment, the reducing power of ChlD1* seems likely to be already compromised in Chl-f-PSII. The results here (Figure 2A) show forward electron transfer and charge separation appear to be comparable to Chl-a PSII and so it is unlikely that redox tuning of PD1 and ChlD1 is responsible for the stabilisation of the S2QA- recombination .

### Effects of the pigment composition on the energetics of the far-red PSII

In addition to changes in the redox potentials of Phe and QA, the size and pigment composition of the antennas of Chl-d-PSII and Chl-f-PSII could also contribute to the functional differences reported in the present work. These differences are summarized in Figure 8.

![Figure 8.](https://cdn.elifesciences.org/articles/79890/elife-79890-fig8-v3.jpg)

**Figure 8.:** The top part of the figure represents the localization of the excitation energy over the antenna pigments and ChlD1* (energies in eV, scale on the left side). The localization of the excitation energy is indicated by the coloured boxes (green for Chl-a, orange for Chl-d and brown for Chl-f), without necessarily assuming a full equilibration (see main text). In Chl-a-PSII, the excitation is distributed over ChlD1, 34 antenna Chl-a (light green) and 2 pheophytin a (Phe-a, dark grey); in Chl-d-PSII, the excitation is distributed over ChlD1 and 31 antenna Chl-d (orange) but not over the 1 Chl-a and 2 Phe-a, that transfer excitation downhill to the Chl-d pigments (black arrows); in Chl-f-PSII, the excitation is distributed only over ChlD1 and 4 antenna Chl-f (brown), while the remaining 29 Chl-a and 2 Phe-a transfer excitation energy downhill to the far-red pigments. In Chl-f-PSII, 3 of the far-red antenna pigments are at longer wavelength than ChlD1, so transfer of excitation energy from them to ChlD1 is less efficient (dashed and dotted black arrows, representing the possible heterogeneity in excitation energy transfer kinetics). The grading of the coloured box for Chl-f represents uncertainty in the degree of excited state sharing between the longest wavelength chlorophylls and ChlD1. The bottom part of the figure represents, on the left, the energetics of the radical pairs and the recombination routes in PSII (direct route: via electron tunnelling; triplet route: via the formation of the triplet state of the primary electron donor; radiative route: via luminescence emission), with the electron transfer steps between PD1 and the Mn-cluster omitted for clarity. The solid and dashed grey arrows represent exergonic and endergonic electron transfer, respectively. The horizontal dashed lines represent the standard free energies of ChlD1* (orange), PD1+Phe- (light green) and PD1+QA- (light blue). The PD1+Phe- radical pair, when formed from the backreaction of PD1+QA-, can be either in the singlet state or in the triplet state. 1[PD1+Phe-] recombines via 1[ChlD1+Phe-] and ChlD1*, while 3[PD1+Phe-] recombines via 3[ChlD1+Phe-] and 3ChlD1. The free energy gaps between ChlD1* and PD1+Phe- and between PD1+Phe- and PD1+QA- in Chl-a-PSII (blue) and our current estimates for Chl-d-PSII (black) and Chl-f-PSII (dark red) are represented on the right.

In PSII, two factors will determine the yield of charge separation: (i) the relative population of the excited state of the primary donor, ChlD1*, which depends on the dynamics of excitation energy transfer between pigments, and (ii) the rate of population of the second radical pair, PD1+Phe-, that is more stable (less reversible) than the first radical pair, ChlD1+Phe-. This rate is determined by the rates of the primary charge separation (forming ChlD1+Phe-) and of its stabilization by secondary electron transfer (forming PD1+Phe-), and hence by the energetics of these electron transfer steps.

In the Chl-a-PSII core, the 37 chlorins absorb light between ~660 and~690 nm and are therefore almost isoenergetic to the ChlD1 primary donor absorbing at 680 nm. Given the small energy differences, there is little driving force for downhill ‘funnelling’ of excitation energy to ChlD1, making it a ‘shallow trap’. Different models have been proposed to explain the shallowness of the photochemical trap in Chl-a-PSII.

In the trap-limited model, the transfer of excitation between pigments is significantly faster than the electron transfer reactions leading to PD1+Phe- formation, and a near-complete equilibration of the excitation energy is established over all pigments, including ChlD1, with a distribution that is determined by their individual site energies (van Mieghem et al., 1995; Schatz et al., 1987; Dau and Sauer, 1996). This leads to a low population of ChlD1* (Table 4), that is diminished as a function of the number of quasi-isoenergetic pigments with which it shares the excitation energy.

**Table 4.**
 Excitation energy partitions calculated for the three types of PSII assuming excitation equilibration between the pigments.E* denotes the energy of the excited state, obtained by applying a+5 nm Stoke’s shift to the absorption of the pigments, n is the number of pigments belonging to each state and Pi is the normalized partition of the excited states, calculated following Boltzmann distribution (Laible et al., 1994).


<table>
  <thead>
    <tr>
      <th colspan="4">Chl-a-PSII</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>State</td>
      <td>E*</td>
      <td>n</td>
      <td>Pi</td>
    </tr>
    <tr>
      <td>Bulk Chl-a/Phe-a</td>
      <td>685</td>
      <td>34</td>
      <td>0.878</td>
    </tr>
    <tr>
      <td>ChlD1680</td>
      <td>685</td>
      <td>1</td>
      <td>0.026</td>
    </tr>
    <tr>
      <td>F685</td>
      <td>685</td>
      <td>1</td>
      <td>0.026</td>
    </tr>
    <tr>
      <td>F695</td>
      <td>695</td>
      <td>1</td>
      <td>0.071</td>
    </tr>
    <tr>
      <td colspan="4">Chl-d-PSII</td>
    </tr>
    <tr>
      <td>State</td>
      <td>E*</td>
      <td>n</td>
      <td>Pi</td>
    </tr>
    <tr>
      <td>Chl-a/Phe-a</td>
      <td>685</td>
      <td>3</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>ChlD1720</td>
      <td>725</td>
      <td>1</td>
      <td>0.029</td>
    </tr>
    <tr>
      <td>Bulk Chl-d</td>
      <td>725</td>
      <td>33</td>
      <td>0.969</td>
    </tr>
    <tr>
      <td colspan="4">Chl-f-PSII</td>
    </tr>
    <tr>
      <td>State</td>
      <td>E*</td>
      <td>n</td>
      <td>Pi</td>
    </tr>
    <tr>
      <td>Bulk Chl-a/Phe-a</td>
      <td>685</td>
      <td>32</td>
      <td>0.046</td>
    </tr>
    <tr>
      <td>ChlD1721</td>
      <td>726</td>
      <td>1</td>
      <td>0.075</td>
    </tr>
    <tr>
      <td>F720/A715</td>
      <td>720</td>
      <td>1</td>
      <td>0.043</td>
    </tr>
    <tr>
      <td>F731/A726</td>
      <td>731</td>
      <td>1</td>
      <td>0.117</td>
    </tr>
    <tr>
      <td>F737/A732</td>
      <td>737</td>
      <td>1</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>F748/A743</td>
      <td>748</td>
      <td>1</td>
      <td>0.52</td>
    </tr>
  </tbody>
</table>

_The states are denoted as follows: ChlD1 is the primary donor (Pi highlighted in bold), Bulk indicates the antenna pigments considered as isoenergetic, and F indicates the antenna pigments considered separately from the bulk, with the fluorescence emission wavelength indicated. In the case of the far-red pigments in Chl-f-PSII the peak absorptions (A) are also indicated, as taken from Judd et al., 2020._

In the transfer-to-trap limited model, the small driving force for downhill ‘funnelling’ of excitation energy to ChlD1 causes kinetic bottlenecks for excitation energy equilibration between the core antenna complexes CP43 and CP47 and for excitation energy transfer from these antennas to the reaction centre (Jennings et al., 2000; Pawlowicz et al., 2007; Raszewski and Renger, 2008; Kaucikas et al., 2016). In this scenario, there is not a full equilibration of the excitation energy over all pigments, but the relatively slow and reversible energy transfer from the core antennas to the reaction centre still leads to a relatively low population of ChlD1*.

Irrespectively of the differences in the details of the kinetic limitation to photochemical trapping between the two models, the common requirement for establishing a high quantum yield of charge separation is a sufficiently large overall energy gap (~160 meV, ) between ChlD1* and PD1+Phe-, that comprises the primary charge separation (ChlD1* ↔ ChlD1+Phe-) and secondary electron transfer (ChlD1+Phe- ↔ PD1+Phe-), as shown in Figure 8. An energy gap of this magnitude is required to avoid rapid recombination to the excited state ChlD1*, thereby limiting the probability of its dissipation via non-photochemical relaxation to the ground state in the antenna (Raszewski and Renger, 2008; Schatz et al., 1988).

For Chl-d-PSII the antenna system is comparable to that in Chl-a-PSII: all 34 Chl-d molecules, including the primary donor ChlD1 at ~720 nm, are close in wavelength and thus both systems are expected to have comparable ChlD1* population (Table 4), irrespective of the rate-limitation model assumed. Chl-a-PSII and Chl-d-PSII should therefore have the same energetic requirements to ensure a sufficiently high yield of charge separation. Given that the energy of ChlD1* is ~100 meV lower in Chl-d-PSII than in Chl-a-PSII, the energy level of the second and more stable radical pair, PD1+Phe-, needs to be decreased by ~100 meV in Chl-d-PSII relative to Chl-a-PSII. This corresponds to the published Em of Phe/Phe- (Allakhverdiev et al., 2011) and to the kinetic data (Figures 5 and 6), as detailed in the previous section.

In A. marina membranes, additional Chl-d containing antenna proteins, which form supercomplexes with PSII cores, have been reported to increase the Chl-d-PSII antenna size by almost 200% (Chen et al., 2005). This will likely result in an increased sharing of the excited state, leading to a diminished population of ChlD1*, and thus a bigger requirement for an energy drop between ChlD1* and PD1+Phe- to ensure efficient charge separation. At the same time, the larger near-isoenergetic antenna could also contribute to its higher luminescence, by increasing the probability of ChlD1* decay via radiative emission with respect to photochemical re-trapping (Rappaport and Lavergne, 2009). This is similar to what happens in plant PSII, where the yield of photochemical trapping of excitation energy is decreased by 10–15% by the association of the Light Harvesting Complex antennas (Engelmann et al., 2005).

The pigment layout of Chl-f-PSII is very different from that of Chl-a-PSII and Chl-d-PSII. The 30 Chl-a molecules are energetically separated from ChlD1, absorbing at 720 nm, by >30 nm (>3 kBT). This means the excitation energy resides predominantly on ChlD1* and on the other 4 far-red pigments. If the equilibration of the excitation energy between the 5 far-red pigments were significantly faster than charge separation, this pigment arrangement would result in a higher probability of populating ChlD1* in Chl-f-PSII than in Chl-a-PSII and Chl-d-PSII (Table 4). The higher ChlD1* population in Chl-f-PSII could ensure that sufficient yield of charge separation is achieved even when the Em of Phe/Phe- is increased by much less that the 100 meV needed to compensate for the nominally lower energy in ChlD1*.

However, thermal equilibration of the excitation energy over the entire antenna in Chl-f-PSII might not occur due to 3 of the 4 long-wavelength antenna chlorophylls absorbing at longer wavelength than ChlD1. This type of antenna energetics could result in rapid excited state equilibration in each of the three main pigment-protein complexes (CP43, CP47 and reaction centre), due to rapid energy transfer from Chl-a to Chl-f/d (with visible light excitation) followed by slower transfer from the two postulated far-red antenna pools to ChlD1, leading to a transfer-to-trap limited bottleneck. As a result, the kinetics of excitation energy transfer from the red and far-red antenna to the reaction centre could be more complex than in Chl-a-PSII and Chl-d-PSII, explaining the spread in charge separation kinetics that has been suggested based on ultrafast absorption data (Zamzam et al., 2020) and the slower excitation energy trapping kinetics measured by time-resolved fluorescence (Mascoli et al., 2020).

The driving force for charge separation is decreased in Chl-f-PSII also by the smaller energy gap between ChlD1* and PD1+Phe-, estimated to be ~80 meV in Chl-f-PSII compared to ~160 meV in Chl-a-PSII and Chl-d-PSII. This decrease in the energy gap between ChlD1* and PD1+Phe- is necessary in Chl-f-PSII to avoid the increased photosensitivity seen in Chl-d-PSII by maintaining a large energy gap between PD1+Phe- and PD1+QA- (~385 meV) (Figure 8). Nonetheless, the slower excitation energy transfer and the smaller energy gap between ChlD1* and PD1+Phe- could be partially compensated by the decreased dilution of the excitation energy on ChlD1* arising from the small number of long-wavelength antenna pigments, resulting in only a small loss of trapping efficiency (Mascoli et al., 2020) and a near-negligible effect on enzyme turnover efficiency (Figures 2—5).

This energetic balancing trick in Chl-f-PSII, which allows both reasonably high enzyme efficiency and high resilience to photodamage (by limiting recombination via the repopulation of PD1+Phe-) despite working with 100 meV less energy, comes with a very significant disadvantage: its absorption cross-section at long wavelength is ~7 times smaller than that of the Chl-a-PSII core antenna in visible light. In the case of Chl-f-PSII, evolution therefore seems to have prioritized the minimization of harmful charge recombination, by maintaining a big energy gap between Phe and QA, over light collection and photochemical quantum efficiency. This makes sense as this system has evolved as a facultative survival mechanism, that is not advantageous when visible light is available. It must be noted that in vivo the far-red antenna cross-section of Chl-f-PSII is increased by the presence of red-shifted phycobilisomes, that replace the visible light-absorbing phycobilisomes when the cells are adapted to far-red light (Gan et al., 2014).

In contrast, Chl-d-PSII seems to have maximized light collection at long wavelengths (with its full-size far-red antenna) and maximized the yield of charge separation (by maintaining the full ChlD1* to PD1+Phe- driving force). However, the energy shortfall at long wavelength is lost from the ‘energy headroom’ (mainly from the transmembrane energy gap between Phe and QA) that is proposed to minimize harmful charge recombination by buffering the effects of pulses of the trans-membrane electric field associated with fluctuations in light intensity (Davis et al., 2016; Davis et al., 2017). This seems to correspond well to the shaded and stable epiphytic niche that A. marina occupies (Nürnberg et al., 2018; Miyashita et al., 1996; Cotton et al., 2015; Davis et al., 2016; Murakami et al., 2004; Miller et al., 2005; Kühl et al., 2005; Mohr et al., 2010).

Chl-d-PSII and Chl-f-PSII have evolved different strategies to do oxygenic photosynthesis in far-red light and have been impacted differently by the decrease in energy available. Understanding how the redox tuning of the electron transfer cofactors and the layout of the far-red pigments determine the trade-off between efficiency and resilience in PSII is a necessary step to inform strategies aimed at using far-red photosynthesis for agricultural and biotechnological applications.

The present findings suggest the exchange of the full Chl-a manifold to long-wavelength chlorophylls, as seen in Chl-d-PSII (A. marina), should allow efficient oxygenic photosynthesis, but only under constant shading and stable light conditions: for example, for cultivation under LED light (vertical farming, etc). The more robust, facultative Chl-f PSII has an intrinsically low absorption cross-section in the far red; however, this could be beneficial in a shaded canopy, especially in combination with a suitably designed far-red external antenna.

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
      <td>Strain, strain background (Chroococcidiopsis)</td>
      <td>Chroococcidiopsis thermalis sp. PCC7203</td>
      <td>Pasteur Culture Collection of Cyanobacteria</td>
      <td>NCBI:txid251229</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Acaryochloris)</td>
      <td>Acaryochloris marinaMBIC 11017</td>
      <td>Marine Biotechnology Institute Culture Collection</td>
      <td>NCBI:txid155978</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Synechocystis)</td>
      <td>Synechocystis sp. PCC6803</td>
      <td>Pasteur Culture Collection of Cyanobacteria</td>
      <td>NCBI:txid1148</td>
      <td>Glucose tolerant</td>
    </tr>
    <tr>
      <td>Genetic reagent (Thermosynechococcus elongatus BP-1)</td>
      <td>ΔpsbA1, ΔpsbA2</td>
      <td>DOI:10.1016 /j.bbabio.2008.01.007</td>
      <td>WT*3</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MES (2-(N-morpholino)ethanesulfonic acid)</td>
      <td>Thermo Scientific</td>
      <td>J18886.A1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>β-DM (n-Dodecyl-β-D-maltoside)</td>
      <td>Thermo Scientific</td>
      <td>89,903</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DCMU (3-(3,4-dichlorophenyl)–1,1-dimethylurea)</td>
      <td>Sigma-Aldrich</td>
      <td>D2425</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DCBQ (2,5-Dichloro-1,4-benzoquinone)</td>
      <td>Sigma-Aldrich</td>
      <td>431,982</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>potassium ferricyanide</td>
      <td>Sigma-Aldrich</td>
      <td>244,023</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>L-Histidine</td>
      <td>BioChemica</td>
      <td>A3738</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>sodium azide (NaN3)</td>
      <td>Sigma-Aldrich</td>
      <td>S2002</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Methyl viologen dichloride hydrate</td>
      <td>Sigma-Aldrich</td>
      <td>856,177</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TMPD (N,N,N′,N′-tetramethyl-p-phenylenediamine)</td>
      <td>Sigma-Aldrich</td>
      <td>T3134</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Rose Bengal</td>
      <td>Sigma-Aldrich</td>
      <td>330,000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PPBQ (Phenyl-p-benzoquinone)</td>
      <td>Sigma-Aldrich</td>
      <td>PH005156</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>6-Aminocaproic acid</td>
      <td>Sigma-Aldrich</td>
      <td>A7824</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Benzamidine hydrochloride hydrate</td>
      <td>Alfa Aesar</td>
      <td>J62823</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cyanobacterial growth

Acaryochloris marina was grown in a modified liquid K-ESM medium containing 14 µM iron (Bailleul et al., 2008), at 30 °C under constant illumination with far-red light (750 nm, Epitex; L750-01AU) at ~30 μmol photons m–2 s–1. Chroococcidiopsis thermalis PCC7203 was grown in liquid BG11 medium (Stanier et al., 1979) at 30 °C, under two illumination conditions: white light at ~30 μmol photons m–2 s–1 (for WL C. thermalis samples) and far-red light (750 nm, Epitex; L750-01AU) at ~30 μmol photons m–2 s–1 (for FR C. thermalis samples). Synechocystis sp. PCC6803 was grown in liquid BG11 medium at 30 °C under constant illumination with white light at ~30 μmol photons m–2 s–1. The Thermosynechococcus elongatus ΔpsbA1, ΔpsbA2 deletion mutant (WT*3, Sugiura et al., 2008) was grown in liquid DNT medium at 45 °C.

### Isolation of membranes and PSII cores

Membranes were prepared as described in Appendix 7, frozen in liquid nitrogen and stored at –80 °C until use. Partially purified C. thermalis PSII cores retaining oxygen evolution activity were isolated by anion exchange chromatography using a 40 ml DEAE column. The column was equilibrated with 20 mM MES (2-(N-morpholino)ethanesulfonic acid)-NaOH pH 6.5, 5 mM CaCl2, 5 mM MgCl2 and 0.03% (w/v) β-DM (n-Dodecyl-β-D-maltoside) and elution was done using a linear gradient of MgSO4 from 0 to 200 mM in 100 min (in the same buffer conditions as those used to equilibrate the column), with a flow rate of 4 ml min–1. Fractions enriched in PSII were pooled, frozen in liquid nitrogen and stored at –80 °C. PSII-PsbA3 cores from T. elongatus WT*3 were purified as previously described (Sugiura et al., 2014).

### Fluorescence

Flash-induced chlorophyll fluorescence and its subsequent decay were measured with a fast double modulation fluorimeter (FL 3000, PSI, Czech Republic). Excitation was provided by a saturating 70 μs flash at 630 nm and the decay in QA- concentration was probed in the 100 μs to 100 s time region using non-actinic measuring pulses following a logarithmic profile as described in Vass et al., 1999. The first measuring point was discarded during the data analysis because it contains a light artefact arising from the tail of the saturating flash used for excitation. Details on the analysis of the fluorescence curves (based on Crofts and Wraight, 1983; Vass et al., 1999; Cser et al., 2008) are provided in Appendix 7. Membrane samples were adjusted to a total chlorophyll concentration of 5 μg Chl ml–1 in resuspension buffer, pre-illuminated with room light (provided by a white fluorescent lamp, ~80 μmol photons m–2 s–1) for 10 s and then kept in the dark on ice until used for measurements. Measurements were performed at 20 °C. Where indicated, 20 µM DCMU (3-(3,4-dichlorophenyl)–1,1-dimethylurea) was used.

### Thermoluminescence and luminescence

Thermoluminescence curves and luminescence decay kinetics were measured with a laboratory-built apparatus, described in De Causmaecker, 2018. Membrane samples were diluted in resuspension buffer to a final concentration of 5 µg Chl ml–1 in the case of A. marina and FR C. thermalis and of 10 µg ml–1 in the case of WL C. thermalis and Synechocystis. The samples were pre-illuminated with room light (provided by a white fluorescent lamp,~80 μmol photons m–2 s–1) for 10 s and then kept in the dark on ice for at least one hour before the measurements. When used, 20 µM DCMU was added to the samples before the pre-illumination step. Excitation was provided by single turnover saturating laser flashes (Continuum Minilite II, frequency doubled to 532 nm, 5 ns FWHM). Details on the measurement conditions and on the analysis of the luminescence decay kinetics are provided in Appendix 7.

### Oxygen evolution and consumption rates

Oxygen evolution and consumption rates were measured with a Clark-type electrode (Oxygraph, Hansatech) at 25 °C. Membrane samples were adjusted to a total chlorophyll concentration of 5 μg Chl ml–1. Illumination was provided by a white xenon lamp filtered with a heat filter plus red filter, emitting 600–700 nm light at 7100 µmol photons m–2 s–1 (Quantitherm light meter, Hansatech). When required, the light intensity was reduced by using neutral density filters (Thorlabs). For PSII maximal oxygen evolution rates, 1 mM DCBQ (2,5-Dichloro-1,4-benzoquinone) and 2 mM potassium ferricyanide were used as an electron acceptor system. Photoinhibitory illumination was performed at room temperature for 30 min with a laboratory-built red LED (660 nm, 2600 µmol photons m-2 s–1). For histidine-mediated chemical trapping of singlet oxygen, 20 µM DCMU, 5 mM L-Histidine and, where specified, 10 mM sodium azide (NaN3) were used. PSI activity was measured as the rate of oxygen consumption in presence of 20 µM DCMU and 100 µM methyl viologen using 5 mM sodium ascorbate and 50 µM TMPD (N,N,N′,N′-tetramethyl-p-phenylenediamine) as electron donors. The dye Rose Bengal was used at a final concentration of 0.1 µM. After all necessary additions, samples were left to equilibrate with air in the measuring chamber for 1 minute, under stirring, to start with similar dissolved O2 concentrations in all measurements. For each measurement, a dark baseline was recorded for 1 min before starting the illumination.

### Flash-dependent oxygen evolution with Joliot electrode

Time-resolved oxygen polarography was performed using a custom-made centrifugable static ring-disk electrode assembly of a bare platinum working electrode and silver-ring counter electrode, as previously described (Dilbeck et al., 2012). For each measurement, membranes equivalent to 10 µg of total chlorophyll were used. Three different light sources were used to induce the S-state transitions: a red LED (613 nm), a far-red LED (730 nm) and a Xenon flashlamp. Details on the experimental setup and on the lights used are provided in Appendix 7. Measurements were performed at 20 °C. For each measurement, a train of 40 flashes fired at 900ms time interval was given and the flash-induced oxygen-evolution patterns were taken from the maximal O2 signal of each flash and fitted with an extended Kok model with flash-independent miss factor, as described in Nöring et al., 2008.

### UV transient absorption

UV pump-probe absorption measurements were performed using a lab-built Optical Parametric Oscillator (OPO)-based spectrophotometer (Joliot et al., 1998) with a time resolution of 10 ns and a spectral resolution of 2 nm (see Appendix 7 for details on the setup). ΔI/I stands for differential absorption, a method that measures the changes in absorption depending on whether or not a sample is subjected to actinic light. Samples were diluted in resuspension buffer to a final concentration of 25 µg Chl ml–1 for isolated C. thermalis and T. elongatus PSII cores and 40 µg Chl ml–1 for A. marina membranes. Samples were pre-illuminated with room light (provided by a white fluorescent lamp,~80 μmol photons m–2 s–1) for 10 s and then kept in the dark on ice for at least one hour before the measurements. 100 µM PPBQ (Phenyl-p-benzoquinone) was added just before the measurements. The sample was refreshed between each train of flashes. For each measurement, a train of 20 flashes (6 ns FWHM) fired at 300ms time interval was given, and absorption changes measured at 100ms after each flash. The data were fitted according to Lavergne, 1991; Lavorel, 1976.
