# Molecular insights into RNA and DNA helicase evolution from the determinants of specificity for a DEAD-box RNA helicase

## Authors

- Anna L Mallam<sup>1</sup>
- David J Sidote<sup>1</sup>
- Alan M Lambowitz<sup>1</sup> †

### Affiliations

1. Institute for Cellular and Molecular Biology University of Texas at Austin Austin United States
2. Department of Molecular Biosciences University of Texas at Austin Austin United States

† Corresponding author

## Abstract

How different helicase families with a conserved catalytic ‘helicase core’ evolved to function on varied RNA and DNA substrates by diverse mechanisms remains unclear. In this study, we used Mss116, a yeast DEAD-box protein that utilizes ATP to locally unwind dsRNA, to investigate helicase specificity and mechanism. Our results define the molecular basis for the substrate specificity of a DEAD-box protein. Additionally, they show that Mss116 has ambiguous substrate-binding properties and interacts with all four NTPs and both RNA and DNA. The efficiency of unwinding correlates with the stability of the ‘closed-state’ helicase core, a complex with nucleotide and nucleic acid that forms as duplexes are unwound. Crystal structures reveal that core stability is modulated by family-specific interactions that favor certain substrates. This suggests how present-day helicases diversified from an ancestral core with broad specificity by retaining core closure as a common catalytic mechanism while optimizing substrate-binding interactions for different cellular functions.

## Introduction

Helicases of superfamilies (SFs) 1 and 2 use ATP or other NTPs to bind, unwind, or remodel RNA or DNA in essentially all facets of nucleic acid metabolism (Preugschat et al., 1996; Tanaka and Schwer, 2005; Singleton et al., 2007; Fairman-Williams et al., 2010; Jarmoskaite and Russell, 2014). They contain a conserved ‘helicase core’ of two RecA-like domains but act on varied substrates by different mechanisms. SF1 and SF2 helicases can be grouped into families with distinct variations in specificity, mechanism, function, and appended domains (Figure 1A) (Gorbalenya and Koonin, 1993; Singleton et al., 2007; Fairman-Williams et al., 2010). The mechanisms by which SF1 and SF2 helicases act on RNA or DNA include non-processive unwinding of short duplexes (e.g., DEAD-box RNA helicases [Jarmoskaite and Russell, 2011; Linder and Jankowsky, 2011]), unwinding coupled to directional movement (‘translocation’) along the unwound single strand (e.g., DEAH/RHA, NS3/NPH-II, and RecQ-like helicases [Pyle, 2008]), and binding or translocation along a duplex without unwinding (e.g., RIG-I-like and Swi/Snf helicases [Durr et al., 2005; Myong et al., 2009; Rawling and Pyle, 2014]) (Figure 1A). How helicases that share a conserved catalytic core evolved such functional diversity remains unknown.

![Figure 1.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig1-v2.jpg)

**Figure 1.:** (A) Domain architecture and characteristics of helicases belonging to different SF1 and SF2 families (Fairman-Williams et al., 2010). Two other SF1 (Pif1-like and Upf1-like) and four other SF2 (Ski2-like; RecG-like; T1R; and Rad3/XPD) families have been identified (Fairman-Williams et al., 2010). Helicase core domains 1 and 2 are colored light blue and green, respectively, while appended domains and insertions, which vary in size, composition, and function, are colored orange; domains are not to scale. (B) Schematic of the domain architecture of the helicase core of Mss116 (D1, blue; D2, green; C-terminal extension of D2 [CTE], orange) showing the location of conserved DEAD-box sequence motifs (Fairman-Williams et al., 2010). Full-length Mss116 contains additional unstructured N-terminal (residues 37–87) and C-terminal (residues 598–664) extensions that are not required for helicase activity (Cao et al., 2011; Mohr et al., 2011). (C) Structure of the closed-state helicase core of Mss116 (PDB accession 3I5X) (Del Campo and Lambowitz, 2009) bound to ssRNA (U10-RNA; yellow) and adenosine nucleotide (AMP-PNP; black). (D) Model for RNA duplex binding and unwinding by Mss116. The helicase core domains of Mss116 have modular roles in substrate loading (Mallam et al., 2012). D1 captures ATP in the open-state enzyme using the Q-motif, which coordinates the adenine base, and motifs I and II, which are the conserved triphosphate-binding loop and Mg2+-binding aspartic acid motifs, respectively, present in many other ATP-binding enzymes (Walker et al., 1982; Rudolph et al., 2006; Schutz et al., 2010; Mallam et al., 2012). D2 recognizes duplex RNA (Mallam et al., 2012). When ATP and dsRNA are bound to D1 and D2, respectively, core closure occurs, leading to unwinding of the dsRNA bound to D2 by bending one RNA strand and displacing the other. During unwinding and formation of the closed-state helicase core complex, ATP bound to D1 makes additional interactions with motifs Va and VI in D2. The closed-state helicase core bound to ssRNA and ATP represents the ‘post-unwound’ state of the enzyme (Figure 1C). ATP hydrolysis occurs in the closed state, followed by dissociation of Pi and ADP, which leads to the reopening of the core and the release of the bound ssRNA, thereby regenerating the enzyme (Henn et al., 2010; Cao et al., 2011).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Examples are taken from the helicase families shown in Figure 1A. Most are in complex with nucleic acid (yellow) and domains are colored as in Figure 1A. The composition and PDB accession code are given for each structure.

Here, we use the yeast DEAD-box protein Mss116 (Figure 1B,C) as a model system to pinpoint the molecular basis for the specificity and mechanism of the conserved helicase core. Mss116 functions as a general RNA chaperone in mitochondrial intron splicing by locally unwinding and disrupting stable but inactive RNA structures that impede RNA folding (Huang et al., 2005; Del Campo et al., 2009; Potratz et al., 2011). As a general RNA chaperone, Mss116 binds diverse RNA substrates non-specifically and has high RNA helicase activity in the absence of partner proteins (Halls et al., 2007; Del Campo et al., 2009). This makes it an ideal model system to study the properties of an isolated helicase core. The helicase core of Mss116 consists of two RecA-like domains (D1 and D2) that are in an extended ‘open state’ in the absence of substrates (Mallam et al., 2011) and recognize ATP and duplex RNA in a modular manner (Mallam et al., 2012) (Figure 1D). Upon substrate binding, the two core domains join to form a ‘closed state’ containing an ATPase active site, while conserved DEAD-box protein motifs in D1 promote the unwinding of short duplexes bound to D2 by excluding one RNA strand and bending the other (Figure 1D). The closed-state complex bound to ssRNA and ATP represents the ‘post-unwound’ state of the helicase core (Figure 1C). ATP hydrolysis is required for core reopening and enzyme turnover (Liu et al., 2008; Cao et al., 2011).

In this study, we determined the structural and biochemical factors that govern how analogues of NTPs (ATP, CTP, GTP, and UTP) and different nucleic acids (single-stranded [ss] RNA, ssDNA, double-stranded [ds] RNA, A-form dsDNA, and B-form dsDNA) interact with the helicase core. In this way, we identify the core–substrate interactions that dictate the physiological specificity and mechanism of Mss116. Our results define the structural and biochemical determinants for the substrate specificity of a DEAD-box protein. Furthermore, they demonstrate that Mss116 has surprisingly ambiguous substrate binding and unwinding properties. Considered in the context of other SF1 and SF2 helicases, our findings show how small structural changes within conserved regions of these protein families can facilitate the emergence of specialized enzymes with new activities and cellular functions.

## Results

### The biochemical basis for the ATP specificity of the helicase core of Mss116

We investigated how Mss116 specifies for ATP during local unwinding by comparing the ability of the helicase core (D1D2, residues 88–597) to use different nucleotides to catalyze RNA unwinding. First, we measured the concentration of different NTP analogues required by the helicase core to unwind an RNA duplex under equilibrium conditions (Figure 2A). This was done by using a 12-base pair (bp) dsRNA, which was labeled with a fluorophore and quencher at its 5′ and 3′ ends, respectively. A native gel-based assay was then used to monitor unwinding by the increase in fluorescence in a closed-state core containing a bound single strand (Figure 2—figure supplement 1). We find that all of the non-hydrolyzable analogues NDP-BeFx, where N = A, C, G, or U, can promote the unwinding of a dsRNA. However, ADP-BeFx is the most efficient with at least sixfold higher concentrations of C-, G-, or U-analogues required for RNA duplex unwinding (K1/2 = 0.14, 0.8, 0.8, and 2.4 mM, respectively; Figure 2A and Figure 2—figure supplement 1B–E).

![Figure 2.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig2-v2.jpg)

**Figure 2.:** (A) dsRNA unwinding by the MBP-tagged helicase core measured under equilibrium conditions using a gel-based fluorescence assay to monitor the formation of a closed-state complex containing bound ssRNA at increasing concentrations of NDP-BeFx, N = A, C, G, or U (Figure 2—figure supplement 1). The fraction of unwound duplex was obtained by normalizing the band intensities separately for each gel using the parameters from the fit to a one-site binding model, as the change in fluorescence upon unwinding is different under each condition. The extent of unwinding with UDP-BeFx was less than that for the other nucleotide analogs, and the maximum concentration of UDP-BeFx used in this assay was insufficient to drive unwinding to completion (Figure 2—figure supplement 1). This could be because UDP-BeFx bound at saturating concentrations to D1 cannot efficiently induce a closed state. (B) Equilibrium binding of A10-RNA to the MBP-tagged helicase core determined by fluorescence anisotropy measurements at increasing concentrations of NDP-BeFx, N = A, C, G, or U. (C) Equilibrium binding of A10-RNA to the MBP-tagged helicase core determined as in (B) at increasing concentrations of ADP-BeFx, AMP-PNP, ADP, and ADP + Pi. Error bars in (A–C) represent the standard error for at least three independent measurements, and the error in the K1/2 or Kd represents the standard error of the non-linear regression. NB, no appreciable binding. In (B and C), the fraction of A10-RNA bound was calculated by normalizing against the anisotropy signal for unbound and fully bound substrate obtained from the fit to a one-site binding model. (D) Normalized SEC profiles monitored by absorbance at 260 nm (red) and 280 nm (black) for the helicase core in the absence of all substrates and in the presence of A10-RNA + NDP-BeFx, N = A, C, G, or U. An A260/A280 >1 at the maximum absorbance indicates the formation of a closed-state complex.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Schematic representation of the equilibrium unwinding reaction measured in this assay. Unwinding was probed by using a 12-bp dsRNA substrate labeled with a fluorophore (6-carboxyfluorescein; FAM) and quencher (Iowa Black FQ; IBFQ) probes at the 5′ and 3′ ends, respectively. An increase in fluorescence of this substrate occurs when the helicase core unwinds the dsRNA and forms a closed-state bound to ssRNA. (B–E) Representative unwinding assays for dsRNA (100 nM) by the helicase core of Mss116 (2 μM) measured at increasing concentrations of NDP-BeFx with N = A, C, G, and U for B–E, respectively. Samples were loaded in the reaction medium and resolved in a non-denaturing 6% polyacrylamide gel run at 4°C in 0.5× Tris/Borate/EDTA buffer (pH 8.3). Arrows mark complexes corresponding to the open- (in the absence of NDP-BeFx) and closed-state protein bound to RNA. Proteins have an N-terminal MBP tag to increase solubility under the EMSA conditions. The double band seen in some lanes could be the result of one or two protein molecules bound to a partially unwound duplex or to a closed-state with or without a partially unwound second strand. (F) Control unwinding assay using an equivalent 12-bp 5′ FAM-dsRNA with no quencher to demonstrate that, under the assay conditions, the RNA is always bound to the helicase core and widely separated from free substrate.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Schematic representation of the unwinding reaction measured in this assay. Unwinding was probed by using a 12-bp dsRNA substrate labeled with a fluorophore (6-carboxyfluorescein; FAM) and quencher (Iowa Black FQ; IBFQ) probes at the 5′ and 3′ ends, respectively (IDT). An increase in fluorescence of this substrate occurs upon unwinding and re-annealing to an unlabeled strand from a duplex of the same sequence that is present in excess. (B) Representative unwinding time course for labeled dsRNA (125 nM) by the helicase core of Mss116 (2 μM) measured at 5 mM ATP-Mg2+. After the addition of stop buffer to remove any bound protein, duplex samples were resolved in a non-denaturing 20% polyacrylamide gel run at 4°C in 1× Tris/Borate/EDTA buffer (pH 8.3). (C) Representative unwinding time course for labeled dsRNA (125 nM) by the helicase core of Mss116 (2 μM) measured at 5 mM CTP-Mg2+ with samples resolved as in (B). The last lane represents the same duplex unwound by ATP after 60 min. (D) Kinetic unwinding profiles of dsRNA by Mss116 for NTP, N = A, C, G, or U. Error bars represent the standard error for at least three independent measurements, and the error in k1 represents the standard error of the non-linear regression. NU, no appreciable unwinding. Unwinding data for ATP were normalized using the parameters obtained from the fit to a first-order reaction with a single exponential. In the case of other nucleoside triphosphates where no unwinding was observed, data were normalized against the signal for a duplex fully unwound by ATP at the same concentration (see panel C, final lane). Assays were performed in a buffer containing 5 mM free Mg2+. Additional assays were performed at 0.5 mM Mg2+, as previous data indicate that the unwinding activity of Mss116 increases at lower Mg2+ concentrations (Halls et al., 2007). These gave similar results.

Kinetic unwinding assays were also performed using the same dye-labeled dsRNA in the presence of an unlabeled duplex. In these experiments, an increase in fluorescence occurs upon unwinding of a labeled duplex and subsequent re-annealing to an unlabeled strand. This was measured by isolating the duplexes using native gel electrophoresis at various times after unwinding was initiated by the addition of NTP, where N = A, C, G, or U (Figure 2—figure supplement 2). These assays show that only ATP, and not other NTPs, catalyzes the unwinding of the dsRNA (Figure 2—figure supplement 2B–D). This indicates that under our assay conditions, the diphosphate beryllium fluoride analogue is necessary to promote unwinding with nucleotide bases other than adenine. This difference likely reflects that the NDP-BeFx analogues form longer-lived, more stable complexes with RNA than do the corresponding NTPs (Liu et al., 2014).

We next examined how the stability of the ternary closed-state complex with ssRNA and the same NTP analogues correlates with the efficiency of duplex unwinding. Equilibrium fluorescence anisotropy binding assays with a fluorescein (FAM)-labeled A10-RNA were used to monitor formation of the closed state with increasing concentrations of NDP-BeFx (N = A, C, G, or U; Figure 2B). These assays show that the closed-state complex is most stable with ADP-BeFx (Kd = 0.022 mM), while CDP-BeFx, GDP-BeFx, and UDP-BeFx promote formation of the closed state only at significantly higher concentrations of nucleotide analogue (Kd = 0.09, 0.11, and 0.63 mM, respectively). Similarly, analytical size-exclusion chromatography (SEC) shows that a closed-state helicase core with A10-RNA is maintained during elution for complexes containing ADP-BeFx, CDP-BeFx, or GDP-BeFx but not those containing UDP-BeFx, consistent with the latter complex having a lower stability (Figure 2D and Table 1). Together, these findings indicate that the unwinding efficiencies and closed-state core stabilities with different NTP analogues follow the same order of A > C, G > U from higher to lower efficiency and stability.

**Table 1.**
 Size exclusion chromatography analysis of the helicase core of Mss116


<table>
  <thead>
    <tr>
      <th>Sample</th>
      <th>Elution volume at maximum absorbance/ml</th>
      <th>A260/A280 of peak at maximum absorbance</th>
      <th>Likely predominant state of core</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Free protein</td>
    </tr>
    <tr>
      <td>D1D2 (Mss116 helicase core)</td>
      <td>11.4</td>
      <td>0.6</td>
      <td>Open</td>
    </tr>
    <tr>
      <td colspan="4">Free nucleic acid</td>
    </tr>
    <tr>
      <td>dsRNA</td>
      <td>16.3</td>
      <td>2.1</td>
      <td>−</td>
    </tr>
    <tr>
      <td>A-DNA duplex</td>
      <td>15.1</td>
      <td>1.6</td>
      <td>−</td>
    </tr>
    <tr>
      <td>B-DNA duplex</td>
      <td>15.3</td>
      <td>1.9</td>
      <td>−</td>
    </tr>
    <tr>
      <td>A10-RNA</td>
      <td>18.6</td>
      <td>3.0</td>
      <td>−</td>
    </tr>
    <tr>
      <td>A10-DNA</td>
      <td>16.6</td>
      <td>3.4</td>
      <td>−</td>
    </tr>
    <tr>
      <td colspan="4">Protein–RNA–nucleotide complexes*</td>
    </tr>
    <tr>
      <td>D1D2–dsRNA–ADP-BeFx</td>
      <td>9.6</td>
      <td>1.1</td>
      <td>Closed</td>
    </tr>
    <tr>
      <td>D1D2–A-DNA-duplex–ADP-BeFx</td>
      <td>9.6</td>
      <td>1.2</td>
      <td>Closed</td>
    </tr>
    <tr>
      <td>D1D2–B-DNA-duplex–ADP-BeFx</td>
      <td>11.4</td>
      <td>0.6</td>
      <td>Open</td>
    </tr>
    <tr>
      <td>D1D2–A10-RNA–ADP-BeFx</td>
      <td>11.0</td>
      <td>2.2</td>
      <td>Closed</td>
    </tr>
    <tr>
      <td>D1D2–A10-RNA–CDP-BeFx</td>
      <td>11.1</td>
      <td>2.2</td>
      <td>Closed</td>
    </tr>
    <tr>
      <td>D1D2–A10-RNA–GDP-BeFx</td>
      <td>11.2</td>
      <td>2.3</td>
      <td>Closed</td>
    </tr>
    <tr>
      <td>D1D2–A10-RNA–UDP-BeFx</td>
      <td>11.4</td>
      <td>1.0</td>
      <td>Open</td>
    </tr>
    <tr>
      <td>D1D2–A10-DNA–ADP-BeFx</td>
      <td>11.4</td>
      <td>0.6</td>
      <td>Open</td>
    </tr>
  </tbody>
</table>

_*Parameters are quoted for the peak containing protein as determined by A214._

Additional fluorescence anisotropy assays show that a closed-state complex with A10-RNA forms at significantly lower concentrations of ADP-BeFx compared to AMP-PNP (Kd = 0.022 and 0.12 mM, respectively; Figure 2C). This indicates a more stable closed state and accounts for the higher unwinding activity observed for ADP-BeFx compared to AMP-PNP for several DEAD-box proteins (Liu et al., 2008). Further, neither ADP nor ADP + Pi in large excess led to the formation of a stable closed state in our assays (Figure 2C), suggesting that the effective concentration of the ATP γ-phosphate is critical for the stability of the closed-state. This finding explains energetically why ATP hydrolysis leads to core re-opening and enzyme turnover in DEAD-box proteins (Henn et al., 2010; Cao et al., 2011) and perhaps other SF1 and SF2 helicases. Together, our results show the unwinding efficiency of Mss116 with different nucleotides is directly correlated with the stability of the post-unwound closed-state complex.

### The structural basis for the ATP specificity of the helicase core of Mss116

To investigate the structural basis for the difference in stability of the closed state with different NTP analogs, we determined crystal structures of the closed-state helicase core with A10-RNA and either ADP-BeFx, CDP-BeFx, GDP-BeFx, or UDP-BeFx at 2.2, 2.7, 2.4, and 3.2 Å resolution, respectively (Figure 3 and Table 2). These structures show that the ATP-binding motifs I and VI make similar direct contacts to the phosphate groups of all four NTP analogs (Figure 3C). Motif II (DEAD) is positioned identically in all structures and interacts indirectly via waters with the BeF3 moiety, which corresponds to the ATP γ-phosphate (Figure 3B). However, each base interacts differently in the ATP-binding pocket. The purine bases (A and G) are stacked optimally with F126 in the Q-motif, which primarily confers ATP specificity in DEAD-box proteins (Linder and Jankowsky, 2011), whereas the pyrimidine bases (C and U) adopt a less favorable stacking orientation with this residue (Figure 3B). Also, fewer direct contacts are made to the C, G, and U bases than to A (Figure 3C). In particular, compared to the closed-state structure with ADP-BeFx, two hydrogen (H)-bonds from G128 and Q133 in the Q-motif to the base are absent in the complex with GDP-BeFx, and all of the direct interactions of the Q-motif with the base are missing in the structures with CDP- or UDP-BeFx. The fewer contacts of all other bases relative to adenine and the less favorable stacking of pyrimidine bases in the ATP-binding pocket explain the relative stabilities of the closed-state complexes and reveal how the helicase core of Mss116 adapted to unwind RNA most efficiently using ATP.

![Figure 3.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig3-v2.jpg)

**Figure 3.:** (A) Crystal structures of the closed-state helicase core of Mss116 bound to ssRNA and different nucleotide analogues (D1D2–A10-RNA–NDP-BeFx for N = A, C, G, or U). Structures are colored according to the scheme in Figure 1C. (B) Comparisons of the protein–substrate interactions in the NDP-BeFx binding pockets of the structures shown in (A). Side chains that make direct contacts with the NDP are shown as ball and stick models. A 2Fo − Fc electron density map contoured at 1.0 σ for the NDP-BeFx ligand is shown in gray. Mg2+ ions and water molecules are shown as green and red spheres, respectively, and the atoms of BeF3 are shown in purple (Be) and yellow (F). Motif II (‘DEAD’) makes indirect contacts via water molecules to the BeF3 moiety, which corresponds to the γ-phosphate of ATP. (C) Schematics of direct NDP–protein interactions for the structures shown in (A). See also Table 2.

**Table 2.**
 Crystallographic data and refinement statistics


<table>
  <thead>
    <tr>
      <th>Complex</th>
      <th>D1D2–A10-RNA–ADP-BeFx</th>
      <th>D1D2–A10-RNA–CDP-BeFx</th>
      <th>D1D2–A10-RNA–GDP-BeFx</th>
      <th>D1D2–A10-RNA–UDP-BeFx</th>
      <th>D1D2–A10-DNA–ADP-BeFx</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="6">Data collection</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P21212</td>
      <td>P21212</td>
      <td>P21212</td>
      <td>P21212</td>
      <td>P21212</td>
    </tr>
    <tr>
      <td colspan="6">Unit cell</td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>89.83, 126.26, 55.55</td>
      <td>89.64, 126.84, 55.03</td>
      <td>89.99, 126.61, 55.55</td>
      <td>89.76, 126.51, 55.51</td>
      <td>90.39, 126.19, 55.23</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <td>Total reflections</td>
      <td>222,375</td>
      <td>129,478</td>
      <td>565,729</td>
      <td>86,580</td>
      <td></td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>32,642</td>
      <td>16,982</td>
      <td>27,148</td>
      <td>10,514</td>
      <td>13,111</td>
    </tr>
    <tr>
      <td>Resolution* (Å)</td>
      <td>50 − 2.20 (2.24 − 2.20)</td>
      <td>50 − 2.60 (2.64 − 2.60)</td>
      <td>50 − 2.35 (2.39 − 2.35)</td>
      <td>50 − 3.30 (3.36 − 3.30)</td>
      <td>50 − 3.00 (3.05 − 3.00)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>6.8 (5.4)</td>
      <td>6.1 (5.4)</td>
      <td>19.2 (14.1)</td>
      <td>8.2 (8.1)</td>
      <td>5.5 (4.9)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>99.4 (97.7)</td>
      <td>99.7 (98.3)</td>
      <td>99.5 (94.9)</td>
      <td>99.5 (95.0)</td>
      <td>96.7 (88.8)</td>
    </tr>
    <tr>
      <td>Overall I/σ(I)</td>
      <td>19.0 (1.5)</td>
      <td>12.1 (1.5)</td>
      <td>26.4 (2.4)</td>
      <td>11.1 (2.5)</td>
      <td>7.1 (1.5)</td>
    </tr>
    <tr>
      <td>Rmerge† (%)</td>
      <td>9.7 (60.3)</td>
      <td>13.8 (77.0)</td>
      <td>13.3 (99.7)</td>
      <td>19.8 (66.5)</td>
      <td>19.8 (61.2)</td>
    </tr>
    <tr>
      <td colspan="6">Refinement</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>47.24 − 2.20</td>
      <td>47.07 − 2.74</td>
      <td>47.28 − 2.35</td>
      <td>47.22 − 3.21</td>
      <td>44.15 − 2.96</td>
    </tr>
    <tr>
      <td>No. of reflections</td>
      <td>32,642</td>
      <td>16,982</td>
      <td>27,146</td>
      <td>10,514</td>
      <td>13,111</td>
    </tr>
    <tr>
      <td>Rwork (%)</td>
      <td>21.6</td>
      <td>22.3</td>
      <td>23.09</td>
      <td>22.16</td>
      <td>19.6</td>
    </tr>
    <tr>
      <td>Rfree§ (%)</td>
      <td>25.4</td>
      <td>26.7</td>
      <td>26.00</td>
      <td>27.43</td>
      <td>24.4</td>
    </tr>
    <tr>
      <td colspan="6">No. atoms</td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>7911</td>
      <td>7519</td>
      <td>7723</td>
      <td>7528</td>
      <td>7774</td>
    </tr>
    <tr>
      <td>Nucleic acid</td>
      <td>232</td>
      <td>298</td>
      <td>230</td>
      <td>232</td>
      <td>147</td>
    </tr>
    <tr>
      <td>Ligands</td>
      <td>45</td>
      <td>42</td>
      <td>43</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>115</td>
      <td>28</td>
      <td>61</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Rmsd bonds (Å)</td>
      <td>0.003</td>
      <td>0.003</td>
      <td>0.003</td>
      <td>0.004</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>Rmsd angles (°)</td>
      <td>0.696</td>
      <td>0.629</td>
      <td>0.710</td>
      <td>0.968</td>
      <td>0.751</td>
    </tr>
    <tr>
      <td>Ramachandran favored# (%)</td>
      <td>97.23</td>
      <td>96.01</td>
      <td>96.84</td>
      <td>98.40</td>
      <td>97.04</td>
    </tr>
    <tr>
      <td>Ramachandran allowed (%)</td>
      <td>2.30</td>
      <td>1.94</td>
      <td>2.19</td>
      <td>1.40</td>
      <td>1.98</td>
    </tr>
    <tr>
      <td>PDB ID</td>
      <td>4TYW</td>
      <td>4TYY</td>
      <td>4TZ0</td>
      <td>4TZ6</td>
      <td>4TYN</td>
    </tr>
  </tbody>
</table>

_*The numbers in parentheses refer to the highest resolution shell.†Rmerge = ∑hkl ∑i |Ihkl,i − 〈Ihkl〉|/∑hkl ∑〈Ihkl〉.§Rfree was calculated with 5% of reflections that were excluded from refinement.#Analysis by MolProbity (Chen et al., 2010)._

### The biochemical basis for the RNA specificity of the helicase core of Mss116

D2 of Mss116 (residues 342–597) functions as an RNA-duplex recognition domain in the open-state enzyme (Mallam et al., 2012) (Figure 1D). To determine how Mss116 specifies for dsRNA, we first examined how 12-bp RNA and DNA duplexes of different geometries (Figure 4) interact with D2 in the absence of nucleotide. EMSAs using fluorescein amidite (FAM)-labeled duplexes show that D2 has surprisingly similar affinities for dsRNA (K1/2 = 400 nM) and A-DNA and B-DNA duplexes (K1/2 = 410 and 510 nM, respectively) (Figure 5A and Figure 5—figure supplement 1A–C). Circular dichroism (CD) measurements confirmed that the geometry of the A-DNA and B-DNA duplexes is maintained upon binding to D2, and that binding does not induce a B- to A-form transition (Figure 4E and Figure 4—figure supplement 1). The B-DNA duplex also competitively displaces dsRNA bound to D2 (Ki = 1700 nM) (Figure 5B). These results indicate that D2 can bind dsRNA and dsDNA of A- or B-form geometry in the dsRNA binding pocket even with the different spacing of the backbone phosphate groups (Mallam et al., 2012). Our findings are consistent with recent studies showing that several DEAD-box proteins can interact with dsDNA (Kammel et al., 2013; Tuteja et al., 2014). D2 of Mss116 is therefore a general and flexible nucleic acid duplex binding domain.

![Figure 4.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig4-v2.jpg)

**Figure 4.:** (A–C) 12-bp model substrates of (A) dsRNA (yellow); (B) A-DNA duplex (pink); and (C) B-DNA duplex (red). The duplex geometry of the DNA substrates has been previously characterized in solution by CD measurements (Basham et al., 1995) and X-ray crystallography (Verdaguer et al., 1991). The duplexes are predicted to have similar stabilities (predicted melting temperatures are 61.0°C, 59.4°C, and 63.9°C for the dsRNA, A-DNA, and B-DNA duplexes, respectively [Owczarzy et al., 2008]). (D) CD spectra of A-DNA (pink) and B-DNA (red) duplexes, which are consistent with previously reported spectra of identical duplexes (Basham et al., 1995; Kypr et al., 2009). The CD-spectrum of the A-DNA duplex has a characteristic strong positive peak at 260 nm and negative peaks at 240 and 210 nm (Ivanov et al., 1973). The B-DNA duplex is characterized by a positive peak at 260–280 nm and a negative peak at ∼245 nm (Kypr et al., 2009). (E) CD spectra of the B-DNA duplex (100 μM) in the absence (solid red line) and presence (dashed black line) of D2 (120 μM). Spectra are shown in units of molar circular dichroism (Δε) and are background subtracted for the presence of protein.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Spectra are shown in units of molar circular dichroism (Δε) and are background subtracted for the presence of protein. The characteristic strong positive and negative peaks in the CD-spectrum of the A-DNA duplex at 260 nm and 240 nm, respectively, remain in the presence of protein.

![Figure 5.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig5-v2.jpg)

**Figure 5.:** (A) Equilibrium binding of duplex substrates to MBP-tagged D2 in the absence of nucleotide determined by EMSA. (B) Competitive displacement from MBP-tagged D2 of 5′ FAM-B-DNA duplex (250 nM) by unlabeled dsRNA (0–6 μM, yellow, Ki = 860 ± 40 nM) and of 5′ FAM-dsRNA (250 nM) by unlabeled B-DNA duplex (0–6 μM, red, Ki = 1700 ± 200 nM). (C) Unwinding of duplex substrates by the MBP-tagged helicase core measured under equilibrium conditions by using a gel-based fluorescence assay to monitor the formation of a closed-state complex at increasing concentrations of ADP-BeFx (see also Figure 2—figure supplement 1). NU, no appreciable unwinding. (D) Equilibrium binding of A10-DNA to the MBP-tagged helicase core determined by fluorescence anisotropy measurements at increasing concentrations of ADP-BeFx. The binding of A10-RNA under the same conditions is shown for comparison (taken from Figure 2B). In (A–D), data were normalized using the signal obtained from the fit to the appropriate model outlined in the ‘Materials and methods’. (E) Normalized SEC profiles monitored by the absorbance at 260 nm (red) and 280 nm (black) for the helicase core in the absence of substrates (top) and in the presence of either A10-RNA + ADP-BeFx (middle) and A10-DNA + ADP-BeFx (bottom). An A260/A280 >1 at the maximum absorbance indicates the formation of a stable closed-state complex (Table 1).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Representative binding assays of Mss116 MBP-D2 (0–6 μM) to a 5′ FAM-labeled 12-bp duplex substrate (100 nM) for (A) dsRNA; (B) an A-DNA duplex; and (C) a B-DNA duplex. Samples were loaded in the reaction medium and resolved in a non-denaturing 6% polyacrylamide gel run at 4°C in 0.5× Tris/Borate/EDTA buffer (pH 8.3). Arrows mark the positions of free and bound duplex substrate. Proteins have an N-terminal MBP tag to increase solubility under the EMSA conditions. The binding data show cooperativity for all duplex substrates (Hill coefficients are 2.2, 1.5, and 1.6 for the dsRNA, A-DNA, and B-DNA duplexes, respectively, Figure 5A), which suggests that multiple molecules of D2 can bind to a single duplex substrate. The second band corresponding to bound substrate seen in some lanes could also be indicative of this. (D) Representative binding assays of Mss116 MBP-D1 (0–6 μM) to a 5′ FAM-B-DNA duplex (100 nM) to demonstrate minimal binding of D1 to the B-DNA duplex under these experimental conditions.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Unwinding was probed by using the duplex substrates shown in Figure 4A–C, which were labeled with fluorophore (FAM) and quencher (IBFQ) probes at the 5′ and 3′ ends, respectively (IDT). A change in fluorescence of these substrates occurs when the helicase core unwinds the duplex and forms a closed-state bound to a single-stranded region of RNA (Figure 2—figure supplement 1A). (A–C) Representative unwinding assays for (A) dsRNA; (B) A-DNA; and (C) B-DNA duplexes by the MBP-tagged helicase core (2 μM) measured at increasing concentrations of ADP-BeFx (0–4 mM), as described in Figure 2—figure supplement 1A. Arrows mark the complexes corresponding to the open and closed state protein bound to nucleic acid.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Kinetic unwinding profiles of dsRNA, A-DNA, and B-DNA duplexes catalyzed by D1D2 (2 μM) and ATP (5 mM). Error bars represent the standard error for at least three independent measurements, and the error in k1 represents the standard error of the non-linear regression. NU, no appreciable unwinding. Data were normalized using the parameters obtained from the fit to a first-order reaction with a single exponential. In the case of B-DNA when no unwinding was observed, data were normalized using a signal for a fully unwound duplex. This was obtained unwinding and re-annealing a control sample containing the same amount of labeled and unlabeled duplex by heating to 94°C for 3 min and cooling to room temperature on the bench.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** SEC was performed using a Superdex 75 10/300 GL column (GE Healthcare) and a BioLogic DuoFlow chromatography system (Bio-Rad) in a buffer of 20 mM Tris–HCl (pH 7.5), 200 mM KCl, 10% glycerol, 1 mM DTT, 5 mM MgCl2. Complexes were assembled as outlined in the ‘Materials and methods’ and SEC data were measured using absorbance at 260 nm (red) and 280 nm (black). Example elution profiles are shown for D1D2 in the absence of substrates; in the presence of dsRNA only; in the presence of dsRNA and ADP-BeFx; in the presence of A-DNA-duplex and ADP-BeFx; and in the presence of B-DNA duplex and ADP-BeFx. The ratio of A260/A280, which is approximately 0.5 for free protein and >1 for protein–nucleic acid complexes, was used as an indicator of the formation of a closed-state complex that contains nucleic acid. However, the smaller elution volume at maximum A260 for dsRNA–D1D2–ADP-BeFx and A-DNA duplex-D1D2–ADP-BeFx (Ve = 9.6 ml for both) suggests the formation of some higher-order closed-state complexes, possibly with two protein molecules bound on either side of a partially unwound duplex. This is consistent with the cooperativity in duplex unwinding reactions previously observed for Mss116 (Halls et al., 2007).

We next examined the ability of Mss116 to unwind the same RNA and DNA model duplexes in the presence of increasing concentrations of ADP-BeFx (Figure 5C and Figure 5—figure supplement 2). Equilibrium duplex unwinding assays (Figure 2—figure supplement 1A) show that Mss116 can unwind dsRNA and an A-DNA duplex, although a lower concentration of ADP-BeFx is required to unwind dsRNA (K1/2 = 0.14 and 0.25 mM, respectively). Notably, we did not observe any appreciable unwinding of the B-DNA duplex under these conditions (Figure 5C and Figure 5—figure supplement 2). In this case, kinetic unwinding assays demonstrate the same trend. They show that Mss116 can unwind dsRNA and the A-DNA duplex in the presence of ATP with observed first-order rate constants (k1) of 0.46 and 0.15 min−1, respectively, but does not unwind the B-DNA duplex (Figure 5—figure supplement 3). Similarly, analytical SEC showed elution profiles for D1D2 that are consistent with closed-state complexes when measured with ADP-BeFx and dsRNA or the A-DNA duplex but not the B-DNA duplex (Table 1 and Figure 5—figure supplement 4). These data indicate that Mss116 selectively unwinds A-form duplex nucleic acids. Further, contrary to what was previously thought (Fairman-Williams et al., 2010), they demonstrate that a DEAD-box protein can unwind an all DNA duplex in a nucleotide-dependent manner if it has A-form geometry. Although D2 can bind a B-DNA duplex, a closed-state complex does not readily form with B-form DNA and unwinding of this substrate does not occur.

To further investigate why Mss116 preferentially unwinds RNA duplexes, we compared the characteristics of the closed-state helicase core with equivalent ssRNA (A10-RNA) and ssDNA (A10-DNA) substrates. Equilibrium fluorescence anisotropy assays in the presence of increasing concentrations of ADP-BeFx indicate that the closed-state complex forms with both substrates, but at a much lower concentration of ADP-BeFx for ssRNA than for ssDNA (Kd = 0.022 and 0.79 mM, respectively; Figure 5D). SEC data also demonstrate that a closed-state complex with A10-RNA and ADP-BeFx remains intact during elution, whereas an identical complex with A10-DNA dissociates on the SEC column (Figure 5E and Table 1). Thus, the closed-state core is significantly more stable and long-lived with ssRNA than with ssDNA.

### The structural basis for the RNA specificity of the helicase core of Mss116

To probe the structural basis for the difference in stability of the closed-state complex with ssRNA compared to ssDNA, we determined crystal structures of the closed-state helicase core with ADP-BeFx and either A10-RNA or A10-DNA at 2.5 and 2.9 Å resolutions, respectively (Figure 6 and Table 2). These structures confirm that Mss116 can form the same closed-state complex with ssRNA and ssDNA and allow a direct comparison of the interactions made by these substrates with the same helicase core. The structures show that trajectories of the bound ssRNA and ssDNA are very similar (Figure 6B) and that most of the interactions between the conserved nucleic acid binding motifs IV–V and the phosphate backbone are identical in both complexes (Figure 6C). However, the closed-state complex with ssRNA contains protein contacts to RNA 2′-OH groups that are not present in the closed-state complex with ssDNA. These include four from residues in motifs Ia and Ic in D1 that form during core closure and account for the higher stability of the closed-state with ssRNA (Figure 5D,E).

![Figure 6.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig6-v2.jpg)

**Figure 6.:** (A) Closed state crystal structures of the helicase core of Mss116 with the ATP analogue ADP-BeFx and A10-RNA (yellow) or A10-DNA (red). The helicase core is colored as in Figure 1C. (B) A comparison of the binding trajectory of equivalent nucleotides of A10-RNA (yellow) and A10-DNA (red) bound in the closed state. (C) A schematic comparing the interactions of A10-RNA (yellow) and A10-DNA (red) with the closed-state helicase core, colored blue and green to D1 and D2, respectively. Interactions unique to each structure are colored black.

## Discussion

Collectively our results elucidate the basis for the physiological preference of the DEAD-box protein Mss116 for ATP and RNA, but also show that the helicase core has a surprising degree of substrate ambiguity. This is a consequence of the ability of conserved helicase motifs to interact with the phosphate groups of different NTPs or nucleic acids and promote the formation of the same closed-state complex (Figure 3A and Figure 6A). The preference of Mss116 for ATP is dictated by optimal base-stacking and H-bonding interactions between the Q-motif and adenine base (Figure 3B,C). However, interactions between conserved motifs I, II, and VI and nucleotide phosphate moieties are sufficient to promote duplex unwinding at lower efficiency irrespective of the nucleotide base (Figure 2A and Figure 3B,C).

The specificity of Mss116 for unwinding RNA duplexes is dictated by both A-form geometry (Figure 5C) and interactions by motifs Ia and Ic in D1 with 2′-OH groups of ssRNA in the closed state (Figure 5D and Figure 6C). Additionally, Mss116 belongs to a subclass of DEAD-box proteins that has a CTE appended to D2 (Figure 1B) (Mohr et al., 2008). This CTE makes additional 2′-OH contacts to dsRNA in the open state (Mallam et al., 2012) that may favor its binding to D2 (Figure 5B). Nevertheless, the interactions of nucleic acid-binding motifs with the phosphate backbone are sufficient to enable Mss116 to unwind A-form DNA duplexes at lower efficiency (Figure 5C and Figure 5—figure supplement 3). Mss116 cannot unwind a B-form DNA duplex (Figure 5C and Figure 5—figure supplement 3), and a model of the closed state with a B-DNA duplex indicates that the helicase motifs in D1 that clash with dsRNA (Mallam et al., 2012) (Figure 7A) are not positioned to catalyze the unwinding of longer, thinner B-form duplexes (Figure 7B).

![Figure 7.](https://cdn.elifesciences.org/articles/04630/elife-04630-fig7-v2.jpg)

**Figure 7.:** (A) Surface representation of closed-state Mss116 with dsRNA modeled in the duplex RNA-binding pocket of D2. Sterically incompatible regions of D1 are highlighted in red, and these indicate how D1 promotes RNA unwinding upon core closure by disrupting the base pairing in the dsRNA. In particular, helicase motifs Ia, Ib, and Ic and the DEAD-box specific post-II motif in D1 displace one RNA strand and bend the other during RNA duplex unwinding (Mallam et al., 2012). (B) Surface representation of closed-state Mss116 with a B-DNA duplex, which is longer and thinner than an A-form duplex (Dickerson et al., 1982), modeled in the duplex RNA-binding pocket of D2. There are no appreciable clashes between dsDNA and the core in this model, which suggests why core closure does not promote unwinding of a B-DNA duplex (Figure 5C and Figure 5—figure supplement 3). (C) Closed-state structure of D1-D3 of human RIG-I helicase (PDB = 3TMI) bound to dsRNA (Jiang et al., 2011). dsRNA is accommodated in the closed-state of RIG-I, which explains how it functions by binding and/or translocating along a duplex RNA substrate (Myong et al., 2009; Rawling and Pyle, 2014). (D) Closed-state model of Sulfolobus solfataricus Swi2/Snf2 helicase core and a B-DNA duplex adapted from Durr et al. (2005). This model suggests that the Swi2/Snf2 helicase core can accommodate a B-form DNA duplex in a closed-state conformation and explains how helicases in this family function by translocating along DNA duplexes (Figure 1A). Proteins and nucleic acids are colored as in Figure 1.

Importantly, the substrate ambiguity of Mss116 suggests an evolutionary scenario for how SF1 and SF2 helicases diverged from an ancestral helicase core with broad specificity into specialized enzymes. In each case, core closure was retained as a catalytic mechanism using the interactions common to all NTP or nucleic acid substrates predicted from our results. However, the stability of the closed-state was further modulated by family-specific interactions that favor a particular NTP and nucleic acid. Thus, helicase families that display the most substrate ambiguity by utilizing all four NTPs and function on either DNA or RNA (for example the DEAH/RHA [Tanaka and Schwer, 2005] and NS3/NPH-II [Preugschat et al., 1996] families; Figure 1A) may contain a core that functions similarly to that of an ancestral helicase. Helicases that preferentially use ATP maintained the conserved interactions with nucleotide phosphate groups but acquired additional interactions with the adenine base that further stabilize the closed-state complex. Similarly, DEAD-box proteins, which act preferentially on RNA (Fairman-Williams et al., 2010), maintained conserved interactions with the nucleic acid backbone but evolved specificity for A-form duplexes and additional stabilizing interactions with RNA 2′-OH groups in the closed state, as demonstrated here for Mss116. The lack of unwinding activity in some DEAD-box proteins may stem from structural changes in the helicase core that mitigate RNA bending or strand displacement (Young et al., 2013). Helicase families that function on DNA (for example, the Swi/Snf, RecQ-like, and UvrD/Rep families) could have diversified by the preservation of conserved interactions with the nucleic acid backbone combined with the selection of additional interactions that favor B-form duplexes and/or disfavor nucleic acids with 2′-OH groups.

Similar inferences can be made from our data about the evolution of distinct mechanisms in SF1 and SF2 families (Figure 1A). We propose that although core-closure was retained as a mode of catalysis, the differences in the stability of the closed-state complex between helicase families allowed the diversification of the observed helicase mechanism. Thus, the localized unwinding mechanism used by DEAD-box proteins (Yang et al., 2007) likely evolved by the selection of a helicase core that is able to ‘clamp’ ssRNA and form a highly stable closed-state complex (Figure 5D,E). This mode of interaction compensates for the energy cost to locally unwind an RNA duplex, which is critical for DEAD-box protein function (Del Campo et al., 2009). In comparison, helicase cores that diverged to form less stable, more transient closed states with ssRNA or ssDNA would favor a mechanism that involved loading and translocating along a single strand (for example, NS3/NPH-II and RecQ-like helicases; Figure 1A).

Our data also demonstrate that the stability of the closed state depends upon interactions with nucleotides as well as nucleic acids (Figure 2). The DEAH family of helicases are a potential example of a case where a sequence change in motif II compared to DEAD-box proteins (‘DEAH’ instead of ‘DEAD’) might result in a weaker interaction with the ATP γ-phosphate and favor the observed switch from localized to translocation-based unwinding (Figure 1A). More generally, ATP-dependent core closure to form a ternary complex with nucleic acid may have evolved from tighter to weaker binding as the helicase mechanism concurrently evolved from localized to translocation-based. This is in addition to structural features, such as extra terminal domains or β-hairpins within the helicase core, which favor translocation-based unwinding in some helicase families (Fairman-Williams et al., 2010). Protein cofactors may also play a role in helicase substrate specificity, as illustrated for the DEAD-box protein Rok1, whose cofactor Rrp5 increases the specificity of the helicase core 10-fold for a pre-rRNA duplex (Young et al., 2013).

Finally, other SF2 helicases have evolved to optimally accommodate dsRNA (e.g., RIG-I) or dsDNA (e.g., Sulfolobus solfataricus Swi2/Snf2) in a closed state complex and translocate with no observable unwinding (Figure 1A, Figure 7C–D) (Durr et al., 2005; Myong et al., 2009; Jiang et al., 2011). In these cases, subtle changes in the closed-state core, perhaps combined with additional flanking domains, enable the helicase to bind duplex nucleic acid without the need to overcome the energetic barrier to unwinding and lead to this distinct mechanism of action. It has been hypothesized that during evolution, progenitor enzymes of low activity and broad specificity diverge into families of more potent and highly specialized enzymes (Jensen, 1976; Khersonsky and Tawfik, 2010). Taken together, our findings suggest how a progenitor helicase core that had broad specificity and used conserved motifs to recognize the phosphate groups of NTPs and the backbone of nucleic acids diverged to present day SF1 and SF2 helicases with different cellular functions.

## Materials and methods

### Oligonucleotides

Unlabeled self-complementary RNA or DNA oligonucleotides (Integrated DNA Technologies, IDT, Coralville, IO; Figure 4A–C) were annealed to form 12-bp RNA or DNA duplexes by heating solutions at 6 mM single strands in 100 mM potassium acetate, 30 mM HEPES (pH 7.5) at 94°C for 1 min and then slowly cooling to room temperature over 1 hr. Labeled duplexes for unwinding and binding assays were annealed similarly at 200 μM single strands. Sequences for 12-bp dsDNA substrates were chosen based upon previous studies which indicated that they adopt either A-form or B-form geometry (Basham et al., 1995; Kypr et al., 2009). We further characterized these substrates by using circular dichroism (CD) to confirm that they retained the required duplex geometry under our experimental conditions in the absence and presence of protein (Figure 4D,E and Figure 4—figure supplement 1).

### Protein expression and purification

The helicase core of Mss116 (D1D2) and separate domains D1 and D2 were expressed as N-terminal MalE fusions in Escherichia coli Rosetta 2 (EMD Biosciences, Germany), grown in ZYP-5052 auto-inducing medium for 24 hr at 22°C, and purified at 4°C, as described (Del Campo and Lambowitz, 2009; Mallam et al., 2011, 2012). Proteins for binding and unwinding assays were exchanged into a storage buffer of 20 mM Tris–HCl (pH 7.5), 200 mM KCl, 1 mM dithiothreitol (DTT), 10% glycerol during a final SEC purification step. D1D2 for crystallization was dialyzed into 10 mM Tris–HCl (pH 7.5), 250 mM NaCl, 1 mM DTT, 50 mM arginine + glutamine, 50% glycerol. All proteins were stored at −80°C before use.

### Duplex-unwinding assays in the presence of nucleotide

Equilibrium unwinding of 12-bp dsRNA, A-form DNA, and B-form DNA duplexes was measured in increasing concentrations of NDP-BeFx (N = A, C, G, or U) using a gel-based fluorescence assay to monitor the formation of a closed-state complex containing a bound single-stranded substrate. Duplexes were labeled with a fluorescent probe (FAM) and quencher (Iowa Black FQ) at the 5′ and 3′ ends, respectively. These substrates gave a change in fluorescence upon unwinding and formation of a closed state (Figure 2—figure supplement 1A). NDP-BeFx (N = A, C, G, or U) was prepared as described (Del Campo and Lambowitz, 2009). Measurements were performed using MBP-tagged D1D2 to increase protein solubility under the experimental conditions. MBP-D1D2 (2 μM) was incubated with the appropriate duplex substrate (100 nM) and increasing concentrations of NDP-BeFx-Mg2+ (ranging from 0 to 20 mM) at 22°C for at least 1 hr in a reaction medium containing 20 mM Tris–HCl (pH 7.5), 100 mM KCl, 10% glycerol, 1 mM DTT, 5 mM MgCl2, and 0.1 mg/ml of bovine serum albumin. The protein concentration was chosen so that all of the duplex substrate is bound in the open state at equilibrium (Figure 5A). Samples were analyzed in a non-denaturing 6% polyacrylamide gel run at 4°C for 60 min. The fluorescence signal of the bound duplex substrate was quantified by using a Typhoon imager (GE Healthcare, UK) to measure the formation of a closed-state complex containing a single-stranded nucleic acid region, indicating duplex unwinding (Figure 2—figure supplement 1). The apparent fraction of unwound duplex at increasing concentrations of NDP-BeFx was quantified by using ImageJ and fit to a one-site binding model to estimate the concentration of nucleotide at the midpoint (K1/2) of the unwinding reaction. In all cases, equilibrium was verified by additional assays for samples that were incubated for extended times (up to approximately 4 hr), which gave the same unwinding profiles as those incubated for 1 hr.

Kinetic-unwinding assays of 12-bp dsRNA, A-form DNA, and B-form DNA duplexes by the helicase core were performed with the same fluorophore–quencher labeled probes (Figure 2—figure supplement 1A) in the presence of 5 mM NTP (N = A, C, G, or U). In these assays, a change in the fluorescence of the labeled duplex was seen upon unwinding and subsequent re-annealing to form a duplex with an unlabeled strand of the same sequence without a quencher present in excess (Figure 2—figure supplement 2). Annealing of these duplexes occurs within the dead time of mixing at the concentration of substrates used in these experiments. D1D2 (2 μM) was mixed with NTP-Mg2+ (5 mM), labeled duplex (125 nM), and unlabeled duplex (500 nM) at 22°C in a reaction medium containing 20 mM Tris–HCl (pH 7.5), 100 mM KCl, 10% glycerol, 1 mM DTT, 5 mM MgCl2. Reactions were terminated at appropriate time points with 1 volume of stop buffer (50 mM EDTA, 1% SDS, 10% glycerol) and run in a non-denaturing 20% polyacrylamide at 22°C for 60 min. The fluorescence signal of duplex substrate was quantified by using a Typhoon imager (GE Healthcare) to measure the extent of unwinding/re-annealing. The apparent fraction of unwound duplex at various time points was quantified by using ImageJ and (where appropriate) fit to a first-order reaction to estimate an observed first-order rate constant (k1).

### Single strand nucleic acid binding assays in the presence of nucleotide

Equilibrium binding of A10-RNA and A10-DNA to D1D2 in increasing concentrations of NDP-BeFx was measured by fluorescence anisotropy using MBP-tagged protein to increase the change in anisotropy upon binding. 5′ FAM-labeled A10-RNA or A10-DNA (10 nM; IDT) was incubated with protein (2 μM) and increasing concentrations of NDP-BeFx (N = A, C, G, or U; 0 to 10 mM) at 22°C for at least 1 hr in a reaction medium containing 20 mM Tris–HCl (pH 7.5), 100 mM KCl, 10% glycerol, 1 mM DTT, 5 mM MgCl2, and 0.1 mg/ml of bovine serum albumin. The observed fluorescence anisotropy at increasing concentrations of protein was measured by using an EnVision Microplate Reader (Perkin Elmer, Waltham, MA) and was fit to a one-site binding model with a Hill coefficient to estimate the Kd of single-stranded nucleic acid in the presence of increasing nucleotide. Equilibrium was verified by carrying out assays on samples incubated for extended times up to 4 hr, which gave the same binding profiles as those incubated for 1 hr. Equivalent experiments were performed to measure the binding of A10-RNA to D1D2 in increasing concentrations of AMP-PNP or ADP (0–10 mM) and ADP + Pi (0–100 mM Pi in the presence of 10 mM ADP).

### Duplex binding assays

Equilibrium binding of 12-bp RNA (A-form) and DNA (A-form and B-form) duplexes to D1 or D2 was measured by EMSA using MBP-tagged proteins to increase protein solubility as described (Mallam et al., 2012). 5′ FAM-labeled 12-bp duplexes (100 nM; IDT; Figure 4A–C) were incubated with increasing concentrations of protein (0–6 μM) at 22°C for at least 1 hr in a reaction medium containing 20 mM Tris–HCl (pH 7.5), 100 mM KCl, 10% glycerol, 1 mM DTT, 5 mM MgCl2, and 0.1 mg/ml of bovine serum albumin to stabilize the protein at low concentrations. Samples were then analyzed in a non-denaturing 6% polyacrylamide gel run at 4°C for 60 min, and the fluorescence signal of the bound duplex substrate was quantified by using a Typhoon imager. The fraction of bound duplex with increasing concentrations of MBP-tagged protein was quantified by using ImageJ and fit to a one-site binding model with a Hill coefficient to estimate a Kd.

Competition assays were performed similarly by measuring the competitive displacement from MBP-D2 (500 nM) of 5′ FAM-B-DNA duplex (250 nM) by unlabeled dsRNA (0–6 μM, Ki = 860 ± 40 nM) and of 5′ FAM-dsRNA (250 nM) by unlabeled B-DNA duplex (0–6 μM, Ki = 1700 ± 200 nM). In these cases, the fraction of free substrate was quantified and a Ki was estimated from a one-site binding model.

### Size-exclusion chromatography

Binding of nucleotide and nucleic acid substrates to D1D2 was examined by size-exclusion chromatography. The helicase core of Mss116 does not contain tryptophan residues and its calculated extinction coefficient is small (ε280 = 18,255 M−1 cm−1; ExPASy Proteomics Server ProtParam tool [Wilkins et al., 1999]). The formation of a closed-state complex in the presence of nucleic acid and NDP-BeFx therefore gives rise to a large change in A260 compared to A280. Protein samples (10 μM) were incubated at 22°C for 30 min in NDP-BeFx-Mg2+ (5 mM, N = A, C, G, or U) and single-stranded (A10-RNA or A10-DNA; 20 μM) or duplex (dsRNA, A-DNA duplex or B-DNA duplex; 10 μM) nucleic acid and loaded onto a Superdex 75 column (GE Healthcare) pre-equilibrated in a buffer containing 20 mM Tris–HCl (pH 7.5), 200 mM KCl, 10% glycerol, 1 mM DTT, 5 mM MgCl2. The absorbance and elution volume of the protein complexes above the background signal of the buffer were measured at 260 and 280 nm (Table 1). Control samples of protein alone, substrate alone, or protein and either nucleotide or nucleic acid were also measured; closed-state complexes were not detected in these cases.

### Circular dichroism

All measurements were performed in 20 mM Tris–HCl (pH 7.5), 100 mM KCl, 10% glycerol, 1 mM DTT, 5 mM MgCl2 buffer using a thermostatically controlled 0.01-cm path-length cuvette at 25°C and a Jasco J-815 spectrometer (Jasco Inc., Easton, MD). Scans were taken between 200 and 325 nm at a scan rate of 0.5 nm s−1 with 30 accumulations. Measurements were made on samples of SEC-purified A-form DNA or B-form DNA duplexes (100 μM) in the absence or presence of Mss116 D2 or MBP-D2 (120 μM).

### Crystallization

For the D1D2–A10-RNA–NDP-BeFx complexes, protein (∼350 μM) was incubated with A10-RNA (600 μM), NDP-BeFx-Mg2+ (5 mM; N = A, C, G, or U) and MgCl2 (1 mM) for 30 min on the desktop. Sitting drops were assembled using 0.5 μl of complex and 0.5 μl of a well solution of 0.1 M HEPES, pH 7.5, 2% tacsimate, pH 7.0, 20% PEG (polyethylene glycol) 3350 for D1D2–A10-RNA–ADP-BeFx; 0.2 M sodium malonate, pH 5.0, 20% PEG 3350 for D1D2–A10-RNA–CDP-BeFx; 4% tacsimate, pH 8.0, 12% PEG 3350 for D1D2–A10-RNA–GDP-BeFx; and 0.1 M DL-malic acid, pH 7.0, 12% PEG 3350 for D1D2–A10-RNA–UDP-BeFx (Hampton Research, Aliso Viejo, CA). Drops were stored at 22°C and plate-like crystals appeared within 1–2 weeks. Crystals were removed from sitting drops and flash cooled immediately in liquid N2. Crystals of D1D2–A10-DNA–ADP-BeFx were obtained similarly and drops were assembled with a well solution of 0.2 M ammonium acetate, 20% PEG 3350.

### Structure determination

X-ray diffraction data were collected at the Advanced Light Source (ALS), Lawrence Berkeley National Laboratory (mail-in service on beamlines 5.0.2 or 5.0.3; wavelength = 1.00003 Å). Details of data collection and refinement are in Table 2. Diffraction intensities were indexed, integrated, and scaled with HKL-2000 (Otwinowski and Minor, 1997). Initial space groups were determined by using Pointless (Evans, 2006) and confirmed by decreases in both Rwork and Rfree after refinement of molecular replacement solutions. Molecular replacement was performed with Phaser (McCoy et al., 2007), using the previously determined structure of Mss116 D1D2 in the closed state (PDB 3I5X) as a search model. Structures were completed with cycles of manual model building in Coot (Emsley et al., 2010) and refinement in Phenix (Adams et al., 2010). Validation of protein and nucleic acid models and their contacts was done by using MolProbity (Chen et al., 2010) and indicated that at least 98% of residues are located in the most favorable region of the Ramachandran plot. Structural figures were prepared by using the PyMOL Molecular Graphics System, Version 1.4, Schrödinger, LLC.

### Accession numbers

Coordinates and structure factors were deposited in the Protein Data Bank under accessions 4TYW (D1D1–A10-RNA–ADP-BeFx), 4TYY (D1D1–A10-RNA–CDP-BeFx), 4TZ0 (D1D1–A10-RNA–GDP-BeFx), 4TZ6 (D1D1–A10-RNA–UDP-BeFx), and 4TYN (D1D1–A10-DNA–ADP-BeFx).
