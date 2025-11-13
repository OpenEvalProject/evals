# Structural insights into mRNA reading frame regulation by tRNA modification and slippery codon–anticodon pairing

## Authors

- Eric D Hoffer<sup>1</sup>
- Samuel Hong<sup>1</sup>
- S Sunita<sup>1</sup>
- Tatsuya Maehigashi<sup>1</sup>
- Ruben L Gonzalez<sup>2</sup> ([ORCID: 0000-0002-1344-5581](https://orcid.org/0000-0002-1344-5581))
- Paul C Whitford<sup>3</sup>
- Christine M Dunham<sup>1</sup> ([ORCID: 0000-0002-8821-688X](https://orcid.org/0000-0002-8821-688X)) †

### Affiliations

1. Department of Biochemistry, Emory University School of Medicine Atlanta United States
2. Department of Chemistry, Columbia University New York United States
3. Department of Physics, Northeastern University Boston United States

† Corresponding author

## Abstract

Modifications in the tRNA anticodon loop, adjacent to the three-nucleotide anticodon, influence translation fidelity by stabilizing the tRNA to allow for accurate reading of the mRNA genetic code. One example is the N1-methylguanosine modification at guanine nucleotide 37 (m1G37) located in the anticodon loop andimmediately adjacent to the anticodon nucleotides 34, 35, 36. The absence of m1G37 in tRNAPro causes +1 frameshifting on polynucleotide, slippery codons. Here, we report structures of the bacterial ribosome containing tRNAPro bound to either cognate or slippery codons to determine how the m1G37 modification prevents mRNA frameshifting. The structures reveal that certain codon–anticodon contexts and the lack of m1G37 destabilize interactions of tRNAPro with the P site of the ribosome, causing large conformational changes typically only seen during EF-G-mediated translocation of the mRNA-tRNA pairs. These studies provide molecular insights into how m1G37 stabilizes the interactions of tRNAPro with the ribosome in the context of a slippery mRNA codon.

## Introduction

Post-transcriptionally modified RNAs, including ribosomal RNA (rRNA), transfer RNA (tRNA) and messenger RNA (mRNA), stabilize RNA tertiary structures during ribonucleoprotein biogenesis, regulate mRNA metabolism, and influence other facets of gene expression. RNA modifications located in the three-nucleotide anticodon of tRNAs contribute to accurate protein synthesis and expand the tRNA coding capacity by facilitating Watson–Crick-like base-pairs with mRNA codons. The most commonly modified tRNA anticodon position is at nucleotide 34 and the modifications to this nucleotide are functionally important for gene expression by facilitating base-pairing interactions with the mRNA codon (Agris et al., 2017; Boccaletto et al., 2018; Agris et al., 2018). Other tRNA nucleotides also contain highly conserved nucleotide modifications, but their precise roles in protein synthesis are not fully understood. For example, nucleotide 37 is adjacent to the anticodon (Figure 1A) and is modified in >70% of all tRNAs (Machnicka et al., 2014). The two most common modifications at nucleotide 37 are 6-threonylcarbamoyladenosine (t6A) and 1-methylguanosine (m1G), which together account for >60% of nucleotide 37 modifications (Boccaletto et al., 2018). Both the t6A37 modification in tRNALys and the m1G37 modification in tRNAPro are thought to stabilize the tertiary structure of the anticodon loop for high-affinity binding to their cognate codons (Murphy et al., 2004; Sundaram et al., 2000; Nguyen et al., 2019). The m1G37 modification also prevents the ribosome from shifting out of the three-nucleotide mRNA codon frame (‘frameshifting’) to ensure the correct polypeptide is expressed (Björk et al., 1989; Li et al., 1997; Urbonavicius et al., 2001; Gamper et al., 2015a). However, the molecular basis for how the m1G37 modification maintains the mRNA reading frame is unknown.

![Figure 1.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig1-v2.jpg)

**Figure 1.:** (A) Secondary structure of the anticodon stem-loop (ASL) of tRNAPro. The m1G37 modified nucleotide is shown in orange and the anticodon nucleotides (C34, G35, and G36) and the U32-A38 pairing are labeled. (B) Structure of 70S-ASLPro bound to a cognate CCG codon in the P site with the codon in the 0 or canonical frame. All 2Fo-Fc electron density maps shown in panels B-D are contoured at 1.0σ. (C,D) Structure of 70S-ASLPro bound to a +1 slippery CCC-U codon shows the mRNA position is either in the 0 (panel C) or +1 frame (panel D) in the two 70S molecules in the crystallographic asymmetric unit. In either the 0 or +1 frame, a cis Watson–Crick interaction at the third base-pair forms (C+3•C34 or U+4•C34). mRNA numbering starts at +1 according to the first position in the P site.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) A cognate G+3-C34 base-pair (mRNA nucleotide:anticodon nucleotide) is shown above. Representative 2Fo-Fc density is shown for the same cognate base-pairingbetween mRNA and ASLPro/tRNAPro(below). The phosphate of G+4is circled in red and its presence signifies that the mRNA is in the 0 frame (B) A near-cognate ASLPro C+3-C34 base-pair is shown with 2Fo-Fc density. The phosphate of U+4 is circled in red and its presence signifies that the mRNA is in the 0 frame. (C) A near-cognate ASLPro U+3-C34 base-pairi is shown with 2Fo-Fc density surrounding U+4.There is a lack of density for an addition phosphate group (circled in red) indicating that another nucleotide is not present and the mRNA is in the +1 frame. (D) A near-cognate tRNAPro C+3-C34 base-pair is shown with 2Fo-Fc density surrounding C+3.The phosphate of U+4 is circled in red and its presence signifies that the mRNA is in the 0 frame. 2Fo-Fc density are set at 1σ for all structures. The cutoff for a base-pair hydrogen bond is 3.5 Å.

The m1G37 modification is present in >95% of all three tRNAPro isoacceptors across all three domains of life (Boccaletto et al., 2018; Björk et al., 1989). The absence of m1G37 in tRNAPro causes high levels of +1 frameshifting on so-called ‘slippery’ or polynucleotide mRNA sequences where four nucleotides encode for a single proline codon (Björk et al., 1989). In the case of the tRNAPro-CGG isoacceptor (anticodon is shown 5'-3'), a +1 slippery codon consists of the CCC proline codon and either an additional C or U to form a four-nucleotide codon, CCC-(U/C) (Sroga et al., 1992; Qian et al., 1998) (codons depicted 5’-3’). tRNAPro-CGG lacking m1G37 results in the ribosome being unable to distinguish a correct from an incorrect codon–anticodon interaction during decoding at the aminoacyl (A) site (Nguyen et al., 2019; Maehigashi et al., 2014). However, this miscoding event does not cause the shift in the mRNA frame in the A site despite the tRNAPro-CGG anticodon stem-loop nucleotides become more mobile (Maehigashi et al., 2014). A post-decoding frameshift event is further supported by detailed kinetic analyses (Gamper et al., 2015a). The absence of the m1G37 modification in tRNAPro causes a ~ 5% frameshifting frequency during translocation of the mRNA-tRNA pair from the A to the peptidyl (P) site and a ~40% frameshifting frequency once the mRNA-tRNA pair has reached the P site. When tRNAPro-CGG lacks m1G37 and decodes a +1 slippery codon, both the process of translocation and the unique environment of the P site appear to contribute to the inability of the ribosome to maintain the mRNA frame.

In circumstances where mRNA frameshifting is caused by changes in the tRNA such as the absence of modifications or changes in the size of the anticodon loop as found in frameshift suppressor tRNAs, primer extension assays demonstrated that the shift into the +1 frame is observed upon direct tRNA binding at the P site (Phelps et al., 2006; Walker and Fredrick, 2006). These studies show that the nature of the interactions between the frameshift-prone mRNA-tRNA pair and the ribosomal P site directly permit frameshifting. Furthermore, the presence of a nascent polypeptide chain, the acylation status of the tRNA (deacylated or aminoacylated), and even the presence of a tRNA in the A site do not appear to contribute to the ability of these tRNAs to cause frameshifting. Structural studies of frameshift-prone or suppressor tRNAs have provided molecular insights into how such tRNAs may dysregulate mRNA frame maintenance (Maehigashi et al., 2014; Fagan et al., 2014; Hong et al., 2018). Frameshift suppressor tRNASufA6 contains an extra nucleotide in its anticodon loop and undergoes high levels of +1 frameshifting on slippery proline codons (Björk et al., 1989; Qian et al., 1998). The structure of the anticodon stem-loop (ASL) of the tRNASufA6 bound directly at the P site revealed that its anticodon engages the slippery CCC-U proline codon in the +1 frame (Hong et al., 2018). Further, the full-length tRNASufA6 bound at the P site reveals that the small 30S subunit head domain swivels and tilts, a movement that is similar to the one that is caused by the GTPase elongation factor-G (EF-G) upon translocation of the tRNAs through the ribosome that several groups have attempted to characterize (Ermolenko and Noller, 2011; Wasserman et al., 2016; Belardinelli et al., 2016a, Nguyen and Whitford, 2016, Guo and Noller, 2012). The process of mRNA-tRNA translocation is coupled to this head domain swivel and tilting which is distinct from other conformational changes the ribosome undergoes including intersubunit rotation (Wasserman et al., 2016; Ratje et al., 2010; Zhou et al., 2013; Zhou et al., 2014; Holtkamp et al., 2014; Belardinelli et al., 2016b; Guo and Noller, 2012, Nguyen and Whitford, 2016). However, the 70S-tRNASufA6 structure is in the absence of EF-G, suggesting that a +1 frameshift event caused by frameshift-prone tRNAs dysregulates some aspect of translocation. Although these studies demonstrate that +1 frameshift-prone tRNAs are good model systems to uncover mechanisms by which both the ribosome and the mRNA-tRNA pair contribute to mRNA frame maintenance, it is unclear whether normal tRNAs lacking modifications result in +1 frameshifting in the same manner. To address this question, here we solved six 70S structures of tRNAPro-CGG in the presence or absence of the m1G37 modification and bound to either cognate or slippery codons in the P site. Our results define how the m1G37 modification stabilizes the interactions of tRNAPro-CGG with the ribosome. We further show that ribosomes bound to mRNA-tRNA pairs that result in +1 frameshifts promoted by tRNAPro-CGG result in large conformational changes of the 30S head domain, consequently biasing the tRNA-mRNA pair toward the E site.

## Results

### A near-cognate interaction between ASLPro and the slippery CCC-U proline codon alone causes a shift into the +1 frame

To address whether tRNAPro-CGG induces a +1 frameshift by a similar mechanism as tRNASufA6, we determined two X-ray structures of ASLPro decoding either a cognate CCG or a near-cognate, slippery CCC-U codon bound at the P site (Figure 1 and Tables 1 and 2). We used chemically synthesized ASLPro (17 nucleotides) to ensure G37 is fully methylated at the N1 position (Figure 1A). The structure of P-site ASLPro interacting with a cognate CCG proline codon was solved to a resolution of 3.1 Å and reveals that the three nucleotides of the anticodon (nucleotides G36-G35-C34) form three Watson–Crick base-pairs with the C+1-C+2-G+3 mRNA codon, respectively (Figure 1A) (mRNA nucleotides are numbered starting at +1 from the P-site codon). The anticodon interacts with the codon in the canonical or 0 mRNA frame indicating a frameshift has not occurred.

**Table 1.**
 RNAs used in this study.


<table>
  <tbody>
    <tr>
      <td>tRNAPro 5’ half</td>
      <td>5’-CGGUGAUUGGCGCAGCCUGGUAGCGCACUUCGUUCGGm1GA-3’</td>
    </tr>
    <tr>
      <td>tRNAPro 3’ half</td>
      <td>5’-CGAAGGGGUCGGAGGUUCGAAUCCUCUAUCACCGACCA-3’</td>
    </tr>
    <tr>
      <td>mRNA_cognate</td>
      <td>5’- GGCAAGGAGGUAAAA CCGG-3’</td>
    </tr>
    <tr>
      <td>mRNA_slippery</td>
      <td>5’- GGCAAGGAGGUAAAA CCCU-3’</td>
    </tr>
  </tbody>
</table>

_The underlined nucleotides indicates the Shine-Dalgarno region while the bold nucleotides are the P-site codons._

**Table 2.**
 Data collection and refinement statistics for 70S-ASLPro structures.


<table>
  <thead>
    <tr>
      <th></th>
      <th>70S-ASLPro-CCG codon</th>
      <th>70S-ASLPro-CCC-U codon</th>
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
      <td>P212121</td>
      <td>P212121</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.9791</td>
      <td>0.9791</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>209.79,451.91,621.58</td>
      <td>210.12,451.80,622.96</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>49.70–3.10 (3.21–3.10)</td>
      <td>49.70–3.40 (3.52–3.40)</td>
    </tr>
    <tr>
      <td>Rpim (%)</td>
      <td>21.2 (80.5)</td>
      <td>14.5 (65.5)</td>
    </tr>
    <tr>
      <td>I/σI</td>
      <td>4.7 (1.1)</td>
      <td>5.9 (1.3)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>97.99 (87.41)</td>
      <td>98.85 (94.87)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>3.7 (3.1)</td>
      <td>4.2 (3.4)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>0.968 (0.250)</td>
      <td>0.987 (0.359)</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Reflections</td>
      <td>1034968 (91757)</td>
      <td>797600 (75973)</td>
    </tr>
    <tr>
      <td>Rwork/Rfree (%)</td>
      <td>24.1/27.2</td>
      <td>19.8/23.7</td>
    </tr>
    <tr>
      <td>No. atoms</td>
      <td>289313</td>
      <td>290047</td>
    </tr>
    <tr>
      <td>B-factors (Å2)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Overall</td>
      <td>90.37</td>
      <td>103.79</td>
    </tr>
    <tr>
      <td>Macromolecule</td>
      <td>90.6</td>
      <td>104.05</td>
    </tr>
    <tr>
      <td>Ligand/ion</td>
      <td>39.43</td>
      <td>43.84</td>
    </tr>
    <tr>
      <td>R.m.s deviations</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.004</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>0.83</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>PDB ID</td>
      <td>6NTA</td>
      <td>6NSH</td>
    </tr>
  </tbody>
</table>

_Highest resolution shell is shown in parentheses._

We next asked how ASLPro interacts in the P site with a CCC-U codon, a slippery codon known to facilitate +1 frameshifts (Björk et al., 1989). In this X-ray structure solved to a resolution of 3.4 Å, we find two different conformations of the codon–anticodon interaction in the two molecules of the crystallographic asymmetric unit (Figure 1C and D and Table 2 and Video 1). Although it is common for one 70S ribosome to contain better electron density than the other in the asymmetric unit in this particular crystal form (Selmer et al., 2006), to our knowledge, it is not common to obtain two different conformational states of the same functional complex. In the first ribosome molecule, nucleotides G36 and G35 of ASLPro form Watson–Crick base-pairs with the first two nucleotides of the 0-frame mRNA codon (Figure 1C). A mismatch C+3•C34 forms at the third base-pair position of the codon–anticodon interaction and contains a single hydrogen bond between the Watson–Crick face of C+3 (the N3 position) and C34 (the N4 position). This codon–anticodon interaction is thus defined as near-cognate because of the single mismatch. The distance between the anticodon nucleotide C34 and the mRNA nucleotide C+3 is increased in the P site as compared to this same mRNA-tRNA pair in the A site (3.6 Å vs. 3.1 Å Maehigashi et al., 2014), indicating that the interaction has weakened. Although this interaction is at the distance limit of a hydrogen bond, C34 and C+3 are positioned to form a cis-Watson–Crick pair, similar to the orientation observed in the A site (Maehigashi et al., 2014; Figure 1—figure supplement 1C). The codon–anticodon interaction is in the 0 frame as indicated by the clear phosphate density of the next mRNA nucleotide, U+4 (Figure 1—figure supplement 1C). The mRNA used in these studies only contained a single nucleotide after the three-nucleotide codon programmed in the P site to allow for the unambiguous identification of the reading frame.

![Video 1.](https://cdn.elifesciences.org/articles/51898/elife-51898-video1.mp4.jpg)

**Video 1.:** An overview of the 70S ribosome (50S is light cyan and the 30S in gray) showing how the anticodon stem-loop (ASL) of tRNAPro (blue) interacts with either a cognate CCG codon or a slippery CCC-U codon (black). The m1G37 modified nucleotide is shown in orange. A zoomed-in view of the anticodon nucleotides (G36, G35, and C34) interacting with the cognate C+1, C+2 and G+3 mRNA respectively, in the 0 frame. All 2Fo-Fc electron density maps shown are contoured at 1.0 σ. A morph from the 0 frame structure to the structure of ASLPro interacting with a slippery CCC-U codon is shown to demonstrate the movement of the mRNA into the +1 frame. The fourth nucleotide of the mRNA codon is shown in green. In either the 0 or +1 frame, a cis Watson–Crick interaction at the third base-pair forms (C+3•C34 or U+4•C34). mRNA numbering starts at +1 according to the first position of the mRNA in the P site.

Strikingly, in the other ribosome molecule in the crystallographic asymmetric unit, the codon–anticodon interaction is in the +1 frame (Figure 1D and Video 1). The first two nucleotides of the anticodon (G36-G35) form Watson–Crick base-pairs with C+2-C+3 nucleotides of the mRNA codon, respectively. The first nucleotide of the proline codon, C+1, no longer interacts with the tRNA and does not appear to make any interactions with the ribosome. At the third position of the codon–anticodon interaction, a cis-Watson–Crick U+4•C34 pair forms that contains a single hydrogen bond between the Watson–Crick face of U+4 (the O4 position) and C34 (the N4 position) (Figure 1—figure supplement 1D). The absence of electron density for the next nucleotide in the mRNA confirms the +1 frame of the codon–anticodon interaction as this is the last nucleotide of the mRNA (Figure 1—figure supplement 1D). Therefore, although the m1G37 modification is present in ASLPro, the shift in the +1 frame can still occur. These data indicate that the presence of a near-cognate, slippery codon is sufficient to promote a +1 mRNA frameshift. Consistent with our observations, biochemical studies of other near-cognate mRNA-tRNA pairs in the P site also show frameshifting in both directions on the mRNA (Zaher and Green, 2009).

### The absence of m1G37 in tRNAPro-CGG bound to a cognate CCG codon does not destabilize its interactions with the ribosome

We next asked how full-length tRNAPro-CGG bound at the P site interacts with mRNA. Our recent structure of the ribosome with +1 frameshift suppressor tRNASufA6 indicated that although the tRNA was placed at the P site, when tRNASufA6 engaged with mRNA that causes +1 frameshifts, the tRNA moves towards the E site and induces large conformational changes of the 30S subunit, specifically the head domain (Hong et al., 2018). We wanted to directly compare these structures given that the +1 frameshift is induced by different signals: an extra nucleotide in the anticodon loop in tRNASufA6 and the absence of m1G37 in tRNAPro-CGG. It is possible that tRNASufA6 causes destabilization and conformational changes of the 30S head domain because of the extra nucleotide in its ASL; such a mechanism would not apply for m1G37 in tRNAPro-CGG. As a control, we solved a structure of tRNAPro-CGG containing the m1G37 modification bound to a cognate CCG codon in the ribosomal P site to a resolution of 3.2 Å (Figure 2A and Table 3 and Video 2). tRNAPro-CGG binds in the classical P/P state (bound to the P site on the 50S and the 30S subunits) and interacts with the proline codon in the 0 frame. Specifically, the G36-G35-C34 anticodon nucleotides form three Watson–Crick base-pairs with the C+1-C+2-G+3 proline codon nucleotides, respectively (Figure 2E, Figure 2—figure supplement 1A and B). The methyl group at position 1 of the nucleobase of G37 stacks with the nucleobase of anticodon nucleotide G36 to form a canonical four-nucleotide stack between nucleotides 34–37. This anticodon stack is important for productive interactions with both mRNA and the ribosome (Maehigashi et al., 2014; Grosjean et al., 1976; Gustilo et al., 2008). The P/P location of tRNAPro-CGG is thus consistent with functional assays demonstrating that tRNAPro isoacceptors do not appear to spontaneously move into the +1 frame on non-slippery codons (Björk et al., 1989; Gamper et al., 2015a).

![Figure 2.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig2-v2.jpg)

**Figure 2.:** Overview of 70S ribosome-tRNAPro complex structures: (A) tRNAPro m1G37 on a cognate CCG codon adopts a P/P orientation (located on the P site on the 30S and 50S subunits); (B) tRNAPro lacking the m1G37 modification (G37 Δm1) on a cognate CCG codon also adopts a P/P orientation; (C) tRNAPro on a +1 slippery CCC-U codon adopts an e*/E orientation (e* denotes the location between the E and P sites on the 30S while "E" is the E site of the 50S); and (D) tRNAPro lacking the m1G37 (G37 Δm1) on a +1 slippery CCC-U codon adopts an e*/E orientation. In this complex (panel D), the 30S head domain and anticodon-codon interaction are disordered. In panels A-D, the 16S rRNA of the 30S head domain is removed for clarity. Zoomed-in view of 2Fo-Fc density of (E) the codon–anticodon for tRNAPro on a cognate CCG codon, (F) tRNAPro G37 (Δm1) on a cognate CCG codon in the P site, and (G) tRNAPro G37 (Δm1) on a near-cognate CCC-U codon in position between the E and the P sites (e*). All 2Fo-Fc electron density maps shown in panels E-G are contoured at 1.0σ.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) 2Fo-Fc electron density for full-length tRNAPro on a cognate codon in the P site. (B) Zoomed-in view of codon–anticodon 2Fo-Fc density for full-length tRNAPro on a cognate CCG codon. (C) 2Fo-Fc density for full-length tRNAPro G37 (Δm1) on a cognate codon in the P site. (D) Zoomed-in view of codon–anticodon 2Fo-Fc density for full-length tRNAPro G37 (Δm1) on a cognate CCG codon. (E) 2Fo-Fc density for full-length tRNAPro on a near-cognate codon in the e* site. (F) Zoomed-in view of codon–anticodon 2Fo-Fc density for tRNAPro on a near-cognate CCC-U codon. (G) 2Fo-Fc density for 16S rRNA and full-length tRNAPro G37 (Δm1) on a near-cognate CCC-U codon in the e* site. The portion of the ASL that lacks density is represented as a hollow blue dashed line. 2Fo-Fc density is is contoured at 1σ for all structures. In the zoomed-in views of panels B, D, and F, the +four position on the mRNA is highlighted in green to indicate the structures are in the 0 frame.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Comparison of the A-minor motif interactions of G1338 with tRNAPro U29-A41 base-pairs (A) and A1339 with tRNAPro C30-G40 base-pairs in (D) 70S-tRNAPro bound to a cognate CCG codon. (B,E) 70S-tRNAPro G37 (Δm1) bound to a cognate CCG codon. (C,F) 70S-tRNAPro bound to a near-cognate CCC-U codon. 2Fo-Fc density for G1338 and A1339 is contoured at 1σ.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) 2Fo-Fc density at 1.0σ of 16S rRNA in the 70S-tRNAPro bound to a cognate CCG codon. (B) 2Fo-Fc density at 1.0σ of 16S rRNA in the 70S-tRNAPro G37 (Δm1) bound to a near-cognate CCC-U codon. (C,D) The same ribosome complexes as in panels A and B but with 2Fo-Fc electron density increased to 1.5σ.

![Video 2.](https://cdn.elifesciences.org/articles/51898/elife-51898-video2.mp4.jpg)

**Video 2.:** An overview of the 70S ribosome (50S is light cyan and the 30S in gray) showing how tRNAPro (blue) (+/- m1G37) interacts with either a cognate CCG codon or a slippery CCC-U codon (black). A zoomed-in view of the anticodon nucleotides (G36, G35, and C34) interacting with the cognate C+1, C+2, and G+3 mRNA respectively, in the 0 frame. All 2Fo-Fc electron density maps shown are contoured at 1.0σ. The m1G37 modified nucleotide is shown in orange and the U32-A38 pairing is indicated. A morph of the changes of the U32-A38 pairing when the tRNA interacts with either a cognate CCG or a slippery CCC-U codon is shown. An overview and a morph of P/P tRNAPro bound to a cognate CCG codon to the e*/E site along with movement of the 30S head domain is shown. Lastly, a zoomed-in view shows a morph from a 0 frame codon-anticodon interaction that forms in the P/P site to the pairing in the e*/E site.

We next solved a 3.9 Å structure of tRNAPro-CGG lacking the m1G37 modification (G37 Δm1) and interacting with a cognate CCG proline codon in the P site (Figure 2B, Figure 2—figure supplement 1C and D and Table 3 and Video 2). Although the m1G37 modification was previously shown to be critical for high-affinity binding and decoding of the cognate CCG codon at the A site (Nguyen et al., 2019), its influence on the overall conformation of tRNAPro-CGG in the P site appears to be minimal as the tRNA adopts a P/P orientation (Figure 2B). Notably, the mRNA remains in the 0 frame with three Watson–Crick base-pair interactions between the codon and the anticodon (Figure 2F). Similar to the structural studies of the ASLPro in the 0 frame (Figure 1B and D), the mRNA used in these studies contains an additional nucleotide after the P-site CCG codon (Figure 1; Figure 2B and Table 1). The mRNA has clear phosphate density for the single A-site nucleotide indicating the mRNA remains in the 0 frame (Figure 2—figure supplement 1D). The absence of the m1G37 modification correlates with a slightly weaker U32-A38 pairing when compared to modified tRNAPro-CGG (Figure 2—figure supplement 2B). These structures suggest that the absence of 1-methyl modification on G37 alone is not sufficient to destabilize the tRNA in the P site of the ribosome. This observation is also consistent with toeprint analyses demonstrating that tRNAPro-GGG lacking m1G37 on a non-slippery codon remained in the 0 frame (Gamper et al., 2015a).

### A CCC-U slippery proline codon in the P site causes tRNAPro-CGG destabilization and 30S head movement

In an attempt to reconcile the exact role of the m1G37 modification in tRNAPro-CGG in the context of a +1 slippery CCC-U codon, we next solved a ribosome structure of this complex in the P site to a resolution of 3.2 Å (Figure 2C and Table 3 and Video 2). Unexpectedly, tRNAPro-CGG moves from the P site towards the E site, adopting a position on the ribosome which we refer to as e*/E (Hong et al., 2018) (where e* signifies an intermediate position between the 30S subunit P and the E sites and E signifies a 50S E-site position) (Figure 2C, Figure 2—figure supplement 1E). The e*/E position of tRNAPro-CGG when bound to this slippery codon is different from the classical P/P position that the same tRNA adopts when it interacts with a cognate CCG codon (compare Figure 2A with Figure 2C). The classical P/P tRNAPro-CGG location on its cognate codon is consistent with dozens of other P-site tRNA bound ribosome structures. Therefore, the ability of tRNAPro-CGG to move towards the E site when bound to a slippery proline codon suggests that it is this near-cognate codon–anticodon interaction alone that is sufficient to destabilize tRNAPro-CGG (Figure 2C).

**Table 3.**
 Data collection and refinement statistics for 70S-tRNAPro structures.Highest resolution shell is shown in parentheses.


<table>
  <thead>
    <tr>
      <th></th>
      <th>tRNAPro m1G37-CCG codon</th>
      <th>tRNAPro m1G37-CCC-U codon</th>
      <th>tRNAPro G37(Δm1)-CCG codon</th>
      <th>tRNAPro G37(Δm1)-CCC-U codon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.9792</td>
      <td>0.9792</td>
      <td>0.9792</td>
      <td>0.9792</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>210.20,451.47,620.21</td>
      <td>210.74,450.26,626.11</td>
      <td>209.97,450.71,619.40</td>
      <td>210.09,450.32,622.89</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>49.20–3.20 (3.31–3.20)</td>
      <td>49.93–3.50 (3.63–3.50)</td>
      <td>49.82–3.97 (4.11–3.97)</td>
      <td>49.83–4.14 (4.29–4.14)</td>
    </tr>
    <tr>
      <td>Rpim (%)</td>
      <td>11.5 (51.7)</td>
      <td>9.00 (44.1)</td>
      <td>8.60 (86.0)</td>
      <td>9.807 (95.5)</td>
    </tr>
    <tr>
      <td>I/σI</td>
      <td>6.7 (1.5)</td>
      <td>7.8 (1.7)</td>
      <td>6.3 (1.0)</td>
      <td>5.1 (1.0)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>99.11 (98.45)</td>
      <td>97.55 (89.72)</td>
      <td>98.60 (95.72)</td>
      <td>98.39 (95.63)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>5.9 (4.4)</td>
      <td>4.2 (2.2)</td>
      <td>14.1 (10.0)</td>
      <td>6.5 (3.6)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>0.991 (0.377)</td>
      <td>0.996 (0.464)</td>
      <td>0.998 (0.313)</td>
      <td>0.998 (0.37)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Reflections</td>
      <td>951115 (93932)</td>
      <td>723555 (66052)</td>
      <td>4959167 (47742)</td>
      <td>439195 (42360)</td>
    </tr>
    <tr>
      <td>Rwork/Rfree (%)</td>
      <td>22.8/25.6</td>
      <td>23.4/25.6</td>
      <td>22.8/25.5</td>
      <td>24.8/29.4</td>
    </tr>
    <tr>
      <td>No. atoms</td>
      <td>291966</td>
      <td>292039</td>
      <td>291793</td>
      <td>291185</td>
    </tr>
    <tr>
      <td>B-factors (Å2)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Overall</td>
      <td>103.87</td>
      <td>113.6</td>
      <td>177.39</td>
      <td>247.09</td>
    </tr>
    <tr>
      <td>Macromolecule</td>
      <td>104.12</td>
      <td>113.9</td>
      <td>177.77</td>
      <td>247.54</td>
    </tr>
    <tr>
      <td>Ligand/ion</td>
      <td>42.04</td>
      <td>37.71</td>
      <td>72.42</td>
      <td>123.12</td>
    </tr>
    <tr>
      <td>R.m.s deviations</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.011</td>
      <td>0.010</td>
      <td>0.007</td>
      <td>0.007</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>1.00</td>
      <td>1.23</td>
      <td>0.94</td>
      <td>1.38</td>
    </tr>
    <tr>
      <td>PDB ID</td>
      <td>6NUO</td>
      <td>6NWY</td>
      <td>6O3M</td>
      <td>6OSI</td>
    </tr>
  </tbody>
</table>

The e*/E position of the tRNAPro-CGG-mRNA pair is additionally coupled to large conformational changes of the 30S head domain (Figure 3 and Video 2). 30S head motions accompanying canonical translocation or caused by a frameshift-prone tRNAs have been previously described by our group and others (Hong et al., 2018; Ratje et al., 2010; Zhou et al., 2013; Zhou et al., 2014; Mohan et al., 2014; Zhou et al., 2019), but the two distinct movements of "swiveling" and "tilting" have never been analyzed separately (Figure 3). To more precisely describe this multidimensional motion, we used previously reported procedures to define ‘swivel’ as the movement of the head relative to the body within a plane (i.e. pure rotation about a single axis defined by structures of the unrotated and swiveled conformations (using PDB codes 4V9D and 4V4Q, respectively)), while ‘tilt’ describes any deviations from pure rotation (Nguyen and Whitford, 2016). Together, these more accurate calculations provide an unambiguous description of the full, three-dimensional orientation of the head during translocation, where the tRNAs are found in intermediate states (Zhou et al., 2013; Zhou et al., 2014). The head domain swivels in a ~18° counterclockwise direction while also undergoing a ~5° tilt away from the ribosome and perpendicular to the mRNA path (Ratje et al., 2010; Zhou et al., 2013; Zhou et al., 2014) (the counterclockwise swivel is defined of the ribosome viewed with the E-, P-, A-tRNA sites oriented from left to right as depicted in Figure 2). The head domain is comprised of 16S rRNA nucleotides 930–1380 and seven ribosomal proteins (S3, S7, S9, S10, S13, S14, and S19) (Belardinelli et al., 2016a; Guo and Noller, 2012) that collectively move as a rigid body during EF-G-mediated translocation of the mRNA-tRNA pairs on the 30S (Ratje et al., 2010; Zhou et al., 2013; Zhou et al., 2014). The same swivel and tilting of the head domain of e*/E tRNAPro-CGG occurs but our structure lacks EF-G. This result indicates that even with the m1G37 modification, interactions of tRNAPro-CGG with the P site are destabilized when bound to a near-cognate codon, promoting its movement toward the E site along with 30S head domain swivel and tilting.

![Figure 3.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig3-v2.jpg)

**Figure 3.:** (A) Overview of the 70S ribosome containing an e*/E tRNAPro bound to a +1 slippery CCC-U codon. Shifts in phosphate atom positions of the 30S head domain (16S rRNA nucleotides 930–1380) in this structure as compared to the unrotated 70S (PDB code 4V5C) are shown as two vectors corresponding to the two directions of rotation/swivel (blue) and tilt (orange and yellow). (B) Top, same view as in panel A but showing only the tilt of the head domain. Bottom, a 90° rotated view showing the tilt is downward resulting in movement of the head domain away from the body domain. (C) Left, the same view as in panel A with only the counterclockwise swivel/rotation of the head domain indicated (left). Right, a 90° horizontal rotated view shows that the swivel is greatest toward the subunit interface, close to e*/E tRNAPro and on the surface of the ribosome.

### The mRNA located in the 30S E and P sites is constricted when tRNAPro-CGG adopts an e*/E position

The path of the mRNA on the ribosome accommodates three nucleotides, or a single codon, in each of the A, P, and E sites (Figure 4A and B). The ribosome interacts extensively with the mRNA in the A site to ensure accurate decoding but interacts less substantially with the P-site codon, while the E-site mRNA codon is the least monitored. The ribosome interacts with E-site mRNA at two positions through non-sequence-specific contacts: 16S rRNA nucleotide G693 stacks with the first nucleotide of the E-site mRNA codon and the G926 nucleobase contacts the phosphate of the third mRNA codon nucleotide (Figure 4B and C; Selmer et al., 2006). The e* position of tRNAPro-CGG signifies that the tRNA is closer to the E site than the P site on the 30S, however it is similar to the pe/E tRNA position seen in translocation intermediate ribosome structures containing EF-G (Figure 4D; Zhou et al., 2014). Only two nucleotides of the codon–anticodon interaction of the pe/E tRNA are positioned in the E site leaving a pocket for an additional nucleotide to occupy upon full translocation of the mRNA-tRNA pair (Zhou et al., 2013; Zhou et al., 2014) (compare Figure 4C with Figure 4D). In our structure containing an e*/E tRNAPro-CGG bound to a near-cognate, slippery codon, the first three nucleotides of the codon fully occupy the E site (Figure 4E), despite the codon–anticodon adopting an intermediate position on the 30S between the P and the E sites. This compaction of the mRNA means there is no space for the entire four-nucleotide codon in the E site upon full translocation of the mRNA-tRNA pair. Additionally, the mRNA path 5’ from the E site turns sharply by ~100° as the mRNA transits to the outside of the ribosome (Figure 4C). In the case of e*/E tRNAPro-CGG, upon full translocation of the mRNA-tRNA pair to the E site, the first nucleotide of the codon would be displaced from the E site to accommodate the three-nucleotide codon or the last three nucleotides of the CCC-U codon. This placement would position the mRNA in the +1 frame.

![Figure 4.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig4-v2.jpg)

**Figure 4.:** (A) Overview of the 70S ribosome with (B) a zoomed-in view of the mRNA-tRNA interaction in the A, P, and E sites (PDB code 4V6F). 16S rRNA nucleotides G693 and G926 interact with the E-site codon–anticodon. (C) The normal path of the mRNA (black) in a ribosome structure containing P/P and E/E tRNAs demonstrates only a three-nucleotide codon (nucleotides +1, +2 and +3) is accommodated in the E site (PDB code 4V5F). 16S rRNA G693 defines the starts of the E-site codon and interacts with the first nucleotide. As the mRNA leaves the E site, there is a 100° kink between the first nucleotide of the E-site codon (+1) and the −1 nucleotide (shaded in purple). Panel C is rotated ~180° relative to the view in panel B. (D) A translocation intermediate structure induced by EF-G contains a tRNA positioned between the P and the E sites on the 30S (denoted ‘pe’). The pe/E tRNA has not undergone full translocation to the E site and thus only two nucleotides (+1 and +2) are located in the E site (PDB code 4W29). In this translocation intermediate state, there is space available to accommodate an additional nucleotide of the codon (shaded in red) that would occur upon full translocation. (E) tRNAPro bound to a +1 slippery CCC-U codon reveals that although the codon–anticodon pair has not been fully translocated, this placement of the mRNA is different as compared to normal translocation intermediates structures as shown in panel D. The additional nucleotide (+4) of the four-nucleotide codon is shown in green.

The mRNA boundary between the P and the E sites on the 30S subunit appears to be demarcated by 16S rRNA nucleotide G926 (Figure 4B and C; Selmer et al., 2006). G926 interacts with the phosphate of the +3 nucleotide of the E-site codon thus defining its 3’-end (Figure 4C). In our structure of tRNAPro-CGG interacting with a near-cognate, +1 slippery codon, G926 instead interacts with U+4 of the CCC-U codon rather than the third nucleotide, thereby defining U+4 as the end of the E-site codon (Figure 4E). Even in translocation intermediate ribosome structures containing EF-G, G926 interacts with the +3 phosphate of the mRNA, although this ribosome complex contains a cognate mRNA-tRNA pair (Figure 4D; Zhou et al., 2014). Comparison of post-translocation (Gao et al., 2009), translocation intermediate (Zhou et al., 2013; Zhou et al., 2014), and our structure presented here reveals that the position of G926 in all three is very similar, while it is the position of the mRNA that changes substantially (Figure 4C, D and E). In summary, although tRNAPro-CGG moves to the E site in our structure presented here, the four-nucleotide mRNA codon is compacted in the E site as if translocation has already taken place (Figure 4E).

### The G966-C1400 bridge connecting the 30S head and body domains is broken in the presence of a near-cognate codon–anticodon interaction

The ribosome minimally interacts with the mRNA-tRNA pair in the P site: 16S rRNA C1400 contacts G966 and stacks with the third base-pair of the codon–anticodon (Figure 5A; Selmer et al., 2006). The G966-C1400 pair remains intact during translocation of the mRNA-tRNA pair from the P to the E site as part of the head domain, as evidenced by ribosome structures in translocation intermediate states containing EF-G (Figure 5B). (Zhou et al., 2013; Zhou et al., 2014). In our structure containing e*/E tRNAPro-CGG bound to a CCC-U codon, the G966-C1400 interaction is ablated (Figure 5C). Since the G966-C1400 interaction is effectively the bridge between the head and body domains, this disruption can be attributed to a dysregulation caused by this spontaneous translocation event.

![Figure 5.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig5-v2.jpg)

**Figure 5.:** (A) In a post-translocation state containing E/E, P/P and A/A tRNAs, 16S rRNA nucleotides G966 and C1400 are located beneath the P-site tRNA (PDB code 4V5F). (B) The G966 and C1400 interaction remains intact during EF-G-mediated translocation as the position of 30S head domain nucleotide G966 shifts while 30S body nucleotide C1400 remains constant (PDB code 4W29). (C) In a ribosome undergoing a +1 frameshift induced by tRNAPro and a slippery CCC-U codon, the G966-C1400 interaction is broken. The additional nucleotide (+4) of the four-nucleotide codon is shown in green.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/51898/elife-51898-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) 70S P-site ASLPro interacting with a cognate CCG codon in the 0 frame. (B) 70S P-site ASLPro interacting with a near-cognate CCC-U codon in the 0 frame. (C) 70S P-site ASLPro interacting with a near-cognate CCC-U codon in the +1 frame. 16S rRNA nucleotides G1338, A1339, C1400, and G966 are shown in panels A-C. The following interactions for each of these three structures are shown beneath. G1338 contacts the minor groove of ASLPro at nucleotides U29-A41 in the structrue of 70S P-site ASLPro interacting with a cognate CCG codon in the 0 frame (D), in the structure of 70S P-site ASLPro interacting with a near-cognate CCC-U codon in the 0 frame (E) and in the structure of 70S P-site ASLPro interacting with a near-cognate CCC-U codon in the +1 frame (F). A1339 contacts ASLPro at nucleotides C30-G40 in the structrue of 70S P-site ASLPro interacting with a cognate CCG codon in the 0 frame (G), in the structure of 70S P-site ASLPro interacting with a near-cognate CCC-U codon in the 0 frame (H) and in the structure of 70S P-site ASLPro interacting with a near-cognate CCC-U codon in the +1 frame (I). 2Fo-Fc density for G1338 and A1339 is contoured at 1σ for all structures. (J) C1400 stacks with G+3 mRNA and ASLPro C34 in the structrue of 70S P-site ASLPro interacting with a cognate CCG codon in the 0 frame (J), in the structure of 70S P-site ASLPro interacting with a near-cognate CCC-U codon in the 0 frame (K) and in the structure of 70S P-site ASLPro interacting with a near-cognate CCC-U codon in the +1 frame (L). The distance cutoff for a hydrogen bondt between 16S and ASLPro is 3.5 Å.

### The absence of the m1G37 modification in tRNAPro-CGG coupled with a +1 slippery codon–anticodon interaction causes disordering of the 30S head domain

Finally, we solved a 4.1 Å structure of tRNAPro-CGG lacking m1G37(Δm1) and interacting with a near-cognate, slippery CCC-U codon at the P site. The electron density for the majority of the tRNAPro-CGG on the 50S subunit is well-resolved, indicating that, similar to the analogous structure solved in the presence of the m1G37 modification (Figure 2C), the tRNA has also moved towards the E site on the 50S subunit (Figure 2D). In contrast, the electron density is weak for the tRNAPro-CGG ASL and E-site mRNA indicating these regions are dynamic in the context of slippery codon and in the absence of m1G37 modification (Figure 2D, Figure 2—figure supplement 2G). Disordering of tRNAPro G37(Δm1) starts approximately at the beginning of the anticodon loop at nucleotides U32-A38. Correspondingly, the 30S head domain region is also disordered (Figure 2D, Figure 2—figure supplement 3D), whereas the only region of the 30S body domain with poor electron density is the P/E loop nucleotides G1338 and A1339. Taken together, in this mRNA-tRNA pairing that causes high levels of frameshifting, interactions with the tRNA are destabilized in the P site resulting in the codon–anticodon adopting an e* location and high mobility of the 30S head domain.

## Discussion

The importance of tRNA modifications in protein synthesis has been recognized for decades, yet the precise roles of modifications located outside the anticodon have been elusive. Modifications in the anticodon loop at position 37 of tRNAs have been implicated in mRNA frame maintenance (Urbonavicius et al., 2001; Yarian et al., 2002), but how the absence of a single methylation can dysregulate the mRNA frame remained unclear. Here, we elucidated the role of m1G37 in tRNAPro-CGG, which was known to be important in stabilizing stacking interactions with anticodon nucleotides during decoding at the A site (Maehigashi et al., 2014) and in the prevention of frameshifting (Björk et al., 1989; Hagervall et al., 1993). We find that this single methyl group influences the overall stability of tRNAPro-CGG on the ribosome in an unexpected manner and causes large conformational changes between the tRNA and the 30S head domain, a domain known to move extensively during translocation of the tRNAs (Wasserman et al., 2016; Ratje et al., 2010; Zhou et al., 2013; Zhou et al., 2014). However, the methylation alone does not stabilize tRNAPro-CGG on the ribosome and, instead, its position is heavily influenced by interactions with a slippery proline codon. Our structures of different mRNA-tRNAPro-CGG pairs on the ribosome reveals the first detailed mechanistic insight into how mRNA frame maintenance is regulated by both the m1G37 modification and the stability of mRNA-tRNA interaction.

The location on the ribosome where frameshifting can occur is likely dependent on the type of frameshift (in the positive or negative directionon the mRNA) and whether tRNA or mRNA causes the frameshift (Dinman, 2012; Dunkle and Dunham, 2015; Atkins et al., 2016; Korniy et al., 2019). The ribosome itself can prevent frameshifts through inherent differences in how the ribosome interacts with the tRNA-mRNA complex at the different tRNA binding sites and such differences could potentially influence frameshifting by relaxing interactions, for example, between the codon and anticodon. While the codon–anticodon interaction located in the 30S A site is strictly monitored by conserved 16S rRNA nucleotides to select for cognate tRNA (Ogle et al., 2002), there are comparatively few interactions with the codon–anticodon when positioned within the P and E sites, underscoring their different functional roles during the translation cycle. The relative absence of interactions in the P and E sites provides an opportunity for the mRNA to shift out of frame. Some tRNAPro isoacceptors frameshift either during translocation from the A to the P site or after the translocation step and once positioned in the P site (Gamper et al., 2015a; Gamper et al., 2015b). Therefore we sought to capture the interactions of tRNAPro during a frameshift event. The structure of ASLPro bound to a slippery codon in the P site reveals the codon–anticodon interaction has shifted into the +1 frame indicating that the anticodon stem-loop interaction with the mRNA codon alone is important for frameshifting (Figure 1D). This frameshift is likely possible because interactions with the P-site tRNA are limited to only 16S rRNA P/E loop nucleotides G1338 and A1339 with the anticodon stem and 16S rRNA C1400 with the anticodon nucleotide 34 (Figure 5A, Figure 5—figure supplement 1). The P/E loop appears to indirectly enforce the mRNA frame by gripping the P-site tRNA and these interactions are maintained as the tRNA moves from the P site to a hybrid P/E state (Dunkle et al., 2011) and to a translocation intermediate pe/E state (Zhou et al., 2013). In the structures of ASLPro interacting with the mRNA in the 0 frame, there is well-resolved density for G1338 and A1339 (Figure 1B and C, Figure 1—figure supplement 1A,D, G), while there is some disordering of these nucleotides in the context of ASLPro bound to the near-cognate, slippery codon in the +1 frame (Figure 1—figure supplement 1C, F and I). The inability for G1338 and A1339 to grip the anticodon stem when the codon–anticodon is in the +1 frame likely results in the destabilization of full-length tRNAPro in these frameshift-competent contexts (Figure 2C and D). Simulations of the ribosome undergoing large movements of the head domain during translocation implicate nucleotides G1338 and A1339 in the coupling of 30S head dynamics and displacement of the P-site tRNA towards the E site (Nguyen and Whitford, 2016). Therefore, the lack of gripping by the P/E loop in the P site when a destabilized mRNA-tRNA interaction is present, appears to bias tRNAPro toward the E site which, in turn, causes the 30S head domain to swivel and tilt as if EF-G were bound.

In addition to P/E loop nucleotides G1338 and A1339, 16S rRNA nucleotide G966 is also part of the 30S head domain and stacks with nucleotide 34 of the P-site tRNA anticodon (Figure 5A). The 30S head is connected to the body domain via interactions of G966 with nucleotide C1400; the G966-C1400 pair remains stacked beneath the P-site tRNA and follows the tRNA as it moves to a hybrid P/E state and to a translocation pe/E intermediate state upon EF-G binding (Figure 5B; Zhou et al., 2013; Zhou et al., 2014; Dunkle et al., 2011). In the case of P-site ASLPro interacting with a +1 slippery codon in the 0 or +1 frame, cis-Watson–Crick interactions form between C+3•C34 and U+4•C34, respectively (Figure 1—figure supplement 1K and L). Both the C+3•C34 and U+4•C34 interactions appear to result in reduced stacking with C1400. In structures of full-length tRNAPro-mRNA pairs that cause +1 frameshifting and destabilization at the P site, the G966-C1400 interaction is broken (Figure 5C). Together, these results suggest a connection between the reduced interactions of G1338-A1339 and G966-C1400 with the tRNA that appear to influence the movement of the P-site tRNA towards the E site.

Although neither C1400 nor G966 have previously been implicated in mRNA frame maintenance, there is a functional link between the P/E loop nucleotides G1338 and A1339 and C1400-G966. 16S rRNA nucleotides in the P site are generally more tolerable of mutations than the A-site 16S rRNA, although substitution of G966 substantially reduces ribosome activity to ~10% despite the mutation not being lethal (Abdi and Fredrick, 2005). This G966 mutant is suppressed by a G1338A mutation, indicating that the G1338A mutation can stabilize interactions with the P-site tRNA even in the absence of the C1400-G966 interaction.

The interactions observed between the codon and anticodon of ASLPro bound to either cognate or near-cognate codons reveal the process of shifting into the +1 frame (Figure 1D). In the context of full-length mRNA-tRNA pairs that cause +1 frameshifting, both the tRNA and mRNA move from the P site to occupy a position between the E and the P site (Figure 2C and D). This mRNA-tRNA placement is similar to the translocation intermediate containing EF-G (Zhou et al., 2013). In the structure presented here containing an e*/E tRNAPro as compared to the EF-G containing structures containing an pe/tRNA, e*/E tRNAPro is positioned slightly further away from the mRNA. In the e*/E tRNAPro-CGG structure, the first position of the codon–anticodon forms a Watson–Crick interaction but the second and third nucleotides of the codon–anticodon are not within hydrogen bonding distances (Figure 2G). Interestingly, in the EF-G-bound translocation intermediate structures, the codon–anticodon is also not within bonding distance (Zhou et al., 2013). These results suggest that it is the disruptive nature of moving between tRNA binding sites that perturbs the interactions between the codon and anticodon and these interactions likely reform once the transition to the next tRNA binding site is complete.

30S head domain conformational changes were first captured in ribosome structures of tRNAs moving between the A to the P sites (ap/ap state) and between the P and the E sites (pe/E state) on the 30S in the presence of EF-G (Zhou et al., 2013; Zhou et al., 2014; Dunkle et al., 2011; Ratje et al., 2010). Upon EF-G binding, the head domain is predicted to first tilt and then swivel in a counterclockwise manner (as viewed with the E, P, A tRNA sites from left to right shown in Figure 2) to translocate the two tRNAs to final E/E and P/P positions (Wasserman et al., 2016; Nguyen and Whitford, 2016). The departure of EF-G and reverse tilting of the head back towards the intersubunit space is followed by clockwise swivel, the rate-limiting step for translocation (Wasserman et al., 2016). Frameshift-prone tRNAs, such as tRNAPro-CGG, cause spontaneous head swiveling and tilting once the tRNA occupies the P site after the mRNA frameshift has occurred. The inability of the ribosome to hold the P-site tRNA is influenced by weakening of the interactions of the P/E loop with the anticodon stem and by disruption of the C1400-G966 interaction, both events likely major contributors to the dysregulation of the 30S head domain. In other words, the head domain is unable to maintain extensive interactions with the P-site tRNA and this failure leads to spontaneous translocation. Single molecule FRET (smFRET) studies of translocation events also show that upon tRNA movement from the P to the E site, there is increased dissociation of the tRNA from the ribosome, bypassing the post-translocation E/E state (Wasserman et al., 2016). These data seem to suggest that even during canonical translocation from the P to the E site, this is a highly dynamic process which leads to destabilized tRNA. Consistent with these observations, we would expect that once EF-G fully translocates tRNAPro-CGG to the post E/E state, there may be a further decrease in interactions between the tRNA and ribosome. Additionally, our structures show 30S head swiveling and tilting in the absence of EF-G, concurrent with the +1 frameshift event. This 30S head swivel and tilt movement would likely prevent EF-G from binding until the the head resets to a non-rotated state. EF-G residues located in the tip of domain IV interact with the anticodon stem-loop of the A-site tRNA during translocation to the P site (Zhou et al., 2013) and mutations in this domain slow the rate of translocation (Rodnina et al., 1997; Savelsbergh et al., 2000). Recent studies using slippery codon sequences where spontaneous frameshifting occurs, EF-G can restrict frameshifting and helps to maintain the mRNA frame (Peng et al., 2019). It is therefore an enticing hypothesis that EF-G may have a role in mRNA frame maintenance in addition to its established function in translocation.

Although all three prokaryotic tRNAPro isoacceptors have the capacity to frameshift, whether they use similar mechanisms of action is unknown (Björk et al., 1989; Gamper et al., 2015a; Qian et al., 1998; O'Connor, 2002). The m1G37 modification minimally influences frameshifting in proline isoacceptor tRNAPro-GGG (proL) in contrast to tRNAPro-cmo5UGG (proM) (Gamper et al., 2015a). An additional difference is the dependency on elongation factor-P (EF-P) to reconcile +1 frameshifts. EF-P binds at the E site to overcome ribosome stalling induced by poly-proline codons (Ude et al., 2013; Huter et al., 2017) and is critical in suppressing frameshifts on poly-proline stretches (Gamper et al., 2015a). While EF-P reduces +1 frameshifts with tRNAPro-GGG G37(Δm1) to an equivalent frequency as native tRNAPro-GGG, the absence or presence of m1G37 has little influence on the ability of isoacceptor tRNAPro-cmo5UGG to frameshift (Gamper et al., 2015a). These mechanistic differences may be due to a combination of the codon–anticodon pairings on slippery codons (tRNAPro-cmo5UGG and tRNAPro-GGG are cognate with slippery codons while tRNAPro-CGG is near-cognate [Nasvall et al., 2004]) and/or the influence of other modifications such as the cmo5U34 modification in tRNAPro-cmo5UGG (Masuda et al., 2018). Further considerations may be the location of the slippery codon on the mRNA, which would have varying nascent chain lengths, and whether the following codon after the slippery codon is rare (Gamper et al., 2015a). Our structures show that both the m1G37 modification status of tRNAPro-CGG and the CCC-U codon causes the tRNA to become destabilized and its position is biased towards the E site, which we predict is indicative of high levels of frameshifting. The possible synergistic effects of cmo5U34 and m1G37 in tRNAPro-cmo5UGG in preventing frameshifts is unclear, but tRNAPro-UGG lacking all modifications exhibits higher levels of frameshifting as compared to tRNAPro-UGG lacking only the m1G37 modification (Gamper et al., 2015b). Since the presence of m1G37 in tRNAPro-cmo5UGG may restrict its movement to the e*/E position, this tRNA isoaccepor may no longer be an optimal substrate for EF-P, which is consistent with kinetic analyses (Gamper et al., 2015a). Together, our structures of tRNAPro-CGG in frameshifting contexts provides new insights into how RNA modifications impact tRNA stability on the ribosome.

## Materials and methods

### mRNA, ASL, and ribosome purification

ASLPro containing a m1G37 modified anticodon stem-loop (17 nucleotides) and mRNA (19 nucleotides) were purchased from GE Healthcare Dharmacon and dissolved in 10 mM Tris-HCl, pH 7.0, and 5 mM MgCl2. We used a chemically synthesized ASL to ensure complete m1G modification at position 37, as previously used to examine interactions in the A site (Maehigashi et al., 2014). Purification of Thermus thermophilus 70S ribosomes was performed as previously described (Zhang et al., 2018).

### tRNAPro-CGG ligation and purification

To ensure that tRNAPro-CGG was methylated at tRNA nucleotide 37 (m1G), the 5’ half of the tRNA (nucleotides 1–39) was chemically synthesized (GE Healthcare Dharmacon) and enzymatically ligated to the chemically synthesized 3’ half following established protocols (Sherlin et al., 2001; Stark and Rader, 2014). Briefly, T4 polynucleotide kinase (NEB) was used to phosphorylate the 5’ end of the 3’ tRNA half and was heat inactivated. The 5’ and 3’ halves of each tRNA were then mixed and annealed in the T4 RNA ligase buffer by heating to 80°C for five min and slow cooling on the heat block to room temperature. T4 RNA ligase (NEB) was added to the reaction at 37°C for 18 hr. The ligation reaction was run on a 12% denaturing 8M urea-polyacrylamide gel and the ligated fragment was excised and purified using a modified crush and soak method (Stark and Rader, 2014). The RNA was ethanol precipitated, the pellet was thoroughly air dried and resuspended in 10 mM Tris-HCl, pH 7.0 and 5 mM MgCl2, followed by annealing at 70°C for 2 min and slow cooled to room temperature on the benchtop. The purified full-length RNA was aliquoted and stored at −20°C.

### Structural studies

ASLPro complexes were formed with 3.5 μM 70S ribosomes programmed with 7 µM mRNA for 6 min at 37°C. Then 22 µM ASLPro was added and incubated for 30 min at 55°C. tRNAPro-CGG and tRNAPro-CGG G37 (Δm1G) complexes were formed with 3.5–4.4 μM of 70S ribosomes programmed with 7–10.5 µM mRNA for 6 min at 37°C. Then 7.7–10.5 µM tRNAPro-CGG or tRNAPro-CGG G37(Δm1G) were incubated for 30 min at 55°C. Each ASL and tRNA were positioned in the ribosomal P site by designing the Shine-Dalgarno sequence eleven nucleotides upstream of the P-site codon. Crystals were grown by sitting-drop vapor diffusion in a 1:1 drop ratio of 100 mM Tris–acetate pH 7.6, 12–13% 2-methyl-2,4-pentanediol (MPD), 2.9–3.0% polyethylene glycol (PEG) 20K, 100–150 mM L-arginine-HCl and 0.5–1 mM β-mercaptoethanol (β-Me). ASLPro crystals were cryoprotected step-wise in 100 mM Tris–acetate pH 7.6, 10 mM NH4Cl, 50 mM KCl, 3.1% PEG 20K, 10 mM Mg(CH3COO)2, 6 mM β-Me and 20–40% MPD, with the final cryoprotection solution containing 30 μM ASLPro. Cryoprotection of tRNAPro-CGG and tRNAPro-CGG G37 (Δm1G) was accomplished similarly to ASLPro, except with 3% PEG 20K and 20 mM Mg(CH3COO)2. Additionally, the final cryoprotection solution for both tRNAPro-CGG and tRNAPro-CGG G37 (Δm1G) did not contain ligand. All crystals were flash frozen in liquid nitrogen for data collection.

X-ray diffraction data were collected at the Southeast Regional Collaborative Access Team (SER-CAT) 22-ID beamline line and the Northeastern Collaborative Access Team (NE-CAT) ID24-C and ID24-E beamlines at the Advanced Photon Source (APS). Data were integrated and scaled using the program XDS (Kabsch, 2010). All structures of 70S-ASLPro- and tRNAPro-CGG bound to cognate mRNA were solved by molecular replacement in PHENIX using coordinates from a 70S structure containing mRNA and tRNAs (PDB code 4V6G) (Jenner et al., 2010; Adams et al., 2010). For the 70S complex containing an e*/E tRNA and mRNA, the start model was changed to tRNASufA6 bound to a slippery sequence (PDB code 5VPP) (Hong et al., 2018). In this structure, the 30S head domain is swiveled ~18°. The structure was solved by molecular replacement in PHENIX followed by iterative rounds of manual building in Coot (Emsley et al., 2010). All figures were prepared in PyMOL (Schrodinger LLC, 2010).

### Calculating 30S head movement

The following protocol was used to describe the 30S head and body domains in terms of Euler angles (ϕ,ψ,θ). Here, ϕ+ψ defines the net swivel angle, tilting is described by θ and the tilt direction is defined by ϕ. Euler angles were calculated separately for the 16S body and head domains as previously defined (Nguyen and Whitford, 2016). Briefly, for all calculations, the P atoms of the ‘core’ residues of the 23S rRNA and 16S head/body were considered. The core residues are defined as the set of atoms that were found to have spatial root mean squared fluctuations of less than 1 Å in a one microsecond explicit-solvent simulation (Whitford et al., 2013). This includes 1351, 442, and 178 residues in the 23S rRNA, 16S body, and 16S head, respectively. To ensure that the calculated angles reflect global domain orientations, rather than local deformations, reference configurations of the 23S, as well as the 16S head and body, were aligned to each group of core residues, separately. To calculate 16S body swivel angles, each model was first aligned to a crystallographic model of a classical unrotated ribosome (PDB codes 4V9D:DA and 4V9D:BA), where alignment was based on the 23S rRNA core atoms. To define the orientation of the body, axes were constructed based on the aligned orientations of residues 41, 127, and 911, which are used to define the plane of rotation. The Euler angles are then calculated based on the orientational difference of the fitted axes in the reference classical configuration and the structural model of interest. To describe the orientation of the head, the 16S body was first aligned to the reference model (alignment based on core atoms) and axes were defined based on residue 984, 940 and 1106. According to these definitions, models (4V9D:DA, 4V9D:BA) and (4V9D:CA, 4V9D:AA) define pure (tilt-free) body rotation, and models (4V9D:DA, 4V9D:BA) and (4V4Q:DB, 4V4Q:CA) define pure (tilt-free) head swivel. The classical model (4V9D:DA, 4V9D:BA) is defined as the zero-tilt, zero-rotation orientation.
