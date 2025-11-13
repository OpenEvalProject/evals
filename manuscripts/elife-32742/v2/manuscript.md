# Mechanistic insights into the active site and allosteric communication pathways in human nonmuscle myosin-2C

## Authors

- Krishna Chinthalapudi<sup>1</sup>
- Sarah M Heissler<sup>1</sup>
- Matthias Preller<sup>1</sup> ([ORCID: 0000-0002-7784-4012](https://orcid.org/0000-0002-7784-4012))
- James R Sellers<sup>4</sup> ([ORCID: 0000-0001-6296-564X](https://orcid.org/0000-0001-6296-564X)) †
- Dietmar J Manstein<sup>1</sup> ([ORCID: 0000-0003-0763-0147](https://orcid.org/0000-0003-0763-0147)) †

### Affiliations

1. Institute for Biophysical Chemistry OE4350, Hannover Medical School Hannover Germany
2. Division for Structural Biochemistry OE8830, Hannover Medical School Hannover Germany
3. Cell Adhesion Laboratory, Department of Integrative Structural and Computational Biology The Scripps Research Institute Jupiter United States
4. Laboratory of Molecular Physiology NHLBI, National Institutes of Health Bethesda United States
5. Centre for Structural Systems Biology (CSSB) German Electron Synchrotron (DESY) Hamburg Germany

† Corresponding author

## Abstract

Despite a generic, highly conserved motor domain, ATP turnover kinetics and their activation by F-actin vary greatly between myosin-2 isoforms. Here, we present a 2.25 Å pre-powerstroke state (ADP⋅VO4) crystal structure of the human nonmuscle myosin-2C motor domain, one of the slowest myosins characterized. In combination with integrated mutagenesis, ensemble-solution kinetics, and molecular dynamics simulation approaches, the structure reveals an allosteric communication pathway that connects the distal end of the motor domain with the active site. Disruption of this pathway by mutation of hub residue R788, which forms the center of a cluster of interactions connecting the converter, the SH1-SH2 helix, the relay helix, and the lever, abolishes nonmuscle myosin-2 specific kinetic signatures. Our results provide insights into structural changes in the myosin motor domain that are triggered upon F-actin binding and contribute critically to the mechanochemical behavior of stress fibers, actin arcs, and cortical actin-based structures.

## Introduction

The extent to which filamentous actin (F-actin) can activate the enzymatic output of conventional myosins-2 varies by more than two orders of magnitude (Heissler and Sellers, 2016; Sellers, 2000). Despite a substantial sequence identity and a highly conserved actomyosin ATPase cycle, structural and allosteric adaptations causative for the tremendous enzymatic and hence physiological differences are largely unknown (Figure 1A) (Heissler and Sellers, 2016, 2013).

![Figure 1.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig1-v2.jpg)

**Figure 1.:** (A) Phylogenetic analysis divides human myosins-2 in the three subfamilies (i) nonmuscle and smooth muscle myosins-2, (ii) cardiac, (iii) and skeletal muscle myosins-2 (Foth et al., 2006). Nonmuscle myosin-2s are essential for the structural integrity of the cytoplasmic architecture during cell shape remodeling and motile events of eukaryotic cells, whereas all other myosins-2 play eminent roles in the contraction of smooth, cardiac and striated muscle cells (Sellers, 2000). Abbreviations used: NM2A: nonmuscle myosin-2A, NM2B: nonmuscle myosin-2B; NM2C: nonmuscle myosin-2C; SM: smooth muscle myosin-2; CardA: α-cardiac myosin-2; CardB: β-cardiac myosin-2; EO2: extraocular myosin-2; EMB: embryonic myosin-2; PERI: perinatal myosin-2; IIb: fast skeletal muscle myosin-2; IIx/d: skeletal muscle myosin-2; IIa: slow skeletal muscle myosin-2. (B) Architecture of the crystallized NM2C construct in the pre-powerstroke state. The myosin motor domain and the α-actinin repeats are shown in cartoon representation in green and grey color. The nucleotide is shown in spheres representation. Inset, Conserved key residues that interact with the nucleotide in the NM2C active site. The Fo-Fc omit map of Mg2+·ADP·VO4 is contoured at 4σ. The salt bridge between switch-1 R261 and switch-2 E483 is highlighted. (C) Subdomain architecture of NM2C. The U50 kDa is shown in green, the L50 kDa in purple, the converter in grey, and the Nter in blue. The region shown in orange corresponds to the active site and the junction of U50 kDa and L50 kDa. The bound nucleotide is shown in spheres representation. The location of the SH1-SH2 helix and the relay helix in the L50 kDa is highlighted.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Consensus scheme of the myosin and actomyosin ATPase cycle. The upper part represents the myosin (M) ATPase cycle. The lower part represents the ATPase cycle in the presence of F-actin (A). The asterisk denotes enhanced states of the intrinsic myosin fluorescence, which are attributed to the nucleotide-induced changes in the microenvironment of the conserved relay loop W525. Lowercase k denotes a rate constant. k+D=k+6, k-D = k-6, k+AD = k+6, k-AD = k-6. An uppercase K denotes a dissociation equilibrium constant (K = k-x/k+x) throughout this work. Normal and bold face notation denote the respective kinetic constants in the absence and presence of F-actin. The main pathway of the actomyosin ATPase cycle is highlighted in grey. Strong and weak actin binding states are indicated. (B) Schematic representation of the expression constructs used in this study. Top, Nonmuscle myosin-2C contains a N-terminal motor domain (green) followed by a neck and a tail domain (dark grey). Middle, For kinetic studies of NM2C, R788K, and R788E, the motor domain was directly fused to spectrin repeats 1 and 2 from Dictyosteliumα-actinin (light grey) which serves as an artificial lever arm. The concept of the artificial lever arm has been successfully used in structural and kinetic studies of myosins-2 (Heissler and Manstein, 2011; Furch et al., 1999; Kliche et al., 2001; Münnich et al., 2014). Bottom: For structural studies, the N-terminal 45 amino acids were deleted. The numbering refers to the amino acid sequence of the full-length protein. (C) The NM2C Cα atoms (green) in ribbon representation superimpose with a root mean square deviation (r.m.s.d.) of 0.57 Å to chicken smooth muscle myosin-2 (grey, PDB entry 1BR2), with 0.78 Å to scallop striated muscle myosin-2 (orange, PDB entry 1QVI), and 0.73 Å to Dictyostelium nonmuscle myosin-2 (blue, PDB entry 2XEL), underlining a strong correlation between Cα geometry and overall motor domain fold. The JK-loop and the nucleotide are highlighted in color and spheres representation. (D) Relative orientation of converter and lever in NM2C (green), chicken smooth muscle myosin-2 (PDB entry 1BR2, grey), and scallop striated muscle myosin-2 (PDB entry 1QVI (orange), 1DFL (violet)) motor domain structures in cartoon representation. α-helices are depicted as cylinders.

Nonmuscle myosin-2C, the gene product of MYH14, is one of the slowest myosins-2 as its steady-state ATPase activity lacks potent F-actin activation (Heissler and Manstein, 2011). Transient kinetic signatures of the nonmuscle myosin-2C enzymatic cycle include a high affinity for ADP, small kinetic (k-AD/k-D) and thermodynamic (KAD/KD) coupling ratios, and a higher duty ratio than it is commonly found in myosins-2 (Figure 1A, Figure 1—figure supplement 1A). Together, these signatures qualify nonmuscle myosin-2C as a dynamic strain-sensing actin tether (Heissler and Manstein, 2013; Heissler and Manstein, 2011; Bloemink and Geeves, 2011). The participation in the active regulation of cytoplasmic contractility in cellular processes including cytokinesis, neuronal dynamics, adhesion, and tension maintenance are in line with this interpretation (Takaoka et al., 2014; Wylie and Chantler, 2008; Ebrahim et al., 2013). Nonmuscle myosin-2C has recently received great attention as the near atomic resolution cryo electron microscopic structure of its motor domain bound to F-actin has been determined (von der Ecken et al., 2016). The structure of the actomyosin complex, together with a detailed kinetic characterization of the motor properties, qualifies nonmuscle myosin-2C as the ideal human myosin to decipher the structure-function relationships in the myosin motor domain that underlie its kinetic signatures (Heissler and Manstein, 2011; von der Ecken et al., 2016).

To understand how structural adaptations lead to characteristic kinetic features, we solved the 2.25 Å crystal structure of the human nonmuscle myosin-2C motor domain (NM2C) (Figure 1B, Table 1). The NM2C pre-powerstroke state structure (ADP⋅VO4) suggests that structural fine-tuning at the active site and a reduced interdomain connectivity in the motor domain define its kinetic signatures. Comparative structural analysis, ensemble solution kinetic studies, and in silico molecular dynamics (MD) simulations collectively demonstrate a communication pathway that connects the active site and the distal end of the motor domain. Disruption of the pathway uncouples the myosin ATPase activity from actin-activation, alters the ATP/ADP sensitivity and results in the loss of nonmuscle myosin-2 kinetic signatures. The allosteric coupling pathway may be of significance in intermolecular gating and load-sensitivity of nonmuscle myosins-2 that is important for their physiological function as cytoskeletal strain-sensor in the context of stress fibers, actin arcs, and cortical actin-based structures.

**Table 1.**
 Crystallographic data collection and refinement statistics for human NM2C.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Hs NM2C-ADP⋅VO4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>X-ray data reduction statistics</td>
      <td></td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P22121</td>
    </tr>
    <tr>
      <td>Unit cell dimensions</td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c</td>
      <td>81.12 Å, 125.61 Å, 153.96 Å</td>
    </tr>
    <tr>
      <td>α,β,γ</td>
      <td>90°, 90°, 90°</td>
    </tr>
    <tr>
      <td>Resolution</td>
      <td>97.33 Å – 2.25 Å</td>
    </tr>
    <tr>
      <td>Last shell</td>
      <td>2.35 Å – 2.25 Å</td>
    </tr>
    <tr>
      <td>Total measurements</td>
      <td>1116790</td>
    </tr>
    <tr>
      <td>No. of unique reflections</td>
      <td>75357</td>
    </tr>
    <tr>
      <td>Last shell</td>
      <td>9069</td>
    </tr>
    <tr>
      <td>Wavelength</td>
      <td>0.91841 Å</td>
    </tr>
    <tr>
      <td>Rmerge</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>Last shell</td>
      <td>0.23</td>
    </tr>
    <tr>
      <td>I/σ(I)</td>
      <td>13.6</td>
    </tr>
    <tr>
      <td>Last shell</td>
      <td>2.63</td>
    </tr>
    <tr>
      <td>Completeness</td>
      <td>0.998</td>
    </tr>
    <tr>
      <td>Last shell</td>
      <td>1.00</td>
    </tr>
    <tr>
      <td>Multiplicity</td>
      <td>14.82</td>
    </tr>
    <tr>
      <td>Last shell</td>
      <td>14.97</td>
    </tr>
    <tr>
      <td>Refinement statistics</td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution</td>
      <td>34.77 Å–2.25 Å</td>
    </tr>
    <tr>
      <td>Last shell</td>
      <td>2.31 Å–2.25 Å</td>
    </tr>
    <tr>
      <td>No. of reflections (working set)</td>
      <td>71459</td>
    </tr>
    <tr>
      <td>No. of reflections (test set)</td>
      <td>3786</td>
    </tr>
    <tr>
      <td>R-factor</td>
      <td>0.2210</td>
    </tr>
    <tr>
      <td>Last shell</td>
      <td>0.2910</td>
    </tr>
    <tr>
      <td>R-free</td>
      <td>0.2410</td>
    </tr>
    <tr>
      <td>Last shell</td>
      <td>0.2920</td>
    </tr>
    <tr>
      <td>No. of non-hydrogen atoms</td>
      <td></td>
    </tr>
    <tr>
      <td>Macromolecules</td>
      <td>7697</td>
    </tr>
    <tr>
      <td>Ligands</td>
      <td>33</td>
    </tr>
    <tr>
      <td>solvent</td>
      <td>666</td>
    </tr>
    <tr>
      <td>Average B-factor</td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>76.06 Å2</td>
    </tr>
    <tr>
      <td>Ligands</td>
      <td>35.59 Å2</td>
    </tr>
    <tr>
      <td>Solvent</td>
      <td>63.37 Å2</td>
    </tr>
    <tr>
      <td>RMS deviations from ideal values</td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths</td>
      <td>0.01 Å</td>
    </tr>
    <tr>
      <td>Bond angles</td>
      <td>1.16°</td>
    </tr>
    <tr>
      <td>Ramachandran favored</td>
      <td>96.22%</td>
    </tr>
    <tr>
      <td>Ramachandran allowed</td>
      <td>3.78%</td>
    </tr>
    <tr>
      <td>Ramachandran outliers</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

## Results

### Overall topology of pre-powerstroke NM2C

We determined a 2.25 Å pre-powerstroke state structure of human NM2C, one of the slowest myosins-2 characterized. Crystallization in the presence of the ATP analog ADP⋅VO4 was achieved after truncation of the flexible N-terminal 45 residues extension and the fusion of the NM2C C-terminus to Dictyostelium α-actinin tandem repeats 1 and 2 (Figure 1B, Figure 1—figure supplement 1B, Table 1). This approach has been used successfully in prior structural and kinetic studies on NM2C and allows the detailed analysis of structure-function relationships in the myosin motor domain (Heissler and Manstein, 2011; von der Ecken et al., 2016).

The overall topology of NM2C shares the structural four-domain architecture of myosin-2 motor domains comprising the N-terminal subdomain (Nter), the upper 50 kDa subdomain (U50 kDa), the lower 50 kDa subdomain (L50 kDa), and the converter that terminates in the lever (Figure 1C) (Rayment et al., 1993). The nucleotide-binding active site is formed by structural elements of the U50 kDa and allosterically communicates with the actin-binding interface that is formed by distant structural elements of the U50 kDa and the L50 kDa. The NM2C Cα atoms superimpose with a root mean square deviation (r.m.s.d.) of 0.57 Å, 0.78 Å, and 0.73 Å to the closely related motor domain structures from chicken smooth muscle myosin-2 (PDB entry 1BR2), scallop striated muscle myosin-2 (PDB entry 1QVI), and Dictyostelium nonmuscle myosin-2 (PDB entry 2XEL) (Figure 1—figure supplement 1C) in the pre-powerstroke state.

NM2C pre-powerstroke state characteristics include a closed conformation of the nucleotide-binding motifs switch-1 and −2 in the active site (Figure 1B). In this conformation, the characteristic salt bridge between switch-1 R261 and switch-2 E483 that is pivotal for the hydrolysis of ATP is formed (Rayment et al., 1993; Furch et al., 1999; Reubold et al., 2003). The coordination of the co-crystallized ADP⋅VO4 is similar to other myosin-2 structures in the pre-powerstroke state. The relay helix is in a kinked conformation, the central seven-stranded β-sheet is untwisted, and the converter domain and the adjacent lever arm in the up-position (Figure 1B). NM2C switch-1 and lever dihedral φ, ψ angles are substantially changed when compared to the pre-powerstroke state structures of chicken smooth muscle myosin-2 (PDB entry 1BR2), indicating that small arrangements in the active site are coupled to conformational changes at the distal end of the motor domain (Figure 1—figure supplement 1C–D, Supplementary file 1). Concomitantly, the relative orientation of converter and lever arm deviates by ~8–10° when compared to the high-resolution pre-powerstroke state crystal structure of chicken smooth muscle myosin-2 (PDB entry 1BR2) and resembled the orientation of the respective regions of scallop striated muscle myosin-2 (PDB entries 1QVI, 1DFL) motor domain structures (Figure 1—figure supplement 1D). In summary, the overall topology of NM2C resembles pre-powerstroke states of other class-2 myosins with subtle changes in the active site and the converter/lever arm orientation that may account for its different kinetic and mechanical output.

### Unique structural rearrangements in the NM2C active site in the pre-powerstroke state

Switch-1, switch-2, P-loop, and the purine-binding A-loop are the prototypic nucleotide-binding motifs in the myosin active site that undergo conformational changes in response to nucleotide binding and release. The active site is flanked by loop-3 and a loop that connects helices J and K in the U50 kDa, hereafter referred to as JK-loop (Figure 2A). The JK-loop constitutes a major connection between switch-1 and the nucleotide is of great functional significance as a hotspot for human cardiomyopathy-causing mutations in cardiac myosin-2 and the site of exon 7 in Drosophila muscle myosin-2 (Figure 2—figure supplement 1A) (Miller et al., 2007; Van Driest et al., 2004; Havndrup et al., 2003).

![Figure 2.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig2-v2.jpg)

**Figure 2.:** (A) Top view on the NM2C active site in the pre-powerstroke state (green) superimposed on pre-powerstroke state structures from chicken smooth muscle myosin-2 (grey, PDB entry 1BR4), Dictyostelium nonmuscle myosin-2 (blue, PDB entry 2XEL), and scallop striated muscle myosin-2 (orange, PDB entry 1QVI). The ATP analog ADP⋅VO4 is shown in spheres representation. (B) Conformation of the JK-loop in vicinity to the NM2C active site. The JK-loop flanks the active site and connects helices J and K. The distance between the residue Q340 of the JK-loop in the U50 kDa and the D257 of switch-1 of the active site is ~8.8 Å. The distance between residue S336 of the JK-loop and switch-1 D257 is ~7.4 Å. Switch-1 residue N256 interacts with α-phosphate (3.1 Å) and β-phosphate (3.5 Å) group of ADP⋅VO4 in the active site. NM2C is colored in green/orange, the JK-loop is colored in brick red and ADP⋅VO4 is shown in spheres. (C) Interactions between the JK-loop and the switch-1 region are compared between the NM2C (green) and scallop striated muscle myosin-2 (orange, PDB entry 1QVI). A-loop residue R128 is coordinating the interaction to the ADP adenosine in the active site of striated muscle myosin-2. The distance between the residues is 3.2 Å. R128 further forms a hydrogen bond (2.8 Å) with E184 of the P-loop. JK-loop N321 is in hydrogen bond interaction with switch-1 N238, located at a distance of 4.6 Å to the hydroxyl group of the C2’ of the ADP ribose. The connectivity between switch-1 and the nucleotide is further strengthened by a hydrogen bond between N237 and the ADP ribose. NM2C lacks all interactions described for scallop striated muscle myosin-2 due to the replacement of R128 with Q150 and JK-loop shortening which increases the distance to the adenosine in the active site to 5.8 Å and disrupts constrains between swich-1 and the JK-loop. All residues in the JK-loop region are labeled for scallop striated muscle myosin-2 (PDB entry 1QVI). For NM2C only amino acid substitutions are labeled for legibility. (D) Superimposition of the NM2C pre-powerstroke state structure (green) and the actin-bound near-rigor actoNM2C complex (red) shows that the nucleotide-binding site does not undergo major structural changes. Actin subunits are colored in shades of grey and the nucleotide is shown in spheres representation. (E) Sequence alignment of select structural elements in the myosin motor domain that interact with the JK-loop. Interactions of A-loop R128 are highlighted with brackets for scallop striated muscle myosin-2 (PDB entry 1QVI). All highlighted interactions are absent in NM2C due to the presence of Q150 in the A-loop. Abbreviations used: Hs NM2C: human NM2C (NP_079005.3); Hs NM2A: human nonmuscle myosin-2A (NP_002464.1); NM2B: human nonmuscle myosin-2B (NP_005955.3); Gg SM: chicken smooth muscle myosin-2 (NP_990605.2); Hs CARD: human beta β-cardiac muscle myosin-2 (NP_000248.2); Ai ST: scallop striated muscle myosin-2 (P24733.1). PDB entries are indicated when available.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Sequence alignment of myosin-2 JK-loops. The asterisk indicates the invariant, negatively charged residues corresponding to NM2C E341. The abbreviations used are as follows: Hs NM2C: human NM2C (NP_079005.3); Hs NM2A: human nonmuscle myosin-2A (NP_002464.1); NM2B: human nonmuscle myosin-2B (NP_005955.3); Gg SM: chicken smooth muscle myosin-2 (NP_990605.2); Hs CARD: human beta β-cardiac muscle myosin-2 (NP_000248.2); Ai ST: scallop striated muscle myosin-2 (P24733.1); Dd NM2: Dictyostelium nonmuscle myosin-2: (XP_637740.1); Dm EMB: Drosophila embryonic body wall muscle myosin-2 (P05661 with spliced exon 7a); Dm IFI: Drosophila indirect flight muscle myosin-2 (P05661 with spliced exon 7d). PDB entries are indicated when available. Cardiomyopathy-associated mutations in β-cardiac myosin-2 on positions F312 (F312C), V320 (V320M), A326 (A326P), and E328 (E328G) are highlighted in the boxed areas. (B) Close-up view of the active site region of pre-powerstroke state structures of NM2C (green), chicken smooth muscle myosin-2 (grey, PDB entry 1BR2), and Dictyostelium nonmuscle myosin-2 (blue, PDB entry 2XEL). The distance between the JK-loops of smooth muscle myosin-2 and Dictyostelium nonmuscle myosin-2 and switch-1 is ~2.8 Å and 8.8 Å for NM2C. The ADP⋅VO4 complex in the active site is shown in spheres. (C) Close-up view of the active site region of pre-powerstroke state chicken smooth muscle myosin-2 (grey, PDB entry 1BR2). The distance between residue P324 of the JK-loop (yellow) in the U50 kDa and D243 of switch-1 is ~2.8 Å. Switch-1 residue N242 interacts with α-phosphate (2.8 Å) and β-phosphate (3.1 Å) group of ADP⋅ALF4 (shown in spheres) in the active site. (D) The volume of the active site, indicated by the spheres, was determined to 3065 Å3 in NM2C by fitting a sphere with a radius (r) of 9.012 Å to the active site with UCSF Chimera (Pettersen et al., 2004). The volume of the sphere was calculated based on its radius using the equation volume = 4/3πr3. (E) The volume of the active site of scallop striated muscle myosin-2 (PDB entry 1QVI) was determined to 697 Å3 based on a radius of r = 5.5 Å as in (D). The structures shown in (D) and (E) are in the pre-powerstroke state.

A slight reduction in the JK-loop length in NM2C causes an 8.8 Å shift between switch-1 and the U50 kDa and abolishes the formation of a tight interaction network with residues of the active site found in other class-2 myosins (Figure 2B,C, Figure 2—figure supplement 1A,B,C). Comparative analysis of interactions between the JK-loop and the switch-1 region in NM2C and scallop striated muscle myosin-2 (PDB entry 1QVI) shows that in the latter, JK-loop N321 is in hydrogen bond interaction with switch-1 N238 and located at a distance of 4.6 Å to the hydroxyl group of the C2’ of the ADP ribose. The connectivity between switch-1 and the nucleotide is further strengthened by a hydrogen bond between N237 and the ADP ribose. Moreover, A-loop residue R128 forms hydrogen bonds with the ADP adenosine (3.2 Å) and E184 (2.8 Å) of the P-loop in the active site of striated muscle myosin-2. Strikingly, NM2C lacks all interactions described for scallop striated muscle myosin-2 due to the replacement of R128 with Q150 and JK-loop shortening. Both structural alterations increase the distance to the adenosine in the active site to 5.8 Å and disrupt constrains between swich-1 and the JK-loop (Figure 2B,C,E). The shift also increases the volume and hence the accessibility of the NM2C active site when compared to the transition state structures of chicken smooth muscle myosin-2 (PDB entry 1BR2), Dictyostelium nonmuscle myosin-2 (PDB entry 2XEL), and scallop striated muscle myosin-2 (PDB entry 1DFL,1QVI) (Figure 2A, Figure 2—figure supplement 1B,D,E). Changes in the spheres that describe the active site volumes indicate a 4.3-fold increase from 697 Å3 in the case of scallop striated muscle myosin-2 (PDB entry 1QVI) to 3054 Å3 for NM2C (Figure 2—figure supplement 1D,E). Strikingly, the enlarged accessibility of the active site region observed in the NM2C pre-powerstroke state structure resembles the conformation of the active site found in the actin-bound NM2C rigor state (PDB entry 5J1H), indicating that F-actin binding does not induce major structural rearrangements in the vicinity of the active site (Figure 2C). Together, these features demonstrate significant differences in the interaction pattern and geometry of the NM2C active site compared to other myosins-2.

The temperature factors obtained from the refined crystal structure show that the NM2C JK-loop is highly flexible despite its reduced length. We attribute the flexibility to the lack of constraints with switch-1 residues and the bound nucleotide (Figure 2A,B,C,E). Specifically, the connectivity of the JK-loop to switch-1 is reduced by the replacement of a conserved arginine (R280 in PDB entry 1QVI) with cysteine (C299) in the loop preceding helix I. This arginine further establishes an interaction with the highly conserved switch-1 K233 in scallop striated muscle myosin-2. The arginine to cysteine substitution in NM2C also abolishes the formation of a salt bridge with JK-loop residue E341 and hence disrupts the connection between the JK-loop and switch-1 (Figure 2C,E, Figure 2—figure supplement 1C). Consequently, the JK-loop loses its ability to sense conformational changes in the nucleotide binding motif switch-1 in response to ATP binding, hydrolysis, and product release.

The interaction between the JK-loop and the nucleotide is weakened by the replacement of an asparagine with G339, which abolishes hydrogen bond formation with switch-1 D257. Comparison with data from previous crystallographic studies shows that D257 replaces an asparagine (N238 in PDB entry 1QVI) in the switch-1 in striated muscle myosins-2. The asparagine interacts weakly with the ADP moiety in the pre-powerstroke state (Figure 2B,D,E, Figure 2—figure supplement 1B,C) and strongly in the near-rigor state (Risal et al., 2004; Swank et al., 2006). The nucleotide coordination in NM2C is further weakened by residue Q150 that replaces an arginine (R128 in PDB entry 1QVI) in the A-loop of scallop striated muscle myosin-2. The substitution disrupts coordinating interactions between the A-loop and the ADP adenosine (Figure 2D, Figure 2—figure supplement 1B,C). The replacement additionally impairs the formation of a salt bridge with the invariant E206 (E184 in PDB entry 1QVI) at the distal end of the P-loop that is predicted to be involved in nucleotide recruitment to the active site (Figure 2D, Table 2) (Risal et al., 2004). Further, the substitution of an arginine with K255 and a glutamate with H700 in NM2C is expected to weaken a tight and highly conserved interaction network between the active site and the Nter of NM2C (Table 2) (Risal et al., 2004). In summary, our comparative structural analysis of the active site of myosins-2 suggests that the interconnectivity of the highly conserved nucleotide switches and myosin subdomains is weaker in NM2C and likely other nonmuscle myosins-2 compared to fast sarcomeric myosins-2.

**Table 2.**
 Structure function relationships in the myosin-2 motor domain.Interactions between residues in the active site involved in nucleotide binding and release kinetics based on this work and previous biochemical and structural studies on myosin motor domains (Miller et al., 2007; Risal et al., 2004; Swank et al., 2006; Grammer et al., 1993; Szilagyi et al., 1979). It is of note that myosin is a highly allosteric enzyme and nucleotide binding and release kinetic involve numerous interactions and subtle structural rearrangements of residues from different motor subdomains. Kinetic parameters from monomeric myosin motor domain constructs that are associated with a structural interaction are listed for direct comparison. An emerging trend from this analysis is that the myosin-2 kinetic cycle does not have a selectivity of ATP versus ADP. The presence of F-actin results in different allosteric communication pathways in myosins-2 and establishes ATP/ADP binding selectivity. Overall, nucleotide-binding rates are decreased for the group of nonmuscle and smooth muscle myosins-2 compared to myosins-2 from cardiac and skeletal muscle. The lacking salt bridge interactions between JK-loop, U50 kDa and switch-1 in nonmuscle myosins-2 results in decreased second-order binding rate constants for ATP (K1k+2) and ADP (k+D) (Figure 1—figure supplement 1A). Either a salt bridge interaction or hydrophobic interactions between the A-loop and the P-loop of muscle and cardiac myosins-2 at the active site favor fast nucleotide binding kinetics and does not or only marginally discriminate between ADP and ATP. The lack of a salt bridge interactions can have different effects dependent on the coordinating residue in the A-loop: An asparagine in the A-loop of nonmuscle myosins-2A and −2B favors ADP over ATP binding to actomyosin. A glutamine in the NM2C A-loop, which has a longer side chain than asparagine, abolishes ATP/ADP sensitivity in NM2C and the closely related smooth muscle myosin-2. The number of salt bridge interactions between P-loop, switch-1, and the Nter correlates with the thermodynamic and kinetic coupling, and the actin-activated ADP release rates in all myosins-2. Abbreviations used: NM2A: human nonmuscle myosin-2A; human NM2B: nonmuscle myosin-2B (PDB entry 4PD3); NM2C: human nonmuscle myosin-2C; SM: chicken smooth muscle myosin-2 (PDB entry 1BR2); CARD: human β-cardiac myosin-2 (PDB entry 4DB1); Oc ST: rabbit striated muscle myosin-2 (PDB entry 1DFL).


<table>
  <thead>
    <tr>
      <th>Myosin</th>
      <th>Residue</th>
      <th>Residue</th>
      <th>Residue</th>
      <th>Residue</th>
      <th>Parameter</th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th>JK-loop</th>
      <th>U50 kDa</th>
      <th>JK-loop</th>
      <th>Switch-1</th>
      <th>K1k+2</th>
      <th>K+D</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hs NM2A (Kovács et al., 2003)</td>
      <td>D315</td>
      <td>R272</td>
      <td>G312</td>
      <td>D230</td>
      <td>0.56</td>
      <td>0.55</td>
      <td></td>
    </tr>
    <tr>
      <td>Hs NM2B (Wang et al., 2003)</td>
      <td>D322</td>
      <td>R279</td>
      <td>G319</td>
      <td>D237</td>
      <td>0.65</td>
      <td>0.81</td>
      <td></td>
    </tr>
    <tr>
      <td>Hs NM2C</td>
      <td>E341</td>
      <td>C299</td>
      <td>G339</td>
      <td>D257</td>
      <td>0.48</td>
      <td>0.39</td>
      <td></td>
    </tr>
    <tr>
      <td>Gg SM (Cremo and Geeves, 1998)</td>
      <td>D328</td>
      <td>R285</td>
      <td>A325</td>
      <td>D243</td>
      <td>2.1</td>
      <td>1.8</td>
      <td></td>
    </tr>
    <tr>
      <td>Hs CARD (Deacon et al., 2012)</td>
      <td>D325</td>
      <td>R281</td>
      <td>S322</td>
      <td>D239</td>
      <td>1.5</td>
      <td>1.5</td>
      <td></td>
    </tr>
    <tr>
      <td>Oc ST (Ritchie et al., 1993; Kurzawa-Goertz et al., 1998)</td>
      <td>D323</td>
      <td>R280</td>
      <td>N321</td>
      <td>N238</td>
      <td>3.9</td>
      <td>1.7</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Residue</td>
      <td>Residue</td>
      <td>Parameter</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>A-loop</td>
      <td>P-loop</td>
      <td>k+AD</td>
      <td>K1k+2</td>
      <td>k+D</td>
      <td>K1k+2</td>
      <td>k+AD/ K1k+2</td>
    </tr>
    <tr>
      <td>Hs NM2A (Kovács et al., 2003)</td>
      <td>N126</td>
      <td>E182</td>
      <td>2.72</td>
      <td>0.14</td>
      <td>0.55</td>
      <td>0.56</td>
      <td>19.4</td>
    </tr>
    <tr>
      <td>Hs NM2B (Wang et al., 2003)</td>
      <td>N130</td>
      <td>E186</td>
      <td>2.41</td>
      <td>0.24</td>
      <td>0.81</td>
      <td>0.65</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Hs NM2C</td>
      <td>Q150</td>
      <td>E206</td>
      <td>2.54</td>
      <td>1.86</td>
      <td>0.39</td>
      <td>0.48</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>Gg SM (Cremo and Geeves, 1998)</td>
      <td>Q129</td>
      <td>E185</td>
      <td>3.6</td>
      <td>2</td>
      <td>1.8</td>
      <td>2.1</td>
      <td>4.4</td>
    </tr>
    <tr>
      <td>Hs CARD (Deacon et al., 2012)</td>
      <td>W130</td>
      <td>V186</td>
      <td>4.4</td>
      <td>1.1</td>
      <td>1.5</td>
      <td>1.5</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td>Oc ST (Ritchie et al., 1993; Kurzawa-Goertz et al., 1998)</td>
      <td>R128</td>
      <td>E184</td>
      <td>1.6</td>
      <td>2.5</td>
      <td>1.7</td>
      <td>3.9</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>Residue</td>
      <td>Residue</td>
      <td>Residue</td>
      <td>Parameter</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>P-loop</td>
      <td>Switch-1</td>
      <td>Nter</td>
      <td>KAD/KD</td>
      <td>k-AD/k-D</td>
      <td>k-AD</td>
      <td></td>
    </tr>
    <tr>
      <td>Hs NM2A (Kovács et al., 2003)</td>
      <td>E175</td>
      <td>K228</td>
      <td>H676</td>
      <td>0.7</td>
      <td>2.8</td>
      <td>1.72</td>
      <td></td>
    </tr>
    <tr>
      <td>Hs NM2B (Wang et al., 2003)</td>
      <td>E179</td>
      <td>K235</td>
      <td>H683</td>
      <td>0.2</td>
      <td>0.7</td>
      <td>0.35</td>
      <td></td>
    </tr>
    <tr>
      <td>Hs NM2C</td>
      <td>E199</td>
      <td>K255</td>
      <td>H700</td>
      <td>0.11</td>
      <td>1</td>
      <td>0.65</td>
      <td></td>
    </tr>
    <tr>
      <td>Gg SM (Cremo and Geeves, 1998)</td>
      <td>E178</td>
      <td>K241</td>
      <td>H689</td>
      <td>4.2</td>
      <td>12</td>
      <td>15</td>
      <td></td>
    </tr>
    <tr>
      <td>Hs CARD (Deacon et al., 2012)</td>
      <td>E179</td>
      <td>R237</td>
      <td>E677</td>
      <td>42</td>
      <td>103.3</td>
      <td>150</td>
      <td></td>
    </tr>
    <tr>
      <td>Oc ST (Ritchie et al., 1993; Kurzawa-Goertz et al., 1998)</td>
      <td>E177</td>
      <td>R236</td>
      <td>E675</td>
      <td>49</td>
      <td>250</td>
      <td>500</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Interdomain connectivity between converter, Nter, and lever

The interdomain connectivity between the converter and the Nter in the myosin-2 motor domain is established by the relay and the SH1-SH2 helix. The Nter controls the movement of the converter, which undergoes a large-scale rotation that drives the powerstroke during force generation (Sasaki et al., 2003; Ramanath et al., 2011; Brenner et al., 2014; Llinas et al., 2015; Preller and Manstein, 2013).

Residue R788 at the interface of converter, Nter, and lever is highly conserved in nonmuscle and smooth muscle myosins-2 and the only connecting hub between structural elements of the L50 kDa and the Nter in NM2C (Figure 3A,B). Notably, replacement of R788 with a lysine in muscle myosins-2 weakens the interaction between the aforementioned structural elements in all states of the myosin and actomyosin kinetic cycle (Figure 3—figure supplement 1A,B). In NM2C, R788 forms three main chain and five side chain interactions with residues of the SH1-SH2 helix, the converter, and the lever in the pre-powerstroke state in addition to a side chain interaction with a water molecule (2.8 Å). Specifically, the guanidinium group of the R788 side chain of NM2C forms hydrogen bonds with the main chain carbonyls of residues Q730 and G731 of the SH1 helix. The hydrophobic methylene groups of R788 are stabilized by SH1 helix F732 and the main chain oxygen and hydroxyl groups of N776 of the converter. Y518 from the relay helix interacts with residues G731 and F732 of the converter, thereby interlinking R788 with both structural elements. The side chain of R788 is in van der Waals distance (4.8 Å) from W525 of the relay loop. The main chain carbonyl of R788 further interacts with V791 at the converter/lever junction (Figure 3A,B). This interaction is important for the stabilization of the converter fold and the interface with the lever in the absence of F-actin. Notably, the R788 side chain:main chain interaction is also evident in crystal structures of nonmuscle myosins-2 in the nucleotide-free (PDB entry 4PD3) and the phosphate-release state (PDB entry 4PJK) (not shown).

![Figure 3.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig3-v2.jpg)

**Figure 3.:** (A) Interaction profile of R788 in the pre-powerstroke state. R788 is shown in orange colored sticks and the converter is colored in white, the relay helix in red, the SH1-SH2 helix in purple, and the lever arm in green colored cartoon representation. The inset shows a close-up view of the complete R788 interaction profile and is rotated 137° respective to the main panel. The guanidinium group of R788 forms hydrogen bonds (2.8 Å) with backbone oxygen atom of Q730 from the SH1 helix and the backbone oxygen atom of G731 (3.0 Å) of the converter. The δ-nitrogen atom of R788 interacts (3.0 Å) with N776 backbone oxygen atom of N776. The R788 guanidinium group interacts (3.1 Å) with the hydroxyl group of N776 of the converter. The backbone nitrogen atom of R788 interacts (3.1 Å) with the carbonyl group of L777 of the converter. The backbone carbonyl group of R788 interacts (3.4 Å) with the backbone nitrogen of V791 of the lever as well as a water molecule (3.0 Å). The hydroxyl group from relay helix Y518 interacts with the backbone nitrogen atom of G731 (2.8 Å) and backbone oxygen atom of F732 (3.4 Å). F732 forms hydrophobic interactions with the methylene groups of R788 with the latter positioned in van der Waals distance to relay loop W525. All the amino acids involved in interactions with R788 are shown as sticks and water molecules as spheres. (B) Sequence alignment of selected regions from relay helix, SH1 helix, converter and lever arm shows the high sequence conservation within the myosin-2 motor domain. The asterisk indicates the invariant, positively charged residue corresponding to NM2C R788. The interactions of NM2C R788 with structural elements of the L50 kDa, the converter, and the lever are highlighted. Abbreviations used: Hs NM2C: human NM2C (NP_079005.3); Hs NM2A: human nonmuscle myosin-2A (NP_002464.1); NM2B: human nonmuscle myosin-2B (NP_005955.3); Gg SM: chicken smooth muscle myosin-2 (NP_990605.2); Hs CARD: human beta β-cardiac muscle myosin-2 (NP_000248.2); Ai ST: scallop striated muscle myosin-2 (P24733.1). PDB entries are indicated when available. Lysine residues that replace R788 in cardiac and striated muscle myosins-2 highlighted in the boxed area.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** In contrast to NM2C (Figure 3), the substitution of R788 with K763 in scallop striated muscle myosin-2 (PDB entry IQVI) (A) and K766 in human β-cardiac muscle myosin-2 (PDB entry 4DB1) (B) reduces the number of side chain and main chain interactions at the converter/Nter/lever junction. (C) In the conservative mutant R788K, the side chain: side chain and side chain: main chain interactions are reduced compared to NM2C (Figure 3). A further reduction in side chain: side chain and side chain: main chain interactions is achieved in the charge reversal mutant R788E (D). Coloring is according to Figure 3.

We therefore hypothesize that (i) the tight interaction network formed by R788 is required for the precise positioning and coupling of the converter, the SH1-SH2 helix, the relay helix, and the lever arm throughout all steps of the myosin ATPase cycle (Figure 1—figure supplement 1A), and that (ii) different communication pathways between the active site and the distal end of the motor domain are employed by NM2C in the presence and absence of F-actin.

### Kinetic consequences after the disruption of the converter/Nter/lever interface

To experimentally probe for a possible effect of R788 on myosin motor function, we performed comparative ensemble solution kinetic studies with NM2C and two mutants in which the interaction between residue 788 and interacting residues at the converter/Nter/lever interface is weakened. In the conservative R788K mutant, a lysine, as it is found in sarcomeric myosins-2 replaces the converter R788. In R788E, a glutamate replaces the converter R788. Rationale for the design of the conservative R788K mutant was to reduce the number of electrostatic side chain:side chain and side chain:main chain interactions compared to NM2C. Based on the NM2C pre-powerstroke state structure, the side chain of K788 interacts with the main chain carbonyl of residue G731 (3.1 Å) of the SH1 helix. The main chain carbonyl of K788 is further predicted to interact with the main chain of V791 at the converter/lever junction. Other interactions with elements of the SH1-SH2 helix, the converter, the lever, and the water molecule (5 Å) as observed in NM2C are lost (Figure 3—figure supplement 1C). The charge reversal mutant R788E was designed to further reduce the number of side chain:side chain and side chain:main chain interactions. Interactions between the side chain carboxyl group of E788 and other residues at the converter/Nter/lever interface are abolished. The distance to the water molecule increases to 4.9–6.3 Å and does not allow the formation of a hydrogen bond. The main chain:main chain interaction with V791 is preserved and represents the only connection with the converter/lever junction (Figure 3—figure supplement 1D).

Confirming our hypotheses, transient kinetic changes in R788E are more severe than in R788K and mainly affect nucleotide binding and release kinetics (Table 3). Transient kinetic changes are more pronounced in the absence of F-actin, as seen in single-turnover measurements (Figure 4A,B). Most importantly, nonmuscle myosin-2 specific transient kinetic signatures such as a high k+AD/K1k+2 ratio (k+AD/K1k+2 ~ 2–20) are absent in R788E (k+AD/K1k+2 ~ 0.02) (Table 3, Figure 4—figure supplement 1A–D) (Heissler and Manstein, 2011; Kovács et al., 2003; Wang et al., 2003). This feature is also described for conventional myosins-2 from cardiac and striated muscle that bind ATP and ADP with similar rates (Table 4) (Marston and Taylor, 1980). Actin-activation of the ADP release (k-AD = 0.68 ± 0.01 s−1 for NM2C, k-AD = 0.59 ± 0.01 s−1 for R788K, and k-AD = 0.19 ± 0.01 s−1 for R788E) results in a kinetic coupling constant k-AD/k-D of ~3.8 for R788E, whereas neutral or negative kinetic coupling are features of NM2C (k-AD/k-D ~ 0.7), R788K (k-AD/k-D ~ 1.1), and other human nonmuscle myosins-2 (Table 4) (Heissler and Manstein, 2011; Kovács et al., 2003; Wang et al., 2003). The changes in ADP binding and release kinetics of R788E result in a 10-fold increase in the ADP dissociation equilibrium constant KAD (KAD ~0.26 µM for NM2C and ~3 µM for R788E). The thermodynamic coupling (KAD/KD = 5) for R788E is 42-times stronger than for NM2C (Table 3). R788E displays an extraordinary slow ADP binding rate constant (k+AD = 0.03 ± 0.001 µM−1s−1) (Table 3, Figure 4—figure supplement 1D) in the presence of F-actin, whereas the kinetic constants for the interaction between actomyosin and ATP, K1k+2, k+2, and 1/K1 are only marginally affected when compared to NM2C (2). The F-actin affinity in the absence and presence of ADP (KA, KDA) of NM2C and R788E is similar (Table 3), whereas KDA is three- to five-fold higher in R788K (Table 3). F-actin can activate the steady-state ATPase activity of R788E to approximately half the kcat of NM2C (kcat = 0.2 ± 0.01 s−1 for R788E and kcat = 0.37 ± 0.02 s−1 of NM2C) (Table 3) under steady-state conditions. The steady-state parameter kcat = 0.26 ± 0.2 s−1 for R788K is in between the respective parameters for NM2C and R788K. The duty ratio at an F-actin concentration of 190 µM and saturating [ATP] increases from ~0.3 for NM2C and R788K to ~1 for R788E due to the decreased kcat and the decreased actin-activated ADP release rate k-AD. This feature makes k-AD likely to rate-limit the kinetic cycle of R788E, whereas the actin-activated Pi release is expected to rate-limit the kinetic cycles of NM2C, R788K, and other myosins-2 (Heissler and Sellers, 2016; Heissler and Manstein, 2011; Kovács et al., 2003; Wang et al., 2003; Woodward et al., 1995; Ritchie et al., 1993).

![Figure 4.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig4-v2.jpg)

**Figure 4.:** (A) Interaction between NM2C/R788K/R788E with ATP under single-turnover conditions. Binding 0.375 µM d-mantATP to 0.5 µM myosin results in a transient fluorescence increase that is followed by a short plateau (hydrolysis) and a slow decrease in mantADP fluorescence that is associated with its release. All three phases are reduced in R788E (grey) compared to NM2C (green) and R788K (yellow). The very slow decrease of the fluorescence signal in R788E indicates that either the ATP hydrolysis rate or a subsequent release rate of the hydrolysis products are severely decreased when compared to NM2C and R788K. (B) Interaction between 0.25 µM pyrene-actoNM2C/R788K/R788E with 0.15 µM ATP under single-turnover conditions. Color coding is according to (A).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Dependence of the observed rate constants (kobs) upon d-mantATP binding to 0.25 µM NM2C/R788K/R788E on the nucleotide concentration. Linear fits to the data result in second-order binding rate constants of K1k+2 = 0.48±0.01 µM−1s−1 for NM2C (green), a two-fold reduced ATP binding constant K1k+2 = 0.22±0.01 µM−1s−1 for R788K (yellow), and a five-fold reduced binding rate constant of K1k+2 = 0.09±0.005 µM−1s−1 for R788E (grey) compared to NM2C. Inset, The rate constants (kobs) obtained from the binding reaction of ATP to NM2C/R788K dependent hyperbolically on the ATP concentration. The rate of ATP hydrolysis (k+3+k-3) and the second-order binding rate constants K1k+2 were determined from a fit to the data (NM2C: k+3+k-3=24.32 ± 0.89 s−1; K1k+2 = 0.39±0.01 µM−1s−1; R788K: k+3+k-3=37.31 ± 0.55 s−1; K1k+2 = 0.18±0.01 µM−1s−1). The respective parameters are not experimentally accessible for R788E. (B) The apparent second-order ATP binding rate constants, determined by the ATP-induced dissociation of the pyrene-labeled actoNM2C (green) or actoR788E (grey) complexes are with K1k+2 = 1.86±0.03 µM−1s−1 and K1k+2 = 2.11±0.05 µM−1s−1 similar. The respective constant is reduced to K1k+2 = 1.03±0.03 µM−1s−1 for actoR788K (yellow). Inset, The maximum isomerization rate constants k+2 = 643.06±22.6 s−1 (NM2C), k+2 = 767.43±21.27 s−1 (R788K), and k+2 = 579.27±12.81 s−1 was determined from a hyperbolic fit to the respective data. (C) The R788K (yellow) and the R788E (grey) mutation decrease the second-order ADP-binding rate constant two- to threefold to k+D = 0.21±0.02 µM−1s−1 and k+D = 0.12±0.01 µM−1s−1 when compared to k+D = 0.39±0.01 µM−1s−1 for NM2C (green). (D) The ADP-binding rate constant k+AD = 0.03±0.001 µM−1s−1, as calculated from the slope of the kobs versus [d-mantADP] plot, is 85-fold decreased for R788E (grey) when compared to k+AD = 2.54±0.18 µM−1s−1 for NM2C (green). (E) Time-dependent change in the intrinsic tryptophan signal upon mixing 0.5 mM ATP with 0.25 µM NM2C (grey) or R778E (grey) in the presence of 5 µM ADP. ATP binding increases the fluorescence signal in NM2C but not R788E under identical conditions in a stopped-flow spectrophotometer. (F) Missense mutations G376C and R726S are associated with autosomal dominant hearing impairment (DFNA4) and their location in NM2C is shown in spheres representation. G376C is in proximity to the JK-loop, R726S is in the SH1-SH2 helix. NM2C subdomains are color coded according to Figure 1C and the nucleotide is shown in spheres representation.

**Table 3.**
 Steady-state and transient state kinetic parameters of NM2C, R788K, and R788E.Numbering of the kinetic constants refers to Figure 1—figure supplement 1A. Measurements of transient kinetic parameters that rely on a change in intrinsic tryptophan fluorescence are not experimentally accessible for R788E. Normal and bold face notation denote the respective kinetic constants in the absence and presence of F-actin.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Signal or calculation</th>
      <th>NM2C</th>
      <th>R788K</th>
      <th>R788E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Steady-state ATPase</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>kcat (s−1)</td>
      <td>NADH assay*</td>
      <td>0.37 ± 0.02</td>
      <td>0.26 ± 0.02</td>
      <td>0.2 ± 0.01</td>
    </tr>
    <tr>
      <td>Kapp (µM)</td>
      <td>NADH assay*</td>
      <td>129.4 ± 17.2</td>
      <td>110.5 ± 15.89</td>
      <td>45.9 ± 13</td>
    </tr>
    <tr>
      <td>kcat/Kapp (µM−1s−1)</td>
      <td>NADH assay</td>
      <td>~0.003</td>
      <td>~0.002</td>
      <td>~0.004</td>
    </tr>
    <tr>
      <td>ATP interaction</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>K1k+2 (µM−1s−1)</td>
      <td>Tryptophan</td>
      <td>0.39 ± 0.01</td>
      <td>0.18 ± 0.01</td>
      <td>Not accessible¶</td>
    </tr>
    <tr>
      <td>K1k+2 (µM-1s−1)</td>
      <td>d-mantATP</td>
      <td>0.48 ± 0.01</td>
      <td>0.22 ± 0.01</td>
      <td>0.09 ± 0.005</td>
    </tr>
    <tr>
      <td>1/K0.5 (µM)</td>
      <td>Tryptophan</td>
      <td>46.23 ± 5.22</td>
      <td>158.03 ± 9</td>
      <td>Not accessible¶</td>
    </tr>
    <tr>
      <td>k3 + k-3 (s−1)</td>
      <td>Tryptophan</td>
      <td>24.2 ± 0.86</td>
      <td>37.31 ± 0.55</td>
      <td>Not accessible¶</td>
    </tr>
    <tr>
      <td>K1k+2 (µM−1s−1)</td>
      <td>Pyrene-actin</td>
      <td>1.86 ± 0.03</td>
      <td>1.03 ± 0.03</td>
      <td>2.11 ± 0.05</td>
    </tr>
    <tr>
      <td>K1k+2 (µM−1s−1)</td>
      <td>d-mantATP</td>
      <td>1.64 ± 0.04</td>
      <td>0.73 ± 0.02</td>
      <td>1.37 ± 0.04</td>
    </tr>
    <tr>
      <td>1/K1 (µM)</td>
      <td>Pyrene-actin</td>
      <td>~318</td>
      <td>~826</td>
      <td>~380</td>
    </tr>
    <tr>
      <td>k + 2 (s−1)</td>
      <td>Pyrene-actin</td>
      <td>643.06 ± 22.6</td>
      <td>767.43 ± 21.27</td>
      <td>579.27 ± 12.81</td>
    </tr>
    <tr>
      <td>ADP interaction</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>k+D (µM−1s−1)</td>
      <td>d-mantADP</td>
      <td>0.39 ± 0.01</td>
      <td>0.21 ± 0.02</td>
      <td>0.12 ± 0.01</td>
    </tr>
    <tr>
      <td>k-D (s−1)</td>
      <td>d-mantADP†</td>
      <td>0.94 ± 0.07</td>
      <td>0.58 ± 0.05</td>
      <td>0.06 ± 0.01</td>
    </tr>
    <tr>
      <td>k-D (s−1)</td>
      <td>d-mantADP‡</td>
      <td>0.39 ± 0.01</td>
      <td>0.51 ± 0.01</td>
      <td>0.05 ± 0.001</td>
    </tr>
    <tr>
      <td>k-D (s−1)</td>
      <td>Tryptophan‡</td>
      <td>0.47 ± 0.02</td>
      <td>0.24 ± 0.001</td>
      <td>Not accessible¶</td>
    </tr>
    <tr>
      <td>KD (µM)</td>
      <td>k-D/k+D</td>
      <td>~1–2.4</td>
      <td>~1.1–2.8</td>
      <td>~0.5</td>
    </tr>
    <tr>
      <td>k+AD (µM−1s−1)</td>
      <td>d-mantADP</td>
      <td>2.54 ± 0.18</td>
      <td>not accessible**</td>
      <td>0.03 ± 0.001</td>
    </tr>
    <tr>
      <td>k-AD (s−1)</td>
      <td>d-mantADPb</td>
      <td>0.65 ± 0.06</td>
      <td>not accessible**</td>
      <td>0.09 ± 0.03</td>
    </tr>
    <tr>
      <td>k-AD (s−1)</td>
      <td>Light scattering‡</td>
      <td>0.39 ± 0.01</td>
      <td>0.42 ± 0.002</td>
      <td>0.15 ± 0.01</td>
    </tr>
    <tr>
      <td>k-AD (s−1)</td>
      <td>d-mantADP‡</td>
      <td>0.68 ± 0.01</td>
      <td>0.59 ± 0.01</td>
      <td>0.19 ± 0.01</td>
    </tr>
    <tr>
      <td>k-AD (s−1)</td>
      <td>Pyrene-actin‡</td>
      <td>0.48 ± 0.01</td>
      <td>0.46 ± 0.01</td>
      <td>0.14 ± 0.01</td>
    </tr>
    <tr>
      <td>KAD (µM)</td>
      <td>k-AD/k+AD</td>
      <td>~0.29</td>
      <td>Not accessible</td>
      <td>~2.68</td>
    </tr>
    <tr>
      <td>Actin interaction</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>k+A (µM−1s−1)</td>
      <td>Light scattering§,#</td>
      <td>2.49 ± 0.07</td>
      <td>1.65 ± 0.03</td>
      <td>0.66 ± 0.03</td>
    </tr>
    <tr>
      <td>k-A (s−1)</td>
      <td>Pyrene-actin§,#</td>
      <td>~0.15</td>
      <td>~0.04–0.07</td>
      <td>~0.031</td>
    </tr>
    <tr>
      <td>KA (nM)</td>
      <td>k-A/k+A</td>
      <td>~60</td>
      <td>~24–42</td>
      <td>~47</td>
    </tr>
    <tr>
      <td>k+DA (µM−1s−1)</td>
      <td>Light scattering§</td>
      <td>0.53 ± 0.01</td>
      <td>2.53 ± 0.05</td>
      <td>0.21 ± 0.01</td>
    </tr>
    <tr>
      <td>k-DA (s−1)</td>
      <td>Pyrene-actin§</td>
      <td>~0.004</td>
      <td>~0.067–0.11</td>
      <td>~0.002</td>
    </tr>
    <tr>
      <td>KDA (nM)</td>
      <td>k-DA/k+DA</td>
      <td>~8</td>
      <td>~26–43</td>
      <td>~9</td>
    </tr>
  </tbody>
</table>

_*In 50 mM NaCl, 2 mM MgATP, T = 25°C.†From y-intercept.‡From chasing experiment.§Measured in salt free stopped-flow buffer.#Samples were treated with apyrase prior to the assay to ensure rigor conditions.¶The lack of a change in intrinsic fluorescence upon nucleotide binding to R788E precludes the direct measurement of this kinetic parameter.**Small amplitudes prevent the direct measurement of this parameter._

**Table 4.**
 Comparative analysis of kinetic signatures of monomeric myosin-2 motor domain constructs.Abbreviations used: NM2A: human nonmuscle myosin-2A, NM2B: human nonmuscle myosin-2B (PDB entry 4PD3); NM2C: human nonmuscle myosin-2C; SM: chicken smooth muscle myosin-2 (PDB entry 1BR2); CARD: human/chicken β-cardiac myosin-2 (PDB entry 4DB1); ST: rabbit/scallop striated muscle myosin-2 (PDB entry 1DFL).


<table>
  <thead>
    <tr>
      <th>Myosin</th>
      <th>kcat/Kapp</th>
      <th>k+AD/K1k+2</th>
      <th>KAD/KD</th>
      <th>k-AD/ k-D</th>
      <th>KDA/KA</th>
      <th>Duty ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hs NM2C</td>
      <td>0.003</td>
      <td>1.5</td>
      <td>0.11</td>
      <td>1</td>
      <td>0.13</td>
      <td>~0.3‡</td>
    </tr>
    <tr>
      <td>Hs R788K</td>
      <td>0.002</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>1</td>
      <td>1</td>
      <td>~0.3‡</td>
    </tr>
    <tr>
      <td>Hs R788E</td>
      <td>0.004</td>
      <td>0.26</td>
      <td>5</td>
      <td>3</td>
      <td>0.19</td>
      <td>~1$</td>
    </tr>
    <tr>
      <td>Hs NM2A (Kovács et al., 2003)</td>
      <td>0.002</td>
      <td>19.4</td>
      <td>0.7</td>
      <td>2.8</td>
      <td>2</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>Hs NM2B (Wang et al., 2003)</td>
      <td>0.002</td>
      <td>10</td>
      <td>0.2</td>
      <td>0.7</td>
      <td>0.4</td>
      <td>0.37</td>
    </tr>
    <tr>
      <td>Gg SM (Marston and Taylor, 1980; Cremo and Geeves, 1998)</td>
      <td>0.07</td>
      <td>4.4</td>
      <td>4.2</td>
      <td>12</td>
      <td>6.9</td>
      <td>&lt;0.05</td>
    </tr>
    <tr>
      <td>Hs/Gg CARD (Marston and Taylor, 1980; Deacon et al., 2012)</td>
      <td>0.07†</td>
      <td>1.6</td>
      <td>42</td>
      <td>103.3</td>
      <td>23.9</td>
      <td>&lt;0.02</td>
    </tr>
    <tr>
      <td>Oc/Ai ST (Ritchie et al., 1993; Kurzawa-Goertz et al., 1998; Wagner, 1981; Harris and Warshaw, 1993)</td>
      <td>1.6*</td>
      <td>1.6*</td>
      <td>49</td>
      <td>250*</td>
      <td>30*</td>
      <td>&lt;0.04</td>
    </tr>
  </tbody>
</table>

_*Rabbit striated muscle myosin-2.†Chicken cardiac muscle myosin-2.‡Calculated at 190 µM F-actin and saturating [ATP]._

The slow nucleotide binding and release kinetics of R788E suggest that the R788-mediated interaction at the converter/Nter/lever interface is allosterically communicated to the active site. This is in line with the observation that R788E does not show a nucleotide-induced change in the intrinsic tryptophan fluorescence signal during steady-state fluorescence measurements and transient-state kinetic assays (Figure 5D,F, Figure 4—figure supplement 1E, Table 3). The fluorescence change observed with NM2C is attributed to a conformation-induced change in the microenvironment of the conserved relay loop W525, which is in van der Waals distance to R788. W525 is generally regarded as a direct indicator for the switch-2 induced converter rotation (Malnasi-Csizmadia et al., 2001; Batra and Manstein, 1999).

![Figure 5.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig5-v2.jpg)

**Figure 5.:** (A) Relay helix angle as a function of MD simulation time, as monitored by the angle between Cα atoms of residues S489, M510, and E521 along the trajectories. The relay helix straightens in NM2C with a steady increase in the angle of the relay helix from approximately 145° to 150°, while the angle does not change significantly in R788E and fluctuates around 145° throughout the 100 ns time course of the simulation. Values for the relay helix angle observed in crystal structures of pre-power stroke (PPS) and post-rigor (PR) are indicated by dotted lines. (B) Population of hydrogen bonds (HB) between R788 (NM2C) or E788 (R788E) and surrounding structural elements over the simulation time of 100 ns. The abbreviations s and m indicate side chain and main chain. (C) Dynamics and conformational changes in NM2C during MD simulations. Snapshots from the start (0 ns simulation time) and end conformations (100 ns simulation time) are shown in light cyan and colored cartoon representation, respectively. The relay helix is shown in red, the SH1-SH2 helix in purple and the converter in grey. Relay loop W525 is shown in red in stick representation. The insets show a close-up view of the conformational changes of W525 along the simulation trajectory. (D) Tryptophan fluorescence emission spectrum of 4 µM NM2C in the absence of nucleotide or the presence of 0.5 mM ATP or 0.5 mM ADP. (E) Dynamics and conformational changes in R788E during MD simulations. Snapshots from the start (0 ns simulation time) and end conformations (100 ns simulation time) are shown in light cyan and colored cartoon representation, respectively. The relay helix is shown in red, the SH1-SH2 helix in purple and the converter in grey. Relay loop W525 is shown in red in stick representation. The insets show a close-up view of the conformational changes of W525 along the simulation trajectory. (F) Tryptophan fluorescence emission spectrum of 4 µM R788E in the absence of nucleotide or presence of 0.5 mM ATP or 0.5 mM ADP.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Monitored number of hydrogen bond (#HB) interactions between R261 (switch-1) and E483 (switch-2) along the simulation time of NM2C. (B) Monitored number of hydrogen bond (#HB) interactions between R261 (switch-1) and E483 (switch-2) along the simulation time of R788E (B). Hydrogen bonds were detected with cutoff values for the donor-acceptor distance and angle of 3.5 Å and 30°. Note the intermediate breaking of the salt-bridge in R788E (B). (C) Distance between main chain of G481 of switch-2 with the γ-phosphate of ATP during the 100 ns simulation time for NM2C. (D) Population of hydrogen bonds (HB) between structural elements of the active site of NM2C and ATP along the 100 ns simulation. The abbreviations s and m indicate side chain and main chain, respectively. (E) Population of hydrogen bonds (HB) between R788 (NM2C) or K788 (R788K) and surrounding structural elements along the simulation time. The abbreviations s and m indicate side chain and main chain, respectively. (F) Monitored number of hydrogen bond (#HB) interactions between R261 (switch-1) and E483 (switch-2) along the simulation trajectory of R788K. Simulations for NM2C, R788K, and R788E were performed in the presence of ATP in the active site.

Charge reversal mutations have been successfully used in in vitro and in vivo studies to probe for the influence of the converter/U50 kDa interface on myosin-2 performance (Ramanath et al., 2011; Bloemink et al., 2016; Kronert et al., 2015; Kronert et al., 2014). As expected, the structural consequences of the charge reversal mutation R788E are more severe than for the R788K mutant. R788K and R788E show prominent changes in virtually all parameters of the myosin and actomyosin ATPase cycle, again with more serious consequences occurring for R788E (Table 3). In summary, our steady-state and transient state kinetic analysis of NM2C, R788K, and R788E suggest that R788 is a key residue and is essential for allosteric communication pathway between the active site and the converter/Nter/lever interface.

### Allosteric communication pathway between the active site and the distal end of the motor domain

R788 is a hub amino acid and forms the center of a cluster of interactions that connect the converter, the SH1-SH2 helix, the relay helix, and the lever (Figure 3A,B). To understand its dynamic interactions that are allosterically communicated to the active site, we performed comparative MD simulations of NM2C, R788E, and R788K in explicit water with Mg2+∙ATP bound to the active site over a time of 100 ns. The co-crystallized ADP·VO4 was replaced by ATP since we found that the presence of ATP, while starting with the crystallized NM2C pre-power stroke structure, led to a straightening of the relay helix that connects the active site and the converter during our simulations. Likewise, the converter undergoes a 27° rotation that directs lever arm motion (Figure 5A,C). This straightening is solely caused by the exchange of the co-crystallized ADP·VO4 to ATP, since neither the replacement with ADP nor the absence of nucleotide led to relay straightening, converter rotation, or larger changes in the active site in control simulations. Therefore, the use of ATP in our simulations allowed us to analyze the effect of the R788E and R788K mutations during the dynamic initial converter rotation and relay straightening.

As expected, the characteristic salt bridge between switch-1 R261 and switch-2 E483 of the active site that is critical for the hydrolysis of ATP is stable throughout the time course of the simulation for NM2C (Figure 5—figure supplement 1A). Negligible shifts of the active site P-loop and switch-1 are detectable during the simulations, which correlate with a minor shift of the ATP. The nucleotide coordination is however unchanged except for an interaction of switch-2 peptide backbone of G481 with the γ-phosphate of ATP (Figure 5—figure supplement 1C,D). This critical interaction, used to define the closed and open states of switch-2, is lost along the MD simulations (Figure 5—figure supplement 1D). This loss of interaction is due to a 2 to 2.5 Å r.m.s.d. rearrangement of switch-2. The cation Mg2+ remains bound to the side chains of S260 and T205, as well as the α- and γ-phosphates of ATP within interaction distances around 2 Å. After 100 ns, the position of the converter and the adjacent lever show an orientation between the post-rigor and pre-powerstroke state, as compared to the crystal structures of Dictyostelium nonmuscle myosin-2 motor domain (PDB entries 1FMW, 2XEL) (Figure 5C). This intermediate state resembles the proposed initial phase of the see-saw mechanism for the recovery stroke of myosin (Koppole et al., 2007). The see-saw mechanism proposes a two-phase swinging of the lever arm, with an initial ∼25° rotation of the converter and lever arm, linked to the formation of a hydrogen bond between G457 and the γ-phosphate, and a second phase, featuring the remaining ∼40° rotation and the complete closing of switch-2. Our simulations appear to show the initial phase with a 27° rotation of the converter and lever arm along the trajectories, an initial rearrangement of switch-2 and the associated loss of the critical interaction between G481 (corresponds to G457 in Dictyostelium myosin-2) and the γ-phosphate of ATP. The important interactions between G481, A480 and N499 in the relay helix, which are suggested to transmit the see-saw information to the relay helix, are stable throughout the simulations. With the movement of the relay helix, the indole ring of relay loop W525 changes its conformation by 70–80°, which agrees with the experimentally observed nucleotide-induced change in the intrinsic tryptophan fluorescence signal in NM2C (Figure 5B,C, Figure 4—figure supplement 1E). The hub amino acid R788 is in transient interactions with main chain and side chain atoms of 10 amino acids of the SH1 helix and the converter during the 100 ns time course of the simulation (Figure 5B).

MD simulations for R788E indicate that all interdomain interactions between R788E of the converter and the SH1 helix are lost (Figure 5B). The straightening angle of the relay helix remains constant and abolishes a detectable converter rotation (Figure 5A,E). This allosteric decoupling at the distal end of the myosin motor domain is translated further upstream via the relay helix and results in a pronounced 6 Å conformational change of a loop that connects the γ-phosphate sensor switch-2 of the active site and the relay helix. As a consequence, the salt bridge between switch-2 E483 and switch-1 R261 appears less stable in the MD simulations of R788E as compared to NM2C (Figure 5—figure supplement 1A,B). The importance of the salt bridge between both switches for the ATP hydrolysis is established and expected to directly contribute to the experimentally observed impaired nucleotide binding, hydrolysis, and release kinetics of R788E in transient-state kinetic assays (Table 3, Figure 4A, Figure 4—figure supplement 1A,D) (Furch et al., 1999; Friedman et al., 1998; Ruppel and Spudich, 1996). Moreover, the side chain of switch-1 N256 changes its orientation, thereby impairing hydrogen bond interactions with the α- and β-phosphate moieties of the nucleotide and constrains of switch-1. The lack of coordinating interactions may be linked to the very slow nucleotide binding and release rate constants (Figure 4A, Figure 4—figure supplement 1A, Table 3).

The side chain of relay loop W525 does not undergo a conformational change throughout the time course of the simulation for R788E, supporting our experimental observation that mutant construct R788E does not exhibit a nucleotide-induced change in its intrinsic tryptophan fluorescence signal (Figure 5D,F, Figure 4—figure supplement 1E). The direct comparison of the dynamic interaction and conformational signatures of W525 in NM2C and R788E reveals that R788 is in van der Waals distance (5.4 Å) from relay loop W525 at the start of the simulations. W525 transiently interacts with I523 (18%) and Q519 (14%), changes its conformation by 70–80° and increases the distance to NM2C R788 to 7.3 Å after 100 ns simulation time. In comparison, the distance between W525 and E788 increases to 9.9 Å during the simulation for R788E. The lack of a conformational change in W525 along the simulation trajectory results in transient interactions with Q515 (55%) and Q730 (14%) instead of the interactions with I532 and Q519 as seen in NM2C.

MD simulations for R788K indicate that K788 forms transient interactions with 10 main chain and side chain atoms of the SH1 helix and the converter (Figure 5—figure supplement 1E). The interaction patters are similar but not identical to NM2C (Figure 5—figure supplement 1E). These subtle changes are allosterically propagated from the converter/Nter/lever interface at the distal end of the myosin motor domain via the relay helix to switch-2 of the active site. The salt bridge between switch-2 E483 and switch-1 R261 is not significantly populated after 10 ns simulation time (Figure 5—figure supplement 1F) and hydrogen bond interactions between switch-1 N256 and the α- and β-phosphate moieties of the nucleotide in R788K break along the simulation trajectory. The dynamic features in the R788K active site resemble those observed for R788E (Figure 5—figure supplement 1B,F) and underline that the precise coordination of R788 at the interface of converter, the SH1-SH2 helix, the relay helix, and the lever is pivotal for the allosteric communication in the NM2C motor domain.

In summary, our in silico and experimental in vitro data show that R788 is a distant allosteric modulator of switch-2 dynamics at the active site that impacts nucleotide binding and release kinetics in the actin-detached states. Moreover, our data support a model of R788 as a quencher of W525 fluorescence (Figure 5D,F, Figure 4—figure supplement 1E).

## Discussion

The experiments presented here collectively demonstrate an allosteric communication pathway from the distal end of the myosin motor domain that, together with substitutions of several key residues in or in vicinity to the active site, account for NM2C-specific kinetic properties. Disruption of the pathway by mutation of R788 to a glutamate causes the loss of its enzymatic signatures and results in a high duty ratio motor. Importantly, several key residues involved in the allosteric communication pathway are implicated in the onset and progression of debilitating human diseases (Fu et al., 2016; Donaudy et al., 2004; Kim et al., 2017). Missense mutation G376C is in proximity to residues C324 of helix J and R328 of the JK-loop (Figure 4—figure supplement 1F). Based on its location, we suggest that this substitution may interfere with the nucleotide binding and release kinetics from the NM2C active site. Missense mutation R726S is in the SH1-SH2 helix and the guanidinium group of the wild-type arginine interacts (3.3 Å) with the NM2C Nter. The serine residue is expected to disrupt this interaction because of the shorter side chain and different charge when compared to arginine. It is therefore likely that these mutations may impact the interaction of the motor domain with nucleotides, thereby contributing to impaired tension-sensing and maintenance of nonmuscle myosin-2C in the human cochlea (Fu et al., 2016; Donaudy et al., 2004; Kim et al., 2017).

### R788 is part of a conserved pathway that connects the active site and the converter

R788 is part of an allosteric communication pathway that connects the converter at the distal end of the myosin motor domain via the relay helix with switch-2 of the active site (Figure 5—figure supplement 1). At the active site, the reduced number of hydrogen bond interactions between P-loop, switch-1, and the Nter together with the reduced interconnectivity within the motor domain contribute to the low thermodynamic (KAD/KD) and kinetic (k-AD/k-D) coupling efficiency and the efficiency of F-actin to displace ADP and Pi during the catalytic cycle in NM2C and likely other nonmuscle and smooth muscle myosins-2 compared to cardiac and striated muscle myosins-2 (Table 2) (Risal et al., 2004). In summary, the discussed structural details contribute to the kinetic features of NM2C that are overall characterized by a slow steady-state ATPase activity and higher duty ratio compared to skeletal muscle myosins (Tables 3 and 4).

Partial uncoupling of the communication pathway by the conservative R788K mutation has a moderate impact on nucleotide binding and release kinetics (Table 3) in the myosin ATPase cycle compared to NM2C. Consequently, the overall kinetic features are similar to NM2C (Table 3). Complete uncoupling of the converter from the motor domain in R788E slows down all kinetic steps of the myosin ATPase cycle and decreases its actin-activation, due to altered switch-2 dynamics. The observed kinetic phenotype of the R788E myosin ATPase cycle is similar to the Dictyostelium nonmuscle myosin-2 non-hydrolyzer mutants in which the salt bridge between switch-1 and switch-2 is completely destroyed by mutagenesis and unable to form (Furch et al., 1999; Friedman et al., 1998). Non-hydrolyzer mutants are characterized by long-lived ATP states and reduced nucleotide release and binding kinetics, including a drastic decrease in k+AD (Furch et al., 1999; Friedman et al., 1998). Like R788E, Dictyostelium myosin-2 non-hydrolyzer mutants do not exhibit a nucleotide-induced change in the intrinsic fluorescence signal (Furch et al., 1999). It is of note that the lack of an intrinsic fluorescence signal in R788E is caused by the blockage of the communication pathway on the relay helix before or at Y518 (Figure 6A,B), whereas the impairment of the nucleotide switches to form a salt bridge and the resulting lack of the switch-2-induced conformational change of the relay helix is the expected cause in the non-hydrolyzer mutants.

![Figure 6.](https://cdn.elifesciences.org/articles/32742/elife-32742-fig6-v2.jpg)

**Figure 6.:** (A) Residue R788 connects the converter to the SH1 interface through main chain and side chain interactions in NM2C. This interface further interacts with Y518 of the relay helix and W525. The interactions are propagated to the active site and vice versa through the relay helix and through an interaction of relay helix residue N499 with the main chain of G481 from switch-2. The latter directly interacts with the nucleotide. Y599 of the wedge loop, that itself contacts the relay helix, establishes an interaction with switch-2 F482. This residue is in contact with S200 of the P-loop by main chain interactions and directly interacts with the nucleotide in the active site. Schematic not drawn to scale. (B) The interface between R788E and both, the SH1 and the relay helix, is perturbed and the allosteric communication from the active site to the converter compromised. The experimental observation that R788E does not change its intrinsic fluorescence upon nucleotide binding which is caused by a lacking conformational change of W525 indicates that the communication pathway is interrupted in the relay helix. The position of W525 in the relay loop at the distal end of the relay helix indicates that the pathway is interrupted before or at Y518, which is supported by the observation that the relay loop does not change its position during the time course of the MD simulation. As a consequence, Y518 cannot establish an interface with E788 and F732 of the converter and SH1 helix. Further, E788 cannot establish interactions with N776 and V791 and completely disrupts the structural integrity of the interface of converter, SH1-SH2 helix, relay helix and the lever arm and uncouples nucleotide-induced changes in the active site from the converter rotation. Only key residues involved are shown in the proposed mechanism. Small grey boxes indicate main chain interactions. Schematic not drawn to scale.

F-Actin affinities are largely unaffected by the R788E mutation, which is in line with the observation that switch-1 dynamics are only marginally affected in comparative MD simulations. The presence of F-actin however establishes ATP/ADP selectivity in the actomyosin ATPase cycle: ActoNM2C preferentially binds ADP over ATP, whereas actoR788E preferentially binds ATP over ADP (Table 3). The ATP selectivity is caused by an 85-fold decreased second-order ADP-binding rate constant k+AD, a key signature of R788E actomyosin ATPase cycle. ATP/ADP selectivity is established by actin-induced conformational changes in the myosin motor domain and underlines that the coupling mechanism from the active site to the converter and vice versa is different in the presence and absence of F-actin. This observation is in line with recent reports on distinct pathways for the myosin and actin-activated ATPase cycle (Llinas et al., 2015).

### Implications for NM2C function in vivo

Nonmuscle myosin-2C assembles into small bipolar filaments that dynamically tether actin filaments in cells (Ebrahim et al., 2013; Billington et al., 2013). The actomyosin interaction and hence the tension exerted by a sarcomeric array of nonmuscle myosin-2C is of importance for the function and organization of the apical junctional complex in the organ of Corti and actin-rich structures including stress fibers and actin arcs (Ebrahim et al., 2013).

Based on our kinetic data, the calculated duty ratio of NM2C suggests that ~14 motor domains would be needed to be geometrically capable of interacting with F-actin at any given time. This number is identical to the number of motor domains per nonmuscle myosin-2C half filament, suggesting that the filament may be at the threshold of being processive in the absence of external loads (Billington et al., 2013). It is likely that this threshold is crossed in the presence of other actin binding proteins, intermolecular loads, and gating between the F-actin bound motor domains (Hundt et al., 2016).

The structural prerequisites underlying gating and load-sensitivity in nonmuscle myosins-2 have not been investigated but include a distortion at the converter/lever or the converter/motor domain interface in the nanometer range that is allosterically communicated through the lever arm via the converter to the active site (Kovács et al., 2007). Resisting load applied to the lever slows down the actin-activated ADP release from the lead motor of nonmuscle myosin-2A around fivefold thereby increasing the duty ratio, but does not alter the rate of ATP binding (Hundt et al., 2016; Kovács et al., 2007). The kinetic signatures of the strained nonmuscle myosin-2A lead motor are very similar to the observed kinetic features of R788E. The reduction of the steady-state ATPase of R788E and the concomitant increase in duty ratio and a rate-limiting ADP release rate goes in line with this finding. We propose that internal strain in the nonmuscle myosin-2 dimer distorts the lead motor at the converter/lever interface and leads to its axial translation as seen in electron microscopic studies (Burgess et al., 2002). This translation abolishes the interaction of the converter R788 with residues of the SH1-SH2 helix and the relay helix, thereby uncoupling the myosin subdomains and disrupting the communication pathway from the converter to the active site, which is expected to result in a similar kinetic effect as in R788E. Consequently, a motor in a nonmuscle myosin-2 filament would decrease its enzymatic activity and stay strongly bound to F-actin. This feature is required to generate processivity and cytoskeletal tension and of physiological significance in the maintenance of cell shape and tensional homeostasis in the actin cytoskeleton.

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
      <td>Cell line (Spodoptera frugiperda)</td>
      <td>Sf9</td>
      <td>Thermo Fisher Scientific</td>
      <td>Thermo Fisher Scientific 11496015</td>
      <td>Maintained in Sf-900 III SFM</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pFastBac1-NMHC- 2C0-2R-His8</td>
      <td>PMID: 21478157</td>
      <td>N/A</td>
      <td>Progenitors: sequence optimized 1–799 human nonmuscle myosin-2C (GenBank accession number NP_079005) directly fused to spectrin repeats 1 and 2 from Dictyostelium discoideum alpha-actinin; vector pFastBac1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pFastBac1-NMHC- 2C0-2R-Flag</td>
      <td>this paper</td>
      <td>NM2C (kinetic studies)</td>
      <td>Progenitor: pFastBac1-NMHC-2C0-2R-His8</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pFastBac1-NMHC (45-799) −2C0-2R-His8</td>
      <td>this paper</td>
      <td>NM2C (crystal structure)</td>
      <td>Progenitor: pFastBac1-NMHC-2C0-2R-His8</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pFastBac1-NMHC (R788K) −2C0-2R-Flag</td>
      <td>this paper</td>
      <td>R788K (kinetic studies)</td>
      <td>Progenitor: pFastBac1-NMHC-2C0-2R-Flag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pFastBac1-NMHC (R788E) −2C0-2R-Flag</td>
      <td>this paper</td>
      <td>R788E (kinetic studies)</td>
      <td>Progenitor: pFastBac1-NMHC-2C0-2R-Flag</td>
    </tr>
  </tbody>
</table>

### Protein production

For structural studies, a His8-tagged human NM2C construct comprising amino acids 45–799 directly fused to spectrin repeats 1 and 2 from α-actinin was generated based on the vector pFastBac1-NMHC-2C0-2R-His8 (Heissler and Manstein, 2011). Mutagenesis was accomplished by sequence-specific deletion using a whole-plasmid amplification approach. For kinetic studies, an equivalent motor domain construct comprising amino acids 1–799 of NM2C was cloned into a modified pFastBac1 vector containing a cDNA sequence encoding a C-terminal Flag-tag (Figure 1—figure supplement 1B). This construct was used as a template to introduce the R788E and R788K mutation by In-Fusion cloning (Clontech, Mountain View, CA 94943, USA). All proteins were recombinantly overproduced in the Sf9/baculovirus system, purified to electrophoretic homogeneity, and concentrated to ~10 mg/ml using Vivaspin ultrafiltration units (Sartorius, Göttingen, Germany) as previously described (Heissler and Manstein, 2011; Heissler et al., 2015). Throughout this manuscript, numbering refers to the amino acid sequence of full-length nonmuscle myosin-2C (GenBank accession number NP_079005).

### Crystallization of NM2C

NM2C at a concentration of ~10 mg/ml was complexed with the ATP analogue ADP⋅VO4 and crystallized using the hanging drop vapor diffusion method by mixing 2 μl of protein solution with 2 μl of reservoir solution containing 50 mM Tris pH 8.2, 10% (w/v) PEG-5K MME, 1% (v/v) MPD, and 0.2 M NaCl at 8°C. Rectangular plate shaped crystals grew up to 400 × 300×400 μm3 within 4 weeks. Crystals were soaked in the corresponding mother liquor supplemented with 100 mM NaCl and 20% (w/v) ethylene glycol. Protein crystals were transferred in serial steps of increasing concentrations of the cryo-solution. Crystals were transferred into liquid nitrogen using MiTeGen loops and stored at 100 K until data collection.

### Data collection, processing, and refinement

X-ray diffraction data of NM2C crystals were collected at the beam line BL14.1 at Bessy II (Helmholtz-Zentrum, Berlin, Germany) to 2.25 Å resolution (Table 1). Data processing was performed using XDS and SADABS (Blessing, 1995). The structure of NM2C in the pre-powerstroke state was solved by molecular replacement using Phaser (McCoy, 2007). The crystal structure of the chicken smooth muscle myosin-2 motor domain (PDB entry 1BR4) was used as a search model and the two α-actinin repeats were manually traced and rebuilt. The electron density map was sharpened using Coot (Emsley and Cowtan, 2004) to ensure the directionality and identity of the α-helices for the two α-actinin repeats. Maximum likelihood crystallographic refinement was performed using iterative refinement cycles in autoBUSTER (Bricogne et al., 2011). Iterative cycles of model building were performed using Coot, and model bias was minimized by building into composite omit maps. The model was initially validated in Coot and final validation was performed using MolProbity (Davis et al., 2004).

### Kinetic experiments

The actin-activated ATPase assays under steady-state conditions were performed as described earlier in buffer containing 10 mM MOPS pH 7.0, 50 mM NaCl, 2 mM MgCl2, 2 mM ATP, 0.15 mM EGTA, 40 U/ml l-lactic dehydrogenase, 200 U/ml pyruvate kinase, 200 μM NADH, and 1 mM phosphoenolpyruvate at 25°C with a Cary 60 Bio spectrophotometer (Agilent Technologies, Wilmington, DE) (Heissler et al., 2015). Transient state kinetic assays were carried out as described previously with a TgK Hi-tech Scientific SF-61 DX stopped-flow system (TgK Hi-tech Scientific Ltd., Bradford-on-Avon, UK) in SF-buffer (25 mM MOPS pH 7.0, 100 mM KCl, 5 mM MgCl2 and 0.1 mM EGTA) unless stated otherwise (Heissler and Manstein, 2011). Initial data fitting was performed with Kinetic Studio Version 2.28 (TgK Hi-tech Scientific Ltd., Bradford-on-Avon, UK). Plots were generated with OriginPro 8.5 (OriginLab Corp., Northampton, MA). Data interpretation is according to the kinetic scheme of the myosin and actomyosin ATPase cycle as presented in Figure 1—figure supplement 1A.

### Fluorescence measurements

Tryptophan fluorescence emission spectra of 4 µM NM2C or R788E in the presence and absence of 0.5 mM ADP and 0.5 mM ATP, respectively, were measured after excitation at 297 nm at a temperature of 20°C in a QuantaMaster fluorescence spectrophotometer (Photon Technology International, Birmingham, NJ) as described previously (Málnási-Csizmadia et al., 2007). Prior to the assay, proteins were transferred to SF-buffer with zebra spin desalting columns (Thermo Fisher Scientific GmbH, Dreieich, Germany). The fluorescence was normalized to the maximum fluorescence of NM2C or R788E in the absence of nucleotide.

### Molecular dynamics simulations

Molecular dynamics based in silico site directed mutagenesis and simulations were performed using NAMD 2.9 and the CHARMM27 force field (MacKerell et al., 1998; Phillips et al., 2005). The X-ray crystal structure of the NM2C motor domain in the pre-powerstroke state, encompassing residues 49–807, served as the starting structure for NM2C, R788K, and R788E simulations. Mutations were introduced in silico and the proteins were prepared and optimized prior to MD simulations using the Protein Preparation Wizard of the Schrödinger software suite (Schrödinger Suite 2012 Protein Preparation Wizard; Epik version 2.3; Impact version 5.8; Prime version 3.1; Maestro version 9.3. Schrödinger LLC, New York, NY). The proteins were fully hydrated with explicit solvent using the TIP3P water model and charge neutralization was accomplished by adding Na+ counter ions (Jorgensen et al., 1983). Simulations for NM2C, R788K, and R788E were performed in the presence of ATP in the active site. Short-range cutoffs of 12 Å were used for the treatment of non-bonded interactions; while long-range electrostatics was treated with the particle-mesh Ewald method (Darden and Pedersen, 1993). All simulations were carried out in an NpT ensemble at 310 K and 1 atm using Langevin dynamics and the Langevin piston method. A 1 fs time step was applied. Prior to production runs the solvated systems were subjected to an initial energy minimization and subsequent equilibration of the entire system for 5 to 10 ns. All MD simulations were carried out at the Computer Cluster of the Norddeutscher Verbund für Hoch- und Höchstleistungsrechnen.
