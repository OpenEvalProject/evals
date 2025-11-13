# Protein sequences bound to mineral surfaces persist into deep time

## Authors

- Beatrice Demarchi<sup>1</sup> ([ORCID: 0000-0002-8398-4409](https://orcid.org/0000-0002-8398-4409)) †
- Shaun Hall<sup>2</sup>
- Teresa Roncal-Herrero<sup>3</sup>
- Colin L Freeman<sup>2</sup> †
- Jos Woolley<sup>1</sup>
- Molly K Crisp<sup>4</sup>
- Julie Wilson<sup>4</sup>
- Anna Fotakis<sup>6</sup>
- Roman Fischer<sup>7</sup>
- Benedikt M Kessler<sup>7</sup>
- Rosa Rakownikow Jersie-Christensen<sup>8</sup>
- Jesper V Olsen<sup>8</sup>
- James Haile<sup>9</sup>
- Jessica Thomas<sup>6</sup>
- Curtis W Marean<sup>11</sup>
- John Parkington<sup>13</sup>
- Samantha Presslee<sup>1</sup>
- Julia Lee-Thorp<sup>9</sup>
- Peter Ditchfield<sup>9</sup>
- Jacqueline F Hamilton<sup>14</sup>
- Martyn W Ward<sup>14</sup>
- Chunting Michelle Wang<sup>14</sup>
- Marvin D Shaw<sup>14</sup>
- Terry Harrison<sup>15</sup>
- Manuel Domínguez-Rodrigo<sup>16</sup>
- Ross DE MacPhee<sup>17</sup>
- Amandus Kwekason<sup>18</sup>
- Michaela Ecker<sup>9</sup> ([ORCID: 0000-0001-9581-1882](https://orcid.org/0000-0001-9581-1882))
- Liora Kolska Horwitz<sup>19</sup>
- Michael Chazan<sup>20</sup>
- Roland Kröger<sup>3</sup>
- Jane Thomas-Oates<sup>4</sup>
- John H Harding<sup>2</sup> †
- Enrico Cappellini<sup>6</sup>
- Kirsty Penkman<sup>4</sup>
- Matthew J Collins<sup>1</sup> †

### Affiliations

1. BioArCh, Department of Archaeology University of York York United Kingdom
2. Department of Material Science and Engineering University of Sheffield Sheffield United Kingdom
3. Department of Physics University of York York United Kingdom
4. Department of Chemistry University of York York United Kingdom
5. Department of Mathematics University of York York United Kingdom
6. Centre for GeoGenetics, Natural History Museum of Denmark University of Copenhagen Copenhagen Denmark
7. Advanced Proteomics Facility, Target Discovery Institute, Nuffield Department of Medicine University of Oxford Oxford United Kingdom
8. Novo Nordisk Foundation Center for Protein Research, Faculty of Health Sciences University of Copenhagen Copenhagen Denmark
9. Research Laboratory for Archaeology and the History of Art University of Oxford Oxford United Kingdom
10. Molecular Ecology and Fisheries Genetics Laboratory, School of Biological Sciences Bangor University Bangor United Kingdom
11. Institute of Human Origins, SHESC Arizona State University Tempe United States
12. Centre for Coastal Palaeoscience Nelson Mandela Metropolitan University Port Elizabeth South Africa
13. Department of Archaeology University of Cape Town Cape Town South Africa
14. Wolfson Atmospheric Chemistry Laboratories, Department of Chemistry University of York York United Kingdom
15. Center for the Study of Human Origins, Department of Anthropology New York University New York United States
16. Department of Prehistory Complutense University of Madrid Madrid Spain
17. Department of Mammalogy American Museum of Natural History New York United States
18. National Museum of Tanzania Dar es Salaam Tanzania
19. National Natural History Collections, Faculty of Life Sciences The Hebrew University Jerusalem Israel
20. Department of Anthropology University of Toronto Toronto Canada
21. Evolutionary Studies Institute University of the Witwatersrand Braamfontein South Africa
22. Centre of Excellence in Mass Spectrometry, University of York New York United States

† Corresponding author

## Abstract

Proteins persist longer in the fossil record than DNA, but the longevity, survival mechanisms and substrates remain contested. Here, we demonstrate the role of mineral binding in preserving the protein sequence in ostrich (Struthionidae) eggshell, including from the palaeontological sites of Laetoli (3.8 Ma) and Olduvai Gorge (1.3 Ma) in Tanzania. By tracking protein diagenesis back in time we find consistent patterns of preservation, demonstrating authenticity of the surviving sequences. Molecular dynamics simulations of struthiocalcin-1 and -2, the dominant proteins within the eggshell, reveal that distinct domains bind to the mineral surface. It is the domain with the strongest calculated binding energy to the calcite surface that is selectively preserved. Thermal age calculations demonstrate that the Laetoli and Olduvai peptides are 50 times older than any previously authenticated sequence (equivalent to ~16 Ma at a constant 10°C).

## Introduction

### Unknown mechanisms of survival of proteins into deep time

Ancient protein and DNA sequences are revolutionising our understanding of the past, providing information on phylogeny, migration, evolution, domestication and extinction (Hagelberg et al., 2015; Cappellini et al., 2014). However, the absence of data from warm regions and deep time (Wade, 2015) highlights the fragility of these biomolecules and has so far hampered our ability to answer fundamental evolutionary questions, such as resolving the phylogenetic tree of the genus Homo in Africa. The survival of proteins and DNA in tropical environments and in fossils that go back a few million years (Ma) is deemed extremely unlikely and therefore the impact of the 'biomolecular revolution' in palaeontology and palaeoanthropology has so far been relatively limited.

Claims for exceptional preservation in the fossil record have been put forward in a number of studies (Towe and Urbanek, 1972; Bertazzo et al., 2015; Schweitzer et al., 2013; Cleland et al., 2015), but these have not been satisfactorily substantiated. Morphological (Towe and Urbanek, 1972; Bertazzo et al., 2015), immunological (Schweitzer et al., 2013) and spectroscopic (Bertazzo et al., 2015) evidence of preserved tissues in dinosaurs and other fossils seems to be inconsistent with the observed levels of hydrolysis, dehydration and racemization (Penkman et al., 2013) in intracrystalline proteins from the fossil mollusc shell (Sykes et al., 1995) and eggshell (Brooks et al., 1990). The mechanisms that might allow preservation over palaeontological and geological time scales are also poorly understood: crosslinking, organo-metallic complexing, including with iron, compression/confinement (Logan et al., 1991; Schweitzer et al., 2014), and mineral stabilization (Collins et al., 2000) have all been proposed as mechanisms that enhance the survival of ancient biomolecules.

### The role of temperature in accelerating diagenesis

A confounding factor when evaluating the authenticity and antiquity of biomolecular sequences is the geographic area of provenance of the fossils and therefore the combined effect of time and temperature on the extent of degradation. Here we have used kinetic estimates of degradation rates of DNA (Allentoft et al., 2012), collagen in bones (Buckley et al., 2008), and intracrystalline amino acids (Crisp et al., 2013) to normalize their numerical (chronological) ages to thermal age (Wehmiller, 1977) (Figure 1, Figure 1—source data 1, Appendix 1). Thermal age is a measure which enables simple comparison between ancient biomolecular targets by normalising them to an equivalent (thermal) age, allowing all samples to be treated as having experienced a constant temperature of 10°C. Thus samples from cooler sites, which experience slower rates of chemical reaction, will have thermal ages younger than their geochronological age, whilst samples from warmer sites will be thermally ‘older’. Various factors can affect the effective diagenetic temperature experienced by a sample (and therefore impact on its thermal age), from burial depth to seasonal and interglacial / glacial cycles (Wehmiller, 1977; Huang et al., 2000; Eischeid et al., 1995). The greatest absolute ages for recovered DNA (Orlando et al., 2013) (0.7 Ma = 0.08 Ma@10°C) and for protein (Rybczynski, 2013) (3.5 Ma = 0.3 Ma@10°C) sequences are from high latitudes and their survival is consistent with predictions from the kinetic data. Younger samples from more temperate latitudes will have greater thermal ages, yet the oldest of these which has preserved protein (Weybourne Crag: 1.5 Ma = 0.2 Ma@10°C) has a thermal age similar to that of Middle Pleistocene DNA at Sima de los Huesos (0.4 Ma = 0.2 Ma@10°C) (Meyer et al., 2014).

![Figure 1.](https://cdn.elifesciences.org/articles/17092/elife-17092-fig1-v1.jpg)

**Figure 1.:** (A) Sites reporting the oldest DNA and collagen sequences are from high latitude sites compared to ostrich eggshell samples from sites in Africa illustrated in (B) for which the current mean annual air temperatures are much higher. (C) Kinetic estimates of rates of decay for DNA (Lindahl and Nyberg, 1972), collagen (Buckley and Collins, 2011) and ostrich eggshell proteins (Crisp et al., 2013) were used to estimate thermal age assuming a constant 10°C (Figure 1—source data 1; Appendix 1. For Elands Bay Cave and Pinnacle Point the oldest samples are shown). Note log scale on the z-axis: struthiocalcin-1 peptide survival is two orders of magnitude greater than any previously reported sequence, offering scope for the survival of peptide sequences into deep time.

### Aim of the study: understanding protein survival in ostrich eggshell from hot environments

Here we explore the impact of strong protein binding in biominerals and its effect on sequence survival, by targeting ancient ostrich eggshell (Struthio camelus; Struthioniformes), which is abundant in archaeological and palaeontological sites throughout Africa (Materials and methods). Our aim was to elucidate a mechanism of preservation and to set out a rigorous methodology for the authentication of ancient protein sequences. We isolated and characterised the intracrystalline proteins (Figure 2, Figure 2—figure supplement 1, Appendix 2) and tracked their diagenesis back in time to 3.8 Ma ago. Using a systematic approach, we validated the sequences from each of the eggshell samples analysed using amino acid racemization (AAR), organic volatile compounds, ancient DNA and proteomic analyses. All our results are supported by in-depth analysis of patterns of diagenesis in both samples and blanks as well as the evaluation of potential contamination and carry-over.

![Figure 2.](https://cdn.elifesciences.org/articles/17092/elife-17092-fig2-v1.jpg)

**Figure 2.:** (A) Amino acid racemization in ostrich eggshell up to 3.8 Ma old from sites in South Africa and Tanzania. (B) Linear increase of THAA Val D/L values with the log of thermal age. (C) Exponential decrease of the number of identified MS/MS spectra with age (THAA Val D/L). (D) The average hydropathicity of the peptides identified remains stable up to Val D/Ls ~1. Note that Val D/Ls > 1.0 are unexpected and may be due to decomposition processes occurring in the closed system. The intracrystalline proteome composition in modern eggshell does not vary across microstructural layers (Figure 2—figure supplement 1), but patterns of degradation are different between fossil samples and purified proteins degraded at high temperature in the absence of the mineral (Figure 2—figure supplement 2).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/17092/elife-17092-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) modern (left) and fossil (LOT 13898; right) OES: crystalline (1), prismatic (2), cone (3) and organic (4) layers. (B) comparison of total THAA yields in each layer before and after bleaching. (C) comparison between the composition of bleached eggshell powder from the cone, palisade and crystalline layers.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/17092/elife-17092-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A–B) fossil OES: (A) number of unique proteins; (B) mean peptide length (excluding contaminants). (C–E) degradation of purified proteins in water: (C) number of unique proteins identified; (D) number of identified product ion spectra; (E) mean peptide length; (F) average hydropathicity. No peptides were detected in the 120 hr heated sample.

## Results

### Fossil eggshell from Africa, 0–3.8 Ma: provenance and thermal age calculations

Twenty-four eggshell samples were sourced from well-dated sites in South Africa and Tanzania (Figure 1, Table 1): Elands Bay Cave (0.3–16 ka BP, Table 3), Pinnacle Point Caves PP 5/6 and PP 30 (50–80 ka BP and ~150 ka BP, respectively, Table 4), Wonderwerk Cave (1 Ma, Table 5), Olduvai Gorge (1.34 Ma, Table 6) and Laetoli (2.6–4.3 Ma, Table 7). The age and stratigraphy of the oldest fossils, from Laetoli, is well-constrained despite the eggshell fragments being surface finds: their morphology shows no evidence of long-distance transport and the fossil-bearing horizons are well identified within the stratigraphy. The absence of lava flows in stratigraphic proximity also excludes the possibility that these fragments had been exposed to additional heat. The provenance of the fragments from Olduvai Gorge is also secure, as these were found in situ during the excavation of the Bell Korongo site, which overlies directly a volcanic tuff dated by 40Ar/39Ar (Domínguez-Rodrigo et al., 2013).

**Table 1.**
 Summary of archaeological and paleontological eggshell samples analysed in this study. See also Tables 3–7.


<table>
  <thead>
    <tr>
      <th>Site</th>
      <th>Approximate age range (ka)</th>
      <th>Approximate thermal age range (ka@10°C)</th>
      <th>Number of specimens</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Elands Bay Cave</td>
      <td>0.3–16</td>
      <td>0.5–45</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Pinnacle Point 5/6</td>
      <td>50–150</td>
      <td>120–470</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Wonderwerk</td>
      <td>~1000</td>
      <td>~3600</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Olduvai</td>
      <td>~1340</td>
      <td>~16300</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Laetoli</td>
      <td>2600–4300</td>
      <td>8900–20400</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Binding of proteins to the (10.4) calcite surface. The binding energies calculated as (a) mean for the full protein (by minimization, see Appendix 3); (b) for four individual domains within the proteins (by molecular dynamics [ovocleidin]; by minimization [struthiocalcin]); (c) for the four domains treated as peptides (by molecular dynamics, see Appendix 3).


<table>
  <thead>
    <tr>
      <th></th>
      <th>OC-17</th>
      <th>SCA-1</th>
      <th>SCA-2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Charge on the protein</td>
      <td>+7 (balanced by Cl-)</td>
      <td>−11 (balanced by Na+, Ca2+)</td>
      <td>−10 (balanced byCa2+)</td>
    </tr>
    <tr>
      <td>Binding energy (mean): kJ mol−1</td>
      <td></td>
      <td>−197 ± 22</td>
      <td>−142 ± 33</td>
    </tr>
    <tr>
      <td>Binding energy (domains): kJ mol−1</td>
      <td>−422 ± 43</td>
      <td>−423 ± 42 (YHHGEEEEDVWI) −611 ± 44 (YSALDDDDYPKG)</td>
      <td>−255 ± 72 (SDSEEEAGEEVW) −231 ± 68 (ASIHSEEEHQAIV)</td>
    </tr>
    <tr>
      <td>Binding energy (peptides only) kJ mol−1</td>
      <td></td>
      <td>−142 ± 19 (YHHGEEEEDVWI) −219 ± 24 (YSALDDDDYPKG)</td>
      <td>−131 ± 32 (SDSEEEAGEEVW) −122 ± 41 (ASIHSEEEHQAIV)</td>
    </tr>
    <tr>
      <td>Water molecules displaced</td>
      <td>21.3</td>
      <td>20.2</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>Estimated binding free energy: kJ mol−1</td>
      <td>−188 ± 37</td>
      <td>−159 ± 24</td>
      <td>−99 ± 39</td>
    </tr>
    <tr>
      <td>Residence times for water (ps) [average surface bound water molecule = 120 ps]</td>
      <td></td>
      <td>130 ± 3 (YHHGEEEEDVWI) 135 ± 3 (YSALDDDDYPKG)</td>
      <td>124 ± 4 (SDSEEEAGEEVW) 123 ± 5 (ASIHSEEEHQAIV)</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Summary of samples from Elands Bay Cave, South Africa. The stratigraphic layers have been independently dated by radiocarbon. Unpublished uncalibrated dates provided by J. Parkington. Date calibration was performed with OxCal v.4.2 (Ramsey, 2009. Calibration curves: IntCal13 for dates obtained on charcoal; Marine13 for dates obtained on shells/crayfish, DeltaR = 93 ± 28 [Dewar et al., 2012]). Age estimates for undated layers based on estimating the median (mid-point) of two dates obtained on layers bracketing the layer with OES samples.


<table>
  <thead>
    <tr>
      <th>LOT</th>
      <th>NEaar</th>
      <th>Layer</th>
      <th>Age (cal BP) 95.4%</th>
      <th>Material used for 14C dating/notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1868</td>
      <td>6887</td>
      <td>Kaunda</td>
      <td>&lt;323 (estimate)</td>
      <td>Layer above dates on layer NKOM</td>
    </tr>
    <tr>
      <td>1872</td>
      <td>6888</td>
      <td>George Best</td>
      <td>322–1008</td>
      <td>Layer between dates on layers NKOM and EDDI</td>
    </tr>
    <tr>
      <td>1866</td>
      <td>6889</td>
      <td>D. Lamour</td>
      <td>906–2282</td>
      <td>Layer between dates on layers EDDI and LARM</td>
    </tr>
    <tr>
      <td>1849</td>
      <td>6891</td>
      <td>Maroon Robson</td>
      <td>8773 ± 125</td>
      <td>Charcoal</td>
    </tr>
    <tr>
      <td>1850</td>
      <td>6893</td>
      <td>Nero</td>
      <td>8748–10096</td>
      <td>Layer between dates on layers Maroon Robson / Burnt Robeson</td>
    </tr>
    <tr>
      <td>1823</td>
      <td>6896</td>
      <td>Crayfish</td>
      <td>11545 ± 441</td>
      <td>Crayfish</td>
    </tr>
    <tr>
      <td>1819</td>
      <td>6899</td>
      <td>Smoke</td>
      <td>12589 ± 104</td>
      <td>Charcoal</td>
    </tr>
    <tr>
      <td>1840</td>
      <td>6907</td>
      <td>OBS 1</td>
      <td>15208–15940</td>
      <td>Layer between dates on layers Smoke and SOSE</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Sample details for sub-fossil OES analysed for LC-MS/MS; from Pinnacle Point, South Africa. Stratigraphic information and weighted mean OSL age estimates (ka) for PP 5–6 (Karkanas et al., 2015) and PP 30 (Rector and Reed, 2010).


<table>
  <thead>
    <tr>
      <th>Site</th>
      <th>LOT</th>
      <th>NEaar</th>
      <th>Archaeological sample information</th>
      <th>Stratigraphic aggregate</th>
      <th>Age (ka)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PP5-6</td>
      <td>4613</td>
      <td>7676</td>
      <td>Plotted Find 102627, Lot 3151</td>
      <td>RBSR</td>
      <td>51 ± 2</td>
    </tr>
    <tr>
      <td>PP5-6</td>
      <td>4649</td>
      <td>7283</td>
      <td>Plotted Find 165702, Lot 8038</td>
      <td>SGS</td>
      <td>64 ± 3</td>
    </tr>
    <tr>
      <td>PP5-6</td>
      <td>4671</td>
      <td>7316</td>
      <td>Specimen 273467, Lot 3255</td>
      <td>SADBS</td>
      <td>71 ± 3</td>
    </tr>
    <tr>
      <td>PP5-6</td>
      <td>4605</td>
      <td>7198</td>
      <td>Specimen 273489, Lot 3277</td>
      <td>SADBS</td>
      <td>71 ± 3</td>
    </tr>
    <tr>
      <td>PP5-6</td>
      <td>4652</td>
      <td>7286</td>
      <td>Plotted Find 178331, Lot 8172</td>
      <td>ALBS</td>
      <td>72 ± 3</td>
    </tr>
    <tr>
      <td>PP5-6</td>
      <td>4675</td>
      <td>7320</td>
      <td>Specimen 273514, Lot 7980</td>
      <td>LBSR</td>
      <td>81 ± 4</td>
    </tr>
    <tr>
      <td>PP 30</td>
      <td>4683</td>
      <td>7328</td>
      <td>Specimen 66008, Lot 1795</td>
      <td>Single horizon</td>
      <td>~151</td>
    </tr>
    <tr>
      <td>PP 30</td>
      <td>4697</td>
      <td>7342</td>
      <td>Specimen 65168, Lot 1750</td>
      <td>Single horizon</td>
      <td>~151</td>
    </tr>
  </tbody>
</table>

**Table 5.**
 Sample details for sub-fossil OES samples from Wonderwerk Cave, South Africa. Ages based on cosmogenic isotope burial dating and magnetostratigraphy, from Matmon et al. (2012).


<table>
  <thead>
    <tr>
      <th>LOT</th>
      <th>NEaar</th>
      <th>Stratum</th>
      <th>Independent age (Ma)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>14426</td>
      <td>10581</td>
      <td>ME46, SPF#4390, Exc. 1, stratum 10, square Q33, depth 15–20 cm</td>
      <td>1.07–0.99</td>
    </tr>
  </tbody>
</table>

**Table 6.**
 Sample details for fossil OES samples from Olduvai, Tanzania.


<table>
  <thead>
    <tr>
      <th>LOT</th>
      <th>NEaar</th>
      <th>Locality/Stratum</th>
      <th>Independent age (Ma)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>15575</td>
      <td>10955</td>
      <td>Sample BK09-3150</td>
      <td>1.338 ± 0.024</td>
    </tr>
    <tr>
      <td>15578</td>
      <td>10958</td>
      <td>Sample BK10-5309</td>
      <td>1.338 ± 0.024</td>
    </tr>
    <tr>
      <td>15579</td>
      <td>10959</td>
      <td>Sample BK09-2627</td>
      <td>1.338 ± 0.024</td>
    </tr>
    <tr>
      <td>15582</td>
      <td>10962</td>
      <td>Sample BK09-2706</td>
      <td>1.338 ± 0.024</td>
    </tr>
  </tbody>
</table>

**Table 7.**
 Sample details for fossil OES samples from Laetoli, Tanzania. Ages of the strata and localities (40Ar/39Ar) from Deino (2011). LOT 13901 is attributed to Struthio camelus. LOTs 13902 and 13898 are attributed to Struthio kakesiensis (Harrison and Msuya, 2005).


<table>
  <thead>
    <tr>
      <th>LOT</th>
      <th>NEaar</th>
      <th>Locality/Stratum</th>
      <th>Independent age (Ma)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>13901</td>
      <td>10574</td>
      <td>Loc 15, Upper Ndolanya Beds</td>
      <td>~2.66</td>
    </tr>
    <tr>
      <td>13902</td>
      <td>10573</td>
      <td>Loc 10 West, Upper Laetolil Beds</td>
      <td>~3.8–3.85</td>
    </tr>
    <tr>
      <td>13898</td>
      <td>10575</td>
      <td>Kakesio 1−6, Lower Laetolil Beds</td>
      <td>~3.85 -&gt; 4.3</td>
    </tr>
  </tbody>
</table>

The chronological ages of the samples were normalised to thermal ages: the mean annual air temperature (MAT) for each site was estimated from the NOAA NCDC GCPS monthly weather station (Eischeid et al., 1995; Karl et al., 1990) and borehole data (Huang et al., 2000; National Climatic Data Center (NCDC), 2012) (Appendix 1—table 1). Samples on the surface or buried at shallow depth will have experienced an effective temperature which is higher than the MAT, as rates of reaction scale exponentially with temperature (Wehmiller, 1977). The greater the seasonal range at the site, the older the thermal age will be, but the effect of seasonal fluctuations will be mitigated by burial depth, which dampens temperature changes. Holocene sites which today have a MAT of exactly 10°C will have been cooler in the past 500 years due to recent anthropogenic warming. In this study, we used borehole temperature estimates (Huang et al., 2000) or long-term historic records (Eischeid et al., 1995) to counter this effect. Pre-Holocene samples from sites which today have an MAT of 10°C will have an even younger thermal age due to the reduction in temperature during glacial periods. This retards the rate of chemical degradation, and therefore slows the advance of thermal age. While we did not correct for seasonal fluctuation, a correction was applied for altitude. The long-term temperature model of Hansen et al. (2013), scaled to local or regional estimates of present day values and predicted temperature decline at the last glacial maximum (LGM), was used to project MATs from present day to the time of deposition (Appendix 1—tables 1, 2, 4).

Ostrich eggshell protein degradation was compared with the extent of degradation of DNA and bone collagen detected in a variety of Northern Hemisphere sites (Figure 1). Published kinetic parameters for the degradation of the molecules (Appendix 1—table 3; [Crisp et al., 2013; Lindahl and Nyberg, 1972; Holmes et al., 2005]) were used to calculate the relative rate difference over a given interval of the long-term temperature record and to quantify the offset from the reference temperature of 10°C, thus estimating the thermal age in years@10°C for each sample (Figure 1C). It is clear that Northern Hemisphere samples are thermally younger than their chronological age (e.g. Ellesmere Island is ~0.02 Ma@10°C), while the age of the eggshell samples considered here increases, e.g. the 3.8 Ma sample from Laetoli and the 1.34 Ma Olduvai samples are estimated to have thermal ages of ~16 Ma@10°C (Appendix 1—table 4; Figure 1—source data 1). The difference in chronological age between our two oldest sites is therefore minimised by the effect of temperature, which is dampened in Laetoli due to the greater altitude relative to Olduvai.

### Eggshell contains proteins (struthiocalcin-1 and -2) that bind very strongly to the calcite surface: good candidates for long-term survival?

This sample set, spanning the last ~16 Ma@10°C (Table 1), was chosen in order to explore patterns of diagenesis and protein survival using a well-established experimental approach that can isolate the intracrystalline fraction of proteins enclosed in biominerals, including ostrich eggshell (bleaching; Crisp et al., 2013). The intracrystalline fraction of avian eggshell typically contains C-lectins; in ostrich these are struthiocalcin 1 & 2 (SCA-1 & SCA-2) (Mann and Siedler, 2004). The eggshell proteins were characterised in terms of their amino acid composition across microstructural layers (Appendix 2, sections A and B) and the main proteins sequenced and identified (Appendix 2, section C) in modern eggshell, revealing uniform composition across the eggshell layers. Therefore, samples of the archaeological and paleontological eggshell, usually recovered in a fragmentary state, can be considered to be representative of the overall proteome.

The crystallography of SCA-1 (Ruiz-Arellano et al., 2015) reveals a similar overall structure to ovocleidin-17 (OC-17), which has previously been proposed to play a catalytic role in the calcification of chicken eggshell via the positively charged cluster of arginine residues interacting with the carbonates on the (10.4) calcite surface (Freeman et al., 2010). OC-17 is, however, absent in ostrich; instead, SCA-1 and 2 are negatively charged (Table 2) and thus likely to bind to calcium ions.

A molecular dynamics (MD) study of the binding of whole SCA molecules at the mineral surface allowed the strongest binding regions of SCA-1 and SCA-2 to be identified, two for each of the two proteins (Appendix 3). In MD simulations the four peptide sequences that cover the binding regions (Table 2) were moved close to the (10.4) calcite surface from aqueous (bulk) solution to determine their respective binding energies (Appendix 3). All four peptides showed negative binding energies, indicating it was energetically favourable for them to bind to the calcite surface, rather than to remain in solution. SCA-1 bound more strongly than SCA-2 and the binding energies for all four peptides had the same relative order as in the simulations with full proteins. This indicates that the peptides operate as effective proxies for the binding of SCA. The differences between bindings of the different peptides are probably due to the individual amino acids and the primary structure of the peptide enabling favoured binding configurations.

When a molecule binds at the surface there will also be changes in entropy - an entropy loss for the molecule as it becomes bound and an entropy gain as water molecules on the surface are displaced. Given only one molecule binds, compared to the displacement of multiple water molecules, this will be an entropically favourable process. We have previously estimated the entropy associated with the water molecules and use this as a correction to the internal energy to estimate the free energy of binding (Freeman and Harding, 2014). These estimated free energy values (including the influence of water displacement) demonstrate the same trends as the configurational energy, since the number of water molecules displaced in all cases is similar.

The structure of the water close to the interface is also more ordered than bulk water and has lower energy. Thus, when hydrolysis of the bound protein or peptide occurs, it must react with the stabilized water at the interface, not the water in the bulk. This will raise the barrier to hydrolysis and thus promote the survival of the sequence (see also the discussion below). We would therefore expect that the stronger the peptide binding, the more likely the sequence is to survive in the fossil record, as it is best stabilized by its interactions with the mineral surface and must react with stabilized water. The MD simulations thus predict that the YSALDDDDYPKG sequence, with the lowest binding energy (Table 2) will survive the longest.

### Tracking protein breakdown in fossil ostrich eggshell: a multi-analytical approach to validate ancient sequences

For fossil eggshell samples the extent of degradation, quantified by chiral amino acid analysis (AAR), shows that both hydrolysis and racemization increase with time, and that racemic equilibrium is reached in samples older than 1 Ma (~3.6 Ma@10°C; Figure 2; and Appendix 4—table 1 and 2). As degradation proceeds, the complexity of the proteome decreases, until only SCA-1 and SCA-2 are detected by LC-MS/MS in the oldest samples (Supplementary file 1). These two proteins are extremely well preserved in samples up to 150,000 years old, but by 3.8 Ma few peptides are recovered (Figure 3, Figure 3—figure supplement 1 and 2). A total of 22 peptide sequences was recovered from SCA-1 & SCA-2 in samples from Laetoli (Appendix 5, section A; Supplementary file 2), consistent with the idea that dehydration, in addition to mineral binding, may also play a role in retarding degradation of non-binding peptides (Collins and Riley, 2000). However, 80% of the spectra, consistently identified in ten independent LC-MS/MS analyses of three ostrich eggshell samples from Laetoli were assigned to charged species that contained the four Asp residues found in the peptide YSALDDDDYPKG. The survival of this Asp-rich peptide region is not limited to the samples from Laetoli; the eggshells from Olduvai (~16 Ma@10°C) and Wonderwerk (~3.6 Ma@10°C) also show that this region of SCA-1 is preferentially preserved.

![Figure 3.](https://cdn.elifesciences.org/articles/17092/elife-17092-fig3-v1.jpg)

**Figure 3.:** Over time (and increasing THAA Val D/L values) the spectral count decreases as degradation progresses. Blue bars highlight the peptides investigated computationally (represented by the filled atoms in the models). Highly degraded samples (Val D/L ~0.8–1.1) preserve the DDDD-containing peptide. The full time series is shown for SCA-1 in Figure 3—figure supplement 1 and for SCA-2 in Figure 3—figure supplement 2.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/17092/elife-17092-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Spectral count scale: 0–400 for fossil OES; 0–200 for kinetics. Sample 4605 has been recognized as burnt (Crisp, 2013) but excellent sequence preservation is observed. Low spectral counts for sample 4613 are likely due to sample preparation, as AAR did not identify this sample as problematic. Coloured bars show protein structure.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/17092/elife-17092-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Spectral count scale: 0–400 for fossil OES; 0–200 for kinetics. Sample 4605 has been recognized as burnt (Crisp 2013) but excellent sequence preservation is observed. No SCA-2 peptides were found for sample 4613; this is likely due to sample preparation. Wonderwerk and Laetoli samples yielded some peptide sequence, but not consistently.

This peptide does not survive in the absence of the mineral, as shown by the artificial degradation experiments we conducted on purified eggshell proteins heated at 140°C in water (Figure 2—figure supplement 2, Appendix 4, sections B and C). Indeed, the same region of the protein was too flexible to be determined when the crystallographic structure of pure SCA-1 was solved (Ruiz-Arellano et al., 2015). The patterns of degradation of the same proteins heated in water vs after demineralisation of the eggshell mineral also differ significantly from each other. It is noteworthy that the hydropathicity calculated for the surviving peptides decreases in eggshell mineral and increases in water (Figure 2 and Figure 2—figure supplement 2), consistent with the hypothesis that mineral binding plays a crucial role in the survival of selected peptide sequences.

The authenticity of the peptide sequences recovered in the oldest samples was thoroughly assessed (Appendix 5). The amino acid concentration was analysed in all bleached eggshell samples and controls (procedural blanks); concentrations in the blanks were negligible, while the samples retain the original organic fraction within the intracrystalline environment (Figure 4A). In addition, the presence of volatile organic compounds in 2.7 Ma ostrich eggshell demonstrates the stability of ostrich eggshell as a closed system (Appendix 5, Section E). Ratite eggshell has previously proven to be an excellent source of ancient DNA (Oskam et al., 2010) but, unsurprisingly, NGS sequencing failed to recover avian DNA from the Laetoli eggshell we tested (Appendix 5, Section F). Water blanks were injected between each LC-MS/MS eggshell sample analysis to assess carry-over (Figure 4B–F). Despite low levels of SCA-1 being occasionally detected in some of the blanks (Figure 4D), the effective carry-over from sample to sample can be estimated to be below 0.01%. We also stress that each batch of fossil eggshell was analysed separately in time (Figure 4C) and that therefore carry-over between younger and older eggshell samples is impossible. Finally, independent analyses of the results in a second laboratory (Copenhagen) also demonstrated the replicability of our results (Appendix 5, Section A). All peptides and proteins detected in this study presented damage patterns (i.e. diagenesis-induced modifications, such as deamidation, oxidation) that are entirely consistent with the age of the samples (Appendix 5, Section D; Supplementary file 3).

![Figure 4.](https://cdn.elifesciences.org/articles/17092/elife-17092-fig4-v1.jpg)

**Figure 4.:** Amino acid analyses (A): Total concentrations in all eggshell samples (sum of Asx, Glx, Gly, Ala, Val and Ile). Carry-over: (B) Total ion chromatogram for one eggshell sample (EBC_1823) and the blank analysed immediately after (blank_post_EBC1823). (C) Spectral abundance of SCA-1 and SCA-2 in LC-MS/MS blanks. (D) SCA-1 coverage in the blank analysed after a Pinnacle Point eggshell sample PP_4652. Note 'DDDD-' and 'EEEED-' peptides and Asn deamidation. (E) Extracted ion chromatogram for LDDDDYPK in EBC_1823, blank_post_EBC1823 and EBC_1819. (F) Absolute and relative total abundance of 'DDDD' peptides in Laetoli samples/blanks. Signal reduction is at least 100-fold (more often 1000- or 10,000-fold). Independent replication and manual de novo sequencing of the peptides from Laetoli (Appendix 5, section A; Supplementary file 2), consistency of diagenesis-induced modifications (Appendix 5, section D; Supplementary file 3) and volatile organic compound analyses (Appendix 5, section E) were also used to validate the results obtained.

## Discussion

### Surface stabilization is the mechanism for long-term survival of biomineralizing peptides

The breakdown of the proteins and peptides should primarily occur via hydrolysis, involving water and proteins or peptides as reactants. The rate-determining step is the attack of a water molecule (or molecules, see Pan et al., 2011 for an extended discussion). We schematically map out the pathway in Figure 5 (red line) where the reaction coordinate denotes approach of water to the peptide and their subsequent reaction. The process requires energy (heat) to be given to the system in order to overcome the energy barrier. In hot environments, such as Tanzania, the high ambient heat means that many interactions have sufficient energy to overcome this barrier, yet our experimental findings demonstrate that some peptides survive.

![Figure 5.](https://cdn.elifesciences.org/articles/17092/elife-17092-fig5-v1.jpg)

**Figure 5.:** A pictorial representation of the energy barriers associated with the lysis of the peptide. The process in bulk water is depicted in red and the process at the surface is depicted in blue. The surface process shows a larger barrier due to the stabilization of the reactants at the surface.

We argue that the mechanism allowing the survival of the ancient sequences over ~4 Ma (~16 Ma@10°C) at equatorial sites is the stabilization of optimally configured peptides and associated water molecules by surface binding at this interface. The low, negative free energy of binding (Table 2) of the amino acid residues means that they will readily bind to the calcite surface and remain bound indefinitely and this binding stabilizes the peptides by lowering their configurational energy (Table 2). Thus, both the position of the ground state and the top of the barrier will be lowered with respect to the situation when the peptide is in bulk water (Figure 5). The binding of the peptide also forces the hydrolysis reaction to take place with the stabilized water close to the calcite surface.

Furthermore, the presence of the calcite surface significantly stabilizes the water molecules surrounding the peptide. Estimates of the residence times (Table 2) and diffusion values of water molecules trapped between the protein and mineral surface indicate that these water molecules have greater residence times and lower diffusion rates than water molecules on the surface with no protein present. This large stabilization of water molecules selectively lowers the ground state energy of the reactants (protein or peptide plus water) at the interface with respect to the bulk. Thus the energy barrier will be significantly larger for the bound protein or peptide than for the unbound one. Our surface molecules would therefore need more energy in the system (i.e. a higher temperature) to overcome the augmented barrier. The net effect of the binding of the protein or peptide is therefore to retard hydrolysis and prolong peptide sequence survival, albeit of a select (mineral-binding) region of the protein.

Translating this concept to real samples in geological settings, the burial temperature in Tanzania, which may be high enough to allow rapid hydrolytic breakdown of most proteins, would not be enough to hydrolyse mineral bound peptides over corresponding timescales because of their own stabilization but particularly because they are surrounded by the stabilized water. This is effectively equivalent to a localised 'cooling' effect: the water molecules at the calcite surface would therefore be expected to operate as if they were 'cooler' in terms of reactivity and rates of peptide bond hydrolysis.

### Conclusions: biominerals are a source of ancient protein sequences, preserved over geological timescales

The survival of 3.8 Ma old peptide sequences in equatorial Africa corresponds to an estimated thermal age of ~16 Ma@10°C, two orders of magnitude beyond the oldest recovered DNA (Figure 1). We explain this exceptional preservation in terms of surface stabilization of both the peptide and water molecules involved in the hydrolytic breakdown of the peptide. Our discovery identifies mineral-binding proteins as the most likely source of ancient biomolecular sequences in the fossil record.

In this study, we also set out parameters for the authentication of ancient sequences: the combination of the consistency in patterns of protein degradation and survival of particular peptide regions, independent replication of the results and an in-depth analysis of analytical blanks provide overwhelming evidence for the endogeneity and integrity of the peptides recovered. We suggest that all ancient proteomics studies undertake a similar approach to verify the authenticity of the sequences reported.

We anticipate that this study will open up new avenues in palaeontology and palaeoanthropology, for the first time enabling direct comparison between morphological and molecular records of fossils in deep time. Furthermore, the selective preservation of domains associated with biomineralization offers a novel strategy for uncovering functional regions governing mineral formation.

## Materials and methods

### Summary

Ostrich eggshell samples were ground and bleached for 72 hr (NaOCl 12% wt/vol) and rinsed thoroughly before demineralization. Amino acid and mass spectrometry analysis of ancient proteins was conducted using published techniques (Buckley et al., 2009; Crisp et al., 2013). Modifications include the use of trypsin and elastase as digestion enzymes for separate preparations (Welker et al., 2015). Liquid chromatography tandem mass spectrometry (LC-MS/MS) analyses were performed on Thermo Scientific Orbitrap platforms. Resulting spectra were searched against the Struthioniformes genomes using PEAKS (version 7.5 [Ma et al., 2003]). For PEAKS, FDR rate was set at 0.5%, with proteins accepted with −10lgp scores ≥ 40 and ALC (%) ≥ 80. A combination of minimization and conventional MD using the DL_Poly Classic code was used to explore possible protein–calcite binding geometries (Freeman et al., 2011).

### Materials

#### Modern ostrich eggshell (OES)

Modern OES was purchased from Oslinc, an ostrich farm based in Boston, Lincolnshire, UK (www.oslinc.co.uk). The complete shell was less than 1 year old; for the purposes of reproducibility all analyses were performed using the same eggshell. Modern OES was used for the investigation of the amino acid composition of the microstructural layers as well as high-temperature studies on purified proteins (kinetic experiments).

#### Archaeological and palaeontological OES

The details of the archaeological and palaeontological samples included in this study are detailed in Tables 3–7. LOT numbers and individual NEaar (sample) numbers were attributed at the NEaar laboratory, University of York.

### Elands Bay Cave

Elands Bay Cave (EBC) is located on the present coastline about 200 km north of Cape Town (South Africa). Human occupation occurred repeatedly since the terminal Pleistocene. Ostrich eggshell is present throughout the sequence. The site’s chronology has been firmly established through multiple radiocarbon dates; the samples analysed in this study can each be assigned to an age range on the basis of dates obtained on each layer and/or bracketing the OES (Parkington, 1980; Stowe and Sealy, 2016).

### Pinnacle Point

The caves at Pinnacle Point (PP) have been in the spotlight of archaeological research for the past few years, and they have yielded extraordinary evidence for early modern human behaviour as well as detailed palaeoclimatic information (Karkanas et al., 2015; Bar-Matthews et al., 2010; Brown et al., 2009; Marean, 2010; Marean et al., 2007). The OES fragments analysed in this study come from two sites in the PP complex, PP 5–6 and PP 30, and were selected from excavations done up to 2010. PP 5–6 is a well-dated sequence, spanning ca. 50–90 ka. PP 30 is a hyena den (~150 ka BP) and the OES material reflects a single depositional episode.

### Wonderwerk Cave

Wonderwerk Cave (WW) is located in the arid interior of South Africa, near the southern border of the Kalahari Desert. The site has yielded a unique ca. 2 million years long archaeological sequence (Horwitz and Chazan, 2015; Berna et al., 2012). Stratum 10, from which the OES samples analysed here are derived, bears the earliest evidence of intentional use of fire during the Acheulean, constrained to the Jaramillo subchron (1.07–0.99 Ma) based on a combination of paleomagnetic and cosmogenic burial age dating (Horwitz and Chazan, 2015; Berna et al., 2012). The OES fragments from the cave have been used as an effective proxy for refining palaeoclimatic and environmental reconstructions, especially for the early-mid Pleistocene and Holocene levels (Ecker et al., 2015; Lee-Thorp and Ecker, 2015).

### Olduvai

Olduvai Gorge (Tanzania) contains an extensive record of the past two million years of human evolution. The eggshell samples analyzed in the present study were found in situ during the excavation of the BK (Bell Korongo) site located in uppermost Bed II. The site is exceptional by the large amount of ostrich eggshell fragments that were found throughout all its stratigraphic sequence. A volcanic tuff just underlying BK was recently dated to ~1.34 Ma (Domínguez-Rodrigo et al., 2013). The samples analyzed were found in Level 4, which contains a wealth of fossil bones and associated stone tools. This level has been interpreted as a central-place where the butchery of several animal carcasses (including megafaunal remains from Sivatherium and Pelorovis) was carried out (Domínguez-Rodrigo et al., 2014).

### Laetoli

Laetoli (Tanzania) is one of the most famous sites for palaeoanthropologists: it has yielded hominin and other animal remains (Harrison, 2011a, 2011b) and the first unequivocal evidence for bipedalism thanks to the footprints of Australopithecus afarensis preserved in Pliocene volcanic ash, discovered by Mary Leakey in 1976 (Leakey and Hay, 1979).

The eggshell at Laetoli are surface finds, but visual examinations show no evidence of rolling, transportation or weathering (having been exposed on the surface for only a very short period of time after having eroded out of the sediment). As a consequence, there is no likelihood of long-distance transport. The location and preservation of the fossils, the absence of significant spatial displacement of surface finds, the short stratigraphic sections at each collecting spot, and the identification of the fossil-bearing horizons in each of those sections, allow the fossils to be placed quite precisely in their original stratigraphic context. The age and stratigraphy given for each of the samples can be assigned with a high degree of confidence. There are no lava flows in stratigraphic proximity or direct superposition to the stratigraphic units from which the Lower Laetolil and Upper Ndolanya specimens were recovered. Given that more than 40 m of consolidated sediment, and a time difference of 1.5 million years, separate the overlying lava flow (the Ogol Lavas) from the stratum from which the Upper Laetolil fossils were obtained, and that the intervening fossil-bearing beds show no geological evidence of having been impacted by heating, we do not believe that the samples have been exposed to additional heating that would have made them thermally older than we predict (Table 7).

### Methods

#### Bleaching pre-treatment

All analyses reported in this study were conducted on bleached ostrich eggshell (OES) in order to isolate the functionally intra-crystalline proteins. Based on the results of Crisp et al. (2013), powdered eggshell was submerged in NaOCl (12% w/v) for a minimum of 72 hr.

#### Chiral amino acid (AAR) analyses

Sample preparation for chiral amino acid analyses (total hydrolysable and free amino acids fractions: THAA and FAA) was carried out following the method of Crisp et al. (2013). Separation of the chiral forms (D and L) of multiple amino acids was performed by RP-HPLC with fluorescence detection using a modified method of Kaufman and Manley (1998). The amino acids reported here are among those detected routinely with good chromatographic resolution in OES: Asx and Glx (Asp+Asn and Glu +Gln due to irreversible deamidation during sample preparation), alanine (Ala), valine (Val) and isoleucine (Ile). Serine (Ser) is not reported as its decomposition patterns are complicated by decomposition and a reversal in D/L values, therefore its utility decreases for older samples (Vallentyne, 1964; Kimber et al., 1986).

### Proteomics

#### High-temperature experiments: purified proteins from modern OES

Bleached modern OES powders were demineralized in cold dilute acetic acid (10% v/v, 4°C, overnight). The solution was centrifuged at 4500 RPM for 1 hr at 4°C, ultrafiltered (Amicon ultra-filters, 10 kDa) and rinsed repeatedly with ultrapure water. The concentrated proteins were lyophilized and resuspended in ultrapure water. 125 μL of suspension was transferred to four individual sterile hydrolysis vials, each sealed with a clean teflon cap and heated at 140°C for 2, 8, 24 and 120 hr respectively. Alkylation / reduction of disulphide bonds was carried out using dithiothreitol (60°C, 60 min; Sigma Aldrich, St Louis, MO) and iodoacetamide (room temperature, 45 min; Sigma Aldrich). The solutions were then dried down in a centrifugal evaporator to be analysed directly by LC-MS/MS.

#### Protein extraction: archaeological OES (York)

The average sample size for proteomics was 35 mg of OES powder. Two separate preparations were carried out on two subsamples (~17 mg each), for digestion with trypsin ('T') and elastase ('E'). All subsamples were demineralized in cold 0.6 M HCl and the solution neutralized, lyophilized and resuspended in ammonium bicarbonate or Tris-HCl buffer containing the RapiGest SF surfactant (1 mg/mL; Waters Ltd, Hertfordshire, UK), for 'T' and 'E' subsamples, respectively. Following reduction and alkylation of disulphide bonds with DTT and IAA according to the usual protocols, digestion was carried out overnight at 37°C by adding: 4 μL trypsin (0.5 μg/μL; Promega, 2800 Woods Hollow Road Madison, WI 53,711 USA) for 'T' subsamples or 4 μL elastase (1 μg/μL; Worthington, Lakewood, NJ, USA) for 'E' subsamples.

Digestion was stopped by adding trifluoroacetic acid (TFA) to a final concentration of ~0.1% (v/v) and RapiGest™ precipitated by incubating in an acidic environment at 37°C for 30 min. Samples were centrifuged on a bench-top centrifuge (13000 RPM, 30 min) and purified using C18 solid-phase extraction (Pierce zip-tip; Thermo-Fisher) according to the manufacturer’s instructions. Eluted peptides were evaporated to dryness using a centrifugal evaporator before LC-MS/MS analyses.

#### Protein extraction: Laetoli OES (Copenhagen)

The Laetoli eggshell samples (LOT 13901r, 13902r, 13898r), powdered and pre-bleached in York, were sent to the University of Copenhagen for replication. A negative control sample, prepared exactly like the ancient ones except for the initial addition of eggshell powder, was processed and analysed together with the ancient samples, following the same procedure. All samples, including the negative extraction control, were processed in laboratories regularly used for ancient DNA extraction, implementing all the measures necessary to avoid potential contamination from modern biomolecules. All surfaces were UV irradiated overnight, and repeatedly cleaned with bleach and ethanol. In addition, facemasks, nitrile gloves, hairnets and body suits were worn continuously by operators.

An aliquot of 58 mg, 48 mg and 64 mg was weighed from samples 13902r, 13901r and 13898r respectively, and placed in 1.5 mL Protein Lo Bind Tubes (Eppendorf). Subsequently, they were suspended in 1 mL 0.5 M EDTA pH 8.00, mechanically shaken for approximately one minute and incubated overnight under rotation at room temperature. The following day, after centrifugation at 17,000 g for 10 min, the EDTA supernatant was removed and stored in a −18˚C freezer. The demineralisation step with 1 mL 0.5 M EDTA was repeated one more time. The third day, after removal of EDTA supernatant, all demineralised pellets were re-suspended with 100 µL of 0.1 M Tris pH 8.00, mechanically shaken for approximately one minute, and precipitated by centrifugation at 17,000 g for 10 min. The wash step with 100 µL of 0.1 M Tris was repeated two more times.

The samples were then further processed in a guanidinium hydrochloride lysis buffer solution following published methods (Kulak et al., 2014; Jersie-Christensen et al., 2016), without sonication or equivalent steps. Samples were instead mechanically shaken for approximately one minute and a micro-pestle (Eppendorf) was used to manually disrupt the pellet. Ancient samples and negative control were initially diluted to 1:3 in dilution buffer (Kulak et al., 2014), 0.5 µg of rLysC (Promega) were added, and the solution was digested at 37˚C, with mechanical shaking at 900 rpm, for two hours. Samples were then further diluted 1:3 in dilution buffer, 0.5 µg of mass spectrometry grade trypsin (Promega) were added, and the solution was digested overnight at 37˚C, with mechanical shaking at 900 rpm. On the following day, samples were acidified, using 10% trifluoroacetic acid (TFA) in ultrapure water, to reach pH < 2.00, and then centrifuged at 17,000 g for 1 hr. The resulting peptide mixtures in the supernatant fraction were then concentrated using in house created C18 solid phase extraction stage tips as described by Cappellini et al. (2012).

#### LC-MS/MS analysis

##### Oxford TDI

Subsamples digested with trypsin and elastase were combined in a single LC-MS/MS run, with the following exceptions:

Elastase and trypsin-digested samples were analysed by LC-MS/MS as described before (Fischer and Kessler, 2015). Briefly, peptides were separated on a PepMAP C18 column (75 μm × 500 mm, 2 μm particle size, Thermo) using a Dionex Ultimate 3000 UPLC at 250 nL/min and Acetonitrile gradient from 2–35% in 5% DMSO/0.1% formic acid. Peptides were detected with a Q-Exactive mass spectrometer (Thermo) at a resolution of 70000 @ m/z 200 and an ion target value of 3e6 between m/z 380 and 1800. Up to 15 precursors were selected for HCD fragmentation at a resolution of 17,500 with an ion target of 1e5 and a maximal injection time of 128 ms. Normalized collision energy was fixed at 28% and the isolation windows was 1.6 m/z units.

##### Copenhagen

The samples were separated on a 50 cm PicoFrit column (75 μm inner diameter) in-house packed with 1.9 μm C18 beads (Reprosil-AQ Pur, Dr. Maisch) on an EASY-nLC 1000 system connected to a Q-Exactive HF (Thermo Scientific, Bremen, Germany). The peptides were separated with a gradient going from 2% to 25% buffer B in 110 min followed by a 25 min step to 40%. After the gradient the column was washed by going to 60% in 5 min, held for 5 min and re-equilibrated back to 2% for 15 min, resulting in a final acquisition of 165 min. Buffers contained 0.1% TFA dissolved in either 80% acetonitrile for buffer B, or milli-Q water for buffer A. The flow rate was 200 nL/min throughout the gradient and wash.

The Q-Exactive HF was operated in data-dependent top 10 mode. Full scan mass spectra were recorded at a resolution of 120,000 at m/z 200 over the m/z range 300–1750 with a target value of 3e6 and a maximum injection time of 20 ms. HCD-generated product ions were recorded with a maximum ion injection time set to 108 ms through a target value set to 2e5 and recorded at a resolution of 60,000 with a fixed first mass set to m/z 100. Normalized collision energy was 28%. The isolation window was set at 1.3 m/z units and the dynamic exclusion to 30 s.

#### Identification of peptides and proteins

Product ion spectra were analysed using the software PEAKS Studio (v. 7.0, Bioinformatics Solutions Inc. (BSI) [Ma et al., 2003]). Mascot generic format (mgf) files were searched against a reference database containing the genomes of all Struthioniformes and common contaminants (40566 entries), assuming no digestion enzyme and with fragment ion mass tolerance of 0.050 Da and a parent ion tolerance of 5.0 ppm. Results obtained by SPIDER searches (i.e. including all modifications) were used for the investigation of protein survival in OES using the following threshold values for acceptance of high-quality peptides: false discovery rate (FDR) threshold 0.5%, protein scores −10lgP ≥ 40, de novo sequences scores (ALC% ) ≥ 80.

### Volatiles

On crushing or demineralisation of the subfossil OES, a strong odour was emitted from some samples, so analysis of these volatiles was attempted using gas chromatography mass spectrometry (GC-MS). A sealed container was designed that allowed in-line crushing of a sample under N2. Volatiles emitted during crushing of the shells were measured using thermal desorption (Unity, Markes International, Llantrisant, UK) coupled to gas chromatography with a high-resolution quadrupole time of flight mass spectrometer (7200B GC/Q-TOFMS, Agilent Technologies,Wilmington, DE, USA). Volatile organic compounds (VOCs) were flushed from the shell crusher onto the trap using high purity nitrogen at 100 mL min−1 for 10 min. The trap was held at −30°C during sampling, then ballistically heated to 250°C and held for 5 min to ensure complete desorption. The heating of the trap triggered the start of the GC run. A 5% phenyl-polysilphenylene-siloxane capillary column was used (50 m × 0.32 mm × 1 mm BPX5, SGE, Australia) to separate the VOCs. The oven was held at 40°C for 5 min, followed by a ramp rate of 10°C min−1 to a final temperature of 230°C, which was held for 3 min. High purity helium gas was used as the mobile phase at a flow rate of 4.5 ml min−1. The mass spectrometer was operated in an electron ionisation mode at 70 eV and the ion source was at 250°C. Spectra were collected between m/z 35 and 500 at an acquisition rate of 5 spectra s−1. The mass spectra obtained were compared to the NIST MS database (NIST MS Search Program version 2.0) after background correction. A nitrogen blank, sampled through the shell crusher was used to determine the method background and identify unique VOCs emitted from the egg shells. Analysis was undertaken on a fragment of one of the subfossil OES from Laetoli (LOT 13901, ~2.7 Ma).

### Ancient DNA

Two DNA extractions using ~0.05 g of eggshell (sample Laetoli LOT 13902) were made following Dabney et al. (2013) and the extracts combined before the final elution in 25 μL TET.

### Data availability

The data discussed in the paper are archived in the following databases: the mass spectrometry proteomics datasets have been deposited to the ProteomeXchange Consortium via the PRIDE partner repository with the dataset identifier PXD003786; Illumina genetic data have been deposited in the NCBI Short Read Archive (SRA), BioProject ID PRJNA314978; computational modelling data can be found at DOI: 10.15131/shef.data.3491387 (this contains pdb files giving the initial configurations used for SCA-1, SCA-2 and the four peptide sequences and input files for DL_POLY that contain a complete specification of the forcefield used and other setting parameters for the simulations).
