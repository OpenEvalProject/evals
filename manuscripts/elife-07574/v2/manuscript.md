# Mapping the conformational landscape of a dynamic enzyme by multitemperature and XFEL crystallography

## Authors

- Daniel A Keedy<sup>1</sup> ([ORCID: 0000-0002-9184-7586](https://orcid.org/0000-0002-9184-7586))
- Lillian R Kenner<sup>1</sup>
- Matthew Warkentin<sup>2</sup>
- Rahel A Woldeyes<sup>1</sup> ([ORCID: 0000-0003-0737-8383](https://orcid.org/0000-0003-0737-8383))
- Jesse B Hopkins<sup>2</sup>
- Michael C Thompson<sup>1</sup>
- Aaron S Brewster<sup>3</sup>
- Andrew H Van Benschoten<sup>1</sup>
- Elizabeth L Baxter<sup>4</sup>
- Monarin Uervirojnangkoorn<sup>5</sup>
- Scott E McPhillips<sup>4</sup>
- Jinhu Song<sup>4</sup>
- Roberto Alonso-Mori<sup>7</sup>
- James M Holton<sup>3</sup>
- William I Weis<sup>5</sup> ([ORCID: 0000-0002-5583-6150](https://orcid.org/0000-0002-5583-6150))
- Axel T Brunger<sup>5</sup> ([ORCID: 0000-0001-5121-2036](https://orcid.org/0000-0001-5121-2036))
- S Michael Soltis<sup>4</sup> ([ORCID: 0000-0003-4678-2995](https://orcid.org/0000-0003-4678-2995))
- Henrik Lemke<sup>7</sup>
- Ana Gonzalez<sup>4</sup>
- Nicholas K Sauter<sup>3</sup>
- Aina E Cohen<sup>4</sup>
- Henry van den Bedem<sup>4</sup> ([ORCID: 0000-0003-2358-841X](https://orcid.org/0000-0003-2358-841X)) †
- Robert E Thorne<sup>2</sup> †
- James S Fraser<sup>1</sup> ([ORCID: 0000-0002-5080-2859](https://orcid.org/0000-0002-5080-2859)) †

### Affiliations

1. Department of Bioengineering and Therapeutic Sciences University of California, San Francisco San Francisco United States
2. Department of Physics Cornell University Ithaca United States
3. Physical Biosciences Division Lawrence Berkeley National Laboratory Berkeley United States
4. Stanford Synchrotron Radiation Lightsource SLAC National Accelerator Laboratory Menlo Park United States
5. Department of Molecular and Cellular Physiology Stanford University Stanford United States
6. Howard Hughes Medical Institute, Stanford University Stanford United States
7. Linac Coherent Light Source SLAC National Accelerator Laboratory Menlo Park United States
8. Department of Biochemistry and Biophysics University of California, San Francisco San Francisco United States
9. Department of Structural Biology Stanford University Stanford United States
10. Department of Photon Science SLAC National Accelerator Laboratory Menlo Park United States

† Corresponding author

## Abstract

Determining the interconverting conformations of dynamic proteins in atomic detail is a major challenge for structural biology. Conformational heterogeneity in the active site of the dynamic enzyme cyclophilin A (CypA) has been previously linked to its catalytic function, but the extent to which the different conformations of these residues are correlated is unclear. Here we compare the conformational ensembles of CypA by multitemperature synchrotron crystallography and fixed-target X-ray free-electron laser (XFEL) crystallography. The diffraction-before-destruction nature of XFEL experiments provides a radiation-damage-free view of the functionally important alternative conformations of CypA, confirming earlier synchrotron-based results. We monitored the temperature dependences of these alternative conformations with eight synchrotron datasets spanning 100-310 K. Multiconformer models show that many alternative conformations in CypA are populated only at 240 K and above, yet others remain populated or become populated at 180 K and below. These results point to a complex evolution of conformational heterogeneity between 180-–240 K that involves both thermal deactivation and solvent-driven arrest of protein motions in the crystal. The lack of a single shared conformational response to temperature within the dynamic active-site network provides evidence for a conformation shuffling model, in which exchange between rotamer states of a large aromatic ring in the middle of the network shifts the conformational ensemble for the other residues in the network. Together, our multitemperature analyses and XFEL data motivate a new generation of temperature- and time-resolved experiments to structurally characterize the dynamic underpinnings of protein function.

## Introduction

Current structural biology methods provide only incomplete pictures of how proteins interconvert between distinct conformations (Motlagh et al., 2014; van den Bedem and Fraser, 2015). Although X-ray crystallography reveals atomic coordinates with relatively high accuracy and precision, the resulting electron density maps contain contributions from multiple alternative conformations reflecting the ensemble average of 106–1015 copies of the protein in one crystal (Rejto and Freer, 1996; Smith et al., 1986; Woldeyes et al., 2014). At high resolution, it is often possible to detect and discretely model these alternative conformations (Burnley et al., 2012; Davis et al., 2006; Lang et al., 2010; van den Bedem et al., 2009). Structural characterization of alternative conformations by X-ray crystallography can complement NMR (Baldwin and Kay, 2009; Fenwick et al., 2014) and computational simulations (Dror et al., 2012; Ollikainen et al., 2013) in defining the structural basis of protein dynamics and ultimately in linking dynamics to function (Henzler-Wildman and Kern, 2007).

However, more than 95% of crystal structures are determined at cryogenic temperatures (∼100 K) to reduce radiation damage by minimizing diffusion of reactive intermediates and chemical-damage-induced structural relaxations (Garman, 2010; Holton, 2009; Warkentin et al., 2013). Unfortunately, cryocooling can modify main chain and side chain conformational distributions throughout the protein, including at active sites and distal regions important for allosteric function (Fraser et al., 2011; Halle, 2004; Keedy, et al., 2014). Recent studies have instead used room temperature data collection to reveal a multitude of previously ‘hidden’ alternative conformations that are not evident at cryogenic temperatures, many of which have important ramifications for determining molecular mechanisms (Deis et al., 2014; Fraser et al., 2009; Fukuda and Inoue, 2015; van den Bedem et al., 2013).

Between these temperature extremes, protein conformational heterogeneity changes in complex ways. Previous studies using a wide variety of biophysical probes including NMR, X-ray crystallography, and neutron scattering have revealed a change in the character of conformational heterogeneity and/or protein dynamics around 180–220 K (Doster, 2010; Frauenfelder et al., 2009; Lewandowski et al., 2015; Ringe and Petsko, 2003) however, the molecular origins of this ‘glass’ or ‘dynamical’ transition remain incompletely understood. Classic work has examined the temperature dependence of protein conformational heterogeneity across individual X-ray structures determined at temperatures from ∼80 to 320 K (Frauenfelder et al., 1979, 1987; Tilton et al., 1992). These studies used atomic B-factors as a proxy for conformational heterogeneity and identified a global inflection point around 180–220 K. This inflection point was interpreted in terms of a transition driven by dynamical arrest of the coupled hydration layer-protein system (Doster et al., 1989; Frauenfelder et al., 1979, 1987; Tilton et al., 1992). By contrast, solution NMR studies of picosecond–nanosecond (ps–ns) timescale methyl side chain order parameters showed heterogeneous changes in motional amplitudes at temperatures between 288 and 346 K. Thermal deactivation of these motions was suggested to predict a transition near 200 K without invoking solvent arrest (Lee and Wand, 2001). Recent solid-state NMR (ssNMR) experiments suggest that protein motions are coupled to solvent, and that three transitions at ∼195, 220, and 250 K mark the onset of distinct classes of motions as temperature increases (Lewandowski et al., 2015). Unfortunately, these studies used either globally averaged data (as with ssNMR or neutron scattering) or imprecise atomic-level models of conformational heterogeneity (as with B-factors in X-ray crystallography or NMR order parameters), thus preventing an all-atom understanding of the complex temperature response of protein crystals.

New crystallographic and computational techniques now enable a more detailed investigation of the temperature dependence of protein conformational heterogeneity at the atomic level. First, the program Ringer (Lang et al., 2014, 2010) evaluates low-level electron density traditionally considered noise to uncover statistically significant ‘hidden’ alternative conformations, which may become populated or depopulated as a function of temperature. Second, multiconformer models with explicit alternative conformations of both backbone and side chain atoms, as created by manual building or methods such as the program qFit (Keedy et al., 2015, van den Bedem et al., 2009), can account for non-harmonic motions across separate energy wells (encoded by discrete alternative conformations with distinct occupancies and coordinates) and harmonic motions within energy wells (encoded by B-factors). Third, crystallographic order parameters (S2) weigh these harmonic and non-harmonic contributions in a single metric that quantifies the disorder of each residue in a multiconformer model, allowing direct comparison with NMR-determined order parameters (Fenwick et al., 2014). Finally, methodological advances based on the physics of ice formation have enabled variable-temperature crystallographic data collection at temperatures between 300 and 100 K with modest or no use of potentially conformation-perturbing cryoprotectants (Warkentin et al., 2012; Warkentin and Thorne, 2009). Together, these methods overcome many of the limitations of previous X-ray-based approaches and will contribute to an integrated view of how protein conformational heterogeneity and dynamics evolve with temperature.

The human proline isomerase cyclophilin A (CypA) is an excellent model system for deploying these tools to study the structural basis of functional conformational dynamics and, in particular, to use temperature to understand the extent of correlated motions during an enzyme’s catalytic cycle. Previous NMR relaxation data for CypA (Eisenmesser et al., 2005, 2002) indicated a single common exchange process, both in the apo state and during catalysis, for a network of dynamic residues extending from the core to the active site. Room temperature crystallography later suggested the precise alternative conformations that collectively interconvert during catalysis (Fraser et al., 2009). However, subsequent NMR relaxation experiments of mutants designed to perturb the dynamics suggested that multiple exchange processes occur within this network (Schlegel et al., 2009). Here, we analyze multitemperature synchrotron experiments to examine the temperature-dependent conformational heterogeneity of CypA. Additionally, we report X-ray-free electron laser (XFEL) data, which are free of conventional radiation damage (Kern et al., 2014; Spence et al., 2012), to validate previous connections between alternative conformations determined by synchrotron crystallography and NMR experiments performed in solution (Eisenmesser et al., 2005; Fraser et al., 2009). Our analysis shows that the temperature dependence of alternative protein conformations is heterogeneous and that the character of this heterogeneity bridges previous models for protein dynamical transitions. Our results also suggest new ways to use variable temperature with both synchrotron and XFEL crystallography to probe the dynamic underpinnings of protein function.

## Results

### Multitemperature X-ray datasets reveal modulated conformational ensembles of CypA

To probe the conformational landscape of CypA, we collected eight high-resolution (1.34 –1.58 Å) synchrotron crystallographic datasets across a wide range of temperatures from 100 to 310 K (Table 1) with no added cryoprotectants. For each dataset, we initially refined single-conformer models. Although the single-conformer models are very similar to each other, the accompanying electron density maps reveal differences throughout the protein. In the active-site network, the mFo-DFc difference electron density maps are relatively featureless below 200 K, suggesting that a single conformation is a valid fit below this temperature. By contrast, positive and negative mFo-DFc peaks become gradually more prevalent as temperature increases above 200 K, suggesting that multiple conformations are increasingly required to explain the data as temperature increases (Figure 2—figure supplement 1).

**Table 1.**
 Crystallographic statistics for multitemperature synchrotron datasets collected on a single crystal per dataset. Statistics for the highest resolution shell are shown in parentheses.


<table>
  <thead>
    <tr>
      <th></th>
      <th>100 K</th>
      <th>150 K</th>
      <th>180 K</th>
      <th>240 K</th>
      <th>260 K</th>
      <th>280 K</th>
      <th>300 K</th>
      <th>310 K</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PDB ID</td>
      <td>4YUG</td>
      <td>4YUH</td>
      <td>4YUI</td>
      <td>4YUJ</td>
      <td>4YUK</td>
      <td>4YUL</td>
      <td>4YUM</td>
      <td>4YUN</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.9767</td>
      <td>0.9767</td>
      <td>0.9767</td>
      <td>0.9767</td>
      <td>0.9767</td>
      <td>0.9767</td>
      <td>0.9767</td>
      <td>0.9767</td>
    </tr>
    <tr>
      <td>Resolution range (Å)</td>
      <td>33.58–1.48 (1.53–1.48)</td>
      <td>16.95–1.34 (1.39–1.34)</td>
      <td>16.12–1.38 (1.43–1.38)</td>
      <td>34.05–1.42 (1.47–1.42)</td>
      <td>33.98–1.48 (1.53–1.48)</td>
      <td>25.23–1.42 (1.47–1.42)</td>
      <td>22.67–1.5 (1.55–1.50)</td>
      <td>22.66–1.58 (1.64–1.58)</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
    </tr>
    <tr>
      <td>Unit cell (a, b, c)</td>
      <td>42.24, 51.91, 88.06</td>
      <td>42.45, 51.82, 88.01</td>
      <td>42.42, 51.96, 88.21</td>
      <td>43.04, 53.22, 88.63</td>
      <td>43.09, 52.79, 88.81</td>
      <td>43.00, 52.61, 89.12</td>
      <td>43.01, 52.61, 89.32</td>
      <td>42.85, 52.58, 89.41</td>
    </tr>
    <tr>
      <td>Total reflections</td>
      <td>160,129 (15,842)</td>
      <td>160,780 (7,437)</td>
      <td>154,202 (11,295)</td>
      <td>152,578 (13,600)</td>
      <td>134,699 (13,381)</td>
      <td>168,932 (15,019)</td>
      <td>144,734 (14,433)</td>
      <td>125,225 (12,326)</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>32,657 (3,240)</td>
      <td>42,288 (3,471)</td>
      <td>39,548 (3,820)</td>
      <td>38,881 (3,710)</td>
      <td>34,411 (3,391)</td>
      <td>38,763 (3,794)</td>
      <td>32,999 (3,254)</td>
      <td>28,291 (2,760)</td>
    </tr>
    <tr>
      <td>Multiplicity</td>
      <td>4.9 (4.9)</td>
      <td>3.8 (2.1)</td>
      <td>3.9 (3.0)</td>
      <td>3.9 (3.7)</td>
      <td>3.9 (3.9)</td>
      <td>4.4 (4.0)</td>
      <td>4.4 (4.4)</td>
      <td>4.4 (4.5)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>99 (100)</td>
      <td>95 (80)</td>
      <td>97 (95)</td>
      <td>99 (96)</td>
      <td>100 (100)</td>
      <td>100 (100)</td>
      <td>99 (100)</td>
      <td>100 (100)</td>
    </tr>
    <tr>
      <td>Mean I/sigma (I)</td>
      <td>14.07 (1.57)</td>
      <td>25.95 (3.24)</td>
      <td>16.47 (1.64)</td>
      <td>12.86 (1.66)</td>
      <td>10.09 (1.46)</td>
      <td>15.51 (1.52)</td>
      <td>16.90 (1.63)</td>
      <td>13.26 (1.45)</td>
    </tr>
    <tr>
      <td>Wilson B-factor (Å2)</td>
      <td>16.07</td>
      <td>13.12</td>
      <td>16.95</td>
      <td>15.55</td>
      <td>16.06</td>
      <td>17.62</td>
      <td>19.75</td>
      <td>21.44</td>
    </tr>
    <tr>
      <td>R-merge (%)</td>
      <td>6.8 (99.4)</td>
      <td>3.0 (29.4)</td>
      <td>4.2 (71.8)</td>
      <td>6.2 (99.2)</td>
      <td>8.1 (104.3)</td>
      <td>4.9 (100.0)</td>
      <td>4.7 (101.7)</td>
      <td>6.7 (127.3)</td>
    </tr>
    <tr>
      <td>R-measurement (%)</td>
      <td>7.6 (111.0)</td>
      <td>3.4 (36.9)</td>
      <td>4.8 (85.6)</td>
      <td>7.2 (116.8)</td>
      <td>9.4 (120.8)</td>
      <td>5.6 (115.3)</td>
      <td>5.4 (115.9)</td>
      <td>7.6 (144.5)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>1.00 (0.62)</td>
      <td>1.00 (0.90)</td>
      <td>1.00 (0.60)</td>
      <td>1.00 (0.50)</td>
      <td>1.00 (0.52)</td>
      <td>1.00 (0.52)</td>
      <td>1.00 (0.59)</td>
      <td>1.00 (0.56)</td>
    </tr>
    <tr>
      <td>CC*</td>
      <td>1.00 (0.88)</td>
      <td>1.00 (0.97)</td>
      <td>1.00 (0.87)</td>
      <td>1.00 (0.82)</td>
      <td>1.00 (0.83)</td>
      <td>1.00 (0.83)</td>
      <td>1.00 (0.86)</td>
      <td>1.00 (0.85)</td>
    </tr>
    <tr>
      <td>Refinement resolution range (Å)</td>
      <td>33.085–1.48 (1.558–1.48)</td>
      <td>19.117–1.34 (1.394–1.34)</td>
      <td>16.995–1.38 (1.435–1.38)</td>
      <td>34.055–1.42 (1.477–1.42)</td>
      <td>33.98–1.48 (1.547–1.48)</td>
      <td>25.23–1.42 (1.477–1.42)</td>
      <td>22.67–1.5 (1.579–1.5)</td>
      <td>25.2221.58 (1.679 –1.58)</td>
    </tr>
    <tr>
      <td>Reflections used in refinement</td>
      <td>32,627 (4,654)</td>
      <td>42,278 (3,932)</td>
      <td>39,545 (4,265)</td>
      <td>38,879 (4,161)</td>
      <td>34,411 (4,237)</td>
      <td>38,762 (4,256)</td>
      <td>32,999 (4,643)</td>
      <td>28,287 (4,632)</td>
    </tr>
    <tr>
      <td>Reflections used for R-free</td>
      <td>1,028 (147)</td>
      <td>1,325 (125)</td>
      <td>1,238 (133)</td>
      <td>1,218 (130)</td>
      <td>1,080 (133)</td>
      <td>1,217 (133)</td>
      <td>1,036 (145)</td>
      <td>889 (146)</td>
    </tr>
    <tr>
      <td>R-work (%)</td>
      <td>13.3 (20.4)</td>
      <td>12.4 (16.4)</td>
      <td>13.3 (25.4)</td>
      <td>12.6 (26.3)</td>
      <td>13.1 (26.0)</td>
      <td>11.1 (22.6)</td>
      <td>10.8 (20.0)</td>
      <td>11.7 (21.8)</td>
    </tr>
    <tr>
      <td>R-free (%)</td>
      <td>18.3 (26.8)</td>
      <td>15.6 (21.3)</td>
      <td>17.5 (33.0)</td>
      <td>15.6 (30.4)</td>
      <td>16.8 (31.2)</td>
      <td>14.3 (25.5)</td>
      <td>14.4 (24.8)</td>
      <td>15.0 (28.8)</td>
    </tr>
    <tr>
      <td>Number of non-hydrogen atoms</td>
      <td>2,279</td>
      <td>2,433</td>
      <td>1,969</td>
      <td>1,993</td>
      <td>2,035</td>
      <td>2,120</td>
      <td>2,096</td>
      <td>2,172</td>
    </tr>
    <tr>
      <td>Macromolecule atoms</td>
      <td>1,933</td>
      <td>2,132</td>
      <td>1,745</td>
      <td>1,750</td>
      <td>1,837</td>
      <td>1,924</td>
      <td>1,952</td>
      <td>2,061</td>
    </tr>
    <tr>
      <td>Protein residues</td>
      <td>165</td>
      <td>164</td>
      <td>164</td>
      <td>163</td>
      <td>163</td>
      <td>163</td>
      <td>163</td>
      <td>163</td>
    </tr>
    <tr>
      <td>RMS (bonds) (Å)</td>
      <td>0.009</td>
      <td>0.008</td>
      <td>0.008</td>
      <td>0.009</td>
      <td>0.009</td>
      <td>0.008</td>
      <td>0.009</td>
      <td>0.009</td>
    </tr>
    <tr>
      <td>RMS (angles) (°)</td>
      <td>1.16</td>
      <td>1.20</td>
      <td>1.23</td>
      <td>1.20</td>
      <td>1.16</td>
      <td>1.16</td>
      <td>1.14</td>
      <td>1.14</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>97</td>
      <td>94</td>
      <td>97</td>
      <td>96</td>
      <td>97</td>
      <td>96</td>
      <td>97</td>
      <td>96</td>
    </tr>
    <tr>
      <td>Ramachandran allowed (%)</td>
      <td>3.3</td>
      <td>5.7</td>
      <td>2.7</td>
      <td>4.1</td>
      <td>3</td>
      <td>4.2</td>
      <td>3.3</td>
      <td>3.9</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>2.4</td>
      <td>1.3</td>
      <td>0.53</td>
      <td>1.1</td>
      <td>1.5</td>
      <td>1.9</td>
      <td>1.4</td>
      <td>0.88</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>0.57</td>
      <td>1.08</td>
      <td>0.00</td>
      <td>1.24</td>
      <td>0.27</td>
      <td>0.78</td>
      <td>0.52</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Average B-factor (Å2)</td>
      <td>21.74</td>
      <td>17.25</td>
      <td>21.85</td>
      <td>20.14</td>
      <td>20.00</td>
      <td>21.48</td>
      <td>24.09</td>
      <td>25.77</td>
    </tr>
    <tr>
      <td>Macromolecule average B-factor (Å2)</td>
      <td>18.48</td>
      <td>14.67</td>
      <td>19.99</td>
      <td>17.95</td>
      <td>18.17</td>
      <td>19.61</td>
      <td>22.82</td>
      <td>24.94</td>
    </tr>
    <tr>
      <td>Solvent average B-factor (Å2)</td>
      <td>39.99</td>
      <td>35.54</td>
      <td>36.34</td>
      <td>35.89</td>
      <td>37.01</td>
      <td>39.89</td>
      <td>41.23</td>
      <td>41.30</td>
    </tr>
  </tbody>
</table>

_PDB: Protein Data Bank. CC: correlation coefficient._

We monitored the shift from single-conformation to multiple conformations both visually (Figure 1A,B) and using the automated electron density scanning program Ringer (Figure 1C,D). Briefly, Ringer identifies alternative conformations at low levels of electron density by evaluating the density value for the γ atom at each possible position about the χ1 dihedral angle, given a fixed main chain conformation (Lang et al., 2014, 2010). We focused on two residues, Ser99 and Leu98, which are key markers of the conformational exchange by NMR (Eisenmesser et al., 2002, 2005) and were implicated in our previous room-temperature X-ray and mutagenesis experiments (Fraser et al., 2009). For both Ser99 (Figure 1A) and Leu98 (Figure 1B), a dominant peak is evident at all temperatures. The reduced height of this peak as temperature increases is accompanied by the increase in a secondary peak corresponding to the electron density of the minor conformation. To quantify this trend, we computed correlation coefficients between the electron density versus dihedral angle curves for each residue (Figure 1C,D). Pairs of curves for similar temperatures have higher correlations than those for different temperatures. In particular, pairs of curves for temperatures that span the low-temperature (100–180 K) and high-temperature (240–310 K) regimes are more poorly correlated than are curves from the same temperature regime. The dynamical transitions observed in previous studies (Doster, 2010; Lee and Wand, 2001; Lewandowski et al., 2015; Ringe and Petsko, 2003; Schiro et al., 2015) generally occur between these two temperature regimes.

![Figure 1.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig1-v2.jpg)

**Figure 1.:** Ringer curves of 2mFo-DFc electron density versus χ1 dihedral angle for (A) Ser99 and (B) Leu98 show large peaks for modeled major conformations and smaller peaks for additional minor conformations (dashed vertical lines). These secondary peaks become more evident as temperature increases (color gradient from blue to purple to red). A backrub motion was used for Ser99. For (C) Ser99 and (D) Leu98, a Pearson correlation coefficient was calculated between each pair of Ringer curves from the corresponding panel in (A) or (B). Circles in diagonal elements are colored as in (A) or (B); circles in off-diagonal elements are all gray but scaled by pairwise correlation coefficient (see legend). Pairs of curves from similar temperatures are generally more correlated to each other (larger circles) than are pairs of curves from more different temperatures (smaller circles).

![Figure 1—Figure supplement 1.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig1-figsupp1-v2.jpg)

**Figure 1—Figure supplement 1.:** Plots of Rd versus frame-number difference for each dataset in the multitemperature trajectory reveal only minimal radiation damage. The datasets around 180– 260 K exhibit higher Rd in later frames, which may reflect either a time-dependent cryocooling artifact or a radiation damage at these intermediate temperatures. Although the rate of X-ray damage varies strongly with temperature, the data collection strategy was adjusted to yield a comparable amount of damage per frame. Therefore, there is no correlation between data collection temperature and the overall extent of radiation damage; the highest temperature datasets are equally undamaged as the lowest temperature datasets. By contrast, we observe a strong correlation between data collection temperature and conformational heterogeneity.

To ground this conformational redistribution in all-atom detail, we built a multiconformer model with qFit (Keedy et al., 2015; van den Bedem et al., 2009) for each multitemperature dataset. We then finalized the model by manually editing alternative conformations and refining to convergence, resulting in models that were improved relative to the single-conformer models (Table 2, Video 1).

**Table 2.**
 Improvements in validation statistics from finalizing raw qFit models. Statistics calculated with phenix.molprobity.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>RT synchrotron</th>
      <th>XFEL</th>
      <th>100 K</th>
      <th>150 K</th>
      <th>180 K</th>
      <th>240 K</th>
      <th>260 K</th>
      <th>280 K</th>
      <th>300 K</th>
      <th>310 K</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Rfree (%)</td>
      <td>Raw qFit</td>
      <td>16.7</td>
      <td>25.2</td>
      <td>19.0</td>
      <td>16.9</td>
      <td>18.5</td>
      <td>17.5</td>
      <td>17.9</td>
      <td>15.7</td>
      <td>16.3</td>
      <td>16.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Final</td>
      <td>14.6</td>
      <td>24.9</td>
      <td>18.3</td>
      <td>15.6</td>
      <td>17.5</td>
      <td>15.6</td>
      <td>16.8</td>
      <td>14.3</td>
      <td>14.4</td>
      <td>15.0</td>
    </tr>
    <tr>
      <td></td>
      <td>Δ</td>
      <td>–2.1</td>
      <td>–0.3</td>
      <td>–0.7</td>
      <td>–1.3</td>
      <td>–1.0</td>
      <td>–1.9</td>
      <td>–1.1</td>
      <td>–1.4</td>
      <td>–1.9</td>
      <td>–1.1</td>
    </tr>
    <tr>
      <td>MolProbity score</td>
      <td>Raw qFit</td>
      <td>1.47</td>
      <td>1.80</td>
      <td>1.79</td>
      <td>1.31</td>
      <td>1.21</td>
      <td>1.18</td>
      <td>1.45</td>
      <td>1.28</td>
      <td>0.95</td>
      <td>1.19</td>
    </tr>
    <tr>
      <td></td>
      <td>Final</td>
      <td>1.08</td>
      <td>1.39</td>
      <td>1.19</td>
      <td>1.29</td>
      <td>0.63</td>
      <td>1.14</td>
      <td>0.91</td>
      <td>1.25</td>
      <td>0.99</td>
      <td>0.76</td>
    </tr>
    <tr>
      <td></td>
      <td>Δ</td>
      <td>–0.39</td>
      <td>–0.41</td>
      <td>–0.80</td>
      <td>–0.02</td>
      <td>–0.58</td>
      <td>–0.04</td>
      <td>–0.54</td>
      <td>–0.03</td>
      <td>0.04</td>
      <td>–0.43</td>
    </tr>
  </tbody>
</table>

_RT: Room temperature; XFEL: X-ray-free electron laser._

![Video 1.](https://cdn.elifesciences.org/articles/07574/elife-07574-media1.mp4.jpg)

**Video 1.:** For each pair of adjacent temperatures (e.g. 100 and 150 K), the temperature regime between them was bisected and an average 2mFo-DFc electron density map was calculated in reciprocal space using CCP4 utilities, until temperature points were spaced by <1 K. A new multiconformer model is shown when the animation reaches the corresponding temperature.

At 180 K and below, the active-site network is best modeled as a single state, with electron density corresponding to ordered water molecules clearly evident adjacent to Phe113 (Figure 2, top row). At 240 K and above, by contrast, multiple conformations provide a better explanation of the data. Interestingly, some partial-occupancy water molecules are still present and likely co-occur with the major conformations (Figure 2, middle and bottom rows). Met61 appears to populate additional conformations above 180 K, although it is difficult to precisely define changes in its conformational ensemble as temperature increases. This residue bridges Phe113 and the catalytic residue Arg55 via steric contacts between alternative conformations in both directions, emphasizing the importance of modeling multiple conformations in all-atom detail for understanding inter-residue coupling.

![Figure 2.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig2-v2.jpg)

**Figure 2.:** Residues extending from the core to the active site of cyclophilin A (CypA) adopt a single conformer at low temperatures, but gradually transition to increasing occupancy of secondary conformations as temperature increases. These conformations are well supported by 2mFo-DFc electron density contoured at 0.6 σ (cyan mesh) and 3.0 σ (dark blue mesh). This is corroborated by the room-temperature X-ray free-electron laser (XFEL) model (gray), which is free from conventional radiation damage and features the same secondary conformations. Water molecules (red spheres) are more fully ordered at low temperatures, but become only partially occupied at higher temperatures because they are mutually exclusive with the secondary Phe113 conformation.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The CypA dynamic network is shown after molecular replacement and refinement (including automated water placement) in PHENIX, before any manual rebuilding. The major state is well supported by 2mFo-DFc electron density contoured at 0.6σ (cyan mesh) and 3.0σ (dark blue mesh) for all datasets, but mFo-DFc difference electron density becomes more negative for the major state (−3.0σ, red mesh) and more positive for the unmodeled minor state ( 3.0σ, green mesh) as temperature increases across the synchrotron datasets (blue to red), especially at and above 240 K. Full-occupancy water molecules (red spheres) are automatically placed by PHENIX near the Phe113 minor state in lower temperature, but not in higher temperature synchrotron models because they are mutually exclusive with the secondary Phe113 conformation.

### XFEL data confirm conformational heterogeneity in synchrotron data is not due to radiation damage

Quantifying radiation damage versus exposure dose (Figure 1—figure supplement 1) and limiting exposure dose per dataset ensured that the conformational heterogeneity observed in multitemperature synchrotron datasets was not dominated by radiation damage. However, XFELs can generate data that are entirely free from conventional radiation damage by diffraction-before-destruction data collection (Kern et al., 2014; Spence et al., 2012). To compare the distribution of alternative conformations between synchrotron and XFEL data, we collected two ambient-temperature datasets: a 1.75 Å resolution radiation-damage-free dataset using serial femtosecond rotation crystallography (Table 3) (Hirata et al., 2014; Schlichting, 2015; Suga et al., 2015) and an additional 1.2 Å resolution synchrotron dataset (Table 4). For the XFEL experiment, we collected 1,239 individual diffraction images, translating to unique unexposed regions of 71 crystals between each shot (Video 2), and processed them using cctbx.xfel (Hattne et al., 2014) with post-refinement in PRIME (Uervirojnangkoorn et al., 2015). Automated molecular replacement yielded interpretable electron density maps that allowed us to refine a single-conformer structural model with reasonable quality statistics. Electron density sampling analysis using Ringer and multiconformer refinement using qFit were performed as for the multitemperature synchrotron data.

**Table 3.**
 Crystallographic statistics for room-temperature XFEL dataset collected across 71 crystals. Statistics for the highest resolution shell are shown in parentheses.


<table>
  <thead>
    <tr>
      <th></th>
      <th>XFEL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PDB ID</td>
      <td>4YUP</td>
    </tr>
    <tr>
      <td>Resolution range (Å)</td>
      <td>43.98 –1.75 (1.81 –1.75)</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P212121</td>
    </tr>
    <tr>
      <td>Unit cell (a, b, c)</td>
      <td>42.42, 51.82, 87.96</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>19,942 (1894)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>99 (96)</td>
    </tr>
    <tr>
      <td>Wilson B-factor (Å2)</td>
      <td>21.12</td>
    </tr>
    <tr>
      <td>Refinement resolution range (Å)</td>
      <td>43.98 –1.75 (1.93 –1.75)</td>
    </tr>
    <tr>
      <td>Reflections used in refinement</td>
      <td>19,936 (4,811)</td>
    </tr>
    <tr>
      <td>Reflections used for R-free</td>
      <td>625 (151)</td>
    </tr>
    <tr>
      <td>R-work (%)</td>
      <td>20.0 (34.3)</td>
    </tr>
    <tr>
      <td>R-free (%)</td>
      <td>24.9 (36.1)</td>
    </tr>
    <tr>
      <td>Number of non-hydrogen atoms</td>
      <td>1,762</td>
    </tr>
    <tr>
      <td>Macromolecular atoms</td>
      <td>1,559</td>
    </tr>
    <tr>
      <td>Protein residues</td>
      <td>164</td>
    </tr>
    <tr>
      <td>RMS (bonds) (Å)</td>
      <td>0.017</td>
    </tr>
    <tr>
      <td>RMS (angles) (°)</td>
      <td>1.44</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>96</td>
    </tr>
    <tr>
      <td>Ramachandran allowed (%)</td>
      <td>3.6</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>1.92</td>
    </tr>
    <tr>
      <td>Average B-factor (Å2)</td>
      <td>29.03</td>
    </tr>
    <tr>
      <td>Macromolecule average B-factor (Å2)</td>
      <td>26.52</td>
    </tr>
    <tr>
      <td>Solvent average B-factor (Å2)</td>
      <td>48.25</td>
    </tr>
    <tr>
      <td>Number of TLS groups</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

_PDB: Protein Data Bank; TLS: translation libration screw; XFEL: X-ray-free electron laser._

**Table 4.**
 Crystallographic statistics for room-temperature synchrotron dataset collected on a single crystal. Statistics for the highest resolution shell are shown in parentheses.


<table>
  <thead>
    <tr>
      <th></th>
      <th>1.2 Å Synchrotron</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PDB ID</td>
      <td>4YUO</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.9795</td>
    </tr>
    <tr>
      <td>Resolution range (Å)</td>
      <td>44.60 –1.20 (1.24 –1.20)</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P212121</td>
    </tr>
    <tr>
      <td>Unit cell (a, b, c)</td>
      <td>42.9, 52.43, 89.11</td>
    </tr>
    <tr>
      <td>Total reflections</td>
      <td>307,722 (18,999)</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>58,118 (5,122)</td>
    </tr>
    <tr>
      <td>Multiplicity</td>
      <td>5.3 (3.7)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>91 (82)</td>
    </tr>
    <tr>
      <td>Mean I/sigma (I)</td>
      <td>10.99 (5.93)</td>
    </tr>
    <tr>
      <td>Wilson B-factor (Å2)</td>
      <td>15.22</td>
    </tr>
    <tr>
      <td>R-merge (%)</td>
      <td>11.2 (20.4)</td>
    </tr>
    <tr>
      <td>R-measurement (%)</td>
      <td>12.2 (23.4)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>0.99 (0.96)</td>
    </tr>
    <tr>
      <td>CC*</td>
      <td>1.00 (0.99)</td>
    </tr>
    <tr>
      <td>Refinement resolution range (Å)</td>
      <td>45.19 –1.20 (1.23 –1.20)</td>
    </tr>
    <tr>
      <td>Reflections used in refinement</td>
      <td>58,108 (3,657)</td>
    </tr>
    <tr>
      <td>Reflections used for R-free</td>
      <td>2,000 (126)</td>
    </tr>
    <tr>
      <td>R-work (%)</td>
      <td>12.7 (31.3)</td>
    </tr>
    <tr>
      <td>R-free (%)</td>
      <td>14.6 (33.5)</td>
    </tr>
    <tr>
      <td>Number of non-hydrogen atoms</td>
      <td>2327</td>
    </tr>
    <tr>
      <td>Macromolecular atoms</td>
      <td>2143</td>
    </tr>
    <tr>
      <td>Protein residues</td>
      <td>163</td>
    </tr>
    <tr>
      <td>RMS (bonds) (Å)</td>
      <td>0.009</td>
    </tr>
    <tr>
      <td>RMS (angles) (°)</td>
      <td>1.16</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>96</td>
    </tr>
    <tr>
      <td>Ramachandran allowed (%)</td>
      <td>4.1</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>Average B-factor (Å2)</td>
      <td>19.62</td>
    </tr>
    <tr>
      <td>Macromolecule average B-factor (Å2)</td>
      <td>18.40</td>
    </tr>
    <tr>
      <td>Solvent average B-factor (Å2)</td>
      <td>33.86</td>
    </tr>
  </tbody>
</table>

_PDB: Protein Data Bank._

![Video 2.](https://cdn.elifesciences.org/articles/07574/elife-07574-media2.mp4.jpg)

**Video 2.:** Screen capture image of the Blu-Ice GUI showing a video display of a CypA crystal. After each shot, a new damage line appears and the crystal is translated.

In agreement with our previous room-temperature studies (Fraser et al., 2009), the XFEL and synchrotron mFo-DFc difference maps reveal evidence for the rate-limiting alternative conformations extending from the active site into the core of the protein (Figure 3A,B). For example, the backrub-coupled (Davis et al., 2006) rotamer jump of Phe113 is apparent from a large positive mFo-DFc peak in both maps. Alternative conformations for core residue Ser99 are also evident from mFo-DFc peaks (Figure 3A,B) and Ringer electron density sampling curves (Figure 3E). We did not conclusively observe a secondary peak in the electron density sampling curve corresponding to a discrete alternative conformation of Leu98 (Figure 3F), but that is likely due to the lower resolution of the XFEL dataset. Multiconformer models for both datasets (Figure 3C,D) again feature alternative conformations across the active-site network and are strongly supported by 2mFo-DFc electron density. These results provide an important positive control on the observation of conformational heterogeneity in our synchrotron studies by establishing that electron density corresponding to the alternative conformations of CypA is not an artifact of radiation damage. The ability of XFEL crystallography to reveal native and functionally important alternative conformations at high resolution may be especially useful for other systems that are presently intractable for room- or variable-temperature synchrotron crystallography due to the small size of available crystals.

![Figure 3.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig3-v2.jpg)

**Figure 3.:** (A) Electron density maps for room-temperature synchrotron (red) and (B) X-ray-free electron laser (XFEL) (silver) single-conformer models reveal conformational heterogeneity extending from the protein core (Leu98 and Ser99) to the active site (Arg55) of CypA. The primary conformation is well supported by 2mFo-DFc electron density contoured at 0.6 σ (cyan mesh) and 3.0 σ (dark blue mesh). mFo-DFc difference electron density contoured at 3.0 σ (green mesh) and − 3.0 σ (red mesh) suggests unmodeled alternative conformations. (C, D) Finalized multiconformer models explicitly model these alternative conformations, which are well-supported by 2mFo-DFc electron density. (E, F) Ringer electron density sampling for the single-conformer models shows peaks representing alternative conformations for (E) Ser99 and (F) Leu98. The primary conformations of both residues are obvious as peaks for both models, but the minor conformations (dashed vertical line; as modeled in 3k0n) are also evident, with 2mFo-DFc values well above the 0.3σ (darker gray horizontal line) threshold, except for the Leu98 in the XFEL model (due to the lower resolution). A backrub motion of −10° positions the backbone properly for Ringer to best detect the minor conformation for Ser99, but not for Leu98.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** A plot of ‘decay R-factor’ (Rd) as a function of frame-number difference (as in Figure 1—figure supplement 2) has a slope of zero, indicating the absence of radiation damage. Rd is calculated using pairwise observations of unique reflections (hkl) with centroids on frames i and j, and the frame-number difference is given by i-j. The calculations were performed using a 2.0 Å resolution cutoff.

### Some regions feature conformational heterogeneity only at low temperatures

Although more conformational heterogeneity is expected with our higher temperature synchrotron datasets, and is evident in the active site of CypA, cooling can also stabilize new conformations (Halle, 2004). For example, the loop containing residues 79–83 (Figure 4, Video 3) exhibits conformational heterogeneity only at cryogenic temperatures. This region is well fit by a single conformation at 240 K and above, but a secondary loop conformation is necessary to explain the electron density at 100, 150, and 180 K. Additionally, the loop is clearly single-state in the highest resolution (1.2 Å) dataset (Figure 4—figure supplement 1), demonstrating that the slightly lower resolution of the elevated-temperature datasets does not obscure a secondary conformation.

![Figure 4.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig4-v2.jpg)

**Figure 4.:** The surface loop containing residues 79–83 adopts alternative conformations at low temperatures (top row) but not at high temperatures (bottom two rows). The secondary loop conformation is separated from the body of the protein by an ordered water molecule (red sphere); the van der Waals interactions between the loop and the water may reflect an enthalpic stabilization that is more dominant at low temperatures. The electron density peak to the right of the water corresponds to the backbone carbonyl oxygen of Glu81. 2mFo-DFc electron density contoured at 0.6σ (cyan mesh) and 2.0σ (dark blue mesh). XFEL: X-ray-free electron laser.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The surface loop containing residues 79–83 does not adopt alternative conformations in the 1.2 Å synchrotron dataset. 2mFo-DFc electron density contoured at 0.6σ (cyan mesh) and 2.0σ (dark blue mesh).

![Video 3.](https://cdn.elifesciences.org/articles/07574/elife-07574-media3.mp4.jpg)

In the primary conformation, the 79–83 loop is not involved in any main chain–main chain hydrogen bonds to the rest of CypA, suggesting that the barrier to forming the secondary conformation does not involve breakage of cooperative secondary-structure-like interactions. The observation of a secondary state for residues 79–83 at 100–180 K, but not at 240–310 K, suggests that it is enthalpically stabilized at lower temperatures (Halle, 2004; Keedy et al., 2014). Consistent with this mechanism, the secondary conformation of the 79–83 loop is accompanied by an ordered, partial-occupancy water molecule (Figure 4, top row). This water molecule, which is clearly distinct from the carbonyl oxygen of the primary conformation of Glu81, wedges between the loop and the rest of the protein. The surprising appearance of specific solvent-linked protein conformational heterogeneity exclusively below 240 K emphasizes the complex and heterogeneous changes in protein–solvent energetics that can occur at cryogenic temperatures.

### Quantifying temperature-dependent changes in conformational heterogeneity

Despite counter examples such as the 79–83 loop, most residues in CypA, especially in the active site, exhibit increases in discrete conformational heterogeneity above 180 K. To quantify these changes in regions implicated by NMR relaxation experiments, we measured the 2mFo-DFc electron density in the volumes occupied by the alternative conformations of Ser99 and Phe113. By contrast, B-factors, which can model the harmonic motions near any single conformation, are poor proxies for the non-harmonic change between discretely separated conformations. To quantify the change in minor state occupancy as a function of temperature, we summed the electron density in the volume that is occupied exclusively by the minor conformation and avoided any voxels that overlap with the van der Waals radii of atoms of the major conformation (Figure 5A). The resulting curves of minor-state electron density versus temperature have a shallow slope at 180 K and below, but a much steeper slope at 240 K and above (Figure 5B,C). Additionally, the electron density for the XFEL data is consistent with the data collection temperature (273 K) and the overall trends.

![Figure 5.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig5-v2.jpg)

**Figure 5.:** (A) 2mFo-DFc electron density was summed over the volume occupied by the minor conformation but not the major conformation (blue grid points) for Ser99 and Phe113. (B,C) Minor-state 2mFo-DFc electron density increases with temperature. Electron density sums were normalized for each residue. Multitemperature points from synchrotron data are shown in colors corresponding to temperature. The X-ray-free electron laser point is shown as a gray triangle. Best-fit lines are shown for 180 K and below (blue) versus 240 K and above (red).

However, most residues that populate alternative conformations do not have such easily characterized and separable regions of electron density. To quantify how conformational heterogeneity throughout CypA varies as a function of temperature, we used B-factor-dependent crystallographic order parameters (S2) (Fenwick et al., 2014). These order parameters include both harmonic contributions, which reflect conformational heterogeneity near one conformation (encoded by B-factors), and non-harmonic contributions, which reflect conformational heterogeneity between multiple discretely separated conformations (encoded by occupancies and displacements in coordinates). Importantly, these order parameters account for both conformational heterogeneity within energy wells, whether it is modeled by B-factors or by subtly different alternative conformations, as well as discretely separated alternative conformations that occupy distinct rotamers. Similar to the 2mFo-DFc electron density integration results for Phe113, we observed a large change in χ1 bond order parameters at 240 K and above (Figure 6A).

![Figure 6.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig6-v2.jpg)

**Figure 6.:** (A) The complement of B-factor-influenced side chain order parameter for the bond most closely associated with the χ1 dihedral angle for Phe113. Lines reflect least-squares fits to synchrotron models at 180 K and below (blue) versus 240 K and above (red). Multitemperature synchrotron points in colors; X-ray-free electron laser (XFEL) point (not included in fits) as gray triangle. (B) Distribution of the intersection temperature between the <200 and >200 K lines fitted with kernel density function. The peak is near 250 K, although there is a tail toward lower temperatures. Intersection temperatures were <170 K for four residues and >330 K for five residues. (C) Predicted and observed values for the complement of side chain order parameter, averaged over all residues in CypA. The predicted values were obtained by extrapolating each residue’s fit line for 240 K and above (red curve) or for the full 100–300 K (purple curve), flooring the result to 0, then averaging across all residues in CypA. Observed values, similarly floored and averaged, are shown as points.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** The complement of B-factor-influenced side chain order parameter for the bond most closely associated with the χ1 dihedral angle for all residues in CypA. Lines reflect least-squares fits to synchrotron models for 180 K and below (blue) versus 240 K and above (red).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Several residues with high 1 – S2 values (Val2, Glu15, Gly80, Glu81, Lys82, Pro105, Ala117, Glu120, Lys125, Met142, Ser147, and Lys151) are shown for the central molecule (blue-to-red sticks and backbone) and also in symmetry mates (green sticks, gray backbone). Many of these residues appear to interact with each other via lattice contacts. Frustration in these interactions may lead to persistent disorder.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** Each panel is as in Figure 6 , but the order parameter now models the final heavy-atom to heavy-atom bond for each side chain (see ‘Methods’).

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig6-figsupp4-v2.jpg)

**Figure 6—figure supplement 4.:** The small multiple plots are as in Figure 6—figure supplement 1 , but the order parameter now models the final heavy-atom to heavy-atom bond for each side chain (see ‘Methods’).

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig6-figsupp5-v2.jpg)

**Figure 6—figure supplement 5.:** Fit lines for temperature points at 240 K and above were used to extrapolate to the maximal-order temperature, at which 1 − S2 = 0. (A) Order parameter modeling the bond most closely associated with the χ1 dihedral angle. (B) Order parameter modeling the final heavy-atom to heavy-atom bond for each side chain.

![Figure 6—figure supplement 6.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig6-figsupp6-v2.jpg)

**Figure 6—figure supplement 6.:** (A– D) Contributions to χ1 order parameter versus temperature for four representative residues in CypA. Ser99 and Phe113 are in the active-site network, Glu81 is surface-exposed and adopts alternative conformations at all temperatures (Figure 4), and Phe8 is buried in the protein core and is single-rotamer at all temperatures. Similar conformations within the same rotameric well were grouped together for this analysis. (A) Occupancy of minor alternative conformations. (B) Intra-residue heavy-atom-average B-factor. (C) Complement of the S2ang component of the χ1 order parameter, which uses occupancy-weighted angles between bond vectors across alternative conformations. (D) Complement of the S2ortho component of the χ1 order parameter, which uses occupancy-weighted B-factors. Placement of XFEL points and coloring as in Figure 6A .

![Figure 6—figure supplement 7.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig6-figsupp7-v2.jpg)

**Figure 6—figure supplement 7.:** Points indicate observed values for the complement of side chain order parameters, floored at 0 and then averaged over all residues in CypA, as in Figure 6 . The blue and red lines represent fits to the ≤180 K and ≥240 K floored and averaged points, respectively. The fits to these globally averaged data suggest a transition at ∼250 K, even though the underlying heterogeneity of the individual residue responses does not indicate there is a transition near this temperature.

### Mapping the transitions in CypA conformational heterogeneity

Next, we applied the order parameter analysis to all side chain χ1 angles in CypA. Although conformational heterogeneity generally increases with temperature throughout the enzyme, we observed a diverse set of conformational responses (Figure 6—figure supplement 1). The trends for the majority of residues suggested a transition somewhere between our data points at 180 and 240 K, below which the change in conformational heterogeneity with temperature is reduced. To quantify this trend, we performed separate fits for the low-temperature (≤180 K) and high-temperature (≥240 K) data points for all residues. The slopes of conformational heterogeneity (1 – S2) versus temperature were significantly different (p=1 × 10–62, paired T-test) on either side of this transition range: the average slope for the low-temperature fit lines (2.5 × 10–4 K–1) was an order of magnitude smaller than for the high-temperature fit lines (2.6 × 10–3 K–1). This is consistent with the idea that heterogeneity is much less dependent on temperature below the 180–240 K ‘transition’ range.

However, some residues behaved differently from the rest of the protein. Val2 retains its conformational heterogeneity at all temperatures, which is expected based on its weakly constrained position at the N terminus. Many of the remaining outlier residues (Glu15, Glu81, Pro105, Ala117, Glu120, Lys125, Met142, Ser147, Lys151) appear to be involved in a spatially contiguous set of crystal contacts across symmetry mates in the context of the crystal lattice (Figure 6—figure supplement 2). This cluster includes Glu81, which adopts alternative backbone conformations only at low temperatures (Figure 4). The variability of these residues can likely be explained by distinct sets of conformations across crystal contacts that are differentially, but somewhat stochastically, favored during the cooling process (Alcorn and Juers, 2010).

Our data suggest that CypA does not undergo a single global transition from having strongly temperature-dependent changes in side chain conformational heterogeneity to relatively temperature-independent behavior. An ‘intersection’ or ‘transition’ temperature for each bond angle can be estimated from the intersection of the low-temperature and high-temperature fit lines of 1 – S2 versus temperature. The distribution of these intersection temperatures is broad and asymmetrical, with an elongated tail from the peak near 250 K toward 200 K (Figure 6B). Furthermore, the distribution of intersection temperatures is more complex for order parameters reporting on the terminal heavy-atom bond of the side chain than for χ1 (Figure 6—figure supplement 3,4). This increase likely occurs because side chain end orientations are subject to more degrees of freedom and therefore temperature changes may redistribute them in a greater variety of ways.

### Distinguishing between models of protein heterogeneity as a function of temperature

Our data provide insight into models for the origin of the temperature dependence of protein conformational heterogeneity and into proposed dynamical transitions. In one model, deactivation of different internal protein motions at high temperatures (near 300 K) is sufficient to predict a dynamical transition near 200 K (Lee and Wand, 2001). In a second model, solvent-coupled arrest of protein motions produces a transition in a similar temperature range (Ringe and Petsko, 2003). To distinguish between these two models, we analyzed the average side chain disorder across all residues in CypA, focusing on the bond most closely associated with the χ1 dihedral angle, at each of the eight temperatures we studied (Figure 6C). These averaged disorder values drop as temperature is decreased from 310 K, then flatten out somewhere between 240 and 180 K, with some scatter due to the variability in the cryocooling process (data points in Figure 6C and Figure 6—figure supplement 7).

Next, we used two different linear fits to extrapolate 1 – S2 across all temperatures for each residue, floored the result at maximum order (1 – S2 = 0), and then averaged across all residues to obtain predictions for the residue-averaged disorder versus temperature. In the first fit, the linear function was fit to data for each residue at all temperatures. Consistent with the necessity of using separate fit lines for the low-temperature and high-temperature data (Figure 5 and Figure 6—figure supplement 1), the resulting prediction gives a poor account of the averaged experimental data and does not indicate a transition (purple line in Figure 6C). In the second fit, only the high-temperature (240 K and above) data for each residue were fit. The resulting prediction is more consistent with the averaged high-temperature experimental data and does indicate a transition (red line in Figure 6C). The flattening of this predicted curve at low temperatures occurs as more individual residues achieve maximal predicted order (S2→1) (Figure 6—figure supplement 5). This latter prediction, which is extrapolated from high-temperature crystallographic data, is reminiscent of predictions based on NMR relaxation experiments conducted at 288–346 K (Lee and Wand, 2001). Our observations are consistent with the idea that thermal depopulation of protein alternative conformations is sufficient to predict the existence of an average inflection without invoking a transition of the solvent. However, the low temperature of the predicted inflection (∼100 K), as well as the large separation in low-temperature disorder between our experimental data (data points in Figure 6C) and predictions from high temperature (red line in Figure 6C), suggest that thermal depopulation of protein alternative conformations cannot by itself account for the observed ∼200 K transition. This large separation also indicates that data collected at high temperatures (>260 K) cannot be reliably extrapolated to predict conformational heterogeneity at low temperatures. It also follows that data from low temperatures (≤180 K) cannot be simply extrapolated to predict the features of the energy landscape that may be important above ∼200 K.

Many effects may contribute to the discrepancy between the observed data and the behavior projected from the high-temperature fits. To gain additional insight into this discrepancy, we decomposed the order parameters into their B-factor versus discrete-conformers components and examined their temperature dependences (Figure 6—figure supplement 6). Roughly 67% of residues (e.g. Phe8) remain within one rotamer well across all temperatures. Approximately 13% of residues (e.g. Ser99 and Phe113) populate clearly separable multiple rotameric states at high temperatures, and then show complete depopulation of minority states on cooling so that only a single rotameric state remains at 180 K and below. However, 6% of residues (e.g. Thr5) continue to populate multiple rotameric states at or below 180 K. An additional 6% of residues (e.g. Lys91) populate new rotameric states only at or below 180 K. These results help explain the excess residual disorder in our experimental structures below 240 K compared to projections based on high-temperature fits. Although slopes of crystallographic B-factors with temperature remain nearly flat below 240 K (Figure 6—figure supplement 6B), we expect that true harmonic thermal disorder does subtly decrease from 180 to 100 K; these thermal effects could be more detectable if even higher resolution data were collected at even lower temperatures, perhaps by using liquid helium as a cryogen to cool to ∼15 K or below (Chinte et al., 2007).

### Imperfect coupling between active- site residues in CypA

While the results above show a variety of thermal and non-thermal conformational responses, it remains unclear whether these responses involve coupled conformational shifts of multiple residues. In particular, the network of alternative side chain conformations spreading from the core of the protein (Ser99) into the active site (Arg55) across multiple β-strands exhibits qualitatively similar behavior of increasing occupancy above 240 K. In previous work (Fraser et al., 2009), the collective presence of these alternative conformations at room temperature, but not at cryogenic temperatures, and the close contacts between these residues had suggested a concordance with the single exchange process fit by NMR relaxation dispersion for this dynamic active-site network. However, using our new multitemperature data, this network appears subdivided based on the apparent intersection or transition temperatures of the constituent residues, with Ser99 and Phe113 behaving most similarly to each other (Figure 7, Video 4).

![Figure 7.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig7-v2.jpg)

**Figure 7.:** Intersection temperatures from (A) χ1 order parameters as in Figure 6B or (B) side chain terminus order parameters as in Figure 6—figure supplement 3 B are mapped to the 1.2 Å room-temperature synchrotron model. Each residue is marked with a sphere colored based on its apparent transition temperature, from low (blue) to high (red). The active-site network is subdivided: Ser99 and Phe113 (left of boxed region) both transition at a low temperature regardless of order parameter bond vector, but Met61 and Arg55 transition at higher, different temperatures.

![Video 4.](https://cdn.elifesciences.org/articles/07574/elife-07574-media4.mp4.jpg)

## Discussion

Here, we have mapped the conformational landscape of the dynamic enzyme CypA by analyzing multiconformer models from multitemperature crystallography. Unlike previous temperature-dependent analyses of X-ray crystallography, here we consider both harmonic disorder (B-factors) and non-harmonic displacements (alternative conformations and occupancies), characterized using crystallographic bond order parameters. We have four primary findings:

Our results provide new insight into the relationship between energy landscapes, the glass transition, and protein function. Glasses and other disordered systems have complex energy landscapes, in part due to the large number of microenvironments and the extensive frustration that disorder generates in the intermolecular interactions. Proteins at biological temperatures are ‘glassy’ in this sense—they have complex energy landscapes, due to their large size, heterogeneous amino acid composition, and many degrees of conformational freedom (Frauenfelder et al., 1991). The extensive heterogeneity in the temperature response of individual residues in CypA that we observe here provides additional direct evidence for this underlying energetic heterogeneity.

In addition to the inherent ‘glassiness’ of proteins at biological temperatures, dynamical transitions, some of which have been called ‘glass transitions’, have been reported at lower temperatures, including 180, 200, 220, 240, and 250 K, based on Mössbauer spectroscopy, X-ray crystallography, liquid and solid-state NMR, neutron scattering, and other techniques (Lewandowski et al., 2015; Schiro et al., 2015). These transitions typically manifest as a change in slope of some measurement in the vicinity of the suggested transition temperature. However, many of these measurements are sensitive to motions only within some timescale window (often ps-ns), monitor only a subset of amino acid types, and/or spatially average over all residues in the protein. By contrast, multitemperature crystallography with multiconformer models has many advantages by providing a time-independent and fully site-resolved measurement of ensemble-averaged atomic displacements, including both harmonic and discrete conformational heterogeneity, within the crystal.

This combined methodology lets us examine dynamical and glass transitions in protein crystals from a new perspective. Glass transitions are by definition non-equilibrium phenomena that arise when the kinetics of relaxation toward equilibrium slow so dramatically that equilibrium cannot be reached on experimental timescales. One signature of a true glass transition in proteins would be if occupancies of minority alternative conformations were arrested at non-zero values below some temperature. Indeed, here we see no appreciable temperature evolution of individual conformer occupancies or B-factors at 180 K and below, and the average disorder at these temperatures is far in excess of what is predicted from high-temperature extrapolations. These observations are consistent with the falling out of equilibrium expected in a glass transition, but not with a transition driven by the thermal freeze-out of alternative side chain conformations (Lee and Wand, 2001). Moreover, the persistence of multiple rotameric states at low temperatures is consistent with solvent arrest that impedes further changes in side chain disorder. Although the details of protein–solvent interactions may differ in crystals versus in solution, local variability at different protein–solvent interface microenvironments in the crystal (Teeter et al., 2001) likely contributes to the heterogeneity of temperature responses that we observe. The critical importance of site resolution is evident in the results of Figure 6. Averaging over side chain disorder in all residues yields an apparent transition near 250 K (Figure 6 and Figure 6—figure supplement 7). Perhaps coincidentally, this same temperature has been associated with a transition for protein side chains in site-averaged solid-state NMR measurements (Lewandowski et al., 2015). However, the ‘transition’ in our residue-averaged result obscures the highly heterogeneous temperature dependence of the individual side chains. We find no evidence of tight cooperativity or of a collective global response near 250 K that would be expected in the case of a ‘true’ dynamical transition. Instead, our data are consistent with local, non-cooperative freeze-out of conformational states defined by the energy landscape over a broad temperature range.

The heterogeneous response of side chain order parameters to temperature is driven largely by the changes to the populations of alternative conformations, which ‘flat-line’ at different temperatures across CypA. This diversity of ‘flat-lining’ temperatures is present even within the dynamic active-site network, even though the constituent residues have similar occupancies for their major and minor states at high temperatures (Figure 7). This result contrasts with previous NMR and X-ray experiments that hypothesized correlated motions of this network as rate-limiting for the catalytic cycle (Eisenmesser et al., 2005; Fraser et al., 2009) (Figure 8A).

![Figure 8.](https://cdn.elifesciences.org/articles/07574/elife-07574-fig8-v2.jpg)

**Figure 8.:** (A) The previous simple model in which Ser99, Phe113, and Arg55 (Met61 omitted for clarity) interconvert from one macrostate (blue) to the other (red) completely collectively. NMR data suggest this process occurs on a millisecond timescale. (B) A more nuanced model in which network microstates are populated differently depending on the network macrostate, defined by the Phe113 rotameric state. In the left macrostate, Ser99 rotamer changes are disfavored because of steric overlaps with Phe113, but Arg55 rotamer changes are accommodated; the reverse is true (perhaps to a lesser extent) in the right macrostate. Within each microstate, rapid thermal motions occur (bottom right), and may alleviate some minor steric overlaps. Timescales are estimates consistent with NMR observables for CypA and other systems. ms: millisecond; ns: nanosecond; ps: picosecond.

To bridge these views, we propose that the active-site network adopts two substates, which are primarily distinguished by Phe113 rotamer interconversion. Each of these substates adopts a differently weighted ensemble of conformations for other residues (Figure 8B). In this model, Met61 and Arg55 can switch rotamers more easily than Ser99 when Phe113 is in its χ1 gauche (p) rotamer pointed toward Ser99, whereas Ser99 can switch rotamers more easily than Met61 and Arg55 when Phe113 is in its χ1 gauche (m) rotamer pointed toward Met61. Additionally, thermal ‘breathing’ motions within rotameric wells may relieve minor steric overlaps within some of these macro- and microstates (Figure 8B , bottom right). This model is consistent with Phe113 having the lowest ‘flat-lining’ temperature of the network (Figure 7), and makes sense sterically because of the large size of the aromatic ring. These hypothesized motions are consistent with the timescales and temperature dependencies of motion assigned by solid-state NMR studies of crystalline protein GB1 (Lewandowski et al., 2015). Furthermore, the model helps explain the difficulty of fitting NMR relaxation data for perturbed versions of the active-site network as a single collective exchange process (Schlegel et al., 2009). The aromatic ring of Phe113 could play a dominant role in determining the chemical shift changes of the surrounding residues. Each of these residues could also populate multiple rotamers in the excited state measured by NMR. Our hierarchical perspective evokes the ‘population shuffling’ model of (Smith et al., 2015), in which a protein macrostate (in CypA, defined by the Phe113 rotamer) also determines the different relative populations of rotamers for a subset of other residues (in CypA, the other residues in the active-site network). In this model, the interconversion between macrostates, and not the collective motion of all residues between distinct rotamers, is correlated with the rate-limiting step of the CypA catalytic cycle.

Diversity in the temperature dependences of alternative conformations as we see here is inevitable given the limitations of the amino acid alphabet, yet its spatial pattern within a protein may provide insight into selective pressures. Evolutionary optimization must ensure that functionally important alternative conformations are robustly populated and interconvert appreciably at physiological conditions. However, the energy landscapes of individual residues are coupled to varying extents, such that some subsets of residues must be collectively optimized to preserve some, but not perfect, collectivity in functional motions. For proteins with large sequence alignments, evolutionary covariation has been used to predict ‘sectors’ of functionally cooperative residues, which are often dispersed in primary sequence but strikingly contiguous in tertiary structure (Halabi et al., 2009). By contrast, temperature-dependent crystallography has the potential to unveil couplings in atomic detail by identifying sets of residues whose conformational ensembles respond concertedly to temperature change. Based on our results with CypA, we expect this coupling to be weak, but measurable. Serial femtosecond XFEL crystallography combined with ultra-fast temperature jumps could enable a temporal view of these coupled conformational changes. Novel static and time-resolved multitemperature crystallographic approaches will provide powerful tools for resolving concerted motions to explore how proteins function and evolve.

## Materials and methods

### Protein expression, purification, and crystallization

Wild-type CypA was produced and crystallized as previously reported (Fraser et al., 2009). Briefly, crystals were grown by mixing equal volumes of well solution (100 mM (4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid) HEPES pH 7.5, 23% PEG 3350, 5 mM Tris (2-carboxymethyl) phosphine [TCEP]) and protein (60 mg mL –1 in 20 mM HEPES pH 7.5, 100 mM NaCl, 0.5 mM TCEP) in the hanging-drop format.

### Crystallographic data collection

For the multitemperature synchrotron datasets at 100, 150, 180, 240, 260, 280, 300, and 310 K, we collected data at the Cornell High Energy Synchrotron Source (CHESS) at beamline A1 with a 100 µm collimator using a wavelength of 0.9767 Å. Crystals were looped by hand, stripped of excess mother liquor (100 mM HEPES pH 7.5, 23% PEG 3350, 5 mM TCEP) using NVH oil (Warkentin and Thorne, 2009), and placed directly into the nitrogen-gas cryostream pre-set to the desired temperature at the beamline. Water inside protein crystals is nanoconfined so that ice nucleation is dramatically suppressed, but water outside crystallizes readily and rapidly. Careful removal of all excess solvent from the crystal surface is essential to obtaining ice-free diffraction between 260 K and 180 K without using large cryoprotectant concentrations.

For the XFEL experiment, we collected multiple diffraction images per crystal using a 10-µm X-ray beam with each irradiation point separated by at least 25–40 µm to avoid collateral radiation damage. A total of 1,239 still diffraction images were collected from 71 CypA crystals over the course of two experiments using a goniometer setup and a Rayonix MX325HE detector at LCLS-XPP (Cohen et al., 2014) (Video 2). All data were collected at ambient temperature (approximately 273 K). To prevent dehydration, crystals were coated with paratone oil immediately after looping and mounted on the goniometer at the XPP endstation of LCLS using the SAM sample exchange robot (Cohen et al., 2002).

For the new 1.2 Å room-temperature synchrotron dataset, paratone oil was applied to cover a 2 μL hanging drop containing a single large crystal of CypA. The crystal was harvested through the paratone and excess mother liquor was removed using a fine paper wick. Attenuated data were collected at SSRL beamline 11-1 at 273 K controlled by the cryojet on the PILATUS 6M PAD detector.

### Crystallographic data processing

The synchrotron datasets were indexed, integrated, and scaled using XDS and XSCALE, and intensities were subsequently converted to structure factor amplitudes using XDSCONV. All datasets were from single crystals. Data reduction statistics for the highest resolution room-temperature dataset and the multitemperature datasets can be found in Tables 1,4 respectively.

The XFEL data were processed using cctbx.xfel  (Hattne et al., 2014). Of the 1,239 images collected, 772 were indexed and their intensities were integrated. Post-refinement, as implemented by PRIME  (post-refinement and merging, version date: November 11, 20:22:51 2014) (Uervirojnangkoorn et al., 2015), was used to correct the intensity measurements and merge the data. We optimized over the uc_tolerance, n-postref_cycle, sigma_min, partiality_min, and gamma_e values to obtain the final structure factor amplitudes. Data reduction statistics for the XFEL data are provided in Table 3 .

To promote consistency between models derived from different datasets, Rfree flags were generated using PHENIX for the highest resolution ‘reference’ (1.2 Å, 273 K) dataset first and were subsequently copied to all other multitemperature and XFEL datasets for the automated molecular replacement and refinement pipeline.

### Model building

For each dataset, we calculated initial phases by performing molecular replacement with phenix.auto_mr using PDB ID 2cpl as a search model. We next refined XYZs and ADPs of the initial model with phenix.refine for 4 macrocycles with XYZ and ADP weight optimization turned on; identified translation libration screw (TLS) groups with phenix.find_tls_groups; and refined optimized XYZs, ADPs, and TLS parameters for six more macrocycles. These single-conformer models and associated electron density maps were used as input for two subsequent steps.

First, the single-conformer models were analyzed with Ringer (Lang et al., 2010) via mmtbx.ringer using default settings. A coupled side chain–backbone ‘backrub’ motion (Davis et al., 2006) of −10° for Ser99 (see Figure 5A) was necessary to match the Cα and Cβ positions of the minor conformation as modeled in PDB ID 3k0n; using this modified backbone indeed yielded maximal minor-conformation Ringer peaks for our multitemperature datasets. No backrub motion was necessary for Leu98 due to the different type of backbone displacement (Fraser et al., 2009). Correlation coefficients between pairs of Ringer electron density versus dihedral angle curves were calculated using the cor function in R (Team, 2014).

Second, the single-conformer models were used as input to qFit (Keedy et al., 2015; van den Bedem et al., 2009). Subsequent to the automated model building, we manually deleted ill-fitting waters and edited alternative protein side chain conformations based on fit to the electron density in Coot  (Emsley et al., 2010) and refinement with phenix.refine. For example, at 240 K, qFit automatically modeled Phe113 as single-state, but significant mFo-DFc peaks remained, so we decided on a two-state model. Met61 was particularly difficult to model accurately across temperatures due to convolved issues of χ3 non-rotamericity for Met in general (Butterfoss et al., 2005), the relatively high electron count for sulfur, and likely temperature-modulated Met-specific radiation damage. For these reasons, visual inspection of the maps and manual building is currently essential for alternative backbone conformations with moderate displacements, as observed in residues 79–83 (Figure 4). We are currently developing new methods to automatically detect and model such backbone excursions in multiscale multiconformer models. These efforts improved Rfree and MolProbity scores across datasets (Table 2). Because of the lower resolution, the XFEL model was refined with three TLS groups and with optimization of X-ray versus geometry and ADP weights.

### Model and electron density analysis

For minor-state electron density sums, 2mFo-DFc (Fc filled) map values were summed across a grid of points defined by superimposing each model onto PDB ID 3k0n using all Cα atoms, summing the 2mFo-DFc value at each point with 0.25 Å of a target minor-state heavy atom (Oγ for Ser99; Cδ1, Cε1, Cε2, or Cζ for Phe113), and normalizing to unity across datasets for each residue being analyzed. This procedure allowed a strictly common reference set of map evaluation points. Results were very similar when using unfilled maps (data not shown).

We calculated B-factor-influenced order parameters (S2) as previously reported (Fenwick et al., 2014) except that we monitored one of two different types of bond vector. For the χ1 order parameter, we used Cβ-Xβ (where X = C or O) for most amino acids, Cα-Cβ for Ala, and Cα-Hα for Gly. For the side chain-end order parameter, we used the heavy-atom to heavy-atom bond vector for each amino acid that was closest to the side chain terminus, with ties broken by the number in the atom name (e.g. Cγ-Cδ1 instead of Cγ-Cδ2 for Leu). All negative order parameters (caused by high B-factors) were floored to 0. χ1 order parameters were floored for 7 residues, and side chain-end order parameters were floored for 23 residues. Per-residue ‘apparent dynamic transition temperatures’ were then calculated as the intersection between the <200 K and >200 K fit lines in order parameter versus temperature plots and floored to 0 K if necessary. The kernel density curve was fit with the density function in R (Team, 2014).

For extrapolation of fit lines in Figure 6 , we used a fit to all data points or to just the high-temperature data points (≥240 K) for each residue, and extrapolated to the temperature at which order would be maximized (1 – S2 = 0). To predict global behavior, at each temperature we averaged across all residues the predicted 1 – S2 values from the fit, making sure to floor non-physical predicted values of 1 – S2 < 0 to 0, as in (Lee and Wand, 2001).
