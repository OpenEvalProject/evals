# Crystal structures of the CPAP/STIL complex reveal its role in centriole assembly and human microcephaly

## Authors

- Matthew A Cottee<sup>1</sup>
- Nadine Muschalik<sup>1</sup>
- Yao Liang Wong<sup>2</sup>
- Christopher M Johnson<sup>3</sup>
- Steven Johnson<sup>1</sup>
- Antonina Andreeva<sup>3</sup>
- Karen Oegema<sup>2</sup>
- Susan M Lea<sup>1</sup>
- Jordan W Raff<sup>1</sup>
- Mark van Breugel<sup>3</sup> †

### Affiliations

1. Sir William Dunn School of Pathology University of Oxford Oxford United Kingdom
2. Department of Cellular and Molecular Medicine Ludwig Institute for Cancer Research, University of California, San Diego La Jolla United States
3. Laboratory of Molecular Biology Medical Research Council Cambridge United Kingdom

† Corresponding author

## Abstract

Centrioles organise centrosomes and template cilia and flagella. Several centriole and centrosome proteins have been linked to microcephaly (MCPH), a neuro-developmental disease associated with small brain size. CPAP (MCPH6) and STIL (MCPH7) are required for centriole assembly, but it is unclear how mutations in them lead to microcephaly. We show that the TCP domain of CPAP constitutes a novel proline recognition domain that forms a 1:1 complex with a short, highly conserved target motif in STIL. Crystal structures of this complex reveal an unusual, all-β structure adopted by the TCP domain and explain how a microcephaly mutation in CPAP compromises complex formation. Through point mutations, we demonstrate that complex formation is essential for centriole duplication in vivo. Our studies provide the first structural insight into how the malfunction of centriole proteins results in human disease and also reveal that the CPAP–STIL interaction constitutes a conserved key step in centriole biogenesis.

## Introduction

Centrioles are small cylindrical organelles whose outer walls contain a ninefold symmetric array of microtubule triplets. These structures form the basal bodies that template the assembly of cilia and flagella, and they also organise a proteinaceous matrix termed the pericentriolar material (PCM) to form centrosomes, the main microtubule organising centres in animal cells. These organelles play an important part in many aspects of cell organisation, and centriolar dysfunction is linked to a plethora of human diseases, including cancer, obesity, macular degeneration and polycystic kidney disease (Nigg and Raff, 2009; Bettencourt-Dias et al., 2011).

Recently, an unexpected genetic link has emerged between centriole/centrosome assembly and human brain size. Autosomal recessive primary microcephaly (MCPH) is a rare condition where patients are born with small brains (Thornton and Woods, 2009). All eight identified MCPH genes encode proteins that localise to centrioles and/or centrosomes/spindle poles (Thornton and Woods, 2009; Hussain et al., 2012). It is unclear why mutations in these proteins are linked to such a specific neuro-developmental problem in humans, but it seems likely that some aspect of centriole/centrosome function must be particularly important for the proper proliferation of human neural progenitors (Siller and Doe, 2009; Megraw et al., 2011). In support of this possibility, mutations in the centriolar components CPAP (DSas-4 in Drosophila, here called dCPAP) and STIL (Ana2 in Drosophila, here called dSTIL) in flies lead to defects in the asymmetric division of larval neural stem/progenitor cells (Basto et al., 2006). Mutations in MCPH proteins in mice, however, lead to complex phenotypes that can include, but are not restricted to, microcephaly (McIntyre et al., 2012). Moreover, compelling genetic links are now emerging between centrioles/centrosomes and DNA damage repair (DDR) pathways: mutations in certain MCPH genes and in genes encoding other centriole/centrosome proteins can lead to Seckel syndrome and MOPD, pathologies normally associated with defects in DDR (Megraw et al., 2011). Thus, the cellular mechanisms that lead to pathology when centriole/centrosome proteins are mutated in humans remain unclear.

Centrioles are complex structures, but work in several model systems revealed only a small number of conserved proteins to be important for centriole assembly. These include PLK4/SAK, SAS-6, STIL/Ana2, CPAP/CenpJ/SAS-4, Cep152/Asl, and CEP135 (Brito et al., 2012; Gonczy, 2012). Several studies have identified a complex web of putative interactions between these proteins (Cizmecioglu et al., 2010; Dzhindzhev et al., 2010; Hatch et al., 2010; Tang et al., 2011; Vulprecht et al., 2012; Lin et al., 2013). However, an understanding of centriole architecture and its assembly mechanisms will ultimately require high-resolution structures of the key centriolar components and their complexes. The power of combining structural studies with protein biochemistry and functional in vivo experiments has been demonstrated by work on SAS-6. These studies revealed how SAS-6 homo-oligomerises to organise the central cartwheel (Kitagawa et al., 2011b; van Breugel et al., 2011), the earliest structurally defined intermediate in centriole assembly (Brito et al., 2012; Gonczy, 2012), and suggested how SAS-6 might interact with SAS-5, the proposed STIL homologue in worms (Qiao et al., 2012). Additionally, high-resolution structures of Sak/Plk4 fragments have recently been solved (Leung et al., 2002; Slevin et al., 2012). However, equivalent studies with other core centriolar components or especially their complexes are currently missing, and how any of these proteins might be structurally and mechanistically compromised in MCPH is not known.

Of particular interest in this regard is the putative centriolar CPAP–STIL complex, as mutations in both components result in MCPH (Leal et al., 2003; Bond et al., 2005; Gul et al., 2006; Darvish et al., 2010). CPAP and STIL are strictly required for centriole assembly: STIL at a very early stage (Stevens et al., 2010b; Tang et al., 2011; Kitagawa et al., 2011a; Arquint et al., 2012; Vulprecht et al., 2012) and CPAP slightly later (Kirkham et al., 2003; Leidel and Gonczy, 2003; Basto et al., 2006; Kleylein-Sohn et al., 2007; Dobbelaere et al., 2008; Vulprecht et al., 2012), possibly by controlling the organisation (Pelletier et al., 2006; Dammermann et al., 2008) and length of the centriolar microtubules (Blachon et al., 2009; Kohlmaier et al., 2009; Schmidt et al., 2009; Tang et al., 2009; Kim et al., 2012). A direct interaction between STIL and CPAP has been observed in yeast-two-hybrid and pull-down experiments (Tang et al., 2011; Vulprecht et al., 2012). Intriguingly, a MCPH mutation (E1235V) in the conserved C-terminal domain of CPAP (the so-called TCP-domain or G-Box) appeared to weaken this yeast-two-hybrid interaction (Tang et al., 2011). Tissue culture experiments suggested that this MCPH mutation might cause a partial loss-of-function of CPAP (Kitagawa et al., 2011a). However, the same study also found that the E1235V mutation results in an enhanced functionality of CPAP when overexpressed in vivo (Kitagawa et al., 2011a). To understand how CPAP and STIL interact and how the MCPH mutation affects CPAP functionality in vitro and in vivo, we undertook a detailed biochemical, structural and functional study of the putative CPAP–STIL complex.

## Results

### The CPAP TCP domain binds to a conserved proline-rich motif in STIL

Yeast-two-hybrid experiments suggested that a region of human CPAP comprising its conserved C-terminal TCP domain (or G-box) can interact with a ∼400 amino acid (aa) region (residues 231–619) of human STIL (Tang et al., 2011). To try to identify the region of STIL most likely to be involved in an interaction with CPAP, we carried out a sequence alignment with multiple metazoan STIL proteins (Figure 1A, Figure 1—figure supplement 1). This analysis revealed a short (∼40 aa) highly conserved proline-rich region (CR2) (Figure 1A) within this interval. To test whether this region of STIL could bind to the CPAP TCP domain, we recombinantly produced the TCP domain of Danio rerio CPAP and used isothermal titration calorimetry (ITC) to test its ability to bind to a fragment of D. rerio STIL that spanned CR2 (residues 404–448) (Figure 1D, Table 1). The two proteins formed a 1:1 complex with a KD of ∼2 μM. Next, we further split the peptide to test the binding contribution from its N-terminal (residues 411–428) and C-terminal region (residues 429–448). The N-terminal region exhibited an only slightly weaker binding (KD ∼4 μM) to the TCP domain, whereas the C-terminal region showed a very weak binding (KD > 500 μM) (Figure 1D; Table 1). We conclude that the CPAP TCP domain binds to a short conserved motif in STIL (CR2) with a potentially biologically significant affinity, and that the majority of the binding affinity comes from interactions with residues within the first proline-rich region in CR2.

![Figure 1.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig1-v1.jpg)

**Figure 1.:** (A) Schematic representation of D. rerio CPAP and STIL. CPAP is a 1124 amino acid (aa) protein with three predicted coiled coil (cc) domains and a C-terminal TCP domain. STIL is a 1263 aa protein with one predicted cc domain and several conserved regions (CR). The proline-rich CR2 domain is enlarged and coloured according to Consurf conservation scores (Glaser et al., 2003) from cyan (variable) to burgundy (conserved). The constructs used in this study are indicated by bars. (B) Two views of the TCP domain structure (green) in complex with the STIL peptide (orange), rotated by 180°. Images on the left of each view show a ribbon representation and images on the right show the TCP domain as a molecular surface coloured according to Consurf conservation scores. Note the presence of a conserved patch (dashed circle) along the edge of the TCP domain where the STIL peptide is bound. This patch contains aromatic residues (black sticks) that would be well placed to interact with conserved prolines in the C-terminal part of the STIL CR2 region that we had to omit for crystallisation. ITC experiments (Figure 1D) suggest that these putative additional contacts would only contribute weakly to overall binding. (C) Detailed view of the D. rerio CPAP–STIL interaction interface coloured according to Consurf conservation scores. Interface residues are shown in sticks, and the TCP domain is shown as a semi-transparent molecular surface. Contact residues are labelled in green (CPAP) and orange (STIL). Dotted yellow lines indicate hydrogen-bonds. The dark orange sphere represents a bound water molecule. (D) ITC analysis using the STIL constructs shown in Figure 1A. The excess heat measured on titrating STIL into CPAP at 25°C was fitted to a single set of binding sites model. Fitted KD values are indicated together with their standard deviations. (E and F) Ribbon models of the apo-structures of the D. rerio CPAP TCP domain: (E) WT apo-structure; (F) E1021V (MCPH mutation) apo-structure (V1021 represented as red spheres).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** The numbering refers to D. rerio STIL. The alignment is coloured by conservation according to the Consurf conservation score from cyan (variable) to burgundy (conserved).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Alignment of the sequence repeats of D. rerio CPAP937–1124. Residues are coloured according to the Clustalx colour scheme. R, Repeat. Repeat 1 was not visible in the electron density map of D. rerio apo-CPAP937–1124 but could be seen partially in the structure of the complex between D. rerio CPAP937–1124 and STIL408–428. (B) Sequence logo of the CPAP937–1124 repeat with the relative residue frequencies at each position. Prominent features of this repeat are two PDG motifs and the high frequency of aromatic residues adjacent to the first PDG motif in position 6 of the repeat. (C) Left: ribbon presentation of the D. rerio apo CPAP937–1124 structure with its sequence repeats rainbow-coloured from N- to C-terminus. R, Repeat. An individual structural repeat consists of a β-hairpin. The aromatic residues found in position 6 of the repeat are shown in black sticks. These aromatic residues run along the edge of one side of the β-sheet, where the proline-rich STIL peptide binds. The PDG motifs frequently constitute the β-turns of the TCP repeats. Boxed are three of these turns that are presented on the right as a close-up. In this close-up, residues of the PDG motif are labelled and shown in sticks. The Asp residue in this motif hydrogen-bonds (dotted black lines) to the main-chain of the (n) + 1 neighbouring residue.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) Panel showing size exclusion chromatography coupled to multi-angle light scattering (SEC-MALS) chromatograms. CPAP937–1124 was injected at concentrations of approximately 70 μM (light grey), 460 μM (dark grey) and 2.4 mM (black). The corresponding chromatogram traces (thin lines) show the refractive index signal. The concentrations of the CPAP937–1124 monomer measured at the peaks are indicated, and heavy solid lines across the peaks show the calculated molar masses. When averaged across the central 50% of the peaks, these molar masses were 22 kDa, 23 kDa, and 29 kDa, respectively. The theoretical molecular weight of a CPAP937–1124 monomer is 22 kDa. The Rh of CPAP937–1124 determined at the intermediate concentration was 2.9 ± 0.15 nm, which is significantly larger than expected for a globular protein of this mass and thus is consistent with the extended crystallographic structure. SEC-MALS measurements were performed using a Wyatt Heleos II 18 angle light scattering instrument coupled to a Wyatt Optilab rEX online refractive index detector. Detector 12 in the Heleos instrument was replaced with Wyatt's QELS detector for dynamic light scattering measurement. Samples (100 μl) were resolved on a Superdex S-200 10/300 analytical gel filtration column (GE Healthcare, Little Chalfont, UK) running at 0.5 ml/min in 25 mM bis Tris pH 7.2, 100 mM NaCl buffer before passing through the light scattering and refractive index detectors in a standard SEC-MALS format. Protein concentration was determined from the excess differential refractive index based on 0.186 RI increment for 1 g/ml protein solution. The concentration and the observed scattered intensity at each point in the chromatograms were used to calculate the absolute molecular mass from the intercept of the Debye plot using Zimm's model as implemented in Wyatt's ASTRA software. Autocorrelation analysis of data from the dynamic light scattering detector was also performed using Wyatt's ASTRA software, and the translational diffusion coefficients determined were used to calculate the hydrodynamic radius using the Stokes-Einstein equation and the measured solvent viscosity of 9.3 e-3 Poise. (B) Small-angle X-ray scattering (SAXS) experiment with approximately 20 μM D. rerio CPAP937–1124 in 25 mM bis Tris pH 7.2, 100 mM NaCl, 2 mM DTT. Shown in blue is the experimentally measured SAXS curve of CPAP937–1124 with the experimental error indicated by black bars. The orange line shows the fitted theoretical SAXS curve of CPAP937–1124 derived from its crystal structure. Fitting was done using CRYSOL (Svergun et al., 1995) and resulted in a χ-value of 1.416. A.U., arbitrary units. At higher CPAP937–1124 concentrations the fit became less good due to the tendency of CPAP937–1124 to self-associate at these concentrations as revealed by a gradual increase of the derived Rg values. SAXS data were collected at the European Synchrotron Radiation Facility (ESRF), Grenoble, France, at beamline ID14–3. Measurements were done at 10°C at a wavelength of 0.931 Å with the standard beamline settings using a PILATUS 1M detector (Dectris, Baden, Switzerland). To minimise radiation damage, a flow cell was used for the measurements. Collected data was buffer subtracted using PRIMUS (Konarev et al., 2003) and the beamstop shadow removed by cutting the data at a q-value of 0.055 nm−1. Above a q-value of 3.8 nm−1 the data became too noisy to be interpretable and the data were therefore cut at this value.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** Side-by-side comparison of the apo-structure of the D. rerio TCP-domain of CPAP (left) with the structure of an engineered peptide-assembly mimic based on Borrelia OspA (right) that is used to study β-rich self-assemblies (PDB code 2FKJ, chain A). Structures are shown as ribbon presentations and are rainbow-coloured from N- to C-terminus. Note that the conformation of the peptide-self-assembly mimic is maintained by two globular domains capping both ends of its β-sheet. In contrast, the TCP domain entirely lacks a hydrophobic core.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** The numbering refers to D. rerio CPAP. The alignment is coloured by conservation according to the Consurf conservation score from cyan (variable) to burgundy (conserved).

**Table 1.**
 Characterisation of the CPAP:STIL interaction in vitro


<table>
  <thead>
    <tr>
      <th>Danio rerio STIL peptide in syringe</th>
      <th>Danio rerio CPAP937–1124 TCP domain in cell</th>
      <th>Number of binding sites (N)</th>
      <th>SD N</th>
      <th>KD (μM)</th>
      <th>SD KD (μM)</th>
      <th>ΔH (kcal/mol)</th>
      <th>SD (kcal/mol)</th>
      <th>n (number of measurements)</th>
      <th>Factor change in KD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>STIL404–448</td>
      <td>WT</td>
      <td>1.07</td>
      <td>0.04</td>
      <td>1.9</td>
      <td>0.2</td>
      <td>−10.1</td>
      <td>0.3</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>STIL411–428</td>
      <td>WT</td>
      <td>0.98</td>
      <td>0.03</td>
      <td>4</td>
      <td>0.3</td>
      <td>−11.3</td>
      <td>0.5</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <td>STIL429–448</td>
      <td>WT</td>
      <td>0.97</td>
      <td>0.08</td>
      <td>540</td>
      <td>130</td>
      <td>−6.3</td>
      <td>0.6</td>
      <td>2</td>
      <td>∼280</td>
    </tr>
  </tbody>
</table>

_Binding parameters between D. rerio CPAP and various D. rerio STIL constructs obtained from ITC experiments. Fitting was performed with N as a variable. Constraining N to a fixed value of 1 during fitting produced KD values that were within the experimental error of those tabulated here._

### The CPAP TCP domain adopts a unique extended open β-sheet conformation that packs against a series of conserved prolines in STIL

To understand how CPAP and STIL interact at the molecular level, we obtained the crystal structures of the TCP-domain of D. rerio CPAP937–1124, both on its own and in a complex with D. rerio STIL408–428 (Figure 1B,C,E; Table 2, Table 3). In both structures, the TCP domain adopts a nearly identical conformation, suggesting that no significant conformational change occurs in CPAP upon binding to STIL (RMSD = 1.5 Å ± 0.2 Å over 148 ± 4 Cα pairs). The TCP domain folds into a single layer β-sheet comprising ∼20 consecutive antiparallel strands connected by type I β-turns and is stabilised by an extensive hydrogen-bonding network. The resulting sheet shows a twist of approximately 13° (i.e., the angle between the consecutive, hydrogen-bonded strands), slightly lower than the average value of 20° observed for typical β-sheets (Chothia, 1973; Murzin, 1992). Individual β-hairpins correspond to previously noted (Islam et al., 1993; Hung et al., 2000) repeats in the TCP domain sequence; the turns of these hairpins are often constituted by a PDG motif explaining the high frequency of proline and glycine residues in this domain (Figure 1—figure supplement 2). Crystal packing interactions involve only small protein interfaces, suggesting that the protein is biologically active as a monomer. Indeed both small-angle X-ray scattering (SAXS) and size-exclusion chromatography—multi angle light scattering (SEC-MALS) experiments demonstrate that the TCP domain is predominantly monomeric in solution (Figure 1—figure supplement 3).

The structure of the TCP domain represents an unusual, novel architecture. It is reminiscent of the β-sheet conformation proposed to exist within amyloid fibrils and resembles engineered water-soluble peptide self-assembly mimics (PSAMs) used to study β-rich self-assemblies (Makabe et al., 2006). In contrast to these PSAM structures whose conformation is maintained by two globular domains capping both ends of the β-sheet, the TCP domain stably exists on its own. (Figure 1—figure supplement 4). The TCP domain structure lacks a defined hydrophobic core typical for globular domains, and both sides of its β-sheet are exposed to the solvent and well hydrated.

The structure of the CPAP–STIL complex revealed that the STIL peptide binds in a polyproline II helical conformation along one edge of the TCP domain β-sheet. The STIL peptide binds to CPAP by four main mechanisms (Figure 1C). First, three STIL prolines (P417, P421, and P423) pack against aromatic CPAP residues (F978, Y996, and F1015) in a way that resembles target motif recognition by other described proline-rich motif (PRM) binding domains (Kay et al., 2000). Second, R418 (STIL) makes a cation-π interaction with the phenyl ring of Y994 (CPAP). Third, STIL R418 is further involved in a water-mediated hydrogen bonding network that includes CPAP residues H1003 and T1005. Finally, sidechain–mainchain interactions are formed between CPAP residues Y994, Q1019, and E1021 and the bound STIL peptide. The CPAP and STIL residues involved in this interaction are highly conserved across metazoans (Figure 1C).

Sequence conservation of the TCP domain is not confined to this section of our structure but extends further along the same edge of the sheet (Figure 1B). This additional conserved region contains aromatic residues that are arranged similar to those that pack against the proline residues of the bound STIL peptide in our crystal structure (Figure 1B,C). Intriguingly, the C-terminal part of STIL’s CR2 region (omitted to obtain diffraction grade crystals) contains two highly conserved proline residues (P435 and P438 in D. rerio) that would be well positioned to bind to these aromatic residues in an analogous way (Figure 1A,B). Thus, we speculate that the entire CR2 region of STIL spanning from residue 417 to residue 438 (D. rerio) may be bound all along the edge of the TCP domain. Although our ITC experiments suggest that these putative additional contacts are insufficient to establish strong binding between STIL and CPAP (Figure 1D) they may contribute cooperatively to the CPAP–STIL interaction once the N-terminal proline-rich region in CR2 established binding. We conclude that the TCP domain of CPAP adopts a unique extended open β-sheet conformation that recognises a series of conserved prolines in the CR2 region of STIL.

### The CPAP E1021V MCPH mutation reduces the binding affinity of the CPAP–STIL interaction

The involvement of CPAP E1021 in the interaction with STIL in zebrafish is potentially significant, as the equivalent residue in human CPAP (E1235) is mutated to valine in some MCPH patients. To test whether this mutation disrupts the organisation of the TCP domain, we obtained the crystal structure of D. rerio CPAP937–1124 carrying the E1021V mutation (Figure 1F; Table 2). The structure of the wild-type and the mutant TCP domain were virtually identical (RMSD = 0.1 Å over 142 Cα pairs) demonstrating that the TCP domain structure was not compromised. To test whether this mutation perturbed the interaction with STIL, we purified WT and various other mutant forms of D. rerio CPAP937–1124 in which we valine substituted residues that our crystal structure suggested to be important for binding (Figure 2B). Circular dichroism (CD) spectra indicated that the mutant forms of the TCP domain were correctly folded with a predominantly β-type profile (Figure 2—figure supplement 1). ITC experiments with WT D. rerio STIL404–448 showed that the mutation of residues F978, Y994, and F1015 decreased the binding strength by ∼20 to 40-fold (Figure 2A, left; Table 4), while mutation of E1021 decreased the binding strength by approximately eightfold. In contrast, mutation of T986, which is not predicted to be in the interaction interface, did not detectably perturb binding.

![Figure 2.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig2-v1.jpg)

**Figure 2.:** (A) Graphs showing the binding constants (KD) determined by ITC for the interaction between WT and mutant constructs of CPAP937–1124 and STIL404–448. Left panel, WT and various mutant forms of CPAP937–1124 binding to WT STIL404–448 (T986 is a non-interacting residue included as a negative control). Error bars, standard deviation. Right panel, WT and various mutant STIL404–448 constructs binding to WT CPAP937–1124 (N422 is a non-interacting residue included as a negative control). Error bars, standard deviation. The wild-type measurements are the same as shown in Figure 1D and are shown again for comparison to the mutants. (B and C) Close-up view of the CPAP (green):STIL (orange) interaction interface from D. rerio (B) and Drosophila (C). Interface residues are shown as sticks, in yellow is the Glutamate residue in Drosophila and D. rerio CPAP that is equivalent to E1235 in human CPAP (mutated in MCPH). Residues of the D. rerio protein mutated for ITC experiments are ringed in green (CPAP) or red (STIL). Dotted black lines indicate hydrogen-bonds. The conserved bound water molecule is shown as a red sphere.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Coomassie stained SDS-PAGE gel of purified, recombinant CPAP937–1124 and its mutants (as labelled in colours above the gel). (B) Buffer-subtracted circular dichroism (CD) spectra of D. rerio CPAP937–1124 and its mutants in 10 mM Na-Phosphate pH 7.3 at approximately 200 μg/ml. Spectra were recorded on a JASCO J-810 from 260 to 190 nm in 0.2 nm steps at 20°C and are colour-coded as in (A). The data were cut at 200 nm as the detector was saturated below this wavelength for some constructs as indicated by a high HT voltage. (C) Coomassie stained SDS-PAGE gel showing purified, recombinant D. rerio STIL404–448 and its mutants.

We also purified mutant forms of the D. rerio STIL404–448 peptide and tested their ability to interact with the WT D. rerio TCP domain in ITC experiments (Figure 2A, right, Figure 2—figure supplement 1C; Table 4). Alanine substitution of P417, R418 or P421 decreased the binding strength by ∼10 to 20-fold and alanine substitution of P423 by approximately twofold to threefold. In contrast, the mutation of residue N422, which is not predicted to be in the interaction interface, did not compromise binding. Taken together these results lend strong support to our structural model and indicate that the E1021V MCPH mutation leads to roughly an order of magnitude decrease in affinity of the CPAP–STIL interaction.

### The CPAP–STIL interaction is highly conserved

The sequence conservation of the CPAP TCP domain (Figure 1—figure supplement 5) and the CR2 region of STIL (Figure 1—figure supplement 1) suggests that this interaction may be conserved. To confirm this, we solved the crystal structure of the TCP domain from Drosophila melanogaster DSas-4 (dCPAP) (residues 700–901) in complex with the region of Ana2 (dSTIL) equivalent to CR2 (residues 1–47) (Table 2, Table 5, Table 6; Figure 2C). The dSTIL–dCPAP interaction interface in this structure was highly similar to the D. rerio complex (inter-species alignments of the structures yielded an average pairwise RMSD of 1.2 ± 0.2 Å across an average of 118 ± 4 Cα pairs). Indeed, all copies of the complex obtained in the structures from both species superimposed well and exhibited the same four major groups of binding interactions as described for the D. rerio structure. This conservation includes the contact made by the E792 residue in dCPAP (the equivalent of the E1235 residue in human CPAP that is mutated in MCPH). Together, these data allow us to determine a consensus CPAP binding motif in metazoan STIL proteins (PRxxPxP, Figure 1—figure supplement 1) and suggest that the described CPAP–STIL interaction constitutes a highly conserved step in centriole biogenesis.

### The CPAP–STIL interaction is essential for centriole assembly in vivo

Since the binding mechanism of CPAP and STIL is conserved between zebrafish and Drosophila, we turned to D. melanogaster as a model system to address the functional relevance of this interaction in vivo. In flies, the lack of dCPAP or dSTIL leads to centriole loss and a consequent severe uncoordinated (unc) phenotype due to the lack of basal bodies and so cilia in Type I sensory neurons. These flies lack all mechano- and chemo-sensation and, although viable, they usually die shortly after eclosion, as they cannot feed or move in a coordinated fashion (Kernan et al., 1994; Basto et al., 2006; Wang et al., 2011). We examined the ability of various GFP-tagged versions of dCPAP and dSTIL to rescue the centriole loss observed in these mutants and assayed their ability to localise to centrosomes in the presence of endogenous dCPAP or dSTIL (Figure 3).

![Figure 3.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig3-v1.jpg)

**Figure 3.:** (A) Schematic view of the complex between dCPAP (green) and dSTIL (magenta) with the residues mutated in MC1 (cyan), MC2 (brown) and MC3 (dark purple) indicated as coloured sticks. The MCPH residue E792 is circled in red. Note that MC1 and MC2 are mapped onto the Drosophila structure (dark-green backbone), while MC3 had to be mapped onto the backbone of the D. rerio structure (light green backbone). Although highly conserved between Drosophila and D. rerio (Figure 1—figure supplement 5) this region was not visible in the electron density map of the Drosophila structure probably due to its partial unfolding to enable packing interactions within the crystal. (B–M) Panels show representative still images taken from movies of Drosophila embryos expressing the indicated dCPAP-GFP or dSTIL-GFP constructs. Note that all analyses were performed in the presence of endogenous WT dCPAP or dSTIL, and that all images were acquired with the same microscope settings at the same stage of the cell cycle. (B–F) dSTIL-GFP constructs localise to centrosomes at similar levels. (G–M) All mutant dCPAP-GFP constructs localise to centrosomes, but at strongly reduced levels compared to wild-type dCPAP-GFP. (N) Graphs show the percentage of cells with 0, 1, 2, and 3 centrosomes in the genotypes analysed (as indicated). All dSTIL-GFP and dCPAP-GFP constructs were analysed in their respective mutant backgrounds. Note that this experiment was performed blind. (O–Q′′) Panels show third instar larval brain cells of various genotypes in metaphase. Cells were stained for the centriolar protein Asterless (Asl—green) and the PCM component Centrosomin (Cnn—red) and DNA (blue). Wild-type metaphase cells have two centrosomes (O), whereas centrosomes are mostly absent in third instar larval brain cells from dCPAP mutants (P). As an example, representative images of dCPAP mutant cells expressing the dCPAP_E792V-GFP construct are shown that were scored with 2 (Q), 1 (Q′) or no (Q′′) centrosomes. Scale bars = 3 μm.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Panels show western blots of third instar larval brain samples probed with antibodies against GFP (recognising the fusion proteins), actin (as a loading control) and dCPAP (recognising both the fusion proteins and the endogenous protein) (highlighted by an arrow). All fusion proteins were expressed in their respective mutant backgrounds, as indicated by the black lines. Left panel, the dCPAP fusion proteins were expressed at approximately equal levels (when compared to the actin control) but were all moderately overexpressed compared to the endogenous dCPAP protein. Right panel, dSTIL_WT, dSTILΔN and dSTILP11AR12A were expressed at slightly higher levels than dSTIL_P11A and dSTIL_R12A, and all GFP fusion proteins were strongly overexpressed when compared to endogenous dSTIL (data not shown).

We first expressed a version of dSTIL that lacks the first 45 aa (including the PRxxPxP motif required for the interaction with dCPAP). GFP-tagged wild-type dSTIL (dSTIL_WT-GFP) served as a control. Both proteins were expressed at similar levels and localised strongly to centrosomes in the presence of endogenous dSTIL (Figure 3B,C; Figure 3—figure supplement 1). Only the wild-type version, however, was able to rescue the unc phenotype and the centriole loss phenotype of the dSTIL mutant (Figure 3N; Table 7). To further characterise the dCPAP binding domain in vivo we mutated the first proline and arginine of the PRxxPxP motif of dSTIL to alanine, both separately and in combination (P11A, R12A, and P11A:R12A, Figure 2C). All three constructs strongly localised to centrosomes in the presence of endogenous dSTIL (Figure 3D–F, Figure 3—figure supplement 1). Both single mutants rescued the unc phenotype of the dSTIL mutation while the double mutant failed to do so (data not shown). The single mutants P11A and R12A were also able to partially rescue the centriole loss phenotype, whereas the double mutant P11A:R12A showed only a poor rescue (Figure 3N; Table 7). These data strongly suggest that the interaction with dCPAP is essential for dSTIL function in centriole assembly.

We next deleted the entire TCP-domain of dCPAP (dCPAP_ΔC), or expressed GFP fusion proteins carrying mutation clusters (MCs) altering 3–4 residues in different regions of the TCP domain (Figure 3A). Mutation clusters were designed that targeted central (dCPAP_MC1) or peripheral (dCPAP_MC2) residues in the dSTIL binding domain, as well as residues that are predicted to not significantly be involved in complex formation (dCPAP_MC3), according to the crystal structure and the ITC data (Figure 3A, Figure 2A, Figure 1D; Table 1). We also analysed dCPAP_E792V-GFP lines, which carried the MCPH equivalent mutation E792V (E1235V in humans and E1021V in zebrafish CPAP). All transgenic dCPAP-GFP proteins were expressed at approximately equivalent levels in vivo, but were moderately overexpressed compared to endogenous dCPAP (Figure 3—figure supplement 1). Wild-type dCPAP-GFP localised strongly to centrosomes and rescued both the unc phenotype and the centriole loss phenotype (Figure 3G,N; Table 7). Strikingly, the rescuing ability of the mutant constructs strongly correlated with the predicted strength of dSTIL binding. dCPAP_ΔC-GFP failed to rescue, dCPAP-MC1 and dCPAP-MC2 rescued poorly, the MCPH mutation E792V showed an intermediate phenotype, while dCPAP-MC3 exhibited a robust rescue (Figure 3N; Table 7). Interestingly, when compared to wild-type dCPAP-GFP, all mutant constructs (including dCPAP_MC3) localised only weakly to centrosomes (Figure 3H–M). Together, these data suggest that the interaction between dCPAP and dSTIL is a key step in centriole assembly and is essential for centriole duplication. Furthermore, they indicate that low total levels of dCPAP at centrosomes might be sufficient for centriole duplication, as long as some interaction with dSTIL is maintained.

### The TCP domain of C. elegans SAS-4 is required for its interaction with SAS-5 and for centriole assembly

It has been proposed that SAS-5 is the C. elegans homolog of the STIL proteins in flies and vertebrates, but there is little sequence homology between these proteins (Stevens et al., 2010a). We failed to identify an unambiguous PRxxPxP motif in worm SAS-5, so we tested whether the TCP domain of SAS-4 (the C. elegans CPAP homologue) is functionally important. We used the Mos single-copy insertion system (MosSCI; Frøkjær-Jensen et al., 2008) to generate transgenic lines with single-copy transgenes under the control of sas-6 regulatory sequences integrated at a specific site on chromosome II (Figure 4A). Transgenes were generated expressing GFP fusions with either WT SAS-4 (SAS-4WT::GFP) or a form in which the C-terminal TCP domain (aa 557–808) had been deleted (SAS-4ΔTCP::GFP); both transgenes contained a 497 bp resequenced region in their N-terminal coding region (preserving codon usage) that rendered them resistant to RNAi-mediated depletion (Figure 4A).

![Figure 4.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig4-v1.jpg)

**Figure 4.:** (A) Schematic illustration of the MosSCI system used for generating single-copy sas-4 transgene insertions. (B) A schematic illustration of the monopolar spindle assay for centriole duplication in C. elegans embryos. Panels show maximum intensity projections of representative fluorescence confocal z-series taken of sas-4(RNAi) embryos expressing either WT or ΔTCP SAS-4::GFP. Transgenic SAS-4WT::GFP localises to sharp foci representing the centrioles, whereas SAS-4ΔTCP::GFP localises diffusely to the pericentriolar material. Bar, 10 μM. (C) Graphs show the quantification of second division monopolar spindles (left) and embryonic viability (right) after sas-4(RNAi) and rescue with either a WT or ΔTCP sas-4::gfp transgene. (D) Panels show autoradiographs (top panel) and a Coomassie stained gel from a Ni-NTA pull-down experiment with 35S-labelled in vitro translated SAS-4 fragments (prey) and SAS-5-6xHis fragments (baits).

SAS-4 depletion by RNAi prevents centriole assembly, resulting in a signature phenotype characterised by a normal first mitotic division followed by monopolar spindles during the second division (Figure 4B,C; O’Connell et al., 2001). This phenotype arises because the sperm that fertilise the SAS-4-depleted oocytes carry two normal centrioles, since sperm are produced prior to introduction of the dsRNA. The two sperm-derived centrioles organise two centrosomes, and the first mitotic division appears normal. If no new centrioles form, each daughter cell inherits a single sperm-derived centriole leading to monopolar spindles in the second division and 100% embryonic lethality (Figure 4C). Both the monopolar spindle phenotype and embryonic viability were fully rescued by the WT sas-4::gfp transgene (aa 1–808), but not by the ΔTCP transgene (aa 1–556) (Figure 4B,C). While SAS-4WT::GFP targeted to centrioles in the absence of the endogenous protein, SAS-4ΔTCP::GFP did not, and instead exhibited a diffuse accumulation in the pericentriolar material (Figure 4B). Thus, the SAS-4 TCP domain is required for SAS-4 to accumulate at centrioles and become incorporated into the microtubule-containing outer centriole wall.

To determine if the failure of SAS-4ΔTCP::GFP to become incorporated in the centriole outer wall could be due to an inability to interact with SAS-5, we performed a pull-down assay to determine whether 35S-labelled in vitro translated SAS-4 fragments could interact with the N-terminal or C-terminal regions of SAS-5 bound to beads (Figure 4D). In vitro translated full-length SAS-4 interacted specifically with the N-terminal domain (aa 1–202) of SAS-5. Interestingly, we could not further narrow down the region of SAS-4 required for this interaction. Neither the SAS-4 N-terminal nor C-terminal region (which includes the TCP domain) alone could be pulled down by SAS-5. This result suggests that although the TCP domain is required for SAS-4 to interact with SAS-5, it is not sufficient. Together, these data suggest that a TCP domain-dependent interaction between SAS-4/CPAP and SAS-5/STIL is conserved and essential for centriole duplication in C. elegans, but that the precise interaction interface may have diverged.

## Discussion

Only a small set of conserved centriolar proteins is essential for centriole assembly (Brito et al., 2012; Gonczy, 2012) and some of these proteins, like CPAP and STIL, have been linked to microcephaly in humans (Leal et al., 2003; Bond et al., 2005; Gul et al., 2006; Thornton and Woods, 2009; Darvish et al., 2010). However, there is currently little structural understanding on how these proteins interact with one another, how mutations in them cause microcephaly in humans and how these interactions are regulated.

Here we have solved the crystal structures of the CPAP–STIL complex from zebrafish and Drosophila. We showed that the CPAP TCP domain folds into an elongated open-sided β-meander that consists of ∼20 consecutive antiparallel β-strands connected by type I β-turns. β-meanders are frequently found in β-barrels, β-propellers and some α+β proteins. However, what, to our knowledge, makes the TCP domain structure unique amongst naturally occurring proteins is that it solely consists of a freestanding meander β-sheet that entirely lacks a defined hydrophobic core and is not flanked by other globular domains that pack against it. We show that the TCP domain is predominantly monomeric in solution and self-interacts in its crystallised form only through small interfaces that are not conserved. Thus, despite some reminiscence to β-sheets observed in amyloid fibrils it is unlikely that the TCP domain self-associates in a similar manner.

Instead, we demonstrate that the TCP domain of CPAP constitutes a novel proline-rich-motif (PRM) recognition-domain that specifically binds to a short target motif in STIL. Although the overall sequence identity of the CPAP and STIL proteins between Drosophila and zebrafish is relatively low (∼22% and ∼13%, respectively), our structural analysis revealed that the interaction interface is conserved, confirming the previous proposal that fly Ana2 is the functional homologue of vertebrate STIL (Stevens et al., 2010a). Our characterisation of the binding interface also allowed us to define a consensus-binding site (PRxxPxP) for the CPAP TCP domain in STIL that is conserved across metazoa. Our mutational analysis of the interface demonstrates a remarkable correlation between the ability of mutant proteins to bind to one another in vitro and their ability to support centriole assembly in vivo, providing compelling support for our structural model of the metazoan CPAP–STIL complex. These data strongly suggest that the interaction between CPAP and STIL is a conserved, essential step in centriole biogenesis. A schematic model that places this interaction in the context of a possible centriole assembly pathway is shown in Figure 5.

![Figure 5.](https://cdn.elifesciences.org/articles/01071/elife-01071-fig5-v1.jpg)

**Figure 5.:** In this illustration, interactions whose crystal structure have been determined are highlighted by green boxes—all other interactions are inferred from biochemical and genetic studies and so are depicted in cartoon form. The cartwheel central hub comprises SAS-6 (red) (Nakazawa et al., 2007; Kitagawa et al., 2011b; van Breugel et al., 2011). The spokes extending outward from the hub consist of a homodimeric SAS-6 coiled-coil, which extends (van Breugel et al., 2011) into a region known as the ‘pinhead’ (cyan in low magnification view, left), where CEP135 (grey) may act as a linker between SAS-6, CPAP and microtubules (Hiraki et al., 2007; Roque et al., 2012; Lin et al., 2013). CPAP (dark blue) localises more towards the periphery of the centriole (Mennella et al., 2012; Sonnen et al., 2012; Lukinavičius et al., 2013), where its N-terminal part may interact directly with both Asterless/CEP152 (Cizmecioglu et al., 2010; Dzhindzhev et al., 2010) (orange arrow) and microtubules (Hsu et al., 2008) (green arrow). In contrast STIL (yellow) localises more towards the interior of centrioles (Arquint et al., 2012), and appears to function upstream of CPAP in centriole biogenesis (Tang et al., 2011; Vulprecht et al., 2012). Thus, we propose that the C-terminal TCP domain of CPAP interacts with the conserved region 2 (CR2) of STIL towards the interior of the centriole and that this interaction is crucial for CPAP/STIL function at centrioles. The orientation of STIL in centrioles is unknown.

The high degree of sequence divergence between vertebrate STIL, Drosophila Ana2 and C. elegans SAS-5 suggests that STIL homologs are under particularly strong lineage-specific selection. Despite the many sequence changes between Drosophila Ana2 and vertebrate STIL, our work suggests that the interaction interface between Ana2/STIL and dSAS-4/CPAP TCP domain has been retained, highlighting its importance. Even in C. elegans, which is the most divergent of the functionally characterised STIL homologs, our work indicates that the SAS-4 TCP domain is essential for centriole assembly, and that a TCP-domain dependent interaction between SAS-4 and SAS-5 has been conserved. Nevertheless, as the SAS-4 TCP domain is not sufficient for interaction with SAS-5 and we were unable to identify a PRxxPxP interaction motif in worm SAS-5, more work will be needed to understand the SAS-4—SAS-5 interaction in C. elegans and its relationship to the CPAP–STIL interaction in other metazoans.

A surprising aspect of our findings is that the E792V (MCPH) mutant and all three of the mutation clusters (MCs) that we analysed in dCPAP localise poorly to centrosomes. For the E792, MC1, and MC2 mutations this could be expected, as these are all predicted to perturb the interaction between dCPAP and dSTIL (as is the case with similar mutations in zebrafish CPAP in our in vitro binding assays), and this would be predicted to perturb the recruitment of dCPAP to centrioles. The MC3 cluster, however, is not predicted to lie in a strong interaction interface and, unlike the MC1 and MC2 mutation clusters, it can rescue the centriole duplication defect in dCPAP mutant cells nearly as efficiently as the WT protein. Possibly, an interaction with another protein that plays some part in recruiting dCPAP to centrioles might be perturbed by these mutations. Alternatively, similar to the situation with C. elegans SAS-4 (Dammermann et al., 2008), dCPAP may localise to both centrioles and the PCM. It might therefore be PCM and not centriole recruitment that is affected by the mutation clusters. If this were the case it would be hard to discern an additional partial loss of centriole recruitment, as this loss would be masked by the PCM pool of dCPAP, especially under conditions of moderate overexpression of dCPAP. Importantly, however, our findings demonstrate that even very reduced amounts of centrosomal dCPAP can support robust centriole duplication as long as this protein can interact efficiently with dSTIL.

Our studies provide the first structural insight into the nature of the link between centrioles and human microcephaly. It is unclear why mutations in genes encoding key centriole or centrosome proteins can lead to such a specific neuro-developmental disorder in humans. It is widely assumed that some aspect of centriole/centrosome function must be particularly important in human neural progenitor cells, and that the failure of these cells to proliferate in an appropriate manner underlies the small brain size in affected individuals (Megraw et al., 2011). One possibility, based on the fact that these neural progenitors seem to divide asymmetrically (Siller and Doe, 2009; Megraw et al., 2011), is that centrioles/centrosomes may play a particularly important role in properly orienting the spindle during asymmetric divisions, and division orientation could in turn be required for the maintenance of neuronal progenitors. This appears to be the case in flies, where mutations in dCPAP/DSas-4 and dSTIL/Ana2 lead to defects in the asymmetric division of the neural stem/progenitor cells (Basto et al., 2006; Wang et al., 2011). However, there are other possible explanations. Human neural progenitor cells form primary cilia, for example, and signalling through the cilium could be perturbed if centriole assembly is perturbed (Han and Alvarez-Buylla, 2010; Megraw et al., 2011). Moreover, several studies have linked centriole and centrosome malfunction to defects in DNA damage repair (DDR) pathways (Megraw et al., 2011), and mutations in MCPH genes can also lead to more severe phenotypes in humans that may be related to DDR pathway malfunction (Al-Dosari et al., 2010; Kalay et al., 2011; Megraw et al., 2011).

A previous analysis of the behaviour of various CPAP mutant proteins (modelled on MCPH mutations) in human cells revealed some surprising findings (Kitagawa et al., 2011a). The deletion of the TCP domain or the mutation of E1235 to Valine did not effect the localisation of CPAP to the centriole, although centriole duplication was compromised by both mutations. Moreover, overexpression of the E1235V mutant protein was able to promote centriole overgrowth to a greater extent than the WT protein, suggesting that it may have acquired some enhanced functionality. The structures we report here reveal that E1235 is one of the several residues involved in the binding interface with STIL, making an important sidechain–mainchain contact. This structural model explains how the E1235V mutation can compromise complex formation, and we have confirmed that this is the case with zebrafish proteins in vitro. Moreover, the equivalent mutation in flies leads to inefficient centriole assembly, but this process is not abolished. Taken together, our data strongly suggest that it is a partial failure in centriole assembly that is the primary cause of microcephaly in these patients. The challenge now is to understand how inefficient centriole assembly leads to microcephaly in humans.

## Materials and methods

### Recombinant protein expression and purification

D. rerio CPAP937–1124 was cloned from D. rerio cDNA. Proteins were expressed in Escherichia coli BL21 (DE3) Rosetta as N-terminally His-tagged constructs, and purified via immobilised metal ion affinity chromatography (NiNTA; Qiagen, Hilden, Germany), proteolytic tag cleavage, followed (optionally) by size-exclusion chromatography and ion-exchange chromatography using standard methods. The selenomethionine derivative protein was expressed in selenomethionine supplemented M9 medium and purified in the same way. Purified constructs contained the sequence GPHM at the N-termini that stem from the cloning and protease cleavage sites.

D. rerio STIL404–448 was cloned from IMAGE clone 7147918 and expressed in E. coli C41 BL21 (DE3), fused to two His-tagged lipoyl domains from Bacillus stearothermophilus dihydrolipoamide acetyltransferase at both the N- and C terminus. The peptide was purified via NiNTA chromatography, proteolytic cleavage of the His-lipoyl domains, and ion-exchange chromatography. The purified constructs contained a G (GG for D. rerio STIL404–448 and its point-mutants) at their N-terminus and the sequence EFGENLYFQ (ENLYFQ for D. rerio STIL408–428 and D. rerio STIL411–428) at their C-terminus. These extra sequences stem from the cloning and protease cleavage sites.

Mutations of the D. rerio constructs were introduced into the expression vectors by site-directed mutagenesis.

Codon-optimised (GeneArt, Carlsbad, CA) Drosophila dSTIL1–47 was genetically fused to the N-terminus of Drosophila dCPAP700–901 via 3-way ligation. The fusion protein was expressed in E. coli B834 (DE3) as an N-terminally His-tagged fusion, and purified via NiNTA chromatography, proteolytic tag cleavage and size exclusion chromatography. The selenomethionine derivative protein was expressed using SelenoMethionine Medium (Molecular Dimensions, Newmarket, UK) and purified in the same way.

**Table 2.**
 Native dataset analysis and refinement statistics


<table>
  <thead>
    <tr>
      <th></th>
      <th>D. rerio CPAP937–1124 WT</th>
      <th>D. rerio CPAP937–1124 E1021V</th>
      <th>D. rerio CPAP937–1124 + D. rerio STIL408–428 complex</th>
      <th>D. melanogaster dSTIL1–47 − dCPAP700–901 fusion complex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Beamline</td>
      <td>Diamond I02</td>
      <td>MRC-LMB Cambridge UK</td>
      <td>Diamond I04</td>
      <td>Diamond I04</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P21</td>
      <td>P21</td>
      <td>P21</td>
      <td>P1</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.9786</td>
      <td>1.5418</td>
      <td>0.9795</td>
      <td>0.9795</td>
    </tr>
    <tr>
      <td>Monomers in the asymmetric unit</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Unit cell dimensions (Å)</td>
      <td>a = 52.34; b = 36.44; c = 56.44; α = 90.00; β = 117.31; γ = 90.00</td>
      <td>a = 52.12; b = 36.48; c = 56.46; α = 90.00; β = 117.47; γ = 90.00</td>
      <td>a = 60.25; b = 67.47; c = 61.65; α = 90.00; β = 113.92; γ = 90</td>
      <td>a = 58.64; b = 69.91; c = 69.98; α = 86.96; β = 88.64; γ = 67.69</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>29.48–1.7</td>
      <td>36.48–1.9</td>
      <td>56.35–2.7/2.2 (anisotropy)</td>
      <td>64.60–2.57</td>
    </tr>
    <tr>
      <td>Completeness(overall/inner/outer shell)</td>
      <td>99.7/99.4/100</td>
      <td>100/99.6/100</td>
      <td>99.9/99.5/99.9</td>
      <td>97.6/93.6/97.2</td>
    </tr>
    <tr>
      <td>Rmerge (overall/inner/outer shell)</td>
      <td>0.074/0.030/0.929</td>
      <td>0.096/0.028/1.093</td>
      <td>0.101/0.053/1.008</td>
      <td>0.091/0.069/0.512</td>
    </tr>
    <tr>
      <td>Rpim (overall/inner/outer shell)</td>
      <td>0.029/0.012/0.369</td>
      <td>0.039/0.012/0.456</td>
      <td>0.050/0.027/0.505</td>
      <td>0.061/0.035/0.449</td>
    </tr>
    <tr>
      <td>Mean I/σI (overall/inner/outer shell)</td>
      <td>14.6/39.9/2.0</td>
      <td>13.8/43.4/1.8</td>
      <td>7.6/19.0/1.4</td>
      <td>7.6/16.3/1.7</td>
    </tr>
    <tr>
      <td>Multiplicity (overall/inner/outer shell)</td>
      <td>7.2/7.0/7.3</td>
      <td>6.8/6.6/6.6</td>
      <td>4.8/4.7/4.9</td>
      <td>3.1/2.9/3.1</td>
    </tr>
    <tr>
      <td>Number of reflections</td>
      <td>19,941</td>
      <td>14,349</td>
      <td>21,892</td>
      <td>31,911</td>
    </tr>
    <tr>
      <td>Number of atoms</td>
      <td>1595</td>
      <td>1515</td>
      <td>3176</td>
      <td>3924</td>
    </tr>
    <tr>
      <td>Waters</td>
      <td>190</td>
      <td>114</td>
      <td>54</td>
      <td>65</td>
    </tr>
    <tr>
      <td>Rwork/Rfree (% data used)</td>
      <td>19.9/24.4 (5.1%)</td>
      <td>20.9/26.7 (5.0%)</td>
      <td>23.4/27.7 (5.0%)</td>
      <td>24.5/26.3 (5.05%)</td>
    </tr>
    <tr>
      <td>rmsd from ideal values: bond length/angles</td>
      <td>0.011/1.478</td>
      <td>0.009/1.310</td>
      <td>0.015/1.619</td>
      <td>0.007/0.900</td>
    </tr>
    <tr>
      <td>Mean B value</td>
      <td>26.52</td>
      <td>31.553</td>
      <td>59.69</td>
      <td>70.80</td>
    </tr>
    <tr>
      <td>Correlation coefficient Fo-Fc/Fo-Fc free</td>
      <td>0.961/0.942</td>
      <td>0.955/0.926</td>
      <td>0.954/0.933</td>
      <td>0.854/0.836</td>
    </tr>
    <tr>
      <td>Molprobity Score</td>
      <td>0.97 (100th percentile)</td>
      <td>1.2 (99th percentile)</td>
      <td>1.70 (96th percentile)</td>
      <td>1.40 (100th percentile)</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 SeMet D. rerio CPAP937–1124 dataset analysis and phasing statistics


<table>
  <tbody>
    <tr>
      <td>Beamline</td>
      <td colspan="3">ESRF ID 23–1</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td colspan="3">P21</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.9791 (Peak)</td>
      <td>0.9794 (Inflection)</td>
      <td>0.9393 (Remote)</td>
    </tr>
    <tr>
      <td>Unit cell dimensions (Å)</td>
      <td>a = 52.39 b = 36.53 c = 56.34 α = 90.00 β = 117.28 γ = 90.00</td>
      <td>a = 52.59 b = 36.60 c = 56.48 α = 90.00 β = 117.24 γ = 90.00</td>
      <td>a = 52.49 b = 36.55 c = 56.38 α = 90.00 β = 117.26 γ = 90.00</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>36.56–1.7</td>
      <td>36.56–1.7</td>
      <td>36.56–1.7</td>
    </tr>
    <tr>
      <td>Completeness (overall/inner/outer shell)</td>
      <td>100.0/99.7/100.0</td>
      <td>100/99.2/100</td>
      <td>100/99.7/100</td>
    </tr>
    <tr>
      <td>Rmerge (overall/inner/outer shell)</td>
      <td>0.09/0.048/1.296</td>
      <td>0.127/0.047/2.840</td>
      <td>0.092/0.046/1.370</td>
    </tr>
    <tr>
      <td>Rpim (overall/inner/outer shell)</td>
      <td>0.042/0.031/0.552</td>
      <td>0.056/0.028/1.201</td>
      <td>0.041/0.026/0.580</td>
    </tr>
    <tr>
      <td>Mean I/sd(I) (overall/inner/outer shell)</td>
      <td>10.7/26.0/1.5</td>
      <td>8.9/26.4/0.7</td>
      <td>10.8/27.4/1.4</td>
    </tr>
    <tr>
      <td>Multiplicity (overall/inner/outer shell)</td>
      <td>7.2/7.0/7.3</td>
      <td>7.2/6.9/7.3</td>
      <td>7.2/7.0/7.3</td>
    </tr>
    <tr>
      <td>Se sites found/expected</td>
      <td colspan="3">5/7</td>
    </tr>
    <tr>
      <td>Overall FOM</td>
      <td colspan="3">0.306</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Characterisation of the CPAP:STIL interaction in vitro


<table>
  <thead>
    <tr>
      <th>Danio rerio STIL404–448 peptide in syringe</th>
      <th>Danio rerio CPAP937–1124 TCP domain in cell</th>
      <th>Number of binding sites (N)</th>
      <th>SD N</th>
      <th>KD (μM)</th>
      <th>SD KD (μM)</th>
      <th>ΔH (kcal/mol)</th>
      <th>SD (kcal/mol)</th>
      <th>n (number of measurements)</th>
      <th>Factor change in KD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WT</td>
      <td>WT</td>
      <td>1.07</td>
      <td>0.04</td>
      <td>1.9</td>
      <td>0.2</td>
      <td>−10.1</td>
      <td>0.3</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>F978V</td>
      <td>0.70</td>
      <td>0.09</td>
      <td>37</td>
      <td>10</td>
      <td>−23</td>
      <td>5</td>
      <td>4</td>
      <td>20</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>T986V</td>
      <td>1.01</td>
      <td>0.07</td>
      <td>1.9</td>
      <td>0.2</td>
      <td>−10.6</td>
      <td>0.4</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>Y994V</td>
      <td>1.00</td>
      <td>0.33</td>
      <td>68</td>
      <td>14</td>
      <td>−9.5</td>
      <td>3.8</td>
      <td>5</td>
      <td>36</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>F1015V</td>
      <td>0.93</td>
      <td>0.13</td>
      <td>70</td>
      <td>18</td>
      <td>−10.4</td>
      <td>2.7</td>
      <td>3</td>
      <td>37</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>E1021V</td>
      <td>0.91</td>
      <td>0.13</td>
      <td>16</td>
      <td>2</td>
      <td>−8.1</td>
      <td>0.6</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>WT</td>
      <td>1.07</td>
      <td>0.04</td>
      <td>1.9</td>
      <td>0.2</td>
      <td>−10.1</td>
      <td>0.3</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>P417A</td>
      <td>WT</td>
      <td>1.06</td>
      <td>0.02</td>
      <td>37</td>
      <td>1.3</td>
      <td>−11.5</td>
      <td>0.2</td>
      <td>3</td>
      <td>20</td>
    </tr>
    <tr>
      <td>R418A</td>
      <td>WT</td>
      <td>1.12</td>
      <td>0.02</td>
      <td>19</td>
      <td>1</td>
      <td>−8.8</td>
      <td>0.1</td>
      <td>4</td>
      <td>10</td>
    </tr>
    <tr>
      <td>P421A</td>
      <td>WT</td>
      <td>1.16</td>
      <td>0.03</td>
      <td>17</td>
      <td>0.3</td>
      <td>−9.8</td>
      <td>0.2</td>
      <td>4</td>
      <td>9</td>
    </tr>
    <tr>
      <td>N422A</td>
      <td>WT</td>
      <td>1.09</td>
      <td>0.03</td>
      <td>0.7</td>
      <td>0.05</td>
      <td>−12.3</td>
      <td>0.3</td>
      <td>4</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>P423A</td>
      <td>WT</td>
      <td>1.16</td>
      <td>0.05</td>
      <td>4.6</td>
      <td>0.3</td>
      <td>−10.9</td>
      <td>0.4</td>
      <td>4</td>
      <td>2.4</td>
    </tr>
  </tbody>
</table>

_Tables show the binding parameters between various D. rerio CPAP and STIL constructs obtained from ITC experiments. The measurements of the WT STIL404–448—WT CPAP937–1124 interaction are identical to each other and identical to those shown in Table 1 and are only presented again to allow easier comparison within each table. Fitting was performed with N as a variable. Constraining N to a fixed value of 1 during fitting produced KD values that were within the experimental error of those tabulated here. In control measurements on wild-type material and a selection of mutants of both CPAP and STIL, the experimental configuration was reversed with CPAP protein titrated into STIL peptide in the ITC cell. These experiments gave similar values for N, KD and ΔH to the standard configuration reported here._

**Table 5.**
 D. melanogaster dSTIL1–47-dCPAP700–901 crystallisation conditions


<table>
  <thead>
    <tr>
      <th>Crystal</th>
      <th>Protein concentration (mg/ml)</th>
      <th>Mother liquor</th>
      <th>µl protein:µl Mother liquor</th>
      <th>µl seed stock</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Native</td>
      <td>6.18</td>
      <td>100 mM MES/imidazole mix pH 6.5, 30 mM MgCl2, 30 mM CaCl2, 20% ethylene glycol, 10% PEG 8000</td>
      <td>0.15:0.05</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Semet1</td>
      <td>5.00</td>
      <td>100 mM MES/imidazole mix pH 6.5, 20% ethylene glycol, 10% PEG8000, 0.2 M racemic glutamic acid, 0.2 M glycine, 0.2 M racemic serine, 0.2 M racemic alanine, 0.2 M racemic lysine HCl</td>
      <td>0.1:0.1</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Semet2</td>
      <td>5.29</td>
      <td>100 mM MES/imidazole mix pH 6.5, 14% ethylene glycol, 7% PEG8000, 30 mM NaNO3, 30 mM NaPO4, 30 mM NH4SO4</td>
      <td>0.3:0.1</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>Semet3</td>
      <td>5.29</td>
      <td>100 mM MES/imidazole mix pH 6.5, 14% ethylene glycol, 7% PEG8000, 30 mM NaNO3, 30 mM NaPO4, 30 mM NH4SO4</td>
      <td>0.3:0.1</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>Semet4</td>
      <td>5.29</td>
      <td>100 mM MES/imidazole mix pH 6.5, 16% ethylene glycol, 8% PEG8000, 30 mM NaNO3, 30 mM NaPO4, 30 mM NH4SO4</td>
      <td>0.3:0.1</td>
      <td>0.05</td>
    </tr>
  </tbody>
</table>

**Table 6.**
 D. melanogaster dSTIL1–47-dCPAP700–901 SeMet dataset analysis


<table>
  <thead>
    <tr>
      <th></th>
      <th>Semet1-PEAK</th>
      <th>SEMET1-LREM</th>
      <th>Semet2-Peak</th>
      <th>Semet3-PEAK</th>
      <th>Semet3-INFL</th>
      <th>Semet4-Peak</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Beamline</td>
      <td>Diamond IO4</td>
      <td>Diamond IO4</td>
      <td>Diamond IO3</td>
      <td>Diamond IO3</td>
      <td>Diamond IO3</td>
      <td>Diamond IO3</td>
    </tr>
    <tr>
      <td>Spacegroup</td>
      <td>P1</td>
      <td>P1</td>
      <td>P1</td>
      <td>P1</td>
      <td>P1</td>
      <td>P1</td>
    </tr>
    <tr>
      <td>Wavelength</td>
      <td>0.9795</td>
      <td>0.9999</td>
      <td>0.9792</td>
      <td>0.9791</td>
      <td>0.9794</td>
      <td>0.9791</td>
    </tr>
    <tr>
      <td>Unit cell dimensions (Å)</td>
      <td>a = 59.31 b = 70.02 c = 70.01 α = 87.65 β = 89.24 γ = 67.37</td>
      <td>a = 59.14 b = 70.24 c = 70.13 α = 87.62 β = 89.12 γ = 67.35</td>
      <td>a = 58.47 b = 70.15 c = 69.99 α = 87.08 β = 88.41 γ = 67.60</td>
      <td>a = 58.56 b = 70.03 c = 70.14 α = 86.93 β = 88.39 γ = 68.09</td>
      <td>a = 58.72 b = 70.06 c = 70.28 α = 86.84 β = 88.47 γ = 68.36</td>
      <td>a = 59.01 b = 70.17 c = 70.15 α = 87.16 β = 88.64 γ = 67.58</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>54.74–3.50</td>
      <td>64.77–3.50</td>
      <td>64.80–3.44</td>
      <td>70.04–3.50</td>
      <td>70.17–4.60</td>
      <td>64.80–3.36</td>
    </tr>
    <tr>
      <td>Completeness (overall/inner/outer)</td>
      <td>98.1/93.8/98.3</td>
      <td>98.4/98.0/98.2</td>
      <td>97.8/91.6/93.7</td>
      <td>98.3/95.3/97.6</td>
      <td>97.8/79.1/89.9</td>
      <td>97.6/91.0/97.4</td>
    </tr>
    <tr>
      <td>Rmerge (overall/inner/outer)</td>
      <td>0.093/0.055/0.118</td>
      <td>0.086/0.041/0.238</td>
      <td>0.17/0.076/0.518</td>
      <td>0.152/0.086/0.336</td>
      <td>0.116/0.039/0.189</td>
      <td>0.125/0.037/0.433</td>
    </tr>
    <tr>
      <td>Rpim (overall/inner/outer)</td>
      <td>0.071/0.047/0.136</td>
      <td>0.062/0.029/0.172</td>
      <td>0.078/0.040/0.229</td>
      <td>0.075/0.043/0.184</td>
      <td>0.087/0.034/0.141</td>
      <td>0.100/0.038/0.323</td>
    </tr>
    <tr>
      <td>I/σI (overall/inner/outer)</td>
      <td>9.1/16.9/5.6</td>
      <td>10.9/24.7/4.9</td>
      <td>7.3/18.8/3.5</td>
      <td>9.1/27.2/3.6</td>
      <td>6.0/20.8/4.6</td>
      <td>6.9/22.5/2.7</td>
    </tr>
    <tr>
      <td>Multiplicity (overall/inner/outer)</td>
      <td>3.9/3.8/3.9</td>
      <td>3.9/3.8/3.8</td>
      <td>7.0/7.0/7.1</td>
      <td>6.0/6.7/5.3</td>
      <td>3.5/3.6/3.5</td>
      <td>3.5/3.4/3.6</td>
    </tr>
    <tr>
      <td>No. unique reflections</td>
      <td>12,832</td>
      <td>12,884</td>
      <td>13,315</td>
      <td>12,797</td>
      <td>5641</td>
      <td>14,461</td>
    </tr>
  </tbody>
</table>

**Table 7.**
 Quantification of centriole/centrosome numbers in dCPAP or dSTIL mutant larval brain cells expressing the indicated WT or mutant constructs


<table>
  <thead>
    <tr>
      <th rowspan="2">Genotype</th>
      <th rowspan="2">Number of brains</th>
      <th rowspan="2">Total number of cells</th>
      <th colspan="4">Cells with centrosome number (%)</th>
    </tr>
    <tr>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WT</td>
      <td>12</td>
      <td>944</td>
      <td>2.1</td>
      <td>2.6</td>
      <td>95.2</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>dCPAP</td>
      <td>8</td>
      <td>661</td>
      <td>95.2</td>
      <td>4.2</td>
      <td>0.6</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>dCPAP_WT-GFP</td>
      <td>9</td>
      <td>715</td>
      <td>2.8</td>
      <td>6.3</td>
      <td>90.5</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>dCPAP_ΔC-GFP</td>
      <td>13</td>
      <td>1147</td>
      <td>95.1</td>
      <td>3.8</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>dCPAP_MC1-GFP</td>
      <td>11</td>
      <td>968</td>
      <td>64.9</td>
      <td>30.1</td>
      <td>4.8</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>dCPAP_MC2-GFP</td>
      <td>17</td>
      <td>1053</td>
      <td>43.5</td>
      <td>42.2</td>
      <td>14.1</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>dCPAP_MC3-GFP</td>
      <td>16</td>
      <td>1870</td>
      <td>4.5</td>
      <td>13.3</td>
      <td>81.9</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>dCPAP_MC1-3-GFP</td>
      <td>11</td>
      <td>888</td>
      <td>90.1</td>
      <td>8.0</td>
      <td>1.8</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>dCPAP_E792V-GFP</td>
      <td>9</td>
      <td>1015</td>
      <td>13.7</td>
      <td>31.1</td>
      <td>54.8</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>dSTIL169</td>
      <td>9</td>
      <td>846</td>
      <td>98.1</td>
      <td>1.9</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>dSTIL719</td>
      <td>9</td>
      <td>980</td>
      <td>99.2</td>
      <td>0.8</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>dSTIL_WT-GFP</td>
      <td>6</td>
      <td>424</td>
      <td>5.7</td>
      <td>9.0</td>
      <td>85.1</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>dSTIL_ΔN-GFP</td>
      <td>13</td>
      <td>884</td>
      <td>88.1</td>
      <td>9.8</td>
      <td>1.9</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>dSTIL_P11A-GFP</td>
      <td>9</td>
      <td>1008</td>
      <td>11.0</td>
      <td>41.0</td>
      <td>48.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>dSTIL_R12A-GFP</td>
      <td>9</td>
      <td>709</td>
      <td>7.0</td>
      <td>31.0</td>
      <td>62.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>dSTIL_P11AR12A-GFP</td>
      <td>9</td>
      <td>727</td>
      <td>41.0</td>
      <td>43.0</td>
      <td>16.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

### Crystallisation

Native D. rerio CPAP937–1124 was crystallised in sitting drops in 80 mM Tris pH 8.5, 160 mM MgCl2, 20% PEG-4000, 18% Glycerol, 1 mM DTT at 19.5°C. The drops were set up using 1 μl of the protein solution and 0.5 μl of the reservoir solution. Crystals were mounted after 3 days and flash-frozen in liquid nitrogen.

D. rerio CPAP937–1124 E1021V was crystallised in sitting drops in 80 mM Tris pH 8.5, 160 mM MgCl2, 24% PEG-4000, 20% glycerol at 19.5°C. Crystals were mounted after 3 days and flash-frozen in liquid nitrogen.

SeMet D. rerio CPAP937–1124 crystals were obtained using the sitting drop method with a reservoir solution of 80 mM Tris pH 8.5, 160 mM MgCl2, 26% PEG-4000, 18% glycerol, 1 mM DTT at 19.5°C. Drops were set up using 1 μl protein solution and 1 μl of reservoir solution. Native CPAP937–1124 crystals were used for streak-seeding into these drops and crystals allowed to grow for 7 days before mounting and flash-freezing them in liquid nitrogen.

Crystals of the complex of D. rerio CPAP937–1124 and D. rerio STIL408–428 were initially obtained using the LMB screening set-up with the Clear Strategy 2 pH 8.5 screen (MDL, Newmarket, UK). Crystals were used to streak seed into sitting drops consisting of 1 μl of a reservoir solution of 100 mM Tris pH 8.5, 200 mM CaAcetate, 17% PEG-2000 MME and 1 μl of protein/peptide mixture (0.25 μl protein + 0.75 μl peptide) at 19.5°C. Crystals were grown for 2 days before mounting them in 100 mM Tris pH 8.5, 200 mM CaAcetate, 17% PEG-2000 MME, 25% glycerol and flash-freezing them in liquid nitrogen.

The protein concentrations of D. rerio CPAP937–1124 used for crystallisations were measured by the Bradford assay with BSA as a standard and were 39.9 mg/ml (apo-CPAP937–1124), 46.2 mg/ml (CPAP937–1124 E1021V), 30.6 mg/ml (SeMet CPAP937–1124) and 81 mg/ml CPAP937–1124 (3.7 mM, CPAP/STIL complex). The concentration of STIL408–428 (CPAP/STIL complex) was determined by amino acid analysis and was 11.8 mg/ml (3.8 mM).

Native D. melanogaster dSTIL1–47-dCPAP700–901 was crystallised using the sitting drop approach, using the Morpheus screen (Molecular Dimensions). Crystals grew after approximately 3 weeks (Table 5, ‘Native’). Crystals were mounted after approximately 4 weeks. SeMet D. melanogaster dSTIL1–47-dCPAP700–901 was initially crystallised using the Morpheus screen (Molecular Dimensions). Crystals typically grew after 3–4 weeks. Some crystals were used for microseeding of further screens including an optimisation screen. Seed stock was generated using a Seed bead kit (Hampton, Aliso Viejo, CA). Details of crystallisation conditions are shown in Table 5.

### Data collection and processing

Native data were collected as described in Table 2. All D. rerio datasets were integrated and scaled using MOSFLM (Leslie and Powell, 2007) and Scala (Evans, 2006) respectively. The D. rerio CPAP937–1124 structure was solved by MAD in CRANK (Ness et al., 2004; Cowtan, 2006), resulting in clear electron density into which an initial model was built using ArpWarp (Langer et al., 2008). Phenix.refine (Afonine et al., 2005) and REFMAC (Murshudov et al., 2011) were used to refine the model against the native dataset with manual building done in Coot (Emsley and Cowtan, 2004). D. rerio CPAP937–1124 E1021V was solved by molecular replacement in Phaser (McCoy et al., 2007) using a poly-alanine model derived from the WT model. The model was further built and refined as described for the WT structure. The complex of D. rerio CPAP937–1124 and D. rerio STIL408–428 was solved by molecular replacement using Phaser (McCoy et al., 2007) with a distorted model of the D. rerio CPAP937–1124 WT apo-structure. Refinement yielded clear density for the residues of STIL shown here. The model was further built and refined as described for the other D. rerio structures.

D. melanogaster dSTIL1–47-dCPAP700–901 data was scaled using Xia2 (Winter, 2010). Phasing was carried out using all SeMet datasets (Table 6) in autoSHARP (Vonrhein et al., 2007), using SHELXC/D (Sheldrick, 2008) for heavy atom finding, SHARP for site refinement/phasing and SOLOMON (Abrahams and Leslie, 1996) for density modification. This resulted in an experimental density map within which a CHAINSAW (Stein, 2008) model based on the D. rerio complex structure could be manually placed, using heavy atom sites as a guide. Experimental density corresponding to the dSTIL peptide could be easily seen. Further refinement cycles allowed the remaining copies of the monomer to be placed and trimmed. Refinement and model building were carried out in autoBUSTER (Bricogne et al., 2011) and Coot (Emsley and Cowtan, 2004) respectively.

### Isothermal calorimetry (ITC) measurements

All ITC measurements were performed using an auto-iTC 200 instrument (GE Healthcare, Little Chalfont, UK) in 50 mM HEPES pH 7.5, 100 mM NaCl at 25°C. Samples were stored by the instrument in 96-well microtiter plates at 5°C prior to loading and performing the titrations. Standard experiments used 19 × 2 μl injections of STIL peptide into CPAP protein preceded by a single 0.5 μl pre-injection. Heat from the pre-injection was not used during fitting. Data were analysed manually in the Origin software package provided by the manufacturer and fit to a single set of binding sites model. All measurements were corrected using control ITC experiments in which the peptide studied was injected into buffer only. The small endothermic heats of injection in these experiments were fitted to a linear function that was subsequently subtracted from the equivalent integrated heats of the peptide–protein binding experiment before fitting. The concentration of CPAP in the cell was typically 40 μM but varied maximally between 20 and 100 μM. The concentration of STIL used in the syringe was typically 700 μM but varied maximally between 600 and 2600 μM depending on the affinity of the peptide interaction being studied.

### In vivo analysis in Drosophila

#### Fly stocks and transgenic constructs

The following mutant alleles and stocks were used in this study: ana2169 (here called dSTIL169), ana2719 (here called dSTIL719) (Wang et al., 2011), sas-4s2214 (here called dCPAP) (Basto et al., 2006), pUbq-dCPAP_WT-GFP, pUbq-dCPAP_ΔC1–724-GFP, pUbq-dCPAP_MC1-GFP, pUbq-dCPAP_MC2-GFP, pUbq-dCPAP_MC3-GFP, pUbq-dCPAP_MC1-3-GFP, pUbq-dCPAP_E792V-GFP, pUbq-dSTIL_WT-GFP, pUbq-dSTIL_ΔN46–420-GFP, pUbq-dSTIL_P11A-GFP, pUbq-dSTIL_R12A-GFP, pUbq-dSTIL_P11AR12A-GFP. Transgenic lines contain GFP fused to the C-terminus of dCPAP and dSTIL, respectively, and are expressed from the Ubiquitin promoter, which drives moderate expression in all cell types (Lee et al., 1988). Flies were kept at 25°C, OregonR served as wild-type control.

GFP-tagged full length versions of dCPAP and dSTIL used in this study were made by cloning the full length dCPAP cDNA and the dSTIL cDNA into the pUbq-GFP(C-terminus) destination vector using the Gateway System (Life Technologies, Carlsbad, CA). PCR with dCPAP_WT and dSTIL_WT as template was used to make dCPAP_ΔC1–724 and dSTIL_ΔN46–420, respectively. Single point mutations and mutation clusters were introduced into full length dCPAP and dSTIL using site-directed mutagenesis (QuickChange II XL/Quick Change Lightening Multi Site-Directed Mutagenesis Kits, Agilent Technologies, Santa Clara, CA). Constructs were injected either by Genetic Services Inc. (Cambridge, MA) or Cambridge DNA Injection Service (Cambridge, UK).

#### Rescue experiments

All constructs were tested for their ability to rescue the uncoordinated phenotype, which is a feature of flies lacking centrioles (Basto et al., 2006). For that purpose, the different versions of dCPAP-GFP and dSTIL-GFP were either crossed into the dCPAP or dSTIL169/dSTIL2719 mutant background, and desired pupae were collected from vials and transferred to filter paper (Whatman, Maidstone, UK) for analysis.

#### Immunohistochemistry on third instar larval brains and centrosome quantification

Brains were dissected, squashed, and stained as previously described (Stevens et al., 2009). The following antibodies were used to stain centrosomes in third instar larval brain cells: sheep anti-Centrosomin (Cnn, directed against the N-terminus, 1:1000, [Lucas and Raff, 2007] but raised in sheep), guinea pig anti-Asterless (Asl, 1:500, [Conduit et al., 2010] but raised in guinea pig). Secondary antibodies conjugated to either Alexa Fluor 488 or Alexa Fluor 568 (Life Technologies) were used 1:1000. Hoechst33258 (Life Technologies) was used to visualise DNA (1:5000). Centrosomes were counted on a Zeiss Axioskop 2 microscope (Zeiss, Oberkochen, Germany). Only brain cells in metaphase were scored that did stain for Asl and Cnn. DNA morphology was used to identify cells at the desired stage of the cell cycle. Furthermore, the assessment of centriole loss was performed blind. Microsoft Excel was used to analyse the data. Images were acquired in Metamorph (molecular devices) using a CoolSNAP HQ camera (Photometrics, Tucson, AZ) and processed using ImageJ/Fiji (www.fiji.sc/Fiji, [Schindelin et al., 2012]), Gimp (www.gimp.org/) and Inkscape (www.inkscape.org/) for figure assembly.

#### Western blot analysis

The following primary and secondary antibodies were used: Mouse anti-GFP (1:500, Roche, Basel, Switzerland), mouse anti-actin (1:1000, SIGMA, St. Louis, MO), rabbit anti-dCPAP (1:500) (Basto et al., 2006), anti-mouse HRP (1:3000, GE Healthcare) and anti-rabbit HRP (1:3000, GE Healthcare).

#### Live imaging of embryos

Embryos expressing the different GFP-tagged versions of dCPAP and dSTIL were dechorionated manually and mounted in a Glass Bottom Microwell Dish (MatTek, Ashland, MA) using heptane glue. Embryos were covered with voltalef oil and followed by time-lapse spinning disc microscopy on a Perkin Elmer spinning disc microscope (Perkin Elmer, Waltham, MA). Images were acquired with a charge-coupled Orca ER device camera (Hamamatsu Photonics, Hamamatsu, Japan) using UltraView ERS (Perkin Elmer) and processed and analysed in Velocity (Perkin Elmer).

### C. elegans experiments

C. elegans strains carrying single-copy sas-4 transgenes were generated using MosSCI (Frøkjær-Jensen et al., 2008). To render the transgenes RNAi-resistant, a 500 bp region at the 5′ end of the sas-4 genomic sequence was re-encoded. The engineered sas-4 sequence was cloned into pCFJ151 with the promoter and 3′ UTR from sas-6, as well as a C-terminal GFP tag. pCFJ151 contains homology arms that direct transposase-mediated insertion of intervening sequence into the ttTi5606 Mos1 site on Chromosome II. Transgene integration was confirmed by PCR of regions spanning each side of the insertion. The genotypes of the strains used are: unc-119(ed9)III; ltSi85[pOD1550; Psas-6::SAS-4 reencoded::GFP; cb-unc-119(+)]II for WT SAS-4; and unc-119(ed9)III; ltSi177[pOD1551; Psas-6::SAS-4(1-556) reencoded::GFP; cb-unc-119(+)]II for SAS-4ΔTCP.

Double-stranded sas-4 RNA was generated as described (Oegema et al., 2001) using DNA templates prepared by PCR. For experiments to quantify monopolar spindle formation, L4 hermaphrodites were injected with dsRNA and incubated at 20°C for 40 hr prior to dissection for imaging. For lethality assays, worms were maintained at 20°C. L4 hermaphrodites were injected with dsRNA and singled 24 hr post-injection. Adult worms were removed from the plates 48 hr post-injection, and hatched larvae and unhatched embryos were counted 24 hr later.

For light microscopy to identify monopolar or bipolar second division cells, images were acquired using an inverted Zeiss Axio Observer Z1 system with a Yokogawa spinning-disk confocal head (CSU-X1), a 63X 1.4 NA Plan Apochromat objective, and a QuantEM:512SC EMCCD camera (Photometrics). Adult worms were dissected in M9 buffer, and embryos were mounted onto 2% agarose pads for imaging. 11 × 1 μm z-stacks were collected in the GFP channel (100 ms, 20% power, no binning), along with one central DIC section.

#### SAS-4/SAS-5 pull-down experiments

SAS-4 constructs were cloned into a pET21a vector for in vitro transcription/translation. Proteins were expressed using the T7 TNT Quick Coupled Transcription/Translation System (Promega, Fitchburg, WI) with 35S-Met labelling.

SAS-5 fragments were cloned into a pRSET-A vector with a C-terminal 6xHis tag. Proteins were expressed in E. coli Rosetta2(DE3) cells and purified on Ni-NTA agarose (Qiagen) using standard protocols. For pull-down experiments, proteins were dialysed into 25 mM HEPES, 100 mM NaCl, 20 mM imidazole, 1 mM DTT, 10% sucrose, 0.02% Tween-20, pH 7.4.

SAS-5 fragments were pre-incubated with 20 μl Ni-NTA beads for 45 min at 4°C. 10 μl of the SAS-4 IVTT product was added to the beads with 190 μl buffer and incubated at 4°C for 30 min. The beads were washed with 3 × 200 μl buffer and resuspended in 100 μl SDS-PAGE sample buffer. Samples were run on 10% SDS-PAGE gels and either stained with Coomassie or dried and exposed to a phosphor screen overnight. Phosphor screens were analysed on a Personal Molecular Imager System (Bio-Rad, Hercules, CA).
