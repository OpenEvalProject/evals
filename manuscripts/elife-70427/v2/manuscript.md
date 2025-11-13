# Cryo-EM reveals new species-specific proteins and symmetry elements in the Legionella pneumophila Dot/Icm T4SS

## Authors

- Michael J Sheedlo<sup>1</sup> ([ORCID: 0000-0002-3185-1727](https://orcid.org/0000-0002-3185-1727))
- Clarissa L Durie<sup>3</sup> ([ORCID: 0000-0002-4027-4386](https://orcid.org/0000-0002-4027-4386))
- Jeong Min Chung<sup>3</sup> ([ORCID: 0000-0002-4285-8764](https://orcid.org/0000-0002-4285-8764))
- Louise Chang<sup>3</sup>
- Jacquelyn Roberts<sup>3</sup>
- Michele Swanson<sup>5</sup> ([ORCID: 0000-0003-2542-0266](https://orcid.org/0000-0003-2542-0266))
- Dana Borden Lacy<sup>2</sup> ([ORCID: 0000-0003-2273-8121](https://orcid.org/0000-0003-2273-8121))
- Melanie D Ohi<sup>3</sup> ([ORCID: 0000-0003-1750-4793](https://orcid.org/0000-0003-1750-4793)) †

### Affiliations

1. Department of Pharmacology, University of Minnesota Minneapolis United States
2. Department of Pathology, Microbiology, and Immunology, Vanderbilt University Medical Center Nashville United States
3. Life Sciences Institute, University of Michigan Ann Arbor United States
4. Department of Biotechnology, The Catholic University of Korea Gyeonggi Republic of Korea
5. Department of Microbiology and Immunology, University Of Michigan Ann Arbor United States
6. The Veterans Affairs Tennessee Valley Healthcare System Nasvhille United States
7. Department of Cell and Developmental Biology, University of Michigan Ann Arbor United States

† Corresponding author

## Abstract

Legionella pneumophila is an opportunistic pathogen that causes the potentially fatal pneumonia known as Legionnaires’ disease. The pathology associated with infection depends on bacterial delivery of effector proteins into the host via the membrane spanning Dot/Icm type IV secretion system (T4SS). We have determined sub-3.0 Å resolution maps of the Dot/Icm T4SS core complex by single particle cryo-EM. The high-resolution structural analysis has allowed us to identify proteins encoded outside the Dot/Icm genetic locus that contribute to the core T4SS structure. We can also now define two distinct areas of symmetry mismatch, one that connects the C18 periplasmic ring (PR) and the C13 outer membrane cap (OMC) and one that connects the C13 OMC with a 16-fold symmetric dome. Unexpectedly, the connection between the PR and OMC is DotH, with five copies sandwiched between the OMC and PR to accommodate the symmetry mismatch. Finally, we observe multiple conformations in the reconstructions that indicate flexibility within the structure.

## Introduction

Type IV secretion systems (T4SS) are large molecular machines utilized by many bacteria and some archaea. Several pathogenic bacteria, such as Legionella pneumophila, Helicobacter pylori, Bordetella pertussis, Brucella, and Bartonella, use T4SSs to deliver bacterial molecules (either nucleic acids or proteins) into the cytoplasm of their host (Christie et al., 2014; Grohmann et al., 2018). The activity of these effector molecules contributes to a variety of human diseases including pneumonia, gastric cancer, whooping cough, and ‘cat scratch fever’ (Christie et al., 2014; Grohmann et al., 2018).

T4SSs in Gram-negative bacteria contain a minimum of 12 components (named VirB1-VirB11 and VirD4 in prototype systems), which are organized into a structure that spans both the inner and outer membranes. The architecture of T4SSs can be subdivided into at least four different features: the outer membrane core or cap (OMC), an inner membrane complex, a complement of cytosolic ATPases, and, in some species, an extracellular pilus (Christie et al., 2014; Grohmann et al., 2018; Fronzes et al., 2009; Gordon et al., 2017; Waksman, 2019; Low et al., 2014; Gonzalez-Rivera et al., 2016). Though several of these features are conserved among species, the exact architecture varies between systems. For example, recent structural studies of the L. pneumophila Dot/Icm and H. pylori Cag T4SSs revealed a periplasmic ring (PR) that had not been identified in ‘minimized’ systems (Ghosal et al., 2017; Ghosal et al., 2019; Chetrit et al., 2018; Park et al., 2020; Chang et al., 2018; Chung et al., 2019; Sheedlo et al., 2020; Durie et al., 2020; Hu et al., 2019). A symmetry mismatch between the OMC and PR was also described for both systems, with a C13:C18 (OMC:PR) mismatch in the L. pneumophila Dot/Icm T4SS and a C14:C17 (OMC:PR) mismatch in the H. pylori Cag T4SS. Though the connections between the OMC and the PR could not be modeled for either system, it was discovered that the H. pylori VirB9 homolog (known as CagX) is present in both the OMC and PR, leading to questions regarding how the symmetry mismatch is accommodated in these systems. The PR is distinct among the structurally characterized T4SSs, though a similar symmetry mismatch phenomenon has been described in bacterial type II (T2SS), type III (T3SS), and type VI (T6SS) secretion systems, suggesting a utility to its conservation (Ghosal et al., 2019; Chung et al., 2019; Sheedlo et al., 2020; Durie et al., 2020; Chernyatina and Low, 2019; Hu et al., 2018; Dix et al., 2018).

The Dot/Icm complex of L. pneumophila is one of the largest known T4SSs. Genetic screens for mutants defective in intracellular replication identified 26 genes, named dot (defect in organelle trafficking) or icm (intracellular multiplication), required for T4SS function (Segal et al., 1998; Segal and Shuman, 1999; Berger and Isberg, 1993; Vogel et al., 1998). The Dot/Icm T4SS has as many as 300 protein substrates, a striking contrast to the H. pylori Cag and B. pertussis Ptl T4SSs, each of which transports only one virulence factor (Schroeder, 2017; Fischer, 2011; Backert et al., 2017; Shrivastava and Miller, 2009). The Dot/Icm ‘core complex’ (which spans the inner and outer membranes) was originally predicted to contain only five proteins: DotC, DotD, DotF, DotG, and DotH (Kubori et al., 2014; Nagai and Kubori, 2011). We recently described parts of the structures and positions of DotC, DotD, and DotH, as well as two additional proteins that associate with the OMC, DotK, and Lpg0657 (Ghosal et al., 2019; Durie et al., 2020; Kubori et al., 2014). However, several features in this map could not be unambiguously identified, including the PR, three chains within the OMC, and a low-resolution ‘dome’ positioned in the center of the OMC which we predict breaches the outer membrane (Durie et al., 2020). Because the dome could not be resolved, we were unable to model the Dot/Icm T4SS pore that facilitates the transfer of cargo across the outer membrane. Structural and mass spectrometry analysis of T4SS particles purified from a deletion mutant strain revealed that two of the unidentified chains within the OMC were not DotG or DotF, because the structural organization of these unassigned regions in the mutant T4SS were unchanged compared to the WT T4SS (Durie et al., 2020). Thus, to improve our understanding of the organization of the Dot/Icm T4SS, we used additional cryo-EM data collection and analysis to increase the resolution and quality of the maps, allowing us to build detailed models for the previously unidentified regions of the complex. Here, we report the structure and organization of the L. pneumophila Dot/Icm T4SS OMC and PR at resolutions that allow us to identify new components which had not previously been detected by decades of fundamental genetic and biochemical work or by more recent cutting edge cryo-electron tomography. Furthermore, this work reveals how the symmetry mismatch between the OMC and PR is accommodated, an observation that may inform the understanding of symmetry mismatch elements in homologous systems. Additionally, we identified another, unexpected symmetry mismatch between the dome and the rest of the OMC, a feature that has not been observed in other structurally characterized T4SSs and also characterize structural flexibility between the dome and the OMC.

## Results and discussion

### Reconstruction of maps of the Dot/Icm T4SS

We have determined a 3.8 Å asymmetric reconstruction (C1) of the Dot/Icm T4SS using single particle cryo-EM approaches. This resolution made it possible to trace connections between the OMC, which contains 13 copies of the asymmetric unit, and the PR, which contains 18 copies of the asymmetric unit. Unexpectedly, we observed five peptide chains originating from the PR, with attached densities sandwiched between the PR and OMC (Figure 1A). Although the resolution was not high enough in the C1 reconstruction to confidently identify the molecular composition of this density, its arrangement in the complex suggested a mechanism for accommodating the symmetry mismatch between the PR and OMC. To increase the resolution of the OMC and PR, C13 and C18 symmetry were applied to the OMC and PR, respectively, in line with our previous report (Durie et al., 2020). This extended the resolution to 2.8 Å for both maps (Figure 1B). Notably, we were not able to resolve the dome feature in the center of the OMC after the application of symmetry, suggesting that this region contained another symmetry and/or was structurally flexible. To help better resolve this important region of the map, we implemented a recently developed data analysis strategy, 3D variability analysis (3DVA) (Punjani and Fleet, 2021). This computational analysis led to the calculation of five distinct maps of the dome at a global resolution of 4.6 Å, revealing that, unlike the rest of the OMC, the dome is 16-fold symmetrical (Figure 1—figure supplement 4). Thus, the Dot/Icm T4SS has three distinct symmetrical regions of the complex, a 16-fold symmetrical dome, a 13-fold symmetrical OMC, and an 18-fold symmetrical PR.

![Figure 1.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig1-v2.jpg)

**Figure 1.:** (A) The asymmetric reconstruction (C1) of the Dot/Icm T4SS includes the outer membrane cap (OMC) (shown in blue), the periplasmic ring (PR) (shown in green), the asymmetric dome (shown in gray), and additional densities with no apparent symmetry sandwiched between the OMC and PR (shown in red). (B) The imposition of symmetry was used to improve the resolution of the OMC (C13 symmetry) and PR (C18 symmetry).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Using template picking in cryoSPARC, ~1,400,000 Dot/Icm type IV secretion system (T4SS) particles were selected. The processing steps done in cryoSPARC are on a blue background, and the processing steps done using RELION are on a tan background. After 2D and 3D classification, the best class of ~136,000 particles was chosen for further refinement with and without C13 symmetry, resulting in reconstruction of 3D maps at 3.8 and 3.4 Å, respectively. The particle stack used in the refinement job in cryoSPARC was exported into Relion for further processing, such as contrast transfer function (CTF)-refinement and focused refinement. The 3.4 Å 3D model with C13 symmetry was used as an initial model for 3D structure determination in Relion using auto-3D refinement with C13 symmetry, resulting in reconstruction of 3D map of 3.8 Å resolution. Focused 3D classification (without alignment) including CTF per-particle refinement and then with either C13 (outer membrane cap [OMC]) or C18 symmetry (periplasmic ring [PR]) imposed was used to determine higher resolution maps of the OMC disk (with 13-fold symmetry) and the PR (with 18-fold symmetry). The maps of the OMC disk and PR were further refined using focused 3D refinement (with local refinement), resulting in 3D maps of the OMC disk (13-fold symmetry) and the PR (18-fold symmetry) at 2.8 Å for each region.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (a) A representative image of the Dot/Icm type IV secretion system (T4SS) particles in cryo-EM (scale bar = 50 nm) and (b) subsequent 2D class averages (edge of box, 510 pixel, 562 Å). (c–e) The Dot/Icm T4SS map was reconstructed with no symmetry applied. The local resolution of the C1 map extends to ~3.0 Å in the best resolved portions of the map. Fourier shell correlation (FSC) indicates a global resolution of 3.8 Å.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (a–b) The outer membrane cap (OMC) disk has been reconstructed to 2.8 Å resolution using C13 symmetry. (c) The local resolution of the OMC extends to ~2.5 Å in the best resolved portions of the map. (d–e) The periplasmic ring (PR) has been reconstructed to 2.8 Å using C18 symmetry. (f) The local resolution of the PR extends to ~2.8 Å in the best resolved regions of the map.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (a–e) The complex has been reconstructed to 4.6 Å resolution using C1 refinements of five clusters of particles identified by 3D variability analysis (3DVA).

### Architecture of the Dot/Icm T4SS OMC

Models of DotC, DotD1, DotD2, DotH, and DotK were built within the map of the OMC that was reconstructed with C13 symmetry imposed. While parts of these models were presented in our previous report (Durie et al., 2020), the quality of the new map of the OMC allowed us to extend many of these models for a nearly complete structural analyses of OMC protein structures and, importantly, to build models within the previously undefined regions of the complex. We now present extended, higher resolution models of DotC (residues 28–35, 60–161, and 173–268), DotD1 (residues 24–162), DotD2 (residues 25–160), DotH (residues 271–361), and DotK (residues 40–188) (Figure 2 and Figure 2—figure supplements 1–3 Table 1). These extended models provide additional insight into the arrangement of the N-termini of these proteins, placing predicted lipidation sites of DotC (C19), DotD1 (C19), DotD2 (C19), and DotK (C27) in positions close to the outer membrane (Figure 2—figure supplement 4A; Yerushalmi et al., 2005). In addition, we modeled into these maps Lpg0657, which we now call Dis1 (Dot/Icm Secretion), in close agreement with our previous assignment (Durie et al., 2020). However, the model contains a newly resolved extension within the N-terminus of Dis1 (residues 42–65 and 88–98) which forms two helices that extend ‘up’ from the OMC disk, placing them near, or perhaps within, the outer membrane. A previous study found that a transposon mutant interrupting the Dis1 gene resulted in a strain that replicates as well as the wild-type strain in liquid culture, but has an intracellular growth defect in both Acanthamoeba castellanii and bone marrow-derived murine macrophages, consistent with Dis1 playing an important role in Dot/Icm T4SS function (Goodwin et al., 2016).

![Figure 2.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig2-v2.jpg)

**Figure 2.:** The asymmetric unit of the OMC is comprised of one copy of DotC (brown), DotF1 (purple), DotK (cyan), DotH (orange), Dis1 (Lpg0657, blue), Dis2 (Lpg0823, green), Dis3 (Lpg2847, tan), and two copies of DotD (red and pink).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) The refinement statistics for each component of the Dot/Icm T4SS OMC are shown in the table. (B) The model map correlation for the entire OMC is shown with the masked data shown in green and the unmasked shown in black. The fit of each model was also determined.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** The quality of the model was interpreted using per residue correlation coefficients for regions of DotC, DotD1, DotD2, DotF1, and DotH. The correlation of each residue is plotted by spectrum on each component (left). The correlation coefficient was also plotted against residue number (right). The average correlation coefficient per residue is indicated by the dashed line.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** The quality of the model was interpreted using per residue correlation coefficients for DotK, Dis1, Dis2, and Dis3. The correlation of each residue is plotted by spectrum on each component (left). The correlation coefficient was also plotted against residue number (right). The average correlation coefficient per residue is indicated by the dashed line.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) The predicted lipidation recognition elements of DotC, DotD, and DotK are shown with the predicted lipidated residue indicated in red (top). We note that a similar site exists within Dis1 with the putative lipidation recognition site indicated in red (bottom). (B) When the asymmetric unit of the OMC is fit into a tomogram of the Dot/Icm type IV secretion system (T4SS) (Chetrit et al., 2018) (left), we note that several features predicted to interact with the outer membrane would indeed be in close proximity to the lipid bilayer (right, dashed circles). (C) A model of the location of predicted membrane interaction sites in the OMC in relation to their position to the outer membrane. In aggregate, these seven sites could anchor the structure to the outer membrane.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** (A) The unknown fold near the ‘top’ of the outer membrane cap (OMC) is Dis2. (B–C) Representative density fits for large residues are indicated. Dis2 is comprised of two domains that are similar in sequence (B) and structure (C). (D) There are a total of five disulfide bonds observed within Dis2 as mapped onto the sequence. Each of the disulfide bonds that are described here include strong density within the reconstructed cryo-EM map.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** (A) Dis3 is a 14-rung β-helical protein that we have modeled into the peripheral ‘arm’ density of the outer membrane cap (OMC) (left). Example density for specific rungs indicate the loss of resolution toward the periphery of the map (right). (B) Dis3 is structurally similar to adhesion proteins found in the genus Bacteroides. (C) The surface of Dis3 is predominantly electropositive as indicated in this electrostatic depiction. (D) Lpg2847 makes contact with three other proteins within the OMC, Dis1, DotK, and DotD1. All interactions are mediated through rungs within the C-terminus of the protein.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig2-figsupp7-v2.jpg)

**Figure 2—figure supplement 7.:** (A) Within the periphery of the OMC, we modeled a two β-sheet protein that we identified as DotF (left). Although the resolution is lower in this portion of the map, several features of DotF fit well within the density (right). (B) DotF1 interacts only with Dis3 within the OMC. (C) The interactions that mediate the DotF1-Dis3 interaction contain several H-bonds and two salt bridges as indicated in the table. (D) DotF is structurally similar to proteins found in the periplasm of other large macromolecular complexes, such as GspC (type II secretion system) and PilP (type IV pilus).

**Table 1.**
 Map reconstruction and model refinement.


<table>
  <thead>
    <tr>
      <th></th>
      <th>OMC</th>
      <th>PR</th>
      <th>OMC/PR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EMDB accession codes</td>
      <td>24005</td>
      <td>24006</td>
      <td>24004</td>
    </tr>
    <tr>
      <td>Data collection and processing</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Magnification</td>
      <td>81,000×</td>
      <td>81,000×</td>
      <td>81,000×</td>
    </tr>
    <tr>
      <td>Voltage (kV)</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
    </tr>
    <tr>
      <td>Total electron dose (e-/Å2)</td>
      <td>50</td>
      <td>50</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Defocus range (µm)</td>
      <td>–1.5 to –2.1</td>
      <td>–1.5 to –2.1</td>
      <td>–1.5 to –2.1</td>
    </tr>
    <tr>
      <td>Pixel size (Å)</td>
      <td>1.1</td>
      <td>1.1</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>Processing software</td>
      <td>CryoSPARC,Relion</td>
      <td>CryoSPARC, Relion</td>
      <td>CryoSPARC,Relion</td>
    </tr>
    <tr>
      <td>Initial particles (number)</td>
      <td>1,389,426</td>
      <td>1,389,426</td>
      <td>1,389,426</td>
    </tr>
    <tr>
      <td>Final particles (number)</td>
      <td>84,886</td>
      <td>43,907</td>
      <td>136,818</td>
    </tr>
    <tr>
      <td>Map sharpening B-factor</td>
      <td>–99.2</td>
      <td>–82.8</td>
      <td>–115</td>
    </tr>
    <tr>
      <td>Map resolution (Å)</td>
      <td>2.8</td>
      <td>2.8</td>
      <td>2.8</td>
    </tr>
    <tr>
      <td>FSC threshold</td>
      <td>0.143</td>
      <td>0.143</td>
      <td>0.143</td>
    </tr>
    <tr>
      <td>Model refinement and validation</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Starting models</td>
      <td>6 × 62</td>
      <td>6 × 64</td>
      <td>6 × 65</td>
    </tr>
    <tr>
      <td>FSC</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>2.8</td>
      <td>2.8</td>
      <td>4.0</td>
    </tr>
    <tr>
      <td>0.143</td>
      <td>2.7</td>
      <td>2.7</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td>Model residues</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total</td>
      <td>17,264</td>
      <td>5490</td>
      <td>23.286</td>
    </tr>
    <tr>
      <td>DotC</td>
      <td>28–35, 60–161, 173–268</td>
      <td>–</td>
      <td>28–35, 57–161, 173–272</td>
    </tr>
    <tr>
      <td>DotD1</td>
      <td>24–162</td>
      <td>–</td>
      <td>23–162</td>
    </tr>
    <tr>
      <td>DotD2</td>
      <td>25–160</td>
      <td>–</td>
      <td>24–160</td>
    </tr>
    <tr>
      <td>DotF1</td>
      <td>208–266</td>
      <td></td>
      <td>208–266</td>
    </tr>
    <tr>
      <td>DotF2</td>
      <td>–</td>
      <td>207–269</td>
      <td>207–269</td>
    </tr>
    <tr>
      <td>DotG</td>
      <td>–</td>
      <td>791–824</td>
      <td>791–824</td>
    </tr>
    <tr>
      <td>DotH</td>
      <td>271–361</td>
      <td>104–263</td>
      <td>104–361</td>
    </tr>
    <tr>
      <td>DotK</td>
      <td>40–188</td>
      <td>–</td>
      <td>38–188</td>
    </tr>
    <tr>
      <td>Dis1</td>
      <td>42–65, 88–234</td>
      <td>–</td>
      <td>42–65, 88–236</td>
    </tr>
    <tr>
      <td>Dis2</td>
      <td>40–115</td>
      <td>–</td>
      <td>39–116</td>
    </tr>
    <tr>
      <td>Dis3</td>
      <td>29–320</td>
      <td>–</td>
      <td>29–320</td>
    </tr>
    <tr>
      <td>Unknown OMC</td>
      <td>122–130</td>
      <td>–</td>
      <td>1–54, 122–130</td>
    </tr>
    <tr>
      <td>Unknown PR</td>
      <td>–</td>
      <td>1–38, 70–79</td>
      <td>1–38, 70–79</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>3.04</td>
      <td>0.67</td>
      <td>5.80</td>
    </tr>
    <tr>
      <td>Molprobity</td>
      <td>1.42</td>
      <td>0.85</td>
      <td>2.22</td>
    </tr>
    <tr>
      <td>Bonds</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Lengths (Å)</td>
      <td>0.003</td>
      <td>0.004</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>Angles (°)</td>
      <td>0.748</td>
      <td>0.785</td>
      <td>1.822</td>
    </tr>
    <tr>
      <td>Ramachandran (%)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Favored</td>
      <td>95.3</td>
      <td>97.3</td>
      <td>94.5</td>
    </tr>
    <tr>
      <td>Allowed</td>
      <td>4.7</td>
      <td>2.7</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>Outliers</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>B-factors</td>
      <td>55.3</td>
      <td>69.7</td>
      <td>165.0</td>
    </tr>
    <tr>
      <td>PDB</td>
      <td>7MUD</td>
      <td>7MUE</td>
      <td>7MUC</td>
    </tr>
  </tbody>
</table>

In addition to the improved models discussed above, this new map identifies the three chains within the OMC that were previously unknown (described simply as ‘chain 1’, ‘chain 2’, and ‘chain 3’) (Figure 2). The former ‘chain 1’ is Lpg0823, now named Dis2 (residues 40–115, Figure 2—figure supplement 5A). Dis2 is positioned near the outer membrane and consists of two lobes, similar in both sequence and structure, that are pinned together with a total of five disulfide bonds, all of which show strong density within the map (Figure 2—figure supplement 5B-D). A DALI search of Dis2 returned no significant structural similarity among PDB entries, making its function difficult to infer (Holm, 2020). Together, the predicted membrane interaction sites in DotC, DotD1, DotD2, DotK, would anchor the Dot/Icm T4SS to the outer membrane at seven positions per asymmetric unit (Figure 2—figure supplement 4E). The improved density maps have allowed us to visualize new structural features and details of previously identified Dot/Icm T4SS components and identify the composition of peptide chains that were previously not able to be modeled. The organization of these regions in regard to the location of their predicted lipidation sites provides the first molecular insight into how this complex becomes anchored in the outer membrane of the bacteria.

We identify ‘chain 2’ as Lpg2847 (residues 29–320), now referred to as Dis3. Dis3, predominantly a β-helical protein, is the major contributor to the ‘arms’ that extend outward radially from the disk of the OMC (Figure 2—figure supplement 6A). Dis3 consists of a total of 14 helical rungs and is structurally similar to membrane associated proteins found in Parabacteroides distasonis (gene BDI3087; PDB 3J × 8), Bacteroides fragilis (gene BF0425; PDB 3PET), and B. pertussis (pertactin; PDB 1DAB, Figure 2—figure supplement 6B). The exterior face of Dis3 is predominantly electropositive, potentially facilitating an interaction with the electronegative head groups of the inner leaflet of the outer membrane (Figure 2—figure supplement 6C). Notably, the C-terminus of Dis3 contacts three different proteins within the OMC: Dis1, DotK, and DotD1 (Figure 2—figure supplement 6D). The presence of Dis2 (Lpg0823, UniprotKB Q5ZXA9) and Dis3 (Lpg2847, UnitprotKB Q5ZRN3) in the isolated Dot/Icm T4SS was confirmed by mass spectrometry using four biologically independent purifications (Table 2). Lpg2847 was previously identified as part of a two-gene operon with lpg2848 or snrnA, an RNase secreted by the L. pneumophila T2SS (Rossier et al., 2009). Insertional mutants of both the srnA and dis1 genes were prepared and tested for the ability to secrete the RNase through the T2SS (Rossier et al., 2009). The dis1 mutant showed no growth defect in the protozoan host H. vermiformis, a well-accepted assay for T2SS function, but has not yet been tested specifically for T4SS assembly or function (Rossier et al., 2009).

**Table 2.**
 Dot/Icm proteins in isolated complex sample.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4">Spectral counts†</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Identified proteins</td>
      <td>Gene number*</td>
      <td>Prep 1</td>
      <td>Prep 2</td>
      <td>Prep 3</td>
      <td>Prep 4</td>
    </tr>
    <tr>
      <td>DotG ‡</td>
      <td>Q5ZYC1</td>
      <td>112</td>
      <td>114</td>
      <td>195</td>
      <td>150</td>
    </tr>
    <tr>
      <td>DotF</td>
      <td>Q5ZYC0</td>
      <td>94</td>
      <td>69</td>
      <td>101</td>
      <td>107</td>
    </tr>
    <tr>
      <td>DotA</td>
      <td>Q5ZS33</td>
      <td>38</td>
      <td>65</td>
      <td>60</td>
      <td>69</td>
    </tr>
    <tr>
      <td>Dis3</td>
      <td>Q5ZRN3</td>
      <td>22</td>
      <td>24</td>
      <td>41</td>
      <td>87</td>
    </tr>
    <tr>
      <td>DotO</td>
      <td>Q5ZYB6</td>
      <td>37</td>
      <td>38</td>
      <td>47</td>
      <td>27</td>
    </tr>
    <tr>
      <td>DotH</td>
      <td>Q5ZYC2</td>
      <td>28</td>
      <td>19</td>
      <td>28</td>
      <td>47</td>
    </tr>
    <tr>
      <td>IcmF</td>
      <td>Q5ZYB4</td>
      <td>15</td>
      <td>18</td>
      <td>36</td>
      <td>38</td>
    </tr>
    <tr>
      <td>IcmX</td>
      <td>Q5ZS30</td>
      <td>19</td>
      <td>13</td>
      <td>28</td>
      <td>33</td>
    </tr>
    <tr>
      <td>DotL</td>
      <td>Q5ZYC6</td>
      <td>10</td>
      <td>26</td>
      <td>20</td>
      <td>32</td>
    </tr>
    <tr>
      <td>DotD</td>
      <td>Q5ZS45</td>
      <td>11</td>
      <td>9</td>
      <td>14</td>
      <td>33</td>
    </tr>
    <tr>
      <td>DotC</td>
      <td>Q5ZS44</td>
      <td>9</td>
      <td>11</td>
      <td>16</td>
      <td>22</td>
    </tr>
    <tr>
      <td>DotB</td>
      <td>Q5ZS43</td>
      <td>16</td>
      <td>11</td>
      <td>7</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Dis1</td>
      <td>Q5ZXS4</td>
      <td>6</td>
      <td>4</td>
      <td>16</td>
      <td>19</td>
    </tr>
    <tr>
      <td>DotY</td>
      <td>Q5ZYR7</td>
      <td>4</td>
      <td>9</td>
      <td>4</td>
      <td>10</td>
    </tr>
    <tr>
      <td>DotM</td>
      <td>Q5ZYC7</td>
      <td>2</td>
      <td>14</td>
      <td>3</td>
      <td>9</td>
    </tr>
    <tr>
      <td>DotK</td>
      <td>Q5ZYC5</td>
      <td>2</td>
      <td>6</td>
      <td>10</td>
      <td>9</td>
    </tr>
    <tr>
      <td>IcmW</td>
      <td>Q5ZS31</td>
      <td>5</td>
      <td>7</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <td>DotZ</td>
      <td>Q5ZV91</td>
      <td>1</td>
      <td>8</td>
      <td>3</td>
      <td>9</td>
    </tr>
    <tr>
      <td>DotN</td>
      <td>Q5ZYB7</td>
      <td>2</td>
      <td>6</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <td>Dis2</td>
      <td>Q5ZXA9</td>
      <td>2</td>
      <td>4</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <td>DotI</td>
      <td>Q5ZYC3</td>
      <td>1</td>
      <td>3</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <td>IcmV</td>
      <td>Q5ZS32</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <td>IcmT</td>
      <td>Q5ZYD1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>IcmS</td>
      <td>Q5ZYD0</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

_*UniProtKB Accession Number.†Proteins were identified by searching theMS/MS data against L. pneumophila(UniProt; 2930 entries) using Proteome Discoverer (v2.1, Thermo Scientific). Search parametersincluded MS1 masstolerance of 10 ppm and fragment tolerance of 0.1 Da. False discovery rate (FDR) was determined using Percolator and proteins/peptides with a FDR of ≤1% were retained for further analysis. Complete results are in Supplementary file 1 in supplementary material.‡Componentsidentified in thisstructure are in bold._

This is not the first time that additional components have been described in the Dot/Icm T4SS directly from the cryo-EM density map. In fact, in 2020 alone three proteins have been identified as components of the Dot/Icm T4SS through high-resolution cryo-EM: Lpg0294 (DotY), Lpg0657 (Dis1), and Lpg1549 (DotZ) (Durie et al., 2020; Meir et al., 2020). Although there is no apparent link between these three genes and the other known components of the Dot/Icm T4SS, a targeted genetic analysis may shed light on how these genes have been integrated into this system. Further studies are needed to probe the function of these newly identified Dot/Icm components.

Finally, we identified ‘chain 3’ as DotF (DotF1, residues 208–266). This portion of DotF consists of a small globular fold comprised of two β-sheets each consisting of three strands (Figure 2—figure supplement 7A). One face of DotF interacts with rungs 9, 10, and 11 of Dis3 (Figure 2—figure supplement 7B). The interface between the two proteins is comprised of hydrogen bonds, hydrophobic interactions, and salt bridges (Figure 2—figure supplement 7C). A DALI search of this portion of DotF resulted in several hits, most notably a T2SS protein from Escherichia coli known as GspC (PDB 3OSS) and a pilus protein from Pseudomonas aeruginosa known as PilP (PDB 21C4, Figure 2—figure supplement 7D). Like DotF, both structurally similar proteins are found within the periplasm in their respective systems (Korotkov et al., 2011; Tammam et al., 2011).

### Architecture of the Dot/Icm T4SS PR

There are a total of four chains within the C18 symmetry-imposed map of the PR. Three of these chains were unambiguously determined to be portions of a second copy of DotF (DotF2), DotG, and DotH, while one chain could not be identified and was left as a polyalanine chain model (Figure 3 and Figure 3—figure supplements 1–2 ). Located in the interior of the PR is a portion of DotG (residues 791–824) consisting of a single helix that starts from the inner membrane side of the PR and is followed by a short loop that extends toward the outer membrane or ‘top’ of the complex (Figure 3—figure supplement 3A). The short loop of DotG contacts a globular domain of DotH consisting of two β-sheets composed of four and five β-strands that contain residues 104–263 (Figure 3—figure supplement 3B). The interaction that is observed between DotG/DotH in the PR is similar in structure to those previously reported for VirB10/VirB9 and CagX/CagY and likely reflects an important function for retaining this organization within the PR (Sheedlo et al., 2020; Sgro et al., 2018).

![Figure 3.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig3-v2.jpg)

**Figure 3.:** (A) The PR of the Dot/Icm type IV secretion system (T4SS) is comprised of at least four peptide chains. Three have been identified as DotG (yellow), DotH (orange), and DotF2 (purple). A fourth chain could not be identified and is shown in gray. (B) Within the asymmetric unit, we observe interactions between DotF2-DotH and DotH-DotG.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) The refinement statistics for each identified component of the Dot/Icm type IV secretion system (T4SS) PR are shown in the table. (B) The model map correlation for the entire PR is shown with the masked data shown in green and the unmasked shown in black. (C) The fit of each model was also determined.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** The quality of the model was interpreted using per residue correlation coefficients. The correlation of each residue is plotted by spectrum on each component (left). The correlation coefficient was also plotted against residue number (right). The average correlation coefficient per residue is indicated by the dashed line.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) In the PR we have modeled portions of DotG and DotH, noting that the N-terminus of each protein is positioned on the inner membrane side of the PR and that the C-terminus of each protein is positioned on the outer membrane side of the PR. (B) The interaction between DotG and DotH spans two asymmetric units. The interactions between DotG and the first asymmetric unit (shown in orange) are shown in the left inset, and the interactions between DotG and the second asymmetric unit (shown in red) are shown in the right inset. (C) The structure of DotH consists of two distinct domains, one in the outer membrane cap (OMC) (DotHOMC) and one in the PR (DotHPR). Both domains show structural similarity to CagX (Helicobacter pylori) and VirB9 (Xanthomonas citri). (D) Though all three proteins are structurally homologous, the distance between the OMC and PR domains varies due to the length of the linker between them (shown in orange stripes). (E) Interactions between DotH and DotG within the PR are similar to those of VirB9/VirB10 and CagX/CagY.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (A) We have modeled a second DotF (DotF2) in the PR of the Dot/Icm type IV secretion system (T4SS) which is nearly identical to DotF1 modeled in the outer membrane cap (OMC). (B–C) DotF2 contacts one copy of DotH in the PR (B) with interactions that include hydrogen bonds and a salt bridge (C). The interactions observed between DotF2 and DotH use a similar surface to that of DotF1 and Dis3.

The structure of DotH is similar to the N-terminal regions of VirB9 (PDB 6GYB, residues 27–133) and CagX (PDB 6 × 6 J, residues 32–311), making DotH a bona fide structural homolog of VirB9 (Figure 3—figure supplement 3C,D) despite very little sequence similarity (Sheedlo et al., 2020; Sgro et al., 2018). The arrangement of DotH and DotG within the PR is similar to interactions between VirB9/VirB10 (PDB 6GYB) in the Xanthomonas citri T4SS and CagX/CagY (PDB 6X6J ) within the PR of the H. pylori Cag T4SS (Figure 3—figure supplement 3E; Sheedlo et al., 2020; Sgro et al., 2018). Interestingly, the X. citri T4SS core complex is smaller and composed of fewer components than the Dot/Icm and Cag T4SSs, and its region that shows structural similarity to the PR of the Dot/Icm and Cag T4SSs has previously not been considered a separate region of the X. citri core complex. Instead, previous reports describe an outer and inner layer of the X. citri T4SS (Sgro et al., 2018). However, when comparing the structures of the Dot/Icm and Cag T4SSs with the prototype X. citri T4SSs, it appears that its inner layer should now be considered structurally similar to the PR regions of the larger Dot/Icm and Cag T4SSs. Importantly, one major distinction observed for the X. citri T4SS is that the outer and inner layers of its core complex share the same symmetry operator (C14), rather than contain a symmetry mismatch as observed for both the Dot/Icm and Cag T4SSs.

Located adjacent to DotH and on the periphery of the PR is a small globular domain that we identified as DotF (residues 207–269). This portion of DotF consists of the same residues as was discovered in the OMC (DotF1) and thus, likely represents unique copies of DotF which we call DotF2. DotF2 is nearly identical in structure to the model of DotF1 that was built in the C13 symmetry-imposed maps of the OMC (RMSD of 0.5 Å). This results in a total of 31 copies of DotF contained within the intact Dot/Icm T4SS (Figure 3—figure supplement 4A). DotF2 engages DotH using a similar interface to that of DotF1 and Dis3, with buried surface areas of 575 and 655 Å, respectively (Figure 3—figure supplement 4B-D).

### Models constructed within the asymmetric map

The models that were generated from the 2.8 Å resolution, symmetry-imposed reconstructions of the OMC and PR were fit into the 3.8 Å map of the Dot/Icm T4SS that was generated without the imposition of symmetry. All models fit well within the asymmetric map with only minor changes in the positions of backbone atoms observed for each protein (Figure 4 and Figure 4—figure supplements 1–5). Notably, we modeled portions of two regions of the map that contained additional density within the asymmetric reconstruction. First, we observe 13 linkers between the OMC and PR (identified as residues 264–270 of DotH) in various conformations, revealing the direct connections between the two regions. Second, we observed five small globular folds located between the OMC and PR (Figure 4A, Figure 4—figure supplement 6A-C). These folds consist of two β-sheets and incorporate the linker from DotH as an additional β-strand in one of the two sheets (Figure 4—figure supplement 6C). Close inspection clearly showed that these domains contain folds nearly identical to that of the C-terminal domain of DotH in the OMC (residues 278–360). Upon fitting the C-terminal domain of DotH into this portion of the map, the register correlates well with the model, with mean side-chain CC values ranging from 0.68 to 0.72 (Figure 4—figure supplement 6D). We propose that these five additional domains of the DotH C-terminal domain are the five copies that do not span the symmetry mismatch between the OMC and PR. Thus, there are 18 copies of DotH in the entire structure with all 18 NTDs comprising the PR, 13 of the associated CTDs extending up to build part of the OMC disk, and the other five CTDs extending up only part way into the intervening space. Each of the intervening DotH C-terminal domains between the OMC and PR occurs every two to three asymmetric units, and the degree to which they can be observed varies, indicating that the position of these domains is not static with respect to the PR or the OMC (Figure 4B and Video 1). The flexibility of these five DotH CTDs suggests a mechanism through which the symmetry mismatch observed between the OMC and PR can be accommodated though the utility of the symmetry mismatch cannot be inferred.

![Figure 4.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig4-v2.jpg)

**Figure 4.:** (A) Within the asymmetric reconstruction of the Dot/Icm type IV secretion system (T4SS), we observe DotH (orange) in three separate places, the OMC (plane 1), the PR (plane 3), and the space in between the two (plane 2). (B) The number of copies of DotH in each plane differs. There are 13 symmetrical copies in the OMC (plane 1), 5 asymmetrical copies in the space between the OMC and PR (plane 2), and 18 symmetrical copies in the PR (plane 3).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) The refinement statistics for each identified component of the Dot/Icm type IV secretion system (T4SS) in the asymmetric reconstruction are shown in the table. (B) The model map correlation for the outer membrane cap (OMC) and periplasmic ring (PR) within the C1 reconstruction is shown with the masked data shown in green and the unmasked shown in black. (C) The fit of each model was also determined.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** The model map correlation of each model within the outer membrane cap (OMC) and periplasmic ring (PR) that was reconstructed using the asymmetric map.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** The quality of the model was interpreted using per residue correlation coefficients. The correlation of each residue is plotted by spectrum on each component (left). The correlation coefficient was also plotted against residue number (right). The average correlation coefficient per residue is indicated by the dashed line.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** The quality of the model was interpreted using per residue correlation coefficients. The correlation of each residue is plotted by spectrum on each component (left). The correlation coefficient was also plotted against residue number (right). The average correlation coefficient per residue is indicated by the dashed line.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** The quality of the model was interpreted using per residue correlation coefficients. The correlation of each residue is plotted by spectrum on each component (left). The correlation coefficient was also plotted against residue number (right). The average correlation coefficient per residue is indicated by the dashed line.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig4-figsupp6-v2.jpg)

**Figure 4—figure supplement 6.:** (A) The density that is observed for the DotH linker varies depending on the position of DotH within the outer membrane cap (OMC). At the extreme ends of the range of flexibility are the ‘bent’ (left) and ‘straight’ forms with varying degrees of the ‘kinked’ form (center) observed between the two extremes. (B) The flexibility within the linker allows for differential placement of DotH within the OMC as compared to the periplasmic ring (PR). (C) The five copies of DotHAsym (dark orange) utilize the linker from an adjacent DotH molecule (orange) as a β-strand in one of two β-sheets. (D) The resolution of the five copies of DotHAsym varies depending on where it is positioned within the map. However, landmark residues are observed fitting well into the density in all five copies.

![Video 1.](https://cdn.elifesciences.org/articles/70427/elife-70427-video1.mp4.jpg)

**Video 1.:** Within the asymmetric reconstruction of the Dot/Icm T4SS we observe DotH (colored in orange) in three distinct portions: the outer membrane cap (OMC), the periplasmic ring (PR), and the asymmetric region between the OMC and PR. The region of DotH observed in each portion varies with the N-terminal domain observed only in the PR and the C-terminal domain observed in the OMC and the asymmetric region. The number of copies of DotH also varies by position with 18 copies of the N-terminal domain observed in the PR, 5 copies of the C-terminal domain observed in the asymmetric region, and 13 copies of the C-terminal domain observed in the OMC.

Interestingly, we do not see similar densities between the OMC and PR of the H. pylori Cag T4SS, even though there is also a symmetry mismatch in this system and DotH is structurally homolgous to CagX. With this understanding of how the symmetry mismatch is accommodated in the Dot/Icm T4SS, we propose that flexible and/or dynamic connection between regions of PR and OMC, that are not seen in the Cag T4SS, will be important for the Dot/Icm T4SS translocating such a uniquely large repertoire of secretion substrates. Although we are now in a position to describe how the symmetry mismatch is accommodated, its impact on function remains to be determined.

### The dome density contains the C-terminus of DotG

Five maps of the T4SS were reconstructed using a 3DVA in cryoSPARC that resolved the secondary structure of the dome positioned in the center of the OMC (Figure 5A, and Table 3). To conduct this analysis, the particles had to be downsampled from 1.1 to 2.2 Å/pix, resulting in a lower global resolution of ~4.6 Å. Within this dome there are 16 α-helices that appear nearly identical at this resolution. Since this resolution is already close to the Nyquist limit of the data (~4.4 Å), imposing C16 symmetry did not improve the resolution of the maps. However, based on previous studies of T4SSs, we reasoned that this portion of the T4SS may correspond to DotG, the proposed L. pneumophila homolog of VirB10 via sequence comparisons (Nagai and Kubori, 2011). Indeed, a model of the C-terminal domain of DotG generated in Swiss Model using VirB10 as a template fits into the resolved dome density (Figure 5B; Waterhouse et al., 2018). This finding is consistent with our previous observation that the Dot/Icm T4SS core complex isolated from a dotG deletion strain lacked the dome portion of the OMC (Durie et al., 2020). Interestingly, the interface between the 16 copies of DotG and the rest of the OMC disk is sparse, potentially leading to the low-resolution reconstruction of this portion of the map (Video 2). Based on the structure of DotG modeled within the PR (residues 791–824) and the homology model fit into the dome density (consisting approximately of residues 857–1046), we hypothesize that DotG extends from the PR to the dome, though a physical connection between the two structures is not observed. This would lead to a total of 18 copies of DotG in the intact Dot/Icm T4SS with two copies of DotG not visualized within the dome likely due to structural heterogeneity. Taken together, we propose a final stoichiometry of 31:26:18:18:13:13:13:13:13 (DotF:DotD:DotG:DotH:DotC:DotK:Dis1:Dis2:Dis3) for the Dot/Icm T4SS.

![Figure 5.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig5-v2.jpg)

**Figure 5.:** (A) The ‘dome’ density located in the center of the outer membrane cap (OMC) was uninterpretable in the C1 reconstruction (top), likely due to structural heterogeneity. The density is considerably improved after 3D variability analysis with an apparent 16-fold symmetry observed about the middle of the structure (bottom). (B) The density within the asymmetric unit of the dome contains similar structural features seen in VirB10 homologs (top). A model of the DotG C-terminus was constructed in Swiss Model which fits into this density after refinement (bottom).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/70427/elife-70427-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Two DotC were observed in the maps that were reconstructed during 3D variability analysis, one which contains an N-terminal extension (DotCLong) and one which does not (DotCshort). (B) The placement of these C-terminal domains is periodic within the maps, occurring every two to three asymmetric units.

**Table 3.**
 Three-dimensional variability analysis (3DVA) map reconstruction and model refinement.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Map 1</th>
      <th>Map 2</th>
      <th>Map 3</th>
      <th>Map 4</th>
      <th>Map 5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EMDB accession codes</td>
      <td>24018</td>
      <td>24020</td>
      <td>24023</td>
      <td>24024</td>
      <td>24026</td>
    </tr>
    <tr>
      <td>Data collection and processing</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Magnification</td>
      <td>81,000×</td>
      <td>81,000×</td>
      <td>81,000×</td>
      <td>81,000×</td>
      <td>81,000×</td>
    </tr>
    <tr>
      <td>Voltage (kV)</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
    </tr>
    <tr>
      <td>Total electron dose (e-/Å2)</td>
      <td>50</td>
      <td>50</td>
      <td>50</td>
      <td>50</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Defocus range (µm)</td>
      <td>–1.5 to –2.1</td>
      <td>–1.5 to –2.1</td>
      <td>–1.5 to –2.1</td>
      <td>–1.5 to –2.1</td>
      <td>–1.5 to –2.1</td>
    </tr>
    <tr>
      <td>Pixel size (Å)</td>
      <td>1.1</td>
      <td>1.1</td>
      <td>1.1</td>
      <td>1.1</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>Processing software</td>
      <td>CryoSPARC</td>
      <td>CryoSPARC</td>
      <td>CryoSPARC</td>
      <td>CryoSPARC</td>
      <td>CryoSPARC</td>
    </tr>
    <tr>
      <td>Initial particles (number)</td>
      <td>303,447</td>
      <td>303,447</td>
      <td>303,447</td>
      <td>303,447</td>
      <td>303,447</td>
    </tr>
    <tr>
      <td>Final particles (number)</td>
      <td>79,720</td>
      <td>75,959</td>
      <td>64,698</td>
      <td>42,013</td>
      <td>41,057</td>
    </tr>
    <tr>
      <td>Map sharpening B-factor</td>
      <td>–88.5</td>
      <td>–85.4</td>
      <td>–85,8</td>
      <td>–84.4</td>
      <td>–80.1</td>
    </tr>
    <tr>
      <td>Map resolution (Å)</td>
      <td>4.6</td>
      <td>4.6</td>
      <td>4.6</td>
      <td>4.6</td>
      <td>4.6</td>
    </tr>
    <tr>
      <td>FSC threshold</td>
      <td>0.143</td>
      <td>0.143</td>
      <td>0.143</td>
      <td>0.143</td>
      <td>0.143</td>
    </tr>
    <tr>
      <td>Model refinement and validation</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Starting models</td>
      <td>7MUC</td>
      <td>7MUC</td>
      <td>7MUC</td>
      <td>7MUC</td>
      <td>7MUC</td>
    </tr>
    <tr>
      <td>FSC</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>4.6</td>
      <td>4.6</td>
      <td>4.6</td>
      <td>4.8</td>
      <td>4.8</td>
    </tr>
    <tr>
      <td>0.143</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>4.5</td>
    </tr>
    <tr>
      <td>Model residues</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total</td>
      <td colspan="5">25,121</td>
    </tr>
    <tr>
      <td>DotC</td>
      <td colspan="5">59–267</td>
    </tr>
    <tr>
      <td>DotD1</td>
      <td colspan="5">23–162</td>
    </tr>
    <tr>
      <td>DotD2</td>
      <td colspan="5">24–160</td>
    </tr>
    <tr>
      <td>DotF1</td>
      <td colspan="5">208–266</td>
    </tr>
    <tr>
      <td>DotF2</td>
      <td colspan="5">207–269</td>
    </tr>
    <tr>
      <td>DotG</td>
      <td colspan="5">791–824, 862–978, 999–1046</td>
    </tr>
    <tr>
      <td>DotH</td>
      <td colspan="5">104–361</td>
    </tr>
    <tr>
      <td>DotK</td>
      <td colspan="5">38–188</td>
    </tr>
    <tr>
      <td>Lpg0657</td>
      <td colspan="5">42–65, 88–236</td>
    </tr>
    <tr>
      <td>Lpg0823</td>
      <td colspan="5">39–116</td>
    </tr>
    <tr>
      <td>Lpg2847</td>
      <td colspan="5">113–320</td>
    </tr>
    <tr>
      <td>Unknown OMC</td>
      <td colspan="5">122–130</td>
    </tr>
    <tr>
      <td>Unknown PR</td>
      <td colspan="5">1–38, 70–79</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>9.55</td>
      <td>9.64</td>
      <td>15.53</td>
      <td>9.47</td>
      <td>9.85</td>
    </tr>
    <tr>
      <td>Molprobity</td>
      <td>2.80</td>
      <td>2.77</td>
      <td>2.76</td>
      <td>2.68</td>
      <td>2.73</td>
    </tr>
    <tr>
      <td>Bonds</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Lengths (Å)</td>
      <td>0.006</td>
      <td>0.005</td>
      <td>0.003</td>
      <td>0.004</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>Angles (°)</td>
      <td>0.798</td>
      <td>0.765</td>
      <td>0.540</td>
      <td>0.702</td>
      <td>0.711</td>
    </tr>
    <tr>
      <td>Ramachandran (%)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Favored</td>
      <td>94.0</td>
      <td>94.2</td>
      <td>94.7</td>
      <td>95.2</td>
      <td>94.7</td>
    </tr>
    <tr>
      <td>Allowed</td>
      <td>6.0</td>
      <td>5.8</td>
      <td>5.3</td>
      <td>4.8</td>
      <td>5.3</td>
    </tr>
    <tr>
      <td>Outliers</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>B-factors</td>
      <td>147.96</td>
      <td>154.48</td>
      <td>146.18</td>
      <td>145.88</td>
      <td>145.07</td>
    </tr>
    <tr>
      <td>PDB</td>
      <td>7MUQ</td>
      <td>7MUS</td>
      <td>7MUV</td>
      <td>7MUW</td>
      <td>7MUY</td>
    </tr>
  </tbody>
</table>

![Video 2.](https://cdn.elifesciences.org/articles/70427/elife-70427-video2.mp4.jpg)

**Video 2.:** Within the five maps that were used to resolve the dome region in the outer membrane cap (OMC) we note that the extent to which the DotC N-terminus varies considerably. The extension of DotC is only strongly observed in four or five copies of DotC in each map.

In addition to the portion of the dome that we predict is DotG, there are also two segments of DotC that were not resolved in our previous electron microscopy density maps. These include an internal connection (residues 162–172) and a relatively long N-terminal extension (residues 28–57, Figure 5, Figure 5—figure supplement 1). The internal bridge within DotC consists of a single loop connecting residues 161 and 173. In contrast, the N-terminal extension of DotC was modeled as two relatively large helices positioned near DotG and bridging adjacent asymmetric units (Figure 5—figure supplement 1B). Notably, this portion of DotC was only observed in either four or five of the 13 copies of DotC observed in each map. The copies of DotC that contain this portion are positioned such that this extension is in a similar position relative to DotG within the dome (Figure 5—figure supplement 1B and Video 3).

![Video 3.](https://cdn.elifesciences.org/articles/70427/elife-70427-video3.mp4.jpg)

**Video 3.:** Within the dome density we observe 16 helical protrusions that contain a fold similar to that of VirB10. These 16 folds are positioned directly above the 18 helices that we have identified as DotG in the periplasmic ring (PR). It is suspected that the heterogeneity of DotG within the disk arises from the sparse contacts observed between DotG and DotC along with a flexible linker that appears to connect the two segments of DotG shown here.

The discovery of the DotG C-terminal domain within the dome density is in line with previous reports that hypothesized that DotG is a homolog of VirB10. However, we have unexpectedly uncovered that the Dot/Icm incorporates only 16 copies of DotG into the OMC dome out of the 18 DotG copies in the PR, giving rise to another symmetry mismatch within this system. The finding that there is variability within the N-terminus of DotC also suggests that interactions between DotG and the rest of the OMC disk are primarily mediated by DotC. Future studies will seek to resolve the origin of the C16:C18 (dome:PR) mismatch, including the location and role of the two DotG C-terminal domains that do not span the mismatch, as well as the interactions between DotC and DotG.

When comparing the five maps determined using 3DVA, not only does DotG sample different positions in the ‘dome’ with respect to the rest of the OMC, but the PR occupies different positions with respect to the OMC disk as well. Having noted that the OMC disk is anchored into the outer membrane with as many as seven interactions per asymmetric unit (or over 90 for the complete complex) and having observed multiple conformations of the OMC dome and the PR relative to the OMC disk, we visualized the continuously distributed conformations in the context of a movie (Video 4). The movie shows that the OMC dome, OMC disk, and PR of Dot/Icm T4SS can accommodate various orientations in relation to each other that suggest that the complex could undergo a ratcheting motion, in which the dome and PR rotate back and forth about the central axis with the different regions of the complex tethered together by the physical connections across the symmetry mismatches. This leads to a prediction that the multiple symmetry mismatches and various conformational states of the complex are important in how the Dot/Icm T4SS accommodates a larger number of protein substrates than other T4SSs (Schroeder, 2017).

![Video 4.](https://cdn.elifesciences.org/articles/70427/elife-70427-video4.mp4.jpg)

**Video 4.:** Using 3D variability analysis, we reconstructed a total of five maps that displayed differences in the way the outer membrane cap (OMC) and periplasmic ring (PR) were positioned. These maps led to the identification of an approximate 16-fold symmetry about the center of the dome positioned within the OMC.

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
      <td>Strain, strain background(Legionella pneumophila)</td>
      <td>Lp02; WT</td>
      <td>PMID:23717549</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MotionCor2</td>
      <td>PMID:28250466</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CTFFind4</td>
      <td>PMID:26278980</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cryoSPARC</td>
      <td>PMID:28165473PMID:33582281</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION</td>
      <td>PMID:27685097PMID:30412051</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>PMID:20383002</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF Chimera</td>
      <td>PMID:15264254 PMID:29340616</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PHENIX</td>
      <td>PMID:29872004</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DALI server</td>
      <td>PMID:31263867PMID:31606894</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Preparation of strains

L. pneumophila was cultured in ACES (Sigma)-buffered yeast extract broth at pH 6.9 supplemented with 0.1 mg/ml thymidine, 0.4 mg/ml L-cysteine, and 0.135 mg/ml ferric nitrate or on solid medium of this broth supplemented with 15 g/l agar and 2 g/l charcoal. The L. pneumophila laboratory strain Lp02, a thymidine auxotroph derived from the clinical isolate Philadelphia-1 (Rao et al., 2013), was utilized.

### Complex isolation

Complexes were isolated from wild-type L. pneumophila strain Lp02 as described (Durie et al., 2020; Kubori et al., 2014; Kubori and Nagai, 2019). Cells were suspended in 140 ml of buffer containing 150 mM Trizma base pH 8.0, 500 mM NaCl, and EDTA-free Complete Protease Inhibitor (Roche) at 4°C. The suspension was incubated on the benchtop, with stirring, until it reached ambient temperature. PMSF (final concentration 1 mM), EDTA (final concentration 1 mM), and lysozyme (final concentration 0.1 mg/ml) were added, and the suspension was incubated at ambient temperature for an additional 30 min. Bacterial membranes were lysed using detergent and alkaline lysis. Triton X-100 (20% w/v) with AG501-X8 resin (BioRad) was added dropwise, followed by MgSO4 (final concentration 3 mM), DNaseI (final concentration 5 μg/ml), and EDTA (final concentration 10 mM), and then the pH was adjusted to 10.0 using NaOH. The remaining steps were conducted at 4°C. The cell lysate was subjected to centrifugation at 12,000 × g for 20 min to remove unlysed material. The supernatant was then subjected to ultracentrifugation at 100,000 × g for 30 min to pellet membrane complexes. The membrane complex pellets were resuspended and soaked overnight in a small volume of TET buffer (10 mM Trizma base pH 8.0, 1 mM EDTA, 0.1% Triton X-100). The resuspended sample was then subjected to centrifugation at 14,000 × g for 30 min to pellet debris. The supernatant was subjected to ultra-centrifugation at 100,000 × g for 30 min. The resulting pellet was resuspended in TET and complexes were further separated by Superose 6 10/300 column chromatography in TET buffer with 150 mM NaCl using an AKTA Pure system (GE Life Sciences). The sample collected from the column was used for microscopy. Mass spectrometry analysis was performed as described (Anwar et al., 2018).

### Cryo-EM data collection and map reconstruction

For cryo-EM, 4 μl of the isolated Dot/Icm T4SS sample was applied to a glow discharged ultrathin continuous carbon film on Quantifoil 2/2 200 mesh copper grids (Electron Microscopy Services). The sample was applied to the grid 5 consecutive times and incubated for ~60 s after each application. The grid was then rinsed in water to remove detergent before vitrification by plunge-freezing in a slurry of liquid ethane using an FEI vitrobot at 4°C and 100% humidity.

The data were collected at the Stanford-SLAC Cryo-EM Facility (Menlo Park, CA) using Titan Krios microscopes (Thermo Fisher, Waltham, MA) operated at 300 keV and equipped with a Quantum energy filter. The images were collected with a K3 Summit direct electron detector operating in counting mode, at a nominal magnification of 81,000, corresponding to a pixel size of 1.1 Å. The energy slit was set at a width of 15 eV. The total dose was 50 e/Å2, fractionated over 33 frames in 2.96 s. Data were collected using EPU software (Thermo Fisher, Waltham, MA) with a nominal defocus range set from −1.5 to −2.1 μm. A total of 12,263 micrographs were collected.

The video frames were first dose-weighted and aligned using Motioncor2 (Zheng et al., 2017). The contrast transfer function (CTF) values were determined using CTFFind4 (Rohou and Grigorieff, 2015). Image processing was carried out using cryoSPARC, RELION 3.0, and RELION 3.1 (Punjani et al., 2017; Zivanov et al., 2018). Using the template picker in cryoSPARC, 1,389,426 particles were picked from 12,204 micrographs. Particles were extracted using a 510 pixel box size (1.1 Å/pix). The extracted particles were used to generate representative 2D classes in cryoSPARC and ~136,000 particles found in the well-resolved classes were kept. The selected particles were used for an ab initio model in cryoSPARC, which was then used as the reference for 3D auto-refinement with and without C13 symmetry (lowpass filtered to 30 Å). Finally, a solvent mask and B-factor were applied to improve the overall features and resolution of the 3D maps with and without C13 symmetry, resulting in reconstruction of 3D maps with a global resolution of 3.4 Å (C13) and 3.8 Å (C1).

The C13 refined volumes and corresponding particles were then exported to RELION for focused refinements. Estimation of beam-tilt values (CTF-refinement) was applied to the selected particles using RELION. With the CTF-refined particle stack, C13 symmetry-imposed refinement with a soft mask around the core complex was done, resulting in a 3.8 Å resolution 3D map.

For focused refinement of the OMC disk, signal subtraction for each particle containing the OMC disk was used with a soft mask. The subtracted particles were subjected to alignment-free focused 3D classification (three classes). The best resolved 3D class of the OMC (~89,000 particles) was then subjected to a masked 3D refinement with local angular searches using C13 symmetry resulting in a 3.7 Å resolution density map. Estimation of per-particle defocus values (CTF-refinement) was applied to the selected particles using RELION. With the CTF-refined particle stack, C13 symmetry-imposed refinement with a soft mask around the OMC disk region of the Dot/Icm T4SS core complex was done, resulting in a 3.2 Å resolution 3D map that contained improved structural features. B-factor sharpening and calculation of masked Fourier shell correlation (FSC) curves steps resulted in the final OMC disk map with 2.8 Å resolution.

The same steps were followed for focused refinement of the PR, starting with signal subtraction for each particle containing the PR with a soft mask. The subtracted particles were subjected to alignment-free focused 3D classification (three classes). The best resolved 3D class of the PR (~44,000 particles) was selected based on class distribution (particle distribution), estimated resolution, and comparison of the 3D density maps. This class was then subjected to a masked 3D refinement with local angular searches using C18 symmetry resulting in a 7.5 Å resolution. Estimation of per-particle defocus values (CTF-refinement) was applied to the selected particles using RELION. With the CTF-refined particle stack, C18 symmetry-imposed refinement with a soft mask around the PR region of the Dot/Icm T4SS core complex was done, resulting in a 4.1 Å resolution 3D map. These maps contained improved features compared to those prior to CTF-refinement. B-factor sharpening and calculation of masked FSC curves resulted in the final PR map with 2.8 Å resolution in.

In a separate workflow from that used for focused refinements, 3DVA in cryoSPARC was performed to assess continuous flexibility in the dome of the OMC. For this analysis, ~136,000 particles, which had resulted in a 3.8 Å resolution map with no symmetry imposed as described above, and, because of box size limits in cryoSPARC, were downsampled to a 250 pixel box size (~2.2 Å/pix). A new ab initio model was generated from these down sampled particles, and a C1 homogeneous refinement resulted in a 4.6 Å map. 3DVA was then performed using the downsampled particles and mask from the refinement job, three modes, and a filter resolution of 5 Å. The 3DVA display job was run in the simple output mode with 20 frames per clusters. All clusters exhibited the differences in alignment of the C16 dome and the C18 PR about the rotational axis, with the C13 OMC disk held in the same relative position (Video 4). The 3DVA display job was then run in the cluster output mode with five clusters. The particles and maps from each cluster were separately subjected to C1 homogeneous refinement. In each case, the resulting 3D maps were at 4.6 Å resolution.

### Model construction and refinement

To construct a model of the OMC, the asymmetric unit of the previously determined structure of the OMC (PDB 6 × 62) was first extracted in Pymol and docked into the map presented here using UCSF Chimera (Pettersen et al., 2004). This model was then refined in PHENIX using Phenix.real.space.refine (Afonine et al., 2018). The models were then inspected in Coot, and any subtle differences between the two maps were examined and corrected by hand. Where appropriate, the models were extended in Coot (Emsley et al., 2010). Each of the components that were identified in this study (Lpg0823, Lpg2847, and DotF1) were constructed de novo in Coot to generate a model of the entire asymmetric unit. This model was then refined in PHENIX using secondary structure and Ramachandran restraints. The refinement strategy was also optimized by adjusting the nonbonded weighting. A model of the entire OMC was then generated in PHENIX by applying symmetry and further refined as described above. The model was inspected for fit by hand and validated in Phenix using phenix.validation.cryoem. A model of the PR was constructed essentially as described above using as a starting point the previously reported polyalanine models (PDB 6 × 64). The models were adjusted in Coot, symmetrized, and refined in PHENIX essentially as described above to generate a model of the entire PR.

To generate a model of the OMC, the models of the OMC and PR described here (PDBs 7MUC and 7MUE, respectively) were first fit into the map generated without symmetry. The model was then refined in PHENIX and adjusted where necessary in Coot. Models of the DotH linkers were generated by hand in Coot. To model the C-terminal domain of DotH between the OMC and PR, a polyalanine model was first constructed. The DotH C-terminal domain was then aligned to this polyalanine model and refined by hand in Coot. Once completed the asymmetric model was refined in PHENIX.
