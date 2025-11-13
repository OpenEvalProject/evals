# A structure of substrate-bound Synaptojanin1 provides new insights in its mechanism and the effect of disease mutations

## Authors

- Jone Paesmans<sup>1</sup> ([ORCID: 0000-0002-3292-4609](https://orcid.org/0000-0002-3292-4609))
- Ella Martin<sup>1</sup> ([ORCID: 0000-0002-9607-7074](https://orcid.org/0000-0002-9607-7074))
- Babette Deckers<sup>1</sup> ([ORCID: 0000-0002-3855-4776](https://orcid.org/0000-0002-3855-4776))
- Marjolijn Berghmans<sup>1</sup> ([ORCID: 0000-0002-8699-6915](https://orcid.org/0000-0002-8699-6915))
- Ritika Sethi<sup>1</sup>
- Yannick Loeys<sup>1</sup>
- Els Pardon<sup>1</sup> ([ORCID: 0000-0002-2466-0172](https://orcid.org/0000-0002-2466-0172))
- Jan Steyaert<sup>1</sup> ([ORCID: 0000-0002-3825-874X](https://orcid.org/0000-0002-3825-874X))
- Patrik Verstreken<sup>3</sup>
- Christian Galicia<sup>1</sup> ([ORCID: 0000-0001-6080-7533](https://orcid.org/0000-0001-6080-7533)) †
- Wim Versées<sup>1</sup> ([ORCID: 0000-0002-4695-696X](https://orcid.org/0000-0002-4695-696X)) †

### Affiliations

1. VIB-VUB Center for Structural Biology Brussels Belgium
2. Structural Biology Brussels, Vrije Universiteit Brussel Brussels Belgium
3. VIB-KU Leuven Center for Brain and Disease Research Leuven Belgium
4. KU Leuven, Department of Neurosciences, Leuven Brain Institute Leuven Belgium

† Corresponding author

## Abstract

Synaptojanin1 (Synj1) is a phosphoinositide phosphatase, important in clathrin uncoating during endocytosis of presynaptic vesicles. It was identified as a potential drug target for Alzheimer’s disease, Down syndrome, and TBC1D24-associated epilepsy, while also loss-of-function mutations in Synj1 are associated with epilepsy and Parkinson’s disease. Despite its involvement in a range of disorders, structural, and detailed mechanistic information regarding the enzyme is lacking. Here, we report the crystal structure of the 5-phosphatase domain of Synj1. Moreover, we also present a structure of this domain bound to the substrate diC8-PI(3,4,5)P3, providing the first image of a 5-phosphatase with a trapped substrate in its active site. Together with an analysis of the contribution of the different inositide phosphate groups to catalysis, these structures provide new insights in the Synj1 mechanism. Finally, we analysed the effect of three clinical missense mutations (Y793C, R800C, Y849C) on catalysis, unveiling the molecular mechanisms underlying Synj1-associated disease.

## Introduction

Phosphoinositides (PIPs) are membrane lipids that, together with their corresponding soluble inositol phosphates (IPs), regulate various cellular processes, including membrane recruitment of proteins, actin polymerization, synaptic vesicle trafficking and exo- and endocytosis (Di Paolo and De Camilli, 2006; Balla, 2013; Ueda, 2014). The dynamic control of the membrane distribution and relative abundance of the seven naturally occurring PIPs by a multitude of phosphoinositide kinases and phosphatases forms a versatile signaling mechanism able to tune the spatial and temporal regulation of many crucial events in the cell (Fruman et al., 1998; Anderson et al., 1999; Hsu and Mao, 2015).

The inositol polyphosphate 5-phosphatases (5PPases) form a family of Mg2+-dependent enzymes, containing ten members in mammals, that catalyse the hydrolytic removal of the phosphate group on the 5-position of lipid-bound and soluble inositol phosphates (Figure 1, Figure 1—figure supplement 1). Based on their substrate specificity, the mammalian 5PPases can be further subdivided into four groups (Majerus et al., 1999): the type I 5PPase INPP5A (Speed et al., 1996), the type II 5PPases OCRL, INPP5B, INPP5J (or PIPP), SKIP, Synaptojanin1 (Synj1) and Synaptojanin 2 (Synj2) (Lowe, 2005; Trésaugues et al., 2014; Mochizuki and Takenawa, 1999; Ijuin et al., 2000; McPherson et al., 1996; Nemoto et al., 1997), the type III 5PPases, SHIP1 and SHIP2 (Rohrschneider et al., 2000; Le Coq et al., 2017), and the type IV 5PPase INPP5E (or Pharbin) (Asano et al., 1999). Among the type II 5PPases, the closely related Synj1 and Synj2 contain a similar domain arrangement, with in addition to the central 5PPase domain, an N-terminal suppressor of actin 1 (SAC1)-like domain and a C-terminal proline-rich domain (PRD). As such, Synj1 and Synj2 are unique in having two phosphatase activities, where the 5PPase domains can hydrolyse PI(4,5)P2, PI(3,4,5)P3, IP3, and IP4, while the SAC1-like domain can degrade PI(3)P, PI(4)P, and PI(3,5)P2 (Hsu and Mao, 2015; Cestra et al., 1999; Whisstock et al., 2002). Both Synaptojanin proteins are implicated in clathrin-mediated endocytosis, where Synj2 is involved in the early stages of this process (Rusk et al., 2003), while the brain-specific 145 kDa splice isoform of Synj1 promotes clathrin uncoating during the late stages of endocytosis (Perera et al., 2006; Ramjaun and McPherson, 1996). In agreement with this role, knock-out studies of Synj1 in mice (Cremona et al., 1999) and Drosophila melanogaster (Verstreken et al., 2003) show endocytic defects at the neuronal synapses, indicating that Synj1 plays a critical role in synaptic function. This key function at the synapse is further illustrated by the implication of Synj1 in several diseases. Brain autopsy of Down syndrome (DS) patients revealed an excessive expression of the Synj1 protein, that is encoded on the triplicated chromosome 21, and it was shown that the overexpression of Synj1 leads to PI(4,5)P2 deficiency and learning deficits in Down syndrome model mice (Voronov et al., 2008; Arai et al., 2002). Elevated levels of Synj1 are also found in individuals showing a high risk for the development of Alzheimer's disease (AD) (Berman et al., 2008; Martin et al., 2015; Miranda et al., 2018). Based on these findings, Synj1 has been proposed as a potential attractive two-faced target for novel DS and AD treatments (Cossec et al., 2012). Additionally, inhibition of the 5-phosphatase activity of Synj1 has also been found to hold promise toward drug development for TBC1D24-associated epilepsy and DOORS syndrome (Fischer et al., 2016; Lüthy et al., 2019). On the other hand, recessive loss-of-function mutations in Synj1 are associated with either early-onset atypical parkinsonism or refractory epileptic seizures with severe progressive neurodegeneration (Hardies et al., 2016; Xie et al., 2019; Taghavi et al., 2018; Hong et al., 2019; Bouhouche et al., 2017).

![Figure 1.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig1-v2.jpg)

**Figure 1.:** The domain organization of the ten human 5PPases, subdivided in four groups (type I–IV), is shown schematically. The different splice forms for Synaptojanin 1 (Synj1) and 2 (Synj2) are also shown. The domain boundaries of the 5PPase domain of Synj1 145 kDa used in this study and the disease mutations under study are indicated. 5PPase = 5-phosphatase domain; PH = Pleckstrin homology domain; ASH = ASPM, SPD-2, Hydin domain; Rho-GAP = Rho GTPase-activating protein domain; CB = clathrin-binding domain; PRD = proline-rich domain; SKICH = SKIP carboxyl homology domain; SAC1 = suppressor of actin 1-like domain; RRM = RNA recognition motif; SH2 = Src homology two domain; SAM = sterile alpha motif.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The sequence alignment of the 5PPase domain of all human 5PPases and SPSynj was obtained via Clustal Omega (https://www.ebi.ac.uk/Tools/msa/clustalo/). Secondary structure assignment was performed using ESPript (http://espript.ibcp.fr/ESPript/ESPript/). Residues important for substrate or metal-ion interactions are indicated as described in the figure legend. The loop containing the P4-interacting-motif (P4IM) and the lipid chain 1 (LC1R) and 2 (LC2R) recognition motifs are indicated by magenta, green-blue, and cyan lines, respectively. Completely conserved residues are indicated by a red background and residues that show similarity across the 5PPases are written in red. Similar sequence motifs are indicated with a blue square. α-helices and 310-helices are displayed as helices and indicated by α or η respectively. β-strands are displayed as arrows and strict β-turns as TT.

Out of the ten 5PPase domains present in human, high-resolution structural information has only been published for three representatives: INPP5B, OCRL, and SHIP2 (Trésaugues et al., 2014; Mills et al., 2016). In addition, an unpublished structure of INPP5E has been deposited in the protein data bank (PDB 2XSW). So far no experimentally determined structure is available for the 5PPase domain of either Synj1 or Synj2, although the very first 5PPase structure ever to be determined was the one of a Synaptojanin homolog of the yeast Schizosaccharomyces pombe (Tsujishita et al., 2001).

In addition to the structural data of the 5PPase domains in their apo form, crystal structures in complex with reaction products and inhibitors, together with detailed studies on the structurally and mechanistically related Apurinic/Apyrimidinic endonucleases (APE), have yielded some insights in the catalytic mechanism of the hydrolysis reaction (Whisstock et al., 2000). Indeed, structural and sequence comparison revealed similarities in the active site architecture of the 5PPases and APE1, a Mg2+-dependent enzyme that catalyses the cleavage of the phosphodiester bond on the 5’ side of the abasic site in DNA using a conserved aspartate as catalytic base and a conserved histidine that presumably stabilizes the phosphorane transition state. Moreover, leaving group activation has been proposed to occur via a Mg2+-bound water molecule, although the exact role of the Mg2+-ion in the catalytic mechanism of 5PPases has not been fully established (Trésaugues et al., 2014; Mills et al., 2016; Aboelnga and Wetmore, 2019). A crystal structure of the S. pombe Synaptojanin (SPSynj) homolog in complex with inositol-(1,4)-bisphosphate provided a first snapshot of a potential enzyme-product complex (Tsujishita et al., 2001). However, subsequent structures of the catalytic domain of INPP5B in complex with diC8-PI(4)P and diC8-PI(3,4)P2 revealed another orientation of these reaction products, suggesting that the placement of the ligand in the SPSynj structure does not correspond to the genuine position of the product (Trésaugues et al., 2014). Further elucidation of the complete hydrolysis mechanism is however hampered by the lack of 5PPase structures in complex with reaction substrates showing directly the exact placement of the 5-phosphate group in the active site.

In this study we report the first structure of the catalytic 5PPase domain of human Synj1 by using Nanobody-aided crystallography. Moreover, we were able, for the first time, to solve a structure of a 5PPase domain with the substrate diC8-PI(3,4,5)P3 trapped in its active site, revealing the placement of, and the interactions with, the 5-phosphate group. In combination with a detailed kinetic analysis of the hydrolysis reaction catalysed by the Synj1 5PPase domain, these structures provide additional insights in the catalytic mechanism. Finally, we investigated in detail the effect of the three currently described homozygous missense mutations in the 5PPase domain (Y793C, R800C, Y849C) associated with either (young onset) Parkinson’s disease or intractable epilepsy with neurodegeneration (Hardies et al., 2016; Xie et al., 2019; Taghavi et al., 2018) on the reaction rate for different substrates, thus providing insights in the molecular mechanisms underlying these diseases.

## Results

### The crystal structure of the 5-phosphatase domain of Synj1 and its complex with the substrate diC8-PI(3,4,5)P3

Since structural information regarding the 5-phosphatase (5PPase) domain of human Synj1 is currently lacking, we set-out to crystallize a construct of the 5PPase domain spanning residues 528–873 (Synj1528–873). Upon multiple unsuccessful attempts to obtain well diffracting crystals, we turned to Nanobody (Nb)-assisted crystallization. After llama immunization, library construction and two successive rounds of phage display panning, six Synj1528–873-specific Nb families were obtained (data not shown). Various Synj1528–873-Nb complexes were used to set-up crystallization screens and well diffracting crystals belonging to space group C121 were obtained for the complex between Synj1528–873 and Nb13015 (hereafter called Nb15).

The first dataset was collected and refined at 2.3 Å resolution (Table 1). The structure was solved using molecular replacement, revealing three Nb15-Synj1528–873 complexes in each asymmetric unit (AU) (Figure 2—figure supplement 1A). Since Synj1528–873 consistently behaves as a monomer in solution, as assessed through gel filtration, it can be assumed that the three complexes in the AU are merely interacting via crystallographic contacts. Despite being soaked overnight with IP6 (inositol-1,2,3,4,5,6-hexakisphosphate), no density accounting for this molecule was observed in the active site, and therefore we will further refer to this structure as an apo-structure. However, several blobs of density in the structure could be modelled as orthophosphates, suggesting that these result from hydrolysis of IP6 (Figure 2—figure supplement 2). Furthermore, all three Synj1528–873 molecules contain density close to N543 and E591, which corresponds to the position of a Mg2+-ion in other 5PPase structures (Trésaugues et al., 2014), and which was therefore also here modelled as Mg2+-ions (Figure 2—figure supplement 2). While these Mg2+-ions were modelled at a very similar position as in the structure of INPP5B in complex with the product diC8-PI(3,4)P2 (Trésaugues et al., 2014), it must be noted that the distances to residues N543 and E591 are rather long.

**Table 1.**
 Data collection and refinement statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Synj1528–873 - Apo</th>
      <th>Synj1528–873 - diC8-PI(3,4,5)P3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PDB code</td>
      <td>7A0V</td>
      <td>7A17</td>
    </tr>
    <tr>
      <td>Data collection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Synchrotron</td>
      <td>Diamond</td>
      <td>Soleil</td>
    </tr>
    <tr>
      <td>Beamline</td>
      <td>i03</td>
      <td>Px2a</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.98</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>Resolution range (Å)*</td>
      <td>87.06–2.30 (2.43–2.30)</td>
      <td>87.39–2.73 (3.02–2.73)</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>C121</td>
      <td>C121</td>
    </tr>
    <tr>
      <td>Unit cell dimensions (Å)</td>
      <td>a = 168.87</td>
      <td>a = 169.32</td>
    </tr>
    <tr>
      <td></td>
      <td>b = 108.79</td>
      <td>b = 109.21</td>
    </tr>
    <tr>
      <td></td>
      <td>c = 100.97</td>
      <td>c = 100.90</td>
    </tr>
    <tr>
      <td>Unit cell angles (°)</td>
      <td>α = 90.00</td>
      <td>α = 90.00</td>
    </tr>
    <tr>
      <td></td>
      <td>β = 120.72</td>
      <td>β = 120.62</td>
    </tr>
    <tr>
      <td></td>
      <td>γ = 90.00</td>
      <td>γ = 90.00</td>
    </tr>
    <tr>
      <td>Spherical completeness (%)*</td>
      <td>77.1 (26.4)</td>
      <td>76.2 (22.8)</td>
    </tr>
    <tr>
      <td>Ellipsoidal completeness (%)*</td>
      <td>92.3 (95.0)</td>
      <td>91.5 (57.3)</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>53789</td>
      <td>32149</td>
    </tr>
    <tr>
      <td>Mean (I)/SD(I)*</td>
      <td>11.2 (1.4)</td>
      <td>5.3 (1.4)</td>
    </tr>
    <tr>
      <td>CC(1/2)*</td>
      <td>0.997 (0.512)</td>
      <td>0.964 (0.474)</td>
    </tr>
    <tr>
      <td>Multiplicity*</td>
      <td>7.0 (5.7)</td>
      <td>3.5 (3.6)</td>
    </tr>
    <tr>
      <td>Rmeas (%)*</td>
      <td>14.5 (125.1)</td>
      <td>28.2 (123.7)</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution range (Å)</td>
      <td>86.81–2.30</td>
      <td>86.83–2.73</td>
    </tr>
    <tr>
      <td>Rwork (%)</td>
      <td>19.64</td>
      <td>19.88</td>
    </tr>
    <tr>
      <td>Rfree (%)†</td>
      <td>25.23</td>
      <td>25.74</td>
    </tr>
    <tr>
      <td>Model content</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Molecules per AU</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Protein atoms per AU</td>
      <td>10574</td>
      <td>10624</td>
    </tr>
    <tr>
      <td>Ligand atoms per AU</td>
      <td>39</td>
      <td>85</td>
    </tr>
    <tr>
      <td>Metal atoms per AU</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Water molecules per AU</td>
      <td>359</td>
      <td>71</td>
    </tr>
    <tr>
      <td>Wilson B factors (Å2)</td>
      <td>38.08</td>
      <td>43.28</td>
    </tr>
    <tr>
      <td>Average B factors (Å2)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein atoms</td>
      <td>47.35</td>
      <td>44.88</td>
    </tr>
    <tr>
      <td>Ligand atoms</td>
      <td>65.62</td>
      <td>67.11</td>
    </tr>
    <tr>
      <td>Metal atoms</td>
      <td>60.08</td>
      <td>42.62</td>
    </tr>
    <tr>
      <td>Water molecules</td>
      <td>42.68</td>
      <td>22.93</td>
    </tr>
    <tr>
      <td>Rmsd bonds (Å)</td>
      <td>0.002</td>
      <td>0.006</td>
    </tr>
    <tr>
      <td>Rmsd angles (°)</td>
      <td>0.456</td>
      <td>1.15</td>
    </tr>
    <tr>
      <td>Ramachandran plot (%) (favored, outliers)</td>
      <td>95.79, 0.23</td>
      <td>97.00, 0.46</td>
    </tr>
  </tbody>
</table>

_* Values in parentheses are for the high-resolution shell.† Rfree is based on a subset of 5% of reflections omitted during refinement.AU, asymmetric unit._

Superposition of the three Synj1528–873 molecules present in the AU shows that they are very similar, with root-mean square deviations (rmsd) for superposition of all main chain atoms of chain A on chain C and E of 0.69 Å and 0.49 Å, respectively (Figure 2—figure supplement 1B). Overall, Synj1528–873 adopts a fold that is very similar to the fold of the catalytic domain of other 5-phosphatases (Figure 2—figure supplement 3, Supplementary file 1A), and is composed of two β sheets forming a β-sandwich surrounded by seven α-helices (Figure 2A; Trésaugues et al., 2014; Tsujishita et al., 2001). Nb15 forms interactions via its three CDR loops with a loop and short 310-helix (aa 641–654) connecting β4 and β5 of Synj1528–873, on the opposite side of the 5PPase active site, thus leaving the active site open for ligand binding (Figure 2A).

![Figure 2.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig2-v2.jpg)

**Figure 2.:** (A) Apo-structure of the Nb15-Synj1528–873 complex. Synj1528–873 (chain E) is represented in different shades of magenta, while the Nb (chain F) is represented in grey with indication of the different CDR regions. The Mg2+-ion is shown as a salmon sphere. (B) The Nb15-Synj1528–873 complex bound to diC8-PI(3,4,5)P3. Synj1528–873 (chain A) is represented in different shades of green, while the Nb (chain B) is represented similar as in (A). The Mg2+-ion is shown as an orange sphere and diC8-PI(3,4,5)P3 is shown as yellow sticks. (C) Zoom-in on the active site region of Synj1528–873 with bound diC8-PI(3,4,5)P3 (yellow sticks), Mg2+ (orange sphere) and the nucleophilic water molecule (red sphere) shown with their corresponding 2FO-FC-map contoured at 1σ. Residues D730 and N732, which play a role in the activation of the nucleophilic water, are shown as green sticks. (D) Superposition of the apo (magenta) and diC8-PI(3,4,5)P3-bound (green) Synj1528–873 structure.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The asymmetric unit (AU) of both structures contains three Nb15-Synj1528–873 complexes. (A) AU of the apo-structure. (B) Superposition of the three Synj1528–873 chains from the apo-structure. (C) AU of the diC8-PI(3,4,5)P3-bound structure. (D) Superposition of the three Synj1528–873 chains from the diC8-PI(3,4,5)P3-bound structure. Mg2+-ions are represented as orange, yellow, and salmon spheres for chain A, C, and E, respectively. diC8-PI(3,4,5)P3, free phosphates, and glycerol are shown as sticks in yellow, orange, and purple, respectively.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** The close-up views of the different Synj1528–873 chains of the apo-structure are show on the left, while the same chains of the diC8-PI(3,4,5)P3-bound structure are shown on the right. The Mg2+-ions are shown as orange, yellow or salmon spheres for chain A (green), chain C (cyan) of chain E (magenta), respectively. The Mg2+-interacting residues, N543 and E591, are shown as sticks in every chain. In chain A of the diC8-PI(3,4,5)P3-bound Synj1528–873 structure (top right panel) residues D730 and N732, which play a direct role in activation of the nucleophilic water (red sphere), are also shown as sticks. Free orthophosphates and the substrate diC8-PI(3,4,5)P3 are shown as orange and yellow sticks, respectively. The omit map, contoured at 3 σ, is shown as a grey mesh around the phosphates, Mg2+-ions, diC8-PI(3,4,5)P3 and the nucleophilic water.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Superposition of Synj1528–873 (green, PDB 7A17) on the 5PPase domain of (A) INPP5B (magenta, PDB 4CML), (B) SHIP2 (blue, PDB 4A9C), (C) OCRL (salmon, PDB 4CMN), (D) INPP5E (grey, PDB 2XSW) and (E) SPSynj (cyan, PDB 1I9Z). The Mg2+-ion and the diC8-PI(3,4,5)P3 substrate of the Synj1528–873 structure are shown as an orange sphere and yellow sticks, respectively. (F) Zoom-in on the active site of the superposed 5PPases described in (A to E). For clarity, only the Mg2+-ion and the diC8-PI(3,4,5)P3 substrate of the Synj1528–873 structure are shown as an orange sphere and yellow sticks, respectively.

A second crystal of the Nb15-Synj1528–873 complex, was soaked with 1 mM diC8-PI(3,4,5)P3 and data were collected and refined at 2.73 Å resolution (Table 1). Analysis of the electron density in the active sites of the three molecules in the asymmetric unit revealed that one active site (corresponding to chain A) contains unambiguous density for the diC8-PI(3,4,5)P3 substrate including the scissile 5-phosphate group (Figure 2B–C, Figure 2—figure supplement 1C, Figure 3), thus showing that we were able to trap the non-hydrolysed substrate by using a strategy of short substrate soaking followed by flash freezing and assisted by the slower substrate turnover under the conditions used for crystallization (Figure 4—figure supplement 1, Figure 4—figure supplement 1—source data 1). The other two Synj1528–873 active sites (corresponding to chain C and E) contain weaker and discontinuous electron density, probably due to substrate already being hydrolysed to a larger extent because of subtle differences in kinetics of substrate access/hydrolysis and product release in these sites depending on the local environment of the crystal packing. The electron density in these active sites was modelled as phosphate ions, with three phosphates in chain C at positions corresponding to the 1-, 4-, and 5-phosphates of diC8-PI(3,4,5)P3, while in chain E only a single phosphate could be modelled between the expected position of the phosphates present on the 4- and 5-position of the substrate (Figure 2—figure supplement 2). Analysis of the density revealed that two out of three Synj1528–873 molecules (chain A and C) also show density close to residues N543 and E591, where Mg2+-ions were modelled (Figure 2—figure supplement 2). Despite the difference in the occupancy of diC8-PI(3,4,5)P3 in the active sites, superposition of the Synj1528–873 molecules (corresponding to chain A, C, and E) does not reveal any large differences in active site loops and residues, indicating that no significant substrate-induced conformational changes take place (Figure 2D).

![Figure 3.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig3-v2.jpg)

**Figure 3.:** (A) Zoom-in on the active site where Synj1528–873 forms interactions with different groups of the diC8-PI(3,4,5)P3 substrate (yellow sticks). The residues coloured in gold are forming interactions with the 1 P group or inositol ring of the PIP (gold dashes), residues coloured in magenta form interactions with the 4 P group (magenta dashes), and residues shown in green are interacting with the 5 P group (green dashes). Residues important for activation of the nucleophilic water (red sphere) are shown in cyan, while two residues shown in salmon are interacting with the Mg2+-ion (orange sphere). (B) Schematic representation of the interactions between Synj1528–873 and diC8-PI(3,4,5)P3. The same colour-code as in (A) was used, except for the substrate that is shown in black. Distances (in Å) between interacting atoms are indicated.

### Enzyme-substrate interactions in the Synj1528–873– diC8-PI(3,4,5)P3 complex

The current crystal structure of Synj1528–873 bound to diC8-PI(3,4,5)P3 provides the first experimental structural view of any inositol polyphosphate 5-phosphatase (5PPase) in complex with a trapped genuine substrate, allowing us to describe and analyse the enzyme-substrate interactions in detail.

In particular, the Synj1528–873-diC8-PI(3,4,5)P3 structure for the first time reveals the exact location and interactions with the scissile phosphate (5 P). This phosphate is oriented towards two regions previously described to correspond to conserved sequence motifs characteristic for the 5PPase family: WXGDXN(Y/F)R (residues 727–734) and P(A/S)W(C/T)DR(I/V)L (residues 802–809) (Jefferson and Majerus, 1996), while it also interacts with a number of other highly conserved active site residues (Figure 3, Figure 1—figure supplement 1, Figure 2—figure supplement 3, Supplementary file 1B). The first oxygen of 5 P (OPH) is within hydrogen bonding distance of N732 (3.0 Å), while it is also appropriately oriented to form a weak hydrogen bond or salt bridge with H689 (3.6 Å). The second oxygen of 5 P (OPF) can form a (weak) salt bridge or hydrogen bond with H859 (3.3 Å). The OPF oxygen is also oriented towards the Mg2+-ion, although, in contrast to what was previously suggested (Trésaugues et al., 2014), the Mg2+-OPF distance of 4.7 Å is too long to account for a direct metal coordination interaction. The third oxygen of 5 P (OPG) potentially forms a weak hydrogen bond with Y784 (3.5 Å) and an electrostatic interaction with R734 (3.5 Å) (Figure 3). D730 and N732 form a pair of conserved residues belonging to one of the conserved sequence motifs of the 5PPase family. It has previously been shown that D730 corresponds to the general base required to activate a water molecule for nucleophilic attack on P5. Analysis of the electron density shows such a water molecule, located at 3.1 Å from D730 and 3.5 Å from the P5-atom (Figure 2C and 3). Additionally, the structure also reveals a hydrogen bond between the water molecule and N732 (2.6 Å), probably required for proper orientation of the water molecule for nucleophilic attack. This thus shows a direct role of the D730/N732 pair in activation of the nucleophilic water.

The phosphate on position 4 (4 P) forms extensive interactions with the enzyme through the conserved P4-interacting-motif (P4IM), containing Y784, K798, and R800 (Figure 3; Figure 1—figure supplement 1; Trésaugues et al., 2014; Mills et al., 2012). These multiple binding interactions explain the preference of Synj1528–873 and most other 5PPases for substrates phosphorylated on the 4-position (Schmid et al., 2004). In addition, the Mg2+-ion is located at a distance of 3.6 Å from the O9P-atom of the 4 P group. It is also noteworthy that a non-proline cis peptide bond is found between active site residues Y784 and K785, belonging to the P4IM region. This cis peptide bond is also conserved in the structure of OCRL, INPP5B, SHIP2, and INPP5E, and, while it was not modelled as such in the SPSynj structure, the density can account for a cis peptide in that latter structure. While the occurrence of such bonds is mostly of functional importance (Jabs et al., 1999), the exact relevance to the 5PPase mechanism is not entirely clear as it is found both in the apo and ligand-bound structures.

In contrast to the 4 P and 5 P groups, the phosphate on position 3 (3 P) is solvent exposed and does not form any interaction with enzyme residues. The only direct contacts between Synj1528–873 and the inositol group of diC8-PI(3,4,5)P3 are mediated by a weak Van der Waals interaction (3.8 Å) between the β-carbon of A692 and the C5 atom of the inositol ring (Figure 3). Additionally, K669 is located at 2.8 Å from the OH-group on position 6 of the inositol ring, forming a hydrogen bond. Besides the inositol ring, also the phosphate on position 1 (1 P) is commonly used by all 5PPases for substrate recognition and binding (Figure 2—figure supplement 3, Supplementary file 1B). In our structure, the 1 P of diC8-PI(3,4,5)P3 forms strong interactions with the side chains of N668 (2.2 Å) and K669 (2.7 Å) (Figure 3). Finally, the lipid anchors of diC8-PI(3,4,5)P3 are interacting with two hydrophobic regions, as also described for other 5PPases (Trésaugues et al., 2014; Mills et al., 2012). The first region is formed by residues V593 to T606 and has been called lipid chain 1 recognition motif (LC1R), while the second region is formed by residues T660 to N668 and has been called lipid chain 2 recognition motif (LC2R) (Figure 1—figure supplement 1; Trésaugues et al., 2014).

### Kinetic analysis of the Synj1 5-phosphatase activity

A detailed and systematic kinetic analysis of the contribution of the different phosphate groups of the phosphoinositide substrate to Synj1 catalysis is currently lacking. To investigate the contribution of the different inositol phosphate groups (3 P, 4 P, and 5 P) and the Mg2+-cofactor on binding and substrate turnover, we therefore performed a full steady-state kinetic analysis of Synj1528–873, using IP3, diC8-PI(3,4,5)P3, diC8-PI(4,5)P2, diC8-PI(3,5)P2, and diC8-PI(5)P as substrates (Figure 4A, Table 2, Figure 4—source data 1).

![Figure 4.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig4-v2.jpg)

**Figure 4.:** (A) Michaelis-Menten curves obtained for Synj1528–873 with different substrates: diC8-PI(3,4,5)P3, diC8-PI(4,5)P2, diC8-PI(3,5)P2, diC8-PI(5)P, IP3, and diC8-PI(4,5)P2 in the absence of Mg2+. The turnover number (kcat), the Michaelis-Menten constant (KM) and specificity constant (kcat/KM) are given for every measurement, together with the standard error. Each datapoint is the average of three independent measurements with the error bars representing the standard deviation. (B) Schematic overview of the contribution of the different groups of the diC8-PI(3,4,5)P3-substrate to the Synj1528–873 mechanism, with the acyl chains coloured in gold, the 3 P group in blue, the 4 P group in magenta, the 5 P group in green and the Mg2+-ion in orange. The ΔΔG value shows the contribution of the acyl chains, 3 P, 4 P, and Mg2+-ion to catalysis (kcat), binding (KM) and overall catalytic efficiency (kcat/KM). The more positive the ΔΔG value, the larger the contribution of the respective group to either catalysis, binding or overall catalytic efficiency.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Michaelis-Menten curves obtained by using the Malachite green assay with 2.5 nM of human Synj1528–873 and various concentrations of diC8-PI(3,4,5)P3 in absence or presence of 100 nM Nb15. (B) Michaelis-Menten curves obtained by using the Malachite green assay with 2.5 nM of human Synj1528–873 and various concentration of diC8-PI(3,4,5)P3 in assay buffer containing 25 mM HEPES at pH 7.5 or in assay buffer containing 25 mM sodium citrate at pH 5.5. The turnover number (kcat), the Michaelis-Menten constant (KM), and specificity constant (kcat/KM) are given for the different measurements, together with the standard error. Each datapoint is the average of three independent measurements with the error bars representing the standard deviation.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Michaelis-Menten curves obtained for Synj1528–873 Y793C with different substrates: diC8-PI(3,4,5)P3, diC8-PI(4,5)P2, diC8-PI(3,5)P2, diC8-PI(5)P, and IP3. The turnover number (kcat), the Michaelis-Menten constant (KM) and specificity constant (kcat/KM) are given for the different measurements, together with the standard error. Each datapoint is the average of three independent measurements with the error bars representing the standard deviation.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Michaelis-Menten curves obtained for Synj1528–873 R800C with different substrates: diC8-PI(3,4,5)P3, diC8-PI(4,5)P2, diC8-PI(3,5)P2, diC8-PI(5)P, and IP3. The turnover number (kcat), the Michaelis-Menten constant (KM) and specificity constant (kcat/KM) are given for the different measurements, together with the standard error. Each datapoint is the average of three independent measurements with the error bars representing the standard deviation. (B) Thermodynamic squares with corresponding ΔΔG values calculated from kcat/KM. Each ΔΔG value corresponds to the contribution of either the substituted R800 side chain or the deleted 4 P group according to ΔΔG = -R.T.ln[(kcat/KM)2 / (kcat/KM)1]. ΔΔΔG shows the difference between ΔΔG1 and ΔΔG2 or ΔΔG3 and ΔΔG4, indicating that R800 performs its role in the Synj1528–873 mechanism through the 4 P group.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Time traces monitoring the activity (change in OD620nm) of 1 µM GST-Synj1528–873 Y849C using either 120 µM diC8-PI(3,4,5)P3, diC8-PI(4,5)P2 or IP3 are shown. After measuring 1 hr, the OD620nm in function of time curve was flat, indicating that no activity could be measured. These curves were compared to the corresponding curves of the wild-type Synj1528–873 at 100- to 1000-fold lower enzyme concentration (1–10 nM).

**Table 2.**
 Steady-state kinetic parameters of Synj1528–873 and the Synj1528–873 Y793C, R800C and Y849C mutants in combination with different substrates.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>Synj1528–873</th>
      <th>Synj1528–873 Y793C</th>
      <th>Synj1528–873 R800C</th>
      <th>Synj1528–873 Y849C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">diC8-PI(3,4,5)P3</td>
      <td>kcat (s−1)</td>
      <td>30.6 ± 2.4</td>
      <td>7.6 ± 0.9</td>
      <td>21.8 ± 4.2</td>
      <td>NMA</td>
    </tr>
    <tr>
      <td>KM (µM)</td>
      <td>18 ± 5</td>
      <td>29 ± 10</td>
      <td>155 ± 49</td>
      <td>NMA</td>
    </tr>
    <tr>
      <td>kcat/KM (•103 (M•s)−1)</td>
      <td>1692 ± 474</td>
      <td>259 ± 97</td>
      <td>141 ± 52</td>
      <td>NMA</td>
    </tr>
    <tr>
      <td rowspan="3">diC8-PI(4,5)P2</td>
      <td>kcat (s−1)</td>
      <td>85.3 ± 7.0</td>
      <td>32.0 ± 3.2</td>
      <td>6.4 ± 1.2</td>
      <td>NMA</td>
    </tr>
    <tr>
      <td>KM (µM)</td>
      <td>39 ± 8</td>
      <td>117 ± 25</td>
      <td>161 ± 52</td>
      <td>NMA</td>
    </tr>
    <tr>
      <td>kcat/KM (•103 (M•s)−1)</td>
      <td>2171 ± 482</td>
      <td>274 ± 64</td>
      <td>40 ± 15</td>
      <td>NMA</td>
    </tr>
    <tr>
      <td rowspan="3">IP3</td>
      <td>kcat (s−1)</td>
      <td>16.4 ± 1.1</td>
      <td>1.5 ± 0.2</td>
      <td>0.055 ± 0.007</td>
      <td>NMA</td>
    </tr>
    <tr>
      <td>KM (µM)</td>
      <td>96 ± 20</td>
      <td>864 ± 171</td>
      <td>289 ± 78</td>
      <td>NMA</td>
    </tr>
    <tr>
      <td>kcat/KM (•103 (M•s)−1)</td>
      <td>171 ± 38</td>
      <td>1.7 ± 0.4</td>
      <td>0.19 ± 0.06</td>
      <td>NMA</td>
    </tr>
    <tr>
      <td rowspan="3">diC8-PI(3,5)P2</td>
      <td>kcat (s−1)</td>
      <td>0.09 ± 0.01</td>
      <td>0.012 ± 0.001</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
    <tr>
      <td>KM (µM)</td>
      <td>133 ± 35</td>
      <td>101 ± 25</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
    <tr>
      <td>kcat/KM (•103 (M•s)−1)</td>
      <td>0.62 ± 0.19</td>
      <td>0.12 ± 0.03</td>
      <td>0.29 ± 0.01</td>
      <td>ND</td>
    </tr>
    <tr>
      <td rowspan="3">diC8-PI(5)P</td>
      <td>kcat (s−1)</td>
      <td>ND</td>
      <td>ND</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
    <tr>
      <td>KM (µM)</td>
      <td>ND</td>
      <td>ND</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
    <tr>
      <td>kcat/KM (•103 (M•s)−1)</td>
      <td>1.45 ± 0.07</td>
      <td>0.14 ± 0.01</td>
      <td>1.2 ± 0.1</td>
      <td>ND</td>
    </tr>
    <tr>
      <td rowspan="3">diC8-PI(4,5)P2 without Mg2+</td>
      <td>kcat (s−1)</td>
      <td>0.06 ± 0.01</td>
      <td>ND</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
    <tr>
      <td>KM (µM)</td>
      <td>289 ± 85</td>
      <td>ND</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
    <tr>
      <td>kcat/KM (•103 (M•s)−1)</td>
      <td>0.22 ± 0.08</td>
      <td>ND</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
  </tbody>
</table>

_ND, not determined.NMA, no measurable activity._

Based on the overall specificity constant (kcat/KM) the following order in substrate preference is observed: diC8-PI(4,5)P2 ≈ diC8-PI(3,4,5)P3 > IP3 >> diC8-PI(5)P ≈ diC8-PI(3,5)P2. While this trend is similar to what has been previously reported based on activity measurements at a single substrate concentration (Schmid et al., 2004), it differs from the substrate preference profile of SPSynj where the following profile was found: IP3 ≈ diC4-PI(4,5)P2 > diC4-PI(3,5)P2 ≈ diC4-PI(3,4,5)P3 (Chi et al., 2004). This indicates that the yeast homolog is not an ideal model system to study the mechanism of human Synj1.

The contribution of the acyl chains to catalysis can be deduced by comparing the kinetic parameters of diC8-PI(4,5)P2 and its corresponding head group IP3 (Figure 4B). This comparison shows that diC8-PI(4,5)P2 has a nearly 13-fold higher kcat/KM value than IP3, due to a 2.5-fold higher affinity (lower KM), but mainly due to the 5-fold higher turnover rate (kcat), suggesting that the acyl chains are required to properly orient the head group in the active site for catalysis.

The contribution of the 4 P group to substrate binding and turnover can be obtained by comparing either diC8-PI(3,4,5)P3 with diC8-PI(3,5)P2 or diC8-PI(4,5)P2 with diC8-PI(5)P (Figure 4B). Overall, this analysis for the kcat/KM value reveals a very large contribution of the 4 P group to Synj1 activity by more than 3 orders of magnitude (corresponding to ΔΔGoverall = 4.3–4.7 kcal/mol). Interestingly, comparing the individual kinetic constants (kcat and KM) of diC8-PI(3,4,5)P3 and diC8-PI(3,5)P2 reveals that this overall contribution is mainly attributed to the catalytic turnover (kcat), with the 4 P group contributing a factor 340 to catalysis (corresponding to ΔΔGcatalysis = 3.5 kcal/mol). In contrast, the 4 P group only contributes relatively little to ligand binding, with removal of the 4 P group leading to a 7-fold increase in the KM value (corresponding to ΔΔGbinding = 1.2 kcal/mol). To the best of our knowledge, this is the first time it is unequivocally shown that the phosphoinositide 4 P group directly contributes to substrate turnover by the Synj1 5PPase domain, having important consequences for its catalytic mechanism (see Discussion).

On the other hand, comparing diC8-PI(3,4,5)P3 with diC8-PI(4,5)P2 shows an overall small effect of the 3 P group on the catalytic parameters, which corresponds to the solvent-exposed 3 P group in our structure.

Finally, the contribution of the Mg2+-ion to catalysis was quantified by comparing the catalytic parameters for diC8-PI(4,5)P2 between Mg2+-bound and Mg2+-free Synj1528–873 (Figure 4B). Removal of Mg2+ severely impacted activity with a decrease in the specificity constant (kcat/KM) by 4 orders of magnitude (ΔΔGoverall = 5.4 kcal/mol). This decrease in activity is mainly caused by a decrease in substrate turnover (1400-fold decrease in kcat, ΔΔG = 4.3 kcal/mol) rather than an effect on substrate binding (7.5-fold increase in KM, ΔΔGbinding = 1.2 kcal/mol). The observed contribution of the Mg2+-ion mainly to catalysis rather than substrate binding is in good agreement with the structure of the enzyme-substrate-complex. In this structure, the Mg2+-ion is located at a relatively large distance from the substrate’s 4 P group (3.6 Å), accounting for a relatively weak binding interaction. On the other hand, its contribution to catalysis can be accounted for by either a role in water-mediated leaving group activation and/or by a stabilizing interaction with the phosphorane transition state (see Discussion).

### Impact of missense disease mutations on the Synj1 5-phosphatase activity

Missense and nonsense mutations in the 5PPase domain of Synj1 have been associated with several neurological disorders, such as early-onset seizures and early-onset atypical Parkinson’s disease (Hardies et al., 2016; Xie et al., 2019; Taghavi et al., 2018; Hong et al., 2019; Bouhouche et al., 2017). At the moment of writing this manuscript, three homozygous point variants in the 5PPase domain of Synj1 had been described in patients: the Y793C mutation leading to typical levodopa-responsive parkinsonism (Xie et al., 2019), the R800C mutation leading to asymmetric parkinsonism and seizures (Taghavi et al., 2018), and the Y849C mutation leading to early-onset treatment-resistant seizures and progressive neurological decline (numbering based on Synaptojanin1-145 isoform 2) (Hardies et al., 2016; Figure 1). To aid in rationalizing the contribution of these mutations in the onset of disease, their impact on the kinetic parameters for different substrates was determined (Table 2).

The Y793 residue is present on the large loop that contains the P4IM. Although its side chain is pointing away from the active site, it is located in between active site residues Y784 and K785 on the one hand and K798 and R800 on the other hand, all located in the P4IM (Figure 5A–B). Y793 could potentially stabilize the conformation of this loop by making hydrogen bonds with Y786 and the main chain carbonyl of P782. The Parkinson’s disease mutation Y793C has a clear but rather moderate effect on the Synj1528–873 5PPase activity. The largest decrease in activity is observed for IP3, where the measured catalytic efficiency (kcat/KM) of the mutant is 100-fold lower compared to the wild-type enzyme. On the other hand, the mutation has a rather similar and less pronounced effect on the catalytic efficiency of hydrolysis of the phosphoinositides, with a 8-, 7-, 5-, and 10-fold reduction for diC8-PI(4,5)P2, diC8-PI(3,4,5)P3, diC8-PI(3,5)P2, and diC8-PI(5)P, respectively (Figure 4—figure supplement 2, Figure 4—figure supplement 2—source data 1). This decreased overall catalytic efficiency is due to an effect on both substrate binding (higher KM) and turnover rate (smaller kcat) for IP3 and diC8-PI(4,5)P2, while for diC8-PI(3,4,5)P3 and diC8-PI(3,5)P2 it can nearly completely be attributed to an effect on catalytic turnover. The observation that hydrolysis of all the phosphoinositides is affected to a similar degree suggests that the Y793C mutation indeed leads to an increased flexibility or conformational change of the entire P4IM-containing loop, potentially by disrupting the interactions with Y786 and P782.

![Figure 5.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig5-v2.jpg)

**Figure 5.:** (A) Overall structure of Synj1528–873 (green) with the Y793, R800, and Y849 residues represented as blue, magenta, and purple sticks, respectively. The Y793 residue is present in a loop close to the active site, while R800 is present in the active site. The Y849 residue, on the other hand, is buried in the core of the 5PPase domain. The Mg2+-ion is represented as an orange sphere and the substrate, diC8-PI(3,4,5)P3, as yellow sticks. (B) Close-up view on Y793 and R800 and their surrounding residues. Y793 forms a hydrogen bond with Y786 and with the main chain of P782 (grey dashes) to potentially stabilize the conformation of the loop. R800 forms multiple hydrogen bonds with the 4 P group of diC8-PI(3,4,5)P3 (grey dashes). (C) Close-up view on Y849 and its surrounding residues. Y849 is buried in the hydrophobic core, where it forms a hydrogen bond with E775 and with the main chain NH of V808 (grey dashes).

Similar to Y793, the R800 residue is located in the P4IM, just before the conserved sequence motif P(A/S)W(C/T)DR(I/V)L. However, in contrast to the Y793 residue, its side chain is pointing into the active site and directly interacts with the substrate via multiple (charged) hydrogen bonds with the 4 P group (Figure 5A,B). The clinical R800C mutation has a clear impact on the overall 5PPase activity (kcat/KM) of Synj1528–873, with the extent of the effect varying depending on the substrate. The largest overall effect is also here observed for IP3 with a 900-fold decrease of kcat/KM due to the mutation, while the kcat/KM value decreases 54-, 12-, 2-, and 1.2-fold for diC8-PI(4,5)P2, diC8-PI(3,4,5)P3, diC8-PI(3,5)P2, and diC8-PI(5)P, respectively (Figure 4—figure supplement 3A, Figure 4—figure supplement 3—source data 1). From these values it is clear that the R800C mutation has a pronounced effect on the 5PPase reaction for substrates containing a phosphate group on position 4, while the mutation has almost no effect on the reaction for substrates without the 4 P group (Figure 4—figure supplement 3B). This effect on kcat/KM is due to a combination of effects on catalytic turnover (kcat) and binding (KM). The mutation has a rather small but consistent effect on binding of the 4-P-containing substrates. On the other hand, the R800C mutation has a very high impact on the kcat value of IP3, which could be caused by misalignment of this smaller substrate in the active site pocket if the interaction with the R800 sidechain is lost. Also for diC8-PI(4,5)P2 a significant effect of the R800C mutation on kcat is observed, which indicates that R800 contributes to substrate turnover via its interaction with the 4 P group, potentially by properly aligning it for catalysis (see Discussion). Rather unexpectedly, only a small effect on kcat is observed for the R800C mutation using diC8-PI(3,4,5)P3 as a substrate (Figure 4—figure supplement 3A).

The Y849 residue is buried for the largest part in the hydrophobic core of the protein on one of the β-strands (β12) forming the central β-sandwich fold of the 5PPase domain (Figure 5A, Figure 1—figure supplement 1). Here, its side chain is surrounded by residues G776, V778, F780, R807, L846 and V862, while its phenol hydroxyl groups forms H-bonds with E775 and the main chain amino-group of V808 (Figure 5C). In agreement with this location in the hydrophobic core, the Y849C mutant could not be expressed in the soluble fraction as a His-tagged protein, but a small amount of soluble protein could be obtained when expressing it as a GST-fusion. However, also here it was observed via size-exclusion chromatography that this protein eluted as a higher-oligomer, indicating a significant effect of the mutation on the protein fold and stability. Moreover, while it was confirmed that the wild-type Synj1528–873 was fully active as a GST-fusion (data not shown), no activity could be found for the Y849C mutant at the highest enzyme concentration tested (1 µM) for any of the tested substrates (IP3, diC8-PI(4,5)P2, and diC8-PI(3,4,5)P3) (Figure 4—figure supplement 4).

## Discussion

In this paper, we report the first structural information on the 5PPase domain of Synj1 (Synj1528–873) to 2.3 Å resolution, relying on a strategy of Nanobody-aided crystallization to obtain well diffracting crystals. In addition to the Synj1528–873 structure in the apo state, a short soak with diC8-PI(3,4,5)P3 followed by flash freezing, also enabled us to trap this substrate in one of the active sites of the protein molecules present in the asymmetric unit, representing the very first structure of any 5PPase in complex with a genuine substrate. This structure thus reveals the interactions with all the important phosphate groups, including the scissile 5-phosphate group. Together with a detailed kinetic analysis of the contribution of these phosphate groups to catalysis, this allows us to propose a refined model for the catalytic mechanism of the 5PPase reaction extending on the previous models based on analogies with the apurinic/apyrimidinic base excision repair endonucleases (Whisstock et al., 2000; Aboelnga and Wetmore, 2019; Dlakić, 2000; Mol et al., 2000; Erzberger and Wilson, 1999), as shown in Figure 6.

![Figure 6.](https://cdn.elifesciences.org/articles/64922/elife-64922-fig6-v2.jpg)

**Figure 6.:** The nucleophilic water is activated by proton transfer to the catalytic base D730, allowing attack on the scissile phosphate (P5), and resulting in a phosphorane transition state with excess negative charge that is stabilized by several surrounding residues. Two routes for leaving group activation are envisioned. In route 1 (upper pathway) a Mg2+-activated water molecule acts as general acid by donating a proton to the leaving hydroxylate. Route 2 (lower pathway) corresponds to a mechanism of substrate-assisted catalysis, where the adjacent 4 P group acts as general acid, potentially assisted by transfer of a proton from K798.

In agreement with its conserved role in AP endonucleases and as previously suggested (Trésaugues et al., 2014), D730 is appropriately positioned to act as a general base by abstracting a proton from an attacking water molecule. Indeed, careful analysis of the electron density in the Synj1528–873 diC8-PI(3,4,5)P3-bound structure reveals electron density accounting for such a water molecule located at 3.1 Å from D730 and at 3.5 Å from the P5-atom. This water molecule is furthermore held in place via a hydrogen bond with the conserved N732 residue (Figure 3; Figure 6). It should be noted that also the catalytically important H859 residue is located close to the nucleophilic water molecule, and, depending on the orientation of the side chain, H859 could either form an interaction with the OPF-atom of the 5 P group or with this water molecule. The 5 P group is closely surrounded by multiple residues, H689, N732, R734, Y784, and H859, many of them potentially bearing a positive charge. Interactions of these residues with the 5 P group in the ground state contribute to binding, while stabilization of the excess of negative charge building up in the trigonal bipyramidal phosphorane transition state would contribute to catalysis. Previous mutagenesis studies on mouse INPP5A, yeast Inp52P and human INPP5B have shown that mutation of the residues corresponding to H689 and H859 negatively impact the activity, although from these studies it is not clear whether this is due to an effect on binding or catalysis (Whisstock et al., 2000; Jefferson and Majerus, 1996). While multiple interactions are formed with the 5 P group, none of the residues is seen within interaction distance of the oxygen bridging the scissile phosphate to the inositol ring (O5) and thus in an appropriate position to act as general acid to activate the leaving group. The O5-atom is however located at a distance of 4.0 Å of the Mg2+-ion allowing this distance to be bridged by a Mg2+-coordinated water molecule as previously suggested (Trésaugues et al., 2014). Additionally, the O5-atom is located in our structure at 3.9 Å from one of the oxygens (O8P) of the 4 P group. This distance could decrease during the reaction path, allowing a direct role of the 4 P group in leaving group activation. We therefore envision two potential scenarios for leaving group activation to occur, indicated as route 1 and route 2 in Figure 6. Route 1 envisions a direct role of the Mg2+-ion in leaving group activation by activating a Mg2+-bound water molecule to donate a proton to the leaving O5-atom, although such a water is not observed in our structure. A direct role of Mg2+ in catalysis also agrees with its observed large contribution to catalytic turnover (ΔΔGcatalysis = 4.3 kcal/mol, Figure 4). In this scenario, the observed role of the 4 P group in catalysis could for example be due to a stabilizing hydrogen bond to the O5-atom in the transition state (Figure 6). Route 2, on the other hand, corresponds to a mechanism of substrate-assisted catalysis, with a more direct role of the adjacent 4 P group in leaving group activation, where the O8P hydroxyl group of the 4 P group would transfer a proton to the leaving O5-atom. The transferred proton could potentially originally come from the K798 residue in a proton relay mechanism (Figure 6). In our structure, the O8P-atom from 4 P is located at 3.9 Å from the O5-atom, but small rearrangements in going towards the transition state could easily bring both atoms in close contact. The residues surrounding the 4 P group could in turn contribute to catalysis by properly orienting the 4-phosphate for this role. Such a scenario is in good agreement with our kinetic data showing that the 4 P group has a large contribution to substrate turnover, with removal of the 4 P moiety (i.e. comparing diC8-PI(3,4,5)P3 with diC8-PI(3,5)P2) leading to a 340-fold reduction in kcat (ΔΔGcatalysis = 3.5 kcal/mol, Figure 4). Moreover, we also showed that the R800 residue contributes to catalysis via its interaction with the 4 P group. Within this scenario, the Mg2+-ion could play its observed role in catalysis via a direct interaction with the negative charges building upon the O5-atom in the transition state. It should of course be noted that the latter mechanism would not apply for the 5PPases that also efficiently catalyse the hydrolysis of PIPs missing the 4 P group (such as SHIP1, SHIP2, and to a lesser extent OCRL). At this point no conclusive distinction between these two scenarios can be made.

Apart from being a potential drug target for Alzheimer’s disease, Down syndrome, and TBC1D24-linked epilepsy, loss-of-function mutations in Synj1 also lead to disease, including epilepsy and Parkinson’s disease (Hardies et al., 2016; Xie et al., 2019; Taghavi et al., 2018; Hong et al., 2019; Bouhouche et al., 2017). This is an important point to take into account in a potential drug design effort. To rationalize such an effort and to find the available therapeutic window for inhibitory drug design, it is of paramount importance to characterize and quantify the effect of the disease-associated mutations on Synj1 activity in detail. At the moment of writing this manuscript, three disease-associated homozygous missense mutations had been described in the 5PPase domain of Synj1: Y793C, R800C, and Y849C (numbering based on Synaptojanin1-145 isoform 2) (Hardies et al., 2016; Xie et al., 2019; Taghavi et al., 2018). Our structural data and detailed kinetic analysis of the mutants in comparison to the wild-type enzyme allow us to gain deeper understanding in the molecular basis underlying the associated diseases. Our data shows that the Y849C mutant does not display any 5PPase activity with any of the tested substrates. The crystal structure shows that Y849 is nearly completely buried in the core of the protein (Figure 5C) and the Y849C mutation leads to severe problems in expressing this protein in a soluble form. Together, this indicates that the Y849C mutant corresponds to a near complete loss-of-function mutation due to disruption of the protein fold. In contrast, the R800 residue is located in the active site where it forms important interactions with the 4-phosphate group of the substrate (Figure 5B). Our kinetic analysis of the R800C mutant shows that this residue contributes to both substrate binding and catalysis, specifically via its interaction with the 4 P group. The contribution to substrate turnover (kcat) can be explained by a model where R800 acts by orienting the 4 P group in an orientation suitable for subsequent proton transfer to the inositol 5-hydroxylate leaving group, as outlined above (Figure 6, route 2). Interestingly, the magnitude of the overall effect of the R800C mutation depends on the substrate that is being considered, with a decrease in kcat/KM of a factor 900, 54, and 12 for IP3, diC8-PI(4,5)P2 and diC8-PI(3,4,5)P3, respectively. Whether this difference in activity toward the different substrates is physiologically relevant and leads to an imbalance in the cellular distribution of PI(3,4,5)P3, PI(4,5)P2, and IP3, remains to be seen. Such an imbalance of the PI(3,4,5)P3/PI(4,5)P2 ratio, with a relative increase in PI(4,5)P2 versus PI(3,4,5)P3 as expected from the kinetics of the R800C mutant, has previously been linked to the occurrence of Parkinson’s disease (Sekar and Taghibiglou, 2018). Finally, the Y793 residue is located on the same active site loop as R800, and likely contributes to stabilizing the loop conformation rather than being directly involved in interactions with the substrate (Figure 5B). Our kinetic analysis of the Y793C clinical mutant shows that the 5PPase activity of Synj1 is diminished between 5- and 10-fold for all the substrates in a rather indiscriminatory way.

As a general trend, it can be observed that the impact of the mutations on the catalytic efficiency of the Synj1528–873 enzyme in vitro links with the severity and age of onset of the clinical manifestations in the patients that are homozygous carriers of these Synj1 mutations. Indeed, the very early onset of the severe neurodegeneration observed for the patients carrying a Y849C mutation (Hardies et al., 2016), corresponds well with our observation that this mutation leads to a complete loss of 5PPase activity. On the other hand, the R800C mutation leads to a decrease in overall activity of 54- to 12-fold for the most relevant substrates PI(4,5)P2 and PI(3,4,5)P3 and was reported to associate with parkinsonism and seizures at age 24 (Taghavi et al., 2018), while the even smaller effects on activity we observe for the Y793C mutation, with a decrease in activity of 8-fold for PI(4,5)P2 and 7-fold for PI(3,4,5)P3, leads to Parkinson’s disease at later age (Xie et al., 2019). Although care should be taken with extending these observations to other mutations, this seems to indicate that the impact of the missense mutations on the kinetics of the 5PPase reaction in vitro can be used to a certain level to predict the severity of the disease outcome in patients who are homozygous for the corresponding mutation. Finally, these observations also have implications for the window that is available to therapeutically target the 5PPase domain of Synj1 in DS, AD, and TBC1D24-associated DOORS syndrome. While it was previously shown that genetic ablation of one Synj allele, corresponding to half of the normal cellular activity, was sufficient to rescue the disease phenotype in TBC1D24-mutant flies (Fischer et al., 2016), we show here that a close to 10-fold reduction of Synj1 activity on the long term could lead to disease in its own respect, thus still leaving a window for inhibitor design.

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
      <td>Gene (Homo sapiens)</td>
      <td>SYNJ1</td>
      <td>NCBI</td>
      <td>Gene ID: 8867</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21(DE3) pLysS</td>
      <td>Weiner et al., 1994</td>
      <td>Genotype: F-hsdSB (rB-mB-) gal dcm (DE3) pLysS (CmR)</td>
      <td>Chemically (CaCl2) competent</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>WK6 (Su-)</td>
      <td>Zell and Fritz, 1987 (PMID:3038536)</td>
      <td>Genotype: Δ(lac-proAB) galE strA/F’ [lacIq lacZΔM15 proA+B+]</td>
      <td>Chemically (CaCl2) competent</td>
    </tr>
    <tr>
      <td>Strain, strain background (M13 helper phage)</td>
      <td>Kanamycin-resistant VCSM13</td>
      <td>Stratagene</td>
      <td>200251</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET28a (plasmid)</td>
      <td>Novagen</td>
      <td>69864</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pGEX-4T1 (plasmid)</td>
      <td>GE Healthcare</td>
      <td>GE28-9545-49</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pMESy4 (plasmid)</td>
      <td>Pardon et al., 2014 (DOI: 10.1038/nprot.2014.039)</td>
      <td>GenBank KF415192</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>IP6 (D-myo-inositol 1,2,3,4,5,6-hexakis phosphate)</td>
      <td>Merck Millipore</td>
      <td>407125</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>IP3 (D-myo-inositol 1,4,5-trisphosphate)</td>
      <td>Merck Millipore</td>
      <td>407137</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>diC8-PI(5)P</td>
      <td>Echelon Biosciences</td>
      <td>P-5008</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>diC8-PI(4,5)P2</td>
      <td>Echelon Biosciences</td>
      <td>P-4508</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>diC8-PI(3,5)P2</td>
      <td>Echelon Biosciences</td>
      <td>P-3508</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>diC8-PI(3,4,5)P3</td>
      <td>Echelon Biosciences</td>
      <td>P-3908</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>disodium-4- nitrophenyl phosphate (DNPP)</td>
      <td>Sigma</td>
      <td>N-4645</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Y793C_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CGACTGTGACACCA GTGAAAAGTGCCG</td>
    </tr>
    <tr>
      <td>Sequenced-based reagent</td>
      <td>Y793C_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CTGGTGTCACAG TCGTCAGAAAACAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>R800C_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GTGCTGCACCCCTG CCTGGACAGAC</td>
    </tr>
    <tr>
      <td>Sequenced-based reagent</td>
      <td>R800C_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GGTGCAGCACTTTT CACTGGTGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Y849C_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CACTGTGGAAGAG CTGAGCTGAAG</td>
    </tr>
    <tr>
      <td>Sequenced-based reagent</td>
      <td>Y849C_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CTTCCACAGTGCAGC AAAGTGCCTGG</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>CaptureSelect Biotin anti-C-tag conjugate</td>
      <td>Thermo Fisher Scientific</td>
      <td>7103252100</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Streptavidin Alkaline Phosphatase</td>
      <td>Promega</td>
      <td>V5591</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Malachite Green Phosphate Assay kit</td>
      <td>Gentaur</td>
      <td>POMG-25H</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>autoPROC</td>
      <td>Vonrhein et al., 2011 (DOI: 10.1107/S0907444911007773)</td>
      <td>RRID:SCR_015748 https://www.globalphasing.comautoproc/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STARANISO</td>
      <td>Tickle et al., 2018</td>
      <td>RRID:SCR_018362 http://staraniso.globalphasing.org/cgi-bin/staraniso.cgi</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phaser</td>
      <td>McCoy et al., 2007 (DOI:10.1107/S0021889807021206)</td>
      <td>RRID:SCR_014219 https://www.phenix-online.org/documentation/reference/phaser.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix.Ligand Fit</td>
      <td>Terwilliger et al., 2006 (DOI:10.1107/S0907444906017161)</td>
      <td>https://www.phenix-online.org/documentation/reference/ligandfit.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix.Refine</td>
      <td>Afonine et al., 2012 (DOI: ﻿10.1107/S0907444912001308)</td>
      <td>RRID:SCR_016736 https://www.phenix-online.org/documentation/reference/refinement.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>Emsley et al., 2010 (DOI: 10.1107/S0907444910007493)</td>
      <td>RRID:SCR_014222 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MolProbity</td>
      <td>Chen et al., 2010 (DOI: 10.1107/S0907444909042073)</td>
      <td>RRID:SCR_014226 http://molprobity.biochem.duke.edu</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PDB-REDO server</td>
      <td>Joosten et al., 2014 (DOI: 10.1107/S2052252514009324)</td>
      <td>RRID:SCR_018936 https://pdb-redo.eu/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PyMOL (version 2.0)</td>
      <td>Schrödinger</td>
      <td>RRID:SCR_000305 https://pymol.org/2/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism (version 8)</td>
      <td>Graphpad Software</td>
      <td>RRID:SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CCP4 suite</td>
      <td>Winn et al., 2011 (DOI: 10.1107/S0907444910045749)</td>
      <td>RRID:SCR_007255 http://www.ccp4.ac.uk/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Clustal Omega</td>
      <td>Madeira et al., 2019 (DOI: 10.1093/nar/gkz268)</td>
      <td>RRID:SCR_001591 http://www.ebi.ac.uk/Tools/msa/clustalo/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ESPript</td>
      <td>Robert and Gouet, 2014 (DOI: ﻿10.1093/nar/gku316)</td>
      <td>RRID:SCR_006587 http://espript.ibcp.fr/ESPript/ESPript/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ACD/ChemSketch (version 2019.2.1)</td>
      <td>Advanced Chemistry Development</td>
      <td>http://www.acdlabs.com</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cloning, protein expression, and protein purification

The open reading frame (ORF) encoding the 5-phosphatase domain of Synj1 (residues 528–873) was amplified from the full length Synj1 ORF (NCBI - Gene ID: 8867) and an N-terminal TEV cleavage site was added. This PCR product was digested with NdeI and NotI and ligated into a pET28a expression vector (Novagen). The Synj1528–873 ORF was also amplified and inserted into a pGEX-4T1 expression vector (GE Healthcare) containing a pre-inserted TEV-site using the BamHI and NotI sites (GE Healthcare). QuickChange site-directed mutagenesis was used to insert the Y793C and R800C mutations into the pET28a-TEV-Synj1528–873 plasmid, while the Y849C mutation was introduced in the pGEX-4T1-nTEV-Synj1528–873 plasmid. The resulting plasmids were verified by sequencing (Eurofins Genomics).

Plasmids containing the wild-type or mutant ORFs were transformed in E. coli BL21 (DE3) pLysS cells. Cells were grown at 37°C in Terrific Broth (TB) medium supplemented with the appropriate antibiotics until an OD600 of 0.6 was reached. Subsequently, protein expression was induced by addition of 1 mM IPTG and after an incubation period of 17 hr at 20°C, cells were harvested by centrifugation.

All steps of Synj1528–873 purification (WT and mutants) were performed at 4°C. The bacterial pellets containing His-tagged wild-type, Y793C, and R800C proteins were resuspended in buffer A (25 mM HEPES pH 7.5, 300 mM NaCl, 5% glycerol, and 5 mM MgCl2) supplemented with 10 mM imidazole pH 8, 1 mM DTT, 1 µg/ml leupeptin protease inhibitor (Roth), 0.1 mg/ml AEBSF serine protease inhibitor (Roth), 2 µM pepstatin A (Promega) and 50 µg/ml DNaseI (Sigma), and lysed with a cell-disruptor system (Constant Systems). After clearance of the lysate via centrifugation, the supernatant was loaded onto a Ni2+-NTA-Sepharose column (GE Healthcare) equilibrated with buffer A supplemented with 10 mM imidazole pH 8. After extensive washing, the protein was eluted by increasing the imidazole concentration to 1 M and fractions containing the protein of interest were pooled. To cleave the His-tag, 1 mg of His-tagged TEV protease was added per 10 mg of His-Synj1528–873 and the mixture was dialysed overnight against buffer A supplemented with 1 mM DTT. The mixture was then loaded onto a Ni2+-NTA-Sepharose column, to remove the His-tagged TEV protease and any remaining non-cleaved protein. The bacterial pellets containing GST-tagged wild-type and Y849C protein were resuspended in buffer B (25 mM HEPES pH 7.5, 150 mM NaCl, 5% glycerol and 5 mM MgCl2) supplemented with 1 mM DTT, 1 µg/ml leupeptin protease inhibitor, 0.1 mg/ml AEBSF serine protease inhibitor, 2 µM pepstatin A and 50 µg/ml DNaseI, and cells were lysed as before. The cell lysate was cleared by centrifugation and the supernatant was incubated with Glutathione Sepharose 4 Fast Flow beads (GE Healthcare) for 1 hr, then packed into an empty PD-10 column (GE Healthcare). Following extensive washing, the protein was eluted with buffer B supplemented with 10 mM of reduced glutathione. As a final purification step, the His-tagged or tag-less proteins were loaded on a Superdex 75 s column (GE Healthcare), while the GST-tagged proteins were loaded on a Superdex 200 s column (GE Healthcare), using buffer B supplemented with 1 mM DTT as running buffer.

### Nanobody (Nb) generation and purification

A llama was immunized with His-Synj1528–873. A six-week immunization protocol was followed consisting of weekly immunizations of 200 µg (first two weeks) or 100 µg (last four weeks) protein in presence of GERBU adjuvant. All animal vaccinations were performed in strict accordance with good practices and EU animal welfare legislation. Blood was collected four days after the last injection. Library construction, Nb selection via phage display and Nb expression and purification were performed as described previously (Pardon et al., 2014). Briefly, the variable domains of the heavy-chain antibody repertoire from the llama were subcloned in a pMESy4 phage display vector, which adds a C-terminal His-tag and EPEA-tag (=CaptureSelect C-tag). This resulted in an immune library of 2.4•109 transformants. This Nb-repertoire was expressed on phages after rescue with the VCSM13 helper phage, and two consecutive rounds of phage display were used to select for phages expressing Nbs that bind to the 5PPase domain of Synj1. Therefore, two different coating strategies were used. In the first coating strategy, biotinylated Synj1528–873 (as well His-tagged as non-tagged) was captured on neutravidine-coated 96 well-plates and all binding and washing steps were performed in buffer B (25 mM HEPES pH 7.5, 150 mM NaCl, 5% glycerol and 5 mM MgCl2). In the second coating strategy, Synj1528–873 was captured directly on the bottom of a 96-well plate and all binding and washing steps were performed in buffer B supplemented with 1 mM DTT. After phage display selection, an ELISA screen was performed on crude cell lysates of E. coli expressing the Nbs, in order to confirm binding. Synj1528–873 was coated on the ELISA plate. Incubation with the Nb-containing cell extracts and all washing steps were performed in buffer B. Binding of the Nbs was detected via their EPEA-tag using a 1:4000 CaptureSelect Biotin anti-C-tag conjugate (Thermo Fisher Scientific) in combination with 1:1000 Streptavidin Alkaline Phosphatase (Promega). Colour was developed by adding 100 µl of a 3 mg/ml disodium-4-nitrophenyl phosphate solution (DNPP, Sigma) and measured at 405 nm. Sequence analysis was used to classify the binding Nb clones in sequence families.

For Nb production and purification, pMESy4 vectors, containing the Nb ORFs, were transformed in E. coli WK6 (Su-) cells. Cells were grown at 37°C in TB medium supplemented with 100 µg/ml ampicillin, 0.1% glucose, and 2 mM MgCl2, until an OD600 of 0.6 was reached. Nb expression was induced by adding 1 mM IPTG. After incubation for 17 hr at 28°C, cells were harvested by centrifugation and subjected to an osmotic shock to obtain the periplasmic extract. Subsequently, an affinity purification step on Ni2+-NTA sepharose and a SEC step on a Superdex 75 16/60 column (in buffer C: 25 mM HEPES pH 7.5, 150 mM NaCl, 5% glycerol) were used to purify the Nbs.

### Crystallization and data collection

To form the Nb-Synj1528–873 complex, 250 µM of Synj1528–873 was mixed with 500 µM of Nb and incubated for 1 hr on ice. Subsequently, a Superdex 75 10/30 column (in buffer B: 25 mM HEPES pH 7.5, 150 mM NaCl, 5% glycerol, and 5 mM MgCl2) was used to separate the complex from the excess of Nb.

Initial crystallization conditions were found using the Wizard III and IV (Rigaku) and SG1 screen (Molecular Dimensions) by the sitting-drop vapour-diffusion method at 20°C using a Mosquito robot (SPT Labtech). After optimization two similar conditions yielded good quality crystals of the Nb15-Synj1528–873 complex prepared at 25 mg/ml. Condition 1 was composed of 15% PEG 4000, 0.1 M sodium citrate pH 5 and 10% 2-propanol, while condition 2 contained 15% PEG 3350, 0.1 M sodium citrate pH 5.5 and 13% ethanol. Crystals from these conditions were soaked overnight with mother liquor supplemented with either 1 mM IP6 (inositol-(1,2,3,4,5,6)-hexakisphosphate) (Merck Millipore) (condition 1) or 1 mM diC8-PI(3,4,5)P3 (Echelon Biosciences) (condition 2). Subsequently, the former crystals were transferred to a cryo-solution containing mother liquor supplemented with 25% glycerol, while the latter crystals were again very briefly soaked in mother liquid supplemented with 1 mM diC8-PI(3,4,5)P3 and 15% glycerol as cryo-protectant, immediately followed by flash freezing in liquid nitrogen.

All data were collected at 100 K. Diffraction data from the crystal soaked with IP6 was collected at the i03 beamline of the DIAMOND synchrotron (λ = 0.980105) using an Eiger2 XE 16M detector. Data from the crystal soaked with diC8-PI(3,4,5)P3 was collected at the Proxima 2a beamline of the SOLEIL synchrotron (λ = 0.976246) equipped with an Eiger X 9M detector. Diffraction data were integrated and scaled with autoPROC (Global Phasing Limited; Vonrhein et al., 2011), using the default pipeline which includes XDS, Truncate, Aimless, and STARANISO (Tickle et al., 2018). Anisotropy analysis by STARANISO showed that diffraction data were anisotropic, with diffraction limits along the reciprocal axes of 2.71 Å along 0.781 a* - 0.625 c*, 2.41 Å along b* and 2.30 Å along 0.975 a* + 0.222 c* for the structure obtained from the IP6-soaked crystal (Appendix 1—figure 1A), and 2.86 Å along 0.043 a* + 0.999 c*, 2.73 Å along b* and 3.14 Å along −0.974 a* + 0.228 c* for the structure obtained from the diC8-PI(3,4,5)P3-soaked crystal (Appendix 1—figure 1B). Automated resolution cutoff of anisotropic corrected data by STARANISO resulted in a 2.30 Å and a 2.73 Å resolution structure for the IP6- and diC8-PI(3,4,5)P3-soaked crystals respectively (using I/σ(I) > 1.4 as a cut-off criterion).

### Structure determination and refinement

For the IP6 soaked crystal the phase problem was solved by molecular replacement using Phaser (McCoy et al., 2007) from the PHENIX suit (Liebschner et al., 2019). The structures of other 5-phosphatase domains (namely the 5-phosphatase domains of Schizosaccaromyces pombe Synaptojanin, human INPP5B, human INPP5B in complex with diC8-PI(4)P and human OCRL) and a random Nb were used as search models (PDB entries 5-phosphatases: 1i9y, 3n9v, 3mtc and 4cmn; PDB entry Nb: 4nc2). Since the resulting structure had no IP6 bound, we flagged it as an apo-structure. The structure of the diC8-PI(3,4,5)P3-containing crystal was solved by refining the data against the refined apo-structure, taking care to use the same set of reflections for cross-validation. Analysis of the 2Fo-Fc, Fo-Fc, and omit maps revealed unambiguous electron density for diC8-PI(3,4,5)P3. Subsequently, the ligand was inserted using Phenix.LigandFit (Terwilliger et al., 2006) followed by a refinement using Phenix.Refine (Afonine et al., 2012).

Models were improved by iterative cycles of refinement with Phenix.Refine (Afonine et al., 2012) and manual building in Coot (Emsley et al., 2010). MolProbity (Chen et al., 2010) was used for structure validation. As a final optimization, the diC8-PI(3,4,5)P3-bound structure was submitted to the PDB-REDO server (Joosten et al., 2014). X-ray data collection and refinement statistics are listed in Table 1.

Coordinates and structure factors have been deposited in the Protein Data Bank under accession codes PDB 7A0V (apo Synj1528–873) and PDB 7A17 (diC8-PI(3,4,5)P3-bound Synj1528–873).

### Structural analysis

All structural figures were produced with PyMOL (The PyMol Molecular Graphic System, version 2.0 Schrödinger, LLC, https://pymol.org/2/). Superpose in CCP4 (Krissinel and Henrick, 2004) was used to determine the root-mean-square deviation (rmsd) between the different Synj528–873 chains present in one asymmetric unit, and between one Synj1528–873 chain and the structures of the 5PPase domain of the other 5PPases. Multiple sequence alignment of the 5PPase domains of all human 5PPases and SPSynj was performed via Clustal Omega (Madeira et al., 2019). ESPript was used to assign secondary structures (Robert and Gouet, 2014). ACD/ChemSketch (version 2019.2.1, Advanced Chemistry Development, Inc, Toronto, ON, Canada, http://www.acdlabs.com, 2020) was used to draw the schematic representations of the interactions in the active site.

### Enzyme kinetics

The enzymatic activity of wild-type and mutant Synj1528–873 using the substrates IP3 (Sigma), diC8-PI(3,4,5)P3, diC8-PI(4,5)P2, diC8-PI(3,5)P2, and diC8-PI(5)P (Echelon Biosciences) was measured using the Malachite Green phosphate assay (Gentaur) that detects the release of free orthophosphates (Pi). A full steady-state Michaelis-Menten analysis of Synj1528–873 wild-type and the R793C and R800C mutants was performed via initial rate measurements using an enzyme concentration optimized for each enzyme/substrate combination to convert around 10% of substrate over the total measuring time, and at varying substrate concentrations (typically within the range 5–500 µM, depending on the KM value). For the GST-tagged Y849C mutant, time measurements at a single substrate concentration of 120 µM (for IP3, diC8-PI(4,5)P2, and diC8-PI(3,4,5)P3) and an enzyme concentration of 1 µM were performed. To assess the effect of Nb15 on catalysis, measurements were carried out by incubating Synj1528–873 with a 40-fold excess (100 nM) of Nb15 for 10 min at 25°C prior to the assay. All measurements were done at 25°C in 25 mM HEPES pH 7.5, 150 mM NaCl, 5% glycerol, 2 mM MgCl2 and 1 mM DTT, except for the measurements performed at pH 5.5 where the HEPES was replaced by 25 mM sodium citrate pH 5.5. At different time points, 80 µl of each reaction mixture was transferred to a 96 well plate containing 20 µl of the Malachite Green working reagent to stop the reaction. After 30 min of incubation, the absorption of the samples was measured in a SPECTROstarNano (BMG Labtech) plate reader at 620 nm. The absorption was plotted against time and a linear trendline was drawn through the plotted points. To obtain the initial reaction velocity (v), the slopes were divided by the slope of a standard curve (measured in quadruplicate). The velocity divided by the enzyme concentration (v/E0) was plotted against the substrate concentration and the curve was fitted on the Michaelis-Menten equation in GraphPad Prism (version 8, GraphPad Software, La Jolla, California USA, http://www.graphpad.com) to determine kcat and KM. Each datapoint was measured in triplicate. ΔΔG values were calculated as follows: ΔΔGoverall = -R.T. ln ([kcat/KM]substrate 2/[kcat/KM]substrate 1); ΔΔGbinding = -R.T. ln ([1/KM]substrate 2/[1/KM]substrate 1); ΔΔGcalatysis = -R.T. ln ([kcat]substrate 2/[kcat]substrate 1).
