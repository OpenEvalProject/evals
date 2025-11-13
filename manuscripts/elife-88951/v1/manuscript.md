# Carotenoid assembly regulates quinone diffusion and the Roseiflexus castenholzii reaction center-light harvesting complex architecture

## Authors

- Jiyu Xin<sup>1</sup> ([ORCID: 0000-0003-2354-2032](https://orcid.org/0000-0003-2354-2032))
- Yang Shi<sup>2</sup>
- Xin Zhang<sup>1</sup> ([ORCID: 0000-0002-6734-759X](https://orcid.org/0000-0002-6734-759X))
- Xinyi Yuan<sup>1</sup>
- Yueyong Xin<sup>3</sup>
- Huimin He<sup>3</sup>
- Jiejie Shen<sup>1</sup>
- Robert E Blankenship<sup>4</sup>
- Xiaoling Xu<sup>1</sup> ([ORCID: 0000-0001-8995-1213](https://orcid.org/0000-0001-8995-1213)) †

### Affiliations

1. Department of Biochemistry and Molecular Biology, School of Basic Medical Sciences and The Affiliated Hospital of Hangzhou Normal University Hangzhou China ([ROR:014v1mr15](https://ror.org/014v1mr15))
2. Liangzhu Laboratory, MOE Frontier Science Center for Brain Science and Brain-machine Integration, State Key Laboratory of Brain-machine Intelligence & Department of Neurobiology and Department of Pathology of the First Affiliated Hospital, Zhejiang University School of Medicine, Zhejiang University Hangzhou China ([ROR:00a2xv884](https://ror.org/00a2xv884))
3. Photosynthesis Research Center, College of Life and Environmental Sciences, Hangzhou Normal University Hangzhou China ([ROR:014v1mr15](https://ror.org/014v1mr15))
4. Departments of Biology and Chemistry, Washington University in St. Louis St. Louis United States ([ROR:01yc7t268](https://ror.org/01yc7t268))

† Corresponding author

## Abstract

Carotenoid (Car) pigments perform central roles in photosynthesis-related light harvesting (LH), photoprotection, and assembly of functional pigment-protein complexes. However, the relationships between Car depletion in the LH, assembly of the prokaryotic reaction center (RC)-LH complex, and quinone exchange are not fully understood. Here, we analyzed native RC-LH (nRC-LH) and Car-depleted RC-LH (dRC-LH) complexes in Roseiflexus castenholzii, a chlorosome-less filamentous anoxygenic phototroph that forms the deepest branch of photosynthetic bacteria. Newly identified exterior Cars functioned with the bacteriochlorophyll B800 to block the proposed quinone channel between LHαβ subunits in the nRC-LH, forming a sealed LH ring that was disrupted by transmembrane helices from cytochrome c and subunit X to allow quinone shuttling. dRC-LH lacked subunit X, leading to an exposed LH ring with a larger opening, which together accelerated the quinone exchange rate. We also assigned amino acid sequences of subunit X and two hypothetical proteins Y and Z that functioned in forming the quinone channel and stabilizing the RC-LH interactions. This study reveals the structural basis by which Cars assembly regulates the architecture and quinone exchange of bacterial RC-LH complexes. These findings mark an important step forward in understanding the evolution and diversity of prokaryotic photosynthetic apparatus.

## Introduction

Carotenoids (Cars) are natural pigments that play important roles in light harvesting (LH), photoprotection, and assembly of the functional pigment-protein complexes required for photosynthesis. Specifically, Cars capture blue-green light (450–550 nm) and transfer it to chlorophyll or bacteriochlorophyll ((B)Chl) in the LH antenna. The excited energy is then transferred to the RC for primary photochemical reactions. In anoxygenic photosynthetic bacteria (PSB), Car-BChl interactions are essential for assembling the functional LH complexes (Davidson and Cogdell, 1981; Hashimoto et al., 2016; Lang and Hunter, 1994; Walz and Ghosh, 1997). The well-studied purple bacterium Rhodobacter (Rba.) sphaeroides contains a closed LH2 ring comprising nine αβ-polypeptides; each LHαβ non-covalently binds three BChls (two B850s and one B800) and one Car (Qian et al., 2021b). The Car-less strains of Rba. sphaeroides are unable to assemble an LH2 complex, indicating that Car-BChl interactions are essential for the maintenance of LH2 structural stability (Lang et al., 1995). In the LH1 ring of Rba. sphaeroides, a combination of two Car groups forms a tightly sealed, impenetrable fence-like structure that blocks the proposed quinone channel of the closed ring (Olsen et al., 2017; Qian et al., 2021c). However, there are fewer Cars in most LH1 structures, so in Thermochromatium (Tch.) tepidum and Rhodospirillum (Rsp.) rubrum for example, there are small gaps that allow quinones to shuttle cross the ring (Niwa et al., 2014; Qian et al., 2021a; Yu et al., 2018b). A point mutation in LHα (W24F) dramatically reduces the amounts of LH1-bound Car. However, in the pufX knockout strain of Rba. sphaeroides, which possesses a closed LH1 ring composed of 17 LHαβs, the same mutation promotes photosynthetic growth (Cao et al., 2022; McGlynn et al., 1994; Olsen et al., 2017). These observations indicate a correlation between the number of LH1-bound Cars and the architecture and photochemical functions of the RC-LH1. This phenomenon could be further studied using structural information about Car-depleted RC-LH (dRC-LH), but no such data have yet been reported.

Roseiflexus (R.) castenholzii is a chlorosome-less filamentous anoxygenic photosynthetic bacterium (Hanada et al., 2002). It contains only one LH, which forms an unusual RC-LH complex. This complex structurally resembles RC-LH1 but has similar spectroscopic characteristics that are similar to the peripheral LH2 of purple bacteria (Collins et al., 2010; Collins et al., 2009). We previously reported the cryo-electron microscopy (EM) structure of R. castenholzii RC-LH at 4.1 Å resolution. It revealed an RC composed of L, M, and cytochrome (cyt) c subunits surrounded by an opened elliptical LH ring of 15 LHαβs, with the tetraheme binding domain of cyt c protruding on the periplasmic side. The RC is compositionally larger in purple bacteria than in R. castenholzii, in which it does not contain an H subunit (Pugh et al., 1998; Qian et al., 2005; Yamada et al., 2005). However, it does contain a unique cyt c transmembrane (c-TM) helix and the newly identified subunit X, both of which flank the gap of the LH ring to form a novel quinone shuttling channel (Xin et al., 2018). Notably, the amino acid sequences of subunit X and TM7, a TM helix separated from the RC-L and RC-M subunits are unassigned. Pigment analyses have revealed a 2:3 Car:BChl molar ratio of R. castenholzii RC-LH (Collins et al., 2009). However, the cryo-EM structure resolved only one keto-γ-carotene (KγC) molecule spanning the interface of each LHαβ, coordinating two B880s and one additional B800 at the periplasmic and the cytoplasmic side, respectively. The lack of a clear cryo-EM density map leaves uncertainty about the presence of additional LH ring-bound Cars, the roles of which are unknown in maintaining the architecture and photochemical functions of the R. castenholzii RC-LH.

We here determined cryo-EM structures of native RC-LH (nRC-LH) complexes purified from R. castenholzii cells grown under high (180 μmol m–2 s–1), medium (32 μmol m–2 s–1), and low (2 μmol m–2 s–1) illuminations at 2.8 Å, 3.1 Å, and 2.9 Å resolutions, respectively. All three structures shared the same architecture, indicating that the Car composition and assembly are not affected by light intensities. From these high-resolution structures, we identified 14 additional KγC molecules in the exterior of the LH ring (KγCext). In combination with the B800 on the cytoplasmic side, the newly identified KγCext molecules blocked the proposed quinone channel between LHαβ subunits, forming a sealed LH ring conformation. We also assigned the full amino acid sequences of subunit X, TM7, and an additional TM helix that were derived from hypothetical proteins Y and Z, respectively, and demonstrated their roles in forming the quinone channel and stabilizing the RC-LH interactions. To investigate the role of Cars in the assembly of RC-LH, R. castenholzii cells were treated with Car biosynthesis inhibitor diphenylamine (DPA) to produce a dRC-LH; a 3.1 Å resolution cryo-EM structure of this complex resolved five KγC molecules bound in the interior of the LH ring (KγCint). The absence of subunit X and exterior KγC (KγCext) molecules in the dRC-LH produced an LH ring with exposed LHαβ interface and a larger opening than that of nRC-LH. This conformation accelerated the in vitro quinone/quinol exchange rate of menaquinone-4, an analog of the native menaquinone-11, but did not affect the Car-to-BChl energy transfer efficiency of dRC-LH. This study thus revealed a previously unrecognized structural basis by which Car assembly regulates the architecture and quinone/quinol exchange rate of the bacterial RC-LH complex. These findings further our understanding of diversity and molecular evolution in the prokaryotic photosynthetic apparatus.

## Results

### Identification of KγCext in the nRC-LH complex

To investigate the LH-bound Car numbers and its correlation with the light intensities, we anaerobically cultured R. castenholzii cells under the light intensity (32 μmol m–2 s–1) used for obtaining the reported 4.1 Å RC-LH structure (Xin et al., 2018), and also a high and a low light intensity at 180 μmol m–2 s–1 and 2 μmol m–2 s–1, respectively. For easier reading, we labeled these three light intensities as high (180 μmol m–2 s–1), medium (32 μmol m–2 s–1), and low (2 μmol m–2 s–1) illuminations. The cell proliferation rate was much faster under high illumination than that grown under medium and low illuminations, and the cells grown showed a darker reddish-brown color after 120 hr of culturing (Figure 1—figure supplement 1A and B). We then isolated and purified nRC-LH complexes from these cells at the stationary growth phase (Figure 1—figure supplement 1C, Table 1). Ultraviolet (UV)-visible-near infrared (NIR) spectrophotometry of the isolated nRC-LH complexes showed typical Qy bands at 800 nm (B800) and 880 nm (B880) and a Qx band at 594 nm, which corresponded to LH-bound BChls. Notably, Car-associated absorption peaks were detected at 457 nm, 482 nm, and 519 nm (Figure 1—figure supplement 1D). The nRC-LH complexes purified from cells under high, medium, and low illuminations showed the same Car absorption spectrum (Figure 1—figure supplement 1E), indicating the pigments content was not affected by light intensities. These nRC-LH complexes were then imaged via cryo-EM, respectively (Figure 1—figure supplements 2 and 3). Using single particle analysis, the nRC-LH structures obtained from the high, medium, and low illumination cultured cells were resolved at an overall resolution of 2.8 Å, 3.1 Å, and 2.9 Å, respectively (Figure 1—figure supplements 2 and 4, Table 2). Superposition of the high illumination model with that of medium and low illumination gave root mean square deviation of 1.753 Å and 1.765 Å, respectively, indicating these three structures share the same architecture, and light intensities did not affect the conformation of the nRC-LH structures.

**Table 1.**
 Peptide mass fingerprinting (PMF) analysis of the R. castenholzii in reaction center-light harvesting (RC-LH) that are separated by blue-native PAGE.


<table>
  <thead>
    <tr>
      <th>Subunit</th>
      <th>Accession</th>
      <th>Description</th>
      <th>Score</th>
      <th>Coverage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cyt c</td>
      <td>BAC76415.1</td>
      <td>Cytochrome subunit of photosynthetic reaction center(R. castenholzii)</td>
      <td>131.79</td>
      <td>40.94%</td>
    </tr>
    <tr>
      <td>L and M</td>
      <td>BAC76414.1</td>
      <td>Precursor for L and M subunits of photosynthetic reaction center(R. castenholzii)</td>
      <td>195.79</td>
      <td>28.39%</td>
    </tr>
    <tr>
      <td>LHα subunit</td>
      <td>BAC76413.1</td>
      <td>Alpha subunit of light harvesting 1(R. castenholzii)</td>
      <td>97.78</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>LHβ subunit</td>
      <td>BAC76412.1</td>
      <td>Beta subunit of light harvesting 1(R. castenholzii)</td>
      <td>49.11</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Z subunit</td>
      <td>WP_041331144.1</td>
      <td>Hypothetical protein(R. castenholzii)</td>
      <td></td>
      <td>19.05%</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Cryo-electron microscopy (cryo-EM) data collection, refinement, and validation statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Native RC-LH at 180 μmol m–2 s–1(nRC-LH)(EMD-34838)(PDB 8HJU)</th>
      <th>Carotenoid-depleted RC-LH at 180 μmol m–2 s–1(dRC-LH)(EMD-34839)(PDB 8HJV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection and processing</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Magnification</td>
      <td>64,000</td>
      <td>81,000</td>
    </tr>
    <tr>
      <td>Voltage (kV)</td>
      <td>300</td>
      <td>300</td>
    </tr>
    <tr>
      <td>Electron exposure (e–/Å2)</td>
      <td>50</td>
      <td>49.65</td>
    </tr>
    <tr>
      <td>Defocus range (μm)</td>
      <td>–1.0 to –2.3</td>
      <td>–1.1 to –1.7</td>
    </tr>
    <tr>
      <td>Pixel size (Å)</td>
      <td>1.08</td>
      <td>0.893</td>
    </tr>
    <tr>
      <td>Symmetry imposed</td>
      <td>C1</td>
      <td>C1</td>
    </tr>
    <tr>
      <td>Initial particle images (no.)</td>
      <td>1,625,156</td>
      <td>1,081,719</td>
    </tr>
    <tr>
      <td>Final particle images (no.)</td>
      <td>372,029</td>
      <td>84,352</td>
    </tr>
    <tr>
      <td>Map resolution (Å)FSC threshold</td>
      <td>2.80.143</td>
      <td>3.10.143</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Initial model used (PDB code)</td>
      <td>5YQ7</td>
      <td>Native RC-LH</td>
    </tr>
    <tr>
      <td>Model resolution (Å)FSC threshold</td>
      <td>2.80.5</td>
      <td>3.10.5</td>
    </tr>
    <tr>
      <td>Map sharpening B factor (Å2)</td>
      <td>98</td>
      <td>120</td>
    </tr>
    <tr>
      <td>Model compositionNon-hydrogen atomsProtein residuesLigands</td>
      <td>23,917233097</td>
      <td>22,193226567</td>
    </tr>
    <tr>
      <td>B factors (Å2)ProteinLigand</td>
      <td>35.8132.21</td>
      <td>52.4655.37</td>
    </tr>
    <tr>
      <td>R.m.s. deviationsBond lengths (Å)Bond angles (°)</td>
      <td>0.0111.509</td>
      <td>0.0101.205</td>
    </tr>
    <tr>
      <td>ValidationMolProbity scoreClashscorePoor rotamers (%)</td>
      <td>2.0016.110.71</td>
      <td>2.1718.870.84</td>
    </tr>
    <tr>
      <td>Ramachandran plotFavored (%)Allowed (%)Disallowed (%)</td>
      <td>95.834.170.00</td>
      <td>94.165.750.09</td>
    </tr>
    <tr>
      <td></td>
      <td>Native RC-LH at 2 μmol m–2 s–1(EMD-35988)(PDB 8J5O)</td>
      <td>Native RC-LH at 32 μmol m–2 s–1(EMD-35989)(PDB 8J5P)</td>
    </tr>
    <tr>
      <td>Data collection and processing</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Magnification</td>
      <td>81,000</td>
      <td>81,000</td>
    </tr>
    <tr>
      <td>Voltage (kV)</td>
      <td>300</td>
      <td>300</td>
    </tr>
    <tr>
      <td>Electron exposure (e–/Å2)</td>
      <td>50</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Defocus range (μm)</td>
      <td>–1.2 to –2.0</td>
      <td>–1.2 to –2.0</td>
    </tr>
    <tr>
      <td>Pixel size (Å)</td>
      <td>0.893</td>
      <td>0.893</td>
    </tr>
    <tr>
      <td>Symmetry imposed</td>
      <td>C1</td>
      <td>C1</td>
    </tr>
    <tr>
      <td>Initial particle images (no.)</td>
      <td>779,594</td>
      <td>686,082</td>
    </tr>
    <tr>
      <td>Final particle images (no.)</td>
      <td>322,595</td>
      <td>272,617</td>
    </tr>
    <tr>
      <td>Map resolution (Å)FSC threshold</td>
      <td>2.90.143</td>
      <td>3.10.143</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Initial model used (PDB code)</td>
      <td>8HJU</td>
      <td>8HJU</td>
    </tr>
    <tr>
      <td>Model resolution (Å)FSC threshold</td>
      <td>2.80.5</td>
      <td>3.10.5</td>
    </tr>
    <tr>
      <td>Map sharpening B factor (Å2)</td>
      <td>98</td>
      <td>120</td>
    </tr>
    <tr>
      <td>Model compositionNon-hydrogen atomsProtein residuesLigands</td>
      <td>23,691231893</td>
      <td>23,737233192</td>
    </tr>
    <tr>
      <td>B factors (Å2)ProteinLigand</td>
      <td>27.5424.73</td>
      <td>39.0137.37</td>
    </tr>
    <tr>
      <td>R.m.s. deviationsBond lengths (Å)Bond angles (°)</td>
      <td>0.0181.915</td>
      <td>0.0171.850</td>
    </tr>
    <tr>
      <td>ValidationMolProbity scoreClashscorePoor rotamers (%)</td>
      <td>1.9718.790.00</td>
      <td>1.9817.690.30</td>
    </tr>
    <tr>
      <td>Ramachandran plotFavored (%)Allowed (%)Disallowed (%)</td>
      <td>96.793.210.00</td>
      <td>96.503.460.04</td>
    </tr>
  </tbody>
</table>

The 15 LHαβ heterodimers formed an opened elliptical ring surrounding the RC, which contained L, M, and cyt c subunits; the long and short axes were 112 Å and 103 Å, respectively, and a tetraheme binding domain of cyt c protruded into the periplasmic space (Figure 1A and B). Similar as most purple bacteria, the RC contained a photo-reactive special pair of BChls, one accessory BChl, three bacteriopheophytins (BPheos), two MQ-11 (MQA and MQB) and a newly identified MQc, and an iron atom to mediate the charge separation and subsequent electron transfer (Figure 1C). Each LHαβ non-covalently bound two B880s and one B800 BChl on the periplasmic and cytoplasmic sides (Figures 1C and 2A). In particular, the LH ring bound 15 KγCint, 14 KγCext Cars, and an additional KγC that inserted between the LHαβ1 and c-TM in all three structures (Figure 1B–D, Figure 1—figure supplement 5, Video 1), indicating both Car compositions and assembly in the nRC-LH were not affected by light intensities. The low-pass filtered cryo-EM map of nRC-LH minus that of the reported 4.1 Å model showed apparent density differences for the KγCext (Figure 1—figure supplement 6), indicating the KγCext molecules were not resolved due to lack of clear EM densities in the 4.1 Å model. Given the similarities between these three nRC-LH structures, we use the 2.8 Å model for following analyses of the nRC-LH structure.

![Figure 1.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig1-v1.jpg)

**Figure 1.:** (A) A cryo-electron microscopy (cryo-EM) map of the native RC-LH (nRC-LH) complex is shown from the side (left panel) and the bottom (right panel). The dimensions of the RC-LH complex and LH ring are represented. The positions of subunit X, proteins Y and Z, and the cytochrome (cyt) c transmembrane (c-TM) domain are labeled. (B) Side and top views of the nRC-LH complex are presented in cartoon form. LH subunits are numbered clockwise from the gap formed by subunit X and c-TM. Heme-c (red) and keto-γ-carotene (KγC) molecules (orange, cyan, ruby) are shown in stick forms; Mg atoms of the bacteriochlorophylls B800 (pink) and B880 (purple) are shown as spheres. (C) The cofactors bound in the nRC-LH complex. All cofactors are shown in stick forms except for the interior KγC (KγCint) in LH, the iron bound in the RC are shown as spheres. (D) The structural models of the KγCint, exterior KγC (KγCext), and KγC in the nRC-LH complex are fitted in the EM density map. The color scheme: lime green, α-polypetides; marine, β-polypetides; yellow-orange, cyt c; wheat, L subunit; salmon, M subunit; pale cyan, protein Y; hot pink, subunit X; light magenta, protein Z; cyan, KγCint; orange, KγCext; ruby, KγC; purple, B880; pink, B800; tv-red, heme-c; chartreuse, bacteriopheophytins (BPheos); blue, menaquinone-11 (MQ); brown, iron.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Appearance of the native R. castenholzii (left) and the fifth subculture of diphenylamine (DPA)-treated (right) cells, which were cultured anaerobically under high (180 μmol m–2 s–1), medium (32 μmol m–2 s–1), and low (2 μmol m–2 s–1) illuminations (ILLs), respectively. (B) Growth curves of the native R. castenholzii and the fifth subculture of DPA-treated cells grown under high, medium, and low illuminations. Data are shown as the mean ± standard deviations (n=3). (C) Representative gel filtration chromatography, blue native PAGE, and SDS-PAGE of the nRC-LH complex from R. castenholzii cultured under high illumination. The chromatography diagram of absorption at 280 nm (red) and 800 nm (green) of nRC-LH is shown. The subunits L, M, and cytochrome (cyt) c subunits of RC and the αβ apoproteins of the LH are labeled. (D) Absorption spectrum analyses of RC-LH complexes purified from R. castenholzii grown under high illumination. Black corresponds to untreated cells; brown, gray, orange, blue, and green correspond to Car-depleted cells from five consecutive subcultures of DPA-treated cells, respectively. The characteristic Qy bands of B800 and B880, the Qx and Soret bands of bacteriochlorophylls (BChls), and the absorption peaks of Cars are labeled. (E) Absorption spectrum analyses of RC-LH complexes purified from R. castenholzii cells with or without DPA treatment under high, medium, and low illuminations. (F) Representative gel filtration chromatography, blue native PAGE, and SDS-PAGE of the dRC-LH complex purified from R. castenholzii cultured under high illumination.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) A representative raw cryo-EM micrograph of the nRC-LH complex purified from the cells grown under high illumination (180 μmol m–2 s–1). (B) Representative reference-free 2D class averages of the nRC-LH complex. (C) Local resolution of the cryo-EM map estimated by ResMap. (D) The different views of angular distribution of the nRC-LH complex particles in final reconstruction. The direction and length of each cylinder represent the direction and amount of particles. (E) The gold-standard Fourier shell correlation (FSC) curve of the cryo-EM map (corrected map, black; unmasked, green; masked, blue; phase randomized, red) and the FSC curve between the map and the final refined model (orange). (F) Cryo-EM data processing workflow for the nRC-LH complex. All structural figures here are generated with ChimeraX.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A, B) Cryo-EM data processing workflow for the native RC-LH purified from R. castenholzii grown under medium (A) and low (B) illuminations. The local resolution of the cryo-EM map and the angular distribution of particles in final reconstruction are shown in upper right panel. The gold-standard Fourier shell correlation (FSC) curve of the cryo-EM map and the FSC curve between the map and the final refined model are shown in lower right panel.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** (A) EM density maps of representative α-helices in the native RC-LH (nRC-LH) complex are shown in mesh forms. The corresponding atomic models are shown in stick forms. (B) The cofactors in the native RC were docked into the EM density map. (C) A density map of the keto-γ-carotenes (KγC) (interior KγC [KγCint]) bound in LH ring interior of the carotenoid-depleted RC-LH (dRC-LH) complex. The corresponding atomic models are colored in limon. (D) EM map densities fitted with resolved lipids for the nRC-LH.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** (A, B) The structural models of the interior keto-γ-carotenes (KγCint), exterior keto-γ-carotenes (KγCext), and a KγC at the LH ring opening in the nRC-LH complexes obtained at low (A) and medium (B) illuminations were fitted in the electron microscopy (EM) density map. (C, D) The structural models of proteins in the nRC-LH complexes obtained at low (C) and medium (D) illuminations. The corresponding EM densities of subunit X and cyt c transmembrane (c-TM) are shown in surface forms.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig1-figsupp6-v1.jpg)

**Figure 1—figure supplement 6.:** (A) Superposition of cryo-EM maps of the reported 4.1 Å RC-LH model and the low-pass filtered nRC-LH map that was obtained at the same medium illumination. The cryo-EM map of nRC-LH complex (blue) was low-pass filtered to the same 4.1 Å resolution as the reported RC-LH (gary). The cryo-EM densities for the exterior keto-γ-carotenes (KγCext) were highlighted in orange. (B) The global density differences between the reported 4.1 Å RC-LH model and the nRC-LH complex obtained at medium illumination. The difference map of KγCext is shown in orange. (C) Superposition of cryo-EM maps of the nRC-LH (surface) and dRC-LH (mesh) complexes obtained at high illumination. The cryo-EM densities of subunit X and KγCext were highlighted in hot pink and orange, respectively. All structural figures here are generated with ChimeraX.

![Video 1.](https://cdn.elifesciences.org/articles/88951/elife-88951-video1.mp4.jpg)

**Video 1.:** The color scheme is same as Figures 1 and 4.

### Incorporation of KγCext and B800s together blocked the LHαβ interface

Each LHαβ heterodimer of R. castenholzii was stabilized by hydrogen bonding interactions between LHβ-Arg55 and LHα-Asn37 on the periplasmic side, and by LHβ-Gln22 and LHα-Arg4 on the cytoplasmic side (Figure 2—figure supplement 1A). These interactions were not resolved in the 4.1 Å model, due to lack of clear cryo-EM densities for the Arg4 and Arg55 residues. The LH-bound B880s and one B800 BChl were coordinated by highly conserved His residues on the periplasmic and cytoplasmic sides (Figure 2A, Figure 2—figure supplement 1). Incorporation of an additional B800 at the cytoplasmic side of the LH ring resembles the exterior LHh ring of Gemmatimonas (G.) phototrophica RC-dLH, in which the B800s were oriented perpendicular to the plane of the membrane (Qian et al., 2022). Superposition of each LHαβ with that of G. phototrophica LHh revealed high overlap at the TM helices, with the exception that the B800 porphyrin ring was inclined nearly 60° relative to the G. phototrophica LHh-bound B800 (Figure 2B). Notably, the B800 conformation was also different from that of B800s bound in Rba. sphaeroides LH2 and R. acidophila LH3, in which the porphyrin rings were both oriented toward the center of the LH ring (Figure 2—figure supplement 1C). Compared to Tch. tepidum RC-LH1 that contains a closed LH1 ring, the B800s occupied the space of an N-terminal helix of LH1-α and the head of an ubiquinone (UQ) bound in the LHαβ interface (Figure 2C). Thus, incorporation of the B800s in nRC-LH occupied the LHαβ interface on the cytoplasmic side.

![Figure 2.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig2-v1.jpg)

**Figure 2.:** (A) Interactions between the LHαβ heterodimer and the bound BChls. Close-up views of amino acid residues that coordinate the LH-bound B880s (left) and B800 (right) are shown on the periplasmic (P) and the cytoplasmic (C) side. The BChls and interacting amino acid residues are shown in stick forms. (B, C) Superposition of LHαβ heterodimer from nRC-LH (colored) with Gemmatimonas (G.) phototrophica LHh (B, gray) and Tch. tepidum LH1 (C, gray). The LH-bound B800 and exterior KγC (KγCext) in nRC-LH are shown as pink and orange sticks, respectively. Mg atoms of LH-bound B880 are shown in spheres. The LHh-bound B800 in G. phototrophica is shown in gray sticks, and Tch. tepidum LH1-bound ubiquinone (UQ) is shown in blue sticks. (D, E) KγC organization. Interior KγC (KγCint) are shown in cyan, KγCext are shown in orange, and the KγC inserted between cytochrome c transmembrane (c-TM) and LHαβ is shown in ruby. (F) Incorporation of the KγCext and B800s at the cytoplasmic side blocked the LHαβ interface. (G, I) Interactions between the assigned subunit X (hot pink), c-TM (yellow-orange), and neighboring LHαβ1 and LHαβ15 in the nRC-LH. The N-terminus (N-ter) and C-terminus (C-ter) of subunit X, c-TM and LHβ15 are indicated. The hydrogen bonding and hydrophobic interactions between the amino acid residues are labeled and indicated with dashed lines. The BChls B880 and B800 are shown as purple and pink sticks, respectively. (H) The assigned subunit X (hot pink) are fitted in the EM density map. Location of the coding sequence (CDS) in R. castenholzii genomic DNA, and the amino acid sequence of subunit X are indicated, with the modeled amino acid residues colored in black.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) The left panel shows the interactions between LHα and LHβ polypeptides. Close-up views of interactions between the C-terminus (top) and N-terminus (bottom) of LHα and LHβ are shown on the right. Interacting amino acid residues are shown in stick forms. (B) Structure-based sequence alignment of the LHα and LHβ subunits from R. castenholzii and the representative purple bacteria. Tch. tepidum (PDB ID: 5Y5S), G. phototrophica (PDB ID: 7O0U), Rhodopila (Rpi.) globiformis (PDB ID: 7XXF), and Rba. sphaeroides (PDB ID: 7F0L). (C) Structural comparison of LHαβ heterodimers from R. castenholzii nRC-LH with Rba. sphaeroides LH2 (left, PDB ID: 7PBW) and Rhodopseudomonas (R.) acidophila LH3 (right, PDB ID: 1IJD) that both bind B800s. The LH-bound B800 and exterior keto-γ-carotenes (KγCext) in nRC-LH are shown as pink and orange sticks, respectively. The B800 bound in Rba. sphaeroides LH2 (violet-purple) and R. acidophila LH3 (salmon) are also shown in stick forms. Mg atoms of LH-bound B880 are shown in spheres. The periplasmic (P) and cytoplasmic (C) sides are labeled.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) B-factors distribution of the keto-γ-carotenes in nRC-LH. B-factor values are indicated by color. Protein subunits of the nRC-LH are shown in gray. (B) B-factors distribution of protein subunits in the nRC-LH complex. (C) B-factor distribution of protein subunits in the dRC-LH complex. B-factor values are indicated by color. The subunit X, cytochrome (cyt) c transmembrane (c-TM) of cyt c subunit, LHβ1 and LHβ15 with higher B-factor are indicated.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A, B) HPLC analysis of the extracted pigments of native RC-LH (nRC-LH) (A) and carotenoid-depleted RC-LH (dRC-LH) (B) that were isolated from the fifth sub-culture of diphenylamine (DPA)-treated R. castenholzii cells. The pigments were detected by their absorbance at 462 nm (black line) and 772 nm (red line), based on the characteristic absorption spectrum and LC-MS. The first peak at retention time of 5.58 min was identified to be the bacteriochlorophyll (BChl) a , which was characterized with absorption peaks at 364 nm, 605 nm, and 770 nm. The following peaks 1–5 were all characterized to be γ-carotene and its derivatives. (C, D) MS analysis of the HPLC peak 1 (C) and peaks 2–5 (D) using atmospheric pressure chemical ionization (APCI) method. The calculated and found molecular weights of γ-carotene, 4-keto-γ-carotene, OH-γ-carotene glucoside, and 4-keto-OH-γ-carotene glucoside were ~536 Da, ~550 Da, ~717 Da, and ~731 Da, respectively. Both the measured m/z values and the chemical formula of γ-carotene and its derivatives were indicated. All the experiments were repeated three times.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** (A, B) Overall structural comparison of R. castenholzii nRC-LH (colored) with Rba. sphaeroides RC-LH1 (white, PDB ID: 7F0L) and Tch. tepidum RC-LH1 (white, PDB ID: 5Y5S). (C, D) Superposition of LHαβ heterodimers from R. castenholzii nRC-LH with Rba. sphaeroides RC-LH1 (C) and Tch. tepidum RC-LH1 (D). R. castenholzii nRC-LH is shown in cartoon form, except for the Mg atoms of LH-bound BChls (B800/B880) are shown in spheres. Interior keto-γ-carotenes (KγCint) and exterior keto-γ-carotenes (KγCext) in the nRC-LH are shown as cyan and orange sticks, respectively. The carotenoids in Rba. sphaeroides and Tch. tepidum RC-LH1 are shown as white sticks. The ubiquinone (UQ) bound in Tch. tepidum LHαβ is colored blue. (E) Superposition of R. castenholzii nRC-LH with Rba. sphaeroides RC-LH1 at the LHαβ15 heterodimer to show the spatial organizations of subunit X, cytochrome c transmembrane (c-TM), and Y with that of PufX and PufY (or protein-U). The right panel shows top view of the superposed region near PufY. Arrow shows the distance (~17 Å) between the N-terminus of the transmembrane helices of c-TM and PufY. The model of R. castenholzii nRC-LH is colored same as Figure 1. The model of Rba. sphaeroides RC-LH1 is colored in white, with PufX colored in arsenic and PufY colored in light pink.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig2-figsupp5-v1.jpg)

**Figure 2—figure supplement 5.:** (A) Amino acid sequences of the KatS3mg058_1126 and KatS3mg058_1154 proteins, and the coding sequence of KatS3mg058_1154 in Roseiflexus sp. genome. (B) Amino acid sequences of subunit X and protein Y, and the coding sequence of protein Y in the genome of R. castenholzii DSM 13941/HLO8 strain. The non-conserved amino acid residues in protein Y and KatS3mg058_1154 are colored in blue and underlined. (C) The structural model of protein Y in the native reaction center-light harvesting (RC-LH) were docked into the electron microscopy (EM) density map. Arrows indicate the non-conserved amino acid residues of protein Y compared with Roseiflexus sp. KatS3mg058_1154.

Notably, KγC in the LH ring of nRC-LH were located at two distinct positions (Figures 1D and 2D). 15 KγCint molecules obliquely spanned the LHαβ subunits, with the 4-oxo-β-ionone rings sandwiched between adjacent LHαβs and the ψ-end groups directed into the LH center. In addition, another 14 KγC were detected in a second position in the LH ring exterior (KγCext), which were almost parallel to the adjacent LHβ subunits; the 4-oxo-β-ionone rings were directed toward the cytoplasmic side and the ψ-end groups stretched into the periplasm (Figure 2D). Alternatively, a newly identified KγC was sandwiched between LHαβ1 and c-TM, with its 4-oxo-β-ionone ring directing toward the RC-Y subunit (Figure 2E). The B-factor was higher for KγCext than for KγCint molecules, with the latter having lower conformational flexibility (Figure 2—figure supplement 2A). Identification of these Cars yielded in a Car:BChl ratio of approximately 1:1.6 for the nRC-LH structure; this was consistent with results from previous pigment studies (Collins et al., 2009). High-performance liquid chromatography (HPLC)-mass spectrometry (MS) analyses of the pigments in nRC-LH revealed a typical BChl peak at the retention time of 5.58 min, and several peaks of γ-carotene and its derivatives (Figure 2—figure supplement 3). In respect to the complicated Car compositions and lack of specific absorption coefficients of the derivatives, it is impracticable to quantify the Car:BChl ratio from nRC-LH solution.

The nRC-LH thus resembled Rba. sphaeroides RC-LH1, which also binds two groups of Cars with different configurations (Tani et al., 2021b). Superposition analyses revealed similar Car positions and orientations between these two structures, although the keto groups of both Car types in nRC-LH were shifted toward the LHα subunits by ~6.7 Å (Figure 2—figure supplement 4A and C). Although KγCext molecules were not well aligned with the LHαβ-bound UQ molecule in Tch. tepidum RC-LH1, they occupied the space between adjacent LHβs (Figure 2C, Figure 2—figure supplement 4B and D). As a result, the KγCext molecules and additional B800s in R. castenholzii nRC-LH together blocked the LHαβ interface (Figure 2F), which serves as the quinone channel for the closed LH1 ring (Qian et al., 2022; Yu et al., 2018b), and for the opened LH1 ring bound only with interior Cars (Qian et al., 2021a; Swainsbury et al., 2021; Yu et al., 2018b).

### Assignment of the subunit X in nRC-LH complex

The R. castenholzii nRC-LH is distinguished from the RC-LH1 of most purple bateria by a newly identified subunit X and a membrane-bound cyt c, which has the TM helices that insert into the gap between LHαβ1 and LHαβ15 to form a putative quinone shuttling channel to the membrane quinone pool (Xin et al., 2018). Unlike the Rba. sphaeroides RC-LH1 protein PufX, which interacts with both LH1 and the L and H subunits of the RC (Cao et al., 2022; Tani et al., 2022a), subunit X in R. castenholzii was an independent TM helix that did not show any spatial overlap with PufX and PufY from the monomeric Rba. sphaeroides RC-LH1 (Figure 2—figure supplement 4E). Furthermore, compared with Tch. tepidum RC-LH1, which contains a closed LH1 ring, the c-TM of R. castenholzii nRC-LH was positioned close to the 16th LH1-α, whereas subunit X showed no overlap with the 16th LH1-β (Figure 2—figure supplement 4B). These structural features indicated that R. castenholzii RC-LH has evolved different structural elements to regulate quinone shuttling. However, the amino acid sequence of subunit X was unassigned in our previous 4.1 Å model, due to lack of clear cryo-EM densities.

From the high-resolution structure of nRC-LH, we successfully assigned the amino acid sequence (Met1-Ser26) for subunit X, which was derived from a hypothetical protein containing 32 amino acid residues (Figure 2G and H). This polypeptide was encoded by coding sequences (CDS: 1,060,366–1,060,464) in R. castenholzii (strain DSM 13941/HLO8) genome, but it was not annotated in the Protein Database of Uniprot and NCBI. The amino acid sequence of subunit X showed strict conservation with a hypothetical protein KatS3mg058_1126 (GenBank: GIV99722.1) from Roseiflexus sp., which was denoted by metagenomic analyses of the uncultivated bacteria in Katase hot spring sediment (Kato et al., 2022; Figure 2—figure supplement 5). The resolved subunit X inserted into the LH opening in opposite orientation with that of LHαβ and c-TM, where these TM helices were stabilized by hydrophobic and weak hydrogen bonding interactions (Figure 2G and I). On the cytoplasmic side, the C-terminus of subunit X was coordinated in a pocket formed by the cyt c N-terminal region (Leu8, Phe9, and Thr13), LHβ15 (Val25 and Ile28), and the 4-oxo-β-ionone ring of a KγCint molecule. A weak hydrogen bond (3.5 Å) formed between the Met25 main chain nitrogen of subunit X and Arg19 amino nitrogen of c-TM. These pigment-protein interactions together stabilized the conformation of subunit X (Figure 2I, Video 2).

![Video 2.](https://cdn.elifesciences.org/articles/88951/elife-88951-video2.mp4.jpg)

**Video 2.:** The color scheme is same as Figure 4C.

### Stabilizing the RC-LH interactions by newly assigned proteins Y and Z

Superposition of the RC structure with that of purple bacteria showed excellent matches at the L and M subunits, each of which contained five TM helices. Unlike purple bacteria, R. castenholzii L and M subunits are encoded by a fused gene puf LM but processed into two independent peptides in the complex (Collins et al., 2010; Collins et al., 2009; Yamada et al., 2005). In current model, RC-L subunit contains TM1-5 and terminates at Ala315, whereas the TM6-10 composed RC-M starts from Pro335 (Figure 3A, Figure 3—figure supplement 1, Figure 3—figure supplement 2). In addition, R. castenholzii RC-L contains an N-terminal extension (Met1-Pro35) that was solvent exposed on the cytoplasmic side (Figure 3B, Figure 3—figure supplement 1A and C). Most importantly, we resolved two additional TM helices in the RC (Figure 3A). Near the TM5 from RC-L and c-TM, a separate TM helix (corresponding to the TM7 in previous 4.1 Å model) was resolved with amino acid residues (Met1-Pro32) from a hypothetical protein Y (Figure 3C). Similar as subunit X, this protein was encoded by CDS (1,089,483–1,089,602) from R. castenholzii (strain DSM 13941/HLO8) genomic DNA, but it was not annotated in Protein Database as well. Coincidently, the amino acid sequence of protein Y was conserved with a hypothetical protein KatS3mg058_1154 (GenBank: GIV99750.1) from Roseiflexus sp. (Figure 2—figure supplement 5). The N-terminal region of protein Y was inclined toward the c-TM on the periplasmic side, wherein the 4-oxo-β-ionone ring of KγC was coordinated by hydrogen bonding interactions with Met11 (3.4 Å) from Y, Ser35 (3.0 Å) and Trp40 (2.8 Å) from the c-TM. On the cytoplasmic side, protein Y was stabilized by hydrogen bonding interactions with the TM5 of RC-L (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig3-v1.jpg)

**Figure 3.:** (A) Superposition of R. castenholzii RC structure (colored) with that of Rba. sphaeroides (white, PDB ID: 7F0L) showed excellent match at the L (wheat) and M (salmon) subunits, each of which contains five transmembrane helices (TM1–5 for L and TM6–10 for M). The newly assigned TM helices from protein Y (pale cyan) and Z (light magenta) are located on the two sides of the RC. The only TM helix of Rba. sphaeroides H subunit (gray) does not match with that of protein Z. (B) Interactions between the assigned protein Y (pale cyan), cytochrome c transmembrane (c-TM) (yellow-orange), and the RC-L (wheat). The N-terminus (N-ter) and C-terminus (C-ter) of Y, and RC-L N-terminal extension (Arg6-Pro35) that located at the periplasmic (P) and the cytoplasmic (C) side are indicated. The hydrogen bonding interactions between the amino acid residues and KγC (ruby sticks) are labeled and indicated with dashed lines. (C, D) The assigned TM helix of protein Y (C, pale cyan) and protein Z (D, light magenta) are fitted in the electron microscopy (EM) density map. Location of the coding sequence (CDS) of Y in R. castenholzii genomic DNA and the protein accession number of protein Z are indicated. The amino acid sequences of protein Y and Z are indicated below, with the modeled amino acid residues colored in black. (E) Interactions between the assigned protein Z (light magenta), LHα11 (lime green), and the RC-M (salmon). The N-terminus (N-ter) and C-terminus (C-ter) of Z that located at the periplasmic (P) and the cytoplasmic (C) side are indicated. The hydrogen bonding interactions are shown in the dashed lines. (F) Superposition of R. castenholzii RC-bound cytochrome (cyt) c (yellow-orange) with that of Rpi. globiformis (cornflower blue, PDB ID: 7XXF) showed excellent match at the tetra-heme binding domain. The c-TM and N-ter of Rpi. globiformis cyt c directed into opposite directions. (G, H) Interactions of the lipids (phosphatidylglycerol, PG; and diglyceride, DG) with the LH and RC. The L, M, and cyt c subunits of RC are shown in surface, and LHαβs are shown in cartoon forms, the lipids and RC-bound menaquinone-11s (MQs) are shown in deep purple and blue sticks, respectively.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Comparison of R. castenholzii native RC structure (colored) with that of G. phototrophica RC-dLH (gary), Tch. tepidum RC-LH1 (purple), and Rpi. globiformis RC-LH1 (cornflower blue). The N- and C-terminus of the L and M subunits are labeled and indicated. The periplasmic (P) and cytoplasmic (C) sides are labeled. (B) Comparison of R. castenholzii cytochrome (cyt) c structure (yellow-orange, heme-c colored in red) with the tetraheme-bound cyt c subunit form of G. phototrophica RC-dLH (gary), Tch. tepidum RC-LH1 (purple), and Rpi. globiformis RC-LH1 (cornflower blue). The N-terminus of each cyt c subunit is labeled. (C) Structure-based sequence alignment of the L subunit from R. castenholzii and the representative purple bacteria. Tch. tepidum (PDB ID: 5Y5S), G. phototrophica (PDB ID: 7O0U), Rpi. globiformis (PDB ID: 7XXF), and Rba. sphaeroides (PDB ID: 7F0L). The amino acid residues essential for coordinating the BChl-Mg are indicated with black triangles.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Tch. tepidum (PDB ID: 5Y5S), G. phototrophica (PDB ID: 7O0U), Rpi. globiformis (PDB ID: 7XXF), and Rba. sphaeroides (PDB ID: 7F0L). The amino acid residues essential for coordinating the BChl-Mg are indicated with black triangles.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** Tch. tepidum (PDB ID: 5Y5S), G. phototrophica (PDB ID: 7O0U), Rpi. globiformis (PDB ID: 7XXF), and Rba. sphaeroides (PDB ID: 7F0L). The amino acid residues essential for coordinating the heme-c are indicated with black triangles.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** (A) The interactions between cytochrome (cyt) c (yellow orange) and L (wheat) and M (salmon) subunits of the RC. The side view of RC is shown in middle. L, M, and cyt c subunits in the RC are shown in cartoon forms, and the c-type hemes (red) are shown in stick forms. The zoom-in views of the interactions are shown on the two sides. The amino acid residues involved in the interactions are shown in stick forms. The distances of hydrogen bonding interactions are labeled and indicated with dashed lines. (B) The amino acid residues involved in the LH and RC (which is composed of L, M, cyt c subunits) interactions are shown in stick forms. The general location of the LH and RC contacting area is shown in middle, zoom-in views of the interactions are shown on the two sides.

Unlike purple bacteria, R. castenholzii RC does not contain an H subunit. Instead, we identified an individual TM helix between the LHα11 and RC-M (Figures 1B and 3D–E). Superposition revealed mismatch of this TM helix with that of the purple bacterial H subunit (Figure 3A). This helix was assigned to cover the amino acid residues Ser12 to Asn58 of a hypothetical protein (WP_041331144.1) from R. castenholzii (strain DSM 13941/HLO8) (Figure 3D), we named it protein Z. This protein was verified with a sequence coverage of 19% by peptide mass fingerprinting (PMF) analyses of the blue-native PAGE of the nRC-LH (Table 1). The resolved protein Z was stabilized by hydrogen bonding and hydrophobic interactions with amino acid residues from the RC-M and LHα11 on the periplasmic and cytoplasmic sides (Figure 3E).

In contrast with most purple bacteria, R. castenholzii cyt c contains an N-terminal transmembrane helix c-TM, which was absent in G. phototrophica and Tch. tepidum RC-bound cyt c, and was even distinct from Rpi. globiformis cyt c that also conains an N-terminal TM helix (Tani et al., 2022b; Figure 3F, Figure 3—figure supplement 1B, Figure 3—figure supplement 3). Compared to Rpi. globiformis cyt c, the c-TM was obliquely inserting into the LH opening in an opposite direction, wherein it formed a potential quinone shuttling channel with the subunit X (Figure 3F). The N-terminal cytoplasmic region of c-TM was stabilized by extensive hydrophobic interactions with LHαβ15 and LHαβ1 (Figure 2I). These included interactions between the cyt c Ile27, Phe20, and Val16 sidechains and the LHβ1 Trp14, Leu17, and Pro16 sidechains. The main chain oxygen of Leu8 formed a hydrogen bond with the guanidine nitrogen of Arg9 from LHα15 (3.2 Å). Notably, cyt c also formed extensive hydrogen bonding interactions with the RC-L and RC-M subunits at the heme3-binding region. In addition to the protein Y, Z, and cyt c-mediated interactions, another two close contact points were evident between the RC and LH: (i) helix 1 (TM1) from RC-L to LHα13, (ii) TM6 from RC-M to LHα4 and LHα5 (Figure 3—figure supplement 4). We also identified several structured lipids (phosphatidylglycerol, PG, and diglyceride, DG) within the interface between the RC and LH subunits (Figure 3G and H), these protein-lipids contacts further stabilized the nRC-LH complex.

### dRC-LH lacked subunit X

To explore the structural and functional relationships between LH-bound Cars and the RC-LH complex, R. castenholzii cells were photoheterotrophically cultured in the presence of DPA, a Car biosynthesis inhibitor (Gall et al., 2005). In response to DPA treatment, bacterial growth curves clearly indicated a decreased proliferation rate of cells grown under high illumination, confirming the important roles of Cars in photosynthesis and cell proliferation (Figure 1—figure supplement 1A and B). Interestingly, DPA treatment did not affect the growth of cells under medium and low illuminations, which showed an overall much lower proliferation rate (Figure 1—figure supplement 1B). Concomitantly, the color of the growing cells changed progressively from brownish red in the first culture to light yellow in the fifth sub-culture (Figure 1—figure supplement 1A), indicating gradual inhibition of Car biosynthesis during sub-culturing. To confirm the effects of DPA treatment on Car incorporation into the RC-LH, dRC-LH complexes were isolated from each successive sub-culture of DPA-treated R. castenholzii cells (Figure 1—figure supplement 1F). There was a striking decrease in Car absorbance in dRC-LH complexes extracted from the third through fifth sub-cultures of DPA-treated cells compared to nRC-LH extracted from untreated cells (Figure 1—figure supplement 1D and E). Additionally, HPLC analysis of dRC-LH isolated from the fifth sub-culture of DPA-treated cells showed same pigment compositions but strikingly decreased Car absorbance compared to the nRC-LH (Figure 2—figure supplement 3B).

To illustrate the effects of DPA treatment on the RC-LH architecture, we determined the cryo-EM structure of dRC-LH isolated from the fifth sub-culture of DPA-treated R. castenholzii cells at 3.1 Å resolution (Figure 4A and B, Figure 4—figure supplement 1). The most obvious difference between these two structures was the absence of the entire X subunit and the cytoplasmic region of cyt c subunit (Pro6-Val16) in the dRC-LH; both were located at the LH opening of nRC-LH (Figure 4C, Video 2, Figure 1—figure supplement 6C). Notably, only five KγCint molecules that spanned the LHαβ5, -7, -9, -10, and -11 heterodimers were resolved with clear density maps and built in the dRC-LH structure, whereas none of the KγCext molecules were observed (Figure 4B, Figure 1—figure supplement 4C, Figure 4—figure supplement 2A, Video 1). The five KγCint molecules were located relatively far from the LH opening (~52 Å), which is where Cars with the highest B-factors were distributed, indicating an unstable conformation (Figure 2—figure supplement 2A). Additionally, the five KγCint molecules in dRC-LH adopted the same conformation and a similar edge-to-edge distance from LH-bound B800/B880s as the corresponding KγCint molecules did in nRC-LH (Figure 4D, Tables 3 and 4). The absence of KγCext and most KγCint molecules in the LH ring confirmed the spectroscopic and HPLC analyses that DPA treatment decreased the numbers of LH-bound Cars in the dRC-LH.

![Figure 4.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig4-v1.jpg)

**Figure 4.:** (A) Cryo-EM map of dRC-LH seen from the bottom with LH ring dimensions indicated. (B) Cartoon representation of the dRC-LH complex from the bottom. The interior keto-γ-carotenes (KγCint) are shown in limon and bacteriochlorophyll (BChl) Mg atoms are shown as spheres. (C) Comparison of the LH ring openings in the nRC-LH (left) and dRC-LH (right). The cryo-EM maps of the subunit X (hot pink), cytochrome c transmembrane (c-TM) (yellow-orange), and neighboring LHαβ1 and LHαβ15 are shown to indicate the conformational changes. The LH-bound B880s (purple), B800s (pink), and KγC (ruby) are shown in sticks and fitted in the EM map. The periplasmic (P) and cytoplasmic (C) sides are labeled. (D) Comparison of the KγC arrangement between the nRC-LH and dRC-LH complexes. The KγCint, KγCext, and KγC in nRC-LH are shown as cyan, orange, and ruby sticks, respectively. The five KγCint molecules bound in the dRC-LH complex are shown as limon spheres. (E) Comparison of the central BChl-Mg atoms in nRC-LH and dRC-LH. The B880 and B800 Mg atoms are shown as purple and pink spheres, respectively, in nRC-LH, and as white spheres in dRC-LH. The two structures are superposed at the TM helices of the L and M subunits. The distances between the central Mg atoms of B880 and the nearest special pair BChls are labeled and indicated with dashed lines. The cofactors bound in the RC are shown in stick form; the iron is shown as spheres. TM helices of subunit X (hot pink), protein Y (pale cyan), Z (light magenta), c-TM (yellow-orange in nRC-LH and white in dRC-LH), and LHαβ1 and LHαβ15 (colored in nRC-LH and white in dRC-LH) are shown in ribbon form to demonstrate the spatial organization. (F) Comparison of the LH ring opening and quinone channels in nRC-LH and dRC-LH. The LH ring of dRC-LH is shown in surface form; the RC (including Y and Z), c-TM, and subunit X in nRC-LH are shown in cartoon forms; and menaquinones (MQs) are shown in blue sticks. Dashed lines indicate the dimensions of the LH ring openings in the two structures. The blue arrow represents the putative quinone shuttling path. (G) Model diagram of the auracyanin (Ac) oxidation assay. Upon illumination, light energy absorbed by the LH-bound BChls (B800 and B880) is transferred to RC. The primary charge separation occurs and initiates sequential electron transfer that reduces the MQs. The generated hydroquinone diffuses out of the RC-LH and exchanges with the menaquinone-4 in the solution. Once the reduced Ac is oxidized, the released electrons can be transferred back to reduce the photo-oxidized special pair through the c-type hemes. (H) The rate of Ac oxidation at various starting concentrations of menaquinone-4, in presence of the nRC-LH (black) or dRC-LH (orange). Data are shown as the mean ± standard deviations (n=3).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) A representative raw cryo-EM micrograph of the dRC-LH complex extracted from the fifth sub-culture of diphenylamine (DPA)-treated R. castenholzii cells grown under high illumination (180 μmol m–2 s–1). (B) Representative reference-free 2D class averages of the dRC-LH complex. (C) Local resolution of the cryo-EM map estimated by ResMap. (D) The different views of angular distribution of the dRC-LH particles in final reconstruction. (E) The gold-standard Fourier shell correlation (FSC) curve of the cryo-EM map (corrected map, black; unmasked, green; masked, blue; phase randomized, red) and the FSC curve between the map and the final refined model (orange). (F) Workflow of the cryo-EM data processing for the dRC-LH complex. All structural figures here are generated with ChimeraX.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) The density map of LH-bound KγC in the carotenoid-depleted RC-LH (dRC-LH) complex. The corresponding atomic models of KγC (interior KγC [KγCint]) bound in LHαβ5, -7, -9, -10, and -11 are colored in limon. (B) Superposition of LHαβ5, -6, -7, and -8 from dRC-LH. LHαβs are shown in ribbon form, the Mg atoms of LH-bound BChls (B800/B880) are shown in spheres. KγCint and Phe28 sidechains are shown as stick forms. (C, D) The LHα-Phe28 sidechain orientations in dRC-LH (C) and native RC-LH (nRC-LH) (D). LHαβs are shown in cartoon form. The Phe28 sidechain and KγC are shown as sticks.

**Table 3.**
 Edge-to-edge distance (Å) of interior keto-γ-carotenes (KγCint) to light harvesting (LH)-bound B800/B880s in the native reaction center-LH (nRC-LH) and carotenoid-depleted RC-LH (dRC-LH) complexes from R. castenholzii.


<table>
  <thead>
    <tr>
      <th>nRC-LH</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>B800</td>
      <td>–</td>
      <td>3.6</td>
      <td>4.2</td>
      <td>3.7</td>
      <td>3.6</td>
      <td>4.1</td>
      <td>3.5</td>
      <td>3.4</td>
      <td>3.7</td>
      <td>3.9</td>
      <td>4.0</td>
      <td>3.8</td>
      <td>4.2</td>
      <td>3.7</td>
      <td>–</td>
    </tr>
    <tr>
      <td>B880</td>
      <td>–</td>
      <td>4.3</td>
      <td>3.8</td>
      <td>3.8</td>
      <td>3.9</td>
      <td>3.9</td>
      <td>4.2</td>
      <td>4.0</td>
      <td>3.9</td>
      <td>4.3</td>
      <td>4.0</td>
      <td>4.1</td>
      <td>3.6</td>
      <td>3.6</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>dRC-LH</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <td>B800</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>4.2</td>
      <td>–</td>
      <td>3.4</td>
      <td>–</td>
      <td>4.1</td>
      <td>3.3</td>
      <td>3.9</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>B880</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>4.0</td>
      <td>–</td>
      <td>4.2</td>
      <td>–</td>
      <td>4.4</td>
      <td>3.8</td>
      <td>4.0</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Edge-to-edge distance (Å) of exterior keto-γ-carotenes (KγCext) to light harvesting (LH)-bound B800/B880s in the native reaction center-LH (nRC-LH) complex from R. castenholzii.


<table>
  <thead>
    <tr>
      <th>nRC-LH</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>B800</td>
      <td>–</td>
      <td>3.7</td>
      <td>3.4</td>
      <td>3.9</td>
      <td>3.8</td>
      <td>3.8</td>
      <td>3.7</td>
      <td>3.3</td>
      <td>3.5</td>
      <td>3.2</td>
      <td>3.3</td>
      <td>3.4</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>4.2</td>
    </tr>
    <tr>
      <td>B880</td>
      <td>–</td>
      <td>4.8</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>4.1</td>
      <td>4.2</td>
      <td>4.3</td>
      <td>4.8</td>
      <td>4.8</td>
      <td>5.1</td>
      <td>4.7</td>
      <td>4.2</td>
      <td>4.8</td>
      <td>4.6</td>
    </tr>
  </tbody>
</table>

To explore the effect of Car depletion on the LHαβ structure, we superposed the Car-bound LHαβ5, LHαβ7 with adjacent Car-unbound LHαβ6 and LHαβ8 in the dRC-LH. Except slight differences at the sidechain orientations of LHα-Phe28, these LHαβ heterodimers adopted exactly the same conformation (Figure 4—figure supplement 2B). However, both nRC-LH and dRC-LH contained the same LHα-Phe28 orientations at LHα7, -9, and -11. In addition, Phe28 sidechain orientations were not correlated with the Car binding, since each LHαβ in nRC-LH bound both KγCint and KγCext (Figure 4—figure supplement 2C and D). These observations thus indicated that Car depletion did not affect the LHαβ structure. Nevertheless, the distances between adjacent LHαs and LHβs in the dRC-LH showed average increases of 0.5 Å and 1.0 Å, respectively, compared with nRC-LH (Table 5). Accordingly, the Mg-to-Mg distances between adjacent B880s and B800s also increased in dRC-LH (Tables 6 and 7). Specifically, the LH-bound B880s and B800s shifted away from the LH ring center by ~2.0 Å, consequently increasing the Mg-to-Mg distance between LH-bound B880s and the nearest special pair of BChls in the RC (Figure 4E, Table 8). These results therefore indicated that Car depletion not only decreased the number of LH-bound Cars, but also altered the conformation of dRC-LH opening and pigments organizations. These alterations could affect the efficiency of energy transfer during the primary photochemical reactions (Şener et al., 2011; Xin et al., 2012).

**Table 5.**
 Distances (Å) between the LHαβ transmembrane (TM) helices of the native reaction center-light harvesting (nRC-LH) and carotenoid-depleted RC-LH (dRC-LH) complexes from R. castenholzii.The distance is measured between LHαβn and LHαβ (n+1).


<table>
  <thead>
    <tr>
      <th>nRC-LH</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15*</th>
      <th>16†</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LHα</td>
      <td>14.8</td>
      <td>14.7</td>
      <td>14.6</td>
      <td>14.3</td>
      <td>14.4</td>
      <td>14.7</td>
      <td>15.4</td>
      <td>14.9</td>
      <td>15.4</td>
      <td>14.6</td>
      <td>14.7</td>
      <td>15.0</td>
      <td>14.5</td>
      <td>14.4</td>
      <td>19.4</td>
      <td>9.7</td>
    </tr>
    <tr>
      <td>LHβ</td>
      <td>20.0</td>
      <td>19.8</td>
      <td>20.0</td>
      <td>20.4</td>
      <td>20.2</td>
      <td>20.0</td>
      <td>19.8</td>
      <td>19.9</td>
      <td>19.7</td>
      <td>20.1</td>
      <td>20.0</td>
      <td>19.9</td>
      <td>20.1</td>
      <td>20.1</td>
      <td>11.2</td>
      <td>28.1</td>
    </tr>
    <tr>
      <td>dRC-LH</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15*</td>
      <td>16†</td>
    </tr>
    <tr>
      <td>LHα</td>
      <td>15.4</td>
      <td>15.4</td>
      <td>15.3</td>
      <td>15.0</td>
      <td>14.9</td>
      <td>15.3</td>
      <td>16.2</td>
      <td>15.5</td>
      <td>16.1</td>
      <td>15.2</td>
      <td>15.4</td>
      <td>15.6</td>
      <td>15.3</td>
      <td>14.9</td>
      <td>19.6</td>
      <td>10.2</td>
    </tr>
    <tr>
      <td>LHβ</td>
      <td>21.0</td>
      <td>20.7</td>
      <td>20.9</td>
      <td>21.2</td>
      <td>20.9</td>
      <td>21.0</td>
      <td>20.5</td>
      <td>20.9</td>
      <td>20.6</td>
      <td>20.8</td>
      <td>21.0</td>
      <td>20.7</td>
      <td>20.9</td>
      <td>20.9</td>
      <td>–</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

_*The distances from LHα15 Met-22 to c-TM Val-33, and LHβ15 Ile-39 to subunit X.†The distances from LHα1 Val-29 to c-TM Tyr-44, and LHβ1 Leu-37 to subunit X._

**Table 6.**
 The distances (Å) between adjacent light harvesting (LH)-bound B880s of the native reaction center-LH (nRC-LH) and carotenoid-depleted RC-LH (dRC-LH) complexes from R. castenholzii.


<table>
  <thead>
    <tr>
      <th>nRC-LH</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Edge-to-edge*</td>
      <td>3.3</td>
      <td>3.1</td>
      <td>3.4</td>
      <td>3.4</td>
      <td>3.6</td>
      <td>3.8</td>
      <td>3.7</td>
      <td>3.8</td>
      <td>3.7</td>
      <td>3.6</td>
      <td>3.5</td>
      <td>3.6</td>
      <td>3.5</td>
      <td>3.6</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td>Edge-to-edge†</td>
      <td>3.5</td>
      <td>3.4</td>
      <td>3.6</td>
      <td>3.6</td>
      <td>3.4</td>
      <td>4.0</td>
      <td>3.6</td>
      <td>3.8</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.3</td>
      <td>3.7</td>
      <td>3.6</td>
      <td>3.6</td>
      <td>19.1</td>
    </tr>
    <tr>
      <td>Mg-to-Mg*</td>
      <td>10.2</td>
      <td>9.9</td>
      <td>9.8</td>
      <td>9.9</td>
      <td>9.7</td>
      <td>9.8</td>
      <td>9.9</td>
      <td>10.0</td>
      <td>9.9</td>
      <td>9.9</td>
      <td>9.8</td>
      <td>9.6</td>
      <td>9.7</td>
      <td>9.3</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>Mg-to-Mg†</td>
      <td>7.6</td>
      <td>7.5</td>
      <td>7.7</td>
      <td>7.7</td>
      <td>7.6</td>
      <td>7.6</td>
      <td>7.6</td>
      <td>7.5</td>
      <td>7.6</td>
      <td>7.8</td>
      <td>7.7</td>
      <td>7.9</td>
      <td>7.9</td>
      <td>7.9</td>
      <td>26.2</td>
    </tr>
    <tr>
      <td>dRC-LH</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <td>Edge-to-edge*</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.7</td>
      <td>3.5</td>
      <td>3.7</td>
      <td>3.7</td>
      <td>3.8</td>
      <td>3.9</td>
      <td>3.8</td>
      <td>3.6</td>
      <td>3.5</td>
      <td>3.6</td>
      <td>3.3</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>Edge-to-edge†</td>
      <td>4.1</td>
      <td>3.8</td>
      <td>4.0</td>
      <td>3.8</td>
      <td>3.9</td>
      <td>3.8</td>
      <td>4.1</td>
      <td>4.0</td>
      <td>4.1</td>
      <td>3.9</td>
      <td>3.9</td>
      <td>3.9</td>
      <td>3.9</td>
      <td>3.8</td>
      <td>20.2</td>
    </tr>
    <tr>
      <td>Mg-to-Mg*</td>
      <td>9.7</td>
      <td>9.7</td>
      <td>9.5</td>
      <td>9.6</td>
      <td>9.6</td>
      <td>9.6</td>
      <td>9.4</td>
      <td>9.7</td>
      <td>9.7</td>
      <td>9.6</td>
      <td>9.5</td>
      <td>9.4</td>
      <td>9.5</td>
      <td>9.3</td>
      <td>9.2</td>
    </tr>
    <tr>
      <td>Mg-to-Mg†</td>
      <td>9.0</td>
      <td>8.7</td>
      <td>8.8</td>
      <td>8.8</td>
      <td>8.4</td>
      <td>8.9</td>
      <td>8.8</td>
      <td>8.6</td>
      <td>8.8</td>
      <td>8.8</td>
      <td>8.9</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>8.7</td>
      <td>27.2</td>
    </tr>
  </tbody>
</table>

_*Distance between the B880 bound by the same transmembrane pairs of LH.†Distance between the B880 bound by adjacent transmembrane pairs of LH._

**Table 7.**
 The distances (Å) between light harvesting (LH)-bound B800s of the native reaction center-LH (nRC-LH) and carotenoid-depleted RC-LH (dRC-LH) complexes from R. castenholzii.


<table>
  <thead>
    <tr>
      <th>nRC-LH</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Edge-to-edge</td>
      <td>15.4</td>
      <td>15.5</td>
      <td>15.5</td>
      <td>15.4</td>
      <td>15.4</td>
      <td>15.6</td>
      <td>15.6</td>
      <td>15.4</td>
      <td>15.6</td>
      <td>15.5</td>
      <td>15.5</td>
      <td>15.6</td>
      <td>15.6</td>
      <td>15.2</td>
      <td>33.4</td>
    </tr>
    <tr>
      <td>Mg-to-Mg</td>
      <td>18.4</td>
      <td>18.3</td>
      <td>18.4</td>
      <td>18.5</td>
      <td>18.5</td>
      <td>18.5</td>
      <td>18.5</td>
      <td>18.3</td>
      <td>18.4</td>
      <td>18.4</td>
      <td>18.5</td>
      <td>18.5</td>
      <td>18.4</td>
      <td>18.3</td>
      <td>38.5</td>
    </tr>
    <tr>
      <td>dRC-LH</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <td>Edge-to-edge</td>
      <td>15.8</td>
      <td>15.9</td>
      <td>16.0</td>
      <td>15.7</td>
      <td>15.8</td>
      <td>16.2</td>
      <td>15.9</td>
      <td>15.8</td>
      <td>16.1</td>
      <td>15.8</td>
      <td>16.0</td>
      <td>16.1</td>
      <td>15.8</td>
      <td>15.8</td>
      <td>33.2</td>
    </tr>
    <tr>
      <td>Mg-to-Mg</td>
      <td>19.1</td>
      <td>19.1</td>
      <td>19.3</td>
      <td>19.1</td>
      <td>19.2</td>
      <td>19.4</td>
      <td>19.1</td>
      <td>19.2</td>
      <td>19.2</td>
      <td>19.1</td>
      <td>19.3</td>
      <td>19.3</td>
      <td>19.1</td>
      <td>19.2</td>
      <td>38.3</td>
    </tr>
  </tbody>
</table>

**Table 8.**
 The Mg-to-Mg distances between light harvesting (LH)-bound B880s and the nearest special pair of bacteriochlorophyll (BChls) in the reaction center (RC) of R. castenholzii native RC-LH (nRC-LH) and carotenoid-depleted RC-LH (dRC-LH) complexes.


<table>
  <thead>
    <tr>
      <th>nRC-LH</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mg-to-Mg*</td>
      <td>40.3</td>
      <td>42.4</td>
      <td>44.7</td>
      <td>47.2</td>
      <td>46.8</td>
      <td>43.9</td>
      <td>40.2</td>
      <td>37.3</td>
      <td>36.5</td>
      <td>37.7</td>
      <td>40.6</td>
      <td>43.7</td>
      <td>44.5</td>
      <td>44.8</td>
      <td>44.2</td>
    </tr>
    <tr>
      <td>Mg-to-Mg†</td>
      <td>41.5</td>
      <td>43.8</td>
      <td>46.3</td>
      <td>48.1</td>
      <td>45.6</td>
      <td>42.0</td>
      <td>38.5</td>
      <td>36.8</td>
      <td>36.8</td>
      <td>39.6</td>
      <td>42.6</td>
      <td>44.5</td>
      <td>44.9</td>
      <td>44.8</td>
      <td>43.6</td>
    </tr>
    <tr>
      <td>dRC-LH</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <td>Mg-to-Mg*</td>
      <td>42.0</td>
      <td>44.8</td>
      <td>47.2</td>
      <td>49.9</td>
      <td>49.0</td>
      <td>45.8</td>
      <td>42.0</td>
      <td>39.1</td>
      <td>38.3</td>
      <td>39.7</td>
      <td>43.0</td>
      <td>46.0</td>
      <td>46.2</td>
      <td>46.4</td>
      <td>45.4</td>
    </tr>
    <tr>
      <td>Mg-to-Mg†</td>
      <td>43.1</td>
      <td>45.8</td>
      <td>48.5</td>
      <td>50.0</td>
      <td>47.2</td>
      <td>43.8</td>
      <td>40.2</td>
      <td>38.4</td>
      <td>38.6</td>
      <td>41.3</td>
      <td>44.5</td>
      <td>46.0</td>
      <td>46.3</td>
      <td>46.1</td>
      <td>44.6</td>
    </tr>
  </tbody>
</table>

_*The distances from Mg2+ of the first LH-bound B880 to the nearest special pair of BChls.†The distances from Mg2+ of the second LH-bound B880 to the nearest special pair of BChls._

### Conformational changes in the dRC-LH accelerated quinone/quinol exchange

In nRC-LH, insertion of the c-TM and subunit X at the LH opening, wherein the N-terminal cytoplasmic region of c-TM was stabilized by extensive hydrophobic and weak hydrogen bonding interactions with subunit X, LHαβ15, and LHαβ1 (Figures 2I and 4C). The c-TM was closer to LHα1 (9.7 Å) than to LHα15, whereas subunit X was closer to LHβ15 (11.2 Å), creating a narrow gap between the c-TM and the LHαβ15 (Figure 4C and F, Table 5). The B800 pigment was not detected between c-TM and LHα15 (Figure 4C). Thus, the c-TM and subunit X were positioned to the sides of LHα1 and LHβ15, respectively; this formed a 19.4 Å gap between the c-TM and LHα15, and a 28 Å gap between subunit X and LHβ1, both of which may have allowed reduced quinones to exit the LH to the membrane quinone pool. Because dRC-LH lacked subunit X, the gap between LHβ1 and LHβ15 increased to ~38.0 Å (Figure 4C and F).

To investigate the functional effects of this conformational change, we compared the quinone/quinol exchange rates for nRC-LH and dRC-LH complexes. In the cyclic electron transport chain of R. castenholzii, the periplasmic electron acceptor auracyanin (Ac) transfers electrons back to the RC special pair through the tetra-heme of cyt c subunit, reducing the photo-oxidized special pair for turnover of the photo-reaction and electron transfer that subsequently reduce the bound menaquinones (MQA and MQB) in the RC. The reduced MQH2 is released from its binding site and exchanges with free MQs outside the RC-LH (Figure 4G). Using sodium dithionite-reduced Ac as the electron donor and menaquinone-4 as the electron acceptor, we measured Ac absorbance changes at 604 nm with varied concentrations of menaquinone-4 (Figure 5—figure supplement 1A and B). The initial oxidation rate of Ac was markedly higher in the presence of dRC-LH than nRC-LH (Figure 4H). This was consistent with the determined apparent Michaelis constants, which showed that dRC-LH had an accelerated quinone/quinol exchange rate of menaquinone-4 at 6.12±0.62 μM min–1 (Table 9). The accelerated quinone/quinol exchange rate in dRC-LH was probably resulted from exposure of the LHαβ interface by Car depletion, and also the increased gap dimension of the LH ring.

**Table 9.**
 Apparent Michaelis constants of menaquinone-4 as electron acceptor in the auracyanin (Ac) oxidation assay, in presence of the R. castenholzii native reaction center-light harvesting (nRC-LH) or carotenoid-depleted RC-LH (dRC-LH) complex.


<table>
  <thead>
    <tr>
      <th></th>
      <th>nRC-LH</th>
      <th>dRC-LH</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Km (μM)</td>
      <td>32.24±6.84</td>
      <td>10.43±1.23</td>
    </tr>
    <tr>
      <td>kcat (min–1)</td>
      <td>82.61±9.09</td>
      <td>63.83±2.49</td>
    </tr>
    <tr>
      <td>kcat/Km</td>
      <td>2.56±0.49</td>
      <td>6.12±0.62</td>
    </tr>
  </tbody>
</table>

### Car depletion did not affect the Car-to-BChl energy transfer efficiency

To elucidate the effects of Cars depletion on the Car-to-BChl energy transfer efficiency of the RC-LH, we first examined the configurations and coordinating environments of the LH-bound Cars. KγCint molecules spanned the TM region of each LHαβ heterodimer; the heads with 4-oxo-β-ionone ring were inserted into the hydrophobic pocket formed by the LHα and LHβ subunits, the phytol tails of two B880s, and the B800 porphyrin ring. On the periplasmic side, the ψ-end group of KγCint was directed into a hydrophobic patch formed by two adjacent LHα subunits (Figure 5A, left). Alternatively, the newly identified KγCext molecules were immobilized in a position that was nearly parallel to the adjacent LHβs. The heads were inserted into a cavity formed by the B800 porphyrin ring and two adjacent LHβs, and their tails extended along the adjacent LHβs, stabilized by hydrophobic interactions (Figure 5A, right). However, depletion of these KγCext molecules in dRC-LH prevented the tight packing of the KγCint molecules with LHαβ heterodimers. Thus, in the absence of KγCext, the head of each KγCint molecule shifted toward the B800 porphyrin ring, which moved the head out from the center of the LH ring by ~3.0 Å (Figure 5B). However, the edge-to-edge distances of KγCint to the B800/B880s remained similar between dRC-LH and nRC-LH (Table 3).

![Figure 5.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig5-v1.jpg)

**Figure 5.:** (A) Coordination of representative KγCint (cyan) and KγCext (orange) molecules in the nRC-LH complex. Shown as stick forms are the amino acid residues from LHα (lime green) and LHβ (marine) surrounding the 4-oxo-β-ionone ring; the ψ-end group of the KγC; and the BChls B880 (purple) and B800 (pink) in the nearby LHαβ. (B) Coordination of the KγCint molecules, which are shown in limon and white in dRC-LH and nRC-LH, respectively. Amino acid residues from the nearby LHα (lime green) and LHβ (marine) and the B800 molecule that covers the KγCint molecule are shown as stick forms. The distance deviations of the central Mg atoms in B880 (purple) and B800 (pink) in the two structures are labeled and indicated with dashed lines. The periplasmic (P) and cytoplasmic (C) sides are labeled. (C) Spectral analysis of the RC-LH complex. Fluorescence emissions are shown for nRC-LH (black) and dRC-LH (orange) complexes isolated from R. castenholzii after excitation at 470 nm. (D) Fluorescence excitation and absorption (1−T) spectra are shown as dotted and solid lines, respectively, for nRC-LH (black) and dRC-LH (orange). The Car-to-BChl energy transfer efficiency (vertical dashed line) was calculated by normalizing the fluorescence excitation and absorption spectra at 880 nm to 1.0.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A, B) Ac oxidation assays of the nRC-LH and dRC-LH complexes. The absorbance of Ac at 604 nm in presence of the nRC-LH (A) or dRC-LH (B) complex was recorded every 2 min, at 323 K and under illumination of 180 μmol m–2 s–1. Reduced Ac was used as electron donor, and varied concentrations of menaquinone-4 was used as electron acceptor.

We next measured the fluorescence excitation and absorption spectra of the nRC-LH and dRC-LH complexes to calculate the Car-to-BChl energy transfer efficiency. Most RC-LH fluorescence is emitted from the B880 Qy band (Collins et al., 2009). Excitation of nRC-LH at 470 nm yielded emissions at 900 nm, whereas dRC-LH excitation produced emissions at 905 nm (Figure 5C). This shift of the emission peak indicated changes in the LH ring pigment configuration between the two complexes. The intensity ratio of fluorescence excitation spectra to absorption spectra, expressed as the 1−T of RC-LH, was then calculated. The results revealed that the Car-to-BChl energy transfer efficiency remained similar between nRC-LH (44%) and dRC-LH (46%) (Figure 5D). Car-to-BChl energy transfer in the LH is closely related to the number of Car conjugated double bonds, the relative distances between Cars and BChls, and Car/BChl spatial organization (Polívka and Frank, 2010). In R. castenholzii, each KγC contains 11 conjugated double bonds (Collins et al., 2009). Although all KγCext and most KγCint molecules were depleted in dRC-LH, the five remaining KγCint molecules adopted the same configuration and similar edge-to-edge distances with LH-bound B800/B880s as that in the nRC-LH (Figure 4D, Table 3). Therefore, Car depletion from the LH ring in dRC-LH did not affect interactions between the remaining Cars and BChls, which exhibited similar excitation energy transfer values in dRC-LH and nRC-LH complexes. These results suggested that the existing Car-to-BChl energy transfer efficiency is similar even though there is variation in the number of LH-bound Cars.

## Discussion

Unlike the well-studied purple bacteria, which contain two types of LH complexes, R. castenholzii contains only one RC-LH complex for LH and primary photochemical reactions. It does not contain the H subunit that is typically found in purple bacteria (Pugh et al., 1998; Qian et al., 2005; Yamada et al., 2005). Especially, R. castenholzii RC-LH contains a tetra-heme cyt c subunit that interrupts the LH ring, which is composed of 15 αβ-polypeptides, through a novel N-terminal TM helix; together with the newly identified subunit X, this forms a potential quinone shuttling channel on the LH ring. In the present study, we determined high-resolution cryo-EM structures of nRC-LH, from which we assigned the full amino acid sequence of subunit X, and two additional TM helices derived from hypothetical proteins Y and Z in the RC, which both functioned in stabilizing the RC-LH interactions. Most importantly, we identified 14 additional KγC molecules (KγCext) in the LH ring exterior, and one KγC inserted between LHαβ1 and c-TM, which generated a 2:3 Car:BChl molar ratio consistent with previous pigments analyses (Collins et al., 2009). Binding of the KγCint and KγCext together with the B800s blocked the proposed quinone channel between LHαβ subunits. DPA treatment of the cells yielded a dRC-LH, referred to as dRC-LH; a 3.1 Å resolution cryo-EM structure resolved only five KγCint molecules, and the absence of subunit X and the cytoplasmic region of c-TM. These alterations in the dRC-LH increased the size of the LH opening and exposed the LHαβ interface, accelerating the in vitro quinone/quinol exchange rate of menaquinone-4, but did not affect the Car-to-BChl energy transfer efficiency.

To maintain continuous photo-reaction and turnover of the electron transport chain, two quinone exchange/transport routes are required for the bacterial RC-LH1 complex. One is the exchange route for the free/bound quinone in the RC, which was represented by a newly identified MQc in our nRC-LH structure (Figure 3H), and also extra UQ molecules found in many purple bacterial RCs (Cao et al., 2022; Kishi et al., 2021; Qian et al., 2022; Qian et al., 2018; Swainsbury et al., 2021; Tani et al., 2022b; Yu et al., 2018a). The other one is shuttling channel between the inside and outside of the LH1 ring. For Tch. tepidum RC-LH1 that contains an almost symmetric and completely closed LH1 ring, except the ‘waiting’ UQ8 identified near QB, one UQ8 was found to be inserted between the LH1α and LH1β subunits (Yu et al., 2018a), representing a potential quinone exchange channel between the LHαβ interface. Therefore, the space between the LHαβ subunits can serve as quinone exchange channel for the closed LH1 ring (Qian et al., 2022; Yu et al., 2018b), and also for the opened LH1 ring bound only with interior Cars (Qian et al., 2021a; Swainsbury et al., 2021; Yu et al., 2018b). For most purple bacterial RC-LH1 complexes with an opened C-shaped LH1 ring, reduced quinones are also shuttled from the RC through a gap at the LH1 ring, which is disrupted by protein W, or PufX and PufY (or protein-U) (Cao et al., 2022; Jackson et al., 2018; Qian et al., 2021a; Tani et al., 2021a; Tani et al., 2022a; Tani et al., 2021b).

Distinct from the RC-LH1 of most purple bacteria, each LHαβ of R. castenholzii non-covalently bound an additional B800 BChl at the cytoplasmic side, which occupied the LHαβ interface at the cytoplasmic side (Figure 2C, Figure 2—figure supplement 1C). In addition, we identified KγC at three distinct positions in the nRC-LH ring: KγCint and KγCext, and also an additional KγC near the LH opening (Figures 1D and 3B). The KγCint molecules embedded between the LHαβs had a similar conformation as they do in the completely closed and also the opened LH1 ring of purple bacteria. In contrast, KγCext molecules occupied the space between adjacent LHβs, although they were not well aligned with the Tch. tepidum LHαβ-bound UQ8 molecule (Figure 2C, Figure 2—figure supplement 4D). Therefore, incorporation of the KγCext molecules and additional B800s in R. castenholzii nRC-LH most likely together blocked the LHαβ interface for putative quinone exchange (Figure 2F). Alternatively, R. castenholzii RC-LH incorporated a membrane-bound cyt c and a hypothetical protein X, which has the TM helices that interrupted the LH ring to form a potential channel for controlled quinone/quinol exchange (Figure 6). Superposition of R. castenholzii with purple bacterial RC-LH1s revealed distinct locations and orientations of subunit X and c-TM compared to PufX and PufY (Figure 2—figure supplement 4E), indicating R. castenholzii has evolved different structural elements for regulating quinone shuttling.

![Figure 6.](https://cdn.elifesciences.org/articles/88951/elife-88951-fig6-v1.jpg)

**Figure 6.:** In native RC-LH, incorporation of the external keto-γ-carotenes (KγCext) and LH-bound B800s blocked the LHαβ interface. Alternatively, the subunit X disrupts the ring and forms a potential quinone channel with the cytochrome c transmembrane (c-TM), facilitating controlled quinone/quinol binding and shuttling. In Car-depleted RC-LH (dRC-LH), less Car assembly exposed the LHαβ interface, absence of the subunit X and cytoplasmic region of c-TM concomitantly broadened the LH opening, which together accelerated the quinone/quinol exchange.

Genetic depletion of the LH1-bound Cars promoted the photosynthetic growth of a PufX-knockout Rba. sphaeroides mutant with a closed LH1 ring (Cao et al., 2022; McGlynn et al., 1994; Olsen et al., 2017); this implies that disruption of Cars binding exposed the blocked quinone channel between LHαβ interface and facilitated the quinone exchange, thus promoting photosynthetic growth. In our study, depletion of the KγCext and most KγCint molecules by DPA treatment could also expose the space between the Car-unbound LHαβ subunits. In addition, absence of the subunit X and cytoplasmic region of c-TM in dRC-LH broadened the dimensions of the LH ring opening, which most likely together accelerated the quinone/quinol exchange rate of the dRC-LH (Figure 6). This was consistent with a previous observation that the open form of the Rhodopseudomonas (Rps.) palustris RC-LH1 has a faster UQ2 diffusion rate than the closed form (Swainsbury et al., 2021). Notably, depletion of most LH-bound Cars only affected the stable conformation of the cytoplasmic region of c-TM, which was closely associated with subunit X to form the putative quinone channel (Figure 2I). Compared to cyt c subunit that formed extensive hydrogen bonding interactions with the L, M, and Y of the RC, the subunit X was characterized by high B-factors, fewer contacts with the RC-LH, and an easily disrupted conformation (Figures 3B and 4C, Figure 2—figure supplement 2B). Especially, the subunit X was derived from a hypothetical protein that inserted into the LH opening in an opposite orientation with LHαβ and c-TM, suggesting that it was likely the last subunit incorporated into the RC-LH. Therefore, R. castenholzii RC-LH could probably evolve the subunit X to control the conformation of the quinone shuttling channel.

Cars contribute to the self-assemble of natural α/β polypeptides to form LH1 complexes in vitro (Fiedor et al., 2004), Car-less Rsp. rubrum LH1 can be obtained by exogenous recombination (Parkes-Loach et al., 1988). In the Car-less Rba. sphaeroides mutant strain R26, the polymerized form of RC-LH is predominantly monomeric, and the curvature of the photosynthetic membrane is altered due to the lack of dimeric RC-LH (Ng et al., 2011). This implies that Cars assembly can regulate the conformation of the RC-LH complex. In our study, Car depletion also affected the LH opening conformation and the quinone/quinol exchange rate of the dRC-LH. Although the extensive interactions between subunit X, c-TM, and LHαβ15 and LHαβ1 were disrupted in dRC-LH (Figures 2I and 4C), the correlation between Car depletion and the absence of subunit X has not been adequately verified. Since DPA treatment is not a clean way to examine the effect of Cars, it left several interior Cars still bound to the LH ring. DPA is a broad-spectrum inhibitor that slows cellular metabolic processes and specifically affects Car biosynthesis by inhibiting phytoene desaturase (CrtI), an essential enzyme catalyzes conversion of the colorless Car precursor phytoene to the colored lycopene (Bramley, 1993). We here found that DPA treatment not only dramatically decreased the R. castenholzii proliferation rate but also depleted the LH-bound Cars in dRC-LH (Figures 1A and 4, Figure 1—figure supplement 1B). However, an efficient genetic manipulation system of R. castenholzii is required to obtain a Car-less RC-LH complex, for elucidating the correlations between Cars and the RC-LH assembly, as well as the photosynthetic growth of cells. To our current knowledge, genetic editing of R. castenholzii is restricted by its morphology as a multicellular filamentous bacterium with an optimal growth temperature ~50°C, and the lack of a well-studied genetic background that facilitates exogenous DNA introduction and replication.

In summary, this study revealed conformational changes of the R. castenholzii RC-LH in the presence and absence of KγCext and subunit X, which played a role in regulating the quinone/quinol exchange. KγCext incorporation results in a sealed conformation of the LH ring, whereas Car depletion and absence of the subunit X produces an exposed LH ring with larger opening, which together accelerate the in vitro quinone/quinol exchange of menaquinone-4. These results indicate a correlation between LH-bound Cars and the assembly and quinone/quinol exchange of R. castenholzii RC-LH. Overall, these findings deepen our understanding of the light absorption and photo-reaction mechanisms in prokaryotic photosynthesis and increase the feasibility of applying prokaryotic photosystems in synthetic microbiology approaches.

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
      <td>Strain, strain background (Roseiflexus castenholzii)</td>
      <td>DSM 13941/HLO8</td>
      <td>Hanada et al., 2002</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>N-Dodecyl-β-D-maltoside(β-DDM)</td>
      <td>Anatrace</td>
      <td>D310</td>
      <td>/</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Bacteriochlorophyll a</td>
      <td>Sigma-Aldrich</td>
      <td>B5906</td>
      <td>/</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>γ-Carotene</td>
      <td>Sigma-Aldrich</td>
      <td>54765</td>
      <td>/</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Menaquinone-4</td>
      <td>Sigma-Aldrich</td>
      <td>PHR2271</td>
      <td>/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION 3.1</td>
      <td>Zivanov et al., 2018</td>
      <td>/</td>
      <td>/</td>
    </tr>
  </tbody>
</table>

### Extraction and purification of the RC-LH complexes from R. castenholzii

The R. castenholzii cells (strain DSM 13941/HLO8) were grown anaerobically at 50°C under high (180 μmol m–2 s–1), medium (32 μmol m–2 s–1), and low (2 μmol m–2 s–1) illuminations in a modified PE medium as previously reported (Hanada et al., 2002). To inhibit Car biosynthesis, DPA was added to the medium (12 mg L–1), and the bacteria were cultured under the same conditions as the native bacteria. Growth curves of the native and DPA-treated R. castenholzii cells were monitored with a UV-vis spectrophotometer (Mapada P6, Shanghai), by recording the absorption of cultured cells at 660 nm for every 12 hr. The mean values of the optical density at each time point and the standard deviations of mean (n=3) were calculated.

Isolation and purification of both the nRC-LH and dRC-LH complexes were carried out as described (Collins et al., 2009) with some modifications. The whole membranes (OD = 20 cm−1 measured at 880 nm) in 20 mM Tris-HCl (pH 8.0) were solubilized by 0.45% (wt/vol) β-DDM (Anatrace, USA) at room temperature for 1 hr with gentle stirring and then were ultracentrifuged at 200,000×g for 1 hr. The supernatant was collected and filtered through a 0.22 μm filter and diluted with buffer A (0.04% β-DDM, 50 mM Tris-HCl, pH 8.0), subsequently loaded on an anion exchange chromatography column (HiTrap Q HP, Cytiva, USA) that had been equilibrated with buffer A. The crude RC-LH complex was eluted from the column with 200 mM NaCl in buffer A, and further purified by gel filtration through a Superdex 200 16/600 column, and a Superose 6 Increase 10/300 GL (Cytiva, USA) in buffer B (0.04% β-DDM, 100 mM NaCl, 50 mM Tris-HCl, pH 8.0). The whole preparation procedure was monitored by detecting the absorption spectrum from 250 to 900 nm.

### HPLC-MS analyses of the pigments in RC-LH complexes

Pigment composition was analyzed by HPLC as described (Collins et al., 2009). The RC-LH samples were mixed with acetone/methanol (vol/vol ratio of 7:2) to extract the pigments, followed by centrifugation at 12,000×g for 15 min. Then, the supernatant was filtered through a 0.22 μm filter membrane. The filtrate was injected into a C18 reversed-phase column (4.6 mm×150 mm, 5 μm particle size, Agilent, USA) in a Thermo Fisher Ultimate 3000 separation module equipped with a DAD-3000 Diode Array Detector. The pigments were eluted at a flow rate of 1 mL min–1 using 100% methanol. Pigments were then detected by their absorbance at 462 nm and 772 nm. The commercial BChl a and γ-carotene (Sigma-Aldrich, USA) were used as standards. Pigments were identified based on their absorption spectra, retention times, and further analyzed by LC-MS. LC-MS was equipped with an Agilent 1200 HPLC system (Agilent, Santa Clara, CA. USA) and a Thermo Finnigan LCQDeca XP Max LC/MS system (Thermo Finnigan, Waltham, MA, USA). The condition of HPLC is the same as the above. MS with an atmospheric pressure chemical ionization source was performed as follows: positive mode, source voltage of 2.5 kV, capillary voltage of 46 V, sheath gas flow of 60 arbitrary units, auxiliary/sweep gas flow of 10 arbitrary units, capillary temperature 150°C. The pigments composition was determined as shown in Figure 2—figure supplement 3.

### Cryo-EM

Three μL aliquots of the purified RC-LH (native and Car-depleted) complexes were placed on glow-discharged CryoMatrix R1.2/1.3 300-mesh amorphous alloy film (product no. M024-Au300-R12/13, Zhenjiang Lehua Technology Co. Ltd., China). Each grid was blotted for 3 s at 4°C in 100% humidity, then plunged into liquid ethane with a Mark IV Vitrobot system (Thermo Fisher Scientific, USA).

Data for the nRC-LH complex was collected on a 300 kV Titan Krios electron microscope (Thermo Fisher Scientific, USA) with a K3 direct electron detector (Gatan, USA) in counting mode. A total of 2,836 movies were recorded at a magnification of ×64,000 and a pixel size of 1.08 Å, with a total dose of approximately 50 e− Å–2, and a defocus range between –1.0 and –2.3 μm. Each movie was collected over 2.59 s and dose-fractionated into 40 frames. Data for the dRC-LH complex was recorded on a 300 kV Titan Krios electron microscope with a K3 direct electron detector in counting mode. A nominal magnification of ×81,000 was used for imaging, which yielded a pixel size of 0.893 Å. A total of 3,514 movies were collected with defocus values between –1.1 μm and –1.7 μm. Each movie was dose-fractionated to 40 frames under a total dose of 49.65 e− Å–2 and an exposure time of 2.2 s. Cryo-EM analyses of nRC-LH complexes extracted from cells grown under medium (32 μmol m–2 s–1) and low (2 μmol m–2 s–1) illuminations were summarized in Figure 1—figure supplement 3 and Table 2.

### Image processing

Beam-induced motion correction and exposure weighting were performed by MotionCorr2 (Zheng et al., 2017), and the CTF (contrast transfer function) was estimated using the Gctf program (Zhang, 2016). The automatic particle picking was performed by Gautomatch (developed by K Zhang, https://www.mrc-lmb.cam.ac.uk/kzhang/Gautomatch/) and RELION. All other steps were performed using RELION 3.1 (Zivanov et al., 2018).

For the dataset of nRC-LH complex extracted from cells grown under high illumination (180 μmol m–2 s–1), the templates for automatic particle picking were 2D class averages of manually picked 3,106 particles. In total, 1,625,156 particles were auto-picked from 2,836 micrographs. The picked particles were extracted at 4×4 binning and subjected to two rounds of 2D classification. Good 2D class averages in different orientations were selected to generate the initial model. A subset of 1,041,360 particles at the original pixel size were selected for 3D classification into three classes with the initial model as a reference, and then 372,029 good particles were refined into a 3.7 Å resolution electron density map. Finally, the resultant data refined by per-particle CTF refinement were subjected to 3D refinement and postprocessing to 2.8 Å resolution on the gold-standard FSC (Fourier shell correlation)=0.143 criterion. The image processing of nRC-LH complexes extracted from cells grown under medium (32 μmol m–2 s–1) and low (2 μmol m–2 s–1) illuminations were summarized in Figure 1—figure supplement 3.

For the dataset of dRC-LH complex, a total of 1,081,719 particles were automatically picked from 3,514 micrographs. The picked particles were extracted at 4×4 binning and subjected to three rounds of reference-free 2D classification, resulting in 191,821 particles being left and re-extracted into the original pixel size of 0.893 Å. After 3D classification with three classes of particles, a subset of 84,352 particles was selected for the final refinement and postprocessing. The resolution of the final map was 3.1 Å. The values of the angular distribution of particles from 3D refinement were visualized by ChimeraX (Pettersen et al., 2021). Local resolution was estimated with ResMap (Kucukelbir et al., 2014).

### Model building and refinement

The reported 4.1 Å resolution model of RC-LH complex from R. castenholzii (PDB ID: 5YQ7) (Xin et al., 2018) was fitted into the density map in ChimeraX. Based on the density map, the structural model of the nRC-LH complex, including the amino acids residues, cofactors, lipids, and the newly identified exterior keto-γ-carotene (KγCext and KγC) molecules were manually built and adjusted in Coot (Emsley and Cowtan, 2004). Then, real-space refinement in PHENIX (Adams et al., 2010) was used for model refinement with intra-cofactor and protein-cofactor geometric constraints. The structure of the dRC-LH complex was also manually built using the refined model of nRC-LH as a reference in COOT (Emsley and Cowtan, 2004) and refined using the real-space refinement in PHENIX (Adams et al., 2010). The refinement and model statistics are listed in Table 2.

### Assignment of the subunit X, proteins Y and Z

The cryo-EM map of nRC-LH was used for automated model building in ModelAngelo, a program developed by Prof. Sjors Scheres (https://arxiv.org/abs/2210.00006v1). BLAST search of the deduced amino acid sequences of subunit X generated a hint with hypothetical protein KatS3mg058_1126 (GenBank: GIV99722.1) from Roseiflexus sp., which was denoted by metagenomic analyses of the uncultivated bacteria in Katase hot spring sediment (Kato et al., 2022). However, this polypeptide has not been annotated in the Protein Database of R. castenholzii (strain DSM 13941/HLO8). By searching the genomic DNA of R. castenholzii (strain DSM 13941/HLO8), we eventually identified the coding sequences (CDS: 1,060,366–1,060,464) of subunit X, which shared strictly conserved amino acid sequence with KatS3mg058_1126. The assigned amino acid residues fitted well with the cryo-EM densities as shown in Figure 2H. Assignment of protein Y and Z was performed in same procedure, except that protein Z was also confirmed by PMF analyses shown in Table 1.

### Steady-state and fluorescence spectroscopy

Absorption spectra of the RC-LH complexes were collected at wavelength ranging from 250 to 900 nm using a UV-vis spectrophotometer (Mapada P6, Shanghai). Fluorescence emission and excitation spectra of the nRC-LH and dRC-LH complexes were recorded using a steady-state and time-resolved photoluminescence spectrometer (Edinburgh FLS1000, UK), equipped with a Hamamatsu NIR PMT detector (Hamamatsu Photonics, Japan) and an external adjustable 980 nm continuous-wave laser. The fluorescence excitation spectra were obtained with emissions monitored at 920 nm, and excitation at 470 nm was used for emission spectra.

### Ac oxidation assays

Isolation and purification of endogenous Ac from R. castenholzii was carried out by the methods as described (Wang et al., 2020). Before the oxidation assay, the purified Ac was treated with sodium dithionite to obtain the reduced Ac. Using the reduced Ac (122 μM) as electron donor and varied concentrations of menaquinone-4 (Sigma-Aldrich, USA) as electron acceptor, the reaction was carried out in the presence of nRC-LH or dRC-LH complex (50 nM) in buffer B (0.04% β-DDM, 100 mM NaCl, 50 mM Tris-HCl, pH 8.0). The reaction was initiated by illumination at 180 μmol m–2 s–1, and the absorbance of Ac at 604 nm was recorded by a UV-vis spectrophotometer (Mapada P6, Shanghai) at 2 min intervals for a total of 14 min. The corresponding concentrations of Ac were calculated with extinction coefficient, and linear initial rates from 2 to 14 min were fitted using the Michaelis-Menten model in Prism8. All data were obtained from three replicative experiments, with the mean and standard deviations calculated and plotted.
