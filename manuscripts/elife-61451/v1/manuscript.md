# ClpAP proteolysis does not require rotation of the ClpA unfoldase relative to ClpP

## Authors

- Sora Kim<sup>1</sup> ([ORCID: 0000-0002-9856-9574](https://orcid.org/0000-0002-9856-9574))
- Kristin L Zuromski<sup>2</sup> ([ORCID: 0000-0003-0960-5009](https://orcid.org/0000-0003-0960-5009))
- Tristan A Bell<sup>1</sup> ([ORCID: 0000-0002-3668-8412](https://orcid.org/0000-0002-3668-8412))
- Robert T Sauer<sup>1</sup> ([ORCID: 0000-0002-1719-5399](https://orcid.org/0000-0002-1719-5399))
- Tania A Baker<sup>1</sup> ([ORCID: 0000-0002-0737-3411](https://orcid.org/0000-0002-0737-3411)) †

### Affiliations

1. Department of Biology, Massachusetts Institute of Technology Cambridge United States
2. Department of Chemistry, Massachusetts Institute of Technology Cambridge United States

† Corresponding author

## Abstract

AAA+ proteases perform regulated protein degradation in all kingdoms of life and consist of a hexameric AAA+ unfoldase/translocase in complex with a self-compartmentalized peptidase. Based on asymmetric features of cryo-EM structures and a sequential hand-over-hand model of substrate translocation, recent publications have proposed that the AAA+ unfoldases ClpA and ClpX rotate with respect to their partner peptidase ClpP to allow function. Here, we test this model by covalently crosslinking ClpA to ClpP to prevent rotation. We find that crosslinked ClpAP complexes unfold, translocate, and degrade protein substrates in vitro, albeit modestly slower than uncrosslinked enzyme controls. Rotation of ClpA with respect to ClpP is therefore not required for ClpAP protease activity, although some flexibility in how the AAA+ ring docks with ClpP may be necessary for optimal function.

## Introduction

The AAA+ (ATPases Associated with diverse cellular Activities) protease subfamily uses the energy of ATP hydrolysis to disassemble and degrade proteins that are misfolded, deleterious, or unneeded (Sauer and Baker, 2011). AAA+ proteases are composed of a hexameric single- or double-ringed AAA+ unfoldase/translocase and a self-compartmentalized partner peptidase. The AAA+ rings form a shallow helix and stack with planar peptidase rings (Puchades et al., 2020). After protein substrate recognition by the unfoldase, repeated cycles of ATP hydrolysis power conformational changes in the AAA+ motor, promoting substrate unfolding and processive translocation of the resulting polypeptide into the proteolytic chamber of the peptidase for degradation. Recent structural and biochemical studies have illuminated some aspects of this process, but the molecular nature of the stepwise cycles these proteolytic machines use to carry out mechanical unfolding and translocation of protein substrates is still being actively explored (Puchades et al., 2020).

The ClpAP protease consists of the ClpA6 AAA+ unfoldase, a double-ring AAA+ enzyme with two AAA+ modules per subunit, and the tetradecameric ClpP14 peptidase, which contains two heptameric rings (Sauer and Baker, 2011; Figure 1A). Thus, the interface between ClpA and ClpP involves an asymmetric six-to-seven subunit mismatch. The ClpXP protease, composed of the single-ring AAA+ ClpX6 unfoldase and the ClpP14 peptidase, also has a six-to-seven mismatch, as do proteasomal AAA+ enzymes. How such mismatches are accommodated structurally and whether the mismatches play important roles in the mechanisms of these ATP-dependent proteases has long been a subject of interest. Recent near-atomic-resolution cryo-EM structures of ClpAP and ClpXP reveal that each unfoldase has six flexible peptidase-binding loops protruding from the bottom face of the AAA+ ring that can interact with ClpP14 (Fei et al., 2020a; Fei et al., 2020b; Ripstein et al., 2020; Lopez et al., 2020). Part of each loop containing a conserved tripeptide motif (IGL in ClpA; IGF in ClpX) docks into hydrophobic clefts on the top of the ClpP7 ring, engaging a total of five or six of the seven clefts and leaving one or two clefts unoccupied (Figure 1A; Fei et al., 2020a; Fei et al., 2020b; Ripstein et al., 2020; Lopez et al., 2020).

![Figure 1.](https://cdn.elifesciences.org/articles/61451/elife-61451-fig1-v1.jpg)

**Figure 1.:** (A) Complex of ClpP with ClpA (PDB 6UQO). Subunits of ClpA, labeled S1 through S6, are ordered from the highest to the lowest position in the spiral relative to ClpP at the beginning of the mechanical cycle. The IGL loops of ClpA hexamers dock into a subset of the seven clefts in a heptameric ClpP ring. In this structure, there is an empty cleft between the second lowest and lowest subunits in the spiral (S5 and S6, respectively). The coloring of the ClpP clefts represents the docked position of the IGL loops from the corresponding AAA+ subunits; empty clefts are colored white. The rightmost panel is a generalized model of the ClpA D2 AAA+ ring docking into the ClpP interface. (B) Rotary translocation model with clockwise around-the-ring ATP hydrolysis and IGL loop release and rebinding (Ripstein et al., 2020; Lopez et al., 2020). When subunit S1 is highest in the spiral, ATP hydrolysis releases the IGL loop of subunit S5 and the AAA+ ring rotates clockwise with respect to ClpP. During rotation, subunit S6 moves to the top in of the spiral, and the IGL loop of subunit S5 takes a clockwise ‘step’ and rebinds to the adjacent empty ClpP cleft. Repetition of this sequence of ATP hydrolysis and IGL loop release and rebinding results in rotary motion of the AAA+ ring with respect to the ClpP ring. (C) Rotary translocation model with at least one crosslinked IGL loop. If one ClpA subunit is crosslinked to a ClpP cleft, the rotary motion of the AAA+ ring with respect to the ClpP ring is blocked. The crosslinked ClpA subunit cannot be released from the ClpP cleft and cannot sequentially move to each position in the ClpA spiral.

Subunits in both the ClpA and ClpX hexamers adopt a shallow helical conformation with axial pore loops that interact with an extended substrate polypeptide to form a structure reminiscent of a spiral staircase. By contrast, ClpP subunits are arranged in near-planar rings that enclose a chamber with luminal peptidase active sites. Other AAA+ proteases have similar architectures, with spiral AAA+ rings and planar peptidase rings (Puchades et al., 2020). In structures of heterohexameric AAA+ protease motors in which the positions of unique subunits can be determined, different subunits can occupy the highest and lowest spiral positions, suggesting that dynamic rearrangement of subunits within the spiral is part of the ATP-fueled mechanical cycle that powers substrate translocation (de la Peña et al., 2018; Dong et al., 2019). In one model for this cycle, an enzyme power stroke is initiated when the second lowest subunit in the spiral hydrolyzes ATP (S5 at the beginning of the cycle, Figure 1A), resulting in a rearrangement that moves this subunit and higher subunits, together with bound substrate, each down one position in the spiral, at the same time that the lowest subunit (S6) disengages from substrate and moves to the top of the spiral (Figure 1B; Puchades et al., 2020). Intriguingly, in recent cryo-EM structures of ClpAP and ClpXP, an empty ClpP cleft is always flanked by clefts that interact with the IGL/IGF loops of the second lowest and lowest subunits within the spiral (S5 and S6 in Figure 1A; Fei et al., 2020a; Fei et al., 2020b; Ripstein et al., 2020; Lopez et al., 2020). If different subunits in the ClpA or ClpX hexamers pass sequentially through each position in the spiral during substrate translocation and the empty cleft in ClpP is always between clefts that interact with specific subunits in the spiral, then the AAA+ ring should rotate with respect to ClpP during protein translocation (Figure 1B; Ripstein et al., 2020; Lopez et al., 2020).

Here, we test the effects of preventing rotation of the ClpA ring with respect to the ClpP ring by covalently crosslinking multiple IGL loops of ClpA to ClpP (Figure 1C). We find that an enzyme containing multiple covalent crosslinks between ClpA and ClpP retains substantial proteolytic activity against unfolded and metastable native substrates but displays defects in degrading more stably folded proteins. We conclude that rotation of ClpA with respect to ClpP is not required for substrate translocation or unfolding, but some freedom of movement at the ClpA-ClpP interface is likely to be important for optimal mechanical activity.

## Results and discussion

### Crosslinking ClpA to ClpP

For crosslinking studies, we used cysteine-free genetic backgrounds for ClpA (C47S, C203S, C243S; Zuromski et al., 2020) and ClpP (C91V, C113A; Amor et al., 2016). We then introduced an E613C mutation into the IGL loop of otherwise cysteine-free ClpA (E613CClpA‡) and appended a cysteine after Asn193, the C-terminal residue of otherwise cysteine-free ClpP (ClpP+C). Based on cryo-EM structures of ClpAP (Lopez et al., 2020), the cysteines introduced by these mutations should be close enough to allow crosslinking of specific subunits of ClpA to neighboring subunits of ClpP. For example, Figure 2A shows that Glu613 in each subunit of the ClpA hexamer is close to a ClpP Arg192 residue, the last ClpP amino acid visible in the ClpAP structure, in six of the seven ClpP protomers. We mixed E613CClpA‡ with ClpP+C in the presence of a homobifunctional cysteine crosslinker and then separated covalently joined E613CClpA‡–ClpP+C complexes (peak 1) from uncrosslinked ClpP+C (peak 2) by size-exclusion chromatography (Figure 2B). After pooling fractions containing E613CClpA‡–ClpP+C complexes (Figure 2B), quantification by SDS-PAGE revealed that 90 ± 1% of the ClpA was crosslinked to ClpP (designated A–P) (Figure 2C lane 7, Figure 2—source data 1). Based on this crosslinking efficiency, the vast majority of ClpA hexamers should contain one or more crosslinked A–P subunits (>99.99%, assuming independent crosslinking), and ~98% of hexamers should contain four, five, or six ClpA subunits crosslinked to ClpP (Figure 2—figure supplement 1). The E613CClpA‡–ClpP+C pool also contained uncrosslinked ClpP+C, as expected, and some crosslinked ClpP+C dimers (Figure 2C, lane 7).

![Figure 2.](https://cdn.elifesciences.org/articles/61451/elife-61451-fig2-v1.jpg)

**Figure 2.:** (A) Proximity of Glu613 residues in six subunits of the hexameric ClpA ring (shown in the dashed outline) to Arg192 residues in six of the seven subunits of a heptameric ClpP ring (shown in the solid outline). (B) Size-exclusion chromatograms of E613CClpA‡–ClpP+C following crosslinking (solid line; peaks 1 and 2) or uncrosslinked E613CClpA‡ (dashed line; peak 3), which is largely monomeric under the chromatography conditions. As shown in panel C, most ClpA in peak one is crosslinked to ClpP. The shaded area in peak 1 represents the crosslinked A–P that was pooled and used in all experiments in this study. Peak 2 corresponds to uncrosslinked ClpP+C remaining after the crosslinking reaction and chromatographs at the position expected for a tetradecamer. (C) Reducing SDS-PAGE of the peak-1 pool. Lanes 1–6 are MW standards or different concentrations of purified E613CClpA‡. Lane 7 is an aliquot of the peak-1 pool. The shift to higher molecular weight from uncrosslinked ClpA (A) to crosslinked ClpA–ClpP (A–P) is consistent with covalent linkage of a single ClpA monomer (~83 kDa) to a single ClpP monomer (~23 kDa). The dashed red box is a zoomed-in view of lane 7 used to calculate crosslinking efficiency of E613CClpA‡ to ClpP+C. Crosslinking efficiency was calculated as the mean ± 1 SD of four independent replicates. The quantification of SDS-PAGE bands used to calculate crosslinking efficiency is available in Figure 2—source data 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/61451/elife-61451-fig2-figsupp1-v1.jpg)

### Crosslinked complexes degrade model substrates

To test if ClpA rotation relative to ClpP is required for ATP-fueled proteolysis, we measured ATP hydrolysis and degradation of model substrates by the purified crosslinked A–P pool in vitro compared to an A•P control consisting of assembled but uncrosslinked E613CClpA‡ and wild-type ClpP (ClpPWT). The A–P pool hydrolyzed ATP at a steady-state rate of 412 ± 40 min−1 enz−1, whereas this rate was 1035 ± 78 min−1 enz−1 for the A•P control. The A•P control hydrolyzed ATP and degraded ssrA-tagged proteins at comparable rates to wild-type ClpAP (ClpAWTClpPWT) and a cysteine-free ClpA (ClpACF) variant (ClpACFClpPWT), demonstrating that the C47S, C203S, C243S, and E613C mutations do not impair activity (Figure 3—figure supplement 1A–B, Figure 3—source data 5). We also observed similar rates of ATP hydrolysis and ssrA-tagged protein degradation when ClpP+C, the ClpP variant used for crosslinking, was paired with ClpAWT, ClpACF, or E613CClpA‡.

To test the effects of crosslinking ClpA to ClpP on proteolysis, we measured the rate at which the A–P and A•P enzymes degraded proteins with a range of native stabilities. These substrates included the N-terminal domain of the phage λ cI repressor with an ssrA tag (λ cIN-ssrA; Gottesman et al., 1998), cp7GFP-ssrA (Nager et al., 2011), 5-IAFV13P titinI27-ssrA (Kenniston et al., 2003; Iosefson et al., 2015), and FITC-casein (Twining, 1984; Thompson et al., 1994). Under the conditions of these assays in vitro, the A–P sample degraded the folded substrates (λ cIN-ssrA and cp7GFP-ssrA) at rates that were 31 ± 5% and 32 ± 4%, respectively, of the A•P control, and degraded unfolded 5-IAFV13P titinI27-ssrA and FITC-casein at 46 ± 2% and 97 ± 7%, respectively, of the control rates (Figure 3A–B, Figure 3—source datas 1–2). The rate of degradation of FITC-casein by the A–P pool was reduced ~6-fold when ATPγS was substituted for ATP (Figure 3C, Figure 3—source data 3), indicating that robust degradation of this molten-globule substrate requires ATP hydrolysis. We also determined steady-state kinetic parameters for degradation of cp7GFP-ssrA by the A–P pool and A•P control (Figure 3D, Figure 3—source data 4). Compared to the A•P control, Vmax was ~50% and KM was ~3-fold weaker for degradation of this substrate by the A–P pool. This reduction in Vmax for the A–P pool was roughly comparable to its reduced ATP-hydrolysis activity, suggesting that slower degradation of folded substrates by the A–P pool results from slower ATPase activity. Thus, our results show that multiple crosslinks between ClpA and ClpP in the A–P pool cause modest slowing of the rates of ATP hydrolysis and protein degradation compared to the uncrosslinked controls (Figure 3—figure supplement 1A–B), with more prominent degradation defects for native substrates. Notably, however, crosslinks between ClpA and ClpP do not prevent the protein unfolding or translocation steps required for proteolysis. Only the crosslinked A–P sample exhibited substantially lower ATP-hydrolysis and protein degradation activity compared to the uncrosslinked controls; thus, the reduced A–P enzymatic activities are likely to be direct consequences of introducing specific covalent crosslinks between ClpA and ClpP rather than other modifications introduced in the experimental design.

![Figure 3.](https://cdn.elifesciences.org/articles/61451/elife-61451-fig3-v1.jpg)

**Figure 3.:** (A) Top, SDS-PAGE assay of the kinetics of λ cIN-ssrA degradation by A–P and the A•P control (CK is creatine kinase). Bottom, quantification of λ cIN-ssrA degradation. Values are means ± 1 SD (n = 3) and provided in Figure 3—source data 1. (B) Degradation of substrates of varying thermodynamic stability (18 µM) FITC-casein, 5 µM 5-IAFV13P titinI27-ssrA, 20 µM cp7GFP-ssrA, 15 µM λ clN-ssrA by A–P. Fractional degradation rates were calculated by dividing the degradation rates of A–P by the A•P rates. Values are means ± propagated error (n ≥ 3) and provided in Figure 3—source data 2. (C) Degradation of FITC-casein (18 µM) by A–P in the presence of ATP or ATPγS. FITC-casein degradation was quantified by normalizing the relative fluorescence units to the total FITC-casein degraded upon porcine elastase addition at the endpoint of the assay and subtracting the contributions of photobleaching from the buffer-only control. Values are means ± 1 SD (n = 3) and provided in Figure 3—source data 3. The inset shows representative degradation kinetics. (D) Michaelis-Menten analysis of cp7GFP-ssrA degradation kinetics by A–P and the A•P control. Values are means ±1 SD (n = 3) and provided in in Figure 3—source data 4. For A–P degradation, Vmax was 1.4 ± 0.07 min−1 ClpA6−1, KM was 13 ± 1.6 µM, and R2 was 0.96; for the A•P control, Vmax was 3.0 ± 0.10 min−1 ClpA6−1, KM was 3.7 ± 0.5 µM, and R2 was 0.96, where the errors are those of non-linear least-squares fitting to the Michaelis-Menten equation.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/61451/elife-61451-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Hydrolysis of ATP (5 mM) by crosslinked ClpAP (A–P) and uncrosslinked controls consisting of wild-type ClpA (ClpAWT), cysteine-free ClpA (ClpACF), or E613CClpA‡ and either wild-type ClpP (ClpPWT) or ClpP+C. (B) Degradation of cp7GFP-ssrA (20 µM) by crosslinked (A–P) and uncrosslinked ClpAP (A•P) variants, as shown in panel (A). A•P and uncrosslinked E613CClpA‡ClpP+C degrade cp7GFP-ssrA (20 µM) at similar rates as wild-type ClpAP and other uncrosslinked controls, and faster than crosslinked A–P. Values are means ± 1 SD (n ≥ 3) and provided in Figure 3—source data 5.

### Mechanistic implications of crosslinked complex activity

Models in which ClpA or ClpX must rotate with respect to ClpP to allow substrate translocation (Figure 1B–C) predict that crosslinking ClpA or ClpX to ClpP would abolish protein degradation by stopping rotation and linked sequential movements of ClpA/ClpX subunits through each position in the spiral. Our experimental results do not support these models. Rather, we find that preventing rotation by ‘riveting’ the ClpA ring to the ClpP ring still permits substantial degradation of native and denatured protein substrates in vitro. ClpXP complexes in which one IGF loop is crosslinked to ClpP can also degrade folded and unfolded substrates, albeit at lower rates than uncrosslinked controls (Bell, 2020). The high degree of crosslinking in our ClpAP experiments, where 98% of complexes contain at least four covalent crosslinks between ClpA and ClpP, and ~50% of complexes are predicted to contain six crosslinks (Figure 2—figure supplement 1), would be expected to hinder each ClpA subunit from adopting each position in the spiral by affecting conformational accessibility, especially near the ClpP interface. Moreover, in approximately half of the crosslinked enzymes, it would not be possible to have two empty ClpP clefts. Hence, the proposal that this intermediate is a requisite step in translocation, as proposed for ClpXP (Ripstein et al., 2020), is also inconsistent with our results. Lopez et al., 2020 proposed that ClpA and ClpP might rotate in defined contexts, for example during the degradation of very stable substrates. Although we cannot exclude this possibility, we prefer simpler models in which the basic mechanism of AAA+ protease function does not change in a substrate-specific manner. As we observe reduced rates of degradation of folded substrates when ClpA and ClpP are crosslinked, conformational flexibility between the unfoldase and protease appears to be important for optimal unfolding. However, rotation of the ClpA or ClpX rings with respect to ClpP is clearly not a strict requirement for degradation. We suggest, therefore, that ring-ring rotation models be considered to be both unproven and unlikely in the absence of direct evidence for such rotation.

AAA+ proteases in the FtsH/Yme1/Agf3l2 and Lon families have AAA+ and peptidase modules that are genetically tethered as part of the same polypeptide chain and therefore also must operate without rotation between the unfoldase and protease components (Glynn, 2017). For ClpAP, a non-rotary mechanism could be explained by the sequential hand-over-hand mechanism if the empty ClpP cleft can localize between any pair of ClpA subunits. Alternative mechanisms, such as the reciprocating action of one or two AAA+ subunits, might also explain both the observed pattern of unfoldase-protein interactions seen in cryo-EM structures and the robust degradation activity of genetically or biochemically tethered AAA+ proteases against multiple substrates. Further experiments will be required to discriminate between these models.

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
      <td>Gene (Escherichia coli)</td>
      <td>clpA</td>
      <td></td>
      <td></td>
      <td>UniProtKB - P0ABH9</td>
    </tr>
    <tr>
      <td>Gene (Escherichia coli)</td>
      <td>clpP</td>
      <td></td>
      <td></td>
      <td>UniProtKB - P0A6G7</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>T7 Express</td>
      <td>New England Biolabs</td>
      <td>C2566I</td>
      <td>Chemically competent cells</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pT7 ClpP+C (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>For overexpression of C-terminally His6-tagged ClpP (C91V, C113A) with extra Cys residue for crosslinking. Progenitor: pT7 ClpP-TEV-cHis6(Stinson et al., 2013; Amor et al., 2016)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET23b His7SumoFLAG E613CClpA‡(plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>For overexpression of ClpA with Cys substitution and C47S, C203S, C243S background for crosslinking. Progenitor: pET23b His7Sumo ClpAcfΔC9 (Zuromski et al., 2020)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET23b His7Sumo ClpAcfΔC9 (plasmid)</td>
      <td>Zuromski et al., 2020</td>
      <td></td>
      <td>For overexpression of cysteine-free ClpA (ClpACF) harbouring C47S, C203S, C243S mutations</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>WT ClpA (plasmid)</td>
      <td>Seol et al., 1994, Hou et al., 2008</td>
      <td></td>
      <td>WT ClpA (M169T background) for overexpression</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ClpP-His6(plasmid)</td>
      <td>Kim et al., 2001</td>
      <td></td>
      <td>WT ClpP for overexpression</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>cp7GFP-ssrA (plasmid)</td>
      <td>Nager et al., 2011</td>
      <td></td>
      <td>Circularly permutated variant of superfolder GFP-ssrA for overexpression</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>V13P titinI27-ssrA (plasmid)</td>
      <td>Kenniston et al., 2003</td>
      <td></td>
      <td>ssrA-tagged I27 domain variant for overexpression</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>His6SUMO λ cIN-ssrA (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>ssrA-tagged residues 1–93 of λ cI (UniProtKB - P03034) for overexpression</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Bismaleimidoethane</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat # 22323</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Adenosine 5ʹ-O-(3-Thiotriphosphate), Tetralithium Salt</td>
      <td>Millipore Sigma</td>
      <td>Cat# 119120–25 MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>5-Iodoacetamidofluorescein</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# I30451</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Casein fluorescein isothiocyanate from bovine milk (FITC-casein)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# C0528-10MG</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Proteins

The gene encoding E. coli ClpP+C was generated using PCR mutagenesis, and the corresponding protein was purified by established protocols (Martin et al., 2005) and stored in buffer containing 0.5 mM dithiothreitol (DTT). Wild-type ClpP (ClpPWT) was purified by established protocols (Kim et al., 2001). The plasmid for E613CClpA‡ was generated by PCR mutagenesis of E. coli ClpAΔC9 fused to the 3′-end of His7SumoFLAG cloned into pET23b (Novagen). His7SumoFLAG-E613CClpA‡ was overexpressed in T7Express (New England Biolabs), and initially purified by Ni-NTA chromatography. Following ULP-1 cleavage to remove His7Sumo, E613CClpA‡ was further purified by SP-Sepharose cation-exchange chromatography and stored in 50 mM HEPES-KOH (pH 7.5), 300 mM NaCl, 20 mM MgCl2, 10% glycerol, and 2 mM TCEP. Cysteine-free (ClpACF) and wild-type (ClpAWT) were purified by established protocols (Zuromski et al., 2020; Hou et al., 2008). The cp7GFP-ssrA and V13P titinI27-ssrA proteins were purified as described (Nager et al., 2011; Kenniston et al., 2003). V13P titinI27-ssrA was labeled with 5-iodoacetamidofluorescein (5-IAF) for fluorescent assays as described (Iosefson et al., 2015). The plasmid for λ cIN-ssrA was generated by PCR mutagenesis of a gene encoding amino acids 1–93 the bacteriophage λ cI repressor. This construct was fused to the 3'-end of His6Sumo cloned into pET23b and appended with the C-terminal ssrA degron. His6Sumo-λ cIN-ssrA was purified by Ni-NTA chromatography, ULP-1 cleavage, Ni-NTA chromatography to remove the His6Sumo fragment, Mono-Q anion-exchange chromatography, and Superdex-75 size-exclusion chromatography, and stored in 25 mM HEPES-KOH (pH 7.5), 150 mM NaCl, 10% glycerol, and 1 mM DTT. ClpA and variant concentrations were calculated as hexamer equivalents, and ClpP and variant concentrations were calculated as tetradecamer equivalents.

### Crosslinking ClpA to ClpP

E613CClpA‡ (4 μM) and ClpP+C (9.6 μM) were mixed in a total volume of 2.5 mL and desalted into 50 mM HEPES-KOH (pH 7), 300 mM NaCl, 20 mM MgCl2, 10% glycerol, and 5 mM EDTA using a Sephadex G-25 PD-10 column (GE Healthcare). After diluting to a final volume of 5 mL, crosslinking was initiated by addition of 5 mM ATPγS and 200 μM bismaleimidoethane (BMOE; Thermo Fisher) and allowed to proceed at room temperature for 45 min. The reaction was quenched by addition of 50 mM DTT at room temperature for 20 min before purification by Superdex-200 size-exclusion chromatography in 50 mM HEPES-KOH (pH 7.5), 300 mM NaCl, 20 mM MgCl2, 10% glycerol, and 2 mM TCEP. The purified A–P pool was used for all subsequent biochemical assays. Quantification of crosslinking and the concentration of A–P were measured by quantifying Coomassie-stained SDS-PAGE bands relative to E613CClpA‡ standards. The area under the curve (AUC) corresponding to pixel intensities of the crosslinked and uncrosslinked species were quantified by ImageQuant (GE Healthcare) after scanning Coomassie-stained SDS-PAGE using a Typhoon FLA 9500 (GE Healthcare). Crosslinking efficiency was measured in four independent replicates by multiplying the calculated concentration of each species by the volume loaded in each lane, and calculated as:

$$
Efficiency=\frac{picomolesA−P_{Crosslinked}}{picomolesA−P_{Crosslinked}+picomoles^{E613C}ClpA_{Uncrosslinked}^{‡}}
$$

### Biochemical assays

We determined the concentration of E613CClpA‡–ClpP+C by a standard-curve comparison to E613CClpA‡ (Figure 2C). We calculated the concentration of the uncrosslinked E613CClpA‡ species by measuring the absorbance at 280 nm (ε = 32890 M−1 cm−1) using a NanoDrop One UV-Vis Spectrophotometer (Thermo-Fisher Scientific), ATP-hydrolysis assays were performed using an NADH-coupled assay (Martin et al., 2005) at 30°C in Buffer HO (25 mM HEPES-KOH, pH 7.5, 300 mM NaCl, 20 mM MgCl2, 10% glycerol, 2 mM TCEP) with 5 mM ATP and 0.25 µM E613CClpA‡ and 0.75 µM ClpPWT for the A•P control; 0.25 µM E613CClpA‡–ClpP+C for the A–P pool; or the combinations of 0.25 µM ClpAWT, ClpACF, or E613CClpA‡ and 0.75 µM ClpPWT or ClpP+C listed in Figure 3—figure supplement 1A. Degradation reactions were performed at 30°C in Buffer HO with 4 mM ATP and an ATP-regeneration system consisting of 50 μg/mL creatine kinase (Millipore-Sigma) and 5 mM creatine phosphate (Millipore-Sigma). Degradation of cp7GFP-ssrA was monitored by loss of substrate fluorescence (excitation 467 nm; emission 511 nm) using a SpectraMax M5 plate reader (Molecular Devices) (Nager et al., 2011). The cp7GFP-ssrA concentration was 20 µM in Figure 3B and Figure 3—figure supplement 1B; concentrations varying from 0.31 to 80 µM in Figure 3D contained 0.25 µM E613CClpA‡ and 0.75 µM ClpPWT for the A•P control or 0.25 µM E613CClpA‡–ClpP+C for the A–P pool. In the cp7GFP-ssrA degradation assays shown in Figure 3—figure supplement 1B, degradation reactions for uncrosslinked controls included the indicated combinations of 0.25 µM ClpAWT, ClpACF, or E613CClpA‡ and 0.75 µM ClpPWT or ClpP+C, in addition to 0.25 µM E613CClpA‡ and 0.75 µM ClpPWT for the A•P control or 0.25 µM E613CClpA‡–ClpP+C for the A–P pool. Degradation of FITC-casein (18 µM, Sigma-Aldrich) containing 0.25 µM E613CClpA‡ and 0.75 µM ClpPWT for the A•P control or 0.25 µM E613CClpA‡–ClpP+C for the A–P pool was monitored by increase in fluorescence (excitation 340 nm; emission 520 nm); to determine the endpoint of complete FITC-casein degradation, 0.5 µL of 5 mg/mL porcine elastase (Sigma-Aldrich) was added to each well and incubated for 30 min. ClpAP degradation reactions with FITC-casein (18 µM) were performed at 30°C in Buffer HO with 4 mM ATP or ATPγS (Millipore Sigma). Degradation of 5-IAFV13P titinI27-ssrA (5 µM) containing 0.2 µM E613CClpA‡ and 0.5 µM ClpPWT for the A•P control or 0.2 µM E613CClpA‡–ClpP+C for the A–P pool was monitored by increase in fluorescence (excitation 494 nm; emission 518 nm). Gel degradation of λ cIN-ssrA (15 µM monomer) containing 0.2 µM E613CClpA‡ and 0.4 µM ClpPWT for the A•P control or 0.2 µM E613CClpA‡–ClpP+C for the A–P pool was performed in triplicate by taking samples of each reaction at specific time points, stopped by addition of SDS-PAGE loading sample and boiling at 100°C before loading on Tris-Glycine-SDS gels. Bands were visualized by staining with colloidal Coomassie G-250 and quantified by ImageQuant (GE Healthcare) after scanning by Typhoon FLA 9500 (GE Healthcare). The fraction of λ cIN-ssrA remaining was calculated by dividing the intensity of this band at a given time point by the density at time zero, after normalization by the creatine kinase density. The biochemical assays were performed with A–P from a single preparation to ensure that crosslinking efficiency was the same throughout all assays. All experiments were performed in at least three independent replicates and values reported were calculated as the mean ±1 SD of independent replicates or the ratio of means ± propagated error of independent replicates. Propagated error for ‘fractional degradation rate (rate of A–P/rate of A•P)’ of A–P mean activity compared to A•P mean activity was computed as:

$$
Propagatederrorof\frac{mean_{A-P}}{mean_{A∙P}}= \frac{mean_{A-P}}{mean_{A∙P}}\sqrt{(\frac{SD_{A−P}}{mean_{A−P}})^{2}+(\frac{SD_{A∙P}}{mean_{A∙P}})^{2}}
$$
