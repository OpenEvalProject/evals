# High-resolution structures with bound Mn2+ and Cd2+ map the metal import pathway in an Nramp transporter

## Authors

- Shamayeeta Ray<sup>1</sup> ([ORCID: 0000-0001-7906-0572](https://orcid.org/0000-0001-7906-0572))
- Samuel P Berry<sup>1</sup>
- Eric A Wilson<sup>2</sup>
- Casey H Zhang<sup>1</sup>
- Mrinal Shekhar<sup>3</sup>
- Abhishek Singharoy<sup>2</sup>
- Rachelle Gaudet<sup>1</sup> ([ORCID: 0000-0002-9177-054X](https://orcid.org/0000-0002-9177-054X)) †

### Affiliations

1. Department of Molecular and Cellular Biology, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
2. School of Molecular Sciences, Arizona State University Tempe United States ([ROR:03efmqc40](https://ror.org/03efmqc40))
3. Broad Institute Cambridge United States ([ROR:05a0ya142](https://ror.org/05a0ya142))

† Corresponding author

## Abstract

Transporters of the Nramp (Natural resistance-associated macrophage protein) family import divalent transition metal ions into cells of most organisms. By supporting metal homeostasis, Nramps prevent diseases and disorders related to metal insufficiency or overload. Previous studies revealed that Nramps take on a LeuT fold and identified the metal-binding site. We present high-resolution structures of Deinococcus radiodurans (Dra)Nramp in three stable conformations of the transport cycle revealing that global conformational changes are supported by distinct coordination geometries of its physiological substrate, Mn2+, across conformations, and by conserved networks of polar residues lining the inner and outer gates. In addition, a high-resolution Cd2+-bound structure highlights differences in how Cd2+ and Mn2+ are coordinated by DraNramp. Complementary metal binding studies using isothermal titration calorimetry with a series of mutated DraNramp proteins indicate that the thermodynamic landscape for binding and transporting physiological metals like Mn2+ is different and more robust to perturbation than for transporting the toxic Cd2+ metal. Overall, the affinity measurements and high-resolution structural information on metal substrate binding provide a foundation for understanding the substrate selectivity of essential metal ion transporters like Nramps.

## Introduction

Transition metal ions like Mn2+ and Fe2+ are essential for various metabolic processes in all living cells and are usually required in low intracellular concentrations for optimal activity (Andrews, 2002; Bozzi and Gaudet, 2021). Excess or deficiency of transition metal ions leads to diseases (Bleackley and Macgillivray, 2011; Nies and Grass, 2009). For example, Fe2+ deficiency causes anemia and neurodegenerative diseases, whereas Fe2+ overload increases the risk of cancer by generating toxic reactive oxygen species (ROS) and mutations (Ekiz et al., 2005; Jung et al., 2015). Mn2+ overload in the brain is linked to neurological disorders and deficiency causes metabolic defects and impairs growth (Budinger et al., 2021; Pittman, 2005). Other transitions metals, like Cd2+ and Hg2+, are toxic and their accumulation affects health by disrupting the physiological levels of essential metals or displacing them in enzyme active sites, thus inhibiting the proteins, or changing their activity (Andrews, 2002; Lin et al., 2009). Cells and organisms have evolved strategies to maintain metal ion homeostasis via highly regulated transport and storage processes (Bleackley and Macgillivray, 2011; Cellier and Gros, 2004; Nies and Grass, 2009).

Natural resistance-associated macrophage proteins (Nramps) are ubiquitous importers of Fe2+ and Mn2+ across cellular membranes into the cytosol (Bozzi and Gaudet, 2021; Cellier and Gros, 2004; Nevo and Nelson, 2006). In humans, Nramp1 extrudes essential metals from phagosomes of macrophages to aid in killing engulfed pathogens, and Nramp2 (DMT1) is expressed at low levels in the endosomes of all nucleated cells and imports Mn2+ and Fe2+ into the cytosol (Pujol-Giménez et al., 2017; Skamene et al., 1998; Vidal et al., 1993). Plant and fungal Nramps aid in Fe2+ and Mn2+ uptake and trafficking, and bacterial Nramps are involved in the acquisition of Mn2+, an essential nutrient (Bozzi and Gaudet, 2021). In addition to the physiological substrates Fe2+ and Mn2+, Nramps can also transport toxic metals like Cd2+ and Hg2+ but exclude the abundant alkaline earth metals like Mg2+ and Ca2+ (Bozzi and Gaudet, 2021).

Recent bacterial Nramp structures reveal a LeuT fold, three stable conformations (outward-open, occluded, and inward-open), and identify the metal-binding site residues, including conserved aspartate, asparagine, and methionine residues (Bozzi et al., 2016b; Bozzi et al., 2019b; Ehrnstorfer et al., 2014; Ehrnstorfer et al., 2017). The metal-binding methionine is essential to select against alkaline earth metals (Bozzi et al., 2016a). This finding is corroborated by the fact that a bacterial Nramp homolog which lacks a metal-binding methionine, NRMT (Nramp-related Mg2+ transporter), can transport Mg2+ (Ramanadane et al., 2022). However, little is known about whether the canonical Nramps can mechanistically distinguish between their physiological substrates (Fe2+ and Mn2+) from non-essential ones like Cd2+ within their broad spectrum of transition metal substrates. Functional studies on Deinococcus radiodurans (Dra)Nramp revealed that Mn2+ and Cd2+ transport differ in their dependence on pH, proton flux, and membrane potential (Bozzi et al., 2019a; Bozzi et al., 2019b). However, we lack high-resolution structural information on binding of different metals to explain these differences.

We present high-resolution structures of DraNramp in three conformations in both Mn2+-bound and metal-free states, providing the first molecular map of the entire Mn2+ transport cycle. The structures along with molecular simulations reveal that Nramps achieve alternate access during transport by adopting distinct Mn2+-coordination spheres in different conformations. These different conformations are also supported by dynamic rearrangements of key polar-residue networks that gate the inner and outer vestibules. This Mn2+ transport cycle also informs on the transport of Fe2+, the other common physiological Nramp substrate, because Fe2+ and Mn2+ have similar coordination preferences and chemical properties (Bozzi and Gaudet, 2021; Davidsson et al., 1989; Kawabata, 2019; Liu et al., 2021). Comparisons with an additional high-resolution structure of DraNramp bound to a non-physiological substrate, Cd2+, and complementary binding and transport measurements and mutational analyses, suggest that Nramps can distinguish physiological from toxic substrates through thermodynamic differences in the conformational landscape of the transport cycle.

## Results

### DraNramp transports a mostly dehydrated Mn2+ ion

To visualize how the metal substrate is coordinated in Nramps, we determined crystal structures of DraNramp using lipid-mesophase based techniques (Supplementary file 1a). We obtained a structure of wildtype (WT) DraNramp in an occluded state bound to Mn2+ at 2.38 Å by soaking crystals with Mn2+ (WT•Mn2+; Table 1, Figure 1A–B). We resolved a comparable structure using co-crystallization with Mn2+ and the inward-locking mutation A47W (A47W•Mn2+; Supplementary file 1b; Cα RMSD=0.47 Å; all pairwise RMSD values listed in Supplementary file 1c; Bozzi et al., 2016b). The similarity of both structures, including a nearly identical Mn2+-coordination sphere (Figure 1B, Figure 1—figure supplement 1A), suggests that the observations we make based on these two structures are robust. Both structures superimpose best with the published occluded metal-free G45R structure (Bozzi et al., 2019b). Although the inner vestibule is occluded in both structures, WT•Mn2+ and A47W•Mn2+ differ in their TM1a position, with WT•Mn2+ nearly identical to G45R whereas the A47W•Mn2+ TM1a is displaced within the inner vestibule, likely to accommodate the bulky tryptophan sidechain. Therefore, we generally used the WT•Mn2+ structure for analysis of the occluded state. As in the metal-free G45R, the Mn2+-bound occluded structures have a completely sealed outer vestibule and a partially closed inner vestibule, with the Mn2+ occluded from bulk solvent (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig1-v2.jpg)

**Figure 1.:** (A) Cartoon representation of WT•Mn2+ in an occluded state. Anomalous signal confirmed the presence of Mn2+ in both the orthosteric metal-binding site and an additional site at the mouth of the external vestibule (Figure 1—figure supplement 1A) which is less conserved across the Nramp family (Figure 1—figure supplement 3). TM1 and TM6 are labeled. (B) Detail of the orthosteric metal-binding site of WT•Mn2+ where D56, N59, M230, and the pseudo-symmetrically related carbonyls of A53 and A227 coordinate the Mn2+ ion (Figure 1—figure supplement 1B). A water molecule completes the six-ligand coordination sphere. Coordinating residues are shown as sticks, and coordinating distances are indicated in Å. (C) ITC measurement of the affinity of WT DraNramp for Mn2+. Top graph shows heat absorbed upon injection of Mn2+ solution to the protein solution. Bottom graph shows the fit of the integrated and corrected heat to a binding isotherm. The data show an endothermic mode of binding and fits best with a two-site sequential binding model. The figure shows one of three measurements and the average Kd values ± SEM (Kd1=190±30 µM, Kd2=1970±520 µM; see Appendix 1). Based on ITC experiments comparing Mn2+ binding to WT or DraNramp constructs with mutations at the external site (Figure 1—figure supplement 2A), we assigned Kd1 to the orthosteric site. In all figures, unless otherwise noted, TMs 1, 5, 6, and 10 are pale yellow, TMs 2, 7, and 11 gray, TMs 3, 4, 8, and 9 light blue, and Mn2+ atoms are magenta spheres.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) 2Fo-Fc (gray mesh; 1σ) and peaks from anomalous difference Fourier (magenta mesh; 4.5σ) maps calculated from the WT•Mn2+ and A47W•Mn2+ structures, respectively show Mn2+ bound at two sites, the orthosteric site (top) and an external site coordinated by D296 and D369 near the N-termini of EH2 and TM10, respectively (bottom). (B) Topology diagram showing the secondary structure organization of DraNramp with its characteristic LeuT fold, where TMs 1–5 and 6–10 form two pseudosymmetric inverted repeats. One intracellular helix, IH, and two extracellular helices, EH1 and EH2, connect TMs 2–3, 5–6, and 7–8, respectively. Black spheres indicate A53 in TM1a and A227 in TM6a, the two Mn2+-coordinating backbone carbonyls in the occluded state of DraNramp, one in each inverted repeat. Mn2+ is shown as magenta sphere.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) ITC measurements of Mn2+ binding to A47W (which behaves like WT) and WT (reproduced here from Figure 1 for comparison) which fit best to a two-site sequential binding model, and D296A and D369A (constructs with point mutations to either of the external site aspartates), which were fit using a one-site model with a fixed n=1 (and did not fit with a two-site model). The resulting Kd values for D296A and D369A are more similar to Kd1 of WT, indicating that the orthosteric site has higher Mn2+ binding affinity compared to the external site. The figure shows one of 2–3 measurements and the average Kd values ± SEM (see Appendix 1). (B) Initial metal uptake rates for DraNramp mutants at membrane potentials ranging from ΔΨ=0 to −120 mV (n=3; each data point is represented in the scatter plots and the black bars are the mean values). The metal ion concentration was 750 μM, and the pH was 7 on both sides of the membrane. D296A and D369A moderately reduced the initial transport rate at high membrane potentials. The overall trends are similar for both metals. Mn2+ transport showed higher voltage dependence than Cd2+ transport. Corresponding time traces are plotted in Figure 1—figure supplement 4.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) External site architecture in the G223W•Mn2+ (outward-open), WT•Mn2+ (occluded), M230A•Mn2+ and WT•Cd2+ (inward-open) structures showing positions of D296 and D369 across conformations, illustrating that the two residues are farther apart in the outward-open structure and cannot bind metal. Metal-coordinating distances are listed in Å. (B) A maximum likelihood phylogenetic tree illustrating evolutionary divergence of the Nramp family into several major clades for prokaryotes (clades A, B and C) and eukaryotes. (C) Frequencies of acidic and other polar amino acids in the loop regions surrounding D296 (left; loop preceding EH2) and D369 (right; loop preceding TM10) across phylogenetic clades, based on the sequence alignment used to build the tree in panel B (bacterial clade A, DraNramp numbering; bacterial clade B, Bacteroides fragilis MntH numbering; bacterial clade C, ScaDMT numbering; eukaryotic clade, human Nramp2 numbering). Across all clades, these two external loops have a high concentration of acidic amino acids. However, the exact positions of acidic residues observed in DraNramp—296 and 369 (arrowheads)—are not highly conserved except 369 in bacterial clades A and B, which is an aspartate, asparagine, or glutamate in most sequences (92.1% and 87.8% in clades A and B, respectively) (D) APBS (Jurrus et al., 2018)-generated electrostatic surface potential of the outward-open structure viewed from the extracellular side illustrates that D296 and D369 contribute to a funnel of negative charge leading into the orthosteric binding site.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A, B) Mn2+ (A) and Cd2+ (B) uptake for WT and mutant DraNramp constructs. (C) Representative time traces of Mn2+ (left) and Cd2+ (right) uptake (n=3) shows that no metal was imported into control liposomes. The initial metal uptake rates calculated from these time traces are in Figure 1—figure supplement 2A, Figure 3C, and Figure 5—figure supplement 4F. The source data for all plots are provided as Figure 1—source data 3.

**Table 1.**
 Data collection and refinement statistics for four new DraNramp structures.


<table>
  <thead>
    <tr>
      <th>StructureConformationBound metal ion substratePDB ID</th>
      <th>WTsoakOccluded none8E5V</th>
      <th>WT•Mn2+OccludedMn2+8E60</th>
      <th>M230A•Mn2+Inward openMn2+8E6I</th>
      <th>WT•Cd2+Inward openCd2+8E6M</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data Collection</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Beamline</td>
      <td>GMCA 23IDB</td>
      <td>GMCA 23IDB</td>
      <td>GMCA 23IDB</td>
      <td>NECAT 24IDC</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>1.033</td>
      <td>1.033</td>
      <td>1.033</td>
      <td>0.984</td>
    </tr>
    <tr>
      <td>Resolution range (Å)</td>
      <td>41.23–2.36 (2.44–2.36)</td>
      <td>41.28–2.38 (2.46–2.38)</td>
      <td>45.32–2.52 (2.61–2.52)</td>
      <td>45.54–2.48 (2.57–2.48)</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P 2 21 21</td>
      <td>P 2 21 21</td>
      <td>P 2 21 21</td>
      <td>P 2 21 21</td>
    </tr>
    <tr>
      <td>Unit cell (a, b, c)</td>
      <td>58.95, 71.04, 98.77</td>
      <td>59.08, 71.10, 98.75</td>
      <td>58.67, 71.35, 98.59</td>
      <td>59.14, 71.37, 99.05</td>
    </tr>
    <tr>
      <td>Unit cell (α, β, γ)</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
    </tr>
    <tr>
      <td>Number of crystals</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Total reflections</td>
      <td>58744 (5928)</td>
      <td>57472 (5733)</td>
      <td>146077 (14913)</td>
      <td>76829 (7275)</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>17477 (1718)</td>
      <td>16468 (1646)</td>
      <td>14548 (1427)</td>
      <td>15351 (1507)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>3.4 (3.4)</td>
      <td>3.5 (3.5)</td>
      <td>10.0 (10.4)</td>
      <td>5.0 (4.8)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>98.71 (98.85)</td>
      <td>95.11 (96.92)</td>
      <td>99.90 (99.79)</td>
      <td>99.03 (99.47)</td>
    </tr>
    <tr>
      <td>Mean I/σ (I)</td>
      <td>8.89 (0.97)</td>
      <td>8.92 (0.89)</td>
      <td>8.47 (0.75)</td>
      <td>9.90 (1.12)</td>
    </tr>
    <tr>
      <td>Wilson B-factor</td>
      <td>49.97</td>
      <td>50.55</td>
      <td>54.29</td>
      <td>49.52</td>
    </tr>
    <tr>
      <td>Rmerge</td>
      <td>0.106 (1.292)</td>
      <td>0.109 (1.241)</td>
      <td>0.269 (2.475)</td>
      <td>0.158 (1.626)</td>
    </tr>
    <tr>
      <td>Rmeas</td>
      <td>0.127 (1.511)</td>
      <td>0.127 (1.447)</td>
      <td>0.284 (2.603)</td>
      <td>0.178 (1.831)</td>
    </tr>
    <tr>
      <td>Rpim</td>
      <td>0.067 (0.759)</td>
      <td>0.063 (0.722)</td>
      <td>0.090 (0.800)</td>
      <td>0.078 (0.816)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>0.99 (0.37)</td>
      <td>0.99 (0.39)</td>
      <td>0.98 (0.34)</td>
      <td>0.99 (0.34)</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution range (Å)</td>
      <td>41.23–2.36 (2.44–2.36)</td>
      <td>41.28–2.38 (2.46–2.38)</td>
      <td>45.32–2.52 (2.61–2.52)</td>
      <td>45.54–2.48 (2.57–2.48)</td>
    </tr>
    <tr>
      <td>No. reflections</td>
      <td>17441 (1714)</td>
      <td>16438 (1636)</td>
      <td>14547 (1425)</td>
      <td>15291 (1507)</td>
    </tr>
    <tr>
      <td>No. reflections in Rfree</td>
      <td>1743 (171)</td>
      <td>1642 (164)</td>
      <td>1454 (143)</td>
      <td>1530 (151)</td>
    </tr>
    <tr>
      <td>Rwork</td>
      <td>0.217 (0.340)</td>
      <td>0.207 (0.316)</td>
      <td>0.225 (0.313)</td>
      <td>0.202 (0.319)</td>
    </tr>
    <tr>
      <td>Rfree</td>
      <td>0.245 (0.350)</td>
      <td>0.259 (0.358)</td>
      <td>0.266 (0.349)</td>
      <td>0.250 (0.354)</td>
    </tr>
    <tr>
      <td>Number of atoms</td>
      <td>3449</td>
      <td>3385</td>
      <td>3451</td>
      <td>3321</td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>2945</td>
      <td>2933</td>
      <td>2934</td>
      <td>2905</td>
    </tr>
    <tr>
      <td>Ligand</td>
      <td>443</td>
      <td>405</td>
      <td>448</td>
      <td>362</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>61</td>
      <td>47</td>
      <td>69</td>
      <td>54</td>
    </tr>
    <tr>
      <td>Protein Residues</td>
      <td>392</td>
      <td>393</td>
      <td>392</td>
      <td>388</td>
    </tr>
    <tr>
      <td>Ramachandran plot</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Favored (%)</td>
      <td>98.46</td>
      <td>98.47</td>
      <td>98.21</td>
      <td>98.96</td>
    </tr>
    <tr>
      <td>Allowed (%)</td>
      <td>1.54</td>
      <td>1.53</td>
      <td>1.79</td>
      <td>1.04</td>
    </tr>
    <tr>
      <td>Outliers (%)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>0.33</td>
      <td>1.00</td>
      <td>1.01</td>
      <td>1.01</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>8.25</td>
      <td>8.97</td>
      <td>7.15</td>
      <td>5.57</td>
    </tr>
    <tr>
      <td>RMS (bonds)</td>
      <td>0.002</td>
      <td>0.002</td>
      <td>0.002</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>RMS (angles)</td>
      <td>0.43</td>
      <td>0.46</td>
      <td>0.43</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>Average B-factor</td>
      <td>65.12</td>
      <td>64.98</td>
      <td>66.61</td>
      <td>64.82</td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>63.36</td>
      <td>63.23</td>
      <td>65.04</td>
      <td>62.68</td>
    </tr>
    <tr>
      <td>Ligand</td>
      <td>77.99</td>
      <td>78.48</td>
      <td>77.70</td>
      <td>83.11</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>56.34</td>
      <td>58.24</td>
      <td>61.33</td>
      <td>57.45</td>
    </tr>
    <tr>
      <td>No. of TLS groups</td>
      <td>9</td>
      <td>8</td>
      <td>3</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

_Values in parentheses are for highest-resolution shell. Data for M230A•Mn2+ merge reflections from three crystals. Data for the other structures were obtained from a single crystal. See Supplementary file 1a for details on soaking or co-crystallization procedures for bound metal ion substrates._

Anomalous difference Fourier maps confirmed presence of Mn2+ at the canonical, orthosteric Nramp metal-binding site between the unwound regions of TM1 and TM6 (Supplementary file 1d, Figure 1—figure supplement 1A). In WT•Mn2+, the Mn2+ is coordinated by conserved residues D56, N59, and M230, and backbone carbonyls of A53 and A227 (Figure 1A, Supplementary file 1e). A53 and A227 are pseudosymmetrically related in the inverted repeats of the LeuT fold of DraNramp (Figure 1—figure supplement 1B). The coordination sphere is completed by a water bridging Mn2+ with Q378, a residue previously proposed to directly coordinate Mn2+ in the occluded state (Bozzi et al., 2019b). This yields a coordination number of 6, typical for Mn2+, and a largely dehydrated metal-binding site with a distorted octahedral Mn2+-coordination geometry (Supplementary file 1f), as often observed in other Mn2+-protein complexes (Barber-Zucker et al., 2017; Couñago et al., 2014; Dudev and Lim, 2014).

At the mouth of the outer vestibule, an additional Mn2+ bridges D296 and D369 at the N termini of extracellular helix 2 (EH2) and TM10, respectively (Figure 1—figure supplement 1A). We denote this site as the ‘external site’ and the canonical substrate-binding site as the ‘orthosteric site’. Corroborating the structures, isothermal titration calorimetry (ITC) measurements reveal an endothermic mode of binding and are best fitted with a two-site model for WT (Kd1=190±30 µM, Kd2=1970±520 µM; Figure 1C) and A47W (Kd1=125±5 µM, Kd2=2450±650 µM; Figure 1—figure supplement 2A; all Kd values are in Supplementary file 1g; see Appendix 1 for a description of our ITC data analyses). To determine the affinity of the orthosteric site, we mutated the external-site aspartates. The D296A and D369A substitutions have little impact on Mn2+ transport (Figure 1—figure supplement 2B). The D296A and D369A variants each bind one Mn2+ with Kd=370±30 µM and 420±30 µM respectively (Figure 1—figure supplement 2A), which is closest to Kd1 of WT. Hence, the affinity for Mn2+ at the orthosteric site is higher than at the external site. A metal ion is present at the external site in all inward-open and occluded metal-bound DraNramp structures, but not outward-open structures, as opening the outer vestibule separates D296 and D369 and disrupts the site (Figure 1—figure supplement 3A). D296 and D369 are not conserved across Nramps, but they are more conserved within bacterial clade A, and there is a general abundance of acidic residues in the corresponding loop regions across all clades (Figure 1—figure supplement 3B–C). At present, our results provide little evidence of a biological role for this previously unidentified external site; perhaps the concentration of acidic residues at the mouth of the outer vestibule (Figure 1—figure supplement 3D) provides electrostatic attraction for metal cations.

### Snapshots of the complete Mn2+ transport cycle by DraNramp

We also determined high-resolution DraNramp structures in metal-free occluded (WT) and Mn2+-bound inward-open (M230A•Mn2+) states and re-refined a Mn2+-bound outward-open conformation (G223W•Mn2+; Table 1, Supplementary file 1a and b). Along with the published structures of outward-open metal-free G223W and inward-open metal-free ‘Patch’ (which has a patch of mutations in intracellular loops) (Bozzi et al., 2016b; Bozzi et al., 2019b), these new structures allow us to map the entire Mn2+ transport cycle to three major conformations, each in Mn2+-bound and metal-free states (Figure 2A–B). By ordering and comparing these six structures, we outline a molecular mechanism by which metal substrate binds, induces conformational change, and is released.

![Figure 2.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig2-v2.jpg)

**Figure 2.:** (A) Schematic of the conformational states that DraNramp traverses to import Mn2+. The mobile and stationary parts are pale yellow and light blue, respectively. (B) Corresponding structures of DraNramp, showing TMs 1 and 6 in green, TMs 5 and 10 in pale yellow, and TMs 2, 7, and 11 gray. Stationary TMs 3, 4, 8, and 9 are omitted to highlight the key motions in the mobile parts. Mn2+ ions are magenta. Black arrows indicate the key motions in TMs 1a and 6a detailed in panel (C), and TMs 5 and 10 detailed in Figure 2—figure supplement 1. Full structures and the electron density for TMs 1 and 6 are illustrated in Figure 2—figure supplement 2. (C) Pairwise superpositions of whole Mn2+-bound structures highlight the motions of TMs 1 and 6. Conformations are indicated at the bottom. The distance between residues 46 and 240 in TMs 1a and 6b, indicated for the green structures, increases from 5.9 Å to 13.8 Å from outward open to inward open. The large angular motions of TM1a and TM6b are also indicated. (D) Plots of B-factor by residue for the TM1 region (residues 40–70) and the TM6 region. The B-factors are highest for the inward-open state in which the interaction between TMs 1a and 6b (both in the inner leaflet) is broken.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Conformations are indicated at the bottom. The angular motions of TMs 5 and 10 across conformations are indicated by black arrows. All TMs other than TMs 5 and 10 are made transparent. The helices colored as in Figure 2B.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Crystal structures of each state of DraNramp. TMs 1 and 6 are colored green, TMs 5 and 10 are colored pale yellow, TMs 2, 7, and 11 in gray and TMs 3, 4, 8, and 9 are light blue. The Mn2+ ion in the orthosteric site, when present, is shown as a magenta sphere. (B) Corresponding 2Fo-Fc maps contoured at 1σ for TMs 1 and 6 of each structure illustrated in A.

TMs 1, 5, 6, and 10 move the most as the Mn2+-binding site accessibility switches from outward to inward across the conformations (Figure 2B–C, Figure 2—figure supplement 1), as also highlighted in previous studies (Bozzi and Gaudet, 2021; Bozzi et al., 2019b; Ehrnstorfer et al., 2017). As Mn2+ binds to the outward-open state, TM10 tilts toward TM1b, the upper half of TM5 toward TM7, and TM6a toward TM11 to seal the outer vestibule and yield an occluded state. The lower half of TM5 also moves away from TM1a, allowing it to swing upward to open the inner vestibule in the following transition. This swing of TM1a is the only noteworthy difference between the Mn2+-bound occluded and inward-open states, allowing release of the Mn2+ into the inner vestibule. TM1a swings to a similar angle in the new inward-open M230A•Mn2+ as in the previous low-resolution inward-open metal-free structure (Bozzi et al., 2016b), and structures of the homologous Eggerthella lenta Nramp-related magnesium transporter (EleNRMT), LeuT, and serotonin transporter (Coleman et al., 2019; Krishnamurthy and Gouaux, 2012; Ramanadane et al., 2022). Thus, most of the structural reorganization in Nramps occurs in the shift from outward open to occluded. The three metal-free DraNramp conformations are similar to their corresponding Mn2+-bound structures, suggesting that once Mn2+ is released, the conformational transitions are reversed, including passing through an occluded metal-free intermediate, to reach the outward-open metal-free conformation ready to accept Mn2+ (Figure 2A–B, Figure 2—figure supplements 1 and 2A).

The substrate-binding TM1 and TM6 are well-resolved in our structures (Figure 2—figure supplement 2B) and pairwise superpositions reveal how their motions contribute to the conformational changes across the transport cycle (Figure 2C). TM6a tilts 22° and the unwound region of TM6 becomes more helical as it moves toward the Mn2+ to close the outer gate. The central unwound regions of TM1 and TM6 are closest in the occluded state, resulting in an almost dehydrated Mn2+-coordination sphere. Finally, the inner vestibule opens when TM1a tilts upward by 32°, increasing the distance between TM1a and TM6b by ~8 Å (Figure 2C). TM6b is largely static relative to the protein core, although in the inward-open structure it has high B-factors (Figure 2D), indicating that the interaction with TM1a stabilizes TM6b to close the inner vestibule.

### Different conformations have distinct Mn2+ coordinations

Our Nramp structures provide snapshots of the complete Mn2+-coordination sphere geometries in each conformation (Figure 3). Two new structures of DraNramp point-mutants reveal the coordination of Mn2+ in the inward-open state: M230A•Mn2+ and D296A•Mn2+ (Cα RMSD of 0.42 Å). The Mn2+ is in the same location of the orthosteric site as in the occluded state, as confirmed by anomalous diffraction for D296A•Mn2+ (Supplementary file 1d, Figure 3—figure supplement 1). As in the occluded state, the Mn2+ binds D56, N59, and the A227 carbonyl, with a water replacing M230 in M230A•Mn2+ (Figure 3A, Supplementary file 1e). However, with TM1a displaced, the A53 carbonyl no longer coordinates Mn2+; instead, the Y54 carbonyl approaches Mn2+ at a longer distance of 3.1 Å. Two more waters, one bound to Q378 and another from the inner vestibule, complete a seven-coordination sphere resembling a pentagonal bipyramidal geometry with substantial distortion (Supplementary file 1f). Seven coordination is infrequent but found in Mn2+-coordinating proteins like MntR (Chen and He, 2008; Glasfeld et al., 2003). Our inward-open structures provide the first evidence that Y54 participates in the Mn2+ transport cycle.

![Figure 3.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig3-v2.jpg)

**Figure 3.:** (A) Structures of the orthosteric metal-binding site in six conformations reveal the differences in coordination geometry and illustrate that the bound Mn2+ is more hydrated in the outward-open and inward-open states than the occluded state. In the occluded structure of metal-free WT DraNramp a density we have assigned as water replaces Mn2+. Y54 in TM1a progressively moves to open the inner vestibule in the transition from outward to inward open, shown by black curved arrows. (B) TM1 and TM6 from a superposition of the three Mn2+-bound structures in panel a illustrate the swing of the Y54 sidechain as sticks. The view is rotated 180° along the vertical axis from Figure 2C. (C) Initial Mn2+ uptake rates for DraNramp variants Y54A and Y54F at membrane potentials ranging from ΔΨ=0 to −120 mV (n=2–3; each data point is on the scatter plot and black bars are the mean values). The Mn2+ concentration was 750 μM, and the pH was 7 on both sides of the membrane. Y54A nearly abolishes transport whereas Y54F has near-wildtype initial transport rates. Corresponding time traces are plotted in Figure 1—figure supplement 4. (D) ITC measurements of G223W (left; one-site binding model with fixed n=1) and M230A (right; two-site sequential binding model) binding to Mn2+. One isotherm is shown of two measured, and the listed Kd values are the average ± SEM (see Appendix 1 for ITC analysis).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Cartoon representation of the inward-open structure of D296A•Mn2+, which is nearly identical to the M230A•Mn2+ inward-open structure (Cα RMSD of 0.38 Å). (B) Coordination sphere of the orthosteric Mn2+ ion in the D296A structure is nearly the same as in M230A Mn2+-bound structure except for the sulfur of M230 replacing a water seen in M230A. We do not observe a bound water to complete the coordination sphere of D296A, likely because the resolution of the structure is lower (2.52 Å for M230A•Mn2+ vs. 3.12 Å for D296A•Mn2+), otherwise the structures are analogous. The peak from the anomalous difference Fourier map (magenta mesh; 4.5σ) calculated from a D296A•Mn2+ crystal confirms a bound Mn2+ in this inward-open state. (C) 2Fo-Fc map (gray mesh; 1σ) of the orthosteric site of D296A•Mn2+.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig3-figsupp2-v2.jpg)

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Eukaryotic Nramps have either tyrosine or phenylalanine at the corresponding position. Residue coloring is based on the ‘chemistry’ coloring scheme of WebLogo (Crooks et al., 2004). Clades are as defined in Figure 1—figure supplement 3B.

The new occluded and inward-open Mn2+-bound structures have a monodentate coordination of D56 with Mn2+. For consistency, we reinterpreted the outward-open G223W•Mn2+ map (PDB ID: 6BU5) with a monodentate coordination of D56 with Mn2+ instead of previously modeled bidentate interaction (Bozzi et al., 2019b); the local and global model statistics are very similar to the original structure (Supplementary file 1e). Re-refined G223W•Mn2+ has six Mn2+-coordinating ligands: D56, N59, M230, carbonyl of A53 and two waters (Figure 3A, Supplementary file 1e); the overall geometry resembles a distorted octahedron as in the occluded structure (Supplementary file 1f). The coordination spheres in all conformations of the transport cycle are well defined as confirmed by the 2Fo-Fc maps of the closeup snapshots of their Mn2+-bound orthosteric site (Figure 3—figure supplement 1C, Figure 5—figure supplement 2).

Comparing the three Mn2+-bound conformations (Figure 3A), the carbonyls of A53 in TM1a and A227 in TM6b alternately coordinate Mn2+ in the outward- and inward-open structures respectively, and both residues interact with Mn2+ in the occluded structure. The pseudosymmetrically related A53 and A227 may thus act as hinges altering the Mn2+-coordination sphere as TM1 and TM6 move in turn to open the gates during Mn2+ transport. Furthermore, as DraNramp switches from outward- to inward-open, Y54 progressively swings downward, acting as a gate in concert with TM1a’s upward swing to open the inner vestibule and allow metal release (Figure 3A–B). Our inward-open structures also suggest that the Y54 carbonyl may participate in Mn2+ release through interaction with the metal ion (Figure 3A). All 3796 Nramp sequences in our alignment have either a tyrosine or a phenylalanine at this position and Y54 is completely conserved among bacterial clades A (including DraNramp) and C, while the position is 40% and 100% phenylalanine among eukaryotes and bacterial clade B, respectively (Figure 3—figure supplement 3). To evaluate the significance of Y54 in Mn2+ transport, we purified and reconstituted into proteoliposomes the Y54A and Y54F variants. While Y54F has near-wildtype Mn2+-transport activity, Y54A nearly eliminates Mn2+ transport (Figure 3C), indicating that an aromatic ring is essential for the gating motion required for transport.

We also measured the Mn2+-binding affinity of the constructs that yielded inward- or outward- open structures, M230A and G223W, respectively. Mn2+ is present at the external site in the inward-open M230A•Mn2+ (Figure 1—figure supplement 3A), and consistently, the ITC data fit a two-site model (Kd1=215±65 µM assigned to the orthosteric site, Kd2=4600±1300 µM for the external site; Figure 3D and Appendix 1). The ITC data for G223W with Mn2+ fits only in a one-site model (Kd=440±15 µM; Figure 3D), which we assign to the orthosteric site because the opening of the outer vestibule displaces TM10, disrupting the external site (Figure 1—figure supplement 3A).

### Mn2+ binding does not significantly alter the three main DraNramp conformations

To compare the metal-bound states to analogous metal-free states of the transport cycle, we determined two metal-free occluded structures of wildtype DraNramp at a higher resolution than the previously reported G45R structure (Bozzi et al., 2019b), which we refer to as WT (2.38 Å; Supplementary file 1b) and WTsoak (2.36 Å; Table 1). The crystal used for WTsoak was mock-soaked (with no metal in the soaking solution). WT and WTsoak are nearly identical, confirming that the soaking process does not influence the conformational state. We analyzed WTsoak, unless otherwise noted. In WTsoak, we observed density but no anomalous signal at the orthosteric site and modeled a water molecule at the position where Mn2+ sits in the occluded state (Figure 3A). WTsoak is nearly identical to WT•Mn2+, indicating that the occluded conformation is unchanged by the presence of metal ion substrate, and the metal-binding site is instead filled by ordered water molecules.

We used previously reported inward-open ‘Patch’ and outward-open G223W metal-free structures for analysis of the Mn2+ transport cycle (Figures 2B and 3A; Bozzi et al., 2016b; Bozzi et al., 2019b). These structures, resolved at lower resolution than the ones described here, have no density at the orthosteric site. This is consistent with a more flexible organization of a metal-binding site open to bulk aqueous solvent. In contrast, metal-free WT has a more ordered orthosteric site, suggesting a stable occluded intermediate in the switch from inward- to outward-open.

### Polar networks latch the gates to achieve alternating access

Vestibules providing access to the orthosteric site from the extracellular or intracellular side alternately open from the motions of DraNramp’s TMs 1, 5, 6, and 10, which form the outer and inner gates during Mn2+ transport (Bozzi et al., 2020; Bozzi et al., 2019b). To pinpoint protein features that enable these motions, we used our Mn2+-bound structures to identify interaction networks with the following attributes: (i) they contain conserved polar residues from at least one of the four mobile helices; (ii) they line the gates; and (iii) they rearrange between the three resolved protein conformations (Figure 4A).

![Figure 4.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig4-v2.jpg)

**Figure 4.:** (A) The Cα positions of residues in the Q378 (orange) and T228 (pink) networks lining the outer gate, R244 (cyan) and Q89 (blue) networks within the inner gate, and the H232 (orange) network coordinating with the proton pathway, are mapped on the occluded WT•Mn2+ structure. Metal-binding and proton pathway residues (Bozzi et al., 2019b) are represented as brown spheres. (B) The Q378 network forms as TM10 moves when DraNramp transitions from outward-open to occluded to close the outer vestibule. Water-mediated interactions form between Q378, D56, and T130. The other D56 carbonyl interacts directly with Mn2+. TM1 is transparent. (C) The T228 network forms with N275, N82, and T228 coordinating a water as TM6a moves to close the outer vestibule. TM1 is transparent. (D) In the R244 network, interactions between R244, E176, and D263 break as TM5 moves in the transition from outward-open to occluded state to initiate the opening of the inner vestibule. (E) In the Q89 network, Y54, Q89, and H237 rearrange from occluded to inward-open state as TM1a swings up to allow for metal release. (F) H232, which abuts the orthosteric Mn2+-binding site, interacts with E134 and T130 through waters conserved in all conformations. In the M230A•Mn2+ structure, H232 flips and is replaced by a water, retaining the interaction with T130 but breaking the connection with E134, suggesting that M230 helps stably position H232. TM8 is transparent. In panels c-e, TMs 3, 4, 8, and 9 are omitted to better visualize the interactions. The illustrated structures are indicated on the figure.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The alignment contains 3762 Nramp sequences, including 1055 bacterial clade A Nramps. Most residues that are less conserved in all Nramps are completely conserved in clade A to which DraNramp belongs. Residue coloring is based on the WebLogo scheme for amino acid chemistry (Crooks et al., 2004).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A–D) Time-course analyses of MD simulations starting in each of the three major conformations, showing replicates in different shades. (A) RMSD, calculated over all Cα atoms relative to the starting structure. Because some simulations experience substantial conformational changes after the first 250 ns (dashed line), we focused on this initial range for subsequent analyses. (B–C) Plots of the minimum distance between T228 and N275 (B) and T130 and Q378 (C) in the outer vestibule show that these interactions are stable in the inward-occluded and inward-open simulations but do not form in the outward-open simulations. (D) Likewise, simulations show that E176 and R244, located in the inner vestibule on TM5 and TM7, respectively, stably interact in the outward-open conformation, but not the occluded or inward-open conformations. (E–F) Representative 50% contour maps of water density calculated from a simulation starting the occluded conformation. (E) The water bridging T130, Q378 and D56 persists throughout most of the simulation, as do (F) the waters coordinated by H232 and T130 and H232 and E134, suggesting that all these waters-mediated interactions are robust. (G) A water is coordinated by H232 and T130 in 40–60% of frames across all simulations. A water is also coordinated by H232 and E134 but less frequently, in 2–40% of frames.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) H232 takes on rotamer 1 in all structures, except in the M230A structure where it takes on rotamer 2. (B) Time-course analyses of the χ1 and χ2 angles of the H232 sidechain during the MD simulations starting in each of the three major conformations, showing replicates in different shades. Interestingly, the simulations in the occluded state show H232 rapidly switching to rotamer 2 and primarily occupying the rotamer 2 state throughout the simulation. In contrast, H232 is fixed in rotamer 1 throughout the outward-open simulation and shows the most flexibility in the inward-open state. (C) Distribution of H232 rotamer states across each MD simulation.

Two networks seal the outer gate. In the occluded and inward-open conformations, Q378 interacts with two waters, one coordinating the orthosteric Mn2+ and the other interacting with D56 and the carbonyl of T130. This network is disrupted in the outward-open conformation as Q378 and the rest of TM10 swing outward to open the outer vestibule (Figure 4B). In the second network, T228, N275, and N82 interact via a water in the occluded and inward-open states, but not in the outward-open state, where the extended unwound region of TM6a positions T228 farther from the orthosteric site and N275 and N82 (Figure 4C). This T228 network helps rearrange TM6a, closing the outer vestibule in the occluded state and generating a nearly dehydrated Mn2+-coordination sphere (Figure 1B). As the inner gate opens to release Mn2+, both networks persist, ensuring that the outer gate remains closed in the inward-open conformation.

All six residues in the Q378 and T228 networks are completely conserved across bacterial clade A and highly conserved across all Nramps (Figure 4—figure supplement 1). To investigate the robustness of these networks, we performed duplicates of molecular dynamics (MD) simulations starting in each of the three conformations and confirmed that within the first 250 ns of these simulations, the T228 and Q378 networks persist in simulations of the occluded and inward-open states and remain broken in simulations starting in the outward-open state (Figure 4—figure supplement 2A–C). This includes the coordinated waters, for example the water at the center of the Q378 network is present in more than 50% of the frames in occluded-state simulations (Figure 4—figure supplement 2E). In line with the X-ray snapshots and simulation outcomes and highlighting their key function in the conformational cycle of Nramps, mutations of any of the six residues across these networks reduces Mn2+ transport by DraNramp (Bozzi et al., 2016a; Bozzi et al., 2019a; Bozzi et al., 2020; Bozzi et al., 2019b).

The inner vestibule is gated by rearrangements of residues in two other polar networks, namely those of R244 and Q89 (Figure 4D–E). In the outward-open state, R244 forms an ion pair with E176 and interacts with the TM1a backbone, as does D263, keeping TM1a and TM5 close and the inner gate closed (Figure 4D; Bozzi et al., 2020). In the occluded state, the E176-R244 interaction breaks and TM5 moves away from TM6b, creating space for TM1a to swing up and open the inner vestibule in the inward-open state. Accordingly, the E176–R244 ion pair is stable in MD simulations of the outward-open state, while these residues are >10 Å apart in simulations of the occluded and inward-open states (Figure 4—figure supplement 2D). Supporting the importance of the R244 network, E176 is 100% and R244 is 85% conserved across all Nramps (Figure 4—figure supplement 1) and mutation of either residue reduces Mn2+ transport by DraNramp (Bozzi et al., 2020).

In the Q89 network, Q89 hydrogen-bonds with Y54 and H237 to seal the inner gate in the outward-open (Bozzi et al., 2020) and occluded states (Figure 4E). In the inward-open structure, the Q89–H237 hydrogen bond is broken and a rearranged Y54–Q89 hydrogen bond buttresses the opening of the inner vestibule (Figure 4E). As discussed above, Y54 is conserved and important for Mn2+ transport by DraNramp (Figure 3C and Figure 3—figure supplement 1C). Similarly, Q89 and H237 are conserved (Figure 4—figure supplement 1), and mutations to either residue impair Mn2+ transport in a cell-based assay (Bozzi et al., 2020). Cysteine accessibility measurements showed that mutations to Q89 or H237 render the outer vestibule solvent-inaccessible (Bozzi et al., 2020), indicating that disrupting the Q89 network likely prevents closing of the inner gate.

H232 (TM6b) is conserved across all Nramps (Figure 4—figure supplement 1), highlighting its importance. H232 sits below the orthosteric site and forms a network conserved across all conformations, with water-mediated hydrogen bonds to E134 (involved in proton transfer to the salt-bridge residues in TMs 3 and 9) (Bozzi et al., 2019a; Bozzi et al., 2019b; Ehrnstorfer et al., 2017) and T130 in TM3 (Figure 4F). Waters occupy these two sites in MD simulations in all states, especially the water coordinated between H232 and T130 (Figure 4—figure supplement 2F–G). However, in M230A•Mn2+ H232 flips to interact with the G330 carbonyl (TM8; Figure 4F), suggesting that it may transiently move during the conformational cycle. Indeed, while the H232 sidechain rotamer is stable in MD simulations of the outward-open state, it explores other rotamers in simulations of the occluded and inward-open states (Figure 4—figure supplement 3).

### Unlike Mn2+ binding, Cd2+ binding to DraNramp is exothermic

Nramps transport divalent transition metals quite promiscuously, including both physiological (Fe2+ and Mn2+) and non-physiological substrates (Cd2+, Zn2+, Co2+, Ni2+, Pb2+), but select against alkaline earth metals (Mg2+, Ca2+) (I Bannon et al., 2002; Bozzi et al., 2016a; Bozzi and Gaudet, 2021; Bozzi et al., 2019b; Ehrnstorfer et al., 2017; Illing et al., 2012; Sacher et al., 2001). DraNramp transports Cd2+ well, but without concomitant proton flux and with weaker voltage dependence (Figure 5—figure supplement 1A; Bozzi et al., 2019a; Bozzi and Gaudet, 2021; Bozzi et al., 2019b). To better understand the underlying mechanistic differences, we compared the binding, transport, and structures of DraNramp with Mn2+ and Cd2+.

In contrast to endothermic binding of Mn2+, ITC measurements show exothermic binding of Cd2+ to WT DraNramp (Figure 5—figure supplement 1B; see Appendix 1 for details of the ITC analyses). Like for Mn2+, the Cd2+ isotherm fits best in a two-site model (Kd1=55±15 µM, Kd2=220±20 µM). Both D296A and D369A—containing mutations at the external metal-binding site—showed exothermic binding but fit best in a one-site model (Figure 5A). Based on their affinity (Kd=120±1 µM for D296A and Kd=70±10 µM for D369A), we conclude that the orthosteric site has higher affinity toward Cd2+ than the external site (Figure 5A–B). Both the orthosteric and external site shows higher affinity toward Cd2+ than Mn2+. The affinities are comparable at the orthosteric site, in low micromolar range for both metals (Kd of 190±30 µM for Mn2+ vs. 55±15 µM for Cd2+), whereas the external site has a much higher affinity toward Cd2+ (Kd of 1970±520 µM for Mn2+ vs. 220±20 µM for Cd2+). Consistent with its inability to transport Mg2+, a representative alkaline earth metal (Bozzi and Gaudet, 2021; Bozzi et al., 2019b), DraNramp does not bind Mg2+ (Figure 5A). These are the first ITC measurements comparing the binding of different metals to an Nramp transporter and they show clear differences in the binding mode and affinity of different substrates toward DraNramp (Figure 5A, Figure 5—figure supplements 2 and 3). In contrast to DraNramp, previous ITC studies showed endothermic binding of Cd2+ to the Staphylococcus capitis Nramp homolog (ScaDMT) with 29 µM affinity (Ehrnstorfer et al., 2014). However, in the absence of ITC data with other metals, it is not known whether ScaDMT also shows differences in the mode and affinity of binding to different metals like DraNramp.

![Figure 5.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig5-v2.jpg)

**Figure 5.:** (A) ITC measurements show that DraNramp binds Mn2+ in an endothermic mode, Cd2+ in an exothermic mode and does not bind Mg2+ (6 mM metal). ITC was performed with DraNramp in which the external site is mutated (D296A) to analyze binding at the orthosteric site. One isotherm is shown of 2 or 3 measured. These isotherms were fit using a one-site model with fixed n=1, and the listed Kd values are the average ± SEM (see Appendix 1 for ITC analysis). (B) Schematic showing the ITC-measured Kd values of various DraNramp constructs for Mn2+ (top) and Cd2+ (bottom). WT DraNramp binds Mn2+ and Cd2+ at the same two sites, with the external-site affinity ~10-fold higher and the orthosteric-site affinity ~threefold higher for Cd2+ than Mn2+. The M230A mutation eliminates binding of Cd2+ but not Mn2+ at the orthosteric site. The D369A mutation eliminates binding of either metal at the external site. A variant with mutations at both the orthosteric and external sites, M230A-D369A, does not bind Cd2+ but maintains orthosteric site binding for Mn2+. For all ITC data, the Kd values were computed while fixing the number of sites (n) to 1 or 2 and assigned to the external or orthosteric site based on knowledge of the crystal structures and mutational analysis (Appendix 1; Supplementary file 1g). ITC traces are shown in Figure 5—figure supplement 1A, Figure 5—figure supplement 2 and Figure 5—figure supplement 3. (C) Comparison of the inward-open state bound to Mn2+ (M230A•Mn2+; top) and Cd2+ (WT•Cd2+; bottom) shows differences in coordination geometry at the orthosteric site. D56 is oriented differently and does not directly coordinate Cd2+. Cd2+ coordinates N59, M230, carbonyls of A227 and Y54, and two waters, for a total of six ligands compared to seven for Mn2+. Mn2+ and Cd2+ are magenta and brown spheres, respectively. Of note, we use M230A•Mn2+ here because soaking of WT crystals with Cd2+ yielded an inward-open WT•Cd2+ structure (Figure 5—figure supplement 1C) whereas soaking the same kind of crystals with Mn2+ yielded an occluded WT•Mn2+ structure (Figure 1).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Proteoliposome-based assay with WT DraNramp showed higher voltage dependence for Mn2+ transport compared to Cd2+, with substantial transport of only Cd2+ at 0 mV. The concentration of metal used in this assay was 750 µM. (B) ITC measurements of WT, D296A, and D369A constructs of DraNramp binding to Cd2+. All Cd2+ isotherms show an exothermic mode of binding and are fit using a two-site sequential binding model (Kd1=55±15 µM, Kd2=220±20 µM) for WT, and one-site model with fixed n=1 for both D296A and D369A. By comparing ITC results from binding of Cd2+ to these constructs, we assigned a lower affinity (Kd2) to the external site. One isotherm is shown of 2 or 3 measured, and the listed Kd values are the average ± SEM (see Appendix 1 for ITC analysis). (C) Cartoon representation of WT•Cd2+, with Cd2+ ions as brown spheres. The positions of TM1 and TM6, especially the upward swing of TM1a, confirms the inward-open conformation. (D) Peaks from the anomalous difference Fourier map (brown mesh; 3.5σ) and electron density from the 2Fo-Fc map (gray mesh; 1σ) from WT•Cd2+ show that Cd2+ binds at both the external and orthosteric sites.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) M230A mutation at the orthosteric site impacts Cd2+ binding more than Mn2+. (B) D56A mutation leads to weaker binding compared to WT for both metals at both binding sites. (C–F) DraNramp constructs with double mutations, one at each metal binding site (M230A or D56A and D296A or D369A), show similar binding behavior, retaining binding of Mn2+ at the orthosteric site, but no Cd2+ binding. All Mn2+ and Cd2+ binding isotherms are endothermic and exothermic, respectively. One isotherm is shown of 2 or 3 measured, and the listed Kd values are the average ± SEM (see Appendix 1 for ITC analysis).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (A) In the G223W outward-locked construct, the orthosteric site is intact but the external-site ligands are far apart because of the opening of the extracellular vestibule (Figure 1—figure supplement 3A). Mn2+ binds at the orthosteric site in G223W, but Cd2+ binding is impaired. (B) The A47W inward-locked occluded construct binds both Mn2+ and Cd2, with two-site sequential binding and one-site binding models yielding the best fits, respectively. (C–D) Double mutants of A47W with either D296A (C) or D369A (D) retain Mn2+ binding but not Cd2+ binding, indicating that Cd2+ binds only at the external site and not the orthosteric site of the A47W construct, whereas Mn2+ binds at both binding sites. All Mn2+ and Cd2+-binding isotherms are endothermic and exothermic, respectively. One isotherm is shown of 2 or 3 measured, and the listed Kd values are the average ± SEM (see Appendix 1 for ITC analysis).

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** (A–E) Structural comparisons of the five networks of polar residues with Mn2+ (top; M230A•Mn2+ or D296A•Mn2+ as indicated) or Cd2+ (WT•Cd2+; bottom) bound at the orthosteric site. Inward-open conformations of Mn2+ and Cd2+ structures show identical arrangement of residues for the Q89 (A), T228 (B), and R244 (C) networks. In the outer-gate Q378 network (D), D56 does not coordinate the Cd2+ directly, but instead coordinates a water that interacts with Cd2+ and Q378. Due to its reorientation, D56 does not hydrogen-bond to T130. The H232 network (E) is conserved except that the interaction between E134 and D56 takes a different orientation in the Cd2+-bound structure. Some of the top (Mn2+-bound) panels are reproduced from Figure 4 for ease of comparison. (F) Initial metal uptake rates for DraNramp variants at different membrane potential (ΔΨ=0 to −120 mV; n=2–3; each data point is represented in the scatter plots and black bars are the mean values). The metal ion concentration was 750 μM, and the pH 7 on both sides of the membrane. Y54A, H232A, H237A, and Q89A strongly reduced the initial transport rate, whereas Y54F only moderately reduced it. The overall trends are similar for both metals. Mn2+ transport showed higher voltage dependence compared to Cd2+. Mn2+ data from Figure 3 are replotted here for ease of comparison. Corresponding time traces are plotted in Figure 1—figure supplement 4.

### A Cd2+-bound structure helps explain functional differences

To understand the differences in binding and transport of Mn2+ and Cd2+, we determined a 2.5 Å Cd2+-bound structure by soaking WT DraNramp crystals with 2 mM Cd2+ (Table 1). In agreement with the ITC data, WT•Cd2+ shows Cd2+ ions at both the external and orthosteric sites as confirmed by anomalous signal (Figure 5—figure supplement 1C–D, Supplementary file 1d). The higher affinity for Cd2+ than Mn2+ at the external site suggests that local geometry favors non-physiological Cd2+ over the physiological substrate Mn2+ (Figure 1—figure supplement 3A). The low affinity of this site for Mn2+, compared to Cd2+, is consistent with the idea that this external site plays a role in general electrostatic attraction of substrate to the orthosteric site, rather than as a finely tuned binding site specific for Mn2+.

Interestingly, WT•Cd2+ is inward open (Figure 5—figure supplement 1C), although both mocked-soaked and Mn2+-soaked crystals under otherwise equivalent conditions yielded occluded structures (WTsoak and WT•Mn2+, respectively; Figures 1 and 3). The larger ionic radius of Cd2+ (~0.95 Å) compared to Mn2+ (~0.82 Å) (Kumarevel et al., 2005; Vashishtha et al., 2016) and different preferred coordination geometry may increase the stability of the inward-open state with Cd2+ bound. Compared with the inward-open M230A•Mn2+, D56 adopts a different rotamer in WT•Cd2+ and does not coordinate the Cd2+ bound at the orthosteric site (Figure 5C). The rest of the coordination sphere is similar and includes N59, M230, the A227 carbonyl, the Y54 carbonyl, a water that coordinates Q378 and another water from inner vestibule. Cd2+ has six coordinating ligands, and the distortion from ideal octahedral geometry is more pronounced compared to Mn2+ (Supplementary file 1f). The coordination distances are larger for Cd2+ than for Mn2+ (Supplementary file 1e), as seen in other proteins (Begg et al., 2015; Yokoyama et al., 2012) and consistent with its larger ionic radius and distinct charge distribution. Cd2+ is a soft metal, likely explaining why it retains coordination by the softer sulfur ligand of M230 (Cammack and Hughes, 2008) but not the hard oxygen of D56, although D56 can still provide favorable electrostatics.

### Cd2+ binding is prone to perturbations and favors the inward-open state

ITC data analysis of different DraNramp variants highlights additional differences between Mn2+ and Cd2+ binding and how their binding affects the conformational preferences of DraNramp (Figure 5B, Figure 5—figure supplements 2–3). A general observation is that, at the orthosteric site, Mn2+ and Cd2+ binding are entropy- and enthalpy-driven, respectively, and entropy contributions (-TΔS) are smaller for Cd2+ than Mn2+ (Appendix 1), suggesting that Cd2+ binding conformationally constrains the protein more, leads to less solvent release, or both (Ferrante and Gorski, 2012; Olsson et al., 2008).

ITC with the orthosteric-site mutants, M230A and D56A, shows metal-specific behavior. For M230A, Mn2+ binding fits with a two-site model and Cd2+ fits only with a one-site model (Figure 5B and Figure 5—figure supplement 2, Appendix 1). M230 is thus a crucial ligand for Cd2+ but not Mn2+, which is further reflected in the transport behavior where M230A affects Cd2+ transport drastically but has negligible effect on Mn2+ (Bozzi et al., 2016a; Bozzi et al., 2019a). Data for D56A fit better with a two-site model with both metals, although D56A does not transport either metal (Bozzi et al., 2019b). This suggests that D56 is more important for catalyzing transport than for substrate binding. Data for variants with an additional mutation at the external site (D56A-D296A, D56A-D369A, M230A-D296A, and M230A-D369A) fit only with a one-site model for Mn2+-binding isotherms, which we assigned as binding to the orthosteric site. However, all four double mutants showed complete loss of Cd2+ binding, which is expected for ones with M230A—which eliminates Cd2+ binding at the orthosteric site on its own, as we have also shown previously (Bozzi et al., 2016a)—but more surprising for double mutants with D56A. Thus, binding of the preferred physiological Mn2+ substrate at the orthosteric site is more robust to perturbations than binding of Cd2+, a toxic metal.

The conformation-locking mutants—A47W, which is outward-closed (Bozzi et al., 2016b) and crystallized in an occluded state, and outward-open G223W (Bozzi et al., 2019b)—also show different behavior with Mn2+ and Cd2+ (Figure 5—figure supplement 3). ITC with Mn2+ agrees with the structural data, with two-site fit for A47W (Figure 1—figure supplement 2A), and one-site fit for A47W-D296A, A47W-D369A, and G223W (assigned to the orthosteric site). However, with Cd2+, the ITC data for A47W fit best with a one-site model and we observed no binding with A47W-D296A, A47W-D369A, and G223W, indicating that there is no significant affinity for Cd2+ at the orthosteric site of A47W and G223W. This is consistent with our inability to obtain Cd2+-bound structures in conformations other than inward-open, despite trying both co-crystallization and soaking with A47W and G223W. These data suggest that Cd2+ has highest affinity for the inward-open state and low affinity for other states, in agreement with the fact that soaking of WT crystals (which yielded the metal-free occluded WTsoak structure) produced an inward-open Cd2+-bound structure.

### Gating network differences in the Cd2+-bound structure are restricted to D56

To better understand the Cd2+ transport mechanism given that its binding at the orthosteric site seems less optimal and robust than Mn2+, we compared the gating networks described above for the inward-open Mn2+- and Cd2+-bound structures. The Q89, T228, and R244 networks are essentially identical in the inward-open state, regardless of whether Mn2+ or Cd2+ is bound (Figure 5—figure supplement 4A–C).

The other two networks, both of which involve D56, have some differences. In the Q378 network gating the outer vestibule, D56 does not coordinate Cd2+ but does interact with the conserved water that connects the metal ion with Q378 in all outward-closed structures (Figure 5—figure supplement 4D). This preserves a connection to both Cd2+ and Q378 to close the outer gate. Most of the H232 network is similar in the Mn2+- and Cd2+-bound structures, except for the orientation of D56 relative to E134 (Figure 5—figure supplement 4E).

Mutations of several residues in these polar networks reduced transport in proteoliposome-based assays (Figure 5—figure supplement 4F), corroborating results from cell-based assays (Bozzi et al., 2020). Y54A, H237A, and H232A mutations cause the largest decreases, Q89A causes a moderate decrease, and Y54F is similar to WT. Mn2+ and Cd2+ follow similar trends although with less voltage dependence for Cd2+ than Mn2+. These results support the idea that although Mn2+ and Cd2+ bind differently at the orthosteric site, the flexibility of the D56 sidechain enables the networks of polar residues that gate the outer and inner vestibules to engage and enable transport of both metals at similar rates.

## Discussion

Our high-resolution structures in different conformations and analysis of substrate-binding affinities reveal a molecular map of the Mn2+ import pathway in DraNramp (Video 1). Binding of the Mn2+ substrate at the orthosteric site takes on different coordination geometries through the three main conformational states in the transport cycle, all of which deviate substantially from ideal, consistent with the moderate binding affinities we measured. We identified several networks of polar interactions that gate both the outer and inner vestibules. Structures of DraNramp bound to Mn2+ and Cd2+ and corresponding analyses of substrate binding demonstrate that the orthosteric site shows similar affinity for physiological (Mn2+) and toxic (Cd2+) substrates, but Cd2+ binding is less robust to various perturbations.

![Video 1.](https://cdn.elifesciences.org/articles/84006/elife-84006-video1.mp4.jpg)

**Video 1.:** The global conformational changes are highlighted first, with cartoon representations of each of the six structures in the Mn2+ transport cycle starting from the outward-open Mn2+-bound conformation rotating through the occluded Mn2+-bound, inward-open Mn2+-bound, and then the metal-free states transitioning back to outward-open Mn2+-bound form. The second set of scenes then focusses on the orthosteric site, cycling through the structures in the same order to illustrate the distinct coordination geometries of the bound Mn2+, and the corresponding positions of its interacting ligands (protein residues and water) in the metal-free states.

Our structures of one Nramp homolog, DraNramp, in all conformations of the transport cycle provide an opportunity to update the overview of the conformational cycle, focusing on the polar interaction networks that gate the outer and inner vestibules (Figure 6A). The structures also provide the first molecular view of how local changes in the coordination spheres and the global conformational transitions coordinate to facilitate Mn2+ transport. Starting in the outward-open state, Mn2+ entry into the outer vestibule and binding at the orthosteric site triggers the transition to the occluded state by two major rearrangements: (i) closing of the outer gate as the T228 and Q378 networks form and support the reorientation of TM6a and TM10, respectively, and (ii) partial opening of the inner gate through motion of TM5 and breaking of the R244 network. TM6a and TM10 approach the orthosteric site and directly (A227 in TM6a) or indirectly (Q378 in TM10 through a conserved water) coordinate Mn2+ and restrict solvent access from the extracellular side in the occluded structure. A227 replaces a water of the outward-open Mn2+-coordination sphere, thus retaining a six-coordination geometry in both conformations. Mn2+ prefers octahedral (six) coordination (Chen and He, 2008; Dudev et al., 2006; Dudev and Lim, 2014) as in the outward-open and occluded structures, although we observed distortions (Supplementary file 1f).

![Figure 6.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig6-v2.jpg)

**Figure 6.:** (A) After Mn2+ enters through the outer vestibule between TM6a and TM10 in the outward-open state, a bulk conformation change closes the outer gate. The occluded conformation arises though rearrangements of TM6a and TM10 facilitated by formation of the T228 and Q378 networks, respectively. The inner gate partially opens in the occluded state as the R244 network breaks and TM5 moves. To achieve the inward-open conformation, disruption of the Q89 network frees TM1a to swing up to fully open the inner vestibule for Mn2+ release into the cytosol. (B) Our data indicate that the most stable Mn2+-bound state is the occluded state, and the three main states are readily accessible to facilitate transport. In contrast, Cd2+ binding stabilizes the inward-open state.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/84006/elife-84006-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** In all structures, Mn2+ binds in an octahedral coordination. The geometry is more distorted (RMSangle=25°) and bond distances are longer in DraNramp, perhaps to enable Mn2+ transport and the associated protein dynamics. In comparison, the geometry is close to ideal (RMSangle=8°) and bond distances shorter in MntR, where Mn2+ binding, but not transport, is essential for regulating downstream signaling.

The inward-open state is achieved when TM1a swings up, rupturing the Q89 network and opening the inner gate. The coordination sphere changes again as a water from the open inner vestibule replaces A53 from TM1a. The TM1a swing introduces Y54 as a long-range seventh ligand. The seven-coordination of Mn2+ in the inward-open structure is less favored and more distorted, which may facilitate Mn2+ release as a solvated ion in the cytosol. In contrast, the more favorable six-coordination in the outward-open and occluded structures could help energize the global conformational changes. Our metal-free structures indicate that after Mn2+ release to the cytosol, the protein resets to the outward-open state through the same occluded state. The residues in the gating networks are highly conserved, suggesting that their role is conserved across the Nramp family.

Compared to other proteins that bind Mn2+ but are not metal transporters, like the Mn2+ regulator MntR (Glasfeld et al., 2003) and PsaA, the solute-binding protein (SBP) domain of an ATP-binding cassette transporter (Couñago et al., 2014), we observe longer Mn2+-coordinating bond lengths for DraNramp (Figure 6—figure supplement 1). Typical manganese-oxygen bonding distances are 2.1–2.5 Å, although ‘weak interactions’ (2.6–3.2 Å) are occasionally part of a Mn2+-coordination sphere (Harding, 2000; Harding, 2001). Metal-sulfur bonding distances are longer owing to the greater van der Waals radius of sulfur (Rulísek and Vondrásek, 1998). The non-ideal metal-ligand bonding distances and angles we observe in DraNramp may allow it to avoid getting trapped in an energy minimum and thus keep moving through the conformational transitions required to transport Mn2+.

While the Mn2+ transport mechanism and associated conformational changes in DraNramp differ appreciably from other LeuT-fold transporters (Bozzi and Gaudet, 2021; Bozzi et al., 2019b), the presence of key residues defining the extracellular and intracellular gates is a common theme (Coleman et al., 2016; Coleman et al., 2019; Faham et al., 2008; Krishnamurthy and Gouaux, 2012; Krishnamurthy et al., 2009; Perez et al., 2012; Shimamura et al., 2010; Watanabe et al., 2010). Comparing the gating networks described for these transporters with DraNramp, the positions and nature of the gating networks are generally not conserved, but two common themes emerge. First, opening (or closing) a particular vestibule often involves a pair of changes, as in the DraNramp intracellular vestibule (Figure 6A). Such paired changes have been associated with ‘thin’ and ‘thick’ gates in Mhp1 (Simmons et al., 2014) and LeuT (Krishnamurthy and Gouaux, 2012), that is, gates based on sidechain and helix motions, respectively. Second, some gating residue positions are shared, but the networks are not, indicating that different families have evolved analogous networks to stabilize equivalent conformations (Coleman et al., 2016; Krishnamurthy and Gouaux, 2012).

The accumulated DraNramp structures also provide clues as to the thermodynamic landscape of the transport process (Figure 6B). Interestingly, both metal-free and Mn2+-bound WT DraNramp crystallized in the occluded conformation, whereas the open conformations were achieved through conformation-locking (Bozzi et al., 2019b) or mutations of functionally important residues (Bozzi et al., 2016b). This occluded state more closely resembles an inward-open conformation (Bozzi et al., 2019b) and is an important intermediate in the Mn2+ transport cycle, with both local changes in coordination geometry and global changes in protein conformation in comparison to the outward-open state. Physiologically, we naïvely expect outward-open, rather than occluded, to be the preferred substrate-free conformation. However, the occluded or inward-open states of other LeuT-fold importers are also more stable, with changes in environmental conditions or the presence of substrate stabilizing specific states and lowering barriers to conformational transitions (Del Alamo et al., 2022). For example, SGLT1 and DraNramp require a negative membrane potential to transport substrates and this negative membrane potential stabilizes the outward-open state of SGLT1 (Bozzi et al., 2019a; Loo et al., 1998). Overall, our DraNramp structures suggest that the occluded state is most stable (at least in the absence of a membrane potential). The occluded and inward-open states may be energetically similar as relatively small perturbations yielded inward-open structures (M230A•Mn2+ and D296A•Mn2+). Furthermore, our previous cysteine accessibility data indicate that the energy barriers between states are low enough for the protein to readily sample the outward- and inward-open states in cell membranes in the absence or presence of metal substrate (Bozzi et al., 2016b; Bozzi et al., 2019b).

In contrast to WT DraNramp, ScaDMT was crystallized in an inward-open state, although its TM1a was deleted from the protein construct (Ehrnstorfer et al., 2014). This deletion would prevent inner vestibule closure, and thus likely affects its energetically preferred conformation. In the case of the Eremococcus coleocola Nramp homolog (EcoDMT), both substrate-free and inhibitor-bound conformations are outward open (Ehrnstorfer et al., 2017; Manatschal et al., 2019), suggesting that the outward-open state is its most stable state. Of note, EcoDMT was crystallized in detergent, whereas the DraNramp structures were obtained in a monoolein lipid bilayer environment. Further studies will be needed to determine to what extent the thermodynamic landscape we begin to outline here for DraNramp is conserved in other Nramp homologs.

Previous metal selectivity studies indicate that Nramps import different substrates with distinct mechanisms (Bozzi et al., 2016a; Bozzi et al., 2019a; Bozzi and Gaudet, 2021; Ehrnstorfer et al., 2014; Nevo and Nelson, 2006). These differences correlate with chemical properties (Irving and Williams, 1953) and preferred coordination chemistry (Ma et al., 2009; Singh et al., 2020) of these transition metals as observed in other transition metal binding proteins like the Psa permease (Begg et al., 2015; Couñago et al., 2014), and cation diffusion facilitators (CDFs) (Barber-Zucker et al., 2017). That WT•Cd2+ retains the M230 sulfur as a coordinating ligand but excludes the D56 carboxylate can be rationalized by the fact that Cd2+ is a softer metal than Mn2+. This difference in coordination likely alters the pKa of nearby residues and water molecules to perturb the proton pathway such that DraNramp co-transports protons with Mn2+ but not Cd2+ (Bozzi et al., 2019a; Bozzi et al., 2019b), although our structures do not yet fully elucidate this mechanistic difference. Moreover, owing to its larger radius, Cd2+ tends to form weaker complexes than Mn2+ with comparable coordination numbers in complexes dominated by harder ligands (Rulísek and Vondrásek, 1998; Singh et al., 2020). The architecture of the orthosteric site in DraNramp appears to facilitate six- or seven-coordinated metal complexes, and thus most Cd2+-bound DraNramp conformations will be less stable than the Mn2+-bound states. Our ITC data also indicate that binding of the toxic Cd2+ to DraNramp is less robust to perturbations compared to its physiological substrate Mn2+. Furthermore, Cd2+ only binds well to the inward-open state, and its binding is exothermic rather than endothermic for Mn2+ (Figure 5A). The crystallographic data similarly suggest that inward-open is the most stable Cd2+-bound state (Figure 6B), based on the following observations: (i) soaking crystals of occluded WT yielded inward-occluded WT•Cd2+, (ii) co-crystallization efforts yielded no other Cd2+-bound structures, and (iii) soaking Cd2+ into crystals of outward-locked G223W yielded very poor diffraction and no structures.

Overall, our data show that the orthosteric metal-binding site of DraNramp, conserved across all Nramps, is best suited to the physiological substrate Mn2+ (and likely the similar ion Fe2+). The distinct interactions of Nramps with Mn2+ and Cd2+ could be leveraged for the design of therapies for metal toxicity and prevention strategies for toxic metal accumulation in crops. These results also lay a foundation for future studies of how metal ion transporters like Nramps evolve their substrate selectivity, for example in response to different environmental conditions. Finally, the first complete set of structures with the same homolog, both in substrate-free and substrate-bound states, suggest a substrate-specific thermodynamic landscape of the transport cycle and provide a framework for future experiments and simulations to fully define this landscape, and for comparisons to other LeuT-fold transporters.

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
      <td>Gene (Deinococcus radiodurans)</td>
      <td>DraNramp</td>
      <td>Genomic DNA</td>
      <td>Uniprot: Q9RTP8</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>C41(DE3)</td>
      <td>Lucigen</td>
      <td>60442–1</td>
      <td>Chemically competent cells</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>DH5α</td>
      <td>Invitrogen</td>
      <td>18265–017</td>
      <td>Chemically competent cells</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET21a</td>
      <td>Novagen</td>
      <td>69740–3</td>
      <td>Vector backbone for cloning DraNramp</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>n-Dodecyl-β-D-Maltopyranoside</td>
      <td>Anatrace</td>
      <td>D310S</td>
      <td>1% for solubilizing membrane, 0.03% used in wash buffer</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>n-Decyl-β-D-Maltopyranoside</td>
      <td>Anatrace</td>
      <td>D322S</td>
      <td>0.1% used in exchange buffer</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Lauryl maltose neopentyl glycol</td>
      <td>Anatrace</td>
      <td>NG310</td>
      <td>0.01% in elution buffer, 0.003% used in SEC buffer</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Monoolein</td>
      <td>Anatrace</td>
      <td>LCP18</td>
      <td>1:1.5 (protein: monoolein) for LCP crystallization</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Fura-2 Pentapotassium Salt, cell impermeant</td>
      <td>Life Technologies</td>
      <td>F-1200</td>
      <td>5 mM mixed with in proteoliposome</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>1-Palmitoyl-2-oleoyl-sn-glycero-3-phospho-(1'-rac-glycerol) (POPG)</td>
      <td>Avanti Polar Lipids</td>
      <td>850457 C</td>
      <td>lipid mixture (3 POPE: 1 POPG) and protein in 400:1 ratio for proteoliposome preparation</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>1-Palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine (POPE)</td>
      <td>Avanti Polar Lipids</td>
      <td>840757 C</td>
      <td>lipid mixture (3 POPE: 1 POPG) and protein in 400:1 ratio for proteoliposome preparation</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Valinomycin</td>
      <td>Sigma-Aldrich</td>
      <td>V0627</td>
      <td>Creates membrane potential by transporting K+ in proteoliposome assay</td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Ni Sepharose High Performance Resin</td>
      <td>Cytiva</td>
      <td>95055–838</td>
      <td>IMAC resin</td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Superdex 200 10/300 GL</td>
      <td>Cytiva</td>
      <td>89497–272</td>
      <td>SEC column</td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>PD-10 Desalting Column</td>
      <td>Cytiva</td>
      <td>95017–001</td>
      <td>Buffer exchange</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>XDS</td>
      <td>PMID:20124692</td>
      <td>RRID:SCR_015652</td>
      <td>Data Porcessing</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PHASER</td>
      <td>PMID:19461840</td>
      <td>RRID:SCR_014219</td>
      <td>Model Builiding</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PHENIX</td>
      <td>PMID:22505256</td>
      <td>RRID:SCR_014224</td>
      <td>Refinement</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>coot</td>
      <td>PMID:20383002</td>
      <td>RRID:SCR_014222</td>
      <td>Refinement and model building</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PyMOL</td>
      <td>Schrödinger</td>
      <td>RRID:SCR_000305</td>
      <td>Figure making</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HMMER</td>
      <td>hmmer.org</td>
      <td>RRID:SCR_005305</td>
      <td>Collected sequences with jackhmmer and aligned with hmmalign</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MUSCLE</td>
      <td>PMID:15318951</td>
      <td>RRID:SCR_011812</td>
      <td>Aligning sequences</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RAxML-NG</td>
      <td>PMID:31070718</td>
      <td>RRID:SCR_022066</td>
      <td>Tree building</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PropKa</td>
      <td>PMID:26596171</td>
      <td></td>
      <td>Identifying protonation states</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CHARMM-GUI</td>
      <td>PMID:25130509</td>
      <td></td>
      <td>Building MD system</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>NAMD</td>
      <td>PMID:20675161</td>
      <td>RRID:SCR_014894</td>
      <td>Running MD simulations</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>mdtraj</td>
      <td>PMID:26488642</td>
      <td></td>
      <td>Analyzing MD data</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>VMD</td>
      <td>PMID:8744570</td>
      <td>RRID:SCR_001820</td>
      <td>Analyzing MD data</td>
    </tr>
  </tbody>
</table>

### Cloning and protein expression vectors

The DraNramp WT and mutant constructs were cloned into pET21a-N8H (Bozzi et al., 2016a). Primer sequences for the mutations are listed in Supplementary file 1h. All constructs used for crystallization had a truncation of 31 residues at the N-terminus (ΔN31, which does not impair metal transport), except for A47W which was full-length and transport deficient (Bozzi et al., 2016b). For proteoliposome-based transport assays, the full-length versions of each construct were used. For ITC, full-length DraNramp constructs were cloned into pET21-NStrep (Bozzi et al., 2016a) to avoid background signal from metals (Mn2+, Cd2+) binding to the His-tag. All mutations were introduced by site-directed mutagenesis using the Quikchange mutagenesis protocol (Stratagene) and confirmed by Sanger DNA sequencing.

### Protein expression

Protein expression was performed as previously described (Bozzi et al., 2016a). Briefly, transformed Escherichia coli C41(DE3) (Lucigen) were induced with 0.1 mM isopropyl-β-D-thiogalactopyranoside and cultured at 18 °C for 16 hr. Cell pellets from 10 L of culture were harvested and flash frozen in liquid nitrogen.

### Protein purification for crystallography

Cells were thawed and resuspended in 50 mL load buffer (20 mM sodium phosphate, pH 7.5, 55 mM imidazole pH 7.5, 500 mM NaCl, 10% (v/v) glycerol) supplemented with 1 mM PMSF, 1 mM benzamidine, 0.3 mg/mL DNAse I and 0.3 mg/mL lysozyme and lysed by sonication on ice (six cycles of 45 s with a Branson Sonifier 450 under duty cycle of 65% and output 10). Lysates were cleared by centrifuging for 20 min at 20,000 rpm (Beckman JA-20) and membranes pelleted from the supernatant by ultracentrifugation at 45,000 rpm (Beckman type 45Ti) for 70 min. Membranes were homogenized in 70 mL load buffer using a glass Potter-Elvehjem grinder, solubilized for 1 hr in 1% (w/v) n-dodecyl-β-D-maltopyranoside (DDM), then ultracentrifuged at 35,000 (Beckman type 45Ti) for 35 min to remove insoluble debris. Pre-equilibrated Ni-Sepharose beads (2 mL; GE Healthcare) were incubated with the supernatant for 90 min at 4 °C, then washed with 20 column volumes (CV) of each of the following buffers sequentially (i) load buffer containing 0.03% DDM, (ii) load buffer containing 0.5% lauryl maltose neopentyl glycol (LMNG), and (iii) load buffer containing 0.1% LMNG. Protein was eluted in 20 mM sodium phosphate, pH 7.5, 450 mM imidazole pH 7.5, 500 mM NaCl, 10% (v/v) glycerol, 0.01% LMNG, concentrated to <0.5 mL in a 50 kDa molecular weight cutoff (MWCO) centrifugal concentrator (EMD Millipore), and purified by size exclusion chromatography (SEC) using a Superdex S200 10/300 (GE Healthcare) pre-equilibrated with SEC buffer (10 mM HEPES pH 7.5, 150 mM NaCl, 0.003% LMNG). Peak protein fractions enriched in DraNramp were combined, concentrated to ~25–40 mg/mL using a 50 kDa MWCO centrifugal concentrator, aliquoted and flash frozen in liquid nitrogen and stored at –80 °C. Purifications of each protein construct were performed at least twice and resulted in similar data.

### Purification of DraNramp for ITC

To purify protein for ITC, harvested cells expressing strep-tagged DraNramp from 10 L of culture were resuspended in 50 mL of buffer W (100 mM Tris, pH 8.0, 150 mM NaCl), and membranes were isolated, homogenized and solubilized in 1% DDM as above. The supernatant was incubated with Strep-Tactin Superflow resin (3 mL; IBA) pre-equilibrated with buffer W+0.03% DDM and washed with the following buffers sequentially: (i) 1 CV buffer W+0.03% DDM, (ii) 2 CV buffer W+0.5% LMNG and (iii) 2 CV buffer W+0.1% LMNG. Protein was eluted with 3 CV buffer W+0.01% LMNG+2.5 mM desthiobiotin. The eluted protein was concentrated up to 2.5 mL using a 50 kDa MWCO centrifugal concentrator and buffer-exchanged into 150 mM NaCl, 10 mM HEPES, pH 7.5, and 0.003% LMNG using disposable PD-10 desalting columns (GE healthcare). Protein was concentrated to ∼2.5 mg/mL a 50 kDa MWCO centrifugal concentrator and flash frozen in liquid nitrogen and stored at –80 °C. Purifications of each protein construct were performed at least twice and resulted in similar data.

### DraNramp crystallization

Crystallization of all constructs was performed using lipidic cubic phase (LCP). Protein was mixed with monoolein in 1:1.5 volume ratio using the syringe reconstitution method (Bozzi et al., 2019b). The protein bolus (60 nL) and 720 nL precipitant were dispensed onto custom-made 96 well glass sandwich plates using an NT8 drop-setting robot (Formulatrix). Metal-free crystals (WT) and metal supplemented (5 mM MnCl2) co-crystals (A47W•Mn2+, M230A•Mn2+, D296A•Mn2+) were grown in different precipitant conditions (Supplementary file 1a), harvested within 7–10 days (after reaching their optimal size of 30–40 μm rods) using mesh loops (MiTeGen) and flash-frozen in liquid nitrogen prior to data collection. Some structures (WT•Cd2+, WT•Mn2+, WTsoak) were obtained by soaking WT DraNramp crystals grown in metal-free precipitant (Supplementary file 1a) for 7–10 days: The glass covering the wells was broken without disturbing the bolus and 2 μl soak solution (Supplementary file 1a) were added before resealing with a fresh siliconized glass coverslip, incubating overnight (16–18 hr), then harvesting and flash freezing for data collection.

### X-ray diffraction data collection and processing

Diffraction data for structure determination and refinement were collected at beamlines 24-ID-C or 23-ID-B of the Advanced Photon Source at wavelengths of 0.984 Å or 1.033 Å, respectively. We used anomalous signals to confirm the presence of metals (Mn2+ or Cd2+) in the binding site. For D296A•Mn2+ and A47W•Mn2+, the same data we used for structure refinement and collected at 1.033 Å, 0.984 Å, respectively, provided strong anomalous signal in the metal-binding sites. For WT•Cd2+, we were able to collect data at 1.904 Å (near the low-energy boundary for the beamline), to maximize the anomalous signal. Locations of the crystals in the mesh loops were identified by grid scanning with a 20 μm beam at 10% transmission followed by data collection with a 10 μm beam at 15% transmission. Data were indexed in XDS (Kabsch, 2010) and scaled in CCP4 AIMLESS (Version 7.0) (Evans and Murshudov, 2013; Winn et al., 2011). For datasets collected from several crystals, data from each crystal were independently indexed and integrated, then combined during scaling using CCP4 AIMLESS (Evans and Murshudov, 2013; Winn et al., 2011) to obtain complete datasets. The resolution cut-off of each structure was defined based on CC1/2 values of 0.3 and above (Karplus and Diederichs, 2012; Karplus and Diederichs, 2015). Initial phases for all structures were determined by molecular replacement in PHENIX (Version 1.17.1–3660) (Liebschner et al., 2019) using an occluded structure of DraNramp (PDB ID 6C3I chain A) (Bozzi et al., 2019b) as search model. Data statistics are listed in Table 1 and Supplementary file 1b and d.

### Model building, refinement, and analysis

Models were built in COOT (Version 7.0) (Emsley et al., 2010) and refined in PHENIX (Liebschner et al., 2019), with macrocycles including reciprocal space, TLS groups, and individual B-factor refinement, and optimization of the X-ray/stereochemistry and X-ray/ADP weights. For WT•Cd2+, ‘anomalous group refinement’ was used to improve the fit to density of the Cd2+ ions, with Cd2+ as an ‘anomalous group’ with the reference f’ and f” values suggested by phenix.form.factor (–0.462 and 2.132, respectively). Ligand restraints for monoolein and spermidine were generated in Phenix.elbow with automatic geometry optimization. All structures contain one protein molecule in the asymmetric unit. The final structures span from residues 45–48 to residues 433–436, except that residues 240–249 and 240–247 were not modeled in D296•Mn2+ and WT•Cd2+, respectively, because of lack of interpretable electron density map. Model refinement statistics are listed in Table 1 and Supplementary file 1b and d. Pairwise RMSD for all structures are listed in Supplementary file 1c. Anomalous difference Fourier maps for Mn2+ (D296A•Mn2+ and A47W•Mn2+) and Cd2+ (WT•Cd2+) were generated in phenix.maps using a high-resolution cutoff of 3.5–4.5 Å. Polder maps omitting the metal ions were generated in phenix.polder to appropriately define the coordination sphere for Mn2+ and Cd2+ in all structures. All software were provided by SBGrid (Morin et al., 2013).

### Metal binding measurements using ITC

ITC experiments were performed using MicroCal iTC200 (GE Healthcare) to determine the affinity and thermodynamic parameters of binding of divalent metals (Mn2+, Cd2+ and Mg2+) to DraNramp (WT and its mutants) (Leavitt and Freire, 2001; Wiseman et al., 1989). All protein and metal solutions were prepared in ITC buffer (150 mM NaCl, 10 mM HEPES, pH 7.5, and 0.003% LMNG). The sample cell containing 25 μM protein was titrated with 20 2 μL injections of 6 mM metal, with an interval of 120 s between each successive 5 s injection, with a 750 rpm stirring rate at 25 °C. To nullify the heat of dilution, the data from titration of a metal solution into ITC buffer (‘buffer blank’ runs) were subtracted from the metal-protein titration curves prior to model fitting. Data were fitted and analyzed as detailed in Appendix 1. Briefly, as per best practice when c values (association constant × molar protein concentration) are below 1 (Picollo et al., 2009; Tellinghuisen, 2008; Turnbull and Daranas, 2003), all the data reported for each construct are fitted fixing the number of sites (one-site binding model with fixed n=1 or sequential binding model with fixed n=2). The binding stoichiometry was selected based the model fits and knowledge from the crystal structures and mutational analysis. Data were fitted with Origin 7 software. The mean Kd values ± SEM from 2 to 3 repeats (from independent protein purifications) for each sample are reported in Supplementary file 1g.

### Proteoliposome-based in vitro transport assays

Protein purification, liposome preparation, and metal transport assays were performed as described (Bozzi et al., 2016a; Bozzi et al., 2019a). Purifications of each protein construct were performed at least twice and resulted in similar data. For each construct, the presented data originates from two to three batches of reconstituted liposomes, each from an independent protein purification, represented as scatter plots of each data point and the corresponding mean.

### Sequence alignments

We used 92 Nramp sequences from Pfam (El-Gebali et al., 2019) to build a seed alignment using MUSCLE (Edgar, 2004). We collected 15,451 sequences from Uniprot (Bateman et al., 2021) using HMMER (Potter et al., 2018). We used HMMER’s hmmalign, with a hidden Markov model profile from the seed alignment as an input, to align all 15,451 sequences. We applied filters to retain sequences 400–600 residues in length and sequences with under 90% pairwise sequence identity, respectively. The final alignment contains 6712 sequences and is well aligned at biologically relevant residues (Figure 1—source data 1). A maximum-likelihood phylogenetic tree was generated via RAxML-NG Kozlov et al., 2019 using the LG substitution model (Le and Gascuel, 2008), with the likeliest final tree selected from 10 parallel optimization trials (Figure 1—source data 2). The canonical Nramp clade in this tree was identified based on conservation of the ‘DPGN’ and ‘MPH’ motifs in transmembrane helices 1 and 6, respectively, and contained 3796 sequences. The Nramp-related magnesium transporters were used to root the canonical Nramp phylogeny. Sequence analysis was done with Biopython (Cock et al., 2009) and sequence logos were generated with logomaker (Tareen and Kinney, 2020) using a ‘chemistry’ color scheme inspired by WebLogo (Crooks et al., 2004).

### Molecular dynamics simulation

Molecular dynamics (MD) simulations were initialized from three high-resolution structures of DraNramp: the outward-open G223W•Mn2+ structure (6BU5) with Mn2+ removed and W223 mutated back to the native glycine residue in silico, the inward-open WT•Cd2+ structure with Cd2+ removed, and the inward-occluded WT structure. Crystallographic waters were retained, and protonation states of key titratable residues were selected with PROPKA (Olsson et al., 2011; Søndergaard et al., 2011) assuming a pH of 5.0 for residues exposed to external solvent and a pH of 7.0 for residues exposed to cytosol, a condition under which DraNramp exhibits high activity. All structures were oriented in the membrane with the PPM web server and membrane systems were prepared with CHARMM-GUI (Jo et al., 2008; Lee et al., 2016). A POPC membrane of surface area 99×99 Å was constructed in the XY plane around the protein (Wu et al., 2014), the system was solvated in a 100×100×100 Å3 rectangular box using TIP3 waters and electronically neutralized using potassium and chlorine ions at an overall concentration of 150 mM. The overall system size was approximately 103,000 atoms.

All-atom simulations were run using GPU-accelerated NAMD (Phillips et al., 2008) and the CHARMM36m forcefield (Huang et al., 2017). Prior to simulation, the energy of each system was minimized for 10,000 steps using a conjugate gradient and line search algorithm native to NAMD. To improve simulation stability, the system was initially equilibrated using an NVT-ensemble with harmonic restraints placed on protein and lipid heavy atoms. The harmonic restraints were then incrementally relaxed over a period of 675 ps according to established CHARMM-GUI protocols (Lee et al., 2016). The system was then simulated at a constant pressure, utilizing the Langevin piston method to maintain 1 atm at 303.15 K, from anywhere between 617 and 1176 ns depending on the starting conformation. Simulations were performed using periodic boundary conditions and a time step of 3.0 fs with all bonds to hydrogens being constrained. Large integration timesteps were enabled by employing hydrogen mass repartitioning (Hopkins et al., 2015). Long-range electrostatic interactions were calculated using the particle mesh Ewald (PME) method with nonbonded interactions being cut off at 12 Å. Each simulation was performed in duplicate resulting in approximately 2 µs of total sampling for each system. Simulations are summarized in Supplementary file 1i.

RMSD, residue distance, and dihedral analyses were performed using mdtraj version 1.9.8 (McGibbon et al., 2015). For distance analysis, the minimum interatomic distances were identified between the specified residues across each frame. For water analysis, simulations were centered and wrapped in VMD and a Tcl script was used to produce water density maps. Contour maps of these densities were then visualized in PyMOL. Water occupancies of sites coordinated by specific residues were also calculated in an alignment-agnostic manner by determining for each frame in each simulation whether a water was present within 2.5 Å of both specified residues. Distinct rotamers were identified from dihedrals using spectral clustering as implemented in scikit-learn version 1.0.

### Data availability

Atomic coordinates and structure factors for the crystal structures reported in this work have been deposited to the Protein Data Bank under accession numbers 8E5S (WT), 8E5V (WTsoak), 8E60 (WT•Mn2+), 8E6H (A47W•Mn2+), 8E6I (M230A•Mn2+), 8E6L (D296A•Mn2+), 8E6M (WT•Cd2+), and 8E6N (re-refined G223W•Mn2+). Corresponding X-ray diffraction images have been deposited to the SBGrid Data Bank under the respective accession numbers 962 (doi:10.15785/SBGRID/962), 963 (doi:10.15785/SBGRID/963), 964 (doi:10.15785/SBGRID/ 964), 966 (doi:10.15785/SBGRID/966), 967 (doi:10.15785/SBGRID/967), 968 (doi:10.15785/SBGRID/968), 969 (doi:10.15785/SBGRID/969), and previously deposited 564 (doi:10.15785/SBGRID/564). The multiple sequence alignment and phylogenetic tree have been provided as Figure 1—source data 1 and Figure 1—source data 2, respectively. All liposome-based transport data are provided in Figure 1—source data 3. Code for analysis of molecular dynamics data, as well as the raw data plotted in Figure 4—figure supplement 2 and Figure 4—figure supplement 3, can be found at https://github.com/samberry19/nramp-md (MIT license). Raw molecular dynamics trajectory files are available on Dryad (https://doi.org/10.5061/dryad.tx95x6b2b). Source files (origin files) of all ITC experiments are provided in Appendix 1—table 1—source data 1 (Mn2+ isotherms), Appendix 1—table 2—source data 1 (Cd2+ isotherms) and Figure 5—source data 1(Mg2+ isotherms).
