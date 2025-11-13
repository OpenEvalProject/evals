# A conserved MCM single-stranded DNA binding element is essential for replication initiation

## Authors

- Clifford A Froelich<sup>1</sup>
- Sukhyun Kang<sup>2</sup>
- Leslie B Epling<sup>1</sup>
- Stephen P Bell<sup>2</sup> †
- Eric J Enemark<sup>1</sup> †

### Affiliations

1. Department of Structural Biology St Jude Children’s Research Hospital Memphis United States
2. Howard Hughes Medical Institute, Massachusetts Institute of Technology Cambridge United States

† Corresponding author

## Abstract

The ring-shaped MCM helicase is essential to all phases of DNA replication. The complex loads at replication origins as an inactive double-hexamer encircling duplex DNA. Helicase activation converts this species to two active single hexamers that encircle single-stranded DNA (ssDNA). The molecular details of MCM DNA interactions during these events are unknown. We determined the crystal structure of the Pyrococcus furiosus MCM N-terminal domain hexamer bound to ssDNA and define a conserved MCM-ssDNA binding motif (MSSB). Intriguingly, ssDNA binds the MCM ring interior perpendicular to the central channel with defined polarity. In eukaryotes, the MSSB is conserved in several Mcm2-7 subunits, and MSSB mutant combinations in S. cerevisiae Mcm2-7 are not viable. Mutant Mcm2-7 complexes assemble and are recruited to replication origins, but are defective in helicase loading and activation. Our findings identify an important MCM-ssDNA interaction and suggest it functions during helicase activation to select the strand for translocation.

## Introduction

Mcm proteins were first identified in yeast when mutations in their genes were defective for minichromosome maintenance (Maiorano et al., 2006). In eukaryotic cells, six related Mcm proteins (Mcm2-7) form a ring-shaped heterohexamer, the Mcm2-7 complex. Hexameric MCM rings act as the replicative DNA helicase (Bochman and Schwacha, 2008; Ilves et al., 2010), encircling the leading strand DNA template at the replication fork (Fu et al., 2011). Replication forks are established in a cell-cycle-regulated manner at specific regions of DNA called replication origins (Bell and Dutta, 2002). Mcm2-7 complexes are loaded onto double-stranded DNA at each replication origin by the Origin Recognition Complex (ORC), Cdc6, and Cdt1 (Remus and Diffley, 2009). Because replication origins are located far from the DNA ends, loading of Mcm2-7 hexamers such that they encircle double-stranded DNA requires opening of the Mcm2-7 ring. A ‘gate’ between the Mcm2 and Mcm5 subunits has been identified and is the likely site of ring opening and closing (Bochman and Schwacha, 2007, 2008; Costa et al., 2011). After helicase loading, the two Mcm2-7 complexes encircle double-stranded DNA (dsDNA) as a head-to-head double hexamer (Evrin et al., 2009; Remus et al., 2009) that is inactive as a helicase.

Helicase activation requires substantial remodeling of the initially loaded Mcm2-7 double hexamer. The Dbf4-dependent Cdc7 kinase (DDK) and cyclin-dependent kinases (CDKs) drive recruitment of two Mcm2-7 activating proteins, Cdc45 and the tetrameric GINS complex (Labib, 2010). These proteins together stimulate the Mcm2-7 ATPase and helicase (Ilves et al., 2010) and with Mcm2-7 form the active replicative DNA helicase, the CMG complex (Cdc45-Mcm2-7-GINS) (Moyer et al., 2006; Bochman and Schwacha, 2008; Ilves et al., 2010). The initially loaded double-hexamer has the capacity to passively slide over dsDNA (Evrin et al., 2009; Remus et al., 2009), suggesting MCM DNA interactions are not fixed at this stage. Upon activation, the two Mcm2-7 helicases translocate independently (Yardimci et al., 2010) in a 3′→5′ direction on the single-stranded leading strand DNA template (Fu et al., 2011). This transformation necessitates two structural changes in the initially loaded double-hexamer that are poorly understood: (i) the double-hexamer interface must be broken to allow independent replisome movement; (ii) the dsDNA at the origin must be melted and the lagging strand DNA template excluded from the central channel of each MCM hexamer. How Mcm2-7 retains one strand in its central channel while excluding the other during this transition is unknown.

Each Mcm subunit contains three domains. The N-terminal domain (MCMN) possesses an OB (oligonucleotide/oligosaccharide binding)-fold and usually a zinc-binding motif (Fletcher et al., 2003). This domain mediates the head-to-head interaction of the two hexamers (Gomez-Llorente et al., 2005; Evrin et al., 2009; Remus et al., 2009). The second domain contains a conserved ATPase AAA+ fold (Neuwald et al., 1999), which binds and hydrolyzes ATP at subunit interfaces around the hexameric ring (Schwacha and Bell, 2001; Davey et al., 2003) and is required for DNA unwinding (Bochman and Schwacha, 2008; Ilves et al., 2010). A short domain at the C-terminus includes a helix-turn-helix fold (Aravind and Koonin, 1999), one of which (Mcm6) interacts with Cdt1 (Wei et al., 2010). MCM hexamers demonstrate a two-tiered ring architecture in electron microscopy studies with an N-terminal domain tier and an ATPase domain tier (Chong et al., 2000; Pape et al., 2003; Gomez-Llorente et al., 2005; Costa et al., 2006; Bochman and Schwacha, 2007; Remus et al., 2009; Costa et al., 2011). The MCM complexes of several archaeal organisms consist of six identical subunits and have provided powerful models to investigate the atomic details of MCM structure. Crystal structures have identified a consistent hexameric arrangement for MCMN of Methanothermobacter thermautotrophicus (Mt) (Fletcher et al., 2003) and Sulfolobus solfataricus (Sso) (Liu et al., 2008) that correspond to the smaller tier observed by electron microscopy (Remus et al., 2009; Costa et al., 2011). Although no atomic structure has been determined for the complete archaeal or eukaryotic Mcm hexamer, hypothetical atomic models for full-length archaeal MCM hexamers have been generated by superimposition of six copies of a monomeric crystal structure of nearly full-length MCM onto the hexameric structure of MtMCMN (Brewster et al., 2008; Bae et al., 2009).

Despite a growing understanding of the overall structure of the MCM complex, its multiple interactions with DNA during helicase loading, activation and elongation remain mysterious. Atomic structures of MCM bound to DNA have not been reported. Given the different forms of DNA that are bound to the MCM complex during the steps of the initiation pathway, the MCM proteins must transition between different DNA interactions during this process. To investigate the interactions after origin melting and how the MCM hexamer selectively encircles the leading strand template, we determined the crystal structure of the MCMN hexamer of Pyrococcus furiosus bound to ssDNA. We present an analysis of this the structure and biochemical and genetic characterizations of archaeal and S. cerevisiae proteins with mutations in the identified ssDNA binding region. These findings reveal two residues on the surface of the MCM OB-fold that are critical for MCM DNA-binding and contribute to multiple Mcm2-7 functions during replication initiation. Our findings support a model in which the identified MCM-ssDNA interactions contribute to the selection of the leading strand DNA template during helicase activation.

## Results

To elucidate how MCM interacts with ssDNA, we determined the crystal structure of the N-terminal domain of the Pyrococcus furiosus MCM (PfMCMN) protein in complex with homopolymeric (dT)30 ssDNA (Table 1).

**Table 1.**
 Data collection and refinement statistics


<table>
  <thead>
    <tr>
      <th></th>
      <th>PfMCMN:dT30</th>
      <th>PfMCMN (no DNA)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P21</td>
      <td>P21</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>94.276, 113.397, 196.854</td>
      <td>122.849, 103.064, 122.435</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 101.354, 90</td>
      <td>90, 119.85, 90</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>50-3.20 (3.31–3.20)</td>
      <td>50-2.65 (2.74–2.65)</td>
    </tr>
    <tr>
      <td>Rsym</td>
      <td>0.109 (0.786)</td>
      <td>0.100 (0.569)</td>
    </tr>
    <tr>
      <td>I/σI</td>
      <td>13.4 (1.64)</td>
      <td>16.3 (2.26)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>100 (100)</td>
      <td>98.8 (98.2)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>4.1 (4.1)</td>
      <td>3.7 (3.7)</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>50-3.20 (3.29–3.20)</td>
      <td>50-2.65 (2.72–2.65)</td>
    </tr>
    <tr>
      <td>No. reflections</td>
      <td>63497/3376 (4453/218)</td>
      <td>72376/3839 (5183/285)</td>
    </tr>
    <tr>
      <td>Rwork/Rfree</td>
      <td>0.257/0.294 (0.372/0.373)</td>
      <td>0.259/0.270 (0.484/0.502)</td>
    </tr>
    <tr>
      <td>No. atoms</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>24359</td>
      <td>12258</td>
    </tr>
    <tr>
      <td>DNA</td>
      <td>584</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Zn2+</td>
      <td>12</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>B-factors</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>129</td>
      <td>78</td>
    </tr>
    <tr>
      <td>DNA</td>
      <td>179</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Zn2+</td>
      <td>204</td>
      <td>145</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>R.m.s. deviations</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.008</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>1.164</td>
      <td>1.361</td>
    </tr>
  </tbody>
</table>

### MCM-ssDNA molecular architecture

The asymmetric unit of the crystal of PfMCMN:ssDNA contains two independent hexamers, each bound to ssDNA (Figure 1, Figure 1—figure supplements 1,2; Video 1). The subunits are referred to as A through F (hexamer 1) and G through L (hexamer 2). Like SsoMCMN (Pucci et al., 2007; Liu et al., 2008), PfMCMN elutes as a monomer by size-exclusion chromatography (data not shown) but adopts a hexameric arrangement in the crystal structure. The structure is similar to those of MtMCMN (Fletcher et al., 2003) and SsoMCMN (Liu et al., 2008) with three subdomains (Figure 1—figure supplement 3): a largely helical subdomain A; a Zn-binding subdomain B; and an OB-fold subdomain C. The central pore of the PfMCMN hexameric ring is oval-shaped with a variable diameter around the ring reflecting a significant deviation from pure sixfold symmetry. The RMSD of the C-subdomain Cα-positions from the sixfold permutation is 3.03 Å and 1.45 Å for hexamers 1 and 2, respectively. In contrast, PfMCMN without DNA bound is highly symmetric and shows minimal RMSD from sixfold symmetry (Figure 1—figure supplements 4–6, RMSD = 0.33 Å), indicating that DNA induces asymmetry in the MCM ring. The narrowest diameter of the channel is at the β-turn of the C-subdomain (Figure 1—figure supplement 3), consistent with previous structures of MCMN (Fletcher et al., 2003; Liu et al., 2008).

![Figure 1.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig1-v1.jpg)

**Figure 1.:** The ssDNA is colored cyan. (A) Each subunit is uniquely colored and labeled. The side-chains of the two MSSB arginine residues that bind ssDNA are represented in stick. The Zn-binding domains project into the page. The ATPase domains, not present in the crystal structure, would project out of the page. (B) The protein is represented in transparent grey to highlight that the ssDNA runs perpendicular to the channel. The Zn-binding domains are at the bottom, and the ATPase domains would be located at the top.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** The ssDNA is colored cyan. (A) Each subunit is uniquely colored and labeled. For hexamer 1, an example MSSB and β-turn are labeled. The Zn-binding domains are projected into the page. The ATPase domains (not present in the crystal structure) would project out of the page. The 5′ and 3′ ends of the ssDNA are marked. (B) The protein is represented in transparent grey to highlight that the ssDNA runs perpendicular to the channel. The Zn-binding domains are at the bottom, and the ATPase domains (not present) would be at the top.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** The final model is displayed with the 2 subunits colored and labeled in yellow and cyan and the DNA colored blue. The Fo-Fc electron density is contoured at 3-sigma (red) and 5-sigma (green). The DNA backbone is visible at 3-sigma, and the phosphates are visible at 5-sigma.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) The individual subdomains are color-coded with the helical bundle in blue, the Zn-binding subdomain in green, the OB-fold subdomain in magenta, and the ssDNA in cyan. (B) Cylindrical merge showing how closely MCMN approaches the channel center at each position along the channel axis, and that the greatest available volume in the MCMN channel is at the OB-fold above the β-turn. The hexamer was rotated 360° about the channel axis in 5° increments. All of the models were superimposed, and the Cα positions of each subdomain were used to generate surfaces with MSMS (Sanner et al., 1996). The surfaces were uniquely colored as in (A), rendered simultaneously with Raster3D (Merritt and Bacon, 1997), and clipped with a vertical plane through the center to show the extent of projection into the channel for each part of the hexamer. A grey cylinder (unclipped) with 20 Å diameter was placed in the center to indicate the volume for a hypothetical B-form DNA. A similar 360° cylindrical merge was constructed for one of the contiguous ssDNA molecules, and a surface was constructed over all ssDNA atoms. The ssDNA surface was clipped with a vertical plane through the center, and is represented in cyan (right).

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** Each subunit is uniquely colored and labeled. (A) The side-chains of the two arginine residues of the MSSB are represented in stick, and the Zn-binding domains are projected into the page. The ATPase domains, not present in the crystal structure, would project out of the page. (B) The Zn-binding domains are at the bottom, and the ATPase domains would be located at the top.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** The MSSB arginines are shown in stick representation. The two hexamers are superimposed based upon least-squares alignment of the six C-subdomains (middle). The oval shape of the ssDNA-bound ring is apparent at the red (chain A) and green (chain D) subunits, which are further from the channel center than in the DNA-free structure.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig1-figsupp6-v1.jpg)

**Figure 1—figure supplement 6.:** For each hexamer, the least-squares superposition of all six subunits upon the permuted configuration (chains ABCDEF superimposed upon BCDEFA) was calculated based upon the C-subdomains.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig1-figsupp7-v1.jpg)

**Figure 1—figure supplement 7.:** Left panels show one monomer of PfMCMN (chain F) colored yellow, and the other subunits of the hexamer colored grey. The ssDNA bound by PfMCMN is in cyan. (A) One monomer of E. coli SSB (Raghunathan et al., 2000) is shown in magenta and its associated ssDNA in blue in the right panel. An overlay with ssDNA bound PfMCMN is shown in the middle. (B) Comparison of PfMCMN:ssDNA with one monomer of H. pylori SSB (Chan et al., 2009) in magenta and its associated ssDNA in blue. Note the ∼90° change in direction of ssDNA for the PfMCM compared to the SSB structures.

![Video 1.](https://cdn.elifesciences.org/articles/01993/elife-01993-media1.mov.jpg)

**Video 1.:** The video illustrates the asymmetric unit, which includes two MCM hexamers in a side-by-side orientation. Each subdomain is illustrated in Hexamer 1 to show that the ssDNA interacts with the OB-fold subdomain C. Finally, detailed views of the β-turn and the MCM Single-Stranded DNA binding motif (MSSB) are illustrated.

The ssDNA binds inside the central channel of the hexameric ring in an intriguing configuration. The ssDNA circles the interior of the PfMCMN ring in a plane perpendicular to the central channel (Figure 1, Figure 1—figure supplement 1). This is in contrast to the ssDNA passing through the central channel, as observed in the structures of the nucleic acid complexes of the motor domains of the hexameric helicases E1 (Enemark and Joshua-Tor, 2006), Rho (Thomsen and Berger, 2009), and DnaB (Itsathitphaisarn et al., 2012). This distinction suggests that the newly identified MCM-ssDNA interactions might serve a function distinct from motor-driven helicase and translocase activities. The ssDNA binds to the MCMN OB-fold subdomain C at a region consistent with that of the prototype OB-fold protein SSB, but the ssDNA is oriented approximately perpendicular to that seen in SSB-ssDNA structures (Figure 1—figure supplement 7, Raghunathan et al., 2000; Chan et al., 2009). The ssDNA does not progress towards a specific end of the channel; therefore, the ssDNA does not have an assignable entry or exit direction from the ring. Instead, the ssDNA has a defined polarity relative to the MCM ring. When viewed from the C-terminal side of the complex (as shown in Figure 1A), the 5′ to 3′ direction of the bound ssDNA proceeds clockwise around the channel. This polarity is observed for both ssDNAs in each hexamer of the asymmetric unit.

The structure reveals that the individual MCM subunits do not all simultaneously participate in ssDNA binding. In each hexamer, the bound nucleotides are not continuous but are separated into two stretches. Overall, two 7-mer stretches are observed in hexamer 1, and 11-mer and 4-mer stretches are observed in hexamer 2. The subunits that interact with DNA use a consistent binding mode with four nucleotides per subunit (Figure 1, Figure 2, Figure 2—figure supplement 1). The fourth nucleotide from the 5′-end of this binding mode is visible in the cases where it spans binding at adjacent subunits, but it is often disordered at the 3′-end of a ssDNA stretch. The four nucleotide per subunit binding increment contrasts with the motor domains of other hexameric helicases that bind either one (E1, Enemark and Joshua-Tor, 2006; Rho, Thomsen and Berger, 2009) or two (DnaB, Itsathitphaisarn et al., 2012) nucleotides per subunit and indicates that 24 nucleotides can bind if all the subunits simultaneously engage the ssDNA. The absence of ssDNA binding at some subunits is not due to insufficient DNA length because a 30-mer oligonucleotide was used for crystallization. The discontinuous DNA could result from the hexamer binding two separate 30-mer strands simultaneously or from the hexamer tightly binding one 30-mer ssDNA strand at two regions with the intervening nucleotides binding either weakly or not at all. We consider the latter to be more likely because binding of two parts of the same strand is anticipated to be cooperative.

![Figure 2.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig2-v1.jpg)

**Figure 2.:** The binding predominantly involves residues on the face of the OB-fold of one subunit, yellow, including an interaction between a thymidine base and main-chain atoms of the β-strand. This thymidine is sandwiched between F202 of one subunit and E127 of the adjacent subunit in cyan. Lysine 129 of the neighboring subunit (cyan) interacts with both the DNA and the yellow subunit. The specific interfaces depicted are (top) between chains F (yellow) and A (cyan) and (bottom) between chains A (yellow) and B (cyan). The structural details of DNA-binding appear highly similar at the other interfaces where DNA is observed (see Figure 2—figure supplement 1). The main interactions involve R124 and R186. The presence of ssDNA correlates with the proximity of the two subunits as defined by the distance between the R201 Cα and E127 Cα positions (magenta arrow).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Electron density following refmac refinement (refmac FWT map) is displayed around DNA in green, and around the protein in blue. The adjacent subunits are colored yellow and cyan, and the specific chains are noted with the same color scheme. The distance between the R201 Cα atom of the yellow subunit and the E127 Cα atom of the cyan subunit is displayed in red. Electron density for ssDNA is observed for each interface where the distance is less than 7.5 Å.

The capacity of a subunit to bind ssDNA is determined by intersubunit distance (Figure 1, Figure 2, Figure 2—figure supplement 1). To compare the distance between different subunit pairs, we measured the distance between the R201 Cα atom of one subunit and the E127 Cα atom of the counterclockwise subunit as viewed in Figure 1 (Magenta arrow, Figure 2). DNA-binding is consistently observed at the first subunit if this distance is less than 7.5 Å, and it is not observed if this distance exceeds 8.4 Å. The interface between subunits J and K shows an intermediate (7.6 Å) distance, and the electron density between F202 (subunit J) and E127 (subunit K) is much weaker than at the interfaces where DNA has been modeled (Figure 2—figure supplement 1). The correlation of ssDNA binding with intersubunit configuration is conceptually similar to multi-subunit ATPase sites where different intersubunit configurations determine the ability to bind or hydrolyze ATP (Abrahams et al., 1994; Enemark and Joshua-Tor, 2008). In MCMN, changes to the intersubunit configuration dictate binding to ssDNA.

### Conserved residues on the OB-fold bind ssDNA

The most significant interactions between PfMCMN and ssDNA involve two adjacent arginines, R124 and R186, that project from the β-barrel of the OB-fold towards the ring interior (Figures 1 and 2). These residues interact with oxygen atoms of the sugars and bases of the ssDNA (Figure 2) and are highly conserved in other MCM proteins (Figure 3). We refer to this conserved region as the MCM Single-Stranded DNA Binding motif (MSSB). Interestingly, one thymidine base projects towards the β-barrel of the OB-fold (Figure 2) and makes two hydrogen bonds to main-chain atoms of one strand of the β-barrel. This base also sits at the subunit interface, between the side-chains of phenylalanine 202 of one subunit and glutamic acid 127 of the adjacent subunit. The β-turn residues R234 and K236 do not interact with ssDNA in the structure. The DNA-binding consists predominantly of interactions with the sugars and bases rather than the backbone phosphates. In contrast, the hexameric helicases E1 (Enemark and Joshua-Tor, 2006); Rho (Thomsen and Berger, 2009); and DnaB (Itsathitphaisarn et al., 2012) bind nucleic acid mainly through interactions with backbone phosphates.

![Figure 3.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig3-v1.jpg)

**Figure 3.:** Globally conserved residues are shaded dark blue, and family-specific conserved residues are shaded light blue. Residues identified to participate in DNA-binding from our structure (red dot) and prior work (Pucci et al., 2004) (lavendar dot) are noted above the sequences. Conserved residue positions for ssDNA binding are shaded red and correspond to R124 and R186 in PfMCM (Figure 2). pf = Pyrococcus furiosus; mt = Methanothermobacter thermautotrophicus; sso = Sulfolobus solfataricus; ap = Aeropyrum pernix; gi = Giardia lamblia; aq = Amphimedon queenslandica; cr = Chlamydomonas reinhardtii; sc = Saccharomyces cerevisiae; sp = Schizosaccharomyces pombe; at = Arabidopsis thaliana; ce = Caenorhabditis elegans; dm = Drosophila melanogaster; xl = Xenopus laevis; dr = Danio rerio; gg = Gallus gallus; hs = Homo sapiens.

We investigated the role of the identified residues in MCM DNA binding using mutational analysis and electrophoretic mobility shift assays. As expected, wild-type PfMCMN binds single-stranded (Figure 4, Khalf = 6.8 μM) and double-stranded (Figure 4—figure supplement 1, Khalf = 7.0 μM) oligonucleotides. The arginine residues R124 and R186 make the most significant ssDNA interactions in the structure. R124A and R186A mutants each show a significant decrease in ssDNA binding (7- and 6-fold reduction, respectively). Simultaneous mutation of both arginines showed even stronger defects (25-fold reduction), with no detectable ssDNA binding unless the protein concentration was increased dramatically (Figure 4). The K129A mutant is modestly defective in binding ssDNA (fourfold reduction, Figure 4). The individual R124A, R186A, and K129A mutants bind dsDNA with comparable affinity to wild-type (Figure 4—figure supplement 1). The R124A/R186A double mutant shows only modest defects in dsDNA binding (threefold reduction). Alanine mutants of other less-conserved residues did not significantly impair ssDNA- or dsDNA-binding. For example, consistent with the involvement of its main chain amide rather than its side chain in ssDNA binding, the β-turn K233A mutant does not significantly impair ssDNA binding. Similarly, the F202 side-chain interacts with a thymidine base, but it is offset from an ideal stacking interaction (Figure 2). The corresponding F202A mutant is not impaired in ssDNA binding and is not conserved as aromatic in other Mcm proteins (Figure 3).

![Figure 4.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig4-v1.jpg)

**Figure 4.:** The ssDNA, 160 nM with a 5′-fluorescein-label, was titrated with increasing concentrations (1.4, 2, 2.7, 6.8, 13.5, 20.3, 27, 40.5, 54 μM) of PfMCMN. The lane marked ‘−’ is loaded with control sample lacking protein. Mutation of residues R124 and R186 significantly impairs binding to ssDNA. The R124A/R186A double mutant was titrated with larger concentrations (54, 81, 108, 135, 162, 189, 216, 243, 270 μM) of PfMCMN in order to detect binding.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** The dsDNA, 160 nM with a 5′-fluorescein-label, was titrated with increasing concentrations (2, 3, 4, 5, 7.5, 10, 12.5, 15, 20 μM) of PfMCMN. The lane marked ‘−’ is loaded with control sample lacking protein. The R124A/R186A double mutant was slightly impaired in binding dsDNA and was titrated with larger concentrations (10, 12.5, 15, 17.5, 20, 25, 30, 35, 40 μM) of PfMCMN.

### Corresponding yeast MCM2-7 mutants are defective in vivo

In S. cerevisiae (Sc), the PfMCM R124 and R186 amino acids within the MSSB motif are both conserved as arginine or lysine in Mcm4, Mcm6 and Mcm7 whereas Mcm2, Mcm3 and Mcm5 show a positively charged residue at only one of the two sites (Figure 3). To test the role of the MSSB motif in S. cerevisiae DNA replication, we constructed double-alanine mutants in ScMCM4 (mcm4-R334A/K398A = mcm4D), ScMCM6 (mcm6-R296A/R360A = mcm6D) and ScMCM7 (mcm7-R247A/K314A = mcm7D) as these subunits showed the most similarity to PfMCM in the MSSB.

We tested the ability of these mutations to replace the corresponding wild-type Mcm subunit in S. cerevisiae cells. When present as the only mutant Mcm subunit in the cell, mutations in the ScMCM4, ScMCM6 or ScMCM7 MSSB complemented deletion of the corresponding gene (Figure 5A, Figure 5—figure supplement 1). Because the DNA binding defects observed for the mutant PfMCM complexes altered all six subunits, we tested the ability of pairwise combinations of the ScMCM MSSB mutations to function in place of their wild-type counterparts. In contrast to the single mutations, all three double-mutant combinations did not support cell division. The dramatic phenotypic difference between the double and single mutations may be due to a requirement for two adjacent subunits to create a productive ssDNA interaction. Because the Mcm4, 6 and 7 subunits are adjacent to one another in the Mcm2-7 complex, each pairwise combination would be expected to interrupt at least three possible subunit pairs for binding (e.g., the Mcm4/6 double mutant would interfere with Mcm2/6, Mcm6/4 and Mcm4/7 subunit pairs for ssDNA binding).

![Figure 5.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig5-v1.jpg)

**Figure 5.:** Mutation of two MSSB motifs is lethal and causes helicase loading defects. (A) Mutation of two Mcm4, 6, 7 MSSB motifs is lethal. Subunit arrangement in the Mcm2-7 ring viewed from the C-terminal side. The Mcm4, 6, and 7 subunits are adjacent to each other across from the Mcm2/5 gate. All pairwise combinations of the Mcm4, 6 and 7 MSSB mutants are lethal whereas the individual MSSB mutants are viable. (B) Helicase loading with the indicated MSSB double mutant Mcm2-7 complexes. Three forms of the assay are shown: following a high-salt wash to monitor completion of loading (top panel); in the presence of ATPγS instead of ATP to monitor the initial association of the helicase and all of the helicase loading proteins (ORC, Cdc6 and Cdt1, middle panel); and with ATP following a low salt-wash, allowing bound helicase loading proteins to be maintained (bottom panel). All loading was dependent on Cdc6 and proteins are detected after SDS-PAGE and fluorescent protein staining.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** The parent strains have an MSSB mutation in the indicated MCM gene. They are also deleted for the indicated MCM gene and depend on a URA+ plasmid expressing a wild-type copy of the same gene for viability. These strains were transformed with the indicated (in the center of each plate) TRP+ plasmid expressing wild-type MCM gene (left) or the MSSB mutant MCM gene (right). Complementation in the absence of the URA3/MCMX-WT plasmid was tested by growth on plates containing 5-FOA (which selects against cells containing the URA3 plasmid). Consistent with the single mcm4, mcm6 or mcm7-MSSB mutations being viable, we observe growth in the presence of the pTRP/MCMX-WT plasmid but no growth when the TRP plasmid contains an MSSB allele in the second MCM gene (creating MSSB mutations in two of the MCM4/6/7 genes).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Wild-type and MSSB mutant Mcm2-7/Cdt1 complexes have similar subunit composition. Purified Mcm2-7/Cdt1 complexes were separated by SDS-PAGE and stained with coomassie blue. Mcm2-7 and Cdt1 proteins are indicated. (B) Wild-type and MSSB mutant complexes have similar Stokes radii. Wild-type and mutant Mcm2-7/Cdt1 complexes were separated on a Superdex 200 gel filtration chromatography. Fractions 16–19 of each separation are shown after SDS-PAGE and coomassie blue staining. (C) Helicase loading with the indicated MSSB mutant Mcm2-7 complexes. Three forms of the assay are shown: following a high-salt wash to monitor completion of loading (top panel); in the presence of ATPγS instead of ATP to monitor the initial association of all of the helicase and all of the helicase loading proteins (ORC, Cdc6 and Cdt1, third panel); and with ATP following a low salt-wash, allowing bound helicase loading proteins to be maintained (fourth panel). The relative loading of the Mcm mutants compared to wild-type Mcm2-7 was measured based on three independent loading (high-salt wash) experiments (second panel). Error bars indicate the standard deviation.

### S. cerevisiae MCM2-7 mutants exhibit helicase loading and replication initiation defects

To define further the molecular defects of the mutant S. cerevisiae Mcm2-7 complexes, we purified Mcm2-7 complexes containing the lethal double mutants (Mcm4D/6D, Mcm4D/7D and Mcm6D/7D) along with the associated Cdt1 protein. We also purified the Mcm4/6/7 triple mutant (Mcm4D/6D/7D) with associated Cdt1. After purification, all of the mutant complexes showed similar subunit composition and migration in gel filtration columns as wild-type Mcm2-7/Cdt1 (Figure 5—figure supplement 2). Thus, these mutations do not inhibit the initial assembly of the Mcm2-7/Cdt1 complex.

We tested each of the mutant complexes for their ability to be loaded onto origin DNA using a reconstituted helicase-loading assay (Evrin et al., 2009; Remus et al., 2009; Figure 5B). To ensure that all of the Mcm2-7 hexamers retained on the DNA were loaded, we washed the final DNA-associated proteins with high salt. This treatment removes all of the helicase loading proteins (ORC, Cdc6 and Cdt1) from the DNA but leaves loaded Mcm2-7 complexes (Figure 5B, top panel) (Randell et al., 2006). Wild-type protein showed robust, Cdc6-dependent loading onto origin DNA. In contrast, each of the double mutant Mcm2-7 complexes showed reduced Mcm2-7 loading. The Mcm4D/6D and Mcm6D/7D complexes showed only modest defects (less than ∼ two-fold, Figure 5—figure supplement 2). The Mcm4D/7D complex showed a stronger defect (∼10-fold), and the Mcm4/6/7 triple mutant showed the most severe defect in helicase loading (∼20-fold reduction, Figure 5—figure supplement 2).

To establish at what step in the helicase loading process these defects occurred, we studied the initial recruitment of the complexes to origin DNA. To this end, we replaced ATP with the poorly hydrolyzable ATP-γS in the assay. In the presence of ATPγS, all of the proteins required for helicase loading are recruited to the origin, but no loading occurs (Randell et al., 2006). Under these conditions, we observed a similar pattern of Mcm2-7/Cdt1 and ORC association for wild-type and the mutant Mcm2-7 complexes (Figure 5B, middle panel, Figure 5—figure supplement 2). Thus, mutating two or three MSSB motifs did not alter the initial recruitment of the Mcm2-7/Cdt1 complex to the origin DNA. We also examined the DNA-associated proteins when ATP-containing reactions were washed with low-salt (Figure 5B, bottom panel, Figure 5—figure supplement 2), a condition that retains helicase-loading proteins on DNA. Under these conditions, the mutant complexes showed a similar pattern of reduced Mcm2-7 DNA association as seen for the high-salt wash experiments. Cdt1 was not retained on the DNA under these conditions for mutant Mcm2-7 complexes, indicating that the MSSB mutations did not interfere with the release of Cdt1 from the Mcm2-7 complex during loading. Together, these data indicate that the loading defect for these Mcm2-7 mutants occurs after their initial recruitment to origin DNA but before the establishment of the ORC-independent association of Mcm2-7 with origin DNA.

We looked for additional replication initiation defects for the Mcm2-7 mutants that showed detectable loading using a modified in vitro replication assay that recapitulates origin-dependent DNA replication initiation and elongation (Heller et al., 2011). In contrast to our original studies, helicase loading in these assays was performed using purified proteins. In addition to measuring new DNA synthesis, we monitored association of Mcm2-7, the helicase activation proteins Cdc45 and GINS and the ssDNA binding protein, RPA, with the origin DNA during the reaction. The analysis of protein associations provided insights into the step during replication initiation during which the mutant Mcm2-7 complexes fail. Consistent with their inability to support cell growth, none of the mutant complexes supported significant DNA synthesis (Figure 6). Analysis of FLAG-Mcm3 DNA association showed that, as in the loading assays, the Mcm4D/6D and Mcm6D/7D complexes are retained on the DNA more strongly than the Mcm4D/7D complex. Cdc45 association mirrored the level of FLAG-Mcm3 association with the DNA, suggesting Cdc45 recruitment is independent of the MSSB (Figure 6—figure supplement 1). In contrast, all of the Mcm2-7 double mutants showed similarly strong defects (≥10-fold) in both GINS and RPA DNA association. In the case of Mcm4D/7D mutant, the DNA replication, GINS and RPA DNA association defects are consistent with its helicase-loading defect. In contrast, for Mcm4D/6D and Mcm6D/7D, the extent of helicase loading and Cdc45 DNA association is distinct from the much larger losses in GINS and RPA DNA association and DNA replication (Figure 6—figure supplement 1). These data strongly suggest that an inability to recruit or maintain GINS and/or RPA is responsible for the replication defects exhibited by these mutants. Because RPA DNA binding is a readout for ssDNA formation and GINS is required to activate the Mcm2-7 helicase, both of these defects indicate that the Mcm4/6 and Mcm6/7 MSSB mutants are defective for helicase activation.

![Figure 6.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig6-v1.jpg)

**Figure 6.:** Proteins associated with the DNA template during DNA replication were analyzed by immunoblotting (top panels) and radiolabeled DNA replication products were analyzed by alkaline agarose electrophoresis (bottom panel). All of the mutants are strongly defective for DNA replication and GINS and RPA DNA template association relative to wild-type Mcm2-7. The levels of Cdc45 and Mcm2-7 (FLAG-Mcm3) association reflected the levels of helicase loading by the same MSSB double mutant Mcm2-7 complexes. Quantitation of these data is shown in Figure 6—figure supplement 1.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** The level of Cdc45 DNA-association mirrored the level of Mcm3 DNA-association. All of the mutants were severely defective for GINS and RPA template association and in vitro replicaiton (bottom right). The levels of GINS and RPA template association (rather than Cdc45 association) correlate with the levels of replication observed.

## Discussion

Here we show how the PfMCM N-terminal domain interacts with single-stranded DNA and identify a critical set of interacting residues that we define as the MSSB. These residues are important for binding ssDNA and, to a lesser extent, dsDNA. A DNA-binding role for positively charged residues in this region is consistent with previous mutational analysis of SsoMCM showing that K129A (equivalent to PfMCM R124) displays very little binding to ssDNA, blunt duplex DNA, and bubble-DNA substrates (Pucci et al., 2004). Although a positive residue equivalent to PfMCM R186 is not conserved in SsoMCM, mutation of an adjacent residue, K194A also displays very little binding to these DNA substrates (Pucci et al., 2004). As previously noted in overall sequence comparisons (Pucci et al., 2004), residues in the MSSB motif are conserved in specific families in eukaryotic Mcm2-7. Importantly, we show that conserved residues within this motif are critical for S. cerevisiae cell division and multiple Mcm2-7 functions during replication initiation.

Biochemical analysis of the S. cerevisiae mutant complexes reveals multiple defects during replication initiation. Two mutant complexes (Mcm4D/7D and Mcm4D/6D/7D) show strong defects in Mcm2-7 loading. This is unexpected because Mcm2-7 proteins are loaded around dsDNA and there is no evidence for ssDNA at this stage of replication (Evrin et al., 2009; Remus et al., 2009). It is possible that one or more MSSB motifs interact with dsDNA prior to ssDNA formation at the origin and that these interactions stabilize loaded Mcm2-7. This would be consistent with the dsDNA binding defects observed for the PfMCMN R124A/R186A double mutant (Figure 4—figure supplement 1) and also the (R124-equivalent) K129A mutant of SsoMCM. Alternatively, elimination of positive charges in the central channel could alter the opening and closing of the Mcm2-7 ring. The abundance of positive charges in the Mcm2-7 ring could predispose the ring to remain open prior to DNA binding. Encircling dsDNA could neutralize the repulsion and favor ring closing. It is possible that a reduction in positive charge in the mutant complexes leads to the Mcm2-7 ring spending more time in the closed state, inhibiting entry of the dsDNA during loading. Analogously, the reduced positive charge of the MSSB mutants could destabilize ring closure around dsDNA during loading. Consistent with this model, the Mcm2-7 complex appears as a cracked-ring in solution (Costa et al., 2011). As we observe, both scenarios predict that the strongest loading defects would be observed for the Mcm4D/6D/7D mutant that eliminates the greatest number of positive charges. Among the double mutants, the strongest loading defect is observed when the Mcm4 and Mcm7 subunits are mutated, which are across from the Mcm2/5 gate and could influence opening and closing more than other subunits.

Several lines of evidence suggest that the MCM-ssDNA interactions that we have identified have a role during dsDNA melting. First, the MCM-ssDNA interactions identified in our structure predominantly involve the sugars and bases of the ssDNA, ideally suited to bind and shield one strand from its complement during melting. Also consistent with a role in dsDNA melting, the Mcm2-7 MSSB mutant complexes showed strong defects in events linked to helicase activation. The MSSB mutations did not alter Cdc45 recruitment, consistent with the observation that this event can occur in G1 phase prior to ssDNA formation (Aparicio et al., 1999; Heller et al., 2011; Tanaka et al., 2011). In contrast, the levels of GINS and RPA DNA association by each of the MSSB mutant complexes were strongly defective. The defect in RPA DNA binding is almost certainly due to reduced ssDNA generation by the mutant complexes. The reduction in DNA-associated GINS could be the result of a defect in recruitment or retention of GINS. Unlike Cdc45, GINS recruitment does not occur until entry into S phase (Kanemaki et al., 2003; Takayama et al., 2003) and, therefore, could require ssDNA formation. Alternatively, it is possible that the defect in ssDNA binding prevents the CMG complex from attaining a particular DNA binding state and this destabilizes GINS binding.

Interactions between the MSSB and ssDNA could also occur during elongation. Consistent with a role for the MSSB in unwinding, the SsoMCM K129A mutant (PfMCM R124 equivalent) is defective for helicase activity (Pucci et al., 2004). Although the MCM ATPase domain alone is sufficient to produce unwinding activity in SsoMCM (Barry et al., 2007; Pucci et al., 2007) and in Aeropyrum pernix MCM (Atanassova and Grainge, 2008), unwinding displays greater processivity in the presence of the N-terminal domain for SsoMCM (Barry et al., 2007). Thus, although the N-terminal domain and the residues of the MSSB are not intrinsically required to produce an unwinding activity, the N-terminal domain can regulate and enhance MCM unwinding activity (Barry et al., 2007). The positively charged residues of the MSSB could help maintain a closed MCM ring as described above for loading, and thus contribute to the enhanced processivity afforded by the N-terminal domain. It is also possible that ssDNA binding by the MSSB has a more direct impact on DNA unwinding. For example, the directional ssDNA:MSSB interactions observed here could influence the polarity of unwinding either during initiation (see below) or elongation. To permit the ssDNA:MCMN interactions that we observe, the ssDNA would need to alter its trajectory as it passes through the MCM central channel. Alternatively, the MSSB could bind ssDNA differently during unwinding. An interesting possibility is that during elongation the MCM OB-fold binds ssDNA similar to the OB-fold prototype SSB (Raghunathan et al., 2000; Chan et al., 2009). This mode of binding would place the ssDNA approximately parallel to the central channel (Figure 1—figure supplement 7), a position consistent with the expected ssDNA trajectory during unwinding. Different modes of interaction between the MSSB and ssDNA could be modulated by the AAA+ domain of MCM and a conserved ‘allosteric communication loop’ (ACL, Sakakibara et al., 2008, Barry et al., 2009) that projects from the N-terminal domain towards the anticipated position of the ATPase domain. The ACL directly follows the β-strand that contains the second positively charged MSSB residue (PfMCM residue R186) and thus could couple the MSSB to the ATPase domains.

The polarity of ssDNA bound to MCMN observed in our structure has important implications for the transition between MCM dsDNA and ssDNA binding. In the view shown in Figure 7A, the AAA+ motors are located above the MCMN domain, and the corresponding Mcm2-7 subunits occur clockwise in the order Mcm5, 3, 7, 4, 6, 2. Given that the Mcm2-7 complex is initially loaded around dsDNA, only one of the two strands of dsDNA can easily attain the 5′→3′ coplanar clockwise configuration observed in our structure: the DNA strand that passes from the C- to N-terminus of the MCM complex in a 5′→3′ direction (Figure 7A). Intriguingly, this strand corresponds to the leading strand DNA template that is encircled by the MCM complex during translocation/DNA unwinding. For the opposite strand to interact with the MCMN with the observed polarity, it would either need to pass through the other strand or dramatically re-orient. Thus, if ssDNA is formed within the MCM ring during origin melting (see below), our structure predicts that MCMN would preferentially bind to the translocating strand (i.e., the leading strand DNA template). Consistent with this model, the 3′→5′ helicase polarity of SsoMCM is only observed when the N-terminal domain is present, implicating this domain in substrate selection (Barry et al., 2007).

![Figure 7.](https://cdn.elifesciences.org/articles/01993/elife-01993-fig7-v1.jpg)

**Figure 7.:** (A) The defined polarity of ssDNA binding by the MCMN would preferentially bind the leading-strand DNA template. The Mcm2-7 complex N-terminus is shown from the C-terminal side of the complex. This is the side where DNA is expected to enter during translocation. Duplex DNA is first encircled by the ring (left). Only the red strand can readily attain the 5′→3′ clockwise polarity observed in the crystal structure. This strand passes through the ring 5′→3′ from the C- to the N-terminal side and thus is the correct polarity to serve as the translocating strand. We propose the grey, lagging strand DNA template will exit through the Mcm2/5 gate, possibly as a result of accumulation of ssDNA in the central channel (right). (B) A model for selecting the translocating strand during origin melting. Symmetric surfaces in different shades of green represent the two MCMN portions of a double hexamer. The dsDNA is first encircled by the MCM double hexamer (left panel). The dsDNA is driven toward the double hexamer interface by the dsDNA translocase activity of the AAA+ ATPase domains (not shown), which would be located above the light green surface and below the dark green surface. The dsDNA translocation creates strand separation where volume is available, enabling the MSSB to preferentially bind the strand with 5′→3′ clockwise polarity when viewed from the ATPase domain (middle panel). Importantly, the MSSB-bound strand corresponds to the strand upon which the MCM helicase will translocate during unwinding (right panel, magenta at top, cyan at bottom).

The MCM helicase is conceptually similar to the Rho hexameric helicase because both possess an N-terminal OB-fold linked to a C-terminal ATPase. This analogy further supports a role for the MCM OB-fold during helicase activation prior to unwinding. The crystal structure of Rho with RNA bound at the OB-fold (Skordalakes and Berger, 2003) suggests that 70–80 nucleotides of RNA would adopt a circular path around the ring (Skordalakes and Berger, 2003) that is roughly perpendicular to the hexameric channel. This arrangement is conceptually similar to our PfMCMN:ssDNA structure. The Rho OB-fold is believed to bind RNA and facilitate encircling of single-stranded RNA during ring closure by the ATPase domains (Skordalakes and Berger, 2003), a prerequisite for establishing an activated helicase. Subsequently, the proposed unwinding mechanism for Rho exclusively involves distinct interactions between the ATPase motor domain and RNA (Thomsen and Berger, 2009). The MCM N-terminal domain may also function to enable the ATPase domains to select and encircle one strand of DNA during ring closure. A key difference between MCM and Rho is that the Rho helicase ring is loaded on a species that is already single-stranded, whereas the MCM hexamer is first loaded onto double-stranded DNA that must somehow be converted to single-stranded DNA (Evrin et al., 2009; Remus et al., 2009).

Combining the features of eukaryotic MCMs with our new structural information, we suggest the following model for MSSB function during helicase activation. After helicase loading, we propose that DNA melting is initiated by activating the ATPase domains of the double-hexamer to pump dsDNA from the C-terminal lobe side towards the double-hexamer interface (Figure 7B; Video 2). This is consistent with the known direction of MCM DNA translocation (McGeoch et al., 2005) as well as observations that Mcm complexes can translocate on dsDNA (Kaplan et al., 2003). As additional nucleotides of DNA are forced to occupy the same distance along the DNA helical axis, a B-form structure can no longer be maintained. We predict that the DNA strands would be forced apart at the site where the diameter of the MCM central channel is largest. Intriguingly, the MSSB is on the surface of the largest diameter of the MCMN central channel (Figure 1—figure supplement 3), putting the MSSB in a prime position to bind the leading strand ssDNA upon DNA melting. The channel diameter elsewhere in the MCMN is too narrow to permit B-form DNA strands to separate. Such melting activity requires that the two hexamers are anchored to one another because the two hexamers would otherwise simply translocate away from one another without melting the DNA. Further dsDNA pumping after the volume around the MSSB has been filled would require the MCM ring to open and allow the unbound lagging strand DNA template to exit (Figure 7A). The presumed exit site would be through the Mcm2/5 gate (Bochman and Schwacha, 2007; Costa et al., 2011). Intriguingly, Mcm2 and Mcm5 are the only two subunits that lack a conserved positive residue at the PfMCM R124 position, reducing ssDNA affinity and potentially facilitating strand exit. Following strand exit and extrusion of additional lengths of ssDNA, ring closure would poise each isolated hexamer to unwind DNA using a strand exclusion mechanism (Fu et al., 2011). The event that would drive double hexamer separation is unclear but could be facilitated by the change from encircling dsDNA to ssDNA, binding of additional factors (e.g., Mcm10) or modification of the helicase. A definitive test for this model awaits the development of assays that directly monitor the events of origin DNA melting and strand exclusion. Nevertheless, our studies provide structural and biochemical evidence that the MSSB is a critical ssDNA binding domain that functions during helicase loading and activation and provide initial insights into how ssDNA binding by MCM complex could facilitate selection of one strand during helicase activation.

![Video 2.](https://cdn.elifesciences.org/articles/01993/elife-01993-media2.mov.jpg)

**Video 2.:** Symmetric surfaces in different shades of green represent the two MCMN portions of a double hexamer. The dsDNA is first encircled by the MCM double hexamer. The dsDNA is driven toward the double hexamer interface by the dsDNA translocase activity of the AAA+ ATPase domains (not shown), which would be located above the light green surface and below the dark green surface. The dsDNA translocation creates strand separation where volume is available, enabling the MSSB to preferentially bind the strand with 5′→3′ clockwise polarity when viewed from the ATPase domain. Importantly, the MSSB-bound strand corresponds to the strand upon which the MCM helicase will translocate (magenta at top, cyan at bottom), as shown in Figure 7B, right panel.

## Materials and methods

### Cloning, mutagenesis, expression, and purification

An N-terminal His6-SUMO-PfMCM1-256 expression construct was prepared. The original SUMO vector was the generous gift of Dr Christopher D Lima (Mossessova and Lima, 2000). An existing His6-SUMO-tagged-fusion protein expression construct in a pRSFduet (EMD Millipore, Darmstadt, Germany) plasmid was treated with BamHI and XhoI to completely excise the original fusion partner to generate a BamHI site in-frame with the SUMO tag. This digested species was treated with phosphatase and gel-purified. A DNA fragment encoding the first 256 amino acids of Pyrococcus furiosus MCM was amplified by PCR with primers flanked by BamHI and SalI restriction sites. This fragment was digested with BamHI/SalI, ligated into the BamHI/XhoI-prepared vector, and was transformed into DH5α cells. The integrity of a single colony clone was verified by restriction digest pattern and by DNA sequencing (pLE009.3). Mutants were prepared by site-directed mutagenesis, and the sequences were verified by the Hartwell Center DNA Sequencing Facility (St. Jude Children’s Research Hospital).

Expression plasmid pLE009.3 (WT), pCF001.1 (R124A), pCF002.1 (K129A), pCF003.1 (R186A), pCF004.1 (F202A), pCF0027.1 (K233A), or pCF009.1 (R124A/R186A) was transformed into BL21(DE3)-RIPL (Agilent Technologies, Santa Clara, CA) chemically competent cells and grown overnight in a 100 ml starter culture containing 30 mg/l kanamycin. The starter culture was distributed among 6 l of LB media containing 0.4% glucose and 30 mg/l kanamycin and grown to an O.D. of 0.3 at 37°C when the temperature was lowered to 18°C. When the O.D. had reached 0.7, expression was induced by 0.5 mM IPTG, and the cells were grown for 16 hr at 18°C and harvested by centrifugation. The cells were lysed with a microfluidizer, and the soluble fraction was isolated by centrifugation and ammonium sulfate was added to 70% saturation. The precipitate was isolated by centrifugation, resuspended, and purified by Ni-NTA (Qiagen, Venlo, the Netherlands) chromatography. The elution was further purified by anion exchange, and the SUMO tag was removed by overnight digestion with Ulp1 protease (the Ulp1 protease plasmid was the generous gift of Dr Christopher D Lima, Mossessova and Lima, 2000). The NaCl concentration was raised to 1M, and the sample was passed over Ni-NTA resin, and the flowthrough was purified by anion exchange followed by gel filtration chromatography. The protein elutes at a volume consistent with a monomer. Pooled fractions were concentrated to 10–20 mg/ml. SDS-PAGE was used to assess the purity, and the protein concentration was determined by A280 measurements (ε = 11,460 M−1 cm−1 as determined by the ExPASy ProtParam tool). Purified PfMCMN variants were stored at 4°C in buffer containing 20 mM HEPES, pH 7.6, 200 mM NaCl, 5 mM β-mercaptoethanol.

### Crystallization, data-collection, structure-solution, and refinement

Crystals of PfMCMN in complex with a 30-mer poly-dT oligonucleotide were grown at 18°C in a hanging drop containing 1 μl of protein solution pre-mixed with a 30-mer poly-dT oligonucleotide (13.2 mg/ml protein; 120 μM poly-dT) and 2 μl of well solution (50 mM MES, pH 6.0, 10 mM Mg(OAc)2, 28.5% PEG 3350). Data were collected at SER-CAT beamline 22-ID at the Advanced Photon Source at Argonne National Lab. Data were collected at 1.0 Å wavelength in 0.5° oscillations for a total of 190° of crystal rotation at 100 K. Data were integrated and scaled with the HKL-2000 package (Otwinowski and Minor, 1997) to 3.2 Å resolution. Initial phases were determined by molecular replacement by the program Phaser (McCoy et al., 2007) that placed 12 copies of a monomer of PfMCMN (see below) in two hexamers. Following this placement, difference maps revealed strong electron density within the hexameric channels of both hexamers. The protein model was iteratively refined and manually improved until advancement ceased. At this stage, the difference electron density within the channel was observed at the 5-sigma level (Figure 1—figure supplement 2), and it was assigned as single-stranded DNA. The model was refined at various stages with CNS (Brunger et al., 1998; Brunger, 2007), phenix (Afonine et al., 2012), and refmac5 (Vagin et al., 2004). The final refinement was carried out with refmac5 using 3 TLS (Winn et al., 2003) groups for each protein monomer (one per subdomain). A Ramachandran plot calculated by Procheck (Laskowski et al., 1993) indicated the following statistics: core: 2244 (82.7%); allowed: 423 (15.6%); generously allowed: 48 (1.8%); disallowed: 0 (0%). Figures were prepared with the program Bobscript (Esnouf, 1997) and rendered with the Raster3D (Merritt and Bacon, 1997) package or prepared with the program PyMOL (Schrodinger, 2010).

Crystals of PfMCMN without DNA were grown at 18°C in a sitting drop containing 200 nl of protein solution (10 mg/ml) and 200 nl of well solution (0.2 M sodium malonate, pH 7.0, 20% PEG 3350). A plate crystal was cryoprotected by quickly passing it through well solution containing 15% ethylene glycol and flash frozen in liquid nitrogen. Data were collected at SER-CAT beamline 22-ID at the Advanced Photon Source at Argonne National Lab. Data were collected at 1.0 Å wavelength in 0.5° oscillations with two different segments of the same crystal. A total of 450 images were integrated and scaled with the HKL-2000 package (Otwinowski and Minor, 1997) to 2.65 Å resolution. The unit cell parameters are very close to hexagonal, but initial data merging showed the presence of a crystallographic twofold axis and a clear absence of a crystallographic threefold axis, indicating a monoclinic lattice. Initial phases were determined by molecular replacement by the program Molrep (Vagin and Teplyakov, 1997) by including a locked rotation and pseudo-translation. The program placed 6 copies of a monomer of MtMCMN (Fletcher et al., 2003) as a single hexamer in the asymmetric unit in space group P21. The hexamers pack in layers with the hexameric axes mutually aligned parallel to the crystallographic 21 axis. Individual layers are highly sixfold symmetric, but a crystallographic 6-fold symmetry is precluded because the NCS 6-fold axes of successive layers are not mutually compatible. The model was refined at various stages with CNS (Brunger et al., 1998; Brunger, 2007), phenix (Afonine et al., 2012), and refmac5 (Vagin et al., 2004). The final refinement was carried out with refmac5 using 3 TLS (Winn et al., 2003) groups for each protein monomer (one per subdomain). A Ramachandran plot calculated by Procheck (Laskowski et al., 1993) indicated the following statistics: core: 1168 (85.8%); allowed: 183 (13.4%); generously allowed: 11 (0.8%); disallowed: 0 (0%). Figures were prepared with the program Bobscript (Esnouf, 1997) and rendered with the Raster3D (Merritt and Bacon, 1997) package.

### Electromobility shift assay

DNA-binding reactions were set up in 20 μl with varying concentrations of PfMCMN (0–54 μM) and 160 nM 5′-fluorescein-labeled T40 ssDNA (Sigma-Aldrich, St. Louis, MO) in 20 mM HEPES, pH 7.6, 200 mM NaCl, 5 mM MgCl2, and 5 mM βME. Reactions were incubated at 25°C in a BioRad DNA Engine thermocycler for 30 min. Loading buffer (2.5 mg/ml bromophenol blue and 40% sucrose; 5 μl) was added, and 5 μl were loaded in a 4–20% 1X TBE gradient PAGE gel (BioRad, Berkeley, CA) and run at 100 V for 105 min. Gels were imaged by a Fuji LAS-4000 with an 8 s exposure and a SYBR-Green filter. The fluorescence intensities of bands for the free and bound species were quantified with MultiGauge (GE Healthcare, Piscataway, NJ) and fit to two simultaneous equations with Prism (GraphPad Software, La Jolla, CA):

$$
I(free)/I_{0}=K_{half}^{h}/(K_{half}^{h}+[MCM_{N}]^{h}) ; I(bound)/I_{0}=[MCM_{N}]^{h}/(K_{half}^{h}+[MCM_{N}]^{h})
$$

to determine the concentration of half-binding (Khalf) and a hill coefficient (h). The dsDNA EMSAs were identical except that they included a 26-mer dsDNA substrate and a different concentration range of PfMCMN (0–20 μM). The dsDNA substrate was prepared by annealing two oligos (5′-[Fluorescein]-ATGGCAGATCTCAATTGGATATCGGC-3′ and 5′-GCCGATATCCAATTGAGATCTGCCAT-3′, Sigma-Aldrich) followed by purification on a gel filtration column (GE Healthcare Superose 12 10/300).

### Yeast protein purification

Mcm2-7/Cdt1, Mcm4D6D/Cdt1, Mcm4D7D/Cdt1, Mcm6D7D/Cdt1 and Mcm4D6D7D/Cdt1complexes were purified from 2 L cultures of ySKM01, ySKM02, ySKM03, ySKM04 and ySKM05, respectively. Cultures were grown to O.D. = 0.8 and arrested at G1 phase by addition of alpha factor (200 ng/ml) for two hours followed by induction of Mcm2-7/Cdt1 expression by addition of galactose to 2% for 4 hr. Harvested cell pellets were re-suspended in 1/3 pellet volume of cell lysis buffer (100 mM HEPES-KOH (pH 7.6), 1.5 M potassium glutamate, 0.8 M sorbitol, 10 mM magnesium acetate, 1 mM dithiothreitol and 1X Complete Protease Inhibitor Cocktail [Roche Diagnostics, Indianapolis, IN]) and frozen in liquid nitrogen. The frozen cell pellets were broken using a SPEX SamplePrep Freezer/Mill. After thawing, 15 ml of Buffer H (25 mM HEPES-KOH (pH 7.6), 1 mM EDTA, 1 mM EGTA, 5 mM magnesium acetate, 10% glycerol, 0.02% NP40) containing 0.5 M potassium glutamate, 3 mM ATP and 1X Complete Protease Inhibitor Cocktail was added to the broken cells. The cell lysate was centrifuged at 45,000×g rpm for 90 min (Ti70 Rotor, Beckman) and the supernatant was mixed with 0.6 ml anti-Flag Agarose (Sigma-Aldrich) equilibrated with Buffer H containing 0.5 M potassium glutamate. The mix was incubated for 4 hr at 4°C. The resin was washed and Mcm2-7/Cdt1 complexes were eluted with Buffer H containing 0.3 M potassium glutamate, 3 mM ATP and 0.15 mg/ml 3xFlag peptides. The eluted fractions were concentrated using Vivaspin 6 (Mw. cutoff 100 KDa, Sartorius) to 500 μl and applied to Superdex 200 HR 10/30 gel filtration column (GE Healthcare). For each mutant complex, the corresponding wild-type proteins were epitope-tagged with V5 (e.g., in the strain expressing the Mcm4D7D/Cdt1 the wild-type MCM4 and MCM7 genes were tagged with V5). This allowed the endogenous V5-tagged Mcm4, 6 or 7 subunits to be depleted by incubating with anti-V5 agarose (Sigma) before applying the MSSB mutant complexes to the gel filtration column.

### Helicase loading assay

2 pmole ORC, 3 pmole Cdc6 and 6 pmole Mcm2-7/Cdt1 were sequentially added to the 40 μl reaction solution containing 1 pmole of bead-coupled 1.3 Kbps ARS1 DNA in helicase loading buffer (25 mM HEPES-KOH (pH7.6), 12.5 mM magnesium acetate, 0.1 mM zinc acetate, 300 mM potassium glutamate, 20 μM creatine phosphate, 0.02% NP40, 10% glycerol, 3 mM ATP, 1 mM dithiothreitol and 2 μg creatine kinase). The reaction mix was incubated at 25°C at 1200 rpm for 30 min in a thermomixer (Eppendorf). Beads were washed three times with Buffer H containing 0.3 M potassium glutamate and DNA bound proteins were eluted from the beads using DNase I. Eluted proteins were separated by SDS-PAGE and stained with a fluorescent protein stain (Krypton, Thermo Scientific). For high salt wash experiments, Buffer H containing 0.5 M NaCl was used at the second wash step. In ATPγS experiments, 6 mM ATPγS was used instead of ATP.

### In vitro replication assay

Helicase loading reactions were performed using 0.5 pmole ORC, 0.75 pmole Cdc6 and 2 pmole MCM/Cdt1 and 250 fmole bead-coupled 3.6 Kbps circular pUC19-ARS1 plasmid DNA (Heller et al., 2011). Origin-loaded MCM complexes were phosphorylated with 450 μg purified DDK in DDK reaction buffer (50 mM HEPES-KOH (pH7.6), 3.5 mM magnesium acetate, 0.1 mM zinc acetate, 150 mM potassium glutamate, 0.02% NP40, 10% glycerol, 1 mM spermine, 1 mM ATP and 1 mM dithiothreitol, 30 μl). Phosphorylated MCM complexes were then activated with 750 μg S phase extract in the replication reaction buffer (25 mM HEPES-KOH (pH7.6), 12.5 mM magnesium acetate, 0.1 mM zinc acetate, 300 mM potassium glutamate, 20 μM creatine phosphate, 0.02% NP40, 10% Glycerol, 3 mM ATP, 40 μM dNTPs, 200 μM CTP/UTP/GTP, 1 mM dithiothreitol, 10 μCi [α-P32] dCTP and 2 μg creatine kinase, 40 μl) for 1 hr at 25°C and 1200 RPM in a Thermomixer (Eppendorf). After the reaction, DNA synthesis was monitored using alkaline agarose gel. DNA bound proteins were released from the beads by DNase I treatment and analyzed by immunoblot. S phase extracts were prepared from ySKS10 and ySKS11 as described previously (Heller et al., 2011).

### S. cerevisiae in vivo complementation assay

MSSB mutations were introduced into TRP + ARS/CEN plasmids containing MCM4, MCM6, or MCM7 under the control of the MCM5 promoter. The resultant constructs were tested for MCM4, MCM6, or MCM7 function by a plasmid shuffle assay (Schwacha and Bell, 2001). To test the double mutant complementation, one MSSB mutant Mcm subunit (either MCM4 or MCM6) was integrated into a plasmid shuffle strain for a second subunit.

### Strain construction for in vivo complementation assay

To integrate MSSB mutations into the chromosomal locus, we constructed plasmids containing the MCM4 or MCM6 promoter upstream of a NatMX4 (for MCM4) or LEU2 (for MCM6) marker cassette, with the Mcm5 promoter plus the MCM4 or MCM6 gene downstream of the marker and restriction enzyme sites flanking the entire integration unit (pSKC04 and pSKC05, respectively). Proper integration was confirmed by PCR followed by sequencing.

To create strains carrying MSSB mutations in MCM4 and MCM6 or MCM6 and MCM7, we began with strains carrying mcm4 or mcm7 deletion and the wild-type copy of MCM4 or MCM7 on URA+ ARS/CEN constructs, respectively. MCM6 MSSB mutation was integrated into these strains using the LEU+ integrating construct described above. For a strain carrying MSSB mutations in MCM4 and MCM7, MCM4 MSSB mutations were incorporated in to a strain carrying mcm7 deletion and wild-type copy of MCM7 on URA+ ARS/CEN constructs, using NAT+ integrating construct. Then TRP+ ARS/CEN plasmids carrying MCM4 or MCM7 MSSB mutant allele were transformed above strains. Proliferation of double-mutant strains was analyzed using FOA counter-selection against the URA+ wild-type MCM4 or MCM7 plasmid.

Yeast strains and plasmids of this study are listed in Tables 2 and 3.

**Table 2.**
 Yeast strains used in this study


<table>
  <thead>
    <tr>
      <th>Strains</th>
      <th>Genotype</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">ySKM01</td>
      <td>ade2-1 trp1-1 leu2-3,112 his3-11,15 ura3-1 can1-100 bar1::HisG lys2::HisG pep4Δ::unmarked</td>
      <td rowspan="4">This study</td>
    </tr>
    <tr>
      <td>his3::pSKM004 (GAL1,10-MCM2, Flag-MCM3) leu::pSKM007 (GAL1,10-Cdt1-Strep, GAL4)</td>
    </tr>
    <tr>
      <td>lys::pSKM002 (GAL1,10-MCM4, MCM5)</td>
    </tr>
    <tr>
      <td>trp::pSKM003 (GAL1,10-MCM6, MCM7)</td>
    </tr>
    <tr>
      <td rowspan="4">ySKM02</td>
      <td>ade2-1 trp1-1 leu2-3,112 his3-11,15 ura3-1 can1-100 bar1::HisG lys2::HisG pep4Δ::KanMX6</td>
      <td rowspan="4">This study</td>
    </tr>
    <tr>
      <td>MCM4-V5 (NatMX4) MCM6-V5 (CaURA3MX4) MCM7-V5 (HphMX4)</td>
    </tr>
    <tr>
      <td>his3::pSKM004 (GAL1,10-MCM2, Flag-MCM3) leu::pSKM007 (GAL1,10-Cdt1-Strep, GAL4)</td>
    </tr>
    <tr>
      <td>lys::pSKM008 (GAL1,10-mcm4[R334A/K398A], MCM5) trp::pSKM009 (GAL1,10-mcm6[R296A/R360A], MCM7)</td>
    </tr>
    <tr>
      <td rowspan="4">ySKM03</td>
      <td>ade2-1 trp1-1 leu2-3,112 his3-11,15 ura3-1 can1-100 bar1::HisG lys2::HisG pep4Δ::KanMX6</td>
      <td rowspan="4">This study</td>
    </tr>
    <tr>
      <td>MCM4-V5 (NatMX4) MCM6-V5 (CaURA3MX4) MCM7-V5 (HphMX4)</td>
    </tr>
    <tr>
      <td>his3::pSKM004 (GAL1,10-MCM2, Flag-MCM3) leu::pSKM007 (GAL1,10-Cdt1-Strep, GAL4)</td>
    </tr>
    <tr>
      <td>lys::pSKM008 (GAL1,10-mcm4[R334A/K398A], MCM5) trp::pSKM010 (GAL1,10-MCM6, mcm7[R247A/K314A])</td>
    </tr>
    <tr>
      <td rowspan="5">ySKM04</td>
      <td>ade2-1 trp1-1 leu2-3,112 his3-11,15 ura3-1 can1-100 bar1::HisG lys2::HisG pep4Δ::KanMX6</td>
      <td rowspan="5">This study</td>
    </tr>
    <tr>
      <td>MCM4-V5 (NatMX4) MCM6-V5 (CaURA3MX4) MCM7-V5 (HphMX4)</td>
    </tr>
    <tr>
      <td>his3::pSKM004 (GAL1,10-MCM2, Flag-MCM3) leu::pSKM007 (GAL1,10-Cdt1-Strep, GAL4)</td>
    </tr>
    <tr>
      <td>lys::pSKM002 (GAL1,10-MCM4, MCM5)</td>
    </tr>
    <tr>
      <td>trp::pSKM011 (GAL1,10-mcm6[R296A/R360A], mcm7[R247A/K314A])</td>
    </tr>
    <tr>
      <td rowspan="5">ySKM05</td>
      <td>ade2-1 trp1-1 leu2-3,112 his3-11,15 ura3-1 can1-100 bar1::HisG lys2::HisG pep4Δ::KanMX6</td>
      <td rowspan="5">This study</td>
    </tr>
    <tr>
      <td>MCM4-V5 (NatMX4) MCM6-V5 (CaURA3MX4) MCM7-V5 (HphMX4)</td>
    </tr>
    <tr>
      <td>his3::pSKM004 (GAL1,10-MCM2, Flag-MCM3) leu::pSKM007 (GAL1,10-Cdt1-Strep, GAL4)</td>
    </tr>
    <tr>
      <td>lys::pSKM008 (GAL1,10-mcm4[R334A/K398A], MCM5)</td>
    </tr>
    <tr>
      <td>trp::pSKM011 (GAL1,10-mcm6[R296A/R360A], mcm7[R247A/K314A])</td>
    </tr>
    <tr>
      <td rowspan="6">ySKS10</td>
      <td>ade2-1 trp1-1 leu2-3,112 his3-11,15 ura3-1 can1-100 lys2::HisG pep4Δ::Hph cdc7-4</td>
      <td rowspan="6">This study</td>
    </tr>
    <tr>
      <td>pol1-5xFlag (KanMX4)</td>
    </tr>
    <tr>
      <td>leu::pSKS001 (GAL1,10-Cdc45-V5, Sld3-S)</td>
    </tr>
    <tr>
      <td>lys::pSKS002 (GAL1,10-Dpb11-VSVG, Sld2-HSV)</td>
    </tr>
    <tr>
      <td>ura::pSKS003 (Gal1,10-Cdc28, Clb5)</td>
    </tr>
    <tr>
      <td>his::pSKS004 (Gal1,10-Sld7)</td>
    </tr>
    <tr>
      <td rowspan="6">ySKS11</td>
      <td>ade2-1 trp1-1 leu2-3,112 his3-11,15 ura3-1 can1-100 lys2::HisG pep4Δ::Hph cdc7-4</td>
      <td rowspan="6">This study</td>
    </tr>
    <tr>
      <td>pol2-5xFlag (KanMX4)</td>
    </tr>
    <tr>
      <td>leu::pSKS001 (GAL1,10-Cdc45-V5, Sld3-S)</td>
    </tr>
    <tr>
      <td>lys::pSKS002 (GAL1,10-Dpb11-VSVG, Sld2-HSV)</td>
    </tr>
    <tr>
      <td>ura::pSKS003 (Gal1,10-Cdc28, Clb5)</td>
    </tr>
    <tr>
      <td>his::pSKS004 (Gal1,10-Sld7)</td>
    </tr>
    <tr>
      <td rowspan="2">ASY1059.1</td>
      <td>MatA, ade2-1, ura3-11, his3-11,15, leu2-3,12, can-100, trp1-1</td>
      <td rowspan="2">(Schwacha and Bell, 2001)</td>
    </tr>
    <tr>
      <td>mcm4 Δ::hisG/pAS412 (ARS/CEN URA+ PMCM5-MCM4-HA/HIS)</td>
    </tr>
    <tr>
      <td rowspan="2">ASY2157</td>
      <td>MatA, ade2-1, ura3-11, his3-11,15, leu2-3,12, can-100, trp1-1, lys2::hisG, bar1::hisG, PEP4 Δ::KANMX4,</td>
      <td rowspan="2">(Schwacha and Bell, 2001)</td>
    </tr>
    <tr>
      <td>MCM6 Δ::HISMX6/pAS452 (ARS/CEN URA+ PMCM5-MCM6-HA/HIS)</td>
    </tr>
    <tr>
      <td rowspan="2">ASY1050.1</td>
      <td>MatA, ade2-1, ura3-11, his3-11,15, leu2-3,12, can-100, trp1-1</td>
      <td rowspan="2">(Schwacha and Bell, 2001)</td>
    </tr>
    <tr>
      <td>mcm7Δ::hisG/pGEMCDC47 (ARS/CEN URA+ MCM7)</td>
    </tr>
    <tr>
      <td rowspan="2">ySKC01</td>
      <td>MatA, ade2-1, ura3-11, his3-11,15, leu2-3,12, can-100, trp1-1</td>
      <td rowspan="2">This study</td>
    </tr>
    <tr>
      <td>mcm4 Δ::hisG/pAS412 (ARS/CEN URA+ PMCM5-MCM4-HA/HIS) mcm6::LEU2-PMCM5-mcm6[R296A/R360A]</td>
    </tr>
    <tr>
      <td rowspan="2">ySKC02</td>
      <td>MatA, ade2-1, ura3-11, his3-11,15, leu2-3,12, can-100, trp1-1</td>
      <td rowspan="2">This study</td>
    </tr>
    <tr>
      <td>mcm7Δ::hisG/pGEMCDC47 (ARS/CEN URA+ MCM7) mcm6::LEU2-PMCM5-mcm6[R296A/R360A]</td>
    </tr>
    <tr>
      <td rowspan="2">ySKC03</td>
      <td>MatA, ade2-1, ura3-11, his3-11,15, leu2-3,12, can-100, trp1-1</td>
      <td rowspan="2">This study</td>
    </tr>
    <tr>
      <td>mcm7Δ::hisG/pGEMCDC47 (ARS/CEN URA+ MCM7) mcm4::NatMX4-PMCM5-mcm4[R334A/K398A]</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Yeast plasmids used in this study


<table>
  <thead>
    <tr>
      <th>Plasmids</th>
      <th>Description</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pSKM002</td>
      <td>pRS307 (GAL1,10-MCM4, MCM5)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKM003</td>
      <td>pRS404 (GAL1,10-MCM6, MCM7)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKM004</td>
      <td>pRS403 (GAL1,10-MCM2, Flag-MCM3)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKM007</td>
      <td>pRS305 (GAL1,10-Cdt1-Strep, GAL4)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKM008</td>
      <td>pRS307 (GAL1,10-mcm4[R334A/K398A], MCM5)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKM009</td>
      <td>pRS404 (GAL1,10-mcm6[R296A/R360A], MCM7)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKM010</td>
      <td>pRS404 (GAL1,10-MCM6, mcm7[R247A/K314A])</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKM011</td>
      <td>pRS404 (GAL1,10-mcm6[R296A/R360A], mcm7[R247A/K314A])</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKS001</td>
      <td>pRS305 (GAL1,10-Cdc45-V5, Sld3-S)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKS002</td>
      <td>pRS307 (GAL1,10-Dpb11-VSVG, Sld2-HSV)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKS003</td>
      <td>pRS306 (Gal1,10-Cdc28, Clb5)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKS004</td>
      <td>pRS403 (Gal1,10-Sld7)</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKC001</td>
      <td>pRS414 (PMCM5-mcm4[R334A/K398A])</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKC002</td>
      <td>pRS414 (PMCM5- mcm6[R296A/R360A])</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKC003</td>
      <td>pRS414 (PMCM5-mcm7[R247A/K314A])</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKC004</td>
      <td>pRS414 (PMCM4-NatMX4-PMCM5- mcm4[R334A/K398A])</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pSKC005</td>
      <td>pRS414 (PMCM6-LEU2-PMCM5- mcm6[R296A/R360A])</td>
      <td>This study</td>
    </tr>
  </tbody>
</table>
